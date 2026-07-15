# JAVA OPENAPI: ProjectModule (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/magicreport/tools/ProjectModule.html
- source_path: `com/nomagic/magicdraw/magicreport/tools/ProjectModule.html`
- source_sha256: `fe1f4c918c4a2fd8516cd8365b4399ef581ced326d42663635a2fc24f79b7a8a`
- captured_utc: `2026-07-14T16:51:24.305245+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.tools](package-summary.html)

## Class ProjectModule

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.magicreport.tools.ProjectModule

@OpenApiAllpublic classProjectModule
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Wrapper Class of `IAttachedProject`.

Since:
Feb 11, 2019

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectModule](#%3Cinit%3E(com.nomagic.ci.persistence.IAttachedProject))(com.nomagic.ci.persistence.IAttachedProject attachedProject)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equalsIgnoreVersion](#equalsIgnoreVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor))([ProjectDescriptor](../../core/project/ProjectDescriptor.html) module)`

`com.nomagic.ci.persistence.IAttachedProject`
`[getAttachedProject](#getAttachedProject())()`
Get real attached project.
`com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration`
`[getAttachmentConfiguration](#getAttachmentConfiguration())()`
Get attachmentConfiguration of attached project
`[AutoLoadKind](../../core/modules/AutoLoadKind.html)`
`[getAutoLoadType](#getAutoLoadType())()`
Return load kind of attached project
`[Project](../../core/Project.html)`
`[getBelongsTo](#getBelongsTo())()`
Returns MagicDraw project for attached project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`
Get attached project description.
`[XmiExporterDescription](../../../persistence/XmiExporterDescription.html)`
`[getExporterDescription](#getExporterDescription())()`
Provide information about project version and required resources/plugins for attached project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLatestVersion](#getLatestVersion())()`
Get latest version of attached project.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.mounting.IMountPoint>`
`[getMounts](#getMounts())()`
Gets mount points for attached project, i.e.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Get attached project name
`[ProjectOptions](../../core/options/ProjectOptions.html)`
`[getOptions](#getOptions())()`
Get attached project options.
`[ProjectVersion](ProjectVersion.html)`
`[getProjectVersion](#getProjectVersion())()`
Return project version of attached project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRemoteID](#getRemoteID())()`
Return remote id for an attached project
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentationString](#getRepresentationString())()`
Return user friendly representation string about attached project
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRequiredVersion](#getRequiredVersion())()`
Get required version of attached project.
`[StyleManager](../../properties/StyleManager.html)`
`[getStyleManager](#getStyleManager())()`
Style manager of an attached project
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getTags](#getTags())()`
Return a list of version tags.
`[URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html)`
`[getURI](#getURI())()`
Convert EMF uri to java.net.URI
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUsedVersion](#getUsedVersion())()`
Get used version of attached project.
`long`
`[getVersion](#getVersion())()`
Get project version number.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersionList](#getVersionList())()`
Return list of project version of attached project.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersions](#getVersions())()`
Return list of project version of attached project.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)>`
`[getVersions](#getVersions(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sortType)`
Return list of project version of attached project. 

 The result will be sorted by specified sortType.
`boolean`
`[isDirty](#isDirty())()`

`boolean`
`[isEditable](#isEditable())()`
Gets attachment mode
`boolean`
`[isLatest](#isLatest())()`
Return true if the attached project is latest version.
`boolean`
`[isLoaded](#isLoaded())()`
Check if attached project is loaded.
`boolean`
`[isLoadIndex](#isLoadIndex())()`
Check if to load index.
`boolean`
`[isLocked](#isLocked())()`
Check if attached project is loaded from old format file and can not be edited in
 current project.
`boolean`
`[isManualUnloaded](#isManualUnloaded())()`
Load mode of the attached project, loaded manually if true.
`boolean`
`[isRemote](#isRemote())()`
Check if an attached project is remote - from teamwork server or TW Cloud.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectModule
public ProjectModule(com.nomagic.ci.persistence.IAttachedProject attachedProject)
 ============ METHOD DETAIL ========== 
Method Details
getAttachedProject
public com.nomagic.ci.persistence.IAttachedProject getAttachedProject()
Get real attached project.
Returns:
an `IAttachedProject`.
getAttachmentConfiguration
public com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration getAttachmentConfiguration()
Get attachmentConfiguration of attached project
Returns:
an `AbstractProjectAttachmentConfiguration`
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Get attached project name
Returns:
attached project name
isLoaded
public boolean isLoaded()
Check if attached project is loaded.
Returns:
true if attached project is loaded.
getAutoLoadType
public [AutoLoadKind](../../core/modules/AutoLoadKind.html) getAutoLoadType()
Return load kind of attached project
Returns:
load kind
isLoadIndex
public boolean isLoadIndex()
Check if to load index.
Returns:
true if option is set to load index.
isManualUnloaded
public boolean isManualUnloaded()
Load mode of the attached project, loaded manually if true.
Returns:
true if load manually
getMounts
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.ci.persistence.mounting.IMountPoint> getMounts()
Gets mount points for attached project, i.e. returns all mount points that are
 mounted share points of attached project. Returns empty set if there are no
 mount points to return.
Returns:
non-`null` set of `mount points` for specific project
getDescription
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
Get attached project description.
Returns:
attached project description
isLocked
public boolean isLocked()
Check if attached project is loaded from old format file and can not be edited in
 current project.
Returns:
true if attached project is loaded from old format file and can not be edited
 in current project
getUsedVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUsedVersion()
Get used version of attached project.
Returns:
used version
getLatestVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLatestVersion()
Get latest version of attached project.
Returns:
latest version
getVersion
public long getVersion()
Get project version number.
Returns:
version number as long
getRequiredVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRequiredVersion()
Get required version of attached project.
Returns:
required version
isLatest
public boolean isLatest()
Return true if the attached project is latest version.
Returns:
true if the attached project is latest version
equalsIgnoreVersion
public boolean equalsIgnoreVersion([ProjectDescriptor](../../core/project/ProjectDescriptor.html) module)
getTags
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getTags()
Return a list of version tags.
Returns:
tags of the version if any
isEditable
public boolean isEditable()
Gets attachment mode
Returns:
attachment mode
getBelongsTo
public [Project](../../core/Project.html) getBelongsTo()
Returns MagicDraw project for attached project.
Returns:
[`Project`](../../core/Project.html)
getRemoteID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRemoteID()
Return remote id for an attached project
Returns:
remote id
getURI
public [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) getURI()
Convert EMF uri to java.net.URI
Returns:
java net uri
isRemote
public boolean isRemote()
Check if an attached project is remote - from teamwork server or TW Cloud.
Returns:
true if an attached project is from server
getStyleManager
public [StyleManager](../../properties/StyleManager.html) getStyleManager()
Style manager of an attached project
Returns:
style manager in an attached project options
getOptions
public [ProjectOptions](../../core/options/ProjectOptions.html) getOptions()
Get attached project options.
Returns:
attached project options.
isDirty
public boolean isDirty()
getRepresentationString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentationString()
Return user friendly representation string about attached project
Returns:
user friendly representation
getExporterDescription
public [XmiExporterDescription](../../../persistence/XmiExporterDescription.html) getExporterDescription()
Provide information about project version and required resources/plugins for attached project.
Returns:
description of attached project
getProjectVersion
public [ProjectVersion](ProjectVersion.html) getProjectVersion()
Return project version of attached project.
Returns:
a [`ProjectVersion`](ProjectVersion.html) of attached project
getVersionList
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersionList()
Return list of project version of attached project.
Returns:
a list of [`ProjectVersion`](ProjectVersion.html) of attached project
getVersions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersions()
Return list of project version of attached project. 

 The result will be sorted in descending order.
Returns:
a list of [`ProjectVersion`](ProjectVersion.html) of attached project
getVersions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ProjectVersion](ProjectVersion.html)> getVersions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sortType)
Return list of project version of attached project. 

 The result will be sorted by specified sortType.
Parameters:
`sortType` - type of sorting. Specify "desc" sort in descending order. Default is ascending sort.
Returns:
a list of [`ProjectVersion`](ProjectVersion.html) of attached project

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.tools</a></div>
<h1 class="title" title="Class ProjectModule">Class ProjectModule</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.magicreport.tools.ProjectModule</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectModule</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Wrapper Class of <code>IAttachedProject</code>.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Feb 11, 2019</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ci.persistence.IAttachedProject)">ProjectModule</a><wbr/>(com.nomagic.ci.persistence.IAttachedProject attachedProject)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equalsIgnoreVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor)">equalsIgnoreVersion</a><wbr/>(<a href="../../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachedProject()">getAttachedProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get real attached project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttachmentConfiguration()">getAttachmentConfiguration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get attachmentConfiguration of attached project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../core/modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoLoadType()">getAutoLoadType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return load kind of attached project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBelongsTo()">getBelongsTo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns MagicDraw project for attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get attached project description.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExporterDescription()">getExporterDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provide information about project version and required resources/plugins for attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLatestVersion()">getLatestVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get latest version of attached project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMounts()">getMounts</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets mount points for attached project, i.e.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get attached project name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../core/options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get attached project options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectVersion()">getProjectVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return project version of attached project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoteID()">getRemoteID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return remote id for an attached project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentationString()">getRepresentationString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return user friendly representation string about attached project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredVersion()">getRequiredVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get required version of attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyleManager()">getStyleManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Style manager of an attached project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTags()">getTags</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a list of version tags.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getURI()">getURI</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert EMF uri to java.net.URI</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUsedVersion()">getUsedVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get used version of attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion()">getVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get project version number.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersionList()">getVersionList</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return list of project version of attached project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersions()">getVersions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return list of project version of attached project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersions(java.lang.String)">getVersions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sortType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return list of project version of attached project.<br/>
 The result will be sorted by specified sortType.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirty()">isDirty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets attachment mode</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLatest()">isLatest</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return true if the attached project is latest version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoaded()">isLoaded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if attached project is loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoadIndex()">isLoadIndex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if to load index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLocked()">isLocked</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if attached project is loaded from old format file and can not be edited in
 current project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isManualUnloaded()">isManualUnloaded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Load mode of the attached project, loaded manually if true.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemote()">isRemote</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if an attached project is remote - from teamwork server or TW Cloud.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.ci.persistence.IAttachedProject)">
<h3>ProjectModule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectModule</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IAttachedProject attachedProject)</span></div>
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
<section class="detail" id="getAttachedProject()">
<h3>getAttachedProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">getAttachedProject</span>()</div>
<div class="block">Get real attached project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an <code>IAttachedProject</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttachmentConfiguration()">
<h3>getAttachmentConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.ci.persistence.spi.decomposition.AbstractProjectAttachmentConfiguration</span> <span class="element-name">getAttachmentConfiguration</span>()</div>
<div class="block">Get attachmentConfiguration of attached project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an <code>AbstractProjectAttachmentConfiguration</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Get attached project name</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>attached project name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoaded()">
<h3>isLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoaded</span>()</div>
<div class="block">Check if attached project is loaded.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if attached project is loaded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAutoLoadType()">
<h3>getAutoLoadType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../core/modules/AutoLoadKind.html" title="class in com.nomagic.magicdraw.core.modules">AutoLoadKind</a></span> <span class="element-name">getAutoLoadType</span>()</div>
<div class="block">Return load kind of attached project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>load kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoadIndex()">
<h3>isLoadIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoadIndex</span>()</div>
<div class="block">Check if to load index.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if option is set to load index.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isManualUnloaded()">
<h3>isManualUnloaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isManualUnloaded</span>()</div>
<div class="block">Load mode of the attached project, loaded manually if true.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if load manually</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMounts()">
<h3>getMounts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.ci.persistence.mounting.IMountPoint&gt;</span> <span class="element-name">getMounts</span>()</div>
<div class="block">Gets mount points for attached project, i.e. returns all mount points that are
 mounted share points of  attached project. Returns empty set if there are no
 mount points to return.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>non-<code>null</code> set of <code>mount points</code> for specific project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block">Get attached project description.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>attached project description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLocked()">
<h3>isLocked</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLocked</span>()</div>
<div class="block">Check if attached project is loaded from old format file and can not be edited in
 current project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if attached project is loaded from old format file and can not be edited
         in current project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUsedVersion()">
<h3>getUsedVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUsedVersion</span>()</div>
<div class="block">Get used version of attached project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>used version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLatestVersion()">
<h3>getLatestVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLatestVersion</span>()</div>
<div class="block">Get latest version of attached project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>latest version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion()">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getVersion</span>()</div>
<div class="block">Get project version number.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>version number as long</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredVersion()">
<h3>getRequiredVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRequiredVersion</span>()</div>
<div class="block">Get required version of attached project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>required version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLatest()">
<h3>isLatest</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLatest</span>()</div>
<div class="block">Return true if the attached project is latest version.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the attached project is latest version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equalsIgnoreVersion(com.nomagic.magicdraw.core.project.ProjectDescriptor)">
<h3>equalsIgnoreVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equalsIgnoreVersion</span><wbr/><span class="parameters">(<a href="../../core/project/ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a> module)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTags()">
<h3>getTags</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getTags</span>()</div>
<div class="block">Return a list of version tags.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tags of the version if any</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="block">Gets attachment mode</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>attachment mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBelongsTo()">
<h3>getBelongsTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getBelongsTo</span>()</div>
<div class="block">Returns MagicDraw project for attached project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core"><code>Project</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoteID()">
<h3>getRemoteID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRemoteID</span>()</div>
<div class="block">Return remote id for an attached project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>remote id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getURI()">
<h3>getURI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></span> <span class="element-name">getURI</span>()</div>
<div class="block">Convert EMF uri to java.net.URI</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>java net uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemote()">
<h3>isRemote</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemote</span>()</div>
<div class="block">Check if an attached project is remote - from teamwork server or TW Cloud.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if an attached project is from server</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyleManager()">
<h3>getStyleManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></span> <span class="element-name">getStyleManager</span>()</div>
<div class="block">Style manager of an attached project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>style manager in an attached project options</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../core/options/ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a></span> <span class="element-name">getOptions</span>()</div>
<div class="block">Get attached project options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>attached project options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDirty()">
<h3>isDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentationString()">
<h3>getRepresentationString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentationString</span>()</div>
<div class="block">Return user friendly representation string about attached project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user friendly representation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExporterDescription()">
<h3>getExporterDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../persistence/XmiExporterDescription.html" title="class in com.nomagic.persistence">XmiExporterDescription</a></span> <span class="element-name">getExporterDescription</span>()</div>
<div class="block">Provide information about project version and required resources/plugins for attached project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>description of attached project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectVersion()">
<h3>getProjectVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a></span> <span class="element-name">getProjectVersion</span>()</div>
<div class="block">Return project version of attached project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of attached project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersionList()">
<h3>getVersionList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersionList</span>()</div>
<div class="block">Return list of project version of attached project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of attached project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions()">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersions</span>()</div>
<div class="block">Return list of project version of attached project. <br/>
 The result will be sorted in descending order.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a list of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of attached project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersions(java.lang.String)">
<h3>getVersions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectVersion</a>&gt;</span> <span class="element-name">getVersions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sortType)</span></div>
<div class="block">Return list of project version of attached project.<br/>
 The result will be sorted by specified sortType.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortType</code> - type of sorting. Specify "desc" sort in descending order. Default is ascending sort.</dd>
<dt>Returns:</dt>
<dd>a list of <a href="ProjectVersion.html" title="class in com.nomagic.magicdraw.magicreport.tools"><code>ProjectVersion</code></a> of attached project</dd>
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
