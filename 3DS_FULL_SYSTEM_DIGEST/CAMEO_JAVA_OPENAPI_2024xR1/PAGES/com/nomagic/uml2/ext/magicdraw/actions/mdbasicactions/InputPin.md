# JAVA OPENAPI: InputPin (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html
- source_path: `com/nomagic/uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html`
- source_sha256: `caa82f59d728e4ff0e570aa6ab3d9401613e58a5301e1be7b8c13d8ff34eafbb`
- captured_utc: `2026-07-14T16:52:42.299281+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions](package-summary.html)

## Interface InputPin

All Superinterfaces:
`[ActivityNode](../../activities/mdfundamentalactivities/ActivityNode.html)`, `[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[MultiplicityElement](../../classes/mdkernel/MultiplicityElement.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[ObjectNode](../../activities/mdbasicactivities/ObjectNode.html)`, `[Pin](Pin.html)`, `[RedefinableElement](../../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TypedElement](../../classes/mdkernel/TypedElement.html)`

All Known Subinterfaces:
`[ActionInputPin](../mdstructuredactions/ActionInputPin.html)`, `[ValuePin](ValuePin.html)`

public interfaceInputPinextends [Pin](Pin.html)

begin-user-doc 
 A representation of the model object '***Input Pin***'.
 end-user-doc 
begin-model-doc 
 An InputPin is a Pin that holds input values to be consumed by an Action.
 end-model-doc 
The following features are supported:
 [`*structural Feature Action Of Object*`](#get_structuralFeatureActionOfObject())
[`*invocation Action Of Argument*`](#get_invocationActionOfArgument())
[`*loop Node Of Loop Variable Input*`](#get_loopNodeOfLoopVariableInput())
[`*reduce Action Of Collection*`](#get_reduceActionOfCollection())
[`*unmarshall Action Of Object*`](#get_unmarshallActionOfObject())
[`*opaque Action Of Input Value*`](#get_opaqueActionOfInputValue())
[`*qualifier Value Of Value*`](#get_qualifierValueOfValue())
[`*link End Data Of Value*`](#get_linkEndDataOfValue())
[`*link Action Of Input Value*`](#get_linkActionOfInputValue())
[`*read Link Object End Action Of Object*`](#get_readLinkObjectEndActionOfObject())
[`*write Structural Feature Action Of Value*`](#get_writeStructuralFeatureActionOfValue())
[`*link End Creation Data Of Insert At*`](#get_linkEndCreationDataOfInsertAt())
[`*test Identity Action Of First*`](#get_testIdentityActionOfFirst())
[`*test Identity Action Of Second*`](#get_testIdentityActionOfSecond())
[`*read Is Classified Object Action Of Object*`](#get_readIsClassifiedObjectActionOfObject())
[`*read Link Object End Qualifier Action Of Object*`](#get_readLinkObjectEndQualifierActionOfObject())
[`*reply Action Of Reply Value*`](#get_replyActionOfReplyValue())
[`*reply Action Of Return Information*`](#get_replyActionOfReturnInformation())
[`*send Signal Action Of Target*`](#get_sendSignalActionOfTarget())
[`*clear Association Action Of Object*`](#get_clearAssociationActionOfObject())
[`*call Operation Action Of Target*`](#get_callOperationActionOfTarget())
[`*send Object Action Of Target*`](#get_sendObjectActionOfTarget())
[`*send Object Action Of Request*`](#get_sendObjectActionOfRequest())
[`*add Structural Feature Value Action Of Insert At*`](#get_addStructuralFeatureValueActionOfInsertAt())
[`*action Of Input*`](#get_actionOfInput())
[`*remove Structural Feature Value Action Of Remove At*`](#get_removeStructuralFeatureValueActionOfRemoveAt())
[`*start Object Behavior Action Of Object*`](#get_startObjectBehaviorActionOfObject())
[`*remove Variable Value Action Of Remove At*`](#get_removeVariableValueActionOfRemoveAt())
[`*write Variable Action Of Value*`](#get_writeVariableActionOfValue())
[`*destroy Object Action Of Target*`](#get_destroyObjectActionOfTarget())
[`*reclassify Object Action Of Object*`](#get_reclassifyObjectActionOfObject())
[`*raise Exception Action Of Exception*`](#get_raiseExceptionActionOfException())
[`*link End Destruction Data Of Destroy At*`](#get_linkEndDestructionDataOfDestroyAt())
[`*add Variable Value Action Of Insert At*`](#get_addVariableValueActionOfInsertAt())
[`*start Classifier Behavior Action Of Object*`](#get_startClassifierBehaviorActionOfObject())
[`*structured Activity Node Of Structured Node Input*`](#get_structuredActivityNodeOfStructuredNodeInput())

See Also:
[`UMLPackage.getInputPin()`](../../metadata/UMLPackage.html#getInputPin())
Model:
annotation="MOF package='actions.mdbasicactions'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Action](Action.html)`
`[get_actionOfInput](#get_actionOfInput())()`
Returns the value of the '***action Of Input***' reference.
`[AddStructuralFeatureValueAction](../mdintermediateactions/AddStructuralFeatureValueAction.html)`
`[get_addStructuralFeatureValueActionOfInsertAt](#get_addStructuralFeatureValueActionOfInsertAt())()`
Returns the value of the '***add Structural Feature Value Action Of Insert At***' container reference.
`[AddVariableValueAction](../mdstructuredactions/AddVariableValueAction.html)`
`[get_addVariableValueActionOfInsertAt](#get_addVariableValueActionOfInsertAt())()`
Returns the value of the '***add Variable Value Action Of Insert At***' container reference.
`[CallOperationAction](CallOperationAction.html)`
`[get_callOperationActionOfTarget](#get_callOperationActionOfTarget())()`
Returns the value of the '***call Operation Action Of Target***' container reference.
`[ClearAssociationAction](../mdintermediateactions/ClearAssociationAction.html)`
`[get_clearAssociationActionOfObject](#get_clearAssociationActionOfObject())()`
Returns the value of the '***clear Association Action Of Object***' container reference.
`[DestroyObjectAction](../mdintermediateactions/DestroyObjectAction.html)`
`[get_destroyObjectActionOfTarget](#get_destroyObjectActionOfTarget())()`
Returns the value of the '***destroy Object Action Of Target***' container reference.
`[InvocationAction](InvocationAction.html)`
`[get_invocationActionOfArgument](#get_invocationActionOfArgument())()`
Returns the value of the '***invocation Action Of Argument***' container reference.
`[LinkAction](../mdintermediateactions/LinkAction.html)`
`[get_linkActionOfInputValue](#get_linkActionOfInputValue())()`
Returns the value of the '***link Action Of Input Value***' container reference.
`[LinkEndCreationData](../mdintermediateactions/LinkEndCreationData.html)`
`[get_linkEndCreationDataOfInsertAt](#get_linkEndCreationDataOfInsertAt())()`
Returns the value of the '***link End Creation Data Of Insert At***' reference.
`[LinkEndData](../mdintermediateactions/LinkEndData.html)`
`[get_linkEndDataOfValue](#get_linkEndDataOfValue())()`
Returns the value of the '***link End Data Of Value***' reference.
`[LinkEndDestructionData](../mdintermediateactions/LinkEndDestructionData.html)`
`[get_linkEndDestructionDataOfDestroyAt](#get_linkEndDestructionDataOfDestroyAt())()`
Returns the value of the '***link End Destruction Data Of Destroy At***' reference.
`[LoopNode](../../activities/mdstructuredactivities/LoopNode.html)`
`[get_loopNodeOfLoopVariableInput](#get_loopNodeOfLoopVariableInput())()`
Returns the value of the '***loop Node Of Loop Variable Input***' container reference.
`[OpaqueAction](OpaqueAction.html)`
`[get_opaqueActionOfInputValue](#get_opaqueActionOfInputValue())()`
Returns the value of the '***opaque Action Of Input Value***' container reference.
`[QualifierValue](../mdcompleteactions/QualifierValue.html)`
`[get_qualifierValueOfValue](#get_qualifierValueOfValue())()`
Returns the value of the '***qualifier Value Of Value***' reference.
`[RaiseExceptionAction](../mdstructuredactions/RaiseExceptionAction.html)`
`[get_raiseExceptionActionOfException](#get_raiseExceptionActionOfException())()`
Returns the value of the '***raise Exception Action Of Exception***' container reference.
`[ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html)`
`[get_readIsClassifiedObjectActionOfObject](#get_readIsClassifiedObjectActionOfObject())()`
Returns the value of the '***read Is Classified Object Action Of Object***' container reference.
`[ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html)`
`[get_readLinkObjectEndActionOfObject](#get_readLinkObjectEndActionOfObject())()`
Returns the value of the '***read Link Object End Action Of Object***' container reference.
`[ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html)`
`[get_readLinkObjectEndQualifierActionOfObject](#get_readLinkObjectEndQualifierActionOfObject())()`
Returns the value of the '***read Link Object End Qualifier Action Of Object***' container reference.
`[ReclassifyObjectAction](../mdcompleteactions/ReclassifyObjectAction.html)`
`[get_reclassifyObjectActionOfObject](#get_reclassifyObjectActionOfObject())()`
Returns the value of the '***reclassify Object Action Of Object***' container reference.
`[ReduceAction](../mdcompleteactions/ReduceAction.html)`
`[get_reduceActionOfCollection](#get_reduceActionOfCollection())()`
Returns the value of the '***reduce Action Of Collection***' container reference.
`[RemoveStructuralFeatureValueAction](../mdintermediateactions/RemoveStructuralFeatureValueAction.html)`
`[get_removeStructuralFeatureValueActionOfRemoveAt](#get_removeStructuralFeatureValueActionOfRemoveAt())()`
Returns the value of the '***remove Structural Feature Value Action Of Remove At***' container reference.
`[RemoveVariableValueAction](../mdstructuredactions/RemoveVariableValueAction.html)`
`[get_removeVariableValueActionOfRemoveAt](#get_removeVariableValueActionOfRemoveAt())()`
Returns the value of the '***remove Variable Value Action Of Remove At***' container reference.
`[ReplyAction](../mdcompleteactions/ReplyAction.html)`
`[get_replyActionOfReplyValue](#get_replyActionOfReplyValue())()`
Returns the value of the '***reply Action Of Reply Value***' container reference.
`[ReplyAction](../mdcompleteactions/ReplyAction.html)`
`[get_replyActionOfReturnInformation](#get_replyActionOfReturnInformation())()`
Returns the value of the '***reply Action Of Return Information***' container reference.
`[SendObjectAction](../mdintermediateactions/SendObjectAction.html)`
`[get_sendObjectActionOfRequest](#get_sendObjectActionOfRequest())()`
Returns the value of the '***send Object Action Of Request***' container reference.
`[SendObjectAction](../mdintermediateactions/SendObjectAction.html)`
`[get_sendObjectActionOfTarget](#get_sendObjectActionOfTarget())()`
Returns the value of the '***send Object Action Of Target***' container reference.
`[SendSignalAction](SendSignalAction.html)`
`[get_sendSignalActionOfTarget](#get_sendSignalActionOfTarget())()`
Returns the value of the '***send Signal Action Of Target***' container reference.
`[StartClassifierBehaviorAction](../mdcompleteactions/StartClassifierBehaviorAction.html)`
`[get_startClassifierBehaviorActionOfObject](#get_startClassifierBehaviorActionOfObject())()`
Returns the value of the '***start Classifier Behavior Action Of Object***' container reference.
`[StartObjectBehaviorAction](../mdcompleteactions/StartObjectBehaviorAction.html)`
`[get_startObjectBehaviorActionOfObject](#get_startObjectBehaviorActionOfObject())()`
Returns the value of the '***start Object Behavior Action Of Object***' container reference.
`[StructuralFeatureAction](../mdintermediateactions/StructuralFeatureAction.html)`
`[get_structuralFeatureActionOfObject](#get_structuralFeatureActionOfObject())()`
Returns the value of the '***structural Feature Action Of Object***' container reference.
`[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html)`
`[get_structuredActivityNodeOfStructuredNodeInput](#get_structuredActivityNodeOfStructuredNodeInput())()`
Returns the value of the '***structured Activity Node Of Structured Node Input***' container reference.
`[TestIdentityAction](../mdintermediateactions/TestIdentityAction.html)`
`[get_testIdentityActionOfFirst](#get_testIdentityActionOfFirst())()`
Returns the value of the '***test Identity Action Of First***' container reference.
`[TestIdentityAction](../mdintermediateactions/TestIdentityAction.html)`
`[get_testIdentityActionOfSecond](#get_testIdentityActionOfSecond())()`
Returns the value of the '***test Identity Action Of Second***' container reference.
`[UnmarshallAction](../mdcompleteactions/UnmarshallAction.html)`
`[get_unmarshallActionOfObject](#get_unmarshallActionOfObject())()`
Returns the value of the '***unmarshall Action Of Object***' container reference.
`[WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html)`
`[get_writeStructuralFeatureActionOfValue](#get_writeStructuralFeatureActionOfValue())()`
Returns the value of the '***write Structural Feature Action Of Value***' container reference.
`[WriteVariableAction](../mdstructuredactions/WriteVariableAction.html)`
`[get_writeVariableActionOfValue](#get_writeVariableActionOfValue())()`
Returns the value of the '***write Variable Action Of Value***' container reference.
`void`
`[set_actionOfInput](#set_actionOfInput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))([Action](Action.html) value)`
Sets the value of the '[`*action Of Input*`](#get_actionOfInput())' reference.
`void`
`[set_addStructuralFeatureValueActionOfInsertAt](#set_addStructuralFeatureValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction))([AddStructuralFeatureValueAction](../mdintermediateactions/AddStructuralFeatureValueAction.html) value)`
Sets the value of the '[`*add Structural
 Feature Value Action Of Insert At*`](#get_addStructuralFeatureValueActionOfInsertAt())' container reference.
`void`
`[set_addVariableValueActionOfInsertAt](#set_addVariableValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction))([AddVariableValueAction](../mdstructuredactions/AddVariableValueAction.html) value)`
Sets the value of the '[`*add Variable Value Action
 Of Insert At*`](#get_addVariableValueActionOfInsertAt())' container reference.
`void`
`[set_callOperationActionOfTarget](#set_callOperationActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction))([CallOperationAction](CallOperationAction.html) value)`
Sets the value of the
 '[`*call Operation Action Of Target*`](#get_callOperationActionOfTarget())' container
 reference.
`void`
`[set_clearAssociationActionOfObject](#set_clearAssociationActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction))([ClearAssociationAction](../mdintermediateactions/ClearAssociationAction.html) value)`
Sets the value of the
 '[`*clear Association Action Of Object*`](#get_clearAssociationActionOfObject())' container
 reference.
`void`
`[set_destroyObjectActionOfTarget](#set_destroyObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction))([DestroyObjectAction](../mdintermediateactions/DestroyObjectAction.html) value)`
Sets the value of the
 '[`*destroy Object Action Of Target*`](#get_destroyObjectActionOfTarget())' container
 reference.
`void`
`[set_invocationActionOfArgument](#set_invocationActionOfArgument(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction))([InvocationAction](InvocationAction.html) value)`
Sets the value of the
 '[`*invocation Action Of Argument*`](#get_invocationActionOfArgument())' container
 reference.
`void`
`[set_linkActionOfInputValue](#set_linkActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction))([LinkAction](../mdintermediateactions/LinkAction.html) value)`
Sets the value of the '[`*link Action Of Input Value*`](#get_linkActionOfInputValue())'
 container reference.
`void`
`[set_linkEndCreationDataOfInsertAt](#set_linkEndCreationDataOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData))([LinkEndCreationData](../mdintermediateactions/LinkEndCreationData.html) value)`
Sets the value of the
 '[`*link End Creation Data Of Insert At*`](#get_linkEndCreationDataOfInsertAt())' reference.
`void`
`[set_linkEndDataOfValue](#set_linkEndDataOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData))([LinkEndData](../mdintermediateactions/LinkEndData.html) value)`
Sets the value of the '[`*link End Data Of Value*`](#get_linkEndDataOfValue())' reference.
`void`
`[set_linkEndDestructionDataOfDestroyAt](#set_linkEndDestructionDataOfDestroyAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData))([LinkEndDestructionData](../mdintermediateactions/LinkEndDestructionData.html) value)`
Sets the value of the
 '[`*link End Destruction Data Of Destroy At*`](#get_linkEndDestructionDataOfDestroyAt())'
 reference.
`void`
`[set_loopNodeOfLoopVariableInput](#set_loopNodeOfLoopVariableInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))([LoopNode](../../activities/mdstructuredactivities/LoopNode.html) value)`
Sets the value of the
 '[`*loop Node Of Loop Variable Input*`](#get_loopNodeOfLoopVariableInput())' container
 reference.
`void`
`[set_opaqueActionOfInputValue](#set_opaqueActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction))([OpaqueAction](OpaqueAction.html) value)`
Sets the value of the '[`*opaque Action Of Input Value*`](#get_opaqueActionOfInputValue())'
 container reference.
`void`
`[set_qualifierValueOfValue](#set_qualifierValueOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue))([QualifierValue](../mdcompleteactions/QualifierValue.html) value)`
Sets the value of the '[`*qualifier Value Of Value*`](#get_qualifierValueOfValue())'
 reference.
`void`
`[set_raiseExceptionActionOfException](#set_raiseExceptionActionOfException(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction))([RaiseExceptionAction](../mdstructuredactions/RaiseExceptionAction.html) value)`
Sets the value of the
 '[`*raise Exception Action Of Exception*`](#get_raiseExceptionActionOfException())'
 container reference.
`void`
`[set_readIsClassifiedObjectActionOfObject](#set_readIsClassifiedObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction))([ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html) value)`
Sets the value of the '[`*read Is Classified
 Object Action Of Object*`](#get_readIsClassifiedObjectActionOfObject())' container reference.
`void`
`[set_readLinkObjectEndActionOfObject](#set_readLinkObjectEndActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction))([ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html) value)`
Sets the value of the '[`*read Link Object End Action
 Of Object*`](#get_readLinkObjectEndActionOfObject())' container reference.
`void`
`[set_readLinkObjectEndQualifierActionOfObject](#set_readLinkObjectEndQualifierActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction))([ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html) value)`
Sets the value of the '[`*read Link Object
 End Qualifier Action Of Object*`](#get_readLinkObjectEndQualifierActionOfObject())' container reference.
`void`
`[set_reclassifyObjectActionOfObject](#set_reclassifyObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction))([ReclassifyObjectAction](../mdcompleteactions/ReclassifyObjectAction.html) value)`
Sets the value of the
 '[`*reclassify Object Action Of Object*`](#get_reclassifyObjectActionOfObject())' container
 reference.
`void`
`[set_reduceActionOfCollection](#set_reduceActionOfCollection(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction))([ReduceAction](../mdcompleteactions/ReduceAction.html) value)`
Sets the value of the '[`*reduce Action Of Collection*`](#get_reduceActionOfCollection())'
 container reference.
`void`
`[set_removeStructuralFeatureValueActionOfRemoveAt](#set_removeStructuralFeatureValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction))([RemoveStructuralFeatureValueAction](../mdintermediateactions/RemoveStructuralFeatureValueAction.html) value)`
Sets the value of the '[`*remove
 Structural Feature Value Action Of Remove At*`](#get_removeStructuralFeatureValueActionOfRemoveAt())' container reference.
`void`
`[set_removeVariableValueActionOfRemoveAt](#set_removeVariableValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction))([RemoveVariableValueAction](../mdstructuredactions/RemoveVariableValueAction.html) value)`
Sets the value of the '[`*remove Variable Value
 Action Of Remove At*`](#get_removeVariableValueActionOfRemoveAt())' container reference.
`void`
`[set_replyActionOfReplyValue](#set_replyActionOfReplyValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction))([ReplyAction](../mdcompleteactions/ReplyAction.html) value)`
Sets the value of the '[`*reply Action Of Reply Value*`](#get_replyActionOfReplyValue())'
 container reference.
`void`
`[set_replyActionOfReturnInformation](#set_replyActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction))([ReplyAction](../mdcompleteactions/ReplyAction.html) value)`
Sets the value of the
 '[`*reply Action Of Return Information*`](#get_replyActionOfReturnInformation())' container
 reference.
`void`
`[set_sendObjectActionOfRequest](#set_sendObjectActionOfRequest(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction))([SendObjectAction](../mdintermediateactions/SendObjectAction.html) value)`
Sets the value of the
 '[`*send Object Action Of Request*`](#get_sendObjectActionOfRequest())' container reference.
`void`
`[set_sendObjectActionOfTarget](#set_sendObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction))([SendObjectAction](../mdintermediateactions/SendObjectAction.html) value)`
Sets the value of the '[`*send Object Action Of Target*`](#get_sendObjectActionOfTarget())'
 container reference.
`void`
`[set_sendSignalActionOfTarget](#set_sendSignalActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction))([SendSignalAction](SendSignalAction.html) value)`
Sets the value of the '[`*send Signal Action Of Target*`](#get_sendSignalActionOfTarget())'
 container reference.
`void`
`[set_startClassifierBehaviorActionOfObject](#set_startClassifierBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction))([StartClassifierBehaviorAction](../mdcompleteactions/StartClassifierBehaviorAction.html) value)`
Sets the value of the '[`*start Classifier
 Behavior Action Of Object*`](#get_startClassifierBehaviorActionOfObject())' container reference.
`void`
`[set_startObjectBehaviorActionOfObject](#set_startObjectBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction))([StartObjectBehaviorAction](../mdcompleteactions/StartObjectBehaviorAction.html) value)`
Sets the value of the '[`*start Object Behavior
 Action Of Object*`](#get_startObjectBehaviorActionOfObject())' container reference.
`void`
`[set_structuralFeatureActionOfObject](#set_structuralFeatureActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction))([StructuralFeatureAction](../mdintermediateactions/StructuralFeatureAction.html) value)`
Sets the value of the
 '[`*structural Feature Action Of Object*`](#get_structuralFeatureActionOfObject())'
 container reference.
`void`
`[set_structuredActivityNodeOfStructuredNodeInput](#set_structuredActivityNodeOfStructuredNodeInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))([StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html) value)`
Sets the value of the '[`*structured
 Activity Node Of Structured Node Input*`](#get_structuredActivityNodeOfStructuredNodeInput())' container reference.
`void`
`[set_testIdentityActionOfFirst](#set_testIdentityActionOfFirst(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction))([TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) value)`
Sets the value of the
 '[`*test Identity Action Of First*`](#get_testIdentityActionOfFirst())' container reference.
`void`
`[set_testIdentityActionOfSecond](#set_testIdentityActionOfSecond(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction))([TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) value)`
Sets the value of the
 '[`*test Identity Action Of Second*`](#get_testIdentityActionOfSecond())' container
 reference.
`void`
`[set_unmarshallActionOfObject](#set_unmarshallActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction))([UnmarshallAction](../mdcompleteactions/UnmarshallAction.html) value)`
Sets the value of the '[`*unmarshall Action Of Object*`](#get_unmarshallActionOfObject())'
 container reference.
`void`
`[set_writeStructuralFeatureActionOfValue](#set_writeStructuralFeatureActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction))([WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html) value)`
Sets the value of the '[`*write Structural Feature
 Action Of Value*`](#get_writeStructuralFeatureActionOfValue())' container reference.
`void`
`[set_writeVariableActionOfValue](#set_writeVariableActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction))([WriteVariableAction](../mdstructuredactions/WriteVariableAction.html) value)`
Sets the value of the
 '[`*write Variable Action Of Value*`](#get_writeVariableActionOfValue())' container
 reference.
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
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
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
get_structuralFeatureActionOfObject
@CheckForNull[StructuralFeatureAction](../mdintermediateactions/StructuralFeatureAction.html) get_structuralFeatureActionOfObject()
Returns the value of the '***structural Feature Action Of Object***' container reference.
 It is bidirectional and its opposite is '[`*Object*`](../mdintermediateactions/StructuralFeatureAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*structural Feature Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*structural Feature Action Of Object*' container reference.
See Also:
[`set_structuralFeatureActionOfObject(StructuralFeatureAction)`](#set_structuralFeatureActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction))
[`UMLPackage.getInputPin__structuralFeatureActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__structuralFeatureActionOfObject())
[`StructuralFeatureAction.getObject()`](../mdintermediateactions/StructuralFeatureAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_structuralFeatureActionOfObject
void set_structuralFeatureActionOfObject(@CheckForNull
 [StructuralFeatureAction](../mdintermediateactions/StructuralFeatureAction.html) value)
Sets the value of the
 '[`*structural Feature Action Of Object*`](#get_structuralFeatureActionOfObject())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*structural Feature Action Of Object*' container reference.
See Also:
[`get_structuralFeatureActionOfObject()`](#get_structuralFeatureActionOfObject())
Generated:
get_writeStructuralFeatureActionOfValue
@CheckForNull[WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html) get_writeStructuralFeatureActionOfValue()
Returns the value of the '***write Structural Feature Action Of Value***' container reference.
 It is bidirectional and its opposite is
 '[`*Value*`](../mdintermediateactions/WriteStructuralFeatureAction.html#getValue())'.
 begin-user-doc 
If the meaning of the '*write Structural Feature Action Of Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*write Structural Feature Action Of Value*' container reference.
See Also:
[`set_writeStructuralFeatureActionOfValue(WriteStructuralFeatureAction)`](#set_writeStructuralFeatureActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction))
[`UMLPackage.getInputPin__writeStructuralFeatureActionOfValue()`](../../metadata/UMLPackage.html#getInputPin__writeStructuralFeatureActionOfValue())
[`WriteStructuralFeatureAction.getValue()`](../mdintermediateactions/WriteStructuralFeatureAction.html#getValue())
Model:
opposite="value" transient="false" ordered="false"
Generated:
set_writeStructuralFeatureActionOfValue
void set_writeStructuralFeatureActionOfValue(@CheckForNull
 [WriteStructuralFeatureAction](../mdintermediateactions/WriteStructuralFeatureAction.html) value)
Sets the value of the '[`*write Structural Feature
 Action Of Value*`](#get_writeStructuralFeatureActionOfValue())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*write Structural Feature Action Of Value*' container reference.
See Also:
[`get_writeStructuralFeatureActionOfValue()`](#get_writeStructuralFeatureActionOfValue())
Generated:
get_readLinkObjectEndActionOfObject
@CheckForNull[ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html) get_readLinkObjectEndActionOfObject()
Returns the value of the '***read Link Object End Action Of Object***' container reference.
 It is bidirectional and its opposite is '[`*Object*`](../mdcompleteactions/ReadLinkObjectEndAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*read Link Object End Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Link Object End Action Of Object*' container reference.
See Also:
[`set_readLinkObjectEndActionOfObject(ReadLinkObjectEndAction)`](#set_readLinkObjectEndActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction))
[`UMLPackage.getInputPin__readLinkObjectEndActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__readLinkObjectEndActionOfObject())
[`ReadLinkObjectEndAction.getObject()`](../mdcompleteactions/ReadLinkObjectEndAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_readLinkObjectEndActionOfObject
void set_readLinkObjectEndActionOfObject(@CheckForNull
 [ReadLinkObjectEndAction](../mdcompleteactions/ReadLinkObjectEndAction.html) value)
Sets the value of the '[`*read Link Object End Action
 Of Object*`](#get_readLinkObjectEndActionOfObject())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Link Object End Action Of Object*' container reference.
See Also:
[`get_readLinkObjectEndActionOfObject()`](#get_readLinkObjectEndActionOfObject())
Generated:
get_qualifierValueOfValue
@CheckForNull[QualifierValue](../mdcompleteactions/QualifierValue.html) get_qualifierValueOfValue()
Returns the value of the '***qualifier Value Of Value***' reference.
 It is bidirectional and its opposite is '[`*Value*`](../mdcompleteactions/QualifierValue.html#getValue())'.
 begin-user-doc 
If the meaning of the '*qualifier Value Of Value*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*qualifier Value Of Value*' reference.
See Also:
[`set_qualifierValueOfValue(QualifierValue)`](#set_qualifierValueOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue))
[`UMLPackage.getInputPin__qualifierValueOfValue()`](../../metadata/UMLPackage.html#getInputPin__qualifierValueOfValue())
[`QualifierValue.getValue()`](../mdcompleteactions/QualifierValue.html#getValue())
Model:
opposite="value" ordered="false"
Generated:
set_qualifierValueOfValue
void set_qualifierValueOfValue(@CheckForNull
 [QualifierValue](../mdcompleteactions/QualifierValue.html) value)
Sets the value of the '[`*qualifier Value Of Value*`](#get_qualifierValueOfValue())'
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*qualifier Value Of Value*' reference.
See Also:
[`get_qualifierValueOfValue()`](#get_qualifierValueOfValue())
Generated:
get_linkEndDataOfValue
@CheckForNull[LinkEndData](../mdintermediateactions/LinkEndData.html) get_linkEndDataOfValue()
Returns the value of the '***link End Data Of Value***' reference.
 It is bidirectional and its opposite is '[`*Value*`](../mdintermediateactions/LinkEndData.html#getValue())'.
 begin-user-doc 
If the meaning of the '*link End Data Of Value*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*link End Data Of Value*' reference.
See Also:
[`set_linkEndDataOfValue(LinkEndData)`](#set_linkEndDataOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData))
[`UMLPackage.getInputPin__linkEndDataOfValue()`](../../metadata/UMLPackage.html#getInputPin__linkEndDataOfValue())
[`LinkEndData.getValue()`](../mdintermediateactions/LinkEndData.html#getValue())
Model:
opposite="value" ordered="false"
Generated:
set_linkEndDataOfValue
void set_linkEndDataOfValue(@CheckForNull
 [LinkEndData](../mdintermediateactions/LinkEndData.html) value)
Sets the value of the '[`*link End Data Of Value*`](#get_linkEndDataOfValue())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*link End Data Of Value*' reference.
See Also:
[`get_linkEndDataOfValue()`](#get_linkEndDataOfValue())
Generated:
get_linkActionOfInputValue
@CheckForNull[LinkAction](../mdintermediateactions/LinkAction.html) get_linkActionOfInputValue()
Returns the value of the '***link Action Of Input Value***' container reference.
 It is bidirectional and its opposite is '[`*Input Value*`](../mdintermediateactions/LinkAction.html#getInputValue())'.
 begin-user-doc 
If the meaning of the '*link Action Of Input Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*link Action Of Input Value*' container reference.
See Also:
[`set_linkActionOfInputValue(LinkAction)`](#set_linkActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction))
[`UMLPackage.getInputPin__linkActionOfInputValue()`](../../metadata/UMLPackage.html#getInputPin__linkActionOfInputValue())
[`LinkAction.getInputValue()`](../mdintermediateactions/LinkAction.html#getInputValue())
Model:
opposite="inputValue" transient="false" ordered="false"
Generated:
set_linkActionOfInputValue
void set_linkActionOfInputValue(@CheckForNull
 [LinkAction](../mdintermediateactions/LinkAction.html) value)
Sets the value of the '[`*link Action Of Input Value*`](#get_linkActionOfInputValue())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*link Action Of Input Value*' container reference.
See Also:
[`get_linkActionOfInputValue()`](#get_linkActionOfInputValue())
Generated:
get_readIsClassifiedObjectActionOfObject
@CheckForNull[ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html) get_readIsClassifiedObjectActionOfObject()
Returns the value of the '***read Is Classified Object Action Of Object***' container reference.
 It is bidirectional and its opposite is '[`*Object*`](../mdcompleteactions/ReadIsClassifiedObjectAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*read Is Classified Object Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Is Classified Object Action Of Object*' container reference.
See Also:
[`set_readIsClassifiedObjectActionOfObject(ReadIsClassifiedObjectAction)`](#set_readIsClassifiedObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction))
[`UMLPackage.getInputPin__readIsClassifiedObjectActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__readIsClassifiedObjectActionOfObject())
[`ReadIsClassifiedObjectAction.getObject()`](../mdcompleteactions/ReadIsClassifiedObjectAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_readIsClassifiedObjectActionOfObject
void set_readIsClassifiedObjectActionOfObject(@CheckForNull
 [ReadIsClassifiedObjectAction](../mdcompleteactions/ReadIsClassifiedObjectAction.html) value)
Sets the value of the '[`*read Is Classified
 Object Action Of Object*`](#get_readIsClassifiedObjectActionOfObject())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Is Classified Object Action Of Object*' container reference.
See Also:
[`get_readIsClassifiedObjectActionOfObject()`](#get_readIsClassifiedObjectActionOfObject())
Generated:
get_readLinkObjectEndQualifierActionOfObject
@CheckForNull[ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html) get_readLinkObjectEndQualifierActionOfObject()
Returns the value of the '***read Link Object End Qualifier Action Of Object***' container reference.
 It is bidirectional and its opposite is
 '[`*Object*`](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*read Link Object End Qualifier Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*read Link Object End Qualifier Action Of Object*' container reference.
See Also:
[`set_readLinkObjectEndQualifierActionOfObject(ReadLinkObjectEndQualifierAction)`](#set_readLinkObjectEndQualifierActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction))
[`UMLPackage.getInputPin__readLinkObjectEndQualifierActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__readLinkObjectEndQualifierActionOfObject())
[`ReadLinkObjectEndQualifierAction.getObject()`](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_readLinkObjectEndQualifierActionOfObject
void set_readLinkObjectEndQualifierActionOfObject(@CheckForNull
 [ReadLinkObjectEndQualifierAction](../mdcompleteactions/ReadLinkObjectEndQualifierAction.html) value)
Sets the value of the '[`*read Link Object
 End Qualifier Action Of Object*`](#get_readLinkObjectEndQualifierActionOfObject())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*read Link Object End Qualifier Action Of Object*' container reference.
See Also:
[`get_readLinkObjectEndQualifierActionOfObject()`](#get_readLinkObjectEndQualifierActionOfObject())
Generated:
get_reclassifyObjectActionOfObject
@CheckForNull[ReclassifyObjectAction](../mdcompleteactions/ReclassifyObjectAction.html) get_reclassifyObjectActionOfObject()
Returns the value of the '***reclassify Object Action Of Object***' container reference.
 It is bidirectional and its opposite is '[`*Object*`](../mdcompleteactions/ReclassifyObjectAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*reclassify Object Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reclassify Object Action Of Object*' container reference.
See Also:
[`set_reclassifyObjectActionOfObject(ReclassifyObjectAction)`](#set_reclassifyObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction))
[`UMLPackage.getInputPin__reclassifyObjectActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__reclassifyObjectActionOfObject())
[`ReclassifyObjectAction.getObject()`](../mdcompleteactions/ReclassifyObjectAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_reclassifyObjectActionOfObject
void set_reclassifyObjectActionOfObject(@CheckForNull
 [ReclassifyObjectAction](../mdcompleteactions/ReclassifyObjectAction.html) value)
Sets the value of the
 '[`*reclassify Object Action Of Object*`](#get_reclassifyObjectActionOfObject())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*reclassify Object Action Of Object*' container reference.
See Also:
[`get_reclassifyObjectActionOfObject()`](#get_reclassifyObjectActionOfObject())
Generated:
get_unmarshallActionOfObject
@CheckForNull[UnmarshallAction](../mdcompleteactions/UnmarshallAction.html) get_unmarshallActionOfObject()
Returns the value of the '***unmarshall Action Of Object***' container reference.
 It is bidirectional and its opposite is '[`*Object*`](../mdcompleteactions/UnmarshallAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*unmarshall Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*unmarshall Action Of Object*' container reference.
See Also:
[`set_unmarshallActionOfObject(UnmarshallAction)`](#set_unmarshallActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction))
[`UMLPackage.getInputPin__unmarshallActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__unmarshallActionOfObject())
[`UnmarshallAction.getObject()`](../mdcompleteactions/UnmarshallAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_unmarshallActionOfObject
void set_unmarshallActionOfObject(@CheckForNull
 [UnmarshallAction](../mdcompleteactions/UnmarshallAction.html) value)
Sets the value of the '[`*unmarshall Action Of Object*`](#get_unmarshallActionOfObject())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*unmarshall Action Of Object*' container reference.
See Also:
[`get_unmarshallActionOfObject()`](#get_unmarshallActionOfObject())
Generated:
get_startClassifierBehaviorActionOfObject
@CheckForNull[StartClassifierBehaviorAction](../mdcompleteactions/StartClassifierBehaviorAction.html) get_startClassifierBehaviorActionOfObject()
Returns the value of the '***start Classifier Behavior Action Of Object***' container reference.
 It is bidirectional and its opposite is
 '[`*Object*`](../mdcompleteactions/StartClassifierBehaviorAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*start Classifier Behavior Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*start Classifier Behavior Action Of Object*' container reference.
See Also:
[`set_startClassifierBehaviorActionOfObject(StartClassifierBehaviorAction)`](#set_startClassifierBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction))
[`UMLPackage.getInputPin__startClassifierBehaviorActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__startClassifierBehaviorActionOfObject())
[`StartClassifierBehaviorAction.getObject()`](../mdcompleteactions/StartClassifierBehaviorAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_startClassifierBehaviorActionOfObject
void set_startClassifierBehaviorActionOfObject(@CheckForNull
 [StartClassifierBehaviorAction](../mdcompleteactions/StartClassifierBehaviorAction.html) value)
Sets the value of the '[`*start Classifier
 Behavior Action Of Object*`](#get_startClassifierBehaviorActionOfObject())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*start Classifier Behavior Action Of Object*' container reference.
See Also:
[`get_startClassifierBehaviorActionOfObject()`](#get_startClassifierBehaviorActionOfObject())
Generated:
get_invocationActionOfArgument
@CheckForNull[InvocationAction](InvocationAction.html) get_invocationActionOfArgument()
Returns the value of the '***invocation Action Of Argument***' container reference.
 It is bidirectional and its opposite is '[`*Argument*`](InvocationAction.html#getArgument())'.
 begin-user-doc 
If the meaning of the '*invocation Action Of Argument*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*invocation Action Of Argument*' container reference.
See Also:
[`set_invocationActionOfArgument(InvocationAction)`](#set_invocationActionOfArgument(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction))
[`UMLPackage.getInputPin__invocationActionOfArgument()`](../../metadata/UMLPackage.html#getInputPin__invocationActionOfArgument())
[`InvocationAction.getArgument()`](InvocationAction.html#getArgument())
Model:
opposite="argument" transient="false" ordered="false"
Generated:
set_invocationActionOfArgument
void set_invocationActionOfArgument(@CheckForNull
 [InvocationAction](InvocationAction.html) value)
Sets the value of the
 '[`*invocation Action Of Argument*`](#get_invocationActionOfArgument())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*invocation Action Of Argument*' container reference.
See Also:
[`get_invocationActionOfArgument()`](#get_invocationActionOfArgument())
Generated:
get_startObjectBehaviorActionOfObject
@CheckForNull[StartObjectBehaviorAction](../mdcompleteactions/StartObjectBehaviorAction.html) get_startObjectBehaviorActionOfObject()
Returns the value of the '***start Object Behavior Action Of Object***' container reference.
 It is bidirectional and its opposite is '[`*Object*`](../mdcompleteactions/StartObjectBehaviorAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*start Object Behavior Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*start Object Behavior Action Of Object*' container reference.
See Also:
[`set_startObjectBehaviorActionOfObject(StartObjectBehaviorAction)`](#set_startObjectBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction))
[`UMLPackage.getInputPin__startObjectBehaviorActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__startObjectBehaviorActionOfObject())
[`StartObjectBehaviorAction.getObject()`](../mdcompleteactions/StartObjectBehaviorAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_startObjectBehaviorActionOfObject
void set_startObjectBehaviorActionOfObject(@CheckForNull
 [StartObjectBehaviorAction](../mdcompleteactions/StartObjectBehaviorAction.html) value)
Sets the value of the '[`*start Object Behavior
 Action Of Object*`](#get_startObjectBehaviorActionOfObject())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*start Object Behavior Action Of Object*' container reference.
See Also:
[`get_startObjectBehaviorActionOfObject()`](#get_startObjectBehaviorActionOfObject())
Generated:
get_reduceActionOfCollection
@CheckForNull[ReduceAction](../mdcompleteactions/ReduceAction.html) get_reduceActionOfCollection()
Returns the value of the '***reduce Action Of Collection***' container reference.
 It is bidirectional and its opposite is '[`*Collection*`](../mdcompleteactions/ReduceAction.html#getCollection())'.
 begin-user-doc 
If the meaning of the '*reduce Action Of Collection*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reduce Action Of Collection*' container reference.
See Also:
[`set_reduceActionOfCollection(ReduceAction)`](#set_reduceActionOfCollection(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction))
[`UMLPackage.getInputPin__reduceActionOfCollection()`](../../metadata/UMLPackage.html#getInputPin__reduceActionOfCollection())
[`ReduceAction.getCollection()`](../mdcompleteactions/ReduceAction.html#getCollection())
Model:
opposite="collection" transient="false" ordered="false"
Generated:
set_reduceActionOfCollection
void set_reduceActionOfCollection(@CheckForNull
 [ReduceAction](../mdcompleteactions/ReduceAction.html) value)
Sets the value of the '[`*reduce Action Of Collection*`](#get_reduceActionOfCollection())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*reduce Action Of Collection*' container reference.
See Also:
[`get_reduceActionOfCollection()`](#get_reduceActionOfCollection())
Generated:
get_replyActionOfReturnInformation
@CheckForNull[ReplyAction](../mdcompleteactions/ReplyAction.html) get_replyActionOfReturnInformation()
Returns the value of the '***reply Action Of Return Information***' container reference.
 It is bidirectional and its opposite is
 '[`*Return Information*`](../mdcompleteactions/ReplyAction.html#getReturnInformation())'.
 begin-user-doc 
If the meaning of the '*reply Action Of Return Information*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reply Action Of Return Information*' container reference.
See Also:
[`set_replyActionOfReturnInformation(ReplyAction)`](#set_replyActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction))
[`UMLPackage.getInputPin__replyActionOfReturnInformation()`](../../metadata/UMLPackage.html#getInputPin__replyActionOfReturnInformation())
[`ReplyAction.getReturnInformation()`](../mdcompleteactions/ReplyAction.html#getReturnInformation())
Model:
opposite="returnInformation" transient="false" ordered="false"
Generated:
set_replyActionOfReturnInformation
void set_replyActionOfReturnInformation(@CheckForNull
 [ReplyAction](../mdcompleteactions/ReplyAction.html) value)
Sets the value of the
 '[`*reply Action Of Return Information*`](#get_replyActionOfReturnInformation())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*reply Action Of Return Information*' container reference.
See Also:
[`get_replyActionOfReturnInformation()`](#get_replyActionOfReturnInformation())
Generated:
get_replyActionOfReplyValue
@CheckForNull[ReplyAction](../mdcompleteactions/ReplyAction.html) get_replyActionOfReplyValue()
Returns the value of the '***reply Action Of Reply Value***' container reference.
 It is bidirectional and its opposite is '[`*Reply Value*`](../mdcompleteactions/ReplyAction.html#getReplyValue())'.
 begin-user-doc 
If the meaning of the '*reply Action Of Reply Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*reply Action Of Reply Value*' container reference.
See Also:
[`set_replyActionOfReplyValue(ReplyAction)`](#set_replyActionOfReplyValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction))
[`UMLPackage.getInputPin__replyActionOfReplyValue()`](../../metadata/UMLPackage.html#getInputPin__replyActionOfReplyValue())
[`ReplyAction.getReplyValue()`](../mdcompleteactions/ReplyAction.html#getReplyValue())
Model:
opposite="replyValue" transient="false" ordered="false"
Generated:
set_replyActionOfReplyValue
void set_replyActionOfReplyValue(@CheckForNull
 [ReplyAction](../mdcompleteactions/ReplyAction.html) value)
Sets the value of the '[`*reply Action Of Reply Value*`](#get_replyActionOfReplyValue())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*reply Action Of Reply Value*' container reference.
See Also:
[`get_replyActionOfReplyValue()`](#get_replyActionOfReplyValue())
Generated:
get_linkEndCreationDataOfInsertAt
@CheckForNull[LinkEndCreationData](../mdintermediateactions/LinkEndCreationData.html) get_linkEndCreationDataOfInsertAt()
Returns the value of the '***link End Creation Data Of Insert At***' reference.
 It is bidirectional and its opposite is '[`*Insert At*`](../mdintermediateactions/LinkEndCreationData.html#getInsertAt())'.
 begin-user-doc 
If the meaning of the '*link End Creation Data Of Insert At*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*link End Creation Data Of Insert At*' reference.
See Also:
[`set_linkEndCreationDataOfInsertAt(LinkEndCreationData)`](#set_linkEndCreationDataOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData))
[`UMLPackage.getInputPin__linkEndCreationDataOfInsertAt()`](../../metadata/UMLPackage.html#getInputPin__linkEndCreationDataOfInsertAt())
[`LinkEndCreationData.getInsertAt()`](../mdintermediateactions/LinkEndCreationData.html#getInsertAt())
Model:
opposite="insertAt" ordered="false"
Generated:
set_linkEndCreationDataOfInsertAt
void set_linkEndCreationDataOfInsertAt(@CheckForNull
 [LinkEndCreationData](../mdintermediateactions/LinkEndCreationData.html) value)
Sets the value of the
 '[`*link End Creation Data Of Insert At*`](#get_linkEndCreationDataOfInsertAt())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*link End Creation Data Of Insert At*' reference.
See Also:
[`get_linkEndCreationDataOfInsertAt()`](#get_linkEndCreationDataOfInsertAt())
Generated:
get_testIdentityActionOfFirst
@CheckForNull[TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) get_testIdentityActionOfFirst()
Returns the value of the '***test Identity Action Of First***' container reference.
 It is bidirectional and its opposite is '[`*First*`](../mdintermediateactions/TestIdentityAction.html#getFirst())'.
 begin-user-doc 
If the meaning of the '*test Identity Action Of First*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*test Identity Action Of First*' container reference.
See Also:
[`set_testIdentityActionOfFirst(TestIdentityAction)`](#set_testIdentityActionOfFirst(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction))
[`UMLPackage.getInputPin__testIdentityActionOfFirst()`](../../metadata/UMLPackage.html#getInputPin__testIdentityActionOfFirst())
[`TestIdentityAction.getFirst()`](../mdintermediateactions/TestIdentityAction.html#getFirst())
Model:
opposite="first" transient="false" ordered="false"
Generated:
set_testIdentityActionOfFirst
void set_testIdentityActionOfFirst(@CheckForNull
 [TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) value)
Sets the value of the
 '[`*test Identity Action Of First*`](#get_testIdentityActionOfFirst())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*test Identity Action Of First*' container reference.
See Also:
[`get_testIdentityActionOfFirst()`](#get_testIdentityActionOfFirst())
Generated:
get_testIdentityActionOfSecond
@CheckForNull[TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) get_testIdentityActionOfSecond()
Returns the value of the '***test Identity Action Of Second***' container reference.
 It is bidirectional and its opposite is '[`*Second*`](../mdintermediateactions/TestIdentityAction.html#getSecond())'.
 begin-user-doc 
If the meaning of the '*test Identity Action Of Second*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*test Identity Action Of Second*' container reference.
See Also:
[`set_testIdentityActionOfSecond(TestIdentityAction)`](#set_testIdentityActionOfSecond(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction))
[`UMLPackage.getInputPin__testIdentityActionOfSecond()`](../../metadata/UMLPackage.html#getInputPin__testIdentityActionOfSecond())
[`TestIdentityAction.getSecond()`](../mdintermediateactions/TestIdentityAction.html#getSecond())
Model:
opposite="second" transient="false" ordered="false"
Generated:
set_testIdentityActionOfSecond
void set_testIdentityActionOfSecond(@CheckForNull
 [TestIdentityAction](../mdintermediateactions/TestIdentityAction.html) value)
Sets the value of the
 '[`*test Identity Action Of Second*`](#get_testIdentityActionOfSecond())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*test Identity Action Of Second*' container reference.
See Also:
[`get_testIdentityActionOfSecond()`](#get_testIdentityActionOfSecond())
Generated:
get_opaqueActionOfInputValue
@CheckForNull[OpaqueAction](OpaqueAction.html) get_opaqueActionOfInputValue()
Returns the value of the '***opaque Action Of Input Value***' container reference.
 It is bidirectional and its opposite is '[`*Input Value*`](OpaqueAction.html#getInputValue())'.
 begin-user-doc 
If the meaning of the '*opaque Action Of Input Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*opaque Action Of Input Value*' container reference.
See Also:
[`set_opaqueActionOfInputValue(OpaqueAction)`](#set_opaqueActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction))
[`UMLPackage.getInputPin__opaqueActionOfInputValue()`](../../metadata/UMLPackage.html#getInputPin__opaqueActionOfInputValue())
[`OpaqueAction.getInputValue()`](OpaqueAction.html#getInputValue())
Model:
opposite="inputValue" transient="false" ordered="false"
Generated:
set_opaqueActionOfInputValue
void set_opaqueActionOfInputValue(@CheckForNull
 [OpaqueAction](OpaqueAction.html) value)
Sets the value of the '[`*opaque Action Of Input Value*`](#get_opaqueActionOfInputValue())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*opaque Action Of Input Value*' container reference.
See Also:
[`get_opaqueActionOfInputValue()`](#get_opaqueActionOfInputValue())
Generated:
get_loopNodeOfLoopVariableInput
@CheckForNull[LoopNode](../../activities/mdstructuredactivities/LoopNode.html) get_loopNodeOfLoopVariableInput()
Returns the value of the '***loop Node Of Loop Variable Input***' container reference.
 It is bidirectional and its opposite is
 '[`*Loop Variable Input*`](../../activities/mdstructuredactivities/LoopNode.html#getLoopVariableInput())'.
 begin-user-doc 
If the meaning of the '*loop Node Of Loop Variable Input*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*loop Node Of Loop Variable Input*' container reference.
See Also:
[`set_loopNodeOfLoopVariableInput(LoopNode)`](#set_loopNodeOfLoopVariableInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode))
[`UMLPackage.getInputPin__loopNodeOfLoopVariableInput()`](../../metadata/UMLPackage.html#getInputPin__loopNodeOfLoopVariableInput())
[`LoopNode.getLoopVariableInput()`](../../activities/mdstructuredactivities/LoopNode.html#getLoopVariableInput())
Model:
opposite="loopVariableInput" transient="false" ordered="false"
Generated:
set_loopNodeOfLoopVariableInput
void set_loopNodeOfLoopVariableInput(@CheckForNull
 [LoopNode](../../activities/mdstructuredactivities/LoopNode.html) value)
Sets the value of the
 '[`*loop Node Of Loop Variable Input*`](#get_loopNodeOfLoopVariableInput())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*loop Node Of Loop Variable Input*' container reference.
See Also:
[`get_loopNodeOfLoopVariableInput()`](#get_loopNodeOfLoopVariableInput())
Generated:
get_structuredActivityNodeOfStructuredNodeInput
@CheckForNull[StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html) get_structuredActivityNodeOfStructuredNodeInput()
Returns the value of the '***structured Activity Node Of Structured Node Input***' container reference.
 It is bidirectional and its opposite is
 '[`*Structured Node Input*`](../../activities/mdstructuredactivities/StructuredActivityNode.html#getStructuredNodeInput())'.
 begin-user-doc 
If the meaning of the '*structured Activity Node Of Structured Node Input*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*structured Activity Node Of Structured Node Input*' container reference.
See Also:
[`set_structuredActivityNodeOfStructuredNodeInput(StructuredActivityNode)`](#set_structuredActivityNodeOfStructuredNodeInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode))
[`UMLPackage.getInputPin__structuredActivityNodeOfStructuredNodeInput()`](../../metadata/UMLPackage.html#getInputPin__structuredActivityNodeOfStructuredNodeInput())
[`StructuredActivityNode.getStructuredNodeInput()`](../../activities/mdstructuredactivities/StructuredActivityNode.html#getStructuredNodeInput())
Model:
opposite="structuredNodeInput" transient="false" ordered="false"
Generated:
set_structuredActivityNodeOfStructuredNodeInput
void set_structuredActivityNodeOfStructuredNodeInput(@CheckForNull
 [StructuredActivityNode](../../activities/mdstructuredactivities/StructuredActivityNode.html) value)
Sets the value of the '[`*structured
 Activity Node Of Structured Node Input*`](#get_structuredActivityNodeOfStructuredNodeInput())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*structured Activity Node Of Structured Node Input*' container reference.
See Also:
[`get_structuredActivityNodeOfStructuredNodeInput()`](#get_structuredActivityNodeOfStructuredNodeInput())
Generated:
get_sendSignalActionOfTarget
@CheckForNull[SendSignalAction](SendSignalAction.html) get_sendSignalActionOfTarget()
Returns the value of the '***send Signal Action Of Target***' container reference.
 It is bidirectional and its opposite is '[`*Target*`](SendSignalAction.html#getTarget())'.
 begin-user-doc 
If the meaning of the '*send Signal Action Of Target*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*send Signal Action Of Target*' container reference.
See Also:
[`set_sendSignalActionOfTarget(SendSignalAction)`](#set_sendSignalActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction))
[`UMLPackage.getInputPin__sendSignalActionOfTarget()`](../../metadata/UMLPackage.html#getInputPin__sendSignalActionOfTarget())
[`SendSignalAction.getTarget()`](SendSignalAction.html#getTarget())
Model:
opposite="target" transient="false" ordered="false"
Generated:
set_sendSignalActionOfTarget
void set_sendSignalActionOfTarget(@CheckForNull
 [SendSignalAction](SendSignalAction.html) value)
Sets the value of the '[`*send Signal Action Of Target*`](#get_sendSignalActionOfTarget())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*send Signal Action Of Target*' container reference.
See Also:
[`get_sendSignalActionOfTarget()`](#get_sendSignalActionOfTarget())
Generated:
get_sendObjectActionOfRequest
@CheckForNull[SendObjectAction](../mdintermediateactions/SendObjectAction.html) get_sendObjectActionOfRequest()
Returns the value of the '***send Object Action Of Request***' container reference.
 It is bidirectional and its opposite is '[`*Request*`](../mdintermediateactions/SendObjectAction.html#getRequest())'.
 begin-user-doc 
If the meaning of the '*send Object Action Of Request*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*send Object Action Of Request*' container reference.
See Also:
[`set_sendObjectActionOfRequest(SendObjectAction)`](#set_sendObjectActionOfRequest(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction))
[`UMLPackage.getInputPin__sendObjectActionOfRequest()`](../../metadata/UMLPackage.html#getInputPin__sendObjectActionOfRequest())
[`SendObjectAction.getRequest()`](../mdintermediateactions/SendObjectAction.html#getRequest())
Model:
opposite="request" transient="false" ordered="false"
Generated:
set_sendObjectActionOfRequest
void set_sendObjectActionOfRequest(@CheckForNull
 [SendObjectAction](../mdintermediateactions/SendObjectAction.html) value)
Sets the value of the
 '[`*send Object Action Of Request*`](#get_sendObjectActionOfRequest())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*send Object Action Of Request*' container reference.
See Also:
[`get_sendObjectActionOfRequest()`](#get_sendObjectActionOfRequest())
Generated:
get_sendObjectActionOfTarget
@CheckForNull[SendObjectAction](../mdintermediateactions/SendObjectAction.html) get_sendObjectActionOfTarget()
Returns the value of the '***send Object Action Of Target***' container reference.
 It is bidirectional and its opposite is '[`*Target*`](../mdintermediateactions/SendObjectAction.html#getTarget())'.
 begin-user-doc 
If the meaning of the '*send Object Action Of Target*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*send Object Action Of Target*' container reference.
See Also:
[`set_sendObjectActionOfTarget(SendObjectAction)`](#set_sendObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction))
[`UMLPackage.getInputPin__sendObjectActionOfTarget()`](../../metadata/UMLPackage.html#getInputPin__sendObjectActionOfTarget())
[`SendObjectAction.getTarget()`](../mdintermediateactions/SendObjectAction.html#getTarget())
Model:
opposite="target" transient="false" ordered="false"
Generated:
set_sendObjectActionOfTarget
void set_sendObjectActionOfTarget(@CheckForNull
 [SendObjectAction](../mdintermediateactions/SendObjectAction.html) value)
Sets the value of the '[`*send Object Action Of Target*`](#get_sendObjectActionOfTarget())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*send Object Action Of Target*' container reference.
See Also:
[`get_sendObjectActionOfTarget()`](#get_sendObjectActionOfTarget())
Generated:
get_clearAssociationActionOfObject
@CheckForNull[ClearAssociationAction](../mdintermediateactions/ClearAssociationAction.html) get_clearAssociationActionOfObject()
Returns the value of the '***clear Association Action Of Object***' container reference.
 It is bidirectional and its opposite is '[`*Object*`](../mdintermediateactions/ClearAssociationAction.html#getObject())'.
 begin-user-doc 
If the meaning of the '*clear Association Action Of Object*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*clear Association Action Of Object*' container reference.
See Also:
[`set_clearAssociationActionOfObject(ClearAssociationAction)`](#set_clearAssociationActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction))
[`UMLPackage.getInputPin__clearAssociationActionOfObject()`](../../metadata/UMLPackage.html#getInputPin__clearAssociationActionOfObject())
[`ClearAssociationAction.getObject()`](../mdintermediateactions/ClearAssociationAction.html#getObject())
Model:
opposite="object" transient="false" ordered="false"
Generated:
set_clearAssociationActionOfObject
void set_clearAssociationActionOfObject(@CheckForNull
 [ClearAssociationAction](../mdintermediateactions/ClearAssociationAction.html) value)
Sets the value of the
 '[`*clear Association Action Of Object*`](#get_clearAssociationActionOfObject())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*clear Association Action Of Object*' container reference.
See Also:
[`get_clearAssociationActionOfObject()`](#get_clearAssociationActionOfObject())
Generated:
get_actionOfInput
@CheckForNull[Action](Action.html) get_actionOfInput()
Returns the value of the '***action Of Input***' reference.
 It is bidirectional and its opposite is '[`*Input*`](Action.html#getInput())'.
 begin-user-doc 
If the meaning of the '*action Of Input*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*action Of Input*' reference.
See Also:
[`set_actionOfInput(Action)`](#set_actionOfInput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action))
[`UMLPackage.getInputPin__actionOfInput()`](../../metadata/UMLPackage.html#getInputPin__actionOfInput())
[`Action.getInput()`](Action.html#getInput())
Model:
opposite="input" transient="true" volatile="true" derived="true" ordered="false"
Generated:
set_actionOfInput
void set_actionOfInput(@CheckForNull
 [Action](Action.html) value)
Sets the value of the '[`*action Of Input*`](#get_actionOfInput())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*action Of Input*' reference.
See Also:
[`get_actionOfInput()`](#get_actionOfInput())
Generated:
get_linkEndDestructionDataOfDestroyAt
@CheckForNull[LinkEndDestructionData](../mdintermediateactions/LinkEndDestructionData.html) get_linkEndDestructionDataOfDestroyAt()
Returns the value of the '***link End Destruction Data Of Destroy At***' reference.
 It is bidirectional and its opposite is
 '[`*Destroy At*`](../mdintermediateactions/LinkEndDestructionData.html#getDestroyAt())'.
 begin-user-doc 
If the meaning of the '*link End Destruction Data Of Destroy At*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*link End Destruction Data Of Destroy At*' reference.
See Also:
[`set_linkEndDestructionDataOfDestroyAt(LinkEndDestructionData)`](#set_linkEndDestructionDataOfDestroyAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData))
[`UMLPackage.getInputPin__linkEndDestructionDataOfDestroyAt()`](../../metadata/UMLPackage.html#getInputPin__linkEndDestructionDataOfDestroyAt())
[`LinkEndDestructionData.getDestroyAt()`](../mdintermediateactions/LinkEndDestructionData.html#getDestroyAt())
Model:
opposite="destroyAt" ordered="false"
Generated:
set_linkEndDestructionDataOfDestroyAt
void set_linkEndDestructionDataOfDestroyAt(@CheckForNull
 [LinkEndDestructionData](../mdintermediateactions/LinkEndDestructionData.html) value)
Sets the value of the
 '[`*link End Destruction Data Of Destroy At*`](#get_linkEndDestructionDataOfDestroyAt())'
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*link End Destruction Data Of Destroy At*' reference.
See Also:
[`get_linkEndDestructionDataOfDestroyAt()`](#get_linkEndDestructionDataOfDestroyAt())
Generated:
get_addVariableValueActionOfInsertAt
@CheckForNull[AddVariableValueAction](../mdstructuredactions/AddVariableValueAction.html) get_addVariableValueActionOfInsertAt()
Returns the value of the '***add Variable Value Action Of Insert At***' container reference.
 It is bidirectional and its opposite is
 '[`*Insert At*`](../mdstructuredactions/AddVariableValueAction.html#getInsertAt())'.
 begin-user-doc 
If the meaning of the '*add Variable Value Action Of Insert At*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*add Variable Value Action Of Insert At*' container reference.
See Also:
[`set_addVariableValueActionOfInsertAt(AddVariableValueAction)`](#set_addVariableValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction))
[`UMLPackage.getInputPin__addVariableValueActionOfInsertAt()`](../../metadata/UMLPackage.html#getInputPin__addVariableValueActionOfInsertAt())
[`AddVariableValueAction.getInsertAt()`](../mdstructuredactions/AddVariableValueAction.html#getInsertAt())
Model:
opposite="insertAt" transient="false" ordered="false"
Generated:
set_addVariableValueActionOfInsertAt
void set_addVariableValueActionOfInsertAt(@CheckForNull
 [AddVariableValueAction](../mdstructuredactions/AddVariableValueAction.html) value)
Sets the value of the '[`*add Variable Value Action
 Of Insert At*`](#get_addVariableValueActionOfInsertAt())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*add Variable Value Action Of Insert At*' container reference.
See Also:
[`get_addVariableValueActionOfInsertAt()`](#get_addVariableValueActionOfInsertAt())
Generated:
get_raiseExceptionActionOfException
@CheckForNull[RaiseExceptionAction](../mdstructuredactions/RaiseExceptionAction.html) get_raiseExceptionActionOfException()
Returns the value of the '***raise Exception Action Of Exception***' container reference.
 It is bidirectional and its opposite is '[`*Exception*`](../mdstructuredactions/RaiseExceptionAction.html#getException())'.
 begin-user-doc 
If the meaning of the '*raise Exception Action Of Exception*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*raise Exception Action Of Exception*' container reference.
See Also:
[`set_raiseExceptionActionOfException(RaiseExceptionAction)`](#set_raiseExceptionActionOfException(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction))
[`UMLPackage.getInputPin__raiseExceptionActionOfException()`](../../metadata/UMLPackage.html#getInputPin__raiseExceptionActionOfException())
[`RaiseExceptionAction.getException()`](../mdstructuredactions/RaiseExceptionAction.html#getException())
Model:
opposite="exception" transient="false" ordered="false"
Generated:
set_raiseExceptionActionOfException
void set_raiseExceptionActionOfException(@CheckForNull
 [RaiseExceptionAction](../mdstructuredactions/RaiseExceptionAction.html) value)
Sets the value of the
 '[`*raise Exception Action Of Exception*`](#get_raiseExceptionActionOfException())'
 container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*raise Exception Action Of Exception*' container reference.
See Also:
[`get_raiseExceptionActionOfException()`](#get_raiseExceptionActionOfException())
Generated:
get_writeVariableActionOfValue
@CheckForNull[WriteVariableAction](../mdstructuredactions/WriteVariableAction.html) get_writeVariableActionOfValue()
Returns the value of the '***write Variable Action Of Value***' container reference.
 It is bidirectional and its opposite is '[`*Value*`](../mdstructuredactions/WriteVariableAction.html#getValue())'.
 begin-user-doc 
If the meaning of the '*write Variable Action Of Value*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*write Variable Action Of Value*' container reference.
See Also:
[`set_writeVariableActionOfValue(WriteVariableAction)`](#set_writeVariableActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction))
[`UMLPackage.getInputPin__writeVariableActionOfValue()`](../../metadata/UMLPackage.html#getInputPin__writeVariableActionOfValue())
[`WriteVariableAction.getValue()`](../mdstructuredactions/WriteVariableAction.html#getValue())
Model:
opposite="value" transient="false" ordered="false"
Generated:
set_writeVariableActionOfValue
void set_writeVariableActionOfValue(@CheckForNull
 [WriteVariableAction](../mdstructuredactions/WriteVariableAction.html) value)
Sets the value of the
 '[`*write Variable Action Of Value*`](#get_writeVariableActionOfValue())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*write Variable Action Of Value*' container reference.
See Also:
[`get_writeVariableActionOfValue()`](#get_writeVariableActionOfValue())
Generated:
get_callOperationActionOfTarget
@CheckForNull[CallOperationAction](CallOperationAction.html) get_callOperationActionOfTarget()
Returns the value of the '***call Operation Action Of Target***' container reference.
 It is bidirectional and its opposite is '[`*Target*`](CallOperationAction.html#getTarget())'.
 begin-user-doc 
If the meaning of the '*call Operation Action Of Target*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*call Operation Action Of Target*' container reference.
See Also:
[`set_callOperationActionOfTarget(CallOperationAction)`](#set_callOperationActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction))
[`UMLPackage.getInputPin__callOperationActionOfTarget()`](../../metadata/UMLPackage.html#getInputPin__callOperationActionOfTarget())
[`CallOperationAction.getTarget()`](CallOperationAction.html#getTarget())
Model:
opposite="target" transient="false" ordered="false"
Generated:
set_callOperationActionOfTarget
void set_callOperationActionOfTarget(@CheckForNull
 [CallOperationAction](CallOperationAction.html) value)
Sets the value of the
 '[`*call Operation Action Of Target*`](#get_callOperationActionOfTarget())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*call Operation Action Of Target*' container reference.
See Also:
[`get_callOperationActionOfTarget()`](#get_callOperationActionOfTarget())
Generated:
get_addStructuralFeatureValueActionOfInsertAt
@CheckForNull[AddStructuralFeatureValueAction](../mdintermediateactions/AddStructuralFeatureValueAction.html) get_addStructuralFeatureValueActionOfInsertAt()
Returns the value of the '***add Structural Feature Value Action Of Insert At***' container reference.
 It is bidirectional and its opposite is
 '[`*Insert At*`](../mdintermediateactions/AddStructuralFeatureValueAction.html#getInsertAt())'.
 begin-user-doc 
If the meaning of the '*add Structural Feature Value Action Of Insert At*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*add Structural Feature Value Action Of Insert At*' container reference.
See Also:
[`set_addStructuralFeatureValueActionOfInsertAt(AddStructuralFeatureValueAction)`](#set_addStructuralFeatureValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction))
[`UMLPackage.getInputPin__addStructuralFeatureValueActionOfInsertAt()`](../../metadata/UMLPackage.html#getInputPin__addStructuralFeatureValueActionOfInsertAt())
[`AddStructuralFeatureValueAction.getInsertAt()`](../mdintermediateactions/AddStructuralFeatureValueAction.html#getInsertAt())
Model:
opposite="insertAt" transient="false" ordered="false"
Generated:
set_addStructuralFeatureValueActionOfInsertAt
void set_addStructuralFeatureValueActionOfInsertAt(@CheckForNull
 [AddStructuralFeatureValueAction](../mdintermediateactions/AddStructuralFeatureValueAction.html) value)
Sets the value of the '[`*add Structural
 Feature Value Action Of Insert At*`](#get_addStructuralFeatureValueActionOfInsertAt())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*add Structural Feature Value Action Of Insert At*' container reference.
See Also:
[`get_addStructuralFeatureValueActionOfInsertAt()`](#get_addStructuralFeatureValueActionOfInsertAt())
Generated:
get_removeVariableValueActionOfRemoveAt
@CheckForNull[RemoveVariableValueAction](../mdstructuredactions/RemoveVariableValueAction.html) get_removeVariableValueActionOfRemoveAt()
Returns the value of the '***remove Variable Value Action Of Remove At***' container reference.
 It is bidirectional and its opposite is
 '[`*Remove At*`](../mdstructuredactions/RemoveVariableValueAction.html#getRemoveAt())'.
 begin-user-doc 
If the meaning of the '*remove Variable Value Action Of Remove At*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*remove Variable Value Action Of Remove At*' container reference.
See Also:
[`set_removeVariableValueActionOfRemoveAt(RemoveVariableValueAction)`](#set_removeVariableValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction))
[`UMLPackage.getInputPin__removeVariableValueActionOfRemoveAt()`](../../metadata/UMLPackage.html#getInputPin__removeVariableValueActionOfRemoveAt())
[`RemoveVariableValueAction.getRemoveAt()`](../mdstructuredactions/RemoveVariableValueAction.html#getRemoveAt())
Model:
opposite="removeAt" transient="false" ordered="false"
Generated:
set_removeVariableValueActionOfRemoveAt
void set_removeVariableValueActionOfRemoveAt(@CheckForNull
 [RemoveVariableValueAction](../mdstructuredactions/RemoveVariableValueAction.html) value)
Sets the value of the '[`*remove Variable Value
 Action Of Remove At*`](#get_removeVariableValueActionOfRemoveAt())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*remove Variable Value Action Of Remove At*' container reference.
See Also:
[`get_removeVariableValueActionOfRemoveAt()`](#get_removeVariableValueActionOfRemoveAt())
Generated:
get_destroyObjectActionOfTarget
@CheckForNull[DestroyObjectAction](../mdintermediateactions/DestroyObjectAction.html) get_destroyObjectActionOfTarget()
Returns the value of the '***destroy Object Action Of Target***' container reference.
 It is bidirectional and its opposite is '[`*Target*`](../mdintermediateactions/DestroyObjectAction.html#getTarget())'.
 begin-user-doc 
If the meaning of the '*destroy Object Action Of Target*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*destroy Object Action Of Target*' container reference.
See Also:
[`set_destroyObjectActionOfTarget(DestroyObjectAction)`](#set_destroyObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction))
[`UMLPackage.getInputPin__destroyObjectActionOfTarget()`](../../metadata/UMLPackage.html#getInputPin__destroyObjectActionOfTarget())
[`DestroyObjectAction.getTarget()`](../mdintermediateactions/DestroyObjectAction.html#getTarget())
Model:
opposite="target" transient="false" ordered="false"
Generated:
set_destroyObjectActionOfTarget
void set_destroyObjectActionOfTarget(@CheckForNull
 [DestroyObjectAction](../mdintermediateactions/DestroyObjectAction.html) value)
Sets the value of the
 '[`*destroy Object Action Of Target*`](#get_destroyObjectActionOfTarget())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*destroy Object Action Of Target*' container reference.
See Also:
[`get_destroyObjectActionOfTarget()`](#get_destroyObjectActionOfTarget())
Generated:
get_removeStructuralFeatureValueActionOfRemoveAt
@CheckForNull[RemoveStructuralFeatureValueAction](../mdintermediateactions/RemoveStructuralFeatureValueAction.html) get_removeStructuralFeatureValueActionOfRemoveAt()
Returns the value of the '***remove Structural Feature Value Action Of Remove At***' container reference.
 It is bidirectional and its opposite is
 '[`*Remove At*`](../mdintermediateactions/RemoveStructuralFeatureValueAction.html#getRemoveAt())'.
 begin-user-doc 
If the meaning of the '*remove Structural Feature Value Action Of Remove At*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*remove Structural Feature Value Action Of Remove At*' container reference.
See Also:
[`set_removeStructuralFeatureValueActionOfRemoveAt(RemoveStructuralFeatureValueAction)`](#set_removeStructuralFeatureValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction))
[`UMLPackage.getInputPin__removeStructuralFeatureValueActionOfRemoveAt()`](../../metadata/UMLPackage.html#getInputPin__removeStructuralFeatureValueActionOfRemoveAt())
[`RemoveStructuralFeatureValueAction.getRemoveAt()`](../mdintermediateactions/RemoveStructuralFeatureValueAction.html#getRemoveAt())
Model:
opposite="removeAt" transient="false" ordered="false"
Generated:
set_removeStructuralFeatureValueActionOfRemoveAt
void set_removeStructuralFeatureValueActionOfRemoveAt(@CheckForNull
 [RemoveStructuralFeatureValueAction](../mdintermediateactions/RemoveStructuralFeatureValueAction.html) value)
Sets the value of the '[`*remove
 Structural Feature Value Action Of Remove At*`](#get_removeStructuralFeatureValueActionOfRemoveAt())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*remove Structural Feature Value Action Of Remove At*' container reference.
See Also:
[`get_removeStructuralFeatureValueActionOfRemoveAt()`](#get_removeStructuralFeatureValueActionOfRemoveAt())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions</a></div>
<h1 class="title" title="Interface InputPin">Interface InputPin</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../activities/mdfundamentalactivities/ActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">ActivityNode</a></code>, <code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../activities/mdbasicactivities/ObjectNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ObjectNode</a></code>, <code><a href="Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></code>, <code><a href="../../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../mdstructuredactions/ActionInputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">ActionInputPin</a></code>, <code><a href="ValuePin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">ValuePin</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">InputPin</span><span class="extends-implements">
extends <a href="Pin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Pin</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Input Pin</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An InputPin is a Pin that holds input values to be consumed by an Action.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_structuralFeatureActionOfObject()"><code><em>structural Feature Action Of Object</em></code></a></li>
<li><a href="#get_invocationActionOfArgument()"><code><em>invocation Action Of Argument</em></code></a></li>
<li><a href="#get_loopNodeOfLoopVariableInput()"><code><em>loop Node Of Loop Variable Input</em></code></a></li>
<li><a href="#get_reduceActionOfCollection()"><code><em>reduce Action Of Collection</em></code></a></li>
<li><a href="#get_unmarshallActionOfObject()"><code><em>unmarshall Action Of Object</em></code></a></li>
<li><a href="#get_opaqueActionOfInputValue()"><code><em>opaque Action Of Input Value</em></code></a></li>
<li><a href="#get_qualifierValueOfValue()"><code><em>qualifier Value Of Value</em></code></a></li>
<li><a href="#get_linkEndDataOfValue()"><code><em>link End Data Of Value</em></code></a></li>
<li><a href="#get_linkActionOfInputValue()"><code><em>link Action Of Input Value</em></code></a></li>
<li><a href="#get_readLinkObjectEndActionOfObject()"><code><em>read Link Object End Action Of Object</em></code></a></li>
<li><a href="#get_writeStructuralFeatureActionOfValue()"><code><em>write Structural Feature Action Of Value</em></code></a></li>
<li><a href="#get_linkEndCreationDataOfInsertAt()"><code><em>link End Creation Data Of Insert At</em></code></a></li>
<li><a href="#get_testIdentityActionOfFirst()"><code><em>test Identity Action Of First</em></code></a></li>
<li><a href="#get_testIdentityActionOfSecond()"><code><em>test Identity Action Of Second</em></code></a></li>
<li><a href="#get_readIsClassifiedObjectActionOfObject()"><code><em>read Is Classified Object Action Of Object</em></code></a></li>
<li><a href="#get_readLinkObjectEndQualifierActionOfObject()"><code><em>read Link Object End Qualifier Action Of Object</em></code></a></li>
<li><a href="#get_replyActionOfReplyValue()"><code><em>reply Action Of Reply Value</em></code></a></li>
<li><a href="#get_replyActionOfReturnInformation()"><code><em>reply Action Of Return Information</em></code></a></li>
<li><a href="#get_sendSignalActionOfTarget()"><code><em>send Signal Action Of Target</em></code></a></li>
<li><a href="#get_clearAssociationActionOfObject()"><code><em>clear Association Action Of Object</em></code></a></li>
<li><a href="#get_callOperationActionOfTarget()"><code><em>call Operation Action Of Target</em></code></a></li>
<li><a href="#get_sendObjectActionOfTarget()"><code><em>send Object Action Of Target</em></code></a></li>
<li><a href="#get_sendObjectActionOfRequest()"><code><em>send Object Action Of Request</em></code></a></li>
<li><a href="#get_addStructuralFeatureValueActionOfInsertAt()"><code><em>add Structural Feature Value Action Of Insert At</em></code></a></li>
<li><a href="#get_actionOfInput()"><code><em>action Of Input</em></code></a></li>
<li><a href="#get_removeStructuralFeatureValueActionOfRemoveAt()"><code><em>remove Structural Feature Value Action Of Remove At</em></code></a></li>
<li><a href="#get_startObjectBehaviorActionOfObject()"><code><em>start Object Behavior Action Of Object</em></code></a></li>
<li><a href="#get_removeVariableValueActionOfRemoveAt()"><code><em>remove Variable Value Action Of Remove At</em></code></a></li>
<li><a href="#get_writeVariableActionOfValue()"><code><em>write Variable Action Of Value</em></code></a></li>
<li><a href="#get_destroyObjectActionOfTarget()"><code><em>destroy Object Action Of Target</em></code></a></li>
<li><a href="#get_reclassifyObjectActionOfObject()"><code><em>reclassify Object Action Of Object</em></code></a></li>
<li><a href="#get_raiseExceptionActionOfException()"><code><em>raise Exception Action Of Exception</em></code></a></li>
<li><a href="#get_linkEndDestructionDataOfDestroyAt()"><code><em>link End Destruction Data Of Destroy At</em></code></a></li>
<li><a href="#get_addVariableValueActionOfInsertAt()"><code><em>add Variable Value Action Of Insert At</em></code></a></li>
<li><a href="#get_startClassifierBehaviorActionOfObject()"><code><em>start Classifier Behavior Action Of Object</em></code></a></li>
<li><a href="#get_structuredActivityNodeOfStructuredNodeInput()"><code><em>structured Activity Node Of Structured Node Input</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getInputPin()"><code>UMLPackage.getInputPin()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_actionOfInput()">get_actionOfInput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>action Of Input</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_addStructuralFeatureValueActionOfInsertAt()">get_addStructuralFeatureValueActionOfInsertAt</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>add Structural Feature Value Action Of Insert At</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_addVariableValueActionOfInsertAt()">get_addVariableValueActionOfInsertAt</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>add Variable Value Action Of Insert At</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_callOperationActionOfTarget()">get_callOperationActionOfTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>call Operation Action Of Target</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_clearAssociationActionOfObject()">get_clearAssociationActionOfObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>clear Association Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_destroyObjectActionOfTarget()">get_destroyObjectActionOfTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>destroy Object Action Of Target</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_invocationActionOfArgument()">get_invocationActionOfArgument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>invocation Action Of Argument</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_linkActionOfInputValue()">get_linkActionOfInputValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>link Action Of Input Value</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_linkEndCreationDataOfInsertAt()">get_linkEndCreationDataOfInsertAt</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>link End Creation Data Of Insert At</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_linkEndDataOfValue()">get_linkEndDataOfValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>link End Data Of Value</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_linkEndDestructionDataOfDestroyAt()">get_linkEndDestructionDataOfDestroyAt</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>link End Destruction Data Of Destroy At</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_loopNodeOfLoopVariableInput()">get_loopNodeOfLoopVariableInput</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>loop Node Of Loop Variable Input</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_opaqueActionOfInputValue()">get_opaqueActionOfInputValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>opaque Action Of Input Value</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_qualifierValueOfValue()">get_qualifierValueOfValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>qualifier Value Of Value</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_raiseExceptionActionOfException()">get_raiseExceptionActionOfException</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>raise Exception Action Of Exception</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readIsClassifiedObjectActionOfObject()">get_readIsClassifiedObjectActionOfObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Is Classified Object Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readLinkObjectEndActionOfObject()">get_readLinkObjectEndActionOfObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Link Object End Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_readLinkObjectEndQualifierActionOfObject()">get_readLinkObjectEndQualifierActionOfObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>read Link Object End Qualifier Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_reclassifyObjectActionOfObject()">get_reclassifyObjectActionOfObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reclassify Object Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_reduceActionOfCollection()">get_reduceActionOfCollection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reduce Action Of Collection</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_removeStructuralFeatureValueActionOfRemoveAt()">get_removeStructuralFeatureValueActionOfRemoveAt</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>remove Structural Feature Value Action Of Remove At</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_removeVariableValueActionOfRemoveAt()">get_removeVariableValueActionOfRemoveAt</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>remove Variable Value Action Of Remove At</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_replyActionOfReplyValue()">get_replyActionOfReplyValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reply Action Of Reply Value</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_replyActionOfReturnInformation()">get_replyActionOfReturnInformation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>reply Action Of Return Information</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_sendObjectActionOfRequest()">get_sendObjectActionOfRequest</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>send Object Action Of Request</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_sendObjectActionOfTarget()">get_sendObjectActionOfTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>send Object Action Of Target</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_sendSignalActionOfTarget()">get_sendSignalActionOfTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>send Signal Action Of Target</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_startClassifierBehaviorActionOfObject()">get_startClassifierBehaviorActionOfObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>start Classifier Behavior Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_startObjectBehaviorActionOfObject()">get_startObjectBehaviorActionOfObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>start Object Behavior Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_structuralFeatureActionOfObject()">get_structuralFeatureActionOfObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>structural Feature Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_structuredActivityNodeOfStructuredNodeInput()">get_structuredActivityNodeOfStructuredNodeInput</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>structured Activity Node Of Structured Node Input</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_testIdentityActionOfFirst()">get_testIdentityActionOfFirst</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>test Identity Action Of First</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_testIdentityActionOfSecond()">get_testIdentityActionOfSecond</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>test Identity Action Of Second</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_unmarshallActionOfObject()">get_unmarshallActionOfObject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>unmarshall Action Of Object</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_writeStructuralFeatureActionOfValue()">get_writeStructuralFeatureActionOfValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>write Structural Feature Action Of Value</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_writeVariableActionOfValue()">get_writeVariableActionOfValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>write Variable Action Of Value</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_actionOfInput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">set_actionOfInput</a><wbr/>(<a href="Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_actionOfInput()"><code><em>action Of Input</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_addStructuralFeatureValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction)">set_addStructuralFeatureValueActionOfInsertAt</a><wbr/>(<a href="../mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_addStructuralFeatureValueActionOfInsertAt()"><code><em>add Structural
 Feature Value Action Of Insert At</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_addVariableValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction)">set_addVariableValueActionOfInsertAt</a><wbr/>(<a href="../mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_addVariableValueActionOfInsertAt()"><code><em>add Variable Value Action
 Of Insert At</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_callOperationActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction)">set_callOperationActionOfTarget</a><wbr/>(<a href="CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_callOperationActionOfTarget()"><code><em>call Operation Action Of Target</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_clearAssociationActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction)">set_clearAssociationActionOfObject</a><wbr/>(<a href="../mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_clearAssociationActionOfObject()"><code><em>clear Association Action Of Object</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_destroyObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction)">set_destroyObjectActionOfTarget</a><wbr/>(<a href="../mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_destroyObjectActionOfTarget()"><code><em>destroy Object Action Of Target</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_invocationActionOfArgument(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction)">set_invocationActionOfArgument</a><wbr/>(<a href="InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_invocationActionOfArgument()"><code><em>invocation Action Of Argument</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_linkActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)">set_linkActionOfInputValue</a><wbr/>(<a href="../mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_linkActionOfInputValue()"><code><em>link Action Of Input Value</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_linkEndCreationDataOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData)">set_linkEndCreationDataOfInsertAt</a><wbr/>(<a href="../mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_linkEndCreationDataOfInsertAt()"><code><em>link End Creation Data Of Insert At</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_linkEndDataOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData)">set_linkEndDataOfValue</a><wbr/>(<a href="../mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_linkEndDataOfValue()"><code><em>link End Data Of Value</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_linkEndDestructionDataOfDestroyAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData)">set_linkEndDestructionDataOfDestroyAt</a><wbr/>(<a href="../mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_linkEndDestructionDataOfDestroyAt()"><code><em>link End Destruction Data Of Destroy At</em></code></a>'
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_loopNodeOfLoopVariableInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">set_loopNodeOfLoopVariableInput</a><wbr/>(<a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_loopNodeOfLoopVariableInput()"><code><em>loop Node Of Loop Variable Input</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_opaqueActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction)">set_opaqueActionOfInputValue</a><wbr/>(<a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_opaqueActionOfInputValue()"><code><em>opaque Action Of Input Value</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_qualifierValueOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue)">set_qualifierValueOfValue</a><wbr/>(<a href="../mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_qualifierValueOfValue()"><code><em>qualifier Value Of Value</em></code></a>'
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_raiseExceptionActionOfException(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction)">set_raiseExceptionActionOfException</a><wbr/>(<a href="../mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_raiseExceptionActionOfException()"><code><em>raise Exception Action Of Exception</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readIsClassifiedObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction)">set_readIsClassifiedObjectActionOfObject</a><wbr/>(<a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readIsClassifiedObjectActionOfObject()"><code><em>read Is Classified
 Object Action Of Object</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readLinkObjectEndActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction)">set_readLinkObjectEndActionOfObject</a><wbr/>(<a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readLinkObjectEndActionOfObject()"><code><em>read Link Object End Action
 Of Object</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_readLinkObjectEndQualifierActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction)">set_readLinkObjectEndQualifierActionOfObject</a><wbr/>(<a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_readLinkObjectEndQualifierActionOfObject()"><code><em>read Link Object
 End Qualifier Action Of Object</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_reclassifyObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction)">set_reclassifyObjectActionOfObject</a><wbr/>(<a href="../mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_reclassifyObjectActionOfObject()"><code><em>reclassify Object Action Of Object</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_reduceActionOfCollection(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction)">set_reduceActionOfCollection</a><wbr/>(<a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_reduceActionOfCollection()"><code><em>reduce Action Of Collection</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_removeStructuralFeatureValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction)">set_removeStructuralFeatureValueActionOfRemoveAt</a><wbr/>(<a href="../mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_removeStructuralFeatureValueActionOfRemoveAt()"><code><em>remove
 Structural Feature Value Action Of Remove At</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_removeVariableValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction)">set_removeVariableValueActionOfRemoveAt</a><wbr/>(<a href="../mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_removeVariableValueActionOfRemoveAt()"><code><em>remove Variable Value
 Action Of Remove At</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_replyActionOfReplyValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction)">set_replyActionOfReplyValue</a><wbr/>(<a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_replyActionOfReplyValue()"><code><em>reply Action Of Reply Value</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_replyActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction)">set_replyActionOfReturnInformation</a><wbr/>(<a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_replyActionOfReturnInformation()"><code><em>reply Action Of Return Information</em></code></a>' container
 reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_sendObjectActionOfRequest(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction)">set_sendObjectActionOfRequest</a><wbr/>(<a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_sendObjectActionOfRequest()"><code><em>send Object Action Of Request</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_sendObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction)">set_sendObjectActionOfTarget</a><wbr/>(<a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_sendObjectActionOfTarget()"><code><em>send Object Action Of Target</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_sendSignalActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction)">set_sendSignalActionOfTarget</a><wbr/>(<a href="SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_sendSignalActionOfTarget()"><code><em>send Signal Action Of Target</em></code></a>'
 container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_startClassifierBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction)">set_startClassifierBehaviorActionOfObject</a><wbr/>(<a href="../mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_startClassifierBehaviorActionOfObject()"><code><em>start Classifier
 Behavior Action Of Object</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_startObjectBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction)">set_startObjectBehaviorActionOfObject</a><wbr/>(<a href="../mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_startObjectBehaviorActionOfObject()"><code><em>start Object Behavior
 Action Of Object</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_structuralFeatureActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction)">set_structuralFeatureActionOfObject</a><wbr/>(<a href="../mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_structuralFeatureActionOfObject()"><code><em>structural Feature Action Of Object</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_structuredActivityNodeOfStructuredNodeInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">set_structuredActivityNodeOfStructuredNodeInput</a><wbr/>(<a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_structuredActivityNodeOfStructuredNodeInput()"><code><em>structured
 Activity Node Of Structured Node Input</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_testIdentityActionOfFirst(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)">set_testIdentityActionOfFirst</a><wbr/>(<a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_testIdentityActionOfFirst()"><code><em>test Identity Action Of First</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_testIdentityActionOfSecond(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)">set_testIdentityActionOfSecond</a><wbr/>(<a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_testIdentityActionOfSecond()"><code><em>test Identity Action Of Second</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_unmarshallActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction)">set_unmarshallActionOfObject</a><wbr/>(<a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_unmarshallActionOfObject()"><code><em>unmarshall Action Of Object</em></code></a>'
 container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_writeStructuralFeatureActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction)">set_writeStructuralFeatureActionOfValue</a><wbr/>(<a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_writeStructuralFeatureActionOfValue()"><code><em>write Structural Feature
 Action Of Value</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_writeVariableActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction)">set_writeVariableActionOfValue</a><wbr/>(<a href="../mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_writeVariableActionOfValue()"><code><em>write Variable Action Of Value</em></code></a>' container
 reference.</div>
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
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
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
<section class="detail" id="get_structuralFeatureActionOfObject()">
<h3>get_structuralFeatureActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a></span> <span class="element-name">get_structuralFeatureActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>structural Feature Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/StructuralFeatureAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>structural Feature Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>structural Feature Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_structuralFeatureActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction)"><code>set_structuralFeatureActionOfObject(StructuralFeatureAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__structuralFeatureActionOfObject()"><code>UMLPackage.getInputPin__structuralFeatureActionOfObject()</code></a></li>
<li><a href="../mdintermediateactions/StructuralFeatureAction.html#getObject()"><code>StructuralFeatureAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_structuralFeatureActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.StructuralFeatureAction)">
<h3>set_structuralFeatureActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_structuralFeatureActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/StructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">StructuralFeatureAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_structuralFeatureActionOfObject()"><code><em>structural Feature Action Of Object</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>structural Feature Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_structuralFeatureActionOfObject()"><code>get_structuralFeatureActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_writeStructuralFeatureActionOfValue()">
<h3>get_writeStructuralFeatureActionOfValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a></span> <span class="element-name">get_writeStructuralFeatureActionOfValue</span>()</div>
<div class="block">Returns the value of the '<em><b>write Structural Feature Action Of Value</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdintermediateactions/WriteStructuralFeatureAction.html#getValue()"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>write Structural Feature Action Of Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>write Structural Feature Action Of Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_writeStructuralFeatureActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction)"><code>set_writeStructuralFeatureActionOfValue(WriteStructuralFeatureAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__writeStructuralFeatureActionOfValue()"><code>UMLPackage.getInputPin__writeStructuralFeatureActionOfValue()</code></a></li>
<li><a href="../mdintermediateactions/WriteStructuralFeatureAction.html#getValue()"><code>WriteStructuralFeatureAction.getValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="value" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_writeStructuralFeatureActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.WriteStructuralFeatureAction)">
<h3>set_writeStructuralFeatureActionOfValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_writeStructuralFeatureActionOfValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/WriteStructuralFeatureAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">WriteStructuralFeatureAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_writeStructuralFeatureActionOfValue()"><code><em>write Structural Feature
 Action Of Value</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>write Structural Feature Action Of Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_writeStructuralFeatureActionOfValue()"><code>get_writeStructuralFeatureActionOfValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readLinkObjectEndActionOfObject()">
<h3>get_readLinkObjectEndActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a></span> <span class="element-name">get_readLinkObjectEndActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>read Link Object End Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReadLinkObjectEndAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Link Object End Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Link Object End Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readLinkObjectEndActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction)"><code>set_readLinkObjectEndActionOfObject(ReadLinkObjectEndAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__readLinkObjectEndActionOfObject()"><code>UMLPackage.getInputPin__readLinkObjectEndActionOfObject()</code></a></li>
<li><a href="../mdcompleteactions/ReadLinkObjectEndAction.html#getObject()"><code>ReadLinkObjectEndAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readLinkObjectEndActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndAction)">
<h3>set_readLinkObjectEndActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readLinkObjectEndActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReadLinkObjectEndAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readLinkObjectEndActionOfObject()"><code><em>read Link Object End Action
 Of Object</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Link Object End Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_readLinkObjectEndActionOfObject()"><code>get_readLinkObjectEndActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_qualifierValueOfValue()">
<h3>get_qualifierValueOfValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a></span> <span class="element-name">get_qualifierValueOfValue</span>()</div>
<div class="block">Returns the value of the '<em><b>qualifier Value Of Value</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/QualifierValue.html#getValue()"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>qualifier Value Of Value</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>qualifier Value Of Value</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_qualifierValueOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue)"><code>set_qualifierValueOfValue(QualifierValue)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__qualifierValueOfValue()"><code>UMLPackage.getInputPin__qualifierValueOfValue()</code></a></li>
<li><a href="../mdcompleteactions/QualifierValue.html#getValue()"><code>QualifierValue.getValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="value" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_qualifierValueOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.QualifierValue)">
<h3>set_qualifierValueOfValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_qualifierValueOfValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/QualifierValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">QualifierValue</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_qualifierValueOfValue()"><code><em>qualifier Value Of Value</em></code></a>'
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>qualifier Value Of Value</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_qualifierValueOfValue()"><code>get_qualifierValueOfValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_linkEndDataOfValue()">
<h3>get_linkEndDataOfValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a></span> <span class="element-name">get_linkEndDataOfValue</span>()</div>
<div class="block">Returns the value of the '<em><b>link End Data Of Value</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/LinkEndData.html#getValue()"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>link End Data Of Value</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>link End Data Of Value</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_linkEndDataOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData)"><code>set_linkEndDataOfValue(LinkEndData)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__linkEndDataOfValue()"><code>UMLPackage.getInputPin__linkEndDataOfValue()</code></a></li>
<li><a href="../mdintermediateactions/LinkEndData.html#getValue()"><code>LinkEndData.getValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="value" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_linkEndDataOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndData)">
<h3>set_linkEndDataOfValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_linkEndDataOfValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/LinkEndData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndData</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_linkEndDataOfValue()"><code><em>link End Data Of Value</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>link End Data Of Value</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_linkEndDataOfValue()"><code>get_linkEndDataOfValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_linkActionOfInputValue()">
<h3>get_linkActionOfInputValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a></span> <span class="element-name">get_linkActionOfInputValue</span>()</div>
<div class="block">Returns the value of the '<em><b>link Action Of Input Value</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/LinkAction.html#getInputValue()"><code><em>Input Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>link Action Of Input Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>link Action Of Input Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_linkActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)"><code>set_linkActionOfInputValue(LinkAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__linkActionOfInputValue()"><code>UMLPackage.getInputPin__linkActionOfInputValue()</code></a></li>
<li><a href="../mdintermediateactions/LinkAction.html#getInputValue()"><code>LinkAction.getInputValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="inputValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_linkActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkAction)">
<h3>set_linkActionOfInputValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_linkActionOfInputValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/LinkAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_linkActionOfInputValue()"><code><em>link Action Of Input Value</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>link Action Of Input Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_linkActionOfInputValue()"><code>get_linkActionOfInputValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readIsClassifiedObjectActionOfObject()">
<h3>get_readIsClassifiedObjectActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a></span> <span class="element-name">get_readIsClassifiedObjectActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>read Is Classified Object Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Is Classified Object Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Is Classified Object Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readIsClassifiedObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction)"><code>set_readIsClassifiedObjectActionOfObject(ReadIsClassifiedObjectAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__readIsClassifiedObjectActionOfObject()"><code>UMLPackage.getInputPin__readIsClassifiedObjectActionOfObject()</code></a></li>
<li><a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html#getObject()"><code>ReadIsClassifiedObjectAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readIsClassifiedObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadIsClassifiedObjectAction)">
<h3>set_readIsClassifiedObjectActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readIsClassifiedObjectActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReadIsClassifiedObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadIsClassifiedObjectAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readIsClassifiedObjectActionOfObject()"><code><em>read Is Classified
 Object Action Of Object</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Is Classified Object Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_readIsClassifiedObjectActionOfObject()"><code>get_readIsClassifiedObjectActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_readLinkObjectEndQualifierActionOfObject()">
<h3>get_readLinkObjectEndQualifierActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a></span> <span class="element-name">get_readLinkObjectEndQualifierActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>read Link Object End Qualifier Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>read Link Object End Qualifier Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>read Link Object End Qualifier Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_readLinkObjectEndQualifierActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction)"><code>set_readLinkObjectEndQualifierActionOfObject(ReadLinkObjectEndQualifierAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__readLinkObjectEndQualifierActionOfObject()"><code>UMLPackage.getInputPin__readLinkObjectEndQualifierActionOfObject()</code></a></li>
<li><a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html#getObject()"><code>ReadLinkObjectEndQualifierAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_readLinkObjectEndQualifierActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReadLinkObjectEndQualifierAction)">
<h3>set_readLinkObjectEndQualifierActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_readLinkObjectEndQualifierActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReadLinkObjectEndQualifierAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReadLinkObjectEndQualifierAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_readLinkObjectEndQualifierActionOfObject()"><code><em>read Link Object
 End Qualifier Action Of Object</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>read Link Object End Qualifier Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_readLinkObjectEndQualifierActionOfObject()"><code>get_readLinkObjectEndQualifierActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_reclassifyObjectActionOfObject()">
<h3>get_reclassifyObjectActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a></span> <span class="element-name">get_reclassifyObjectActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>reclassify Object Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReclassifyObjectAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reclassify Object Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reclassify Object Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_reclassifyObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction)"><code>set_reclassifyObjectActionOfObject(ReclassifyObjectAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__reclassifyObjectActionOfObject()"><code>UMLPackage.getInputPin__reclassifyObjectActionOfObject()</code></a></li>
<li><a href="../mdcompleteactions/ReclassifyObjectAction.html#getObject()"><code>ReclassifyObjectAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_reclassifyObjectActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReclassifyObjectAction)">
<h3>set_reclassifyObjectActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_reclassifyObjectActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReclassifyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReclassifyObjectAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_reclassifyObjectActionOfObject()"><code><em>reclassify Object Action Of Object</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>reclassify Object Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_reclassifyObjectActionOfObject()"><code>get_reclassifyObjectActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_unmarshallActionOfObject()">
<h3>get_unmarshallActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a></span> <span class="element-name">get_unmarshallActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>unmarshall Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/UnmarshallAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>unmarshall Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>unmarshall Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_unmarshallActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction)"><code>set_unmarshallActionOfObject(UnmarshallAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__unmarshallActionOfObject()"><code>UMLPackage.getInputPin__unmarshallActionOfObject()</code></a></li>
<li><a href="../mdcompleteactions/UnmarshallAction.html#getObject()"><code>UnmarshallAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_unmarshallActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.UnmarshallAction)">
<h3>set_unmarshallActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_unmarshallActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/UnmarshallAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">UnmarshallAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_unmarshallActionOfObject()"><code><em>unmarshall Action Of Object</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>unmarshall Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_unmarshallActionOfObject()"><code>get_unmarshallActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_startClassifierBehaviorActionOfObject()">
<h3>get_startClassifierBehaviorActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a></span> <span class="element-name">get_startClassifierBehaviorActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>start Classifier Behavior Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdcompleteactions/StartClassifierBehaviorAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>start Classifier Behavior Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>start Classifier Behavior Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_startClassifierBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction)"><code>set_startClassifierBehaviorActionOfObject(StartClassifierBehaviorAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__startClassifierBehaviorActionOfObject()"><code>UMLPackage.getInputPin__startClassifierBehaviorActionOfObject()</code></a></li>
<li><a href="../mdcompleteactions/StartClassifierBehaviorAction.html#getObject()"><code>StartClassifierBehaviorAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_startClassifierBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartClassifierBehaviorAction)">
<h3>set_startClassifierBehaviorActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_startClassifierBehaviorActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/StartClassifierBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartClassifierBehaviorAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_startClassifierBehaviorActionOfObject()"><code><em>start Classifier
 Behavior Action Of Object</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>start Classifier Behavior Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_startClassifierBehaviorActionOfObject()"><code>get_startClassifierBehaviorActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_invocationActionOfArgument()">
<h3>get_invocationActionOfArgument</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a></span> <span class="element-name">get_invocationActionOfArgument</span>()</div>
<div class="block">Returns the value of the '<em><b>invocation Action Of Argument</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="InvocationAction.html#getArgument()"><code><em>Argument</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>invocation Action Of Argument</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>invocation Action Of Argument</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_invocationActionOfArgument(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction)"><code>set_invocationActionOfArgument(InvocationAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__invocationActionOfArgument()"><code>UMLPackage.getInputPin__invocationActionOfArgument()</code></a></li>
<li><a href="InvocationAction.html#getArgument()"><code>InvocationAction.getArgument()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="argument" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_invocationActionOfArgument(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.InvocationAction)">
<h3>set_invocationActionOfArgument</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_invocationActionOfArgument</span><wbr/><span class="parameters">(@CheckForNull
 <a href="InvocationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InvocationAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_invocationActionOfArgument()"><code><em>invocation Action Of Argument</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>invocation Action Of Argument</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_invocationActionOfArgument()"><code>get_invocationActionOfArgument()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_startObjectBehaviorActionOfObject()">
<h3>get_startObjectBehaviorActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a></span> <span class="element-name">get_startObjectBehaviorActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>start Object Behavior Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/StartObjectBehaviorAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>start Object Behavior Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>start Object Behavior Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_startObjectBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction)"><code>set_startObjectBehaviorActionOfObject(StartObjectBehaviorAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__startObjectBehaviorActionOfObject()"><code>UMLPackage.getInputPin__startObjectBehaviorActionOfObject()</code></a></li>
<li><a href="../mdcompleteactions/StartObjectBehaviorAction.html#getObject()"><code>StartObjectBehaviorAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_startObjectBehaviorActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.StartObjectBehaviorAction)">
<h3>set_startObjectBehaviorActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_startObjectBehaviorActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/StartObjectBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">StartObjectBehaviorAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_startObjectBehaviorActionOfObject()"><code><em>start Object Behavior
 Action Of Object</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>start Object Behavior Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_startObjectBehaviorActionOfObject()"><code>get_startObjectBehaviorActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_reduceActionOfCollection()">
<h3>get_reduceActionOfCollection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a></span> <span class="element-name">get_reduceActionOfCollection</span>()</div>
<div class="block">Returns the value of the '<em><b>reduce Action Of Collection</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReduceAction.html#getCollection()"><code><em>Collection</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reduce Action Of Collection</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reduce Action Of Collection</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_reduceActionOfCollection(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction)"><code>set_reduceActionOfCollection(ReduceAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__reduceActionOfCollection()"><code>UMLPackage.getInputPin__reduceActionOfCollection()</code></a></li>
<li><a href="../mdcompleteactions/ReduceAction.html#getCollection()"><code>ReduceAction.getCollection()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="collection" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_reduceActionOfCollection(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReduceAction)">
<h3>set_reduceActionOfCollection</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_reduceActionOfCollection</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReduceAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReduceAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_reduceActionOfCollection()"><code><em>reduce Action Of Collection</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>reduce Action Of Collection</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_reduceActionOfCollection()"><code>get_reduceActionOfCollection()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_replyActionOfReturnInformation()">
<h3>get_replyActionOfReturnInformation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></span> <span class="element-name">get_replyActionOfReturnInformation</span>()</div>
<div class="block">Returns the value of the '<em><b>reply Action Of Return Information</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdcompleteactions/ReplyAction.html#getReturnInformation()"><code><em>Return Information</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reply Action Of Return Information</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reply Action Of Return Information</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_replyActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction)"><code>set_replyActionOfReturnInformation(ReplyAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__replyActionOfReturnInformation()"><code>UMLPackage.getInputPin__replyActionOfReturnInformation()</code></a></li>
<li><a href="../mdcompleteactions/ReplyAction.html#getReturnInformation()"><code>ReplyAction.getReturnInformation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="returnInformation" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_replyActionOfReturnInformation(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction)">
<h3>set_replyActionOfReturnInformation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_replyActionOfReturnInformation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_replyActionOfReturnInformation()"><code><em>reply Action Of Return Information</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>reply Action Of Return Information</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_replyActionOfReturnInformation()"><code>get_replyActionOfReturnInformation()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_replyActionOfReplyValue()">
<h3>get_replyActionOfReplyValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a></span> <span class="element-name">get_replyActionOfReplyValue</span>()</div>
<div class="block">Returns the value of the '<em><b>reply Action Of Reply Value</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdcompleteactions/ReplyAction.html#getReplyValue()"><code><em>Reply Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>reply Action Of Reply Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>reply Action Of Reply Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_replyActionOfReplyValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction)"><code>set_replyActionOfReplyValue(ReplyAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__replyActionOfReplyValue()"><code>UMLPackage.getInputPin__replyActionOfReplyValue()</code></a></li>
<li><a href="../mdcompleteactions/ReplyAction.html#getReplyValue()"><code>ReplyAction.getReplyValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="replyValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_replyActionOfReplyValue(com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions.ReplyAction)">
<h3>set_replyActionOfReplyValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_replyActionOfReplyValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdcompleteactions/ReplyAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdcompleteactions">ReplyAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_replyActionOfReplyValue()"><code><em>reply Action Of Reply Value</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>reply Action Of Reply Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_replyActionOfReplyValue()"><code>get_replyActionOfReplyValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_linkEndCreationDataOfInsertAt()">
<h3>get_linkEndCreationDataOfInsertAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a></span> <span class="element-name">get_linkEndCreationDataOfInsertAt</span>()</div>
<div class="block">Returns the value of the '<em><b>link End Creation Data Of Insert At</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/LinkEndCreationData.html#getInsertAt()"><code><em>Insert At</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>link End Creation Data Of Insert At</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>link End Creation Data Of Insert At</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_linkEndCreationDataOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData)"><code>set_linkEndCreationDataOfInsertAt(LinkEndCreationData)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__linkEndCreationDataOfInsertAt()"><code>UMLPackage.getInputPin__linkEndCreationDataOfInsertAt()</code></a></li>
<li><a href="../mdintermediateactions/LinkEndCreationData.html#getInsertAt()"><code>LinkEndCreationData.getInsertAt()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="insertAt" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_linkEndCreationDataOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndCreationData)">
<h3>set_linkEndCreationDataOfInsertAt</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_linkEndCreationDataOfInsertAt</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/LinkEndCreationData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndCreationData</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_linkEndCreationDataOfInsertAt()"><code><em>link End Creation Data Of Insert At</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>link End Creation Data Of Insert At</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_linkEndCreationDataOfInsertAt()"><code>get_linkEndCreationDataOfInsertAt()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_testIdentityActionOfFirst()">
<h3>get_testIdentityActionOfFirst</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></span> <span class="element-name">get_testIdentityActionOfFirst</span>()</div>
<div class="block">Returns the value of the '<em><b>test Identity Action Of First</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/TestIdentityAction.html#getFirst()"><code><em>First</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>test Identity Action Of First</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>test Identity Action Of First</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_testIdentityActionOfFirst(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)"><code>set_testIdentityActionOfFirst(TestIdentityAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__testIdentityActionOfFirst()"><code>UMLPackage.getInputPin__testIdentityActionOfFirst()</code></a></li>
<li><a href="../mdintermediateactions/TestIdentityAction.html#getFirst()"><code>TestIdentityAction.getFirst()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="first" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_testIdentityActionOfFirst(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)">
<h3>set_testIdentityActionOfFirst</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_testIdentityActionOfFirst</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_testIdentityActionOfFirst()"><code><em>test Identity Action Of First</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>test Identity Action Of First</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_testIdentityActionOfFirst()"><code>get_testIdentityActionOfFirst()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_testIdentityActionOfSecond()">
<h3>get_testIdentityActionOfSecond</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a></span> <span class="element-name">get_testIdentityActionOfSecond</span>()</div>
<div class="block">Returns the value of the '<em><b>test Identity Action Of Second</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/TestIdentityAction.html#getSecond()"><code><em>Second</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>test Identity Action Of Second</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>test Identity Action Of Second</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_testIdentityActionOfSecond(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)"><code>set_testIdentityActionOfSecond(TestIdentityAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__testIdentityActionOfSecond()"><code>UMLPackage.getInputPin__testIdentityActionOfSecond()</code></a></li>
<li><a href="../mdintermediateactions/TestIdentityAction.html#getSecond()"><code>TestIdentityAction.getSecond()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="second" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_testIdentityActionOfSecond(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.TestIdentityAction)">
<h3>set_testIdentityActionOfSecond</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_testIdentityActionOfSecond</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/TestIdentityAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">TestIdentityAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_testIdentityActionOfSecond()"><code><em>test Identity Action Of Second</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>test Identity Action Of Second</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_testIdentityActionOfSecond()"><code>get_testIdentityActionOfSecond()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_opaqueActionOfInputValue()">
<h3>get_opaqueActionOfInputValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a></span> <span class="element-name">get_opaqueActionOfInputValue</span>()</div>
<div class="block">Returns the value of the '<em><b>opaque Action Of Input Value</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="OpaqueAction.html#getInputValue()"><code><em>Input Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>opaque Action Of Input Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>opaque Action Of Input Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_opaqueActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction)"><code>set_opaqueActionOfInputValue(OpaqueAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__opaqueActionOfInputValue()"><code>UMLPackage.getInputPin__opaqueActionOfInputValue()</code></a></li>
<li><a href="OpaqueAction.html#getInputValue()"><code>OpaqueAction.getInputValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="inputValue" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_opaqueActionOfInputValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.OpaqueAction)">
<h3>set_opaqueActionOfInputValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_opaqueActionOfInputValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="OpaqueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">OpaqueAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_opaqueActionOfInputValue()"><code><em>opaque Action Of Input Value</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>opaque Action Of Input Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_opaqueActionOfInputValue()"><code>get_opaqueActionOfInputValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_loopNodeOfLoopVariableInput()">
<h3>get_loopNodeOfLoopVariableInput</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a></span> <span class="element-name">get_loopNodeOfLoopVariableInput</span>()</div>
<div class="block">Returns the value of the '<em><b>loop Node Of Loop Variable Input</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdstructuredactivities/LoopNode.html#getLoopVariableInput()"><code><em>Loop Variable Input</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>loop Node Of Loop Variable Input</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>loop Node Of Loop Variable Input</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_loopNodeOfLoopVariableInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)"><code>set_loopNodeOfLoopVariableInput(LoopNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__loopNodeOfLoopVariableInput()"><code>UMLPackage.getInputPin__loopNodeOfLoopVariableInput()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/LoopNode.html#getLoopVariableInput()"><code>LoopNode.getLoopVariableInput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="loopVariableInput" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_loopNodeOfLoopVariableInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.LoopNode)">
<h3>set_loopNodeOfLoopVariableInput</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_loopNodeOfLoopVariableInput</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdstructuredactivities/LoopNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">LoopNode</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_loopNodeOfLoopVariableInput()"><code><em>loop Node Of Loop Variable Input</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>loop Node Of Loop Variable Input</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_loopNodeOfLoopVariableInput()"><code>get_loopNodeOfLoopVariableInput()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_structuredActivityNodeOfStructuredNodeInput()">
<h3>get_structuredActivityNodeOfStructuredNodeInput</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></span> <span class="element-name">get_structuredActivityNodeOfStructuredNodeInput</span>()</div>
<div class="block">Returns the value of the '<em><b>structured Activity Node Of Structured Node Input</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../../activities/mdstructuredactivities/StructuredActivityNode.html#getStructuredNodeInput()"><code><em>Structured Node Input</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>structured Activity Node Of Structured Node Input</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>structured Activity Node Of Structured Node Input</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_structuredActivityNodeOfStructuredNodeInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)"><code>set_structuredActivityNodeOfStructuredNodeInput(StructuredActivityNode)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__structuredActivityNodeOfStructuredNodeInput()"><code>UMLPackage.getInputPin__structuredActivityNodeOfStructuredNodeInput()</code></a></li>
<li><a href="../../activities/mdstructuredactivities/StructuredActivityNode.html#getStructuredNodeInput()"><code>StructuredActivityNode.getStructuredNodeInput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="structuredNodeInput" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_structuredActivityNodeOfStructuredNodeInput(com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities.StructuredActivityNode)">
<h3>set_structuredActivityNodeOfStructuredNodeInput</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_structuredActivityNodeOfStructuredNodeInput</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_structuredActivityNodeOfStructuredNodeInput()"><code><em>structured
 Activity Node Of Structured Node Input</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>structured Activity Node Of Structured Node Input</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_structuredActivityNodeOfStructuredNodeInput()"><code>get_structuredActivityNodeOfStructuredNodeInput()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_sendSignalActionOfTarget()">
<h3>get_sendSignalActionOfTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a></span> <span class="element-name">get_sendSignalActionOfTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>send Signal Action Of Target</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="SendSignalAction.html#getTarget()"><code><em>Target</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>send Signal Action Of Target</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>send Signal Action Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_sendSignalActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction)"><code>set_sendSignalActionOfTarget(SendSignalAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__sendSignalActionOfTarget()"><code>UMLPackage.getInputPin__sendSignalActionOfTarget()</code></a></li>
<li><a href="SendSignalAction.html#getTarget()"><code>SendSignalAction.getTarget()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="target" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_sendSignalActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.SendSignalAction)">
<h3>set_sendSignalActionOfTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_sendSignalActionOfTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="SendSignalAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">SendSignalAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_sendSignalActionOfTarget()"><code><em>send Signal Action Of Target</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>send Signal Action Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_sendSignalActionOfTarget()"><code>get_sendSignalActionOfTarget()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_sendObjectActionOfRequest()">
<h3>get_sendObjectActionOfRequest</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></span> <span class="element-name">get_sendObjectActionOfRequest</span>()</div>
<div class="block">Returns the value of the '<em><b>send Object Action Of Request</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/SendObjectAction.html#getRequest()"><code><em>Request</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>send Object Action Of Request</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>send Object Action Of Request</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_sendObjectActionOfRequest(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction)"><code>set_sendObjectActionOfRequest(SendObjectAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__sendObjectActionOfRequest()"><code>UMLPackage.getInputPin__sendObjectActionOfRequest()</code></a></li>
<li><a href="../mdintermediateactions/SendObjectAction.html#getRequest()"><code>SendObjectAction.getRequest()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="request" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_sendObjectActionOfRequest(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction)">
<h3>set_sendObjectActionOfRequest</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_sendObjectActionOfRequest</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_sendObjectActionOfRequest()"><code><em>send Object Action Of Request</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>send Object Action Of Request</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_sendObjectActionOfRequest()"><code>get_sendObjectActionOfRequest()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_sendObjectActionOfTarget()">
<h3>get_sendObjectActionOfTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a></span> <span class="element-name">get_sendObjectActionOfTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>send Object Action Of Target</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/SendObjectAction.html#getTarget()"><code><em>Target</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>send Object Action Of Target</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>send Object Action Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_sendObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction)"><code>set_sendObjectActionOfTarget(SendObjectAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__sendObjectActionOfTarget()"><code>UMLPackage.getInputPin__sendObjectActionOfTarget()</code></a></li>
<li><a href="../mdintermediateactions/SendObjectAction.html#getTarget()"><code>SendObjectAction.getTarget()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="target" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_sendObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.SendObjectAction)">
<h3>set_sendObjectActionOfTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_sendObjectActionOfTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/SendObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">SendObjectAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_sendObjectActionOfTarget()"><code><em>send Object Action Of Target</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>send Object Action Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_sendObjectActionOfTarget()"><code>get_sendObjectActionOfTarget()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_clearAssociationActionOfObject()">
<h3>get_clearAssociationActionOfObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a></span> <span class="element-name">get_clearAssociationActionOfObject</span>()</div>
<div class="block">Returns the value of the '<em><b>clear Association Action Of Object</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/ClearAssociationAction.html#getObject()"><code><em>Object</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>clear Association Action Of Object</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>clear Association Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_clearAssociationActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction)"><code>set_clearAssociationActionOfObject(ClearAssociationAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__clearAssociationActionOfObject()"><code>UMLPackage.getInputPin__clearAssociationActionOfObject()</code></a></li>
<li><a href="../mdintermediateactions/ClearAssociationAction.html#getObject()"><code>ClearAssociationAction.getObject()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="object" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_clearAssociationActionOfObject(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ClearAssociationAction)">
<h3>set_clearAssociationActionOfObject</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_clearAssociationActionOfObject</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/ClearAssociationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">ClearAssociationAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_clearAssociationActionOfObject()"><code><em>clear Association Action Of Object</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>clear Association Action Of Object</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_clearAssociationActionOfObject()"><code>get_clearAssociationActionOfObject()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_actionOfInput()">
<h3>get_actionOfInput</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a></span> <span class="element-name">get_actionOfInput</span>()</div>
<div class="block">Returns the value of the '<em><b>action Of Input</b></em>' reference.
 It is bidirectional and its opposite is '<a href="Action.html#getInput()"><code><em>Input</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>action Of Input</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>action Of Input</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_actionOfInput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)"><code>set_actionOfInput(Action)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__actionOfInput()"><code>UMLPackage.getInputPin__actionOfInput()</code></a></li>
<li><a href="Action.html#getInput()"><code>Action.getInput()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="input" transient="true" volatile="true" derived="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_actionOfInput(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.Action)">
<h3>set_actionOfInput</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_actionOfInput</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Action.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">Action</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_actionOfInput()"><code><em>action Of Input</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>action Of Input</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#get_actionOfInput()"><code>get_actionOfInput()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_linkEndDestructionDataOfDestroyAt()">
<h3>get_linkEndDestructionDataOfDestroyAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a></span> <span class="element-name">get_linkEndDestructionDataOfDestroyAt</span>()</div>
<div class="block">Returns the value of the '<em><b>link End Destruction Data Of Destroy At</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="../mdintermediateactions/LinkEndDestructionData.html#getDestroyAt()"><code><em>Destroy At</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>link End Destruction Data Of Destroy At</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>link End Destruction Data Of Destroy At</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_linkEndDestructionDataOfDestroyAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData)"><code>set_linkEndDestructionDataOfDestroyAt(LinkEndDestructionData)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__linkEndDestructionDataOfDestroyAt()"><code>UMLPackage.getInputPin__linkEndDestructionDataOfDestroyAt()</code></a></li>
<li><a href="../mdintermediateactions/LinkEndDestructionData.html#getDestroyAt()"><code>LinkEndDestructionData.getDestroyAt()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="destroyAt" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_linkEndDestructionDataOfDestroyAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.LinkEndDestructionData)">
<h3>set_linkEndDestructionDataOfDestroyAt</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_linkEndDestructionDataOfDestroyAt</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/LinkEndDestructionData.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">LinkEndDestructionData</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_linkEndDestructionDataOfDestroyAt()"><code><em>link End Destruction Data Of Destroy At</em></code></a>'
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>link End Destruction Data Of Destroy At</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_linkEndDestructionDataOfDestroyAt()"><code>get_linkEndDestructionDataOfDestroyAt()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_addVariableValueActionOfInsertAt()">
<h3>get_addVariableValueActionOfInsertAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a></span> <span class="element-name">get_addVariableValueActionOfInsertAt</span>()</div>
<div class="block">Returns the value of the '<em><b>add Variable Value Action Of Insert At</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdstructuredactions/AddVariableValueAction.html#getInsertAt()"><code><em>Insert At</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>add Variable Value Action Of Insert At</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>add Variable Value Action Of Insert At</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_addVariableValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction)"><code>set_addVariableValueActionOfInsertAt(AddVariableValueAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__addVariableValueActionOfInsertAt()"><code>UMLPackage.getInputPin__addVariableValueActionOfInsertAt()</code></a></li>
<li><a href="../mdstructuredactions/AddVariableValueAction.html#getInsertAt()"><code>AddVariableValueAction.getInsertAt()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="insertAt" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_addVariableValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.AddVariableValueAction)">
<h3>set_addVariableValueActionOfInsertAt</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_addVariableValueActionOfInsertAt</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdstructuredactions/AddVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">AddVariableValueAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_addVariableValueActionOfInsertAt()"><code><em>add Variable Value Action
 Of Insert At</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>add Variable Value Action Of Insert At</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_addVariableValueActionOfInsertAt()"><code>get_addVariableValueActionOfInsertAt()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_raiseExceptionActionOfException()">
<h3>get_raiseExceptionActionOfException</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a></span> <span class="element-name">get_raiseExceptionActionOfException</span>()</div>
<div class="block">Returns the value of the '<em><b>raise Exception Action Of Exception</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdstructuredactions/RaiseExceptionAction.html#getException()"><code><em>Exception</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>raise Exception Action Of Exception</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>raise Exception Action Of Exception</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_raiseExceptionActionOfException(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction)"><code>set_raiseExceptionActionOfException(RaiseExceptionAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__raiseExceptionActionOfException()"><code>UMLPackage.getInputPin__raiseExceptionActionOfException()</code></a></li>
<li><a href="../mdstructuredactions/RaiseExceptionAction.html#getException()"><code>RaiseExceptionAction.getException()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="exception" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_raiseExceptionActionOfException(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RaiseExceptionAction)">
<h3>set_raiseExceptionActionOfException</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_raiseExceptionActionOfException</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdstructuredactions/RaiseExceptionAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RaiseExceptionAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_raiseExceptionActionOfException()"><code><em>raise Exception Action Of Exception</em></code></a>'
 container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>raise Exception Action Of Exception</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_raiseExceptionActionOfException()"><code>get_raiseExceptionActionOfException()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_writeVariableActionOfValue()">
<h3>get_writeVariableActionOfValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a></span> <span class="element-name">get_writeVariableActionOfValue</span>()</div>
<div class="block">Returns the value of the '<em><b>write Variable Action Of Value</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdstructuredactions/WriteVariableAction.html#getValue()"><code><em>Value</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>write Variable Action Of Value</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>write Variable Action Of Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_writeVariableActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction)"><code>set_writeVariableActionOfValue(WriteVariableAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__writeVariableActionOfValue()"><code>UMLPackage.getInputPin__writeVariableActionOfValue()</code></a></li>
<li><a href="../mdstructuredactions/WriteVariableAction.html#getValue()"><code>WriteVariableAction.getValue()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="value" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_writeVariableActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.WriteVariableAction)">
<h3>set_writeVariableActionOfValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_writeVariableActionOfValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdstructuredactions/WriteVariableAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">WriteVariableAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_writeVariableActionOfValue()"><code><em>write Variable Action Of Value</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>write Variable Action Of Value</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_writeVariableActionOfValue()"><code>get_writeVariableActionOfValue()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_callOperationActionOfTarget()">
<h3>get_callOperationActionOfTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a></span> <span class="element-name">get_callOperationActionOfTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>call Operation Action Of Target</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="CallOperationAction.html#getTarget()"><code><em>Target</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>call Operation Action Of Target</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>call Operation Action Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_callOperationActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction)"><code>set_callOperationActionOfTarget(CallOperationAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__callOperationActionOfTarget()"><code>UMLPackage.getInputPin__callOperationActionOfTarget()</code></a></li>
<li><a href="CallOperationAction.html#getTarget()"><code>CallOperationAction.getTarget()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="target" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_callOperationActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.CallOperationAction)">
<h3>set_callOperationActionOfTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_callOperationActionOfTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="CallOperationAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallOperationAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_callOperationActionOfTarget()"><code><em>call Operation Action Of Target</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>call Operation Action Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_callOperationActionOfTarget()"><code>get_callOperationActionOfTarget()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_addStructuralFeatureValueActionOfInsertAt()">
<h3>get_addStructuralFeatureValueActionOfInsertAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a></span> <span class="element-name">get_addStructuralFeatureValueActionOfInsertAt</span>()</div>
<div class="block">Returns the value of the '<em><b>add Structural Feature Value Action Of Insert At</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdintermediateactions/AddStructuralFeatureValueAction.html#getInsertAt()"><code><em>Insert At</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>add Structural Feature Value Action Of Insert At</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>add Structural Feature Value Action Of Insert At</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_addStructuralFeatureValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction)"><code>set_addStructuralFeatureValueActionOfInsertAt(AddStructuralFeatureValueAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__addStructuralFeatureValueActionOfInsertAt()"><code>UMLPackage.getInputPin__addStructuralFeatureValueActionOfInsertAt()</code></a></li>
<li><a href="../mdintermediateactions/AddStructuralFeatureValueAction.html#getInsertAt()"><code>AddStructuralFeatureValueAction.getInsertAt()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="insertAt" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_addStructuralFeatureValueActionOfInsertAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.AddStructuralFeatureValueAction)">
<h3>set_addStructuralFeatureValueActionOfInsertAt</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_addStructuralFeatureValueActionOfInsertAt</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/AddStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">AddStructuralFeatureValueAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_addStructuralFeatureValueActionOfInsertAt()"><code><em>add Structural
 Feature Value Action Of Insert At</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>add Structural Feature Value Action Of Insert At</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_addStructuralFeatureValueActionOfInsertAt()"><code>get_addStructuralFeatureValueActionOfInsertAt()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_removeVariableValueActionOfRemoveAt()">
<h3>get_removeVariableValueActionOfRemoveAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a></span> <span class="element-name">get_removeVariableValueActionOfRemoveAt</span>()</div>
<div class="block">Returns the value of the '<em><b>remove Variable Value Action Of Remove At</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdstructuredactions/RemoveVariableValueAction.html#getRemoveAt()"><code><em>Remove At</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>remove Variable Value Action Of Remove At</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>remove Variable Value Action Of Remove At</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_removeVariableValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction)"><code>set_removeVariableValueActionOfRemoveAt(RemoveVariableValueAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__removeVariableValueActionOfRemoveAt()"><code>UMLPackage.getInputPin__removeVariableValueActionOfRemoveAt()</code></a></li>
<li><a href="../mdstructuredactions/RemoveVariableValueAction.html#getRemoveAt()"><code>RemoveVariableValueAction.getRemoveAt()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="removeAt" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_removeVariableValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions.RemoveVariableValueAction)">
<h3>set_removeVariableValueActionOfRemoveAt</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_removeVariableValueActionOfRemoveAt</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdstructuredactions/RemoveVariableValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdstructuredactions">RemoveVariableValueAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_removeVariableValueActionOfRemoveAt()"><code><em>remove Variable Value
 Action Of Remove At</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>remove Variable Value Action Of Remove At</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_removeVariableValueActionOfRemoveAt()"><code>get_removeVariableValueActionOfRemoveAt()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_destroyObjectActionOfTarget()">
<h3>get_destroyObjectActionOfTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a></span> <span class="element-name">get_destroyObjectActionOfTarget</span>()</div>
<div class="block">Returns the value of the '<em><b>destroy Object Action Of Target</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="../mdintermediateactions/DestroyObjectAction.html#getTarget()"><code><em>Target</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>destroy Object Action Of Target</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>destroy Object Action Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_destroyObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction)"><code>set_destroyObjectActionOfTarget(DestroyObjectAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__destroyObjectActionOfTarget()"><code>UMLPackage.getInputPin__destroyObjectActionOfTarget()</code></a></li>
<li><a href="../mdintermediateactions/DestroyObjectAction.html#getTarget()"><code>DestroyObjectAction.getTarget()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="target" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_destroyObjectActionOfTarget(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.DestroyObjectAction)">
<h3>set_destroyObjectActionOfTarget</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_destroyObjectActionOfTarget</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/DestroyObjectAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">DestroyObjectAction</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_destroyObjectActionOfTarget()"><code><em>destroy Object Action Of Target</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>destroy Object Action Of Target</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_destroyObjectActionOfTarget()"><code>get_destroyObjectActionOfTarget()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_removeStructuralFeatureValueActionOfRemoveAt()">
<h3>get_removeStructuralFeatureValueActionOfRemoveAt</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a></span> <span class="element-name">get_removeStructuralFeatureValueActionOfRemoveAt</span>()</div>
<div class="block">Returns the value of the '<em><b>remove Structural Feature Value Action Of Remove At</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="../mdintermediateactions/RemoveStructuralFeatureValueAction.html#getRemoveAt()"><code><em>Remove At</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>remove Structural Feature Value Action Of Remove At</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>remove Structural Feature Value Action Of Remove At</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_removeStructuralFeatureValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction)"><code>set_removeStructuralFeatureValueActionOfRemoveAt(RemoveStructuralFeatureValueAction)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getInputPin__removeStructuralFeatureValueActionOfRemoveAt()"><code>UMLPackage.getInputPin__removeStructuralFeatureValueActionOfRemoveAt()</code></a></li>
<li><a href="../mdintermediateactions/RemoveStructuralFeatureValueAction.html#getRemoveAt()"><code>RemoveStructuralFeatureValueAction.getRemoveAt()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="removeAt" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_removeStructuralFeatureValueActionOfRemoveAt(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.RemoveStructuralFeatureValueAction)">
<h3>set_removeStructuralFeatureValueActionOfRemoveAt</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_removeStructuralFeatureValueActionOfRemoveAt</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../mdintermediateactions/RemoveStructuralFeatureValueAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions">RemoveStructuralFeatureValueAction</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_removeStructuralFeatureValueActionOfRemoveAt()"><code><em>remove
 Structural Feature Value Action Of Remove At</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>remove Structural Feature Value Action Of Remove At</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_removeStructuralFeatureValueActionOfRemoveAt()"><code>get_removeStructuralFeatureValueActionOfRemoveAt()</code></a></li>
</ul>
</dd>
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
