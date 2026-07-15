# JAVA OPENAPI: Constraint (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Constraint.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/Constraint.html`
- source_sha256: `30fadcbe39100b84a2ce71b401adf027e0c2a4b2be8cfa2273d517310be0e285`
- captured_utc: `2026-07-14T16:56:15.753685+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface Constraint

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[DurationConstraint](../../commonbehaviors/mdsimpletime/DurationConstraint.html)`, `[InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html)`, `[IntervalConstraint](../../commonbehaviors/mdsimpletime/IntervalConstraint.html)`, `[TimeConstraint](../../commonbehaviors/mdsimpletime/TimeConstraint.html)`

public interfaceConstraintextends [PackageableElement](PackageableElement.html)

begin-user-doc 
 A representation of the model object '***Constraint***'.
 end-user-doc 
begin-model-doc 
 A Constraint is a condition or restriction expressed in natural language text or in a machine readable language for the purpose of declaring some of the semantics
 of an Element or set of Elements.
 end-model-doc 
The following features are supported:
 [`*Constrained Element*`](#getConstrainedElement())
[`*Context*`](#getContext())
[`*Specification*`](#getSpecification())
[`*Owning State*`](#getOwningState())
[`*action Of Local Postcondition*`](#get_actionOfLocalPostcondition())
[`*extend Of Condition*`](#get_extendOfCondition())
[`*Owning Transition*`](#getOwningTransition())
[`*protocol Transition Of Pre Condition*`](#get_protocolTransitionOfPreCondition())
[`*parameter Set Of Condition*`](#get_parameterSetOfCondition())
[`*message Of Guard*`](#get_messageOfGuard())
[`*Body Context*`](#getBodyContext())
[`*Post Context*`](#getPostContext())
[`*Pre Context*`](#getPreContext())
[`*behavior Of Postcondition*`](#get_behaviorOfPostcondition())
[`*behavior Of Precondition*`](#get_behaviorOfPrecondition())
[`*state Invariant Of Invariant*`](#get_stateInvariantOfInvariant())
[`*action Of Local Precondition*`](#get_actionOfLocalPrecondition())
[`*transition Of Guard*`](#get_transitionOfGuard())

See Also:
[`UMLPackage.getConstraint()`](../../metadata/UMLPackage.html#getConstraint())
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Action](../../actions/mdbasicactions/Action.html)`
`[get_actionOfLocalPostcondition](#get_actionOfLocalPostcondition())()`
Returns the value of the '***action Of Local Postcondition***' container reference.
`[Action](../../actions/mdbasicactions/Action.html)`
`[get_actionOfLocalPrecondition](#get_actionOfLocalPrecondition())()`
Returns the value of the '***action Of Local Precondition***' container reference.
`[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[get_behaviorOfPostcondition](#get_behaviorOfPostcondition())()`
Returns the value of the '***behavior Of Postcondition***' reference.
`[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`
`[get_behaviorOfPrecondition](#get_behaviorOfPrecondition())()`
Returns the value of the '***behavior Of Precondition***' reference.
`[Extend](../../mdusecases/Extend.html)`
`[get_extendOfCondition](#get_extendOfCondition())()`
Returns the value of the '***extend Of Condition***' container reference.
`[Message](../../interactions/mdbasicinteractions/Message.html)`
`[get_messageOfGuard](#get_messageOfGuard())()`
Returns the value of the '***message Of Guard***' container reference.
`[ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html)`
`[get_parameterSetOfCondition](#get_parameterSetOfCondition())()`
Returns the value of the '***parameter Set Of Condition***' container reference.
`[ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html)`
`[get_protocolTransitionOfPreCondition](#get_protocolTransitionOfPreCondition())()`
Returns the value of the '***protocol Transition Of Pre Condition***' reference.
`[StateInvariant](../../interactions/mdbasicinteractions/StateInvariant.html)`
`[get_stateInvariantOfInvariant](#get_stateInvariantOfInvariant())()`
Returns the value of the '***state Invariant Of Invariant***' container reference.
`[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html)`
`[get_transitionOfGuard](#get_transitionOfGuard())()`
Returns the value of the '***transition Of Guard***' reference.
`[Operation](Operation.html)`
`[getBodyContext](#getBodyContext())()`
Returns the value of the '***Body Context***' reference.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](Element.html)>`
`[getConstrainedElement](#getConstrainedElement())()`
Returns the value of the '***Constrained Element***' reference list.
`[Namespace](Namespace.html)`
`[getContext](#getContext())()`
Returns the value of the '***Context***' container reference.
`[State](../../statemachines/mdbehaviorstatemachines/State.html)`
`[getOwningState](#getOwningState())()`
Returns the value of the '***Owning State***' reference.
`[ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html)`
`[getOwningTransition](#getOwningTransition())()`
Returns the value of the '***Owning Transition***' reference.
`[Operation](Operation.html)`
`[getPostContext](#getPostContext())()`
Returns the value of the '***Post Context***' reference.
`[Operation](Operation.html)`
`[getPreContext](#getPreContext())()`
Returns the value of the '***Pre Context***' reference.
`[ValueSpecification](ValueSpecification.html)`
`[getSpecification](#getSpecification())()`
Returns the value of the '***Specification***' containment reference.
`boolean`
`[hasConstrainedElement](#hasConstrainedElement())()`

`void`
`[set_actionOfLocalPostcondition](#set_actionOfLocalPostcondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))([Action](../../actions/mdbasicactions/Action.html) value)`
Sets the value of the '[`*action Of Local Postcondition*`](#get_actionOfLocalPostcondition())'
 container reference.
`void`
`[set_actionOfLocalPrecondition](#set_actionOfLocalPrecondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))([Action](../../actions/mdbasicactions/Action.html) value)`
Sets the value of the '[`*action Of Local Precondition*`](#get_actionOfLocalPrecondition())'
 container reference.
`void`
`[set_behaviorOfPostcondition](#set_behaviorOfPostcondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)`
Sets the value of the '[`*behavior Of Postcondition*`](#get_behaviorOfPostcondition())'
 reference.
`void`
`[set_behaviorOfPrecondition](#set_behaviorOfPrecondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)`
Sets the value of the '[`*behavior Of Precondition*`](#get_behaviorOfPrecondition())' reference.
`void`
`[set_extendOfCondition](#set_extendOfCondition(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend))([Extend](../../mdusecases/Extend.html) value)`
Sets the value of the '[`*extend Of Condition*`](#get_extendOfCondition())' container reference.
`void`
`[set_messageOfGuard](#set_messageOfGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../interactions/mdbasicinteractions/Message.html) value)`
Sets the value of the '[`*message Of Guard*`](#get_messageOfGuard())' container reference.
`void`
`[set_parameterSetOfCondition](#set_parameterSetOfCondition(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet))([ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html) value)`
Sets the value of the '[`*parameter Set Of Condition*`](#get_parameterSetOfCondition())'
 container reference.
`void`
`[set_protocolTransitionOfPreCondition](#set_protocolTransitionOfPreCondition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition))([ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html) value)`
Sets the value of the
 '[`*protocol Transition Of Pre Condition*`](#get_protocolTransitionOfPreCondition())' reference.
`void`
`[set_stateInvariantOfInvariant](#set_stateInvariantOfInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant))([StateInvariant](../../interactions/mdbasicinteractions/StateInvariant.html) value)`
Sets the value of the '[`*state Invariant Of Invariant*`](#get_stateInvariantOfInvariant())'
 container reference.
`void`
`[set_transitionOfGuard](#set_transitionOfGuard(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) value)`
Sets the value of the '[`*transition Of Guard*`](#get_transitionOfGuard())' reference.
`void`
`[setBodyContext](#setBodyContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Operation](Operation.html) value)`
Sets the value of the '[`*Body Context*`](#getBodyContext())' reference.
`void`
`[setContext](#setContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Namespace](Namespace.html) value)`
Sets the value of the '[`*Context*`](#getContext())' container reference.
`void`
`[setOwningState](#setOwningState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([State](../../statemachines/mdbehaviorstatemachines/State.html) value)`
Sets the value of the '[`*Owning State*`](#getOwningState())' reference.
`void`
`[setOwningTransition](#setOwningTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition))([ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html) value)`
Sets the value of the '[`*Owning Transition*`](#getOwningTransition())' reference.
`void`
`[setPostContext](#setPostContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Operation](Operation.html) value)`
Sets the value of the '[`*Post Context*`](#getPostContext())' reference.
`void`
`[setPreContext](#setPreContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Operation](Operation.html) value)`
Sets the value of the '[`*Pre Context*`](#getPreContext())' reference.
`void`
`[setSpecification](#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))([ValueSpecification](ValueSpecification.html) value)`
Sets the value of the '[`*Specification*`](#getSpecification())' containment reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](Element.html)
`[get_activityPartitionOfRepresents](Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](Element.html#get_elementTaggedValue()), [get_elementValueOfElement](Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](Element.html#getAppliedStereotype()), [getOwnedComment](Element.html#getOwnedComment()), [getOwnedElement](Element.html#getOwnedElement()), [getOwner](Element.html#getOwner()), [getSyncElement](Element.html#getSyncElement()), [getTaggedValue](Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](Element.html#hasAppliedStereotype()), [hasElementTaggedValue](Element.html#hasElementTaggedValue()), [hasOwnedComment](Element.html#hasOwnedComment()), [hasOwnedElement](Element.html#hasOwnedElement()), [hasTaggedValue](Element.html#hasTaggedValue()), [setOwner](Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](NamedElement.html#getClientDependency()), [getName](NamedElement.html#getName()), [getNameExpression](NamedElement.html#getNameExpression()), [getNamespace](NamedElement.html#getNamespace()), [getQualifiedName](NamedElement.html#getQualifiedName()), [getSupplierDependency](NamedElement.html#getSupplierDependency()), [has_considerIgnoreFragmentOfMessage](NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](NamedElement.html#hasClientDependency()), [hasSupplierDependency](NamedElement.html#hasSupplierDependency()), [setName](NamedElement.html#setName(java.lang.String)), [setNameExpression](NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[PackageableElement](PackageableElement.html)
`[get_componentOfPackagedElement](PackageableElement.html#get_componentOfPackagedElement()), [get_elementImportOfImportedElement](PackageableElement.html#get_elementImportOfImportedElement()), [get_manifestationOfUtilizedElement](PackageableElement.html#get_manifestationOfUtilizedElement()), [getOwningPackage](PackageableElement.html#getOwningPackage()), [getVisibility](PackageableElement.html#getVisibility()), [has_elementImportOfImportedElement](PackageableElement.html#has_elementImportOfImportedElement()), [has_manifestationOfUtilizedElement](PackageableElement.html#has_manifestationOfUtilizedElement()), [set_componentOfPackagedElement](PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)), [setOwningPackage](PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)), [setVisibility](PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [getTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getConstrainedElement
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](Element.html)> getConstrainedElement()
Returns the value of the '***Constrained Element***' reference list.
 The list contents are of type [`Element`](Element.html).
 It is bidirectional and its opposite is
 '[`*constraint Of Constrained Element*`](Element.html#get_constraintOfConstrainedElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ordered set of Elements referenced by this Constraint.
 end-model-doc
Returns:
the value of the '*Constrained Element*' reference list.
See Also:
[`UMLPackage.getConstraint_ConstrainedElement()`](../../metadata/UMLPackage.html#getConstraint_ConstrainedElement())
[`Element.get_constraintOfConstrainedElement()`](Element.html#get_constraintOfConstrainedElement())
Model:
opposite="_constraintOfConstrainedElement"
Generated:
getSpecification
@CheckForNull[ValueSpecification](ValueSpecification.html) getSpecification()
Returns the value of the '***Specification***' containment reference.
 It is bidirectional and its opposite is
 '[`*Owning Constraint*`](ValueSpecification.html#getOwningConstraint())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 A condition that must be true when evaluated in order for the Constraint to be satisfied.
 end-model-doc
Returns:
the value of the '*Specification*' containment reference.
See Also:
[`setSpecification(ValueSpecification)`](#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))
[`UMLPackage.getConstraint_Specification()`](../../metadata/UMLPackage.html#getConstraint_Specification())
[`ValueSpecification.getOwningConstraint()`](ValueSpecification.html#getOwningConstraint())
Model:
opposite="owningConstraint" containment="true" resolveProxies="true" required="true" ordered="false"
Generated:
setSpecification
void setSpecification(@CheckForNull
 [ValueSpecification](ValueSpecification.html) value)
Sets the value of the '[`*Specification*`](#getSpecification())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Specification*' containment reference.
See Also:
[`getSpecification()`](#getSpecification())
Generated:
getContext
@CheckForNull[Namespace](Namespace.html) getContext()
Returns the value of the '***Context***' container reference.
 It is bidirectional and its opposite is '[`*Owned Rule*`](Namespace.html#getOwnedRule())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the Namespace that owns the Constraint.
 end-model-doc
Returns:
the value of the '*Context*' container reference.
See Also:
[`setContext(Namespace)`](#setContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))
[`UMLPackage.getConstraint_Context()`](../../metadata/UMLPackage.html#getConstraint_Context())
[`Namespace.getOwnedRule()`](Namespace.html#getOwnedRule())
Model:
opposite="ownedRule" transient="false" ordered="false"
Generated:
setContext
void setContext(@CheckForNull
 [Namespace](Namespace.html) value)
Sets the value of the '[`*Context*`](#getContext())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Context*' container reference.
See Also:
[`getContext()`](#getContext())
Generated:
getBodyContext
@CheckForNull[Operation](Operation.html) getBodyContext()
Returns the value of the '***Body Context***' reference.
 It is bidirectional and its opposite is '[`*Body Condition*`](Operation.html#getBodyCondition())'.
 begin-user-doc 
If the meaning of the '*Body Context*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Body Context*' reference.
See Also:
[`setBodyContext(Operation)`](#setBodyContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))
[`UMLPackage.getConstraint_BodyContext()`](../../metadata/UMLPackage.html#getConstraint_BodyContext())
[`Operation.getBodyCondition()`](Operation.html#getBodyCondition())
Model:
opposite="bodyCondition" ordered="false"
Generated:
setBodyContext
void setBodyContext(@CheckForNull
 [Operation](Operation.html) value)
Sets the value of the '[`*Body Context*`](#getBodyContext())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Body Context*' reference.
See Also:
[`getBodyContext()`](#getBodyContext())
Generated:
get_parameterSetOfCondition
@CheckForNull[ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html) get_parameterSetOfCondition()
Returns the value of the '***parameter Set Of Condition***' container reference.
 It is bidirectional and its opposite is '[`*Condition*`](../../activities/mdcompleteactivities/ParameterSet.html#getCondition())'.
 begin-user-doc 
If the meaning of the '*parameter Set Of Condition*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*parameter Set Of Condition*' container reference.
See Also:
[`set_parameterSetOfCondition(ParameterSet)`](#set_parameterSetOfCondition(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet))
[`UMLPackage.getConstraint__parameterSetOfCondition()`](../../metadata/UMLPackage.html#getConstraint__parameterSetOfCondition())
[`ParameterSet.getCondition()`](../../activities/mdcompleteactivities/ParameterSet.html#getCondition())
Model:
opposite="condition" transient="false" ordered="false"
Generated:
set_parameterSetOfCondition
void set_parameterSetOfCondition(@CheckForNull
 [ParameterSet](../../activities/mdcompleteactivities/ParameterSet.html) value)
Sets the value of the '[`*parameter Set Of Condition*`](#get_parameterSetOfCondition())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*parameter Set Of Condition*' container reference.
See Also:
[`get_parameterSetOfCondition()`](#get_parameterSetOfCondition())
Generated:
get_messageOfGuard
@CheckForNull[Message](../../interactions/mdbasicinteractions/Message.html) get_messageOfGuard()
Returns the value of the '***message Of Guard***' container reference.
 It is bidirectional and its opposite is '[`*Guard*`](../../interactions/mdbasicinteractions/Message.html#getGuard())'.
 begin-user-doc 
If the meaning of the '*message Of Guard*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*message Of Guard*' container reference.
See Also:
[`set_messageOfGuard(Message)`](#set_messageOfGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))
[`UMLPackage.getConstraint__messageOfGuard()`](../../metadata/UMLPackage.html#getConstraint__messageOfGuard())
[`Message.getGuard()`](../../interactions/mdbasicinteractions/Message.html#getGuard())
Model:
opposite="guard" transient="false" ordered="false"
Generated:
set_messageOfGuard
void set_messageOfGuard(@CheckForNull
 [Message](../../interactions/mdbasicinteractions/Message.html) value)
Sets the value of the '[`*message Of Guard*`](#get_messageOfGuard())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*message Of Guard*' container reference.
See Also:
[`get_messageOfGuard()`](#get_messageOfGuard())
Generated:
get_stateInvariantOfInvariant
@CheckForNull[StateInvariant](../../interactions/mdbasicinteractions/StateInvariant.html) get_stateInvariantOfInvariant()
Returns the value of the '***state Invariant Of Invariant***' container reference.
 It is bidirectional and its opposite is '[`*Invariant*`](../../interactions/mdbasicinteractions/StateInvariant.html#getInvariant())'.
 begin-user-doc 
If the meaning of the '*state Invariant Of Invariant*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*state Invariant Of Invariant*' container reference.
See Also:
[`set_stateInvariantOfInvariant(StateInvariant)`](#set_stateInvariantOfInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant))
[`UMLPackage.getConstraint__stateInvariantOfInvariant()`](../../metadata/UMLPackage.html#getConstraint__stateInvariantOfInvariant())
[`StateInvariant.getInvariant()`](../../interactions/mdbasicinteractions/StateInvariant.html#getInvariant())
Model:
opposite="invariant" transient="false" ordered="false"
Generated:
set_stateInvariantOfInvariant
void set_stateInvariantOfInvariant(@CheckForNull
 [StateInvariant](../../interactions/mdbasicinteractions/StateInvariant.html) value)
Sets the value of the '[`*state Invariant Of Invariant*`](#get_stateInvariantOfInvariant())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*state Invariant Of Invariant*' container reference.
See Also:
[`get_stateInvariantOfInvariant()`](#get_stateInvariantOfInvariant())
Generated:
get_transitionOfGuard
@CheckForNull[Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) get_transitionOfGuard()
Returns the value of the '***transition Of Guard***' reference.
 It is bidirectional and its opposite is '[`*Guard*`](../../statemachines/mdbehaviorstatemachines/Transition.html#getGuard())'.
 begin-user-doc 
If the meaning of the '*transition Of Guard*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*transition Of Guard*' reference.
See Also:
[`set_transitionOfGuard(Transition)`](#set_transitionOfGuard(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))
[`UMLPackage.getConstraint__transitionOfGuard()`](../../metadata/UMLPackage.html#getConstraint__transitionOfGuard())
[`Transition.getGuard()`](../../statemachines/mdbehaviorstatemachines/Transition.html#getGuard())
Model:
opposite="guard" ordered="false"
Generated:
set_transitionOfGuard
void set_transitionOfGuard(@CheckForNull
 [Transition](../../statemachines/mdbehaviorstatemachines/Transition.html) value)
Sets the value of the '[`*transition Of Guard*`](#get_transitionOfGuard())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*transition Of Guard*' reference.
See Also:
[`get_transitionOfGuard()`](#get_transitionOfGuard())
Generated:
getOwningState
@CheckForNull[State](../../statemachines/mdbehaviorstatemachines/State.html) getOwningState()
Returns the value of the '***Owning State***' reference.
 It is bidirectional and its opposite is
 '[`*State Invariant*`](../../statemachines/mdbehaviorstatemachines/State.html#getStateInvariant())'.
 begin-user-doc 
If the meaning of the '*Owning State*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning State*' reference.
See Also:
[`setOwningState(State)`](#setOwningState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))
[`UMLPackage.getConstraint_OwningState()`](../../metadata/UMLPackage.html#getConstraint_OwningState())
[`State.getStateInvariant()`](../../statemachines/mdbehaviorstatemachines/State.html#getStateInvariant())
Model:
opposite="stateInvariant" ordered="false"
Generated:
setOwningState
void setOwningState(@CheckForNull
 [State](../../statemachines/mdbehaviorstatemachines/State.html) value)
Sets the value of the '[`*Owning State*`](#getOwningState())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning State*' reference.
See Also:
[`getOwningState()`](#getOwningState())
Generated:
getOwningTransition
@CheckForNull[ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html) getOwningTransition()
Returns the value of the '***Owning Transition***' reference.
 It is bidirectional and its opposite is
 '[`*Post Condition*`](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html#getPostCondition())'.
 begin-user-doc 
If the meaning of the '*Owning Transition*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Transition*' reference.
See Also:
[`setOwningTransition(ProtocolTransition)`](#setOwningTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition))
[`UMLPackage.getConstraint_OwningTransition()`](../../metadata/UMLPackage.html#getConstraint_OwningTransition())
[`ProtocolTransition.getPostCondition()`](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html#getPostCondition())
Model:
opposite="postCondition" ordered="false"
Generated:
setOwningTransition
void setOwningTransition(@CheckForNull
 [ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html) value)
Sets the value of the '[`*Owning Transition*`](#getOwningTransition())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Transition*' reference.
See Also:
[`getOwningTransition()`](#getOwningTransition())
Generated:
get_protocolTransitionOfPreCondition
@CheckForNull[ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html) get_protocolTransitionOfPreCondition()
Returns the value of the '***protocol Transition Of Pre Condition***' reference.
 It is bidirectional and its opposite is
 '[`*Pre Condition*`](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html#getPreCondition())'.
 begin-user-doc 
If the meaning of the '*protocol Transition Of Pre Condition*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*protocol Transition Of Pre Condition*' reference.
See Also:
[`set_protocolTransitionOfPreCondition(ProtocolTransition)`](#set_protocolTransitionOfPreCondition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition))
[`UMLPackage.getConstraint__protocolTransitionOfPreCondition()`](../../metadata/UMLPackage.html#getConstraint__protocolTransitionOfPreCondition())
[`ProtocolTransition.getPreCondition()`](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html#getPreCondition())
Model:
opposite="preCondition" ordered="false"
Generated:
set_protocolTransitionOfPreCondition
void set_protocolTransitionOfPreCondition(@CheckForNull
 [ProtocolTransition](../../statemachines/mdprotocolstatemachines/ProtocolTransition.html) value)
Sets the value of the
 '[`*protocol Transition Of Pre Condition*`](#get_protocolTransitionOfPreCondition())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*protocol Transition Of Pre Condition*' reference.
See Also:
[`get_protocolTransitionOfPreCondition()`](#get_protocolTransitionOfPreCondition())
Generated:
get_behaviorOfPrecondition
@CheckForNull[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) get_behaviorOfPrecondition()
Returns the value of the '***behavior Of Precondition***' reference.
 It is bidirectional and its opposite is '[`*Precondition*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPrecondition())'.
 begin-user-doc 
If the meaning of the '*behavior Of Precondition*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*behavior Of Precondition*' reference.
See Also:
[`set_behaviorOfPrecondition(Behavior)`](#set_behaviorOfPrecondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))
[`UMLPackage.getConstraint__behaviorOfPrecondition()`](../../metadata/UMLPackage.html#getConstraint__behaviorOfPrecondition())
[`Behavior.getPrecondition()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPrecondition())
Model:
opposite="precondition" ordered="false"
Generated:
set_behaviorOfPrecondition
void set_behaviorOfPrecondition(@CheckForNull
 [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)
Sets the value of the '[`*behavior Of Precondition*`](#get_behaviorOfPrecondition())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*behavior Of Precondition*' reference.
See Also:
[`get_behaviorOfPrecondition()`](#get_behaviorOfPrecondition())
Generated:
get_behaviorOfPostcondition
@CheckForNull[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) get_behaviorOfPostcondition()
Returns the value of the '***behavior Of Postcondition***' reference.
 It is bidirectional and its opposite is
 '[`*Postcondition*`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPostcondition())'.
 begin-user-doc 
If the meaning of the '*behavior Of Postcondition*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*behavior Of Postcondition*' reference.
See Also:
[`set_behaviorOfPostcondition(Behavior)`](#set_behaviorOfPostcondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))
[`UMLPackage.getConstraint__behaviorOfPostcondition()`](../../metadata/UMLPackage.html#getConstraint__behaviorOfPostcondition())
[`Behavior.getPostcondition()`](../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPostcondition())
Model:
opposite="postcondition" ordered="false"
Generated:
set_behaviorOfPostcondition
void set_behaviorOfPostcondition(@CheckForNull
 [Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html) value)
Sets the value of the '[`*behavior Of Postcondition*`](#get_behaviorOfPostcondition())'
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*behavior Of Postcondition*' reference.
See Also:
[`get_behaviorOfPostcondition()`](#get_behaviorOfPostcondition())
Generated:
get_actionOfLocalPrecondition
@CheckForNull[Action](../../actions/mdbasicactions/Action.html) get_actionOfLocalPrecondition()
Returns the value of the '***action Of Local Precondition***' container reference.
 It is bidirectional and its opposite is '[`*Local Precondition*`](../../actions/mdbasicactions/Action.html#getLocalPrecondition())'.
 begin-user-doc 
If the meaning of the '*action Of Local Precondition*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*action Of Local Precondition*' container reference.
See Also:
[`set_actionOfLocalPrecondition(Action)`](#set_actionOfLocalPrecondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))
[`UMLPackage.getConstraint__actionOfLocalPrecondition()`](../../metadata/UMLPackage.html#getConstraint__actionOfLocalPrecondition())
[`Action.getLocalPrecondition()`](../../actions/mdbasicactions/Action.html#getLocalPrecondition())
Model:
opposite="localPrecondition" transient="false" ordered="false"
Generated:
set_actionOfLocalPrecondition
void set_actionOfLocalPrecondition(@CheckForNull
 [Action](../../actions/mdbasicactions/Action.html) value)
Sets the value of the '[`*action Of Local Precondition*`](#get_actionOfLocalPrecondition())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*action Of Local Precondition*' container reference.
See Also:
[`get_actionOfLocalPrecondition()`](#get_actionOfLocalPrecondition())
Generated:
get_actionOfLocalPostcondition
@CheckForNull[Action](../../actions/mdbasicactions/Action.html) get_actionOfLocalPostcondition()
Returns the value of the '***action Of Local Postcondition***' container reference.
 It is bidirectional and its opposite is '[`*Local Postcondition*`](../../actions/mdbasicactions/Action.html#getLocalPostcondition())'.
 begin-user-doc 
If the meaning of the '*action Of Local Postcondition*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*action Of Local Postcondition*' container reference.
See Also:
[`set_actionOfLocalPostcondition(Action)`](#set_actionOfLocalPostcondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))
[`UMLPackage.getConstraint__actionOfLocalPostcondition()`](../../metadata/UMLPackage.html#getConstraint__actionOfLocalPostcondition())
[`Action.getLocalPostcondition()`](../../actions/mdbasicactions/Action.html#getLocalPostcondition())
Model:
opposite="localPostcondition" transient="false" ordered="false"
Generated:
set_actionOfLocalPostcondition
void set_actionOfLocalPostcondition(@CheckForNull
 [Action](../../actions/mdbasicactions/Action.html) value)
Sets the value of the '[`*action Of Local Postcondition*`](#get_actionOfLocalPostcondition())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*action Of Local Postcondition*' container reference.
See Also:
[`get_actionOfLocalPostcondition()`](#get_actionOfLocalPostcondition())
Generated:
getPreContext
@CheckForNull[Operation](Operation.html) getPreContext()
Returns the value of the '***Pre Context***' reference.
 It is bidirectional and its opposite is '[`*Precondition*`](Operation.html#getPrecondition())'.
 begin-user-doc 
If the meaning of the '*Pre Context*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Pre Context*' reference.
See Also:
[`setPreContext(Operation)`](#setPreContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))
[`UMLPackage.getConstraint_PreContext()`](../../metadata/UMLPackage.html#getConstraint_PreContext())
[`Operation.getPrecondition()`](Operation.html#getPrecondition())
Model:
opposite="precondition" ordered="false"
Generated:
setPreContext
void setPreContext(@CheckForNull
 [Operation](Operation.html) value)
Sets the value of the '[`*Pre Context*`](#getPreContext())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Pre Context*' reference.
See Also:
[`getPreContext()`](#getPreContext())
Generated:
getPostContext
@CheckForNull[Operation](Operation.html) getPostContext()
Returns the value of the '***Post Context***' reference.
 It is bidirectional and its opposite is '[`*Postcondition*`](Operation.html#getPostcondition())'.
 begin-user-doc 
If the meaning of the '*Post Context*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Post Context*' reference.
See Also:
[`setPostContext(Operation)`](#setPostContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))
[`UMLPackage.getConstraint_PostContext()`](../../metadata/UMLPackage.html#getConstraint_PostContext())
[`Operation.getPostcondition()`](Operation.html#getPostcondition())
Model:
opposite="postcondition" ordered="false"
Generated:
setPostContext
void setPostContext(@CheckForNull
 [Operation](Operation.html) value)
Sets the value of the '[`*Post Context*`](#getPostContext())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Post Context*' reference.
See Also:
[`getPostContext()`](#getPostContext())
Generated:
get_extendOfCondition
@CheckForNull[Extend](../../mdusecases/Extend.html) get_extendOfCondition()
Returns the value of the '***extend Of Condition***' container reference.
 It is bidirectional and its opposite is '[`*Condition*`](../../mdusecases/Extend.html#getCondition())'.
 begin-user-doc 
If the meaning of the '*extend Of Condition*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*extend Of Condition*' container reference.
See Also:
[`set_extendOfCondition(Extend)`](#set_extendOfCondition(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend))
[`UMLPackage.getConstraint__extendOfCondition()`](../../metadata/UMLPackage.html#getConstraint__extendOfCondition())
[`Extend.getCondition()`](../../mdusecases/Extend.html#getCondition())
Model:
opposite="condition" transient="false" ordered="false"
Generated:
set_extendOfCondition
void set_extendOfCondition(@CheckForNull
 [Extend](../../mdusecases/Extend.html) value)
Sets the value of the '[`*extend Of Condition*`](#get_extendOfCondition())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*extend Of Condition*' container reference.
See Also:
[`get_extendOfCondition()`](#get_extendOfCondition())
Generated:
hasConstrainedElement
boolean hasConstrainedElement()
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
<h1 class="title" title="Interface Constraint">Interface Constraint</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></code>, <code><a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">Constraint</span><span class="extends-implements">
extends <a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Constraint</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A Constraint is a condition or restriction expressed in natural language text or in a machine readable language for the purpose of declaring some of the semantics
 of an Element or set of Elements.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getConstrainedElement()"><code><em>Constrained Element</em></code></a></li>
<li><a href="#getContext()"><code><em>Context</em></code></a></li>
<li><a href="#getSpecification()"><code><em>Specification</em></code></a></li>
<li><a href="#getOwningState()"><code><em>Owning State</em></code></a></li>
<li><a href="#get_actionOfLocalPostcondition()"><code><em>action Of Local Postcondition</em></code></a></li>
<li><a href="#get_extendOfCondition()"><code><em>extend Of Condition</em></code></a></li>
<li><a href="#getOwningTransition()"><code><em>Owning Transition</em></code></a></li>
<li><a href="#get_protocolTransitionOfPreCondition()"><code><em>protocol Transition Of Pre Condition</em></code></a></li>
<li><a href="#get_parameterSetOfCondition()"><code><em>parameter Set Of Condition</em></code></a></li>
<li><a href="#get_messageOfGuard()"><code><em>message Of Guard</em></code></a></li>
<li><a href="#getBodyContext()"><code><em>Body Context</em></code></a></li>
<li><a href="#getPostContext()"><code><em>Post Context</em></code></a></li>
<li><a href="#getPreContext()"><code><em>Pre Context</em></code></a></li>
<li><a href="#get_behaviorOfPostcondition()"><code><em>behavior Of Postcondition</em></code></a></li>
<li><a href="#get_behaviorOfPrecondition()"><code><em>behavior Of Precondition</em></code></a></li>
<li><a href="#get_stateInvariantOfInvariant()"><code><em>state Invariant Of Invariant</em></code></a></li>
<li><a href="#get_actionOfLocalPrecondition()"><code><em>action Of Local Precondition</em></code></a></li>
<li><a href="#get_transitionOfGuard()"><code><em>transition Of Guard</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getConstraint()"><code>UMLPackage.getConstraint()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_actionOfLocalPostcondition()">get_actionOfLocalPostcondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>action Of Local Postcondition</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_actionOfLocalPrecondition()">get_actionOfLocalPrecondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>action Of Local Precondition</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_behaviorOfPostcondition()">get_behaviorOfPostcondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>behavior Of Postcondition</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_behaviorOfPrecondition()">get_behaviorOfPrecondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>behavior Of Precondition</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_extendOfCondition()">get_extendOfCondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>extend Of Condition</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_messageOfGuard()">get_messageOfGuard</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>message Of Guard</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_parameterSetOfCondition()">get_parameterSetOfCondition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>parameter Set Of Condition</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_protocolTransitionOfPreCondition()">get_protocolTransitionOfPreCondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>protocol Transition Of Pre Condition</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_stateInvariantOfInvariant()">get_stateInvariantOfInvariant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>state Invariant Of Invariant</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_transitionOfGuard()">get_transitionOfGuard</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>transition Of Guard</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBodyContext()">getBodyContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Body Context</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConstrainedElement()">getConstrainedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Constrained Element</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Context</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningState()">getOwningState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning State</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningTransition()">getOwningTransition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Transition</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPostContext()">getPostContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Post Context</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPreContext()">getPreContext</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Pre Context</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSpecification()">getSpecification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Specification</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasConstrainedElement()">hasConstrainedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_actionOfLocalPostcondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">set_actionOfLocalPostcondition</a><wbr/>(<a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_actionOfLocalPostcondition()"><code><em>action Of Local Postcondition</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_actionOfLocalPrecondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">set_actionOfLocalPrecondition</a><wbr/>(<a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_actionOfLocalPrecondition()"><code><em>action Of Local Precondition</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_behaviorOfPostcondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">set_behaviorOfPostcondition</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_behaviorOfPostcondition()"><code><em>behavior Of Postcondition</em></code></a>'
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_behaviorOfPrecondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">set_behaviorOfPrecondition</a><wbr/>(<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_behaviorOfPrecondition()"><code><em>behavior Of Precondition</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_extendOfCondition(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend)">set_extendOfCondition</a><wbr/>(<a href="../../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_extendOfCondition()"><code><em>extend Of Condition</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_messageOfGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfGuard</a><wbr/>(<a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_messageOfGuard()"><code><em>message Of Guard</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_parameterSetOfCondition(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet)">set_parameterSetOfCondition</a><wbr/>(<a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_parameterSetOfCondition()"><code><em>parameter Set Of Condition</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_protocolTransitionOfPreCondition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">set_protocolTransitionOfPreCondition</a><wbr/>(<a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_protocolTransitionOfPreCondition()"><code><em>protocol Transition Of Pre Condition</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_stateInvariantOfInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)">set_stateInvariantOfInvariant</a><wbr/>(<a href="../../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_stateInvariantOfInvariant()"><code><em>state Invariant Of Invariant</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_transitionOfGuard(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">set_transitionOfGuard</a><wbr/>(<a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_transitionOfGuard()"><code><em>transition Of Guard</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBodyContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">setBodyContext</a><wbr/>(<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getBodyContext()"><code><em>Body Context</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setContext</a><wbr/>(<a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getContext()"><code><em>Context</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">setOwningState</a><wbr/>(<a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningState()"><code><em>Owning State</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">setOwningTransition</a><wbr/>(<a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningTransition()"><code><em>Owning Transition</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setPostContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">setPostContext</a><wbr/>(<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getPostContext()"><code><em>Post Context</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setPreContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">setPreContext</a><wbr/>(<a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getPreContext()"><code><em>Pre Context</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setSpecification</a><wbr/>(<a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSpecification()"><code><em>Specification</em></code></a>' containment reference.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="Element.html#getOwnedComment()">getOwnedComment</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getSyncElement()">getSyncElement</a>, <a href="Element.html#getTaggedValue()">getTaggedValue</a>, <a href="Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="NamedElement.html#getName()">getName</a>, <a href="NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="NamedElement.html#getNamespace()">getNamespace</a>, <a href="NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="NamedElement.html#setName(java.lang.String)">setName</a>, <a href="NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></h3>
<code><a href="PackageableElement.html#get_componentOfPackagedElement()">get_componentOfPackagedElement</a>, <a href="PackageableElement.html#get_elementImportOfImportedElement()">get_elementImportOfImportedElement</a>, <a href="PackageableElement.html#get_manifestationOfUtilizedElement()">get_manifestationOfUtilizedElement</a>, <a href="PackageableElement.html#getOwningPackage()">getOwningPackage</a>, <a href="PackageableElement.html#getVisibility()">getVisibility</a>, <a href="PackageableElement.html#has_elementImportOfImportedElement()">has_elementImportOfImportedElement</a>, <a href="PackageableElement.html#has_manifestationOfUtilizedElement()">has_manifestationOfUtilizedElement</a>, <a href="PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">set_componentOfPackagedElement</a>, <a href="PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setOwningPackage</a>, <a href="PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.<a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></h3>
<code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()">getOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()">getTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a>, <a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a></code></div>
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
<section class="detail" id="getConstrainedElement()">
<h3>getConstrainedElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getConstrainedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Constrained Element</b></em>' reference list.
 The list contents are of type <a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>.
 It is bidirectional and its opposite is
 '<a href="Element.html#get_constraintOfConstrainedElement()"><code><em>constraint Of Constrained Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ordered set of Elements referenced by this Constraint.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Constrained Element</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getConstraint_ConstrainedElement()"><code>UMLPackage.getConstraint_ConstrainedElement()</code></a></li>
<li><a href="Element.html#get_constraintOfConstrainedElement()"><code>Element.get_constraintOfConstrainedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_constraintOfConstrainedElement"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpecification()">
<h3>getSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></span> <span class="element-name">getSpecification</span>()</div>
<div class="block">Returns the value of the '<em><b>Specification</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="ValueSpecification.html#getOwningConstraint()"><code><em>Owning Constraint</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 A condition that must be true when evaluated in order for the Constraint to be satisfied.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Specification</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)"><code>setSpecification(ValueSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint_Specification()"><code>UMLPackage.getConstraint_Specification()</code></a></li>
<li><a href="ValueSpecification.html#getOwningConstraint()"><code>ValueSpecification.getOwningConstraint()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningConstraint" containment="true" resolveProxies="true" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">
<h3>setSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSpecification()"><code><em>Specification</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Specification</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getSpecification()"><code>getSpecification()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Context</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Namespace.html#getOwnedRule()"><code><em>Owned Rule</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the Namespace that owns the Constraint.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Context</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)"><code>setContext(Namespace)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint_Context()"><code>UMLPackage.getConstraint_Context()</code></a></li>
<li><a href="Namespace.html#getOwnedRule()"><code>Namespace.getOwnedRule()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedRule" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>setContext</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setContext</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getContext()"><code><em>Context</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Context</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getContext()"><code>getContext()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBodyContext()">
<h3>getBodyContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">getBodyContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Body Context</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Operation.html#getBodyCondition()"><code><em>Body Condition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Body Context</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Body Context</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setBodyContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)"><code>setBodyContext(Operation)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint_BodyContext()"><code>UMLPackage.getConstraint_BodyContext()</code></a></li>
<li><a href="Operation.html#getBodyCondition()"><code>Operation.getBodyCondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="bodyCondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBodyContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>setBodyContext</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setBodyContext</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getBodyContext()"><code><em>Body Context</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Body Context</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getBodyContext()"><code>getBodyContext()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_parameterSetOfCondition()">
<h3>get_parameterSetOfCondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a></span> <span class="element-name">get_parameterSetOfCondition</span>()</div>
<div class="block">Returns the value of the '<em><b>parameter Set Of Condition</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdcompleteactivities/ParameterSet.html#getCondition()"><code><em>Condition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>parameter Set Of Condition</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>parameter Set Of Condition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_parameterSetOfCondition(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet)"><code>set_parameterSetOfCondition(ParameterSet)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__parameterSetOfCondition()"><code>UMLPackage.getConstraint__parameterSetOfCondition()</code></a></li>
<li><a href="../../activities/mdcompleteactivities/ParameterSet.html#getCondition()"><code>ParameterSet.getCondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="condition" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_parameterSetOfCondition(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ParameterSet)">
<h3>set_parameterSetOfCondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_parameterSetOfCondition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdcompleteactivities/ParameterSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities">ParameterSet</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_parameterSetOfCondition()"><code><em>parameter Set Of Condition</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>parameter Set Of Condition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_parameterSetOfCondition()"><code>get_parameterSetOfCondition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_messageOfGuard()">
<h3>get_messageOfGuard</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">get_messageOfGuard</span>()</div>
<div class="block">Returns the value of the '<em><b>message Of Guard</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/Message.html#getGuard()"><code><em>Guard</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>message Of Guard</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>message Of Guard</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_messageOfGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)"><code>set_messageOfGuard(Message)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__messageOfGuard()"><code>UMLPackage.getConstraint__messageOfGuard()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/Message.html#getGuard()"><code>Message.getGuard()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="guard" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_messageOfGuard(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>set_messageOfGuard</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_messageOfGuard</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_messageOfGuard()"><code><em>message Of Guard</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>message Of Guard</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_messageOfGuard()"><code>get_messageOfGuard()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_stateInvariantOfInvariant()">
<h3>get_stateInvariantOfInvariant</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a></span> <span class="element-name">get_stateInvariantOfInvariant</span>()</div>
<div class="block">Returns the value of the '<em><b>state Invariant Of Invariant</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/StateInvariant.html#getInvariant()"><code><em>Invariant</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>state Invariant Of Invariant</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>state Invariant Of Invariant</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_stateInvariantOfInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)"><code>set_stateInvariantOfInvariant(StateInvariant)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__stateInvariantOfInvariant()"><code>UMLPackage.getConstraint__stateInvariantOfInvariant()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/StateInvariant.html#getInvariant()"><code>StateInvariant.getInvariant()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="invariant" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_stateInvariantOfInvariant(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.StateInvariant)">
<h3>set_stateInvariantOfInvariant</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_stateInvariantOfInvariant</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdbasicinteractions/StateInvariant.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">StateInvariant</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_stateInvariantOfInvariant()"><code><em>state Invariant Of Invariant</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>state Invariant Of Invariant</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_stateInvariantOfInvariant()"><code>get_stateInvariantOfInvariant()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_transitionOfGuard()">
<h3>get_transitionOfGuard</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a></span> <span class="element-name">get_transitionOfGuard</span>()</div>
<div class="block">Returns the value of the '<em><b>transition Of Guard</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../statemachines/mdbehaviorstatemachines/Transition.html#getGuard()"><code><em>Guard</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>transition Of Guard</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>transition Of Guard</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_transitionOfGuard(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)"><code>set_transitionOfGuard(Transition)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__transitionOfGuard()"><code>UMLPackage.getConstraint__transitionOfGuard()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/Transition.html#getGuard()"><code>Transition.getGuard()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="guard" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_transitionOfGuard(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>set_transitionOfGuard</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_transitionOfGuard</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_transitionOfGuard()"><code><em>transition Of Guard</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>transition Of Guard</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_transitionOfGuard()"><code>get_transitionOfGuard()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningState()">
<h3>getOwningState</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a></span> <span class="element-name">getOwningState</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning State</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../statemachines/mdbehaviorstatemachines/State.html#getStateInvariant()"><code><em>State Invariant</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning State</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning State</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)"><code>setOwningState(State)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint_OwningState()"><code>UMLPackage.getConstraint_OwningState()</code></a></li>
<li><a href="../../statemachines/mdbehaviorstatemachines/State.html#getStateInvariant()"><code>State.getStateInvariant()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="stateInvariant" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningState(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>setOwningState</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningState</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningState()"><code><em>Owning State</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning State</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningState()"><code>getOwningState()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningTransition()">
<h3>getOwningTransition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></span> <span class="element-name">getOwningTransition</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Transition</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html#getPostCondition()"><code><em>Post Condition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Transition</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Transition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)"><code>setOwningTransition(ProtocolTransition)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint_OwningTransition()"><code>UMLPackage.getConstraint_OwningTransition()</code></a></li>
<li><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html#getPostCondition()"><code>ProtocolTransition.getPostCondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="postCondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">
<h3>setOwningTransition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningTransition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningTransition()"><code><em>Owning Transition</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Transition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningTransition()"><code>getOwningTransition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_protocolTransitionOfPreCondition()">
<h3>get_protocolTransitionOfPreCondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a></span> <span class="element-name">get_protocolTransitionOfPreCondition</span>()</div>
<div class="block">Returns the value of the '<em><b>protocol Transition Of Pre Condition</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html#getPreCondition()"><code><em>Pre Condition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>protocol Transition Of Pre Condition</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>protocol Transition Of Pre Condition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_protocolTransitionOfPreCondition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)"><code>set_protocolTransitionOfPreCondition(ProtocolTransition)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__protocolTransitionOfPreCondition()"><code>UMLPackage.getConstraint__protocolTransitionOfPreCondition()</code></a></li>
<li><a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html#getPreCondition()"><code>ProtocolTransition.getPreCondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="preCondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_protocolTransitionOfPreCondition(com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines.ProtocolTransition)">
<h3>set_protocolTransitionOfPreCondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_protocolTransitionOfPreCondition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../statemachines/mdprotocolstatemachines/ProtocolTransition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolTransition</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_protocolTransitionOfPreCondition()"><code><em>protocol Transition Of Pre Condition</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>protocol Transition Of Pre Condition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_protocolTransitionOfPreCondition()"><code>get_protocolTransitionOfPreCondition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_behaviorOfPrecondition()">
<h3>get_behaviorOfPrecondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">get_behaviorOfPrecondition</span>()</div>
<div class="block">Returns the value of the '<em><b>behavior Of Precondition</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPrecondition()"><code><em>Precondition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>behavior Of Precondition</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>behavior Of Precondition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_behaviorOfPrecondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)"><code>set_behaviorOfPrecondition(Behavior)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__behaviorOfPrecondition()"><code>UMLPackage.getConstraint__behaviorOfPrecondition()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPrecondition()"><code>Behavior.getPrecondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="precondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_behaviorOfPrecondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>set_behaviorOfPrecondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_behaviorOfPrecondition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_behaviorOfPrecondition()"><code><em>behavior Of Precondition</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>behavior Of Precondition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_behaviorOfPrecondition()"><code>get_behaviorOfPrecondition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_behaviorOfPostcondition()">
<h3>get_behaviorOfPostcondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></span> <span class="element-name">get_behaviorOfPostcondition</span>()</div>
<div class="block">Returns the value of the '<em><b>behavior Of Postcondition</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPostcondition()"><code><em>Postcondition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>behavior Of Postcondition</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>behavior Of Postcondition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_behaviorOfPostcondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)"><code>set_behaviorOfPostcondition(Behavior)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__behaviorOfPostcondition()"><code>UMLPackage.getConstraint__behaviorOfPostcondition()</code></a></li>
<li><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html#getPostcondition()"><code>Behavior.getPostcondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="postcondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_behaviorOfPostcondition(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>set_behaviorOfPostcondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_behaviorOfPostcondition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_behaviorOfPostcondition()"><code><em>behavior Of Postcondition</em></code></a>'
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>behavior Of Postcondition</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_behaviorOfPostcondition()"><code>get_behaviorOfPostcondition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_actionOfLocalPrecondition()">
<h3>get_actionOfLocalPrecondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></span> <span class="element-name">get_actionOfLocalPrecondition</span>()</div>
<div class="block">Returns the value of the '<em><b>action Of Local Precondition</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/Action.html#getLocalPrecondition()"><code><em>Local Precondition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>action Of Local Precondition</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>action Of Local Precondition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_actionOfLocalPrecondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)"><code>set_actionOfLocalPrecondition(Action)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__actionOfLocalPrecondition()"><code>UMLPackage.getConstraint__actionOfLocalPrecondition()</code></a></li>
<li><a href="../../actions/mdbasicactions/Action.html#getLocalPrecondition()"><code>Action.getLocalPrecondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="localPrecondition" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_actionOfLocalPrecondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">
<h3>set_actionOfLocalPrecondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_actionOfLocalPrecondition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_actionOfLocalPrecondition()"><code><em>action Of Local Precondition</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>action Of Local Precondition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_actionOfLocalPrecondition()"><code>get_actionOfLocalPrecondition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_actionOfLocalPostcondition()">
<h3>get_actionOfLocalPostcondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></span> <span class="element-name">get_actionOfLocalPostcondition</span>()</div>
<div class="block">Returns the value of the '<em><b>action Of Local Postcondition</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/Action.html#getLocalPostcondition()"><code><em>Local Postcondition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>action Of Local Postcondition</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>action Of Local Postcondition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_actionOfLocalPostcondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)"><code>set_actionOfLocalPostcondition(Action)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__actionOfLocalPostcondition()"><code>UMLPackage.getConstraint__actionOfLocalPostcondition()</code></a></li>
<li><a href="../../actions/mdbasicactions/Action.html#getLocalPostcondition()"><code>Action.getLocalPostcondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="localPostcondition" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_actionOfLocalPostcondition(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">
<h3>set_actionOfLocalPostcondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_actionOfLocalPostcondition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../actions/mdbasicactions/Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_actionOfLocalPostcondition()"><code><em>action Of Local Postcondition</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>action Of Local Postcondition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_actionOfLocalPostcondition()"><code>get_actionOfLocalPostcondition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPreContext()">
<h3>getPreContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">getPreContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Pre Context</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Operation.html#getPrecondition()"><code><em>Precondition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Pre Context</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Pre Context</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setPreContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)"><code>setPreContext(Operation)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint_PreContext()"><code>UMLPackage.getConstraint_PreContext()</code></a></li>
<li><a href="Operation.html#getPrecondition()"><code>Operation.getPrecondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="precondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>setPreContext</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setPreContext</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getPreContext()"><code><em>Pre Context</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Pre Context</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getPreContext()"><code>getPreContext()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPostContext()">
<h3>getPostContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">getPostContext</span>()</div>
<div class="block">Returns the value of the '<em><b>Post Context</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Operation.html#getPostcondition()"><code><em>Postcondition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Post Context</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Post Context</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setPostContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)"><code>setPostContext(Operation)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint_PostContext()"><code>UMLPackage.getConstraint_PostContext()</code></a></li>
<li><a href="Operation.html#getPostcondition()"><code>Operation.getPostcondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="postcondition" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPostContext(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>setPostContext</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setPostContext</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getPostContext()"><code><em>Post Context</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Post Context</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getPostContext()"><code>getPostContext()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_extendOfCondition()">
<h3>get_extendOfCondition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a></span> <span class="element-name">get_extendOfCondition</span>()</div>
<div class="block">Returns the value of the '<em><b>extend Of Condition</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../mdusecases/Extend.html#getCondition()"><code><em>Condition</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>extend Of Condition</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>extend Of Condition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_extendOfCondition(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend)"><code>set_extendOfCondition(Extend)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getConstraint__extendOfCondition()"><code>UMLPackage.getConstraint__extendOfCondition()</code></a></li>
<li><a href="../../mdusecases/Extend.html#getCondition()"><code>Extend.getCondition()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="condition" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_extendOfCondition(com.nomagic.uml2.ext.magicdraw.mdusecases.Extend)">
<h3>set_extendOfCondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_extendOfCondition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../mdusecases/Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_extendOfCondition()"><code><em>extend Of Condition</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>extend Of Condition</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_extendOfCondition()"><code>get_extendOfCondition()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasConstrainedElement()">
<h3>hasConstrainedElement</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasConstrainedElement</span>()
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
