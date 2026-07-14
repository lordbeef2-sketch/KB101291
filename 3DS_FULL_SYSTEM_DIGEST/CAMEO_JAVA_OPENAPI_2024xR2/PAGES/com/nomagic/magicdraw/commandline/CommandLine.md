# JAVA OPENAPI: CommandLine (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/commandline/CommandLine.html
- source_path: `com/nomagic/magicdraw/commandline/CommandLine.html`
- source_sha256: `26d09eb64b76a4bb9aafd578df63edd96900fb09cef7a319ea0cb54552a785e1`
- captured_utc: `2026-07-14T16:55:10.967960+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.commandline](package-summary.html)

## Class CommandLine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.commandline.CommandLine

Direct Known Subclasses:
`[ProjectCommandLine](ProjectCommandLine.html)`

@OpenApiAllpublic abstract classCommandLine
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

MagicDraw commandline launcher. 

 Extend it and implement [`execute()`](#execute()) method.
 *Code sample:*
public class TestCommandLine extends CommandLine
 {
 public static void main(String[] args)
 {
 new TestCommandLine().launch(args);
 }

 protected void execute()
 {
 // load project
 File fileToLoad = new File("myProject.mdzip");
 ProjectDescriptor descriptor = ProjectDescriptorsFactory.createProjectDescriptor(fileToLoad.toURI());
 ProjectsManager projectsManager = Application.getInstance().getProjectsManager();
 projectsManager.loadProject(descriptor, true);

 Project project = Application.getInstance().getProject();

 // "save as" project
 File fileToSave = new File("myProject2.mdzip");
 ProjectDescriptor localProjectDescriptor = ProjectDescriptorsFactory.createLocalProjectDescriptor(project, fileToSave);
 projectsManager.saveProject(localProjectDescriptor, true);
 }
 }

 Check documentation ("Running programs in batch mode") on how to start command line.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CommandLine](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected abstract byte`
`[execute](#execute())()`
Override this method to execute your custom task(s) in running MagicDraw environment.
`final void`
`[launch](#launch(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)`
Launch MagicDraw in commandline mode (without GUI). 

 Method starts MagicDraw application, calls [`execute()`](#execute()) method, and shuts down the application.
`protected void`
`[parseArgs](#parseArgs(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)`
Override to parse arguments before launching MagicDraw.
`protected static void`
`[printToCommandLineConsole](#printToCommandLineConsole(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Print to commandline console.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CommandLine
public CommandLine()
 ============ METHOD DETAIL ========== 
Method Details
launch
public final void launch([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)
 throws [InstantiationException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InstantiationException.html)
Launch MagicDraw in commandline mode (without GUI). 

 Method starts MagicDraw application, calls [`execute()`](#execute()) method, and shuts down the application.
Parameters:
`args` - command line arguments passed to MagicDraw.
Throws:
`[InstantiationException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InstantiationException.html)` - if the failed return code needs to be indicated
parseArgs
protected void parseArgs([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Override to parse arguments before launching MagicDraw.
Parameters:
`args` - program arguments
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - if arguments are not correct and MagicDraw should not be started
printToCommandLineConsole
protected static void printToCommandLineConsole([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Print to commandline console. Do not use `System.out` since it might be redirected to log.
Parameters:
`text` - test to print
execute
protected abstract byte execute()
Override this method to execute your custom task(s) in running MagicDraw environment.
 Do not explicitly call this method - call [`launch(String[])`](#launch(java.lang.String%5B%5D)) to launch the commandline.
Returns:
application exit status

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.commandline</a></div>
<h1 class="title" title="Class CommandLine">Class CommandLine</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.commandline.CommandLine</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ProjectCommandLine.html" title="class in com.nomagic.magicdraw.commandline">ProjectCommandLine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">CommandLine</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">MagicDraw commandline launcher.<br/>
 Extend it and implement <a href="#execute()"><code>execute()</code></a> method.
 <p>
<p></p><em>Code sample:</em>
<pre>public class TestCommandLine extends CommandLine
 {
        public static void main(String[] args)
     {
                new TestCommandLine().launch(args);
     }

        protected void execute()
     {
                // load project
                File fileToLoad = new File("myProject.mdzip");
                ProjectDescriptor descriptor = ProjectDescriptorsFactory.createProjectDescriptor(fileToLoad.toURI());
                ProjectsManager projectsManager = Application.getInstance().getProjectsManager();
                projectsManager.loadProject(descriptor, true);

                Project project = Application.getInstance().getProject();

                // "save as" project
                File fileToSave = new File("myProject2.mdzip");
                ProjectDescriptor localProjectDescriptor = ProjectDescriptorsFactory.createLocalProjectDescriptor(project, fileToSave);
                projectsManager.saveProject(localProjectDescriptor, true);
     }
 }</pre>
<p></p>
 Check documentation ("Running programs in batch mode") on how to start command line.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CommandLine</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract byte</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute()">execute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Override this method to execute your custom task(s) in running MagicDraw environment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#launch(java.lang.String%5B%5D)">launch</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Launch MagicDraw in commandline mode (without GUI).<br/>
 Method starts MagicDraw application, calls <a href="#execute()"><code>execute()</code></a> method, and shuts down the application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#parseArgs(java.lang.String%5B%5D)">parseArgs</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Override to parse arguments before launching MagicDraw.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#printToCommandLineConsole(java.lang.String)">printToCommandLineConsole</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Print to commandline console.</div>
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
<h3>CommandLine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CommandLine</span>()</div>
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
<section class="detail" id="launch(java.lang.String[])">
<h3>launch</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">launch</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InstantiationException.html" title="class or interface in java.lang">InstantiationException</a></span></div>
<div class="block">Launch MagicDraw in commandline mode (without GUI).<br/>
 Method starts MagicDraw application, calls <a href="#execute()"><code>execute()</code></a> method, and shuts down the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>args</code> - command line arguments passed to MagicDraw.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InstantiationException.html" title="class or interface in java.lang">InstantiationException</a></code> - if the failed return code needs to be indicated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parseArgs(java.lang.String[])">
<h3>parseArgs</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">parseArgs</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Override to parse arguments before launching MagicDraw.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>args</code> - program arguments</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if arguments are not correct and MagicDraw should not be started</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="printToCommandLineConsole(java.lang.String)">
<h3>printToCommandLineConsole</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">void</span> <span class="element-name">printToCommandLineConsole</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Print to commandline console. Do not use <code>System.out</code> since it might be redirected to log.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - test to print</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute()">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">byte</span> <span class="element-name">execute</span>()</div>
<div class="block">Override this method to execute your custom task(s) in running MagicDraw environment.
 Do not explicitly call this method - call <a href="#launch(java.lang.String%5B%5D)"><code>launch(String[])</code></a> to launch the commandline.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application exit status</dd>
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
