# JAVA OPENAPI: ProjectDescriptorsFactory (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/project/ProjectDescriptorsFactory.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectDescriptorsFactory.html`
- source_sha256: `ae9ac0853fd2349e9d3e8ced0e675d661c7098a5a533fbe352db38996d6f01a5`
- captured_utc: `2026-07-14T16:55:13.463989+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Class ProjectDescriptorsFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.project.ProjectDescriptorsFactory

@OpenApiAllpublic classProjectDescriptorsFactory
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Factory for ProjectDescriptors creating.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectDescriptorsFactory](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html)`
`[constructRemoteURI](#constructRemoteURI(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)`
Creates project URI for remote project.
`static [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html)`
`[constructRemoteURI](#constructRemoteURI(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 int version)`
Creates project URI for remote project and given version.
`static [AbstractRemoteProjectDescriptor](AbstractRemoteProjectDescriptor.html)`
`[createAbstractRemoteProjectDescriptorWithActualVersion](#createAbstractRemoteProjectDescriptorWithActualVersion(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Creates remote project descriptor.
`static [ProjectDescriptor](ProjectDescriptor.html)`
`[createAnyRemoteProjectDescriptor](#createAnyRemoteProjectDescriptor(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Creates remote project descriptor.
`static [ProjectDescriptor](ProjectDescriptor.html)`
`[createLocalProjectDescriptor](#createLocalProjectDescriptor(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Creates local project descriptor.
`static [ProjectDescriptor](ProjectDescriptor.html)`
`[createLocalProjectDescriptor](#createLocalProjectDescriptor(com.nomagic.magicdraw.core.Project,java.io.File))([Project](../Project.html) project,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`
Creates local project descriptor with given project and file
`static [ProjectDescriptor](ProjectDescriptor.html)`
`[createProjectDescriptor](#createProjectDescriptor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) location)`
Deprecated.
Use [`createProjectDescriptor(URI)`](#createProjectDescriptor(java.net.URI))
 Parses location String and creates ProjectDescriptor object from project's location string.
`static [ProjectDescriptor](ProjectDescriptor.html)`
`[createProjectDescriptor](#createProjectDescriptor(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) location)`
Parses location String and creates ProjectDescriptor object from project's location string.
`static [ProjectDescriptor](ProjectDescriptor.html)`
`[createRemoteProjectDescriptor](#createRemoteProjectDescriptor(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 int actualVersionNumber)`
Creates project descriptor for remote project and given version.
`static [ProjectDescriptor](ProjectDescriptor.html)`
`[createRemoteProjectDescriptor](#createRemoteProjectDescriptor(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actualVersionNumber)`
Creates project descriptor for remote project and given version.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](ProjectDescriptor.html)>`
`[getAvailableDescriptorsForProject](#getAvailableDescriptorsForProject(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Returns all available descriptors for given project.
`static [ProjectDescriptor](ProjectDescriptor.html)`
`[getDescriptorForProject](#getDescriptorForProject(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Returns project descriptor for given project
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Retrieves project name from given uri.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getProjectFullPath](#getProjectFullPath(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Get project branch path (WITH project name) or just project name if branches are not applicable for given uri
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getProjectName](#getProjectName(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Extract project name from the URI.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemoteID](#getRemoteID(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Retrieves project id from given uri.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemoteID](#getRemoteID(java.net.URI,java.lang.String))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Retrieves project id from given uri.
`static long`
`[getRemoteLongVersion](#getRemoteLongVersion(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Retrieves remote version from given uri.
`static int`
`[getRemoteVersion](#getRemoteVersion(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Deprecated.
use [`getRemoteLongVersion(URI)`](#getRemoteLongVersion(java.net.URI))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemoteVersionAsString](#getRemoteVersionAsString(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Retrieves remote version from given uri.
`static boolean`
`[isAnyRemote](#isAnyRemote(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectDescriptorsFactory
public ProjectDescriptorsFactory()
 ============ METHOD DETAIL ========== 
Method Details
createProjectDescriptor
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [ProjectDescriptor](ProjectDescriptor.html) createProjectDescriptor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) location)
Deprecated.
Use [`createProjectDescriptor(URI)`](#createProjectDescriptor(java.net.URI))
 Parses location String and creates ProjectDescriptor object from project's location string.
Parameters:
`location` - the project's location
Returns:
constructed ProjectDescriptor object.
createProjectDescriptor
@CheckForNullpublic static [ProjectDescriptor](ProjectDescriptor.html) createProjectDescriptor(@CheckForNull
 [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) location)
Parses location String and creates ProjectDescriptor object from project's location string.
Parameters:
`location` - the project's location
Returns:
constructed ProjectDescriptor object.
getAvailableDescriptorsForProject
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectDescriptor](ProjectDescriptor.html)> getAvailableDescriptorsForProject([Project](../Project.html) project)
Returns all available descriptors for given project.
Parameters:
`project` - the project.
Returns:
List of descriptors.
getDescriptorForProject
public static [ProjectDescriptor](ProjectDescriptor.html) getDescriptorForProject([Project](../Project.html) project)
Returns project descriptor for given project
Parameters:
`project` - project for which descriptor is created.
Returns:
Local project descriptor if project is local, remote project descriptor if project is remote.
createLocalProjectDescriptor
public static [ProjectDescriptor](ProjectDescriptor.html) createLocalProjectDescriptor([Project](../Project.html) project)
Creates local project descriptor.
Parameters:
`project` - project for which descriptor is created.
Returns:
created project descriptor
createLocalProjectDescriptor
public static [ProjectDescriptor](ProjectDescriptor.html) createLocalProjectDescriptor(@CheckForNull
 [Project](../Project.html) project,
 @CheckForNull
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
Creates local project descriptor with given project and file
Parameters:
`project` - project for which descriptor is created
`file` - new location for project
Returns:
created project descriptor.
createAnyRemoteProjectDescriptor
@CheckForNullpublic static [ProjectDescriptor](ProjectDescriptor.html) createAnyRemoteProjectDescriptor([Project](../Project.html) project)
Creates remote project descriptor. Supports teamwork and ESI projects
Parameters:
`project` - project for which descriptor is created.
Returns:
null if project is not remote
createAbstractRemoteProjectDescriptorWithActualVersion
@CheckForNullpublic static [AbstractRemoteProjectDescriptor](AbstractRemoteProjectDescriptor.html) createAbstractRemoteProjectDescriptorWithActualVersion([Project](../Project.html) project)
Creates remote project descriptor. Even for latest version uses actual version number instead
 of -1.
Parameters:
`project` - project for which descriptor is created
Returns:
null if project is not remote
constructRemoteURI
@CheckForNullpublic static [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) constructRemoteURI([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 int version)
Creates project URI for remote project and given version.
Parameters:
`id` - remote project id
`qualifiedName` - qualified name - branch (if any) combination with project name
`version` - version number for which descriptor is created. Use -1 for latest version
Returns:
created uri
constructRemoteURI
@CheckForNullpublic static [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) constructRemoteURI([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName)
Creates project URI for remote project.
Parameters:
`id` - remote project id
`qualifiedName` - qualified name - branch (if any) combination with project name
Returns:
created uri
getRemoteVersionAsString
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemoteVersionAsString([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Retrieves remote version from given uri.
Parameters:
`uri` - uri to check
Returns:
version number from uri.
getRemoteVersion
public static int getRemoteVersion([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Deprecated.
use [`getRemoteLongVersion(URI)`](#getRemoteLongVersion(java.net.URI))
Retrieves remote version from given uri.
Parameters:
`uri` - uri to check
Returns:
version number from uri.
getRemoteLongVersion
public static long getRemoteLongVersion([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Retrieves remote version from given uri.
Parameters:
`uri` - uri to check
Returns:
version number from uri.
isAnyRemote
public static boolean isAnyRemote([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Parameters:
`uri` - uri to check.
Returns:
true if uri is remote project descriptor uri
getRemoteID
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemoteID([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Retrieves project id from given uri.
Parameters:
`uri` - remote project uri to check.
Returns:
remote project id from project uri.
getRemoteID
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemoteID([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Retrieves project id from given uri.
Parameters:
`uri` - remote project uri to check.
`separator` - uri info separator
Returns:
remote project id from project uri.
getName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName(@CheckForNull
 [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Retrieves project name from given uri.
Parameters:
`uri` - remote uri to check.
Returns:
remote project name.
getProjectName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getProjectName([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Extract project name from the URI. Name doesn't contain branch name, if such was (remote)
Parameters:
`uri` - uri used to retrieve name.
Returns:
project name
See Also:
[`getName(java.net.URI)`](#getName(java.net.URI))
getProjectFullPath
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getProjectFullPath([URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
Get project branch path (WITH project name) or just project name if branches are not applicable for given uri
Parameters:
`uri` - used to retrieve full path.
Returns:
null if no branch was found
createRemoteProjectDescriptor
@CheckForNullpublic static [ProjectDescriptor](ProjectDescriptor.html) createRemoteProjectDescriptor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) actualVersionNumber)
Creates project descriptor for remote project and given version.
Parameters:
`id` - remote project id.
`qualifiedName` - qualified name - branch (if any) combination with project name.
`actualVersionNumber` - version number for which descriptor is created. Use -1 for latest version.
Returns:
created descriptor.
createRemoteProjectDescriptor
@CheckForNullpublic static [ProjectDescriptor](ProjectDescriptor.html) createRemoteProjectDescriptor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) qualifiedName,
 int actualVersionNumber)
Creates project descriptor for remote project and given version.
Parameters:
`id` - remote project id.
`qualifiedName` - qualified name - branch (if any) combination with project name.
`actualVersionNumber` - version number for which descriptor is created. Use -1 for latest version.
Returns:
created descriptor.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Class ProjectDescriptorsFactory">Class ProjectDescriptorsFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.project.ProjectDescriptorsFactory</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectDescriptorsFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Factory for ProjectDescriptors creating.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectDescriptorsFactory</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#constructRemoteURI(java.lang.String,java.lang.String)">constructRemoteURI</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates project URI for remote project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#constructRemoteURI(java.lang.String,java.lang.String,int)">constructRemoteURI</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 int version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates project URI for remote project and given version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="AbstractRemoteProjectDescriptor.html" title="class in com.nomagic.magicdraw.core.project">AbstractRemoteProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createAbstractRemoteProjectDescriptorWithActualVersion(com.nomagic.magicdraw.core.Project)">createAbstractRemoteProjectDescriptorWithActualVersion</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates remote project descriptor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createAnyRemoteProjectDescriptor(com.nomagic.magicdraw.core.Project)">createAnyRemoteProjectDescriptor</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates remote project descriptor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createLocalProjectDescriptor(com.nomagic.magicdraw.core.Project)">createLocalProjectDescriptor</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates local project descriptor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createLocalProjectDescriptor(com.nomagic.magicdraw.core.Project,java.io.File)">createLocalProjectDescriptor</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates local project descriptor with given project and file</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createProjectDescriptor(java.lang.String)">createProjectDescriptor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#createProjectDescriptor(java.net.URI)"><code>createProjectDescriptor(URI)</code></a>
 Parses location String and creates ProjectDescriptor object from project's location string.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createProjectDescriptor(java.net.URI)">createProjectDescriptor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Parses location String and creates ProjectDescriptor object from project's location string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRemoteProjectDescriptor(java.lang.String,java.lang.String,int)">createRemoteProjectDescriptor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 int actualVersionNumber)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates project descriptor for remote project and given version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRemoteProjectDescriptor(java.lang.String,java.lang.String,java.lang.String)">createRemoteProjectDescriptor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actualVersionNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates project descriptor for remote project and given version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAvailableDescriptorsForProject(com.nomagic.magicdraw.core.Project)">getAvailableDescriptorsForProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all available descriptors for given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescriptorForProject(com.nomagic.magicdraw.core.Project)">getDescriptorForProject</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns project descriptor for given project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getName(java.net.URI)">getName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves project name from given uri.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectFullPath(java.net.URI)">getProjectFullPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get project branch path (WITH project name) or just project name if branches are not applicable for given uri</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectName(java.net.URI)">getProjectName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extract project name from the URI.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteID(java.net.URI)">getRemoteID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves project id from given uri.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteID(java.net.URI,java.lang.String)">getRemoteID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves project id from given uri.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteLongVersion(java.net.URI)">getRemoteLongVersion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves remote version from given uri.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRemoteVersion(java.net.URI)">getRemoteVersion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getRemoteLongVersion(java.net.URI)"><code>getRemoteLongVersion(URI)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteVersionAsString(java.net.URI)">getRemoteVersionAsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves remote version from given uri.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAnyRemote(java.net.URI)">isAnyRemote</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<h3>ProjectDescriptorsFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectDescriptorsFactory</span>()</div>
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
<section class="detail" id="createProjectDescriptor(java.lang.String)">
<h3>createProjectDescriptor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createProjectDescriptor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#createProjectDescriptor(java.net.URI)"><code>createProjectDescriptor(URI)</code></a>
 Parses location String and creates ProjectDescriptor object from project's location string.</div>
</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - the project's location</dd>
<dt>Returns:</dt>
<dd>constructed ProjectDescriptor object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProjectDescriptor(java.net.URI)">
<h3>createProjectDescriptor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createProjectDescriptor</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> location)</span></div>
<div class="block">Parses location String and creates ProjectDescriptor object from project's location string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - the project's location</dd>
<dt>Returns:</dt>
<dd>constructed ProjectDescriptor object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAvailableDescriptorsForProject(com.nomagic.magicdraw.core.Project)">
<h3>getAvailableDescriptorsForProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a>&gt;</span> <span class="element-name">getAvailableDescriptorsForProject</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns all available descriptors for given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project.</dd>
<dt>Returns:</dt>
<dd>List of descriptors.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescriptorForProject(com.nomagic.magicdraw.core.Project)">
<h3>getDescriptorForProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">getDescriptorForProject</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns project descriptor for given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project for which descriptor is created.</dd>
<dt>Returns:</dt>
<dd>Local project descriptor if project is local, remote project descriptor if project is remote.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLocalProjectDescriptor(com.nomagic.magicdraw.core.Project)">
<h3>createLocalProjectDescriptor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createLocalProjectDescriptor</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Creates local project descriptor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project for which descriptor is created.</dd>
<dt>Returns:</dt>
<dd>created project descriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createLocalProjectDescriptor(com.nomagic.magicdraw.core.Project,java.io.File)">
<h3>createLocalProjectDescriptor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createLocalProjectDescriptor</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Creates local project descriptor with given project and file</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project for which descriptor is created</dd>
<dd><code>file</code> - new location for project</dd>
<dt>Returns:</dt>
<dd>created project descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnyRemoteProjectDescriptor(com.nomagic.magicdraw.core.Project)">
<h3>createAnyRemoteProjectDescriptor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createAnyRemoteProjectDescriptor</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Creates remote project descriptor. Supports teamwork and ESI projects</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project for which descriptor is created.</dd>
<dt>Returns:</dt>
<dd>null if project is not remote</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAbstractRemoteProjectDescriptorWithActualVersion(com.nomagic.magicdraw.core.Project)">
<h3>createAbstractRemoteProjectDescriptorWithActualVersion</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="AbstractRemoteProjectDescriptor.html" title="class in com.nomagic.magicdraw.core.project">AbstractRemoteProjectDescriptor</a></span> <span class="element-name">createAbstractRemoteProjectDescriptorWithActualVersion</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Creates remote project descriptor. Even for latest version uses actual version number instead
 of -1.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project for which descriptor is created</dd>
<dt>Returns:</dt>
<dd>null if project is not remote</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="constructRemoteURI(java.lang.String,java.lang.String,int)">
<h3>constructRemoteURI</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></span> <span class="element-name">constructRemoteURI</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 int version)</span></div>
<div class="block">Creates project URI for remote project and given version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - remote project id</dd>
<dd><code>qualifiedName</code> - qualified name - branch (if any) combination with project name</dd>
<dd><code>version</code> - version number for which descriptor is created. Use -1 for latest version</dd>
<dt>Returns:</dt>
<dd>created uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="constructRemoteURI(java.lang.String,java.lang.String)">
<h3>constructRemoteURI</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></span> <span class="element-name">constructRemoteURI</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName)</span></div>
<div class="block">Creates project URI for remote project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - remote project id</dd>
<dd><code>qualifiedName</code> - qualified name - branch (if any) combination with project name</dd>
<dt>Returns:</dt>
<dd>created uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteVersionAsString(java.net.URI)">
<h3>getRemoteVersionAsString</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemoteVersionAsString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Retrieves remote version from given uri.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri to check</dd>
<dt>Returns:</dt>
<dd>version number from uri.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteVersion(java.net.URI)">
<h3>getRemoteVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">getRemoteVersion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getRemoteLongVersion(java.net.URI)"><code>getRemoteLongVersion(URI)</code></a></div>
</div>
<div class="block">Retrieves remote version from given uri.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri to check</dd>
<dt>Returns:</dt>
<dd>version number from uri.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteLongVersion(java.net.URI)">
<h3>getRemoteLongVersion</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">long</span> <span class="element-name">getRemoteLongVersion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Retrieves remote version from given uri.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri to check</dd>
<dt>Returns:</dt>
<dd>version number from uri.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAnyRemote(java.net.URI)">
<h3>isAnyRemote</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAnyRemote</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri to check.</dd>
<dt>Returns:</dt>
<dd>true if uri is remote project descriptor uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteID(java.net.URI)">
<h3>getRemoteID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemoteID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Retrieves project id from given uri.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - remote project uri to check.</dd>
<dt>Returns:</dt>
<dd>remote project id from project uri.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteID(java.net.URI,java.lang.String)">
<h3>getRemoteID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemoteID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="block">Retrieves project id from given uri.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - remote project uri to check.</dd>
<dd><code>separator</code> - uri info separator</dd>
<dt>Returns:</dt>
<dd>remote project id from project uri.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName(java.net.URI)">
<h3>getName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Retrieves project name from given uri.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - remote uri to check.</dd>
<dt>Returns:</dt>
<dd>remote project name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectName(java.net.URI)">
<h3>getProjectName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Extract project name from the URI. Name doesn't contain branch name, if such was (remote)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - uri used to retrieve name.</dd>
<dt>Returns:</dt>
<dd>project name</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getName(java.net.URI)"><code>getName(java.net.URI)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectFullPath(java.net.URI)">
<h3>getProjectFullPath</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectFullPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Get project branch path (WITH project name) or just project name if branches are not applicable for given uri</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - used to retrieve full path.</dd>
<dt>Returns:</dt>
<dd>null if no branch was found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoteProjectDescriptor(java.lang.String,java.lang.String,java.lang.String)">
<h3>createRemoteProjectDescriptor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createRemoteProjectDescriptor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actualVersionNumber)</span></div>
<div class="block">Creates project descriptor for remote project and given version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - remote project id.</dd>
<dd><code>qualifiedName</code> - qualified name - branch (if any) combination with project name.</dd>
<dd><code>actualVersionNumber</code> - version number for which descriptor is created. Use -1 for latest version.</dd>
<dt>Returns:</dt>
<dd>created descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoteProjectDescriptor(java.lang.String,java.lang.String,int)">
<h3>createRemoteProjectDescriptor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></span> <span class="element-name">createRemoteProjectDescriptor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qualifiedName,
 int actualVersionNumber)</span></div>
<div class="block">Creates project descriptor for remote project and given version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - remote project id.</dd>
<dd><code>qualifiedName</code> - qualified name - branch (if any) combination with project name.</dd>
<dd><code>actualVersionNumber</code> - version number for which descriptor is created. Use -1 for latest version.</dd>
<dt>Returns:</dt>
<dd>created descriptor.</dd>
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
