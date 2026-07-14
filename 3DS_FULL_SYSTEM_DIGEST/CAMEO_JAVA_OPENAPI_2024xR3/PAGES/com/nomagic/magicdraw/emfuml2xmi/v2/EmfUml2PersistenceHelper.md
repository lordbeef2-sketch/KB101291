# JAVA OPENAPI: EmfUml2PersistenceHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v2/EmfUml2PersistenceHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/EmfUml2PersistenceHelper.html`
- source_sha256: `9506d37562d52589d3f87da60d969207cbc95a34dedb5f4ec33b4ecffddd9f8f`
- captured_utc: `2026-07-14T16:55:18.851047+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v2](package-summary.html)

## Class EmfUml2PersistenceHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper
com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper

@OpenApipublic final classEmfUml2PersistenceHelper
extends com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper
Stores save and load options.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EmfUml2PersistenceHelper](#%3Cinit%3E(java.lang.String,java.lang.String,java.util.Set))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourcesJarPath,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsDir,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> supportedUmlUris)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addResourceSetInitializer](#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer))([ResourceSetInitializer](ResourceSetInitializer.html) initializer)`
Register resource set initializer.
`void`
`[clean](#clean(com.nomagic.task.ProgressStatus))([ProgressStatus](../../../task/ProgressStatus.html) progress)`

`static void`
`[clean](#clean(java.util.Collection,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)`
Disposes given Eclipse UML2 elements.
`org.eclipse.emf_2_2_3.ecore.resource.Resource`
`[createResource](#createResource(org.eclipse.emf_2_2_3.common.util.URI,org.eclipse.uml2_2_0_4.uml.Package))(org.eclipse.emf_2_2_3.common.util.URI uri,
 org.eclipse.uml2_2_0_4.uml.Package ePackage)`

`static org.eclipse.emf_2_2_3.common.util.URI`
`[createURI](#createURI(org.eclipse.emf_2_2_3.common.util.URI,java.lang.String,java.lang.String))(org.eclipse.emf_2_2_3.common.util.URI path,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension)`

`static [PersistenceOptionsProvider](PersistenceOptionsProvider.html)`
`[getLoadOptionsProvider](#getLoadOptionsProvider())()`
Returns load options provider.
`protected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getPackageInstance](#getPackageInstance())()`

`protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[getPackageRegistry](#getPackageRegistry())()`

`org.eclipse.emf_2_2_3.ecore.resource.ResourceSet`
`[getResourceSet](#getResourceSet())()`

`static [PersistenceOptionsProvider](PersistenceOptionsProvider.html)`
`[getSaveOptionsProvider](#getSaveOptionsProvider())()`
Returns save options provider
`org.eclipse.uml2_2_0_4.uml.Package`
`[load](#load(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceString)`

`org.eclipse.uml2_2_0_4.uml.Package`
`[loadFile](#loadFile(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`

`protected void`
`[registerPathmaps](#registerPathmaps(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourcesJarPath)`

`protected void`
`[registerResourceFactories](#registerResourceFactories())()`

`static void`
`[removeResourceSetInitializer](#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer))([ResourceSetInitializer](ResourceSetInitializer.html) initializer)`
Remove resource set initializer.
`void`
`[save](#save(org.eclipse.emf_2_2_3.ecore.resource.Resource))(org.eclipse.emf_2_2_3.ecore.resource.Resource resource)`

`static void`
`[setLoadOptionsProvider](#setLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)`
Sets load options provider.
`static void`
`[setSaveOptionsProvider](#setSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)`
Sets save options provider.
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper
`getOptionsDir, registerPackage, removeIllegalCharacters`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EmfUml2PersistenceHelper
public EmfUml2PersistenceHelper([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourcesJarPath,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsDir,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> supportedUmlUris)
 ============ METHOD DETAIL ========== 
Method Details
getSaveOptionsProvider
@OpenApipublic static [PersistenceOptionsProvider](PersistenceOptionsProvider.html) getSaveOptionsProvider()
Returns save options provider
Returns:
persistence options provider
setSaveOptionsProvider
@OpenApipublic static void setSaveOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)
Sets save options provider.
getLoadOptionsProvider
@OpenApipublic static [PersistenceOptionsProvider](PersistenceOptionsProvider.html) getLoadOptionsProvider()
Returns load options provider.
Returns:
persistence options provider
addResourceSetInitializer
@OpenApipublic static void addResourceSetInitializer([ResourceSetInitializer](ResourceSetInitializer.html) initializer)
Register resource set initializer.
Parameters:
`initializer` - resource set initializer to add.
removeResourceSetInitializer
@OpenApipublic static void removeResourceSetInitializer([ResourceSetInitializer](ResourceSetInitializer.html) initializer)
Remove resource set initializer.
Parameters:
`initializer` - resource set initializer to remove.
getResourceSet
public org.eclipse.emf_2_2_3.ecore.resource.ResourceSet getResourceSet()
setLoadOptionsProvider
@OpenApipublic static void setLoadOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)
Sets load options provider.
createResource
public org.eclipse.emf_2_2_3.ecore.resource.Resource createResource(org.eclipse.emf_2_2_3.common.util.URI uri,
 org.eclipse.uml2_2_0_4.uml.Package ePackage)
save
public void save(org.eclipse.emf_2_2_3.ecore.resource.Resource resource)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
load
public org.eclipse.uml2_2_0_4.uml.Package load([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceString)
loadFile
public org.eclipse.uml2_2_0_4.uml.Package loadFile([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
createURI
public static org.eclipse.emf_2_2_3.common.util.URI createURI(org.eclipse.emf_2_2_3.common.util.URI path,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension)
registerResourceFactories
protected void registerResourceFactories()
Specified by:
`registerResourceFactories` in class `com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper`
getPackageInstance
protected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getPackageInstance()
Specified by:
`getPackageInstance` in class `com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper`
getPackageRegistry
protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) getPackageRegistry()
Specified by:
`getPackageRegistry` in class `com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper`
registerPathmaps
protected void registerPathmaps([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourcesJarPath)
Specified by:
`registerPathmaps` in class `com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper`
clean
public void clean([ProgressStatus](../../../task/ProgressStatus.html) progress)
Specified by:
`clean` in class `com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper`
clean
@OpenApipublic static void clean([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)
Disposes given Eclipse UML2 elements.
Parameters:
`elements` - Eclipse UML2 elements.
`progress` - progress

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v2</a></div>
<h1 class="title" title="Class EmfUml2PersistenceHelper">Class EmfUml2PersistenceHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">EmfUml2PersistenceHelper</span>
<span class="extends-implements">extends com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</span></div>
<div class="block">Stores save and load options.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.util.Set)">EmfUml2PersistenceHelper</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourcesJarPath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; supportedUmlUris)</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer)">addResourceSetInitializer</a><wbr/>(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">ResourceSetInitializer</a> initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register resource set initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clean(com.nomagic.task.ProgressStatus)">clean</a><wbr/>(<a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clean(java.util.Collection,com.nomagic.task.ProgressStatus)">clean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Disposes given Eclipse UML2 elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf_2_2_3.ecore.resource.Resource</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createResource(org.eclipse.emf_2_2_3.common.util.URI,org.eclipse.uml2_2_0_4.uml.Package)">createResource</a><wbr/>(org.eclipse.emf_2_2_3.common.util.URI uri,
 org.eclipse.uml2_2_0_4.uml.Package ePackage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf_2_2_3.common.util.URI</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createURI(org.eclipse.emf_2_2_3.common.util.URI,java.lang.String,java.lang.String)">createURI</a><wbr/>(org.eclipse.emf_2_2_3.common.util.URI path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoadOptionsProvider()">getLoadOptionsProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns load options provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackageInstance()">getPackageInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackageRegistry()">getPackageRegistry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf_2_2_3.ecore.resource.ResourceSet</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourceSet()">getResourceSet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSaveOptionsProvider()">getSaveOptionsProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns save options provider</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Package</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#load(java.lang.String)">load</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceString)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Package</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadFile(java.io.File)">loadFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerPathmaps(java.lang.String)">registerPathmaps</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourcesJarPath)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerResourceFactories()">registerResourceFactories</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer)">removeResourceSetInitializer</a><wbr/>(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">ResourceSetInitializer</a> initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove resource set initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#save(org.eclipse.emf_2_2_3.ecore.resource.Resource)">save</a><wbr/>(org.eclipse.emf_2_2_3.ecore.resource.Resource resource)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider)">setLoadOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a> loadOptionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets load options provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider)">setSaveOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a> saveOptionsProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets save options provider.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</h3>
<code>getOptionsDir, registerPackage, removeIllegalCharacters</code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.util.Set)">
<h3>EmfUml2PersistenceHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EmfUml2PersistenceHelper</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourcesJarPath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; supportedUmlUris)</span></div>
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
<section class="detail" id="getSaveOptionsProvider()">
<h3>getSaveOptionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a></span> <span class="element-name">getSaveOptionsProvider</span>()</div>
<div class="block">Returns save options provider</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>persistence options provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider)">
<h3>setSaveOptionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSaveOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a> saveOptionsProvider)</span></div>
<div class="block">Sets save options provider.</div>
</section>
</li>
<li>
<section class="detail" id="getLoadOptionsProvider()">
<h3>getLoadOptionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a></span> <span class="element-name">getLoadOptionsProvider</span>()</div>
<div class="block">Returns load options provider.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>persistence options provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer)">
<h3>addResourceSetInitializer</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addResourceSetInitializer</span><wbr/><span class="parameters">(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">ResourceSetInitializer</a> initializer)</span></div>
<div class="block">Register resource set initializer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initializer</code> - resource set initializer to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer)">
<h3>removeResourceSetInitializer</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeResourceSetInitializer</span><wbr/><span class="parameters">(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">ResourceSetInitializer</a> initializer)</span></div>
<div class="block">Remove resource set initializer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initializer</code> - resource set initializer to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourceSet()">
<h3>getResourceSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf_2_2_3.ecore.resource.ResourceSet</span> <span class="element-name">getResourceSet</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider)">
<h3>setLoadOptionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setLoadOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a> loadOptionsProvider)</span></div>
<div class="block">Sets load options provider.</div>
</section>
</li>
<li>
<section class="detail" id="createResource(org.eclipse.emf_2_2_3.common.util.URI,org.eclipse.uml2_2_0_4.uml.Package)">
<h3>createResource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf_2_2_3.ecore.resource.Resource</span> <span class="element-name">createResource</span><wbr/><span class="parameters">(org.eclipse.emf_2_2_3.common.util.URI uri,
 org.eclipse.uml2_2_0_4.uml.Package ePackage)</span></div>
</section>
</li>
<li>
<section class="detail" id="save(org.eclipse.emf_2_2_3.ecore.resource.Resource)">
<h3>save</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">save</span><wbr/><span class="parameters">(org.eclipse.emf_2_2_3.ecore.resource.Resource resource)</span>
          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="load(java.lang.String)">
<h3>load</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Package</span> <span class="element-name">load</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceString)</span></div>
</section>
</li>
<li>
<section class="detail" id="loadFile(java.io.File)">
<h3>loadFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Package</span> <span class="element-name">loadFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
</section>
</li>
<li>
<section class="detail" id="createURI(org.eclipse.emf_2_2_3.common.util.URI,java.lang.String,java.lang.String)">
<h3>createURI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf_2_2_3.common.util.URI</span> <span class="element-name">createURI</span><wbr/><span class="parameters">(org.eclipse.emf_2_2_3.common.util.URI path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</span></div>
</section>
</li>
<li>
<section class="detail" id="registerResourceFactories()">
<h3>registerResourceFactories</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">registerResourceFactories</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>registerResourceFactories</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageInstance()">
<h3>getPackageInstance</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getPackageInstance</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getPackageInstance</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageRegistry()">
<h3>getPackageRegistry</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getPackageRegistry</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getPackageRegistry</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerPathmaps(java.lang.String)">
<h3>registerPathmaps</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">registerPathmaps</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourcesJarPath)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>registerPathmaps</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clean(com.nomagic.task.ProgressStatus)">
<h3>clean</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clean</span><wbr/><span class="parameters">(<a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>clean</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clean(java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>clean</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clean</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</span></div>
<div class="block">Disposes given Eclipse UML2 elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - Eclipse UML2 elements.</dd>
<dd><code>progress</code> - progress</dd>
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
