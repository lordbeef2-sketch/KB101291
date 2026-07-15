# JAVA OPENAPI: TimeInterval (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html
- source_path: `com/nomagic/uml2/ext/magicdraw/commonbehaviors/mdsimpletime/TimeInterval.html`
- source_sha256: `0ef33c0c2b04c5303208fc8ab5b7da940934817f95f54d6c5299866a7ee544de`
- captured_utc: `2026-07-14T16:53:06.419565+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime](package-summary.html)

## Interface TimeInterval

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[Interval](Interval.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](../../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](../../classes/mdkernel/PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TypedElement](../../classes/mdkernel/TypedElement.html)`, `[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)`

public interfaceTimeIntervalextends [Interval](Interval.html)

begin-user-doc 
 A representation of the model object '***Time Interval***'.
 end-user-doc 
begin-model-doc 
 A TimeInterval defines the range between two TimeExpressions.
 end-model-doc 
The following features are supported:
 [`*time Constraint Of Specification*`](#get_timeConstraintOfSpecification())

See Also:
[`UMLPackage.getTimeInterval()`](../../metadata/UMLPackage.html#getTimeInterval())
Model:
annotation="MOF package='commonbehaviors.mdsimpletime'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[TimeConstraint](TimeConstraint.html)`
`[get_timeConstraintOfSpecification](#get_timeConstraintOfSpecification())()`
Returns the value of the '***time Constraint Of Specification***' container reference.
`[TimeExpression](TimeExpression.html)`
`[getMax](#getMax())()`
Returns the value of the '***Max***' reference.
`[TimeExpression](TimeExpression.html)`
`[getMin](#getMin())()`
Returns the value of the '***Min***' reference.
`void`
`[set_timeConstraintOfSpecification](#set_timeConstraintOfSpecification(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint))([TimeConstraint](TimeConstraint.html) value)`
Sets the value of the '[`*time Constraint Of
 Specification*`](#get_timeConstraintOfSpecification())' container reference.
`void`
`[setMax](#setMax(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression))([TimeExpression](TimeExpression.html) value)`
Sets the value of the '[`*Max*`](#getMax())' reference.
`void`
`[setMin](#setMin(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression))([TimeExpression](TimeExpression.html) value)`
Sets the value of the '[`*Min*`](#getMin())' reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.[Interval](Interval.html)
`[get_intervalConstraintOfSpecification](Interval.html#get_intervalConstraintOfSpecification()), [set_intervalConstraintOfSpecification](Interval.html#set_intervalConstraintOfSpecification(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint)), [setMax](Interval.html#setMax(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)), [setMin](Interval.html#setMin(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification))`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../../base/ModelObject.html)
`[get_representationText](../../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../../classes/mdkernel/NamedElement.html#getSupplierDependency()), [has_considerIgnoreFragmentOfMessage](../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[PackageableElement](../../classes/mdkernel/PackageableElement.html)
`[get_componentOfPackagedElement](../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()), [get_elementImportOfImportedElement](../../classes/mdkernel/PackageableElement.html#get_elementImportOfImportedElement()), [get_manifestationOfUtilizedElement](../../classes/mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()), [getOwningPackage](../../classes/mdkernel/PackageableElement.html#getOwningPackage()), [getVisibility](../../classes/mdkernel/PackageableElement.html#getVisibility()), [has_elementImportOfImportedElement](../../classes/mdkernel/PackageableElement.html#has_elementImportOfImportedElement()), [has_manifestationOfUtilizedElement](../../classes/mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()), [set_componentOfPackagedElement](../../classes/mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)), [setOwningPackage](../../classes/mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)), [setVisibility](../../classes/mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)
`[get_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfDefault()), [get_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterOfOwnedDefault()), [get_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfActual()), [get_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()), [getOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getOwningTemplateParameter()), [getTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#getTemplateParameter()), [has_templateParameterOfDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterOfDefault()), [has_templateParameterSubstitutionOfActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#has_templateParameterSubstitutionOfActual()), [set_templateParameterOfOwnedDefault](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [set_templateParameterSubstitutionOfOwnedActual](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)), [setOwningTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)), [setTemplateParameter](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[TypedElement](../../classes/mdkernel/TypedElement.html)
`[getType](../../classes/mdkernel/TypedElement.html#getType()), [setType](../../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)
`[get_activityEdgeOfGuard](../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfGuard()), [get_activityEdgeOfWeight](../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfWeight()), [get_changeEventOfChangeExpression](../../classes/mdkernel/ValueSpecification.html#get_changeEventOfChangeExpression()), [get_durationOfExpr](../../classes/mdkernel/ValueSpecification.html#get_durationOfExpr()), [get_interactionConstraintOfMaxint](../../classes/mdkernel/ValueSpecification.html#get_interactionConstraintOfMaxint()), [get_interactionConstraintOfMinint](../../classes/mdkernel/ValueSpecification.html#get_interactionConstraintOfMinint()), [get_interactionUseOfArgument](../../classes/mdkernel/ValueSpecification.html#get_interactionUseOfArgument()), [get_interactionUseOfReturnValue](../../classes/mdkernel/ValueSpecification.html#get_interactionUseOfReturnValue()), [get_intervalOfMax](../../classes/mdkernel/ValueSpecification.html#get_intervalOfMax()), [get_intervalOfMin](../../classes/mdkernel/ValueSpecification.html#get_intervalOfMin()), [get_joinNodeOfJoinSpec](../../classes/mdkernel/ValueSpecification.html#get_joinNodeOfJoinSpec()), [get_lifelineOfSelector](../../classes/mdkernel/ValueSpecification.html#get_lifelineOfSelector()), [get_messageOfArgument](../../classes/mdkernel/ValueSpecification.html#get_messageOfArgument()), [get_messageOfTarget](../../classes/mdkernel/ValueSpecification.html#get_messageOfTarget()), [get_objectNodeOfUpperBound](../../classes/mdkernel/ValueSpecification.html#get_objectNodeOfUpperBound()), [get_timeExpressionOfExpr](../../classes/mdkernel/ValueSpecification.html#get_timeExpressionOfExpr()), [get_valuePinOfValue](../../classes/mdkernel/ValueSpecification.html#get_valuePinOfValue()), [get_valueSpecificationActionOfValue](../../classes/mdkernel/ValueSpecification.html#get_valueSpecificationActionOfValue()), [getExpression](../../classes/mdkernel/ValueSpecification.html#getExpression()), [getOwningConstraint](../../classes/mdkernel/ValueSpecification.html#getOwningConstraint()), [getOwningInstanceSpec](../../classes/mdkernel/ValueSpecification.html#getOwningInstanceSpec()), [getOwningLower](../../classes/mdkernel/ValueSpecification.html#getOwningLower()), [getOwningParameter](../../classes/mdkernel/ValueSpecification.html#getOwningParameter()), [getOwningProperty](../../classes/mdkernel/ValueSpecification.html#getOwningProperty()), [getOwningSlot](../../classes/mdkernel/ValueSpecification.html#getOwningSlot()), [getOwningUpper](../../classes/mdkernel/ValueSpecification.html#getOwningUpper()), [has_intervalOfMax](../../classes/mdkernel/ValueSpecification.html#has_intervalOfMax()), [has_intervalOfMin](../../classes/mdkernel/ValueSpecification.html#has_intervalOfMin()), [set_activityEdgeOfGuard](../../classes/mdkernel/ValueSpecification.html#set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)), [set_activityEdgeOfWeight](../../classes/mdkernel/ValueSpecification.html#set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)), [set_changeEventOfChangeExpression](../../classes/mdkernel/ValueSpecification.html#set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)), [set_durationOfExpr](../../classes/mdkernel/ValueSpecification.html#set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)), [set_interactionConstraintOfMaxint](../../classes/mdkernel/ValueSpecification.html#set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)), [set_interactionConstraintOfMinint](../../classes/mdkernel/ValueSpecification.html#set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)), [set_interactionUseOfArgument](../../classes/mdkernel/ValueSpecification.html#set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)), [set_interactionUseOfReturnValue](../../classes/mdkernel/ValueSpecification.html#set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)), [set_joinNodeOfJoinSpec](../../classes/mdkernel/ValueSpecification.html#set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)), [set_lifelineOfSelector](../../classes/mdkernel/ValueSpecification.html#set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)), [set_messageOfArgument](../../classes/mdkernel/ValueSpecification.html#set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)), [set_messageOfTarget](../../classes/mdkernel/ValueSpecification.html#set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)), [set_objectNodeOfUpperBound](../../classes/mdkernel/ValueSpecification.html#set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)), [set_timeExpressionOfExpr](../../classes/mdkernel/ValueSpecification.html#set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)), [set_valuePinOfValue](../../classes/mdkernel/ValueSpecification.html#set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)), [set_valueSpecificationActionOfValue](../../classes/mdkernel/ValueSpecification.html#set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)), [setExpression](../../classes/mdkernel/ValueSpecification.html#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)), [setOwningConstraint](../../classes/mdkernel/ValueSpecification.html#setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)), [setOwningInstanceSpec](../../classes/mdkernel/ValueSpecification.html#setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)), [setOwningLower](../../classes/mdkernel/ValueSpecification.html#setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [setOwningParameter](../../classes/mdkernel/ValueSpecification.html#setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)), [setOwningProperty](../../classes/mdkernel/ValueSpecification.html#setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [setOwningSlot](../../classes/mdkernel/ValueSpecification.html#setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)), [setOwningUpper](../../classes/mdkernel/ValueSpecification.html#setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))`

============ METHOD DETAIL ========== 
Method Details
get_timeConstraintOfSpecification
@CheckForNull[TimeConstraint](TimeConstraint.html) get_timeConstraintOfSpecification()
Returns the value of the '***time Constraint Of Specification***' container reference.
 It is bidirectional and its opposite is
 '[`*Specification*`](TimeConstraint.html#getSpecification())'.
 begin-user-doc 
If the meaning of the '*time Constraint Of Specification*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*time Constraint Of Specification*' container reference.
See Also:
[`set_timeConstraintOfSpecification(TimeConstraint)`](#set_timeConstraintOfSpecification(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint))
[`UMLPackage.getTimeInterval__timeConstraintOfSpecification()`](../../metadata/UMLPackage.html#getTimeInterval__timeConstraintOfSpecification())
[`TimeConstraint.getSpecification()`](TimeConstraint.html#getSpecification())
Model:
opposite="specification" volatile="true" ordered="false"
Generated:
set_timeConstraintOfSpecification
void set_timeConstraintOfSpecification(@CheckForNull
 [TimeConstraint](TimeConstraint.html) value)
Sets the value of the '[`*time Constraint Of
 Specification*`](#get_timeConstraintOfSpecification())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*time Constraint Of Specification*' container reference.
See Also:
[`get_timeConstraintOfSpecification()`](#get_timeConstraintOfSpecification())
Generated:
getMin
@CheckForNull[TimeExpression](TimeExpression.html) getMin()
Returns the value of the '***Min***' reference.
 It is bidirectional and its opposite is
 '[`*time Interval Of Min*`](TimeExpression.html#get_timeIntervalOfMin())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Refers to the TimeExpression denoting the minimum value of the range.
 end-model-doc
Specified by:
`[getMin](Interval.html#getMin())` in interface `[Interval](Interval.html)`
Returns:
the value of the '*Min*' reference.
See Also:
[`setMin(TimeExpression)`](#setMin(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression))
[`UMLPackage.getTimeInterval_Min()`](../../metadata/UMLPackage.html#getTimeInterval_Min())
[`TimeExpression.get_timeIntervalOfMin()`](TimeExpression.html#get_timeIntervalOfMin())
Model:
opposite="_timeIntervalOfMin" required="true" ordered="false"
Generated:
setMin
void setMin(@CheckForNull
 [TimeExpression](TimeExpression.html) value)
Sets the value of the '[`*Min*`](#getMin())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Min*' reference.
See Also:
[`getMin()`](#getMin())
Generated:
getMax
@CheckForNull[TimeExpression](TimeExpression.html) getMax()
Returns the value of the '***Max***' reference.
 It is bidirectional and its opposite is
 '[`*time Interval Of Max*`](TimeExpression.html#get_timeIntervalOfMax())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Refers to the TimeExpression denoting the maximum value of the range.
 end-model-doc
Specified by:
`[getMax](Interval.html#getMax())` in interface `[Interval](Interval.html)`
Returns:
the value of the '*Max*' reference.
See Also:
[`setMax(TimeExpression)`](#setMax(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression))
[`UMLPackage.getTimeInterval_Max()`](../../metadata/UMLPackage.html#getTimeInterval_Max())
[`TimeExpression.get_timeIntervalOfMax()`](TimeExpression.html#get_timeIntervalOfMax())
Model:
opposite="_timeIntervalOfMax" required="true" ordered="false"
Generated:
setMax
void setMax(@CheckForNull
 [TimeExpression](TimeExpression.html) value)
Sets the value of the '[`*Max*`](#getMax())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Max*' reference.
See Also:
[`getMax()`](#getMax())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime</a></div>
<h1 class="title" title="Interface TimeInterval">Interface TimeInterval</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code>, <code><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TimeInterval</span><span class="extends-implements">
extends <a href="Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Time Interval</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A TimeInterval defines the range between two TimeExpressions.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#get_timeConstraintOfSpecification()"><code><em>time Constraint Of Specification</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../metadata/UMLPackage.html#getTimeInterval()"><code>UMLPackage.getTimeInterval()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='commonbehaviors.mdsimpletime'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_timeConstraintOfSpecification()">get_timeConstraintOfSpecification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>time Constraint Of Specification</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMax()">getMax</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Max</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMin()">getMin</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Min</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_timeConstraintOfSpecification(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint)">set_timeConstraintOfSpecification</a><wbr/>(<a href="TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_timeConstraintOfSpecification()"><code><em>time Constraint Of
 Specification</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMax(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">setMax</a><wbr/>(<a href="TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getMax()"><code><em>Max</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMin(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">setMin</a><wbr/>(<a href="TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getMin()"><code><em>Min</em></code></a>' reference.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Interval">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.<a href="Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></h3>
<code><a href="Interval.html#get_intervalConstraintOfSpecification()">get_intervalConstraintOfSpecification</a>, <a href="Interval.html#set_intervalConstraintOfSpecification(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.IntervalConstraint)">set_intervalConstraintOfSpecification</a>, <a href="Interval.html#setMax(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setMax</a>, <a href="Interval.html#setMin(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification)">setMin</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></h3>
<code><a href="../../classes/mdkernel/PackageableElement.html#get_componentOfPackagedElement()">get_componentOfPackagedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#get_elementImportOfImportedElement()">get_elementImportOfImportedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#get_manifestationOfUtilizedElement()">get_manifestationOfUtilizedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#getOwningPackage()">getOwningPackage</a>, <a href="../../classes/mdkernel/PackageableElement.html#getVisibility()">getVisibility</a>, <a href="../../classes/mdkernel/PackageableElement.html#has_elementImportOfImportedElement()">has_elementImportOfImportedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#has_manifestationOfUtilizedElement()">has_manifestationOfUtilizedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#set_componentOfPackagedElement(com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents.Component)">set_componentOfPackagedElement</a>, <a href="../../classes/mdkernel/PackageableElement.html#setOwningPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setOwningPackage</a>, <a href="../../classes/mdkernel/PackageableElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></h3>
<code><a href="../../classes/mdkernel/TypedElement.html#getType()">getType</a>, <a href="../../classes/mdkernel/TypedElement.html#setType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">setType</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></h3>
<code><a href="../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfGuard()">get_activityEdgeOfGuard</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_activityEdgeOfWeight()">get_activityEdgeOfWeight</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_changeEventOfChangeExpression()">get_changeEventOfChangeExpression</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_durationOfExpr()">get_durationOfExpr</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_interactionConstraintOfMaxint()">get_interactionConstraintOfMaxint</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_interactionConstraintOfMinint()">get_interactionConstraintOfMinint</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_interactionUseOfArgument()">get_interactionUseOfArgument</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_interactionUseOfReturnValue()">get_interactionUseOfReturnValue</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_intervalOfMax()">get_intervalOfMax</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_intervalOfMin()">get_intervalOfMin</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_joinNodeOfJoinSpec()">get_joinNodeOfJoinSpec</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_lifelineOfSelector()">get_lifelineOfSelector</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_messageOfArgument()">get_messageOfArgument</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_messageOfTarget()">get_messageOfTarget</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_objectNodeOfUpperBound()">get_objectNodeOfUpperBound</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_timeExpressionOfExpr()">get_timeExpressionOfExpr</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_valuePinOfValue()">get_valuePinOfValue</a>, <a href="../../classes/mdkernel/ValueSpecification.html#get_valueSpecificationActionOfValue()">get_valueSpecificationActionOfValue</a>, <a href="../../classes/mdkernel/ValueSpecification.html#getExpression()">getExpression</a>, <a href="../../classes/mdkernel/ValueSpecification.html#getOwningConstraint()">getOwningConstraint</a>, <a href="../../classes/mdkernel/ValueSpecification.html#getOwningInstanceSpec()">getOwningInstanceSpec</a>, <a href="../../classes/mdkernel/ValueSpecification.html#getOwningLower()">getOwningLower</a>, <a href="../../classes/mdkernel/ValueSpecification.html#getOwningParameter()">getOwningParameter</a>, <a href="../../classes/mdkernel/ValueSpecification.html#getOwningProperty()">getOwningProperty</a>, <a href="../../classes/mdkernel/ValueSpecification.html#getOwningSlot()">getOwningSlot</a>, <a href="../../classes/mdkernel/ValueSpecification.html#getOwningUpper()">getOwningUpper</a>, <a href="../../classes/mdkernel/ValueSpecification.html#has_intervalOfMax()">has_intervalOfMax</a>, <a href="../../classes/mdkernel/ValueSpecification.html#has_intervalOfMin()">has_intervalOfMin</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">set_activityEdgeOfGuard</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">set_activityEdgeOfWeight</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)">set_changeEventOfChangeExpression</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)">set_durationOfExpr</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">set_interactionConstraintOfMaxint</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">set_interactionConstraintOfMinint</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">set_interactionUseOfArgument</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">set_interactionUseOfReturnValue</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)">set_joinNodeOfJoinSpec</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">set_lifelineOfSelector</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfArgument</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfTarget</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)">set_objectNodeOfUpperBound</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">set_timeExpressionOfExpr</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)">set_valuePinOfValue</a>, <a href="../../classes/mdkernel/ValueSpecification.html#set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)">set_valueSpecificationActionOfValue</a>, <a href="../../classes/mdkernel/ValueSpecification.html#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)">setExpression</a>, <a href="../../classes/mdkernel/ValueSpecification.html#setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setOwningConstraint</a>, <a href="../../classes/mdkernel/ValueSpecification.html#setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">setOwningInstanceSpec</a>, <a href="../../classes/mdkernel/ValueSpecification.html#setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setOwningLower</a>, <a href="../../classes/mdkernel/ValueSpecification.html#setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">setOwningParameter</a>, <a href="../../classes/mdkernel/ValueSpecification.html#setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setOwningProperty</a>, <a href="../../classes/mdkernel/ValueSpecification.html#setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">setOwningSlot</a>, <a href="../../classes/mdkernel/ValueSpecification.html#setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setOwningUpper</a></code></div>
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
<section class="detail" id="get_timeConstraintOfSpecification()">
<h3>get_timeConstraintOfSpecification</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></span> <span class="element-name">get_timeConstraintOfSpecification</span>()</div>
<div class="block">Returns the value of the '<em><b>time Constraint Of Specification</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="TimeConstraint.html#getSpecification()"><code><em>Specification</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>time Constraint Of Specification</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>time Constraint Of Specification</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_timeConstraintOfSpecification(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint)"><code>set_timeConstraintOfSpecification(TimeConstraint)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTimeInterval__timeConstraintOfSpecification()"><code>UMLPackage.getTimeInterval__timeConstraintOfSpecification()</code></a></li>
<li><a href="TimeConstraint.html#getSpecification()"><code>TimeConstraint.getSpecification()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="specification" volatile="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_timeConstraintOfSpecification(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeConstraint)">
<h3>set_timeConstraintOfSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_timeConstraintOfSpecification</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_timeConstraintOfSpecification()"><code><em>time Constraint Of
 Specification</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>time Constraint Of Specification</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_timeConstraintOfSpecification()"><code>get_timeConstraintOfSpecification()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMin()">
<h3>getMin</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></span> <span class="element-name">getMin</span>()</div>
<div class="block">Returns the value of the '<em><b>Min</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="TimeExpression.html#get_timeIntervalOfMin()"><code><em>time Interval Of Min</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Refers to the TimeExpression denoting the minimum value of the range.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Interval.html#getMin()">getMin</a></code> in interface <code><a href="Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Min</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setMin(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)"><code>setMin(TimeExpression)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTimeInterval_Min()"><code>UMLPackage.getTimeInterval_Min()</code></a></li>
<li><a href="TimeExpression.html#get_timeIntervalOfMin()"><code>TimeExpression.get_timeIntervalOfMin()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_timeIntervalOfMin" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMin(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">
<h3>setMin</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMin</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getMin()"><code><em>Min</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Min</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getMin()"><code>getMin()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMax()">
<h3>getMax</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></span> <span class="element-name">getMax</span>()</div>
<div class="block">Returns the value of the '<em><b>Max</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="TimeExpression.html#get_timeIntervalOfMax()"><code><em>time Interval Of Max</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Refers to the TimeExpression denoting the maximum value of the range.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Interval.html#getMax()">getMax</a></code> in interface <code><a href="Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code></dd>
<dt>Returns:</dt>
<dd>the value of the '<em>Max</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setMax(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)"><code>setMax(TimeExpression)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTimeInterval_Max()"><code>UMLPackage.getTimeInterval_Max()</code></a></li>
<li><a href="TimeExpression.html#get_timeIntervalOfMax()"><code>TimeExpression.get_timeIntervalOfMax()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_timeIntervalOfMax" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMax(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">
<h3>setMax</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMax</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getMax()"><code><em>Max</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Max</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getMax()"><code>getMax()</code></a></li>
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
