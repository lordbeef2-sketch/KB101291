# JAVA OPENAPI: ExtendablePropertyManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/properties/ExtendablePropertyManager.html
- source_path: `com/nomagic/magicdraw/properties/ExtendablePropertyManager.html`
- source_sha256: `79e704e32aeca8d306ab45930cdd8b5a10b1d82c891561c0748234d979b3477e`
- captured_utc: `2026-07-14T16:58:00.385561+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class ExtendablePropertyManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.properties.PropertyManager](PropertyManager.html)
com.nomagic.magicdraw.properties.ExtendablePropertyManager

All Implemented Interfaces:
`[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[PropertyManagerByDiagram](PropertyManagerByDiagram.html)`, `[PropertyManagerByStereotype](PropertyManagerByStereotype.html)`

@OpenApiAllpublic classExtendablePropertyManager
extends [PropertyManager](PropertyManager.html)

Property manager which can be specified by another property manager.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected boolean`
`[removable](#removable)`
Some property managers by diagram should be fixed and not allowed to be removed.
Fields inherited from class com.nomagic.magicdraw.properties.[PropertyManager](PropertyManager.html)
`[IS_UNIQUE](PropertyManager.html#IS_UNIQUE), [OWN_PROPERTY_ADDED](PropertyManager.html#OWN_PROPERTY_ADDED), [OWN_PROPERTY_REMOVED](PropertyManager.html#OWN_PROPERTY_REMOVED)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ExtendablePropertyManager](#%3Cinit%3E())()`
Construct ExtendablePropertyManager
`[ExtendablePropertyManager](#%3Cinit%3E(boolean,boolean))(boolean extendableByDiagram,
 boolean extendableByStereotype)`
Construct ExtendablePropertyManager with given arguments.
`[ExtendablePropertyManager](#%3Cinit%3E(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,java.util.List))([PropertyManager](PropertyManager.html) parentPropertyManager,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)`
Construct ExtendablePropertyManager with the given argument.
`[ExtendablePropertyManager](#%3Cinit%3E(java.lang.String,java.util.List))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)`
Construct ExtendablePropertyManager with given arguments.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) visitor)`
Accepts the given visitor.
`boolean`
`[elementIsAllowed](#elementIsAllowed(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](../uml/DiagramType.html) diagramType)`
Checks If element is allowed by diagram type.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`com.nomagic.ci.persistence.IProject`
`[getDefinedIn](#getDefinedIn())()`

`[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[]`
`[getSymbolType](#getSymbolType())()`
Get Symbol type.
`boolean`
`[isExtendableByDiagram](#isExtendableByDiagram())()`
Tests If ExtendablePropertyManager is ExtendableByDiagram.
`boolean`
`[isExtendableByStereotype](#isExtendableByStereotype())()`
Tests If ExtendablePropertyManager is ExtendableByStereotype.
`boolean`
`[isRemovable](#isRemovable())()`
Tests Manager is removable.
`[PropertyManager](PropertyManager.html)`
`[makeCopy](#makeCopy())()`
Make copy of property.
`void`
`[setDefinedIn](#setDefinedIn(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject definedIn)`
Set project where this module is read from.
`void`
`[setExtendableByDiagram](#setExtendableByDiagram(boolean))(boolean extendableByDiagram)`
Sets this manager extendable by diagram.
`void`
`[setExtendableByStereotype](#setExtendableByStereotype(boolean))(boolean extendableByStereotype)`
Sets this manager extendable by stereotype.
`void`
`[setRemovable](#setRemovable(boolean))(boolean removable)`
Set Removable flag.
`void`
`[setSymbolType](#setSymbolType(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) symbolType)`
Set symbol type.
`void`
`[setSymbolType](#setSymbolType(java.lang.Class%5B%5D))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] symbolType)`
Set symbol type.
Methods inherited from class com.nomagic.magicdraw.properties.[PropertyManager](PropertyManager.html)
`[addProperties](PropertyManager.html#addProperties(java.util.Collection)), [addProperty](PropertyManager.html#addProperty(com.nomagic.magicdraw.properties.Property)), [addPropertyChangeListener](PropertyManager.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [append](PropertyManager.html#append(com.nomagic.magicdraw.properties.PropertyManager)), [append](PropertyManager.html#append(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)), [append](PropertyManager.html#append(java.util.List)), [append](PropertyManager.html#append(java.util.List,boolean,boolean)), [apply](PropertyManager.html#apply(com.nomagic.magicdraw.properties.PropertyManager)), [apply](PropertyManager.html#apply(java.util.Collection)), [applyValues](PropertyManager.html#applyValues(java.util.Collection)), [clone](PropertyManager.html#clone()), [cloneProperties](PropertyManager.html#cloneProperties(java.util.List)), [distinct](PropertyManager.html#distinct(com.nomagic.magicdraw.properties.PropertyManager)), [distinct](PropertyManager.html#distinct(java.util.List)), [equalsTo](PropertyManager.html#equalsTo(com.nomagic.magicdraw.properties.PropertyManager)), [equalsWithValues](PropertyManager.html#equalsWithValues(com.nomagic.magicdraw.properties.PropertyManager,java.util.Set)), [generateDefaultDescriptionID](PropertyManager.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.PropertyManager)), [generateNullDescriptionID](PropertyManager.html#generateNullDescriptionID(com.nomagic.magicdraw.properties.PropertyManager)), [getHiddenProperties](PropertyManager.html#getHiddenProperties()), [getID](PropertyManager.html#getID()), [getName](PropertyManager.html#getName()), [getOrderedProperties](PropertyManager.html#getOrderedProperties()), [getOwnProperties](PropertyManager.html#getOwnProperties()), [getParentPropertyManager](PropertyManager.html#getParentPropertyManager()), [getProperties](PropertyManager.html#getProperties()), [getProperty](PropertyManager.html#getProperty(java.lang.String)), [getPropertyByName](PropertyManager.html#getPropertyByName(java.lang.String)), [getStyle](PropertyManager.html#getStyle()), [hideParentProperty](PropertyManager.html#hideParentProperty(java.lang.String)), [isFrozen](PropertyManager.html#isFrozen()), [isHiddenParentProperty](PropertyManager.html#isHiddenParentProperty(java.lang.String)), [isTheSame](PropertyManager.html#isTheSame(com.nomagic.magicdraw.properties.PropertyManager)), [isUndefinedStateOrValuesDiffer](PropertyManager.html#isUndefinedStateOrValuesDiffer(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property)), [leaveTheSame](PropertyManager.html#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager)), [leaveTheSame](PropertyManager.html#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)), [makeOwnProperty](PropertyManager.html#makeOwnProperty(com.nomagic.magicdraw.properties.Property)), [mergeBooleanProperty](PropertyManager.html#mergeBooleanProperty(com.nomagic.magicdraw.properties.BooleanProperty,com.nomagic.magicdraw.properties.BooleanProperty)), [mergeChoiceProperty](PropertyManager.html#mergeChoiceProperty(com.nomagic.magicdraw.properties.ChoiceProperty,com.nomagic.magicdraw.properties.ChoiceProperty)), [mergeElementProperty](PropertyManager.html#mergeElementProperty(com.nomagic.magicdraw.properties.ElementProperty,com.nomagic.magicdraw.properties.ElementProperty)), [mergeProperties](PropertyManager.html#mergeProperties(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property,boolean,boolean)), [mergePropertyByType](PropertyManager.html#mergePropertyByType(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property)), [propertyChange](PropertyManager.html#propertyChange(java.beans.PropertyChangeEvent)), [removeProperty](PropertyManager.html#removeProperty(com.nomagic.magicdraw.properties.Property)), [removeProperty](PropertyManager.html#removeProperty(java.lang.String)), [removeProperty](PropertyManager.html#removeProperty(java.util.Collection)), [removePropertyChangeListener](PropertyManager.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [retainProperties](PropertyManager.html#retainProperties(java.util.Collection)), [setFrozen](PropertyManager.html#setFrozen(boolean)), [setID](PropertyManager.html#setID(java.lang.String)), [setName](PropertyManager.html#setName(java.lang.String)), [setParentPropertyManager](PropertyManager.html#setParentPropertyManager(com.nomagic.magicdraw.properties.PropertyManager)), [setParentPropertyManagerOnly](PropertyManager.html#setParentPropertyManagerOnly(com.nomagic.magicdraw.properties.PropertyManager)), [setProperties](PropertyManager.html#setProperties(java.util.List)), [setPropertyEnableMap](PropertyManager.html#setPropertyEnableMap(java.lang.String,java.lang.Object%5B%5D%5B%5D)), [setStyle](PropertyManager.html#setStyle(com.nomagic.magicdraw.properties.Style)), [sGetID](PropertyManager.html#sGetID()), [shareProperty](PropertyManager.html#shareProperty(com.nomagic.magicdraw.properties.Property)), [showParentProperty](PropertyManager.html#showParentProperty(java.lang.String)), [toString](PropertyManager.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
removable
protected boolean removable
Some property managers by diagram should be fixed and not allowed to be removed.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ExtendablePropertyManager
public ExtendablePropertyManager()
Construct ExtendablePropertyManager
ExtendablePropertyManager
public ExtendablePropertyManager([PropertyManager](PropertyManager.html) parentPropertyManager,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)
Construct ExtendablePropertyManager with the given argument.
Parameters:
`parentPropertyManager` - Parent of this Property manager
`name` - ExtendablePropertyManager 's name.
`properties` - List of properties.
ExtendablePropertyManager
public ExtendablePropertyManager([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)
Construct ExtendablePropertyManager with given arguments.
Parameters:
`name` - Property manager name.
`properties` - List of property.
ExtendablePropertyManager
public ExtendablePropertyManager(boolean extendableByDiagram,
 boolean extendableByStereotype)
Construct ExtendablePropertyManager with given arguments.
Parameters:
`extendableByDiagram` - extendable by diagram
`extendableByStereotype` - extendable by stereotype
 ============ METHOD DETAIL ========== 
Method Details
isExtendableByDiagram
public boolean isExtendableByDiagram()
Tests If ExtendablePropertyManager is ExtendableByDiagram.
Returns:
true if this manager can be extended for diagram.
setExtendableByDiagram
public void setExtendableByDiagram(boolean extendableByDiagram)
Sets this manager extendable by diagram.
Parameters:
`extendableByDiagram` - value
isExtendableByStereotype
public boolean isExtendableByStereotype()
Tests If ExtendablePropertyManager is ExtendableByStereotype.
Returns:
true if this manager can be extended by stereotype.
setExtendableByStereotype
public void setExtendableByStereotype(boolean extendableByStereotype)
Sets this manager extendable by stereotype.
Parameters:
`extendableByStereotype` - value
accept
public void accept([PropertyVisitor](PropertyVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Description copied from class: `[PropertyManager](PropertyManager.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))`
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[accept](PropertyManager.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in class `[PropertyManager](PropertyManager.html)`
Parameters:
`visitor` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
See Also:
[`PropertyManager.accept(com.nomagic.magicdraw.properties.PropertyVisitor)`](PropertyManager.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))
getClassType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getClassType()
Description copied from class: `[PropertyManager](PropertyManager.html#getClassType())`
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Overrides:
`[getClassType](PropertyManager.html#getClassType())` in class `[PropertyManager](PropertyManager.html)`
Returns:
PropertyID.PROPERTY_MANAGER
See Also:
[`PropertyVisitorAcceptor.getClassType()`](PropertyVisitorAcceptor.html#getClassType())
setSymbolType
public void setSymbolType([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) symbolType)
Set symbol type. If set null manager can be used for diagrams.
Parameters:
`symbolType` - symbol type
setSymbolType
public void setSymbolType([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] symbolType)
Set symbol type. If set null manager can be used for diagrams.
Parameters:
`symbolType` - symbol types
getSymbolType
public [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)[] getSymbolType()
Get Symbol type.
Returns:
symbol type.
isRemovable
public boolean isRemovable()
Tests Manager is removable.
Returns:
true if manager can be removed using GUI.
setRemovable
public void setRemovable(boolean removable)
Set Removable flag.
Parameters:
`removable` - true if manager can be removed using GUI.
elementIsAllowed
public boolean elementIsAllowed([DiagramType](../uml/DiagramType.html) diagramType)
Checks If element is allowed by diagram type.
Parameters:
`diagramType` - The given diagram type.
Returns:
boolean
makeCopy
public [PropertyManager](PropertyManager.html) makeCopy()
Description copied from class: `[PropertyManager](PropertyManager.html#makeCopy())`
Make copy of property.
Overrides:
`[makeCopy](PropertyManager.html#makeCopy())` in class `[PropertyManager](PropertyManager.html)`
Returns:
Property Manager.
getDefinedIn
@CheckForNullpublic com.nomagic.ci.persistence.IProject getDefinedIn()
Returns:
module or project where this manager is defined (read from). In case manager is defined
 in primary project it may return null.
setDefinedIn
public void setDefinedIn(@CheckForNull
 com.nomagic.ci.persistence.IProject definedIn)
Set project where this module is read from.
Parameters:
`definedIn` - project where module is defined.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class ExtendablePropertyManager">Class ExtendablePropertyManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">com.nomagic.magicdraw.properties.PropertyManager</a>
<div class="inheritance">com.nomagic.magicdraw.properties.ExtendablePropertyManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="PropertyManagerByDiagram.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByDiagram</a></code>, <code><a href="PropertyManagerByStereotype.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByStereotype</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ExtendablePropertyManager</span>
<span class="extends-implements">extends <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span></div>
<div class="block">Property manager which can be specified by another property manager.</div>
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
<div class="col-first even-row-color"><code>protected boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#removable">removable</a></code></div>
<div class="col-last even-row-color">
<div class="block">Some property managers by diagram should be fixed and not allowed to be removed.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.properties.PropertyManager">Fields inherited from class com.nomagic.magicdraw.properties.<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></h3>
<code><a href="PropertyManager.html#IS_UNIQUE">IS_UNIQUE</a>, <a href="PropertyManager.html#OWN_PROPERTY_ADDED">OWN_PROPERTY_ADDED</a>, <a href="PropertyManager.html#OWN_PROPERTY_REMOVED">OWN_PROPERTY_REMOVED</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ExtendablePropertyManager</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Construct ExtendablePropertyManager</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean,boolean)">ExtendablePropertyManager</a><wbr/>(boolean extendableByDiagram,
 boolean extendableByStereotype)</code></div>
<div class="col-last odd-row-color">
<div class="block">Construct ExtendablePropertyManager with given arguments.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,java.util.List)">ExtendablePropertyManager</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> parentPropertyManager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last even-row-color">
<div class="block">Construct ExtendablePropertyManager with the given argument.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.util.List)">ExtendablePropertyManager</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last odd-row-color">
<div class="block">Construct ExtendablePropertyManager with given arguments.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts the given visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#elementIsAllowed(com.nomagic.magicdraw.uml.DiagramType)">elementIsAllowed</a><wbr/>(<a href="../uml/DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks If element is allowed by diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ci.persistence.IProject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefinedIn()">getDefinedIn</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSymbolType()">getSymbolType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get Symbol type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExtendableByDiagram()">isExtendableByDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests If ExtendablePropertyManager is ExtendableByDiagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExtendableByStereotype()">isExtendableByStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests If ExtendablePropertyManager is ExtendableByStereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemovable()">isRemovable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests Manager is removable.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#makeCopy()">makeCopy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Make copy of property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefinedIn(com.nomagic.ci.persistence.IProject)">setDefinedIn</a><wbr/>(com.nomagic.ci.persistence.IProject definedIn)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set project where this module is read from.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExtendableByDiagram(boolean)">setExtendableByDiagram</a><wbr/>(boolean extendableByDiagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets this manager extendable by diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExtendableByStereotype(boolean)">setExtendableByStereotype</a><wbr/>(boolean extendableByStereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets this manager extendable by stereotype.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRemovable(boolean)">setRemovable</a><wbr/>(boolean removable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Removable flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSymbolType(java.lang.Class)">setSymbolType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> symbolType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set symbol type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSymbolType(java.lang.Class%5B%5D)">setSymbolType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] symbolType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set symbol type.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.properties.PropertyManager">Methods inherited from class com.nomagic.magicdraw.properties.<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></h3>
<code><a href="PropertyManager.html#addProperties(java.util.Collection)">addProperties</a>, <a href="PropertyManager.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="PropertyManager.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="PropertyManager.html#append(com.nomagic.magicdraw.properties.PropertyManager)">append</a>, <a href="PropertyManager.html#append(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)">append</a>, <a href="PropertyManager.html#append(java.util.List)">append</a>, <a href="PropertyManager.html#append(java.util.List,boolean,boolean)">append</a>, <a href="PropertyManager.html#apply(com.nomagic.magicdraw.properties.PropertyManager)">apply</a>, <a href="PropertyManager.html#apply(java.util.Collection)">apply</a>, <a href="PropertyManager.html#applyValues(java.util.Collection)">applyValues</a>, <a href="PropertyManager.html#clone()">clone</a>, <a href="PropertyManager.html#cloneProperties(java.util.List)">cloneProperties</a>, <a href="PropertyManager.html#distinct(com.nomagic.magicdraw.properties.PropertyManager)">distinct</a>, <a href="PropertyManager.html#distinct(java.util.List)">distinct</a>, <a href="PropertyManager.html#equalsTo(com.nomagic.magicdraw.properties.PropertyManager)">equalsTo</a>, <a href="PropertyManager.html#equalsWithValues(com.nomagic.magicdraw.properties.PropertyManager,java.util.Set)">equalsWithValues</a>, <a href="PropertyManager.html#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.PropertyManager)">generateDefaultDescriptionID</a>, <a href="PropertyManager.html#generateNullDescriptionID(com.nomagic.magicdraw.properties.PropertyManager)">generateNullDescriptionID</a>, <a href="PropertyManager.html#getHiddenProperties()">getHiddenProperties</a>, <a href="PropertyManager.html#getID()">getID</a>, <a href="PropertyManager.html#getName()">getName</a>, <a href="PropertyManager.html#getOrderedProperties()">getOrderedProperties</a>, <a href="PropertyManager.html#getOwnProperties()">getOwnProperties</a>, <a href="PropertyManager.html#getParentPropertyManager()">getParentPropertyManager</a>, <a href="PropertyManager.html#getProperties()">getProperties</a>, <a href="PropertyManager.html#getProperty(java.lang.String)">getProperty</a>, <a href="PropertyManager.html#getPropertyByName(java.lang.String)">getPropertyByName</a>, <a href="PropertyManager.html#getStyle()">getStyle</a>, <a href="PropertyManager.html#hideParentProperty(java.lang.String)">hideParentProperty</a>, <a href="PropertyManager.html#isFrozen()">isFrozen</a>, <a href="PropertyManager.html#isHiddenParentProperty(java.lang.String)">isHiddenParentProperty</a>, <a href="PropertyManager.html#isTheSame(com.nomagic.magicdraw.properties.PropertyManager)">isTheSame</a>, <a href="PropertyManager.html#isUndefinedStateOrValuesDiffer(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property)">isUndefinedStateOrValuesDiffer</a>, <a href="PropertyManager.html#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager)">leaveTheSame</a>, <a href="PropertyManager.html#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)">leaveTheSame</a>, <a href="PropertyManager.html#makeOwnProperty(com.nomagic.magicdraw.properties.Property)">makeOwnProperty</a>, <a href="PropertyManager.html#mergeBooleanProperty(com.nomagic.magicdraw.properties.BooleanProperty,com.nomagic.magicdraw.properties.BooleanProperty)">mergeBooleanProperty</a>, <a href="PropertyManager.html#mergeChoiceProperty(com.nomagic.magicdraw.properties.ChoiceProperty,com.nomagic.magicdraw.properties.ChoiceProperty)">mergeChoiceProperty</a>, <a href="PropertyManager.html#mergeElementProperty(com.nomagic.magicdraw.properties.ElementProperty,com.nomagic.magicdraw.properties.ElementProperty)">mergeElementProperty</a>, <a href="PropertyManager.html#mergeProperties(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property,boolean,boolean)">mergeProperties</a>, <a href="PropertyManager.html#mergePropertyByType(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property)">mergePropertyByType</a>, <a href="PropertyManager.html#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a>, <a href="PropertyManager.html#removeProperty(com.nomagic.magicdraw.properties.Property)">removeProperty</a>, <a href="PropertyManager.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="PropertyManager.html#removeProperty(java.util.Collection)">removeProperty</a>, <a href="PropertyManager.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="PropertyManager.html#retainProperties(java.util.Collection)">retainProperties</a>, <a href="PropertyManager.html#setFrozen(boolean)">setFrozen</a>, <a href="PropertyManager.html#setID(java.lang.String)">setID</a>, <a href="PropertyManager.html#setName(java.lang.String)">setName</a>, <a href="PropertyManager.html#setParentPropertyManager(com.nomagic.magicdraw.properties.PropertyManager)">setParentPropertyManager</a>, <a href="PropertyManager.html#setParentPropertyManagerOnly(com.nomagic.magicdraw.properties.PropertyManager)">setParentPropertyManagerOnly</a>, <a href="PropertyManager.html#setProperties(java.util.List)">setProperties</a>, <a href="PropertyManager.html#setPropertyEnableMap(java.lang.String,java.lang.Object%5B%5D%5B%5D)">setPropertyEnableMap</a>, <a href="PropertyManager.html#setStyle(com.nomagic.magicdraw.properties.Style)">setStyle</a>, <a href="PropertyManager.html#sGetID()">sGetID</a>, <a href="PropertyManager.html#shareProperty(com.nomagic.magicdraw.properties.Property)">shareProperty</a>, <a href="PropertyManager.html#showParentProperty(java.lang.String)">showParentProperty</a>, <a href="PropertyManager.html#toString()">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="removable">
<h3>removable</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">removable</span></div>
<div class="block">Some property managers by diagram should be fixed and not allowed to be removed.</div>
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
<h3>ExtendablePropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExtendablePropertyManager</span>()</div>
<div class="block">Construct ExtendablePropertyManager</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,java.util.List)">
<h3>ExtendablePropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExtendablePropertyManager</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> parentPropertyManager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Construct ExtendablePropertyManager with the given argument.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentPropertyManager</code> - Parent of this Property manager</dd>
<dd><code>name</code> - ExtendablePropertyManager 's name.</dd>
<dd><code>properties</code> - List of properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.util.List)">
<h3>ExtendablePropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExtendablePropertyManager</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Construct ExtendablePropertyManager with given arguments.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - Property manager name.</dd>
<dd><code>properties</code> - List of property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean,boolean)">
<h3>ExtendablePropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExtendablePropertyManager</span><wbr/><span class="parameters">(boolean extendableByDiagram,
 boolean extendableByStereotype)</span></div>
<div class="block">Construct ExtendablePropertyManager with given arguments.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extendableByDiagram</code> - extendable by diagram</dd>
<dd><code>extendableByStereotype</code> - extendable by stereotype</dd>
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
<section class="detail" id="isExtendableByDiagram()">
<h3>isExtendableByDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExtendableByDiagram</span>()</div>
<div class="block">Tests If ExtendablePropertyManager is ExtendableByDiagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this manager can be extended for diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExtendableByDiagram(boolean)">
<h3>setExtendableByDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExtendableByDiagram</span><wbr/><span class="parameters">(boolean extendableByDiagram)</span></div>
<div class="block">Sets this manager extendable by diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extendableByDiagram</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExtendableByStereotype()">
<h3>isExtendableByStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExtendableByStereotype</span>()</div>
<div class="block">Tests If ExtendablePropertyManager is ExtendableByStereotype.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this manager can be extended by stereotype.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExtendableByStereotype(boolean)">
<h3>setExtendableByStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExtendableByStereotype</span><wbr/><span class="parameters">(boolean extendableByStereotype)</span></div>
<div class="block">Sets this manager extendable by stereotype.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extendableByStereotype</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="PropertyManager.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">PropertyManager</a></code></span></div>
<div class="block">Accepts the given visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PropertyManager.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in class <code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - the PropertyVisitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PropertyManager.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)"><code>PropertyManager.accept(com.nomagic.magicdraw.properties.PropertyVisitor)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="PropertyManager.html#getClassType()">PropertyManager</a></code></span></div>
<div class="block">Returns property class type.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#getClassType()">getClassType</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="PropertyManager.html#getClassType()">getClassType</a></code> in class <code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.PROPERTY_MANAGER</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="PropertyVisitorAcceptor.html#getClassType()"><code>PropertyVisitorAcceptor.getClassType()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSymbolType(java.lang.Class)">
<h3>setSymbolType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSymbolType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> symbolType)</span></div>
<div class="block">Set symbol type. If set null manager can be used for diagrams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>symbolType</code> - symbol type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSymbolType(java.lang.Class[])">
<h3>setSymbolType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSymbolType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] symbolType)</span></div>
<div class="block">Set symbol type. If set null manager can be used for diagrams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>symbolType</code> - symbol types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSymbolType()">
<h3>getSymbolType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[]</span> <span class="element-name">getSymbolType</span>()</div>
<div class="block">Get Symbol type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>symbol type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemovable()">
<h3>isRemovable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemovable</span>()</div>
<div class="block">Tests Manager is removable.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if manager can be removed using GUI.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRemovable(boolean)">
<h3>setRemovable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRemovable</span><wbr/><span class="parameters">(boolean removable)</span></div>
<div class="block">Set Removable flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>removable</code> - true if manager can be removed using GUI.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="elementIsAllowed(com.nomagic.magicdraw.uml.DiagramType)">
<h3>elementIsAllowed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">elementIsAllowed</span><wbr/><span class="parameters">(<a href="../uml/DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> diagramType)</span></div>
<div class="block">Checks If element is allowed by diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - The given diagram type.</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeCopy()">
<h3>makeCopy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">makeCopy</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="PropertyManager.html#makeCopy()">PropertyManager</a></code></span></div>
<div class="block">Make copy of property.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="PropertyManager.html#makeCopy()">makeCopy</a></code> in class <code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></dd>
<dt>Returns:</dt>
<dd>Property Manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefinedIn()">
<h3>getDefinedIn</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.ci.persistence.IProject</span> <span class="element-name">getDefinedIn</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>module or project where this manager is defined (read from). In case manager is defined
 in primary project it may return null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefinedIn(com.nomagic.ci.persistence.IProject)">
<h3>setDefinedIn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefinedIn</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.ci.persistence.IProject definedIn)</span></div>
<div class="block">Set project where this module is read from.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>definedIn</code> - project where module is defined.</dd>
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
