# JAVA OPENAPI: ProjectVersion (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/teamwork2/ProjectVersion.html
- source_path: `com/nomagic/magicdraw/teamwork2/ProjectVersion.html`
- source_sha256: `f9ca2e3ac2fe4da7d824bc841bbf2d04af46273ae862094a157bc4862e372c5f`
- captured_utc: `2026-07-14T16:51:46.195534+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.teamwork2](package-summary.html)

## Class ProjectVersion

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.teamwork2.ProjectVersion

All Implemented Interfaces:
`com.nomagic.ci.persistence.versioning.IVersionDescriptor`

@OpenApiAllpublic classProjectVersion
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements com.nomagic.ci.persistence.versioning.IVersionDescriptor

Project version information

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectVersion](#%3Cinit%3E(com.nomagic.ci.persistence.versioning.IVersionDescriptor))(com.nomagic.ci.persistence.versioning.IVersionDescriptor v)`
Constructs a version from version descriptor
`[ProjectVersion](#%3Cinit%3E(java.lang.String,long,java.util.Date,java.lang.String,java.util.List,long))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) user,
 long number,
 [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) date,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) comment,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> tags,
 long revertedVersion)`
Constructs new version with given user, number and date.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAuthor](#getAuthor())()`
Returns the user who created the version.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getComment](#getComment())()`

`[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)`
`[getDate](#getDate())()`
Returns the date of the version.
`long`
`[getLongNumber](#getLongNumber())()`
Returns the number of the version.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRevertedVersion](#getRevertedVersion())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getTags](#getTags())()`

`void`
`[setAuthor](#setAuthor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) user)`
Sets user for the version
`void`
`[setComment](#setComment(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) com)`
Sets comment text.
`void`
`[setDate](#setDate(java.util.Date))([Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) date)`
Sets version date.
`void`
`[setLongNumber](#setLongNumber(long))(long number)`
Sets version number
`void`
`[setLongRevertedVersion](#setLongRevertedVersion(long))(long revertedVersion)`

`void`
`[setTags](#setTags(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> tags)`
Sets tags.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectVersion
public ProjectVersion(com.nomagic.ci.persistence.versioning.IVersionDescriptor v)
Constructs a version from version descriptor
Parameters:
`v` - version
ProjectVersion
public ProjectVersion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) user,
 long number,
 [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) date,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) comment,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> tags,
 long revertedVersion)
Constructs new version with given user, number and date.
Parameters:
`user` - the user login name.
`number` - the version number.
`date` - the date when this version was created.
`comment` - the comment text.
`tags` - tags
`revertedVersion` - reverted version
 ============ METHOD DETAIL ========== 
Method Details
getDate
public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) getDate()
Returns the date of the version.
Specified by:
`getDate` in interface `com.nomagic.ci.persistence.versioning.IVersionDescriptor`
Returns:
the date.
setDate
public void setDate([Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) date)
Sets version date.
Parameters:
`date` - date
getLongNumber
public long getLongNumber()
Returns the number of the version.
Returns:
the number.
setLongNumber
public void setLongNumber(long number)
Sets version number
Parameters:
`number` - number
getAuthor
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAuthor()
Returns the user who created the version.
Specified by:
`getAuthor` in interface `com.nomagic.ci.persistence.versioning.IVersionDescriptor`
Returns:
the user who created the version.
setAuthor
public void setAuthor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) user)
Sets user for the version
Parameters:
`user` - user
getComment
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getComment()
Specified by:
`getComment` in interface `com.nomagic.ci.persistence.versioning.IVersionDescriptor`
Returns:
comment for this version.
setComment
public void setComment([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) com)
Sets comment text.
Parameters:
`com` - the comment text.
getTags
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getTags()
Returns:
all tags.
setTags
public void setTags([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> tags)
Sets tags.
Parameters:
`tags` - tags
getRevertedVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRevertedVersion()
Specified by:
`getRevertedVersion` in interface `com.nomagic.ci.persistence.versioning.IVersionDescriptor`
setLongRevertedVersion
public void setLongRevertedVersion(long revertedVersion)
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Specified by:
`getName` in interface `com.nomagic.ci.persistence.versioning.IVersionDescriptor`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.teamwork2</a></div>
<h1 class="title" title="Class ProjectVersion">Class ProjectVersion</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.teamwork2.ProjectVersion</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectVersion</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements com.nomagic.ci.persistence.versioning.IVersionDescriptor</span></div>
<div class="block">Project version information</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ci.persistence.versioning.IVersionDescriptor)">ProjectVersion</a><wbr/>(com.nomagic.ci.persistence.versioning.IVersionDescriptor v)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a version from version descriptor</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,long,java.util.Date,java.lang.String,java.util.List,long)">ProjectVersion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user,
 long number,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> date,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 long revertedVersion)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs new version with given user, number and date.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAuthor()">getAuthor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the user who created the version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getComment()">getComment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDate()">getDate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the date of the version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLongNumber()">getLongNumber</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the number of the version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRevertedVersion()">getRevertedVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTags()">getTags</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAuthor(java.lang.String)">setAuthor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets user for the version</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setComment(java.lang.String)">setComment</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> com)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets comment text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDate(java.util.Date)">setDate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> date)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets version date.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLongNumber(long)">setLongNumber</a><wbr/>(long number)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets version number</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLongRevertedVersion(long)">setLongRevertedVersion</a><wbr/>(long revertedVersion)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTags(java.util.List)">setTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets tags.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.ci.persistence.versioning.IVersionDescriptor)">
<h3>ProjectVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectVersion</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.versioning.IVersionDescriptor v)</span></div>
<div class="block">Constructs a version from version descriptor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,long,java.util.Date,java.lang.String,java.util.List,long)">
<h3>ProjectVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectVersion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user,
 long number,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> date,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> comment,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags,
 long revertedVersion)</span></div>
<div class="block">Constructs new version with given user, number and date.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>user</code> - the user login name.</dd>
<dd><code>number</code> - the version number.</dd>
<dd><code>date</code> - the date when this version was created.</dd>
<dd><code>comment</code> - the comment text.</dd>
<dd><code>tags</code> - tags</dd>
<dd><code>revertedVersion</code> - reverted version</dd>
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
<section class="detail" id="getDate()">
<h3>getDate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">getDate</span>()</div>
<div class="block">Returns the date of the version.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getDate</code> in interface <code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></dd>
<dt>Returns:</dt>
<dd>the date.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDate(java.util.Date)">
<h3>setDate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> date)</span></div>
<div class="block">Sets version date.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>date</code> - date</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLongNumber()">
<h3>getLongNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getLongNumber</span>()</div>
<div class="block">Returns the number of the version.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the number.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLongNumber(long)">
<h3>setLongNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLongNumber</span><wbr/><span class="parameters">(long number)</span></div>
<div class="block">Sets version number</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>number</code> - number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAuthor()">
<h3>getAuthor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAuthor</span>()</div>
<div class="block">Returns the user who created the version.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getAuthor</code> in interface <code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></dd>
<dt>Returns:</dt>
<dd>the user who created the version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAuthor(java.lang.String)">
<h3>setAuthor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAuthor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</span></div>
<div class="block">Sets user for the version</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>user</code> - user</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getComment()">
<h3>getComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getComment</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getComment</code> in interface <code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></dd>
<dt>Returns:</dt>
<dd>comment for this version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setComment(java.lang.String)">
<h3>setComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setComment</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> com)</span></div>
<div class="block">Sets comment text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>com</code> - the comment text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTags()">
<h3>getTags</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getTags</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all tags.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTags(java.util.List)">
<h3>setTags</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; tags)</span></div>
<div class="block">Sets tags.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tags</code> - tags</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRevertedVersion()">
<h3>getRevertedVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRevertedVersion</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getRevertedVersion</code> in interface <code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLongRevertedVersion(long)">
<h3>setLongRevertedVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLongRevertedVersion</span><wbr/><span class="parameters">(long revertedVersion)</span></div>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getName</code> in interface <code>com.nomagic.ci.persistence.versioning.IVersionDescriptor</code></dd>
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
