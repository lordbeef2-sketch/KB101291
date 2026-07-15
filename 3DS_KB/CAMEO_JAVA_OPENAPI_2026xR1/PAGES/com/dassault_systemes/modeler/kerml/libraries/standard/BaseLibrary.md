# JAVA OPENAPI: BaseLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/libraries/standard/BaseLibrary.html
- source_path: `com/dassault_systemes/modeler/kerml/libraries/standard/BaseLibrary.html`
- source_sha256: `ede95d98163b1d9f13eaa5e655dbeb3541b21ceb38a0abb9cd3aeec019984e39`
- captured_utc: `2026-07-14T16:44:45.323812+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.libraries.standard](package-summary.html)

## Class BaseLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
[com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary](../AbstractLibrary.html)
com.dassault_systemes.modeler.kerml.libraries.standard.BaseLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

@OpenApiAllpublic classBaseLibrary
extends [AbstractLibrary](../AbstractLibrary.html)

Provides typed access to elements from the Base standard library.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[BaseLibrary.AnythingClassifier](BaseLibrary.AnythingClassifier.html)`
Type wrapper for the AnythingClassifier library element.
`static class`
`[BaseLibrary.DataValueDataType](BaseLibrary.DataValueDataType.html)`
Type wrapper for the DataValueDataType library element.
`static class`
`[BaseLibrary.DataValuesFeature](BaseLibrary.DataValuesFeature.html)`
Type wrapper for the DataValuesFeature library element.
`static class`
`[BaseLibrary.ExactlyOneMultiplicityRange](BaseLibrary.ExactlyOneMultiplicityRange.html)`
Type wrapper for the ExactlyOneMultiplicityRange library element.
`static class`
`[BaseLibrary.NaturalsFeature](BaseLibrary.NaturalsFeature.html)`
Type wrapper for the NaturalsFeature library element.
`static class`
`[BaseLibrary.ThingsFeature](BaseLibrary.ThingsFeature.html)`
Type wrapper for the ThingsFeature library element.
`static class`
`[BaseLibrary.ZeroOrOneMultiplicityRange](BaseLibrary.ZeroOrOneMultiplicityRange.html)`
Type wrapper for the ZeroOrOneMultiplicityRange library element.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BaseLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Creates a BaseLibrary for the given project.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[BaseLibrary.AnythingClassifier](BaseLibrary.AnythingClassifier.html)`
`[Anything](#Anything())()`
Returns the wrapper for the Anything library element.
`[BaseLibrary.DataValueDataType](BaseLibrary.DataValueDataType.html)`
`[DataValue](#DataValue())()`
Returns the wrapper for the DataValue library element.
`[BaseLibrary.DataValuesFeature](BaseLibrary.DataValuesFeature.html)`
`[dataValues](#dataValues())()`
Returns the wrapper for the dataValues library element.
`[BaseLibrary.ExactlyOneMultiplicityRange](BaseLibrary.ExactlyOneMultiplicityRange.html)`
`[exactlyOne](#exactlyOne())()`
Returns the wrapper for the exactlyOne library element.
`static [BaseLibrary](BaseLibrary.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the BaseLibrary instance for the project that owns the given element.
`static [BaseLibrary](BaseLibrary.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Returns the BaseLibrary instance for the given project.
`protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`
Returns the type wrappers exposed by this library.
`boolean`
`[isSemantic](#isSemantic())()`
Returns whether this library is treated as semantic.
`[BaseLibrary.NaturalsFeature](BaseLibrary.NaturalsFeature.html)`
`[naturals](#naturals())()`
Returns the wrapper for the naturals library element.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Returns the names of the library packages exposed by this wrapper.
`[BaseLibrary.ThingsFeature](BaseLibrary.ThingsFeature.html)`
`[things](#things())()`
Returns the wrapper for the things library element.
`[BaseLibrary.ZeroOrOneMultiplicityRange](BaseLibrary.ZeroOrOneMultiplicityRange.html)`
`[zeroOrOne](#zeroOrOne())()`
Returns the wrapper for the zeroOrOne library element.
Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.[AbstractLibrary](../AbstractLibrary.html)
`[findFunctionInLibrary](../AbstractLibrary.html#findFunctionInLibrary(java.lang.String)), [findLibraryPackage](../AbstractLibrary.html#findLibraryPackage(java.lang.String)), [findPackage](../AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)), [getLibraryPackages](../AbstractLibrary.html#getLibraryPackages()), [getNamespace](../AbstractLibrary.html#getNamespace()), [initialized](../AbstractLibrary.html#initialized())`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BaseLibrary
public BaseLibrary([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Creates a BaseLibrary for the given project.
Parameters:
`project` - the project that provides access to the library model elements
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [BaseLibrary](BaseLibrary.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Returns the BaseLibrary instance for the given project.
Parameters:
`project` - the project whose library instance is requested
Returns:
the library instance for the project
getInstance
public static [BaseLibrary](BaseLibrary.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the BaseLibrary instance for the project that owns the given element.
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
Anything
public [BaseLibrary.AnythingClassifier](BaseLibrary.AnythingClassifier.html) Anything()
Returns the wrapper for the Anything library element.
Returns:
the wrapper for the Anything element
DataValue
public [BaseLibrary.DataValueDataType](BaseLibrary.DataValueDataType.html) DataValue()
Returns the wrapper for the DataValue library element.
Returns:
the wrapper for the DataValue element
things
public [BaseLibrary.ThingsFeature](BaseLibrary.ThingsFeature.html) things()
Returns the wrapper for the things library element.
Returns:
the wrapper for the things element
dataValues
public [BaseLibrary.DataValuesFeature](BaseLibrary.DataValuesFeature.html) dataValues()
Returns the wrapper for the dataValues library element.
Returns:
the wrapper for the dataValues element
naturals
public [BaseLibrary.NaturalsFeature](BaseLibrary.NaturalsFeature.html) naturals()
Returns the wrapper for the naturals library element.
Returns:
the wrapper for the naturals element
exactlyOne
public [BaseLibrary.ExactlyOneMultiplicityRange](BaseLibrary.ExactlyOneMultiplicityRange.html) exactlyOne()
Returns the wrapper for the exactlyOne library element.
Returns:
the wrapper for the exactlyOne element
zeroOrOne
public [BaseLibrary.ZeroOrOneMultiplicityRange](BaseLibrary.ZeroOrOneMultiplicityRange.html) zeroOrOne()
Returns the wrapper for the zeroOrOne library element.
Returns:
the wrapper for the zeroOrOne element
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
<h1 class="title" title="Class BaseLibrary">Class BaseLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance"><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.libraries.standard.BaseLibrary</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">BaseLibrary</span>
<span class="extends-implements">extends <a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></span></div>
<div class="block">Provides typed access to elements from the Base standard library.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="BaseLibrary.AnythingClassifier.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.AnythingClassifier</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the AnythingClassifier library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="BaseLibrary.DataValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.DataValueDataType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the DataValueDataType library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="BaseLibrary.DataValuesFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.DataValuesFeature</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the DataValuesFeature library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="BaseLibrary.ExactlyOneMultiplicityRange.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ExactlyOneMultiplicityRange</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the ExactlyOneMultiplicityRange library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="BaseLibrary.NaturalsFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.NaturalsFeature</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the NaturalsFeature library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="BaseLibrary.ThingsFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ThingsFeature</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the ThingsFeature library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="BaseLibrary.ZeroOrOneMultiplicityRange.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ZeroOrOneMultiplicityRange</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the ZeroOrOneMultiplicityRange library element.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">BaseLibrary</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a BaseLibrary for the given project.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseLibrary.AnythingClassifier.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.AnythingClassifier</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Anything()">Anything</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Anything library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseLibrary.DataValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.DataValueDataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#DataValue()">DataValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the DataValue library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseLibrary.DataValuesFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.DataValuesFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dataValues()">dataValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the dataValues library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseLibrary.ExactlyOneMultiplicityRange.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ExactlyOneMultiplicityRange</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exactlyOne()">exactlyOne</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the exactlyOne library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="BaseLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the BaseLibrary instance for the project that owns the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="BaseLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the BaseLibrary instance for the given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the type wrappers exposed by this library.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this library is treated as semantic.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseLibrary.NaturalsFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.NaturalsFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#naturals()">naturals</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the naturals library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the names of the library packages exposed by this wrapper.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseLibrary.ThingsFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ThingsFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#things()">things</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the things library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BaseLibrary.ZeroOrOneMultiplicityRange.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ZeroOrOneMultiplicityRange</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#zeroOrOne()">zeroOrOne</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the zeroOrOne library element.</div>
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
<h3>BaseLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BaseLibrary</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Creates a BaseLibrary for the given project.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="BaseLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the BaseLibrary instance for the given project.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="BaseLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the BaseLibrary instance for the project that owns the given element.</div>
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
<section class="detail" id="Anything()">
<h3>Anything</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseLibrary.AnythingClassifier.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.AnythingClassifier</a></span> <span class="element-name">Anything</span>()</div>
<div class="block">Returns the wrapper for the Anything library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Anything element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DataValue()">
<h3>DataValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseLibrary.DataValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.DataValueDataType</a></span> <span class="element-name">DataValue</span>()</div>
<div class="block">Returns the wrapper for the DataValue library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the DataValue element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="things()">
<h3>things</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseLibrary.ThingsFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ThingsFeature</a></span> <span class="element-name">things</span>()</div>
<div class="block">Returns the wrapper for the things library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the things element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dataValues()">
<h3>dataValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseLibrary.DataValuesFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.DataValuesFeature</a></span> <span class="element-name">dataValues</span>()</div>
<div class="block">Returns the wrapper for the dataValues library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the dataValues element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="naturals()">
<h3>naturals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseLibrary.NaturalsFeature.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.NaturalsFeature</a></span> <span class="element-name">naturals</span>()</div>
<div class="block">Returns the wrapper for the naturals library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the naturals element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exactlyOne()">
<h3>exactlyOne</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseLibrary.ExactlyOneMultiplicityRange.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ExactlyOneMultiplicityRange</a></span> <span class="element-name">exactlyOne</span>()</div>
<div class="block">Returns the wrapper for the exactlyOne library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the exactlyOne element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="zeroOrOne()">
<h3>zeroOrOne</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BaseLibrary.ZeroOrOneMultiplicityRange.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">BaseLibrary.ZeroOrOneMultiplicityRange</a></span> <span class="element-name">zeroOrOne</span>()</div>
<div class="block">Returns the wrapper for the zeroOrOne library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the zeroOrOne element</dd>
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
