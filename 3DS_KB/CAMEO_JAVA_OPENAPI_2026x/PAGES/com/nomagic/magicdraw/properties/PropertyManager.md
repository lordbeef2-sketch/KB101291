# JAVA OPENAPI: PropertyManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/properties/PropertyManager.html
- source_path: `com/nomagic/magicdraw/properties/PropertyManager.html`
- source_sha256: `1f41fcf12923c891349facf2b3794b70c0e9f20357cf4b1fe0852c7d419ffdda`
- captured_utc: `2026-07-14T16:58:00.883568+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Class PropertyManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.properties.PropertyManager

All Implemented Interfaces:
`[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html)`

Direct Known Subclasses:
`[ExtendablePropertyManager](ExtendablePropertyManager.html)`

@OpenApiAllpublic classPropertyManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html), [PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html), [PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)

This class is used for managing of the set of the properties. The manager has name. Also manager can
 return some property with given property ID.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[IS_UNIQUE](#IS_UNIQUE)`
Identifies the property as "unique".
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OWN_PROPERTY_ADDED](#OWN_PROPERTY_ADDED)`
Identifies type of [`PropertyChangeEvent`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html).
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OWN_PROPERTY_REMOVED](#OWN_PROPERTY_REMOVED)`
Identifies type of [`PropertyChangeEvent`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html).
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PropertyManager](#%3Cinit%3E())()`
Constructs new property manager
`[PropertyManager](#%3Cinit%3E(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,java.util.List))([PropertyManager](PropertyManager.html) parentPropertyManager,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Property](Property.html)> properties)`
Constructs new property manager.
`[PropertyManager](#%3Cinit%3E(java.lang.String,java.util.List))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Property](Property.html)> properties)`
Constructs new property manager.
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
`[addProperties](#addProperties(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> properties)`
Adds the properties to the property manager.
`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property))([Property](Property.html) prop)`
Adds the property to the property manager.
`void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Adds `PropertyChangeListener` to the listeners list.
`void`
`[append](#append(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`
Adds not existing properties from given manager to itself.
`void`
`[append](#append(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean))([PropertyManager](PropertyManager.html) manager,
 boolean makeUndefined,
 boolean mergeSources)`
Adds not existing properties from given manager to itself.
`void`
`[append](#append(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)`
Adds not existing properties from given list to itself.
`void`
`[append](#append(java.util.List,boolean,boolean))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties,
 boolean makeUndefined,
 boolean mergeSources)`
Adds not existing properties from given list to itself.
`void`
`[apply](#apply(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`
Applies properties from given manager.
`void`
`[apply](#apply(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> properties)`
Applies properties from given list.
`void`
`[applyValues](#applyValues(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> col)`
Applies properties values only from given list.
`[PropertyManager](PropertyManager.html)`
`[clone](#clone())()`
Clones the manager.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[cloneProperties](#cloneProperties(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)`

`void`
`[distinct](#distinct(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) man)`
Sets to itself properties those are not equal to the given properties.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[distinct](#distinct(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)`
Returns properties those are not equal to the given properties.
`boolean`
`[equalsTo](#equalsTo(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) given)`

`boolean`
`[equalsWithValues](#equalsWithValues(com.nomagic.magicdraw.properties.PropertyManager,java.util.Set))([PropertyManager](PropertyManager.html) pm,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> ids)`
Check it equals with given property value.
`static void`
`[generateDefaultDescriptionID](#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`

`static void`
`[generateNullDescriptionID](#generateNullDescriptionID(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns property class type.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getHiddenProperties](#getHiddenProperties())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Get ID
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns name of the property manager.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[getOrderedProperties](#getOrderedProperties())()`
Returns list of properties.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[getOwnProperties](#getOwnProperties())()`
Returns the list of the properties.
`[PropertyManager](PropertyManager.html)`
`[getParentPropertyManager](#getParentPropertyManager())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)>`
`[getProperties](#getProperties())()`
Returns the list of the properties.
`[Property](Property.html)`
`[getProperty](#getProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Returns the property from the properties list with given id.
`[Property](Property.html)`
`[getPropertyByName](#getPropertyByName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns property from the properties list with given name.
`[Style](Style.html)`
`[getStyle](#getStyle())()`
Get property style.
`void`
`[hideParentProperty](#hideParentProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyID)`
Hides given property with id from parent property manager.
`boolean`
`[isFrozen](#isFrozen())()`

`boolean`
`[isHiddenParentProperty](#isHiddenParentProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyID)`
Check if property with a given ID is hidden parent property
`boolean`
`[isTheSame](#isTheSame(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`
Check if given property manager is the same as current.
`static boolean`
`[isUndefinedStateOrValuesDiffer](#isUndefinedStateOrValuesDiffer(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property))([Property](Property.html) first,
 [Property](Property.html) second)`

`void`
`[leaveTheSame](#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) manager)`
Removes from this manager all properties those does not exist in the given manager.
`void`
`[leaveTheSame](#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean))([PropertyManager](PropertyManager.html) manager,
 boolean makeUndefined,
 boolean mergeSources)`
Removes from this manager all properties those does not exist in the given manager.
`[PropertyManager](PropertyManager.html)`
`[makeCopy](#makeCopy())()`
Make copy of property.
`void`
`[makeOwnProperty](#makeOwnProperty(com.nomagic.magicdraw.properties.Property))([Property](Property.html) prop)`
Makes given property as own property even if property with such id is in parent (makes property not shared)
`protected void`
`[mergeBooleanProperty](#mergeBooleanProperty(com.nomagic.magicdraw.properties.BooleanProperty,com.nomagic.magicdraw.properties.BooleanProperty))([BooleanProperty](BooleanProperty.html) currentProp,
 [BooleanProperty](BooleanProperty.html) otherProp)`

`protected void`
`[mergeChoiceProperty](#mergeChoiceProperty(com.nomagic.magicdraw.properties.ChoiceProperty,com.nomagic.magicdraw.properties.ChoiceProperty))([ChoiceProperty](ChoiceProperty.html) currentProperty,
 [ChoiceProperty](ChoiceProperty.html) otherProperty)`

`protected void`
`[mergeElementProperty](#mergeElementProperty(com.nomagic.magicdraw.properties.ElementProperty,com.nomagic.magicdraw.properties.ElementProperty))([ElementProperty](ElementProperty.html) currentProp,
 [ElementProperty](ElementProperty.html) otherProp)`

`protected void`
`[mergeProperties](#mergeProperties(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property,boolean,boolean))([Property](Property.html) currentManagerProperty,
 [Property](Property.html) property,
 boolean makeUndefined,
 boolean mergeSources)`

`protected void`
`[mergePropertyByType](#mergePropertyByType(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property))([Property](Property.html) currentProperty,
 [Property](Property.html) otherProperty)`

`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)`
Listens to `PropertyChangeEvents`.
`void`
`[removeProperty](#removeProperty(com.nomagic.magicdraw.properties.Property))([Property](Property.html) prop)`
Removes the property from the property manager.
`void`
`[removeProperty](#removeProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Removes the property with given ID from the property manager.
`void`
`[removeProperty](#removeProperty(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyIDs)`
Removes all properties with given ids.
`void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Removes `PropertyChangeListener` from the listeners list.
`void`
`[retainProperties](#retainProperties(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> ids)`
Removes all properties except the the ones with given ids.
`void`
`[setFrozen](#setFrozen(boolean))(boolean mFrozen)`

`void`
`[setID](#setID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Sets id for this property manager.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Sets name of the manager.
`void`
`[setParentPropertyManager](#setParentPropertyManager(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) parentPropertyManager)`
Set parent Property Manager.
`void`
`[setParentPropertyManagerOnly](#setParentPropertyManagerOnly(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) parentPropertyManager)`
Set parent Property Manager.
`void`
`[setProperties](#setProperties(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> prop)`
Sets the list of the properties.
`void`
`[setPropertyEnableMap](#setPropertyEnableMap(java.lang.String,java.lang.Object%5B%5D%5B%5D))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyId,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)[][] map)`
Set Property Enable Map
`void`
`[setStyle](#setStyle(com.nomagic.magicdraw.properties.Style))([Style](Style.html) style)`
Set style.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[sGetID](#sGetID())()`
Property manager simple ID getter (does not generate ID if it is not present).
`void`
`[shareProperty](#shareProperty(com.nomagic.magicdraw.properties.Property))([Property](Property.html) prop)`
Makes given property shared form parent PropertyManager.
`void`
`[showParentProperty](#showParentProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyID)`
Show parent property.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns info used for debug.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
OWN_PROPERTY_ADDED
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OWN_PROPERTY_ADDED
Identifies type of [`PropertyChangeEvent`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html). This type of even is fired
 when particular property is added to [`PropertyManager`](PropertyManager.html) own properties collection.
 It may be triggered by [`addProperty(Property)`](#addProperty(com.nomagic.magicdraw.properties.Property)) or [`makeOwnProperty(Property)`](#makeOwnProperty(com.nomagic.magicdraw.properties.Property)) method call.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.PropertyManager.OWN_PROPERTY_ADDED)
OWN_PROPERTY_REMOVED
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OWN_PROPERTY_REMOVED
Identifies type of [`PropertyChangeEvent`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html). This type of even is fired
 when particular property is removed from [`PropertyManager`](PropertyManager.html) own properties collection.
 It may be triggered by [`removeProperty(Property)`](#removeProperty(com.nomagic.magicdraw.properties.Property)) or [`shareProperty(Property)`](#shareProperty(com.nomagic.magicdraw.properties.Property)) method call.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.PropertyManager.OWN_PROPERTY_REMOVED)
IS_UNIQUE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) IS_UNIQUE
Identifies the property as "unique". Is set via [`Property.setAdditionalProperty(String, Object)`](Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)):
 `property.setAdditionalProperty(PropertyManager.IS_UNIQUE, true);` 

 Unique property will always be removed when calling [`leaveTheSame(PropertyManager, boolean, boolean)`](#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)) method.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.properties.PropertyManager.IS_UNIQUE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PropertyManager
public PropertyManager()
Constructs new property manager
PropertyManager
public PropertyManager(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Property](Property.html)> properties)
Constructs new property manager.
Parameters:
`name` - the name of the manager.
`properties` - the list of properties.
PropertyManager
public PropertyManager(@CheckForNull
 [PropertyManager](PropertyManager.html) parentPropertyManager,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Property](Property.html)> properties)
Constructs new property manager.
Parameters:
`parentPropertyManager` - parent property manager which can provides properties can be shared in this manager.
`name` - the name of the manager.
`properties` - the list of properties.
 ============ METHOD DETAIL ========== 
Method Details
getHiddenProperties
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getHiddenProperties()
getID
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getID()
Get ID
Returns:
ID of property.
sGetID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sGetID()
Property manager simple ID getter (does not generate ID if it is not present).
Returns:
property manager ID or `null`
getParentPropertyManager
@CheckForNullpublic [PropertyManager](PropertyManager.html) getParentPropertyManager()
setParentPropertyManager
public void setParentPropertyManager(@CheckForNull
 [PropertyManager](PropertyManager.html) parentPropertyManager)
Set parent Property Manager.
Parameters:
`parentPropertyManager` - parent manager
setParentPropertyManagerOnly
public void setParentPropertyManagerOnly(@CheckForNull
 [PropertyManager](PropertyManager.html) parentPropertyManager)
Set parent Property Manager.
Parameters:
`parentPropertyManager` - parent manager
getProperty
@CheckForNullpublic [Property](Property.html) getProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Returns the property from the properties list with given id.
Parameters:
`id` - the ID of property.
Returns:
property with given ID. Null if such property is not added into the manager.
getPropertyByName
@CheckForNullpublic [Property](Property.html) getPropertyByName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns property from the properties list with given name.
Parameters:
`name` - name of the property
Returns:
property with given name. Null if such property is not added into the manager.
addProperty
public void addProperty([Property](Property.html) prop)
Adds the property to the property manager.
 If property with such ID was already added, the old property is removed.
 Checking if property with same id already exists in parent property manager, and they value is the same do nothing
Parameters:
`prop` - the new property.
addProperties
public void addProperties([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> properties)
Adds the properties to the property manager.
 If property with such ID was already added, the old property is removed.
 Checking if property with same id already exists in parent property manager, and they value is the same do nothing
Parameters:
`properties` - the new properties.
removeProperty
public void removeProperty([Property](Property.html) prop)
Removes the property from the property manager.
Parameters:
`prop` - the property.
removeProperty
public void removeProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Removes the property with given ID from the property manager.
Parameters:
`id` - the property's ID.
getProperties
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> getProperties()
Returns the list of the properties.
Returns:
all properties from this manager and parent managers.
getOwnProperties
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> getOwnProperties()
Returns the list of the properties.
Returns:
all properties only from this manager. List is unmodifiable.
setProperties
public void setProperties([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> prop)
Sets the list of the properties.
Parameters:
`prop` - the list of new properties for this manager.
getOrderedProperties
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> getOrderedProperties()
Returns list of properties. Properties are stored in list no sorting needed
Returns:
list of properties
clone
public [PropertyManager](PropertyManager.html) clone()
Clones the manager. Does deep clone - all properties will be cloned too.
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
the cloned manager.
cloneProperties
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> cloneProperties([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)
makeCopy
public [PropertyManager](PropertyManager.html) makeCopy()
Make copy of property.
Returns:
Property Manager.
apply
public void apply([PropertyManager](PropertyManager.html) manager)
Applies properties from given manager.
 Property from given manager will be replaced with property from this manager if this manager:
 1.has property with such ID.
 2.state of this property is not UNDEFINED.
Parameters:
`manager` - manager which properties will be applied to this.
See Also:
[`apply(Collection)`](#apply(java.util.Collection))
apply
public void apply([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> properties)
Applies properties from given list.
 Property from given list will be replaced with property from this manager if this manager:
 1.has property with such ID.
 2.state of this property is not UNDEFINED.
Parameters:
`properties` - collection of properties to be applied to this.
applyValues
public void applyValues([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Property](Property.html)> col)
Applies properties values only from given list.
Parameters:
`col` - collection of properties to be applied to this.
leaveTheSame
public void leaveTheSame([PropertyManager](PropertyManager.html) manager)
Removes from this manager all properties those does not exist in the given manager.
 Property will be removed if given manager does not have property with the same ID.
 Existing property in this manager will be set to undefined state if
 property in the given manager has different value.
Parameters:
`manager` - the given manager.
leaveTheSame
public void leaveTheSame([PropertyManager](PropertyManager.html) manager,
 boolean makeUndefined,
 boolean mergeSources)
Removes from this manager all properties those does not exist in the given manager.
 Property will be removed if given manager does not have property with the same ID and the same value.
Parameters:
`manager` - the given manager.
`makeUndefined` - existing property in this manager will be set to undefined state if property in given manager has different value.
`mergeSources` - if true, properties sources will be merged
mergeProperties
protected void mergeProperties([Property](Property.html) currentManagerProperty,
 [Property](Property.html) property,
 boolean makeUndefined,
 boolean mergeSources)
mergePropertyByType
protected void mergePropertyByType([Property](Property.html) currentProperty,
 [Property](Property.html) otherProperty)
mergeBooleanProperty
protected void mergeBooleanProperty([BooleanProperty](BooleanProperty.html) currentProp,
 [BooleanProperty](BooleanProperty.html) otherProp)
mergeElementProperty
protected void mergeElementProperty([ElementProperty](ElementProperty.html) currentProp,
 [ElementProperty](ElementProperty.html) otherProp)
mergeChoiceProperty
protected void mergeChoiceProperty([ChoiceProperty](ChoiceProperty.html) currentProperty,
 [ChoiceProperty](ChoiceProperty.html) otherProperty)
setName
public void setName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Sets name of the manager.
Parameters:
`name` - the new name.
getName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Returns name of the property manager.
Returns:
the name of the property manager.
distinct
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> distinct([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)
Returns properties those are not equal to the given properties.
Parameters:
`properties` - the given properties.
Returns:
not equal properties to the given properties or empty list.
isUndefinedStateOrValuesDiffer
public static boolean isUndefinedStateOrValuesDiffer([Property](Property.html) first,
 [Property](Property.html) second)
distinct
public void distinct([PropertyManager](PropertyManager.html) man)
Sets to itself properties those are not equal to the given properties.
Parameters:
`man` - the manager with given properties.
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)
Listens to `PropertyChangeEvents`. Takes new value from the
 event(new value must be a list of properties) and sets these properties
 to itself.
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Parameters:
`e` - the property change event.
accept
public void accept([PropertyVisitor](PropertyVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Accepts the given visitor.
Specified by:
`[accept](PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor))` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Parameters:
`visitor` - the PropertyVisitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
getClassType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getClassType()
Returns property class type.
Specified by:
`[getClassType](PropertyVisitorAcceptor.html#getClassType())` in interface `[PropertyVisitorAcceptor](PropertyVisitorAcceptor.html)`
Returns:
PropertyID.PROPERTY_MANAGER
See Also:
[`PropertyID.PROPERTY_MANAGER`](PropertyID.html#PROPERTY_MANAGER)
append
public void append([PropertyManager](PropertyManager.html) manager)
Adds not existing properties from given manager to itself.
 The properties existence is checked by property ID.
Parameters:
`manager` - the manager with properties.
append
public void append([PropertyManager](PropertyManager.html) manager,
 boolean makeUndefined,
 boolean mergeSources)
Adds not existing properties from given manager to itself.
 The properties existence is checked by property ID.
Parameters:
`manager` - the manager with properties.
`makeUndefined` - existing property in this manager will be set to undefined state if property in given manager has different value.
`mergeSources` - if true, properties sources will be merged
append
public void append([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties)
Adds not existing properties from given list to itself.
 The properties existence is checked by property ID.
Parameters:
`properties` - the list of given properties.
append
public void append([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Property](Property.html)> properties,
 boolean makeUndefined,
 boolean mergeSources)
Adds not existing properties from given list to itself.
 The properties existence is checked by property ID.
Parameters:
`properties` - the list of given properties.
`makeUndefined` - existing property in this manager will be set to undefined state if property in given manager has different value.
`mergeSources` - if true, properties sources will be merged
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Returns info used for debug.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
info for debug
shareProperty
public void shareProperty([Property](Property.html) prop)
Makes given property shared form parent PropertyManager. Value changed in parent will affect property in this property manager.
Parameters:
`prop` - property to share.
makeOwnProperty
public void makeOwnProperty([Property](Property.html) prop)
Makes given property as own property even if property with such id is in parent (makes property not shared)
Parameters:
`prop` - property
hideParentProperty
public void hideParentProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyID)
Hides given property with id from parent property manager. Not that if property with this id is in this property manager nothing will be changed.
Parameters:
`propertyID` - property ID to hide from parent manager;
isHiddenParentProperty
public boolean isHiddenParentProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyID)
Check if property with a given ID is hidden parent property
Parameters:
`propertyID` - property ID
showParentProperty
public void showParentProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyID)
Show parent property.
Parameters:
`propertyID` - property ID
setID
public void setID(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Sets id for this property manager.
Parameters:
`id` - new id of this property manager.
getStyle
@CheckForNullpublic [Style](Style.html) getStyle()
Get property style.
Returns:
Returns the style.
setStyle
public void setStyle(@CheckForNull
 [Style](Style.html) style)
Set style.
Parameters:
`style` - The style to set.
setPropertyEnableMap
public void setPropertyEnableMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyId,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)[][] map)
Set Property Enable Map
Parameters:
`propertyId` - Property id.
`map` - map
addPropertyChangeListener
public void addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Adds `PropertyChangeListener` to the listeners list.
 Each listeners receives [`OWN_PROPERTY_ADDED`](#OWN_PROPERTY_ADDED) and [`OWN_PROPERTY_REMOVED`](#OWN_PROPERTY_REMOVED) event types.
Parameters:
`listener` - the `PropertyChangeListener` to be added
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
removePropertyChangeListener
public void removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Removes `PropertyChangeListener` from the listeners list.
 Each listeners receives [`OWN_PROPERTY_ADDED`](#OWN_PROPERTY_ADDED) and [`OWN_PROPERTY_REMOVED`](#OWN_PROPERTY_REMOVED) event types.
Parameters:
`listener` - the PropertyChangeListener to be removed
See Also:
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
equalsTo
public boolean equalsTo([PropertyManager](PropertyManager.html) given)
generateDefaultDescriptionID
public static void generateDefaultDescriptionID([PropertyManager](PropertyManager.html) manager)
generateNullDescriptionID
public static void generateNullDescriptionID([PropertyManager](PropertyManager.html) manager)
equalsWithValues
public boolean equalsWithValues([PropertyManager](PropertyManager.html) pm,
 @CheckForNull
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> ids)
Check it equals with given property value.
Parameters:
`pm` - The given property value.
`ids` - properties IDs to check (may be null - to check all properties)
Returns:
boolean
removeProperty
public void removeProperty([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyIDs)
Removes all properties with given ids.
Parameters:
`propertyIDs` - ids of the properties to remove from the manager.
retainProperties
public void retainProperties([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> ids)
Removes all properties except the the ones with given ids.
Parameters:
`ids` - ids of the properties to leave in the manager.
isTheSame
public boolean isTheSame([PropertyManager](PropertyManager.html) manager)
Check if given property manager is the same as current. Managers are the same if names are equal and parent managers are equal
Parameters:
`manager` - manager
Returns:
true if the same
isFrozen
public boolean isFrozen()
setFrozen
public void setFrozen(boolean mFrozen)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Class PropertyManager">Class PropertyManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.properties.PropertyManager</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ExtendablePropertyManager.html" title="class in com.nomagic.magicdraw.properties">ExtendablePropertyManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PropertyManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>, <a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></span></div>
<div class="block">This class is used for managing of the set of the properties. The manager has name. Also manager can
 return some property with given property ID.</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IS_UNIQUE">IS_UNIQUE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies the property as "unique".</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OWN_PROPERTY_ADDED">OWN_PROPERTY_ADDED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Identifies type of <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans"><code>PropertyChangeEvent</code></a>.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OWN_PROPERTY_REMOVED">OWN_PROPERTY_REMOVED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies type of <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans"><code>PropertyChangeEvent</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PropertyManager</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs new property manager</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,java.util.List)">PropertyManager</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> parentPropertyManager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs new property manager.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.util.List)">PropertyManager</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs new property manager.</div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperties(java.util.Collection)">addProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the properties to the property manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the property to the property manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds <code>PropertyChangeListener</code> to the listeners list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#append(com.nomagic.magicdraw.properties.PropertyManager)">append</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds not existing properties from given manager to itself.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#append(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)">append</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 boolean makeUndefined,
 boolean mergeSources)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds not existing properties from given manager to itself.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.List)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds not existing properties from given list to itself.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#append(java.util.List,boolean,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties,
 boolean makeUndefined,
 boolean mergeSources)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds not existing properties from given list to itself.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#apply(com.nomagic.magicdraw.properties.PropertyManager)">apply</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#apply(java.util.Collection)">apply</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties from given list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#applyValues(java.util.Collection)">applyValues</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; col)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies properties values only from given list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#cloneProperties(java.util.List)">cloneProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#distinct(com.nomagic.magicdraw.properties.PropertyManager)">distinct</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> man)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets to itself properties those are not equal to the given properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#distinct(java.util.List)">distinct</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns properties those are not equal to the given properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equalsTo(com.nomagic.magicdraw.properties.PropertyManager)">equalsTo</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> given)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equalsWithValues(com.nomagic.magicdraw.properties.PropertyManager,java.util.Set)">equalsWithValues</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> pm,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check it equals with given property value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#generateDefaultDescriptionID(com.nomagic.magicdraw.properties.PropertyManager)">generateDefaultDescriptionID</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#generateNullDescriptionID(com.nomagic.magicdraw.properties.PropertyManager)">generateNullDescriptionID</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property class type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHiddenProperties()">getHiddenProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get ID</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns name of the property manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrderedProperties()">getOrderedProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnProperties()">getOwnProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of the properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentPropertyManager()">getParentPropertyManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of the properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the property from the properties list with given id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyByName(java.lang.String)">getPropertyByName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property from the properties list with given name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyle()">getStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get property style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hideParentProperty(java.lang.String)">hideParentProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hides given property with id from parent property manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFrozen()">isFrozen</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHiddenParentProperty(java.lang.String)">isHiddenParentProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if property with a given ID is hidden parent property</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTheSame(com.nomagic.magicdraw.properties.PropertyManager)">isTheSame</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if given property manager is the same as current.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isUndefinedStateOrValuesDiffer(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property)">isUndefinedStateOrValuesDiffer</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> first,
 <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> second)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager)">leaveTheSame</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes from this manager all properties those does not exist in the given manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)">leaveTheSame</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 boolean makeUndefined,
 boolean mergeSources)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes from this manager all properties those does not exist in the given manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#makeCopy()">makeCopy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Make copy of property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#makeOwnProperty(com.nomagic.magicdraw.properties.Property)">makeOwnProperty</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Makes given property as own property even if property with such id is in parent (makes property not shared)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mergeBooleanProperty(com.nomagic.magicdraw.properties.BooleanProperty,com.nomagic.magicdraw.properties.BooleanProperty)">mergeBooleanProperty</a><wbr/>(<a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> currentProp,
 <a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> otherProp)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mergeChoiceProperty(com.nomagic.magicdraw.properties.ChoiceProperty,com.nomagic.magicdraw.properties.ChoiceProperty)">mergeChoiceProperty</a><wbr/>(<a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> currentProperty,
 <a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> otherProperty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mergeElementProperty(com.nomagic.magicdraw.properties.ElementProperty,com.nomagic.magicdraw.properties.ElementProperty)">mergeElementProperty</a><wbr/>(<a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> currentProp,
 <a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> otherProp)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mergeProperties(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property,boolean,boolean)">mergeProperties</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> currentManagerProperty,
 <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 boolean makeUndefined,
 boolean mergeSources)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mergePropertyByType(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property)">mergePropertyByType</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> currentProperty,
 <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> otherProperty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens to <code>PropertyChangeEvents</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProperty(com.nomagic.magicdraw.properties.Property)">removeProperty</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the property from the  property manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProperty(java.lang.String)">removeProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the property with given ID from the  property manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProperty(java.util.Collection)">removeProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyIDs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all properties with given ids.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes <code>PropertyChangeListener</code> from the listeners list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#retainProperties(java.util.Collection)">retainProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all properties except the the ones with given ids.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFrozen(boolean)">setFrozen</a><wbr/>(boolean mFrozen)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setID(java.lang.String)">setID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets id for this property manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets name of the manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentPropertyManager(com.nomagic.magicdraw.properties.PropertyManager)">setParentPropertyManager</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> parentPropertyManager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set parent Property Manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentPropertyManagerOnly(com.nomagic.magicdraw.properties.PropertyManager)">setParentPropertyManagerOnly</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> parentPropertyManager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set parent Property Manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.List)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; prop)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the list of the properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPropertyEnableMap(java.lang.String,java.lang.Object%5B%5D%5B%5D)">setPropertyEnableMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[][] map)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set Property Enable Map</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyle(com.nomagic.magicdraw.properties.Style)">setStyle</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sGetID()">sGetID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Property manager simple ID getter (does not generate ID if it is not present).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shareProperty(com.nomagic.magicdraw.properties.Property)">shareProperty</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Makes given property shared form parent PropertyManager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showParentProperty(java.lang.String)">showParentProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show parent property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns info used for debug.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="OWN_PROPERTY_ADDED">
<h3>OWN_PROPERTY_ADDED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OWN_PROPERTY_ADDED</span></div>
<div class="block">Identifies type of <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans"><code>PropertyChangeEvent</code></a>. This type of even is fired
 when particular property is added to <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties"><code>PropertyManager</code></a> own properties collection.
 It may be triggered by <a href="#addProperty(com.nomagic.magicdraw.properties.Property)"><code>addProperty(Property)</code></a> or <a href="#makeOwnProperty(com.nomagic.magicdraw.properties.Property)"><code>makeOwnProperty(Property)</code></a> method call.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.PropertyManager.OWN_PROPERTY_ADDED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OWN_PROPERTY_REMOVED">
<h3>OWN_PROPERTY_REMOVED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OWN_PROPERTY_REMOVED</span></div>
<div class="block">Identifies type of <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans"><code>PropertyChangeEvent</code></a>. This type of even is fired
 when particular property is removed from <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties"><code>PropertyManager</code></a> own properties collection.
 It may be triggered by <a href="#removeProperty(com.nomagic.magicdraw.properties.Property)"><code>removeProperty(Property)</code></a> or <a href="#shareProperty(com.nomagic.magicdraw.properties.Property)"><code>shareProperty(Property)</code></a> method call.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.PropertyManager.OWN_PROPERTY_REMOVED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IS_UNIQUE">
<h3>IS_UNIQUE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IS_UNIQUE</span></div>
<div class="block">Identifies the property as "unique". Is set via <a href="Property.html#setAdditionalProperty(java.lang.String,java.lang.Object)"><code>Property.setAdditionalProperty(String, Object)</code></a>:
 <code>property.setAdditionalProperty(PropertyManager.IS_UNIQUE, true);</code><br/>
 Unique property will always be removed when calling <a href="#leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)"><code>leaveTheSame(PropertyManager, boolean, boolean)</code></a> method.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.properties.PropertyManager.IS_UNIQUE">Constant Field Values</a></li>
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
<h3>PropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyManager</span>()</div>
<div class="block">Constructs new property manager</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.util.List)">
<h3>PropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyManager</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Constructs new property manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the manager.</dd>
<dd><code>properties</code> - the list of properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.properties.PropertyManager,java.lang.String,java.util.List)">
<h3>PropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyManager</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> parentPropertyManager,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Constructs new property manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentPropertyManager</code> - parent property manager which can provides properties can be shared in this manager.</dd>
<dd><code>name</code> - the name of the manager.</dd>
<dd><code>properties</code> - the list of properties.</dd>
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
<section class="detail" id="getHiddenProperties()">
<h3>getHiddenProperties</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getHiddenProperties</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Get ID</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ID of property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sGetID()">
<h3>sGetID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">sGetID</span>()</div>
<div class="block">Property manager simple ID getter (does not generate ID if it is not present).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property manager ID or <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentPropertyManager()">
<h3>getParentPropertyManager</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getParentPropertyManager</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setParentPropertyManager(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setParentPropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentPropertyManager</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> parentPropertyManager)</span></div>
<div class="block">Set parent Property Manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentPropertyManager</code> - parent manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParentPropertyManagerOnly(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setParentPropertyManagerOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentPropertyManagerOnly</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> parentPropertyManager)</span></div>
<div class="block">Set parent Property Manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentPropertyManager</code> - parent manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Returns the property from the properties list with given id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the ID of property.</dd>
<dt>Returns:</dt>
<dd>property with given ID. Null if such property is not added into the manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyByName(java.lang.String)">
<h3>getPropertyByName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></span> <span class="element-name">getPropertyByName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns property from the properties list with given name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name of the property</dd>
<dt>Returns:</dt>
<dd>property with given name. Null if such property is not added into the manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</span></div>
<div class="block">Adds the property to the property manager.
 If property with such ID was already added, the old property is removed.
 Checking if property with same id already exists in parent property manager, and they value is the same do nothing</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prop</code> - the new property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProperties(java.util.Collection)">
<h3>addProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Adds the properties to the property manager.
 If property with such ID was already added, the old property is removed.
 Checking if property with same id already exists in parent property manager, and they value is the same do nothing</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - the new properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProperty(com.nomagic.magicdraw.properties.Property)">
<h3>removeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProperty</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</span></div>
<div class="block">Removes the property from the  property manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prop</code> - the property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProperty(java.lang.String)">
<h3>removeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Removes the property with given ID from the  property manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the property's ID.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</span> <span class="element-name">getProperties</span>()</div>
<div class="block">Returns the list of the properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all properties from this manager and parent managers.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnProperties()">
<h3>getOwnProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</span> <span class="element-name">getOwnProperties</span>()</div>
<div class="block">Returns the list of the properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all properties only from this manager. List is unmodifiable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperties(java.util.List)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; prop)</span></div>
<div class="block">Sets the list of the properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prop</code> - the list of new properties for this manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrderedProperties()">
<h3>getOrderedProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</span> <span class="element-name">getOrderedProperties</span>()</div>
<div class="block">Returns list of properties. Properties are stored in list no sorting needed</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Clones the manager. Does deep clone - all properties will be cloned too.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>the cloned manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cloneProperties(java.util.List)">
<h3>cloneProperties</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</span> <span class="element-name">cloneProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
</section>
</li>
<li>
<section class="detail" id="makeCopy()">
<h3>makeCopy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">makeCopy</span>()</div>
<div class="block">Make copy of property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Property Manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="apply(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>apply</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">apply</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
<div class="block">Applies properties from given manager.
 Property from given manager will be replaced with property from this manager if this manager:
 1.has property with such ID.
 2.state of this property is not UNDEFINED.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager which properties will be applied to this.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#apply(java.util.Collection)"><code>apply(Collection)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="apply(java.util.Collection)">
<h3>apply</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">apply</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Applies properties from given list.
 Property from given list will be replaced with property from this manager if this manager:
 1.has property with such ID.
 2.state of this property is not UNDEFINED.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - collection of properties to be applied to this.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyValues(java.util.Collection)">
<h3>applyValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">applyValues</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; col)</span></div>
<div class="block">Applies properties values only from given list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>col</code> - collection of properties to be applied to this.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>leaveTheSame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">leaveTheSame</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
<div class="block">Removes from this manager all properties those does not exist in the given manager.
 Property will be removed if given manager does not have property with the same ID.
 Existing property in this manager will be set to undefined state if
 property in the given manager has different value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the given manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="leaveTheSame(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)">
<h3>leaveTheSame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">leaveTheSame</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 boolean makeUndefined,
 boolean mergeSources)</span></div>
<div class="block">Removes from this manager all properties those does not exist in the given manager.
 Property will be removed if given manager does not have property with the same ID and the same value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the given manager.</dd>
<dd><code>makeUndefined</code> - existing property in this manager will be set to undefined state if property in given manager has different value.</dd>
<dd><code>mergeSources</code> - if true, properties sources will be merged</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mergeProperties(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property,boolean,boolean)">
<h3>mergeProperties</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">mergeProperties</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> currentManagerProperty,
 <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property,
 boolean makeUndefined,
 boolean mergeSources)</span></div>
</section>
</li>
<li>
<section class="detail" id="mergePropertyByType(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property)">
<h3>mergePropertyByType</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">mergePropertyByType</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> currentProperty,
 <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> otherProperty)</span></div>
</section>
</li>
<li>
<section class="detail" id="mergeBooleanProperty(com.nomagic.magicdraw.properties.BooleanProperty,com.nomagic.magicdraw.properties.BooleanProperty)">
<h3>mergeBooleanProperty</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">mergeBooleanProperty</span><wbr/><span class="parameters">(<a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> currentProp,
 <a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> otherProp)</span></div>
</section>
</li>
<li>
<section class="detail" id="mergeElementProperty(com.nomagic.magicdraw.properties.ElementProperty,com.nomagic.magicdraw.properties.ElementProperty)">
<h3>mergeElementProperty</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">mergeElementProperty</span><wbr/><span class="parameters">(<a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> currentProp,
 <a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> otherProp)</span></div>
</section>
</li>
<li>
<section class="detail" id="mergeChoiceProperty(com.nomagic.magicdraw.properties.ChoiceProperty,com.nomagic.magicdraw.properties.ChoiceProperty)">
<h3>mergeChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">mergeChoiceProperty</span><wbr/><span class="parameters">(<a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> currentProperty,
 <a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> otherProperty)</span></div>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Sets name of the manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the new name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns name of the property manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the name of the property manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="distinct(java.util.List)">
<h3>distinct</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt;</span> <span class="element-name">distinct</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Returns properties those are not equal to the given properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - the given properties.</dd>
<dt>Returns:</dt>
<dd>not equal properties to the given properties or empty list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUndefinedStateOrValuesDiffer(com.nomagic.magicdraw.properties.Property,com.nomagic.magicdraw.properties.Property)">
<h3>isUndefinedStateOrValuesDiffer</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUndefinedStateOrValuesDiffer</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> first,
 <a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> second)</span></div>
</section>
</li>
<li>
<section class="detail" id="distinct(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>distinct</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">distinct</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> man)</span></div>
<div class="block">Sets to itself properties those are not equal to the given properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>man</code> - the manager with given properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</span></div>
<div class="block">Listens to <code>PropertyChangeEvents</code>. Takes new value from the
 event(new value must be a list of properties) and sets these properties
 to itself.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - the property change event.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Accepts the given visitor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>visitor</code> - the PropertyVisitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Returns property class type.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="PropertyVisitorAcceptor.html#getClassType()">getClassType</a></code> in interface <code><a href="PropertyVisitorAcceptor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitorAcceptor</a></code></dd>
<dt>Returns:</dt>
<dd>PropertyID.PROPERTY_MANAGER</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="PropertyID.html#PROPERTY_MANAGER"><code>PropertyID.PROPERTY_MANAGER</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
<div class="block">Adds not existing properties from given manager to itself.
 The properties existence is checked by property ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the manager with properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(com.nomagic.magicdraw.properties.PropertyManager,boolean,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager,
 boolean makeUndefined,
 boolean mergeSources)</span></div>
<div class="block">Adds not existing properties from given manager to itself.
 The properties existence is checked by property ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the manager with properties.</dd>
<dd><code>makeUndefined</code> - existing property in this manager will be set to undefined state if property in given manager has different value.</dd>
<dd><code>mergeSources</code> - if true, properties sources will be merged</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.List)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Adds not existing properties from given list to itself.
 The properties existence is checked by property ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - the list of given properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.List,boolean,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties,
 boolean makeUndefined,
 boolean mergeSources)</span></div>
<div class="block">Adds not existing properties from given list to itself.
 The properties existence is checked by property ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - the list of given properties.</dd>
<dd><code>makeUndefined</code> - existing property in this manager will be set to undefined state if property in given manager has different value.</dd>
<dd><code>mergeSources</code> - if true, properties sources will be merged</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns info used for debug.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>info for debug</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shareProperty(com.nomagic.magicdraw.properties.Property)">
<h3>shareProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">shareProperty</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</span></div>
<div class="block">Makes given property shared form parent PropertyManager. Value changed in parent will affect property in this property manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prop</code> - property to share.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeOwnProperty(com.nomagic.magicdraw.properties.Property)">
<h3>makeOwnProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">makeOwnProperty</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> prop)</span></div>
<div class="block">Makes given property as own property even if property with such id is in parent (makes property not shared)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prop</code> - property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideParentProperty(java.lang.String)">
<h3>hideParentProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">hideParentProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</span></div>
<div class="block">Hides given property with id from parent property manager. Not that if property with this id is in this property manager nothing will be changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyID</code> - property ID to hide from parent manager;</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isHiddenParentProperty(java.lang.String)">
<h3>isHiddenParentProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHiddenParentProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</span></div>
<div class="block">Check if property with a given ID is hidden parent property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyID</code> - property ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showParentProperty(java.lang.String)">
<h3>showParentProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showParentProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyID)</span></div>
<div class="block">Show parent property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyID</code> - property ID</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(java.lang.String)">
<h3>setID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sets id for this property manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - new id of this property manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyle()">
<h3>getStyle</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getStyle</span>()</div>
<div class="block">Get property style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns the style.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStyle(com.nomagic.magicdraw.properties.Style)">
<h3>setStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyle</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style)</span></div>
<div class="block">Set style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - The style to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPropertyEnableMap(java.lang.String,java.lang.Object[][])">
<h3>setPropertyEnableMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPropertyEnableMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[][] map)</span></div>
<div class="block">Set Property Enable Map</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyId</code> - Property id.</dd>
<dd><code>map</code> - map</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Adds <code>PropertyChangeListener</code> to the listeners list.
 Each listeners receives <a href="#OWN_PROPERTY_ADDED"><code>OWN_PROPERTY_ADDED</code></a> and <a href="#OWN_PROPERTY_REMOVED"><code>OWN_PROPERTY_REMOVED</code></a> event types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the <code>PropertyChangeListener</code> to be added</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Removes <code>PropertyChangeListener</code> from the listeners list.
 Each listeners receives <a href="#OWN_PROPERTY_ADDED"><code>OWN_PROPERTY_ADDED</code></a> and <a href="#OWN_PROPERTY_REMOVED"><code>OWN_PROPERTY_REMOVED</code></a> event types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the PropertyChangeListener to be removed</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equalsTo(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>equalsTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equalsTo</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> given)</span></div>
</section>
</li>
<li>
<section class="detail" id="generateDefaultDescriptionID(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>generateDefaultDescriptionID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">generateDefaultDescriptionID</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
</section>
</li>
<li>
<section class="detail" id="generateNullDescriptionID(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>generateNullDescriptionID</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">generateNullDescriptionID</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
</section>
</li>
<li>
<section class="detail" id="equalsWithValues(com.nomagic.magicdraw.properties.PropertyManager,java.util.Set)">
<h3>equalsWithValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equalsWithValues</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> pm,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</span></div>
<div class="block">Check it equals with given property value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pm</code> - The given property value.</dd>
<dd><code>ids</code> - properties IDs to check (may be null - to check all properties)</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProperty(java.util.Collection)">
<h3>removeProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyIDs)</span></div>
<div class="block">Removes all properties with given ids.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyIDs</code> - ids of the properties to remove from the manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="retainProperties(java.util.Collection)">
<h3>retainProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">retainProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</span></div>
<div class="block">Removes all properties except the the ones with given ids.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ids</code> - ids of the properties to leave in the manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTheSame(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>isTheSame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTheSame</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> manager)</span></div>
<div class="block">Check if given property manager is the same as current. Managers are the same if names are equal and parent managers are equal</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager</dd>
<dt>Returns:</dt>
<dd>true if the same</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFrozen()">
<h3>isFrozen</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFrozen</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setFrozen(boolean)">
<h3>setFrozen</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFrozen</span><wbr/><span class="parameters">(boolean mFrozen)</span></div>
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
