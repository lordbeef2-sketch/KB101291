# JAVA OPENAPI: Namespace (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Namespace.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Namespace.html`
- source_sha256: `0114839fef023e999a24f58b78d328a802051d887fcac62731af8f18180ce1ef`
- captured_utc: `2026-07-14T16:46:29.512193+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Namespace

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[Activity](../../activities/mdfundamentalactivities/Activity.html)`, `[Actor](../../mdusecases/Actor.html)`, `[Artifact](../../deployments/mdartifacts/Artifact.html)`, `[Association](Association.html)`, `[AssociationClass](../mdassociationclasses/AssociationClass.html)`, `[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[BehavioralFeature](BehavioralFeature.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[Class](Class.html)`, `[Classifier](Classifier.html)`, `[Collaboration](../../compositestructures/mdcollaborations/Collaboration.html)`, `[CommunicationPath](../../deployments/mdnodes/CommunicationPath.html)`, `[Component](../../components/mdbasiccomponents/Component.html)`, `[ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html)`, `[DataType](DataType.html)`, `[DeploymentSpecification](../../deployments/mdcomponentdeployments/DeploymentSpecification.html)`, `[Device](../../deployments/mdnodes/Device.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `[Enumeration](Enumeration.html)`, `[ExecutionEnvironment](../../deployments/mdnodes/ExecutionEnvironment.html)`, `[ExpansionRegion](../../activities/mdextrastructuredactivities/ExpansionRegion.html)`, `[Extension](../../mdprofiles/Extension.html)`, `[FinalState](../../statemachines/mdbehaviorstatemachines/FinalState.html)`, `[FunctionBehavior](../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`, `[InformationItem](../../auxiliaryconstructs/mdinformationflows/InformationItem.html)`, `[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`, `[InteractionOperand](../../interactions/mdfragments/InteractionOperand.html)`, `[Interface](../mdinterfaces/Interface.html)`, `[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`, `[Model](../../auxiliaryconstructs/mdmodels/Model.html)`, `[Node](../../deployments/mdnodes/Node.html)`, `[OpaqueBehavior](../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`, `[Operation](Operation.html)`, `[Package](Package.html)`, `[PrimitiveType](PrimitiveType.html)`, `[Profile](../../mdprofiles/Profile.html)`, `[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html)`, `[Reception](../../commonbehaviors/mdcommunications/Reception.html)`, `[Region](../../statemachines/mdbehaviorstatemachines/Region.html)`, `[SequenceNode](../../activities/mdstructuredactivities/SequenceNode.html)`, `[Signal](../../commonbehaviors/mdcommunications/Signal.html)`, `[State](../../statemachines/mdbehaviorstatemachines/State.html)`, `[StateMachine](../../statemachines/mdbehaviorstatemachines/StateMachine.html)`, `[Stereotype](../../mdprofiles/Stereotype.html)`, `[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html)`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html)`, `[UseCase](../../mdusecases/UseCase.html)`

public interfaceNamespaceextends [NamedElement](NamedElement.html)

begin-user-doc 
 A representation of the model object '***Namespace***'.
 end-user-doc 
begin-model-doc 
 A Namespace is an Element in a model that owns and/or imports a set of NamedElements that can be identified by name.
 end-model-doc 
The following features are supported:
 [`*Element Import*`](#getElementImport())
[`*Owned Rule*`](#getOwnedRule())
[`*Package Import*`](#getPackageImport())
[`*Imported Member*`](#getImportedMember())
[`*Member*`](#getMember())
[`*Owned Member*`](#getOwnedMember())
[`*Owned Diagram*`](#getOwnedDiagram())

See Also:
[`UMLPackage.getNamespace()`](../../metadata/UMLPackage.html#getNamespace())
Model:
abstract="true"
 annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ElementImport](ElementImport.html)>`
`[getElementImport](#getElementImport())()`
Returns the value of the '***Element Import***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PackageableElement](PackageableElement.html)>`
`[getImportedMember](#getImportedMember())()`
Returns the value of the '***Imported Member***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[NamedElement](NamedElement.html)>`
`[getMember](#getMember())()`
Returns the value of the '***Member***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Diagram](Diagram.html)>`
`[getOwnedDiagram](#getOwnedDiagram())()`
Returns the value of the '***Owned Diagram***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[NamedElement](NamedElement.html)>`
`[getOwnedMember](#getOwnedMember())()`
Returns the value of the '***Owned Member***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](Constraint.html)>`
`[getOwnedRule](#getOwnedRule())()`
Returns the value of the '***Owned Rule***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PackageImport](PackageImport.html)>`
`[getPackageImport](#getPackageImport())()`
Returns the value of the '***Package Import***' containment reference list.
`boolean`
`[hasElementImport](#hasElementImport())()`

`boolean`
`[hasImportedMember](#hasImportedMember())()`

`boolean`
`[hasMember](#hasMember())()`

`boolean`
`[hasOwnedDiagram](#hasOwnedDiagram())()`

`boolean`
`[hasOwnedMember](#hasOwnedMember())()`

`boolean`
`[hasOwnedRule](#hasOwnedRule())()`

`boolean`
`[hasPackageImport](#hasPackageImport())()`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](NamedElement.html#getClientDependency()), [getName](NamedElement.html#getName()), [getNameExpression](NamedElement.html#getNameExpression()), [getNamespace](NamedElement.html#getNamespace()), [getQualifiedName](NamedElement.html#getQualifiedName()), [getSupplierDependency](NamedElement.html#getSupplierDependency()), [getVisibility](NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](NamedElement.html#hasClientDependency()), [hasSupplierDependency](NamedElement.html#hasSupplierDependency()), [setName](NamedElement.html#setName(java.lang.String)), [setNameExpression](NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getElementImport
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ElementImport](ElementImport.html)> getElementImport()
Returns the value of the '***Element Import***' containment reference list.
 The list contents are of type [`ElementImport`](ElementImport.html).
 It is bidirectional and its opposite is
 '[`*Importing Namespace*`](ElementImport.html#getImportingNamespace())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the ElementImports owned by the Namespace.
 end-model-doc
Returns:
the value of the '*Element Import*' containment reference list.
See Also:
[`UMLPackage.getNamespace_ElementImport()`](../../metadata/UMLPackage.html#getNamespace_ElementImport())
[`ElementImport.getImportingNamespace()`](ElementImport.html#getImportingNamespace())
Model:
opposite="importingNamespace" containment="true" resolveProxies="true" ordered="false"
Generated:
getOwnedRule
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Constraint](Constraint.html)> getOwnedRule()
Returns the value of the '***Owned Rule***' containment reference list.
 The list contents are of type [`Constraint`](Constraint.html).
 It is bidirectional and its opposite is '[`*Context*`](Constraint.html#getContext())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies a set of Constraints owned by this Namespace.
 end-model-doc
Returns:
the value of the '*Owned Rule*' containment reference list.
See Also:
[`UMLPackage.getNamespace_OwnedRule()`](../../metadata/UMLPackage.html#getNamespace_OwnedRule())
[`Constraint.getContext()`](Constraint.html#getContext())
Model:
opposite="context" containment="true" resolveProxies="true" ordered="false"
Generated:
getPackageImport
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PackageImport](PackageImport.html)> getPackageImport()
Returns the value of the '***Package Import***' containment reference list.
 The list contents are of type [`PackageImport`](PackageImport.html).
 It is bidirectional and its opposite is
 '[`*Importing Namespace*`](PackageImport.html#getImportingNamespace())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the PackageImports owned by the Namespace.
 end-model-doc
Returns:
the value of the '*Package Import*' containment reference list.
See Also:
[`UMLPackage.getNamespace_PackageImport()`](../../metadata/UMLPackage.html#getNamespace_PackageImport())
[`PackageImport.getImportingNamespace()`](PackageImport.html#getImportingNamespace())
Model:
opposite="importingNamespace" containment="true" resolveProxies="true" ordered="false"
Generated:
getOwnedMember
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[NamedElement](NamedElement.html)> getOwnedMember()
Returns the value of the '***Owned Member***' reference list.
 The list contents are of type [`NamedElement`](NamedElement.html).
 It is bidirectional and its opposite is '[`*Namespace*`](NamedElement.html#getNamespace())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A collection of NamedElements owned by the Namespace.
 end-model-doc
Returns:
the value of the '*Owned Member*' reference list.
See Also:
[`UMLPackage.getNamespace_OwnedMember()`](../../metadata/UMLPackage.html#getNamespace_OwnedMember())
[`NamedElement.getNamespace()`](NamedElement.html#getNamespace())
Model:
opposite="namespace" transient="true" volatile="true" derived="true" ordered="false"
Generated:
getMember
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[NamedElement](NamedElement.html)> getMember()
Returns the value of the '***Member***' reference list.
 The list contents are of type [`NamedElement`](NamedElement.html).
 It is bidirectional and its opposite is '[`*namespace Of Member*`](NamedElement.html#get_namespaceOfMember())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A collection of NamedElements identifiable within the Namespace, either by being owned or by being introduced by importing or inheritance.
 end-model-doc
Returns:
the value of the '*Member*' reference list.
See Also:
[`UMLPackage.getNamespace_Member()`](../../metadata/UMLPackage.html#getNamespace_Member())
[`NamedElement.get_namespaceOfMember()`](NamedElement.html#get_namespaceOfMember())
Model:
opposite="_namespaceOfMember" transient="true" volatile="true" derived="true" ordered="false"
Generated:
getImportedMember
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PackageableElement](PackageableElement.html)> getImportedMember()
Returns the value of the '***Imported Member***' reference list.
 The list contents are of type [`PackageableElement`](PackageableElement.html).
 It is bidirectional and its opposite is
 '
invalid reference
`*namespace Of Imported Member*`
'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the PackageableElements that are members of this Namespace as a result of either PackageImports or ElementImports.
 end-model-doc
Returns:
the value of the '*Imported Member*' reference list.
See Also:
[`UMLPackage.getNamespace_ImportedMember()`](../../metadata/UMLPackage.html#getNamespace_ImportedMember())
invalid reference
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement#get_namespaceOfImportedMember`
Model:
opposite="_namespaceOfImportedMember" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getOwnedDiagram
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Diagram](Diagram.html)> getOwnedDiagram()
Returns the value of the '***Owned Diagram***' containment reference list.
 The list contents are of type [`Diagram`](Diagram.html).
 It is bidirectional and its opposite is '[`*Owner Of Diagram*`](Diagram.html#getOwnerOfDiagram())'.
 begin-user-doc 
If the meaning of the '*Owned Diagram*' containment reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owned Diagram*' containment reference list.
See Also:
[`UMLPackage.getNamespace_OwnedDiagram()`](../../metadata/UMLPackage.html#getNamespace_OwnedDiagram())
[`Diagram.getOwnerOfDiagram()`](Diagram.html#getOwnerOfDiagram())
Model:
opposite="ownerOfDiagram" containment="true" resolveProxies="true" ordered="false"
Generated:
hasElementImport
boolean hasElementImport()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedRule
boolean hasOwnedRule()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasPackageImport
boolean hasPackageImport()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedMember
boolean hasOwnedMember()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasMember
boolean hasMember()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasImportedMember
boolean hasImportedMember()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasOwnedDiagram
boolean hasOwnedDiagram()
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
<h1 class="title" title="Interface Namespace">Interface Namespace</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="../../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code>, <code><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code>, <code><a href="Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code>, <code><a href="../mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="BehavioralFeature.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">BehavioralFeature</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a href="../../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code>, <code><a href="../../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code>, <code><a href="../../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code>, <code><a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code>, <code><a href="DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code>, <code><a href="../../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code>, <code><a href="../../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code><a href="Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code>, <code><a href="../../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code>, <code><a href="../../activities/mdextrastructuredactivities/ExpansionRegion.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionRegion</a></code>, <code><a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../auxiliaryconstructs/mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code>, <code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="../../interactions/mdfragments/InteractionOperand.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionOperand</a></code>, <code><a href="../mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code>, <code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code>, <code><a href="../../auxiliaryconstructs/mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code>, <code><a href="../../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code>, <code><a href="Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code>, <code><a href="PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code>, <code><a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Reception.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Reception</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code>, <code><a href="../../activities/mdstructuredactivities/SequenceNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">SequenceNode</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code>, <code><a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code>, <code><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code>, <code><a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Namespace</span><span class="extends-implements">
extends <a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Namespace</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Namespace is an Element in a model that owns and/or imports a set of NamedElements that can be identified by name.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getElementImport()"><code><em>Element Import</em></code></a></li>
<li><a href="#getOwnedRule()"><code><em>Owned Rule</em></code></a></li>
<li><a href="#getPackageImport()"><code><em>Package Import</em></code></a></li>
<li><a href="#getImportedMember()"><code><em>Imported Member</em></code></a></li>
<li><a href="#getMember()"><code><em>Member</em></code></a></li>
<li><a href="#getOwnedMember()"><code><em>Owned Member</em></code></a></li>
<li><a href="#getOwnedDiagram()"><code><em>Owned Diagram</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getNamespace()"><code>UMLPackage.getNamespace()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='classes.mdkernel'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElementImport()">getElementImport</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Element Import</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportedMember()">getImportedMember</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Imported Member</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMember()">getMember</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Member</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedDiagram()">getOwnedDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Diagram</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedMember()">getOwnedMember</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Member</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedRule()">getOwnedRule</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Rule</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPackageImport()">getPackageImport</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Package Import</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasElementImport()">hasElementImport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasImportedMember()">hasImportedMember</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasMember()">hasMember</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedDiagram()">hasOwnedDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedMember()">hasOwnedMember</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasOwnedRule()">hasOwnedRule</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPackageImport()">hasPackageImport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="NamedElement.html#getName()">getName</a>, <a href="NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="NamedElement.html#getNamespace()">getNamespace</a>, <a href="NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="NamedElement.html#getVisibility()">getVisibility</a>, <a href="NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="NamedElement.html#setName(java.lang.String)">setName</a>, <a href="NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefBaseObject">Methods inherited from interface javax.jmi.reflect.RefBaseObject</h3>
<code>equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefFeatured">Methods inherited from interface javax.jmi.reflect.RefFeatured</h3>
<code>refGetValue, refInvokeOperation, refInvokeOperation, refSetValue</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.jmi.reflect.RefObject">Methods inherited from interface javax.jmi.reflect.RefObject</h3>
<code>refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite</code></div>
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
<section class="detail" id="getElementImport()">
<h3>getElementImport</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementImport</a>&gt;</span> <span class="element-name">getElementImport</span>()</div>
<div class="block">Returns the value of the '<em><b>Element Import</b></em>' containment reference list.
 The list contents are of type <a href="ElementImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ElementImport</code></a>.
 It is bidirectional and its opposite is
 '<a href="ElementImport.html#getImportingNamespace()"><code><em>Importing Namespace</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the ElementImports owned by the Namespace.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Element Import</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamespace_ElementImport()"><code>UMLPackage.getNamespace_ElementImport()</code></a></li>
<li><a href="ElementImport.html#getImportingNamespace()"><code>ElementImport.getImportingNamespace()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="importingNamespace" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedRule()">
<h3>getOwnedRule</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getOwnedRule</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Rule</b></em>' containment reference list.
 The list contents are of type <a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Constraint</code></a>.
 It is bidirectional and its opposite is '<a href="Constraint.html#getContext()"><code><em>Context</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies a set of Constraints owned by this Namespace.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Rule</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamespace_OwnedRule()"><code>UMLPackage.getNamespace_OwnedRule()</code></a></li>
<li><a href="Constraint.html#getContext()"><code>Constraint.getContext()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="context" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPackageImport()">
<h3>getPackageImport</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageImport</a>&gt;</span> <span class="element-name">getPackageImport</span>()</div>
<div class="block">Returns the value of the '<em><b>Package Import</b></em>' containment reference list.
 The list contents are of type <a href="PackageImport.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageImport</code></a>.
 It is bidirectional and its opposite is
 '<a href="PackageImport.html#getImportingNamespace()"><code><em>Importing Namespace</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the PackageImports owned by the Namespace.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Package Import</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamespace_PackageImport()"><code>UMLPackage.getNamespace_PackageImport()</code></a></li>
<li><a href="PackageImport.html#getImportingNamespace()"><code>PackageImport.getImportingNamespace()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="importingNamespace" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedMember()">
<h3>getOwnedMember</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getOwnedMember</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Member</b></em>' reference list.
 The list contents are of type <a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.
 It is bidirectional and its opposite is '<a href="NamedElement.html#getNamespace()"><code><em>Namespace</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A collection of NamedElements owned by the Namespace.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Member</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamespace_OwnedMember()"><code>UMLPackage.getNamespace_OwnedMember()</code></a></li>
<li><a href="NamedElement.html#getNamespace()"><code>NamedElement.getNamespace()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="namespace" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMember()">
<h3>getMember</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt;</span> <span class="element-name">getMember</span>()</div>
<div class="block">Returns the value of the '<em><b>Member</b></em>' reference list.
 The list contents are of type <a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>NamedElement</code></a>.
 It is bidirectional and its opposite is '<a href="NamedElement.html#get_namespaceOfMember()"><code><em>namespace Of Member</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A collection of NamedElements identifiable within the Namespace, either by being owned or by being introduced by importing or inheritance.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Member</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamespace_Member()"><code>UMLPackage.getNamespace_Member()</code></a></li>
<li><a href="NamedElement.html#get_namespaceOfMember()"><code>NamedElement.get_namespaceOfMember()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_namespaceOfMember" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImportedMember()">
<h3>getImportedMember</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a>&gt;</span> <span class="element-name">getImportedMember</span>()</div>
<div class="block">Returns the value of the '<em><b>Imported Member</b></em>' reference list.
 The list contents are of type <a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>PackageableElement</code></a>.
 It is bidirectional and its opposite is
 '
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code><em>namespace Of Imported Member</em></code></pre>
</details>
'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the PackageableElements that are members of this Namespace as a result of either PackageImports or ElementImports.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Imported Member</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamespace_ImportedMember()"><code>UMLPackage.getNamespace_ImportedMember()</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement#get_namespaceOfImportedMember</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_namespaceOfImportedMember" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedDiagram()">
<h3>getOwnedDiagram</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</span> <span class="element-name">getOwnedDiagram</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Diagram</b></em>' containment reference list.
 The list contents are of type <a href="Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Diagram</code></a>.
 It is bidirectional and its opposite is '<a href="Diagram.html#getOwnerOfDiagram()"><code><em>Owner Of Diagram</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owned Diagram</em>' containment reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Diagram</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getNamespace_OwnedDiagram()"><code>UMLPackage.getNamespace_OwnedDiagram()</code></a></li>
<li><a href="Diagram.html#getOwnerOfDiagram()"><code>Diagram.getOwnerOfDiagram()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownerOfDiagram" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasElementImport()">
<h3>hasElementImport</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasElementImport</span>()
                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedRule()">
<h3>hasOwnedRule</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedRule</span>()
              throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPackageImport()">
<h3>hasPackageImport</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPackageImport</span>()
                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedMember()">
<h3>hasOwnedMember</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedMember</span>()
                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasMember()">
<h3>hasMember</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasMember</span>()
           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasImportedMember()">
<h3>hasImportedMember</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasImportedMember</span>()
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedDiagram()">
<h3>hasOwnedDiagram</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasOwnedDiagram</span>()
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
