# JAVA OPENAPI: Style (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/properties/Style.html
- source_path: `com/nomagic/magicdraw/properties/Style.html`
- source_sha256: `a022f2bae52f6c6f5391ae56fbbda269f59c6e4585cf0a1feb0dc6ff5f18f25b`
- captured_utc: `2026-07-14T16:55:27.240143+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class Style

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.properties.Style

All Implemented Interfaces:
`com.nomagic.magicdraw.core.project.options.PersistentStyle`, `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApiAllpublic classStyle
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html), [PropertyVisitorAcceptor](PropertyVisitorAcceptor.html), [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html), com.nomagic.magicdraw.core.project.options.PersistentStyle

Style stores and manages a set of `PropertyManagers`.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ADDED_STYLE_MANAGER](#ADDED_STYLE_MANAGER)`
Deprecated.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CHANGE_STYLE_PROPERTY](#CHANGE_STYLE_PROPERTY)`
Name of property fired on some style change.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CHANGE_STYLE_PROPERTY_VALUE](#CHANGE_STYLE_PROPERTY_VALUE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MERGED](#MERGED)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MERGED_PRE1704](#MERGED_PRE1704)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHARED](#SHARED)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Style](#%3Cinit%3E())()`
Constructs new Style.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) visitor)`
Accepts the given visitor.
`void`
`[addManager](#addManager(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`
Adds given property manager.
`void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Registers the listener to the element.
`void`
`[append](#append(com.nomagic.magicdraw.properties.Style))([Style](Style.html) s)`
Adds all managers from given style to this style.
`void`
`[appendExtendedManagers](#appendExtendedManagers(com.nomagic.magicdraw.properties.Style))([Style](Style.html) s)`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PropertyManager](PropertyManager.html),[PropertyManager](PropertyManager.html)>`
`[apply](#apply(com.nomagic.magicdraw.properties.Style))([Style](Style.html) s)`
Applies all managers from given style to the existing managers here.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`
/**
 Creates and returns a copy of this style.
`protected void`
`[cloneManagers](#cloneManagers(com.nomagic.magicdraw.properties.Style))([Style](Style.html) newS)`

`static [PropertyManager](PropertyManager.html)`
`[findPropertyManagerWithPath](#findPropertyManagerWithPath(com.nomagic.magicdraw.properties.Style,java.util.Collection))([Style](Style.html) findIn,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyManager](PropertyManager.html)> path)`

`static [PropertyManager](PropertyManager.html)`
`[findPropertyManagerWithSamePath](#findPropertyManagerWithSamePath(com.nomagic.magicdraw.properties.Style,com.nomagic.magicdraw.properties.PropertyManager))([Style](Style.html) findIn,
 [PropertyManager](PropertyManager.html) find)`
Finds same property manager(with same path) in given style.
`static void`
`[generateDefaultDescriptionID](#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Style))([Style](Style.html) style)`
Generate default description id.
`void`
`[generateID](#generateID())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`

`[PropertyManager](PropertyManager.html)`
`[getManager](#getManager(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns property manager with given name.
`int`
`[getManagerCount](#getManagerCount())()`
Returns managers count.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyManager](PropertyManager.html)>`
`[getManagers](#getManagers())()`
Returns a collection of all managers.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyManager](PropertyManager.html)>`
`[getManagers](#getManagers(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns property managers with given name.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyManager](PropertyManager.html)>`
`[getManagersFromParent](#getManagersFromParent(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) root)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns the name of the style.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyManager](PropertyManager.html)>`
`[getOrderedManagers](#getOrderedManagers())()`
Returns collection of managers sorted by name.
`boolean`
`[hasStereotype](#hasStereotype(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Check if style has stereotype with given id.
`boolean`
`[isDefault](#isDefault())()`
Is this style a default one?
`boolean`
`[isDiagramStyle](#isDiagramStyle())()`

`boolean`
`[isEqual](#isEqual(com.nomagic.magicdraw.properties.Style))([Style](Style.html) style)`
Checks if given style has same property managers with same values.
`boolean`
`[isSnapshotStyleForDiagramSymbols](#isSnapshotStyleForDiagramSymbols())()`

`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`
On CHANGE_STYLE_PROPERTY property change takes the manager from
 property's new Value and replaces itself properties with properties from
 this manager.
`void`
`[propertyManagerNameChanged](#propertyManagerNameChanged(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`
Called when property manager name is changed
`void`
`[removeManager](#removeManager(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`
Removes given property manager.
`void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Unregisters the given listener from the element.
`void`
`[setAppliedPropertyManagerIDs](#setAppliedPropertyManagerIDs(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PropertyManager](PropertyManager.html),[PropertyManager](PropertyManager.html)> propertyManagers)`
Sets applied property manager id to managers which does not have it.
`void`
`[setDefault](#setDefault(boolean))(boolean def)`
Sets default flag value.
`void`
`[setID](#setID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Set Id
`void`
`[setManagers](#setManagers(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyManager](PropertyManager.html)> managers)`
Sets the collection of all managers.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Set the name of the style.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns a string representation of the style.
`void`
`[updateDefinedIn](#updateDefinedIn(com.nomagic.magicdraw.properties.Style))([Style](Style.html) src)`
Update all [`ExtendablePropertyManager`](ExtendablePropertyManager.html) in this style defined in.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SHARED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHARED
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.SHARED)
MERGED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MERGED
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.MERGED)
MERGED_PRE1704
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MERGED_PRE1704
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.MERGED_PRE1704)
CHANGE_STYLE_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CHANGE_STYLE_PROPERTY
Name of property fired on some style change.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.CHANGE_STYLE_PROPERTY)
CHANGE_STYLE_PROPERTY_VALUE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CHANGE_STYLE_PROPERTY_VALUE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.CHANGE_STYLE_PROPERTY_VALUE)
ADDED_STYLE_MANAGER
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ADDED_STYLE_MANAGER
Deprecated.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.ADDED_STYLE_MANAGER)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Style
public Style()
Constructs new Style.
 Style will have name "default", but it will not be default.
 ============ METHOD DETAIL ========== 
Method Details
addManager
public void addManager(@CheckForNull
 [PropertyManager](PropertyManager.html) manager)
Adds given property manager.
Parameters:
`manager` - the manager to add.
removeManager
public void removeManager([PropertyManager](PropertyManager.html) manager)
Removes given property manager.
Parameters:
`manager` - the manager to remove.
getManagerCount
public int getManagerCount()
Returns managers count.
Returns:
count of managers.
setManagers
public void setManagers([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyManager](PropertyManager.html)> managers)
Sets the collection of all managers.
Parameters:
`managers` - a collection of new managers.
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns the name of the style.
Returns:
name of the style.
setName
public void setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Set the name of the style.
Parameters:
`name` - the new name of the style.
setAppliedPropertyManagerIDs
public void setAppliedPropertyManagerIDs([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PropertyManager](PropertyManager.html),[PropertyManager](PropertyManager.html)> propertyManagers)
Sets applied property manager id to managers which does not have it.
Parameters:
`propertyManagers` - property managers to analyze
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Returns a string representation of the style. Used for debug.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
the string representation.
setDefault
public void setDefault(boolean def)
Sets default flag value.
Parameters:
`def` - new flag value.
isDefault
public boolean isDefault()
Is this style a default one?
Returns:
default flag value.
clone
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) clone()
/**
 Creates and returns a copy of this style.
 Does deep clone.
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
the clone of this style.
cloneManagers
protected void cloneManagers([Style](Style.html) newS)
getManagers
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyManager](PropertyManager.html)> getManagers()
Returns a collection of all managers.
Returns:
all managers.
getOrderedManagers
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyManager](PropertyManager.html)> getOrderedManagers()
Returns collection of managers sorted by name.
Returns:
collection of managers sorted by name.
getManager
@CheckForNullpublic [PropertyManager](PropertyManager.html) getManager([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns property manager with given name.
Parameters:
`name` - the name of manager.
Returns:
manager with given name or null.
getManagers
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyManager](PropertyManager.html)> getManagers([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns property managers with given name.
Parameters:
`name` - the name of manager.
Returns:
managers with given name or null.
accept
public void accept([PropertyVisitor](PropertyVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Parameters:
`visitor` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getClassType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Returns:
PropertyID.SIMPLE_STYLE
See Also:
[`PropertyID.SIMPLE_STYLE`](PropertyID.html#SIMPLE_STYLE)
append
public void append([Style](Style.html) s)
Adds all managers from given style to this style.
 If some manager exists in given style, but does not exist in this style - clone this manager and add.
 If some manager exists in given style and exists in this style - append properties from given manager to
 this manager.
Parameters:
`s` - the given style.
apply
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PropertyManager](PropertyManager.html),[PropertyManager](PropertyManager.html)> apply([Style](Style.html) s)
Applies all managers from given style to the existing managers here.
 If some manager exists in given style, but does not exist in this style - do nothing.
Parameters:
`s` - the given style.
appendExtendedManagers
public void appendExtendedManagers([Style](Style.html) s)
isDiagramStyle
public boolean isDiagramStyle()
Returns:
if it is diagram style
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
On CHANGE_STYLE_PROPERTY property change takes the manager from
 property's new Value and replaces itself properties with properties from
 this manager.
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Parameters:
`evt` - PropertyChangeEvent.
getManagersFromParent
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[PropertyManager](PropertyManager.html)> getManagersFromParent(@CheckForNull
 [PropertyManager](PropertyManager.html) root)
findPropertyManagerWithSamePath
@CheckForNullpublic static [PropertyManager](PropertyManager.html) findPropertyManagerWithSamePath([Style](Style.html) findIn,
 [PropertyManager](PropertyManager.html) find)
Finds same property manager(with same path) in given style.
Parameters:
`findIn` - style where find manager.
`find` - manager to find.
Returns:
found manager, or null if not found.
findPropertyManagerWithPath
@CheckForNullpublic static [PropertyManager](PropertyManager.html) findPropertyManagerWithPath([Style](Style.html) findIn,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyManager](PropertyManager.html)> path)
generateID
public void generateID()
getID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Returns:
Returns the iD. Can return null if ID was not generated.
 ID is generated only for styles used for not loaded diagrams.
setID
public void setID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Set Id
Parameters:
`id` - given ID.
addPropertyChangeListener
public void addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Registers the listener to the element. The given listener will get notifications about
 property changes in this element.
Parameters:
`listener` - the `PropertyChangeListener` to be added.
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
removePropertyChangeListener
public void removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Unregisters the given listener from the element. The given listener will not get any notifications about
 property changes in this element.
Parameters:
`listener` - the PropertyChangeListener to be removed.
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
generateDefaultDescriptionID
public static void generateDefaultDescriptionID([Style](Style.html) style)
Generate default description id.
Parameters:
`style` - style
isSnapshotStyleForDiagramSymbols
public boolean isSnapshotStyleForDiagramSymbols()
Returns:
true if style is clone used for diagram style preserving.
isEqual
public boolean isEqual([Style](Style.html) style)
Checks if given style has same property managers with same values.
Parameters:
`style` - given style.
Returns:
true if given style has same values as this style.
updateDefinedIn
public void updateDefinedIn([Style](Style.html) src)
Update all [`ExtendablePropertyManager`](ExtendablePropertyManager.html) in this style defined in.
Parameters:
`src` - source to get defined in values
hasStereotype
public boolean hasStereotype([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Check if style has stereotype with given id. This method is faster than iterate through all property managers.
Parameters:
`id` - stereotype id
Returns:
true if stereotype with given id has property manager in this style.
propertyManagerNameChanged
public void propertyManagerNameChanged([PropertyManager](PropertyManager.html) manager)
Called when property manager name is changed
Parameters:
`manager` - manager which name is changed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class Style">Class Style</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.properties.Style</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.core.project.options.PersistentStyle</code>, <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Style</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a>, <a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>, com.nomagic.magicdraw.core.project.options.PersistentStyle</span></div>
<div class="block">Style stores and manages a set of <code>PropertyManagers</code>.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ADDED_STYLE_MANAGER">ADDED_STYLE_MANAGER</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CHANGE_STYLE_PROPERTY">CHANGE_STYLE_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Name of property fired on some style change.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CHANGE_STYLE_PROPERTY_VALUE">CHANGE_STYLE_PROPERTY_VALUE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MERGED">MERGED</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MERGED_PRE1704">MERGED_PRE1704</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHARED">SHARED</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Style</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs new Style.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts the given visitor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addManager(com.nomagic.magicdraw.properties.PropertyManager)">addManager</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds given property manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers the listener to the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#append(com.nomagic.magicdraw.properties.Style)">append</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds all managers from given style to this style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendExtendedManagers(com.nomagic.magicdraw.properties.Style)">appendExtendedManagers</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> s)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>,<wbr/><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#apply(com.nomagic.magicdraw.properties.Style)">apply</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies all managers from given style to the existing managers here.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">/**
 Creates and returns a copy of this style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#cloneManagers(com.nomagic.magicdraw.properties.Style)">cloneManagers</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> newS)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findPropertyManagerWithPath(com.nomagic.magicdraw.properties.Style,java.util.Collection)">findPropertyManagerWithPath</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> findIn,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt; path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findPropertyManagerWithSamePath(com.nomagic.magicdraw.properties.Style,com.nomagic.magicdraw.properties.PropertyManager)">findPropertyManagerWithSamePath</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> findIn,
 <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> find)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds same property manager(with same path) in given style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Style)">generateDefaultDescriptionID</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Generate default description id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generateID()">generateID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManager(java.lang.String)">getManager</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property manager with given name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManagerCount()">getManagerCount</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns managers count.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManagers()">getManagers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a collection of all managers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManagers(java.lang.String)">getManagers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property managers with given name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManagersFromParent(com.nomagic.magicdraw.properties.PropertyManager)">getManagersFromParent</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the name of the style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrderedManagers()">getOrderedManagers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns collection of managers sorted by name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasStereotype(java.lang.String)">hasStereotype</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if style has stereotype with given id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDefault()">isDefault</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Is this style a default one?</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDiagramStyle()">isDiagramStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEqual(com.nomagic.magicdraw.properties.Style)">isEqual</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given style has same property managers with same values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSnapshotStyleForDiagramSymbols()">isSnapshotStyleForDiagramSymbols</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">On CHANGE_STYLE_PROPERTY property change takes the manager from
 property's new Value and replaces itself properties with properties from
 this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyManagerNameChanged(com.nomagic.magicdraw.properties.PropertyManager)">propertyManagerNameChanged</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called when property manager name is changed</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeManager(com.nomagic.magicdraw.properties.PropertyManager)">removeManager</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes given property manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregisters the given listener from the element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAppliedPropertyManagerIDs(java.util.Map)">setAppliedPropertyManagerIDs</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>,<wbr/><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt; propertyManagers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets applied property manager id to managers which does not have it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefault(boolean)">setDefault</a><wbr/>(boolean def)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default flag value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setID(java.lang.String)">setID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Id</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setManagers(java.util.Collection)">setManagers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt; managers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the collection of all managers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the name of the style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a string representation of the style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateDefinedIn(com.nomagic.magicdraw.properties.Style)">updateDefinedIn</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> src)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update all <a href="ExtendablePropertyManager.html" title="class in com.nomagic.magicdraw.properties"><code>ExtendablePropertyManager</code></a> in this style defined in.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="SHARED">
<h3>SHARED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHARED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.SHARED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MERGED">
<h3>MERGED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MERGED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.MERGED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MERGED_PRE1704">
<h3>MERGED_PRE1704</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MERGED_PRE1704</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.MERGED_PRE1704">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CHANGE_STYLE_PROPERTY">
<h3>CHANGE_STYLE_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHANGE_STYLE_PROPERTY</span></div>
<div class="block">Name of property fired on some style change.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.CHANGE_STYLE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CHANGE_STYLE_PROPERTY_VALUE">
<h3>CHANGE_STYLE_PROPERTY_VALUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHANGE_STYLE_PROPERTY_VALUE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.CHANGE_STYLE_PROPERTY_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ADDED_STYLE_MANAGER">
<h3>ADDED_STYLE_MANAGER</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ADDED_STYLE_MANAGER</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.Style.ADDED_STYLE_MANAGER">Constant Field Values</a></li>
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
<h3>Style</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Style</span>()</div>
<div class="block">Constructs new Style.
 Style will have name "default", but it will not be default.</div>
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
<section class="detail" id="addManager(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>addManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addManager</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
<div class="block">Adds given property manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the manager to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeManager(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>removeManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeManager</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
<div class="block">Removes given property manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the manager to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManagerCount()">
<h3>getManagerCount</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getManagerCount</span>()</div>
<div class="block">Returns managers count.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>count of managers.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManagers(java.util.Collection)">
<h3>setManagers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManagers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt; managers)</span></div>
<div class="block">Sets the collection of all managers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>managers</code> - a collection of new managers.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns the name of the style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of the style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Set the name of the style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the new name of the style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAppliedPropertyManagerIDs(java.util.Map)">
<h3>setAppliedPropertyManagerIDs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAppliedPropertyManagerIDs</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>,<wbr/><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt; propertyManagers)</span></div>
<div class="block">Sets applied property manager id to managers which does not have it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyManagers</code> - property managers to analyze</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns a string representation of the style. Used for debug.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>the string representation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefault(boolean)">
<h3>setDefault</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefault</span><wbr/><span class="parameters">(boolean def)</span></div>
<div class="block">Sets default flag value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>def</code> - new flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDefault()">
<h3>isDefault</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDefault</span>()</div>
<div class="block">Is this style a default one?</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>default flag value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()</div>
<div class="block">/**
 Creates and returns a copy of this style.
 Does deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>the clone of this style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cloneManagers(com.nomagic.magicdraw.properties.Style)">
<h3>cloneManagers</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">cloneManagers</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> newS)</span></div>
</section>
</li>
<li>
<section class="detail" id="getManagers()">
<h3>getManagers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</span> <span class="element-name">getManagers</span>()</div>
<div class="block">Returns a collection of all managers.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all managers.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrderedManagers()">
<h3>getOrderedManagers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</span> <span class="element-name">getOrderedManagers</span>()</div>
<div class="block">Returns collection of managers sorted by name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of managers sorted by name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManager(java.lang.String)">
<h3>getManager</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getManager</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns property manager with given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of manager.</dd>
<dt>Returns:</dt>
<dd>manager with given name or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManagers(java.lang.String)">
<h3>getManagers</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</span> <span class="element-name">getManagers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns property managers with given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of manager.</dd>
<dt>Returns:</dt>
<dd>managers with given name or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Accepts the given visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - the PropertyVisitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Returns property class type.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#getClassType()">getClassType</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.SIMPLE_STYLE</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PropertyID.html#SIMPLE_STYLE"><code>PropertyID.SIMPLE_STYLE</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(com.nomagic.magicdraw.properties.Style)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> s)</span></div>
<div class="block">Adds all managers from given style to this style.
 If some manager exists in given style, but does not exist in this style - clone this manager and add.
 If some manager exists in given style and exists in this style - append properties from given manager to
 this manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - the given style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="apply(com.nomagic.magicdraw.properties.Style)">
<h3>apply</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>,<wbr/><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</span> <span class="element-name">apply</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> s)</span></div>
<div class="block">Applies all managers from given style to the existing managers here.
 If some manager exists in given style, but does not exist in this style - do nothing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - the given style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendExtendedManagers(com.nomagic.magicdraw.properties.Style)">
<h3>appendExtendedManagers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">appendExtendedManagers</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> s)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDiagramStyle()">
<h3>isDiagramStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDiagramStyle</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>if it is diagram style</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</span></div>
<div class="block">On CHANGE_STYLE_PROPERTY property change takes the manager from
 property's new Value and replaces itself properties with properties from
 this manager.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>evt</code> - PropertyChangeEvent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManagersFromParent(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>getManagersFromParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt;</span> <span class="element-name">getManagersFromParent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> root)</span></div>
</section>
</li>
<li>
<section class="detail" id="findPropertyManagerWithSamePath(com.nomagic.magicdraw.properties.Style,com.nomagic.magicdraw.properties.PropertyManager)">
<h3>findPropertyManagerWithSamePath</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">findPropertyManagerWithSamePath</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> findIn,
 <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> find)</span></div>
<div class="block">Finds same property manager(with same path) in given style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>findIn</code> - style where find manager.</dd>
<dd><code>find</code> - manager to find.</dd>
<dt>Returns:</dt>
<dd>found manager, or null if not found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findPropertyManagerWithPath(com.nomagic.magicdraw.properties.Style,java.util.Collection)">
<h3>findPropertyManagerWithPath</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">findPropertyManagerWithPath</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> findIn,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a>&gt; path)</span></div>
</section>
</li>
<li>
<section class="detail" id="generateID()">
<h3>generateID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">generateID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns the iD. Can return null if ID was not generated.
 ID is generated only for styles used for not loaded diagrams.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(java.lang.String)">
<h3>setID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Set Id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - given ID.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Registers the listener to the element. The given listener will get notifications about
 property changes in this element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be added.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Unregisters the given listener from the element. The given listener will not get any notifications about
 property changes in this element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the PropertyChangeListener to be removed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generateDefaultDescriptionID(com.nomagic.magicdraw.properties.Style)">
<h3>generateDefaultDescriptionID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">generateDefaultDescriptionID</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</span></div>
<div class="block">Generate default description id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - style</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSnapshotStyleForDiagramSymbols()">
<h3>isSnapshotStyleForDiagramSymbols</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSnapshotStyleForDiagramSymbols</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if style is clone used for diagram style preserving.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEqual(com.nomagic.magicdraw.properties.Style)">
<h3>isEqual</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEqual</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</span></div>
<div class="block">Checks if given style has same property managers with same values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - given style.</dd>
<dt>Returns:</dt>
<dd>true if given style has same values as this style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateDefinedIn(com.nomagic.magicdraw.properties.Style)">
<h3>updateDefinedIn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateDefinedIn</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> src)</span></div>
<div class="block">Update all <a href="ExtendablePropertyManager.html" title="class in com.nomagic.magicdraw.properties"><code>ExtendablePropertyManager</code></a> in this style defined in.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>src</code> - source to get defined in values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasStereotype(java.lang.String)">
<h3>hasStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasStereotype</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Check if style has stereotype with given id. This method is faster than iterate through all property managers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - stereotype id</dd>
<dt>Returns:</dt>
<dd>true if stereotype with given id has property manager in this style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyManagerNameChanged(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>propertyManagerNameChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyManagerNameChanged</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
<div class="block">Called when property manager name is changed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager which name is changed</dd>
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
