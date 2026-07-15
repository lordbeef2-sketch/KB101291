# JAVA OPENAPI: ITeamworkService (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/teamwork2/ITeamworkService.html
- source_path: `com/nomagic/magicdraw/teamwork2/ITeamworkService.html`
- source_sha256: `09eff70ac8bb12b3253e65561e9961fbe996532249197476f0e79a0ffffd521e`
- captured_utc: `2026-07-14T16:45:47.497635+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.teamwork2](package-summary.html)

## Interface ITeamworkService

All Known Implementing Classes:
`[TeamworkService](TeamworkService.html)`

@OpenApiAllpublic interfaceITeamworkService

Interface for team server service

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ESI_SERVICE](#ESI_SERVICE)`
Identifier of ESI Server service
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getConnectedUser](#getConnectedUser())()`
Returns name of connected user .
`[EsiUtils](../esi/EsiUtils.html)`
`[getEsiUtils](#getEsiUtils())()`

`[ServerLoginInfo](ServerLoginInfo.html)`
`[getLastUsedLoginInfo](#getLastUsedLoginInfo())()`
Returns ServerLoginInfo
`default [ProjectDescriptor](../core/project/ProjectDescriptor.html)`
`[getProjectDescriptorById](#getProjectDescriptorById(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.createProjectDescriptorById(String)`](../esi/EsiUtils.html#createProjectDescriptorById(java.lang.String))
 Returns descriptor of project with given id
`[ProjectDescriptor](../core/project/ProjectDescriptor.html)`
`[getProjectDescriptorByQualifiedName](#getProjectDescriptorByQualifiedName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.getProjectDescriptorByQualifiedName(String)`](../esi/EsiUtils.html#getProjectDescriptorByQualifiedName(java.lang.String))
 Returns project descriptor.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)>`
`[getProjectDescriptors](#getProjectDescriptors())()`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.getRemoteProjectDescriptors()`](../esi/EsiUtils.html#getRemoteProjectDescriptors())
 Collect information about all projects on server
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getProjectIdByQualifiedName](#getProjectIdByQualifiedName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.getProjectIdByQualifiedName(String)`](../esi/EsiUtils.html#getProjectIdByQualifiedName(java.lang.String))
 Returns project id for given project qualified name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getServiceID](#getServiceID())()`
Return service id.
`com.nomagic.ci.persistence.versioning.IVersionDescriptor`
`[getVersion](#getVersion(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Deprecated.
use
 Current versions of given project
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.ci.persistence.versioning.IVersionDescriptor>`
`[getVersions](#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)`
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.getVersions(ProjectDescriptor)`](../esi/EsiUtils.html#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor))
 Versions of given project
`boolean`
`[isConnected](#isConnected())()`
Returns true, when connection between MD and server is established.
`boolean`
`[login](#login(boolean))(boolean useLastLoginData)`
Logs into last successful server using last successful input data.
`void`
`[login](#login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))([ServerLoginInfo](ServerLoginInfo.html) info,
 boolean encryptPassword)`
Login with given data
`boolean`
`[logout](#logout())()`
Logs out from server.
`void`
`[setLastUsedTeamworkInfo](#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))([ServerLoginInfo](ServerLoginInfo.html) info,
 boolean encryptPassword)`
Saves given input data, as last successful user connection info.

============ FIELD DETAIL =========== 
Field Details
ESI_SERVICE
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ESI_SERVICE
Identifier of ESI Server service
See Also:
[`getServiceID()`](#getServiceID())
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.teamwork2.ITeamworkService.ESI_SERVICE)
 ============ METHOD DETAIL ========== 
Method Details
getServiceID
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getServiceID()
Return service id.
Returns:
service id
isConnected
boolean isConnected()
Returns true, when connection between MD and server is established.
Returns:
true, when user is connected to server.
getConnectedUser
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getConnectedUser()
Returns name of connected user .
Returns:
User name of connected user. Null when no user is connected.
login
boolean login(boolean useLastLoginData)
Logs into last successful server using last successful input data.
Parameters:
`useLastLoginData` - true use last login data, false - specify new login data.
Returns:
return true if log-in was successful.
See Also:
[`setLastUsedTeamworkInfo(ServerLoginInfo, boolean)`](#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean))
login
void login([ServerLoginInfo](ServerLoginInfo.html) info,
 boolean encryptPassword)
Login with given data
Parameters:
`info` - login info
`encryptPassword` - encrypt password from given info
logout
boolean logout()
Logs out from server.
Returns:
True, when log out was successful.
setLastUsedTeamworkInfo
void setLastUsedTeamworkInfo([ServerLoginInfo](ServerLoginInfo.html) info,
 boolean encryptPassword)
Saves given input data, as last successful user connection info.
Parameters:
`info` - login info
`encryptPassword` - encrypt password from given info
getLastUsedLoginInfo
[ServerLoginInfo](ServerLoginInfo.html) getLastUsedLoginInfo()
Returns ServerLoginInfo
Returns:
ServerLoginInfo
getProjectDescriptors
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](../core/project/ProjectDescriptor.html)> getProjectDescriptors()
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.getRemoteProjectDescriptors()`](../esi/EsiUtils.html#getRemoteProjectDescriptors())
 Collect information about all projects on server
Returns:
descriptors of all projects
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some error
getProjectDescriptorById
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)default [ProjectDescriptor](../core/project/ProjectDescriptor.html) getProjectDescriptorById([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.createProjectDescriptorById(String)`](../esi/EsiUtils.html#createProjectDescriptorById(java.lang.String))
 Returns descriptor of project with given id
Parameters:
`id` - project id
Returns:
descriptor
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some error
getProjectIdByQualifiedName
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getProjectIdByQualifiedName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.getProjectIdByQualifiedName(String)`](../esi/EsiUtils.html#getProjectIdByQualifiedName(java.lang.String))
 Returns project id for given project qualified name.
Parameters:
`qualifiedName` - project qualified name, unique name constructed from project name and it's branches.
 Examples:
 "MyProject" with no branches = "MyProject"
 "MyProject" branch ["release"] = "MyProject##release"
 "MyProject" branch with subbranch ["release", "sp1"] = "MyProject##release##sp1"
Returns:
project id.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some error
getProjectDescriptorByQualifiedName
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)[ProjectDescriptor](../core/project/ProjectDescriptor.html) getProjectDescriptorByQualifiedName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qualifiedName)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.getProjectDescriptorByQualifiedName(String)`](../esi/EsiUtils.html#getProjectDescriptorByQualifiedName(java.lang.String))
 Returns project descriptor.
Parameters:
`qualifiedName` - project qualified name, unique name constructed from project name and it's branches.
 E.g:
 "MyProject" with no branches = "MyProject" 

 "MyProject" branch ["release"] = "MyProject##release" 

 "MyProject" branch with subbranch ["release", "sp1"] = "MyProject##release##sp1"
Returns:
remote project descriptor
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some error
getVersions
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.ci.persistence.versioning.IVersionDescriptor> getVersions([ProjectDescriptor](../core/project/ProjectDescriptor.html) descriptor)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Deprecated, for removal: This API element is subject to removal in a future version.
use [`EsiUtils.getVersions(ProjectDescriptor)`](../esi/EsiUtils.html#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor))
 Versions of given project
Parameters:
`descriptor` - descriptor.
Returns:
versions
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - in case of some error
getVersion
com.nomagic.ci.persistence.versioning.IVersionDescriptor getVersion([Project](../core/Project.html) project)
Deprecated.
use
 Current versions of given project
Parameters:
`project` - project
Returns:
versions
getEsiUtils
[EsiUtils](../esi/EsiUtils.html) getEsiUtils()
Returns:
EsiUtils

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.teamwork2</a></div>
<h1 class="title" title="Interface ITeamworkService">Interface ITeamworkService</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="TeamworkService.html" title="class in com.nomagic.magicdraw.teamwork2">TeamworkService</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ITeamworkService</span></div>
<div class="block">Interface for team server service</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ESI_SERVICE">ESI_SERVICE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifier of ESI Server service</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConnectedUser()">getConnectedUser</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns name of connected user .</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../esi/EsiUtils.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEsiUtils()">getEsiUtils</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLastUsedLoginInfo()">getLastUsedLoginInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns ServerLoginInfo</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default <a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#getProjectDescriptorById(java.lang.String)">getProjectDescriptorById</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use  <a href="../esi/EsiUtils.html#createProjectDescriptorById(java.lang.String)"><code>EsiUtils.createProjectDescriptorById(String)</code></a>
 Returns descriptor of project with given id</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getProjectDescriptorByQualifiedName(java.lang.String)">getProjectDescriptorByQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../esi/EsiUtils.html#getProjectDescriptorByQualifiedName(java.lang.String)"><code>EsiUtils.getProjectDescriptorByQualifiedName(String)</code></a>
 Returns project descriptor.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getProjectDescriptors()">getProjectDescriptors</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../esi/EsiUtils.html#getRemoteProjectDescriptors()"><code>EsiUtils.getRemoteProjectDescriptors()</code></a>
 Collect information about all projects on server</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getProjectIdByQualifiedName(java.lang.String)">getProjectIdByQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../esi/EsiUtils.html#getProjectIdByQualifiedName(java.lang.String)"><code>EsiUtils.getProjectIdByQualifiedName(String)</code></a>
 Returns project id for given project qualified name.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getServiceID()">getServiceID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return service id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getVersion(com.nomagic.magicdraw.core.Project)">getVersion</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use
 Current versions of given project</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.ci.persistence.versioning.IVersionDescriptor&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)">getVersions</a><wbr/>(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../esi/EsiUtils.html#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)"><code>EsiUtils.getVersions(ProjectDescriptor)</code></a>
 Versions of given project</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isConnected()">isConnected</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns true, when connection between MD and server is established.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#login(boolean)">login</a><wbr/>(boolean useLastLoginData)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Logs into last successful server using last successful input data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">login</a><wbr/>(<a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a> info,
 boolean encryptPassword)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Login with given data</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#logout()">logout</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Logs out from server.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">setLastUsedTeamworkInfo</a><wbr/>(<a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a> info,
 boolean encryptPassword)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Saves given input data, as last successful user connection info.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="ESI_SERVICE">
<h3>ESI_SERVICE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ESI_SERVICE</span></div>
<div class="block">Identifier of ESI Server service</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getServiceID()"><code>getServiceID()</code></a></li>
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.teamwork2.ITeamworkService.ESI_SERVICE">Constant Field Values</a></li>
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
<section class="detail" id="getServiceID()">
<h3>getServiceID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getServiceID</span>()</div>
<div class="block">Return service id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>service id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConnected()">
<h3>isConnected</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isConnected</span>()</div>
<div class="block">Returns true, when connection between MD and server is established.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, when user is connected to server.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedUser()">
<h3>getConnectedUser</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getConnectedUser</span>()</div>
<div class="block">Returns name of connected user .</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>User name of connected user. Null when no user is connected.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="login(boolean)">
<h3>login</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">login</span><wbr/><span class="parameters">(boolean useLastLoginData)</span></div>
<div class="block">Logs into last successful server using last successful input data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useLastLoginData</code> - true use last login data, false - specify new login data.</dd>
<dt>Returns:</dt>
<dd>return true if log-in was successful.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)"><code>setLastUsedTeamworkInfo(ServerLoginInfo, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="login(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">
<h3>login</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">login</span><wbr/><span class="parameters">(<a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a> info,
 boolean encryptPassword)</span></div>
<div class="block">Login with given data</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>info</code> - login info</dd>
<dd><code>encryptPassword</code> - encrypt password from given info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logout()">
<h3>logout</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">logout</span>()</div>
<div class="block">Logs out from server.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>True, when log out was successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLastUsedTeamworkInfo(com.nomagic.magicdraw.teamwork2.ServerLoginInfo,boolean)">
<h3>setLastUsedTeamworkInfo</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setLastUsedTeamworkInfo</span><wbr/><span class="parameters">(<a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a> info,
 boolean encryptPassword)</span></div>
<div class="block">Saves given input data, as last successful user connection info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>info</code> - login info</dd>
<dd><code>encryptPassword</code> - encrypt password from given info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastUsedLoginInfo()">
<h3>getLastUsedLoginInfo</h3>
<div class="member-signature"><span class="return-type"><a href="ServerLoginInfo.html" title="class in com.nomagic.magicdraw.teamwork2">ServerLoginInfo</a></span> <span class="element-name">getLastUsedLoginInfo</span>()</div>
<div class="block">Returns ServerLoginInfo</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ServerLoginInfo</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptors()">
<h3>getProjectDescriptors</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</span> <span class="element-name">getProjectDescriptors</span>()
                                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../esi/EsiUtils.html#getRemoteProjectDescriptors()"><code>EsiUtils.getRemoteProjectDescriptors()</code></a>
 Collect information about all projects on server</div>
</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>descriptors of all projects</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptorById(java.lang.String)">
<h3>getProjectDescriptorById</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">default</span> <span class="return-type"><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">getProjectDescriptorById</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span>
                                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use  <a href="../esi/EsiUtils.html#createProjectDescriptorById(java.lang.String)"><code>EsiUtils.createProjectDescriptorById(String)</code></a>
 Returns descriptor of project with given id</div>
</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - project id</dd>
<dt>Returns:</dt>
<dd>descriptor</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectIdByQualifiedName(java.lang.String)">
<h3>getProjectIdByQualifiedName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectIdByQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../esi/EsiUtils.html#getProjectIdByQualifiedName(java.lang.String)"><code>EsiUtils.getProjectIdByQualifiedName(String)</code></a>
 Returns project id for given project qualified name.</div>
</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qualifiedName</code> - project qualified name, unique name constructed from project name and it's branches.
                      Examples:
                      "MyProject" with no branches = "MyProject"
                      "MyProject" branch ["release"] = "MyProject##release"
                      "MyProject" branch with subbranch ["release", "sp1"] = "MyProject##release##sp1"</dd>
<dt>Returns:</dt>
<dd>project id.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectDescriptorByQualifiedName(java.lang.String)">
<h3>getProjectDescriptorByQualifiedName</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type"><a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">getProjectDescriptorByQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span>
                                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../esi/EsiUtils.html#getProjectDescriptorByQualifiedName(java.lang.String)"><code>EsiUtils.getProjectDescriptorByQualifiedName(String)</code></a>
 Returns project descriptor.</div>
</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qualifiedName</code> - project qualified name, unique name constructed from project name and it's branches.
                      <p>E.g:</p>
                      "MyProject" with no branches = "MyProject"<br/>
                      "MyProject" branch ["release"] = "MyProject##release"<br/>
                      "MyProject" branch with subbranch ["release", "sp1"] = "MyProject##release##sp1"<br/></dd>
<dt>Returns:</dt>
<dd>remote project descriptor</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>getVersions</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.ci.persistence.versioning.IVersionDescriptor&gt;</span> <span class="element-name">getVersions</span><wbr/><span class="parameters">(<a href="../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> descriptor)</span>
                                                                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use <a href="../esi/EsiUtils.html#getVersions(com.nomagic.magicdraw.core.project.ProjectDescriptor)"><code>EsiUtils.getVersions(ProjectDescriptor)</code></a>
 Versions of given project</div>
</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - descriptor.</dd>
<dt>Returns:</dt>
<dd>versions</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion(com.nomagic.magicdraw.core.Project)">
<h3>getVersion</h3>
<div class="member-signature"><span class="return-type">com.nomagic.ci.persistence.versioning.IVersionDescriptor</span> <span class="element-name">getVersion</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use
 Current versions of given project</div>
</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>versions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEsiUtils()">
<h3>getEsiUtils</h3>
<div class="member-signature"><span class="return-type"><a href="../esi/EsiUtils.html" title="interface in com.nomagic.magicdraw.esi">EsiUtils</a></span> <span class="element-name">getEsiUtils</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>EsiUtils</dd>
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
