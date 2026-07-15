# JAVA OPENAPI: DataFunctionsLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/libraries/standard/DataFunctionsLibrary.html
- source_path: `com/dassault_systemes/modeler/kerml/libraries/standard/DataFunctionsLibrary.html`
- source_sha256: `ef26a22c1fbcd964bb784a33f2d6181b2100f45aceb07999e45750deabd404ab`
- captured_utc: `2026-07-14T16:44:45.525809+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.libraries.standard](package-summary.html)

## Class DataFunctionsLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
[com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary](../AbstractLibrary.html)
com.dassault_systemes.modeler.kerml.libraries.standard.DataFunctionsLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

@OpenApiAllpublic classDataFunctionsLibrary
extends [AbstractLibrary](../AbstractLibrary.html)

Provides typed access to elements from the DataFunctions standard library.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[DataFunctionsLibrary.AMPFunction](DataFunctionsLibrary.AMPFunction.html)`
Type wrapper for the AMPFunction library element.
`static class`
`[DataFunctionsLibrary.EQUALEQUALEQUALFunction](DataFunctionsLibrary.EQUALEQUALEQUALFunction.html)`
Type wrapper for the EQUALEQUALEQUALFunction library element.
`static class`
`[DataFunctionsLibrary.EQUALEQUALFunction](DataFunctionsLibrary.EQUALEQUALFunction.html)`
Type wrapper for the EQUALEQUALFunction library element.
`static class`
`[DataFunctionsLibrary.LESSEQUALFunction](DataFunctionsLibrary.LESSEQUALFunction.html)`
Type wrapper for the LESSEQUALFunction library element.
`static class`
`[DataFunctionsLibrary.LESSFunction](DataFunctionsLibrary.LESSFunction.html)`
Type wrapper for the LESSFunction library element.
`static class`
`[DataFunctionsLibrary.MOREEQUALFunction](DataFunctionsLibrary.MOREEQUALFunction.html)`
Type wrapper for the MOREEQUALFunction library element.
`static class`
`[DataFunctionsLibrary.MOREFunction](DataFunctionsLibrary.MOREFunction.html)`
Type wrapper for the MOREFunction library element.
`static class`
`[DataFunctionsLibrary.NotFunction](DataFunctionsLibrary.NotFunction.html)`
Type wrapper for the NotFunction library element.
`static class`
`[DataFunctionsLibrary.PIPEFunction](DataFunctionsLibrary.PIPEFunction.html)`
Type wrapper for the PIPEFunction library element.
`static class`
`[DataFunctionsLibrary.XorFunction](DataFunctionsLibrary.XorFunction.html)`
Type wrapper for the XorFunction library element.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DataFunctionsLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Creates a DataFunctionsLibrary for the given project.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[DataFunctionsLibrary.AMPFunction](DataFunctionsLibrary.AMPFunction.html)`
`[AMP](#AMP())()`
Returns the wrapper for the AMP library element.
`[DataFunctionsLibrary.EQUALEQUALFunction](DataFunctionsLibrary.EQUALEQUALFunction.html)`
`[EQUALEQUAL](#EQUALEQUAL())()`
Returns the wrapper for the EQUALEQUAL library element.
`[DataFunctionsLibrary.EQUALEQUALEQUALFunction](DataFunctionsLibrary.EQUALEQUALEQUALFunction.html)`
`[EQUALEQUALEQUAL](#EQUALEQUALEQUAL())()`
Returns the wrapper for the EQUALEQUALEQUAL library element.
`static [DataFunctionsLibrary](DataFunctionsLibrary.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the DataFunctionsLibrary instance for the project that owns the given element.
`static [DataFunctionsLibrary](DataFunctionsLibrary.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Returns the DataFunctionsLibrary instance for the given project.
`protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`
Returns the type wrappers exposed by this library.
`boolean`
`[isSemantic](#isSemantic())()`
Returns whether this library is treated as semantic.
`[DataFunctionsLibrary.LESSFunction](DataFunctionsLibrary.LESSFunction.html)`
`[LESS](#LESS())()`
Returns the wrapper for the LESS library element.
`[DataFunctionsLibrary.LESSEQUALFunction](DataFunctionsLibrary.LESSEQUALFunction.html)`
`[LESSEQUAL](#LESSEQUAL())()`
Returns the wrapper for the LESSEQUAL library element.
`[DataFunctionsLibrary.MOREFunction](DataFunctionsLibrary.MOREFunction.html)`
`[MORE](#MORE())()`
Returns the wrapper for the MORE library element.
`[DataFunctionsLibrary.MOREEQUALFunction](DataFunctionsLibrary.MOREEQUALFunction.html)`
`[MOREEQUAL](#MOREEQUAL())()`
Returns the wrapper for the MOREEQUAL library element.
`[DataFunctionsLibrary.NotFunction](DataFunctionsLibrary.NotFunction.html)`
`[not](#not())()`
Returns the wrapper for the not library element.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Returns the names of the library packages exposed by this wrapper.
`[DataFunctionsLibrary.PIPEFunction](DataFunctionsLibrary.PIPEFunction.html)`
`[PIPE](#PIPE())()`
Returns the wrapper for the PIPE library element.
`[DataFunctionsLibrary.XorFunction](DataFunctionsLibrary.XorFunction.html)`
`[xor](#xor())()`
Returns the wrapper for the xor library element.
Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.[AbstractLibrary](../AbstractLibrary.html)
`[findFunctionInLibrary](../AbstractLibrary.html#findFunctionInLibrary(java.lang.String)), [findLibraryPackage](../AbstractLibrary.html#findLibraryPackage(java.lang.String)), [findPackage](../AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)), [getLibraryPackages](../AbstractLibrary.html#getLibraryPackages()), [getNamespace](../AbstractLibrary.html#getNamespace()), [initialized](../AbstractLibrary.html#initialized())`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DataFunctionsLibrary
public DataFunctionsLibrary([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Creates a DataFunctionsLibrary for the given project.
Parameters:
`project` - the project that provides access to the library model elements
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [DataFunctionsLibrary](DataFunctionsLibrary.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Returns the DataFunctionsLibrary instance for the given project.
Parameters:
`project` - the project whose library instance is requested
Returns:
the library instance for the project
getInstance
public static [DataFunctionsLibrary](DataFunctionsLibrary.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the DataFunctionsLibrary instance for the project that owns the given element.
Parameters:
`element` - the element whose owning project is used to resolve the library instance
Returns:
the library instance associated with the element project
isSemantic
public boolean isSemantic()
Returns whether this library is treated as semantic.
Specified by:
`[isSemantic](../AbstractLibrary.html#isSemantic())` in class `[AbstractLibrary](../AbstractLibrary.html)`
Returns:
`true` if this library is semantic
packagesNames
protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> packagesNames()
Returns the names of the library packages exposed by this wrapper.
Specified by:
`[packagesNames](../AbstractLibrary.html#packagesNames())` in class `[AbstractLibrary](../AbstractLibrary.html)`
Returns:
package names that belong to this library
EQUALEQUAL
public [DataFunctionsLibrary.EQUALEQUALFunction](DataFunctionsLibrary.EQUALEQUALFunction.html) EQUALEQUAL()
Returns the wrapper for the EQUALEQUAL library element.
Returns:
the wrapper for the EQUALEQUAL element
EQUALEQUALEQUAL
public [DataFunctionsLibrary.EQUALEQUALEQUALFunction](DataFunctionsLibrary.EQUALEQUALEQUALFunction.html) EQUALEQUALEQUAL()
Returns the wrapper for the EQUALEQUALEQUAL library element.
Returns:
the wrapper for the EQUALEQUALEQUAL element
not
public [DataFunctionsLibrary.NotFunction](DataFunctionsLibrary.NotFunction.html) not()
Returns the wrapper for the not library element.
Returns:
the wrapper for the not element
xor
public [DataFunctionsLibrary.XorFunction](DataFunctionsLibrary.XorFunction.html) xor()
Returns the wrapper for the xor library element.
Returns:
the wrapper for the xor element
PIPE
public [DataFunctionsLibrary.PIPEFunction](DataFunctionsLibrary.PIPEFunction.html) PIPE()
Returns the wrapper for the PIPE library element.
Returns:
the wrapper for the PIPE element
AMP
public [DataFunctionsLibrary.AMPFunction](DataFunctionsLibrary.AMPFunction.html) AMP()
Returns the wrapper for the AMP library element.
Returns:
the wrapper for the AMP element
LESS
public [DataFunctionsLibrary.LESSFunction](DataFunctionsLibrary.LESSFunction.html) LESS()
Returns the wrapper for the LESS library element.
Returns:
the wrapper for the LESS element
MORE
public [DataFunctionsLibrary.MOREFunction](DataFunctionsLibrary.MOREFunction.html) MORE()
Returns the wrapper for the MORE library element.
Returns:
the wrapper for the MORE element
LESSEQUAL
public [DataFunctionsLibrary.LESSEQUALFunction](DataFunctionsLibrary.LESSEQUALFunction.html) LESSEQUAL()
Returns the wrapper for the LESSEQUAL library element.
Returns:
the wrapper for the LESSEQUAL element
MOREEQUAL
public [DataFunctionsLibrary.MOREEQUALFunction](DataFunctionsLibrary.MOREEQUALFunction.html) MOREEQUAL()
Returns the wrapper for the MOREEQUAL library element.
Returns:
the wrapper for the MOREEQUAL element
getTypeWrappers
protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper> getTypeWrappers()
Returns the type wrappers exposed by this library.
Specified by:
`[getTypeWrappers](../AbstractLibrary.html#getTypeWrappers())` in class `[AbstractLibrary](../AbstractLibrary.html)`
Returns:
type wrappers managed by this library

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.libraries.standard</a></div>
<h1 class="title" title="Class DataFunctionsLibrary">Class DataFunctionsLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance"><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.libraries.standard.DataFunctionsLibrary</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DataFunctionsLibrary</span>
<span class="extends-implements">extends <a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></span></div>
<div class="block">Provides typed access to elements from the DataFunctions standard library.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.AMPFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.AMPFunction</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the AMPFunction library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.EQUALEQUALEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.EQUALEQUALEQUALFunction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the EQUALEQUALEQUALFunction library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.EQUALEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.EQUALEQUALFunction</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the EQUALEQUALFunction library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.LESSEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.LESSEQUALFunction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the LESSEQUALFunction library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.LESSFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.LESSFunction</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the LESSFunction library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.MOREEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.MOREEQUALFunction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the MOREEQUALFunction library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.MOREFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.MOREFunction</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the MOREFunction library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.NotFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.NotFunction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the NotFunction library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.PIPEFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.PIPEFunction</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the PIPEFunction library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DataFunctionsLibrary.XorFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.XorFunction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the XorFunction library element.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">DataFunctionsLibrary</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a DataFunctionsLibrary for the given project.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.AMPFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.AMPFunction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#AMP()">AMP</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the AMP library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.EQUALEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.EQUALEQUALFunction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#EQUALEQUAL()">EQUALEQUAL</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the EQUALEQUAL library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.EQUALEQUALEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.EQUALEQUALEQUALFunction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#EQUALEQUALEQUAL()">EQUALEQUALEQUAL</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the EQUALEQUALEQUAL library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the DataFunctionsLibrary instance for the project that owns the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the DataFunctionsLibrary instance for the given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the type wrappers exposed by this library.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this library is treated as semantic.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.LESSFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.LESSFunction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#LESS()">LESS</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the LESS library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.LESSEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.LESSEQUALFunction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#LESSEQUAL()">LESSEQUAL</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the LESSEQUAL library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.MOREFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.MOREFunction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#MORE()">MORE</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the MORE library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.MOREEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.MOREEQUALFunction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#MOREEQUAL()">MOREEQUAL</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the MOREEQUAL library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.NotFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.NotFunction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#not()">not</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the not library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the names of the library packages exposed by this wrapper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.PIPEFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.PIPEFunction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#PIPE()">PIPE</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the PIPE library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DataFunctionsLibrary.XorFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.XorFunction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#xor()">xor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the xor library element.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary">Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.<a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></h3>
<code><a href="../AbstractLibrary.html#findFunctionInLibrary(java.lang.String)">findFunctionInLibrary</a>, <a href="../AbstractLibrary.html#findLibraryPackage(java.lang.String)">findLibraryPackage</a>, <a href="../AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)">findPackage</a>, <a href="../AbstractLibrary.html#getLibraryPackages()">getLibraryPackages</a>, <a href="../AbstractLibrary.html#getNamespace()">getNamespace</a>, <a href="../AbstractLibrary.html#initialized()">initialized</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
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
<section class="detail" id="&lt;init&gt;(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>DataFunctionsLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DataFunctionsLibrary</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Creates a DataFunctionsLibrary for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project that provides access to the library model elements</dd>
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
<section class="detail" id="getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the DataFunctionsLibrary instance for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project whose library instance is requested</dd>
<dt>Returns:</dt>
<dd>the library instance for the project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the DataFunctionsLibrary instance for the project that owns the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element whose owning project is used to resolve the library instance</dd>
<dt>Returns:</dt>
<dd>the library instance associated with the element project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSemantic()">
<h3>isSemantic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSemantic</span>()</div>
<div class="block">Returns whether this library is treated as semantic.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractLibrary.html#isSemantic()">isSemantic</a></code> in class <code><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if this library is semantic</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="packagesNames()">
<h3>packagesNames</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">packagesNames</span>()</div>
<div class="block">Returns the names of the library packages exposed by this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractLibrary.html#packagesNames()">packagesNames</a></code> in class <code><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>package names that belong to this library</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EQUALEQUAL()">
<h3>EQUALEQUAL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.EQUALEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.EQUALEQUALFunction</a></span> <span class="element-name">EQUALEQUAL</span>()</div>
<div class="block">Returns the wrapper for the EQUALEQUAL library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the EQUALEQUAL element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EQUALEQUALEQUAL()">
<h3>EQUALEQUALEQUAL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.EQUALEQUALEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.EQUALEQUALEQUALFunction</a></span> <span class="element-name">EQUALEQUALEQUAL</span>()</div>
<div class="block">Returns the wrapper for the EQUALEQUALEQUAL library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the EQUALEQUALEQUAL element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="not()">
<h3>not</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.NotFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.NotFunction</a></span> <span class="element-name">not</span>()</div>
<div class="block">Returns the wrapper for the not library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the not element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="xor()">
<h3>xor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.XorFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.XorFunction</a></span> <span class="element-name">xor</span>()</div>
<div class="block">Returns the wrapper for the xor library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the xor element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PIPE()">
<h3>PIPE</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.PIPEFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.PIPEFunction</a></span> <span class="element-name">PIPE</span>()</div>
<div class="block">Returns the wrapper for the PIPE library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the PIPE element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AMP()">
<h3>AMP</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.AMPFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.AMPFunction</a></span> <span class="element-name">AMP</span>()</div>
<div class="block">Returns the wrapper for the AMP library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the AMP element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LESS()">
<h3>LESS</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.LESSFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.LESSFunction</a></span> <span class="element-name">LESS</span>()</div>
<div class="block">Returns the wrapper for the LESS library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the LESS element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MORE()">
<h3>MORE</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.MOREFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.MOREFunction</a></span> <span class="element-name">MORE</span>()</div>
<div class="block">Returns the wrapper for the MORE library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the MORE element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LESSEQUAL()">
<h3>LESSEQUAL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.LESSEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.LESSEQUALFunction</a></span> <span class="element-name">LESSEQUAL</span>()</div>
<div class="block">Returns the wrapper for the LESSEQUAL library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the LESSEQUAL element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MOREEQUAL()">
<h3>MOREEQUAL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DataFunctionsLibrary.MOREEQUALFunction.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">DataFunctionsLibrary.MOREEQUALFunction</a></span> <span class="element-name">MOREEQUAL</span>()</div>
<div class="block">Returns the wrapper for the MOREEQUAL library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the MOREEQUAL element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeWrappers()">
<h3>getTypeWrappers</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</span> <span class="element-name">getTypeWrappers</span>()</div>
<div class="block">Returns the type wrappers exposed by this library.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractLibrary.html#getTypeWrappers()">getTypeWrappers</a></code> in class <code><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>type wrappers managed by this library</dd>
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
