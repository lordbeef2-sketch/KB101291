# JAVA OPENAPI: SysPhSProfile (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/sysml/util/SysPhSProfile.html
- source_path: `com/nomagic/magicdraw/sysml/util/SysPhSProfile.html`
- source_sha256: `9884b094ffed970efc9d7b590bf4abcebe6a6f649af14f4d812dab5d358bca49`
- captured_utc: `2026-07-14T16:45:47.529635+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.sysml.util](package-summary.html)

## Class SysPhSProfile

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation](../../../profiles/ProfileImplementation.html)
com.nomagic.magicdraw.sysml.util.SysPhSProfile

@OpenApiAllpublic classSysPhSProfile
extends [ProfileImplementation](../../../profiles/ProfileImplementation.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[SysPhSProfile.InitialValueReferenceStereotype](SysPhSProfile.InitialValueReferenceStereotype.html)`

`static class`
`[SysPhSProfile.InitialValuesSpecificationStereotype](SysPhSProfile.InitialValuesSpecificationStereotype.html)`

`static class`
`[SysPhSProfile.ModelicaBlockStereotype](SysPhSProfile.ModelicaBlockStereotype.html)`

`static class`
`[SysPhSProfile.ModelicaBusStereotype](SysPhSProfile.ModelicaBusStereotype.html)`

`static class`
`[SysPhSProfile.ModelicaExtensionStereotype](SysPhSProfile.ModelicaExtensionStereotype.html)`

`static class`
`[SysPhSProfile.ModelicaParameterStereotype](SysPhSProfile.ModelicaParameterStereotype.html)`

`static class`
`[SysPhSProfile.ModelicaPortStereotype](SysPhSProfile.ModelicaPortStereotype.html)`

`static class`
`[SysPhSProfile.MultidimensionalElementStereotype](SysPhSProfile.MultidimensionalElementStereotype.html)`

`static class`
`[SysPhSProfile.PhSConstantStereotype](SysPhSProfile.PhSConstantStereotype.html)`

`static class`
`[SysPhSProfile.PhSVariableStereotype](SysPhSProfile.PhSVariableStereotype.html)`

`static class`
`[SysPhSProfile.SimulationVertexStereotype](SysPhSProfile.SimulationVertexStereotype.html)`

`static class`
`[SysPhSProfile.SimulinkBlockStereotype](SysPhSProfile.SimulinkBlockStereotype.html)`

`static class`
`[SysPhSProfile.SimulinkParameterStereotype](SysPhSProfile.SimulinkParameterStereotype.html)`

`static class`
`[SysPhSProfile.SimulinkPortStereotype](SysPhSProfile.SimulinkPortStereotype.html)`
Nested classes/interfaces inherited from class com.nomagic.profiles.[ProfileImplementation](../../../profiles/ProfileImplementation.html)
`[ProfileImplementation.StereotypeWrapper](../../../profiles/ProfileImplementation.StereotypeWrapper.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROFILE_NAME](#PROFILE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROFILE_URI](#PROFILE_URI)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SysPhSProfile](#%3Cinit%3E(com.nomagic.profiles.ProfileCache))(com.nomagic.profiles.ProfileCache cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper>`
`[generatedGetAllElementWrappers](#generatedGetAllElementWrappers())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[generatedGetAllStereotypes](#generatedGetAllStereotypes())()`

`static [SysPhSProfile](SysPhSProfile.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) baseElement)`

`static [SysPhSProfile](SysPhSProfile.html)`
`[getInstanceByProject](#getInstanceByProject(com.nomagic.uml2.project.ElementProject))(com.nomagic.uml2.project.ElementProject project)`

`[SysPhSProfile.InitialValueReferenceStereotype](SysPhSProfile.InitialValueReferenceStereotype.html)`
`[initialValueReference](#initialValueReference())()`

`[SysPhSProfile.InitialValuesSpecificationStereotype](SysPhSProfile.InitialValuesSpecificationStereotype.html)`
`[initialValuesSpecification](#initialValuesSpecification())()`

`[SysPhSProfile.ModelicaBlockStereotype](SysPhSProfile.ModelicaBlockStereotype.html)`
`[modelicaBlock](#modelicaBlock())()`

`[SysPhSProfile.ModelicaBusStereotype](SysPhSProfile.ModelicaBusStereotype.html)`
`[modelicaBus](#modelicaBus())()`

`[SysPhSProfile.ModelicaExtensionStereotype](SysPhSProfile.ModelicaExtensionStereotype.html)`
`[modelicaExtension](#modelicaExtension())()`

`[SysPhSProfile.ModelicaParameterStereotype](SysPhSProfile.ModelicaParameterStereotype.html)`
`[modelicaParameter](#modelicaParameter())()`

`[SysPhSProfile.ModelicaPortStereotype](SysPhSProfile.ModelicaPortStereotype.html)`
`[modelicaPort](#modelicaPort())()`

`[SysPhSProfile.MultidimensionalElementStereotype](SysPhSProfile.MultidimensionalElementStereotype.html)`
`[multidimensionalElement](#multidimensionalElement())()`

`[SysPhSProfile.PhSConstantStereotype](SysPhSProfile.PhSConstantStereotype.html)`
`[phSConstant](#phSConstant())()`

`[SysPhSProfile.PhSVariableStereotype](SysPhSProfile.PhSVariableStereotype.html)`
`[phSVariable](#phSVariable())()`

`[SysPhSProfile.SimulationVertexStereotype](SysPhSProfile.SimulationVertexStereotype.html)`
`[simulationVertex](#simulationVertex())()`

`[SysPhSProfile.SimulinkBlockStereotype](SysPhSProfile.SimulinkBlockStereotype.html)`
`[simulinkBlock](#simulinkBlock())()`

`[SysPhSProfile.SimulinkParameterStereotype](SysPhSProfile.SimulinkParameterStereotype.html)`
`[simulinkParameter](#simulinkParameter())()`

`[SysPhSProfile.SimulinkPortStereotype](SysPhSProfile.SimulinkPortStereotype.html)`
`[simulinkPort](#simulinkPort())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PROFILE_URI
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROFILE_URI
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.sysml.util.SysPhSProfile.PROFILE_URI)
PROFILE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROFILE_NAME
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.sysml.util.SysPhSProfile.PROFILE_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SysPhSProfile
public SysPhSProfile(com.nomagic.profiles.ProfileCache cache)
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [SysPhSProfile](SysPhSProfile.html) getInstance([BaseElement](../../uml/BaseElement.html) baseElement)
getInstanceByProject
public static [SysPhSProfile](SysPhSProfile.html) getInstanceByProject(com.nomagic.uml2.project.ElementProject project)
initialValueReference
public [SysPhSProfile.InitialValueReferenceStereotype](SysPhSProfile.InitialValueReferenceStereotype.html) initialValueReference()
initialValuesSpecification
public [SysPhSProfile.InitialValuesSpecificationStereotype](SysPhSProfile.InitialValuesSpecificationStereotype.html) initialValuesSpecification()
modelicaBlock
public [SysPhSProfile.ModelicaBlockStereotype](SysPhSProfile.ModelicaBlockStereotype.html) modelicaBlock()
modelicaBus
public [SysPhSProfile.ModelicaBusStereotype](SysPhSProfile.ModelicaBusStereotype.html) modelicaBus()
modelicaExtension
public [SysPhSProfile.ModelicaExtensionStereotype](SysPhSProfile.ModelicaExtensionStereotype.html) modelicaExtension()
modelicaParameter
public [SysPhSProfile.ModelicaParameterStereotype](SysPhSProfile.ModelicaParameterStereotype.html) modelicaParameter()
modelicaPort
public [SysPhSProfile.ModelicaPortStereotype](SysPhSProfile.ModelicaPortStereotype.html) modelicaPort()
multidimensionalElement
public [SysPhSProfile.MultidimensionalElementStereotype](SysPhSProfile.MultidimensionalElementStereotype.html) multidimensionalElement()
phSConstant
public [SysPhSProfile.PhSConstantStereotype](SysPhSProfile.PhSConstantStereotype.html) phSConstant()
phSVariable
public [SysPhSProfile.PhSVariableStereotype](SysPhSProfile.PhSVariableStereotype.html) phSVariable()
simulationVertex
public [SysPhSProfile.SimulationVertexStereotype](SysPhSProfile.SimulationVertexStereotype.html) simulationVertex()
simulinkBlock
public [SysPhSProfile.SimulinkBlockStereotype](SysPhSProfile.SimulinkBlockStereotype.html) simulinkBlock()
simulinkParameter
public [SysPhSProfile.SimulinkParameterStereotype](SysPhSProfile.SimulinkParameterStereotype.html) simulinkParameter()
simulinkPort
public [SysPhSProfile.SimulinkPortStereotype](SysPhSProfile.SimulinkPortStereotype.html) simulinkPort()
generatedGetAllElementWrappers
protected [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper> generatedGetAllElementWrappers()
generatedGetAllStereotypes
protected [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> generatedGetAllStereotypes()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.sysml.util</a></div>
<h1 class="title" title="Class SysPhSProfile">Class SysPhSProfile</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation</a>
<div class="inheritance">com.nomagic.magicdraw.sysml.util.SysPhSProfile</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SysPhSProfile</span>
<span class="extends-implements">extends <a href="../../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></span></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysPhSProfile.InitialValueReferenceStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.InitialValueReferenceStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysPhSProfile.InitialValuesSpecificationStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.InitialValuesSpecificationStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysPhSProfile.ModelicaBlockStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaBlockStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysPhSProfile.ModelicaBusStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaBusStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysPhSProfile.ModelicaExtensionStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaExtensionStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysPhSProfile.ModelicaParameterStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaParameterStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysPhSProfile.ModelicaPortStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaPortStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysPhSProfile.MultidimensionalElementStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.MultidimensionalElementStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysPhSProfile.PhSConstantStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.PhSConstantStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysPhSProfile.PhSVariableStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.PhSVariableStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysPhSProfile.SimulationVertexStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulationVertexStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysPhSProfile.SimulinkBlockStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkBlockStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SysPhSProfile.SimulinkParameterStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkParameterStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SysPhSProfile.SimulinkPortStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkPortStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.profiles.ProfileImplementation">Nested classes/interfaces inherited from class com.nomagic.profiles.<a href="../../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></h2>
<code><a href="../../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROFILE_NAME">PROFILE_NAME</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROFILE_URI">PROFILE_URI</a></code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.profiles.ProfileCache)">SysPhSProfile</a><wbr/>(com.nomagic.profiles.ProfileCache cache)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllStereotypes()">generatedGetAllStereotypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SysPhSProfile.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SysPhSProfile.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.nomagic.uml2.project.ElementProject)">getInstanceByProject</a><wbr/>(com.nomagic.uml2.project.ElementProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.InitialValueReferenceStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.InitialValueReferenceStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialValueReference()">initialValueReference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.InitialValuesSpecificationStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.InitialValuesSpecificationStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initialValuesSpecification()">initialValuesSpecification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.ModelicaBlockStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaBlockStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#modelicaBlock()">modelicaBlock</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.ModelicaBusStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaBusStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#modelicaBus()">modelicaBus</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.ModelicaExtensionStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaExtensionStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#modelicaExtension()">modelicaExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.ModelicaParameterStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaParameterStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#modelicaParameter()">modelicaParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.ModelicaPortStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaPortStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#modelicaPort()">modelicaPort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.MultidimensionalElementStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.MultidimensionalElementStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#multidimensionalElement()">multidimensionalElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.PhSConstantStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.PhSConstantStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#phSConstant()">phSConstant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.PhSVariableStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.PhSVariableStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#phSVariable()">phSVariable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.SimulationVertexStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulationVertexStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simulationVertex()">simulationVertex</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.SimulinkBlockStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkBlockStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simulinkBlock()">simulinkBlock</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.SimulinkParameterStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkParameterStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simulinkParameter()">simulinkParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SysPhSProfile.SimulinkPortStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkPortStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#simulinkPort()">simulinkPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="PROFILE_URI">
<h3>PROFILE_URI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_URI</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.sysml.util.SysPhSProfile.PROFILE_URI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROFILE_NAME">
<h3>PROFILE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.sysml.util.SysPhSProfile.PROFILE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.profiles.ProfileCache)">
<h3>SysPhSProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SysPhSProfile</span><wbr/><span class="parameters">(com.nomagic.profiles.ProfileCache cache)</span></div>
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
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SysPhSProfile.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstanceByProject(com.nomagic.uml2.project.ElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SysPhSProfile.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(com.nomagic.uml2.project.ElementProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="initialValueReference()">
<h3>initialValueReference</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.InitialValueReferenceStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.InitialValueReferenceStereotype</a></span> <span class="element-name">initialValueReference</span>()</div>
</section>
</li>
<li>
<section class="detail" id="initialValuesSpecification()">
<h3>initialValuesSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.InitialValuesSpecificationStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.InitialValuesSpecificationStereotype</a></span> <span class="element-name">initialValuesSpecification</span>()</div>
</section>
</li>
<li>
<section class="detail" id="modelicaBlock()">
<h3>modelicaBlock</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.ModelicaBlockStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaBlockStereotype</a></span> <span class="element-name">modelicaBlock</span>()</div>
</section>
</li>
<li>
<section class="detail" id="modelicaBus()">
<h3>modelicaBus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.ModelicaBusStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaBusStereotype</a></span> <span class="element-name">modelicaBus</span>()</div>
</section>
</li>
<li>
<section class="detail" id="modelicaExtension()">
<h3>modelicaExtension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.ModelicaExtensionStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaExtensionStereotype</a></span> <span class="element-name">modelicaExtension</span>()</div>
</section>
</li>
<li>
<section class="detail" id="modelicaParameter()">
<h3>modelicaParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.ModelicaParameterStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaParameterStereotype</a></span> <span class="element-name">modelicaParameter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="modelicaPort()">
<h3>modelicaPort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.ModelicaPortStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.ModelicaPortStereotype</a></span> <span class="element-name">modelicaPort</span>()</div>
</section>
</li>
<li>
<section class="detail" id="multidimensionalElement()">
<h3>multidimensionalElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.MultidimensionalElementStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.MultidimensionalElementStereotype</a></span> <span class="element-name">multidimensionalElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="phSConstant()">
<h3>phSConstant</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.PhSConstantStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.PhSConstantStereotype</a></span> <span class="element-name">phSConstant</span>()</div>
</section>
</li>
<li>
<section class="detail" id="phSVariable()">
<h3>phSVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.PhSVariableStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.PhSVariableStereotype</a></span> <span class="element-name">phSVariable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="simulationVertex()">
<h3>simulationVertex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.SimulationVertexStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulationVertexStereotype</a></span> <span class="element-name">simulationVertex</span>()</div>
</section>
</li>
<li>
<section class="detail" id="simulinkBlock()">
<h3>simulinkBlock</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.SimulinkBlockStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkBlockStereotype</a></span> <span class="element-name">simulinkBlock</span>()</div>
</section>
</li>
<li>
<section class="detail" id="simulinkParameter()">
<h3>simulinkParameter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.SimulinkParameterStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkParameterStereotype</a></span> <span class="element-name">simulinkParameter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="simulinkPort()">
<h3>simulinkPort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SysPhSProfile.SimulinkPortStereotype.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile.SimulinkPortStereotype</a></span> <span class="element-name">simulinkPort</span>()</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllElementWrappers()">
<h3>generatedGetAllElementWrappers</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</span> <span class="element-name">generatedGetAllElementWrappers</span>()</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllStereotypes()">
<h3>generatedGetAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">generatedGetAllStereotypes</span>()</div>
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
