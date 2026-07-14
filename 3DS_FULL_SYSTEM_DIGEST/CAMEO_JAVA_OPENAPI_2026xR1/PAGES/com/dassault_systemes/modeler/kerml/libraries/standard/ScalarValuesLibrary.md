# JAVA OPENAPI: ScalarValuesLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/libraries/standard/ScalarValuesLibrary.html
- source_path: `com/dassault_systemes/modeler/kerml/libraries/standard/ScalarValuesLibrary.html`
- source_sha256: `406f5cfcdc344d942cceafc7cc9ab0077103fad6cc82b9e5426cc6a73b7565b7`
- captured_utc: `2026-07-14T16:44:46.921829+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.libraries.standard](package-summary.html)

## Class ScalarValuesLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
[com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary](../AbstractLibrary.html)
com.dassault_systemes.modeler.kerml.libraries.standard.ScalarValuesLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

@OpenApiAllpublic classScalarValuesLibrary
extends [AbstractLibrary](../AbstractLibrary.html)

Provides typed access to elements from the ScalarValues standard library.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ScalarValuesLibrary.BooleanDataType](ScalarValuesLibrary.BooleanDataType.html)`
Type wrapper for the BooleanDataType library element.
`static class`
`[ScalarValuesLibrary.ComplexDataType](ScalarValuesLibrary.ComplexDataType.html)`
Type wrapper for the ComplexDataType library element.
`static class`
`[ScalarValuesLibrary.IntegerDataType](ScalarValuesLibrary.IntegerDataType.html)`
Type wrapper for the IntegerDataType library element.
`static class`
`[ScalarValuesLibrary.NaturalDataType](ScalarValuesLibrary.NaturalDataType.html)`
Type wrapper for the NaturalDataType library element.
`static class`
`[ScalarValuesLibrary.NumberDataType](ScalarValuesLibrary.NumberDataType.html)`
Type wrapper for the NumberDataType library element.
`static class`
`[ScalarValuesLibrary.NumericalValueDataType](ScalarValuesLibrary.NumericalValueDataType.html)`
Type wrapper for the NumericalValueDataType library element.
`static class`
`[ScalarValuesLibrary.PositiveDataType](ScalarValuesLibrary.PositiveDataType.html)`
Type wrapper for the PositiveDataType library element.
`static class`
`[ScalarValuesLibrary.RationalDataType](ScalarValuesLibrary.RationalDataType.html)`
Type wrapper for the RationalDataType library element.
`static class`
`[ScalarValuesLibrary.RealDataType](ScalarValuesLibrary.RealDataType.html)`
Type wrapper for the RealDataType library element.
`static class`
`[ScalarValuesLibrary.ScalarValueDataType](ScalarValuesLibrary.ScalarValueDataType.html)`
Type wrapper for the ScalarValueDataType library element.
`static class`
`[ScalarValuesLibrary.StringDataType](ScalarValuesLibrary.StringDataType.html)`
Type wrapper for the StringDataType library element.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ScalarValuesLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Creates a ScalarValuesLibrary for the given project.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ScalarValuesLibrary.BooleanDataType](ScalarValuesLibrary.BooleanDataType.html)`
`[Boolean](#Boolean())()`
Returns the wrapper for the Boolean library element.
`[ScalarValuesLibrary.ComplexDataType](ScalarValuesLibrary.ComplexDataType.html)`
`[Complex](#Complex())()`
Returns the wrapper for the Complex library element.
`static [ScalarValuesLibrary](ScalarValuesLibrary.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the ScalarValuesLibrary instance for the project that owns the given element.
`static [ScalarValuesLibrary](ScalarValuesLibrary.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Returns the ScalarValuesLibrary instance for the given project.
`protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`
Returns the type wrappers exposed by this library.
`[ScalarValuesLibrary.IntegerDataType](ScalarValuesLibrary.IntegerDataType.html)`
`[Integer](#Integer())()`
Returns the wrapper for the Integer library element.
`boolean`
`[isSemantic](#isSemantic())()`
Returns whether this library is treated as semantic.
`[ScalarValuesLibrary.NaturalDataType](ScalarValuesLibrary.NaturalDataType.html)`
`[Natural](#Natural())()`
Returns the wrapper for the Natural library element.
`[ScalarValuesLibrary.NumberDataType](ScalarValuesLibrary.NumberDataType.html)`
`[Number](#Number())()`
Returns the wrapper for the Number library element.
`[ScalarValuesLibrary.NumericalValueDataType](ScalarValuesLibrary.NumericalValueDataType.html)`
`[NumericalValue](#NumericalValue())()`
Returns the wrapper for the NumericalValue library element.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Returns the names of the library packages exposed by this wrapper.
`[ScalarValuesLibrary.PositiveDataType](ScalarValuesLibrary.PositiveDataType.html)`
`[Positive](#Positive())()`
Returns the wrapper for the Positive library element.
`[ScalarValuesLibrary.RationalDataType](ScalarValuesLibrary.RationalDataType.html)`
`[Rational](#Rational())()`
Returns the wrapper for the Rational library element.
`[ScalarValuesLibrary.RealDataType](ScalarValuesLibrary.RealDataType.html)`
`[Real](#Real())()`
Returns the wrapper for the Real library element.
`[ScalarValuesLibrary.ScalarValueDataType](ScalarValuesLibrary.ScalarValueDataType.html)`
`[ScalarValue](#ScalarValue())()`
Returns the wrapper for the ScalarValue library element.
`[ScalarValuesLibrary.StringDataType](ScalarValuesLibrary.StringDataType.html)`
`[String](#String())()`
Returns the wrapper for the String library element.
Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.[AbstractLibrary](../AbstractLibrary.html)
`[findFunctionInLibrary](../AbstractLibrary.html#findFunctionInLibrary(java.lang.String)), [findLibraryPackage](../AbstractLibrary.html#findLibraryPackage(java.lang.String)), [findPackage](../AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)), [getLibraryPackages](../AbstractLibrary.html#getLibraryPackages()), [getNamespace](../AbstractLibrary.html#getNamespace()), [initialized](../AbstractLibrary.html#initialized())`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ScalarValuesLibrary
public ScalarValuesLibrary([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Creates a ScalarValuesLibrary for the given project.
Parameters:
`project` - the project that provides access to the library model elements
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [ScalarValuesLibrary](ScalarValuesLibrary.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Returns the ScalarValuesLibrary instance for the given project.
Parameters:
`project` - the project whose library instance is requested
Returns:
the library instance for the project
getInstance
public static [ScalarValuesLibrary](ScalarValuesLibrary.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the ScalarValuesLibrary instance for the project that owns the given element.
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
ScalarValue
public [ScalarValuesLibrary.ScalarValueDataType](ScalarValuesLibrary.ScalarValueDataType.html) ScalarValue()
Returns the wrapper for the ScalarValue library element.
Returns:
the wrapper for the ScalarValue element
Boolean
public [ScalarValuesLibrary.BooleanDataType](ScalarValuesLibrary.BooleanDataType.html) Boolean()
Returns the wrapper for the Boolean library element.
Returns:
the wrapper for the Boolean element
String
public [ScalarValuesLibrary.StringDataType](ScalarValuesLibrary.StringDataType.html) String()
Returns the wrapper for the String library element.
Returns:
the wrapper for the String element
NumericalValue
public [ScalarValuesLibrary.NumericalValueDataType](ScalarValuesLibrary.NumericalValueDataType.html) NumericalValue()
Returns the wrapper for the NumericalValue library element.
Returns:
the wrapper for the NumericalValue element
Number
public [ScalarValuesLibrary.NumberDataType](ScalarValuesLibrary.NumberDataType.html) Number()
Returns the wrapper for the Number library element.
Returns:
the wrapper for the Number element
Complex
public [ScalarValuesLibrary.ComplexDataType](ScalarValuesLibrary.ComplexDataType.html) Complex()
Returns the wrapper for the Complex library element.
Returns:
the wrapper for the Complex element
Real
public [ScalarValuesLibrary.RealDataType](ScalarValuesLibrary.RealDataType.html) Real()
Returns the wrapper for the Real library element.
Returns:
the wrapper for the Real element
Rational
public [ScalarValuesLibrary.RationalDataType](ScalarValuesLibrary.RationalDataType.html) Rational()
Returns the wrapper for the Rational library element.
Returns:
the wrapper for the Rational element
Integer
public [ScalarValuesLibrary.IntegerDataType](ScalarValuesLibrary.IntegerDataType.html) Integer()
Returns the wrapper for the Integer library element.
Returns:
the wrapper for the Integer element
Natural
public [ScalarValuesLibrary.NaturalDataType](ScalarValuesLibrary.NaturalDataType.html) Natural()
Returns the wrapper for the Natural library element.
Returns:
the wrapper for the Natural element
Positive
public [ScalarValuesLibrary.PositiveDataType](ScalarValuesLibrary.PositiveDataType.html) Positive()
Returns the wrapper for the Positive library element.
Returns:
the wrapper for the Positive element
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
<h1 class="title" title="Class ScalarValuesLibrary">Class ScalarValuesLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance"><a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.libraries.standard.ScalarValuesLibrary</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ScalarValuesLibrary</span>
<span class="extends-implements">extends <a href="../AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></span></div>
<div class="block">Provides typed access to elements from the ScalarValues standard library.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.BooleanDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.BooleanDataType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the BooleanDataType library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.ComplexDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.ComplexDataType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the ComplexDataType library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.IntegerDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.IntegerDataType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the IntegerDataType library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.NaturalDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NaturalDataType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the NaturalDataType library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.NumberDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NumberDataType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the NumberDataType library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.NumericalValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NumericalValueDataType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the NumericalValueDataType library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.PositiveDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.PositiveDataType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the PositiveDataType library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.RationalDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.RationalDataType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the RationalDataType library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.RealDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.RealDataType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the RealDataType library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.ScalarValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.ScalarValueDataType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Type wrapper for the ScalarValueDataType library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ScalarValuesLibrary.StringDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.StringDataType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type wrapper for the StringDataType library element.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">ScalarValuesLibrary</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a ScalarValuesLibrary for the given project.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.BooleanDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.BooleanDataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Boolean()">Boolean</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Boolean library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.ComplexDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.ComplexDataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Complex()">Complex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Complex library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ScalarValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the ScalarValuesLibrary instance for the project that owns the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ScalarValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the ScalarValuesLibrary instance for the given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the type wrappers exposed by this library.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.IntegerDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.IntegerDataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Integer()">Integer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Integer library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this library is treated as semantic.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.NaturalDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NaturalDataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Natural()">Natural</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Natural library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.NumberDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NumberDataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Number()">Number</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Number library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.NumericalValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NumericalValueDataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#NumericalValue()">NumericalValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the NumericalValue library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the names of the library packages exposed by this wrapper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.PositiveDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.PositiveDataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Positive()">Positive</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Positive library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.RationalDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.RationalDataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Rational()">Rational</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Rational library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.RealDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.RealDataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Real()">Real</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the Real library element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.ScalarValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.ScalarValueDataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ScalarValue()">ScalarValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the ScalarValue library element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ScalarValuesLibrary.StringDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.StringDataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#String()">String</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the wrapper for the String library element.</div>
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
<h3>ScalarValuesLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScalarValuesLibrary</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Creates a ScalarValuesLibrary for the given project.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ScalarValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the ScalarValuesLibrary instance for the given project.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ScalarValuesLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the ScalarValuesLibrary instance for the project that owns the given element.</div>
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
<section class="detail" id="ScalarValue()">
<h3>ScalarValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.ScalarValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.ScalarValueDataType</a></span> <span class="element-name">ScalarValue</span>()</div>
<div class="block">Returns the wrapper for the ScalarValue library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the ScalarValue element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Boolean()">
<h3>Boolean</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.BooleanDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.BooleanDataType</a></span> <span class="element-name">Boolean</span>()</div>
<div class="block">Returns the wrapper for the Boolean library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Boolean element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="String()">
<h3>String</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.StringDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.StringDataType</a></span> <span class="element-name">String</span>()</div>
<div class="block">Returns the wrapper for the String library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the String element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NumericalValue()">
<h3>NumericalValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.NumericalValueDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NumericalValueDataType</a></span> <span class="element-name">NumericalValue</span>()</div>
<div class="block">Returns the wrapper for the NumericalValue library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the NumericalValue element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Number()">
<h3>Number</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.NumberDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NumberDataType</a></span> <span class="element-name">Number</span>()</div>
<div class="block">Returns the wrapper for the Number library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Number element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Complex()">
<h3>Complex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.ComplexDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.ComplexDataType</a></span> <span class="element-name">Complex</span>()</div>
<div class="block">Returns the wrapper for the Complex library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Complex element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Real()">
<h3>Real</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.RealDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.RealDataType</a></span> <span class="element-name">Real</span>()</div>
<div class="block">Returns the wrapper for the Real library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Real element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Rational()">
<h3>Rational</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.RationalDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.RationalDataType</a></span> <span class="element-name">Rational</span>()</div>
<div class="block">Returns the wrapper for the Rational library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Rational element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Integer()">
<h3>Integer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.IntegerDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.IntegerDataType</a></span> <span class="element-name">Integer</span>()</div>
<div class="block">Returns the wrapper for the Integer library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Integer element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Natural()">
<h3>Natural</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.NaturalDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.NaturalDataType</a></span> <span class="element-name">Natural</span>()</div>
<div class="block">Returns the wrapper for the Natural library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Natural element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Positive()">
<h3>Positive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ScalarValuesLibrary.PositiveDataType.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard">ScalarValuesLibrary.PositiveDataType</a></span> <span class="element-name">Positive</span>()</div>
<div class="block">Returns the wrapper for the Positive library element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the wrapper for the Positive element</dd>
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
