# JAVA OPENAPI: AbstractRepository (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/jmi/reflect/AbstractRepository.html
- source_path: `com/nomagic/uml2/ext/jmi/reflect/AbstractRepository.html`
- source_sha256: `54b42af4050c07d895e37cb7c48cedcf85326b6228aa4a65b190d06cd5294dd1`
- captured_utc: `2026-07-14T16:52:40.367257+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.reflect](package-summary.html)

## Class AbstractRepository

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
[com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage](AbstractRefPackage.html)
com.nomagic.uml2.ext.jmi.reflect.AbstractRepository

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`, `com.nomagic.uml2.ext.jmi.MapOwner`, `[AbstractRefBaseObject](AbstractRefBaseObject.html)`, `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefPackage`

public abstract classAbstractRepository
extends [AbstractRefPackage](AbstractRefPackage.html)
implements com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[AbstractRepository.Calculator](AbstractRepository.Calculator.html)`
Calculator used in to calculate derived values.
`static enum`
`[AbstractRepository.Calculators](AbstractRepository.Calculators.html)`

`static interface`
`[AbstractRepository.CandidatesForDisposeListener](AbstractRepository.CandidatesForDisposeListener.html)`
Candidates for dispose listener
`final class`
`[AbstractRepository.MofRepository](AbstractRepository.MofRepository.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[interfacePackagePrefixes](#interfacePackagePrefixes)`

`protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[interfacePackagePrefixToRefPackage](#interfacePackagePrefixToRefPackage)`

`protected com.io_software.catools.tas.mof.TASMofRepository`
`[mofRepository](#mofRepository)`
Fields inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
`mMetaObject, repository`
Fields inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElementRepository
`BASIC_VERSION`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractRepository](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[AbstractRepository.Calculator](AbstractRepository.Calculator.html)`
`[addCalculator](#addCalculator(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculators,com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculator))([AbstractRepository.Calculators](AbstractRepository.Calculators.html) id,
 [AbstractRepository.Calculator](AbstractRepository.Calculator.html) calculator)`

`void`
`[addCandidateElementForDispose](#addCandidateElementForDispose(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`

`void`
`[addCandidateForDispose](#addCandidateForDispose(javax.jmi.reflect.RefObject))(javax.jmi.reflect.RefObject object)`

`void`
`[addCandidatesForDisposeListener](#addCandidatesForDisposeListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.CandidatesForDisposeListener))([AbstractRepository.CandidatesForDisposeListener](AbstractRepository.CandidatesForDisposeListener.html) listener)`
Adds a [`AbstractRepository.CandidatesForDisposeListener`](AbstractRepository.CandidatesForDisposeListener.html) to get notifications about
`boolean`
`[canSetID](#canSetID())()`

`protected void`
`[checkAlive](#checkAlive())()`

`protected void`
`[classProxies](#classProxies())()`

`void`
`[clearCandidatesForDispose](#clearCandidatesForDispose())()`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[createMap](#createMap(com.nomagic.uml2.ext.jmi.MapOwner,java.lang.String))(com.nomagic.uml2.ext.jmi.MapOwner owner,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mapName)`

`final long`
`[getBasicVersion](#getBasicVersion())()`
Returns the repository version.
`[AbstractRepository.Calculator](AbstractRepository.Calculator.html)`
`[getCalculator](#getCalculator(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculators))([AbstractRepository.Calculators](AbstractRepository.Calculators.html) calculatorName)`

`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<javax.jmi.reflect.RefObject>`
`[getCandidatesForDispose](#getCandidatesForDispose())()`

`com.nomagic.util.Counter`
`[getCounter](#getCounter())()`
Standalone repositories (those, having no Project object)
 can have a separate counter assigned to them.
`javax.jmi.reflect.RefObject`
`[getElementById](#getElementById(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`[ElementsFactory](../../../impl/ElementsFactory.html)`
`[getElementsFactory](#getElementsFactory())()`

`[EventSupport](../EventSupport.html)`
`[getEventSupport](#getEventSupport())()`

`com.dassault_systemes.modeler.foundation.model.IDProxy`
`[getIDProxy](#getIDProxy())()`

`com.io_software.catools.tas.mof.TASRepository`
`[getMetamodelProvider](#getMetamodelProvider())()`

`com.io_software.catools.tas.mof.TASMofRepository`
`[getMofRepository](#getMofRepository())()`

`int`
`[getObjectsCount](#getObjectsCount())()`

`com.nomagic.uml2.ext.jmi.reflect.ElementRegistry`
`[getProject](#getProject())()`

`[AbstractRepository](AbstractRepository.html)`
`[getRepository](#getRepository())()`
Get repository.
`[TransactionManager](../../../transaction/TransactionManager.html)`
`[getTransactionManager](#getTransactionManager())()`

`com.nomagic.uml2.impl.ValuesTable`
`[getValuesTable](#getValuesTable())()`

`final long`
`[getVersion](#getVersion())()`
Returns the repository version.
`void`
`[invokeAfterTransaction](#invokeAfterTransaction(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) r)`
If at the current moment firing cached events, running runnable after these events are fired.
`boolean`
`[isAlive](#isAlive())()`

`boolean`
`[isFullPreLoad](#isFullPreLoad())()`

`boolean`
`[isRawMode](#isRawMode())()`
Deprecated.
not used
`void`
`[kill](#kill())()`
Destroys repository.
`final void`
`[nextBasicVersion](#nextBasicVersion())()`
Sets new repository version.
`final void`
`[nextVersion](#nextVersion())()`
Deprecated, for removal: This API element is subject to removal in a future version.
use {[`nextBasicVersion()`](#nextBasicVersion())}
`javax.jmi.reflect.RefEnum`
`[refGetEnum](#refGetEnum(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) enumName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) args)`
The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
`void`
`[registerElement](#registerElement(javax.jmi.reflect.RefBaseObject))(javax.jmi.reflect.RefBaseObject object)`

`void`
`[registerModelElement](#registerModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`

`void`
`[removeCandidateElementForDispose](#removeCandidateElementForDispose(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`

`void`
`[removeCandidateForDispose](#removeCandidateForDispose(javax.jmi.reflect.RefObject))(javax.jmi.reflect.RefObject object)`

`void`
`[removeCandidatesForDisposeListener](#removeCandidatesForDisposeListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.CandidatesForDisposeListener))([AbstractRepository.CandidatesForDisposeListener](AbstractRepository.CandidatesForDisposeListener.html) listener)`

`void`
`[setCanSetID](#setCanSetID(boolean))(boolean canSetID)`

`void`
`[setCounter](#setCounter(com.nomagic.util.Counter))(com.nomagic.util.Counter count)`
Standalone repositories (those, having no Project object)
 can have a separate counter assigned to them.
`void`
`[setElementsFactory](#setElementsFactory(com.nomagic.uml2.impl.ElementsFactory))([ElementsFactory](../../../impl/ElementsFactory.html) elementsFactory)`

`protected void`
`[setEventSupport](#setEventSupport(com.nomagic.uml2.ext.jmi.EventSupport))([EventSupport](../EventSupport.html) eventSupport)`

`void`
`[setIDProxy](#setIDProxy(com.dassault_systemes.modeler.foundation.model.IDProxy))(com.dassault_systemes.modeler.foundation.model.IDProxy useEsiID)`

`void`
`[setProject](#setProject(com.nomagic.uml2.ext.jmi.reflect.ElementRegistry))(com.nomagic.uml2.ext.jmi.reflect.ElementRegistry project)`

`void`
`[setRawMode](#setRawMode(boolean))(boolean rawMode)`
Deprecated.
not used
`boolean`
`[unRegisterBaseElement](#unRegisterBaseElement(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../magicdraw/uml/BaseElement.html) element)`

`void`
`[unRegisterElement](#unRegisterElement(javax.jmi.reflect.RefBaseObject))(javax.jmi.reflect.RefBaseObject object)`

`void`
`[unRegisterModelElement](#unRegisterModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement))(com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.[AbstractRefPackage](AbstractRefPackage.html)
`[addAssociation](AbstractRefPackage.html#addAssociation(java.lang.String,javax.jmi.reflect.RefAssociation)), [addClass](AbstractRefPackage.html#addClass(java.lang.String,javax.jmi.reflect.RefClass)), [addPackage](AbstractRefPackage.html#addPackage(java.lang.String,javax.jmi.reflect.RefBaseObject)), [getMetaObjects](AbstractRefPackage.html#getMetaObjects()), [internalError](AbstractRefPackage.html#internalError(java.lang.String,javax.jmi.reflect.InvalidCallException)), [refAllAssociations](AbstractRefPackage.html#refAllAssociations()), [refAllClasses](AbstractRefPackage.html#refAllClasses()), [refAllPackages](AbstractRefPackage.html#refAllPackages()), [refAssociation](AbstractRefPackage.html#refAssociation(java.lang.String)), [refAssociation](AbstractRefPackage.html#refAssociation(javax.jmi.reflect.RefObject)), [refClass](AbstractRefPackage.html#refClass(java.lang.String)), [refClass](AbstractRefPackage.html#refClass(javax.jmi.reflect.RefObject)), [refCreateStruct](AbstractRefPackage.html#refCreateStruct(java.lang.String,java.util.List)), [refCreateStruct](AbstractRefPackage.html#refCreateStruct(javax.jmi.reflect.RefObject,java.util.List)), [refDelete](AbstractRefPackage.html#refDelete()), [refGetEnum](AbstractRefPackage.html#refGetEnum(javax.jmi.reflect.RefObject,java.lang.String)), [refPackage](AbstractRefPackage.html#refPackage(java.lang.String)), [refPackage](AbstractRefPackage.html#refPackage(javax.jmi.reflect.RefObject)), [removeClass](AbstractRefPackage.html#removeClass(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass)), [removePackage](AbstractRefPackage.html#removePackage(javax.jmi.reflect.RefBaseObject))`
Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
`mapClear, mapPut, mapPutAll, mapRemove, mof_getRepository, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints, setMofID, setOwner, setRefMetaObject, setRepository`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`

============ FIELD DETAIL =========== 
Field Details
interfacePackagePrefixToRefPackage
protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) interfacePackagePrefixToRefPackage
interfacePackagePrefixes
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) interfacePackagePrefixes
mofRepository
protected com.io_software.catools.tas.mof.TASMofRepository mofRepository
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractRepository
public AbstractRepository()
 ============ METHOD DETAIL ========== 
Method Details
isFullPreLoad
public boolean isFullPreLoad()
Specified by:
`isFullPreLoad` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
getIDProxy
public com.dassault_systemes.modeler.foundation.model.IDProxy getIDProxy()
Specified by:
`getIDProxy` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
setIDProxy
public void setIDProxy(com.dassault_systemes.modeler.foundation.model.IDProxy useEsiID)
Specified by:
`setIDProxy` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
getVersion
public final long getVersion()
Description copied from interface: `com.dassault_systemes.modeler.foundation.model.ModelElementRepository`
Returns the repository version.
 It is a number that will be increased after any repository change.
Specified by:
`getVersion` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
Returns:
repository version.
getBasicVersion
public final long getBasicVersion()
Description copied from interface: `com.dassault_systemes.modeler.foundation.model.ModelElementRepository`
Returns the repository version.
 It is a number that will be increased after repository update from persistence.
Specified by:
`getBasicVersion` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
Returns:
repository version.
nextBasicVersion
public final void nextBasicVersion()
Sets new repository version.
Specified by:
`nextBasicVersion` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
nextVersion
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public final void nextVersion()
Deprecated, for removal: This API element is subject to removal in a future version.
use {[`nextBasicVersion()`](#nextBasicVersion())}
setEventSupport
protected void setEventSupport([EventSupport](../EventSupport.html) eventSupport)
getElementsFactory
public [ElementsFactory](../../../impl/ElementsFactory.html) getElementsFactory()
setElementsFactory
public void setElementsFactory([ElementsFactory](../../../impl/ElementsFactory.html) elementsFactory)
getElementById
@CheckForNullpublic javax.jmi.reflect.RefObject getElementById([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Returns:
element registered with such id.
checkAlive
protected void checkAlive()
isAlive
public boolean isAlive()
Returns:
true if repository is not killed.
kill
public void kill()
Destroys repository.
classProxies
protected void classProxies()
getMofRepository
public com.io_software.catools.tas.mof.TASMofRepository getMofRepository()
createMap
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) createMap(com.nomagic.uml2.ext.jmi.MapOwner owner,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mapName)
getEventSupport
public [EventSupport](../EventSupport.html) getEventSupport()
Specified by:
`getEventSupport` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
Returns:
Event support for this repository
registerModelElement
public void registerModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Specified by:
`registerModelElement` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
registerElement
public void registerElement(javax.jmi.reflect.RefBaseObject object)
getObjectsCount
public int getObjectsCount()
unRegisterModelElement
public void unRegisterModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Specified by:
`unRegisterModelElement` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
unRegisterElement
public void unRegisterElement(javax.jmi.reflect.RefBaseObject object)
unRegisterBaseElement
public boolean unRegisterBaseElement([BaseElement](../../../../magicdraw/uml/BaseElement.html) element)
getRepository
public [AbstractRepository](AbstractRepository.html) getRepository()
Description copied from interface: `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`
Get repository.
Specified by:
`[getRepository](AbstractRefBaseObject.html#getRepository())` in interface `[AbstractRefBaseObject](AbstractRefBaseObject.html)`
Specified by:
`getRepository` in interface `com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider`
Overrides:
`getRepository` in class `com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl`
Returns:
repository.
getProject
public com.nomagic.uml2.ext.jmi.reflect.ElementRegistry getProject()
Specified by:
`getProject` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
setProject
public void setProject(com.nomagic.uml2.ext.jmi.reflect.ElementRegistry project)
Specified by:
`setProject` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
refGetEnum
@CheckForNullpublic javax.jmi.reflect.RefEnum refGetEnum([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) enumName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) args)
Description copied from class: `[AbstractRefPackage](AbstractRefPackage.html#refGetEnum(java.lang.String,java.lang.String))`
The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
 Note that the type of enumeration is defined by the meta object that owns
 the metaLiteral object. InvalidCallException is raised if the enumType
 parameter does not designate a valid enumeration. InvalidNameException is
 raised when the enumName does not denote a valid enum name. This
 refGetEnum returns the enumeration object representing the enumeration
 literal. specific analog: none. return type: RefEnum parameters:
 RefObject enumType (or String enumName ) String literalName exceptions:
 JmiException (TypeMismatchException, InvalidCallException,
 InvalidNameException, java.lang.NullPointerException)
Specified by:
`refGetEnum` in interface `javax.jmi.reflect.RefPackage`
Overrides:
`[refGetEnum](AbstractRefPackage.html#refGetEnum(java.lang.String,java.lang.String))` in class `[AbstractRefPackage](AbstractRefPackage.html)`
getMetamodelProvider
@CheckForNullpublic com.io_software.catools.tas.mof.TASRepository getMetamodelProvider()
getCounter
public com.nomagic.util.Counter getCounter()
Standalone repositories (those, having no Project object)
 can have a separate counter assigned to them.
setCounter
public void setCounter(com.nomagic.util.Counter count)
Standalone repositories (those, having no Project object)
 can have a separate counter assigned to them.
canSetID
public boolean canSetID()
setCanSetID
public void setCanSetID(boolean canSetID)
Parameters:
`canSetID` - The canSetID to set.
getValuesTable
public com.nomagic.uml2.impl.ValuesTable getValuesTable()
invokeAfterTransaction
public void invokeAfterTransaction([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) r)
If at the current moment firing cached events, running runnable after these events are fired. Running now in other case.
Parameters:
`r` - [`Runnable`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) to run.
isRawMode
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public boolean isRawMode()
Deprecated.
not used
setRawMode
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void setRawMode(boolean rawMode)
Deprecated.
not used
getTransactionManager
public [TransactionManager](../../../transaction/TransactionManager.html) getTransactionManager()
addCandidateForDispose
public void addCandidateForDispose(javax.jmi.reflect.RefObject object)
removeCandidateForDispose
public void removeCandidateForDispose(javax.jmi.reflect.RefObject object)
addCandidateElementForDispose
public void addCandidateElementForDispose(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Specified by:
`addCandidateElementForDispose` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
removeCandidateElementForDispose
public void removeCandidateElementForDispose(com.dassault_systemes.modeler.foundation.model.ModelElement element)
Specified by:
`removeCandidateElementForDispose` in interface `com.dassault_systemes.modeler.foundation.model.ModelElementRepository<com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,javax.jmi.reflect.RefObject,[EventSupport](../EventSupport.html)>`
getCandidatesForDispose
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<javax.jmi.reflect.RefObject> getCandidatesForDispose()
clearCandidatesForDispose
public void clearCandidatesForDispose()
addCandidatesForDisposeListener
public void addCandidatesForDisposeListener([AbstractRepository.CandidatesForDisposeListener](AbstractRepository.CandidatesForDisposeListener.html) listener)
Adds a [`AbstractRepository.CandidatesForDisposeListener`](AbstractRepository.CandidatesForDisposeListener.html) to get notifications about
Parameters:
`listener` - the listener
removeCandidatesForDisposeListener
public void removeCandidatesForDisposeListener([AbstractRepository.CandidatesForDisposeListener](AbstractRepository.CandidatesForDisposeListener.html) listener)
getCalculator
public [AbstractRepository.Calculator](AbstractRepository.Calculator.html) getCalculator([AbstractRepository.Calculators](AbstractRepository.Calculators.html) calculatorName)
addCalculator
@CheckForNullpublic [AbstractRepository.Calculator](AbstractRepository.Calculator.html) addCalculator([AbstractRepository.Calculators](AbstractRepository.Calculators.html) id,
 [AbstractRepository.Calculator](AbstractRepository.Calculator.html) calculator)
Parameters:
`id` - calculator identifier.
`calculator` - value calculator.
Returns:
calculator which was registered by same id.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.reflect</a></div>
<h1 class="title" title="Class AbstractRepository">Class AbstractRepository</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl
<div class="inheritance"><a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.reflect.AbstractRepository</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code>, <code>com.nomagic.uml2.ext.jmi.MapOwner</code>, <code><a href="AbstractRefBaseObject.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRefBaseObject</a></code>, <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefPackage</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractRepository</span>
<span class="extends-implements">extends <a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a>
implements com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</span></div>
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
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="AbstractRepository.Calculator.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculator</a></code></div>
<div class="col-last even-row-color">
<div class="block">Calculator used in to calculate derived values.</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="AbstractRepository.Calculators.html" title="enum class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculators</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="AbstractRepository.CandidatesForDisposeListener.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.CandidatesForDisposeListener</a></code></div>
<div class="col-last even-row-color">
<div class="block">Candidates for dispose listener</div>
</div>
<div class="col-first odd-row-color"><code>final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="AbstractRepository.MofRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.MofRepository</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#interfacePackagePrefixes">interfacePackagePrefixes</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#interfacePackagePrefixToRefPackage">interfacePackagePrefixToRefPackage</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>protected com.io_software.catools.tas.mof.TASMofRepository</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#mofRepository">mofRepository</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl">Fields inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</h3>
<code>mMetaObject, repository</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElementRepository">Fields inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElementRepository</h3>
<code>BASIC_VERSION</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractRepository</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractRepository.Calculator.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCalculator(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculators,com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculator)">addCalculator</a><wbr/>(<a href="AbstractRepository.Calculators.html" title="enum class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculators</a> id,
 <a href="AbstractRepository.Calculator.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculator</a> calculator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCandidateElementForDispose(com.dassault_systemes.modeler.foundation.model.ModelElement)">addCandidateElementForDispose</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCandidateForDispose(javax.jmi.reflect.RefObject)">addCandidateForDispose</a><wbr/>(javax.jmi.reflect.RefObject object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCandidatesForDisposeListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.CandidatesForDisposeListener)">addCandidatesForDisposeListener</a><wbr/>(<a href="AbstractRepository.CandidatesForDisposeListener.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.CandidatesForDisposeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a <a href="AbstractRepository.CandidatesForDisposeListener.html" title="interface in com.nomagic.uml2.ext.jmi.reflect"><code>AbstractRepository.CandidatesForDisposeListener</code></a> to get notifications about</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canSetID()">canSetID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkAlive()">checkAlive</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#classProxies()">classProxies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCandidatesForDispose()">clearCandidatesForDispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMap(com.nomagic.uml2.ext.jmi.MapOwner,java.lang.String)">createMap</a><wbr/>(com.nomagic.uml2.ext.jmi.MapOwner owner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mapName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBasicVersion()">getBasicVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the repository version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractRepository.Calculator.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCalculator(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculators)">getCalculator</a><wbr/>(<a href="AbstractRepository.Calculators.html" title="enum class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculators</a> calculatorName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;javax.jmi.reflect.RefObject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCandidatesForDispose()">getCandidatesForDispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.util.Counter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCounter()">getCounter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Standalone repositories (those, having no Project object)
 can have a separate counter assigned to them.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefObject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementById(java.lang.String)">getElementById</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsFactory()">getElementsFactory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEventSupport()">getEventSupport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.model.IDProxy</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIDProxy()">getIDProxy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.io_software.catools.tas.mof.TASRepository</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetamodelProvider()">getMetamodelProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.io_software.catools.tas.mof.TASMofRepository</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMofRepository()">getMofRepository</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectsCount()">getObjectsCount</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepository()">getRepository</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get repository.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../transaction/TransactionManager.html" title="interface in com.nomagic.uml2.transaction">TransactionManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransactionManager()">getTransactionManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.uml2.impl.ValuesTable</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValuesTable()">getValuesTable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion()">getVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the repository version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeAfterTransaction(java.lang.Runnable)">invokeAfterTransaction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If at the current moment firing cached events, running runnable after these events are fired.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAlive()">isAlive</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isFullPreLoad()">isFullPreLoad</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isRawMode()">isRawMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#kill()">kill</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Destroys repository.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#nextBasicVersion()">nextBasicVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new repository version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#nextVersion()">nextVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use {<a href="#nextBasicVersion()"><code>nextBasicVersion()</code></a>}</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>javax.jmi.reflect.RefEnum</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#refGetEnum(java.lang.String,java.lang.String)">refGetEnum</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> enumName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> args)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerElement(javax.jmi.reflect.RefBaseObject)">registerElement</a><wbr/>(javax.jmi.reflect.RefBaseObject object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">registerModelElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCandidateElementForDispose(com.dassault_systemes.modeler.foundation.model.ModelElement)">removeCandidateElementForDispose</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCandidateForDispose(javax.jmi.reflect.RefObject)">removeCandidateForDispose</a><wbr/>(javax.jmi.reflect.RefObject object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCandidatesForDisposeListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.CandidatesForDisposeListener)">removeCandidatesForDisposeListener</a><wbr/>(<a href="AbstractRepository.CandidatesForDisposeListener.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.CandidatesForDisposeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCanSetID(boolean)">setCanSetID</a><wbr/>(boolean canSetID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCounter(com.nomagic.util.Counter)">setCounter</a><wbr/>(com.nomagic.util.Counter count)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Standalone repositories (those, having no Project object)
 can have a separate counter assigned to them.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElementsFactory(com.nomagic.uml2.impl.ElementsFactory)">setElementsFactory</a><wbr/>(<a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> elementsFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEventSupport(com.nomagic.uml2.ext.jmi.EventSupport)">setEventSupport</a><wbr/>(<a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a> eventSupport)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIDProxy(com.dassault_systemes.modeler.foundation.model.IDProxy)">setIDProxy</a><wbr/>(com.dassault_systemes.modeler.foundation.model.IDProxy useEsiID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProject(com.nomagic.uml2.ext.jmi.reflect.ElementRegistry)">setProject</a><wbr/>(com.nomagic.uml2.ext.jmi.reflect.ElementRegistry project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setRawMode(boolean)">setRawMode</a><wbr/>(boolean rawMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unRegisterBaseElement(com.nomagic.magicdraw.uml.BaseElement)">unRegisterBaseElement</a><wbr/>(<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unRegisterElement(javax.jmi.reflect.RefBaseObject)">unRegisterElement</a><wbr/>(javax.jmi.reflect.RefBaseObject object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unRegisterModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">unRegisterModelElement</a><wbr/>(com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefPackage">Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.<a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a></h3>
<code><a href="AbstractRefPackage.html#addAssociation(java.lang.String,javax.jmi.reflect.RefAssociation)">addAssociation</a>, <a href="AbstractRefPackage.html#addClass(java.lang.String,javax.jmi.reflect.RefClass)">addClass</a>, <a href="AbstractRefPackage.html#addPackage(java.lang.String,javax.jmi.reflect.RefBaseObject)">addPackage</a>, <a href="AbstractRefPackage.html#getMetaObjects()">getMetaObjects</a>, <a href="AbstractRefPackage.html#internalError(java.lang.String,javax.jmi.reflect.InvalidCallException)">internalError</a>, <a href="AbstractRefPackage.html#refAllAssociations()">refAllAssociations</a>, <a href="AbstractRefPackage.html#refAllClasses()">refAllClasses</a>, <a href="AbstractRefPackage.html#refAllPackages()">refAllPackages</a>, <a href="AbstractRefPackage.html#refAssociation(java.lang.String)">refAssociation</a>, <a href="AbstractRefPackage.html#refAssociation(javax.jmi.reflect.RefObject)">refAssociation</a>, <a href="AbstractRefPackage.html#refClass(java.lang.String)">refClass</a>, <a href="AbstractRefPackage.html#refClass(javax.jmi.reflect.RefObject)">refClass</a>, <a href="AbstractRefPackage.html#refCreateStruct(java.lang.String,java.util.List)">refCreateStruct</a>, <a href="AbstractRefPackage.html#refCreateStruct(javax.jmi.reflect.RefObject,java.util.List)">refCreateStruct</a>, <a href="AbstractRefPackage.html#refDelete()">refDelete</a>, <a href="AbstractRefPackage.html#refGetEnum(javax.jmi.reflect.RefObject,java.lang.String)">refGetEnum</a>, <a href="AbstractRefPackage.html#refPackage(java.lang.String)">refPackage</a>, <a href="AbstractRefPackage.html#refPackage(javax.jmi.reflect.RefObject)">refPackage</a>, <a href="AbstractRefPackage.html#removeClass(com.nomagic.uml2.ext.jmi.reflect.AbstractRefClass)">removeClass</a>, <a href="AbstractRefPackage.html#removePackage(javax.jmi.reflect.RefBaseObject)">removePackage</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl">Methods inherited from class com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</h3>
<code>mapClear, mapPut, mapPutAll, mapRemove, mof_getRepository, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints, setMofID, setOwner, setRefMetaObject, setRepository</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
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
<section class="detail" id="interfacePackagePrefixToRefPackage">
<h3>interfacePackagePrefixToRefPackage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">interfacePackagePrefixToRefPackage</span></div>
</section>
</li>
<li>
<section class="detail" id="interfacePackagePrefixes">
<h3>interfacePackagePrefixes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">interfacePackagePrefixes</span></div>
</section>
</li>
<li>
<section class="detail" id="mofRepository">
<h3>mofRepository</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.io_software.catools.tas.mof.TASMofRepository</span> <span class="element-name">mofRepository</span></div>
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
<h3>AbstractRepository</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractRepository</span>()</div>
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
<section class="detail" id="isFullPreLoad()">
<h3>isFullPreLoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isFullPreLoad</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isFullPreLoad</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIDProxy()">
<h3>getIDProxy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.model.IDProxy</span> <span class="element-name">getIDProxy</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getIDProxy</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIDProxy(com.dassault_systemes.modeler.foundation.model.IDProxy)">
<h3>setIDProxy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIDProxy</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.IDProxy useEsiID)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setIDProxy</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion()">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">long</span> <span class="element-name">getVersion</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository</code></span></div>
<div class="block">Returns the repository version.
 It is a number that will be increased after any repository change.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getVersion</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>repository version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBasicVersion()">
<h3>getBasicVersion</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">long</span> <span class="element-name">getBasicVersion</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository</code></span></div>
<div class="block">Returns the repository version.
 It is a number that will be increased after repository update from persistence.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getBasicVersion</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>repository version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="nextBasicVersion()">
<h3>nextBasicVersion</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">nextBasicVersion</span>()</div>
<div class="block">Sets new repository version.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>nextBasicVersion</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="nextVersion()">
<h3>nextVersion</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">nextVersion</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use {<a href="#nextBasicVersion()"><code>nextBasicVersion()</code></a>}</div>
</div>
</section>
</li>
<li>
<section class="detail" id="setEventSupport(com.nomagic.uml2.ext.jmi.EventSupport)">
<h3>setEventSupport</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setEventSupport</span><wbr/><span class="parameters">(<a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a> eventSupport)</span></div>
</section>
</li>
<li>
<section class="detail" id="getElementsFactory()">
<h3>getElementsFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a></span> <span class="element-name">getElementsFactory</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setElementsFactory(com.nomagic.uml2.impl.ElementsFactory)">
<h3>setElementsFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElementsFactory</span><wbr/><span class="parameters">(<a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> elementsFactory)</span></div>
</section>
</li>
<li>
<section class="detail" id="getElementById(java.lang.String)">
<h3>getElementById</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefObject</span> <span class="element-name">getElementById</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element registered with such id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkAlive()">
<h3>checkAlive</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">checkAlive</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isAlive()">
<h3>isAlive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAlive</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if repository is not killed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="kill()">
<h3>kill</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">kill</span>()</div>
<div class="block">Destroys repository.</div>
</section>
</li>
<li>
<section class="detail" id="classProxies()">
<h3>classProxies</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">classProxies</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMofRepository()">
<h3>getMofRepository</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.io_software.catools.tas.mof.TASMofRepository</span> <span class="element-name">getMofRepository</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createMap(com.nomagic.uml2.ext.jmi.MapOwner,java.lang.String)">
<h3>createMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">createMap</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.MapOwner owner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mapName)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEventSupport()">
<h3>getEventSupport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a></span> <span class="element-name">getEventSupport</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getEventSupport</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>Event support for this repository</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>registerModelElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerModelElement</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>registerModelElement</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerElement(javax.jmi.reflect.RefBaseObject)">
<h3>registerElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerElement</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject object)</span></div>
</section>
</li>
<li>
<section class="detail" id="getObjectsCount()">
<h3>getObjectsCount</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getObjectsCount</span>()</div>
</section>
</li>
<li>
<section class="detail" id="unRegisterModelElement(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>unRegisterModelElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unRegisterModelElement</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>unRegisterModelElement</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unRegisterElement(javax.jmi.reflect.RefBaseObject)">
<h3>unRegisterElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unRegisterElement</span><wbr/><span class="parameters">(javax.jmi.reflect.RefBaseObject object)</span></div>
</section>
</li>
<li>
<section class="detail" id="unRegisterBaseElement(com.nomagic.magicdraw.uml.BaseElement)">
<h3>unRegisterBaseElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">unRegisterBaseElement</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRepository()">
<h3>getRepository</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractRepository.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository</a></span> <span class="element-name">getRepository</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code></span></div>
<div class="block">Get repository.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractRefBaseObject.html#getRepository()">getRepository</a></code> in interface <code><a href="AbstractRefBaseObject.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRefBaseObject</a></code></dd>
<dt>Specified by:</dt>
<dd><code>getRepository</code> in interface <code>com.nomagic.uml2.ext.jmi.reflect.RepositoryProvider</code></dd>
<dt>Overrides:</dt>
<dd><code>getRepository</code> in class <code>com.nomagic.uml2.ext.jmi.reflect.AbstractRefBaseObjectImpl</code></dd>
<dt>Returns:</dt>
<dd>repository.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.uml2.ext.jmi.reflect.ElementRegistry</span> <span class="element-name">getProject</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getProject</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProject(com.nomagic.uml2.ext.jmi.reflect.ElementRegistry)">
<h3>setProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProject</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.reflect.ElementRegistry project)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setProject</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refGetEnum(java.lang.String,java.lang.String)">
<h3>refGetEnum</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">javax.jmi.reflect.RefEnum</span> <span class="element-name">refGetEnum</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> enumName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> args)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractRefPackage.html#refGetEnum(java.lang.String,java.lang.String)">AbstractRefPackage</a></code></span></div>
<div class="block">The refGetEnum operation returns the instance of an enumeration (i.e., an
 enumeration literal) whose value is described by the value of literalName .
 Note that the type of enumeration is defined by the meta object that owns
 the metaLiteral object. InvalidCallException is raised if the enumType
 parameter does not designate a valid enumeration. InvalidNameException is
 raised when the enumName does not denote a valid enum name. This
 refGetEnum returns the enumeration object representing the enumeration
 literal. specific analog: none. return type: RefEnum parameters:
 RefObject enumType (or String enumName ) String literalName exceptions:
 JmiException (TypeMismatchException, InvalidCallException,
 InvalidNameException, java.lang.NullPointerException)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>refGetEnum</code> in interface <code>javax.jmi.reflect.RefPackage</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="AbstractRefPackage.html#refGetEnum(java.lang.String,java.lang.String)">refGetEnum</a></code> in class <code><a href="AbstractRefPackage.html" title="class in com.nomagic.uml2.ext.jmi.reflect">AbstractRefPackage</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetamodelProvider()">
<h3>getMetamodelProvider</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.io_software.catools.tas.mof.TASRepository</span> <span class="element-name">getMetamodelProvider</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCounter()">
<h3>getCounter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.util.Counter</span> <span class="element-name">getCounter</span>()</div>
<div class="block">Standalone repositories (those, having no Project object)
 can have a separate counter assigned to them.</div>
</section>
</li>
<li>
<section class="detail" id="setCounter(com.nomagic.util.Counter)">
<h3>setCounter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCounter</span><wbr/><span class="parameters">(com.nomagic.util.Counter count)</span></div>
<div class="block">Standalone repositories (those, having no Project object)
 can have a separate counter assigned to them.</div>
</section>
</li>
<li>
<section class="detail" id="canSetID()">
<h3>canSetID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canSetID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCanSetID(boolean)">
<h3>setCanSetID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCanSetID</span><wbr/><span class="parameters">(boolean canSetID)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canSetID</code> - The canSetID to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValuesTable()">
<h3>getValuesTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.uml2.impl.ValuesTable</span> <span class="element-name">getValuesTable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="invokeAfterTransaction(java.lang.Runnable)">
<h3>invokeAfterTransaction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">invokeAfterTransaction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</span></div>
<div class="block">If at the current moment firing cached events, running runnable after these events are fired. Running now in other case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a> to run.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRawMode()">
<h3>isRawMode</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRawMode</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used</div>
</div>
</section>
</li>
<li>
<section class="detail" id="setRawMode(boolean)">
<h3>setRawMode</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRawMode</span><wbr/><span class="parameters">(boolean rawMode)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">not used</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getTransactionManager()">
<h3>getTransactionManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../transaction/TransactionManager.html" title="interface in com.nomagic.uml2.transaction">TransactionManager</a></span> <span class="element-name">getTransactionManager</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addCandidateForDispose(javax.jmi.reflect.RefObject)">
<h3>addCandidateForDispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCandidateForDispose</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject object)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeCandidateForDispose(javax.jmi.reflect.RefObject)">
<h3>removeCandidateForDispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCandidateForDispose</span><wbr/><span class="parameters">(javax.jmi.reflect.RefObject object)</span></div>
</section>
</li>
<li>
<section class="detail" id="addCandidateElementForDispose(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>addCandidateElementForDispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCandidateElementForDispose</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>addCandidateElementForDispose</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCandidateElementForDispose(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>removeCandidateElementForDispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCandidateElementForDispose</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>removeCandidateElementForDispose</code> in interface <code>com.dassault_systemes.modeler.foundation.model.ModelElementRepository&lt;com.nomagic.uml2.ext.jmi.reflect.ElementRegistry,<wbr/>javax.jmi.reflect.RefObject,<wbr/><a href="../EventSupport.html" title="class in com.nomagic.uml2.ext.jmi">EventSupport</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCandidatesForDispose()">
<h3>getCandidatesForDispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;javax.jmi.reflect.RefObject&gt;</span> <span class="element-name">getCandidatesForDispose</span>()</div>
</section>
</li>
<li>
<section class="detail" id="clearCandidatesForDispose()">
<h3>clearCandidatesForDispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCandidatesForDispose</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addCandidatesForDisposeListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.CandidatesForDisposeListener)">
<h3>addCandidatesForDisposeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCandidatesForDisposeListener</span><wbr/><span class="parameters">(<a href="AbstractRepository.CandidatesForDisposeListener.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.CandidatesForDisposeListener</a> listener)</span></div>
<div class="block">Adds a <a href="AbstractRepository.CandidatesForDisposeListener.html" title="interface in com.nomagic.uml2.ext.jmi.reflect"><code>AbstractRepository.CandidatesForDisposeListener</code></a> to get notifications about</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCandidatesForDisposeListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.CandidatesForDisposeListener)">
<h3>removeCandidatesForDisposeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCandidatesForDisposeListener</span><wbr/><span class="parameters">(<a href="AbstractRepository.CandidatesForDisposeListener.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.CandidatesForDisposeListener</a> listener)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCalculator(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculators)">
<h3>getCalculator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractRepository.Calculator.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculator</a></span> <span class="element-name">getCalculator</span><wbr/><span class="parameters">(<a href="AbstractRepository.Calculators.html" title="enum class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculators</a> calculatorName)</span></div>
</section>
</li>
<li>
<section class="detail" id="addCalculator(com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculators,com.nomagic.uml2.ext.jmi.reflect.AbstractRepository.Calculator)">
<h3>addCalculator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="AbstractRepository.Calculator.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculator</a></span> <span class="element-name">addCalculator</span><wbr/><span class="parameters">(<a href="AbstractRepository.Calculators.html" title="enum class in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculators</a> id,
 <a href="AbstractRepository.Calculator.html" title="interface in com.nomagic.uml2.ext.jmi.reflect">AbstractRepository.Calculator</a> calculator)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - calculator identifier.</dd>
<dd><code>calculator</code> - value calculator.</dd>
<dt>Returns:</dt>
<dd>calculator which was registered by same id.</dd>
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
