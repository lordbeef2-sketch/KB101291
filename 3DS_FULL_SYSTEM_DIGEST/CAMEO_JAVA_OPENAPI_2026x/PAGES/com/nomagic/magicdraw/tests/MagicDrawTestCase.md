# JAVA OPENAPI: MagicDrawTestCase (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/tests/MagicDrawTestCase.html
- source_path: `com/nomagic/magicdraw/tests/MagicDrawTestCase.html`
- source_sha256: `606aa2c80a9a8903599fa92e396014de91365e47e56de34a25a620d6bc6afc70`
- captured_utc: `2026-07-14T16:58:10.703677+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests](package-summary.html)

## Class MagicDrawTestCase

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
junit.framework.Assert
junit.framework.TestCase
com.nomagic.magicdraw.tests.NamedTestCase
com.nomagic.magicdraw.tests.MagicDrawTestCase

All Implemented Interfaces:
`junit.framework.Test`

@OpenApipublic abstract classMagicDrawTestCase
extends com.nomagic.magicdraw.tests.NamedTestCase

Base class for JUnit3 Test Cases which should be run with MagicDraw Application started.
 Starts new MagicDraw application before each test. Provides methods for opening, saving, closing, and comparing projects.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MagicDrawTestCase](#%3Cinit%3E())()`
Default test case initialization for executing test* methods.
`[MagicDrawTestCase](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method)`
Creates MagicDrawTestCase for executing specific test method.
`[MagicDrawTestCase](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) testName)`
Creates MagicDrawTestCase of specific name for executing specific test method.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected void`
`[checkMemoryLeaks](#checkMemoryLeaks())()`
Force memory leaks test execution.
`void`
`[closeAllProjects](#closeAllProjects())()`
Close all currently opened MagicDraw projects with performing memory leaks test.
`void`
`[closeProject](#closeProject(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Close opened MagicDraw project.
`protected [ProjectsComparator](common/comparators/ProjectsComparator.html)`
`[createProjectComparator](#createProjectComparator(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) logText)`
Creates project comparator with default model and diagram comparators implementation.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getFileWithExtension](#getFileWithExtension(java.io.File,java.lang.String))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) projectFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)`
Computes test case specific properties file according given project file.
`protected org.apache.log4j.Logger`
`[getLogger](#getLogger())()`
Gets logger for Test related output logging.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getPropertiesFile](#getPropertiesFile(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) projectFile)`
Computes test case specific properties file according given project file.
`protected [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getRequiredPlugins](#getRequiredPlugins())()`
Is used to specify plug-ins required by test case.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRequiredPluginsDescription](#getRequiredPluginsDescription())()`
Formats textual message about available plug-ins status(loaded/enabled).
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getXmlFile](#getXmlFile(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) projectFile)`
Computes test case specific properties file according given project file.
`static void`
`[invokeAndWaitOnDispatcher](#invokeAndWaitOnDispatcher(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r)`
Executes runnable on dispatcher thread and waits till runnable is done.
`final boolean`
`[isDoNotUseSilentMode](#isDoNotUseSilentMode())()`
Check if silent mode is not used for starting MagicDraw.
`boolean`
`[isFailed](#isFailed())()`
Check if test has failed because of JUnit assertion or any other exception.
`protected final boolean`
`[isMemoryTestReady](#isMemoryTestReady())()`
Check if memory leaks test might be performed.
`protected boolean`
`[isRequiredPluginsLoaded](#isRequiredPluginsLoaded())()`
Check if all plug-ins required by this test case are loaded and enabled.
`static [Project](../core/Project.html)`
`[loadProject](#loadProject(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) file)`
Opens MagicDraw project by absolute project file name.
`static [Project](../core/Project.html)`
`[loadProject](#loadProject(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) projectPath,
 boolean failIfProjectHasErrors)`
Opens MagicDraw project by absolute project file name.
`static [Project](../core/Project.html)`
`[loadProject](#loadProject(java.lang.String,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) projectPath,
 boolean failIfProjectHasErrors,
 boolean loadAllDiagrams)`
Opens MagicDraw project by absolute project file name.
`protected [Project](../core/Project.html)`
`[openProject](#openProject(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) projectFile)`
Opens MagicDraw project by its absolute file name.
`protected [Project](../core/Project.html)`
`[openProject](#openProject(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) projectFile,
 boolean loadAllDiagram)`
Opens MagicDraw project by its absolute file name.
`protected void`
`[saveProject](#saveProject(com.nomagic.magicdraw.core.Project,java.io.File))([Project](../core/Project.html) project,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Save opened MagicDraw project to specific file.
`final void`
`[setDoNotUseSilentMode](#setDoNotUseSilentMode(boolean))(boolean doNotUseSilentMode)`
Specify if MagicDraw should show GUI modal dialogs during startup and features testing.
`final void`
`[setMemoryTestReady](#setMemoryTestReady(boolean))(boolean memoryTestReady)`
Specify if memory leaks test is ready, so it might be performed at the end of the test.
`final void`
`[setRunOnEventDispatcher](#setRunOnEventDispatcher(boolean))(boolean runOnEventDispatcher)`
Sets if test case should be executed on event dispatching thread.
`final void`
`[setRunOnEventDispather](#setRunOnEventDispather(boolean))(boolean runOnEventDispatcher)`
Deprecated.
spelling error in name, use set #setRunOnEventDispatcher
`final void`
`[setSkipMemoryTest](#setSkipMemoryTest(boolean))(boolean skipMemoryTest)`
Set to true in order to skip memory leaks test.
`protected void`
`[setUpTest](#setUpTest())()`
Override to prepare test case after MagicDraw application started.
`protected void`
`[tearDownTest](#tearDownTest())()`
Tear down test case after it execution.
Methods inherited from class com.nomagic.magicdraw.tests.NamedTestCase
`getFullTestName, getMethodName, getTestName, getTestNamePrefix, isOverridingTestName, setMethodName, setTestName`
Methods inherited from class junit.framework.TestCase
`assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertFalse, assertFalse, assertNotNull, assertNotNull, assertNotSame, assertNotSame, assertNull, assertNull, assertSame, assertSame, assertTrue, assertTrue, countTestCases, createResult, fail, fail, failNotEquals, failNotSame, failSame, format, getName, run, runBare, setName, toString`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MagicDrawTestCase
@OpenApipublic MagicDrawTestCase()
Default test case initialization for executing test* methods.
MagicDrawTestCase
@OpenApipublic MagicDrawTestCase([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method)
Creates MagicDrawTestCase for executing specific test method.
Parameters:
`method` - test method name to execute.
MagicDrawTestCase
@OpenApipublic MagicDrawTestCase([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) testName)
Creates MagicDrawTestCase of specific name for executing specific test method.
Parameters:
`method` - test method name to execute.
`testName` - name of created test. All none alpha numerical characters in name will be replaced by underscore character.
 ============ METHOD DETAIL ========== 
Method Details
setMemoryTestReady
@OpenApipublic final void setMemoryTestReady(boolean memoryTestReady)
Specify if memory leaks test is ready, so it might be performed at the end of the test.
 Set it false if you need to disable memory leaks test performing at the end of the test.
Parameters:
`memoryTestReady` - true if memory test is ready
setSkipMemoryTest
@OpenApipublic final void setSkipMemoryTest(boolean skipMemoryTest)
Set to true in order to skip memory leaks test.
 Memory leaks test is always performed by default after MagicDraw project is closed
 and after each completed test.
Parameters:
`skipMemoryTest` - true if memory test should be skipped, false otherwise.
setRunOnEventDispather
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public final void setRunOnEventDispather(boolean runOnEventDispatcher)
Deprecated.
spelling error in name, use set #setRunOnEventDispatcher
Sets if test case should be executed on event dispatching thread.
 MagicDrawTestCase is run on event dispatcher thread by default.
Parameters:
`runOnEventDispatcher` - True if test case should be executed on event dispatching thread.
setRunOnEventDispatcher
@OpenApipublic final void setRunOnEventDispatcher(boolean runOnEventDispatcher)
Sets if test case should be executed on event dispatching thread.
 MagicDrawTestCase is run on event dispatcher thread by default.
Parameters:
`runOnEventDispatcher` - True if test case should be executed on event dispatching thread.
setDoNotUseSilentMode
@OpenApipublic final void setDoNotUseSilentMode(boolean doNotUseSilentMode)
Specify if MagicDraw should show GUI modal dialogs during startup and features testing.
 MagicDraw is started up in silent mode by default.
Parameters:
`doNotUseSilentMode` - provide true value if GUI dialogs need to be shown during MagicDraw testing.
isDoNotUseSilentMode
@OpenApipublic final boolean isDoNotUseSilentMode()
Check if silent mode is not used for starting MagicDraw. Silent mode prevents
 confirmation dialogs pop-up during MagicDraw test.
 MagicDraw is started up in silent mode by default.
Returns:
True if MagicDraw is started in Not silent mode.
isMemoryTestReady
@OpenApiprotected final boolean isMemoryTestReady()
Check if memory leaks test might be performed.
Returns:
True if memory leaks test is ready and might be performed, false otherwise.
getRequiredPlugins
@OpenApiprotected [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getRequiredPlugins()
Is used to specify plug-ins required by test case. Should be overridden in specific MagicDrawTestCase implementation.
 Default implementation returns empty List.
Returns:
List of plug-in IDs required by this test case.
getRequiredPluginsDescription
@OpenApiprotected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRequiredPluginsDescription()
Formats textual message about available plug-ins status(loaded/enabled).
Returns:
String message about required plug-ins status.
isRequiredPluginsLoaded
@OpenApiprotected boolean isRequiredPluginsLoaded()
Check if all plug-ins required by this test case are loaded and enabled.
Returns:
True if all required plug-ins are loaded and enabled, false otherwise.
setUpTest
@OpenApiprotected void setUpTest()
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Override to prepare test case after MagicDraw application started.
 Test set up should be done here. Do not use default JUnit setUp() instead.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - from default JUnit setUp()
tearDownTest
@OpenApiprotected void tearDownTest()
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Tear down test case after it execution.
 This method is called after test method execution completed but MagicDraw Application not closed yet.
 Test tear down should be done here. Do not use default JUnit tearDown() instead.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - from default JUnit tearDown()
closeProject
@OpenApipublic void closeProject([Project](../core/Project.html) project)
Close opened MagicDraw project. Performs memory leaks test after project is closed,
 so all references to the elements of the closed project should be disposed before method execution.
Parameters:
`project` - MagicDraw Project to close.
closeAllProjects
@OpenApipublic void closeAllProjects()
Close all currently opened MagicDraw projects with performing memory leaks test.
 All references to the elements of the closed projects should be disposed before method execution.
checkMemoryLeaks
@OpenApiprotected void checkMemoryLeaks()
Force memory leaks test execution.
invokeAndWaitOnDispatcher
@OpenApipublic static void invokeAndWaitOnDispatcher([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) r)
Executes runnable on dispatcher thread and waits till runnable is done.
Parameters:
`r` - Runnable to execute.
getPropertiesFile
@OpenApipublic static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getPropertiesFile([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) projectFile)
Computes test case specific properties file according given project file.
 MagicDraw Project properties file pattern "project_name.properties".
Parameters:
`projectFile` - project file
Returns:
test case properties file
getXmlFile
@OpenApipublic static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getXmlFile([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) projectFile)
Computes test case specific properties file according given project file.
 MagicDraw Project properties file pattern "project_name.xml".
Parameters:
`projectFile` - project file
Returns:
test case properties file
getFileWithExtension
@OpenApipublic static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getFileWithExtension([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) projectFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)
Computes test case specific properties file according given project file.
 MagicDraw Project properties file pattern "project_name.[extension]".
Parameters:
`projectFile` - project file
Returns:
test case properties file
loadProject
@OpenApipublic static [Project](../core/Project.html) loadProject([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) file)
Opens MagicDraw project by absolute project file name.
Parameters:
`file` - absolute file name of project to open.
Returns:
Opened project.
loadProject
@OpenApipublic static [Project](../core/Project.html) loadProject([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) projectPath,
 boolean failIfProjectHasErrors)
Opens MagicDraw project by absolute project file name.
Parameters:
`projectPath` - absolute file name of project to open.
`failIfProjectHasErrors` - Specifies if test should fail if loaded project has any model inconsistency errors. Recommended to run with silentMode turned on.
Returns:
Opened project.
loadProject
@OpenApipublic static [Project](../core/Project.html) loadProject([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) projectPath,
 boolean failIfProjectHasErrors,
 boolean loadAllDiagrams)
Opens MagicDraw project by absolute project file name.
Parameters:
`projectPath` - absolute file name of project to open.
`failIfProjectHasErrors` - Specifies if test should fail if loaded project has any model inconsistency errors. Recommended to run with silentMode turned on.
Returns:
Opened project.
getLogger
@OpenApiprotected org.apache.log4j.Logger getLogger()
Gets logger for Test related output logging.
Returns:
log4j Logger for TEST category.
See Also:
`Logger`
isFailed
@OpenApipublic boolean isFailed()
Check if test has failed because of JUnit assertion or any other exception.
Returns:
True if this test has failed, false otherwise.
createProjectComparator
@OpenApiprotected [ProjectsComparator](common/comparators/ProjectsComparator.html) createProjectComparator(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) logText)
Creates project comparator with default model and diagram comparators implementation.
 Comparator does not compare projects regarding their modules, author information, and diagram info data.
Parameters:
`logText` - information message which should be printed to log at the beginning of comparison.
Returns:
new instance of ProjectsComparator with model and diagrams comparators initialized.
openProject
@OpenApiprotected [Project](../core/Project.html) openProject([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) projectFile)
Opens MagicDraw project by its absolute file name.
 It reopens the project if project is already opened.
Parameters:
`projectFile` - absolute file name of project to open.
Returns:
opened project or null if project cannot be opened.
openProject
@OpenApiprotected [Project](../core/Project.html) openProject([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) projectFile,
 boolean loadAllDiagram)
Opens MagicDraw project by its absolute file name.
 It reopens the project if project is already opened.
Parameters:
`projectFile` - absolute file name of project to open.
`loadAllDiagram` - load content of all diagrams in the opened project
Returns:
opened project or null if project cannot be opened.
saveProject
@OpenApiprotected void saveProject([Project](../core/Project.html) project,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
Save opened MagicDraw project to specific file. S
 Save is done ins silent mode without any GUI confirmation messages.
Parameters:
`project` - MagicDraw opened project to save.
`file` - File to save project.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests</a></div>
<h1 class="title" title="Class MagicDrawTestCase">Class MagicDrawTestCase</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">junit.framework.Assert
<div class="inheritance">junit.framework.TestCase
<div class="inheritance">com.nomagic.magicdraw.tests.NamedTestCase
<div class="inheritance">com.nomagic.magicdraw.tests.MagicDrawTestCase</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>junit.framework.Test</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">MagicDrawTestCase</span>
<span class="extends-implements">extends com.nomagic.magicdraw.tests.NamedTestCase</span></div>
<div class="block">Base class for JUnit3 Test Cases which should be run with MagicDraw Application started.
 Starts new MagicDraw application before each test. Provides methods for opening, saving, closing, and comparing projects.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MagicDrawTestCase</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default test case initialization for executing test* methods.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">MagicDrawTestCase</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates MagicDrawTestCase for executing specific test method.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">MagicDrawTestCase</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> testName)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates MagicDrawTestCase of specific name for executing specific test method.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkMemoryLeaks()">checkMemoryLeaks</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Force memory leaks test execution.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeAllProjects()">closeAllProjects</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Close all currently opened MagicDraw projects with performing memory leaks test.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeProject(com.nomagic.magicdraw.core.Project)">closeProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Close opened MagicDraw project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="common/comparators/ProjectsComparator.html" title="class in com.nomagic.magicdraw.tests.common.comparators">ProjectsComparator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProjectComparator(java.lang.String)">createProjectComparator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> logText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates project comparator with default model and diagram comparators implementation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileWithExtension(java.io.File,java.lang.String)">getFileWithExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> projectFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Computes test case specific properties file according given project file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected org.apache.log4j.Logger</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLogger()">getLogger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets logger for Test related output logging.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertiesFile(java.io.File)">getPropertiesFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> projectFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Computes test case specific properties file according given project file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredPlugins()">getRequiredPlugins</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Is used to specify plug-ins required by test case.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredPluginsDescription()">getRequiredPluginsDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Formats textual message about available plug-ins status(loaded/enabled).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getXmlFile(java.io.File)">getXmlFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> projectFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Computes test case specific properties file according given project file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeAndWaitOnDispatcher(java.lang.Runnable)">invokeAndWaitOnDispatcher</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes runnable on dispatcher thread and waits till runnable is done.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDoNotUseSilentMode()">isDoNotUseSilentMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if silent mode is not used for starting MagicDraw.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFailed()">isFailed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if test has failed because of JUnit assertion or any other exception.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMemoryTestReady()">isMemoryTestReady</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if memory leaks test might be performed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRequiredPluginsLoaded()">isRequiredPluginsLoaded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if all plug-ins required by this test case are loaded and enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadProject(java.lang.String)">loadProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Opens MagicDraw project by absolute project file name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadProject(java.lang.String,boolean)">loadProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectPath,
 boolean failIfProjectHasErrors)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Opens MagicDraw project by absolute project file name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadProject(java.lang.String,boolean,boolean)">loadProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectPath,
 boolean failIfProjectHasErrors,
 boolean loadAllDiagrams)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Opens MagicDraw project by absolute project file name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openProject(java.lang.String)">openProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens MagicDraw project by its absolute file name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openProject(java.lang.String,boolean)">openProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectFile,
 boolean loadAllDiagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens MagicDraw project by its absolute file name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveProject(com.nomagic.magicdraw.core.Project,java.io.File)">saveProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Save opened MagicDraw project to specific file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDoNotUseSilentMode(boolean)">setDoNotUseSilentMode</a><wbr/>(boolean doNotUseSilentMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Specify if MagicDraw should show GUI modal dialogs during startup and features testing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMemoryTestReady(boolean)">setMemoryTestReady</a><wbr/>(boolean memoryTestReady)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Specify if memory leaks test is ready, so it might be performed at the end of the test.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRunOnEventDispatcher(boolean)">setRunOnEventDispatcher</a><wbr/>(boolean runOnEventDispatcher)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets if test case should be executed on event dispatching thread.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setRunOnEventDispather(boolean)">setRunOnEventDispather</a><wbr/>(boolean runOnEventDispatcher)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">spelling error in name, use set #setRunOnEventDispatcher</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSkipMemoryTest(boolean)">setSkipMemoryTest</a><wbr/>(boolean skipMemoryTest)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set to true in order to skip memory leaks test.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUpTest()">setUpTest</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Override to prepare test case after MagicDraw application started.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#tearDownTest()">tearDownTest</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tear down test case after it execution.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.tests.NamedTestCase">Methods inherited from class com.nomagic.magicdraw.tests.NamedTestCase</h3>
<code>getFullTestName, getMethodName, getTestName, getTestNamePrefix, isOverridingTestName, setMethodName, setTestName</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-junit.framework.TestCase">Methods inherited from class junit.framework.TestCase</h3>
<code>assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertEquals, assertFalse, assertFalse, assertNotNull, assertNotNull, assertNotSame, assertNotSame, assertNull, assertNull, assertSame, assertSame, assertTrue, assertTrue, countTestCases, createResult, fail, fail, failNotEquals, failNotSame, failSame, format, getName, run, runBare, setName, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>MagicDrawTestCase</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">MagicDrawTestCase</span>()</div>
<div class="block">Default test case initialization for executing test* methods.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>MagicDrawTestCase</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">MagicDrawTestCase</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method)</span></div>
<div class="block">Creates MagicDrawTestCase for executing specific test method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>method</code> - test method name to execute.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>MagicDrawTestCase</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">MagicDrawTestCase</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> testName)</span></div>
<div class="block">Creates MagicDrawTestCase of specific name for executing specific test method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>method</code> - test method name to execute.</dd>
<dd><code>testName</code> - name of created test. All none alpha numerical characters in name will be replaced by underscore character.</dd>
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
<section class="detail" id="setMemoryTestReady(boolean)">
<h3>setMemoryTestReady</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setMemoryTestReady</span><wbr/><span class="parameters">(boolean memoryTestReady)</span></div>
<div class="block">Specify if memory leaks test is ready, so it might be performed at the end of the test.
 Set it false if you need to disable memory leaks test performing at the end of the test.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>memoryTestReady</code> - true if memory test is ready</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSkipMemoryTest(boolean)">
<h3>setSkipMemoryTest</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setSkipMemoryTest</span><wbr/><span class="parameters">(boolean skipMemoryTest)</span></div>
<div class="block">Set to true in order to skip memory leaks test.
 Memory leaks test is always performed by default after MagicDraw project is closed
 and after each completed test.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>skipMemoryTest</code> - true if memory test should be skipped, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRunOnEventDispather(boolean)">
<h3>setRunOnEventDispather</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setRunOnEventDispather</span><wbr/><span class="parameters">(boolean runOnEventDispatcher)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">spelling error in name, use set #setRunOnEventDispatcher</div>
</div>
<div class="block">Sets if test case should be executed on event dispatching thread.
 MagicDrawTestCase is run on event dispatcher thread by default.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runOnEventDispatcher</code> - True if test case should be executed on event dispatching thread.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRunOnEventDispatcher(boolean)">
<h3>setRunOnEventDispatcher</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setRunOnEventDispatcher</span><wbr/><span class="parameters">(boolean runOnEventDispatcher)</span></div>
<div class="block">Sets if test case should be executed on event dispatching thread.
 MagicDrawTestCase is run on event dispatcher thread by default.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runOnEventDispatcher</code> - True if test case should be executed on event dispatching thread.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDoNotUseSilentMode(boolean)">
<h3>setDoNotUseSilentMode</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setDoNotUseSilentMode</span><wbr/><span class="parameters">(boolean doNotUseSilentMode)</span></div>
<div class="block">Specify if MagicDraw should show GUI modal dialogs during startup and features testing.
 MagicDraw is started up in silent mode by default.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>doNotUseSilentMode</code> - provide true value if GUI dialogs need to be shown during MagicDraw testing.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDoNotUseSilentMode()">
<h3>isDoNotUseSilentMode</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">isDoNotUseSilentMode</span>()</div>
<div class="block">Check if silent mode is not used for starting MagicDraw. Silent mode prevents
 confirmation dialogs pop-up during MagicDraw test.
 MagicDraw is started up in silent mode by default.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>True if MagicDraw is started in Not silent mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMemoryTestReady()">
<h3>isMemoryTestReady</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected final</span> <span class="return-type">boolean</span> <span class="element-name">isMemoryTestReady</span>()</div>
<div class="block">Check if memory leaks test might be performed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>True if memory leaks test is ready and might be performed, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredPlugins()">
<h3>getRequiredPlugins</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getRequiredPlugins</span>()</div>
<div class="block">Is used to specify plug-ins required by test case. Should be overridden in specific MagicDrawTestCase implementation.
 Default implementation returns empty List.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>List of plug-in IDs required by this test case.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredPluginsDescription()">
<h3>getRequiredPluginsDescription</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRequiredPluginsDescription</span>()</div>
<div class="block">Formats textual message about available plug-ins status(loaded/enabled).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String message about required plug-ins status.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequiredPluginsLoaded()">
<h3>isRequiredPluginsLoaded</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isRequiredPluginsLoaded</span>()</div>
<div class="block">Check if all plug-ins required by this test case are loaded and enabled.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>True if all required plug-ins are loaded and enabled, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUpTest()">
<h3>setUpTest</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setUpTest</span>()
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Override to prepare test case after MagicDraw application started.
 Test set up should be done here. Do not use default JUnit setUp() instead.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - from default JUnit setUp()</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="tearDownTest()">
<h3>tearDownTest</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">tearDownTest</span>()
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Tear down test case after it execution.
 This method is called after test method execution completed but MagicDraw Application not closed yet.
 Test tear down should be done here. Do not use default JUnit tearDown() instead.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - from default JUnit tearDown()</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeProject(com.nomagic.magicdraw.core.Project)">
<h3>closeProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeProject</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Close opened MagicDraw project. Performs memory leaks test after project is closed,
 so all references to the elements of the closed project should be disposed before method execution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MagicDraw Project to close.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeAllProjects()">
<h3>closeAllProjects</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeAllProjects</span>()</div>
<div class="block">Close all currently opened MagicDraw projects with performing memory leaks test.
 All references to the elements of the closed projects should be disposed before method execution.</div>
</section>
</li>
<li>
<section class="detail" id="checkMemoryLeaks()">
<h3>checkMemoryLeaks</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">checkMemoryLeaks</span>()</div>
<div class="block">Force memory leaks test execution.</div>
</section>
</li>
<li>
<section class="detail" id="invokeAndWaitOnDispatcher(java.lang.Runnable)">
<h3>invokeAndWaitOnDispatcher</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">invokeAndWaitOnDispatcher</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</span></div>
<div class="block">Executes runnable on dispatcher thread and waits till runnable is done.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - Runnable to execute.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertiesFile(java.io.File)">
<h3>getPropertiesFile</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getPropertiesFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> projectFile)</span></div>
<div class="block">Computes test case specific properties file according given project file.
 MagicDraw Project properties file pattern "project_name.properties".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectFile</code> - project file</dd>
<dt>Returns:</dt>
<dd>test case properties file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getXmlFile(java.io.File)">
<h3>getXmlFile</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getXmlFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> projectFile)</span></div>
<div class="block">Computes test case specific properties file according given project file.
 MagicDraw Project properties file pattern "project_name.xml".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectFile</code> - project file</dd>
<dt>Returns:</dt>
<dd>test case properties file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileWithExtension(java.io.File,java.lang.String)">
<h3>getFileWithExtension</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getFileWithExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> projectFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</span></div>
<div class="block">Computes test case specific properties file according given project file.
 MagicDraw Project properties file pattern "project_name.[extension]".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectFile</code> - project file</dd>
<dt>Returns:</dt>
<dd>test case properties file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadProject(java.lang.String)">
<h3>loadProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">loadProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> file)</span></div>
<div class="block">Opens MagicDraw project by absolute project file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - absolute file name of project to open.</dd>
<dt>Returns:</dt>
<dd>Opened project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadProject(java.lang.String,boolean)">
<h3>loadProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">loadProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectPath,
 boolean failIfProjectHasErrors)</span></div>
<div class="block">Opens MagicDraw project by absolute project file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectPath</code> - absolute file name of project to open.</dd>
<dd><code>failIfProjectHasErrors</code> - Specifies if test should fail if loaded project has any model inconsistency errors. Recommended to run with silentMode turned on.</dd>
<dt>Returns:</dt>
<dd>Opened project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadProject(java.lang.String,boolean,boolean)">
<h3>loadProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">loadProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectPath,
 boolean failIfProjectHasErrors,
 boolean loadAllDiagrams)</span></div>
<div class="block">Opens MagicDraw project by absolute project file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectPath</code> - absolute file name of project to open.</dd>
<dd><code>failIfProjectHasErrors</code> - Specifies if test should fail if loaded project has any model inconsistency errors. Recommended to run with silentMode turned on.</dd>
<dt>Returns:</dt>
<dd>Opened project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLogger()">
<h3>getLogger</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">org.apache.log4j.Logger</span> <span class="element-name">getLogger</span>()</div>
<div class="block">Gets logger for Test related output logging.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>log4j Logger for TEST category.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>Logger</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFailed()">
<h3>isFailed</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFailed</span>()</div>
<div class="block">Check if test has failed because of JUnit assertion or any other exception.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>True if this test has failed, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProjectComparator(java.lang.String)">
<h3>createProjectComparator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type"><a href="common/comparators/ProjectsComparator.html" title="class in com.nomagic.magicdraw.tests.common.comparators">ProjectsComparator</a></span> <span class="element-name">createProjectComparator</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> logText)</span></div>
<div class="block">Creates project comparator with default model and diagram comparators implementation.
 Comparator does not compare projects regarding their modules, author information, and diagram info data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>logText</code> - information message which should be printed to log at the beginning of comparison.</dd>
<dt>Returns:</dt>
<dd>new instance of ProjectsComparator with model and diagrams comparators initialized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openProject(java.lang.String)">
<h3>openProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">openProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectFile)</span></div>
<div class="block">Opens MagicDraw project by its absolute file name.
 It reopens the project if project is already opened.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectFile</code> - absolute file name of project to open.</dd>
<dt>Returns:</dt>
<dd>opened project or null if project cannot be opened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openProject(java.lang.String,boolean)">
<h3>openProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">openProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> projectFile,
 boolean loadAllDiagram)</span></div>
<div class="block">Opens MagicDraw project by its absolute file name.
 It reopens the project if project is already opened.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>projectFile</code> - absolute file name of project to open.</dd>
<dd><code>loadAllDiagram</code> - load content of all diagrams in the opened project</dd>
<dt>Returns:</dt>
<dd>opened project or null if project cannot be opened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveProject(com.nomagic.magicdraw.core.Project,java.io.File)">
<h3>saveProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">saveProject</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Save opened MagicDraw project to specific file. S
 Save is done ins silent mode without any GUI confirmation messages.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MagicDraw opened project to save.</dd>
<dd><code>file</code> - File to save project.</dd>
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
