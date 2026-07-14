# JAVA OPENAPI: LiteralUnlimitedNatural (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/LiteralUnlimitedNatural.html`
- source_sha256: `488e7e7cf814f8363c7513613314360bd0f44d9baf456a122153831aa26a23aa`
- captured_utc: `2026-07-14T16:46:29.287190+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface LiteralUnlimitedNatural

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[LiteralSpecification](LiteralSpecification.html)`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `[NamedElement](NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[PackageableElement](PackageableElement.html)`, `[ParameterableElement](../../auxiliaryconstructs/mdtemplates/ParameterableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[TypedElement](TypedElement.html)`, `[ValueSpecification](ValueSpecification.html)`

public interfaceLiteralUnlimitedNaturalextends [LiteralSpecification](LiteralSpecification.html)

begin-user-doc 
 A representation of the model object '***Literal Unlimited Natural***'.
 end-user-doc 
begin-model-doc 
 A LiteralUnlimitedNatural is a specification of an UnlimitedNatural number.
 end-model-doc 
The following features are supported:
 [`*Value*`](#getValue())

See Also:
[`UMLPackage.getLiteralUnlimitedNatural()`](../../metadata/UMLPackage.html#getLiteralUnlimitedNatural())
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`int`
`[getValue](#getValue())()`
Returns the value of the '***Value***' attribute.
`void`
`[setValue](#setValue(int))(int value)`
Sets the value of the '[`*Value*`](#getValue())' attribute.
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[ValueSpecification](ValueSpecification.html)
`[get_activityEdgeOfGuard](ValueSpecification.html#get_activityEdgeOfGuard()), [get_activityEdgeOfWeight](ValueSpecification.html#get_activityEdgeOfWeight()), [get_changeEventOfChangeExpression](ValueSpecification.html#get_changeEventOfChangeExpression()), [get_durationOfExpr](ValueSpecification.html#get_durationOfExpr()), [get_interactionConstraintOfMaxint](ValueSpecification.html#get_interactionConstraintOfMaxint()), [get_interactionConstraintOfMinint](ValueSpecification.html#get_interactionConstraintOfMinint()), [get_interactionUseOfArgument](ValueSpecification.html#get_interactionUseOfArgument()), [get_interactionUseOfReturnValue](ValueSpecification.html#get_interactionUseOfReturnValue()), [get_intervalOfMax](ValueSpecification.html#get_intervalOfMax()), [get_intervalOfMin](ValueSpecification.html#get_intervalOfMin()), [get_joinNodeOfJoinSpec](ValueSpecification.html#get_joinNodeOfJoinSpec()), [get_lifelineOfSelector](ValueSpecification.html#get_lifelineOfSelector()), [get_messageOfArgument](ValueSpecification.html#get_messageOfArgument()), [get_messageOfTarget](ValueSpecification.html#get_messageOfTarget()), [get_objectNodeOfUpperBound](ValueSpecification.html#get_objectNodeOfUpperBound()), [get_timeExpressionOfExpr](ValueSpecification.html#get_timeExpressionOfExpr()), [get_valuePinOfValue](ValueSpecification.html#get_valuePinOfValue()), [get_valueSpecificationActionOfValue](ValueSpecification.html#get_valueSpecificationActionOfValue()), [getExpression](ValueSpecification.html#getExpression()), [getOwningConstraint](ValueSpecification.html#getOwningConstraint()), [getOwningInstanceSpec](ValueSpecification.html#getOwningInstanceSpec()), [getOwningLower](ValueSpecification.html#getOwningLower()), [getOwningParameter](ValueSpecification.html#getOwningParameter()), [getOwningProperty](ValueSpecification.html#getOwningProperty()), [getOwningSlot](ValueSpecification.html#getOwningSlot()), [getOwningUpper](ValueSpecification.html#getOwningUpper()), [has_intervalOfMax](ValueSpecification.html#has_intervalOfMax()), [has_intervalOfMin](ValueSpecification.html#has_intervalOfMin()), [set_activityEdgeOfGuard](ValueSpecification.html#set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)), [set_activityEdgeOfWeight](ValueSpecification.html#set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)), [set_changeEventOfChangeExpression](ValueSpecification.html#set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)), [set_durationOfExpr](ValueSpecification.html#set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)), [set_interactionConstraintOfMaxint](ValueSpecification.html#set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)), [set_interactionConstraintOfMinint](ValueSpecification.html#set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)), [set_interactionUseOfArgument](ValueSpecification.html#set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)), [set_interactionUseOfReturnValue](ValueSpecification.html#set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)), [set_joinNodeOfJoinSpec](ValueSpecification.html#set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)), [set_lifelineOfSelector](ValueSpecification.html#set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)), [set_messageOfArgument](ValueSpecification.html#set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)), [set_messageOfTarget](ValueSpecification.html#set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)), [set_objectNodeOfUpperBound](ValueSpecification.html#set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)), [set_timeExpressionOfExpr](ValueSpecification.html#set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)), [set_valuePinOfValue](ValueSpecification.html#set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)), [set_valueSpecificationActionOfValue](ValueSpecification.html#set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)), [setExpression](ValueSpecification.html#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)), [setOwningConstraint](ValueSpecification.html#setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)), [setOwningInstanceSpec](ValueSpecification.html#setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)), [setOwningLower](ValueSpecification.html#setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)), [setOwningParameter](ValueSpecification.html#setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)), [setOwningProperty](ValueSpecification.html#setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)), [setOwningSlot](ValueSpecification.html#setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)), [setOwningUpper](ValueSpecification.html#setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement))`

============ METHOD DETAIL ========== 
Method Details
getValue
int getValue()
Returns the value of the '***Value***' attribute.
 The default value is `"0"`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The specified UnlimitedNatural value.
 end-model-doc
Returns:
the value of the '*Value*' attribute.
See Also:
[`setValue(int)`](#setValue(int))
[`UMLPackage.getLiteralUnlimitedNatural_Value()`](../../metadata/UMLPackage.html#getLiteralUnlimitedNatural_Value())
Model:
default="0" dataType="com.nomagic.uml2.ext.magicdraw.UnlimitedNatural" required="true" ordered="false"
Generated:
setValue
void setValue(int value)
Sets the value of the '[`*Value*`](#getValue())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Value*' attribute.
See Also:
[`getValue()`](#getValue())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface LiteralUnlimitedNatural">Interface LiteralUnlimitedNatural</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a></code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../auxiliaryconstructs/mdtemplates/ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a></code>, <code><a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">LiteralUnlimitedNatural</span><span class="extends-implements">
extends <a href="LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Literal Unlimited Natural</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A LiteralUnlimitedNatural is a specification of an UnlimitedNatural number.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getValue()"><code><em>Value</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getLiteralUnlimitedNatural()"><code>UMLPackage.getLiteralUnlimitedNatural()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Value</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setValue(int)">setValue</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getValue()"><code><em>Value</em></code></a>' attribute.</div>
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
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></h3>
<code><a href="ValueSpecification.html#get_activityEdgeOfGuard()">get_activityEdgeOfGuard</a>, <a href="ValueSpecification.html#get_activityEdgeOfWeight()">get_activityEdgeOfWeight</a>, <a href="ValueSpecification.html#get_changeEventOfChangeExpression()">get_changeEventOfChangeExpression</a>, <a href="ValueSpecification.html#get_durationOfExpr()">get_durationOfExpr</a>, <a href="ValueSpecification.html#get_interactionConstraintOfMaxint()">get_interactionConstraintOfMaxint</a>, <a href="ValueSpecification.html#get_interactionConstraintOfMinint()">get_interactionConstraintOfMinint</a>, <a href="ValueSpecification.html#get_interactionUseOfArgument()">get_interactionUseOfArgument</a>, <a href="ValueSpecification.html#get_interactionUseOfReturnValue()">get_interactionUseOfReturnValue</a>, <a href="ValueSpecification.html#get_intervalOfMax()">get_intervalOfMax</a>, <a href="ValueSpecification.html#get_intervalOfMin()">get_intervalOfMin</a>, <a href="ValueSpecification.html#get_joinNodeOfJoinSpec()">get_joinNodeOfJoinSpec</a>, <a href="ValueSpecification.html#get_lifelineOfSelector()">get_lifelineOfSelector</a>, <a href="ValueSpecification.html#get_messageOfArgument()">get_messageOfArgument</a>, <a href="ValueSpecification.html#get_messageOfTarget()">get_messageOfTarget</a>, <a href="ValueSpecification.html#get_objectNodeOfUpperBound()">get_objectNodeOfUpperBound</a>, <a href="ValueSpecification.html#get_timeExpressionOfExpr()">get_timeExpressionOfExpr</a>, <a href="ValueSpecification.html#get_valuePinOfValue()">get_valuePinOfValue</a>, <a href="ValueSpecification.html#get_valueSpecificationActionOfValue()">get_valueSpecificationActionOfValue</a>, <a href="ValueSpecification.html#getExpression()">getExpression</a>, <a href="ValueSpecification.html#getOwningConstraint()">getOwningConstraint</a>, <a href="ValueSpecification.html#getOwningInstanceSpec()">getOwningInstanceSpec</a>, <a href="ValueSpecification.html#getOwningLower()">getOwningLower</a>, <a href="ValueSpecification.html#getOwningParameter()">getOwningParameter</a>, <a href="ValueSpecification.html#getOwningProperty()">getOwningProperty</a>, <a href="ValueSpecification.html#getOwningSlot()">getOwningSlot</a>, <a href="ValueSpecification.html#getOwningUpper()">getOwningUpper</a>, <a href="ValueSpecification.html#has_intervalOfMax()">has_intervalOfMax</a>, <a href="ValueSpecification.html#has_intervalOfMin()">has_intervalOfMin</a>, <a href="ValueSpecification.html#set_activityEdgeOfGuard(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">set_activityEdgeOfGuard</a>, <a href="ValueSpecification.html#set_activityEdgeOfWeight(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ActivityEdge)">set_activityEdgeOfWeight</a>, <a href="ValueSpecification.html#set_changeEventOfChangeExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.ChangeEvent)">set_changeEventOfChangeExpression</a>, <a href="ValueSpecification.html#set_durationOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.Duration)">set_durationOfExpr</a>, <a href="ValueSpecification.html#set_interactionConstraintOfMaxint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">set_interactionConstraintOfMaxint</a>, <a href="ValueSpecification.html#set_interactionConstraintOfMinint(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionConstraint)">set_interactionConstraintOfMinint</a>, <a href="ValueSpecification.html#set_interactionUseOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">set_interactionUseOfArgument</a>, <a href="ValueSpecification.html#set_interactionUseOfReturnValue(com.nomagic.uml2.ext.magicdraw.interactions.mdfragments.InteractionUse)">set_interactionUseOfReturnValue</a>, <a href="ValueSpecification.html#set_joinNodeOfJoinSpec(com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities.JoinNode)">set_joinNodeOfJoinSpec</a>, <a href="ValueSpecification.html#set_lifelineOfSelector(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Lifeline)">set_lifelineOfSelector</a>, <a href="ValueSpecification.html#set_messageOfArgument(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfArgument</a>, <a href="ValueSpecification.html#set_messageOfTarget(com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions.Message)">set_messageOfTarget</a>, <a href="ValueSpecification.html#set_objectNodeOfUpperBound(com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities.ObjectNode)">set_objectNodeOfUpperBound</a>, <a href="ValueSpecification.html#set_timeExpressionOfExpr(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime.TimeExpression)">set_timeExpressionOfExpr</a>, <a href="ValueSpecification.html#set_valuePinOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions.ValuePin)">set_valuePinOfValue</a>, <a href="ValueSpecification.html#set_valueSpecificationActionOfValue(com.nomagic.uml2.ext.magicdraw.actions.mdintermediateactions.ValueSpecificationAction)">set_valueSpecificationActionOfValue</a>, <a href="ValueSpecification.html#setExpression(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Expression)">setExpression</a>, <a href="ValueSpecification.html#setOwningConstraint(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">setOwningConstraint</a>, <a href="ValueSpecification.html#setOwningInstanceSpec(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.InstanceSpecification)">setOwningInstanceSpec</a>, <a href="ValueSpecification.html#setOwningLower(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setOwningLower</a>, <a href="ValueSpecification.html#setOwningParameter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter)">setOwningParameter</a>, <a href="ValueSpecification.html#setOwningProperty(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">setOwningProperty</a>, <a href="ValueSpecification.html#setOwningSlot(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Slot)">setOwningSlot</a>, <a href="ValueSpecification.html#setOwningUpper(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement)">setOwningUpper</a></code></div>
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
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getValue</span>()</div>
<div class="block">Returns the value of the '<em><b>Value</b></em>' attribute.
 The default value is <code>"0"</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The specified UnlimitedNatural value.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Value</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setValue(int)"><code>setValue(int)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getLiteralUnlimitedNatural_Value()"><code>UMLPackage.getLiteralUnlimitedNatural_Value()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="0" dataType="com.nomagic.uml2.ext.magicdraw.UnlimitedNatural" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(int)">
<h3>setValue</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Sets the value of the '<a href="#getValue()"><code><em>Value</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Value</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getValue()"><code>getValue()</code></a></li>
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
