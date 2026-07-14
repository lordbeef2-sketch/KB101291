# JAVA OPENAPI: Transition (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html
- source_path: `com/nomagic/uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/Transition.html`
- source_sha256: `a870f01d62e03d67d3d7a13cc4003f2f0e7b8a0269ef247ce9cb32633a38907c`
- captured_utc: `2026-07-14T16:53:04.964548+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines](package-summary.html)

## Interface Transition

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `[Namespace](../../classes/mdkernel/Namespace.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[ProtocolTransition](../mdprotocolstatemachines/ProtocolTransition.html)`

public interfaceTransitionextends [Namespace](../../classes/mdkernel/Namespace.html), [RedefinableElement](../../classes/mdkernel/RedefinableElement.html)

begin-user-doc 
 A representation of the model object '***Transition***'.
 end-user-doc 
begin-model-doc 
 A Transition represents an arc between exactly one source Vertex and exactly one Target vertex (the source and targets may be the same Vertex). It may form part of
 a compound transition, which takes the StateMachine from one steady State configuration to another, representing the full response of the StateMachine to an
 occurrence of an Event that triggered it.
 end-model-doc 
The following features are supported:
 [`*Effect*`](#getEffect())
[`*Guard*`](#getGuard())
[`*Trigger*`](#getTrigger())
[`*Kind*`](#getKind())
[`*Redefined Transition*`](#getRedefinedTransition())
[`*transition Of Redefined Transition*`](#get_transitionOfRedefinedTransition())
[`*Source*`](#getSource())
[`*Target*`](#getTarget())
[`*Container*`](#getContainer())

See Also:
[`UMLPackage.getTransition()`](../../metadata/UMLPackage.html#getTransition())
Model:
annotation="MOF package='statemachines.mdbehaviorstatemachines'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Transition](Transition.html)>`
`[get_transitionOfRedefinedTransition](#get_transitionOfRedefinedTransition())()`
Returns the value of the '***transition Of Redefined Transition***' reference list.
`[Region](Region.html)`
`[getContainer](#getContainer())()`
Returns the value of the '***Container***' container reference.
`[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[getEffect](#getEffect())()`
Returns the value of the '***Effect***' containment reference.
`[Constraint](../../classes/mdkernel/Constraint.html)`
`[getGuard](#getGuard())()`
Returns the value of the '***Guard***' reference.
`[TransitionKind](TransitionKind.html)`
`[getKind](#getKind())()`
Returns the value of the '***Kind***' attribute.
`[Transition](Transition.html)`
`[getRedefinedTransition](#getRedefinedTransition())()`
Returns the value of the '***Redefined Transition***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../classes/mdkernel/Classifier.html)>`
`[getRedefinitionContext](#getRedefinitionContext())()`
Returns the value of the '***Redefinition Context***' reference list.
`[Vertex](Vertex.html)`
`[getSource](#getSource())()`
Returns the value of the '***Source***' reference.
`[Vertex](Vertex.html)`
`[getTarget](#getTarget())()`
Returns the value of the '***Target***' reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Trigger](../../commonbehaviors/mdcommunications/Trigger.html)>`
`[getTrigger](#getTrigger())()`
Returns the value of the '***Trigger***' containment reference list.
`boolean`
`[has_transitionOfRedefinedTransition](#has_transitionOfRedefinedTransition())()`

`boolean`
`[hasTrigger](#hasTrigger())()`

`void`
`[setContainer](#setContainer(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region))([Region](Region.html) value)`
Sets the value of the '[`*Container*`](#getContainer())' container
 reference.
`void`
`[setEffect](#setEffect(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)`
Sets the value of the '[`*Effect*`](#getEffect())' containment reference.
`void`
`[setGuard](#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](../../classes/mdkernel/Constraint.html) value)`
Sets the value of the '[`*Guard*`](#getGuard())' reference.
`void`
`[setKind](#setKind(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKind))([TransitionKind](TransitionKind.html) value)`
Sets the value of the '[`*Kind*`](#getKind())' attribute.
`void`
`[setRedefinedTransition](#setRedefinedTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](Transition.html) value)`
Sets the value of the
 '[`*Redefined Transition*`](#getRedefinedTransition())' reference.
`void`
`[setSource](#setSource(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex))([Vertex](Vertex.html) value)`
Sets the value of the '[`*Source*`](#getSource())' reference.
`void`
`[setTarget](#setTarget(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex))([Vertex](Vertex.html) value)`
Sets the value of the '[`*Target*`](#getTarget())' reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
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

============ METHOD DETAIL ========== 
Method Details
getKind
@CheckForNull[TransitionKind](TransitionKind.html) getKind()
Returns the value of the '***Kind***' attribute.
 The default value is `"external"`.
 The literals are from the enumeration [`TransitionKind`](TransitionKind.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Indicates the precise type of the Transition.
 end-model-doc
Returns:
the value of the '*Kind*' attribute.
See Also:
[`TransitionKind`](TransitionKind.html)
[`setKind(TransitionKind)`](#setKind(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKind))
[`UMLPackage.getTransition_Kind()`](../../metadata/UMLPackage.html#getTransition_Kind())
Model:
default="external" required="true" ordered="false"
Generated:
setKind
void setKind(@CheckForNull
 [TransitionKind](TransitionKind.html) value)
Sets the value of the '[`*Kind*`](#getKind())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Kind*' attribute.
See Also:
[`TransitionKind`](TransitionKind.html)
[`getKind()`](#getKind())
Generated:
getContainer
@CheckForNull[Region](Region.html) getContainer()
Returns the value of the '***Container***' container reference.
 It is bidirectional and its opposite is '[`*Transition*`](Region.html#getTransition())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Designates the Region that owns this Transition.
 end-model-doc
Returns:
the value of the '*Container*' container reference.
See Also:
[`setContainer(Region)`](#setContainer(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region))
[`UMLPackage.getTransition_Container()`](../../metadata/UMLPackage.html#getTransition_Container())
[`Region.getTransition()`](Region.html#getTransition())
Model:
opposite="transition" required="true" transient="false" ordered="false"
Generated:
setContainer
void setContainer(@CheckForNull
 [Region](Region.html) value)
Sets the value of the '[`*Container*`](#getContainer())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Container*' container reference.
See Also:
[`getContainer()`](#getContainer())
Generated:
getTarget
@CheckForNull[Vertex](Vertex.html) getTarget()
Returns the value of the '***Target***' reference.
 It is bidirectional and its opposite is '[`*Incoming*`](Vertex.html#getIncoming())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Designates the target Vertex that is reached when the Transition is taken.
 end-model-doc
Returns:
the value of the '*Target*' reference.
See Also:
[`setTarget(Vertex)`](#setTarget(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex))
[`UMLPackage.getTransition_Target()`](../../metadata/UMLPackage.html#getTransition_Target())
[`Vertex.getIncoming()`](Vertex.html#getIncoming())
Model:
opposite="incoming" required="true" ordered="false"
Generated:
setTarget
void setTarget(@CheckForNull
 [Vertex](Vertex.html) value)
Sets the value of the '[`*Target*`](#getTarget())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Target*' reference.
See Also:
[`getTarget()`](#getTarget())
Generated:
getRedefinedTransition
@CheckForNull[Transition](Transition.html) getRedefinedTransition()
Returns the value of the '***Redefined Transition***' reference.
 It is bidirectional and its opposite is '`.mdbehaviorstatemachines.Transition#get_transitionOfRedefinedTransition *transition Of Redefined Transition*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The Transition that is redefined by this Transition.
 end-model-doc
Returns:
the value of the '*Redefined Transition*' reference.
See Also:
[`setRedefinedTransition(Transition)`](#setRedefinedTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))
[`UMLPackage.getTransition_RedefinedTransition()`](../../metadata/UMLPackage.html#getTransition_RedefinedTransition())
[`get_transitionOfRedefinedTransition()`](#get_transitionOfRedefinedTransition())
Model:
opposite="_transitionOfRedefinedTransition" ordered="false"
Generated:
setRedefinedTransition
void setRedefinedTransition(@CheckForNull
 [Transition](Transition.html) value)
Sets the value of the
 '[`*Redefined Transition*`](#getRedefinedTransition())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Redefined Transition*' reference.
See Also:
[`getRedefinedTransition()`](#getRedefinedTransition())
Generated:
get_transitionOfRedefinedTransition
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Transition](Transition.html)> get_transitionOfRedefinedTransition()
Returns the value of the '***transition Of Redefined Transition***' reference list.
 The list contents are of type [`Transition`](Transition.html).
 It is bidirectional and its opposite is
 '[`*Redefined Transition*`](#getRedefinedTransition())'.
 begin-user-doc 
If the meaning of the '*transition Of Redefined Transition*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*transition Of Redefined Transition*' reference list.
See Also:
[`UMLPackage.getTransition__transitionOfRedefinedTransition()`](../../metadata/UMLPackage.html#getTransition__transitionOfRedefinedTransition())
[`getRedefinedTransition()`](#getRedefinedTransition())
Model:
opposite="redefinedTransition" ordered="false"
Generated:
getGuard
@CheckForNull[Constraint](../../classes/mdkernel/Constraint.html) getGuard()
Returns the value of the '***Guard***' reference.
 It is bidirectional and its opposite is '[`*transition Of Guard*`](../../classes/mdkernel/Constraint.html#get_transitionOfGuard())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A guard is a Constraint that provides a fine-grained control over the firing of the Transition. The guard is evaluated when an Event occurrence is dispatched by
 the StateMachine. If the guard is true at that time, the Transition may be enabled, otherwise, it is disabled. Guards should be pure expressions without side
 effects. Guard expressions with side effects are ill formed.
 end-model-doc
Returns:
the value of the '*Guard*' reference.
See Also:
[`setGuard(Constraint)`](#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))
[`UMLPackage.getTransition_Guard()`](../../metadata/UMLPackage.html#getTransition_Guard())
[`Constraint.get_transitionOfGuard()`](../../classes/mdkernel/Constraint.html#get_transitionOfGuard())
Model:
opposite="_transitionOfGuard" ordered="false"
Generated:
setGuard
void setGuard(@CheckForNull
 [Constraint](../../classes/mdkernel/Constraint.html) value)
Sets the value of the '[`*Guard*`](#getGuard())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Guard*' reference.
See Also:
[`getGuard()`](#getGuard())
Generated:
getEffect
@CheckForNull[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) getEffect()
Returns the value of the '***Effect***' containment reference.
 It is bidirectional and its opposite is
 '[`*transition Of Effect*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_transitionOfEffect())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies an optional behavior to be performed when the Transition fires.
 end-model-doc
Returns:
the value of the '*Effect*' containment reference.
See Also:
[`setEffect(Behavior)`](#setEffect(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))
[`UMLPackage.getTransition_Effect()`](../../metadata/UMLPackage.html#getTransition_Effect())
[`Behavior.get_transitionOfEffect()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_transitionOfEffect())
Model:
opposite="_transitionOfEffect" containment="true" resolveProxies="true" ordered="false"
Generated:
setEffect
void setEffect(@CheckForNull
 [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)
Sets the value of the '[`*Effect*`](#getEffect())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Effect*' containment reference.
See Also:
[`getEffect()`](#getEffect())
Generated:
getTrigger
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Trigger](../../commonbehaviors/mdcommunications/Trigger.html)> getTrigger()
Returns the value of the '***Trigger***' containment reference list.
 The list contents are of type [`Trigger`](../../commonbehaviors/mdcommunications/Trigger.html).
 It is bidirectional and its opposite is
 '[`*transition Of Trigger*`](../../commonbehaviors/mdcommunications/Trigger.html#get_transitionOfTrigger())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the Triggers that may fire the transition.
 end-model-doc
Returns:
the value of the '*Trigger*' containment reference list.
See Also:
[`UMLPackage.getTransition_Trigger()`](../../metadata/UMLPackage.html#getTransition_Trigger())
[`Trigger.get_transitionOfTrigger()`](../../commonbehaviors/mdcommunications/Trigger.html#get_transitionOfTrigger())
Model:
opposite="_transitionOfTrigger" containment="true" resolveProxies="true" ordered="false"
Generated:
getSource
@CheckForNull[Vertex](Vertex.html) getSource()
Returns the value of the '***Source***' reference.
 It is bidirectional and its opposite is '[`*Outgoing*`](Vertex.html#getOutgoing())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Designates the originating Vertex (State or Pseudostate) of the Transition.
 end-model-doc
Returns:
the value of the '*Source*' reference.
See Also:
[`setSource(Vertex)`](#setSource(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex))
[`UMLPackage.getTransition_Source()`](../../metadata/UMLPackage.html#getTransition_Source())
[`Vertex.getOutgoing()`](Vertex.html#getOutgoing())
Model:
opposite="outgoing" required="true" ordered="false"
Generated:
setSource
void setSource(@CheckForNull
 [Vertex](Vertex.html) value)
Sets the value of the '[`*Source*`](#getSource())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Source*' reference.
See Also:
[`getSource()`](#getSource())
Generated:
getRedefinitionContext
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Classifier](../../classes/mdkernel/Classifier.html)> getRedefinitionContext()
Returns the value of the '***Redefinition Context***' reference list.
 The list contents are of type [`Classifier`](../../classes/mdkernel/Classifier.html).
 It is bidirectional and its opposite is
 '`*transition Of Redefinition Context*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 References the Classifier in which context this element may be redefined.
 end-model-doc
Specified by:
`[getRedefinitionContext](../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext())` in interface `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`
Returns:
the value of the '*Redefinition Context*' reference list.
See Also:
[`UMLPackage.getTransition_RedefinitionContext()`](../../metadata/UMLPackage.html#getTransition_RedefinitionContext())
`com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier#get_transitionOfRedefinitionContext`
Model:
opposite="_transitionOfRedefinitionContext" transient="true" changeable="false" volatile="true" derived="true" ordered="false"
Generated:
has_transitionOfRedefinedTransition
boolean has_transitionOfRedefinedTransition()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
hasTrigger
boolean hasTrigger()
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
<h1 class="title" title="Interface Transition">Interface Transition</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code><a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Transition</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a>, <a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Transition</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Transition represents an arc between exactly one source Vertex and exactly one Target vertex (the source and targets may be the same Vertex). It may form part of
 a compound transition, which takes the StateMachine from one steady State configuration to another, representing the full response of the StateMachine to an
 occurrence of an Event that triggered it.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getEffect()"><code><em>Effect</em></code></a></li>
<li><a href="#getGuard()"><code><em>Guard</em></code></a></li>
<li><a href="#getTrigger()"><code><em>Trigger</em></code></a></li>
<li><a href="#getKind()"><code><em>Kind</em></code></a></li>
<li><a href="#getRedefinedTransition()"><code><em>Redefined Transition</em></code></a></li>
<li><a href="#get_transitionOfRedefinedTransition()"><code><em>transition Of Redefined Transition</em></code></a></li>
<li><a href="#getSource()"><code><em>Source</em></code></a></li>
<li><a href="#getTarget()"><code><em>Target</em></code></a></li>
<li><a href="#getContainer()"><code><em>Container</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getTransition()"><code>UMLPackage.getTransition()</code></a></li>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_transitionOfRedefinedTransition()">get_transitionOfRedefinedTransition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>transition Of Redefined Transition</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContainer()">getContainer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Container</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEffect()">getEffect</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Effect</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getGuard()">getGuard</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Guard</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getKind()">getKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Kind</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedTransition()">getRedefinedTransition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefined Transition</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinitionContext()">getRedefinitionContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Redefinition Context</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSource()">getSource</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Source</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTarget()">getTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Target</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTrigger()">getTrigger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Trigger</b></em>' containment reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_transitionOfRedefinedTransition()">has_transitionOfRedefinedTransition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasTrigger()">hasTrigger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setContainer(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)">setContainer</a><wbr/>(<a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getContainer()"><code><em>Container</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEffect(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setEffect</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getEffect()"><code><em>Effect</em></code></a>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setGuard</a><wbr/>(<a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getGuard()"><code><em>Guard</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setKind(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKind)">setKind</a><wbr/>(<a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getKind()"><code><em>Kind</em></code></a>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRedefinedTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">setRedefinedTransition</a><wbr/>(<a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#getRedefinedTransition()"><code><em>Redefined Transition</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSource(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)">setSource</a><wbr/>(<a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSource()"><code><em>Source</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTarget(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)">setTarget</a><wbr/>(<a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getTarget()"><code><em>Target</em></code></a>' reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
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
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
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
<section class="detail" id="getKind()">
<h3>getKind</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a></span> <span class="element-name">getKind</span>()</div>
<div class="block">Returns the value of the '<em><b>Kind</b></em>' attribute.
 The default value is <code>"external"</code>.
 The literals are from the enumeration <a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>TransitionKind</code></a>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Indicates the precise type of the Transition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Kind</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>TransitionKind</code></a></li>
<li><a href="#setKind(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKind)"><code>setKind(TransitionKind)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTransition_Kind()"><code>UMLPackage.getTransition_Kind()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="external" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setKind(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.TransitionKind)">
<h3>setKind</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setKind</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">TransitionKind</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getKind()"><code><em>Kind</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Kind</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="TransitionKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>TransitionKind</code></a></li>
<li><a href="#getKind()"><code>getKind()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainer()">
<h3>getContainer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a></span> <span class="element-name">getContainer</span>()</div>
<div class="block">Returns the value of the '<em><b>Container</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Region.html#getTransition()"><code><em>Transition</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Designates the Region that owns this Transition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Container</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setContainer(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)"><code>setContainer(Region)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTransition_Container()"><code>UMLPackage.getTransition_Container()</code></a></li>
<li><a href="Region.html#getTransition()"><code>Region.getTransition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="transition" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContainer(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Region)">
<h3>setContainer</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setContainer</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Region.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Region</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getContainer()"><code><em>Container</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Container</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getContainer()"><code>getContainer()</code></a></li>
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
</span><span class="return-type"><a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></span> <span class="element-name">getTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>Target</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Vertex.html#getIncoming()"><code><em>Incoming</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Designates the target Vertex that is reached when the Transition is taken.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Target</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setTarget(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)"><code>setTarget(Vertex)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTransition_Target()"><code>UMLPackage.getTransition_Target()</code></a></li>
<li><a href="Vertex.html#getIncoming()"><code>Vertex.getIncoming()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="incoming" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTarget(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)">
<h3>setTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getTarget()"><code><em>Target</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Target</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getTarget()"><code>getTarget()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedTransition()">
<h3>getRedefinedTransition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></span> <span class="element-name">getRedefinedTransition</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefined Transition</b></em>' reference.
 It is bidirectional and its opposite is '<code>.mdbehaviorstatemachines.Transition#get_transitionOfRedefinedTransition <em>transition Of Redefined Transition</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The Transition that is redefined by this Transition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Redefined Transition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setRedefinedTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)"><code>setRedefinedTransition(Transition)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTransition_RedefinedTransition()"><code>UMLPackage.getTransition_RedefinedTransition()</code></a></li>
<li><a href="#get_transitionOfRedefinedTransition()"><code>get_transitionOfRedefinedTransition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_transitionOfRedefinedTransition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRedefinedTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>setRedefinedTransition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRedefinedTransition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#getRedefinedTransition()"><code><em>Redefined Transition</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Redefined Transition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getRedefinedTransition()"><code>getRedefinedTransition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_transitionOfRedefinedTransition()">
<h3>get_transitionOfRedefinedTransition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a>&gt;</span> <span class="element-name">get_transitionOfRedefinedTransition</span>()</div>
<div class="block">Returns the value of the '<em><b>transition Of Redefined Transition</b></em>' reference list.
 The list contents are of type <a href="Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines"><code>Transition</code></a>.
 It is bidirectional and its opposite is
 '<a href="#getRedefinedTransition()"><code><em>Redefined Transition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>transition Of Redefined Transition</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>transition Of Redefined Transition</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getTransition__transitionOfRedefinedTransition()"><code>UMLPackage.getTransition__transitionOfRedefinedTransition()</code></a></li>
<li><a href="#getRedefinedTransition()"><code>getRedefinedTransition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="redefinedTransition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGuard()">
<h3>getGuard</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getGuard</span>()</div>
<div class="block">Returns the value of the '<em><b>Guard</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../classes/mdkernel/Constraint.html#get_transitionOfGuard()"><code><em>transition Of Guard</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A guard is a Constraint that provides a fine-grained control over the firing of the Transition. The guard is evaluated when an Event occurrence is dispatched by
 the StateMachine. If the guard is true at that time, the Transition may be enabled, otherwise, it is disabled. Guards should be pure expressions without side
 effects. Guard expressions with side effects are ill formed.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Guard</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)"><code>setGuard(Constraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTransition_Guard()"><code>UMLPackage.getTransition_Guard()</code></a></li>
<li><a href="../../classes/mdkernel/Constraint.html#get_transitionOfGuard()"><code>Constraint.get_transitionOfGuard()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_transitionOfGuard" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGuard(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>setGuard</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setGuard</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getGuard()"><code><em>Guard</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Guard</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getGuard()"><code>getGuard()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEffect()">
<h3>getEffect</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">getEffect</span>()</div>
<div class="block">Returns the value of the '<em><b>Effect</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_transitionOfEffect()"><code><em>transition Of Effect</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies an optional behavior to be performed when the Transition fires.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Effect</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setEffect(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)"><code>setEffect(Behavior)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTransition_Effect()"><code>UMLPackage.getTransition_Effect()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#get_transitionOfEffect()"><code>Behavior.get_transitionOfEffect()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_transitionOfEffect" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEffect(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>setEffect</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEffect</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getEffect()"><code><em>Effect</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Effect</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getEffect()"><code>getEffect()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrigger()">
<h3>getTrigger</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt;</span> <span class="element-name">getTrigger</span>()</div>
<div class="block">Returns the value of the '<em><b>Trigger</b></em>' containment reference list.
 The list contents are of type <a href="../../commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications"><code>Trigger</code></a>.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdcommunications/Trigger.html#get_transitionOfTrigger()"><code><em>transition Of Trigger</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the Triggers that may fire the transition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Trigger</em>' containment reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getTransition_Trigger()"><code>UMLPackage.getTransition_Trigger()</code></a></li>
<li><a href="../../commonbehaviors/mdcommunications/Trigger.html#get_transitionOfTrigger()"><code>Trigger.get_transitionOfTrigger()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_transitionOfTrigger" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSource()">
<h3>getSource</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a></span> <span class="element-name">getSource</span>()</div>
<div class="block">Returns the value of the '<em><b>Source</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Vertex.html#getOutgoing()"><code><em>Outgoing</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Designates the originating Vertex (State or Pseudostate) of the Transition.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Source</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setSource(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)"><code>setSource(Vertex)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTransition_Source()"><code>UMLPackage.getTransition_Source()</code></a></li>
<li><a href="Vertex.html#getOutgoing()"><code>Vertex.getOutgoing()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="outgoing" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSource(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Vertex)">
<h3>setSource</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSource</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Vertex.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Vertex</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSource()"><code><em>Source</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Source</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getSource()"><code>getSource()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinitionContext()">
<h3>getRedefinitionContext</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getRedefinitionContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Redefinition Context</b></em>' reference list.
 The list contents are of type <a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Classifier</code></a>.
 It is bidirectional and its opposite is
 '<code><em>transition Of Redefinition Context</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 References the Classifier in which context this element may be redefined.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a></code> in interface <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Redefinition Context</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getTransition_RedefinitionContext()"><code>UMLPackage.getTransition_RedefinitionContext()</code></a></li>
<li><code>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier#get_transitionOfRedefinitionContext</code></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_transitionOfRedefinitionContext" transient="true" changeable="false" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_transitionOfRedefinedTransition()">
<h3>has_transitionOfRedefinedTransition</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_transitionOfRedefinedTransition</span>()
                                     throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasTrigger()">
<h3>hasTrigger</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasTrigger</span>()
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
