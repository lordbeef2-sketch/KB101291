# JAVA OPENAPI: OutputPin (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/actions/mdbasicactions/OutputPin.html
- source_path: `com/nomagic/uml2/ext/magicdraw/actions/mdbasicactions/OutputPin.html`
- source_sha256: `756e5713c5a6c7b270fa5a31512e01186861ebb2802b5530ea4b95b4824d52fd`
- captured_utc: `2026-07-14T16:52:49.303373+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions](package-summary.html)

## Interface OutputPin

All Superinterfaces:
`[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[MultiplicityElement](../../classes/mdkernel/MultiplicityElement.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)`, `[Pin](Pin.html)`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TypedElement](../../classes/mdkernel/TypedElement.html)`

public interfaceOutputPinextends [Pin](Pin.html)

begin-user-doc 
 A representation of the model object '***Output Pin***'.
 end-user-doc 
begin-model-doc 
 An OutputPin is a Pin that holds output values produced by an Action.
 end-model-doc 
The following features are supported:
 [`*structured Activity Node Of Structured Node Output*`](#get_structuredActivityNodeOfStructuredNodeOutput())
[`*read Extent Action Of Result*`](#get_readExtentActionOfResult())
[`*conditional Node Of Result*`](#get_conditionalNodeOfResult())
[`*clause Of Body Output*`](#get_clauseOfBodyOutput())
[`*clause Of Decider*`](#get_clauseOfDecider())
[`*loop Node Of Loop Variable*`](#get_loopNodeOfLoopVariable())
[`*loop Node Of Body Output*`](#get_loopNodeOfBodyOutput())
[`*loop Node Of Decider*`](#get_loopNodeOfDecider())
[`*loop Node Of Result*`](#get_loopNodeOfResult())
[`*reduce Action Of Result*`](#get_reduceActionOfResult())
[`*action Of Output*`](#get_actionOfOutput())
[`*create Object Action Of Result*`](#get_createObjectActionOfResult())
[`*unmarshall Action Of Result*`](#get_unmarshallActionOfResult())
[`*opaque Action Of Output Value*`](#get_opaqueActionOfOutputValue())
[`*read Link Action Of Result*`](#get_readLinkActionOfResult())
[`*read Link Object End Action Of Result*`](#get_readLinkObjectEndActionOfResult())
[`*accept Call Action Of Return Information*`](#get_acceptCallActionOfReturnInformation())
[`*write Structural Feature Action Of Result*`](#get_writeStructuralFeatureActionOfResult())
[`*create Link Object Action Of Result*`](#get_createLinkObjectActionOfResult())
[`*read Structural Feature Action Of Result*`](#get_readStructuralFeatureActionOfResult())
[`*clear Structural Feature Action Of Result*`](#get_clearStructuralFeatureActionOfResult())
[`*value Specification Action Of Result*`](#get_valueSpecificationActionOfResult())
[`*test Identity Action Of Result*`](#get_testIdentityActionOfResult())
[`*read Is Classified Object Action Of Result*`](#get_readIsClassifiedObjectActionOfResult())
[`*call Action Of Result*`](#get_callActionOfResult())
[`*read Self Action Of Result*`](#get_readSelfActionOfResult())
[`*read Variable Action Of Result*`](#get_readVariableActionOfResult())
[`*read Link Object End Qualifier Action Of Result*`](#get_readLinkObjectEndQualifierActionOfResult())
[`*accept Event Action Of Result*`](#get_acceptEventActionOfResult())

See Also:
[`UMLPackage.getOutputPin()`](../../metadata/UMLPackage.html#getOutputPin())
Model:
annotation="MOF package='actions.mdbasicactions'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[AcceptCallAction](../mdcompleteactions/AcceptCallAction.html)`
`[get_acceptCallActionOfReturnInformation](#get_acceptCallActionOfReturnInformation())()`
Returns the value of the '***accept Call Action Of Return Information***' container reference.
`[AcceptEventAction](../mdcompleteactions/AcceptEventAction.html)`
`[get_acceptEventActionOfResult](#get_acceptEventActionOfResult())()`
Returns the value of the '***accept Event Action Of Result***' container reference.
`[Action](Action.html)`
`[get_actionOfOutput](#get_actionOfOutput())()`
Returns the value of the '***action Of Output***' reference.
`[CallAction](CallAction.html)`
`[get_callActionOfResult](#get_callActionOfResult())()`
Returns the value of the '***call Action Of Result***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Clause](../../activities/mdstructuredactivities/Clause.html)>`
`[get_clauseOfBodyOutput](#get_clauseOfBodyOutput())()`
Returns the value of the '***clause Of Body Output***' reference list.
`[Clause](../../activities/mdstructuredactivities/Clause.html)`
`[get_clauseOfDecider](#get_clauseOfDecider())()`
Returns the value of the '***clause Of Decider***' reference.
`[ClearStructuralFeatureAction](../mdintermediateactions/ClearStructuralFeatureAction.html)`
`[get_clearStructuralFeatureActionOfResult](#get_clearStructuralFeatureActionOfResult())()`
Returns the value of the '***clear Structural Feature Action Of Result***' container reference.
`[ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html)`
`[get_conditionalNodeOfResult](#get_conditionalNodeOfResult())()`
Returns the value of the '***conditional Node Of Result***' container reference.
`[CreateLinkObjectAction](../mdcompleteactions/CreateLinkObjectAction.html)`
`[get_createLinkObjectActionOfResult](#get_createLinkObjectActionOfResult())()`
Returns the value of the '***create Link Object Action Of Result***' container reference.
`[CreateObjectAction](../mdintermediateactions/CreateObjectAction.html)`
`[get_createObjectActionOfResult](#get_createObjectActionOfResult())()`
Returns the value of the '***create Object Action Of Result***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)>`
`[get_loopNodeOfBodyOutput](#get_loopNodeOfBodyOutput())()`
Returns the value of the '***loop Node Of Body Output***' reference list.
`[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`
`[get_loopNodeOfDecider](#get_loopNodeOfDecider())()`
Returns the value of the '***loop Node Of Decider***' reference.
`[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`
`[get_loopNodeOfLoopVariable](#get_loopNodeOfLoopVariable())()`
Returns the value of the '***loop Node Of Loop Variable***' container reference.
`[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`
`[get_loopNodeOfResult](#get_loopNodeOfResult())()`
Returns the value of the '***loop Node Of Result***' container reference.
`[OpaqueAction](OpaqueAction.html)`
`[get_opaqueActionOfOutputValue](#get_opaqueActionOfOutputValue())()`
Returns the value of the '***opaque Action Of Output Value***' container reference.
`[ReadExtentAction](../mdcompleteactions/ReadExtentAction.html)`
`[get_readExtentActionOfResult](#get_readExtentActionOfResult())()`
Returns the value of the '***read Extent Action Of Result***' container reference.
`[ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html)`
`[get_readIsClassifiedObjectActionOfResult](#get_readIsClassifiedObjectActionOfResult())()`
Returns the value of the '***read Is Classified Object Action Of Result***' container reference.
`[ReadLinkAction](../mdintermediateactions/ReadLinkAction.html)`
`[get_readLinkActionOfResult](#get_readLinkActionOfResult())()`
Returns the value of the '***read Link Action Of Result***' container reference.
`[ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html)`
`[get_readLinkObjectEndActionOfResult](#get_readLinkObjectEndActionOfResult())()`
Returns the value of the '***read Link Object End Action Of Result***' container reference.
`[ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`
`[get_readLinkObjectEndQualifierActionOfResult](#get_readLinkObjectEndQualifierActionOfResult())()`
Returns the value of the '***read Link Object End Qualifier Action Of Result***' container reference.
`[ReadSelfAction](../mdintermediateactions/ReadSelfAction.html)`
`[get_readSelfActionOfResult](#get_readSelfActionOfResult())()`
Returns the value of the '***read Self Action Of Result***' container reference.
`[ReadStructuralFeatureAction](../mdintermediateactions/ReadStructuralFeatureAction.html)`
`[get_readStructuralFeatureActionOfResult](#get_readStructuralFeatureActionOfResult())()`
Returns the value of the '***read Structural Feature Action Of Result***' container reference.
`[ReadVariableAction](../mdstructuredactions/ReadVariableAction.html)`
`[get_readVariableActionOfResult](#get_readVariableActionOfResult())()`
Returns the value of the '***read Variable Action Of Result***' container reference.
`[ReduceAction](../mdcompleteactions/ReduceAction.html)`
`[get_reduceActionOfResult](#get_reduceActionOfResult())()`
Returns the value of the '***reduce Action Of Result***' container reference.
`[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html)`
`[get_structuredActivityNodeOfStructuredNodeOutput](#get_structuredActivityNodeOfStructuredNodeOutput())()`
Returns the value of the '***structured Activity Node Of Structured Node Output***' container reference.
`[TestIdentityAction](../mdintermediateactions/TestIdentityAction.html)`
`[get_testIdentityActionOfResult](#get_testIdentityActionOfResult())()`
Returns the value of the '***test Identity Action Of Result***' container reference.
`[UnmarshallAction](../mdcompleteactions/UnmarshallAction.html)`
`[get_unmarshallActionOfResult](#get_unmarshallActionOfResult())()`
Returns the value of the '***unmarshall Action Of Result***' container reference.
`[ValueSpecificationAction](../mdintermediateactions/ValueSpecificationAction.html)`
`[get_valueSpecificationActionOfResult](#get_valueSpecificationActionOfResult())()`
Returns the value of the '***value Specification Action Of Result***' container reference.
`[WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html)`
`[get_writeStructuralFeatureActionOfResult](#get_writeStructuralFeatureActionOfResult())()`
Returns the value of the '***write Structural Feature Action Of Result***' container reference.
`boolean`
`[has_clauseOfBodyOutput](#has_clauseOfBodyOutput())()`

`boolean`
`[has_loopNodeOfBodyOutput](#has_loopNodeOfBodyOutput())()`

`void`
`[set_acceptCallActionOfReturnInformation](#set_acceptCallActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction))([AcceptCallAction](../mdcompleteactions/AcceptCallAction.html) value)`
Sets the value of the '[`*accept Call Action Of
 Return Information*`](#get_acceptCallActionOfReturnInformation())' container reference.
`void`
`[set_acceptEventActionOfResult](#set_acceptEventActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))([AcceptEventAction](../mdcompleteactions/AcceptEventAction.html) value)`
Sets the value of the
 '[`*accept Event Action Of Result*`](#get_acceptEventActionOfResult())' container
 reference.
`void`
`[set_actionOfOutput](#set_actionOfOutput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))([Action](Action.html) value)`
Sets the value of the '[`*action Of Output*`](#get_actionOfOutput())' reference.
`void`
`[set_callActionOfResult](#set_callActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction))([CallAction](CallAction.html) value)`
Sets the value of the '[`*call Action Of Result*`](#get_callActionOfResult())' container
 reference.
`void`
`[set_clauseOfDecider](#set_clauseOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause))([Clause](../../activities/mdstructuredactivities/Clause.html) value)`
Sets the value of the '[`*clause Of Decider*`](#get_clauseOfDecider())' reference.
`void`
`[set_clearStructuralFeatureActionOfResult](#set_clearStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction))([ClearStructuralFeatureAction](../mdintermediateactions/ClearStructuralFeatureAction.html) value)`
Sets the value of the '[`*clear Structural
 Feature Action Of Result*`](#get_clearStructuralFeatureActionOfResult())' container reference.
`void`
`[set_conditionalNodeOfResult](#set_conditionalNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode))([ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html) value)`
Sets the value of the '[`*conditional Node Of Result*`](#get_conditionalNodeOfResult())'
 container reference.
`void`
`[set_createLinkObjectActionOfResult](#set_createLinkObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction))([CreateLinkObjectAction](../mdcompleteactions/CreateLinkObjectAction.html) value)`
Sets the value of the
 '[`*create Link Object Action Of Result*`](#get_createLinkObjectActionOfResult())'
 container reference.
`void`
`[set_createObjectActionOfResult](#set_createObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction))([CreateObjectAction](../mdintermediateactions/CreateObjectAction.html) value)`
Sets the value of the
 '[`*create Object Action Of Result*`](#get_createObjectActionOfResult())' container
 reference.
`void`
`[set_loopNodeOfDecider](#set_loopNodeOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))([LoopNode](../../activities/mdstructuredactivities/LoopNode.html) value)`
Sets the value of the '[`*loop Node Of Decider*`](#get_loopNodeOfDecider())' reference.
`void`
`[set_loopNodeOfLoopVariable](#set_loopNodeOfLoopVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))([LoopNode](../../activities/mdstructuredactivities/LoopNode.html) value)`
Sets the value of the '[`*loop Node Of Loop Variable*`](#get_loopNodeOfLoopVariable())'
 container reference.
`void`
`[set_loopNodeOfResult](#set_loopNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))([LoopNode](../../activities/mdstructuredactivities/LoopNode.html) value)`
Sets the value of the '[`*loop Node Of Result*`](#get_loopNodeOfResult())' container
 reference.
`void`
`[set_opaqueActionOfOutputValue](#set_opaqueActionOfOutputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction))([OpaqueAction](OpaqueAction.html) value)`
Sets the value of the
 '[`*opaque Action Of Output Value*`](#get_opaqueActionOfOutputValue())' container
 reference.
`void`
`[set_readExtentActionOfResult](#set_readExtentActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction))([ReadExtentAction](../mdcompleteactions/ReadExtentAction.html) value)`
Sets the value of the
 '[`*read Extent Action Of Result*`](#get_readExtentActionOfResult())' container reference.
`void`
`[set_readIsClassifiedObjectActionOfResult](#set_readIsClassifiedObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction))([ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html) value)`
Sets the value of the '[`*read Is Classified
 Object Action Of Result*`](#get_readIsClassifiedObjectActionOfResult())' container reference.
`void`
`[set_readLinkActionOfResult](#set_readLinkActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction))([ReadLinkAction](../mdintermediateactions/ReadLinkAction.html) value)`
Sets the value of the '[`*read Link Action Of Result*`](#get_readLinkActionOfResult())'
 container reference.
`void`
`[set_readLinkObjectEndActionOfResult](#set_readLinkObjectEndActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction))([ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html) value)`
Sets the value of the '[`*read Link Object End Action
 Of Result*`](#get_readLinkObjectEndActionOfResult())' container reference.
`void`
`[set_readLinkObjectEndQualifierActionOfResult](#set_readLinkObjectEndQualifierActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction))([ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html) value)`
Sets the value of the '[`*read Link Object
 End Qualifier Action Of Result*`](#get_readLinkObjectEndQualifierActionOfResult())' container reference.
`void`
`[set_readSelfActionOfResult](#set_readSelfActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction))([ReadSelfAction](../mdintermediateactions/ReadSelfAction.html) value)`
Sets the value of the '[`*read Self Action Of Result*`](#get_readSelfActionOfResult())'
 container reference.
`void`
`[set_readStructuralFeatureActionOfResult](#set_readStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction))([ReadStructuralFeatureAction](../mdintermediateactions/ReadStructuralFeatureAction.html) value)`
Sets the value of the '[`*read Structural Feature
 Action Of Result*`](#get_readStructuralFeatureActionOfResult())' container reference.
`void`
`[set_readVariableActionOfResult](#set_readVariableActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction))([ReadVariableAction](../mdstructuredactions/ReadVariableAction.html) value)`
Sets the value of the
 '[`*read Variable Action Of Result*`](#get_readVariableActionOfResult())' container
 reference.
`void`
`[set_reduceActionOfResult](#set_reduceActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction))([ReduceAction](../mdcompleteactions/ReduceAction.html) value)`
Sets the value of the '[`*reduce Action Of Result*`](#get_reduceActionOfResult())'
 container reference.
`void`
`[set_structuredActivityNodeOfStructuredNodeOutput](#set_structuredActivityNodeOfStructuredNodeOutput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))([StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html) value)`
Sets the value of the '[`*structured
 Activity Node Of Structured Node Output*`](#get_structuredActivityNodeOfStructuredNodeOutput())' container reference.
`void`
`[set_testIdentityActionOfResult](#set_testIdentityActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction))([TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) value)`
Sets the value of the
 '[`*test Identity Action Of Result*`](#get_testIdentityActionOfResult())' container
 reference.
`void`
`[set_unmarshallActionOfResult](#set_unmarshallActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction))([UnmarshallAction](../mdcompleteactions/UnmarshallAction.html) value)`
Sets the value of the '[`*unmarshall Action Of Result*`](#get_unmarshallActionOfResult())'
 container reference.
`void`
`[set_valueSpecificationActionOfResult](#set_valueSpecificationActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction))([ValueSpecificationAction](../mdintermediateactions/ValueSpecificationAction.html) value)`
Sets the value of the '[`*value Specification Action
 Of Result*`](#get_valueSpecificationActionOfResult())' container reference.
`void`
`[set_writeStructuralFeatureActionOfResult](#set_writeStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction))([WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html) value)`
Sets the value of the '[`*write Structural
 Feature Action Of Result*`](#get_writeStructuralFeatureActionOfResult())' container reference.
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)
`[get_activityNodeOfRedefinedNode](../../activities/mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()), [getActivity](../../activities/mdfundamentalactivities/ActivityNode.html#getActivity()), [getIncoming](../../activities/mdfundamentalactivities/ActivityNode.html#getIncoming()), [getInGroup](../../activities/mdfundamentalactivities/ActivityNode.html#getInGroup()), [getInInterruptibleRegion](../../activities/mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()), [getInPartition](../../activities/mdfundamentalactivities/ActivityNode.html#getInPartition()), [getInStructuredNode](../../activities/mdfundamentalactivities/ActivityNode.html#getInStructuredNode()), [getOutgoing](../../activities/mdfundamentalactivities/ActivityNode.html#getOutgoing()), [getRedefinedNode](../../activities/mdfundamentalactivities/ActivityNode.html#getRedefinedNode()), [has_activityNodeOfRedefinedNode](../../activities/mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()), [hasIncoming](../../activities/mdfundamentalactivities/ActivityNode.html#hasIncoming()), [hasInGroup](../../activities/mdfundamentalactivities/ActivityNode.html#hasInGroup()), [hasInInterruptibleRegion](../../activities/mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()), [hasInPartition](../../activities/mdfundamentalactivities/ActivityNode.html#hasInPartition()), [hasOutgoing](../../activities/mdfundamentalactivities/ActivityNode.html#hasOutgoing()), [hasRedefinedNode](../../activities/mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()), [setActivity](../../activities/mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)), [setInStructuredNode](../../activities/mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))`
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
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[MultiplicityElement](../../classes/mdkernel/MultiplicityElement.html)
`[getLower](../../classes/mdkernel/MultiplicityElement.html#getLower()), [getLowerValue](../../classes/mdkernel/MultiplicityElement.html#getLowerValue()), [getUpper](../../classes/mdkernel/MultiplicityElement.html#getUpper()), [getUpperValue](../../classes/mdkernel/MultiplicityElement.html#getUpperValue()), [isOrdered](../../classes/mdkernel/MultiplicityElement.html#isOrdered()), [isUnique](../../classes/mdkernel/MultiplicityElement.html#isUnique()), [setLowerValue](../../classes/mdkernel/MultiplicityElement.html#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setOrdered](../../classes/mdkernel/MultiplicityElement.html#setOrdered(boolean)), [setUnique](../../classes/mdkernel/MultiplicityElement.html#setUnique(boolean)), [setUpperValue](../../classes/mdkernel/MultiplicityElement.html#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)
`[get_exceptionHandlerOfExceptionInput](../../activities/mdbasicactivities/ObjectNode.html#get_exceptionHandlerOfExceptionInput()), [getInState](../../activities/mdbasicactivities/ObjectNode.html#getInState()), [getOrdering](../../activities/mdbasicactivities/ObjectNode.html#getOrdering()), [getSelection](../../activities/mdbasicactivities/ObjectNode.html#getSelection()), [getUpperBound](../../activities/mdbasicactivities/ObjectNode.html#getUpperBound()), [has_exceptionHandlerOfExceptionInput](../../activities/mdbasicactivities/ObjectNode.html#has_exceptionHandlerOfExceptionInput()), [hasInState](../../activities/mdbasicactivities/ObjectNode.html#hasInState()), [isControlType](../../activities/mdbasicactivities/ObjectNode.html#isControlType()), [setControlType](../../activities/mdbasicactivities/ObjectNode.html#setControlType(boolean)), [setOrdering](../../activities/mdbasicactivities/ObjectNode.html#setOrdering(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKind)), [setSelection](../../activities/mdbasicactivities/ObjectNode.html#setSelection(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)), [setUpperBound](../../activities/mdbasicactivities/ObjectNode.html#setUpperBound(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.[Pin](Pin.html)
`[isControl](Pin.html#isControl()), [setControl](Pin.html#setControl(boolean))`
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
get_clearStructuralFeatureActionOfResult
@CheckForNull[ClearStructuralFeatureAction](../mdintermediateactions/ClearStructuralFeatureAction.html) get_clearStructuralFeatureActionOfResult()
Returns the value of the '***clear Structural Feature Action Of Result***' container reference.
 It is bidirectional and its opposite is
 '[`*Result*`](../mdintermediateactions/ClearStructuralFeatureAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*clear Structural Feature Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*clear Structural Feature Action Of Result*' container reference.
See Also:
[`set_clearStructuralFeatureActionOfResult(ClearStructuralFeatureAction)`](#set_clearStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction))
[`UMLPackage.getOutputPin__clearStructuralFeatureActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__clearStructuralFeatureActionOfResult())
[`ClearStructuralFeatureAction.getResult()`](../mdintermediateactions/ClearStructuralFeatureAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_clearStructuralFeatureActionOfResult
void set_clearStructuralFeatureActionOfResult(@CheckForNull
 [ClearStructuralFeatureAction](../mdintermediateactions/ClearStructuralFeatureAction.html) value)
Sets the value of the '[`*clear Structural
 Feature Action Of Result*`](#get_clearStructuralFeatureActionOfResult())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*clear Structural Feature Action Of Result*' container reference.
See Also:
[`get_clearStructuralFeatureActionOfResult()`](#get_clearStructuralFeatureActionOfResult())
Generated:
get_writeStructuralFeatureActionOfResult
@CheckForNull[WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html) get_writeStructuralFeatureActionOfResult()
Returns the value of the '***write Structural Feature Action Of Result***' container reference.
 It is bidirectional and its opposite is
 '[`*Result*`](../mdintermediateactions/WriteStructuralFeatureAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*write Structural Feature Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*write Structural Feature Action Of Result*' container reference.
See Also:
[`set_writeStructuralFeatureActionOfResult(WriteStructuralFeatureAction)`](#set_writeStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction))
[`UMLPackage.getOutputPin__writeStructuralFeatureActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__writeStructuralFeatureActionOfResult())
[`WriteStructuralFeatureAction.getResult()`](../mdintermediateactions/WriteStructuralFeatureAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_writeStructuralFeatureActionOfResult
void set_writeStructuralFeatureActionOfResult(@CheckForNull
 [WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html) value)
Sets the value of the '[`*write Structural
 Feature Action Of Result*`](#get_writeStructuralFeatureActionOfResult())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*write Structural Feature Action Of Result*' container reference.
See Also:
[`get_writeStructuralFeatureActionOfResult()`](#get_writeStructuralFeatureActionOfResult())
Generated:
get_createLinkObjectActionOfResult
@CheckForNull[CreateLinkObjectAction](../mdcompleteactions/CreateLinkObjectAction.html) get_createLinkObjectActionOfResult()
Returns the value of the '***create Link Object Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdcompleteactions/CreateLinkObjectAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*create Link Object Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*create Link Object Action Of Result*' container reference.
See Also:
[`set_createLinkObjectActionOfResult(CreateLinkObjectAction)`](#set_createLinkObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction))
[`UMLPackage.getOutputPin__createLinkObjectActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__createLinkObjectActionOfResult())
[`CreateLinkObjectAction.getResult()`](../mdcompleteactions/CreateLinkObjectAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_createLinkObjectActionOfResult
void set_createLinkObjectActionOfResult(@CheckForNull
 [CreateLinkObjectAction](../mdcompleteactions/CreateLinkObjectAction.html) value)
Sets the value of the
 '[`*create Link Object Action Of Result*`](#get_createLinkObjectActionOfResult())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*create Link Object Action Of Result*' container reference.
See Also:
[`get_createLinkObjectActionOfResult()`](#get_createLinkObjectActionOfResult())
Generated:
get_acceptEventActionOfResult
@CheckForNull[AcceptEventAction](../mdcompleteactions/AcceptEventAction.html) get_acceptEventActionOfResult()
Returns the value of the '***accept Event Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdcompleteactions/AcceptEventAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*accept Event Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*accept Event Action Of Result*' container reference.
See Also:
[`set_acceptEventActionOfResult(AcceptEventAction)`](#set_acceptEventActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction))
[`UMLPackage.getOutputPin__acceptEventActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__acceptEventActionOfResult())
[`AcceptEventAction.getResult()`](../mdcompleteactions/AcceptEventAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_acceptEventActionOfResult
void set_acceptEventActionOfResult(@CheckForNull
 [AcceptEventAction](../mdcompleteactions/AcceptEventAction.html) value)
Sets the value of the
 '[`*accept Event Action Of Result*`](#get_acceptEventActionOfResult())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*accept Event Action Of Result*' container reference.
See Also:
[`get_acceptEventActionOfResult()`](#get_acceptEventActionOfResult())
Generated:
get_readLinkObjectEndActionOfResult
@CheckForNull[ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html) get_readLinkObjectEndActionOfResult()
Returns the value of the '***read Link Object End Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdcompleteactions/ReadLinkObjectEndAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*read Link Object End Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Link Object End Action Of Result*' container reference.
See Also:
[`set_readLinkObjectEndActionOfResult(ReadLinkObjectEndAction)`](#set_readLinkObjectEndActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction))
[`UMLPackage.getOutputPin__readLinkObjectEndActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__readLinkObjectEndActionOfResult())
[`ReadLinkObjectEndAction.getResult()`](../mdcompleteactions/ReadLinkObjectEndAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_readLinkObjectEndActionOfResult
void set_readLinkObjectEndActionOfResult(@CheckForNull
 [ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html) value)
Sets the value of the '[`*read Link Object End Action
 Of Result*`](#get_readLinkObjectEndActionOfResult())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Link Object End Action Of Result*' container reference.
See Also:
[`get_readLinkObjectEndActionOfResult()`](#get_readLinkObjectEndActionOfResult())
Generated:
get_readIsClassifiedObjectActionOfResult
@CheckForNull[ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html) get_readIsClassifiedObjectActionOfResult()
Returns the value of the '***read Is Classified Object Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdcompleteactions/ReadIsClassifiedObjectAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*read Is Classified Object Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Is Classified Object Action Of Result*' container reference.
See Also:
[`set_readIsClassifiedObjectActionOfResult(ReadIsClassifiedObjectAction)`](#set_readIsClassifiedObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction))
[`UMLPackage.getOutputPin__readIsClassifiedObjectActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__readIsClassifiedObjectActionOfResult())
[`ReadIsClassifiedObjectAction.getResult()`](../mdcompleteactions/ReadIsClassifiedObjectAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_readIsClassifiedObjectActionOfResult
void set_readIsClassifiedObjectActionOfResult(@CheckForNull
 [ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html) value)
Sets the value of the '[`*read Is Classified
 Object Action Of Result*`](#get_readIsClassifiedObjectActionOfResult())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Is Classified Object Action Of Result*' container reference.
See Also:
[`get_readIsClassifiedObjectActionOfResult()`](#get_readIsClassifiedObjectActionOfResult())
Generated:
get_readExtentActionOfResult
@CheckForNull[ReadExtentAction](../mdcompleteactions/ReadExtentAction.html) get_readExtentActionOfResult()
Returns the value of the '***read Extent Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdcompleteactions/ReadExtentAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*read Extent Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Extent Action Of Result*' container reference.
See Also:
[`set_readExtentActionOfResult(ReadExtentAction)`](#set_readExtentActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction))
[`UMLPackage.getOutputPin__readExtentActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__readExtentActionOfResult())
[`ReadExtentAction.getResult()`](../mdcompleteactions/ReadExtentAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_readExtentActionOfResult
void set_readExtentActionOfResult(@CheckForNull
 [ReadExtentAction](../mdcompleteactions/ReadExtentAction.html) value)
Sets the value of the
 '[`*read Extent Action Of Result*`](#get_readExtentActionOfResult())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Extent Action Of Result*' container reference.
See Also:
[`get_readExtentActionOfResult()`](#get_readExtentActionOfResult())
Generated:
get_readLinkObjectEndQualifierActionOfResult
@CheckForNull[ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html) get_readLinkObjectEndQualifierActionOfResult()
Returns the value of the '***read Link Object End Qualifier Action Of Result***' container reference.
 It is bidirectional and its opposite is
 '[`*Result*`](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*read Link Object End Qualifier Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Link Object End Qualifier Action Of Result*' container reference.
See Also:
[`set_readLinkObjectEndQualifierActionOfResult(ReadLinkObjectEndQualifierAction)`](#set_readLinkObjectEndQualifierActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction))
[`UMLPackage.getOutputPin__readLinkObjectEndQualifierActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__readLinkObjectEndQualifierActionOfResult())
[`ReadLinkObjectEndQualifierAction.getResult()`](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_readLinkObjectEndQualifierActionOfResult
void set_readLinkObjectEndQualifierActionOfResult(@CheckForNull
 [ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html) value)
Sets the value of the '[`*read Link Object
 End Qualifier Action Of Result*`](#get_readLinkObjectEndQualifierActionOfResult())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Link Object End Qualifier Action Of Result*' container reference.
See Also:
[`get_readLinkObjectEndQualifierActionOfResult()`](#get_readLinkObjectEndQualifierActionOfResult())
Generated:
get_unmarshallActionOfResult
@CheckForNull[UnmarshallAction](../mdcompleteactions/UnmarshallAction.html) get_unmarshallActionOfResult()
Returns the value of the '***unmarshall Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdcompleteactions/UnmarshallAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*unmarshall Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*unmarshall Action Of Result*' container reference.
See Also:
[`set_unmarshallActionOfResult(UnmarshallAction)`](#set_unmarshallActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction))
[`UMLPackage.getOutputPin__unmarshallActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__unmarshallActionOfResult())
[`UnmarshallAction.getResult()`](../mdcompleteactions/UnmarshallAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_unmarshallActionOfResult
void set_unmarshallActionOfResult(@CheckForNull
 [UnmarshallAction](../mdcompleteactions/UnmarshallAction.html) value)
Sets the value of the '[`*unmarshall Action Of Result*`](#get_unmarshallActionOfResult())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*unmarshall Action Of Result*' container reference.
See Also:
[`get_unmarshallActionOfResult()`](#get_unmarshallActionOfResult())
Generated:
get_acceptCallActionOfReturnInformation
@CheckForNull[AcceptCallAction](../mdcompleteactions/AcceptCallAction.html) get_acceptCallActionOfReturnInformation()
Returns the value of the '***accept Call Action Of Return Information***' container reference.
 It is bidirectional and its opposite is
 '[`*Return Information*`](../mdcompleteactions/AcceptCallAction.html#getReturnInformation())'.
 begin-user-doc 
If the meaning of the '*accept Call Action Of Return Information*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*accept Call Action Of Return Information*' container reference.
See Also:
[`set_acceptCallActionOfReturnInformation(AcceptCallAction)`](#set_acceptCallActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction))
[`UMLPackage.getOutputPin__acceptCallActionOfReturnInformation()`](../../metadata/UMLPackage.html#getOutputPin__acceptCallActionOfReturnInformation())
[`AcceptCallAction.getReturnInformation()`](../mdcompleteactions/AcceptCallAction.html#getReturnInformation())
Model:
opposite="returnInformation" transient="false" ordered="false"
Generated:
set_acceptCallActionOfReturnInformation
void set_acceptCallActionOfReturnInformation(@CheckForNull
 [AcceptCallAction](../mdcompleteactions/AcceptCallAction.html) value)
Sets the value of the '[`*accept Call Action Of
 Return Information*`](#get_acceptCallActionOfReturnInformation())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*accept Call Action Of Return Information*' container reference.
See Also:
[`get_acceptCallActionOfReturnInformation()`](#get_acceptCallActionOfReturnInformation())
Generated:
get_callActionOfResult
@CheckForNull[CallAction](CallAction.html) get_callActionOfResult()
Returns the value of the '***call Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](CallAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*call Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*call Action Of Result*' container reference.
See Also:
[`set_callActionOfResult(CallAction)`](#set_callActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction))
[`UMLPackage.getOutputPin__callActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__callActionOfResult())
[`CallAction.getResult()`](CallAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_callActionOfResult
void set_callActionOfResult(@CheckForNull
 [CallAction](CallAction.html) value)
Sets the value of the '[`*call Action Of Result*`](#get_callActionOfResult())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*call Action Of Result*' container reference.
See Also:
[`get_callActionOfResult()`](#get_callActionOfResult())
Generated:
get_reduceActionOfResult
@CheckForNull[ReduceAction](../mdcompleteactions/ReduceAction.html) get_reduceActionOfResult()
Returns the value of the '***reduce Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdcompleteactions/ReduceAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*reduce Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reduce Action Of Result*' container reference.
See Also:
[`set_reduceActionOfResult(ReduceAction)`](#set_reduceActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction))
[`UMLPackage.getOutputPin__reduceActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__reduceActionOfResult())
[`ReduceAction.getResult()`](../mdcompleteactions/ReduceAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_reduceActionOfResult
void set_reduceActionOfResult(@CheckForNull
 [ReduceAction](../mdcompleteactions/ReduceAction.html) value)
Sets the value of the '[`*reduce Action Of Result*`](#get_reduceActionOfResult())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*reduce Action Of Result*' container reference.
See Also:
[`get_reduceActionOfResult()`](#get_reduceActionOfResult())
Generated:
get_clauseOfDecider
@CheckForNull[Clause](../../activities/mdstructuredactivities/Clause.html) get_clauseOfDecider()
Returns the value of the '***clause Of Decider***' reference.
 It is bidirectional and its opposite is '[`*Decider*`](../../activities/mdstructuredactivities/Clause.html#getDecider())'.
 begin-user-doc 
If the meaning of the '*clause Of Decider*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*clause Of Decider*' reference.
See Also:
[`set_clauseOfDecider(Clause)`](#set_clauseOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause))
[`UMLPackage.getOutputPin__clauseOfDecider()`](../../metadata/UMLPackage.html#getOutputPin__clauseOfDecider())
[`Clause.getDecider()`](../../activities/mdstructuredactivities/Clause.html#getDecider())
Model:
opposite="decider" ordered="false"
Generated:
set_clauseOfDecider
void set_clauseOfDecider(@CheckForNull
 [Clause](../../activities/mdstructuredactivities/Clause.html) value)
Sets the value of the '[`*clause Of Decider*`](#get_clauseOfDecider())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*clause Of Decider*' reference.
See Also:
[`get_clauseOfDecider()`](#get_clauseOfDecider())
Generated:
get_clauseOfBodyOutput
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Clause](../../activities/mdstructuredactivities/Clause.html)> get_clauseOfBodyOutput()
Returns the value of the '***clause Of Body Output***' reference list.
 The list contents are of type [`Clause`](../../activities/mdstructuredactivities/Clause.html).
 It is bidirectional and its opposite is '[`*Body Output*`](../../activities/mdstructuredactivities/Clause.html#getBodyOutput())'.
 begin-user-doc 
If the meaning of the '*clause Of Body Output*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*clause Of Body Output*' reference list.
See Also:
[`UMLPackage.getOutputPin__clauseOfBodyOutput()`](../../metadata/UMLPackage.html#getOutputPin__clauseOfBodyOutput())
[`Clause.getBodyOutput()`](../../activities/mdstructuredactivities/Clause.html#getBodyOutput())
Model:
opposite="bodyOutput" ordered="false"
Generated:
get_conditionalNodeOfResult
@CheckForNull[ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html) get_conditionalNodeOfResult()
Returns the value of the '***conditional Node Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../../activities/mdstructuredactivities/ConditionalNode.html#getResult())'.
 begin-user-doc 
If the meaning of the '*conditional Node Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*conditional Node Of Result*' container reference.
See Also:
[`set_conditionalNodeOfResult(ConditionalNode)`](#set_conditionalNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode))
[`UMLPackage.getOutputPin__conditionalNodeOfResult()`](../../metadata/UMLPackage.html#getOutputPin__conditionalNodeOfResult())
[`ConditionalNode.getResult()`](../../activities/mdstructuredactivities/ConditionalNode.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_conditionalNodeOfResult
void set_conditionalNodeOfResult(@CheckForNull
 [ConditionalNode](../../activities/mdstructuredactivities/ConditionalNode.html) value)
Sets the value of the '[`*conditional Node Of Result*`](#get_conditionalNodeOfResult())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*conditional Node Of Result*' container reference.
See Also:
[`get_conditionalNodeOfResult()`](#get_conditionalNodeOfResult())
Generated:
get_actionOfOutput
@CheckForNull[Action](Action.html) get_actionOfOutput()
Returns the value of the '***action Of Output***' reference.
 It is bidirectional and its opposite is '[`*Output*`](Action.html#getOutput())'.
 begin-user-doc 
If the meaning of the '*action Of Output*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*action Of Output*' reference.
See Also:
[`set_actionOfOutput(Action)`](#set_actionOfOutput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))
[`UMLPackage.getOutputPin__actionOfOutput()`](../../metadata/UMLPackage.html#getOutputPin__actionOfOutput())
[`Action.getOutput()`](Action.html#getOutput())
Model:
opposite="output" transient="true" volatile="true" derived="true" ordered="false"
Generated:
set_actionOfOutput
void set_actionOfOutput(@CheckForNull
 [Action](Action.html) value)
Sets the value of the '[`*action Of Output*`](#get_actionOfOutput())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*action Of Output*' reference.
See Also:
[`get_actionOfOutput()`](#get_actionOfOutput())
Generated:
get_testIdentityActionOfResult
@CheckForNull[TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) get_testIdentityActionOfResult()
Returns the value of the '***test Identity Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdintermediateactions/TestIdentityAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*test Identity Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*test Identity Action Of Result*' container reference.
See Also:
[`set_testIdentityActionOfResult(TestIdentityAction)`](#set_testIdentityActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction))
[`UMLPackage.getOutputPin__testIdentityActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__testIdentityActionOfResult())
[`TestIdentityAction.getResult()`](../mdintermediateactions/TestIdentityAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_testIdentityActionOfResult
void set_testIdentityActionOfResult(@CheckForNull
 [TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) value)
Sets the value of the
 '[`*test Identity Action Of Result*`](#get_testIdentityActionOfResult())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*test Identity Action Of Result*' container reference.
See Also:
[`get_testIdentityActionOfResult()`](#get_testIdentityActionOfResult())
Generated:
get_readLinkActionOfResult
@CheckForNull[ReadLinkAction](../mdintermediateactions/ReadLinkAction.html) get_readLinkActionOfResult()
Returns the value of the '***read Link Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdintermediateactions/ReadLinkAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*read Link Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Link Action Of Result*' container reference.
See Also:
[`set_readLinkActionOfResult(ReadLinkAction)`](#set_readLinkActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction))
[`UMLPackage.getOutputPin__readLinkActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__readLinkActionOfResult())
[`ReadLinkAction.getResult()`](../mdintermediateactions/ReadLinkAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_readLinkActionOfResult
void set_readLinkActionOfResult(@CheckForNull
 [ReadLinkAction](../mdintermediateactions/ReadLinkAction.html) value)
Sets the value of the '[`*read Link Action Of Result*`](#get_readLinkActionOfResult())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Link Action Of Result*' container reference.
See Also:
[`get_readLinkActionOfResult()`](#get_readLinkActionOfResult())
Generated:
get_readSelfActionOfResult
@CheckForNull[ReadSelfAction](../mdintermediateactions/ReadSelfAction.html) get_readSelfActionOfResult()
Returns the value of the '***read Self Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdintermediateactions/ReadSelfAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*read Self Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Self Action Of Result*' container reference.
See Also:
[`set_readSelfActionOfResult(ReadSelfAction)`](#set_readSelfActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction))
[`UMLPackage.getOutputPin__readSelfActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__readSelfActionOfResult())
[`ReadSelfAction.getResult()`](../mdintermediateactions/ReadSelfAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_readSelfActionOfResult
void set_readSelfActionOfResult(@CheckForNull
 [ReadSelfAction](../mdintermediateactions/ReadSelfAction.html) value)
Sets the value of the '[`*read Self Action Of Result*`](#get_readSelfActionOfResult())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Self Action Of Result*' container reference.
See Also:
[`get_readSelfActionOfResult()`](#get_readSelfActionOfResult())
Generated:
get_loopNodeOfResult
@CheckForNull[LoopNode](../../activities/mdstructuredactivities/LoopNode.html) get_loopNodeOfResult()
Returns the value of the '***loop Node Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../../activities/mdstructuredactivities/LoopNode.html#getResult())'.
 begin-user-doc 
If the meaning of the '*loop Node Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*loop Node Of Result*' container reference.
See Also:
[`set_loopNodeOfResult(LoopNode)`](#set_loopNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))
[`UMLPackage.getOutputPin__loopNodeOfResult()`](../../metadata/UMLPackage.html#getOutputPin__loopNodeOfResult())
[`LoopNode.getResult()`](../../activities/mdstructuredactivities/LoopNode.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_loopNodeOfResult
void set_loopNodeOfResult(@CheckForNull
 [LoopNode](../../activities/mdstructuredactivities/LoopNode.html) value)
Sets the value of the '[`*loop Node Of Result*`](#get_loopNodeOfResult())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*loop Node Of Result*' container reference.
See Also:
[`get_loopNodeOfResult()`](#get_loopNodeOfResult())
Generated:
get_valueSpecificationActionOfResult
@CheckForNull[ValueSpecificationAction](../mdintermediateactions/ValueSpecificationAction.html) get_valueSpecificationActionOfResult()
Returns the value of the '***value Specification Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdintermediateactions/ValueSpecificationAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*value Specification Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*value Specification Action Of Result*' container reference.
See Also:
[`set_valueSpecificationActionOfResult(ValueSpecificationAction)`](#set_valueSpecificationActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction))
[`UMLPackage.getOutputPin__valueSpecificationActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__valueSpecificationActionOfResult())
[`ValueSpecificationAction.getResult()`](../mdintermediateactions/ValueSpecificationAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_valueSpecificationActionOfResult
void set_valueSpecificationActionOfResult(@CheckForNull
 [ValueSpecificationAction](../mdintermediateactions/ValueSpecificationAction.html) value)
Sets the value of the '[`*value Specification Action
 Of Result*`](#get_valueSpecificationActionOfResult())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*value Specification Action Of Result*' container reference.
See Also:
[`get_valueSpecificationActionOfResult()`](#get_valueSpecificationActionOfResult())
Generated:
get_loopNodeOfLoopVariable
@CheckForNull[LoopNode](../../activities/mdstructuredactivities/LoopNode.html) get_loopNodeOfLoopVariable()
Returns the value of the '***loop Node Of Loop Variable***' container reference.
 It is bidirectional and its opposite is
 '[`*Loop Variable*`](../../activities/mdstructuredactivities/LoopNode.html#getLoopVariable())'.
 begin-user-doc 
If the meaning of the '*loop Node Of Loop Variable*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*loop Node Of Loop Variable*' container reference.
See Also:
[`set_loopNodeOfLoopVariable(LoopNode)`](#set_loopNodeOfLoopVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))
[`UMLPackage.getOutputPin__loopNodeOfLoopVariable()`](../../metadata/UMLPackage.html#getOutputPin__loopNodeOfLoopVariable())
[`LoopNode.getLoopVariable()`](../../activities/mdstructuredactivities/LoopNode.html#getLoopVariable())
Model:
opposite="loopVariable" transient="false" ordered="false"
Generated:
set_loopNodeOfLoopVariable
void set_loopNodeOfLoopVariable(@CheckForNull
 [LoopNode](../../activities/mdstructuredactivities/LoopNode.html) value)
Sets the value of the '[`*loop Node Of Loop Variable*`](#get_loopNodeOfLoopVariable())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*loop Node Of Loop Variable*' container reference.
See Also:
[`get_loopNodeOfLoopVariable()`](#get_loopNodeOfLoopVariable())
Generated:
get_readVariableActionOfResult
@CheckForNull[ReadVariableAction](../mdstructuredactions/ReadVariableAction.html) get_readVariableActionOfResult()
Returns the value of the '***read Variable Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdstructuredactions/ReadVariableAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*read Variable Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Variable Action Of Result*' container reference.
See Also:
[`set_readVariableActionOfResult(ReadVariableAction)`](#set_readVariableActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction))
[`UMLPackage.getOutputPin__readVariableActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__readVariableActionOfResult())
[`ReadVariableAction.getResult()`](../mdstructuredactions/ReadVariableAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_readVariableActionOfResult
void set_readVariableActionOfResult(@CheckForNull
 [ReadVariableAction](../mdstructuredactions/ReadVariableAction.html) value)
Sets the value of the
 '[`*read Variable Action Of Result*`](#get_readVariableActionOfResult())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Variable Action Of Result*' container reference.
See Also:
[`get_readVariableActionOfResult()`](#get_readVariableActionOfResult())
Generated:
get_structuredActivityNodeOfStructuredNodeOutput
@CheckForNull[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html) get_structuredActivityNodeOfStructuredNodeOutput()
Returns the value of the '***structured Activity Node Of Structured Node Output***' container reference.
 It is bidirectional and its opposite is
 '[`*Structured Node Output*`](../../activities/mdstructuredactivities/StructuredActivityNode.html#getStructuredNodeOutput())'.
 begin-user-doc 
If the meaning of the '*structured Activity Node Of Structured Node Output*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*structured Activity Node Of Structured Node Output*' container reference.
See Also:
[`set_structuredActivityNodeOfStructuredNodeOutput(StructuredActivityNode)`](#set_structuredActivityNodeOfStructuredNodeOutput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))
[`UMLPackage.getOutputPin__structuredActivityNodeOfStructuredNodeOutput()`](../../metadata/UMLPackage.html#getOutputPin__structuredActivityNodeOfStructuredNodeOutput())
[`StructuredActivityNode.getStructuredNodeOutput()`](../../activities/mdstructuredactivities/StructuredActivityNode.html#getStructuredNodeOutput())
Model:
opposite="structuredNodeOutput" transient="false" ordered="false"
Generated:
set_structuredActivityNodeOfStructuredNodeOutput
void set_structuredActivityNodeOfStructuredNodeOutput(@CheckForNull
 [StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html) value)
Sets the value of the '[`*structured
 Activity Node Of Structured Node Output*`](#get_structuredActivityNodeOfStructuredNodeOutput())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*structured Activity Node Of Structured Node Output*' container reference.
See Also:
[`get_structuredActivityNodeOfStructuredNodeOutput()`](#get_structuredActivityNodeOfStructuredNodeOutput())
Generated:
get_loopNodeOfBodyOutput
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)> get_loopNodeOfBodyOutput()
Returns the value of the '***loop Node Of Body Output***' reference list.
 The list contents are of type [`LoopNode`](../../activities/mdstructuredactivities/LoopNode.html).
 It is bidirectional and its opposite is '[`*Body Output*`](../../activities/mdstructuredactivities/LoopNode.html#getBodyOutput())'.
 begin-user-doc 
If the meaning of the '*loop Node Of Body Output*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*loop Node Of Body Output*' reference list.
See Also:
[`UMLPackage.getOutputPin__loopNodeOfBodyOutput()`](../../metadata/UMLPackage.html#getOutputPin__loopNodeOfBodyOutput())
[`LoopNode.getBodyOutput()`](../../activities/mdstructuredactivities/LoopNode.html#getBodyOutput())
Model:
opposite="bodyOutput" ordered="false"
Generated:
get_createObjectActionOfResult
@CheckForNull[CreateObjectAction](../mdintermediateactions/CreateObjectAction.html) get_createObjectActionOfResult()
Returns the value of the '***create Object Action Of Result***' container reference.
 It is bidirectional and its opposite is '[`*Result*`](../mdintermediateactions/CreateObjectAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*create Object Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*create Object Action Of Result*' container reference.
See Also:
[`set_createObjectActionOfResult(CreateObjectAction)`](#set_createObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction))
[`UMLPackage.getOutputPin__createObjectActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__createObjectActionOfResult())
[`CreateObjectAction.getResult()`](../mdintermediateactions/CreateObjectAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_createObjectActionOfResult
void set_createObjectActionOfResult(@CheckForNull
 [CreateObjectAction](../mdintermediateactions/CreateObjectAction.html) value)
Sets the value of the
 '[`*create Object Action Of Result*`](#get_createObjectActionOfResult())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*create Object Action Of Result*' container reference.
See Also:
[`get_createObjectActionOfResult()`](#get_createObjectActionOfResult())
Generated:
get_readStructuralFeatureActionOfResult
@CheckForNull[ReadStructuralFeatureAction](../mdintermediateactions/ReadStructuralFeatureAction.html) get_readStructuralFeatureActionOfResult()
Returns the value of the '***read Structural Feature Action Of Result***' container reference.
 It is bidirectional and its opposite is
 '[`*Result*`](../mdintermediateactions/ReadStructuralFeatureAction.html#getResult())'.
 begin-user-doc 
If the meaning of the '*read Structural Feature Action Of Result*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Structural Feature Action Of Result*' container reference.
See Also:
[`set_readStructuralFeatureActionOfResult(ReadStructuralFeatureAction)`](#set_readStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction))
[`UMLPackage.getOutputPin__readStructuralFeatureActionOfResult()`](../../metadata/UMLPackage.html#getOutputPin__readStructuralFeatureActionOfResult())
[`ReadStructuralFeatureAction.getResult()`](../mdintermediateactions/ReadStructuralFeatureAction.html#getResult())
Model:
opposite="result" transient="false" ordered="false"
Generated:
set_readStructuralFeatureActionOfResult
void set_readStructuralFeatureActionOfResult(@CheckForNull
 [ReadStructuralFeatureAction](../mdintermediateactions/ReadStructuralFeatureAction.html) value)
Sets the value of the '[`*read Structural Feature
 Action Of Result*`](#get_readStructuralFeatureActionOfResult())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Structural Feature Action Of Result*' container reference.
See Also:
[`get_readStructuralFeatureActionOfResult()`](#get_readStructuralFeatureActionOfResult())
Generated:
get_opaqueActionOfOutputValue
@CheckForNull[OpaqueAction](OpaqueAction.html) get_opaqueActionOfOutputValue()
Returns the value of the '***opaque Action Of Output Value***' container reference.
 It is bidirectional and its opposite is '[`*Output Value*`](OpaqueAction.html#getOutputValue())'.
 begin-user-doc 
If the meaning of the '*opaque Action Of Output Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*opaque Action Of Output Value*' container reference.
See Also:
[`set_opaqueActionOfOutputValue(OpaqueAction)`](#set_opaqueActionOfOutputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction))
[`UMLPackage.getOutputPin__opaqueActionOfOutputValue()`](../../metadata/UMLPackage.html#getOutputPin__opaqueActionOfOutputValue())
[`OpaqueAction.getOutputValue()`](OpaqueAction.html#getOutputValue())
Model:
opposite="outputValue" transient="false" ordered="false"
Generated:
set_opaqueActionOfOutputValue
void set_opaqueActionOfOutputValue(@CheckForNull
 [OpaqueAction](OpaqueAction.html) value)
Sets the value of the
 '[`*opaque Action Of Output Value*`](#get_opaqueActionOfOutputValue())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*opaque Action Of Output Value*' container reference.
See Also:
[`get_opaqueActionOfOutputValue()`](#get_opaqueActionOfOutputValue())
Generated:
get_loopNodeOfDecider
@CheckForNull[LoopNode](../../activities/mdstructuredactivities/LoopNode.html) get_loopNodeOfDecider()
Returns the value of the '***loop Node Of Decider***' reference.
 It is bidirectional and its opposite is '[`*Decider*`](../../activities/mdstructuredactivities/LoopNode.html#getDecider())'.
 begin-user-doc 
If the meaning of the '*loop Node Of Decider*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*loop Node Of Decider*' reference.
See Also:
[`set_loopNodeOfDecider(LoopNode)`](#set_loopNodeOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))
[`UMLPackage.getOutputPin__loopNodeOfDecider()`](../../metadata/UMLPackage.html#getOutputPin__loopNodeOfDecider())
[`LoopNode.getDecider()`](../../activities/mdstructuredactivities/LoopNode.html#getDecider())
Model:
opposite="decider" ordered="false"
Generated:
set_loopNodeOfDecider
void set_loopNodeOfDecider(@CheckForNull
 [LoopNode](../../activities/mdstructuredactivities/LoopNode.html) value)
Sets the value of the '[`*loop Node Of Decider*`](#get_loopNodeOfDecider())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*loop Node Of Decider*' reference.
See Also:
[`get_loopNodeOfDecider()`](#get_loopNodeOfDecider())
Generated:
has_clauseOfBodyOutput
boolean has_clauseOfBodyOutput()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_loopNodeOfBodyOutput
boolean has_loopNodeOfBodyOutput()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions</a></div>
<h1 class="title" title="Interface OutputPin">Interface OutputPin</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></code>, <code><a href="Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">OutputPin</span><span class="extends-implements">
extends <a href="Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Output Pin</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An OutputPin is a Pin that holds output values produced by an Action.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_structuredActivityNodeOfStructuredNodeOutput()"><code><em>structured Activity Node Of Structured Node Output</em></code></a></li>
<li><a href="#get_readExtentActionOfResult()"><code><em>read Extent Action Of Result</em></code></a></li>
<li><a href="#get_conditionalNodeOfResult()"><code><em>conditional Node Of Result</em></code></a></li>
<li><a href="#get_clauseOfBodyOutput()"><code><em>clause Of Body Output</em></code></a></li>
<li><a href="#get_clauseOfDecider()"><code><em>clause Of Decider</em></code></a></li>
<li><a href="#get_loopNodeOfLoopVariable()"><code><em>loop Node Of Loop Variable</em></code></a></li>
<li><a href="#get_loopNodeOfBodyOutput()"><code><em>loop Node Of Body Output</em></code></a></li>
<li><a href="#get_loopNodeOfDecider()"><code><em>loop Node Of Decider</em></code></a></li>
<li><a href="#get_loopNodeOfResult()"><code><em>loop Node Of Result</em></code></a></li>
<li><a href="#get_reduceActionOfResult()"><code><em>reduce Action Of Result</em></code></a></li>
<li><a href="#get_actionOfOutput()"><code><em>action Of Output</em></code></a></li>
<li><a href="#get_createObjectActionOfResult()"><code><em>create Object Action Of Result</em></code></a></li>
<li><a href="#get_unmarshallActionOfResult()"><code><em>unmarshall Action Of Result</em></code></a></li>
<li><a href="#get_opaqueActionOfOutputValue()"><code><em>opaque Action Of Output Value</em></code></a></li>
<li><a href="#get_readLinkActionOfResult()"><code><em>read Link Action Of Result</em></code></a></li>
<li><a href="#get_readLinkObjectEndActionOfResult()"><code><em>read Link Object End Action Of Result</em></code></a></li>
<li><a href="#get_acceptCallActionOfReturnInformation()"><code><em>accept Call Action Of Return Information</em></code></a></li>
<li><a href="#get_writeStructuralFeatureActionOfResult()"><code><em>write Structural Feature Action Of Result</em></code></a></li>
<li><a href="#get_createLinkObjectActionOfResult()"><code><em>create Link Object Action Of Result</em></code></a></li>
<li><a href="#get_readStructuralFeatureActionOfResult()"><code><em>read Structural Feature Action Of Result</em></code></a></li>
<li><a href="#get_clearStructuralFeatureActionOfResult()"><code><em>clear Structural Feature Action Of Result</em></code></a></li>
<li><a href="#get_valueSpecificationActionOfResult()"><code><em>value Specification Action Of Result</em></code></a></li>
<li><a href="#get_testIdentityActionOfResult()"><code><em>test Identity Action Of Result</em></code></a></li>
<li><a href="#get_readIsClassifiedObjectActionOfResult()"><code><em>read Is Classified Object Action Of Result</em></code></a></li>
<li><a href="#get_callActionOfResult()"><code><em>call Action Of Result</em></code></a></li>
<li><a href="#get_readSelfActionOfResult()"><code><em>read Self Action Of Result</em></code></a></li>
<li><a href="#get_readVariableActionOfResult()"><code><em>read Variable Action Of Result</em></code></a></li>
<li><a href="#get_readLinkObjectEndQualifierActionOfResult()"><code><em>read Link Object End Qualifier Action Of Result</em></code></a></li>
<li><a href="#get_acceptEventActionOfResult()"><code><em>accept Event Action Of Result</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getOutputPin()"><code>UMLPackage.getOutputPin()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='actions.mdbasicactions'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_acceptCallActionOfReturnInformation()">get_acceptCallActionOfReturnInformation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>accept Call Action Of Return Information</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_acceptEventActionOfResult()">get_acceptEventActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>accept Event Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_actionOfOutput()">get_actionOfOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>action Of Output</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_callActionOfResult()">get_callActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>call Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_clauseOfBodyOutput()">get_clauseOfBodyOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>clause Of Body Output</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_clauseOfDecider()">get_clauseOfDecider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>clause Of Decider</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_clearStructuralFeatureActionOfResult()">get_clearStructuralFeatureActionOfResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>clear Structural Feature Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_conditionalNodeOfResult()">get_conditionalNodeOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>conditional Node Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_createLinkObjectActionOfResult()">get_createLinkObjectActionOfResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>create Link Object Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_createObjectActionOfResult()">get_createObjectActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>create Object Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_loopNodeOfBodyOutput()">get_loopNodeOfBodyOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>loop Node Of Body Output</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_loopNodeOfDecider()">get_loopNodeOfDecider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>loop Node Of Decider</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_loopNodeOfLoopVariable()">get_loopNodeOfLoopVariable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>loop Node Of Loop Variable</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_loopNodeOfResult()">get_loopNodeOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>loop Node Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_opaqueActionOfOutputValue()">get_opaqueActionOfOutputValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>opaque Action Of Output Value</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readExtentActionOfResult()">get_readExtentActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Extent Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readIsClassifiedObjectActionOfResult()">get_readIsClassifiedObjectActionOfResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Is Classified Object Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readLinkActionOfResult()">get_readLinkActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Link Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readLinkObjectEndActionOfResult()">get_readLinkObjectEndActionOfResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Link Object End Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readLinkObjectEndQualifierActionOfResult()">get_readLinkObjectEndQualifierActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Link Object End Qualifier Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readSelfActionOfResult()">get_readSelfActionOfResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Self Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readStructuralFeatureActionOfResult()">get_readStructuralFeatureActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Structural Feature Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readVariableActionOfResult()">get_readVariableActionOfResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Variable Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_reduceActionOfResult()">get_reduceActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reduce Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_structuredActivityNodeOfStructuredNodeOutput()">get_structuredActivityNodeOfStructuredNodeOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>structured Activity Node Of Structured Node Output</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_testIdentityActionOfResult()">get_testIdentityActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>test Identity Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_unmarshallActionOfResult()">get_unmarshallActionOfResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>unmarshall Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_valueSpecificationActionOfResult()">get_valueSpecificationActionOfResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>value Specification Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_writeStructuralFeatureActionOfResult()">get_writeStructuralFeatureActionOfResult</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>write Structural Feature Action Of Result</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_clauseOfBodyOutput()">has_clauseOfBodyOutput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_loopNodeOfBodyOutput()">has_loopNodeOfBodyOutput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_acceptCallActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction)">set_acceptCallActionOfReturnInformation</a><wbr/>(<a href="../mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_acceptCallActionOfReturnInformation()"><code><em>accept Call Action Of
 Return Information</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_acceptEventActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">set_acceptEventActionOfResult</a><wbr/>(<a href="../mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_acceptEventActionOfResult()"><code><em>accept Event Action Of Result</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_actionOfOutput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">set_actionOfOutput</a><wbr/>(<a href="Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_actionOfOutput()"><code><em>action Of Output</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_callActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction)">set_callActionOfResult</a><wbr/>(<a href="CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_callActionOfResult()"><code><em>call Action Of Result</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_clauseOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">set_clauseOfDecider</a><wbr/>(<a href="../../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_clauseOfDecider()"><code><em>clause Of Decider</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_clearStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction)">set_clearStructuralFeatureActionOfResult</a><wbr/>(<a href="../mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_clearStructuralFeatureActionOfResult()"><code><em>clear Structural
 Feature Action Of Result</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_conditionalNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode)">set_conditionalNodeOfResult</a><wbr/>(<a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_conditionalNodeOfResult()"><code><em>conditional Node Of Result</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_createLinkObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction)">set_createLinkObjectActionOfResult</a><wbr/>(<a href="../mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_createLinkObjectActionOfResult()"><code><em>create Link Object Action Of Result</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_createObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction)">set_createObjectActionOfResult</a><wbr/>(<a href="../mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_createObjectActionOfResult()"><code><em>create Object Action Of Result</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_loopNodeOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfDecider</a><wbr/>(<a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_loopNodeOfDecider()"><code><em>loop Node Of Decider</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_loopNodeOfLoopVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfLoopVariable</a><wbr/>(<a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_loopNodeOfLoopVariable()"><code><em>loop Node Of Loop Variable</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_loopNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfResult</a><wbr/>(<a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_loopNodeOfResult()"><code><em>loop Node Of Result</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_opaqueActionOfOutputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction)">set_opaqueActionOfOutputValue</a><wbr/>(<a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_opaqueActionOfOutputValue()"><code><em>opaque Action Of Output Value</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readExtentActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction)">set_readExtentActionOfResult</a><wbr/>(<a href="../mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_readExtentActionOfResult()"><code><em>read Extent Action Of Result</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readIsClassifiedObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction)">set_readIsClassifiedObjectActionOfResult</a><wbr/>(<a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readIsClassifiedObjectActionOfResult()"><code><em>read Is Classified
 Object Action Of Result</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readLinkActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction)">set_readLinkActionOfResult</a><wbr/>(<a href="../mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readLinkActionOfResult()"><code><em>read Link Action Of Result</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readLinkObjectEndActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction)">set_readLinkObjectEndActionOfResult</a><wbr/>(<a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readLinkObjectEndActionOfResult()"><code><em>read Link Object End Action
 Of Result</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readLinkObjectEndQualifierActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction)">set_readLinkObjectEndQualifierActionOfResult</a><wbr/>(<a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readLinkObjectEndQualifierActionOfResult()"><code><em>read Link Object
 End Qualifier Action Of Result</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readSelfActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction)">set_readSelfActionOfResult</a><wbr/>(<a href="../mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readSelfActionOfResult()"><code><em>read Self Action Of Result</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction)">set_readStructuralFeatureActionOfResult</a><wbr/>(<a href="../mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readStructuralFeatureActionOfResult()"><code><em>read Structural Feature
 Action Of Result</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readVariableActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction)">set_readVariableActionOfResult</a><wbr/>(<a href="../mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_readVariableActionOfResult()"><code><em>read Variable Action Of Result</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_reduceActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction)">set_reduceActionOfResult</a><wbr/>(<a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_reduceActionOfResult()"><code><em>reduce Action Of Result</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_structuredActivityNodeOfStructuredNodeOutput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">set_structuredActivityNodeOfStructuredNodeOutput</a><wbr/>(<a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_structuredActivityNodeOfStructuredNodeOutput()"><code><em>structured
 Activity Node Of Structured Node Output</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_testIdentityActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)">set_testIdentityActionOfResult</a><wbr/>(<a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_testIdentityActionOfResult()"><code><em>test Identity Action Of Result</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_unmarshallActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction)">set_unmarshallActionOfResult</a><wbr/>(<a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_unmarshallActionOfResult()"><code><em>unmarshall Action Of Result</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_valueSpecificationActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)">set_valueSpecificationActionOfResult</a><wbr/>(<a href="../mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_valueSpecificationActionOfResult()"><code><em>value Specification Action
 Of Result</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_writeStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction)">set_writeStructuralFeatureActionOfResult</a><wbr/>(<a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_writeStructuralFeatureActionOfResult()"><code><em>write Structural
 Feature Action Of Result</em></code></a>' container reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.ActivityNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.<a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></h3>
<code><a href="../../activities/mdfundamentalactivities/ActivityNode.html#get_activityNodeOfRedefinedNode()">get_activityNodeOfRedefinedNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getActivity()">getActivity</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getIncoming()">getIncoming</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getInGroup()">getInGroup</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getInInterruptibleRegion()">getInInterruptibleRegion</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getInPartition()">getInPartition</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getInStructuredNode()">getInStructuredNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getOutgoing()">getOutgoing</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#getRedefinedNode()">getRedefinedNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#has_activityNodeOfRedefinedNode()">has_activityNodeOfRedefinedNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasIncoming()">hasIncoming</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasInGroup()">hasInGroup</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasInInterruptibleRegion()">hasInInterruptibleRegion</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasInPartition()">hasInPartition</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasOutgoing()">hasOutgoing</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#hasRedefinedNode()">hasRedefinedNode</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#setActivity(com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities.Activity)">setActivity</a>, <a href="../../activities/mdfundamentalactivities/ActivityNode.html#setInStructuredNode(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">setInStructuredNode</a></code></div>
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
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></h3>
<code><a href="../../classes/mdkernel/MultiplicityElement.html#getLower()">getLower</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#getLowerValue()">getLowerValue</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#getUpper()">getUpper</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#getUpperValue()">getUpperValue</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#isOrdered()">isOrdered</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#isUnique()">isUnique</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#setLowerValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setLowerValue</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#setOrdered(boolean)">setOrdered</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#setUnique(boolean)">setUnique</a>, <a href="../../classes/mdkernel/MultiplicityElement.html#setUpperValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setUpperValue</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.<a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></h3>
<code><a href="../../activities/mdbasicactivities/ObjectNode.html#get_exceptionHandlerOfExceptionInput()">get_exceptionHandlerOfExceptionInput</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#getInState()">getInState</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#getOrdering()">getOrdering</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#getSelection()">getSelection</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#getUpperBound()">getUpperBound</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#has_exceptionHandlerOfExceptionInput()">has_exceptionHandlerOfExceptionInput</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#hasInState()">hasInState</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#isControlType()">isControlType</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#setControlType(boolean)">setControlType</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#setOrdering(com.nomagic.uml2.ext.magicdraw.activities.mdcompleteactivities.ObjectNodeOrderingKind)">setOrdering</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#setSelection(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">setSelection</a>, <a href="../../activities/mdbasicactivities/ObjectNode.html#setUpperBound(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setUpperBound</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Pin">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.<a href="Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></h3>
<code><a href="Pin.html#isControl()">isControl</a>, <a href="Pin.html#setControl(boolean)">setControl</a></code></div>
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
<section class="detail" id="get_clearStructuralFeatureActionOfResult()">
<h3>get_clearStructuralFeatureActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a></span> <span class="element-name">get_clearStructuralFeatureActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>clear Structural Feature Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdintermediateactions/ClearStructuralFeatureAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>clear Structural Feature Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>clear Structural Feature Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_clearStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction)"><code>set_clearStructuralFeatureActionOfResult(ClearStructuralFeatureAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__clearStructuralFeatureActionOfResult()"><code>UMLPackage.getOutputPin__clearStructuralFeatureActionOfResult()</code></a></li>
<li><a href="../mdintermediateactions/ClearStructuralFeatureAction.html#getResult()"><code>ClearStructuralFeatureAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_clearStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearStructuralFeatureAction)">
<h3>set_clearStructuralFeatureActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_clearStructuralFeatureActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/ClearStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearStructuralFeatureAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_clearStructuralFeatureActionOfResult()"><code><em>clear Structural
 Feature Action Of Result</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>clear Structural Feature Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_clearStructuralFeatureActionOfResult()"><code>get_clearStructuralFeatureActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_writeStructuralFeatureActionOfResult()">
<h3>get_writeStructuralFeatureActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></span> <span class="element-name">get_writeStructuralFeatureActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>write Structural Feature Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdintermediateactions/WriteStructuralFeatureAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>write Structural Feature Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>write Structural Feature Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_writeStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction)"><code>set_writeStructuralFeatureActionOfResult(WriteStructuralFeatureAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__writeStructuralFeatureActionOfResult()"><code>UMLPackage.getOutputPin__writeStructuralFeatureActionOfResult()</code></a></li>
<li><a href="../mdintermediateactions/WriteStructuralFeatureAction.html#getResult()"><code>WriteStructuralFeatureAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_writeStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction)">
<h3>set_writeStructuralFeatureActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_writeStructuralFeatureActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_writeStructuralFeatureActionOfResult()"><code><em>write Structural
 Feature Action Of Result</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>write Structural Feature Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_writeStructuralFeatureActionOfResult()"><code>get_writeStructuralFeatureActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_createLinkObjectActionOfResult()">
<h3>get_createLinkObjectActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a></span> <span class="element-name">get_createLinkObjectActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>create Link Object Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/CreateLinkObjectAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>create Link Object Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>create Link Object Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_createLinkObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction)"><code>set_createLinkObjectActionOfResult(CreateLinkObjectAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__createLinkObjectActionOfResult()"><code>UMLPackage.getOutputPin__createLinkObjectActionOfResult()</code></a></li>
<li><a href="../mdcompleteactions/CreateLinkObjectAction.html#getResult()"><code>CreateLinkObjectAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_createLinkObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.CreateLinkObjectAction)">
<h3>set_createLinkObjectActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_createLinkObjectActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/CreateLinkObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">CreateLinkObjectAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_createLinkObjectActionOfResult()"><code><em>create Link Object Action Of Result</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>create Link Object Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_createLinkObjectActionOfResult()"><code>get_createLinkObjectActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_acceptEventActionOfResult()">
<h3>get_acceptEventActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a></span> <span class="element-name">get_acceptEventActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>accept Event Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/AcceptEventAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>accept Event Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>accept Event Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_acceptEventActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)"><code>set_acceptEventActionOfResult(AcceptEventAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__acceptEventActionOfResult()"><code>UMLPackage.getOutputPin__acceptEventActionOfResult()</code></a></li>
<li><a href="../mdcompleteactions/AcceptEventAction.html#getResult()"><code>AcceptEventAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_acceptEventActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptEventAction)">
<h3>set_acceptEventActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_acceptEventActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/AcceptEventAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptEventAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_acceptEventActionOfResult()"><code><em>accept Event Action Of Result</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>accept Event Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_acceptEventActionOfResult()"><code>get_acceptEventActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readLinkObjectEndActionOfResult()">
<h3>get_readLinkObjectEndActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></span> <span class="element-name">get_readLinkObjectEndActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>read Link Object End Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReadLinkObjectEndAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Link Object End Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Link Object End Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readLinkObjectEndActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction)"><code>set_readLinkObjectEndActionOfResult(ReadLinkObjectEndAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__readLinkObjectEndActionOfResult()"><code>UMLPackage.getOutputPin__readLinkObjectEndActionOfResult()</code></a></li>
<li><a href="../mdcompleteactions/ReadLinkObjectEndAction.html#getResult()"><code>ReadLinkObjectEndAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readLinkObjectEndActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction)">
<h3>set_readLinkObjectEndActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readLinkObjectEndActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readLinkObjectEndActionOfResult()"><code><em>read Link Object End Action
 Of Result</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Link Object End Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_readLinkObjectEndActionOfResult()"><code>get_readLinkObjectEndActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readIsClassifiedObjectActionOfResult()">
<h3>get_readIsClassifiedObjectActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></span> <span class="element-name">get_readIsClassifiedObjectActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>read Is Classified Object Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Is Classified Object Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Is Classified Object Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readIsClassifiedObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction)"><code>set_readIsClassifiedObjectActionOfResult(ReadIsClassifiedObjectAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__readIsClassifiedObjectActionOfResult()"><code>UMLPackage.getOutputPin__readIsClassifiedObjectActionOfResult()</code></a></li>
<li><a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html#getResult()"><code>ReadIsClassifiedObjectAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readIsClassifiedObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction)">
<h3>set_readIsClassifiedObjectActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readIsClassifiedObjectActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readIsClassifiedObjectActionOfResult()"><code><em>read Is Classified
 Object Action Of Result</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Is Classified Object Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_readIsClassifiedObjectActionOfResult()"><code>get_readIsClassifiedObjectActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readExtentActionOfResult()">
<h3>get_readExtentActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a></span> <span class="element-name">get_readExtentActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>read Extent Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReadExtentAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Extent Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Extent Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readExtentActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction)"><code>set_readExtentActionOfResult(ReadExtentAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__readExtentActionOfResult()"><code>UMLPackage.getOutputPin__readExtentActionOfResult()</code></a></li>
<li><a href="../mdcompleteactions/ReadExtentAction.html#getResult()"><code>ReadExtentAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readExtentActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadExtentAction)">
<h3>set_readExtentActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readExtentActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReadExtentAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadExtentAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_readExtentActionOfResult()"><code><em>read Extent Action Of Result</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Extent Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_readExtentActionOfResult()"><code>get_readExtentActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readLinkObjectEndQualifierActionOfResult()">
<h3>get_readLinkObjectEndQualifierActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></span> <span class="element-name">get_readLinkObjectEndQualifierActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>read Link Object End Qualifier Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Link Object End Qualifier Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Link Object End Qualifier Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readLinkObjectEndQualifierActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction)"><code>set_readLinkObjectEndQualifierActionOfResult(ReadLinkObjectEndQualifierAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__readLinkObjectEndQualifierActionOfResult()"><code>UMLPackage.getOutputPin__readLinkObjectEndQualifierActionOfResult()</code></a></li>
<li><a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getResult()"><code>ReadLinkObjectEndQualifierAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readLinkObjectEndQualifierActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction)">
<h3>set_readLinkObjectEndQualifierActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readLinkObjectEndQualifierActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readLinkObjectEndQualifierActionOfResult()"><code><em>read Link Object
 End Qualifier Action Of Result</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Link Object End Qualifier Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_readLinkObjectEndQualifierActionOfResult()"><code>get_readLinkObjectEndQualifierActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_unmarshallActionOfResult()">
<h3>get_unmarshallActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></span> <span class="element-name">get_unmarshallActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>unmarshall Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/UnmarshallAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>unmarshall Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>unmarshall Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_unmarshallActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction)"><code>set_unmarshallActionOfResult(UnmarshallAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__unmarshallActionOfResult()"><code>UMLPackage.getOutputPin__unmarshallActionOfResult()</code></a></li>
<li><a href="../mdcompleteactions/UnmarshallAction.html#getResult()"><code>UnmarshallAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_unmarshallActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction)">
<h3>set_unmarshallActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_unmarshallActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_unmarshallActionOfResult()"><code><em>unmarshall Action Of Result</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>unmarshall Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_unmarshallActionOfResult()"><code>get_unmarshallActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_acceptCallActionOfReturnInformation()">
<h3>get_acceptCallActionOfReturnInformation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a></span> <span class="element-name">get_acceptCallActionOfReturnInformation</span>()</div>
<div class="block">Returns the value of the '<em><b>accept Call Action Of Return Information</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdcompleteactions/AcceptCallAction.html#getReturnInformation()"><code><em>Return Information</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>accept Call Action Of Return Information</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>accept Call Action Of Return Information</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_acceptCallActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction)"><code>set_acceptCallActionOfReturnInformation(AcceptCallAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__acceptCallActionOfReturnInformation()"><code>UMLPackage.getOutputPin__acceptCallActionOfReturnInformation()</code></a></li>
<li><a href="../mdcompleteactions/AcceptCallAction.html#getReturnInformation()"><code>AcceptCallAction.getReturnInformation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="returnInformation" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_acceptCallActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.AcceptCallAction)">
<h3>set_acceptCallActionOfReturnInformation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_acceptCallActionOfReturnInformation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/AcceptCallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">AcceptCallAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_acceptCallActionOfReturnInformation()"><code><em>accept Call Action Of
 Return Information</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>accept Call Action Of Return Information</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_acceptCallActionOfReturnInformation()"><code>get_acceptCallActionOfReturnInformation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_callActionOfResult()">
<h3>get_callActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a></span> <span class="element-name">get_callActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>call Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="CallAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>call Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>call Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_callActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction)"><code>set_callActionOfResult(CallAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__callActionOfResult()"><code>UMLPackage.getOutputPin__callActionOfResult()</code></a></li>
<li><a href="CallAction.html#getResult()"><code>CallAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_callActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallAction)">
<h3>set_callActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_callActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="CallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_callActionOfResult()"><code><em>call Action Of Result</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>call Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_callActionOfResult()"><code>get_callActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_reduceActionOfResult()">
<h3>get_reduceActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></span> <span class="element-name">get_reduceActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>reduce Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReduceAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reduce Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reduce Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_reduceActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction)"><code>set_reduceActionOfResult(ReduceAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__reduceActionOfResult()"><code>UMLPackage.getOutputPin__reduceActionOfResult()</code></a></li>
<li><a href="../mdcompleteactions/ReduceAction.html#getResult()"><code>ReduceAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_reduceActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction)">
<h3>set_reduceActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_reduceActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_reduceActionOfResult()"><code><em>reduce Action Of Result</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>reduce Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_reduceActionOfResult()"><code>get_reduceActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_clauseOfDecider()">
<h3>get_clauseOfDecider</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a></span> <span class="element-name">get_clauseOfDecider</span>()</div>
<div class="block">Returns the value of the '<em><b>clause Of Decider</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdstructuredactivities/Clause.html#getDecider()"><code><em>Decider</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>clause Of Decider</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>clause Of Decider</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_clauseOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)"><code>set_clauseOfDecider(Clause)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__clauseOfDecider()"><code>UMLPackage.getOutputPin__clauseOfDecider()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/Clause.html#getDecider()"><code>Clause.getDecider()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="decider" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_clauseOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.Clause)">
<h3>set_clauseOfDecider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_clauseOfDecider</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_clauseOfDecider()"><code><em>clause Of Decider</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>clause Of Decider</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_clauseOfDecider()"><code>get_clauseOfDecider()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_clauseOfBodyOutput()">
<h3>get_clauseOfBodyOutput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Clause</a>&gt;</span> <span class="element-name">get_clauseOfBodyOutput</span>()</div>
<div class="block">Returns the value of the '<em><b>clause Of Body Output</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdstructuredactivities/Clause.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>Clause</code></a>.
 It is bidirectional and its opposite is '<a href="../../activities/mdstructuredactivities/Clause.html#getBodyOutput()"><code><em>Body Output</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>clause Of Body Output</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>clause Of Body Output</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOutputPin__clauseOfBodyOutput()"><code>UMLPackage.getOutputPin__clauseOfBodyOutput()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/Clause.html#getBodyOutput()"><code>Clause.getBodyOutput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="bodyOutput" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_conditionalNodeOfResult()">
<h3>get_conditionalNodeOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a></span> <span class="element-name">get_conditionalNodeOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>conditional Node Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdstructuredactivities/ConditionalNode.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>conditional Node Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>conditional Node Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_conditionalNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode)"><code>set_conditionalNodeOfResult(ConditionalNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__conditionalNodeOfResult()"><code>UMLPackage.getOutputPin__conditionalNodeOfResult()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/ConditionalNode.html#getResult()"><code>ConditionalNode.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_conditionalNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.ConditionalNode)">
<h3>set_conditionalNodeOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_conditionalNodeOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdstructuredactivities/ConditionalNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">ConditionalNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_conditionalNodeOfResult()"><code><em>conditional Node Of Result</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>conditional Node Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_conditionalNodeOfResult()"><code>get_conditionalNodeOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_actionOfOutput()">
<h3>get_actionOfOutput</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></span> <span class="element-name">get_actionOfOutput</span>()</div>
<div class="block">Returns the value of the '<em><b>action Of Output</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Action.html#getOutput()"><code><em>Output</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>action Of Output</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>action Of Output</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_actionOfOutput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)"><code>set_actionOfOutput(Action)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__actionOfOutput()"><code>UMLPackage.getOutputPin__actionOfOutput()</code></a></li>
<li><a href="Action.html#getOutput()"><code>Action.getOutput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="output" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_actionOfOutput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">
<h3>set_actionOfOutput</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_actionOfOutput</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_actionOfOutput()"><code><em>action Of Output</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>action Of Output</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_actionOfOutput()"><code>get_actionOfOutput()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_testIdentityActionOfResult()">
<h3>get_testIdentityActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></span> <span class="element-name">get_testIdentityActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>test Identity Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/TestIdentityAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>test Identity Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>test Identity Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_testIdentityActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)"><code>set_testIdentityActionOfResult(TestIdentityAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__testIdentityActionOfResult()"><code>UMLPackage.getOutputPin__testIdentityActionOfResult()</code></a></li>
<li><a href="../mdintermediateactions/TestIdentityAction.html#getResult()"><code>TestIdentityAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_testIdentityActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)">
<h3>set_testIdentityActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_testIdentityActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_testIdentityActionOfResult()"><code><em>test Identity Action Of Result</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>test Identity Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_testIdentityActionOfResult()"><code>get_testIdentityActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readLinkActionOfResult()">
<h3>get_readLinkActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a></span> <span class="element-name">get_readLinkActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>read Link Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/ReadLinkAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Link Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Link Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readLinkActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction)"><code>set_readLinkActionOfResult(ReadLinkAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__readLinkActionOfResult()"><code>UMLPackage.getOutputPin__readLinkActionOfResult()</code></a></li>
<li><a href="../mdintermediateactions/ReadLinkAction.html#getResult()"><code>ReadLinkAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readLinkActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadLinkAction)">
<h3>set_readLinkActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readLinkActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/ReadLinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadLinkAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readLinkActionOfResult()"><code><em>read Link Action Of Result</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Link Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_readLinkActionOfResult()"><code>get_readLinkActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readSelfActionOfResult()">
<h3>get_readSelfActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a></span> <span class="element-name">get_readSelfActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>read Self Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/ReadSelfAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Self Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Self Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readSelfActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction)"><code>set_readSelfActionOfResult(ReadSelfAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__readSelfActionOfResult()"><code>UMLPackage.getOutputPin__readSelfActionOfResult()</code></a></li>
<li><a href="../mdintermediateactions/ReadSelfAction.html#getResult()"><code>ReadSelfAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readSelfActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadSelfAction)">
<h3>set_readSelfActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readSelfActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/ReadSelfAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadSelfAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readSelfActionOfResult()"><code><em>read Self Action Of Result</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Self Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_readSelfActionOfResult()"><code>get_readSelfActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_loopNodeOfResult()">
<h3>get_loopNodeOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">get_loopNodeOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>loop Node Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdstructuredactivities/LoopNode.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>loop Node Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>loop Node Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_loopNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)"><code>set_loopNodeOfResult(LoopNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__loopNodeOfResult()"><code>UMLPackage.getOutputPin__loopNodeOfResult()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/LoopNode.html#getResult()"><code>LoopNode.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_loopNodeOfResult(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">
<h3>set_loopNodeOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_loopNodeOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_loopNodeOfResult()"><code><em>loop Node Of Result</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>loop Node Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_loopNodeOfResult()"><code>get_loopNodeOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_valueSpecificationActionOfResult()">
<h3>get_valueSpecificationActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a></span> <span class="element-name">get_valueSpecificationActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>value Specification Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/ValueSpecificationAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>value Specification Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>value Specification Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_valueSpecificationActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)"><code>set_valueSpecificationActionOfResult(ValueSpecificationAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__valueSpecificationActionOfResult()"><code>UMLPackage.getOutputPin__valueSpecificationActionOfResult()</code></a></li>
<li><a href="../mdintermediateactions/ValueSpecificationAction.html#getResult()"><code>ValueSpecificationAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_valueSpecificationActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)">
<h3>set_valueSpecificationActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_valueSpecificationActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/ValueSpecificationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ValueSpecificationAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_valueSpecificationActionOfResult()"><code><em>value Specification Action
 Of Result</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>value Specification Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_valueSpecificationActionOfResult()"><code>get_valueSpecificationActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_loopNodeOfLoopVariable()">
<h3>get_loopNodeOfLoopVariable</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">get_loopNodeOfLoopVariable</span>()</div>
<div class="block">Returns the value of the '<em><b>loop Node Of Loop Variable</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdstructuredactivities/LoopNode.html#getLoopVariable()"><code><em>Loop Variable</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>loop Node Of Loop Variable</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>loop Node Of Loop Variable</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_loopNodeOfLoopVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)"><code>set_loopNodeOfLoopVariable(LoopNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__loopNodeOfLoopVariable()"><code>UMLPackage.getOutputPin__loopNodeOfLoopVariable()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/LoopNode.html#getLoopVariable()"><code>LoopNode.getLoopVariable()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="loopVariable" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_loopNodeOfLoopVariable(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">
<h3>set_loopNodeOfLoopVariable</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_loopNodeOfLoopVariable</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_loopNodeOfLoopVariable()"><code><em>loop Node Of Loop Variable</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>loop Node Of Loop Variable</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_loopNodeOfLoopVariable()"><code>get_loopNodeOfLoopVariable()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readVariableActionOfResult()">
<h3>get_readVariableActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a></span> <span class="element-name">get_readVariableActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>read Variable Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdstructuredactions/ReadVariableAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Variable Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Variable Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readVariableActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction)"><code>set_readVariableActionOfResult(ReadVariableAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__readVariableActionOfResult()"><code>UMLPackage.getOutputPin__readVariableActionOfResult()</code></a></li>
<li><a href="../mdstructuredactions/ReadVariableAction.html#getResult()"><code>ReadVariableAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readVariableActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.ReadVariableAction)">
<h3>set_readVariableActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readVariableActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdstructuredactions/ReadVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ReadVariableAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_readVariableActionOfResult()"><code><em>read Variable Action Of Result</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Variable Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_readVariableActionOfResult()"><code>get_readVariableActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_structuredActivityNodeOfStructuredNodeOutput()">
<h3>get_structuredActivityNodeOfStructuredNodeOutput</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></span> <span class="element-name">get_structuredActivityNodeOfStructuredNodeOutput</span>()</div>
<div class="block">Returns the value of the '<em><b>structured Activity Node Of Structured Node Output</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdstructuredactivities/StructuredActivityNode.html#getStructuredNodeOutput()"><code><em>Structured Node Output</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>structured Activity Node Of Structured Node Output</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>structured Activity Node Of Structured Node Output</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_structuredActivityNodeOfStructuredNodeOutput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)"><code>set_structuredActivityNodeOfStructuredNodeOutput(StructuredActivityNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__structuredActivityNodeOfStructuredNodeOutput()"><code>UMLPackage.getOutputPin__structuredActivityNodeOfStructuredNodeOutput()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html#getStructuredNodeOutput()"><code>StructuredActivityNode.getStructuredNodeOutput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="structuredNodeOutput" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_structuredActivityNodeOfStructuredNodeOutput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">
<h3>set_structuredActivityNodeOfStructuredNodeOutput</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_structuredActivityNodeOfStructuredNodeOutput</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_structuredActivityNodeOfStructuredNodeOutput()"><code><em>structured
 Activity Node Of Structured Node Output</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>structured Activity Node Of Structured Node Output</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_structuredActivityNodeOfStructuredNodeOutput()"><code>get_structuredActivityNodeOfStructuredNodeOutput()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_loopNodeOfBodyOutput()">
<h3>get_loopNodeOfBodyOutput</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a>&gt;</span> <span class="element-name">get_loopNodeOfBodyOutput</span>()</div>
<div class="block">Returns the value of the '<em><b>loop Node Of Body Output</b></em>' reference list.
 The list contents are of type <a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities"><code>LoopNode</code></a>.
 It is bidirectional and its opposite is '<a href="../../activities/mdstructuredactivities/LoopNode.html#getBodyOutput()"><code><em>Body Output</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>loop Node Of Body Output</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>loop Node Of Body Output</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getOutputPin__loopNodeOfBodyOutput()"><code>UMLPackage.getOutputPin__loopNodeOfBodyOutput()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/LoopNode.html#getBodyOutput()"><code>LoopNode.getBodyOutput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="bodyOutput" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_createObjectActionOfResult()">
<h3>get_createObjectActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a></span> <span class="element-name">get_createObjectActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>create Object Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/CreateObjectAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>create Object Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>create Object Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_createObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction)"><code>set_createObjectActionOfResult(CreateObjectAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__createObjectActionOfResult()"><code>UMLPackage.getOutputPin__createObjectActionOfResult()</code></a></li>
<li><a href="../mdintermediateactions/CreateObjectAction.html#getResult()"><code>CreateObjectAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_createObjectActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.CreateObjectAction)">
<h3>set_createObjectActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_createObjectActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/CreateObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">CreateObjectAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_createObjectActionOfResult()"><code><em>create Object Action Of Result</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>create Object Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_createObjectActionOfResult()"><code>get_createObjectActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readStructuralFeatureActionOfResult()">
<h3>get_readStructuralFeatureActionOfResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a></span> <span class="element-name">get_readStructuralFeatureActionOfResult</span>()</div>
<div class="block">Returns the value of the '<em><b>read Structural Feature Action Of Result</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdintermediateactions/ReadStructuralFeatureAction.html#getResult()"><code><em>Result</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Structural Feature Action Of Result</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Structural Feature Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction)"><code>set_readStructuralFeatureActionOfResult(ReadStructuralFeatureAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__readStructuralFeatureActionOfResult()"><code>UMLPackage.getOutputPin__readStructuralFeatureActionOfResult()</code></a></li>
<li><a href="../mdintermediateactions/ReadStructuralFeatureAction.html#getResult()"><code>ReadStructuralFeatureAction.getResult()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="result" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readStructuralFeatureActionOfResult(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ReadStructuralFeatureAction)">
<h3>set_readStructuralFeatureActionOfResult</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readStructuralFeatureActionOfResult</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/ReadStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ReadStructuralFeatureAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readStructuralFeatureActionOfResult()"><code><em>read Structural Feature
 Action Of Result</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Structural Feature Action Of Result</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_readStructuralFeatureActionOfResult()"><code>get_readStructuralFeatureActionOfResult()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_opaqueActionOfOutputValue()">
<h3>get_opaqueActionOfOutputValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></span> <span class="element-name">get_opaqueActionOfOutputValue</span>()</div>
<div class="block">Returns the value of the '<em><b>opaque Action Of Output Value</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="OpaqueAction.html#getOutputValue()"><code><em>Output Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>opaque Action Of Output Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>opaque Action Of Output Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_opaqueActionOfOutputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction)"><code>set_opaqueActionOfOutputValue(OpaqueAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__opaqueActionOfOutputValue()"><code>UMLPackage.getOutputPin__opaqueActionOfOutputValue()</code></a></li>
<li><a href="OpaqueAction.html#getOutputValue()"><code>OpaqueAction.getOutputValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="outputValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_opaqueActionOfOutputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction)">
<h3>set_opaqueActionOfOutputValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_opaqueActionOfOutputValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_opaqueActionOfOutputValue()"><code><em>opaque Action Of Output Value</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>opaque Action Of Output Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_opaqueActionOfOutputValue()"><code>get_opaqueActionOfOutputValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_loopNodeOfDecider()">
<h3>get_loopNodeOfDecider</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">get_loopNodeOfDecider</span>()</div>
<div class="block">Returns the value of the '<em><b>loop Node Of Decider</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../activities/mdstructuredactivities/LoopNode.html#getDecider()"><code><em>Decider</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>loop Node Of Decider</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>loop Node Of Decider</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_loopNodeOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)"><code>set_loopNodeOfDecider(LoopNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getOutputPin__loopNodeOfDecider()"><code>UMLPackage.getOutputPin__loopNodeOfDecider()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/LoopNode.html#getDecider()"><code>LoopNode.getDecider()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="decider" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_loopNodeOfDecider(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">
<h3>set_loopNodeOfDecider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_loopNodeOfDecider</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_loopNodeOfDecider()"><code><em>loop Node Of Decider</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>loop Node Of Decider</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_loopNodeOfDecider()"><code>get_loopNodeOfDecider()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_clauseOfBodyOutput()">
<h3>has_clauseOfBodyOutput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_clauseOfBodyOutput</span>()
                        throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_loopNodeOfBodyOutput()">
<h3>has_loopNodeOfBodyOutput</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_loopNodeOfBodyOutput</span>()
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
