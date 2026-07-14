# JAVA OPENAPI: AbstractRemoteProjectDescriptor (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/project/AbstractRemoteProjectDescriptor.html
- source_path: `com/nomagic/magicdraw/core/project/AbstractRemoteProjectDescriptor.html`
- source_sha256: `378c10a73745e5cdad72aa9ffeec66a9841351429f0f612da0b38c57a080571d`
- captured_utc: `2026-07-14T16:55:13.201985+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Class AbstractRemoteProjectDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.project.AProjectDescriptor
com.nomagic.magicdraw.core.project.AbstractRemoteProjectDescriptor

All Implemented Interfaces:
`[ProjectDescriptor](ProjectDescriptor.html)`

@OpenApipublic abstract classAbstractRemoteProjectDescriptor
extends com.nomagic.magicdraw.core.project.AProjectDescriptor

This class represents location of the remote project.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[AbstractRemoteProjectDescriptor](#%3Cinit%3E(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,java.net.URI))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) scheme,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) teamworkServiceID,
 [Project](../Project.html) project,
 [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLocation](#getLocation())()`

`[Project](../Project.html)`
`[getProject](#getProject())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRepresentationString](#getRepresentationString())()`
Constructs human representation of the project.
`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSeparator](#getSeparator())()`

`com.nomagic.magicdraw.teamwork2.ITeamworkServiceInternal`
`[getTeamworkService](#getTeamworkService())()`

`[URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html)`
`[getURI](#getURI())()`
Returns project location URI.
`int`
`[hashCode](#hashCode())()`

`boolean`
`[isRemote](#isRemote())()`

`static void`
`[loadRemote](#loadRemote(com.nomagic.magicdraw.core.project.AbstractRemoteProjectDescriptor,com.nomagic.task.ProgressStatus))([AbstractRemoteProjectDescriptor](AbstractRemoteProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Load project from given remote descriptor
`static boolean`
`[save](#save(com.nomagic.magicdraw.core.project.AbstractRemoteProjectDescriptor,boolean))([AbstractRemoteProjectDescriptor](AbstractRemoteProjectDescriptor.html) descriptor,
 boolean silent)`
WARNING status is not working properly, for this commit dialog should be refactored.
`protected abstract void`
`[updateOptions](#updateOptions(java.lang.String,java.lang.String,java.lang.String,int,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) host,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) login,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pass,
 int port,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) token)`
Methods inherited from class com.nomagic.magicdraw.core.project.AProjectDescriptor
`load, save`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractRemoteProjectDescriptor
protected AbstractRemoteProjectDescriptor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) scheme,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) teamworkServiceID,
 @CheckForNull
 [Project](../Project.html) project,
 @CheckForNull
 [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) uri)
 throws [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)`
 ============ METHOD DETAIL ========== 
Method Details
getLocation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLocation()
getRepresentationString
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRepresentationString()
Constructs human representation of the project.
Returns:
project's representation as String.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)` - if project isn't specified or loaded.
save
public static boolean save([AbstractRemoteProjectDescriptor](AbstractRemoteProjectDescriptor.html) descriptor,
 boolean silent)
WARNING status is not working properly, for this commit dialog should be refactored.
 WARNING on not silent mode result is always true.
Parameters:
`silent` -
loadRemote
public static void loadRemote([AbstractRemoteProjectDescriptor](AbstractRemoteProjectDescriptor.html) descriptor,
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Load project from given remote descriptor
Parameters:
`descriptor` - remote project descriptor
`status` - progress status
isRemote
public boolean isRemote()
Returns:
true if descriptor points to remote project location.
getURI
public [URI](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html) getURI()
Description copied from interface: `[ProjectDescriptor](ProjectDescriptor.html#getURI())`
Returns project location URI.
 Used only for persistence, not for human representation.
 This location can be used for new descriptors creating in ProjectDescriptorsFactory.
Returns:
project URI.
getProject
@CheckForNullpublic [Project](../Project.html) getProject()
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
updateOptions
protected abstract void updateOptions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) host,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) login,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pass,
 int port,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) token)
getTeamworkService
public com.nomagic.magicdraw.teamwork2.ITeamworkServiceInternal getTeamworkService()
getSeparator
public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSeparator()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Class AbstractRemoteProjectDescriptor">Class AbstractRemoteProjectDescriptor</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.project.AProjectDescriptor
<div class="inheritance">com.nomagic.magicdraw.core.project.AbstractRemoteProjectDescriptor</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ProjectDescriptor.html" title="interface in com.nomagic.magicdraw.core.project">ProjectDescriptor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractRemoteProjectDescriptor</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.project.AProjectDescriptor</span></div>
<div class="block">This class represents location of the remote project.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,java.net.URI)">AbstractRemoteProjectDescriptor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> scheme,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> teamworkServiceID,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocation()">getLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentationString()">getRepresentationString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Constructs human representation of the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSeparator()">getSeparator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.teamwork2.ITeamworkServiceInternal</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTeamworkService()">getTeamworkService</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getURI()">getURI</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project location URI.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemote()">isRemote</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadRemote(com.nomagic.magicdraw.core.project.AbstractRemoteProjectDescriptor,com.nomagic.task.ProgressStatus)">loadRemote</a><wbr/>(<a href="AbstractRemoteProjectDescriptor.html" title="class in com.nomagic.magicdraw.core.project">AbstractRemoteProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load project from given remote descriptor</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#save(com.nomagic.magicdraw.core.project.AbstractRemoteProjectDescriptor,boolean)">save</a><wbr/>(<a href="AbstractRemoteProjectDescriptor.html" title="class in com.nomagic.magicdraw.core.project">AbstractRemoteProjectDescriptor</a> descriptor,
 boolean silent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">WARNING status is not working properly, for this commit dialog should be refactored.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#updateOptions(java.lang.String,java.lang.String,java.lang.String,int,java.lang.String)">updateOptions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> host,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> login,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pass,
 int port,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.AProjectDescriptor">Methods inherited from class com.nomagic.magicdraw.core.project.AProjectDescriptor</h3>
<code>load, save</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,java.net.URI)">
<h3>AbstractRemoteProjectDescriptor</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">AbstractRemoteProjectDescriptor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> scheme,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> teamworkServiceID,
 @CheckForNull
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code></dd>
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
<section class="detail" id="getLocation()">
<h3>getLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLocation</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentationString()">
<h3>getRepresentationString</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentationString</span>()</div>
<div class="block">Constructs human representation of the project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project's representation as String.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if project isn't specified or loaded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="save(com.nomagic.magicdraw.core.project.AbstractRemoteProjectDescriptor,boolean)">
<h3>save</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">save</span><wbr/><span class="parameters">(<a href="AbstractRemoteProjectDescriptor.html" title="class in com.nomagic.magicdraw.core.project">AbstractRemoteProjectDescriptor</a> descriptor,
 boolean silent)</span></div>
<div class="block">WARNING status is not working properly, for this commit dialog should be refactored.
 WARNING on not silent mode result is always true.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>silent</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadRemote(com.nomagic.magicdraw.core.project.AbstractRemoteProjectDescriptor,com.nomagic.task.ProgressStatus)">
<h3>loadRemote</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">loadRemote</span><wbr/><span class="parameters">(<a href="AbstractRemoteProjectDescriptor.html" title="class in com.nomagic.magicdraw.core.project">AbstractRemoteProjectDescriptor</a> descriptor,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Load project from given remote descriptor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - remote project descriptor</dd>
<dd><code>status</code> - progress status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemote()">
<h3>isRemote</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemote</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if descriptor points to remote project location.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getURI()">
<h3>getURI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></span> <span class="element-name">getURI</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProjectDescriptor.html#getURI()">ProjectDescriptor</a></code></span></div>
<div class="block">Returns project location URI.
 Used only for persistence, not for human representation.
 This location can be used for new descriptors creating in ProjectDescriptorsFactory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project URI.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateOptions(java.lang.String,java.lang.String,java.lang.String,int,java.lang.String)">
<h3>updateOptions</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">updateOptions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> host,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> login,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pass,
 int port,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTeamworkService()">
<h3>getTeamworkService</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.teamwork2.ITeamworkServiceInternal</span> <span class="element-name">getTeamworkService</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSeparator()">
<h3>getSeparator</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSeparator</span>()</div>
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
