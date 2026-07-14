# JAVA OPENAPI: Parameters (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Parameters.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Parameters.html`
- source_sha256: `cac698c5ec225096132bf825241c3eede7078dd52bf1c366e86b2c5c2687a7da`
- captured_utc: `2026-07-14T16:44:48.398848+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Parameters

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Parameters

@OpenApiAllpublic classParameters
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with parameters (directed [`Feature`](kerml/Feature.html)) of [`Behavior`](kerml/Behavior.html) or [`Step`](kerml/Step.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Parameters](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static <T extends [Feature](kerml/Feature.html)> 
T`
`[createInputParameter](#createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Creates an input parameter for the given type.
`static <T extends [Feature](kerml/Feature.html)> 
T`
`[createInputParameter](#createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Expression))([Type](kerml/Type.html) type,
 [Expression](kerml/Expression.html) argument)`
Creates an input parameter and assigns an argument expression.
`static <T extends [Feature](kerml/Feature.html)> 
T`
`[createInputParameter](#createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Supplier))([Type](kerml/Type.html) type,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<T> parameterFactory)`
Creates an input parameter using a custom factory.
`static <T extends [Feature](kerml/Feature.html)> 
T`
`[createParameter](#createParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind,java.util.function.Supplier,org.eclipse.emf.ecore.EClass))([Type](kerml/Type.html) type,
 [FeatureDirectionKind](kerml/FeatureDirectionKind.html) featureDirectionKind,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<T> parameterFactory,
 org.eclipse.emf.ecore.EClass membershipClass)`
Creates a parameter using a custom factory and membership class.
`static <T extends [Feature](kerml/Feature.html)> 
T`
`[createParameter](#createParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind,org.eclipse.emf.ecore.EClass))([Type](kerml/Type.html) type,
 [FeatureDirectionKind](kerml/FeatureDirectionKind.html) featureDirectionKind,
 org.eclipse.emf.ecore.EClass membershipClass)`
Creates a parameter of the given direction and membership class.
`static <T extends [Feature](kerml/Feature.html)> 
T`
`[createReturnParameter](#createReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Creates a return parameter for the given type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getAllInputParameters](#getAllInputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns all input parameters of the given type, including inherited ones.
`static [Feature](kerml/Feature.html)`
`[getFirstOwnedInputParameter](#getFirstOwnedInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the first owned input parameter of the given type.
`static [Feature](kerml/Feature.html)`
`[getFirstParameter](#getFirstParameter(com.dassault_systemes.modeler.kerml.model.ParametersParams))([ParametersParams](ParametersParams.html) params)`
Returns the first parameter matching the given query.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getNotReturnOutputParameters](#getNotReturnOutputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns all output parameters except return parameters.
`static [Feature](kerml/Feature.html)`
`[getOrCreateOwnedReturnParameter](#getOrCreateOwnedReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the owned return parameter, creating one if necessary.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getOwnedInputParameters](#getOwnedInputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns all owned input parameters of the given type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getOwnedParameters](#getOwnedParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns all owned parameters of the given type.
`static [Feature](kerml/Feature.html)`
`[getOwnedReturnParameter](#getOwnedReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the owned return parameter of the given type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getParameters](#getParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns all parameters of the given type.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getParameters](#getParameters(com.dassault_systemes.modeler.kerml.model.ParametersParams))([ParametersParams](ParametersParams.html) params)`
Returns all parameters matching the given query.
`static [Feature](kerml/Feature.html)`
`[getReturnParameter](#getReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,boolean))([Type](kerml/Type.html) type,
 boolean owned)`
Returns the return parameter of the given type.
`static boolean`
`[isParameter](#isParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the given feature is a parameter.
`static boolean`
`[isReturnParameter](#isReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the given feature is a return parameter.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Feature](kerml/Feature.html)>`
`[streamOfParameters](#streamOfParameters(com.dassault_systemes.modeler.kerml.model.ParametersParams))([ParametersParams](ParametersParams.html) params)`
Returns a stream of parameters for the given parameter query.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Parameters
public Parameters()
 ============ METHOD DETAIL ========== 
Method Details
streamOfParameters
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Feature](kerml/Feature.html)> streamOfParameters([ParametersParams](ParametersParams.html) params)
Returns a stream of parameters for the given parameter query.
 Supports filtering by ownership, direction, and return inclusion.
Parameters:
`params` - parameter query settings
Returns:
stream of matching parameters
getFirstParameter
@CheckForNullpublic static [Feature](kerml/Feature.html) getFirstParameter([ParametersParams](ParametersParams.html) params)
Returns the first parameter matching the given query.
Parameters:
`params` - parameter query settings
Returns:
first matching parameter, or null
getFirstOwnedInputParameter
@CheckForNullpublic static [Feature](kerml/Feature.html) getFirstOwnedInputParameter([Type](kerml/Type.html) type)
Returns the first owned input parameter of the given type.
Parameters:
`type` - the type to inspect
Returns:
first owned input parameter, or null
getParameters
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getParameters([ParametersParams](ParametersParams.html) params)
Returns all parameters matching the given query.
Parameters:
`params` - parameter query settings
Returns:
list of matching parameters
isParameter
public static boolean isParameter([Feature](kerml/Feature.html) feature)
Checks whether the given feature is a parameter.
Parameters:
`feature` - the feature to check
Returns:
true if the feature is a parameter
getParameters
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getParameters([Type](kerml/Type.html) type)
Returns all parameters of the given type.
Parameters:
`type` - the type to inspect
Returns:
list of parameters, or empty list if not a behavior or step
getOwnedParameters
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getOwnedParameters([Type](kerml/Type.html) type)
Returns all owned parameters of the given type.
Parameters:
`type` - the type to inspect
Returns:
list of owned parameters
getOwnedInputParameters
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getOwnedInputParameters([Type](kerml/Type.html) type)
Returns all owned input parameters of the given type.
Parameters:
`type` - the type to inspect
Returns:
list of owned input parameters
getAllInputParameters
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getAllInputParameters([Type](kerml/Type.html) type)
Returns all input parameters of the given type, including inherited ones.
Parameters:
`type` - the type to inspect
Returns:
list of input parameters
getNotReturnOutputParameters
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getNotReturnOutputParameters([Type](kerml/Type.html) type)
Returns all output parameters except return parameters.
Parameters:
`type` - the type to inspect
Returns:
list of output parameters excluding return
getOwnedReturnParameter
@CheckForNullpublic static [Feature](kerml/Feature.html) getOwnedReturnParameter([Type](kerml/Type.html) type)
Returns the owned return parameter of the given type.
Parameters:
`type` - the type to inspect
Returns:
return parameter, or null
getOrCreateOwnedReturnParameter
public static [Feature](kerml/Feature.html) getOrCreateOwnedReturnParameter([Type](kerml/Type.html) type)
Returns the owned return parameter, creating one if necessary.
Parameters:
`type` - the type to modify
Returns:
existing or newly created return parameter
getReturnParameter
@CheckForNullpublic static [Feature](kerml/Feature.html) getReturnParameter([Type](kerml/Type.html) type,
 boolean owned)
Returns the return parameter of the given type.
Parameters:
`type` - the type to inspect
`owned` - whether to restrict to owned parameters
Returns:
return parameter, or null
isReturnParameter
public static boolean isReturnParameter([Feature](kerml/Feature.html) feature)
Checks whether the given feature is a return parameter.
Parameters:
`feature` - the feature to check
Returns:
true if the feature is a return parameter
createReturnParameter
public static <T extends [Feature](kerml/Feature.html)> T createReturnParameter([Type](kerml/Type.html) type)
Creates a return parameter for the given type.
Parameters:
`type` - the type to modify
Returns:
the created return parameter
createInputParameter
public static <T extends [Feature](kerml/Feature.html)> T createInputParameter([Type](kerml/Type.html) type)
Creates an input parameter for the given type.
Parameters:
`type` - the type to modify
Returns:
the created input parameter
createInputParameter
public static <T extends [Feature](kerml/Feature.html)> T createInputParameter([Type](kerml/Type.html) type,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<T> parameterFactory)
Creates an input parameter using a custom factory.
Parameters:
`type` - the type to modify
`parameterFactory` - factory for creating the parameter
Returns:
the created input parameter
createInputParameter
public static <T extends [Feature](kerml/Feature.html)> T createInputParameter([Type](kerml/Type.html) type,
 @CheckForNull
 [Expression](kerml/Expression.html) argument)
Creates an input parameter and assigns an argument expression.
Parameters:
`type` - the type to modify
`argument` - the argument expression, or null
Returns:
the created input parameter
createParameter
public static <T extends [Feature](kerml/Feature.html)> T createParameter([Type](kerml/Type.html) type,
 [FeatureDirectionKind](kerml/FeatureDirectionKind.html) featureDirectionKind,
 org.eclipse.emf.ecore.EClass membershipClass)
Creates a parameter of the given direction and membership class.
Parameters:
`type` - the type to modify
`featureDirectionKind` - direction of the parameter
`membershipClass` - membership class to assign
Returns:
the created parameter
createParameter
public static <T extends [Feature](kerml/Feature.html)> T createParameter([Type](kerml/Type.html) type,
 [FeatureDirectionKind](kerml/FeatureDirectionKind.html) featureDirectionKind,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<T> parameterFactory,
 org.eclipse.emf.ecore.EClass membershipClass)
Creates a parameter using a custom factory and membership class.
Parameters:
`type` - the type to modify
`featureDirectionKind` - direction of the parameter
`parameterFactory` - factory for creating the parameter
`membershipClass` - membership class to assign
Returns:
the created parameter

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Parameters">Class Parameters</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Parameters</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Parameters</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with parameters (directed <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a>) of <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a> or <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Parameters</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">createInputParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an input parameter for the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Expression)">createInputParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> argument)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an input parameter and assigns an argument expression.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Supplier)">createInputParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; parameterFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an input parameter using a custom factory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind,java.util.function.Supplier,org.eclipse.emf.ecore.EClass)">createParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> featureDirectionKind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; parameterFactory,
 org.eclipse.emf.ecore.EClass membershipClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a parameter using a custom factory and membership class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind,org.eclipse.emf.ecore.EClass)">createParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> featureDirectionKind,
 org.eclipse.emf.ecore.EClass membershipClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a parameter of the given direction and membership class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">createReturnParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a return parameter for the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllInputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getAllInputParameters</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all input parameters of the given type, including inherited ones.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstOwnedInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getFirstOwnedInputParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first owned input parameter of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstParameter(com.dassault_systemes.modeler.kerml.model.ParametersParams)">getFirstParameter</a><wbr/>(<a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a> params)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first parameter matching the given query.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotReturnOutputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getNotReturnOutputParameters</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all output parameters except return parameters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateOwnedReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOrCreateOwnedReturnParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned return parameter, creating one if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedInputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedInputParameters</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all owned input parameters of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedParameters</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all owned parameters of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedReturnParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned return parameter of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getParameters</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all parameters of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getParameters(com.dassault_systemes.modeler.kerml.model.ParametersParams)">getParameters</a><wbr/>(<a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a> params)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all parameters matching the given query.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,boolean)">getReturnParameter</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 boolean owned)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the return parameter of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isParameter</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature is a parameter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isReturnParameter</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature is a return parameter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfParameters(com.dassault_systemes.modeler.kerml.model.ParametersParams)">streamOfParameters</a><wbr/>(<a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a> params)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of parameters for the given parameter query.</div>
</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Parameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Parameters</span>()</div>
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
<section class="detail" id="streamOfParameters(com.dassault_systemes.modeler.kerml.model.ParametersParams)">
<h3>streamOfParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">streamOfParameters</span><wbr/><span class="parameters">(<a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a> params)</span></div>
<div class="block">Returns a stream of parameters for the given parameter query.
 Supports filtering by ownership, direction, and return inclusion.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>params</code> - parameter query settings</dd>
<dt>Returns:</dt>
<dd>stream of matching parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstParameter(com.dassault_systemes.modeler.kerml.model.ParametersParams)">
<h3>getFirstParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getFirstParameter</span><wbr/><span class="parameters">(<a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a> params)</span></div>
<div class="block">Returns the first parameter matching the given query.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>params</code> - parameter query settings</dd>
<dt>Returns:</dt>
<dd>first matching parameter, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstOwnedInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getFirstOwnedInputParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getFirstOwnedInputParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the first owned input parameter of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>first owned input parameter, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameters(com.dassault_systemes.modeler.kerml.model.ParametersParams)">
<h3>getParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getParameters</span><wbr/><span class="parameters">(<a href="ParametersParams.html" title="class in com.dassault_systemes.modeler.kerml.model">ParametersParams</a> params)</span></div>
<div class="block">Returns all parameters matching the given query.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>params</code> - parameter query settings</dd>
<dt>Returns:</dt>
<dd>list of matching parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isParameter</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature is a parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to check</dd>
<dt>Returns:</dt>
<dd>true if the feature is a parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getParameters</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all parameters of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>list of parameters, or empty list if not a behavior or step</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getOwnedParameters</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all owned parameters of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>list of owned parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedInputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedInputParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getOwnedInputParameters</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all owned input parameters of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>list of owned input parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllInputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getAllInputParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getAllInputParameters</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all input parameters of the given type, including inherited ones.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>list of input parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNotReturnOutputParameters(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getNotReturnOutputParameters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getNotReturnOutputParameters</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all output parameters except return parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>list of output parameters excluding return</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedReturnParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedReturnParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the owned return parameter of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>return parameter, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateOwnedReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOrCreateOwnedReturnParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateOwnedReturnParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the owned return parameter, creating one if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to modify</dd>
<dt>Returns:</dt>
<dd>existing or newly created return parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,boolean)">
<h3>getReturnParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getReturnParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 boolean owned)</span></div>
<div class="block">Returns the return parameter of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dd><code>owned</code> - whether to restrict to owned parameters</dd>
<dt>Returns:</dt>
<dd>return parameter, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isReturnParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isReturnParameter</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature is a return parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to check</dd>
<dt>Returns:</dt>
<dd>true if the feature is a return parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createReturnParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>createReturnParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">createReturnParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Creates a return parameter for the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to modify</dd>
<dt>Returns:</dt>
<dd>the created return parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>createInputParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">createInputParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Creates an input parameter for the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to modify</dd>
<dt>Returns:</dt>
<dd>the created input parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Supplier)">
<h3>createInputParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">createInputParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; parameterFactory)</span></div>
<div class="block">Creates an input parameter using a custom factory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to modify</dd>
<dd><code>parameterFactory</code> - factory for creating the parameter</dd>
<dt>Returns:</dt>
<dd>the created input parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInputParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Expression)">
<h3>createInputParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">createInputParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 @CheckForNull
 <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> argument)</span></div>
<div class="block">Creates an input parameter and assigns an argument expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to modify</dd>
<dd><code>argument</code> - the argument expression, or null</dd>
<dt>Returns:</dt>
<dd>the created input parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind,org.eclipse.emf.ecore.EClass)">
<h3>createParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">createParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> featureDirectionKind,
 org.eclipse.emf.ecore.EClass membershipClass)</span></div>
<div class="block">Creates a parameter of the given direction and membership class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to modify</dd>
<dd><code>featureDirectionKind</code> - direction of the parameter</dd>
<dd><code>membershipClass</code> - membership class to assign</dd>
<dt>Returns:</dt>
<dd>the created parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParameter(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind,java.util.function.Supplier,org.eclipse.emf.ecore.EClass)">
<h3>createParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">createParameter</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> featureDirectionKind,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; parameterFactory,
 org.eclipse.emf.ecore.EClass membershipClass)</span></div>
<div class="block">Creates a parameter using a custom factory and membership class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to modify</dd>
<dd><code>featureDirectionKind</code> - direction of the parameter</dd>
<dd><code>parameterFactory</code> - factory for creating the parameter</dd>
<dd><code>membershipClass</code> - membership class to assign</dd>
<dt>Returns:</dt>
<dd>the created parameter</dd>
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
