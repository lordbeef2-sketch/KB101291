# JAVA OPENAPI: TeamworkService (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/teamwork2/TeamworkService.html
- source_path: `com/nomagic/magicdraw/teamwork2/TeamworkService.html`
- source_sha256: `e86acf0400305567aacbbbdb500083ccd96d6fdc4f076018a7ec7f32fb63730f`
- captured_utc: `2026-07-14T16:55:37.050252+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.teamwork2](package-summary.html)

## Class TeamworkService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.teamwork2.TeamworkService

All Implemented Interfaces:
`[ITeamworkService](ITeamworkService.html)`

@OpenApiAllpublic abstract classTeamworkService
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ITeamworkService](ITeamworkService.html)

Implementation of teamwork service.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.magicdraw.teamwork2.[ITeamworkService](ITeamworkService.html)
`[ESI_SERVICE](ITeamworkService.html#ESI_SERVICE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TeamworkService](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected abstract boolean`
`[autoLoginFromOptions](#autoLoginFromOptions(com.nomagic.task.ProgressStatus))([ProgressStatus](../../task/ProgressStatus.html) status)`
Auto logs into last successful server using last successful input data.
`boolean`
`[autoLoginOnTask](#autoLoginOnTask(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Task](../../task/Task.html)> taskRunner)`
Auto logs into last successful server using last successful input data with task runner
`static [ITeamworkService](ITeamworkService.html)`
`[getActiveInstance](#getActiveInstance())()`
Returns active server service, according to current connected state.
`static [ITeamworkService](ITeamworkService.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Returns server service, according to current project.
`static [ITeamworkService](ITeamworkService.html)`
`[getInstance](#getInstance(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Return instance by service id.
`[ServerLoginInfo](ServerLoginInfo.html)`
`[getLastUsedLoginInfo](#getLastUsedLoginInfo())()`
Returns list of input data, which was entered on last successful connection.
`protected [TeamworkOptionsGroup](../core/options/TeamworkOptionsGroup.html)`
`[getTeamworkOptions](#getTeamworkOptions())()`

`com.nomagic.ci.persistence.versioning.IVersionDescriptor`
`[getVersion](#getVersion(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Current versions of given project
`final boolean`
`[login](#login(boolean))(boolean useLastLoginData)`
Logs into last successful server using last successful input data.
`void`
`[login](#login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))([ServerLoginInfo](ServerLoginInfo.html) info,
 boolean encryptPassword)`
Login with given data
`protected abstract boolean`
`[loginFromOptions](#loginFromOptions(java.util.Map,com.nomagic.task.ProgressStatus))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> options,
 [ProgressStatus](../../task/ProgressStatus.html) status)`
Logs into last successful server using last successful input data.
`protected boolean`
`[loginOnTask](#loginOnTask(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> options)`

`boolean`
`[loginOnTask](#loginOnTask(java.util.Map,java.util.function.Consumer))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> options,
 [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Task](../../task/Task.html)> taskRunner)`

`static [ITeamworkService](ITeamworkService.html)`
`[setActiveInstance](#setActiveInstance(com.nomagic.magicdraw.teamwork2.ITeamworkService))([ITeamworkService](ITeamworkService.html) activeTeamworkService)`
Set active Teamwork Service instance.
`void`
`[setLastUsedTeamworkInfo](#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))([ServerLoginInfo](ServerLoginInfo.html) info,
 boolean encryptPassword)`
Saves given input data, as last successful user connection info.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.teamwork2.[ITeamworkService](ITeamworkService.html)
`[getConnectedUser](ITeamworkService.html#getConnectedUser()), [getProjectDescriptorById](ITeamworkService.html#getProjectDescriptorById(java.lang.String)), [getProjectDescriptorByQualifiedName](ITeamworkService.html#getProjectDescriptorByQualifiedName(java.lang.String)), [getProjectDescriptors](ITeamworkService.html#getProjectDescriptors()), [getProjectIdByQualifiedName](ITeamworkService.html#getProjectIdByQualifiedName(java.lang.String)), [getServiceID](ITeamworkService.html#getServiceID()), [getVersions](ITeamworkService.html#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)), [isConnected](ITeamworkService.html#isConnected()), [isLiveConnection](ITeamworkService.html#isLiveConnection()), [logout](ITeamworkService.html#logout()), [setAsLastUsedService](ITeamworkService.html#setAsLastUsedService())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TeamworkService
public TeamworkService()
 ============ METHOD DETAIL ========== 
Method Details
getInstance
@Nonnullpublic static [ITeamworkService](ITeamworkService.html) getInstance(@Nonnull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Return instance by service id.
Parameters:
`id` - service id
Returns:
service instance or null
setActiveInstance
@CheckForNullpublic static [ITeamworkService](ITeamworkService.html) setActiveInstance(@CheckForNull
 [ITeamworkService](ITeamworkService.html) activeTeamworkService)
Set active Teamwork Service instance. If set to null uses first found connected instance (default behavior).
Parameters:
`activeTeamworkService` - active service
Returns:
old active instance
getActiveInstance
@CheckForNullpublic static [ITeamworkService](ITeamworkService.html) getActiveInstance()
Returns active server service, according to current connected state. - whether it connected (to MU or CI) or not.
Returns:
if it is connected to MU server, returns Teamwork service, if to Cameo Team server, returns cameo service.
getInstance
@CheckForNullpublic static [ITeamworkService](ITeamworkService.html) getInstance([Project](../core/Project.html) project)
Returns server service, according to current project.
Parameters:
`project` - project
Returns:
if it is teamwork server project, returns Teamwork service, if Cameo Team server project, returns cameo service.
login
public final boolean login(boolean useLastLoginData)
Description copied from interface: `[ITeamworkService](ITeamworkService.html#login(boolean))`
Logs into last successful server using last successful input data.
Specified by:
`[login](ITeamworkService.html#login(boolean))` in interface `[ITeamworkService](ITeamworkService.html)`
Parameters:
`useLastLoginData` - true use last login data, false - specify new login data.
Returns:
return true if log-in was successful.
See Also:
[`ITeamworkService.setLastUsedTeamworkInfo(ServerLoginInfo, boolean)`](ITeamworkService.html#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))
loginOnTask
protected boolean loginOnTask(@CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> options)
loginOnTask
public boolean loginOnTask(@CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> options,
 [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Task](../../task/Task.html)> taskRunner)
autoLoginOnTask
public boolean autoLoginOnTask([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Task](../../task/Task.html)> taskRunner)
Auto logs into last successful server using last successful input data with task runner
Parameters:
`taskRunner` - runs auto login task
Returns:
return true if log-in was successful.
loginFromOptions
protected abstract boolean loginFromOptions(@CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> options,
 [ProgressStatus](../../task/ProgressStatus.html) status)
Logs into last successful server using last successful input data.
Parameters:
`options` - options.
`status` - progress status
Returns:
return true if log-in was successful.
autoLoginFromOptions
protected abstract boolean autoLoginFromOptions([ProgressStatus](../../task/ProgressStatus.html) status)
Auto logs into last successful server using last successful input data.
Parameters:
`status` - progress status
Returns:
return true if log-in was successful.
getTeamworkOptions
protected [TeamworkOptionsGroup](../core/options/TeamworkOptionsGroup.html) getTeamworkOptions()
login
public void login(@Nonnull
 [ServerLoginInfo](ServerLoginInfo.html) info,
 boolean encryptPassword)
Description copied from interface: `[ITeamworkService](ITeamworkService.html#login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))`
Login with given data
Specified by:
`[login](ITeamworkService.html#login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))` in interface `[ITeamworkService](ITeamworkService.html)`
Parameters:
`info` - login info
`encryptPassword` - encrypt password from given info
setLastUsedTeamworkInfo
public void setLastUsedTeamworkInfo(@Nonnull
 [ServerLoginInfo](ServerLoginInfo.html) info,
 boolean encryptPassword)
Description copied from interface: `[ITeamworkService](ITeamworkService.html#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))`
Saves given input data, as last successful user connection info.
Specified by:
`[setLastUsedTeamworkInfo](ITeamworkService.html#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))` in interface `[ITeamworkService](ITeamworkService.html)`
Parameters:
`info` - login info
`encryptPassword` - encrypt password from given info
getLastUsedLoginInfo
public [ServerLoginInfo](ServerLoginInfo.html) getLastUsedLoginInfo()
Description copied from interface: `[ITeamworkService](ITeamworkService.html#getLastUsedLoginInfo())`
Returns list of input data, which was entered on last successful connection. Array of: login username, pass,
 servername.
Specified by:
`[getLastUsedLoginInfo](ITeamworkService.html#getLastUsedLoginInfo())` in interface `[ITeamworkService](ITeamworkService.html)`
Returns:
array of username, pass, servername.
getVersion
public com.nomagic.ci.persistence.versioning.IVersionDescriptor getVersion(@Nonnull
 [Project](../core/Project.html) project)
Description copied from interface: `[ITeamworkService](ITeamworkService.html#getVersion(com.nomagic.magicdraw.core.Project))`
Current versions of given project
Specified by:
`[getVersion](ITeamworkService.html#getVersion(com.nomagic.magicdraw.core.Project))` in interface `[ITeamworkService](ITeamworkService.html)`
Parameters:
`project` - project
Returns:
versions

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.teamwork2</a></div>
<h1 class="title" title="Class TeamworkService">Class TeamworkService</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.teamwork2.TeamworkService</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">TeamworkService</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></span></div>
<div class="block">Implementation of teamwork service.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.teamwork2.ITeamworkService">Fields inherited from interface com.nomagic.magicdraw.teamwork2.<a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></h3>
<code><a href="ITeamworkService.html#ESI_SERVICE">ESI_SERVICE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TeamworkService</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#autoLoginFromOptions(com.nomagic.task.ProgressStatus)">autoLoginFromOptions</a><wbr/>(<a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Auto logs into last successful server using last successful input data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#autoLoginOnTask(java.util.function.Consumer)">autoLoginOnTask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="../../task/Task.html" title="class in com.nomagic.task">Task</a>&gt; taskRunner)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Auto logs into last successful server using last successful input data with task runner</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveInstance()">getActiveInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns active server service, according to current connected state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.core.Project)">getInstance</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns server service, according to current project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(java.lang.String)">getInstance</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return instance by service id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastUsedLoginInfo()">getLastUsedLoginInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of input data, which was entered on last successful connection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../core/options/TeamworkOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">TeamworkOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTeamworkOptions()">getTeamworkOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion(com.nomagic.magicdraw.core.Project)">getVersion</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Current versions of given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#login(boolean)">login</a><wbr/>(boolean useLastLoginData)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Logs into last successful server using last successful input data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">login</a><wbr/>(<a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a> info,
 boolean encryptPassword)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Login with given data</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#loginFromOptions(java.util.Map,com.nomagic.task.ProgressStatus)">loginFromOptions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; options,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Logs into last successful server using last successful input data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loginOnTask(java.util.Map)">loginOnTask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loginOnTask(java.util.Map,java.util.function.Consumer)">loginOnTask</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; options,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="../../task/Task.html" title="class in com.nomagic.task">Task</a>&gt; taskRunner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setActiveInstance(com.nomagic.magicdraw.teamwork2.ITeamworkService)">setActiveInstance</a><wbr/>(<a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a> activeTeamworkService)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set active Teamwork Service instance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">setLastUsedTeamworkInfo</a><wbr/>(<a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a> info,
 boolean encryptPassword)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves given input data, as last successful user connection info.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.teamwork2.ITeamworkService">Methods inherited from interface com.nomagic.magicdraw.teamwork2.<a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></h3>
<code><a href="ITeamworkService.html#getConnectedUser()">getConnectedUser</a>, <a href="ITeamworkService.html#getProjectDescriptorById(java.lang.String)">getProjectDescriptorById</a>, <a href="ITeamworkService.html#getProjectDescriptorByQualifiedName(java.lang.String)">getProjectDescriptorByQualifiedName</a>, <a href="ITeamworkService.html#getProjectDescriptors()">getProjectDescriptors</a>, <a href="ITeamworkService.html#getProjectIdByQualifiedName(java.lang.String)">getProjectIdByQualifiedName</a>, <a href="ITeamworkService.html#getServiceID()">getServiceID</a>, <a href="ITeamworkService.html#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getVersions</a>, <a href="ITeamworkService.html#isConnected()">isConnected</a>, <a href="ITeamworkService.html#isLiveConnection()">isLiveConnection</a>, <a href="ITeamworkService.html#logout()">logout</a>, <a href="ITeamworkService.html#setAsLastUsedService()">setAsLastUsedService</a></code></div>
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
<h3>TeamworkService</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TeamworkService</span>()</div>
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
<section class="detail" id="getInstance(java.lang.String)">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@Nonnull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(@Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Return instance by service id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - service id</dd>
<dt>Returns:</dt>
<dd>service instance or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActiveInstance(com.nomagic.magicdraw.teamwork2.ITeamworkService)">
<h3>setActiveInstance</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></span> <span class="element-name">setActiveInstance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a> activeTeamworkService)</span></div>
<div class="block">Set active Teamwork Service instance. If set to null uses first found connected instance (default behavior).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activeTeamworkService</code> - active service</dd>
<dt>Returns:</dt>
<dd>old active instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveInstance()">
<h3>getActiveInstance</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></span> <span class="element-name">getActiveInstance</span>()</div>
<div class="block">Returns active server service, according to current connected state. - whether it connected (to MU or CI) or not.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>if it is connected to MU server, returns Teamwork service, if to Cameo Team server, returns cameo service.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.core.Project)">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns server service, according to current project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>if it is teamwork server project, returns Teamwork service, if Cameo Team server project, returns cameo service.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="login(boolean)">
<h3>login</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">login</span><wbr/><span class="parameters">(boolean useLastLoginData)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ITeamworkService.html#login(boolean)">ITeamworkService</a></code></span></div>
<div class="block">Logs into last successful server using last successful input data.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITeamworkService.html#login(boolean)">login</a></code> in interface <code><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></dd>
<dt>Parameters:</dt>
<dd><code>useLastLoginData</code> - true use last login data, false - specify new login data.</dd>
<dt>Returns:</dt>
<dd>return true if log-in was successful.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="ITeamworkService.html#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)"><code>ITeamworkService.setLastUsedTeamworkInfo(ServerLoginInfo, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loginOnTask(java.util.Map)">
<h3>loginOnTask</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">loginOnTask</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; options)</span></div>
</section>
</li>
<li>
<section class="detail" id="loginOnTask(java.util.Map,java.util.function.Consumer)">
<h3>loginOnTask</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loginOnTask</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; options,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="../../task/Task.html" title="class in com.nomagic.task">Task</a>&gt; taskRunner)</span></div>
</section>
</li>
<li>
<section class="detail" id="autoLoginOnTask(java.util.function.Consumer)">
<h3>autoLoginOnTask</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">autoLoginOnTask</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="../../task/Task.html" title="class in com.nomagic.task">Task</a>&gt; taskRunner)</span></div>
<div class="block">Auto logs into last successful server using last successful input data with task runner</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taskRunner</code> - runs auto login task</dd>
<dt>Returns:</dt>
<dd>return true if log-in was successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loginFromOptions(java.util.Map,com.nomagic.task.ProgressStatus)">
<h3>loginFromOptions</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">boolean</span> <span class="element-name">loginFromOptions</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; options,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Logs into last successful server using last successful input data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - options.</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>return true if log-in was successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="autoLoginFromOptions(com.nomagic.task.ProgressStatus)">
<h3>autoLoginFromOptions</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">boolean</span> <span class="element-name">autoLoginFromOptions</span><wbr/><span class="parameters">(<a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Auto logs into last successful server using last successful input data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>return true if log-in was successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTeamworkOptions()">
<h3>getTeamworkOptions</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../core/options/TeamworkOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">TeamworkOptionsGroup</a></span> <span class="element-name">getTeamworkOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">
<h3>login</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">login</span><wbr/><span class="parameters">(@Nonnull
 <a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a> info,
 boolean encryptPassword)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ITeamworkService.html#login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">ITeamworkService</a></code></span></div>
<div class="block">Login with given data</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITeamworkService.html#login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">login</a></code> in interface <code><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></dd>
<dt>Parameters:</dt>
<dd><code>info</code> - login info</dd>
<dd><code>encryptPassword</code> - encrypt password from given info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">
<h3>setLastUsedTeamworkInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastUsedTeamworkInfo</span><wbr/><span class="parameters">(@Nonnull
 <a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a> info,
 boolean encryptPassword)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ITeamworkService.html#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">ITeamworkService</a></code></span></div>
<div class="block">Saves given input data, as last successful user connection info.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITeamworkService.html#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">setLastUsedTeamworkInfo</a></code> in interface <code><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></dd>
<dt>Parameters:</dt>
<dd><code>info</code> - login info</dd>
<dd><code>encryptPassword</code> - encrypt password from given info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastUsedLoginInfo()">
<h3>getLastUsedLoginInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a></span> <span class="element-name">getLastUsedLoginInfo</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ITeamworkService.html#getLastUsedLoginInfo()">ITeamworkService</a></code></span></div>
<div class="block">Returns list of input data, which was entered on last successful connection. Array of: login username, pass,
 servername.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITeamworkService.html#getLastUsedLoginInfo()">getLastUsedLoginInfo</a></code> in interface <code><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></dd>
<dt>Returns:</dt>
<dd>array of username, pass, servername.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion(com.nomagic.magicdraw.core.Project)">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.ci.persistence.versioning.IVersionDescriptor</span> <span class="element-name">getVersion</span><wbr/><span class="parameters">(@Nonnull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ITeamworkService.html#getVersion(com.nomagic.magicdraw.core.Project)">ITeamworkService</a></code></span></div>
<div class="block">Current versions of given project</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITeamworkService.html#getVersion(com.nomagic.magicdraw.core.Project)">getVersion</a></code> in interface <code><a href="ITeamworkService.html" title="interface in com.nomagic.magicdraw.teamwork2">ITeamworkService</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>versions</dd>
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
