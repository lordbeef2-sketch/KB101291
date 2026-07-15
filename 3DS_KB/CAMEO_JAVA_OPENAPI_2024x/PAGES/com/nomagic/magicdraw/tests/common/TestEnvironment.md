# JAVA OPENAPI: TestEnvironment (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/tests/common/TestEnvironment.html
- source_path: `com/nomagic/magicdraw/tests/common/TestEnvironment.html`
- source_sha256: `e588ab7c703b4d5076910a7db1f22ecd44ad6fbd3f043cdcda0ab85c159c0600`
- captured_utc: `2026-07-14T16:51:48.830571+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests.common](package-summary.html)

## Class TestEnvironment

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.tests.common.TestEnvironment

@OpenApipublic classTestEnvironment
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The class which is used for initializing the MagicDraw test environment(starting the MagicDraw and specifying the necessary variables).

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[TestEnvironment.ProjectFilenameFilter](TestEnvironment.ProjectFilenameFilter.html)`
File name filter to filter MagicDraw loadable files (mdzip, mdxml, zip.xml, and etc).
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[createFileNameWithPrefix](#createFileNameWithPrefix(java.io.File,java.lang.String))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix)`
Insert specific prefix after file name before file extension.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)>`
`[getFiles](#getFiles(java.io.File,java.io.FilenameFilter,java.util.Collection))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) rootDirectory,
 [FilenameFilter](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FilenameFilter.html) filter,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> skipNames)`
Collects files from root directory and inner directories recursively except those specified to skip.
`static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getFileWithExtension](#getFileWithExtension(java.io.File,java.lang.String))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension)`
Replace MagicDraw project file extension by the given one.
`static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getOutputDir](#getOutputDir(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz)`
Get default directory for specific test case output.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)>`
`[getProjects](#getProjects(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) rootDirectory)`
Collects MagicDraw project files from specific directory and from its inner directories recursively.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)>`
`[getProjects](#getProjects(java.io.File,java.util.Collection))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) rootDirectory,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> skipNames)`
Collects MagicDraw projects files from root directory and inner directories recursively except those specified
 to skip.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)>`
`[getProjects](#getProjects(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) directory)`
Collects MagicDraw projects recursively from the given directory of resource directory.
`static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getRelativeOutputFile](#getRelativeOutputFile(java.lang.Class,java.io.File))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) resourceFile)`
Creates output file relative to given resource file in specific test case output directory.
`static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getResourceDir](#getResourceDir())()`
Returns test framework resources directory specified by "tests.resources" system property.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[splitFileName](#splitFileName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)`
Splits MagicDraw project file name to file name and extension.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getResourceDir
@OpenApipublic static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getResourceDir()
Returns test framework resources directory specified by "tests.resources" system property.
 Resources directory is a central place for all resources required by test cases.
Returns:
File representing test framework resources directory.
getRelativeOutputFile
@OpenApipublic static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getRelativeOutputFile([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) resourceFile)
Creates output file relative to given resource file in specific test case output directory.
Parameters:
`clazz` - test case class to create related output file for.
`resourceFile` - resource file to create related output file for.
Returns:
output file in given test case output directory with name related to given resource file.
getOutputDir
@OpenApipublic static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getOutputDir([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz)
Get default directory for specific test case output. Output directory is created if it does not exist.
 Output directory is located in parent directory if specified by "tests.output" system property or
 MagicDraw install root otherwise.
Parameters:
`clazz` - Test case class to get output directory for.
Returns:
File representing output directory for test case.
getProjects
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> getProjects([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) rootDirectory)
Collects MagicDraw project files from specific directory and from its inner directories recursively.
Parameters:
`rootDirectory` - Root directory to collect project files recursively from.
Returns:
List of MagicDraw projects Files.
createFileNameWithPrefix
@OpenApipublic static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) createFileNameWithPrefix([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) prefix)
Insert specific prefix after file name before file extension. For instance my_projectPREFIX.mdzip.
Parameters:
`file` - file to insert prefix to.
`prefix` - prefix to insert.
Returns:
File representing new file there name has prefix inserted.
getFileWithExtension
@OpenApipublic static [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getFileWithExtension([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension)
Replace MagicDraw project file extension by the given one.
Parameters:
`file` - File to replace extension.
`extension` - new extension.
Returns:
new File with replaced given extension.
getFiles
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> getFiles([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) rootDirectory,
 [FilenameFilter](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FilenameFilter.html) filter,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> skipNames)
Collects files from root directory and inner directories recursively except those specified to skip.
 Files needed to skip might be also listed in skip.txt file located in root or nested directories.
Parameters:
`rootDirectory` - Root directory to collect project files recursively from.
`filter` - only files matching this filter will be returned
`skipNames` - the Collection of project file names to skip. Project file is skipped if it
 name contains any name defined in skipNames collection or skip.txt file.
Returns:
The list of MagicDraw project files collected.
getProjects
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> getProjects([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) rootDirectory,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> skipNames)
Collects MagicDraw projects files from root directory and inner directories recursively except those specified
 to skip. Projects needed to skip might be also listed in skip.txt file located in root or nested directories.
Parameters:
`rootDirectory` - Root directory to collect project files recursively from.
`skipNames` - the Collection of project file names to skip. Project file is skipped if it
 name contains any name defined in skipNames collection or skip.txt file.
Returns:
The list of MagicDraw project files collected.
getProjects
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> getProjects([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) directory)
Collects MagicDraw projects recursively from the given directory of resource directory.
Parameters:
`directory` - directory name in the resource directory
Returns:
List of MagicDraw project files found in the given resource directory and its nested directories.
splitFileName
@CheckForNull
@OpenApipublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] splitFileName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)
Splits MagicDraw project file name to file name and extension.
Parameters:
`fileName` - MagicDraw project file name to split.
Returns:
String[2] = {fileName, fileExtension}

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests.common</a></div>
<h1 class="title" title="Class TestEnvironment">Class TestEnvironment</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.tests.common.TestEnvironment</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TestEnvironment</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The class which is used for initializing the MagicDraw test environment(starting the MagicDraw and specifying the necessary variables).</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="TestEnvironment.ProjectFilenameFilter.html" title="class in com.nomagic.magicdraw.tests.common">TestEnvironment.ProjectFilenameFilter</a></code></div>
<div class="col-last even-row-color">
<div class="block">File name filter to filter MagicDraw loadable files (mdzip, mdxml, zip.xml, and etc).</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createFileNameWithPrefix(java.io.File,java.lang.String)">createFileNameWithPrefix</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Insert specific prefix after file name before file extension.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFiles(java.io.File,java.io.FilenameFilter,java.util.Collection)">getFiles</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> rootDirectory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FilenameFilter.html" title="class or interface in java.io">FilenameFilter</a> filter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; skipNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects files from root directory and inner directories recursively except those specified to skip.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileWithExtension(java.io.File,java.lang.String)">getFileWithExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replace MagicDraw project file extension by the given one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutputDir(java.lang.Class)">getOutputDir</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get default directory for specific test case output.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjects(java.io.File)">getProjects</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> rootDirectory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects MagicDraw project files from specific directory and from its inner directories recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjects(java.io.File,java.util.Collection)">getProjects</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> rootDirectory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; skipNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects MagicDraw projects files from root directory and inner directories recursively except those specified
 to skip.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjects(java.lang.String)">getProjects</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects MagicDraw projects recursively from the given directory of resource directory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelativeOutputFile(java.lang.Class,java.io.File)">getRelativeOutputFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> resourceFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates output file relative to given resource file in specific test case output directory.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceDir()">getResourceDir</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns test framework resources directory specified by "tests.resources" system property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#splitFileName(java.lang.String)">splitFileName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Splits  MagicDraw project file name to file name and extension.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getResourceDir()">
<h3>getResourceDir</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getResourceDir</span>()</div>
<div class="block">Returns test framework resources directory specified by "tests.resources" system property.
 Resources directory is a central place for all resources required by test cases.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>File representing test framework resources directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelativeOutputFile(java.lang.Class,java.io.File)">
<h3>getRelativeOutputFile</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getRelativeOutputFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> resourceFile)</span></div>
<div class="block">Creates output file relative to given resource file in specific test case output directory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - test case class to create related output file for.</dd>
<dd><code>resourceFile</code> - resource file to create related output file for.</dd>
<dt>Returns:</dt>
<dd>output file in given test case output directory with name related to given resource file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutputDir(java.lang.Class)">
<h3>getOutputDir</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getOutputDir</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz)</span></div>
<div class="block">Get default directory for specific test case output. Output directory is created if it does not exist.
 Output directory is located in parent directory if specified by "tests.output" system property or
 MagicDraw install root otherwise.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - Test case class to get output directory for.</dd>
<dt>Returns:</dt>
<dd>File representing output directory for test case.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjects(java.io.File)">
<h3>getProjects</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</span> <span class="element-name">getProjects</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> rootDirectory)</span></div>
<div class="block">Collects MagicDraw project files from specific directory and from its inner directories recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rootDirectory</code> - Root directory to collect project files recursively from.</dd>
<dt>Returns:</dt>
<dd>List of MagicDraw projects Files.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createFileNameWithPrefix(java.io.File,java.lang.String)">
<h3>createFileNameWithPrefix</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">createFileNameWithPrefix</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix)</span></div>
<div class="block">Insert specific prefix after file name before file extension. For instance my_projectPREFIX.mdzip.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - file to insert prefix to.</dd>
<dd><code>prefix</code> - prefix to insert.</dd>
<dt>Returns:</dt>
<dd>File representing new file there name has prefix inserted.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileWithExtension(java.io.File,java.lang.String)">
<h3>getFileWithExtension</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getFileWithExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</span></div>
<div class="block">Replace MagicDraw project file extension by the given one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - File to replace extension.</dd>
<dd><code>extension</code> - new extension.</dd>
<dt>Returns:</dt>
<dd>new File with replaced given extension.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFiles(java.io.File,java.io.FilenameFilter,java.util.Collection)">
<h3>getFiles</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</span> <span class="element-name">getFiles</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> rootDirectory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/FilenameFilter.html" title="class or interface in java.io">FilenameFilter</a> filter,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; skipNames)</span></div>
<div class="block">Collects files from root directory and inner directories recursively except those specified to skip.
 Files needed to skip might be also listed in skip.txt file located in root or nested directories.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rootDirectory</code> - Root directory to collect project files recursively from.</dd>
<dd><code>filter</code> - only files matching this filter will be returned</dd>
<dd><code>skipNames</code> - the Collection of project file names to skip. Project file is skipped if it
                      name contains any name defined in skipNames collection or skip.txt file.</dd>
<dt>Returns:</dt>
<dd>The list of MagicDraw project files collected.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjects(java.io.File,java.util.Collection)">
<h3>getProjects</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</span> <span class="element-name">getProjects</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> rootDirectory,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; skipNames)</span></div>
<div class="block">Collects MagicDraw projects files from root directory and inner directories recursively except those specified
 to skip. Projects needed to skip might be also listed in skip.txt file located in root or nested directories.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rootDirectory</code> - Root directory to collect project files recursively from.</dd>
<dd><code>skipNames</code> - the Collection of project file names to skip. Project file is skipped if it
                      name contains any name defined in skipNames collection or skip.txt file.</dd>
<dt>Returns:</dt>
<dd>The list of MagicDraw project files collected.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjects(java.lang.String)">
<h3>getProjects</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</span> <span class="element-name">getProjects</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory)</span></div>
<div class="block">Collects MagicDraw projects recursively from the given directory of resource directory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>directory</code> - directory name in the resource directory</dd>
<dt>Returns:</dt>
<dd>List of MagicDraw project files found in the given resource directory and its nested directories.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="splitFileName(java.lang.String)">
<h3>splitFileName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">splitFileName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</span></div>
<div class="block">Splits  MagicDraw project file name to file name and extension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - MagicDraw project file name to split.</dd>
<dt>Returns:</dt>
<dd>String[2] = {fileName, fileExtension}</dd>
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
