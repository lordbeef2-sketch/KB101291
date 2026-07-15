# JAVA OPENAPI: OrganicLayouterOptionsGroup (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/core/options/OrganicLayouterOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/OrganicLayouterOptionsGroup.html`
- source_sha256: `2bfa96608c7efe45497408d79843349ca95a5074e7dc0ea8fe3688d4079b22cf`
- captured_utc: `2026-07-14T16:51:15.242125+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class OrganicLayouterOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
com.nomagic.magicdraw.core.options.OrganicLayouterOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classOrganicLayouterOptionsGroup
extends [AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)

Organic Layouter options group.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`
Fields inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[ALIGNMENT_BOTTOM](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM), [ALIGNMENT_CENTER](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER), [ALIGNMENT_TOP](AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP), [LAYOUT_LABEL_CONSIDERATION](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION), [LAYOUT_LABEL_CONSIDERATION_FULL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL), [LAYOUT_LABEL_CONSIDERATION_NONE](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE), [LAYOUT_LABEL_CONSIDERATION_PARTIAL](AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL), [MAX_INT_VALUE](AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE), [SHAPE_ALIGNMENT](AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OrganicLayouterOptionsGroup](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds property to this group.
`double`
`[getGravityFactor](#getGravityFactor())()`
Get Gravity Factor property value.
`int`
`[getLinkAttraction](#getLinkAttraction())()`
Get Link Attraction property value.
`double`
`[getPackageShapeCompactness](#getPackageShapeCompactness())()`
Get Packages Shape Compactness property value.
`int`
`[getPreferredLinkLength](#getPreferredLinkLength())()`
Get the preferred length of all paths.
`int`
`[getShapeRepulsion](#getShapeRepulsion())()`
Get Shape Repulsion.
`protected void`
`[initCommonDefaultValues](#initCommonDefaultValues())()`

`boolean`
`[isActivateTreeBeautifier](#isActivateTreeBeautifier())()`
Checks Activate Tree Beautifier.
`boolean`
`[isLayoutOnlyTopLevel](#isLayoutOnlyTopLevel())()`
Check Layout Only Top Level property value.
`boolean`
`[isObeyShapeSize](#isObeyShapeSize())()`
Checks The obay Shape Size.
`void`
`[setActivateTreeBeautifier](#setActivateTreeBeautifier(boolean))(boolean b)`
Set Activate Tree Beautifier.
`void`
`[setGravityFactor](#setGravityFactor(double))(double d)`
Set Gravity Factor property value.
`void`
`[setLayoutOnlyTopLevel](#setLayoutOnlyTopLevel(boolean))(boolean b)`
Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.
`void`
`[setLinkAttraction](#setLinkAttraction(int))(int a)`
Set Link Attraction property value.
`void`
`[setObeyShapeSize](#setObeyShapeSize(boolean))(boolean b)`
Set The obey Shape Size.
`void`
`[setPackageShapeCompactness](#setPackageShapeCompactness(double))(double d)`
Set Packages Shape Compactness property value.
`void`
`[setPreferredLinkLength](#setPreferredLinkLength(int))(int len)`
Set the preferred length of all paths.
`void`
`[setShapeRepulsion](#setShapeRepulsion(int))(int a)`
Set Shape Repulsion.
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)
`[getCopy](AbstractDiagramLayouterOptionsGroup.html#getCopy()), [getMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()), [getOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()), [isMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()), [setDefaultValues](AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()), [setMakePreferredLayoutSize](AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)), [setMoveToFreeSpace](AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)), [setOptimizeLabelOrientations](AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [getOptions](AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](AbstractPropertyOptionsGroup.html#getVisibleOptions()), [removeProperty](AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[getGroupIcon](OptionsGroup.html#getGroupIcon()), [getIcon](OptionsGroup.html#getIcon()), [getName](OptionsGroup.html#getName())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ID
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.OrganicLayouterOptionsGroup.ID)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OrganicLayouterOptionsGroup
public OrganicLayouterOptionsGroup()
 ============ METHOD DETAIL ========== 
Method Details
initCommonDefaultValues
protected void initCommonDefaultValues()
Overrides:
`[initCommonDefaultValues](AbstractDiagramLayouterOptionsGroup.html#initCommonDefaultValues())` in class `[AbstractDiagramLayouterOptionsGroup](AbstractDiagramLayouterOptionsGroup.html)`
setPreferredLinkLength
public void setPreferredLinkLength(int len)
Set the preferred length of all paths. The layouter tries to arrange the shapes in such a way that paths have the determined path length.
Parameters:
`len` - The given value.
getPreferredLinkLength
public int getPreferredLinkLength()
Get the preferred length of all paths. The layouter tries to arrange the shapes in such a way that paths have the determined path length.
Returns:
Int value.
setObeyShapeSize
public void setObeyShapeSize(boolean b)
Set The obey Shape Size.
 If True, the distance between two shapes is calculated with respect to shapes' size.
Parameters:
`b` - boolean.
isObeyShapeSize
public boolean isObeyShapeSize()
Checks The obay Shape Size.
 If True, the distance between two shapes is calculated with respect to shapes' size.
Returns:
true if should obey shape size, false otherwise
setActivateTreeBeautifier
public void setActivateTreeBeautifier(boolean b)
Set Activate Tree Beautifier.
 If True, optimizes tree-like substructures of the diagram. Optimization process might ignore some layout options.
Parameters:
`b` - boolean
isActivateTreeBeautifier
public boolean isActivateTreeBeautifier()
Checks Activate Tree Beautifier.
 If True, optimizes tree-like substructures of the diagram. Optimization process might ignore some layout options.
Returns:
boolean
setLayoutOnlyTopLevel
public void setLayoutOnlyTopLevel(boolean b)
Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.
Parameters:
`b` - boolean.
isLayoutOnlyTopLevel
public boolean isLayoutOnlyTopLevel()
Check Layout Only Top Level property value. It indicates position of symbols inside packages is on the top level layout.
Returns:
true if only top level of the diagram should be layouted, false otherwise
setGravityFactor
public void setGravityFactor(double d)
Set Gravity Factor property value.
 This value regulates the tendency of the shapes to be placed near the center of the diagram. The greater factor is the closer shapes are placed to the center of diagram. Negative values lead to huge layouts.
Parameters:
`d` - double.
getGravityFactor
public double getGravityFactor()
Get Gravity Factor property value.
 This value regulates the tendency of the shapes to be placed near the center of the diagram. The greater factor is the closer shapes are placed to the center of diagram. Negative values lead to huge layouts.
Returns:
double
setPackageShapeCompactness
public void setPackageShapeCompactness(double d)
Set Packages Shape Compactness property value.
 This value control the compactness of package shape. Larger values lead to more compact package shapes but paths between packages may be longer and shapes inside packages tend to get clutched together at the center of the package.
Parameters:
`d` - double.
getPackageShapeCompactness
public double getPackageShapeCompactness()
Get Packages Shape Compactness property value.
 This value control the compactness of package shape. Larger values lead to more compact package shapes but paths between packages may be longer and shapes inside packages tend to get clutched together at the center of the package.
Returns:
double
setLinkAttraction
public void setLinkAttraction(int a)
Set Link Attraction property value.
 Higher values makes Layouter obey the given preferred path length.
Parameters:
`a` - int.
getLinkAttraction
public int getLinkAttraction()
Get Link Attraction property value.
 Higher values makes Layouter obey the given preferred path length.
Returns:
int.
setShapeRepulsion
public void setShapeRepulsion(int a)
Set Shape Repulsion.
 Higher values result in greater shape distances.
Parameters:
`a` - the shape repulsion value to set
getShapeRepulsion
public int getShapeRepulsion()
Get Shape Repulsion.
 Higher values result in greater shape distances.
Returns:
int.
addProperty
public void addProperty([Property](../../properties/Property.html) property)
Description copied from class: `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))`
Adds property to this group. DescriptionID will be reset. To add property with description use
 [`AbstractPropertyOptionsGroup.addProperty(Property, String)`](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)) method.
Overrides:
`[addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))` in class `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)`
Parameters:
`property` - property to be added.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class OrganicLayouterOptionsGroup">Class OrganicLayouterOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance"><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.OrganicLayouterOptionsGroup</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">OrganicLayouterOptionsGroup</span>
<span class="extends-implements">extends <a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></span></div>
<div class="block">Organic Layouter options group.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></h3>
<code><a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_BOTTOM">ALIGNMENT_BOTTOM</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_CENTER">ALIGNMENT_CENTER</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#ALIGNMENT_TOP">ALIGNMENT_TOP</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION">LAYOUT_LABEL_CONSIDERATION</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_FULL">LAYOUT_LABEL_CONSIDERATION_FULL</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_NONE">LAYOUT_LABEL_CONSIDERATION_NONE</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#LAYOUT_LABEL_CONSIDERATION_PARTIAL">LAYOUT_LABEL_CONSIDERATION_PARTIAL</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#MAX_INT_VALUE">MAX_INT_VALUE</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#SHAPE_ALIGNMENT">SHAPE_ALIGNMENT</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">OrganicLayouterOptionsGroup</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds property to this group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGravityFactor()">getGravityFactor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Gravity Factor property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkAttraction()">getLinkAttraction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Link Attraction property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPackageShapeCompactness()">getPackageShapeCompactness</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Packages Shape Compactness property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPreferredLinkLength()">getPreferredLinkLength</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the preferred length of all paths.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShapeRepulsion()">getShapeRepulsion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Shape Repulsion.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initCommonDefaultValues()">initCommonDefaultValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isActivateTreeBeautifier()">isActivateTreeBeautifier</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks Activate Tree Beautifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLayoutOnlyTopLevel()">isLayoutOnlyTopLevel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check Layout Only Top Level property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isObeyShapeSize()">isObeyShapeSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks The obay Shape Size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActivateTreeBeautifier(boolean)">setActivateTreeBeautifier</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Activate Tree Beautifier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGravityFactor(double)">setGravityFactor</a><wbr/>(double d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Gravity Factor property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLayoutOnlyTopLevel(boolean)">setLayoutOnlyTopLevel</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLinkAttraction(int)">setLinkAttraction</a><wbr/>(int a)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Link Attraction property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setObeyShapeSize(boolean)">setObeyShapeSize</a><wbr/>(boolean b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set The obey Shape Size.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPackageShapeCompactness(double)">setPackageShapeCompactness</a><wbr/>(double d)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Packages Shape Compactness property value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPreferredLinkLength(int)">setPreferredLinkLength</a><wbr/>(int len)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the preferred length of all paths.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShapeRepulsion(int)">setShapeRepulsion</a><wbr/>(int a)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Shape Repulsion.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></h3>
<code><a href="AbstractDiagramLayouterOptionsGroup.html#getCopy()">getCopy</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#getMakePreferredLayoutSize()">getMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#getOptimizeLabelOrientations()">getOptimizeLabelOrientations</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#isMoveToFreeSpace()">isMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setDefaultValues()">setDefaultValues</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMakePreferredLayoutSize(boolean)">setMakePreferredLayoutSize</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setMoveToFreeSpace(boolean)">setMoveToFreeSpace</a>, <a href="AbstractDiagramLayouterOptionsGroup.html#setOptimizeLabelOrientations(boolean)">setOptimizeLabelOrientations</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="ID">
<h3>ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.OrganicLayouterOptionsGroup.ID">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>OrganicLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OrganicLayouterOptionsGroup</span>()</div>
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
<section class="detail" id="initCommonDefaultValues()">
<h3>initCommonDefaultValues</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">initCommonDefaultValues</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouterOptionsGroup.html#initCommonDefaultValues()">initCommonDefaultValues</a></code> in class <code><a href="AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreferredLinkLength(int)">
<h3>setPreferredLinkLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPreferredLinkLength</span><wbr/><span class="parameters">(int len)</span></div>
<div class="block">Set the preferred length of all paths. The layouter tries to arrange the shapes in such a way that paths have the determined path length.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>len</code> - The given value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreferredLinkLength()">
<h3>getPreferredLinkLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPreferredLinkLength</span>()</div>
<div class="block">Get the preferred length of all paths. The layouter tries to arrange the shapes in such a way that paths have the determined path length.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Int value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setObeyShapeSize(boolean)">
<h3>setObeyShapeSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setObeyShapeSize</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set The obey Shape Size.
 If True, the distance between two shapes is calculated with respect to shapes' size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isObeyShapeSize()">
<h3>isObeyShapeSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isObeyShapeSize</span>()</div>
<div class="block">Checks The obay Shape Size.
 If True, the distance between two shapes is calculated with respect to shapes' size.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if should obey shape size, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActivateTreeBeautifier(boolean)">
<h3>setActivateTreeBeautifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActivateTreeBeautifier</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Activate Tree Beautifier.
 If True, optimizes tree-like substructures of the diagram. Optimization process might ignore some layout options.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isActivateTreeBeautifier()">
<h3>isActivateTreeBeautifier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isActivateTreeBeautifier</span>()</div>
<div class="block">Checks Activate Tree Beautifier.
 If True, optimizes tree-like substructures of the diagram. Optimization process might ignore some layout options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLayoutOnlyTopLevel(boolean)">
<h3>setLayoutOnlyTopLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayoutOnlyTopLevel</span><wbr/><span class="parameters">(boolean b)</span></div>
<div class="block">Set Layout Only Top Level property value in order to keeps the relative position of symbols inside packages and performs the top level layout.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLayoutOnlyTopLevel()">
<h3>isLayoutOnlyTopLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLayoutOnlyTopLevel</span>()</div>
<div class="block">Check Layout Only Top Level property value. It indicates position of symbols inside packages is on the top level layout.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if only top level of the diagram should be layouted, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGravityFactor(double)">
<h3>setGravityFactor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGravityFactor</span><wbr/><span class="parameters">(double d)</span></div>
<div class="block">Set Gravity Factor property value.
 This value regulates the tendency of the shapes to be placed near the center of the diagram. The greater factor is the closer shapes are placed to the center of diagram. Negative values lead to huge layouts.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - double.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGravityFactor()">
<h3>getGravityFactor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getGravityFactor</span>()</div>
<div class="block">Get Gravity Factor property value.
 This value regulates the tendency of the shapes to be placed near the center of the diagram. The greater factor is the closer shapes are placed to the center of diagram. Negative values lead to huge layouts.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>double</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPackageShapeCompactness(double)">
<h3>setPackageShapeCompactness</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPackageShapeCompactness</span><wbr/><span class="parameters">(double d)</span></div>
<div class="block">Set Packages Shape Compactness property value.
 This value control the compactness of package shape. Larger values lead to more compact package shapes but paths between packages may be longer and shapes inside packages tend to get clutched together at the center of the package.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>d</code> - double.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageShapeCompactness()">
<h3>getPackageShapeCompactness</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getPackageShapeCompactness</span>()</div>
<div class="block">Get Packages Shape Compactness property value.
 This value control the compactness of package shape. Larger values lead to more compact package shapes but paths between packages may be longer and shapes inside packages tend to get clutched together at the center of the package.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>double</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLinkAttraction(int)">
<h3>setLinkAttraction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLinkAttraction</span><wbr/><span class="parameters">(int a)</span></div>
<div class="block">Set Link Attraction property value.
 Higher values makes Layouter obey the given preferred path length.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - int.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLinkAttraction()">
<h3>getLinkAttraction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLinkAttraction</span>()</div>
<div class="block">Get Link Attraction property value.
 Higher values makes Layouter obey the given preferred path length.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShapeRepulsion(int)">
<h3>setShapeRepulsion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShapeRepulsion</span><wbr/><span class="parameters">(int a)</span></div>
<div class="block">Set Shape Repulsion.
 Higher values result in greater shape distances.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - the shape repulsion value to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getShapeRepulsion()">
<h3>getShapeRepulsion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getShapeRepulsion</span>()</div>
<div class="block">Get Shape Repulsion.
 Higher values result in greater shape distances.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>int.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">AbstractPropertyOptionsGroup</a></code></span></div>
<div class="block">Adds property to this group. DescriptionID will be reset. To add property with description use
 <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)"><code>AbstractPropertyOptionsGroup.addProperty(Property, String)</code></a> method.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a></code> in class <code><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></code></dd>
<dt>Parameters:</dt>
<dd><code>property</code> - property to be added.</dd>
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
