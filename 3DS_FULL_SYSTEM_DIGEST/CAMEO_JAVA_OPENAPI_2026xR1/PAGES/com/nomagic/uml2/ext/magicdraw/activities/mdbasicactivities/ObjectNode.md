# JAVA OPENAPI: ObjectNode (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/activities/mdbasicactivities/ObjectNode.html
- source_path: `com/nomagic/uml2/ext/magicdraw/activities/mdbasicactivities/ObjectNode.html`
- source_sha256: `f1f0511cefedef5a93628e975f7630f64563747a8d428ec184cfa8a4ec915008`
- captured_utc: `2026-07-14T16:46:26.269149+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities](package-summary.html)

## Interface ObjectNode

All Superinterfaces:
`[ActivityNode](../mdfundamentalactivities/ActivityNode.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TypedElement](../../classes/mdkernel/TypedElement.html)`

All Known Subinterfaces:
`[ActionInputPin](../../actions/mdstructuredactions/ActionInputPin.html)`, `[ActivityParameterNode](ActivityParameterNode.html)`, `[CentralBufferNode](../mdintermediateactivities/CentralBufferNode.html)`, `[DataStoreNode](../mdcompleteactivities/DataStoreNode.html)`, `[ExpansionNode](../mdextrastructuredactivities/ExpansionNode.html)`, `[InputPin](../../actions/mdbasicactions/InputPin.html)`, `[OutputPin](../../actions/mdbasicactions/OutputPin.html)`, `[Pin](../../actions/mdbasicactions/Pin.html)`, `[ValuePin](../../actions/mdbasicactions/ValuePin.html)`

public interfaceObjectNodeextends [ActivityNode](../mdfundamentalactivities/ActivityNode.html), [TypedElement](../../classes/mdkernel/TypedElement.html)

begin-user-doc 
 A representation of the model object '***Object Node***'.
 end-user-doc 
begin-model-doc 
 An ObjectNode is an abstract ActivityNode that may hold tokens within the object flow in an Activity. ObjectNodes also support token selection, limitation on the
 number of tokens held, specification of the state required for tokens being held, and carrying control values.
 end-model-doc 
The following features are supported:
 [`*In State*`](#getInState())
[`*Control Type*`](#isControlType())
[`*Ordering*`](#getOrdering())
[`*Selection*`](#getSelection())
[`*Upper Bound*`](#getUpperBound())
[`*exception Handler Of Exception Input*`](#get_exceptionHandlerOfExceptionInput())

See Also:
[`UMLPackage.getObjectNode()`](../../metadata/UMLPackage.html#getObjectNode())
Model:
abstract="true"
 annotation="MOF package='activities.mdbasicactivities'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ExceptionHandler](../mdextrastructuredactivities/ExceptionHandler.html)>`
`[get_exceptionHandlerOfExceptionInput](#get_exceptionHandlerOfExceptionInput())()`
Returns the value of the '***exception Handler Of Exception Input***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[State](../../statemachines/mdbehaviorstatemachines/State.html)>`
`[getInState](#getInState())()`
Returns the value of the '***In State***' reference list.
`[ObjectNodeOrderingKind](../mdcompleteactivities/ObjectNodeOrderingKind.html)`
`[getOrdering](#getOrdering())()`
Returns the value of the '***Ordering***' attribute.
`[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[getSelection](#getSelection())()`
Returns the value of the '***Selection***' reference.
`[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)`
`[getUpperBound](#getUpperBound())()`
Returns the value of the '***Upper Bound***' containment reference.
`boolean`
`[has_exceptionHandlerOfExceptionInput](#has_exceptionHandlerOfExceptionInput())()`

`boolean`
`[hasInState](#hasInState())()`

`boolean`
`[isControlType](#isControlType())()`
Returns the value of the '***Control Type***' attribute.
`void`
`[setControlType](#setControlType(boolean))(boolean value)`
Sets the value of the '[`*Control Type*`](#isControlType())' attribute.
`void`
`[setOrdering](#setOrdering(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKind))([ObjectNodeOrderingKind](../mdcompleteactivities/ObjectNodeOrderingKind.html) value)`
Sets the value of the '[`*Ordering*`](#getOrdering())' attribute.
`void`
`[setSelection](#setSelection(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)`
Sets the value of the '[`*Selection*`](#getSelection())' reference.
`void`
`[setUpperBound](#setUpperBound(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)`
Sets the value of the '[`*Upper Bound*`](#getUpperBound())' containment reference.
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityNode](../mdfundamentalactivities/ActivityNode.html)
`[get_activityNodeOfRedefinedNode](../mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()), [getActivity](../mdfundamentalactivities/ActivityNode.html#getActivity()), [getIncoming](../mdfundamentalactivities/ActivityNode.html#getIncoming()), [getInGroup](../mdfundamentalactivities/ActivityNode.html#getInGroup()), [getInInterruptibleRegion](../mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()), [getInPartition](../mdfundamentalactivities/ActivityNode.html#getInPartition()), [getInStructuredNode](../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()), [getOutgoing](../mdfundamentalactivities/ActivityNode.html#getOutgoing()), [getRedefinedNode](../mdfundamentalactivities/ActivityNode.html#getRedefinedNode()), [has_activityNodeOfRedefinedNode](../mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()), [hasIncoming](../mdfundamentalactivities/ActivityNode.html#hasIncoming()), [hasInGroup](../mdfundamentalactivities/ActivityNode.html#hasInGroup()), [hasInInterruptibleRegion](../mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()), [hasInPartition](../mdfundamentalactivities/ActivityNode.html#hasInPartition()), [hasOutgoing](../mdfundamentalactivities/ActivityNode.html#hasOutgoing()), [hasRedefinedNode](../mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()), [setActivity](../mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)), [setInStructuredNode](../mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))`
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[TypedElement](../../classes/mdkernel/TypedElement.html)
`[getType](../../classes/mdkernel/TypedElement.html#getType()), [setType](../../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))`

============ METHOD DETAIL ========== 
Method Details
get_exceptionHandlerOfExceptionInput
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ExceptionHandler](../mdextrastructuredactivities/ExceptionHandler.html)> get_exceptionHandlerOfExceptionInput()
Returns the value of the '***exception Handler Of Exception Input***' reference list.
 The list contents are of type [`ExceptionHandler`](../mdextrastructuredactivities/ExceptionHandler.html).
 It is bidirectional and its opposite is
 '[`*Exception Input*`](../mdextrastructuredactivities/ExceptionHandler.html#getExceptionInput())'.
 begin-user-doc 
If the meaning of the '*exception Handler Of Exception Input*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*exception Handler Of Exception Input*' reference list.
See Also:
[`UMLPackage.getObjectNode__exceptionHandlerOfExceptionInput()`](../../metadata/UMLPackage.html#getObjectNode__exceptionHandlerOfExceptionInput())
[`ExceptionHandler.getExceptionInput()`](../mdextrastructuredactivities/ExceptionHandler.html#getExceptionInput())
Model:
opposite="exceptionInput" ordered="false"
Generated:
getInState
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[State](../../statemachines/mdbehaviorstatemachines/State.html)> getInState()
Returns the value of the '***In State***' reference list.
 The list contents are of type [`State`](../../statemachines/mdbehaviorstatemachines/State.html).
 It is bidirectional and its opposite is
 '[`*object Node Of In State*`](../../statemachines/mdbehaviorstatemachines/State.html#get_objectNodeOfInState())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The States required to be associated with the values held by tokens on this ObjectNode.
 end-model-doc
Returns:
the value of the '*In State*' reference list.
See Also:
[`UMLPackage.getObjectNode_InState()`](../../metadata/UMLPackage.html#getObjectNode_InState())
[`State.get_objectNodeOfInState()`](../../statemachines/mdbehaviorstatemachines/State.html#get_objectNodeOfInState())
Model:
opposite="_objectNodeOfInState" ordered="false"
Generated:
isControlType
boolean isControlType()
Returns the value of the '***Control Type***' attribute.
 The default value is `"false"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates whether the type of the ObjectNode is to be treated as representing control values that may traverse ControlFlows.
 end-model-doc
Returns:
the value of the '*Control Type*' attribute.
See Also:
[`setControlType(boolean)`](#setControlType(boolean))
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getObjectNode_ControlType()`
Model:
default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"
Generated:
setControlType
void setControlType(boolean value)
Sets the value of the '[`*Control Type*`](#isControlType())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Control Type*' attribute.
See Also:
[`isControlType()`](#isControlType())
Generated:
getSelection
@CheckForNull[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) getSelection()
Returns the value of the '***Selection***' reference.
 It is bidirectional and its opposite is
 '[`*object Node Of Selection*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectNodeOfSelection())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A Behavior used to select tokens to be offered on outgoing ActivityEdges.
 end-model-doc
Returns:
the value of the '*Selection*' reference.
See Also:
[`setSelection(Behavior)`](#setSelection(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))
[`UMLPackage.getObjectNode_Selection()`](../../metadata/UMLPackage.html#getObjectNode_Selection())
[`Behavior.get_objectNodeOfSelection()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectNodeOfSelection())
Model:
opposite="_objectNodeOfSelection" ordered="false"
Generated:
setSelection
void setSelection(@CheckForNull
 [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)
Sets the value of the '[`*Selection*`](#getSelection())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Selection*' reference.
See Also:
[`getSelection()`](#getSelection())
Generated:
getOrdering
@CheckForNull[ObjectNodeOrderingKind](../mdcompleteactivities/ObjectNodeOrderingKind.html) getOrdering()
Returns the value of the '***Ordering***' attribute.
 The default value is `"FIFO"`.
 The literals are from the enumeration [`ObjectNodeOrderingKind`](../mdcompleteactivities/ObjectNodeOrderingKind.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates how the tokens held by the ObjectNode are ordered for selection to traverse ActivityEdges outgoing from the ObjectNode.
 end-model-doc
Returns:
the value of the '*Ordering*' attribute.
See Also:
[`ObjectNodeOrderingKind`](../mdcompleteactivities/ObjectNodeOrderingKind.html)
[`setOrdering(ObjectNodeOrderingKind)`](#setOrdering(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKind))
[`UMLPackage.getObjectNode_Ordering()`](../../metadata/UMLPackage.html#getObjectNode_Ordering())
Model:
default="FIFO" required="true" ordered="false"
Generated:
setOrdering
void setOrdering(@CheckForNull
 [ObjectNodeOrderingKind](../mdcompleteactivities/ObjectNodeOrderingKind.html) value)
Sets the value of the '[`*Ordering*`](#getOrdering())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Ordering*' attribute.
See Also:
[`ObjectNodeOrderingKind`](../mdcompleteactivities/ObjectNodeOrderingKind.html)
[`getOrdering()`](#getOrdering())
Generated:
getUpperBound
@CheckForNull[ValueSpecification](../../classes/mdkernel/ValueSpecification.html) getUpperBound()
Returns the value of the '***Upper Bound***' containment reference.
 It is bidirectional and its opposite is
 '[`*object Node Of Upper Bound*`](../../classes/mdkernel/ValueSpecification.html#get_objectNodeOfUpperBound())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The maximum number of tokens that may be held by this ObjectNode. Tokens cannot flow into the ObjectNode if the upperBound is reached. If no upperBound is
 specified, then there is no limit on how many tokens the ObjectNode can hold.
 end-model-doc
Returns:
the value of the '*Upper Bound*' containment reference.
See Also:
[`setUpperBound(ValueSpecification)`](#setUpperBound(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getObjectNode_UpperBound()`](../../metadata/UMLPackage.html#getObjectNode_UpperBound())
[`ValueSpecification.get_objectNodeOfUpperBound()`](../../classes/mdkernel/ValueSpecification.html#get_objectNodeOfUpperBound())
Model:
opposite="_objectNodeOfUpperBound" containment="true" resolveProxies="true" ordered="false"
Generated:
setUpperBound
void setUpperBound(@CheckForNull
 [ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)
Sets the value of the '[`*Upper Bound*`](#getUpperBound())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Upper Bound*' containment reference.
See Also:
[`getUpperBound()`](#getUpperBound())
Generated:
has_exceptionHandlerOfExceptionInput
boolean has_exceptionHandlerOfExceptionInput()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasInState
boolean hasInState()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities</a></div>
<h1 class="title" title="Interface ObjectNode">Interface ObjectNode</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../actions/mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code>, <code><a href="ActivityParameterNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityParameterNode</a></code>, <code><a href="../mdintermediateactivities/CentralBufferNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">CentralBufferNode</a></code>, <code><a href="../mdcompleteactivities/DataStoreNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">DataStoreNode</a></code>, <code><a href="../mdextrastructuredactivities/ExpansionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExpansionNode</a></code>, <code><a href="../../actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code>, <code><a href="../../actions/mdbasicactions/OutputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OutputPin</a></code>, <code><a href="../../actions/mdbasicactions/Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></code>, <code><a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ObjectNode</span><span class="extends-implements">
extends <a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a>, <a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Object Node</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An ObjectNode is an abstract ActivityNode that may hold tokens within the object flow in an Activity. ObjectNodes also support token selection, limitation on the
 number of tokens held, specification of the state required for tokens being held, and carrying control values.
 <p>
<!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getInState()"><code><em>In State</em></code></a></li>
<li><a href="#isControlType()"><code><em>Control Type</em></code></a></li>
<li><a href="#getOrdering()"><code><em>Ordering</em></code></a></li>
<li><a href="#getSelection()"><code><em>Selection</em></code></a></li>
<li><a href="#getUpperBound()"><code><em>Upper Bound</em></code></a></li>
<li><a href="#get_exceptionHandlerOfExceptionInput()"><code><em>exception Handler Of Exception Input</em></code></a></li>
</ul>
</p></p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getObjectNode()"><code>UMLPackage.getObjectNode()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='activities.mdbasicactivities'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_exceptionHandlerOfExceptionInput()">get_exceptionHandlerOfExceptionInput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>exception Handler Of Exception Input</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInState()">getInState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>In State</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactivities/ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOrdering()">getOrdering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Ordering</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSelection()">getSelection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Selection</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUpperBound()">getUpperBound</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Upper Bound</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_exceptionHandlerOfExceptionInput()">has_exceptionHandlerOfExceptionInput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasInState()">hasInState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isControlType()">isControlType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Control Type</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setControlType(boolean)">setControlType</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#isControlType()"><code><em>Control Type</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOrdering(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKind)">setOrdering</a><wbr/>(<a href="../mdcompleteactivities/ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOrdering()"><code><em>Ordering</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSelection(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setSelection</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSelection()"><code><em>Selection</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUpperBound(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setUpperBound</a><wbr/>(<a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getUpperBound()"><code><em>Upper Bound</em></code></a>' containment reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></h3>
<code><a href="../mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()">get_activityNodeOfRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getActivity()">getActivity</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getIncoming()">getIncoming</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInGroup()">getInGroup</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()">getInInterruptibleRegion</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInPartition()">getInPartition</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getInStructuredNode()">getInStructuredNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getOutgoing()">getOutgoing</a>, <a href="../mdfundamentalactivities/ActivityNode.html#getRedefinedNode()">getRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()">has_activityNodeOfRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasIncoming()">hasIncoming</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInGroup()">hasInGroup</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()">hasInInterruptibleRegion</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasInPartition()">hasInPartition</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasOutgoing()">hasOutgoing</a>, <a href="../mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()">hasRedefinedNode</a>, <a href="../mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setActivity</a>, <a href="../mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">setInStructuredNode</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="../../classes/mdkernel/RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></h3>
<code><a href="../../classes/mdkernel/TypedElement.html#getType()">getType</a>, <a href="../../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">setType</a></code></div>
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
<section class="detail" id="get_exceptionHandlerOfExceptionInput()">
<h3>get_exceptionHandlerOfExceptionInput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a>&gt;</span> <span class="element-name">get_exceptionHandlerOfExceptionInput</span>()</div>
<div class="block">Returns the value of the '<em><b>exception Handler Of Exception Input</b></em>' reference list.
 The list contents are of type <a href="../mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities"><code>ExceptionHandler</code></a>.
 It is bidirectional and its opposite is
 '<a href="../mdextrastructuredactivities/ExceptionHandler.html#getExceptionInput()"><code><em>Exception Input</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>exception Handler Of Exception Input</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>exception Handler Of Exception Input</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getObjectNode__exceptionHandlerOfExceptionInput()"><code>UMLPackage.getObjectNode__exceptionHandlerOfExceptionInput()</code></a></li>
<li><a href="../mdextrastructuredactivities/ExceptionHandler.html#getExceptionInput()"><code>ExceptionHandler.getExceptionInput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="exceptionInput" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInState()">
<h3>getInState</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a>&gt;</span> <span class="element-name">getInState</span>()</div>
<div class="block">Returns the value of the '<em><b>In State</b></em>' reference list.
 The list contents are of type <a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>State</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../statemachines/mdbehaviorstatemachines/State.html#get_objectNodeOfInState()"><code><em>object Node Of In State</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The States required to be associated with the values held by tokens on this ObjectNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>In State</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getObjectNode_InState()"><code>UMLPackage.getObjectNode_InState()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/State.html#get_objectNodeOfInState()"><code>State.get_objectNodeOfInState()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_objectNodeOfInState" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isControlType()">
<h3>isControlType</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isControlType</span>()</div>
<div class="block">Returns the value of the '<em><b>Control Type</b></em>' attribute.
 The default value is <code>"false"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates whether the type of the ObjectNode is to be treated as representing control values that may traverse ControlFlows.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Control Type</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setControlType(boolean)"><code>setControlType(boolean)</code></a></li>
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getObjectNode_ControlType()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="false" dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setControlType(boolean)">
<h3>setControlType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setControlType</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets the value of the '<a href="#isControlType()"><code><em>Control Type</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Control Type</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isControlType()"><code>isControlType()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelection()">
<h3>getSelection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">getSelection</span>()</div>
<div class="block">Returns the value of the '<em><b>Selection</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectNodeOfSelection()"><code><em>object Node Of Selection</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A Behavior used to select tokens to be offered on outgoing ActivityEdges.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Selection</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSelection(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)"><code>setSelection(Behavior)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getObjectNode_Selection()"><code>UMLPackage.getObjectNode_Selection()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_objectNodeOfSelection()"><code>Behavior.get_objectNodeOfSelection()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_objectNodeOfSelection" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSelection(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>setSelection</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSelection</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSelection()"><code><em>Selection</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Selection</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSelection()"><code>getSelection()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrdering()">
<h3>getOrdering</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactivities/ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a></span> <span class="element-name">getOrdering</span>()</div>
<div class="block">Returns the value of the '<em><b>Ordering</b></em>' attribute.
 The default value is <code>"FIFO"</code>.
 The literals are from the enumeration <a href="../mdcompleteactivities/ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ObjectNodeOrderingKind</code></a>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates how the tokens held by the ObjectNode are ordered for selection to traverse ActivityEdges outgoing from the ObjectNode.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Ordering</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../mdcompleteactivities/ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ObjectNodeOrderingKind</code></a></li>
<li><a href="#setOrdering(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKind)"><code>setOrdering(ObjectNodeOrderingKind)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getObjectNode_Ordering()"><code>UMLPackage.getObjectNode_Ordering()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="FIFO" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOrdering(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKind)">
<h3>setOrdering</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOrdering</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactivities/ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ObjectNodeOrderingKind</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOrdering()"><code><em>Ordering</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Ordering</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../mdcompleteactivities/ObjectNodeOrderingKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities"><code>ObjectNodeOrderingKind</code></a></li>
<li><a href="#getOrdering()"><code>getOrdering()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUpperBound()">
<h3>getUpperBound</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getUpperBound</span>()</div>
<div class="block">Returns the value of the '<em><b>Upper Bound</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/ValueSpecification.html#get_objectNodeOfUpperBound()"><code><em>object Node Of Upper Bound</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The maximum number of tokens that may be held by this ObjectNode. Tokens cannot flow into the ObjectNode if the upperBound is reached. If no upperBound is
 specified, then there is no limit on how many tokens the ObjectNode can hold.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Upper Bound</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setUpperBound(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setUpperBound(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getObjectNode_UpperBound()"><code>UMLPackage.getObjectNode_UpperBound()</code></a></li>
<li><a href="../../classes/mdkernel/ValueSpecification.html#get_objectNodeOfUpperBound()"><code>ValueSpecification.get_objectNodeOfUpperBound()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_objectNodeOfUpperBound" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUpperBound(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setUpperBound</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUpperBound</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getUpperBound()"><code><em>Upper Bound</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Upper Bound</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getUpperBound()"><code>getUpperBound()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_exceptionHandlerOfExceptionInput()">
<h3>has_exceptionHandlerOfExceptionInput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_exceptionHandlerOfExceptionInput</span>()
                                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasInState()">
<h3>hasInState</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasInState</span>()
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
