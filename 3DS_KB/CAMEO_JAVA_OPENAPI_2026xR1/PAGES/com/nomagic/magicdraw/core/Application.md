# JAVA OPENAPI: Application (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/Application.html
- source_path: `com/nomagic/magicdraw/core/Application.html`
- source_sha256: `b826dc2114114a4322cd1564efc3095ad99cf3380ec6c3fd71409e4936fe070a`
- captured_utc: `2026-07-14T16:45:30.767412+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class Application

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.Application

@OpenApipublic classApplication
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Main class which connects main parts of MagicDraw.
 This class is singleton, only one instance of this class can exist.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[Application.Environment](Application.Environment.html)`
Contains application environment specific constants and utility methods.
`static class`
`[Application.Runtime](Application.Runtime.html)`
Contains application runtime related constants and utility methods.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[Application](#%3Cinit%3E())()`
Constructor of Application.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addActivityAfterStartup](#addActivityAfterStartup(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) activity)`
Registered runnable is executed right after MagicDraw application startup.
`void`
`[addNewDiagramType](#addNewDiagramType(com.nomagic.magicdraw.uml.DiagramDescriptor))([DiagramDescriptor](../uml/DiagramDescriptor.html) descriptor)`
Registers new diagram type in the MagicDraw application.
`final void`
`[addProjectEventListener](#addProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener))([ProjectEventListener](project/ProjectEventListener.html) listener)`
Method adds new ProjectEventListener.
`void`
`[addSaveParticipant](#addSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant))([SaveParticipant](SaveParticipant.html) participant)`
Registers SaveParticipant for custom actions on project saving.
`static [Application.Environment](Application.Environment.html)`
`[environment](#environment())()`
Gets application environment.
`final [CookieSet](../cookies/CookieSet.html)`
`[getCookieSet](#getCookieSet())()`
Returns cookie set of the application.
`[EnvironmentOptions](options/EnvironmentOptions.html)`
`[getEnvironmentOptions](#getEnvironmentOptions())()`
Gets application environment options.
`[GUILog](GUILog.html)`
`[getGUILog](#getGUILog())()`
Returns the interface to log window.
`static [Application](Application.html)`
`[getInstance](#getInstance())()`
Returns single instance of Application.
`[MainFrame](../ui/MainFrame.html)`
`[getMainFrame](#getMainFrame())()`
Returns the mainFrame - main MagicDraw GUI component.
`[Project](Project.html)`
`[getProject](#getProject())()`
Returns current active Project.
`[ProjectsManager](project/ProjectsManager.html)`
`[getProjectsManager](#getProjectsManager())()`
Returns the projectsManager.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[SaveParticipant](SaveParticipant.html)>`
`[getSaveParticipants](#getSaveParticipants())()`
List of registered SaveParticipants.
`boolean`
`[isTryToLoadProject](#isTryToLoadProject())()`
Checks if it is allowed to load project on startup.
`void`
`[loadAliases](#loadAliases())()`
Loads alias.properties file into memory.
`void`
`[removeProjectEventListener](#removeProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener))([ProjectEventListener](project/ProjectEventListener.html) listener)`
Method removes ProjectEventListener.
`void`
`[removeSaveParticipant](#removeSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant))([SaveParticipant](SaveParticipant.html) participant)`
Unregister custom SaveParticipant.
`static [Application.Runtime](Application.Runtime.html)`
`[runtime](#runtime())()`
Gets application runtime.
`void`
`[setApplicationName](#setApplicationName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Set the name of the application.
`void`
`[shutdown](#shutdown())()`
Shutdowns the application.
`void`
`[start](#start(boolean,boolean,boolean,java.lang.String%5B%5D,com.nomagic.magicdraw.core.StartupParticipant))(boolean guiVisible,
 boolean silentMode,
 boolean tryToLoadProject,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] args,
 [StartupParticipant](StartupParticipant.html) participant)`
Starts the application.
`void`
`[start](#start(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] args)`
Starts the application.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Application
@OpenApiprotected Application()
Constructor of Application.
 ============ METHOD DETAIL ========== 
Method Details
loadAliases
@OpenApipublic void loadAliases()
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Loads alias.properties file into memory. If alias were already loaded reload it.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some error
getEnvironmentOptions
@OpenApipublic [EnvironmentOptions](options/EnvironmentOptions.html) getEnvironmentOptions()
Gets application environment options.
Returns:
application environment options.
getInstance
@OpenApipublic static [Application](Application.html) getInstance()
Returns single instance of Application.
Returns:
single instance of Application.
getProject
@CheckForNull
@OpenApipublic [Project](Project.html) getProject()
Returns current active Project.
Returns:
current project, null if there is no current project.
getProjectsManager
@OpenApipublic [ProjectsManager](project/ProjectsManager.html) getProjectsManager()
Returns the projectsManager.
Returns:
ProjectsManager
getMainFrame
@OpenApipublic [MainFrame](../ui/MainFrame.html) getMainFrame()
Returns the mainFrame - main MagicDraw GUI component.
Returns:
MainFrame
setApplicationName
@OpenApipublic void setApplicationName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Set the name of the application.
Parameters:
`name` - application name
start
@OpenApipublic void start([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] args)
 throws [ApplicationExitedException](../../runtime/ApplicationExitedException.html)
Starts the application.
Parameters:
`args` - command line arguments passed to MagicDraw.
Throws:
`[ApplicationExitedException](../../runtime/ApplicationExitedException.html)` - in case of some error
start
@OpenApipublic void start(boolean guiVisible,
 boolean silentMode,
 boolean tryToLoadProject,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] args,
 @CheckForNull
 [StartupParticipant](StartupParticipant.html) participant)
 throws [ApplicationExitedException](../../runtime/ApplicationExitedException.html)
Starts the application.
Parameters:
`guiVisible` - start MagicDraw with visible GUI.
`silentMode` - true if GUI must be in silent mode(batch mode).
`tryToLoadProject` - true if application should try to load file passed as argument.
`args` - command line arguments passed to MagicDraw.
`participant` - the participant of startup process. May be null.
Throws:
`[ApplicationExitedException](../../runtime/ApplicationExitedException.html)` - if application exists during the startup.
shutdown
@OpenApipublic void shutdown()
 throws [ApplicationExitedException](../../runtime/ApplicationExitedException.html)
Shutdowns the application. User will be asked to save all opened projects before
 exiting the application.
Throws:
`[ApplicationExitedException](../../runtime/ApplicationExitedException.html)` - in case of some error
getGUILog
@OpenApipublic [GUILog](GUILog.html) getGUILog()
Returns the interface to log window.
Returns:
window for writing messages.
addProjectEventListener
@OpenApipublic final void addProjectEventListener([ProjectEventListener](project/ProjectEventListener.html) listener)
Method adds new ProjectEventListener.
Parameters:
`listener` - listener to be added.
removeProjectEventListener
@OpenApipublic void removeProjectEventListener([ProjectEventListener](project/ProjectEventListener.html) listener)
Method removes ProjectEventListener.
Parameters:
`listener` - to be removed.
addActivityAfterStartup
@OpenApipublic void addActivityAfterStartup([Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) activity)
Registered runnable is executed right after MagicDraw application startup.
Parameters:
`activity` - runnable to execute.
getCookieSet
@OpenApipublic final [CookieSet](../cookies/CookieSet.html) getCookieSet()
Returns cookie set of the application. 
This cookie set may be used for example to replace standard application
 CloseCookie with some other. 

 The example: 

 CookieSet set = application.getCookieSet(); 

 CloseCookie newCloseCookie = ...; 

 CloseCookie close = (CloseCookie) set.getCookie(CloseCookie.class); 

 set.remove(close); 

 set.add(newCloseCookie);
Returns:
cookie set of the application.
addNewDiagramType
@OpenApipublic void addNewDiagramType([DiagramDescriptor](../uml/DiagramDescriptor.html) descriptor)
Registers new diagram type in the MagicDraw application.
Parameters:
`descriptor` - descriptor of the new diagram.
getSaveParticipants
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[SaveParticipant](SaveParticipant.html)> getSaveParticipants()
List of registered SaveParticipants.
Returns:
list of registered Save Participants.
addSaveParticipant
@OpenApipublic void addSaveParticipant([SaveParticipant](SaveParticipant.html) participant)
Registers SaveParticipant for custom actions on project saving.
Parameters:
`participant` - the custom SaveParticipant.
removeSaveParticipant
@OpenApipublic void removeSaveParticipant([SaveParticipant](SaveParticipant.html) participant)
Unregister custom SaveParticipant.
Parameters:
`participant` - the custom SaveParticipant.
isTryToLoadProject
@OpenApipublic boolean isTryToLoadProject()
Checks if it is allowed to load project on startup. Under integrations loading may cause deadlock and is disabled.
Returns:
true if project may be loaded on application startup.
runtime
@OpenApipublic static [Application.Runtime](Application.Runtime.html) runtime()
Gets application runtime.
Returns:
application runtime.
environment
@OpenApipublic static [Application.Environment](Application.Environment.html) environment()
Gets application environment.
Returns:
application environment.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Class Application">Class Application</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.Application</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Application</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Main class which  connects main parts of MagicDraw.
 This class is singleton, only one instance of this class can exist.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Application.Environment.html" title="class in com.nomagic.magicdraw.core">Application.Environment</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains application environment specific constants and utility methods.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Application.Runtime.html" title="class in com.nomagic.magicdraw.core">Application.Runtime</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains application runtime related constants and utility methods.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Application</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor of Application.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addActivityAfterStartup(java.lang.Runnable)">addActivityAfterStartup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> activity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registered runnable is executed right after MagicDraw application startup.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addNewDiagramType(com.nomagic.magicdraw.uml.DiagramDescriptor)">addNewDiagramType</a><wbr/>(<a href="../uml/DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers new diagram type in the MagicDraw application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">addProjectEventListener</a><wbr/>(<a href="project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method adds new ProjectEventListener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant)">addSaveParticipant</a><wbr/>(<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a> participant)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers SaveParticipant for custom actions on project saving.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Application.Environment.html" title="class in com.nomagic.magicdraw.core">Application.Environment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#environment()">environment</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets application environment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../cookies/CookieSet.html" title="class in com.nomagic.magicdraw.cookies">CookieSet</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCookieSet()">getCookieSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns cookie set of the application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="options/EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options">EnvironmentOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnvironmentOptions()">getEnvironmentOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets application environment options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="GUILog.html" title="class in com.nomagic.magicdraw.core">GUILog</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGUILog()">getGUILog</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the interface to log window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Application.html" title="class in com.nomagic.magicdraw.core">Application</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns single instance of Application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/MainFrame.html" title="class in com.nomagic.magicdraw.ui">MainFrame</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainFrame()">getMainFrame</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the mainFrame - main MagicDraw GUI component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns current active Project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="project/ProjectsManager.html" title="class in com.nomagic.magicdraw.core.project">ProjectsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectsManager()">getProjectsManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the projectsManager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSaveParticipants()">getSaveParticipants</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">List of registered SaveParticipants.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTryToLoadProject()">isTryToLoadProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if it is allowed to load project on startup.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadAliases()">loadAliases</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads alias.properties file into memory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">removeProjectEventListener</a><wbr/>(<a href="project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method removes ProjectEventListener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant)">removeSaveParticipant</a><wbr/>(<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a> participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister custom SaveParticipant.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Application.Runtime.html" title="class in com.nomagic.magicdraw.core">Application.Runtime</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#runtime()">runtime</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets application runtime.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setApplicationName(java.lang.String)">setApplicationName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the name of the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shutdown()">shutdown</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shutdowns the application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(boolean,boolean,boolean,java.lang.String%5B%5D,com.nomagic.magicdraw.core.StartupParticipant)">start</a><wbr/>(boolean guiVisible,
 boolean silentMode,
 boolean tryToLoadProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args,
 <a href="StartupParticipant.html" title="interface in com.nomagic.magicdraw.core">StartupParticipant</a> participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(java.lang.String%5B%5D)">start</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts the application.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>Application</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="element-name">Application</span>()</div>
<div class="block">Constructor of Application.</div>
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
<section class="detail" id="loadAliases()">
<h3>loadAliases</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadAliases</span>()
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Loads alias.properties file into memory. If alias were already loaded reload it.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnvironmentOptions()">
<h3>getEnvironmentOptions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="options/EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options">EnvironmentOptions</a></span> <span class="element-name">getEnvironmentOptions</span>()</div>
<div class="block">Gets application environment options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application environment options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Application.html" title="class in com.nomagic.magicdraw.core">Application</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns single instance of Application.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>single instance of Application.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Returns current active Project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>current project, null if there is no current project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectsManager()">
<h3>getProjectsManager</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="project/ProjectsManager.html" title="class in com.nomagic.magicdraw.core.project">ProjectsManager</a></span> <span class="element-name">getProjectsManager</span>()</div>
<div class="block">Returns the projectsManager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ProjectsManager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainFrame()">
<h3>getMainFrame</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../ui/MainFrame.html" title="class in com.nomagic.magicdraw.ui">MainFrame</a></span> <span class="element-name">getMainFrame</span>()</div>
<div class="block">Returns the mainFrame - main MagicDraw GUI component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>MainFrame</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplicationName(java.lang.String)">
<h3>setApplicationName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setApplicationName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Set the name of the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - application name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(java.lang.String[])">
<h3>start</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</span>
           throws <span class="exceptions"><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></span></div>
<div class="block">Starts the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>args</code> - command line arguments passed to MagicDraw.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(boolean,boolean,boolean,java.lang.String[],com.nomagic.magicdraw.core.StartupParticipant)">
<h3>start</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(boolean guiVisible,
 boolean silentMode,
 boolean tryToLoadProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args,
 @CheckForNull
 <a href="StartupParticipant.html" title="interface in com.nomagic.magicdraw.core">StartupParticipant</a> participant)</span>
           throws <span class="exceptions"><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></span></div>
<div class="block">Starts the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>guiVisible</code> - start MagicDraw with visible GUI.</dd>
<dd><code>silentMode</code> - true if GUI must be in silent mode(batch mode).</dd>
<dd><code>tryToLoadProject</code> - true if application should try to load file passed as argument.</dd>
<dd><code>args</code> - command line arguments passed to MagicDraw.</dd>
<dd><code>participant</code> - the participant of startup process. May be null.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></code> - if application exists during the startup.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shutdown()">
<h3>shutdown</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">shutdown</span>()
              throws <span class="exceptions"><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></span></div>
<div class="block">Shutdowns the application. User will be asked to save all opened projects before
 exiting the application.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGUILog()">
<h3>getGUILog</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="GUILog.html" title="class in com.nomagic.magicdraw.core">GUILog</a></span> <span class="element-name">getGUILog</span>()</div>
<div class="block">Returns the interface to log window.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>window for writing messages.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">
<h3>addProjectEventListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">addProjectEventListener</span><wbr/><span class="parameters">(<a href="project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</span></div>
<div class="block">Method adds new ProjectEventListener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">
<h3>removeProjectEventListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProjectEventListener</span><wbr/><span class="parameters">(<a href="project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</span></div>
<div class="block">Method removes ProjectEventListener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addActivityAfterStartup(java.lang.Runnable)">
<h3>addActivityAfterStartup</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addActivityAfterStartup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> activity)</span></div>
<div class="block">Registered runnable is executed right after MagicDraw application startup.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activity</code> - runnable to execute.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCookieSet()">
<h3>getCookieSet</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../cookies/CookieSet.html" title="class in com.nomagic.magicdraw.cookies">CookieSet</a></span> <span class="element-name">getCookieSet</span>()</div>
<div class="block">Returns cookie set of the application. <br/>This cookie set may be used for example to replace standard application
 CloseCookie with some other.<br/>
 The example:<br/>
 CookieSet set = application.getCookieSet();<br/>
 CloseCookie newCloseCookie = ...;<br/>
 CloseCookie close = (CloseCookie) set.getCookie(CloseCookie.class);<br/>
 set.remove(close);<br/>
 set.add(newCloseCookie);<br/></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>cookie set of the application.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addNewDiagramType(com.nomagic.magicdraw.uml.DiagramDescriptor)">
<h3>addNewDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addNewDiagramType</span><wbr/><span class="parameters">(<a href="../uml/DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a> descriptor)</span></div>
<div class="block">Registers new diagram type in the MagicDraw application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - descriptor of the new diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSaveParticipants()">
<h3>getSaveParticipants</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a>&gt;</span> <span class="element-name">getSaveParticipants</span>()</div>
<div class="block">List of registered SaveParticipants.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of registered Save Participants.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant)">
<h3>addSaveParticipant</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSaveParticipant</span><wbr/><span class="parameters">(<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a> participant)</span></div>
<div class="block">Registers SaveParticipant for custom actions on project saving.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>participant</code> - the custom SaveParticipant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant)">
<h3>removeSaveParticipant</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSaveParticipant</span><wbr/><span class="parameters">(<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a> participant)</span></div>
<div class="block">Unregister custom SaveParticipant.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>participant</code> - the custom SaveParticipant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTryToLoadProject()">
<h3>isTryToLoadProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTryToLoadProject</span>()</div>
<div class="block">Checks if it is allowed to load project on startup. Under integrations loading may cause deadlock and is disabled.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project may be loaded on application startup.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runtime()">
<h3>runtime</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Application.Runtime.html" title="class in com.nomagic.magicdraw.core">Application.Runtime</a></span> <span class="element-name">runtime</span>()</div>
<div class="block">Gets application runtime.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application runtime.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="environment()">
<h3>environment</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Application.Environment.html" title="class in com.nomagic.magicdraw.core">Application.Environment</a></span> <span class="element-name">environment</span>()</div>
<div class="block">Gets application environment.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application environment.</dd>
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
