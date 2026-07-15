# JAVA OPENAPI: ExtensionClassLoader (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/ExtensionClassLoader.html
- source_path: `com/nomagic/magicreport/ExtensionClassLoader.html`
- source_sha256: `abd2903f94a5a4f2beb1abe9fedba2a60b234f2b284f49731cd0a6259bba2a62`
- captured_utc: `2026-07-14T16:58:36.588274+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class ExtensionClassLoader

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.lang.ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)
com.nomagic.magicreport.ExtensionClassLoader

@OpenApiAllpublic classExtensionClassLoader
extends [ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)

This class loader is used to provide class loader for MagicReport extension. This loader will load classes and
 resources from a search URLs referring to JAR files and prevent resource locking from class loader.

Since:
Mar 28, 2008

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ExtensionClassLoader](#%3Cinit%3E(java.net.URL))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)`
Constructs a new URLClassLoader for the specified URL using the system class loader as parent
 `ClassLoader`.
`[ExtensionClassLoader](#%3Cinit%3E(java.net.URL%5B%5D))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)[] urls)`
Constructs a new URLClassLoader for the specified URLs using the system class loader as parent
 `ClassLoader`.
`[ExtensionClassLoader](#%3Cinit%3E(java.net.URL%5B%5D,java.lang.ClassLoader))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)[] urls,
 [ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) parent)`
Constructs a new ExtensionClassLoader for the given URLs.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addOtherClassLoader](#addOtherClassLoader(java.lang.ClassLoader))([ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) otherClassLoader)`
Add other class loader
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)>`
`[getOtherClassLoaders](#getOtherClassLoaders())()`
Return other class loaders for delegation
`[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)`
`[getParentClassLoader](#getParentClassLoader())()`
Return parent class loader for delegation
`[URLClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URLClassLoader.html)`
`[getURLClassLoader](#getURLClassLoader())()`
Return url class loader
`[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?>`
`[loadClass](#loadClass(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`

`protected [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?>`
`[loadClass](#loadClass(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean resolve)`

`void`
`[setOtherClassLoader](#setOtherClassLoader(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)> otherClassLoaders)`
Set other class loaders for delegation
Methods inherited from class java.lang.[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)
`[clearAssertionStatus](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#clearAssertionStatus()), [defineClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#defineClass(byte%5B%5D,int,int)), [defineClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#defineClass(java.lang.String,byte%5B%5D,int,int)), [defineClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#defineClass(java.lang.String,byte%5B%5D,int,int,java.security.ProtectionDomain)), [defineClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#defineClass(java.lang.String,java.nio.ByteBuffer,java.security.ProtectionDomain)), [definePackage](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#definePackage(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.net.URL)), [findClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findClass(java.lang.String)), [findClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findClass(java.lang.String,java.lang.String)), [findLibrary](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findLibrary(java.lang.String)), [findLoadedClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findLoadedClass(java.lang.String)), [findResource](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findResource(java.lang.String)), [findResource](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findResource(java.lang.String,java.lang.String)), [findResources](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findResources(java.lang.String)), [findSystemClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findSystemClass(java.lang.String)), [getClassLoadingLock](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getClassLoadingLock(java.lang.String)), [getDefinedPackage](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getDefinedPackage(java.lang.String)), [getDefinedPackages](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getDefinedPackages()), [getName](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getName()), [getPackage](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getPackage(java.lang.String)), [getPackages](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getPackages()), [getParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getParent()), [getPlatformClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getPlatformClassLoader()), [getResource](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getResource(java.lang.String)), [getResourceAsStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getResourceAsStream(java.lang.String)), [getResources](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getResources(java.lang.String)), [getSystemClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getSystemClassLoader()), [getSystemResource](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getSystemResource(java.lang.String)), [getSystemResourceAsStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getSystemResourceAsStream(java.lang.String)), [getSystemResources](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getSystemResources(java.lang.String)), [getUnnamedModule](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getUnnamedModule()), [isRegisteredAsParallelCapable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#isRegisteredAsParallelCapable()), [registerAsParallelCapable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#registerAsParallelCapable()), [resolveClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#resolveClass(java.lang.Class)), [resources](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#resources(java.lang.String)), [setClassAssertionStatus](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#setClassAssertionStatus(java.lang.String,boolean)), [setDefaultAssertionStatus](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#setDefaultAssertionStatus(boolean)), [setPackageAssertionStatus](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#setPackageAssertionStatus(java.lang.String,boolean)), [setSigners](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#setSigners(java.lang.Class,java.lang.Object%5B%5D))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ExtensionClassLoader
public ExtensionClassLoader([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)
Constructs a new URLClassLoader for the specified URL using the system class loader as parent
 `ClassLoader`. The URL will be searched in the order specified for classes and resources after
 first searching in the specified parent class loader.The URL is assumed to refer to a JAR file.
Parameters:
`url` - the URL from which to load classes and resources
ExtensionClassLoader
public ExtensionClassLoader([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)[] urls)
Constructs a new URLClassLoader for the specified URLs using the system class loader as parent
 `ClassLoader`. The URLs will be searched in the order specified for classes and resources after
 first searching in the specified parent class loader.The URL is assumed to refer to a JAR file.
Parameters:
`urls` - the URLs from which to load classes and resources
ExtensionClassLoader
public ExtensionClassLoader([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)[] urls,
 [ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) parent)
Constructs a new ExtensionClassLoader for the given URLs. The URLs will be searched in the order specified
 for classes and resources after first searching in the specified parent class loader.The URL is assumed to
 refer to a JAR file.
Parameters:
`urls` - the URLs from which to load classes and resources
`parent` - the parent class loader for delegation
 ============ METHOD DETAIL ========== 
Method Details
getURLClassLoader
public [URLClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URLClassLoader.html) getURLClassLoader()
Return url class loader
Returns:
URLClassLoader
getParentClassLoader
public [ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) getParentClassLoader()
Return parent class loader for delegation
Returns:
parent class loader
getOtherClassLoaders
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)> getOtherClassLoaders()
Return other class loaders for delegation
Returns:
OtherClassLoaders
setOtherClassLoader
public void setOtherClassLoader([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)> otherClassLoaders)
Set other class loaders for delegation
Parameters:
`otherClassLoaders` - other class loaders for delegation
addOtherClassLoader
public void addOtherClassLoader([ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) otherClassLoader)
Add other class loader
Parameters:
`otherClassLoader` - other class loaders for delegation
loadClass
public [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> loadClass([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
 throws [ClassNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassNotFoundException.html)
Overrides:
`[loadClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#loadClass(java.lang.String))` in class `[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)`
Throws:
`[ClassNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassNotFoundException.html)`
loadClass
protected [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> loadClass([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 boolean resolve)
 throws [ClassNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassNotFoundException.html)
Overrides:
`[loadClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#loadClass(java.lang.String,boolean))` in class `[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)`
Throws:
`[ClassNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassNotFoundException.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class ExtensionClassLoader">Class ExtensionClassLoader</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">java.lang.ClassLoader</a>
<div class="inheritance">com.nomagic.magicreport.ExtensionClassLoader</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ExtensionClassLoader</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></span></div>
<div class="block">This class loader is used to provide class loader for MagicReport extension. This loader will load classes and
 resources from a search URLs referring to JAR files and prevent resource locking from class loader.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 28, 2008</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.net.URL)">ExtensionClassLoader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new URLClassLoader for the specified URL using the system class loader as parent
 <code>ClassLoader</code>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.net.URL%5B%5D)">ExtensionClassLoader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[] urls)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new URLClassLoader for the specified URLs using the system class loader as parent
 <code>ClassLoader</code>.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.net.URL%5B%5D,java.lang.ClassLoader)">ExtensionClassLoader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[] urls,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> parent)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new ExtensionClassLoader for the given URLs.</div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addOtherClassLoader(java.lang.ClassLoader)">addOtherClassLoader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> otherClassLoader)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add other class loader</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOtherClassLoaders()">getOtherClassLoaders</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return other class loaders for delegation</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentClassLoader()">getParentClassLoader</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return parent class loader for delegation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URLClassLoader.html" title="class or interface in java.net">URLClassLoader</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getURLClassLoader()">getURLClassLoader</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return url class loader</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadClass(java.lang.String)">loadClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadClass(java.lang.String,boolean)">loadClass</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean resolve)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOtherClassLoader(java.util.List)">setOtherClassLoader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a>&gt; otherClassLoaders)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set other class loaders for delegation</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.ClassLoader">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#clearAssertionStatus()" title="class or interface in java.lang">clearAssertionStatus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#defineClass(byte%5B%5D,int,int)" title="class or interface in java.lang">defineClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#defineClass(java.lang.String,byte%5B%5D,int,int)" title="class or interface in java.lang">defineClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#defineClass(java.lang.String,byte%5B%5D,int,int,java.security.ProtectionDomain)" title="class or interface in java.lang">defineClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#defineClass(java.lang.String,java.nio.ByteBuffer,java.security.ProtectionDomain)" title="class or interface in java.lang">defineClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#definePackage(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.net.URL)" title="class or interface in java.lang">definePackage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findClass(java.lang.String)" title="class or interface in java.lang">findClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findClass(java.lang.String,java.lang.String)" title="class or interface in java.lang">findClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findLibrary(java.lang.String)" title="class or interface in java.lang">findLibrary</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findLoadedClass(java.lang.String)" title="class or interface in java.lang">findLoadedClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findResource(java.lang.String)" title="class or interface in java.lang">findResource</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findResource(java.lang.String,java.lang.String)" title="class or interface in java.lang">findResource</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findResources(java.lang.String)" title="class or interface in java.lang">findResources</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#findSystemClass(java.lang.String)" title="class or interface in java.lang">findSystemClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getClassLoadingLock(java.lang.String)" title="class or interface in java.lang">getClassLoadingLock</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getDefinedPackage(java.lang.String)" title="class or interface in java.lang">getDefinedPackage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getDefinedPackages()" title="class or interface in java.lang">getDefinedPackages</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getName()" title="class or interface in java.lang">getName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getPackage(java.lang.String)" title="class or interface in java.lang">getPackage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getPackages()" title="class or interface in java.lang">getPackages</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getParent()" title="class or interface in java.lang">getParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getPlatformClassLoader()" title="class or interface in java.lang">getPlatformClassLoader</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getResource(java.lang.String)" title="class or interface in java.lang">getResource</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getResourceAsStream(java.lang.String)" title="class or interface in java.lang">getResourceAsStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getResources(java.lang.String)" title="class or interface in java.lang">getResources</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getSystemClassLoader()" title="class or interface in java.lang">getSystemClassLoader</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getSystemResource(java.lang.String)" title="class or interface in java.lang">getSystemResource</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getSystemResourceAsStream(java.lang.String)" title="class or interface in java.lang">getSystemResourceAsStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getSystemResources(java.lang.String)" title="class or interface in java.lang">getSystemResources</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#getUnnamedModule()" title="class or interface in java.lang">getUnnamedModule</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#isRegisteredAsParallelCapable()" title="class or interface in java.lang">isRegisteredAsParallelCapable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#registerAsParallelCapable()" title="class or interface in java.lang">registerAsParallelCapable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#resolveClass(java.lang.Class)" title="class or interface in java.lang">resolveClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#resources(java.lang.String)" title="class or interface in java.lang">resources</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#setClassAssertionStatus(java.lang.String,boolean)" title="class or interface in java.lang">setClassAssertionStatus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#setDefaultAssertionStatus(boolean)" title="class or interface in java.lang">setDefaultAssertionStatus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#setPackageAssertionStatus(java.lang.String,boolean)" title="class or interface in java.lang">setPackageAssertionStatus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#setSigners(java.lang.Class,java.lang.Object%5B%5D)" title="class or interface in java.lang">setSigners</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.net.URL)">
<h3>ExtensionClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExtensionClassLoader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</span></div>
<div class="block">Constructs a new URLClassLoader for the specified URL using the system class loader as parent
 <code>ClassLoader</code>. The URL will be searched in the order specified for classes and resources after
 first searching in the specified parent class loader.The URL is assumed to refer to a JAR file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - the URL from which to load classes and resources</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.net.URL[])">
<h3>ExtensionClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExtensionClassLoader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[] urls)</span></div>
<div class="block">Constructs a new URLClassLoader for the specified URLs using the system class loader as parent
 <code>ClassLoader</code>. The URLs will be searched in the order specified for classes and resources after
 first searching in the specified parent class loader.The URL is assumed to refer to a JAR file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>urls</code> - the URLs from which to load classes and resources</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.net.URL[],java.lang.ClassLoader)">
<h3>ExtensionClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExtensionClassLoader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[] urls,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> parent)</span></div>
<div class="block">Constructs a new ExtensionClassLoader for the given URLs. The URLs will be searched in the order specified
 for classes and resources after first searching in the specified parent class loader.The URL is assumed to
 refer to a JAR file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>urls</code> - the URLs from which to load classes and resources</dd>
<dd><code>parent</code> - the parent class loader for delegation</dd>
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
<section class="detail" id="getURLClassLoader()">
<h3>getURLClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URLClassLoader.html" title="class or interface in java.net">URLClassLoader</a></span> <span class="element-name">getURLClassLoader</span>()</div>
<div class="block">Return url class loader</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>URLClassLoader</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentClassLoader()">
<h3>getParentClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></span> <span class="element-name">getParentClassLoader</span>()</div>
<div class="block">Return parent class loader for delegation</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent class loader</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOtherClassLoaders()">
<h3>getOtherClassLoaders</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a>&gt;</span> <span class="element-name">getOtherClassLoaders</span>()</div>
<div class="block">Return other class loaders for delegation</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>OtherClassLoaders</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOtherClassLoader(java.util.List)">
<h3>setOtherClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOtherClassLoader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a>&gt; otherClassLoaders)</span></div>
<div class="block">Set other class loaders for delegation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>otherClassLoaders</code> - other class loaders for delegation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addOtherClassLoader(java.lang.ClassLoader)">
<h3>addOtherClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOtherClassLoader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> otherClassLoader)</span></div>
<div class="block">Add other class loader</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>otherClassLoader</code> - other class loaders for delegation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadClass(java.lang.String)">
<h3>loadClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;</span> <span class="element-name">loadClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassNotFoundException.html" title="class or interface in java.lang">ClassNotFoundException</a></span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#loadClass(java.lang.String)" title="class or interface in java.lang">loadClass</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassNotFoundException.html" title="class or interface in java.lang">ClassNotFoundException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadClass(java.lang.String,boolean)">
<h3>loadClass</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;</span> <span class="element-name">loadClass</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean resolve)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassNotFoundException.html" title="class or interface in java.lang">ClassNotFoundException</a></span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html#loadClass(java.lang.String,boolean)" title="class or interface in java.lang">loadClass</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassNotFoundException.html" title="class or interface in java.lang">ClassNotFoundException</a></code></dd>
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
