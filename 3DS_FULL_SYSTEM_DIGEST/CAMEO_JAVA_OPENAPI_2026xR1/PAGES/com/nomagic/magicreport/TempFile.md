# JAVA OPENAPI: TempFile (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/TempFile.html
- source_path: `com/nomagic/magicreport/TempFile.html`
- source_sha256: `115d81b208f4faf587711a6a635cff791caedf5a64a8dfe3ce1cffd41fa4eebe`
- captured_utc: `2026-07-14T16:46:11.634955+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class TempFile

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.io.File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)
com.nomagic.magicreport.TempFile

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)<[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)>`

@OpenApiAllpublic classTempFile
extends [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)

Temporary file.
 When we create a file on temporary directory, it may need to be deleted after executed.

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.magicreport.TempFile)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class java.io.[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)
`[pathSeparator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#pathSeparator), [pathSeparatorChar](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#pathSeparatorChar), [separator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#separator), [separatorChar](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#separatorChar)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TempFile](#%3Cinit%3E(java.io.File,java.lang.String))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) parent,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) child)`
Constructor. 

 Creates a new File instance from a parent abstract pathname and a child pathname string.
`[TempFile](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pathname)`
Constructor. 

 Creates a new File instance by converting the given pathname string into an abstract pathname.
`[TempFile](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) parent,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) child)`
Constructor. 

 Creates a new File instance from a parent pathname string and a child pathname string.
`[TempFile](#%3Cinit%3E(java.net.URI))([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri)`
Constructor. 

 Creates a new File instance by converting the given file: URI into an abstract pathname.
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.io.[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)
`[canExecute](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#canExecute()), [canRead](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#canRead()), [canWrite](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#canWrite()), [compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#compareTo(java.io.File)), [createNewFile](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#createNewFile()), [createTempFile](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#createTempFile(java.lang.String,java.lang.String)), [createTempFile](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#createTempFile(java.lang.String,java.lang.String,java.io.File)), [delete](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#delete()), [deleteOnExit](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#deleteOnExit()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#equals(java.lang.Object)), [exists](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#exists()), [getAbsoluteFile](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getAbsoluteFile()), [getAbsolutePath](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getAbsolutePath()), [getCanonicalFile](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getCanonicalFile()), [getCanonicalPath](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getCanonicalPath()), [getFreeSpace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getFreeSpace()), [getName](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getName()), [getParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getParent()), [getParentFile](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getParentFile()), [getPath](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getPath()), [getTotalSpace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getTotalSpace()), [getUsableSpace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getUsableSpace()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#hashCode()), [isAbsolute](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#isAbsolute()), [isDirectory](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#isDirectory()), [isFile](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#isFile()), [isHidden](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#isHidden()), [lastModified](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#lastModified()), [length](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#length()), [list](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#list()), [list](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#list(java.io.FilenameFilter)), [listFiles](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#listFiles()), [listFiles](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#listFiles(java.io.FileFilter)), [listFiles](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#listFiles(java.io.FilenameFilter)), [listRoots](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#listRoots()), [mkdir](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#mkdir()), [mkdirs](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#mkdirs()), [renameTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#renameTo(java.io.File)), [setExecutable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setExecutable(boolean)), [setExecutable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setExecutable(boolean,boolean)), [setLastModified](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setLastModified(long)), [setReadable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setReadable(boolean)), [setReadable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setReadable(boolean,boolean)), [setReadOnly](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setReadOnly()), [setWritable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setWritable(boolean)), [setWritable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setWritable(boolean,boolean)), [toPath](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#toPath()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#toString()), [toURI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#toURI()), [toURL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#toURL())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TempFile
public TempFile([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pathname)
Constructor. 

 Creates a new File instance by converting the given pathname string into an abstract pathname.
Parameters:
`pathname` - A pathname string
TempFile
public TempFile([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) parent,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) child)
Constructor. 

 Creates a new File instance from a parent abstract pathname and a child pathname string.
Parameters:
`parent` - The parent abstract pathname
`child` - The child pathname string
TempFile
public TempFile([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) parent,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) child)
Constructor. 

 Creates a new File instance from a parent pathname string and a child pathname string.
Parameters:
`parent` - The parent pathname string
`child` - The child pathname string
TempFile
public TempFile([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri)
Constructor. 

 Creates a new File instance by converting the given file: URI into an abstract pathname.
Parameters:
`uri` - An absolute, hierarchical URI with a scheme equal to "file", a non-empty path component, and undefined authority, query, and fragment components

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class TempFile">Class TempFile</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">java.io.File</a>
<div class="inheritance">com.nomagic.magicreport.TempFile</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TempFile</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span></div>
<div class="block">Temporary file.
 When we create a file on temporary directory, it may need to be deleted after executed.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.magicreport.TempFile">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.io.File">Fields inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#pathSeparator" title="class or interface in java.io">pathSeparator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#pathSeparatorChar" title="class or interface in java.io">pathSeparatorChar</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#separator" title="class or interface in java.io">separator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#separatorChar" title="class or interface in java.io">separatorChar</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.File,java.lang.String)">TempFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> child)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.<br/>
 Creates a new File instance from a parent abstract pathname and a child pathname string.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">TempFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathname)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.<br/>
 Creates a new File instance by converting the given pathname string into an abstract pathname.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">TempFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> child)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.<br/>
 Creates a new File instance from a parent pathname string and a child pathname string.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.net.URI)">TempFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.<br/>
 Creates a new File instance by converting the given file: URI into an abstract pathname.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.io.File">Methods inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#canExecute()" title="class or interface in java.io">canExecute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#canRead()" title="class or interface in java.io">canRead</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#canWrite()" title="class or interface in java.io">canWrite</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#compareTo(java.io.File)" title="class or interface in java.io">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#createNewFile()" title="class or interface in java.io">createNewFile</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#createTempFile(java.lang.String,java.lang.String)" title="class or interface in java.io">createTempFile</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#createTempFile(java.lang.String,java.lang.String,java.io.File)" title="class or interface in java.io">createTempFile</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#delete()" title="class or interface in java.io">delete</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#deleteOnExit()" title="class or interface in java.io">deleteOnExit</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#equals(java.lang.Object)" title="class or interface in java.io">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#exists()" title="class or interface in java.io">exists</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getAbsoluteFile()" title="class or interface in java.io">getAbsoluteFile</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getAbsolutePath()" title="class or interface in java.io">getAbsolutePath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getCanonicalFile()" title="class or interface in java.io">getCanonicalFile</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getCanonicalPath()" title="class or interface in java.io">getCanonicalPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getFreeSpace()" title="class or interface in java.io">getFreeSpace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getName()" title="class or interface in java.io">getName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getParent()" title="class or interface in java.io">getParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getParentFile()" title="class or interface in java.io">getParentFile</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getPath()" title="class or interface in java.io">getPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getTotalSpace()" title="class or interface in java.io">getTotalSpace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#getUsableSpace()" title="class or interface in java.io">getUsableSpace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#hashCode()" title="class or interface in java.io">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#isAbsolute()" title="class or interface in java.io">isAbsolute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#isDirectory()" title="class or interface in java.io">isDirectory</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#isFile()" title="class or interface in java.io">isFile</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#isHidden()" title="class or interface in java.io">isHidden</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#lastModified()" title="class or interface in java.io">lastModified</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#length()" title="class or interface in java.io">length</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#list()" title="class or interface in java.io">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#list(java.io.FilenameFilter)" title="class or interface in java.io">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#listFiles()" title="class or interface in java.io">listFiles</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#listFiles(java.io.FileFilter)" title="class or interface in java.io">listFiles</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#listFiles(java.io.FilenameFilter)" title="class or interface in java.io">listFiles</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#listRoots()" title="class or interface in java.io">listRoots</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#mkdir()" title="class or interface in java.io">mkdir</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#mkdirs()" title="class or interface in java.io">mkdirs</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#renameTo(java.io.File)" title="class or interface in java.io">renameTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setExecutable(boolean)" title="class or interface in java.io">setExecutable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setExecutable(boolean,boolean)" title="class or interface in java.io">setExecutable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setLastModified(long)" title="class or interface in java.io">setLastModified</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setReadable(boolean)" title="class or interface in java.io">setReadable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setReadable(boolean,boolean)" title="class or interface in java.io">setReadable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setReadOnly()" title="class or interface in java.io">setReadOnly</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setWritable(boolean)" title="class or interface in java.io">setWritable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#setWritable(boolean,boolean)" title="class or interface in java.io">setWritable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#toPath()" title="class or interface in java.io">toPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#toString()" title="class or interface in java.io">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#toURI()" title="class or interface in java.io">toURI</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html#toURL()" title="class or interface in java.io">toURL</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>TempFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TempFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathname)</span></div>
<div class="block">Constructor.<br/>
 Creates a new File instance by converting the given pathname string into an abstract pathname.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathname</code> - A pathname string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.io.File,java.lang.String)">
<h3>TempFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TempFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> child)</span></div>
<div class="block">Constructor.<br/>
 Creates a new File instance from a parent abstract pathname and a child pathname string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - The parent abstract pathname</dd>
<dd><code>child</code> - The child pathname string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>TempFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TempFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> child)</span></div>
<div class="block">Constructor.<br/>
 Creates a new File instance from a parent pathname string and a child pathname string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - The parent pathname string</dd>
<dd><code>child</code> - The child pathname string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.net.URI)">
<h3>TempFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TempFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Constructor.<br/>
 Creates a new File instance by converting the given file: URI into an abstract pathname.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - An absolute, hierarchical URI with a scheme equal to "file", a non-empty path component, and undefined authority, query, and fragment components</dd>
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
