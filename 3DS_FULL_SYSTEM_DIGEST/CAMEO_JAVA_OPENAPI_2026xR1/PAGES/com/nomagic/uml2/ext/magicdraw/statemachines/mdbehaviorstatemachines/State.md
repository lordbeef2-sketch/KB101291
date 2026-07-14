# JAVA OPENAPI: State (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html
- source_path: `com/nomagic/uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html`
- source_sha256: `9ff7e4510490a35c44b57dc2aa1f1a5d57f38c616f057deefcb80df6dd88903f`
- captured_utc: `2026-07-14T16:46:34.047252+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines](package-summary.html)

## Interface State

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[Vertex](Vertex.html)`

All Known Subinterfaces:
`[FinalState](FinalState.html)`

public interfaceStateextends [Namespace](../../classes/mdkernel/Namespace.html), [Vertex](Vertex.html)

begin-user-doc 
 A representation of the model object '***State***'.
 end-user-doc 
begin-model-doc 
 A State models a situation during which some (usually implicit) invariant condition holds.
 end-model-doc 
The following features are supported:
 [`*Region*`](#getRegion())
[`*Connection Point*`](#getConnectionPoint())
[`*Connection*`](#getConnection())
[`*Submachine*`](#getSubmachine())
[`*State Invariant*`](#getStateInvariant())
[`*Deferrable Trigger*`](#getDeferrableTrigger())
[`*Do Activity*`](#getDoActivity())
[`*Entry*`](#getEntry())
[`*Exit*`](#getExit())
[`*Composite*`](#isComposite())
[`*Orthogonal*`](#isOrthogonal())
[`*Simple*`](#isSimple())
[`*Submachine State*`](#isSubmachineState())
[`*object Node Of In State*`](#get_objectNodeOfInState())

See Also:
[`UMLPackage.getState()`](../../metadata/UMLPackage.html#getState())
Model:
annotation="MOF package='statemachines.mdbehaviorstatemachines'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)>`
`[get_objectNodeOfInState](#get_objectNodeOfInState())()`
Returns the value of the '***object Node Of In State***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ConnectionPointReference](ConnectionPointReference.html)>`
`[getConnection](#getConnection())()`
Returns the value of the '***Connection***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Pseudostate](Pseudostate.html)>`
`[getConnectionPoint](#getConnectionPoint())()`
Returns the value of the '***Connection Point***' containment reference list.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Trigger](../../commonbehaviors/mdcommunications/Trigger.html)>`
`[getDeferrableTrigger](#getDeferrableTrigger())()`
Returns the value of the '***Deferrable Trigger***' containment reference list.
`[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[getDoActivity](#getDoActivity())()`
Returns the value of the '***Do Activity***' containment reference.
`[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[getEntry](#getEntry())()`
Returns the value of the '***Entry***' containment reference.
`[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[getExit](#getExit())()`
Returns the value of the '***Exit***' containment reference.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Region](Region.html)>`
`[getRegion](#getRegion())()`
Returns the value of the '***Region***' containment reference list.
`[Constraint](../../classes/mdkernel/Constraint.html)`
`[getStateInvariant](#getStateInvariant())()`
Returns the value of the '***State Invariant***' reference.
`[StateMachine](StateMachine.html)`
`[getSubmachine](#getSubmachine())()`
Returns the value of the '***Submachine***' reference.
`boolean`
`[has_objectNodeOfInState](#has_objectNodeOfInState())()`

`boolean`
`[hasConnection](#hasConnection())()`

`boolean`
`[hasConnectionPoint](#hasConnectionPoint())()`

`boolean`
`[hasDeferrableTrigger](#hasDeferrableTrigger())()`

`boolean`
`[hasRegion](#hasRegion())()`

`boolean`
`[isComposite](#isComposite())()`
Returns the value of the '***Composite***' attribute.
`boolean`
`[isOrthogonal](#isOrthogonal())()`
Returns the value of the '***Orthogonal***' attribute.
`boolean`
`[isSimple](#isSimple())()`
Returns the value of the '***Simple***' attribute.
`boolean`
`[isSubmachineState](#isSubmachineState())()`
Returns the value of the '***Submachine State***' attribute.
`void`
`[setDoActivity](#setDoActivity(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)`
Sets the value of the '[`*Do Activity*`](#getDoActivity())' containment
 reference.
`void`
`[setEntry](#setEntry(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)`
Sets the value of the '[`*Entry*`](#getEntry())' containment reference.
`void`
`[setExit](#setExit(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)`
Sets the value of the '[`*Exit*`](#getExit())' containment reference.
`void`
`[setStateInvariant](#setStateInvariant(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](../../classes/mdkernel/Constraint.html) value)`
Sets the value of the '[`*State Invariant*`](#getStateInvariant())' reference.
`void`
`[setSubmachine](#setSubmachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine))([StateMachine](StateMachine.html) value)`
Sets the value of the '[`*Submachine*`](#getSubmachine())' reference.
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Namespace](../../classes/mdkernel/Namespace.html)
`[getElementImport](../../classes/mdkernel/Namespace.html#getElementImport()), [getImportedMember](../../classes/mdkernel/Namespace.html#getImportedMember()), [getMember](../../classes/mdkernel/Namespace.html#getMember()), [getOwnedDiagram](../../classes/mdkernel/Namespace.html#getOwnedDiagram()), [getOwnedMember](../../classes/mdkernel/Namespace.html#getOwnedMember()), [getOwnedRule](../../classes/mdkernel/Namespace.html#getOwnedRule()), [getPackageImport](../../classes/mdkernel/Namespace.html#getPackageImport()), [hasElementImport](../../classes/mdkernel/Namespace.html#hasElementImport()), [hasImportedMember](../../classes/mdkernel/Namespace.html#hasImportedMember()), [hasMember](../../classes/mdkernel/Namespace.html#hasMember()), [hasOwnedDiagram](../../classes/mdkernel/Namespace.html#hasOwnedDiagram()), [hasOwnedMember](../../classes/mdkernel/Namespace.html#hasOwnedMember()), [hasOwnedRule](../../classes/mdkernel/Namespace.html#hasOwnedRule()), [hasPackageImport](../../classes/mdkernel/Namespace.html#hasPackageImport())`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [has_redefinableElementOfRedefinedElement](../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.[Vertex](Vertex.html)
`[get_vertexOfRedefinedVertex](Vertex.html#get_vertexOfRedefinedVertex()), [getContainer](Vertex.html#getContainer()), [getIncoming](Vertex.html#getIncoming()), [getOutgoing](Vertex.html#getOutgoing()), [getRedefinedVertex](Vertex.html#getRedefinedVertex()), [getRedefinitionContext](Vertex.html#getRedefinitionContext()), [hasIncoming](Vertex.html#hasIncoming()), [hasOutgoing](Vertex.html#hasOutgoing()), [setContainer](Vertex.html#setContainer(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)), [setRedefinedVertex](Vertex.html#setRedefinedVertex(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex))`

============ METHOD DETAIL ========== 
Method Details
getSubmachine
@CheckForNull[StateMachine](StateMachine.html) getSubmachine()
Returns the value of the '***Submachine***' reference.
 It is bidirectional and its opposite is
 '[`*Submachine State*`](StateMachine.html#getSubmachineState())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The StateMachine that is to be inserted in place of the (submachine) State.
 end-model-doc
Returns:
the value of the '*Submachine*' reference.
See Also:
[`setSubmachine(StateMachine)`](#setSubmachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine))
[`UMLPackage.getState_Submachine()`](../../metadata/UMLPackage.html#getState_Submachine())
[`StateMachine.getSubmachineState()`](StateMachine.html#getSubmachineState())
Model:
opposite="submachineState" ordered="false"
Generated:
setSubmachine
void setSubmachine(@CheckForNull
 [StateMachine](StateMachine.html) value)
Sets the value of the '[`*Submachine*`](#getSubmachine())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Submachine*' reference.
See Also:
[`getSubmachine()`](#getSubmachine())
Generated:
getConnection
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ConnectionPointReference](ConnectionPointReference.html)> getConnection()
Returns the value of the '***Connection***' containment reference list.
 The list contents are of type [`ConnectionPointReference`](ConnectionPointReference.html).
 It is bidirectional and its opposite is
 '[`*State*`](ConnectionPointReference.html#getState())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The entry and exit connection points used in conjunction with this (submachine) State, i.e., as targets and sources, respectively, in the Region with the
 submachine State. A connection point reference references the corresponding definition of a connection point Pseudostate in the StateMachine referenced by the
 submachine State.
 end-model-doc
Returns:
the value of the '*Connection*' containment reference list.
See Also:
[`UMLPackage.getState_Connection()`](../../metadata/UMLPackage.html#getState_Connection())
[`ConnectionPointReference.getState()`](ConnectionPointReference.html#getState())
Model:
opposite="state" containment="true" resolveProxies="true" ordered="false"
Generated:
getRegion
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Region](Region.html)> getRegion()
Returns the value of the '***Region***' containment reference list.
 The list contents are of type [`Region`](Region.html).
 It is bidirectional and its opposite is '[`*State*`](Region.html#getState())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Regions owned directly by the State.
 end-model-doc
Returns:
the value of the '*Region*' containment reference list.
See Also:
[`UMLPackage.getState_Region()`](../../metadata/UMLPackage.html#getState_Region())
[`Region.getState()`](Region.html#getState())
Model:
opposite="state" containment="true" resolveProxies="true" ordered="false"
Generated:
getStateInvariant
@CheckForNull[Constraint](../../classes/mdkernel/Constraint.html) getStateInvariant()
Returns the value of the '***State Invariant***' reference.
 It is bidirectional and its opposite is '[`*Owning State*`](../../classes/mdkernel/Constraint.html#getOwningState())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies conditions that are always true when this State is the current State. In ProtocolStateMachines state invariants are additional conditions to the
 preconditions of the outgoing Transitions, and to the postcondition of the incoming Transitions.
 end-model-doc
Returns:
the value of the '*State Invariant*' reference.
See Also:
[`setStateInvariant(Constraint)`](#setStateInvariant(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))
[`UMLPackage.getState_StateInvariant()`](../../metadata/UMLPackage.html#getState_StateInvariant())
[`Constraint.getOwningState()`](../../classes/mdkernel/Constraint.html#getOwningState())
Model:
opposite="owningState" ordered="false"
Generated:
setStateInvariant
void setStateInvariant(@CheckForNull
 [Constraint](../../classes/mdkernel/Constraint.html) value)
Sets the value of the '[`*State Invariant*`](#getStateInvariant())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*State Invariant*' reference.
See Also:
[`getStateInvariant()`](#getStateInvariant())
Generated:
getEntry
@CheckForNull[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) getEntry()
Returns the value of the '***Entry***' containment reference.
 It is bidirectional and its opposite is
 '[`*state Of Entry*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfEntry())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional Behavior that is executed whenever this State is entered regardless of the Transition taken to reach the State. If defined, entry Behaviors are
 always executed to completion prior to any internal Behavior or Transitions performed within the State.
 end-model-doc
Returns:
the value of the '*Entry*' containment reference.
See Also:
[`setEntry(Behavior)`](#setEntry(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))
[`UMLPackage.getState_Entry()`](../../metadata/UMLPackage.html#getState_Entry())
[`Behavior.get_stateOfEntry()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfEntry())
Model:
opposite="_stateOfEntry" containment="true" resolveProxies="true" ordered="false"
Generated:
setEntry
void setEntry(@CheckForNull
 [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)
Sets the value of the '[`*Entry*`](#getEntry())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Entry*' containment reference.
See Also:
[`getEntry()`](#getEntry())
Generated:
getExit
@CheckForNull[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) getExit()
Returns the value of the '***Exit***' containment reference.
 It is bidirectional and its opposite is '[`*state Of Exit*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfExit())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional Behavior that is executed whenever this State is exited regardless of which Transition was taken out of the State. If defined, exit Behaviors are
 always executed to completion only after all internal and transition Behaviors have completed execution.
 end-model-doc
Returns:
the value of the '*Exit*' containment reference.
See Also:
[`setExit(Behavior)`](#setExit(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))
[`UMLPackage.getState_Exit()`](../../metadata/UMLPackage.html#getState_Exit())
[`Behavior.get_stateOfExit()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfExit())
Model:
opposite="_stateOfExit" containment="true" resolveProxies="true" ordered="false"
Generated:
setExit
void setExit(@CheckForNull
 [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)
Sets the value of the '[`*Exit*`](#getExit())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Exit*' containment reference.
See Also:
[`getExit()`](#getExit())
Generated:
isComposite
boolean isComposite()
Returns the value of the '***Composite***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A state with isComposite=true is said to be a composite State. A composite State is a State that contains at least one Region.
 end-model-doc
Returns:
the value of the '*Composite*' attribute.
See Also:
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getState_Composite()`
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
isOrthogonal
boolean isOrthogonal()
Returns the value of the '***Orthogonal***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A State with isOrthogonal=true is said to be an orthogonal composite State An orthogonal composite State contains two or more Regions.
 end-model-doc
Returns:
the value of the '*Orthogonal*' attribute.
See Also:
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getState_Orthogonal()`
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
isSimple
boolean isSimple()
Returns the value of the '***Simple***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A State with isSimple=true is said to be a simple State A simple State does not have any Regions and it does not refer to any submachine StateMachine.
 end-model-doc
Returns:
the value of the '*Simple*' attribute.
See Also:
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getState_Simple()`
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
isSubmachineState
boolean isSubmachineState()
Returns the value of the '***Submachine State***' attribute.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A State with isSubmachineState=true is said to be a submachine State Such a State refers to another StateMachine(submachine).
 end-model-doc
Returns:
the value of the '*Submachine State*' attribute.
See Also:
invalid reference
`com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getState_SubmachineState()`
Model:
dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
getDoActivity
@CheckForNull[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) getDoActivity()
Returns the value of the '***Do Activity***' containment reference.
 It is bidirectional and its opposite is
 '[`*state Of Do Activity*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfDoActivity())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 An optional Behavior that is executed while being in the State. The execution starts when this State is entered, and ceases either by itself when done, or when
 the State is exited, whichever comes first.
 end-model-doc
Returns:
the value of the '*Do Activity*' containment reference.
See Also:
[`setDoActivity(Behavior)`](#setDoActivity(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))
[`UMLPackage.getState_DoActivity()`](../../metadata/UMLPackage.html#getState_DoActivity())
[`Behavior.get_stateOfDoActivity()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfDoActivity())
Model:
opposite="_stateOfDoActivity" containment="true" resolveProxies="true" ordered="false"
Generated:
setDoActivity
void setDoActivity(@CheckForNull
 [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)
Sets the value of the '[`*Do Activity*`](#getDoActivity())' containment
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Do Activity*' containment reference.
See Also:
[`getDoActivity()`](#getDoActivity())
Generated:
getDeferrableTrigger
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Trigger](../../commonbehaviors/mdcommunications/Trigger.html)> getDeferrableTrigger()
Returns the value of the '***Deferrable Trigger***' containment reference list.
 The list contents are of type [`Trigger`](../../commonbehaviors/mdcommunications/Trigger.html).
 It is bidirectional and its opposite is
 '[`*state Of Deferrable Trigger*`](../../commonbehaviors/mdcommunications/Trigger.html#get_stateOfDeferrableTrigger())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A list of Triggers that are candidates to be retained by the StateMachine if they trigger no Transitions out of the State (not consumed). A deferred Trigger is
 retained until the StateMachine reaches a State configuration where it is no longer deferred.
 end-model-doc
Returns:
the value of the '*Deferrable Trigger*' containment reference list.
See Also:
[`UMLPackage.getState_DeferrableTrigger()`](../../metadata/UMLPackage.html#getState_DeferrableTrigger())
[`Trigger.get_stateOfDeferrableTrigger()`](../../commonbehaviors/mdcommunications/Trigger.html#get_stateOfDeferrableTrigger())
Model:
opposite="_stateOfDeferrableTrigger" containment="true" resolveProxies="true" ordered="false"
Generated:
get_objectNodeOfInState
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)> get_objectNodeOfInState()
Returns the value of the '***object Node Of In State***' reference list.
 The list contents are of type [`ObjectNode`](../../activities/mdbasicactivities/ObjectNode.html).
 It is bidirectional and its opposite is '[`*In State*`](../../activities/mdbasicactivities/ObjectNode.html#getInState())'.
 begin-user-doc 
If the meaning of the '*object Node Of In State*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*object Node Of In State*' reference list.
See Also:
[`UMLPackage.getState__objectNodeOfInState()`](../../metadata/UMLPackage.html#getState__objectNodeOfInState())
[`ObjectNode.getInState()`](../../activities/mdbasicactivities/ObjectNode.html#getInState())
Model:
opposite="inState" ordered="false"
Generated:
getConnectionPoint
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Pseudostate](Pseudostate.html)> getConnectionPoint()
Returns the value of the '***Connection Point***' containment reference list.
 The list contents are of type [`Pseudostate`](Pseudostate.html).
 It is bidirectional and its opposite is '[`*State*`](Pseudostate.html#getState())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The entry and exit Pseudostates of a composite State. These can only be entry or exit Pseudostates, and they must have different names. They can only be defined
 for composite States.
 end-model-doc
Returns:
the value of the '*Connection Point*' containment reference list.
See Also:
[`UMLPackage.getState_ConnectionPoint()`](../../metadata/UMLPackage.html#getState_ConnectionPoint())
[`Pseudostate.getState()`](Pseudostate.html#getState())
Model:
opposite="state" containment="true" resolveProxies="true" ordered="false"
Generated:
hasConnection
boolean hasConnection()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasRegion
boolean hasRegion()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasDeferrableTrigger
boolean hasDeferrableTrigger()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_objectNodeOfInState
boolean has_objectNodeOfInState()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasConnectionPoint
boolean hasConnectionPoint()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines</a></div>
<h1 class="title" title="Interface State">Interface State</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="FinalState.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">FinalState</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">State</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>, <a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>State</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A State models a situation during which some (usually implicit) invariant condition holds.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getRegion()"><code><em>Region</em></code></a></li>
<li><a href="#getConnectionPoint()"><code><em>Connection Point</em></code></a></li>
<li><a href="#getConnection()"><code><em>Connection</em></code></a></li>
<li><a href="#getSubmachine()"><code><em>Submachine</em></code></a></li>
<li><a href="#getStateInvariant()"><code><em>State Invariant</em></code></a></li>
<li><a href="#getDeferrableTrigger()"><code><em>Deferrable Trigger</em></code></a></li>
<li><a href="#getDoActivity()"><code><em>Do Activity</em></code></a></li>
<li><a href="#getEntry()"><code><em>Entry</em></code></a></li>
<li><a href="#getExit()"><code><em>Exit</em></code></a></li>
<li><a href="#isComposite()"><code><em>Composite</em></code></a></li>
<li><a href="#isOrthogonal()"><code><em>Orthogonal</em></code></a></li>
<li><a href="#isSimple()"><code><em>Simple</em></code></a></li>
<li><a href="#isSubmachineState()"><code><em>Submachine State</em></code></a></li>
<li><a href="#get_objectNodeOfInState()"><code><em>object Node Of In State</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getState()"><code>UMLPackage.getState()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='statemachines.mdbehaviorstatemachines'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_objectNodeOfInState()">get_objectNodeOfInState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>object Node Of In State</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConnection()">getConnection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Connection</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConnectionPoint()">getConnectionPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Connection Point</b></em>' containment reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDeferrableTrigger()">getDeferrableTrigger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Deferrable Trigger</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDoActivity()">getDoActivity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Do Activity</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEntry()">getEntry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Entry</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExit()">getExit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Exit</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRegion()">getRegion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Region</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStateInvariant()">getStateInvariant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>State Invariant</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSubmachine()">getSubmachine</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Submachine</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_objectNodeOfInState()">has_objectNodeOfInState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasConnection()">hasConnection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasConnectionPoint()">hasConnectionPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasDeferrableTrigger()">hasDeferrableTrigger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasRegion()">hasRegion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isComposite()">isComposite</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Composite</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isOrthogonal()">isOrthogonal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Orthogonal</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSimple()">isSimple</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Simple</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSubmachineState()">isSubmachineState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Submachine State</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDoActivity(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setDoActivity</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDoActivity()"><code><em>Do Activity</em></code></a>' containment
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEntry(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setEntry</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getEntry()"><code><em>Entry</em></code></a>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setExit(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setExit</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getExit()"><code><em>Exit</em></code></a>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setStateInvariant(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setStateInvariant</a><wbr/>(<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getStateInvariant()"><code><em>State Invariant</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSubmachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)">setSubmachine</a><wbr/>(<a href="StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSubmachine()"><code><em>Submachine</em></code></a>' reference.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></h3>
<code><a href="../../classes/mdkernel/Namespace.html#getElementImport()">getElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#getImportedMember()">getImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getMember()">getMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedDiagram()">getOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedMember()">getOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#getOwnedRule()">getOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#getPackageImport()">getPackageImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasElementImport()">hasElementImport</a>, <a href="../../classes/mdkernel/Namespace.html#hasImportedMember()">hasImportedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasMember()">hasMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedDiagram()">hasOwnedDiagram</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedMember()">hasOwnedMember</a>, <a href="../../classes/mdkernel/Namespace.html#hasOwnedRule()">hasOwnedRule</a>, <a href="../../classes/mdkernel/Namespace.html#hasPackageImport()">hasPackageImport</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="../../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="../../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="../../classes/mdkernel/RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="../../classes/mdkernel/RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.<a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></h3>
<code><a href="Vertex.html#get_vertexOfRedefinedVertex()">get_vertexOfRedefinedVertex</a>, <a href="Vertex.html#getContainer()">getContainer</a>, <a href="Vertex.html#getIncoming()">getIncoming</a>, <a href="Vertex.html#getOutgoing()">getOutgoing</a>, <a href="Vertex.html#getRedefinedVertex()">getRedefinedVertex</a>, <a href="Vertex.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="Vertex.html#hasIncoming()">hasIncoming</a>, <a href="Vertex.html#hasOutgoing()">hasOutgoing</a>, <a href="Vertex.html#setContainer(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)">setContainer</a>, <a href="Vertex.html#setRedefinedVertex(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)">setRedefinedVertex</a></code></div>
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
<section class="detail" id="getSubmachine()">
<h3>getSubmachine</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></span> <span class="element-name">getSubmachine</span>()</div>
<div class="block">Returns the value of the '<em><b>Submachine</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="StateMachine.html#getSubmachineState()"><code><em>Submachine State</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The StateMachine that is to be inserted in place of the (submachine) State.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Submachine</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setSubmachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)"><code>setSubmachine(StateMachine)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getState_Submachine()"><code>UMLPackage.getState_Submachine()</code></a></li>
<li><a href="StateMachine.html#getSubmachineState()"><code>StateMachine.getSubmachineState()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="submachineState" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSubmachine(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)">
<h3>setSubmachine</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSubmachine</span><wbr/><span class="parameters">(@CheckForNull
 <a href="StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSubmachine()"><code><em>Submachine</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Submachine</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getSubmachine()"><code>getSubmachine()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnection()">
<h3>getConnection</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">ConnectionPointReference</a>&gt;</span> <span class="element-name">getConnection</span>()</div>
<div class="block">Returns the value of the '<em><b>Connection</b></em>' containment reference list.
 The list contents are of type <a href="ConnectionPointReference.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>ConnectionPointReference</code></a>.
 It is bidirectional and its opposite is
 '<a href="ConnectionPointReference.html#getState()"><code><em>State</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The entry and exit connection points used in conjunction with this (submachine) State, i.e., as targets and sources, respectively, in the Region with the
 submachine State. A connection point reference references the corresponding definition of a connection point Pseudostate in the StateMachine referenced by the
 submachine State.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Connection</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getState_Connection()"><code>UMLPackage.getState_Connection()</code></a></li>
<li><a href="ConnectionPointReference.html#getState()"><code>ConnectionPointReference.getState()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="state" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRegion()">
<h3>getRegion</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a>&gt;</span> <span class="element-name">getRegion</span>()</div>
<div class="block">Returns the value of the '<em><b>Region</b></em>' containment reference list.
 The list contents are of type <a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Region</code></a>.
 It is bidirectional and its opposite is '<a href="Region.html#getState()"><code><em>State</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Regions owned directly by the State.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Region</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getState_Region()"><code>UMLPackage.getState_Region()</code></a></li>
<li><a href="Region.html#getState()"><code>Region.getState()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="state" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateInvariant()">
<h3>getStateInvariant</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getStateInvariant</span>()</div>
<div class="block">Returns the value of the '<em><b>State Invariant</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../classes/mdkernel/Constraint.html#getOwningState()"><code><em>Owning State</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies conditions that are always true when this State is the current State. In ProtocolStateMachines state invariants are additional conditions to the
 preconditions of the outgoing Transitions, and to the postcondition of the incoming Transitions.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>State Invariant</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setStateInvariant(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)"><code>setStateInvariant(Constraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getState_StateInvariant()"><code>UMLPackage.getState_StateInvariant()</code></a></li>
<li><a href="../../classes/mdkernel/Constraint.html#getOwningState()"><code>Constraint.getOwningState()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningState" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStateInvariant(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>setStateInvariant</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setStateInvariant</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getStateInvariant()"><code><em>State Invariant</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>State Invariant</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getStateInvariant()"><code>getStateInvariant()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEntry()">
<h3>getEntry</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">getEntry</span>()</div>
<div class="block">Returns the value of the '<em><b>Entry</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfEntry()"><code><em>state Of Entry</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional Behavior that is executed whenever this State is entered regardless of the Transition taken to reach the State. If defined, entry Behaviors are
 always executed to completion prior to any internal Behavior or Transitions performed within the State.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Entry</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#setEntry(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)"><code>setEntry(Behavior)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getState_Entry()"><code>UMLPackage.getState_Entry()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfEntry()"><code>Behavior.get_stateOfEntry()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_stateOfEntry" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEntry(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>setEntry</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEntry</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getEntry()"><code><em>Entry</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Entry</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getEntry()"><code>getEntry()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExit()">
<h3>getExit</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">getExit</span>()</div>
<div class="block">Returns the value of the '<em><b>Exit</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfExit()"><code><em>state Of Exit</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional Behavior that is executed whenever this State is exited regardless of which Transition was taken out of the State. If defined, exit Behaviors are
 always executed to completion only after all internal and transition Behaviors have completed execution.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Exit</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#setExit(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)"><code>setExit(Behavior)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getState_Exit()"><code>UMLPackage.getState_Exit()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfExit()"><code>Behavior.get_stateOfExit()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_stateOfExit" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExit(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>setExit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setExit</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getExit()"><code><em>Exit</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Exit</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getExit()"><code>getExit()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isComposite()">
<h3>isComposite</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isComposite</span>()</div>
<div class="block">Returns the value of the '<em><b>Composite</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A state with isComposite=true is said to be a composite State. A composite State is a State that contains at least one Region.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Composite</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getState_Composite()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOrthogonal()">
<h3>isOrthogonal</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isOrthogonal</span>()</div>
<div class="block">Returns the value of the '<em><b>Orthogonal</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A State with isOrthogonal=true is said to be an orthogonal composite State An orthogonal composite State contains two or more Regions.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Orthogonal</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getState_Orthogonal()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSimple()">
<h3>isSimple</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSimple</span>()</div>
<div class="block">Returns the value of the '<em><b>Simple</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A State with isSimple=true is said to be a simple State A simple State does not have any Regions and it does not refer to any submachine StateMachine.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Simple</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getState_Simple()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSubmachineState()">
<h3>isSubmachineState</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSubmachineState</span>()</div>
<div class="block">Returns the value of the '<em><b>Submachine State</b></em>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A State with isSubmachineState=true is said to be a submachine State Such a State refers to another StateMachine(submachine).
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Submachine State</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li>
<details class="invalid-tag">
<summary>invalid reference</summary>
<pre><code>com.nomagic.uml2.ext.magicdraw.metadata.UMLPackage#getState_SubmachineState()</code></pre>
</details>
</li>
</ul>
</dd>
<dt>Model:</dt>
<dd>dataType="com.nomagic.uml2.ext.magicdraw.Boolean" required="true" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDoActivity()">
<h3>getDoActivity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">getDoActivity</span>()</div>
<div class="block">Returns the value of the '<em><b>Do Activity</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfDoActivity()"><code><em>state Of Do Activity</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 An optional Behavior that is executed while being in the State. The execution starts when this State is entered, and ceases either by itself when done, or when
 the State is exited, whichever comes first.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Do Activity</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setDoActivity(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)"><code>setDoActivity(Behavior)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getState_DoActivity()"><code>UMLPackage.getState_DoActivity()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_stateOfDoActivity()"><code>Behavior.get_stateOfDoActivity()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_stateOfDoActivity" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDoActivity(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>setDoActivity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDoActivity</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDoActivity()"><code><em>Do Activity</em></code></a>' containment
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Do Activity</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getDoActivity()"><code>getDoActivity()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDeferrableTrigger()">
<h3>getDeferrableTrigger</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt;</span> <span class="element-name">getDeferrableTrigger</span>()</div>
<div class="block">Returns the value of the '<em><b>Deferrable Trigger</b></em>' containment reference list.
 The list contents are of type <a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdcommunications/Trigger.html#get_stateOfDeferrableTrigger()"><code><em>state Of Deferrable Trigger</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A list of Triggers that are candidates to be retained by the StateMachine if they trigger no Transitions out of the State (not consumed). A deferred Trigger is
 retained until the StateMachine reaches a State configuration where it is no longer deferred.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Deferrable Trigger</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getState_DeferrableTrigger()"><code>UMLPackage.getState_DeferrableTrigger()</code></a></li>
<li><a href="../../commonbehaviors/mdcommunications/Trigger.html#get_stateOfDeferrableTrigger()"><code>Trigger.get_stateOfDeferrableTrigger()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_stateOfDeferrableTrigger" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_objectNodeOfInState()">
<h3>get_objectNodeOfInState</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a>&gt;</span> <span class="element-name">get_objectNodeOfInState</span>()</div>
<div class="block">Returns the value of the '<em><b>object Node Of In State</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities"><code>ObjectNode</code></a>.
 It is bidirectional and its opposite is '<a href="../../activities/mdbasicactivities/ObjectNode.html#getInState()"><code><em>In State</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>object Node Of In State</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>object Node Of In State</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getState__objectNodeOfInState()"><code>UMLPackage.getState__objectNodeOfInState()</code></a></li>
<li><a href="../../activities/mdbasicactivities/ObjectNode.html#getInState()"><code>ObjectNode.getInState()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="inState" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectionPoint()">
<h3>getConnectionPoint</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Pseudostate</a>&gt;</span> <span class="element-name">getConnectionPoint</span>()</div>
<div class="block">Returns the value of the '<em><b>Connection Point</b></em>' containment reference list.
 The list contents are of type <a href="Pseudostate.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Pseudostate</code></a>.
 It is bidirectional and its opposite is '<a href="Pseudostate.html#getState()"><code><em>State</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The entry and exit Pseudostates of a composite State. These can only be entry or exit Pseudostates, and they must have different names. They can only be defined
 for composite States.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Connection Point</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getState_ConnectionPoint()"><code>UMLPackage.getState_ConnectionPoint()</code></a></li>
<li><a href="Pseudostate.html#getState()"><code>Pseudostate.getState()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="state" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasConnection()">
<h3>hasConnection</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasConnection</span>()
               throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasRegion()">
<h3>hasRegion</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasRegion</span>()
           throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasDeferrableTrigger()">
<h3>hasDeferrableTrigger</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasDeferrableTrigger</span>()
                      throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_objectNodeOfInState()">
<h3>has_objectNodeOfInState</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_objectNodeOfInState</span>()
                         throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasConnectionPoint()">
<h3>hasConnectionPoint</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasConnectionPoint</span>()
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
