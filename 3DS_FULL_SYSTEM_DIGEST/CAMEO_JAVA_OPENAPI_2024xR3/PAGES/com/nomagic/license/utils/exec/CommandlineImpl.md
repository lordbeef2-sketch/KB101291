# JAVA OPENAPI: CommandlineImpl (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/license/utils/exec/CommandlineImpl.html
- source_path: `com/nomagic/license/utils/exec/CommandlineImpl.html`
- source_sha256: `a4dd49508d35e7fa0e946f212605492d71356d6d195a189fc9408f918ebc9974`
- captured_utc: `2026-07-14T16:55:02.560864+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.license.utils.exec](package-summary.html)

## Class CommandlineImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.license.utils.exec.CommandlineImpl

All Implemented Interfaces:
`[Commandline](Commandline.html)`

@OpenApiAllpublic classCommandlineImpl
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Commandline](Commandline.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.license.utils.exec.[Commandline](Commandline.html)
`[DEFAULT_TIMEOUT](Commandline.html#DEFAULT_TIMEOUT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CommandlineImpl](#%3Cinit%3E())()`

`[CommandlineImpl](#%3Cinit%3E(boolean))(boolean logEnabled)`

`[CommandlineImpl](#%3Cinit%3E(long))(long timeout)`

`[CommandlineImpl](#%3Cinit%3E(long,boolean))(long timeout,
 boolean logEnabled)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
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
`protected void`
`[log](#log(java.lang.String%5B%5D,java.lang.String%5B%5D,java.io.File))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)`

`protected void`
`[log](#log(java.lang.String,java.lang.String%5B%5D,java.io.File))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)`

`protected [ProcessOutput](ProcessOutput.html)`
`[read](#read(java.lang.Process))([Process](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Process.html) process)`

`void`
`[setLogEnabled](#setLogEnabled(boolean))(boolean logEnabled)`

`void`
`[setTimeout](#setTimeout(long))(long timeout)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CommandlineImpl
public CommandlineImpl()
CommandlineImpl
public CommandlineImpl(long timeout)
CommandlineImpl
public CommandlineImpl(boolean logEnabled)
CommandlineImpl
public CommandlineImpl(long timeout,
 boolean logEnabled)
 ============ METHOD DETAIL ========== 
Method Details
read
protected [ProcessOutput](ProcessOutput.html) read([Process](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Process.html) process)
 throws [InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html),
[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Throws:
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
log
public void log([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Description copied from interface: `[Commandline](Commandline.html#log(java.lang.String))`
Print some log information.
Specified by:
`[log](Commandline.html#log(java.lang.String))` in interface `[Commandline](Commandline.html)`
log
protected void log([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 @CheckForNull
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
log
protected void log([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 @CheckForNull
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
execute
public [ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 @CheckForNull
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Specified by:
`[execute](Commandline.html#execute(java.lang.String,java.lang.String%5B%5D,java.io.File))` in interface `[Commandline](Commandline.html)`
Parameters:
`dir` - file working directory
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
public [ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Specified by:
`[execute](Commandline.html#execute(java.lang.String,java.lang.String%5B%5D))` in interface `[Commandline](Commandline.html)`
Parameters:
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
public [ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Specified by:
`[execute](Commandline.html#execute(java.lang.String,java.io.File))` in interface `[Commandline](Commandline.html)`
Parameters:
`dir` - file working directory
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
public [ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Specified by:
`[execute](Commandline.html#execute(java.lang.String))` in interface `[Commandline](Commandline.html)`
Parameters:
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
public [ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment,
 @CheckForNull
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Specified by:
`[execute](Commandline.html#execute(java.lang.String%5B%5D,java.lang.String%5B%5D,java.io.File))` in interface `[Commandline](Commandline.html)`
Parameters:
`dir` - file working directory
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
public [ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] environment)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Specified by:
`[execute](Commandline.html#execute(java.lang.String%5B%5D,java.lang.String%5B%5D))` in interface `[Commandline](Commandline.html)`
Parameters:
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
public [ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Specified by:
`[execute](Commandline.html#execute(java.lang.String%5B%5D,java.io.File))` in interface `[Commandline](Commandline.html)`
Parameters:
`dir` - file working directory
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
execute
public [ProcessOutput](ProcessOutput.html) execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] cmd)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html),
[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)
Execute command line
Specified by:
`[execute](Commandline.html#execute(java.lang.String%5B%5D))` in interface `[Commandline](Commandline.html)`
Parameters:
`cmd` - command line
Returns:
output of command
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
`[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html)`
getTimeout
public long getTimeout()
Specified by:
`[getTimeout](Commandline.html#getTimeout())` in interface `[Commandline](Commandline.html)`
Returns:
setTimeout
public void setTimeout(long timeout)
Specified by:
`[setTimeout](Commandline.html#setTimeout(long))` in interface `[Commandline](Commandline.html)`
isLogEnabled
public boolean isLogEnabled()
Specified by:
`[isLogEnabled](Commandline.html#isLogEnabled())` in interface `[Commandline](Commandline.html)`
Returns:
setLogEnabled
public void setLogEnabled(boolean logEnabled)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.license.utils.exec</a></div>
<h1 class="title" title="Class CommandlineImpl">Class CommandlineImpl</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.license.utils.exec.CommandlineImpl</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CommandlineImpl</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.license.utils.exec.Commandline">Fields inherited from interface com.nomagic.license.utils.exec.<a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></h3>
<code><a href="Commandline.html#DEFAULT_TIMEOUT">DEFAULT_TIMEOUT</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CommandlineImpl</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean)">CommandlineImpl</a><wbr/>(boolean logEnabled)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(long)">CommandlineImpl</a><wbr/>(long timeout)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(long,boolean)">CommandlineImpl</a><wbr/>(long timeout,
 boolean logEnabled)</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute command line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute command line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D,java.io.File)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute command line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D,java.lang.String%5B%5D)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute command line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D,java.lang.String%5B%5D,java.io.File)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute command line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String,java.io.File)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute command line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String,java.lang.String%5B%5D)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute command line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String,java.lang.String%5B%5D,java.io.File)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute command line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTimeout()">getTimeout</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLogEnabled()">isLogEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#log(java.lang.String)">log</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Print some log information.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#log(java.lang.String%5B%5D,java.lang.String%5B%5D,java.io.File)">log</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#log(java.lang.String,java.lang.String%5B%5D,java.io.File)">log</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#read(java.lang.Process)">read</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Process.html" title="class or interface in java.lang">Process</a> process)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLogEnabled(boolean)">setLogEnabled</a><wbr/>(boolean logEnabled)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTimeout(long)">setTimeout</a><wbr/>(long timeout)</code></div>
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
<h3>CommandlineImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CommandlineImpl</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(long)">
<h3>CommandlineImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CommandlineImpl</span><wbr/><span class="parameters">(long timeout)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean)">
<h3>CommandlineImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CommandlineImpl</span><wbr/><span class="parameters">(boolean logEnabled)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(long,boolean)">
<h3>CommandlineImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CommandlineImpl</span><wbr/><span class="parameters">(long timeout,
 boolean logEnabled)</span></div>
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
<section class="detail" id="read(java.lang.Process)">
<h3>read</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">read</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Process.html" title="class or interface in java.lang">Process</a> process)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="log(java.lang.String)">
<h3>log</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">log</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="Commandline.html#log(java.lang.String)">Commandline</a></code></span></div>
<div class="block">Print some log information.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#log(java.lang.String)">log</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="log(java.lang.String,java.lang.String[],java.io.File)">
<h3>log</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">log</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span></div>
</section>
</li>
<li>
<section class="detail" id="log(java.lang.String[],java.lang.String[],java.io.File)">
<h3>log</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">log</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span></div>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String,java.lang.String[],java.io.File)">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#execute(java.lang.String,java.lang.String%5B%5D,java.io.File)">execute</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#execute(java.lang.String,java.lang.String%5B%5D)">execute</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#execute(java.lang.String,java.io.File)">execute</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#execute(java.lang.String)">execute</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#execute(java.lang.String%5B%5D,java.lang.String%5B%5D,java.io.File)">execute</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] environment)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#execute(java.lang.String%5B%5D,java.lang.String%5B%5D)">execute</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dir)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#execute(java.lang.String%5B%5D,java.io.File)">execute</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProcessOutput.html" title="class in com.nomagic.license.utils.exec">ProcessOutput</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] cmd)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html" title="class or interface in java.lang">InterruptedException</a></span></div>
<div class="block">Execute command line</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#execute(java.lang.String%5B%5D)">execute</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getTimeout</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#getTimeout()">getTimeout</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTimeout(long)">
<h3>setTimeout</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTimeout</span><wbr/><span class="parameters">(long timeout)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#setTimeout(long)">setTimeout</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLogEnabled()">
<h3>isLogEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLogEnabled</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Commandline.html#isLogEnabled()">isLogEnabled</a></code> in interface <code><a href="Commandline.html" title="interface in com.nomagic.license.utils.exec">Commandline</a></code></dd>
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLogEnabled(boolean)">
<h3>setLogEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLogEnabled</span><wbr/><span class="parameters">(boolean logEnabled)</span></div>
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
