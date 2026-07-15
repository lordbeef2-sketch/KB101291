# JAVA OPENAPI: ProjectCommandLineAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/commandline/ProjectCommandLineAction.html
- source_path: `com/nomagic/magicdraw/commandline/ProjectCommandLineAction.html`
- source_sha256: `bad1c5f6c8b8eb4332044b8ede500c2407c15cd5e7d8dcc585842c97327a6086`
- captured_utc: `2026-07-14T16:51:13.436100+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.commandline](package-summary.html)

## Class ProjectCommandLineAction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.commandline.ProjectCommandLineAction

All Implemented Interfaces:
`[CommandLineAction](CommandLineAction.html)`

@OpenApiAllpublic abstract classProjectCommandLineAction
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [CommandLineAction](CommandLineAction.html)

This class contains general methods (open, close project, read command line properties, connect to server, etc)
 related to project in command line for plugins
 Override [`execute(String[], Properties, Project)`](#execute(java.lang.String%5B%5D,java.util.Properties,com.nomagic.magicdraw.core.Project))
 

 Arguments are specified as name=value pairs. 

 Default arguments that will be used to try and open project:
 project - Project name or path
projectDescriptor - Project descriptor
server - Server url
username - Username on server
password - Password for provided username
enableSSL - To use ssl
serverType - Should be any value of `ServerType`, if not specified `ServerType.TEAMWORK_CLOUD` will be used
encryptPassword - Set true if provided password is in plain text
properties - Path to properties file containing properties. Multiple properties files can be provided "properties=prop1.properties;prop2.properties"
projectPassword - Project password
version - Project version
branch - Project branch
useDefaultPropertyValidation - set false to disable validation of default properties

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectCommandLineAction](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`final byte`
`[execute](#execute(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)`
Implement this method to execute custom task in running MagicDraw application environment.
`protected abstract byte`
`[execute](#execute(java.lang.String%5B%5D,java.util.Properties,com.nomagic.magicdraw.core.Project))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args,
 [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html) properties,
 [Project](../core/Project.html) project)`
Override this method to execute your custom task(s) in running MagicDraw environment on opened project.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectCommandLineAction
public ProjectCommandLineAction()
 ============ METHOD DETAIL ========== 
Method Details
execute
public final byte execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)
Description copied from interface: `[CommandLineAction](CommandLineAction.html#execute(java.lang.String%5B%5D))`
Implement this method to execute custom task in running MagicDraw application environment.
Specified by:
`[execute](CommandLineAction.html#execute(java.lang.String%5B%5D))` in interface `[CommandLineAction](CommandLineAction.html)`
Returns:
application exit status.
execute
protected abstract byte execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args,
 [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html) properties,
 [Project](../core/Project.html) project)
Override this method to execute your custom task(s) in running MagicDraw environment on opened project.
Parameters:
`args` - arguments environment was started with
`properties` - parsed arguments for this project
`project` - project opened based on provided arguments
Returns:
application exit status (default is 0).

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.commandline</a></div>
<h1 class="title" title="Class ProjectCommandLineAction">Class ProjectCommandLineAction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.commandline.ProjectCommandLineAction</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="CommandLineAction.html" title="interface in com.nomagic.magicdraw.commandline">CommandLineAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ProjectCommandLineAction</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="CommandLineAction.html" title="interface in com.nomagic.magicdraw.commandline">CommandLineAction</a></span></div>
<div class="block">This class contains general methods (open, close project, read command line properties, connect to server, etc)
 related to project in command line for plugins
 Override <a href="#execute(java.lang.String%5B%5D,java.util.Properties,com.nomagic.magicdraw.core.Project)"><code>execute(String[], Properties, Project)</code></a>
<br/>
 Arguments are specified as name=value pairs.<br/>
 Default arguments that will be used to try and open project:
 <ul>
<li>project - Project name or path</li>
<li>projectDescriptor - Project descriptor</li>
<li>server - Server url</li>
<li>username - Username on server</li>
<li>password - Password for provided username</li>
<li>enableSSL - To use ssl</li>
<li>serverType - Should be any value of <code>ServerType</code>, if not specified <code>ServerType.TEAMWORK_CLOUD</code> will be used</li>
<li>encryptPassword - Set true if provided password is in plain text</li>
<li>properties - Path to properties file containing properties. Multiple properties files can be provided "properties=prop1.properties;prop2.properties"</li>
<li>projectPassword - Project password</li>
<li>version - Project version</li>
<li>branch - Project branch</li>
<li>useDefaultPropertyValidation - set false to disable validation of default properties</li>
</ul></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectCommandLineAction</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final byte</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Implement this method to execute custom task in running MagicDraw application environment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract byte</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(java.lang.String%5B%5D,java.util.Properties,com.nomagic.magicdraw.core.Project)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Override this method to execute your custom task(s) in running MagicDraw environment on opened project.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ProjectCommandLineAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectCommandLineAction</span>()</div>
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
<section class="detail" id="execute(java.lang.String[])">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">byte</span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="CommandLineAction.html#execute(java.lang.String%5B%5D)">CommandLineAction</a></code></span></div>
<div class="block">Implement this method to execute custom task in running MagicDraw application environment.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="CommandLineAction.html#execute(java.lang.String%5B%5D)">execute</a></code> in interface <code><a href="CommandLineAction.html" title="interface in com.nomagic.magicdraw.commandline">CommandLineAction</a></code></dd>
<dt>Returns:</dt>
<dd>application exit status.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String[],java.util.Properties,com.nomagic.magicdraw.core.Project)">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">byte</span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Override this method to execute your custom task(s) in running MagicDraw environment on opened project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>args</code> - arguments environment was started with</dd>
<dd><code>properties</code> - parsed arguments for this project</dd>
<dd><code>project</code> - project opened based on provided arguments</dd>
<dt>Returns:</dt>
<dd>application exit status (default is 0).</dd>
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
