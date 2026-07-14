# JAVA OPENAPI: ValueSpecification (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html`
- source_sha256: `76fcb08a8782a25416910ec57e4b47a2c0c272c5a380211e0d3c480d93d486db`
- captured_utc: `2026-07-14T16:53:05.877559+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface ValueSpecification

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TypedElement](TypedElement.html)`

All Known Subinterfaces:
`[Duration](../../commonbehaviors/mdsimpletime/Duration.html)`, `[DurationInterval](../../commonbehaviors/mdsimpletime/DurationInterval.html)`, `[ElementValue](ElementValue.html)`, `[Expression](Expression.html)`, `[InstanceValue](InstanceValue.html)`, `[Interval](../../commonbehaviors/mdsimpletime/Interval.html)`, `[LiteralBoolean](LiteralBoolean.html)`, `[LiteralInteger](LiteralInteger.html)`, `[LiteralNull](LiteralNull.html)`, `[LiteralReal](LiteralReal.html)`, `[LiteralSpecification](LiteralSpecification.html)`, `[LiteralString](LiteralString.html)`, `[LiteralUnlimitedNatural](LiteralUnlimitedNatural.html)`, `[OpaqueExpression](OpaqueExpression.html)`, `[StringExpression](../../auxiliaryconstructs/mdtemplates/StringExpression.html)`, `[TimeExpression](../../commonbehaviors/mdsimpletime/TimeExpression.html)`, `[TimeInterval](../../commonbehaviors/mdsimpletime/TimeInterval.html)`

public interfaceValueSpecificationextends [PackageableElement](PackageableElement.html), [TypedElement](TypedElement.html)

begin-user-doc 
 A representation of the model object '***Value Specification***'.
 end-user-doc 
begin-model-doc 
 A ValueSpecification is the specification of a (possibly empty) set of values. A ValueSpecification is a ParameterableElement that may be exposed as a formal
 TemplateParameter and provided as the actual parameter in the binding of a template.
 end-model-doc 
The following features are supported:
 [`*lifeline Of Selector*`](#get_lifelineOfSelector())
[`*activity Edge Of Guard*`](#get_activityEdgeOfGuard())
[`*Owning Constraint*`](#getOwningConstraint())
[`*Owning Slot*`](#getOwningSlot())
[`*Owning Property*`](#getOwningProperty())
[`*message Of Argument*`](#get_messageOfArgument())
[`*message Of Target*`](#get_messageOfTarget())
[`*value Specification Action Of Value*`](#get_valueSpecificationActionOfValue())
[`*interaction Constraint Of Maxint*`](#get_interactionConstraintOfMaxint())
[`*interaction Constraint Of Minint*`](#get_interactionConstraintOfMinint())
[`*interaction Use Of Argument*`](#get_interactionUseOfArgument())
[`*interaction Use Of Return Value*`](#get_interactionUseOfReturnValue())
[`*object Node Of Upper Bound*`](#get_objectNodeOfUpperBound())
[`*activity Edge Of Weight*`](#get_activityEdgeOfWeight())
[`*value Pin Of Value*`](#get_valuePinOfValue())
[`*interval Of Max*`](#get_intervalOfMax())
[`*interval Of Min*`](#get_intervalOfMin())
[`*Owning Parameter*`](#getOwningParameter())
[`*change Event Of Change Expression*`](#get_changeEventOfChangeExpression())
[`*join Node Of Join Spec*`](#get_joinNodeOfJoinSpec())
[`*Owning Instance Spec*`](#getOwningInstanceSpec())
[`*Owning Upper*`](#getOwningUpper())
[`*duration Of Expr*`](#get_durationOfExpr())
[`*time Expression Of Expr*`](#get_timeExpressionOfExpr())
[`*Expression*`](#getExpression())
[`*Owning Lower*`](#getOwningLower())

See Also:
[`UMLPackage.getValueSpecification()`](../../metadata/UMLPackage.html#getValueSpecification())
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
`[ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html)`
`[get_activityEdgeOfGuard](#get_activityEdgeOfGuard())()`
Returns the value of the '***activity Edge Of Guard***' container reference.
`[ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html)`
`[get_activityEdgeOfWeight](#get_activityEdgeOfWeight())()`
Returns the value of the '***activity Edge Of Weight***' container reference.
`[ChangeEvent](../../commonbehaviors/mdcommunications/ChangeEvent.html)`
`[get_changeEventOfChangeExpression](#get_changeEventOfChangeExpression())()`
Returns the value of the '***change Event Of Change Expression***' container reference.
`[Duration](../../commonbehaviors/mdsimpletime/Duration.html)`
`[get_durationOfExpr](#get_durationOfExpr())()`
Returns the value of the '***duration Of Expr***' container reference.
`[InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html)`
`[get_interactionConstraintOfMaxint](#get_interactionConstraintOfMaxint())()`
Returns the value of the '***interaction Constraint Of Maxint***' container reference.
`[InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html)`
`[get_interactionConstraintOfMinint](#get_interactionConstraintOfMinint())()`
Returns the value of the '***interaction Constraint Of Minint***' container reference.
`[InteractionUse](../../interactions/mdfragments/InteractionUse.html)`
`[get_interactionUseOfArgument](#get_interactionUseOfArgument())()`
Returns the value of the '***interaction Use Of Argument***' container reference.
`[InteractionUse](../../interactions/mdfragments/InteractionUse.html)`
`[get_interactionUseOfReturnValue](#get_interactionUseOfReturnValue())()`
Returns the value of the '***interaction Use Of Return Value***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interval](../../commonbehaviors/mdsimpletime/Interval.html)>`
`[get_intervalOfMax](#get_intervalOfMax())()`
Returns the value of the '***interval Of Max***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interval](../../commonbehaviors/mdsimpletime/Interval.html)>`
`[get_intervalOfMin](#get_intervalOfMin())()`
Returns the value of the '***interval Of Min***' reference list.
`[JoinNode](../../activities/mdintermediateactivities/JoinNode.html)`
`[get_joinNodeOfJoinSpec](#get_joinNodeOfJoinSpec())()`
Returns the value of the '***join Node Of Join Spec***' container reference.
`[Lifeline](../../interactions/mdbasicinteractions/Lifeline.html)`
`[get_lifelineOfSelector](#get_lifelineOfSelector())()`
Returns the value of the '***lifeline Of Selector***' container reference.
`[Message](../../interactions/mdbasicinteractions/Message.html)`
`[get_messageOfArgument](#get_messageOfArgument())()`
Returns the value of the '***message Of Argument***' container reference.
`[Message](../../interactions/mdbasicinteractions/Message.html)`
`[get_messageOfTarget](#get_messageOfTarget())()`
Returns the value of the '***message Of Target***' container reference.
`[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)`
`[get_objectNodeOfUpperBound](#get_objectNodeOfUpperBound())()`
Returns the value of the '***object Node Of Upper Bound***' container reference.
`[TimeExpression](../../commonbehaviors/mdsimpletime/TimeExpression.html)`
`[get_timeExpressionOfExpr](#get_timeExpressionOfExpr())()`
Returns the value of the '***time Expression Of Expr***' container reference.
`[ValuePin](../../actions/mdbasicactions/ValuePin.html)`
`[get_valuePinOfValue](#get_valuePinOfValue())()`
Returns the value of the '***value Pin Of Value***' container reference.
`[ValueSpecificationAction](../../actions/mdintermediateactions/ValueSpecificationAction.html)`
`[get_valueSpecificationActionOfValue](#get_valueSpecificationActionOfValue())()`
Returns the value of the '***value Specification Action Of Value***' container reference.
`[Expression](Expression.html)`
`[getExpression](#getExpression())()`
Returns the value of the '***Expression***' container reference.
`[Constraint](Constraint.html)`
`[getOwningConstraint](#getOwningConstraint())()`
Returns the value of the '***Owning Constraint***' container reference.
`[InstanceSpecification](InstanceSpecification.html)`
`[getOwningInstanceSpec](#getOwningInstanceSpec())()`
Returns the value of the '***Owning Instance Spec***' container reference.
`[MultiplicityElement](MultiplicityElement.html)`
`[getOwningLower](#getOwningLower())()`
Returns the value of the '***Owning Lower***' container reference.
`[Parameter](Parameter.html)`
`[getOwningParameter](#getOwningParameter())()`
Returns the value of the '***Owning Parameter***' container reference.
`[Property](Property.html)`
`[getOwningProperty](#getOwningProperty())()`
Returns the value of the '***Owning Property***' container reference.
`[Slot](Slot.html)`
`[getOwningSlot](#getOwningSlot())()`
Returns the value of the '***Owning Slot***' container reference.
`[MultiplicityElement](MultiplicityElement.html)`
`[getOwningUpper](#getOwningUpper())()`
Returns the value of the '***Owning Upper***' container reference.
`boolean`
`[has_intervalOfMax](#has_intervalOfMax())()`

`boolean`
`[has_intervalOfMin](#has_intervalOfMin())()`

`void`
`[set_activityEdgeOfGuard](#set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge))([ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html) value)`
Sets the value of the '[`*activity Edge Of Guard*`](#get_activityEdgeOfGuard())'
 container reference.
`void`
`[set_activityEdgeOfWeight](#set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge))([ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html) value)`
Sets the value of the '[`*activity Edge Of Weight*`](#get_activityEdgeOfWeight())'
 container reference.
`void`
`[set_changeEventOfChangeExpression](#set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent))([ChangeEvent](../../commonbehaviors/mdcommunications/ChangeEvent.html) value)`
Sets the value of the
 '[`*change Event Of Change Expression*`](#get_changeEventOfChangeExpression())'
 container reference.
`void`
`[set_durationOfExpr](#set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration))([Duration](../../commonbehaviors/mdsimpletime/Duration.html) value)`
Sets the value of the '[`*duration Of Expr*`](#get_durationOfExpr())' container
 reference.
`void`
`[set_interactionConstraintOfMaxint](#set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint))([InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html) value)`
Sets the value of the
 '[`*interaction Constraint Of Maxint*`](#get_interactionConstraintOfMaxint())'
 container reference.
`void`
`[set_interactionConstraintOfMinint](#set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint))([InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html) value)`
Sets the value of the
 '[`*interaction Constraint Of Minint*`](#get_interactionConstraintOfMinint())'
 container reference.
`void`
`[set_interactionUseOfArgument](#set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse))([InteractionUse](../../interactions/mdfragments/InteractionUse.html) value)`
Sets the value of the
 '[`*interaction Use Of Argument*`](#get_interactionUseOfArgument())' container
 reference.
`void`
`[set_interactionUseOfReturnValue](#set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse))([InteractionUse](../../interactions/mdfragments/InteractionUse.html) value)`
Sets the value of the
 '[`*interaction Use Of Return Value*`](#get_interactionUseOfReturnValue())' container
 reference.
`void`
`[set_joinNodeOfJoinSpec](#set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode))([JoinNode](../../activities/mdintermediateactivities/JoinNode.html) value)`
Sets the value of the '[`*join Node Of Join Spec*`](#get_joinNodeOfJoinSpec())'
 container reference.
`void`
`[set_lifelineOfSelector](#set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))([Lifeline](../../interactions/mdbasicinteractions/Lifeline.html) value)`
Sets the value of the '[`*lifeline Of Selector*`](#get_lifelineOfSelector())' container
 reference.
`void`
`[set_messageOfArgument](#set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../interactions/mdbasicinteractions/Message.html) value)`
Sets the value of the '[`*message Of Argument*`](#get_messageOfArgument())' container
 reference.
`void`
`[set_messageOfTarget](#set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))([Message](../../interactions/mdbasicinteractions/Message.html) value)`
Sets the value of the '[`*message Of Target*`](#get_messageOfTarget())' container
 reference.
`void`
`[set_objectNodeOfUpperBound](#set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode))([ObjectNode](../../activities/mdbasicactivities/ObjectNode.html) value)`
Sets the value of the '[`*object Node Of Upper Bound*`](#get_objectNodeOfUpperBound())'
 container reference.
`void`
`[set_timeExpressionOfExpr](#set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression))([TimeExpression](../../commonbehaviors/mdsimpletime/TimeExpression.html) value)`
Sets the value of the '[`*time Expression Of Expr*`](#get_timeExpressionOfExpr())'
 container reference.
`void`
`[set_valuePinOfValue](#set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin))([ValuePin](../../actions/mdbasicactions/ValuePin.html) value)`
Sets the value of the '[`*value Pin Of Value*`](#get_valuePinOfValue())' container
 reference.
`void`
`[set_valueSpecificationActionOfValue](#set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction))([ValueSpecificationAction](../../actions/mdintermediateactions/ValueSpecificationAction.html) value)`
Sets the value of the '[`*value Specification
 Action Of Value*`](#get_valueSpecificationActionOfValue())' container reference.
`void`
`[setExpression](#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression))([Expression](Expression.html) value)`
Sets the value of the '[`*Expression*`](#getExpression())' container reference.
`void`
`[setOwningConstraint](#setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Constraint](Constraint.html) value)`
Sets the value of the '[`*Owning Constraint*`](#getOwningConstraint())' container
 reference.
`void`
`[setOwningInstanceSpec](#setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))([InstanceSpecification](InstanceSpecification.html) value)`
Sets the value of the '[`*Owning Instance Spec*`](#getOwningInstanceSpec())' container
 reference.
`void`
`[setOwningLower](#setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))([MultiplicityElement](MultiplicityElement.html) value)`
Sets the value of the '[`*Owning Lower*`](#getOwningLower())' container reference.
`void`
`[setOwningParameter](#setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter))([Parameter](Parameter.html) value)`
Sets the value of the '[`*Owning Parameter*`](#getOwningParameter())' container
 reference.
`void`
`[setOwningProperty](#setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))([Property](Property.html) value)`
Sets the value of the '[`*Owning Property*`](#getOwningProperty())' container reference.
`void`
`[setOwningSlot](#setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot))([Slot](Slot.html) value)`
Sets the value of the '[`*Owning Slot*`](#getOwningSlot())' container reference.
`void`
`[setOwningUpper](#setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))([MultiplicityElement](MultiplicityElement.html) value)`
Sets the value of the '[`*Owning Upper*`](#getOwningUpper())' container reference.
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
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[TypedElement](TypedElement.html)
`[getType](TypedElement.html#getType()), [setType](TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))`

============ METHOD DETAIL ========== 
Method Details
getOwningConstraint
@CheckForNull[Constraint](Constraint.html) getOwningConstraint()
Returns the value of the '***Owning Constraint***' container reference.
 It is bidirectional and its opposite is '[`*Specification*`](Constraint.html#getSpecification())'.
 begin-user-doc 
If the meaning of the '*Owning Constraint*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Constraint*' container reference.
See Also:
[`setOwningConstraint(Constraint)`](#setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))
[`UMLPackage.getValueSpecification_OwningConstraint()`](../../metadata/UMLPackage.html#getValueSpecification_OwningConstraint())
[`Constraint.getSpecification()`](Constraint.html#getSpecification())
Model:
opposite="specification" transient="false" ordered="false"
Generated:
setOwningConstraint
void setOwningConstraint(@CheckForNull
 [Constraint](Constraint.html) value)
Sets the value of the '[`*Owning Constraint*`](#getOwningConstraint())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Constraint*' container reference.
See Also:
[`getOwningConstraint()`](#getOwningConstraint())
Generated:
getOwningUpper
@CheckForNull[MultiplicityElement](MultiplicityElement.html) getOwningUpper()
Returns the value of the '***Owning Upper***' container reference.
 It is bidirectional and its opposite is '[`*Upper Value*`](MultiplicityElement.html#getUpperValue())'.
 begin-user-doc 
If the meaning of the '*Owning Upper*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Upper*' container reference.
See Also:
[`setOwningUpper(MultiplicityElement)`](#setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))
[`UMLPackage.getValueSpecification_OwningUpper()`](../../metadata/UMLPackage.html#getValueSpecification_OwningUpper())
[`MultiplicityElement.getUpperValue()`](MultiplicityElement.html#getUpperValue())
Model:
opposite="upperValue" transient="false" ordered="false"
Generated:
setOwningUpper
void setOwningUpper(@CheckForNull
 [MultiplicityElement](MultiplicityElement.html) value)
Sets the value of the '[`*Owning Upper*`](#getOwningUpper())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Upper*' container reference.
See Also:
[`getOwningUpper()`](#getOwningUpper())
Generated:
getOwningLower
@CheckForNull[MultiplicityElement](MultiplicityElement.html) getOwningLower()
Returns the value of the '***Owning Lower***' container reference.
 It is bidirectional and its opposite is '[`*Lower Value*`](MultiplicityElement.html#getLowerValue())'.
 begin-user-doc 
If the meaning of the '*Owning Lower*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Lower*' container reference.
See Also:
[`setOwningLower(MultiplicityElement)`](#setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))
[`UMLPackage.getValueSpecification_OwningLower()`](../../metadata/UMLPackage.html#getValueSpecification_OwningLower())
[`MultiplicityElement.getLowerValue()`](MultiplicityElement.html#getLowerValue())
Model:
opposite="lowerValue" transient="false" ordered="false"
Generated:
setOwningLower
void setOwningLower(@CheckForNull
 [MultiplicityElement](MultiplicityElement.html) value)
Sets the value of the '[`*Owning Lower*`](#getOwningLower())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Lower*' container reference.
See Also:
[`getOwningLower()`](#getOwningLower())
Generated:
get_intervalOfMin
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interval](../../commonbehaviors/mdsimpletime/Interval.html)> get_intervalOfMin()
Returns the value of the '***interval Of Min***' reference list.
 The list contents are of type [`Interval`](../../commonbehaviors/mdsimpletime/Interval.html).
 It is bidirectional and its opposite is '[`*Min*`](../../commonbehaviors/mdsimpletime/Interval.html#getMin())'.
 begin-user-doc 
If the meaning of the '*interval Of Min*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interval Of Min*' reference list.
See Also:
[`UMLPackage.getValueSpecification__intervalOfMin()`](../../metadata/UMLPackage.html#getValueSpecification__intervalOfMin())
[`Interval.getMin()`](../../commonbehaviors/mdsimpletime/Interval.html#getMin())
Model:
opposite="min" ordered="false"
Generated:
get_intervalOfMax
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Interval](../../commonbehaviors/mdsimpletime/Interval.html)> get_intervalOfMax()
Returns the value of the '***interval Of Max***' reference list.
 The list contents are of type [`Interval`](../../commonbehaviors/mdsimpletime/Interval.html).
 It is bidirectional and its opposite is '[`*Max*`](../../commonbehaviors/mdsimpletime/Interval.html#getMax())'.
 begin-user-doc 
If the meaning of the '*interval Of Max*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interval Of Max*' reference list.
See Also:
[`UMLPackage.getValueSpecification__intervalOfMax()`](../../metadata/UMLPackage.html#getValueSpecification__intervalOfMax())
[`Interval.getMax()`](../../commonbehaviors/mdsimpletime/Interval.html#getMax())
Model:
opposite="max" ordered="false"
Generated:
get_durationOfExpr
@CheckForNull[Duration](../../commonbehaviors/mdsimpletime/Duration.html) get_durationOfExpr()
Returns the value of the '***duration Of Expr***' container reference.
 It is bidirectional and its opposite is '[`*Expr*`](../../commonbehaviors/mdsimpletime/Duration.html#getExpr())'.
 begin-user-doc 
If the meaning of the '*duration Of Expr*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*duration Of Expr*' container reference.
See Also:
[`set_durationOfExpr(Duration)`](#set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration))
[`UMLPackage.getValueSpecification__durationOfExpr()`](../../metadata/UMLPackage.html#getValueSpecification__durationOfExpr())
[`Duration.getExpr()`](../../commonbehaviors/mdsimpletime/Duration.html#getExpr())
Model:
opposite="expr" transient="false" ordered="false"
Generated:
set_durationOfExpr
void set_durationOfExpr(@CheckForNull
 [Duration](../../commonbehaviors/mdsimpletime/Duration.html) value)
Sets the value of the '[`*duration Of Expr*`](#get_durationOfExpr())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*duration Of Expr*' container reference.
See Also:
[`get_durationOfExpr()`](#get_durationOfExpr())
Generated:
get_timeExpressionOfExpr
@CheckForNull[TimeExpression](../../commonbehaviors/mdsimpletime/TimeExpression.html) get_timeExpressionOfExpr()
Returns the value of the '***time Expression Of Expr***' container reference.
 It is bidirectional and its opposite is '[`*Expr*`](../../commonbehaviors/mdsimpletime/TimeExpression.html#getExpr())'.
 begin-user-doc 
If the meaning of the '*time Expression Of Expr*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*time Expression Of Expr*' container reference.
See Also:
[`set_timeExpressionOfExpr(TimeExpression)`](#set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression))
[`UMLPackage.getValueSpecification__timeExpressionOfExpr()`](../../metadata/UMLPackage.html#getValueSpecification__timeExpressionOfExpr())
[`TimeExpression.getExpr()`](../../commonbehaviors/mdsimpletime/TimeExpression.html#getExpr())
Model:
opposite="expr" transient="false" ordered="false"
Generated:
set_timeExpressionOfExpr
void set_timeExpressionOfExpr(@CheckForNull
 [TimeExpression](../../commonbehaviors/mdsimpletime/TimeExpression.html) value)
Sets the value of the '[`*time Expression Of Expr*`](#get_timeExpressionOfExpr())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*time Expression Of Expr*' container reference.
See Also:
[`get_timeExpressionOfExpr()`](#get_timeExpressionOfExpr())
Generated:
get_messageOfArgument
@CheckForNull[Message](../../interactions/mdbasicinteractions/Message.html) get_messageOfArgument()
Returns the value of the '***message Of Argument***' container reference.
 It is bidirectional and its opposite is '[`*Argument*`](../../interactions/mdbasicinteractions/Message.html#getArgument())'.
 begin-user-doc 
If the meaning of the '*message Of Argument*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*message Of Argument*' container reference.
See Also:
[`set_messageOfArgument(Message)`](#set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))
[`UMLPackage.getValueSpecification__messageOfArgument()`](../../metadata/UMLPackage.html#getValueSpecification__messageOfArgument())
[`Message.getArgument()`](../../interactions/mdbasicinteractions/Message.html#getArgument())
Model:
opposite="argument" transient="false" ordered="false"
Generated:
set_messageOfArgument
void set_messageOfArgument(@CheckForNull
 [Message](../../interactions/mdbasicinteractions/Message.html) value)
Sets the value of the '[`*message Of Argument*`](#get_messageOfArgument())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*message Of Argument*' container reference.
See Also:
[`get_messageOfArgument()`](#get_messageOfArgument())
Generated:
get_joinNodeOfJoinSpec
@CheckForNull[JoinNode](../../activities/mdintermediateactivities/JoinNode.html) get_joinNodeOfJoinSpec()
Returns the value of the '***join Node Of Join Spec***' container reference.
 It is bidirectional and its opposite is '[`*Join Spec*`](../../activities/mdintermediateactivities/JoinNode.html#getJoinSpec())'.
 begin-user-doc 
If the meaning of the '*join Node Of Join Spec*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*join Node Of Join Spec*' container reference.
See Also:
[`set_joinNodeOfJoinSpec(JoinNode)`](#set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode))
[`UMLPackage.getValueSpecification__joinNodeOfJoinSpec()`](../../metadata/UMLPackage.html#getValueSpecification__joinNodeOfJoinSpec())
[`JoinNode.getJoinSpec()`](../../activities/mdintermediateactivities/JoinNode.html#getJoinSpec())
Model:
opposite="joinSpec" transient="false" ordered="false"
Generated:
set_joinNodeOfJoinSpec
void set_joinNodeOfJoinSpec(@CheckForNull
 [JoinNode](../../activities/mdintermediateactivities/JoinNode.html) value)
Sets the value of the '[`*join Node Of Join Spec*`](#get_joinNodeOfJoinSpec())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*join Node Of Join Spec*' container reference.
See Also:
[`get_joinNodeOfJoinSpec()`](#get_joinNodeOfJoinSpec())
Generated:
get_activityEdgeOfGuard
@CheckForNull[ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html) get_activityEdgeOfGuard()
Returns the value of the '***activity Edge Of Guard***' container reference.
 It is bidirectional and its opposite is '[`*Guard*`](../../activities/mdbasicactivities/ActivityEdge.html#getGuard())'.
 begin-user-doc 
If the meaning of the '*activity Edge Of Guard*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*activity Edge Of Guard*' container reference.
See Also:
[`set_activityEdgeOfGuard(ActivityEdge)`](#set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge))
[`UMLPackage.getValueSpecification__activityEdgeOfGuard()`](../../metadata/UMLPackage.html#getValueSpecification__activityEdgeOfGuard())
[`ActivityEdge.getGuard()`](../../activities/mdbasicactivities/ActivityEdge.html#getGuard())
Model:
opposite="guard" transient="false" ordered="false"
Generated:
set_activityEdgeOfGuard
void set_activityEdgeOfGuard(@CheckForNull
 [ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html) value)
Sets the value of the '[`*activity Edge Of Guard*`](#get_activityEdgeOfGuard())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*activity Edge Of Guard*' container reference.
See Also:
[`get_activityEdgeOfGuard()`](#get_activityEdgeOfGuard())
Generated:
get_activityEdgeOfWeight
@CheckForNull[ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html) get_activityEdgeOfWeight()
Returns the value of the '***activity Edge Of Weight***' container reference.
 It is bidirectional and its opposite is '[`*Weight*`](../../activities/mdbasicactivities/ActivityEdge.html#getWeight())'.
 begin-user-doc 
If the meaning of the '*activity Edge Of Weight*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*activity Edge Of Weight*' container reference.
See Also:
[`set_activityEdgeOfWeight(ActivityEdge)`](#set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge))
[`UMLPackage.getValueSpecification__activityEdgeOfWeight()`](../../metadata/UMLPackage.html#getValueSpecification__activityEdgeOfWeight())
[`ActivityEdge.getWeight()`](../../activities/mdbasicactivities/ActivityEdge.html#getWeight())
Model:
opposite="weight" transient="false" ordered="false"
Generated:
set_activityEdgeOfWeight
void set_activityEdgeOfWeight(@CheckForNull
 [ActivityEdge](../../activities/mdbasicactivities/ActivityEdge.html) value)
Sets the value of the '[`*activity Edge Of Weight*`](#get_activityEdgeOfWeight())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*activity Edge Of Weight*' container reference.
See Also:
[`get_activityEdgeOfWeight()`](#get_activityEdgeOfWeight())
Generated:
get_valueSpecificationActionOfValue
@CheckForNull[ValueSpecificationAction](../../actions/mdintermediateactions/ValueSpecificationAction.html) get_valueSpecificationActionOfValue()
Returns the value of the '***value Specification Action Of Value***' container reference.
 It is bidirectional and its opposite is '[`*Value*`](../../actions/mdintermediateactions/ValueSpecificationAction.html#getValue())'.
 begin-user-doc 
If the meaning of the '*value Specification Action Of Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*value Specification Action Of Value*' container reference.
See Also:
[`set_valueSpecificationActionOfValue(ValueSpecificationAction)`](#set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction))
[`UMLPackage.getValueSpecification__valueSpecificationActionOfValue()`](../../metadata/UMLPackage.html#getValueSpecification__valueSpecificationActionOfValue())
[`ValueSpecificationAction.getValue()`](../../actions/mdintermediateactions/ValueSpecificationAction.html#getValue())
Model:
opposite="value" transient="false" ordered="false"
Generated:
set_valueSpecificationActionOfValue
void set_valueSpecificationActionOfValue(@CheckForNull
 [ValueSpecificationAction](../../actions/mdintermediateactions/ValueSpecificationAction.html) value)
Sets the value of the '[`*value Specification
 Action Of Value*`](#get_valueSpecificationActionOfValue())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*value Specification Action Of Value*' container reference.
See Also:
[`get_valueSpecificationActionOfValue()`](#get_valueSpecificationActionOfValue())
Generated:
get_messageOfTarget
@CheckForNull[Message](../../interactions/mdbasicinteractions/Message.html) get_messageOfTarget()
Returns the value of the '***message Of Target***' container reference.
 It is bidirectional and its opposite is '[`*Target*`](../../interactions/mdbasicinteractions/Message.html#getTarget())'.
 begin-user-doc 
If the meaning of the '*message Of Target*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*message Of Target*' container reference.
See Also:
[`set_messageOfTarget(Message)`](#set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message))
[`UMLPackage.getValueSpecification__messageOfTarget()`](../../metadata/UMLPackage.html#getValueSpecification__messageOfTarget())
[`Message.getTarget()`](../../interactions/mdbasicinteractions/Message.html#getTarget())
Model:
opposite="target" transient="false" ordered="false"
Generated:
set_messageOfTarget
void set_messageOfTarget(@CheckForNull
 [Message](../../interactions/mdbasicinteractions/Message.html) value)
Sets the value of the '[`*message Of Target*`](#get_messageOfTarget())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*message Of Target*' container reference.
See Also:
[`get_messageOfTarget()`](#get_messageOfTarget())
Generated:
get_interactionUseOfArgument
@CheckForNull[InteractionUse](../../interactions/mdfragments/InteractionUse.html) get_interactionUseOfArgument()
Returns the value of the '***interaction Use Of Argument***' container reference.
 It is bidirectional and its opposite is '[`*Argument*`](../../interactions/mdfragments/InteractionUse.html#getArgument())'.
 begin-user-doc 
If the meaning of the '*interaction Use Of Argument*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interaction Use Of Argument*' container reference.
See Also:
[`set_interactionUseOfArgument(InteractionUse)`](#set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse))
[`UMLPackage.getValueSpecification__interactionUseOfArgument()`](../../metadata/UMLPackage.html#getValueSpecification__interactionUseOfArgument())
[`InteractionUse.getArgument()`](../../interactions/mdfragments/InteractionUse.html#getArgument())
Model:
opposite="argument" transient="false" ordered="false"
Generated:
set_interactionUseOfArgument
void set_interactionUseOfArgument(@CheckForNull
 [InteractionUse](../../interactions/mdfragments/InteractionUse.html) value)
Sets the value of the
 '[`*interaction Use Of Argument*`](#get_interactionUseOfArgument())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*interaction Use Of Argument*' container reference.
See Also:
[`get_interactionUseOfArgument()`](#get_interactionUseOfArgument())
Generated:
get_interactionUseOfReturnValue
@CheckForNull[InteractionUse](../../interactions/mdfragments/InteractionUse.html) get_interactionUseOfReturnValue()
Returns the value of the '***interaction Use Of Return Value***' container reference.
 It is bidirectional and its opposite is '[`*Return Value*`](../../interactions/mdfragments/InteractionUse.html#getReturnValue())'.
 begin-user-doc 
If the meaning of the '*interaction Use Of Return Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interaction Use Of Return Value*' container reference.
See Also:
[`set_interactionUseOfReturnValue(InteractionUse)`](#set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse))
[`UMLPackage.getValueSpecification__interactionUseOfReturnValue()`](../../metadata/UMLPackage.html#getValueSpecification__interactionUseOfReturnValue())
[`InteractionUse.getReturnValue()`](../../interactions/mdfragments/InteractionUse.html#getReturnValue())
Model:
opposite="returnValue" transient="false" ordered="false"
Generated:
set_interactionUseOfReturnValue
void set_interactionUseOfReturnValue(@CheckForNull
 [InteractionUse](../../interactions/mdfragments/InteractionUse.html) value)
Sets the value of the
 '[`*interaction Use Of Return Value*`](#get_interactionUseOfReturnValue())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*interaction Use Of Return Value*' container reference.
See Also:
[`get_interactionUseOfReturnValue()`](#get_interactionUseOfReturnValue())
Generated:
get_lifelineOfSelector
@CheckForNull[Lifeline](../../interactions/mdbasicinteractions/Lifeline.html) get_lifelineOfSelector()
Returns the value of the '***lifeline Of Selector***' container reference.
 It is bidirectional and its opposite is '[`*Selector*`](../../interactions/mdbasicinteractions/Lifeline.html#getSelector())'.
 begin-user-doc 
If the meaning of the '*lifeline Of Selector*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*lifeline Of Selector*' container reference.
See Also:
[`set_lifelineOfSelector(Lifeline)`](#set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline))
[`UMLPackage.getValueSpecification__lifelineOfSelector()`](../../metadata/UMLPackage.html#getValueSpecification__lifelineOfSelector())
[`Lifeline.getSelector()`](../../interactions/mdbasicinteractions/Lifeline.html#getSelector())
Model:
opposite="selector" transient="false" ordered="false"
Generated:
set_lifelineOfSelector
void set_lifelineOfSelector(@CheckForNull
 [Lifeline](../../interactions/mdbasicinteractions/Lifeline.html) value)
Sets the value of the '[`*lifeline Of Selector*`](#get_lifelineOfSelector())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*lifeline Of Selector*' container reference.
See Also:
[`get_lifelineOfSelector()`](#get_lifelineOfSelector())
Generated:
get_interactionConstraintOfMinint
@CheckForNull[InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html) get_interactionConstraintOfMinint()
Returns the value of the '***interaction Constraint Of Minint***' container reference.
 It is bidirectional and its opposite is '[`*Minint*`](../../interactions/mdfragments/InteractionConstraint.html#getMinint())'.
 begin-user-doc 
If the meaning of the '*interaction Constraint Of Minint*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interaction Constraint Of Minint*' container reference.
See Also:
[`set_interactionConstraintOfMinint(InteractionConstraint)`](#set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint))
[`UMLPackage.getValueSpecification__interactionConstraintOfMinint()`](../../metadata/UMLPackage.html#getValueSpecification__interactionConstraintOfMinint())
[`InteractionConstraint.getMinint()`](../../interactions/mdfragments/InteractionConstraint.html#getMinint())
Model:
opposite="minint" transient="false" ordered="false"
Generated:
set_interactionConstraintOfMinint
void set_interactionConstraintOfMinint(@CheckForNull
 [InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html) value)
Sets the value of the
 '[`*interaction Constraint Of Minint*`](#get_interactionConstraintOfMinint())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*interaction Constraint Of Minint*' container reference.
See Also:
[`get_interactionConstraintOfMinint()`](#get_interactionConstraintOfMinint())
Generated:
get_interactionConstraintOfMaxint
@CheckForNull[InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html) get_interactionConstraintOfMaxint()
Returns the value of the '***interaction Constraint Of Maxint***' container reference.
 It is bidirectional and its opposite is '[`*Maxint*`](../../interactions/mdfragments/InteractionConstraint.html#getMaxint())'.
 begin-user-doc 
If the meaning of the '*interaction Constraint Of Maxint*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*interaction Constraint Of Maxint*' container reference.
See Also:
[`set_interactionConstraintOfMaxint(InteractionConstraint)`](#set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint))
[`UMLPackage.getValueSpecification__interactionConstraintOfMaxint()`](../../metadata/UMLPackage.html#getValueSpecification__interactionConstraintOfMaxint())
[`InteractionConstraint.getMaxint()`](../../interactions/mdfragments/InteractionConstraint.html#getMaxint())
Model:
opposite="maxint" transient="false" ordered="false"
Generated:
set_interactionConstraintOfMaxint
void set_interactionConstraintOfMaxint(@CheckForNull
 [InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html) value)
Sets the value of the
 '[`*interaction Constraint Of Maxint*`](#get_interactionConstraintOfMaxint())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*interaction Constraint Of Maxint*' container reference.
See Also:
[`get_interactionConstraintOfMaxint()`](#get_interactionConstraintOfMaxint())
Generated:
get_changeEventOfChangeExpression
@CheckForNull[ChangeEvent](../../commonbehaviors/mdcommunications/ChangeEvent.html) get_changeEventOfChangeExpression()
Returns the value of the '***change Event Of Change Expression***' container reference.
 It is bidirectional and its opposite is
 '[`*Change Expression*`](../../commonbehaviors/mdcommunications/ChangeEvent.html#getChangeExpression())'.
 begin-user-doc 
If the meaning of the '*change Event Of Change Expression*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*change Event Of Change Expression*' container reference.
See Also:
[`set_changeEventOfChangeExpression(ChangeEvent)`](#set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent))
[`UMLPackage.getValueSpecification__changeEventOfChangeExpression()`](../../metadata/UMLPackage.html#getValueSpecification__changeEventOfChangeExpression())
[`ChangeEvent.getChangeExpression()`](../../commonbehaviors/mdcommunications/ChangeEvent.html#getChangeExpression())
Model:
opposite="changeExpression" transient="false" ordered="false"
Generated:
set_changeEventOfChangeExpression
void set_changeEventOfChangeExpression(@CheckForNull
 [ChangeEvent](../../commonbehaviors/mdcommunications/ChangeEvent.html) value)
Sets the value of the
 '[`*change Event Of Change Expression*`](#get_changeEventOfChangeExpression())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*change Event Of Change Expression*' container reference.
See Also:
[`get_changeEventOfChangeExpression()`](#get_changeEventOfChangeExpression())
Generated:
get_objectNodeOfUpperBound
@CheckForNull[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html) get_objectNodeOfUpperBound()
Returns the value of the '***object Node Of Upper Bound***' container reference.
 It is bidirectional and its opposite is '[`*Upper Bound*`](../../activities/mdbasicactivities/ObjectNode.html#getUpperBound())'.
 begin-user-doc 
If the meaning of the '*object Node Of Upper Bound*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*object Node Of Upper Bound*' container reference.
See Also:
[`set_objectNodeOfUpperBound(ObjectNode)`](#set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode))
[`UMLPackage.getValueSpecification__objectNodeOfUpperBound()`](../../metadata/UMLPackage.html#getValueSpecification__objectNodeOfUpperBound())
[`ObjectNode.getUpperBound()`](../../activities/mdbasicactivities/ObjectNode.html#getUpperBound())
Model:
opposite="upperBound" transient="false" ordered="false"
Generated:
set_objectNodeOfUpperBound
void set_objectNodeOfUpperBound(@CheckForNull
 [ObjectNode](../../activities/mdbasicactivities/ObjectNode.html) value)
Sets the value of the '[`*object Node Of Upper Bound*`](#get_objectNodeOfUpperBound())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*object Node Of Upper Bound*' container reference.
See Also:
[`get_objectNodeOfUpperBound()`](#get_objectNodeOfUpperBound())
Generated:
get_valuePinOfValue
@CheckForNull[ValuePin](../../actions/mdbasicactions/ValuePin.html) get_valuePinOfValue()
Returns the value of the '***value Pin Of Value***' container reference.
 It is bidirectional and its opposite is '[`*Value*`](../../actions/mdbasicactions/ValuePin.html#getValue())'.
 begin-user-doc 
If the meaning of the '*value Pin Of Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*value Pin Of Value*' container reference.
See Also:
[`set_valuePinOfValue(ValuePin)`](#set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin))
[`UMLPackage.getValueSpecification__valuePinOfValue()`](../../metadata/UMLPackage.html#getValueSpecification__valuePinOfValue())
[`ValuePin.getValue()`](../../actions/mdbasicactions/ValuePin.html#getValue())
Model:
opposite="value" transient="false" ordered="false"
Generated:
set_valuePinOfValue
void set_valuePinOfValue(@CheckForNull
 [ValuePin](../../actions/mdbasicactions/ValuePin.html) value)
Sets the value of the '[`*value Pin Of Value*`](#get_valuePinOfValue())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*value Pin Of Value*' container reference.
See Also:
[`get_valuePinOfValue()`](#get_valuePinOfValue())
Generated:
getOwningParameter
@CheckForNull[Parameter](Parameter.html) getOwningParameter()
Returns the value of the '***Owning Parameter***' container reference.
 It is bidirectional and its opposite is '[`*Default Value*`](Parameter.html#getDefaultValue())'.
 begin-user-doc 
If the meaning of the '*Owning Parameter*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Parameter*' container reference.
See Also:
[`setOwningParameter(Parameter)`](#setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter))
[`UMLPackage.getValueSpecification_OwningParameter()`](../../metadata/UMLPackage.html#getValueSpecification_OwningParameter())
[`Parameter.getDefaultValue()`](Parameter.html#getDefaultValue())
Model:
opposite="defaultValue" transient="false" ordered="false"
Generated:
setOwningParameter
void setOwningParameter(@CheckForNull
 [Parameter](Parameter.html) value)
Sets the value of the '[`*Owning Parameter*`](#getOwningParameter())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Parameter*' container reference.
See Also:
[`getOwningParameter()`](#getOwningParameter())
Generated:
getOwningSlot
@CheckForNull[Slot](Slot.html) getOwningSlot()
Returns the value of the '***Owning Slot***' container reference.
 It is bidirectional and its opposite is '[`*Value*`](Slot.html#getValue())'.
 begin-user-doc 
If the meaning of the '*Owning Slot*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Slot*' container reference.
See Also:
[`setOwningSlot(Slot)`](#setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot))
[`UMLPackage.getValueSpecification_OwningSlot()`](../../metadata/UMLPackage.html#getValueSpecification_OwningSlot())
[`Slot.getValue()`](Slot.html#getValue())
Model:
opposite="value" transient="false" ordered="false"
Generated:
setOwningSlot
void setOwningSlot(@CheckForNull
 [Slot](Slot.html) value)
Sets the value of the '[`*Owning Slot*`](#getOwningSlot())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Slot*' container reference.
See Also:
[`getOwningSlot()`](#getOwningSlot())
Generated:
getOwningInstanceSpec
@CheckForNull[InstanceSpecification](InstanceSpecification.html) getOwningInstanceSpec()
Returns the value of the '***Owning Instance Spec***' container reference.
 It is bidirectional and its opposite is '[`*Specification*`](InstanceSpecification.html#getSpecification())'.
 begin-user-doc 
If the meaning of the '*Owning Instance Spec*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Instance Spec*' container reference.
See Also:
[`setOwningInstanceSpec(InstanceSpecification)`](#setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification))
[`UMLPackage.getValueSpecification_OwningInstanceSpec()`](../../metadata/UMLPackage.html#getValueSpecification_OwningInstanceSpec())
[`InstanceSpecification.getSpecification()`](InstanceSpecification.html#getSpecification())
Model:
opposite="specification" transient="false" ordered="false"
Generated:
setOwningInstanceSpec
void setOwningInstanceSpec(@CheckForNull
 [InstanceSpecification](InstanceSpecification.html) value)
Sets the value of the '[`*Owning Instance Spec*`](#getOwningInstanceSpec())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Instance Spec*' container reference.
See Also:
[`getOwningInstanceSpec()`](#getOwningInstanceSpec())
Generated:
getOwningProperty
@CheckForNull[Property](Property.html) getOwningProperty()
Returns the value of the '***Owning Property***' container reference.
 It is bidirectional and its opposite is '[`*Default Value*`](Property.html#getDefaultValue())'.
 begin-user-doc 
If the meaning of the '*Owning Property*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Owning Property*' container reference.
See Also:
[`setOwningProperty(Property)`](#setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))
[`UMLPackage.getValueSpecification_OwningProperty()`](../../metadata/UMLPackage.html#getValueSpecification_OwningProperty())
[`Property.getDefaultValue()`](Property.html#getDefaultValue())
Model:
opposite="defaultValue" transient="false" ordered="false"
Generated:
setOwningProperty
void setOwningProperty(@CheckForNull
 [Property](Property.html) value)
Sets the value of the '[`*Owning Property*`](#getOwningProperty())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Property*' container reference.
See Also:
[`getOwningProperty()`](#getOwningProperty())
Generated:
getExpression
@CheckForNull[Expression](Expression.html) getExpression()
Returns the value of the '***Expression***' container reference.
 It is bidirectional and its opposite is '[`*Operand*`](Expression.html#getOperand())'.
 begin-user-doc 
If the meaning of the '*Expression*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Expression*' container reference.
See Also:
[`setExpression(Expression)`](#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression))
[`UMLPackage.getValueSpecification_Expression()`](../../metadata/UMLPackage.html#getValueSpecification_Expression())
[`Expression.getOperand()`](Expression.html#getOperand())
Model:
opposite="operand" transient="false" ordered="false"
Generated:
setExpression
void setExpression(@CheckForNull
 [Expression](Expression.html) value)
Sets the value of the '[`*Expression*`](#getExpression())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Expression*' container reference.
See Also:
[`getExpression()`](#getExpression())
Generated:
has_intervalOfMin
boolean has_intervalOfMin()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_intervalOfMax
boolean has_intervalOfMax()
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
<h1 class="title" title="Interface ValueSpecification">Interface ValueSpecification</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></code>, <code><a href="ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></code>, <code><a href="Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></code>, <code><a href="InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code>, <code><a href="LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></code>, <code><a href="LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></code>, <code><a href="LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></code>, <code><a href="LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></code>, <code><a href="LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a></code>, <code><a href="LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></code>, <code><a href="LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></code>, <code><a href="OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ValueSpecification</span><span class="extends-implements">
extends <a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a>, <a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Value Specification</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A ValueSpecification is the specification of a (possibly empty) set of values. A ValueSpecification is a ParameterableElement that may be exposed as a formal
 TemplateParameter and provided as the actual parameter in the binding of a template.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_lifelineOfSelector()"><code><em>lifeline Of Selector</em></code></a></li>
<li><a href="#get_activityEdgeOfGuard()"><code><em>activity Edge Of Guard</em></code></a></li>
<li><a href="#getOwningConstraint()"><code><em>Owning Constraint</em></code></a></li>
<li><a href="#getOwningSlot()"><code><em>Owning Slot</em></code></a></li>
<li><a href="#getOwningProperty()"><code><em>Owning Property</em></code></a></li>
<li><a href="#get_messageOfArgument()"><code><em>message Of Argument</em></code></a></li>
<li><a href="#get_messageOfTarget()"><code><em>message Of Target</em></code></a></li>
<li><a href="#get_valueSpecificationActionOfValue()"><code><em>value Specification Action Of Value</em></code></a></li>
<li><a href="#get_interactionConstraintOfMaxint()"><code><em>interaction Constraint Of Maxint</em></code></a></li>
<li><a href="#get_interactionConstraintOfMinint()"><code><em>interaction Constraint Of Minint</em></code></a></li>
<li><a href="#get_interactionUseOfArgument()"><code><em>interaction Use Of Argument</em></code></a></li>
<li><a href="#get_interactionUseOfReturnValue()"><code><em>interaction Use Of Return Value</em></code></a></li>
<li><a href="#get_objectNodeOfUpperBound()"><code><em>object Node Of Upper Bound</em></code></a></li>
<li><a href="#get_activityEdgeOfWeight()"><code><em>activity Edge Of Weight</em></code></a></li>
<li><a href="#get_valuePinOfValue()"><code><em>value Pin Of Value</em></code></a></li>
<li><a href="#get_intervalOfMax()"><code><em>interval Of Max</em></code></a></li>
<li><a href="#get_intervalOfMin()"><code><em>interval Of Min</em></code></a></li>
<li><a href="#getOwningParameter()"><code><em>Owning Parameter</em></code></a></li>
<li><a href="#get_changeEventOfChangeExpression()"><code><em>change Event Of Change Expression</em></code></a></li>
<li><a href="#get_joinNodeOfJoinSpec()"><code><em>join Node Of Join Spec</em></code></a></li>
<li><a href="#getOwningInstanceSpec()"><code><em>Owning Instance Spec</em></code></a></li>
<li><a href="#getOwningUpper()"><code><em>Owning Upper</em></code></a></li>
<li><a href="#get_durationOfExpr()"><code><em>duration Of Expr</em></code></a></li>
<li><a href="#get_timeExpressionOfExpr()"><code><em>time Expression Of Expr</em></code></a></li>
<li><a href="#getExpression()"><code><em>Expression</em></code></a></li>
<li><a href="#getOwningLower()"><code><em>Owning Lower</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getValueSpecification()"><code>UMLPackage.getValueSpecification()</code></a></li>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_activityEdgeOfGuard()">get_activityEdgeOfGuard</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>activity Edge Of Guard</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_activityEdgeOfWeight()">get_activityEdgeOfWeight</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>activity Edge Of Weight</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_changeEventOfChangeExpression()">get_changeEventOfChangeExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>change Event Of Change Expression</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_durationOfExpr()">get_durationOfExpr</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>duration Of Expr</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interactionConstraintOfMaxint()">get_interactionConstraintOfMaxint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interaction Constraint Of Maxint</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interactionConstraintOfMinint()">get_interactionConstraintOfMinint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interaction Constraint Of Minint</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interactionUseOfArgument()">get_interactionUseOfArgument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interaction Use Of Argument</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_interactionUseOfReturnValue()">get_interactionUseOfReturnValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interaction Use Of Return Value</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_intervalOfMax()">get_intervalOfMax</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interval Of Max</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_intervalOfMin()">get_intervalOfMin</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>interval Of Min</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_joinNodeOfJoinSpec()">get_joinNodeOfJoinSpec</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>join Node Of Join Spec</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_lifelineOfSelector()">get_lifelineOfSelector</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>lifeline Of Selector</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_messageOfArgument()">get_messageOfArgument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>message Of Argument</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_messageOfTarget()">get_messageOfTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>message Of Target</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_objectNodeOfUpperBound()">get_objectNodeOfUpperBound</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>object Node Of Upper Bound</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_timeExpressionOfExpr()">get_timeExpressionOfExpr</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>time Expression Of Expr</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_valuePinOfValue()">get_valuePinOfValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>value Pin Of Value</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_valueSpecificationActionOfValue()">get_valueSpecificationActionOfValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>value Specification Action Of Value</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExpression()">getExpression</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Expression</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningConstraint()">getOwningConstraint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Constraint</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningInstanceSpec()">getOwningInstanceSpec</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Instance Spec</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningLower()">getOwningLower</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Lower</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningParameter()">getOwningParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Parameter</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningProperty()">getOwningProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Property</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningSlot()">getOwningSlot</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Slot</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningUpper()">getOwningUpper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Upper</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_intervalOfMax()">has_intervalOfMax</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_intervalOfMin()">has_intervalOfMin</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">set_activityEdgeOfGuard</a><wbr/>(<a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_activityEdgeOfGuard()"><code><em>activity Edge Of Guard</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">set_activityEdgeOfWeight</a><wbr/>(<a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_activityEdgeOfWeight()"><code><em>activity Edge Of Weight</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)">set_changeEventOfChangeExpression</a><wbr/>(<a href="../../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_changeEventOfChangeExpression()"><code><em>change Event Of Change Expression</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)">set_durationOfExpr</a><wbr/>(<a href="../../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_durationOfExpr()"><code><em>duration Of Expr</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">set_interactionConstraintOfMaxint</a><wbr/>(<a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_interactionConstraintOfMaxint()"><code><em>interaction Constraint Of Maxint</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">set_interactionConstraintOfMinint</a><wbr/>(<a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_interactionConstraintOfMinint()"><code><em>interaction Constraint Of Minint</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">set_interactionUseOfArgument</a><wbr/>(<a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_interactionUseOfArgument()"><code><em>interaction Use Of Argument</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">set_interactionUseOfReturnValue</a><wbr/>(<a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_interactionUseOfReturnValue()"><code><em>interaction Use Of Return Value</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)">set_joinNodeOfJoinSpec</a><wbr/>(<a href="../../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_joinNodeOfJoinSpec()"><code><em>join Node Of Join Spec</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">set_lifelineOfSelector</a><wbr/>(<a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_lifelineOfSelector()"><code><em>lifeline Of Selector</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfArgument</a><wbr/>(<a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_messageOfArgument()"><code><em>message Of Argument</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfTarget</a><wbr/>(<a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_messageOfTarget()"><code><em>message Of Target</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)">set_objectNodeOfUpperBound</a><wbr/>(<a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_objectNodeOfUpperBound()"><code><em>object Node Of Upper Bound</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">set_timeExpressionOfExpr</a><wbr/>(<a href="../../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_timeExpressionOfExpr()"><code><em>time Expression Of Expr</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)">set_valuePinOfValue</a><wbr/>(<a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_valuePinOfValue()"><code><em>value Pin Of Value</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)">set_valueSpecificationActionOfValue</a><wbr/>(<a href="../../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_valueSpecificationActionOfValue()"><code><em>value Specification
 Action Of Value</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)">setExpression</a><wbr/>(<a href="Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getExpression()"><code><em>Expression</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setOwningConstraint</a><wbr/>(<a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningConstraint()"><code><em>Owning Constraint</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">setOwningInstanceSpec</a><wbr/>(<a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningInstanceSpec()"><code><em>Owning Instance Spec</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setOwningLower</a><wbr/>(<a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningLower()"><code><em>Owning Lower</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">setOwningParameter</a><wbr/>(<a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningParameter()"><code><em>Owning Parameter</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setOwningProperty</a><wbr/>(<a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningProperty()"><code><em>Owning Property</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">setOwningSlot</a><wbr/>(<a href="Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningSlot()"><code><em>Owning Slot</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setOwningUpper</a><wbr/>(<a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningUpper()"><code><em>Owning Upper</em></code></a>' container reference.</div>
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
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID</code></div>
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
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></h3>
<code><a href="TypedElement.html#getType()">getType</a>, <a href="TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">setType</a></code></div>
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
<section class="detail" id="getOwningConstraint()">
<h3>getOwningConstraint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></span> <span class="element-name">getOwningConstraint</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Constraint</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Constraint.html#getSpecification()"><code><em>Specification</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Constraint</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Constraint</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)"><code>setOwningConstraint(Constraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification_OwningConstraint()"><code>UMLPackage.getValueSpecification_OwningConstraint()</code></a></li>
<li><a href="Constraint.html#getSpecification()"><code>Constraint.getSpecification()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="specification" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>setOwningConstraint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningConstraint</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningConstraint()"><code><em>Owning Constraint</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Constraint</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningConstraint()"><code>getOwningConstraint()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningUpper()">
<h3>getOwningUpper</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></span> <span class="element-name">getOwningUpper</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Upper</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="MultiplicityElement.html#getUpperValue()"><code><em>Upper Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Upper</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Upper</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)"><code>setOwningUpper(MultiplicityElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification_OwningUpper()"><code>UMLPackage.getValueSpecification_OwningUpper()</code></a></li>
<li><a href="MultiplicityElement.html#getUpperValue()"><code>MultiplicityElement.getUpperValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="upperValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">
<h3>setOwningUpper</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningUpper</span><wbr/><span class="parameters">(@CheckForNull
 <a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningUpper()"><code><em>Owning Upper</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Upper</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningUpper()"><code>getOwningUpper()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningLower()">
<h3>getOwningLower</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></span> <span class="element-name">getOwningLower</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Lower</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="MultiplicityElement.html#getLowerValue()"><code><em>Lower Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Lower</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Lower</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)"><code>setOwningLower(MultiplicityElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification_OwningLower()"><code>UMLPackage.getValueSpecification_OwningLower()</code></a></li>
<li><a href="MultiplicityElement.html#getLowerValue()"><code>MultiplicityElement.getLowerValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="lowerValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">
<h3>setOwningLower</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningLower</span><wbr/><span class="parameters">(@CheckForNull
 <a href="MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningLower()"><code><em>Owning Lower</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Lower</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningLower()"><code>getOwningLower()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_intervalOfMin()">
<h3>get_intervalOfMin</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a>&gt;</span> <span class="element-name">get_intervalOfMin</span>()</div>
<div class="block">Returns the value of the '<em><b>interval Of Min</b></em>' reference list.
 The list contents are of type <a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Interval</code></a>.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdsimpletime/Interval.html#getMin()"><code><em>Min</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interval Of Min</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interval Of Min</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__intervalOfMin()"><code>UMLPackage.getValueSpecification__intervalOfMin()</code></a></li>
<li><a href="../../commonbehaviors/mdsimpletime/Interval.html#getMin()"><code>Interval.getMin()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="min" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_intervalOfMax()">
<h3>get_intervalOfMax</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a>&gt;</span> <span class="element-name">get_intervalOfMax</span>()</div>
<div class="block">Returns the value of the '<em><b>interval Of Max</b></em>' reference list.
 The list contents are of type <a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime"><code>Interval</code></a>.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdsimpletime/Interval.html#getMax()"><code><em>Max</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interval Of Max</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interval Of Max</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__intervalOfMax()"><code>UMLPackage.getValueSpecification__intervalOfMax()</code></a></li>
<li><a href="../../commonbehaviors/mdsimpletime/Interval.html#getMax()"><code>Interval.getMax()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="max" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_durationOfExpr()">
<h3>get_durationOfExpr</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></span> <span class="element-name">get_durationOfExpr</span>()</div>
<div class="block">Returns the value of the '<em><b>duration Of Expr</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdsimpletime/Duration.html#getExpr()"><code><em>Expr</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>duration Of Expr</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>duration Of Expr</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)"><code>set_durationOfExpr(Duration)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__durationOfExpr()"><code>UMLPackage.getValueSpecification__durationOfExpr()</code></a></li>
<li><a href="../../commonbehaviors/mdsimpletime/Duration.html#getExpr()"><code>Duration.getExpr()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="expr" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)">
<h3>set_durationOfExpr</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_durationOfExpr</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_durationOfExpr()"><code><em>duration Of Expr</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>duration Of Expr</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_durationOfExpr()"><code>get_durationOfExpr()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_timeExpressionOfExpr()">
<h3>get_timeExpressionOfExpr</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></span> <span class="element-name">get_timeExpressionOfExpr</span>()</div>
<div class="block">Returns the value of the '<em><b>time Expression Of Expr</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../commonbehaviors/mdsimpletime/TimeExpression.html#getExpr()"><code><em>Expr</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>time Expression Of Expr</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>time Expression Of Expr</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)"><code>set_timeExpressionOfExpr(TimeExpression)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__timeExpressionOfExpr()"><code>UMLPackage.getValueSpecification__timeExpressionOfExpr()</code></a></li>
<li><a href="../../commonbehaviors/mdsimpletime/TimeExpression.html#getExpr()"><code>TimeExpression.getExpr()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="expr" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">
<h3>set_timeExpressionOfExpr</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_timeExpressionOfExpr</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_timeExpressionOfExpr()"><code><em>time Expression Of Expr</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>time Expression Of Expr</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_timeExpressionOfExpr()"><code>get_timeExpressionOfExpr()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_messageOfArgument()">
<h3>get_messageOfArgument</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">get_messageOfArgument</span>()</div>
<div class="block">Returns the value of the '<em><b>message Of Argument</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/Message.html#getArgument()"><code><em>Argument</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>message Of Argument</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>message Of Argument</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)"><code>set_messageOfArgument(Message)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__messageOfArgument()"><code>UMLPackage.getValueSpecification__messageOfArgument()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/Message.html#getArgument()"><code>Message.getArgument()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="argument" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>set_messageOfArgument</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_messageOfArgument</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_messageOfArgument()"><code><em>message Of Argument</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>message Of Argument</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_messageOfArgument()"><code>get_messageOfArgument()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_joinNodeOfJoinSpec()">
<h3>get_joinNodeOfJoinSpec</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a></span> <span class="element-name">get_joinNodeOfJoinSpec</span>()</div>
<div class="block">Returns the value of the '<em><b>join Node Of Join Spec</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdintermediateactivities/JoinNode.html#getJoinSpec()"><code><em>Join Spec</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>join Node Of Join Spec</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>join Node Of Join Spec</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)"><code>set_joinNodeOfJoinSpec(JoinNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__joinNodeOfJoinSpec()"><code>UMLPackage.getValueSpecification__joinNodeOfJoinSpec()</code></a></li>
<li><a href="../../activities/mdintermediateactivities/JoinNode.html#getJoinSpec()"><code>JoinNode.getJoinSpec()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="joinSpec" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)">
<h3>set_joinNodeOfJoinSpec</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_joinNodeOfJoinSpec</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdintermediateactivities/JoinNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">JoinNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_joinNodeOfJoinSpec()"><code><em>join Node Of Join Spec</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>join Node Of Join Spec</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_joinNodeOfJoinSpec()"><code>get_joinNodeOfJoinSpec()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_activityEdgeOfGuard()">
<h3>get_activityEdgeOfGuard</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a></span> <span class="element-name">get_activityEdgeOfGuard</span>()</div>
<div class="block">Returns the value of the '<em><b>activity Edge Of Guard</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdbasicactivities/ActivityEdge.html#getGuard()"><code><em>Guard</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>activity Edge Of Guard</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>activity Edge Of Guard</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)"><code>set_activityEdgeOfGuard(ActivityEdge)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__activityEdgeOfGuard()"><code>UMLPackage.getValueSpecification__activityEdgeOfGuard()</code></a></li>
<li><a href="../../activities/mdbasicactivities/ActivityEdge.html#getGuard()"><code>ActivityEdge.getGuard()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="guard" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">
<h3>set_activityEdgeOfGuard</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_activityEdgeOfGuard</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_activityEdgeOfGuard()"><code><em>activity Edge Of Guard</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>activity Edge Of Guard</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_activityEdgeOfGuard()"><code>get_activityEdgeOfGuard()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_activityEdgeOfWeight()">
<h3>get_activityEdgeOfWeight</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a></span> <span class="element-name">get_activityEdgeOfWeight</span>()</div>
<div class="block">Returns the value of the '<em><b>activity Edge Of Weight</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdbasicactivities/ActivityEdge.html#getWeight()"><code><em>Weight</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>activity Edge Of Weight</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>activity Edge Of Weight</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)"><code>set_activityEdgeOfWeight(ActivityEdge)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__activityEdgeOfWeight()"><code>UMLPackage.getValueSpecification__activityEdgeOfWeight()</code></a></li>
<li><a href="../../activities/mdbasicactivities/ActivityEdge.html#getWeight()"><code>ActivityEdge.getWeight()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="weight" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">
<h3>set_activityEdgeOfWeight</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_activityEdgeOfWeight</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdbasicactivities/ActivityEdge.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ActivityEdge</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_activityEdgeOfWeight()"><code><em>activity Edge Of Weight</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>activity Edge Of Weight</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_activityEdgeOfWeight()"><code>get_activityEdgeOfWeight()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_valueSpecificationActionOfValue()">
<h3>get_valueSpecificationActionOfValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></span> <span class="element-name">get_valueSpecificationActionOfValue</span>()</div>
<div class="block">Returns the value of the '<em><b>value Specification Action Of Value</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../actions/mdintermediateactions/ValueSpecificationAction.html#getValue()"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>value Specification Action Of Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>value Specification Action Of Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)"><code>set_valueSpecificationActionOfValue(ValueSpecificationAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__valueSpecificationActionOfValue()"><code>UMLPackage.getValueSpecification__valueSpecificationActionOfValue()</code></a></li>
<li><a href="../../actions/mdintermediateactions/ValueSpecificationAction.html#getValue()"><code>ValueSpecificationAction.getValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="value" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)">
<h3>set_valueSpecificationActionOfValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_valueSpecificationActionOfValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../actions/mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_valueSpecificationActionOfValue()"><code><em>value Specification
 Action Of Value</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>value Specification Action Of Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_valueSpecificationActionOfValue()"><code>get_valueSpecificationActionOfValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_messageOfTarget()">
<h3>get_messageOfTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a></span> <span class="element-name">get_messageOfTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>message Of Target</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/Message.html#getTarget()"><code><em>Target</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>message Of Target</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>message Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)"><code>set_messageOfTarget(Message)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__messageOfTarget()"><code>UMLPackage.getValueSpecification__messageOfTarget()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/Message.html#getTarget()"><code>Message.getTarget()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="target" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">
<h3>set_messageOfTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_messageOfTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdbasicinteractions/Message.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Message</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_messageOfTarget()"><code><em>message Of Target</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>message Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_messageOfTarget()"><code>get_messageOfTarget()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interactionUseOfArgument()">
<h3>get_interactionUseOfArgument</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></span> <span class="element-name">get_interactionUseOfArgument</span>()</div>
<div class="block">Returns the value of the '<em><b>interaction Use Of Argument</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdfragments/InteractionUse.html#getArgument()"><code><em>Argument</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interaction Use Of Argument</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interaction Use Of Argument</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)"><code>set_interactionUseOfArgument(InteractionUse)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__interactionUseOfArgument()"><code>UMLPackage.getValueSpecification__interactionUseOfArgument()</code></a></li>
<li><a href="../../interactions/mdfragments/InteractionUse.html#getArgument()"><code>InteractionUse.getArgument()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="argument" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">
<h3>set_interactionUseOfArgument</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_interactionUseOfArgument</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_interactionUseOfArgument()"><code><em>interaction Use Of Argument</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>interaction Use Of Argument</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_interactionUseOfArgument()"><code>get_interactionUseOfArgument()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interactionUseOfReturnValue()">
<h3>get_interactionUseOfReturnValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a></span> <span class="element-name">get_interactionUseOfReturnValue</span>()</div>
<div class="block">Returns the value of the '<em><b>interaction Use Of Return Value</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdfragments/InteractionUse.html#getReturnValue()"><code><em>Return Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interaction Use Of Return Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interaction Use Of Return Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)"><code>set_interactionUseOfReturnValue(InteractionUse)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__interactionUseOfReturnValue()"><code>UMLPackage.getValueSpecification__interactionUseOfReturnValue()</code></a></li>
<li><a href="../../interactions/mdfragments/InteractionUse.html#getReturnValue()"><code>InteractionUse.getReturnValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="returnValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">
<h3>set_interactionUseOfReturnValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_interactionUseOfReturnValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdfragments/InteractionUse.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionUse</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_interactionUseOfReturnValue()"><code><em>interaction Use Of Return Value</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>interaction Use Of Return Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_interactionUseOfReturnValue()"><code>get_interactionUseOfReturnValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_lifelineOfSelector()">
<h3>get_lifelineOfSelector</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a></span> <span class="element-name">get_lifelineOfSelector</span>()</div>
<div class="block">Returns the value of the '<em><b>lifeline Of Selector</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdbasicinteractions/Lifeline.html#getSelector()"><code><em>Selector</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>lifeline Of Selector</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>lifeline Of Selector</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)"><code>set_lifelineOfSelector(Lifeline)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__lifelineOfSelector()"><code>UMLPackage.getValueSpecification__lifelineOfSelector()</code></a></li>
<li><a href="../../interactions/mdbasicinteractions/Lifeline.html#getSelector()"><code>Lifeline.getSelector()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="selector" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">
<h3>set_lifelineOfSelector</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_lifelineOfSelector</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdbasicinteractions/Lifeline.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Lifeline</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_lifelineOfSelector()"><code><em>lifeline Of Selector</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>lifeline Of Selector</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_lifelineOfSelector()"><code>get_lifelineOfSelector()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interactionConstraintOfMinint()">
<h3>get_interactionConstraintOfMinint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></span> <span class="element-name">get_interactionConstraintOfMinint</span>()</div>
<div class="block">Returns the value of the '<em><b>interaction Constraint Of Minint</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdfragments/InteractionConstraint.html#getMinint()"><code><em>Minint</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interaction Constraint Of Minint</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interaction Constraint Of Minint</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)"><code>set_interactionConstraintOfMinint(InteractionConstraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__interactionConstraintOfMinint()"><code>UMLPackage.getValueSpecification__interactionConstraintOfMinint()</code></a></li>
<li><a href="../../interactions/mdfragments/InteractionConstraint.html#getMinint()"><code>InteractionConstraint.getMinint()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="minint" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">
<h3>set_interactionConstraintOfMinint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_interactionConstraintOfMinint</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_interactionConstraintOfMinint()"><code><em>interaction Constraint Of Minint</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>interaction Constraint Of Minint</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_interactionConstraintOfMinint()"><code>get_interactionConstraintOfMinint()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_interactionConstraintOfMaxint()">
<h3>get_interactionConstraintOfMaxint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></span> <span class="element-name">get_interactionConstraintOfMaxint</span>()</div>
<div class="block">Returns the value of the '<em><b>interaction Constraint Of Maxint</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../interactions/mdfragments/InteractionConstraint.html#getMaxint()"><code><em>Maxint</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>interaction Constraint Of Maxint</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>interaction Constraint Of Maxint</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)"><code>set_interactionConstraintOfMaxint(InteractionConstraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__interactionConstraintOfMaxint()"><code>UMLPackage.getValueSpecification__interactionConstraintOfMaxint()</code></a></li>
<li><a href="../../interactions/mdfragments/InteractionConstraint.html#getMaxint()"><code>InteractionConstraint.getMaxint()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="maxint" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">
<h3>set_interactionConstraintOfMaxint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_interactionConstraintOfMaxint</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_interactionConstraintOfMaxint()"><code><em>interaction Constraint Of Maxint</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>interaction Constraint Of Maxint</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_interactionConstraintOfMaxint()"><code>get_interactionConstraintOfMaxint()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_changeEventOfChangeExpression()">
<h3>get_changeEventOfChangeExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></span> <span class="element-name">get_changeEventOfChangeExpression</span>()</div>
<div class="block">Returns the value of the '<em><b>change Event Of Change Expression</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../commonbehaviors/mdcommunications/ChangeEvent.html#getChangeExpression()"><code><em>Change Expression</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>change Event Of Change Expression</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>change Event Of Change Expression</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)"><code>set_changeEventOfChangeExpression(ChangeEvent)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__changeEventOfChangeExpression()"><code>UMLPackage.getValueSpecification__changeEventOfChangeExpression()</code></a></li>
<li><a href="../../commonbehaviors/mdcommunications/ChangeEvent.html#getChangeExpression()"><code>ChangeEvent.getChangeExpression()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="changeExpression" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)">
<h3>set_changeEventOfChangeExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_changeEventOfChangeExpression</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_changeEventOfChangeExpression()"><code><em>change Event Of Change Expression</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>change Event Of Change Expression</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_changeEventOfChangeExpression()"><code>get_changeEventOfChangeExpression()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_objectNodeOfUpperBound()">
<h3>get_objectNodeOfUpperBound</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></span> <span class="element-name">get_objectNodeOfUpperBound</span>()</div>
<div class="block">Returns the value of the '<em><b>object Node Of Upper Bound</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdbasicactivities/ObjectNode.html#getUpperBound()"><code><em>Upper Bound</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>object Node Of Upper Bound</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>object Node Of Upper Bound</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)"><code>set_objectNodeOfUpperBound(ObjectNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__objectNodeOfUpperBound()"><code>UMLPackage.getValueSpecification__objectNodeOfUpperBound()</code></a></li>
<li><a href="../../activities/mdbasicactivities/ObjectNode.html#getUpperBound()"><code>ObjectNode.getUpperBound()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="upperBound" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)">
<h3>set_objectNodeOfUpperBound</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_objectNodeOfUpperBound</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_objectNodeOfUpperBound()"><code><em>object Node Of Upper Bound</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>object Node Of Upper Bound</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_objectNodeOfUpperBound()"><code>get_objectNodeOfUpperBound()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_valuePinOfValue()">
<h3>get_valuePinOfValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></span> <span class="element-name">get_valuePinOfValue</span>()</div>
<div class="block">Returns the value of the '<em><b>value Pin Of Value</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../actions/mdbasicactions/ValuePin.html#getValue()"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>value Pin Of Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>value Pin Of Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)"><code>set_valuePinOfValue(ValuePin)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification__valuePinOfValue()"><code>UMLPackage.getValueSpecification__valuePinOfValue()</code></a></li>
<li><a href="../../actions/mdbasicactions/ValuePin.html#getValue()"><code>ValuePin.getValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="value" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)">
<h3>set_valuePinOfValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_valuePinOfValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../actions/mdbasicactions/ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_valuePinOfValue()"><code><em>value Pin Of Value</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>value Pin Of Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_valuePinOfValue()"><code>get_valuePinOfValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningParameter()">
<h3>getOwningParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></span> <span class="element-name">getOwningParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Parameter</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Parameter.html#getDefaultValue()"><code><em>Default Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Parameter</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Parameter</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)"><code>setOwningParameter(Parameter)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification_OwningParameter()"><code>UMLPackage.getValueSpecification_OwningParameter()</code></a></li>
<li><a href="Parameter.html#getDefaultValue()"><code>Parameter.getDefaultValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="defaultValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">
<h3>setOwningParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningParameter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningParameter()"><code><em>Owning Parameter</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Parameter</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningParameter()"><code>getOwningParameter()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningSlot()">
<h3>getOwningSlot</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a></span> <span class="element-name">getOwningSlot</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Slot</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Slot.html#getValue()"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Slot</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Slot</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)"><code>setOwningSlot(Slot)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification_OwningSlot()"><code>UMLPackage.getValueSpecification_OwningSlot()</code></a></li>
<li><a href="Slot.html#getValue()"><code>Slot.getValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="value" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">
<h3>setOwningSlot</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningSlot</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Slot.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Slot</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningSlot()"><code><em>Owning Slot</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Slot</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningSlot()"><code>getOwningSlot()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningInstanceSpec()">
<h3>getOwningInstanceSpec</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></span> <span class="element-name">getOwningInstanceSpec</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Instance Spec</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="InstanceSpecification.html#getSpecification()"><code><em>Specification</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Instance Spec</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Instance Spec</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)"><code>setOwningInstanceSpec(InstanceSpecification)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification_OwningInstanceSpec()"><code>UMLPackage.getValueSpecification_OwningInstanceSpec()</code></a></li>
<li><a href="InstanceSpecification.html#getSpecification()"><code>InstanceSpecification.getSpecification()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="specification" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">
<h3>setOwningInstanceSpec</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningInstanceSpec</span><wbr/><span class="parameters">(@CheckForNull
 <a href="InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningInstanceSpec()"><code><em>Owning Instance Spec</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Instance Spec</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningInstanceSpec()"><code>getOwningInstanceSpec()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningProperty()">
<h3>getOwningProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getOwningProperty</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Property</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Property.html#getDefaultValue()"><code><em>Default Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Owning Property</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Property</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)"><code>setOwningProperty(Property)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification_OwningProperty()"><code>UMLPackage.getValueSpecification_OwningProperty()</code></a></li>
<li><a href="Property.html#getDefaultValue()"><code>Property.getDefaultValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="defaultValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>setOwningProperty</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningProperty</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningProperty()"><code><em>Owning Property</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Property</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningProperty()"><code>getOwningProperty()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExpression()">
<h3>getExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></span> <span class="element-name">getExpression</span>()</div>
<div class="block">Returns the value of the '<em><b>Expression</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Expression.html#getOperand()"><code><em>Operand</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Expression</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Expression</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)"><code>setExpression(Expression)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getValueSpecification_Expression()"><code>UMLPackage.getValueSpecification_Expression()</code></a></li>
<li><a href="Expression.html#getOperand()"><code>Expression.getOperand()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="operand" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)">
<h3>setExpression</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setExpression</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getExpression()"><code><em>Expression</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Expression</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getExpression()"><code>getExpression()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_intervalOfMin()">
<h3>has_intervalOfMin</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_intervalOfMin</span>()
                   throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_intervalOfMax()">
<h3>has_intervalOfMax</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_intervalOfMax</span>()
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
