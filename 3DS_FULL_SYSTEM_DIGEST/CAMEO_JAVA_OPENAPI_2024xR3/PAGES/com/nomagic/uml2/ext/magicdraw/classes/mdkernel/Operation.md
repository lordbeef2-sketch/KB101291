# JAVA OPENAPI: Operation (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Operation.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Operation.html`
- source_sha256: `3d67a22b534bfc759ffc774f03d7a78d9fee4e2c244489f864772e0850ae34ab`
- captured_utc: `2026-07-14T16:56:23.076768+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Operation

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[BehavioralFeature](BehavioralFeature.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Feature](Feature.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `[Namespace](Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `[RedefinableElement](RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)`

public interfaceOperationextends [BehavioralFeature](BehavioralFeature.html), [ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html), [TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)

begin-user-doc 
 A representation of the model object '***Operation***'.
 end-user-doc 
begin-model-doc 
 An Operation is a BehavioralFeature of a Classifier that specifies the name, type, parameters, and constraints for invoking an associated Behavior. An Operation may
 invoke both the execution of method behaviors as well as other behavioral responses. Operation specializes TemplateableElement in order to support specification of
 template operations and bound operations. Operation specializes ParameterableElement to specify that an operation can be exposed as a formal template parameter, and
 provided as an actual parameter in a binding of a template.
 end-model-doc 
The following features are supported:
 [`*Type*`](#getType())
[`*Datatype*`](#getDatatype())
[`*Interface*`](#getInterface())
[`*artifact Of Owned Operation*`](#get_artifactOfOwnedOperation())
[`*Body Condition*`](#getBodyCondition())
[`*UML Class*`](#getUMLClass())
[`*Ordered*`](#isOrdered())
[`*Query*`](#isQuery())
[`*Unique*`](#isUnique())
[`*Lower*`](#getLower())
[`*Postcondition*`](#getPostcondition())
[`*Precondition*`](#getPrecondition())
[`*Redefined Operation*`](#getRedefinedOperation())
[`*operation Of Redefined Operation*`](#get_operationOfRedefinedOperation())
[`*Upper*`](#getUpper())
[`*call Operation Action Of Operation*`](#get_callOperationActionOfOperation())
[`*call Event Of Operation*`](#get_callEventOfOperation())

See Also:
[`UMLPackage.getOperation()`](../../metadata/UMLPackage.html#getOperation())
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Artifact](../../deployments/mdartifacts/Artifact.html)`
`[get_artifactOfOwnedOperation](#get_artifactOfOwnedOperation())()`
Returns the value of the '***artifact Of Owned Operation***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[CallEvent](../../commonbehaviors/mdcommunications/CallEvent.html)>`
`[get_callEventOfOperation](#get_callEventOfOperation())()`
Returns the value of the '***call Event Of Operation***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[CallOperationAction](../../actions/mdbasicactions/CallOperationAction.html)>`
`[get_callOperationActionOfOperation](#get_callOperationActionOfOperation())()`
Returns the value of the '***call Operation Action Of Operation***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](Operation.html)>`
`[get_operationOfRedefinedOperation](#get_operationOfRedefinedOperation())()`
Returns the value of the '***operation Of Redefined Operation***' reference list.
`[Constraint](Constraint.html)`
`[getBodyCondition](#getBodyCondition())()`
Returns the value of the '***Body Condition***' reference.
`[DataType](DataType.html)`
`[getDatatype](#getDatatype())()`
Returns the value of the '***Datatype***' container reference.
`[Interface](../mdinterfaces/Interface.html)`
`[getInterface](#getInterface())()`
Returns the value of the '***Interface***' container reference.
`int`
`[getLower](#getLower())()`
Returns the value of the '***Lower***' attribute.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Parameter](Parameter.html)>`
`[getOwnedParameter](#getOwnedParameter())()`
Returns the value of the '***Owned Parameter***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](Constraint.html)>`
`[getPostcondition](#getPostcondition())()`
Returns the value of the '***Postcondition***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](Constraint.html)>`
`[getPrecondition](#getPrecondition())()`
Returns the value of the '***Precondition***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Type](Type.html)>`
`[getRaisedException](#getRaisedException())()`
Returns the value of the '***Raised Exception***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](Operation.html)>`
`[getRedefinedOperation](#getRedefinedOperation())()`
Returns the value of the '***Redefined Operation***' reference list.
`[OperationTemplateParameter](../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html)`
`[getTemplateParameter](#getTemplateParameter())()`
Returns the value of the '***Template Parameter***' reference.
`[Type](Type.html)`
`[getType](#getType())()`
Returns the value of the '***Type***' reference.
`[Class](Class.html)`
`[getUMLClass](#getUMLClass())()`
Returns the value of the '***UML Class***' container reference.
`int`
`[getUpper](#getUpper())()`
Returns the value of the '***Upper***' attribute.
`boolean`
`[has_callEventOfOperation](#has_callEventOfOperation())()`

`boolean`
`[has_callOperationActionOfOperation](#has_callOperationActionOfOperation())()`

`boolean`
`[has_operationOfRedefinedOperation](#has_operationOfRedefinedOperation())()`

`boolean`
`[hasPostcondition](#hasPostcondition())()`

`boolean`
`[hasPrecondition](#hasPrecondition())()`

`boolean`
`[hasRedefinedOperation](#hasRedefinedOperation())()`

`boolean`
`[isOrdered](#isOrdered())()`
Returns the value of the '***Ordered***' attribute.
`boolean`
`[isQuery](#isQuery())()`
Returns the value of the '***Query***' attribute.
`boolean`
`[isUnique](#isUnique())()`
Returns the value of the '***Unique***' attribute.
`void`
`[set_artifactOfOwnedOperation](#set_artifactOfOwnedOperation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact))([Artifact](../../deployments/mdartifacts/Artifact.html) value)`
Sets the value of the '[`*artifact Of Owned Operation*`](#get_artifactOfOwnedOperation())'
 container reference.
`void`
`[setBodyCondition](#setBodyCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](Constraint.html) value)`
Sets the value of the '[`*Body Condition*`](#getBodyCondition())' reference.
`void`
`[setDatatype](#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType))([DataType](DataType.html) value)`
Sets the value of the '[`*Datatype*`](#getDatatype())' container reference.
`void`
`[setInterface](#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))([Interface](../mdinterfaces/Interface.html) value)`
Sets the value of the '[`*Interface*`](#getInterface())' container reference.
`void`
`[setQuery](#setQuery(boolean))(boolean value)`
Sets the value of the '[`*Query*`](#isQuery())' attribute.
`void`
`[setTemplateParameter](#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter))([OperationTemplateParameter](../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) value)`
Sets the value of the '[`*Template Parameter*`](#getTemplateParameter())' reference.
`void`
`[setUMLClass](#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))([Class](Class.html) value)`
Sets the value of the '[`*UML Class*`](#getUMLClass())' container reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[BehavioralFeature](BehavioralFeature.html)
`[getConcurrency](BehavioralFeature.html#getConcurrency()), [getMethod](BehavioralFeature.html#getMethod()), [getOwnedParameterSet](BehavioralFeature.html#getOwnedParameterSet()), [hasMethod](BehavioralFeature.html#hasMethod()), [hasOwnedParameter](BehavioralFeature.html#hasOwnedParameter()), [hasOwnedParameterSet](BehavioralFeature.html#hasOwnedParameterSet()), [hasRaisedException](BehavioralFeature.html#hasRaisedException()), [isAbstract](BehavioralFeature.html#isAbstract()), [setAbstract](BehavioralFeature.html#setAbstract(boolean)), [setConcurrency](BehavioralFeature.html#setConcurrency(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKind))`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Feature](Feature.html)
`[getFeaturingClassifier](Feature.html#getFeaturingClassifier()), [isStatic](Feature.html#isStatic()), [setFeaturingClassifier](Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)), [setStatic](Feature.html#setStatic(boolean))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](NamedElement.html#getClientDependency()), [getName](NamedElement.html#getName()), [getNameExpression](NamedElement.html#getNameExpression()), [getNamespace](NamedElement.html#getNamespace()), [getQualifiedName](NamedElement.html#getQualifiedName()), [getSupplierDependency](NamedElement.html#getSupplierDependency()), [getVisibility](NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](NamedElement.html#hasClientDependency()), [hasSupplierDependency](NamedElement.html#hasSupplierDependency()), [setName](NamedElement.html#setName(java.lang.String)), [setNameExpression](NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](Namespace.html)
`[getElementImport](Namespace.html#getElementImport()), [getImportedMember](Namespace.html#getImportedMember()), [getMember](Namespace.html#getMember()), [getOwnedDiagram](Namespace.html#getOwnedDiagram()), [getOwnedMember](Namespace.html#getOwnedMember()), [getOwnedRule](Namespace.html#getOwnedRule()), [getPackageImport](Namespace.html#getPackageImport()), [hasElementImport](Namespace.html#hasElementImport()), [hasImportedMember](Namespace.html#hasImportedMember()), [hasMember](Namespace.html#hasMember()), [hasOwnedDiagram](Namespace.html#hasOwnedDiagram()), [hasOwnedMember](Namespace.html#hasOwnedMember()), [hasOwnedRule](Namespace.html#hasOwnedRule()), [hasPackageImport](Namespace.html#hasPackageImport())`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](RedefinableElement.html#hasRedefinitionContext()), [isLeaf](RedefinableElement.html#isLeaf()), [setLeaf](RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[TemplateableElement](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html)
`[getOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getOwnedTemplateSignature()), [getTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()), [hasTemplateBinding](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()), [setOwnedTemplateSignature](../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))`

============ METHOD DETAIL ========== 
Method Details
getInterface
@CheckForNull[Interface](../mdinterfaces/Interface.html) getInterface()
Returns the value of the '***Interface***' container reference.
 It is bidirectional and its opposite is '[`*Owned Operation*`](../mdinterfaces/Interface.html#getOwnedOperation())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Interface that owns this Operation, if any.
 end-model-doc
Returns:
the value of the '*Interface*' container reference.
See Also:
[`setInterface(Interface)`](#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface))
[`UMLPackage.getOperation_Interface()`](../../metadata/UMLPackage.html#getOperation_Interface())
[`Interface.getOwnedOperation()`](../mdinterfaces/Interface.html#getOwnedOperation())
Model:
opposite="ownedOperation" transient="false" ordered="false"
Generated:
setInterface
void setInterface(@CheckForNull
 [Interface](../mdinterfaces/Interface.html) value)
Sets the value of the '[`*Interface*`](#getInterface())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Interface*' container reference.
See Also:
[`getInterface()`](#getInterface())
Generated:
isOrdered
boolean isOrdered()
Returns the value of the '***Ordered***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies whether the return parameter is ordered or not, if present. This information is derived from the return result for this Operation.
 end-model-doc
Returns:
the value of the '*Ordered*' attribute.
See Also:
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getOperation_Ordered()`
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
isQuery
boolean isQuery()
Returns the value of the '***Query***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies whether an execution of the BehavioralFeature leaves the state of the system unchanged (isQuery=true) or whether side effects may occur (isQuery=false).
 end-model-doc
Returns:
the value of the '*Query*' attribute.
See Also:
[`setQuery(boolean)`](#setQuery(boolean))
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getOperation_Query()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setQuery
void setQuery(boolean value)
Sets the value of the '[`*Query*`](#isQuery())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Query*' attribute.
See Also:
[`isQuery()`](#isQuery())
Generated:
isUnique
boolean isUnique()
Returns the value of the '***Unique***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies whether the return parameter is unique or not, if present. This information is derived from the return result for this Operation.
 end-model-doc
Returns:
the value of the '*Unique*' attribute.
See Also:
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getOperation_Unique()`
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getUMLClass
@CheckForNull[Class](Class.html) getUMLClass()
Returns the value of the '***UML Class***' container reference.
 It is bidirectional and its opposite is '[`*Owned Operation*`](Class.html#getOwnedOperation())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Class that owns this operation, if any.
 end-model-doc
Returns:
the value of the '*UML Class*' container reference.
See Also:
[`setUMLClass(Class)`](#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class))
[`UMLPackage.getOperation_UMLClass()`](../../metadata/UMLPackage.html#getOperation_UMLClass())
[`Class.getOwnedOperation()`](Class.html#getOwnedOperation())
Model:
opposite="ownedOperation" transient="false" ordered="false"
Generated:
setUMLClass
void setUMLClass(@CheckForNull
 [Class](Class.html) value)
Sets the value of the '[`*UML Class*`](#getUMLClass())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*UML Class*' container reference.
See Also:
[`getUMLClass()`](#getUMLClass())
Generated:
get_callEventOfOperation
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[CallEvent](../../commonbehaviors/mdcommunications/CallEvent.html)> get_callEventOfOperation()
Returns the value of the '***call Event Of Operation***' reference list.
 The list contents are of type [`CallEvent`](../../commonbehaviors/mdcommunications/CallEvent.html).
 It is bidirectional and its opposite is '[`*Operation*`](../../commonbehaviors/mdcommunications/CallEvent.html#getOperation())'.
 begin-user-doc 
If the meaning of the '*call Event Of Operation*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*call Event Of Operation*' reference list.
See Also:
[`UMLPackage.getOperation__callEventOfOperation()`](../../metadata/UMLPackage.html#getOperation__callEventOfOperation())
[`CallEvent.getOperation()`](../../commonbehaviors/mdcommunications/CallEvent.html#getOperation())
Model:
opposite="operation" ordered="false"
Generated:
get_callOperationActionOfOperation
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[CallOperationAction](../../actions/mdbasicactions/CallOperationAction.html)> get_callOperationActionOfOperation()
Returns the value of the '***call Operation Action Of Operation***' reference list.
 The list contents are of type [`CallOperationAction`](../../actions/mdbasicactions/CallOperationAction.html).
 It is bidirectional and its opposite is '[`*Operation*`](../../actions/mdbasicactions/CallOperationAction.html#getOperation())'.
 begin-user-doc 
If the meaning of the '*call Operation Action Of Operation*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*call Operation Action Of Operation*' reference list.
See Also:
[`UMLPackage.getOperation__callOperationActionOfOperation()`](../../metadata/UMLPackage.html#getOperation__callOperationActionOfOperation())
[`CallOperationAction.getOperation()`](../../actions/mdbasicactions/CallOperationAction.html#getOperation())
Model:
opposite="operation" ordered="false"
Generated:
getLower
int getLower()
Returns the value of the '***Lower***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the lower multiplicity of the return parameter, if present. This information is derived from the return result for this Operation.
 end-model-doc
Returns:
the value of the '*Lower*' attribute.
See Also:
[`UMLPackage.getOperation_Lower()`](../../metadata/UMLPackage.html#getOperation_Lower())
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Integer" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getUpper
int getUpper()
Returns the value of the '***Upper***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The upper multiplicity of the return parameter, if present. This information is derived from the return result for this Operation.
 end-model-doc
Returns:
the value of the '*Upper*' attribute.
See Also:
[`UMLPackage.getOperation_Upper()`](../../metadata/UMLPackage.html#getOperation_Upper())
Model:
dataType="com.nomagic.uml2.ext.magicdraw.UnlimitedNatural" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getPrecondition
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](Constraint.html)> getPrecondition()
Returns the value of the '***Precondition***' reference list.
 The list contents are of type [`Constraint`](Constraint.html).
 It is bidirectional and its opposite is '[`*Pre Context*`](Constraint.html#getPreContext())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional set of Constraints on the state of the system when the Operation is invoked.
 end-model-doc
Returns:
the value of the '*Precondition*' reference list.
See Also:
[`UMLPackage.getOperation_Precondition()`](../../metadata/UMLPackage.html#getOperation_Precondition())
[`Constraint.getPreContext()`](Constraint.html#getPreContext())
Model:
opposite="preContext" ordered="false"
Generated:
getPostcondition
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](Constraint.html)> getPostcondition()
Returns the value of the '***Postcondition***' reference list.
 The list contents are of type [`Constraint`](Constraint.html).
 It is bidirectional and its opposite is '[`*Post Context*`](Constraint.html#getPostContext())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional set of Constraints specifying the state of the system when the Operation is completed.
 end-model-doc
Returns:
the value of the '*Postcondition*' reference list.
See Also:
[`UMLPackage.getOperation_Postcondition()`](../../metadata/UMLPackage.html#getOperation_Postcondition())
[`Constraint.getPostContext()`](Constraint.html#getPostContext())
Model:
opposite="postContext" ordered="false"
Generated:
getRedefinedOperation
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](Operation.html)> getRedefinedOperation()
Returns the value of the '***Redefined Operation***' reference list.
 The list contents are of type [`Operation`](Operation.html).
 It is bidirectional and its opposite is
 '[`*operation Of Redefined Operation*`](#get_operationOfRedefinedOperation())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Operations that are redefined by this Operation.
 end-model-doc
Returns:
the value of the '*Redefined Operation*' reference list.
See Also:
[`UMLPackage.getOperation_RedefinedOperation()`](../../metadata/UMLPackage.html#getOperation_RedefinedOperation())
[`get_operationOfRedefinedOperation()`](#get_operationOfRedefinedOperation())
Model:
opposite="_operationOfRedefinedOperation" ordered="false"
Generated:
get_operationOfRedefinedOperation
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](Operation.html)> get_operationOfRedefinedOperation()
Returns the value of the '***operation Of Redefined Operation***' reference list.
 The list contents are of type [`Operation`](Operation.html).
 It is bidirectional and its opposite is '[`*Redefined Operation*`](#getRedefinedOperation())'.
 begin-user-doc 
If the meaning of the '*operation Of Redefined Operation*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*operation Of Redefined Operation*' reference list.
See Also:
[`UMLPackage.getOperation__operationOfRedefinedOperation()`](../../metadata/UMLPackage.html#getOperation__operationOfRedefinedOperation())
[`getRedefinedOperation()`](#getRedefinedOperation())
Model:
opposite="redefinedOperation" ordered="false"
Generated:
getDatatype
@CheckForNull[DataType](DataType.html) getDatatype()
Returns the value of the '***Datatype***' container reference.
 It is bidirectional and its opposite is '[`*Owned Operation*`](DataType.html#getOwnedOperation())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The DataType that owns this Operation, if any.
 end-model-doc
Returns:
the value of the '*Datatype*' container reference.
See Also:
[`setDatatype(DataType)`](#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType))
[`UMLPackage.getOperation_Datatype()`](../../metadata/UMLPackage.html#getOperation_Datatype())
[`DataType.getOwnedOperation()`](DataType.html#getOwnedOperation())
Model:
opposite="ownedOperation" transient="false" ordered="false"
Generated:
setDatatype
void setDatatype(@CheckForNull
 [DataType](DataType.html) value)
Sets the value of the '[`*Datatype*`](#getDatatype())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Datatype*' container reference.
See Also:
[`getDatatype()`](#getDatatype())
Generated:
getType
@CheckForNull[Type](Type.html) getType()
Returns the value of the '***Type***' reference.
 It is bidirectional and its opposite is '`*operation Of Type*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The return type of the operation, if present. This information is derived from the return result for this Operation.
 end-model-doc
Returns:
the value of the '*Type*' reference.
See Also:
[`UMLPackage.getOperation_Type()`](../../metadata/UMLPackage.html#getOperation_Type())
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type#get_operationOfType`
Model:
opposite="_operationOfType" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
get_artifactOfOwnedOperation
@CheckForNull[Artifact](../../deployments/mdartifacts/Artifact.html) get_artifactOfOwnedOperation()
Returns the value of the '***artifact Of Owned Operation***' container reference.
 It is bidirectional and its opposite is '[`*Owned Operation*`](../../deployments/mdartifacts/Artifact.html#getOwnedOperation())'.
 begin-user-doc 
If the meaning of the '*artifact Of Owned Operation*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*artifact Of Owned Operation*' container reference.
See Also:
[`set_artifactOfOwnedOperation(Artifact)`](#set_artifactOfOwnedOperation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact))
[`UMLPackage.getOperation__artifactOfOwnedOperation()`](../../metadata/UMLPackage.html#getOperation__artifactOfOwnedOperation())
[`Artifact.getOwnedOperation()`](../../deployments/mdartifacts/Artifact.html#getOwnedOperation())
Model:
opposite="ownedOperation" transient="false" ordered="false"
Generated:
set_artifactOfOwnedOperation
void set_artifactOfOwnedOperation(@CheckForNull
 [Artifact](../../deployments/mdartifacts/Artifact.html) value)
Sets the value of the '[`*artifact Of Owned Operation*`](#get_artifactOfOwnedOperation())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*artifact Of Owned Operation*' container reference.
See Also:
[`get_artifactOfOwnedOperation()`](#get_artifactOfOwnedOperation())
Generated:
getBodyCondition
@CheckForNull[Constraint](Constraint.html) getBodyCondition()
Returns the value of the '***Body Condition***' reference.
 It is bidirectional and its opposite is '[`*Body Context*`](Constraint.html#getBodyContext())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional Constraint on the result values of an invocation of this Operation.
 end-model-doc
Returns:
the value of the '*Body Condition*' reference.
See Also:
[`setBodyCondition(Constraint)`](#setBodyCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))
[`UMLPackage.getOperation_BodyCondition()`](../../metadata/UMLPackage.html#getOperation_BodyCondition())
[`Constraint.getBodyContext()`](Constraint.html#getBodyContext())
Model:
opposite="bodyContext" ordered="false"
Generated:
setBodyCondition
void setBodyCondition(@CheckForNull
 [Constraint](Constraint.html) value)
Sets the value of the '[`*Body Condition*`](#getBodyCondition())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Body Condition*' reference.
See Also:
[`getBodyCondition()`](#getBodyCondition())
Generated:
getOwnedParameter
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Parameter](Parameter.html)> getOwnedParameter()
Returns the value of the '***Owned Parameter***' containment reference list.
 The list contents are of type [`Parameter`](Parameter.html).
 It is bidirectional and its opposite is '[`*Operation*`](Parameter.html#getOperation())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The parameters owned by this Operation.
 end-model-doc
Specified by:
`[getOwnedParameter](BehavioralFeature.html#getOwnedParameter())` in interface `[BehavioralFeature](BehavioralFeature.html)`
Returns:
the value of the '*Owned Parameter*' containment reference list.
See Also:
[`UMLPackage.getOperation_OwnedParameter()`](../../metadata/UMLPackage.html#getOperation_OwnedParameter())
[`Parameter.getOperation()`](Parameter.html#getOperation())
Model:
opposite="operation" containment="true" resolveProxies="true"
Generated:
getRaisedException
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Type](Type.html)> getRaisedException()
Returns the value of the '***Raised Exception***' reference list.
 The list contents are of type [`Type`](Type.html).
 It is bidirectional and its opposite is
 '[`*operation Of Raised Exception*`](Type.html#get_operationOfRaisedException())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Types representing exceptions that may be raised during an invocation of this operation.
 end-model-doc
Specified by:
`[getRaisedException](BehavioralFeature.html#getRaisedException())` in interface `[BehavioralFeature](BehavioralFeature.html)`
Returns:
the value of the '*Raised Exception*' reference list.
See Also:
[`UMLPackage.getOperation_RaisedException()`](../../metadata/UMLPackage.html#getOperation_RaisedException())
[`Type.get_operationOfRaisedException()`](Type.html#get_operationOfRaisedException())
Model:
opposite="_operationOfRaisedException" ordered="false"
Generated:
getTemplateParameter
@CheckForNull[OperationTemplateParameter](../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) getTemplateParameter()
Returns the value of the '***Template Parameter***' reference.
 It is bidirectional and its opposite is
 '[`*Parametered Element*`](../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html#getParameteredElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The OperationTemplateParameter that exposes this element as a formal parameter.
 end-model-doc
Specified by:
`[getTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter())` in interface `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`
Returns:
the value of the '*Template Parameter*' reference.
See Also:
[`setTemplateParameter(OperationTemplateParameter)`](#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter))
[`UMLPackage.getOperation_TemplateParameter()`](../../metadata/UMLPackage.html#getOperation_TemplateParameter())
[`OperationTemplateParameter.getParameteredElement()`](../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html#getParameteredElement())
Model:
opposite="parameteredElement" ordered="false"
Generated:
setTemplateParameter
void setTemplateParameter(@CheckForNull
 [OperationTemplateParameter](../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html) value)
Sets the value of the '[`*Template Parameter*`](#getTemplateParameter())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Template Parameter*' reference.
See Also:
[`getTemplateParameter()`](#getTemplateParameter())
Generated:
has_callEventOfOperation
boolean has_callEventOfOperation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_callOperationActionOfOperation
boolean has_callOperationActionOfOperation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPrecondition
boolean hasPrecondition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPostcondition
boolean hasPostcondition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRedefinedOperation
boolean hasRedefinedOperation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_operationOfRedefinedOperation
boolean has_operationOfRedefinedOperation()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface Operation">Interface Operation</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code><a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Operation</span><span class="extends-implements">
extends <a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Operation</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An Operation is a BehavioralFeature of a Classifier that specifies the name, type, parameters, and constraints for invoking an associated Behavior. An Operation may
 invoke both the execution of method behaviors as well as other behavioral responses. Operation specializes TemplateableElement in order to support specification of
 template operations and bound operations. Operation specializes ParameterableElement to specify that an operation can be exposed as a formal template parameter, and
 provided as an actual parameter in a binding of a template.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getType()"><code><em>Type</em></code></a></li>
<li><a href="#getDatatype()"><code><em>Datatype</em></code></a></li>
<li><a href="#getInterface()"><code><em>Interface</em></code></a></li>
<li><a href="#get_artifactOfOwnedOperation()"><code><em>artifact Of Owned Operation</em></code></a></li>
<li><a href="#getBodyCondition()"><code><em>Body Condition</em></code></a></li>
<li><a href="#getUMLClass()"><code><em>UML Class</em></code></a></li>
<li><a href="#isOrdered()"><code><em>Ordered</em></code></a></li>
<li><a href="#isQuery()"><code><em>Query</em></code></a></li>
<li><a href="#isUnique()"><code><em>Unique</em></code></a></li>
<li><a href="#getLower()"><code><em>Lower</em></code></a></li>
<li><a href="#getPostcondition()"><code><em>Postcondition</em></code></a></li>
<li><a href="#getPrecondition()"><code><em>Precondition</em></code></a></li>
<li><a href="#getRedefinedOperation()"><code><em>Redefined Operation</em></code></a></li>
<li><a href="#get_operationOfRedefinedOperation()"><code><em>operation Of Redefined Operation</em></code></a></li>
<li><a href="#getUpper()"><code><em>Upper</em></code></a></li>
<li><a href="#get_callOperationActionOfOperation()"><code><em>call Operation Action Of Operation</em></code></a></li>
<li><a href="#get_callEventOfOperation()"><code><em>call Event Of Operation</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getOperation()"><code>UMLPackage.getOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='classes.mdkernel'"</dd>
<dt>Generated:</dt>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_artifactOfOwnedOperation()">get_artifactOfOwnedOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>artifact Of Owned Operation</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_callEventOfOperation()">get_callEventOfOperation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>call Event Of Operation</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_callOperationActionOfOperation()">get_callOperationActionOfOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>call Operation Action Of Operation</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_operationOfRedefinedOperation()">get_operationOfRedefinedOperation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>operation Of Redefined Operation</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBodyCondition()">getBodyCondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Body Condition</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDatatype()">getDatatype</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Datatype</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInterface()">getInterface</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Interface</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLower()">getLower</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Lower</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedParameter()">getOwnedParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Parameter</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPostcondition()">getPostcondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Postcondition</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrecondition()">getPrecondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Precondition</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRaisedException()">getRaisedException</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Raised Exception</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedOperation()">getRedefinedOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Operation</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTemplateParameter()">getTemplateParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Template Parameter</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Type</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUMLClass()">getUMLClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>UML Class</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUpper()">getUpper</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Upper</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_callEventOfOperation()">has_callEventOfOperation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_callOperationActionOfOperation()">has_callOperationActionOfOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_operationOfRedefinedOperation()">has_operationOfRedefinedOperation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPostcondition()">hasPostcondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPrecondition()">hasPrecondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRedefinedOperation()">hasRedefinedOperation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isOrdered()">isOrdered</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Ordered</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isQuery()">isQuery</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Query</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isUnique()">isUnique</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Unique</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_artifactOfOwnedOperation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)">set_artifactOfOwnedOperation</a><wbr/>(<a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_artifactOfOwnedOperation()"><code><em>artifact Of Owned Operation</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBodyCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setBodyCondition</a><wbr/>(<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getBodyCondition()"><code><em>Body Condition</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)">setDatatype</a><wbr/>(<a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDatatype()"><code><em>Datatype</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">setInterface</a><wbr/>(<a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getInterface()"><code><em>Interface</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setQuery(boolean)">setQuery</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isQuery()"><code><em>Query</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter)">setTemplateParameter</a><wbr/>(<a href="../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">setUMLClass</a><wbr/>(<a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getUMLClass()"><code><em>UML Class</em></code></a>' container reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#atInsert()">atInsert</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#clone()">clone</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()">removeAllPropertyChangeListeners</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></h3>
<code><a href="BehavioralFeature.html#getConcurrency()">getConcurrency</a>, <a href="BehavioralFeature.html#getMethod()">getMethod</a>, <a href="BehavioralFeature.html#getOwnedParameterSet()">getOwnedParameterSet</a>, <a href="BehavioralFeature.html#hasMethod()">hasMethod</a>, <a href="BehavioralFeature.html#hasOwnedParameter()">hasOwnedParameter</a>, <a href="BehavioralFeature.html#hasOwnedParameterSet()">hasOwnedParameterSet</a>, <a href="BehavioralFeature.html#hasRaisedException()">hasRaisedException</a>, <a href="BehavioralFeature.html#isAbstract()">isAbstract</a>, <a href="BehavioralFeature.html#setAbstract(boolean)">setAbstract</a>, <a href="BehavioralFeature.html#setConcurrency(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.CallConcurrencyKind)">setConcurrency</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Feature">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Feature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Feature</a></h3>
<code><a href="Feature.html#getFeaturingClassifier()">getFeaturingClassifier</a>, <a href="Feature.html#isStatic()">isStatic</a>, <a href="Feature.html#setFeaturingClassifier(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">setFeaturingClassifier</a>, <a href="Feature.html#setStatic(boolean)">setStatic</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="NamedElement.html#getName()">getName</a>, <a href="NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="NamedElement.html#getNamespace()">getNamespace</a>, <a href="NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="NamedElement.html#getVisibility()">getVisibility</a>, <a href="NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="NamedElement.html#setName(java.lang.String)">setName</a>, <a href="NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="Namespace.html#getElementImport()">getElementImport</a>, <a href="Namespace.html#getImportedMember()">getImportedMember</a>, <a href="Namespace.html#getMember()">getMember</a>, <a href="Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="Namespace.html#getPackageImport()">getPackageImport</a>, <a href="Namespace.html#hasElementImport()">hasElementImport</a>, <a href="Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="Namespace.html#hasMember()">hasMember</a>, <a href="Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefFeatured">Methods inherited from interface javax.jmi.reflect.RefFeatured</h3>
<code>refGetValue, refInvokeOperation, refInvokeOperation, refSetValue</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefObject">Methods inherited from interface javax.jmi.reflect.RefObject</h3>
<code>refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getOwnedTemplateSignature()">getOwnedTemplateSignature</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#getTemplateBinding()">getTemplateBinding</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#hasTemplateBinding()">hasTemplateBinding</a>, <a href="../../auxiliaryconstructs/mdtemplates/TemplateableElement.html#setOwnedTemplateSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)">setOwnedTemplateSignature</a></code></div>
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
<section class="detail" id="getInterface()">
<h3>getInterface</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></span> <span class="element-name">getInterface</span>()</div>
<div class="block">Returns the value of the '<em><b>Interface</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdinterfaces/Interface.html#getOwnedOperation()"><code><em>Owned Operation</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Interface that owns this Operation, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Interface</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)"><code>setInterface(Interface)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOperation_Interface()"><code>UMLPackage.getOperation_Interface()</code></a></li>
<li><a href="../mdinterfaces/Interface.html#getOwnedOperation()"><code>Interface.getOwnedOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedOperation" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInterface(com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces.Interface)">
<h3>setInterface</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInterface</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getInterface()"><code><em>Interface</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Interface</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getInterface()"><code>getInterface()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOrdered()">
<h3>isOrdered</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isOrdered</span>()</div>
<div class="block">Returns the value of the '<em><b>Ordered</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies whether the return parameter is ordered or not, if present.  This information is derived from the return result for this Operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Ordered</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getOperation_Ordered()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isQuery()">
<h3>isQuery</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isQuery</span>()</div>
<div class="block">Returns the value of the '<em><b>Query</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies whether an execution of the BehavioralFeature leaves the state of the system unchanged (isQuery=true) or whether side effects may occur (isQuery=false).
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Query</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setQuery(boolean)"><code>setQuery(boolean)</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getOperation_Query()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setQuery(boolean)">
<h3>setQuery</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setQuery</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isQuery()"><code><em>Query</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Query</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isQuery()"><code>isQuery()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUnique()">
<h3>isUnique</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isUnique</span>()</div>
<div class="block">Returns the value of the '<em><b>Unique</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies whether the return parameter is unique or not, if present. This information is derived from the return result for this Operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Unique</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getOperation_Unique()</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUMLClass()">
<h3>getUMLClass</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getUMLClass</span>()</div>
<div class="block">Returns the value of the '<em><b>UML Class</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Class.html#getOwnedOperation()"><code><em>Owned Operation</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Class that owns this operation, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>UML Class</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)"><code>setUMLClass(Class)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOperation_UMLClass()"><code>UMLPackage.getOperation_UMLClass()</code></a></li>
<li><a href="Class.html#getOwnedOperation()"><code>Class.getOwnedOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedOperation" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUMLClass(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Class)">
<h3>setUMLClass</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUMLClass</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getUMLClass()"><code><em>UML Class</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>UML Class</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getUMLClass()"><code>getUMLClass()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_callEventOfOperation()">
<h3>get_callEventOfOperation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a>&gt;</span> <span class="element-name">get_callEventOfOperation</span>()</div>
<div class="block">Returns the value of the '<em><b>call Event Of Operation</b></em>' reference list.
 The list contents are of type <a href="../../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>CallEvent</code></a>.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdcommunications/CallEvent.html#getOperation()"><code><em>Operation</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>call Event Of Operation</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>call Event Of Operation</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation__callEventOfOperation()"><code>UMLPackage.getOperation__callEventOfOperation()</code></a></li>
<li><a href="../../commonbehaviors/mdcommunications/CallEvent.html#getOperation()"><code>CallEvent.getOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="operation" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_callOperationActionOfOperation()">
<h3>get_callOperationActionOfOperation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a>&gt;</span> <span class="element-name">get_callOperationActionOfOperation</span>()</div>
<div class="block">Returns the value of the '<em><b>call Operation Action Of Operation</b></em>' reference list.
 The list contents are of type <a href="../../actions/mdbasicactions/CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions"><code>CallOperationAction</code></a>.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/CallOperationAction.html#getOperation()"><code><em>Operation</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>call Operation Action Of Operation</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>call Operation Action Of Operation</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation__callOperationActionOfOperation()"><code>UMLPackage.getOperation__callOperationActionOfOperation()</code></a></li>
<li><a href="../../actions/mdbasicactions/CallOperationAction.html#getOperation()"><code>CallOperationAction.getOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="operation" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLower()">
<h3>getLower</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getLower</span>()</div>
<div class="block">Returns the value of the '<em><b>Lower</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the lower multiplicity of the return parameter, if present. This information is derived from the return result for this Operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Lower</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation_Lower()"><code>UMLPackage.getOperation_Lower()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Integer" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUpper()">
<h3>getUpper</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getUpper</span>()</div>
<div class="block">Returns the value of the '<em><b>Upper</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The upper multiplicity of the return parameter, if present. This information is derived from the return result for this Operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Upper</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation_Upper()"><code>UMLPackage.getOperation_Upper()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.UnlimitedNatural" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrecondition()">
<h3>getPrecondition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getPrecondition</span>()</div>
<div class="block">Returns the value of the '<em><b>Precondition</b></em>' reference list.
 The list contents are of type <a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.
 It is bidirectional and its opposite is '<a href="Constraint.html#getPreContext()"><code><em>Pre Context</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional set of Constraints on the state of the system when the Operation is invoked.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Precondition</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation_Precondition()"><code>UMLPackage.getOperation_Precondition()</code></a></li>
<li><a href="Constraint.html#getPreContext()"><code>Constraint.getPreContext()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="preContext" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPostcondition()">
<h3>getPostcondition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getPostcondition</span>()</div>
<div class="block">Returns the value of the '<em><b>Postcondition</b></em>' reference list.
 The list contents are of type <a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.
 It is bidirectional and its opposite is '<a href="Constraint.html#getPostContext()"><code><em>Post Context</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional set of Constraints specifying the state of the system when the Operation is completed.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Postcondition</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation_Postcondition()"><code>UMLPackage.getOperation_Postcondition()</code></a></li>
<li><a href="Constraint.html#getPostContext()"><code>Constraint.getPostContext()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="postContext" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedOperation()">
<h3>getRedefinedOperation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">getRedefinedOperation</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Operation</b></em>' reference list.
 The list contents are of type <a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.
 It is bidirectional and its opposite is
 '<a href="#get_operationOfRedefinedOperation()"><code><em>operation Of Redefined Operation</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Operations that are redefined by this Operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Operation</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation_RedefinedOperation()"><code>UMLPackage.getOperation_RedefinedOperation()</code></a></li>
<li><a href="#get_operationOfRedefinedOperation()"><code>get_operationOfRedefinedOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_operationOfRedefinedOperation" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_operationOfRedefinedOperation()">
<h3>get_operationOfRedefinedOperation</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">get_operationOfRedefinedOperation</span>()</div>
<div class="block">Returns the value of the '<em><b>operation Of Redefined Operation</b></em>' reference list.
 The list contents are of type <a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Operation</code></a>.
 It is bidirectional and its opposite is '<a href="#getRedefinedOperation()"><code><em>Redefined Operation</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>operation Of Redefined Operation</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>operation Of Redefined Operation</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation__operationOfRedefinedOperation()"><code>UMLPackage.getOperation__operationOfRedefinedOperation()</code></a></li>
<li><a href="#getRedefinedOperation()"><code>getRedefinedOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedOperation" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDatatype()">
<h3>getDatatype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></span> <span class="element-name">getDatatype</span>()</div>
<div class="block">Returns the value of the '<em><b>Datatype</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="DataType.html#getOwnedOperation()"><code><em>Owned Operation</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The DataType that owns this Operation, if any.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Datatype</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)"><code>setDatatype(DataType)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOperation_Datatype()"><code>UMLPackage.getOperation_Datatype()</code></a></li>
<li><a href="DataType.html#getOwnedOperation()"><code>DataType.getOwnedOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedOperation" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDatatype(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DataType)">
<h3>setDatatype</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDatatype</span><wbr/><span class="parameters">(@CheckForNull
 <a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDatatype()"><code><em>Datatype</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Datatype</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getDatatype()"><code>getDatatype()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns the value of the '<em><b>Type</b></em>' reference.
 It is bidirectional and its opposite is '<code><em>operation Of Type</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The return type of the operation, if present. This information is derived from the return result for this Operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Type</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation_Type()"><code>UMLPackage.getOperation_Type()</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type#get_operationOfType</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_operationOfType" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_artifactOfOwnedOperation()">
<h3>get_artifactOfOwnedOperation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></span> <span class="element-name">get_artifactOfOwnedOperation</span>()</div>
<div class="block">Returns the value of the '<em><b>artifact Of Owned Operation</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../deployments/mdartifacts/Artifact.html#getOwnedOperation()"><code><em>Owned Operation</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>artifact Of Owned Operation</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>artifact Of Owned Operation</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_artifactOfOwnedOperation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)"><code>set_artifactOfOwnedOperation(Artifact)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOperation__artifactOfOwnedOperation()"><code>UMLPackage.getOperation__artifactOfOwnedOperation()</code></a></li>
<li><a href="../../deployments/mdartifacts/Artifact.html#getOwnedOperation()"><code>Artifact.getOwnedOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedOperation" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_artifactOfOwnedOperation(com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts.Artifact)">
<h3>set_artifactOfOwnedOperation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_artifactOfOwnedOperation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_artifactOfOwnedOperation()"><code><em>artifact Of Owned Operation</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>artifact Of Owned Operation</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_artifactOfOwnedOperation()"><code>get_artifactOfOwnedOperation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBodyCondition()">
<h3>getBodyCondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getBodyCondition</span>()</div>
<div class="block">Returns the value of the '<em><b>Body Condition</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Constraint.html#getBodyContext()"><code><em>Body Context</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional Constraint on the result values of an invocation of this Operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Body Condition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setBodyCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)"><code>setBodyCondition(Constraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOperation_BodyCondition()"><code>UMLPackage.getOperation_BodyCondition()</code></a></li>
<li><a href="Constraint.html#getBodyContext()"><code>Constraint.getBodyContext()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="bodyContext" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBodyCondition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>setBodyCondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setBodyCondition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getBodyCondition()"><code><em>Body Condition</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Body Condition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getBodyCondition()"><code>getBodyCondition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedParameter()">
<h3>getOwnedParameter</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a>&gt;</span> <span class="element-name">getOwnedParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Parameter</b></em>' containment reference list.
 The list contents are of type <a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Parameter</code></a>.
 It is bidirectional and its opposite is '<a href="Parameter.html#getOperation()"><code><em>Operation</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The parameters owned by this Operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BehavioralFeature.html#getOwnedParameter()">getOwnedParameter</a></code> in interface <code><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Parameter</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation_OwnedParameter()"><code>UMLPackage.getOperation_OwnedParameter()</code></a></li>
<li><a href="Parameter.html#getOperation()"><code>Parameter.getOperation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="operation" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRaisedException()">
<h3>getRaisedException</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt;</span> <span class="element-name">getRaisedException</span>()</div>
<div class="block">Returns the value of the '<em><b>Raised Exception</b></em>' reference list.
 The list contents are of type <a href="Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Type</code></a>.
 It is bidirectional and its opposite is
 '<a href="Type.html#get_operationOfRaisedException()"><code><em>operation Of Raised Exception</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Types representing exceptions that may be raised during an invocation of this operation.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BehavioralFeature.html#getRaisedException()">getRaisedException</a></code> in interface <code><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Raised Exception</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOperation_RaisedException()"><code>UMLPackage.getOperation_RaisedException()</code></a></li>
<li><a href="Type.html#get_operationOfRaisedException()"><code>Type.get_operationOfRaisedException()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_operationOfRaisedException" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateParameter()">
<h3>getTemplateParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></span> <span class="element-name">getTemplateParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>Template Parameter</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html#getParameteredElement()"><code><em>Parametered Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The OperationTemplateParameter that exposes this element as a formal parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()">getTemplateParameter</a></code> in interface <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Template Parameter</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter)"><code>setTemplateParameter(OperationTemplateParameter)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOperation_TemplateParameter()"><code>UMLPackage.getOperation_TemplateParameter()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html#getParameteredElement()"><code>OperationTemplateParameter.getParameteredElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="parameteredElement" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.OperationTemplateParameter)">
<h3>setTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTemplateParameter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../auxiliaryconstructs/mdtemplates/OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Template Parameter</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getTemplateParameter()"><code>getTemplateParameter()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_callEventOfOperation()">
<h3>has_callEventOfOperation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_callEventOfOperation</span>()
                          throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_callOperationActionOfOperation()">
<h3>has_callOperationActionOfOperation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_callOperationActionOfOperation</span>()
                                    throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPrecondition()">
<h3>hasPrecondition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPrecondition</span>()
                 throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPostcondition()">
<h3>hasPostcondition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPostcondition</span>()
                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRedefinedOperation()">
<h3>hasRedefinedOperation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRedefinedOperation</span>()
                       throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_operationOfRedefinedOperation()">
<h3>has_operationOfRedefinedOperation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_operationOfRedefinedOperation</span>()
                                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
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
