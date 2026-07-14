# JAVA OPENAPI: ModelTransformationsManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/modeltransformations/ModelTransformationsManager.html
- source_path: `com/nomagic/magicdraw/modeltransformations/ModelTransformationsManager.html`
- source_sha256: `45f81fd016686151cf04a13cdbce48b1fb6c0dc4cc6b2bb780e46f03a8d7e371`
- captured_utc: `2026-07-14T16:51:25.306257+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modeltransformations](package-summary.html)

## Class ModelTransformationsManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.modeltransformations.ModelTransformationsManager

@OpenApiAllpublic final classModelTransformationsManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
ModelTransformationsManager organizes process of application of model transformation.
 This class is responsible for Undo/redo commands etc.
 Use this class as singleton.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addTransformation](#addTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo))([ModelTransformationInfo](ModelTransformationInfo.html) info)`
Adds the given model transformation in registered model transformations collection.
`boolean`
`[doTransformation](#doTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo))([ModelTransformationsWizardInformation](ModelTransformationsWizardInformation.html) wi,
 [ModelTransformationInfo](ModelTransformationInfo.html) mti)`

`boolean`
`[doUpdateTransformation](#doUpdateTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,com.nomagic.magicdraw.properties.PropertyManager))([ModelTransformationInfo](ModelTransformationInfo.html) mti_final,
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformedPackage_final,
 boolean sync_final,
 [PropertyManager](../properties/PropertyManager.html) prop)`

`static [ModelTransformationsManager](ModelTransformationsManager.html)`
`[getInstance](#getInstance())()`
Returns a shared instance of model transformations manager.
`[ModelTransformationInfo](ModelTransformationInfo.html)`
`[getTransformationInfoByName](#getTransformationInfoByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationName)`
Returns transformation info by transformation name
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModelTransformationInfo](ModelTransformationInfo.html)>`
`[getTransformations](#getTransformations())()`
Returns all registered model transformations.
`static void`
`[loadTransformationProperties](#loadTransformationProperties(com.nomagic.magicdraw.properties.Style,com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation,com.nomagic.magicdraw.core.Project))([Style](../properties/Style.html) style,
 [ModelTransformationsWizardInformation](ModelTransformationsWizardInformation.html) wi,
 [Project](../core/Project.html) project)`

`static [Style](../properties/Style.html)`
`[loadTransformationProperties](#loadTransformationProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformedPackage,
 [ModelTransformationsWizardInformation](ModelTransformationsWizardInformation.html) wi)`

`void`
`[removeTransformation](#removeTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo))([ModelTransformationInfo](ModelTransformationInfo.html) info)`
Removes the given model transformation from registered collection of model transformations.
`void`
`[saveTransformationProperties](#saveTransformationProperties(com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation))([ModelTransformationsWizardInformation](ModelTransformationsWizardInformation.html) wizardInformation)`

`boolean`
`[transform](#transform(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [BaseElement](../uml/BaseElement.html)> selectedElements)`
Displays transformation wizard and runs transformation
`void`
`[updateProperties](#updateProperties(com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](../properties/PropertyManager.html) source,
 [PropertyManager](../properties/PropertyManager.html) propertiesToUpdate)`

`boolean`
`[updateTransformation](#updateTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformed)`
Checks for already applied transformations, sets the right one and runs transformation update
`boolean`
`[updateTransformation](#updateTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformed,
 boolean testingMode)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [ModelTransformationsManager](ModelTransformationsManager.html) getInstance()
Returns a shared instance of model transformations manager.
Returns:
instance of model transformations manager.
addTransformation
public void addTransformation([ModelTransformationInfo](ModelTransformationInfo.html) info)
Adds the given model transformation in registered model transformations collection.
Parameters:
`info` - the give transformation to add.
removeTransformation
public void removeTransformation([ModelTransformationInfo](ModelTransformationInfo.html) info)
Removes the given model transformation from registered collection of model transformations.
Parameters:
`info` - the given transformation to remove.
getTransformations
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModelTransformationInfo](ModelTransformationInfo.html)> getTransformations()
Returns all registered model transformations.
Returns:
a collection of registered model transformations.
getTransformationInfoByName
@CheckForNullpublic [ModelTransformationInfo](ModelTransformationInfo.html) getTransformationInfoByName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationName)
Returns transformation info by transformation name
Parameters:
`transformationName` - transformation name
Returns:
transformation info
transform
public boolean transform([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [BaseElement](../uml/BaseElement.html)> selectedElements)
Displays transformation wizard and runs transformation
Parameters:
`selectedElements` - list of elements to transform
Returns:
true if transformation was successful
doTransformation
public boolean doTransformation([ModelTransformationsWizardInformation](ModelTransformationsWizardInformation.html) wi,
 [ModelTransformationInfo](ModelTransformationInfo.html) mti)
updateTransformation
public boolean updateTransformation([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformed,
 boolean testingMode)
updateTransformation
public boolean updateTransformation([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformed)
Checks for already applied transformations, sets the right one and runs transformation update
Parameters:
`transformed` - list of elements to transform
Returns:
true if transformation update was successful
doUpdateTransformation
public boolean doUpdateTransformation([ModelTransformationInfo](ModelTransformationInfo.html) mti_final,
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformedPackage_final,
 boolean sync_final,
 @CheckForNull
 [PropertyManager](../properties/PropertyManager.html) prop)
updateProperties
public void updateProperties([PropertyManager](../properties/PropertyManager.html) source,
 [PropertyManager](../properties/PropertyManager.html) propertiesToUpdate)
loadTransformationProperties
@CheckForNullpublic static [Style](../properties/Style.html) loadTransformationProperties([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformedPackage,
 [ModelTransformationsWizardInformation](ModelTransformationsWizardInformation.html) wi)
loadTransformationProperties
public static void loadTransformationProperties([Style](../properties/Style.html) style,
 [ModelTransformationsWizardInformation](ModelTransformationsWizardInformation.html) wi,
 [Project](../core/Project.html) project)
saveTransformationProperties
public void saveTransformationProperties([ModelTransformationsWizardInformation](ModelTransformationsWizardInformation.html) wizardInformation)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modeltransformations</a></div>
<h1 class="title" title="Class ModelTransformationsManager">Class ModelTransformationsManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.modeltransformations.ModelTransformationsManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ModelTransformationsManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">ModelTransformationsManager organizes process of application of model transformation.
 This class is responsible for Undo/redo commands etc.
 <p>
 Use this class as singleton.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo)">addTransformation</a><wbr/>(<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the given model transformation in registered model transformations collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo)">doTransformation</a><wbr/>(<a href="ModelTransformationsWizardInformation.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsWizardInformation</a> wi,
 <a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> mti)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doUpdateTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,com.nomagic.magicdraw.properties.PropertyManager)">doUpdateTransformation</a><wbr/>(<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> mti_final,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformedPackage_final,
 boolean sync_final,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> prop)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ModelTransformationsManager.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a shared instance of model transformations manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformationInfoByName(java.lang.String)">getTransformationInfoByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns transformation info by transformation name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformations()">getTransformations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all registered model transformations.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadTransformationProperties(com.nomagic.magicdraw.properties.Style,com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation,com.nomagic.magicdraw.core.Project)">loadTransformationProperties</a><wbr/>(<a href="../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style,
 <a href="ModelTransformationsWizardInformation.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsWizardInformation</a> wi,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#loadTransformationProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation)">loadTransformationProperties</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformedPackage,
 <a href="ModelTransformationsWizardInformation.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsWizardInformation</a> wi)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo)">removeTransformation</a><wbr/>(<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the given model transformation from registered collection of model transformations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveTransformationProperties(com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation)">saveTransformationProperties</a><wbr/>(<a href="ModelTransformationsWizardInformation.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsWizardInformation</a> wizardInformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(java.util.List)">transform</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; selectedElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Displays transformation wizard and runs transformation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateProperties(com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.magicdraw.properties.PropertyManager)">updateProperties</a><wbr/>(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> source,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertiesToUpdate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">updateTransformation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformed)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks for already applied transformations, sets the right one and runs transformation update</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean)">updateTransformation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformed,
 boolean testingMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ModelTransformationsManager.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns a shared instance of model transformations manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of model transformations manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo)">
<h3>addTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addTransformation</span><wbr/><span class="parameters">(<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info)</span></div>
<div class="block">Adds the given model transformation in registered model transformations collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>info</code> - the give transformation to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo)">
<h3>removeTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeTransformation</span><wbr/><span class="parameters">(<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info)</span></div>
<div class="block">Removes the given model transformation from registered collection of model transformations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>info</code> - the given transformation to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransformations()">
<h3>getTransformations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a>&gt;</span> <span class="element-name">getTransformations</span>()</div>
<div class="block">Returns all registered model transformations.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a collection of registered model transformations.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransformationInfoByName(java.lang.String)">
<h3>getTransformationInfoByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></span> <span class="element-name">getTransformationInfoByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationName)</span></div>
<div class="block">Returns transformation info by transformation name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformationName</code> - transformation name</dd>
<dt>Returns:</dt>
<dd>transformation info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(java.util.List)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; selectedElements)</span></div>
<div class="block">Displays transformation wizard and runs transformation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>selectedElements</code> - list of elements to transform</dd>
<dt>Returns:</dt>
<dd>true if transformation was successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo)">
<h3>doTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">doTransformation</span><wbr/><span class="parameters">(<a href="ModelTransformationsWizardInformation.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsWizardInformation</a> wi,
 <a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> mti)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean)">
<h3>updateTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">updateTransformation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformed,
 boolean testingMode)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateTransformation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>updateTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">updateTransformation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformed)</span></div>
<div class="block">Checks for already applied transformations, sets the right one and runs transformation update</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformed</code> - list of elements to transform</dd>
<dt>Returns:</dt>
<dd>true if transformation update was successful</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doUpdateTransformation(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,com.nomagic.magicdraw.properties.PropertyManager)">
<h3>doUpdateTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">doUpdateTransformation</span><wbr/><span class="parameters">(<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> mti_final,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformedPackage_final,
 boolean sync_final,
 @CheckForNull
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> prop)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateProperties(com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.magicdraw.properties.PropertyManager)">
<h3>updateProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateProperties</span><wbr/><span class="parameters">(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> source,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertiesToUpdate)</span></div>
</section>
</li>
<li>
<section class="detail" id="loadTransformationProperties(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation)">
<h3>loadTransformationProperties</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">loadTransformationProperties</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformedPackage,
 <a href="ModelTransformationsWizardInformation.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsWizardInformation</a> wi)</span></div>
</section>
</li>
<li>
<section class="detail" id="loadTransformationProperties(com.nomagic.magicdraw.properties.Style,com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation,com.nomagic.magicdraw.core.Project)">
<h3>loadTransformationProperties</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">loadTransformationProperties</span><wbr/><span class="parameters">(<a href="../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style,
 <a href="ModelTransformationsWizardInformation.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsWizardInformation</a> wi,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
</section>
</li>
<li>
<section class="detail" id="saveTransformationProperties(com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation)">
<h3>saveTransformationProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">saveTransformationProperties</span><wbr/><span class="parameters">(<a href="ModelTransformationsWizardInformation.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationsWizardInformation</a> wizardInformation)</span>
                                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
