# JAVA OPENAPI: ModelTransformationsWizardInformation (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/modeltransformations/ModelTransformationsWizardInformation.html
- source_path: `com/nomagic/magicdraw/modeltransformations/ModelTransformationsWizardInformation.html`
- source_sha256: `a98e652691f0f9736cbb31b7f974a343c9e5311b7f5144efe93b1da542982c96`
- captured_utc: `2026-07-14T16:51:25.828265+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modeltransformations](package-summary.html)

## Class ModelTransformationsWizardInformation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation
com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation

@OpenApiAllpublic classModelTransformationsWizardInformation
extends com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation
Model Transformations Wizard Information

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation
`DEFAULT_DEPRECATED_PROPERTIES, DEFAULT_RELATIONSHIPS`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ModelTransformationsWizardInformation](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)>`
`[getFilteredObjects](#getFilteredObjects())()`
Returns collection of legal selected objects
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLastSelectedTransformationName](#getLastSelectedTransformationName())()`
Returns last selected transformation name
`boolean`
`[getLastSelectedTypeMapDirection](#getLastSelectedTypeMapDirection())()`
Returns last selected type map direction
`[ModelTransformationInfo](ModelTransformationInfo.html)`
`[getModelTransformationInfo](#getModelTransformationInfo())()`
Getter for Model Transformation Info
`[PropertyManager](../properties/PropertyManager.html)`
`[getPropertyManager](#getPropertyManager())()`
Returns property manager
`[TypeMapProfile](TypeMapProfile.html)`
`[getSelectedTypeMapProfile](#getSelectedTypeMapProfile())()`
Returns selected type map profile
`[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getTargetPackage](#getTargetPackage())()`
Getter for target package
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModelTransformationInfo](ModelTransformationInfo.html)>`
`[getTransformations](#getTransformations())()`

`[TypeMapProfile](TypeMapProfile.html)[]`
`[getTypeMapProfiles](#getTypeMapProfiles())()`
Returns loaded type map profiles
`boolean`
`[isTransformationPrepared](#isTransformationPrepared())()`
Checks if transformation is prepared
`boolean`
`[isTransformInPlace](#isTransformInPlace())()`
Getter for transformation in place
`void`
`[loadProperties](#loadProperties())()`
Loads environmental properties
`void`
`[resetPropertyManager](#resetPropertyManager())()`
Resets property manager
`void`
`[saveSettings](#saveSettings())()`
Saves transformation environmental and project info
`void`
`[setModelTransformationInfo](#setModelTransformationInfo(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo))([ModelTransformationInfo](ModelTransformationInfo.html) info)`
Setter for Model Transformation Info
`void`
`[setPropertyManager](#setPropertyManager(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](../properties/PropertyManager.html) propertyManager)`
Sets property manager
`void`
`[setSelectedTypeMapProfile](#setSelectedTypeMapProfile(com.nomagic.magicdraw.modeltransformations.TypeMapProfile))([TypeMapProfile](TypeMapProfile.html) tmp)`
Set the selected type map profile.
`void`
`[setShowWarningForSourceSelectedAsDestination](#setShowWarningForSourceSelectedAsDestination(boolean))(boolean show)`
Set show warning status for source selection as destination
`void`
`[setShowWarningForTransformationInPlace](#setShowWarningForTransformationInPlace(boolean))(boolean show)`
Set show warning status for transformation in place
`void`
`[setTargetPackage](#setTargetPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) mp)`
Setter for target package
`void`
`[setTransformationPrepared](#setTransformationPrepared(boolean))(boolean transformationPrepared)`
Set transformation status
`void`
`[setTransformations](#setTransformations(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModelTransformationInfo](ModelTransformationInfo.html)> transformations)`
Setting the Transformations that will appear in the SelectTransformationTypePanel
`void`
`[setTransformInPlace](#setTransformInPlace(boolean))(boolean transformInPlace)`
Setter for transformation in place
`boolean`
`[showWarningForSourceSelectedAsDestination](#showWarningForSourceSelectedAsDestination())()`
Do we need to show warning for source selection as destination
`boolean`
`[showWarningForTransformationInPlace](#showWarningForTransformationInPlace())()`
Do we need to show warning for transformation in place
Methods inherited from class com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation
`addSymbolProperties, createElementsStylesMap, getCreatableElementTypes, getCreatableTypes, getDeprecatedSymbolPropertiesIDs, getDiagramType, getFirstDiagramType, getName, getObjects, getParent, getSelectableTypes, getSelectedRelationships, getSymbolProperties, setCreatableElementTypes, setCreatableTypes, setDeprecatedSymbolPropertiesIDs, setDiagramType, setDiagramType, setName, setObjects, setParent, setSelectableTypes, setSymbolProperties`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ModelTransformationsWizardInformation
public ModelTransformationsWizardInformation()
 ============ METHOD DETAIL ========== 
Method Details
saveSettings
public void saveSettings()
Saves transformation environmental and project info
loadProperties
public void loadProperties()
Loads environmental properties
getPropertyManager
public [PropertyManager](../properties/PropertyManager.html) getPropertyManager()
Returns property manager
Returns:
property manager
setPropertyManager
public void setPropertyManager([PropertyManager](../properties/PropertyManager.html) propertyManager)
Sets property manager
Parameters:
`propertyManager` - properties
resetPropertyManager
public void resetPropertyManager()
Resets property manager
getTypeMapProfiles
public [TypeMapProfile](TypeMapProfile.html)[] getTypeMapProfiles()
Returns loaded type map profiles
Returns:
array of type map profiles
getLastSelectedTypeMapDirection
public boolean getLastSelectedTypeMapDirection()
Returns last selected type map direction
Returns:
last selected type map direction
getLastSelectedTransformationName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLastSelectedTransformationName()
Returns last selected transformation name
Returns:
last selected transformation name
isTransformationPrepared
public boolean isTransformationPrepared()
Checks if transformation is prepared
Returns:
true if transformation is prepared
setTransformationPrepared
public void setTransformationPrepared(boolean transformationPrepared)
Set transformation status
Parameters:
`transformationPrepared` - true for prepared
getModelTransformationInfo
public [ModelTransformationInfo](ModelTransformationInfo.html) getModelTransformationInfo()
Getter for Model Transformation Info
Returns:
Model Transformation Info
setModelTransformationInfo
public void setModelTransformationInfo([ModelTransformationInfo](ModelTransformationInfo.html) info)
Setter for Model Transformation Info
Parameters:
`info` - Model Transformation Info
setTargetPackage
public void setTargetPackage(@CheckForNull
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) mp)
Setter for target package
Parameters:
`mp` - target package
getTargetPackage
public [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getTargetPackage()
Getter for target package
Returns:
target package
setTransformInPlace
public void setTransformInPlace(boolean transformInPlace)
Setter for transformation in place
Parameters:
`transformInPlace` - true if transformation in place
isTransformInPlace
public boolean isTransformInPlace()
Getter for transformation in place
Returns:
true if transformation in place
setSelectedTypeMapProfile
public void setSelectedTypeMapProfile(@CheckForNull
 [TypeMapProfile](TypeMapProfile.html) tmp)
Set the selected type map profile.
Parameters:
`tmp` - TypeMapProfile.
getSelectedTypeMapProfile
@CheckForNullpublic [TypeMapProfile](TypeMapProfile.html) getSelectedTypeMapProfile()
Returns selected type map profile
Returns:
selected type map profile
showWarningForTransformationInPlace
public boolean showWarningForTransformationInPlace()
Do we need to show warning for transformation in place
Returns:
true if need to show warning
setShowWarningForTransformationInPlace
public void setShowWarningForTransformationInPlace(boolean show)
Set show warning status for transformation in place
Parameters:
`show` - warning status
showWarningForSourceSelectedAsDestination
public boolean showWarningForSourceSelectedAsDestination()
Do we need to show warning for source selection as destination
Returns:
true if need to show warning
setShowWarningForSourceSelectedAsDestination
public void setShowWarningForSourceSelectedAsDestination(boolean show)
Set show warning status for source selection as destination
Parameters:
`show` - warning status
getFilteredObjects
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)> getFilteredObjects()
Returns collection of legal selected objects
Returns:
collection of legal selected objects
getTransformations
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModelTransformationInfo](ModelTransformationInfo.html)> getTransformations()
setTransformations
public void setTransformations([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModelTransformationInfo](ModelTransformationInfo.html)> transformations)
Setting the Transformations that will appear in the SelectTransformationTypePanel
Parameters:
`transformations` - a collection of ModelTransformationInfos

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modeltransformations</a></div>
<h1 class="title" title="Class ModelTransformationsWizardInformation">Class ModelTransformationsWizardInformation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation
<div class="inheritance">com.nomagic.magicdraw.modeltransformations.ModelTransformationsWizardInformation</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ModelTransformationsWizardInformation</span>
<span class="extends-implements">extends com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation</span></div>
<div class="block">Model Transformations Wizard Information</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation">Fields inherited from class com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation</h3>
<code>DEFAULT_DEPRECATED_PROPERTIES, DEFAULT_RELATIONSHIPS</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ModelTransformationsWizardInformation</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilteredObjects()">getFilteredObjects</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns collection of legal selected objects</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedTransformationName()">getLastSelectedTransformationName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last selected transformation name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedTypeMapDirection()">getLastSelectedTypeMapDirection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last selected type map direction</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelTransformationInfo()">getModelTransformationInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for Model Transformation Info</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyManager()">getPropertyManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedTypeMapProfile()">getSelectedTypeMapProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns selected type map profile</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetPackage()">getTargetPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for target package</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformations()">getTransformations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeMapProfiles()">getTypeMapProfiles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns loaded type map profiles</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTransformationPrepared()">isTransformationPrepared</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if transformation is prepared</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTransformInPlace()">isTransformInPlace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for transformation in place</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadProperties()">loadProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads environmental properties</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetPropertyManager()">resetPropertyManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resets property manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveSettings()">saveSettings</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves transformation environmental and project info</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setModelTransformationInfo(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo)">setModelTransformationInfo</a><wbr/>(<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Setter for Model Transformation Info</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertyManager(com.nomagic.magicdraw.properties.PropertyManager)">setPropertyManager</a><wbr/>(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets property manager</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSelectedTypeMapProfile(com.nomagic.magicdraw.modeltransformations.TypeMapProfile)">setSelectedTypeMapProfile</a><wbr/>(<a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> tmp)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the selected type map profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowWarningForSourceSelectedAsDestination(boolean)">setShowWarningForSourceSelectedAsDestination</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set show warning status for source selection as destination</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowWarningForTransformationInPlace(boolean)">setShowWarningForTransformationInPlace</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set show warning status for transformation in place</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTargetPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setTargetPackage</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> mp)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Setter for target package</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTransformationPrepared(boolean)">setTransformationPrepared</a><wbr/>(boolean transformationPrepared)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set transformation status</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTransformations(java.util.Collection)">setTransformations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a>&gt; transformations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Setting the Transformations that will appear in the SelectTransformationTypePanel</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTransformInPlace(boolean)">setTransformInPlace</a><wbr/>(boolean transformInPlace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Setter for transformation in place</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showWarningForSourceSelectedAsDestination()">showWarningForSourceSelectedAsDestination</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Do we need to show warning for source selection as destination</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showWarningForTransformationInPlace()">showWarningForTransformationInPlace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Do we need to show warning for transformation in place</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation">Methods inherited from class com.nomagic.magicdraw.ui.dialogs.wizards.WizardInformation</h3>
<code>addSymbolProperties, createElementsStylesMap, getCreatableElementTypes, getCreatableTypes, getDeprecatedSymbolPropertiesIDs, getDiagramType, getFirstDiagramType, getName, getObjects, getParent, getSelectableTypes, getSelectedRelationships, getSymbolProperties, setCreatableElementTypes, setCreatableTypes, setDeprecatedSymbolPropertiesIDs, setDiagramType, setDiagramType, setName, setObjects, setParent, setSelectableTypes, setSymbolProperties</code></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>ModelTransformationsWizardInformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModelTransformationsWizardInformation</span>()</div>
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
<section class="detail" id="saveSettings()">
<h3>saveSettings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">saveSettings</span>()</div>
<div class="block">Saves transformation environmental and project info</div>
</section>
</li>
<li>
<section class="detail" id="loadProperties()">
<h3>loadProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadProperties</span>()</div>
<div class="block">Loads environmental properties</div>
</section>
</li>
<li>
<section class="detail" id="getPropertyManager()">
<h3>getPropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getPropertyManager</span>()</div>
<div class="block">Returns property manager</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertyManager(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setPropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPropertyManager</span><wbr/><span class="parameters">(<a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</span></div>
<div class="block">Sets property manager</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyManager</code> - properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetPropertyManager()">
<h3>resetPropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetPropertyManager</span>()</div>
<div class="block">Resets property manager</div>
</section>
</li>
<li>
<section class="detail" id="getTypeMapProfiles()">
<h3>getTypeMapProfiles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a>[]</span> <span class="element-name">getTypeMapProfiles</span>()</div>
<div class="block">Returns loaded type map profiles</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>array of type map profiles</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedTypeMapDirection()">
<h3>getLastSelectedTypeMapDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getLastSelectedTypeMapDirection</span>()</div>
<div class="block">Returns last selected type map direction</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>last selected type map direction</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedTransformationName()">
<h3>getLastSelectedTransformationName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastSelectedTransformationName</span>()</div>
<div class="block">Returns last selected transformation name</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>last selected transformation name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTransformationPrepared()">
<h3>isTransformationPrepared</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTransformationPrepared</span>()</div>
<div class="block">Checks if transformation is prepared</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if transformation is prepared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTransformationPrepared(boolean)">
<h3>setTransformationPrepared</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTransformationPrepared</span><wbr/><span class="parameters">(boolean transformationPrepared)</span></div>
<div class="block">Set transformation status</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformationPrepared</code> - true for prepared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModelTransformationInfo()">
<h3>getModelTransformationInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></span> <span class="element-name">getModelTransformationInfo</span>()</div>
<div class="block">Getter for Model Transformation Info</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Model Transformation Info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setModelTransformationInfo(com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo)">
<h3>setModelTransformationInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setModelTransformationInfo</span><wbr/><span class="parameters">(<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info)</span></div>
<div class="block">Setter for Model Transformation Info</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>info</code> - Model Transformation Info</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>setTargetPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTargetPackage</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> mp)</span></div>
<div class="block">Setter for target package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mp</code> - target package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetPackage()">
<h3>getTargetPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getTargetPackage</span>()</div>
<div class="block">Getter for target package</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTransformInPlace(boolean)">
<h3>setTransformInPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTransformInPlace</span><wbr/><span class="parameters">(boolean transformInPlace)</span></div>
<div class="block">Setter for transformation in place</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformInPlace</code> - true if transformation in place</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTransformInPlace()">
<h3>isTransformInPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTransformInPlace</span>()</div>
<div class="block">Getter for transformation in place</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if transformation in place</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelectedTypeMapProfile(com.nomagic.magicdraw.modeltransformations.TypeMapProfile)">
<h3>setSelectedTypeMapProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedTypeMapProfile</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> tmp)</span></div>
<div class="block">Set the selected type map profile.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tmp</code> - TypeMapProfile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedTypeMapProfile()">
<h3>getSelectedTypeMapProfile</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a></span> <span class="element-name">getSelectedTypeMapProfile</span>()</div>
<div class="block">Returns selected type map profile</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>selected type map profile</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showWarningForTransformationInPlace()">
<h3>showWarningForTransformationInPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showWarningForTransformationInPlace</span>()</div>
<div class="block">Do we need to show warning for transformation in place</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if need to show warning</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowWarningForTransformationInPlace(boolean)">
<h3>setShowWarningForTransformationInPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowWarningForTransformationInPlace</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Set show warning status for transformation in place</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>show</code> - warning status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showWarningForSourceSelectedAsDestination()">
<h3>showWarningForSourceSelectedAsDestination</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showWarningForSourceSelectedAsDestination</span>()</div>
<div class="block">Do we need to show warning for source selection as destination</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if need to show warning</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowWarningForSourceSelectedAsDestination(boolean)">
<h3>setShowWarningForSourceSelectedAsDestination</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowWarningForSourceSelectedAsDestination</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Set show warning status for source selection as destination</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>show</code> - warning status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFilteredObjects()">
<h3>getFilteredObjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getFilteredObjects</span>()</div>
<div class="block">Returns collection of legal selected objects</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of legal selected objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransformations()">
<h3>getTransformations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a>&gt;</span> <span class="element-name">getTransformations</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setTransformations(java.util.Collection)">
<h3>setTransformations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTransformations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a>&gt; transformations)</span></div>
<div class="block">Setting the Transformations that will appear in the SelectTransformationTypePanel</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformations</code> - a collection of ModelTransformationInfos</dd>
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
