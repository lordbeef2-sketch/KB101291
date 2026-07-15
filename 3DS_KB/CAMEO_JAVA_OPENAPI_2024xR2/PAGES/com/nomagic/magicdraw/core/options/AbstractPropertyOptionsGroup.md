# JAVA OPENAPI: AbstractPropertyOptionsGroup (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/core/options/AbstractPropertyOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/AbstractPropertyOptionsGroup.html`
- source_sha256: `fe01cae532122d070ff51d11c88f862df8f9e52f7225fd79504ad194e0ed92b3`
- captured_utc: `2026-07-14T16:55:11.447967+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class AbstractPropertyOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`, `com.nomagic.magicdraw.core.options.VersionedOptionsGroup`

@OpenApipublic abstract classAbstractPropertyOptionsGroup
extends [OptionsGroup](OptionsGroup.html)

Manages editing of properties as options in an application.

See Also:
[`EnvironmentOptions`](EnvironmentOptions.html)
[`OptionsGroup`](OptionsGroup.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractPropertyOptionsGroup](#%3Cinit%3E(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](../../properties/PropertyManager.html) propertyManager)`
Constructs property options group.
`[AbstractPropertyOptionsGroup](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Constructs property options group.
`[AbstractPropertyOptionsGroup](#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [PropertyManager](../../properties/PropertyManager.html) propertyManager,
 boolean visible)`
Constructs property options group.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addInvisibleProperty](#addInvisibleProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds a property which is invisible to the user.
`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds property to this group.
`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property,boolean))([Property](../../properties/Property.html) property,
 boolean generateDescription)`
Adds property to this group.
`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String))([Property](../../properties/Property.html) property,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) descriptionID)`
Adds property with given descriptionID.
`[PropertyManager](../../properties/PropertyManager.html)`
`[getOptions](#getOptions())()`
Gets properties managed by options.
`[Property](../../properties/Property.html)`
`[getProperty](#getProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Gets property by name.
`[PropertyManager](../../properties/PropertyManager.html)`
`[getVisibleOptions](#getVisibleOptions())()`
Gets properties which are visible to the user.
`void`
`[removeProperty](#removeProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Removes a property by name.
`void`
`[setDefaultValues](#setDefaultValues())()`
Sets default values for the properties contained in this group.
`protected void`
`[setOptions](#setOptions(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](../../properties/PropertyManager.html) propertyManager)`
Sets properties for options.
`void`
`[setPropertiesInvisible](#setPropertiesInvisible(java.lang.String%5B%5D,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] ids,
 boolean invisible)`
Sets visibility flag for an array of properties.
`void`
`[setPropertyInvisible](#setPropertyInvisible(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 boolean invisible)`
Changes visibility flag to the property.
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[getGroupIcon](OptionsGroup.html#getGroupIcon()), [getIcon](OptionsGroup.html#getIcon()), [getName](OptionsGroup.html#getName())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractPropertyOptionsGroup
@OpenApipublic AbstractPropertyOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [PropertyManager](../../properties/PropertyManager.html) propertyManager,
 boolean visible)
Constructs property options group.
Parameters:
`id` - id of the group.
`propertyManager` - property options managed by this group.
`visible` - indicates if group is visible to the user.
AbstractPropertyOptionsGroup
@OpenApipublic AbstractPropertyOptionsGroup([PropertyManager](../../properties/PropertyManager.html) propertyManager)
Constructs property options group.
Parameters:
`propertyManager` - property options managed by this group.
AbstractPropertyOptionsGroup
@OpenApipublic AbstractPropertyOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Constructs property options group.
Parameters:
`id` - id of the group.
 ============ METHOD DETAIL ========== 
Method Details
setDefaultValues
@OpenApipublic void setDefaultValues()
Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.
getOptions
@OpenApipublic [PropertyManager](../../properties/PropertyManager.html) getOptions()
Gets properties managed by options.
Returns:
properties managed by options.
getVisibleOptions
@OpenApipublic [PropertyManager](../../properties/PropertyManager.html) getVisibleOptions()
Gets properties which are visible to the user.
Returns:
properties which are visible to the user.
setOptions
@OpenApiprotected void setOptions([PropertyManager](../../properties/PropertyManager.html) propertyManager)
Sets properties for options.
Parameters:
`propertyManager` - property manager to set.
getProperty
@CheckForNull
@OpenApipublic [Property](../../properties/Property.html) getProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Gets property by name.
Parameters:
`name` - name of the property.
Returns:
property found by name.
addProperty
@OpenApipublic void addProperty([Property](../../properties/Property.html) property)
Adds property to this group. DescriptionID will be reset. To add property with description use
 [`addProperty(Property, String)`](#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)) method.
Parameters:
`property` - property to be added.
addProperty
@OpenApipublic void addProperty([Property](../../properties/Property.html) property,
 boolean generateDescription)
Adds property to this group.
 Property description ID will be generated or reset depending on generateDescription parameter value.
 If generateDescription = true, standard description resource ID will be generated by MagicDraw.
 If generateDescription = false, description ID will be set to null.
 To add property with its own description ID use [`addProperty(Property, String)`](#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)) method
Parameters:
`property` - property to add.
`generateDescription` - true if description for property must be generated. Otherwise, description ID will be reset.
addProperty
@OpenApipublic void addProperty([Property](../../properties/Property.html) property,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) descriptionID)
Adds property with given descriptionID.
Parameters:
`property` - property to be added.
`descriptionID` - descriptionID for property.
addInvisibleProperty
@OpenApipublic void addInvisibleProperty([Property](../../properties/Property.html) property)
Adds a property which is invisible to the user.
Parameters:
`property` - property to add.
removeProperty
@OpenApipublic void removeProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Removes a property by name.
Parameters:
`name` - name by which to remove the property.
setPropertyInvisible
@OpenApipublic void setPropertyInvisible([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 boolean invisible)
Changes visibility flag to the property.
Parameters:
`id` - id of the property for which to change visibility.
`invisible` - visibility flag value.
setPropertiesInvisible
@OpenApipublic void setPropertiesInvisible([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] ids,
 boolean invisible)
Sets visibility flag for an array of properties.
Parameters:
`ids` - ids of properties for which to change visibility flag.
`invisible` - visibility flag value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class AbstractPropertyOptionsGroup">Class AbstractPropertyOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></code>, <code>com.nomagic.magicdraw.core.options.VersionedOptionsGroup</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractPropertyOptionsGroup</span>
<span class="extends-implements">extends <a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></span></div>
<div class="block">Manages editing of properties as options in an application.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options"><code>EnvironmentOptions</code></a></li>
<li><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>OptionsGroup</code></a></li>
</ul>
</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.properties.PropertyManager)">AbstractPropertyOptionsGroup</a><wbr/>(<a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs property options group.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">AbstractPropertyOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs property options group.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,boolean)">AbstractPropertyOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 boolean visible)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs property options group.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a property which is invisible to the user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds property to this group.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 boolean generateDescription)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds property to this group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> descriptionID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds property with given descriptionID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets properties managed by options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets property by name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleOptions()">getVisibleOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets properties which are visible to the user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProperty(java.lang.String)">removeProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a property by name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultValues()">setDefaultValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default values for the properties contained in this group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a><wbr/>(<a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets properties for options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] ids,
 boolean invisible)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets visibility flag for an array of properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean invisible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Changes visibility flag to the property.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="OptionsGroup.html#getGroupIcon()">getGroupIcon</a>, <a href="OptionsGroup.html#getIcon()">getIcon</a>, <a href="OptionsGroup.html#getName()">getName</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicdraw.properties.PropertyManager,boolean)">
<h3>AbstractPropertyOptionsGroup</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">AbstractPropertyOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 boolean visible)</span></div>
<div class="block">Constructs property options group.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of the group.</dd>
<dd><code>propertyManager</code> - property options managed by this group.</dd>
<dd><code>visible</code> - indicates if group is visible to the user.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>AbstractPropertyOptionsGroup</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">AbstractPropertyOptionsGroup</span><wbr/><span class="parameters">(<a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</span></div>
<div class="block">Constructs property options group.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyManager</code> - property options managed by this group.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>AbstractPropertyOptionsGroup</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">AbstractPropertyOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Constructs property options group.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of the group.</dd>
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
<section class="detail" id="setDefaultValues()">
<h3>setDefaultValues</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultValues</span>()</div>
<div class="block">Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.</div>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getOptions</span>()</div>
<div class="block">Gets properties managed by options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>properties managed by options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleOptions()">
<h3>getVisibleOptions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getVisibleOptions</span>()</div>
<div class="block">Gets properties which are visible to the user.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>properties which are visible to the user.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOptions(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setOptions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setOptions</span><wbr/><span class="parameters">(<a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</span></div>
<div class="block">Sets properties for options.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyManager</code> - property manager to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Gets property by name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name of the property.</dd>
<dt>Returns:</dt>
<dd>property found by name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addProperty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block">Adds property to this group. DescriptionID will be reset. To add property with description use
 <a href="#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)"><code>addProperty(Property, String)</code></a> method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - property to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property,boolean)">
<h3>addProperty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 boolean generateDescription)</span></div>
<div class="block">Adds property to this group.
 Property description ID will be generated or reset depending on generateDescription parameter value.
 If generateDescription = true, standard description resource ID will be generated by MagicDraw.
 If generateDescription = false, description ID will be set to null.
 To add property with its own description ID use <a href="#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)"><code>addProperty(Property, String)</code></a> method</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - property to add.</dd>
<dd><code>generateDescription</code> - true if description for property must be generated. Otherwise, description ID will be reset.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">
<h3>addProperty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> descriptionID)</span></div>
<div class="block">Adds property with given descriptionID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - property to be added.</dd>
<dd><code>descriptionID</code> - descriptionID for property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addInvisibleProperty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInvisibleProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block">Adds a property which is invisible to the user.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - property to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProperty(java.lang.String)">
<h3>removeProperty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Removes a property by name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name by which to remove the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertyInvisible(java.lang.String,boolean)">
<h3>setPropertyInvisible</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPropertyInvisible</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean invisible)</span></div>
<div class="block">Changes visibility flag to the property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of the property for which to change visibility.</dd>
<dd><code>invisible</code> - visibility flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertiesInvisible(java.lang.String[],boolean)">
<h3>setPropertiesInvisible</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPropertiesInvisible</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] ids,
 boolean invisible)</span></div>
<div class="block">Sets visibility flag for an array of properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ids</code> - ids of properties for which to change visibility flag.</dd>
<dd><code>invisible</code> - visibility flag value.</dd>
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
