# JAVA OPENAPI: ValueSpecificationHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/helpers/ValueSpecificationHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/ValueSpecificationHelper.html`
- source_sha256: `60cca9b2cbc7c15b48a05ada87027464075b5356dd3901d72c07ec882cf4c517`
- captured_utc: `2026-07-14T16:56:16.439693+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class ValueSpecificationHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.uml2.ext.jmi.helpers.CoreHelper](CoreHelper.html)
com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper

Direct Known Subclasses:
`[ClassifierHelper](ClassifierHelper.html)`

@OpenApiAllpublic classValueSpecificationHelper
extends [CoreHelper](CoreHelper.html)

An utility class to work with ValueSpecifications

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ValueSpecificationHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[cloneValueSpecification](#cloneValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 [Element](../../magicdraw/classes/mdkernel/Element.html) newOwner)`
Clones value specification
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createValueSpecification](#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean,java.util.Collection))([Project](../../../../magicdraw/core/Project.html) project,
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean checkNullValue,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)`
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createValueSpecification](#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,java.util.Collection))([Project](../../../../magicdraw/core/Project.html) project,
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)`
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createValueSpecification](#createValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection))([Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../../impl/ElementsFactory.html) elementsFactory,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)`
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createValueSpecification](#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> valueSpecificationClass,
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../../impl/ElementsFactory.html) factory,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)`
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[createValueSpecification](#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> valueSpecificationClass,
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../../impl/ElementsFactory.html) factory,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse,
 boolean ignoreValuesOfReuse)`
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)>`
`[getValueSpecificationClass](#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Type](../../magicdraw/classes/mdkernel/Type.html) valueType)`
Return a meta type of ValueSpecification which should be used to store values of given type
`static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)>`
`[getValueSpecificationClass](#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object))([Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Return a meta type of ValueSpecification which should be used to store values of given type or value.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValueSpecificationValue](#getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification)`
Return value of given ValueSpecification
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValueString](#getValueString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification)`
Return string representation of given ValueSpecification
`static boolean`
`[isValueSpecificationClassElementValue](#isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Type](../../magicdraw/classes/mdkernel/Type.html) valueType)`

`static void`
`[setValueDisposeIfNeeded](#setValueDisposeIfNeeded(java.util.function.Supplier,java.util.function.Consumer,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> oldValueSupplier,
 [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> newValueConsumer,
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) newValue)`
Set value specification as a new value.
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[setValueSpecificationValue](#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object))([Project](../../../../magicdraw/core/Project.html) project,
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Sets value to value specification, creates value specification if necessary.
`static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)`
`[setValueSpecificationValue](#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean))([Project](../../../../magicdraw/core/Project.html) project,
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean checkNullValue)`
Sets value to value specification, creates value specification if necessary.
`static void`
`[setValueSpecificationValue](#setValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.lang.Object))([ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Set a value of value specification
Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.[CoreHelper](CoreHelper.html)
`[areElementsEditable](CoreHelper.html#areElementsEditable(java.util.Collection)), [canAddChild](CoreHelper.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean)), [canAssignName](CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean)), [canMoveChildInto](CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [canMoveChildInto](CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [collectRelationships](CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [collectRelationships](CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean)), [collectRelationshipsByType](CoreHelper.html#collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)), [collectRelationshipsIncludeIndirect](CoreHelper.html#collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [dispose](CoreHelper.html#dispose(java.util.Collection)), [findAcceptableParentFor](CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [findAcceptableParentFor](CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [findOwnerOfStrictType](CoreHelper.html#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfStrictTypeIncludingItself](CoreHelper.html#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfType](CoreHelper.html#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findOwnerOfTypeIncludingItself](CoreHelper.html#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)), [findParent](CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [findParent](CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getAdditionalElementsIterator](CoreHelper.html#getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getClientElement](CoreHelper.html#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getComment](CoreHelper.html#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getCommentElement](CoreHelper.html#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getCommentElementOrCreate](CoreHelper.html#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getDependentClients](CoreHelper.html#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)), [getDependentSuppliers](CoreHelper.html#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)), [getFirstMemberEnd](CoreHelper.html#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [getMultiplicity](CoreHelper.html#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [getName](CoreHelper.html#getName(com.nomagic.magicdraw.uml.BaseElement)), [getOppositeEnd](CoreHelper.html#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getOwnedElementsIncludingAdditional](CoreHelper.html#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getSecondMemberEnd](CoreHelper.html#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)), [getSupplierElement](CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getSupplierElement](CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getSupplierElements](CoreHelper.html#getSupplierElements(java.util.Collection)), [hasParentIn](CoreHelper.html#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [isChildOf](CoreHelper.html#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isDocumentationComment](CoreHelper.html#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)), [isMultiplicityMany](CoreHelper.html#isMultiplicityMany(int)), [isParentOf](CoreHelper.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)), [isParentOf](CoreHelper.html#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isRelationship](CoreHelper.html#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isRelationshipAlwaysInClient](CoreHelper.html#isRelationshipAlwaysInClient(java.lang.Class)), [parseMultiplicityString](CoreHelper.html#parseMultiplicityString(java.lang.String)), [setClientElement](CoreHelper.html#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setComment](CoreHelper.html#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [setCommentElement](CoreHelper.html#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)), [setConstraintText](CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean)), [setConstraintText](CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean)), [setMultiplicity](CoreHelper.html#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [setMultiplicity](CoreHelper.html#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [setSupplierElement](CoreHelper.html#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ValueSpecificationHelper
public ValueSpecificationHelper()
 ============ METHOD DETAIL ========== 
Method Details
createValueSpecification
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) createValueSpecification([Project](../../../../magicdraw/core/Project.html) project,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
Parameters:
`project` - project
`valueType` - type defining the value specification
`value` - value value of ValueSpecification
`reuse` - a collection of possible value specifications to reuse
Returns:
specification
createValueSpecification
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) createValueSpecification([Project](../../../../magicdraw/core/Project.html) project,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean checkNullValue,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
Parameters:
`project` - project
`valueType` - type defining the value specification
`value` - value value of ValueSpecification
`checkNullValue` - if true and value is null, null is returned
`reuse` - a collection of possible value specifications to reuse
Returns:
specification
createValueSpecification
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) createValueSpecification(@CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../../impl/ElementsFactory.html) elementsFactory,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
Parameters:
`valueType` - type defining the value specification
`value` - value value of ValueSpecification
`elementsFactory` - factory
`reuse` - a collection of possible value specifications to reuse
Returns:
specification
createValueSpecification
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) createValueSpecification(@CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> valueSpecificationClass,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../../impl/ElementsFactory.html) factory,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse)
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
Parameters:
`valueSpecificationClass` - meta type of value specification
`value` - value value of ValueSpecification
`factory` - factory
`reuse` - a collection of possible value specifications to reuse
Returns:
specification
createValueSpecification
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) createValueSpecification(@CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> valueSpecificationClass,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [ElementsFactory](../../../impl/ElementsFactory.html) factory,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> reuse,
 boolean ignoreValuesOfReuse)
Create a new value specification for a given value or returns a suitable from the given specifications to reuse.
Parameters:
`valueSpecificationClass` - meta type of value specification
`value` - value value of ValueSpecification
`factory` - factory
`reuse` - a collection of possible value specifications to reuse
`ignoreValuesOfReuse` - if false, checks is value if reuse candidate is suitable, not only the meta type. If true, checks just a metatype and overwrites the value
Returns:
specification
setValueSpecificationValue
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) setValueSpecificationValue([Project](../../../../magicdraw/core/Project.html) project,
 @CheckForNull
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Sets value to value specification, creates value specification if necessary.
 If valueSpecification is passed, set a value to it.
 If value is null, passed value specification is disposed and null is returned.
Parameters:
`project` - project
`valueSpecification` - value specification
`valueType` - value type
`value` - value
Returns:
passed value specification or created a new one. If value is null, null can be returned.
setValueSpecificationValue
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) setValueSpecificationValue([Project](../../../../magicdraw/core/Project.html) project,
 @CheckForNull
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 @CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 boolean checkNullValue)
Sets value to value specification, creates value specification if necessary.
 If valueSpecification is passed, set a value to it.
 If value is null and checkNullValue is true, passed value specification is disposed and null is returned.
Parameters:
`project` - project
`valueSpecification` - value specification
`valueType` - value type
`value` - value
`checkNullValue` - check null value
Returns:
passed value specification or created a new one. If value is null, null can be returned.
setValueSpecificationValue
public static void setValueSpecificationValue([ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Set a value of value specification
Parameters:
`valueSpecification` - value specification
`value` - value
getValueSpecificationClass
public static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> getValueSpecificationClass(@CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Return a meta type of ValueSpecification which should be used to store values of given type or value. If valueType is null, value is used to define a meta type of value specification.
Parameters:
`valueType` - value type
Returns:
meta type of value specification
isValueSpecificationClassElementValue
public static boolean isValueSpecificationClassElementValue(@CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType)
Parameters:
`valueType` - value type
Returns:
true if ValueSpecification for given type should be ElementValue
getValueSpecificationClass
public static [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> getValueSpecificationClass(@CheckForNull
 [Type](../../magicdraw/classes/mdkernel/Type.html) valueType)
Return a meta type of ValueSpecification which should be used to store values of given type
Parameters:
`valueType` - value type
Returns:
meta type of value specification
cloneValueSpecification
@CheckForNullpublic static [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) cloneValueSpecification([ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 @CheckForNull
 [Element](../../magicdraw/classes/mdkernel/Element.html) newOwner)
Clones value specification
Parameters:
`valueSpecification` - value specification to clone
`newOwner` - owner of new value specification. It will not be set as owner, but it should be passed for correct cloning
Returns:
cloned value specification
getValueSpecificationValue
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValueSpecificationValue(@CheckForNull
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification)
Return value of given ValueSpecification
Parameters:
`valueSpecification` - value specification
Returns:
value
getValueString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValueString(@CheckForNull
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification)
Return string representation of given ValueSpecification
Parameters:
`valueSpecification` - value specification
Returns:
string representation of given value specification
setValueDisposeIfNeeded
public static void setValueDisposeIfNeeded([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> oldValueSupplier,
 [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html)> newValueConsumer,
 @CheckForNull
 [ValueSpecification](../../magicdraw/classes/mdkernel/ValueSpecification.html) newValue)
Set value specification as a new value. If old value is not the same as new value, old ValueSpecification is disposed.
Parameters:
`oldValueSupplier` - the supplier of olf value
`newValueConsumer` - the consumer of new value
`newValue` - new value

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class ValueSpecificationHelper">Class ValueSpecificationHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="CoreHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">com.nomagic.uml2.ext.jmi.helpers.CoreHelper</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.ValueSpecificationHelper</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ClassifierHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">ClassifierHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ValueSpecificationHelper</span>
<span class="extends-implements">extends <a href="CoreHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">CoreHelper</a></span></div>
<div class="block">An utility class to work with ValueSpecifications</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ValueSpecificationHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#cloneValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">cloneValueSpecification</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> newOwner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Clones value specification</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean,java.util.Collection)">createValueSpecification</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean checkNullValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,java.util.Collection)">createValueSpecification</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">createValueSpecification</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> elementsFactory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">createValueSpecification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; valueSpecificationClass,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean)">createValueSpecification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; valueSpecificationClass,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse,
 boolean ignoreValuesOfReuse)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">getValueSpecificationClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a meta type of ValueSpecification which should be used to store values of given type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">getValueSpecificationClass</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return a meta type of ValueSpecification which should be used to store values of given type or value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">getValueSpecificationValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return value of given ValueSpecification</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">getValueString</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return string representation of given ValueSpecification</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">isValueSpecificationClassElementValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValueDisposeIfNeeded(java.util.function.Supplier,java.util.function.Consumer,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setValueDisposeIfNeeded</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; oldValueSupplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; newValueConsumer,
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set value specification as a new value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">setValueSpecificationValue</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets value to value specification, creates value specification if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean)">setValueSpecificationValue</a><wbr/>(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean checkNullValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets value to value specification, creates value specification if necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.lang.Object)">setValueSpecificationValue</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set a value of value specification</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.helpers.CoreHelper">Methods inherited from class com.nomagic.uml2.ext.jmi.helpers.<a href="CoreHelper.html" title="class in com.nomagic.uml2.ext.jmi.helpers">CoreHelper</a></h3>
<code><a href="CoreHelper.html#areElementsEditable(java.util.Collection)">areElementsEditable</a>, <a href="CoreHelper.html#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean)">canAssignName</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean)">canAssignName</a>, <a href="CoreHelper.html#canAssignName(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,boolean,boolean,boolean)">canAssignName</a>, <a href="CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canMoveChildInto</a>, <a href="CoreHelper.html#canMoveChildInto(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">canMoveChildInto</a>, <a href="CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationships</a>, <a href="CoreHelper.html#collectRelationships(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Predicate,boolean)">collectRelationships</a>, <a href="CoreHelper.html#collectRelationshipsByType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">collectRelationshipsByType</a>, <a href="CoreHelper.html#collectRelationshipsIncludeIndirect(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">collectRelationshipsIncludeIndirect</a>, <a href="CoreHelper.html#dispose(java.util.Collection)">dispose</a>, <a href="CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findAcceptableParentFor</a>, <a href="CoreHelper.html#findAcceptableParentFor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findAcceptableParentFor</a>, <a href="CoreHelper.html#findOwnerOfStrictType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictType</a>, <a href="CoreHelper.html#findOwnerOfStrictTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfStrictTypeIncludingItself</a>, <a href="CoreHelper.html#findOwnerOfType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfType</a>, <a href="CoreHelper.html#findOwnerOfTypeIncludingItself(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">findOwnerOfTypeIncludingItself</a>, <a href="CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findParent</a>, <a href="CoreHelper.html#findParent(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findParent</a>, <a href="CoreHelper.html#getAdditionalElementsIterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAdditionalElementsIterator</a>, <a href="CoreHelper.html#getClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getClientElement</a>, <a href="CoreHelper.html#getComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getComment</a>, <a href="CoreHelper.html#getCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElement</a>, <a href="CoreHelper.html#getCommentElementOrCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getCommentElementOrCreate</a>, <a href="CoreHelper.html#getDependentClients(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentClients</a>, <a href="CoreHelper.html#getDependentSuppliers(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement,java.lang.Class)">getDependentSuppliers</a>, <a href="CoreHelper.html#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getFirstMemberEnd</a>, <a href="CoreHelper.html#getMultiplicity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">getMultiplicity</a>, <a href="CoreHelper.html#getName(com.nomagic.magicdraw.uml.BaseElement)">getName</a>, <a href="CoreHelper.html#getOppositeEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getOppositeEnd</a>, <a href="CoreHelper.html#getOwnedElementsIncludingAdditional(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getOwnedElementsIncludingAdditional</a>, <a href="CoreHelper.html#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getSecondMemberEnd</a>, <a href="CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSupplierElement</a>, <a href="CoreHelper.html#getSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getSupplierElement</a>, <a href="CoreHelper.html#getSupplierElements(java.util.Collection)">getSupplierElements</a>, <a href="CoreHelper.html#hasParentIn(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">hasParentIn</a>, <a href="CoreHelper.html#isChildOf(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isChildOf</a>, <a href="CoreHelper.html#isDocumentationComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">isDocumentationComment</a>, <a href="CoreHelper.html#isMultiplicityMany(int)">isMultiplicityMany</a>, <a href="CoreHelper.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="CoreHelper.html#isParentOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isParentOf</a>, <a href="CoreHelper.html#isRelationship(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRelationship</a>, <a href="CoreHelper.html#isRelationshipAlwaysInClient(java.lang.Class)">isRelationshipAlwaysInClient</a>, <a href="CoreHelper.html#parseMultiplicityString(java.lang.String)">parseMultiplicityString</a>, <a href="CoreHelper.html#setClientElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setClientElement</a>, <a href="CoreHelper.html#setComment(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setComment</a>, <a href="CoreHelper.html#setCommentElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment)">setCommentElement</a>, <a href="CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean)">setConstraintText</a>, <a href="CoreHelper.html#setConstraintText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.lang.String,boolean,boolean,boolean)">setConstraintText</a>, <a href="CoreHelper.html#setMultiplicity(int,int,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a>, <a href="CoreHelper.html#setMultiplicity(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setMultiplicity</a>, <a href="CoreHelper.html#setSupplierElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSupplierElement</a></code></div>
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
<h3>ValueSpecificationHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValueSpecificationHelper</span>()</div>
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
<section class="detail" id="createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,java.util.Collection)">
<h3>createValueSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createValueSpecification</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</span></div>
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>valueType</code> - type defining the value specification</dd>
<dd><code>value</code> - value value of ValueSpecification</dd>
<dd><code>reuse</code> - a collection of possible value specifications to reuse</dd>
<dt>Returns:</dt>
<dd>specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecification(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean,java.util.Collection)">
<h3>createValueSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createValueSpecification</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean checkNullValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</span></div>
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>valueType</code> - type defining the value specification</dd>
<dd><code>value</code> - value value of ValueSpecification</dd>
<dd><code>checkNullValue</code> - if true and value is null, null is returned</dd>
<dd><code>reuse</code> - a collection of possible value specifications to reuse</dd>
<dt>Returns:</dt>
<dd>specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">
<h3>createValueSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createValueSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> elementsFactory,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</span></div>
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueType</code> - type defining the value specification</dd>
<dd><code>value</code> - value value of ValueSpecification</dd>
<dd><code>elementsFactory</code> - factory</dd>
<dd><code>reuse</code> - a collection of possible value specifications to reuse</dd>
<dt>Returns:</dt>
<dd>specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection)">
<h3>createValueSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createValueSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; valueSpecificationClass,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse)</span></div>
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecificationClass</code> - meta type of value specification</dd>
<dd><code>value</code> - value value of ValueSpecification</dd>
<dd><code>factory</code> - factory</dd>
<dd><code>reuse</code> - a collection of possible value specifications to reuse</dd>
<dt>Returns:</dt>
<dd>specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecification(java.lang.Class,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,com.nomagic.uml2.impl.ElementsFactory,java.util.Collection,boolean)">
<h3>createValueSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">createValueSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; valueSpecificationClass,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../../impl/ElementsFactory.html" title="class in com.nomagic.uml2.impl">ElementsFactory</a> factory,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; reuse,
 boolean ignoreValuesOfReuse)</span></div>
<div class="block">Create a new value specification for a given value or returns a suitable from the given specifications to reuse.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecificationClass</code> - meta type of value specification</dd>
<dd><code>value</code> - value value of ValueSpecification</dd>
<dd><code>factory</code> - factory</dd>
<dd><code>reuse</code> - a collection of possible value specifications to reuse</dd>
<dd><code>ignoreValuesOfReuse</code> - if false, checks is value if reuse candidate is suitable, not only the meta type. If true, checks just a metatype and overwrites the value</dd>
<dt>Returns:</dt>
<dd>specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">
<h3>setValueSpecificationValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">setValueSpecificationValue</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets value to value specification, creates value specification if necessary.
 If valueSpecification is passed, set a value to it.
 If value is null, passed value specification is disposed and null is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>valueSpecification</code> - value specification</dd>
<dd><code>valueType</code> - value type</dd>
<dd><code>value</code> - value</dd>
<dt>Returns:</dt>
<dd>passed value specification or created a new one. If value is null, null can be returned.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValueSpecificationValue(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object,boolean)">
<h3>setValueSpecificationValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">setValueSpecificationValue</span><wbr/><span class="parameters">(<a href="../../../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 boolean checkNullValue)</span></div>
<div class="block">Sets value to value specification, creates value specification if necessary.
 If valueSpecification is passed, set a value to it.
 If value is null and checkNullValue is true, passed value specification is disposed and null is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>valueSpecification</code> - value specification</dd>
<dd><code>valueType</code> - value type</dd>
<dd><code>value</code> - value</dd>
<dd><code>checkNullValue</code> - check null value</dd>
<dt>Returns:</dt>
<dd>passed value specification or created a new one. If value is null, null can be returned.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.lang.Object)">
<h3>setValueSpecificationValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setValueSpecificationValue</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Set a value of value specification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecification</code> - value specification</dd>
<dd><code>value</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,java.lang.Object)">
<h3>getValueSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</span> <span class="element-name">getValueSpecificationClass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Return a meta type of ValueSpecification which should be used to store values of given type or value. If valueType is null, value is used to define a meta type of value specification.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueType</code> - value type</dd>
<dt>Returns:</dt>
<dd>meta type of value specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValueSpecificationClassElementValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>isValueSpecificationClassElementValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isValueSpecificationClassElementValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueType</code> - value type</dd>
<dt>Returns:</dt>
<dd>true if ValueSpecification for given type should be ElementValue</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueSpecificationClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>getValueSpecificationClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</span> <span class="element-name">getValueSpecificationClass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> valueType)</span></div>
<div class="block">Return a meta type of ValueSpecification which should be used to store values of given type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueType</code> - value type</dd>
<dt>Returns:</dt>
<dd>meta type of value specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cloneValueSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>cloneValueSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">cloneValueSpecification</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> newOwner)</span></div>
<div class="block">Clones value specification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecification</code> - value specification to clone</dd>
<dd><code>newOwner</code> - owner of new value specification. It will not be set as owner, but it should be passed for correct cloning</dd>
<dt>Returns:</dt>
<dd>cloned value specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueSpecificationValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>getValueSpecificationValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValueSpecificationValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification)</span></div>
<div class="block">Return value of given ValueSpecification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecification</code> - value specification</dd>
<dt>Returns:</dt>
<dd>value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueString(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>getValueString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValueString</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification)</span></div>
<div class="block">Return string representation of given ValueSpecification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecification</code> - value specification</dd>
<dt>Returns:</dt>
<dd>string representation of given value specification</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValueDisposeIfNeeded(java.util.function.Supplier,java.util.function.Consumer,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setValueDisposeIfNeeded</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setValueDisposeIfNeeded</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; oldValueSupplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt; newValueConsumer,
 @CheckForNull
 <a href="../../magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> newValue)</span></div>
<div class="block">Set value specification as a new value. If old value is not the same as new value, old ValueSpecification is disposed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldValueSupplier</code> - the supplier of olf value</dd>
<dd><code>newValueConsumer</code> - the consumer of new value</dd>
<dd><code>newValue</code> - new value</dd>
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
