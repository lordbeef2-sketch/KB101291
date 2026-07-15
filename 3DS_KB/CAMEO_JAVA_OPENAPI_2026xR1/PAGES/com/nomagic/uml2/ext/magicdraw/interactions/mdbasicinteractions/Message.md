# JAVA OPENAPI: Message (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html
- source_path: `com/nomagic/uml2/ext/magicdraw/interactions/mdbasicinteractions/Message.html`
- source_sha256: `851aa9ac8834527ed33faf325c67254a4a3ee3eb8c4c209d59e4a901c07ac9f0`
- captured_utc: `2026-07-14T16:46:32.866238+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions](package-summary.html)

## Interface Message

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceMessageextends [NamedElement](../../classes/mdkernel/NamedElement.html)

begin-user-doc 
 A representation of the model object '***Message***'.
 end-user-doc 
begin-model-doc 
 A Message defines a particular communication between Lifelines of an Interaction.
 end-model-doc 
The following features are supported:
 [`*Argument*`](#getArgument())
[`*Interaction*`](#getInteraction())
[`*Message Kind*`](#getMessageKind())
[`*Message Sort*`](#getMessageSort())
[`*Receive Event*`](#getReceiveEvent())
[`*message End Of Message*`](#get_messageEndOfMessage())
[`*Send Event*`](#getSendEvent())
[`*Signature*`](#getSignature())
[`*Guard*`](#getGuard())
[`*Target*`](#getTarget())
[`*Reply Message*`](#getReplyMessage())
[`*message Of Reply Message*`](#get_messageOfReplyMessage())
[`*information Flow Of Realizing Message*`](#get_informationFlowOfRealizingMessage())
[`*Connector*`](#getConnector())

See Also:
[`UMLPackage.getMessage()`](../../metadata/UMLPackage.html#getMessage())
Model:
annotation="MOF package='interactions.mdbasicinteractions'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)>`
`[get_informationFlowOfRealizingMessage](#get_informationFlowOfRealizingMessage())()`
Returns the value of the '***information Flow Of Realizing Message***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MessageEnd](MessageEnd.html)>`
`[get_messageEndOfMessage](#get_messageEndOfMessage())()`
Returns the value of the '***message End Of Message***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Message](Message.html)>`
`[get_messageOfReplyMessage](#get_messageOfReplyMessage())()`
Returns the value of the '***message Of Reply Message***' reference list.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)>`
`[getArgument](#getArgument())()`
Returns the value of the '***Argument***' containment reference list.
`[Connector](../../compositestructures/mdinternalstructures/Connector.html)`
`[getConnector](#getConnector())()`
Returns the value of the '***Connector***' reference.
`[Constraint](../../classes/mdkernel/Constraint.html)`
`[getGuard](#getGuard())()`
Returns the value of the '***Guard***' containment reference.
`[Interaction](Interaction.html)`
`[getInteraction](#getInteraction())()`
Returns the value of the '***Interaction***' container reference.
`[MessageKind](MessageKind.html)`
`[getMessageKind](#getMessageKind())()`
Returns the value of the '***Message Kind***' attribute.
`[MessageSort](MessageSort.html)`
`[getMessageSort](#getMessageSort())()`
Returns the value of the '***Message Sort***' attribute.
`[MessageEnd](MessageEnd.html)`
`[getReceiveEvent](#getReceiveEvent())()`
Returns the value of the '***Receive Event***' reference.
`[Message](Message.html)`
`[getReplyMessage](#getReplyMessage())()`
Returns the value of the '***Reply Message***' reference.
`[MessageEnd](MessageEnd.html)`
`[getSendEvent](#getSendEvent())()`
Returns the value of the '***Send Event***' reference.
`[NamedElement](../../classes/mdkernel/NamedElement.html)`
`[getSignature](#getSignature())()`
Returns the value of the '***Signature***' reference.
`[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)`
`[getTarget](#getTarget())()`
Returns the value of the '***Target***' containment reference.
`boolean`
`[has_informationFlowOfRealizingMessage](#has_informationFlowOfRealizingMessage())()`

`boolean`
`[has_messageEndOfMessage](#has_messageEndOfMessage())()`

`boolean`
`[has_messageOfReplyMessage](#has_messageOfReplyMessage())()`

`boolean`
`[hasArgument](#hasArgument())()`

`void`
`[setConnector](#setConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector))([Connector](../../compositestructures/mdinternalstructures/Connector.html) value)`
Sets the value of the '[`*Connector*`](#getConnector())' reference.
`void`
`[setGuard](#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](../../classes/mdkernel/Constraint.html) value)`
Sets the value of the '[`*Guard*`](#getGuard())' containment reference.
`void`
`[setInteraction](#setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))([Interaction](Interaction.html) value)`
Sets the value of the '[`*Interaction*`](#getInteraction())' container reference.
`void`
`[setMessageSort](#setMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort))([MessageSort](MessageSort.html) value)`
Sets the value of the '[`*Message Sort*`](#getMessageSort())' attribute.
`void`
`[setReceiveEvent](#setReceiveEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd))([MessageEnd](MessageEnd.html) value)`
Sets the value of the '[`*Receive Event*`](#getReceiveEvent())' reference.
`void`
`[setReplyMessage](#setReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](Message.html) value)`
Sets the value of the '[`*Reply Message*`](#getReplyMessage())' reference.
`void`
`[setSendEvent](#setSendEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd))([MessageEnd](MessageEnd.html) value)`
Sets the value of the '[`*Send Event*`](#getSendEvent())' reference.
`void`
`[setSignature](#setSignature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement))([NamedElement](../../classes/mdkernel/NamedElement.html) value)`
Sets the value of the '[`*Signature*`](#getSignature())' reference.
`void`
`[setTarget](#setTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)`
Sets the value of the '[`*Target*`](#getTarget())' containment reference.
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
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getMessageKind
@CheckForNull[MessageKind](MessageKind.html) getMessageKind()
Returns the value of the '***Message Kind***' attribute.
 The literals are from the enumeration [`MessageKind`](MessageKind.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The derived kind of the Message (complete, lost, found, or unknown).
 end-model-doc
Returns:
the value of the '*Message Kind*' attribute.
See Also:
[`MessageKind`](MessageKind.html)
[`UMLPackage.getMessage_MessageKind()`](../../metadata/UMLPackage.html#getMessage_MessageKind())
Model:
required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getMessageSort
@CheckForNull[MessageSort](MessageSort.html) getMessageSort()
Returns the value of the '***Message Sort***' attribute.
 The default value is `"synchCall"`.
 The literals are from the enumeration [`MessageSort`](MessageSort.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The sort of communication reflected by the Message.
 end-model-doc
Returns:
the value of the '*Message Sort*' attribute.
See Also:
[`MessageSort`](MessageSort.html)
[`setMessageSort(MessageSort)`](#setMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort))
[`UMLPackage.getMessage_MessageSort()`](../../metadata/UMLPackage.html#getMessage_MessageSort())
Model:
default="synchCall" required="true" ordered="false"
Generated:
setMessageSort
void setMessageSort(@CheckForNull
 [MessageSort](MessageSort.html) value)
Sets the value of the '[`*Message Sort*`](#getMessageSort())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Message Sort*' attribute.
See Also:
[`MessageSort`](MessageSort.html)
[`getMessageSort()`](#getMessageSort())
Generated:
getReceiveEvent
@CheckForNull[MessageEnd](MessageEnd.html) getReceiveEvent()
Returns the value of the '***Receive Event***' reference.
 It is bidirectional and its opposite is
 '[`*message Of Receive Event*`](MessageEnd.html#get_messageOfReceiveEvent())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Receiving of the Message.
 end-model-doc
Returns:
the value of the '*Receive Event*' reference.
See Also:
[`setReceiveEvent(MessageEnd)`](#setReceiveEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd))
[`UMLPackage.getMessage_ReceiveEvent()`](../../metadata/UMLPackage.html#getMessage_ReceiveEvent())
[`MessageEnd.get_messageOfReceiveEvent()`](MessageEnd.html#get_messageOfReceiveEvent())
Model:
opposite="_messageOfReceiveEvent" ordered="false"
Generated:
setReceiveEvent
void setReceiveEvent(@CheckForNull
 [MessageEnd](MessageEnd.html) value)
Sets the value of the '[`*Receive Event*`](#getReceiveEvent())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Receive Event*' reference.
See Also:
[`getReceiveEvent()`](#getReceiveEvent())
Generated:
get_messageEndOfMessage
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[MessageEnd](MessageEnd.html)> get_messageEndOfMessage()
Returns the value of the '***message End Of Message***' reference list.
 The list contents are of type [`MessageEnd`](MessageEnd.html).
 It is bidirectional and its opposite is '[`*Message*`](MessageEnd.html#getMessage())'.
 begin-user-doc 
If the meaning of the '*message End Of Message*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*message End Of Message*' reference list.
See Also:
[`UMLPackage.getMessage__messageEndOfMessage()`](../../metadata/UMLPackage.html#getMessage__messageEndOfMessage())
[`MessageEnd.getMessage()`](MessageEnd.html#getMessage())
Model:
opposite="message" upper="2" ordered="false"
Generated:
getSendEvent
@CheckForNull[MessageEnd](MessageEnd.html) getSendEvent()
Returns the value of the '***Send Event***' reference.
 It is bidirectional and its opposite is
 '[`*message Of Send Event*`](MessageEnd.html#get_messageOfSendEvent())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Sending of the Message.
 end-model-doc
Returns:
the value of the '*Send Event*' reference.
See Also:
[`setSendEvent(MessageEnd)`](#setSendEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd))
[`UMLPackage.getMessage_SendEvent()`](../../metadata/UMLPackage.html#getMessage_SendEvent())
[`MessageEnd.get_messageOfSendEvent()`](MessageEnd.html#get_messageOfSendEvent())
Model:
opposite="_messageOfSendEvent" ordered="false"
Generated:
setSendEvent
void setSendEvent(@CheckForNull
 [MessageEnd](MessageEnd.html) value)
Sets the value of the '[`*Send Event*`](#getSendEvent())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Send Event*' reference.
See Also:
[`getSendEvent()`](#getSendEvent())
Generated:
getConnector
@CheckForNull[Connector](../../compositestructures/mdinternalstructures/Connector.html) getConnector()
Returns the value of the '***Connector***' reference.
 It is bidirectional and its opposite is
 '[`*message Of Connector*`](../../compositestructures/mdinternalstructures/Connector.html#get_messageOfConnector())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Connector on which this Message is sent.
 end-model-doc
Returns:
the value of the '*Connector*' reference.
See Also:
[`setConnector(Connector)`](#setConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector))
[`UMLPackage.getMessage_Connector()`](../../metadata/UMLPackage.html#getMessage_Connector())
[`Connector.get_messageOfConnector()`](../../compositestructures/mdinternalstructures/Connector.html#get_messageOfConnector())
Model:
opposite="_messageOfConnector" ordered="false"
Generated:
setConnector
void setConnector(@CheckForNull
 [Connector](../../compositestructures/mdinternalstructures/Connector.html) value)
Sets the value of the '[`*Connector*`](#getConnector())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Connector*' reference.
See Also:
[`getConnector()`](#getConnector())
Generated:
getArgument
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)> getArgument()
Returns the value of the '***Argument***' containment reference list.
 The list contents are of type [`ValueSpecification`](../../classes/mdkernel/ValueSpecification.html).
 It is bidirectional and its opposite is
 '[`*message Of Argument*`](../../classes/mdkernel/ValueSpecification.html#get_messageOfArgument())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The arguments of the Message.
 end-model-doc
Returns:
the value of the '*Argument*' containment reference list.
See Also:
[`UMLPackage.getMessage_Argument()`](../../metadata/UMLPackage.html#getMessage_Argument())
[`ValueSpecification.get_messageOfArgument()`](../../classes/mdkernel/ValueSpecification.html#get_messageOfArgument())
Model:
opposite="_messageOfArgument" containment="true" resolveProxies="true"
Generated:
getSignature
@CheckForNull[NamedElement](../../classes/mdkernel/NamedElement.html) getSignature()
Returns the value of the '***Signature***' reference.
 It is bidirectional and its opposite is
 '[`*message Of Signature*`](../../classes/mdkernel/NamedElement.html#get_messageOfSignature())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The signature of the Message is the specification of its content. It refers either an Operation or a Signal.
 end-model-doc
Returns:
the value of the '*Signature*' reference.
See Also:
[`setSignature(NamedElement)`](#setSignature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement))
[`UMLPackage.getMessage_Signature()`](../../metadata/UMLPackage.html#getMessage_Signature())
[`NamedElement.get_messageOfSignature()`](../../classes/mdkernel/NamedElement.html#get_messageOfSignature())
Model:
opposite="_messageOfSignature" ordered="false"
Generated:
setSignature
void setSignature(@CheckForNull
 [NamedElement](../../classes/mdkernel/NamedElement.html) value)
Sets the value of the '[`*Signature*`](#getSignature())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Signature*' reference.
See Also:
[`getSignature()`](#getSignature())
Generated:
get_informationFlowOfRealizingMessage
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[InformationFlow](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html)> get_informationFlowOfRealizingMessage()
Returns the value of the '***information Flow Of Realizing Message***' reference list.
 The list contents are of type [`InformationFlow`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html).
 It is bidirectional and its opposite is
 '[`*Realizing Message*`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingMessage())'.
 begin-user-doc 
If the meaning of the '*information Flow Of Realizing Message*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*information Flow Of Realizing Message*' reference list.
See Also:
[`UMLPackage.getMessage__informationFlowOfRealizingMessage()`](../../metadata/UMLPackage.html#getMessage__informationFlowOfRealizingMessage())
[`InformationFlow.getRealizingMessage()`](../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingMessage())
Model:
opposite="realizingMessage" ordered="false"
Generated:
getReplyMessage
@CheckForNull[Message](Message.html) getReplyMessage()
Returns the value of the '***Reply Message***' reference.
 It is bidirectional and its opposite is
 '[`*message Of Reply Message*`](#get_messageOfReplyMessage())'.
 begin-user-doc 
If the meaning of the '*Reply Message*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Reply Message*' reference.
See Also:
[`setReplyMessage(Message)`](#setReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))
[`UMLPackage.getMessage_ReplyMessage()`](../../metadata/UMLPackage.html#getMessage_ReplyMessage())
[`get_messageOfReplyMessage()`](#get_messageOfReplyMessage())
Model:
opposite="_messageOfReplyMessage" ordered="false"
Generated:
setReplyMessage
void setReplyMessage(@CheckForNull
 [Message](Message.html) value)
Sets the value of the '[`*Reply Message*`](#getReplyMessage())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Reply Message*' reference.
See Also:
[`getReplyMessage()`](#getReplyMessage())
Generated:
get_messageOfReplyMessage
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Message](Message.html)> get_messageOfReplyMessage()
Returns the value of the '***message Of Reply Message***' reference list.
 The list contents are of type [`Message`](Message.html).
 It is bidirectional and its opposite is '[`*Reply Message*`](#getReplyMessage())'.
 begin-user-doc 
If the meaning of the '*message Of Reply Message*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*message Of Reply Message*' reference list.
See Also:
[`UMLPackage.getMessage__messageOfReplyMessage()`](../../metadata/UMLPackage.html#getMessage__messageOfReplyMessage())
[`getReplyMessage()`](#getReplyMessage())
Model:
opposite="replyMessage" ordered="false"
Generated:
getGuard
@CheckForNull[Constraint](../../classes/mdkernel/Constraint.html) getGuard()
Returns the value of the '***Guard***' containment reference.
 It is bidirectional and its opposite is '[`*message Of Guard*`](../../classes/mdkernel/Constraint.html#get_messageOfGuard())'.
 begin-user-doc 
If the meaning of the '*Guard*' containment reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Guard*' containment reference.
See Also:
[`setGuard(Constraint)`](#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))
[`UMLPackage.getMessage_Guard()`](../../metadata/UMLPackage.html#getMessage_Guard())
[`Constraint.get_messageOfGuard()`](../../classes/mdkernel/Constraint.html#get_messageOfGuard())
Model:
opposite="_messageOfGuard" containment="true" resolveProxies="true" ordered="false"
Generated:
setGuard
void setGuard(@CheckForNull
 [Constraint](../../classes/mdkernel/Constraint.html) value)
Sets the value of the '[`*Guard*`](#getGuard())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Guard*' containment reference.
See Also:
[`getGuard()`](#getGuard())
Generated:
getTarget
@CheckForNull[ValueSpecification](../../classes/mdkernel/ValueSpecification.html) getTarget()
Returns the value of the '***Target***' containment reference.
 It is bidirectional and its opposite is
 '[`*message Of Target*`](../../classes/mdkernel/ValueSpecification.html#get_messageOfTarget())'.
 begin-user-doc 
If the meaning of the '*Target*' containment reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Target*' containment reference.
See Also:
[`setTarget(ValueSpecification)`](#setTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getMessage_Target()`](../../metadata/UMLPackage.html#getMessage_Target())
[`ValueSpecification.get_messageOfTarget()`](../../classes/mdkernel/ValueSpecification.html#get_messageOfTarget())
Model:
opposite="_messageOfTarget" containment="true" resolveProxies="true" ordered="false"
Generated:
setTarget
void setTarget(@CheckForNull
 [ValueSpecification](../../classes/mdkernel/ValueSpecification.html) value)
Sets the value of the '[`*Target*`](#getTarget())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Target*' containment reference.
See Also:
[`getTarget()`](#getTarget())
Generated:
getInteraction
@CheckForNull[Interaction](Interaction.html) getInteraction()
Returns the value of the '***Interaction***' container reference.
 It is bidirectional and its opposite is '[`*Message*`](Interaction.html#getMessage())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The enclosing Interaction owning the Message.
 end-model-doc
Returns:
the value of the '*Interaction*' container reference.
See Also:
[`setInteraction(Interaction)`](#setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction))
[`UMLPackage.getMessage_Interaction()`](../../metadata/UMLPackage.html#getMessage_Interaction())
[`Interaction.getMessage()`](Interaction.html#getMessage())
Model:
opposite="message" required="true" transient="false" ordered="false"
Generated:
setInteraction
void setInteraction(@CheckForNull
 [Interaction](Interaction.html) value)
Sets the value of the '[`*Interaction*`](#getInteraction())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Interaction*' container reference.
See Also:
[`getInteraction()`](#getInteraction())
Generated:
has_messageEndOfMessage
boolean has_messageEndOfMessage()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasArgument
boolean hasArgument()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_messageOfReplyMessage
boolean has_messageOfReplyMessage()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_informationFlowOfRealizingMessage
boolean has_informationFlowOfRealizingMessage()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions</a></div>
<h1 class="title" title="Interface Message">Interface Message</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Message</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Message</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Message defines a particular communication between Lifelines of an Interaction.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getArgument()"><code><em>Argument</em></code></a></li>
<li><a href="#getInteraction()"><code><em>Interaction</em></code></a></li>
<li><a href="#getMessageKind()"><code><em>Message Kind</em></code></a></li>
<li><a href="#getMessageSort()"><code><em>Message Sort</em></code></a></li>
<li><a href="#getReceiveEvent()"><code><em>Receive Event</em></code></a></li>
<li><a href="#get_messageEndOfMessage()"><code><em>message End Of Message</em></code></a></li>
<li><a href="#getSendEvent()"><code><em>Send Event</em></code></a></li>
<li><a href="#getSignature()"><code><em>Signature</em></code></a></li>
<li><a href="#getGuard()"><code><em>Guard</em></code></a></li>
<li><a href="#getTarget()"><code><em>Target</em></code></a></li>
<li><a href="#getReplyMessage()"><code><em>Reply Message</em></code></a></li>
<li><a href="#get_messageOfReplyMessage()"><code><em>message Of Reply Message</em></code></a></li>
<li><a href="#get_informationFlowOfRealizingMessage()"><code><em>information Flow Of Realizing Message</em></code></a></li>
<li><a href="#getConnector()"><code><em>Connector</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getMessage()"><code>UMLPackage.getMessage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='interactions.mdbasicinteractions'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_informationFlowOfRealizingMessage()">get_informationFlowOfRealizingMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>information Flow Of Realizing Message</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_messageEndOfMessage()">get_messageEndOfMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>message End Of Message</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_messageOfReplyMessage()">get_messageOfReplyMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>message Of Reply Message</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getArgument()">getArgument</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Argument</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConnector()">getConnector</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Connector</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGuard()">getGuard</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Guard</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInteraction()">getInteraction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Interaction</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MessageKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMessageKind()">getMessageKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Message Kind</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMessageSort()">getMessageSort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Message Sort</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getReceiveEvent()">getReceiveEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Receive Event</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getReplyMessage()">getReplyMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Reply Message</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSendEvent()">getSendEvent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Send Event</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSignature()">getSignature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Signature</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTarget()">getTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Target</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_informationFlowOfRealizingMessage()">has_informationFlowOfRealizingMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_messageEndOfMessage()">has_messageEndOfMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_messageOfReplyMessage()">has_messageOfReplyMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasArgument()">hasArgument</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)">setConnector</a><wbr/>(<a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getConnector()"><code><em>Connector</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setGuard</a><wbr/>(<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getGuard()"><code><em>Guard</em></code></a>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">setInteraction</a><wbr/>(<a href="Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getInteraction()"><code><em>Interaction</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort)">setMessageSort</a><wbr/>(<a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getMessageSort()"><code><em>Message Sort</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setReceiveEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd)">setReceiveEvent</a><wbr/>(<a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getReceiveEvent()"><code><em>Receive Event</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">setReplyMessage</a><wbr/>(<a href="Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getReplyMessage()"><code><em>Reply Message</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSendEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd)">setSendEvent</a><wbr/>(<a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSendEvent()"><code><em>Send Event</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSignature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">setSignature</a><wbr/>(<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSignature()"><code><em>Signature</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setTarget</a><wbr/>(<a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getTarget()"><code><em>Target</em></code></a>' containment reference.</div>
</div>
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
<section class="detail" id="getMessageKind()">
<h3>getMessageKind</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="MessageKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageKind</a></span> <span class="element-name">getMessageKind</span>()</div>
<div class="block">Returns the value of the '<em><b>Message Kind</b></em>' attribute.
 The literals are from the enumeration <a href="MessageKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageKind</code></a>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The derived kind of the Message (complete, lost, found, or unknown).
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Message Kind</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="MessageKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageKind</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_MessageKind()"><code>UMLPackage.getMessage_MessageKind()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessageSort()">
<h3>getMessageSort</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a></span> <span class="element-name">getMessageSort</span>()</div>
<div class="block">Returns the value of the '<em><b>Message Sort</b></em>' attribute.
 The default value is <code>"synchCall"</code>.
 The literals are from the enumeration <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageSort</code></a>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The sort of communication reflected by the Message.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Message Sort</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageSort</code></a></li>
<li><a href="#setMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort)"><code>setMessageSort(MessageSort)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_MessageSort()"><code>UMLPackage.getMessage_MessageSort()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="synchCall" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMessageSort(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageSort)">
<h3>setMessageSort</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMessageSort</span><wbr/><span class="parameters">(@CheckForNull
 <a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageSort</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getMessageSort()"><code><em>Message Sort</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Message Sort</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="MessageSort.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageSort</code></a></li>
<li><a href="#getMessageSort()"><code>getMessageSort()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReceiveEvent()">
<h3>getReceiveEvent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></span> <span class="element-name">getReceiveEvent</span>()</div>
<div class="block">Returns the value of the '<em><b>Receive Event</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="MessageEnd.html#get_messageOfReceiveEvent()"><code><em>message Of Receive Event</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Receiving of the Message.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Receive Event</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setReceiveEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd)"><code>setReceiveEvent(MessageEnd)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_ReceiveEvent()"><code>UMLPackage.getMessage_ReceiveEvent()</code></a></li>
<li><a href="MessageEnd.html#get_messageOfReceiveEvent()"><code>MessageEnd.get_messageOfReceiveEvent()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_messageOfReceiveEvent" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReceiveEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd)">
<h3>setReceiveEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setReceiveEvent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getReceiveEvent()"><code><em>Receive Event</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Receive Event</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getReceiveEvent()"><code>getReceiveEvent()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_messageEndOfMessage()">
<h3>get_messageEndOfMessage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a>&gt;</span> <span class="element-name">get_messageEndOfMessage</span>()</div>
<div class="block">Returns the value of the '<em><b>message End Of Message</b></em>' reference list.
 The list contents are of type <a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>MessageEnd</code></a>.
 It is bidirectional and its opposite is '<a href="MessageEnd.html#getMessage()"><code><em>Message</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>message End Of Message</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>message End Of Message</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getMessage__messageEndOfMessage()"><code>UMLPackage.getMessage__messageEndOfMessage()</code></a></li>
<li><a href="MessageEnd.html#getMessage()"><code>MessageEnd.getMessage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="message" upper="2" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSendEvent()">
<h3>getSendEvent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a></span> <span class="element-name">getSendEvent</span>()</div>
<div class="block">Returns the value of the '<em><b>Send Event</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="MessageEnd.html#get_messageOfSendEvent()"><code><em>message Of Send Event</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Sending of the Message.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Send Event</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSendEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd)"><code>setSendEvent(MessageEnd)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_SendEvent()"><code>UMLPackage.getMessage_SendEvent()</code></a></li>
<li><a href="MessageEnd.html#get_messageOfSendEvent()"><code>MessageEnd.get_messageOfSendEvent()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_messageOfSendEvent" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSendEvent(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.MessageEnd)">
<h3>setSendEvent</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSendEvent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="MessageEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">MessageEnd</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSendEvent()"><code><em>Send Event</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Send Event</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSendEvent()"><code>getSendEvent()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnector()">
<h3>getConnector</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a></span> <span class="element-name">getConnector</span>()</div>
<div class="block">Returns the value of the '<em><b>Connector</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../compositestructures/mdinternalstructures/Connector.html#get_messageOfConnector()"><code><em>message Of Connector</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Connector on which this Message is sent.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Connector</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)"><code>setConnector(Connector)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_Connector()"><code>UMLPackage.getMessage_Connector()</code></a></li>
<li><a href="../../compositestructures/mdinternalstructures/Connector.html#get_messageOfConnector()"><code>Connector.get_messageOfConnector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_messageOfConnector" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConnector(com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures.Connector)">
<h3>setConnector</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setConnector</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../compositestructures/mdinternalstructures/Connector.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">Connector</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getConnector()"><code><em>Connector</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Connector</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getConnector()"><code>getConnector()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getArgument()">
<h3>getArgument</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a>&gt;</span> <span class="element-name">getArgument</span>()</div>
<div class="block">Returns the value of the '<em><b>Argument</b></em>' containment reference list.
 The list contents are of type <a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/ValueSpecification.html#get_messageOfArgument()"><code><em>message Of Argument</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The arguments of the Message.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Argument</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getMessage_Argument()"><code>UMLPackage.getMessage_Argument()</code></a></li>
<li><a href="../../classes/mdkernel/ValueSpecification.html#get_messageOfArgument()"><code>ValueSpecification.get_messageOfArgument()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_messageOfArgument" containment="true" resolveProxies="true"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignature()">
<h3>getSignature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></span> <span class="element-name">getSignature</span>()</div>
<div class="block">Returns the value of the '<em><b>Signature</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()"><code><em>message Of Signature</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The signature of the Message is the specification of its content. It refers either an Operation or a Signal.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Signature</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSignature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)"><code>setSignature(NamedElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_Signature()"><code>UMLPackage.getMessage_Signature()</code></a></li>
<li><a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()"><code>NamedElement.get_messageOfSignature()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_messageOfSignature" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSignature(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement)">
<h3>setSignature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSignature</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSignature()"><code><em>Signature</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Signature</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSignature()"><code>getSignature()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_informationFlowOfRealizingMessage()">
<h3>get_informationFlowOfRealizingMessage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a>&gt;</span> <span class="element-name">get_informationFlowOfRealizingMessage</span>()</div>
<div class="block">Returns the value of the '<em><b>information Flow Of Realizing Message</b></em>' reference list.
 The list contents are of type <a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows"><code>InformationFlow</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingMessage()"><code><em>Realizing Message</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>information Flow Of Realizing Message</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>information Flow Of Realizing Message</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getMessage__informationFlowOfRealizingMessage()"><code>UMLPackage.getMessage__informationFlowOfRealizingMessage()</code></a></li>
<li><a href="../../auxiliaryconstructs/mdinformationflows/InformationFlow.html#getRealizingMessage()"><code>InformationFlow.getRealizingMessage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="realizingMessage" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReplyMessage()">
<h3>getReplyMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">getReplyMessage</span>()</div>
<div class="block">Returns the value of the '<em><b>Reply Message</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="#get_messageOfReplyMessage()"><code><em>message Of Reply Message</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Reply Message</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Reply Message</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)"><code>setReplyMessage(Message)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_ReplyMessage()"><code>UMLPackage.getMessage_ReplyMessage()</code></a></li>
<li><a href="#get_messageOfReplyMessage()"><code>get_messageOfReplyMessage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_messageOfReplyMessage" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReplyMessage(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>setReplyMessage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setReplyMessage</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getReplyMessage()"><code><em>Reply Message</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Reply Message</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getReplyMessage()"><code>getReplyMessage()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_messageOfReplyMessage()">
<h3>get_messageOfReplyMessage</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a>&gt;</span> <span class="element-name">get_messageOfReplyMessage</span>()</div>
<div class="block">Returns the value of the '<em><b>message Of Reply Message</b></em>' reference list.
 The list contents are of type <a href="Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions"><code>Message</code></a>.
 It is bidirectional and its opposite is '<a href="#getReplyMessage()"><code><em>Reply Message</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>message Of Reply Message</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>message Of Reply Message</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getMessage__messageOfReplyMessage()"><code>UMLPackage.getMessage__messageOfReplyMessage()</code></a></li>
<li><a href="#getReplyMessage()"><code>getReplyMessage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="replyMessage" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGuard()">
<h3>getGuard</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getGuard</span>()</div>
<div class="block">Returns the value of the '<em><b>Guard</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="../../classes/mdkernel/Constraint.html#get_messageOfGuard()"><code><em>message Of Guard</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Guard</em>' containment reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Guard</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)"><code>setGuard(Constraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_Guard()"><code>UMLPackage.getMessage_Guard()</code></a></li>
<li><a href="../../classes/mdkernel/Constraint.html#get_messageOfGuard()"><code>Constraint.get_messageOfGuard()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_messageOfGuard" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>setGuard</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setGuard</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getGuard()"><code><em>Guard</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Guard</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getGuard()"><code>getGuard()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTarget()">
<h3>getTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>Target</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../classes/mdkernel/ValueSpecification.html#get_messageOfTarget()"><code><em>message Of Target</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Target</em>' containment reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Target</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setTarget(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_Target()"><code>UMLPackage.getMessage_Target()</code></a></li>
<li><a href="../../classes/mdkernel/ValueSpecification.html#get_messageOfTarget()"><code>ValueSpecification.get_messageOfTarget()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_messageOfTarget" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getTarget()"><code><em>Target</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Target</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getTarget()"><code>getTarget()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInteraction()">
<h3>getInteraction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></span> <span class="element-name">getInteraction</span>()</div>
<div class="block">Returns the value of the '<em><b>Interaction</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Interaction.html#getMessage()"><code><em>Message</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The enclosing Interaction owning the Message.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Interaction</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)"><code>setInteraction(Interaction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getMessage_Interaction()"><code>UMLPackage.getMessage_Interaction()</code></a></li>
<li><a href="Interaction.html#getMessage()"><code>Interaction.getMessage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="message" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInteraction(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Interaction)">
<h3>setInteraction</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setInteraction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getInteraction()"><code><em>Interaction</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Interaction</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getInteraction()"><code>getInteraction()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_messageEndOfMessage()">
<h3>has_messageEndOfMessage</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_messageEndOfMessage</span>()
                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasArgument()">
<h3>hasArgument</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasArgument</span>()
             throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_messageOfReplyMessage()">
<h3>has_messageOfReplyMessage</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_messageOfReplyMessage</span>()
                           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_informationFlowOfRealizingMessage()">
<h3>has_informationFlowOfRealizingMessage</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_informationFlowOfRealizingMessage</span>()
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
