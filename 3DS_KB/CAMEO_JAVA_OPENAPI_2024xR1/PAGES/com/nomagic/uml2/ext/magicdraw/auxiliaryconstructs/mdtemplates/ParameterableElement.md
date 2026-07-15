# JAVA OPENAPI: ParameterableElement (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html
- source_path: `com/nomagic/uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/ParameterableElement.html`
- source_sha256: `b2d55424756c325ba5b38f24bc6515074c942e88ae02c0e8ec2ab06426c34236`
- captured_utc: `2026-07-14T16:52:48.439363+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates](package-summary.html)

## Interface ParameterableElement

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[Abstraction](../../classes/mddependencies/Abstraction.html)`, `[Activity](../../activities/mdfundamentalactivities/Activity.html)`, `[Actor](../../mdusecases/Actor.html)`, `[AnyReceiveEvent](../../commonbehaviors/mdcommunications/AnyReceiveEvent.html)`, `[Artifact](../../deployments/mdartifacts/Artifact.html)`, `[Association](../../classes/mdkernel/Association.html)`, `[AssociationClass](../../classes/mdassociationclasses/AssociationClass.html)`, `[Behavior](../../commonbehaviors/mdbasicbehaviors/Behavior.html)`, `[BehavioredClassifier](../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html)`, `[CallEvent](../../commonbehaviors/mdcommunications/CallEvent.html)`, `[ChangeEvent](../../commonbehaviors/mdcommunications/ChangeEvent.html)`, `[Class](../../classes/mdkernel/Class.html)`, `[Classifier](../../classes/mdkernel/Classifier.html)`, `[Collaboration](../../compositestructures/mdcollaborations/Collaboration.html)`, `[CommunicationPath](../../deployments/mdnodes/CommunicationPath.html)`, `[Component](../../components/mdbasiccomponents/Component.html)`, `[ComponentRealization](../../components/mdbasiccomponents/ComponentRealization.html)`, `[ConnectableElement](../../compositestructures/mdinternalstructures/ConnectableElement.html)`, `[Constraint](../../classes/mdkernel/Constraint.html)`, `[DataType](../../classes/mdkernel/DataType.html)`, `[Dependency](../../classes/mddependencies/Dependency.html)`, `[Deployment](../../deployments/mdnodes/Deployment.html)`, `[DeploymentSpecification](../../deployments/mdcomponentdeployments/DeploymentSpecification.html)`, `[Device](../../deployments/mdnodes/Device.html)`, `[Duration](../../commonbehaviors/mdsimpletime/Duration.html)`, `[DurationConstraint](../../commonbehaviors/mdsimpletime/DurationConstraint.html)`, `[DurationInterval](../../commonbehaviors/mdsimpletime/DurationInterval.html)`, `[DurationObservation](../../commonbehaviors/mdsimpletime/DurationObservation.html)`, `[ElementValue](../../classes/mdkernel/ElementValue.html)`, `[EncapsulatedClassifier](../../compositestructures/mdports/EncapsulatedClassifier.html)`, `[Enumeration](../../classes/mdkernel/Enumeration.html)`, `[EnumerationLiteral](../../classes/mdkernel/EnumerationLiteral.html)`, `[Event](../../commonbehaviors/mdcommunications/Event.html)`, `[ExecutionEnvironment](../../deployments/mdnodes/ExecutionEnvironment.html)`, `[Expression](../../classes/mdkernel/Expression.html)`, `[Extension](../../mdprofiles/Extension.html)`, `[ExtensionEnd](../../mdprofiles/ExtensionEnd.html)`, `[FunctionBehavior](../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html)`, `[GeneralizationSet](../../classes/mdpowertypes/GeneralizationSet.html)`, `[InformationFlow](../mdinformationflows/InformationFlow.html)`, `[InformationItem](../mdinformationflows/InformationItem.html)`, `[InstanceSpecification](../../classes/mdkernel/InstanceSpecification.html)`, `[InstanceValue](../../classes/mdkernel/InstanceValue.html)`, `[Interaction](../../interactions/mdbasicinteractions/Interaction.html)`, `[InteractionConstraint](../../interactions/mdfragments/InteractionConstraint.html)`, `[Interface](../../classes/mdinterfaces/Interface.html)`, `[InterfaceRealization](../../classes/mdinterfaces/InterfaceRealization.html)`, `[Interval](../../commonbehaviors/mdsimpletime/Interval.html)`, `[IntervalConstraint](../../commonbehaviors/mdsimpletime/IntervalConstraint.html)`, `[LiteralBoolean](../../classes/mdkernel/LiteralBoolean.html)`, `[LiteralInteger](../../classes/mdkernel/LiteralInteger.html)`, `[LiteralNull](../../classes/mdkernel/LiteralNull.html)`, `[LiteralReal](../../classes/mdkernel/LiteralReal.html)`, `[LiteralSpecification](../../classes/mdkernel/LiteralSpecification.html)`, `[LiteralString](../../classes/mdkernel/LiteralString.html)`, `[LiteralUnlimitedNatural](../../classes/mdkernel/LiteralUnlimitedNatural.html)`, `[Manifestation](../../deployments/mdartifacts/Manifestation.html)`, `[MessageEvent](../../commonbehaviors/mdcommunications/MessageEvent.html)`, `[Model](../mdmodels/Model.html)`, `[Node](../../deployments/mdnodes/Node.html)`, `[Observation](../../commonbehaviors/mdsimpletime/Observation.html)`, `[OpaqueBehavior](../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html)`, `[OpaqueExpression](../../classes/mdkernel/OpaqueExpression.html)`, `[Operation](../../classes/mdkernel/Operation.html)`, `[Package](../../classes/mdkernel/Package.html)`, `[PackageableElement](../../classes/mdkernel/PackageableElement.html)`, `[Parameter](../../classes/mdkernel/Parameter.html)`, `[Port](../../compositestructures/mdports/Port.html)`, `[PrimitiveType](../../classes/mdkernel/PrimitiveType.html)`, `[Profile](../../mdprofiles/Profile.html)`, `[Property](../../classes/mdkernel/Property.html)`, `[ProtocolStateMachine](../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html)`, `[Realization](../../classes/mddependencies/Realization.html)`, `[Signal](../../commonbehaviors/mdcommunications/Signal.html)`, `[SignalEvent](../../commonbehaviors/mdcommunications/SignalEvent.html)`, `[StateMachine](../../statemachines/mdbehaviorstatemachines/StateMachine.html)`, `[Stereotype](../../mdprofiles/Stereotype.html)`, `[StringExpression](StringExpression.html)`, `[StructuredClassifier](../../compositestructures/mdinternalstructures/StructuredClassifier.html)`, `[Substitution](../../classes/mddependencies/Substitution.html)`, `[TimeConstraint](../../commonbehaviors/mdsimpletime/TimeConstraint.html)`, `[TimeEvent](../../commonbehaviors/mdcommunications/TimeEvent.html)`, `[TimeExpression](../../commonbehaviors/mdsimpletime/TimeExpression.html)`, `[TimeInterval](../../commonbehaviors/mdsimpletime/TimeInterval.html)`, `[TimeObservation](../../commonbehaviors/mdsimpletime/TimeObservation.html)`, `[Type](../../classes/mdkernel/Type.html)`, `[Usage](../../classes/mddependencies/Usage.html)`, `[UseCase](../../mdusecases/UseCase.html)`, `[ValueSpecification](../../classes/mdkernel/ValueSpecification.html)`, `[Variable](../../activities/mdstructuredactivities/Variable.html)`

public interfaceParameterableElementextends [Element](../../classes/mdkernel/Element.html)

begin-user-doc 
 A representation of the model object '***Parameterable Element***'.
 end-user-doc 
begin-model-doc 
 A ParameterableElement is an Element that can be exposed as a formal TemplateParameter for a template, or specified as an actual parameter in a binding of a template.
 end-model-doc 
The following features are supported:
 [`*Owning Template Parameter*`](#getOwningTemplateParameter())
[`*template Parameter Of Default*`](#get_templateParameterOfDefault())
[`*template Parameter Of Owned Default*`](#get_templateParameterOfOwnedDefault())
[`*Template Parameter*`](#getTemplateParameter())
[`*template Parameter Substitution Of Actual*`](#get_templateParameterSubstitutionOfActual())
[`*template Parameter
 Substitution Of Owned Actual*`](#get_templateParameterSubstitutionOfOwnedActual())

See Also:
[`UMLPackage.getParameterableElement()`](../../metadata/UMLPackage.html#getParameterableElement())
Model:
abstract="true"
 annotation="MOF package='auxiliaryconstructs.mdtemplates'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[TemplateParameter](TemplateParameter.html)>`
`[get_templateParameterOfDefault](#get_templateParameterOfDefault())()`
Returns the value of the '***template Parameter Of Default***' reference list.
`[TemplateParameter](TemplateParameter.html)`
`[get_templateParameterOfOwnedDefault](#get_templateParameterOfOwnedDefault())()`
Returns the value of the '***template Parameter Of Owned Default***' container reference.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[TemplateParameterSubstitution](TemplateParameterSubstitution.html)>`
`[get_templateParameterSubstitutionOfActual](#get_templateParameterSubstitutionOfActual())()`
Returns the value of the '***template Parameter Substitution Of Actual***' reference list.
`[TemplateParameterSubstitution](TemplateParameterSubstitution.html)`
`[get_templateParameterSubstitutionOfOwnedActual](#get_templateParameterSubstitutionOfOwnedActual())()`
Returns the value of the '***template Parameter Substitution Of Owned Actual***' container reference.
`[TemplateParameter](TemplateParameter.html)`
`[getOwningTemplateParameter](#getOwningTemplateParameter())()`
Returns the value of the '***Owning Template Parameter***' container reference.
`[TemplateParameter](TemplateParameter.html)`
`[getTemplateParameter](#getTemplateParameter())()`
Returns the value of the '***Template Parameter***' reference.
`boolean`
`[has_templateParameterOfDefault](#has_templateParameterOfDefault())()`

`boolean`
`[has_templateParameterSubstitutionOfActual](#has_templateParameterSubstitutionOfActual())()`

`void`
`[set_templateParameterOfOwnedDefault](#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))([TemplateParameter](TemplateParameter.html) value)`
Sets the value of the '[`*template Parameter Of Owned Default*`](#get_templateParameterOfOwnedDefault())' container reference.
`void`
`[set_templateParameterSubstitutionOfOwnedActual](#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution))([TemplateParameterSubstitution](TemplateParameterSubstitution.html) value)`
Sets the value of the '[`*template Parameter Substitution Of Owned Actual*`](#get_templateParameterSubstitutionOfOwnedActual())' container reference.
`void`
`[setOwningTemplateParameter](#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))([TemplateParameter](TemplateParameter.html) value)`
Sets the value of the '[`*Owning Template
 Parameter*`](#getOwningTemplateParameter())' container reference.
`void`
`[setTemplateParameter](#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))([TemplateParameter](TemplateParameter.html) value)`
Sets the value of the
 '[`*Template Parameter*`](#getTemplateParameter())' reference.
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
getTemplateParameter
@CheckForNull[TemplateParameter](TemplateParameter.html) getTemplateParameter()
Returns the value of the '***Template Parameter***' reference.
 It is bidirectional and its opposite is
 '[`*Parametered Element*`](TemplateParameter.html#getParameteredElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The TemplateParameter that exposes this ParameterableElement as a formal parameter.
 end-model-doc
Returns:
the value of the '*Template Parameter*' reference.
See Also:
[`setTemplateParameter(TemplateParameter)`](#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))
[`UMLPackage.getParameterableElement_TemplateParameter()`](../../metadata/UMLPackage.html#getParameterableElement_TemplateParameter())
[`TemplateParameter.getParameteredElement()`](TemplateParameter.html#getParameteredElement())
Model:
opposite="parameteredElement" ordered="false"
Generated:
setTemplateParameter
void setTemplateParameter(@CheckForNull
 [TemplateParameter](TemplateParameter.html) value)
Sets the value of the
 '[`*Template Parameter*`](#getTemplateParameter())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Template Parameter*' reference.
See Also:
[`getTemplateParameter()`](#getTemplateParameter())
Generated:
getOwningTemplateParameter
@CheckForNull[TemplateParameter](TemplateParameter.html) getOwningTemplateParameter()
Returns the value of the '***Owning Template Parameter***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Parametered Element*`](TemplateParameter.html#getOwnedParameteredElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The formal TemplateParameter that owns this ParameterableElement.
 end-model-doc
Returns:
the value of the '*Owning Template Parameter*' container reference.
See Also:
[`setOwningTemplateParameter(TemplateParameter)`](#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))
[`UMLPackage.getParameterableElement_OwningTemplateParameter()`](../../metadata/UMLPackage.html#getParameterableElement_OwningTemplateParameter())
[`TemplateParameter.getOwnedParameteredElement()`](TemplateParameter.html#getOwnedParameteredElement())
Model:
opposite="ownedParameteredElement" transient="false" ordered="false"
Generated:
setOwningTemplateParameter
void setOwningTemplateParameter(@CheckForNull
 [TemplateParameter](TemplateParameter.html) value)
Sets the value of the '[`*Owning Template
 Parameter*`](#getOwningTemplateParameter())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owning Template Parameter*' container reference.
See Also:
[`getOwningTemplateParameter()`](#getOwningTemplateParameter())
Generated:
get_templateParameterOfDefault
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[TemplateParameter](TemplateParameter.html)> get_templateParameterOfDefault()
Returns the value of the '***template Parameter Of Default***' reference list.
 The list contents are of type [`TemplateParameter`](TemplateParameter.html).
 It is bidirectional and its opposite is '[`*Default*`](TemplateParameter.html#getDefault())'.
 begin-user-doc 
If the meaning of the '*template Parameter Of Default*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*template Parameter Of Default*' reference list.
See Also:
[`UMLPackage.getParameterableElement__templateParameterOfDefault()`](../../metadata/UMLPackage.html#getParameterableElement__templateParameterOfDefault())
[`TemplateParameter.getDefault()`](TemplateParameter.html#getDefault())
Model:
opposite="default" ordered="false"
Generated:
get_templateParameterOfOwnedDefault
@CheckForNull[TemplateParameter](TemplateParameter.html) get_templateParameterOfOwnedDefault()
Returns the value of the '***template Parameter Of Owned Default***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Default*`](TemplateParameter.html#getOwnedDefault())'.
 begin-user-doc 
If the meaning of the '*template Parameter Of Owned Default*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*template Parameter Of Owned Default*' container reference.
See Also:
[`set_templateParameterOfOwnedDefault(TemplateParameter)`](#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))
[`UMLPackage.getParameterableElement__templateParameterOfOwnedDefault()`](../../metadata/UMLPackage.html#getParameterableElement__templateParameterOfOwnedDefault())
[`TemplateParameter.getOwnedDefault()`](TemplateParameter.html#getOwnedDefault())
Model:
opposite="ownedDefault" transient="false" ordered="false"
Generated:
set_templateParameterOfOwnedDefault
void set_templateParameterOfOwnedDefault(@CheckForNull
 [TemplateParameter](TemplateParameter.html) value)
Sets the value of the '[`*template Parameter Of Owned Default*`](#get_templateParameterOfOwnedDefault())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*template Parameter Of Owned Default*' container reference.
See Also:
[`get_templateParameterOfOwnedDefault()`](#get_templateParameterOfOwnedDefault())
Generated:
get_templateParameterSubstitutionOfActual
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[TemplateParameterSubstitution](TemplateParameterSubstitution.html)> get_templateParameterSubstitutionOfActual()
Returns the value of the '***template Parameter Substitution Of Actual***' reference list.
 The list contents are of type [`TemplateParameterSubstitution`](TemplateParameterSubstitution.html).
 It is bidirectional and its opposite is
 '[`*Actual*`](TemplateParameterSubstitution.html#getActual())'.
 begin-user-doc 
If the meaning of the '*template Parameter Substitution Of Actual*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*template Parameter Substitution Of Actual*' reference list.
See Also:
[`UMLPackage.getParameterableElement__templateParameterSubstitutionOfActual()`](../../metadata/UMLPackage.html#getParameterableElement__templateParameterSubstitutionOfActual())
[`TemplateParameterSubstitution.getActual()`](TemplateParameterSubstitution.html#getActual())
Model:
opposite="actual" ordered="false"
Generated:
get_templateParameterSubstitutionOfOwnedActual
@CheckForNull[TemplateParameterSubstitution](TemplateParameterSubstitution.html) get_templateParameterSubstitutionOfOwnedActual()
Returns the value of the '***template Parameter Substitution Of Owned Actual***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Actual*`](TemplateParameterSubstitution.html#getOwnedActual())'.
 begin-user-doc 
If the meaning of the '*template Parameter Substitution Of Owned Actual*' container reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*template Parameter Substitution Of Owned Actual*' container reference.
See Also:
[`set_templateParameterSubstitutionOfOwnedActual(TemplateParameterSubstitution)`](#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution))
[`UMLPackage.getParameterableElement__templateParameterSubstitutionOfOwnedActual()`](../../metadata/UMLPackage.html#getParameterableElement__templateParameterSubstitutionOfOwnedActual())
[`TemplateParameterSubstitution.getOwnedActual()`](TemplateParameterSubstitution.html#getOwnedActual())
Model:
opposite="ownedActual" transient="false" ordered="false"
Generated:
set_templateParameterSubstitutionOfOwnedActual
void set_templateParameterSubstitutionOfOwnedActual(@CheckForNull
 [TemplateParameterSubstitution](TemplateParameterSubstitution.html) value)
Sets the value of the '[`*template Parameter Substitution Of Owned Actual*`](#get_templateParameterSubstitutionOfOwnedActual())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*template Parameter Substitution Of Owned Actual*' container reference.
See Also:
[`get_templateParameterSubstitutionOfOwnedActual()`](#get_templateParameterSubstitutionOfOwnedActual())
Generated:
has_templateParameterOfDefault
boolean has_templateParameterOfDefault()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_templateParameterSubstitutionOfActual
boolean has_templateParameterSubstitutionOfActual()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates</a></div>
<h1 class="title" title="Interface ParameterableElement">Interface ParameterableElement</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../classes/mddependencies/Abstraction.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Abstraction</a></code>, <code><a href="../../activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code>, <code><a href="../../mdusecases/Actor.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Actor</a></code>, <code><a href="../../commonbehaviors/mdcommunications/AnyReceiveEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">AnyReceiveEvent</a></code>, <code><a href="../../deployments/mdartifacts/Artifact.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Artifact</a></code>, <code><a href="../../classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a></code>, <code><a href="../../classes/mdassociationclasses/AssociationClass.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdassociationclasses">AssociationClass</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/BehavioredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">BehavioredClassifier</a></code>, <code><a href="../../commonbehaviors/mdcommunications/CallEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">CallEvent</a></code>, <code><a href="../../commonbehaviors/mdcommunications/ChangeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">ChangeEvent</a></code>, <code><a href="../../classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code>, <code><a href="../../classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code>, <code><a href="../../compositestructures/mdcollaborations/Collaboration.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdcollaborations">Collaboration</a></code>, <code><a href="../../deployments/mdnodes/CommunicationPath.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">CommunicationPath</a></code>, <code><a href="../../components/mdbasiccomponents/Component.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">Component</a></code>, <code><a href="../../components/mdbasiccomponents/ComponentRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.components.mdbasiccomponents">ComponentRealization</a></code>, <code><a href="../../compositestructures/mdinternalstructures/ConnectableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">ConnectableElement</a></code>, <code><a href="../../classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a></code>, <code><a href="../../classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code>, <code><a href="../../classes/mddependencies/Dependency.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Dependency</a></code>, <code><a href="../../deployments/mdnodes/Deployment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Deployment</a></code>, <code><a href="../../deployments/mdcomponentdeployments/DeploymentSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdcomponentdeployments">DeploymentSpecification</a></code>, <code><a href="../../deployments/mdnodes/Device.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Device</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Duration.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Duration</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationConstraint</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationInterval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/DurationObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">DurationObservation</a></code>, <code><a href="../../classes/mdkernel/ElementValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ElementValue</a></code>, <code><a href="../../compositestructures/mdports/EncapsulatedClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">EncapsulatedClassifier</a></code>, <code><a href="../../classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code>, <code><a href="../../classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></code>, <code><a href="../../deployments/mdnodes/ExecutionEnvironment.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">ExecutionEnvironment</a></code>, <code><a href="../../classes/mdkernel/Expression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Expression</a></code>, <code><a href="../../mdprofiles/Extension.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Extension</a></code>, <code><a href="../../mdprofiles/ExtensionEnd.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">ExtensionEnd</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/FunctionBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">FunctionBehavior</a></code>, <code><a href="../../classes/mdpowertypes/GeneralizationSet.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdpowertypes">GeneralizationSet</a></code>, <code><a href="../mdinformationflows/InformationFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationFlow</a></code>, <code><a href="../mdinformationflows/InformationItem.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdinformationflows">InformationItem</a></code>, <code><a href="../../classes/mdkernel/InstanceSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceSpecification</a></code>, <code><a href="../../classes/mdkernel/InstanceValue.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">InstanceValue</a></code>, <code><a href="../../interactions/mdbasicinteractions/Interaction.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdbasicinteractions">Interaction</a></code>, <code><a href="../../interactions/mdfragments/InteractionConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.interactions.mdfragments">InteractionConstraint</a></code>, <code><a href="../../classes/mdinterfaces/Interface.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">Interface</a></code>, <code><a href="../../classes/mdinterfaces/InterfaceRealization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdinterfaces">InterfaceRealization</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Interval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Interval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/IntervalConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">IntervalConstraint</a></code>, <code><a href="../../classes/mdkernel/LiteralBoolean.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralBoolean</a></code>, <code><a href="../../classes/mdkernel/LiteralInteger.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralInteger</a></code>, <code><a href="../../classes/mdkernel/LiteralNull.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralNull</a></code>, <code><a href="../../classes/mdkernel/LiteralReal.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralReal</a></code>, <code><a href="../../classes/mdkernel/LiteralSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralSpecification</a></code>, <code><a href="../../classes/mdkernel/LiteralString.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralString</a></code>, <code><a href="../../classes/mdkernel/LiteralUnlimitedNatural.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">LiteralUnlimitedNatural</a></code>, <code><a href="../../deployments/mdartifacts/Manifestation.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdartifacts">Manifestation</a></code>, <code><a href="../../commonbehaviors/mdcommunications/MessageEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">MessageEvent</a></code>, <code><a href="../mdmodels/Model.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdmodels">Model</a></code>, <code><a href="../../deployments/mdnodes/Node.html" title="interface in com.nomagic.uml2.ext.magicdraw.deployments.mdnodes">Node</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/Observation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">Observation</a></code>, <code><a href="../../commonbehaviors/mdbasicbehaviors/OpaqueBehavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">OpaqueBehavior</a></code>, <code><a href="../../classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a></code>, <code><a href="../../classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code>, <code><a href="../../classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code>, <code><a href="../../classes/mdkernel/PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code>, <code><a href="../../classes/mdkernel/Parameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Parameter</a></code>, <code><a href="../../compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a></code>, <code><a href="../../classes/mdkernel/PrimitiveType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PrimitiveType</a></code>, <code><a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code>, <code><a href="../../classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code>, <code><a href="../../statemachines/mdprotocolstatemachines/ProtocolStateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdprotocolstatemachines">ProtocolStateMachine</a></code>, <code><a href="../../classes/mddependencies/Realization.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Realization</a></code>, <code><a href="../../commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code>, <code><a href="../../commonbehaviors/mdcommunications/SignalEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">SignalEvent</a></code>, <code><a href="../../statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a></code>, <code><a href="../../mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code>, <code><a href="StringExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">StringExpression</a></code>, <code><a href="../../compositestructures/mdinternalstructures/StructuredClassifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdinternalstructures">StructuredClassifier</a></code>, <code><a href="../../classes/mddependencies/Substitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Substitution</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeConstraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeConstraint</a></code>, <code><a href="../../commonbehaviors/mdcommunications/TimeEvent.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">TimeEvent</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeExpression</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeInterval.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeInterval</a></code>, <code><a href="../../commonbehaviors/mdsimpletime/TimeObservation.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdsimpletime">TimeObservation</a></code>, <code><a href="../../classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a></code>, <code><a href="../../classes/mddependencies/Usage.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mddependencies">Usage</a></code>, <code><a href="../../mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code>, <code><a href="../../classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a></code>, <code><a href="../../activities/mdstructuredactivities/Variable.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">Variable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ParameterableElement</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Parameterable Element</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A ParameterableElement is an Element that can be exposed as a formal TemplateParameter for a template, or specified as an actual parameter in a binding of a template.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getOwningTemplateParameter()"><code><em>Owning Template Parameter</em></code></a></li>
<li><a href="#get_templateParameterOfDefault()"><code><em>template Parameter Of Default</em></code></a></li>
<li><a href="#get_templateParameterOfOwnedDefault()"><code><em>template Parameter Of Owned Default</em></code></a></li>
<li><a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a></li>
<li><a href="#get_templateParameterSubstitutionOfActual()"><code><em>template Parameter Substitution Of Actual</em></code></a></li>
<li><a href="#get_templateParameterSubstitutionOfOwnedActual()"><code><em>template Parameter
 Substitution Of Owned Actual</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getParameterableElement()"><code>UMLPackage.getParameterableElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>abstract="true"
 annotation="MOF package='auxiliaryconstructs.mdtemplates'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_templateParameterOfDefault()">get_templateParameterOfDefault</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>template Parameter Of Default</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_templateParameterOfOwnedDefault()">get_templateParameterOfOwnedDefault</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>template Parameter Of Owned Default</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_templateParameterSubstitutionOfActual()">get_templateParameterSubstitutionOfActual</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>template Parameter Substitution Of Actual</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_templateParameterSubstitutionOfOwnedActual()">get_templateParameterSubstitutionOfOwnedActual</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>template Parameter Substitution Of Owned Actual</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwningTemplateParameter()">getOwningTemplateParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owning Template Parameter</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTemplateParameter()">getTemplateParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Template Parameter</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_templateParameterOfDefault()">has_templateParameterOfDefault</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_templateParameterSubstitutionOfActual()">has_templateParameterSubstitutionOfActual</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">set_templateParameterOfOwnedDefault</a><wbr/>(<a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_templateParameterOfOwnedDefault()"><code><em>template Parameter Of Owned Default</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">set_templateParameterSubstitutionOfOwnedActual</a><wbr/>(<a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#get_templateParameterSubstitutionOfOwnedActual()"><code><em>template Parameter Substitution Of Owned Actual</em></code></a>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setOwningTemplateParameter</a><wbr/>(<a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwningTemplateParameter()"><code><em>Owning Template
 Parameter</em></code></a>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setTemplateParameter</a><wbr/>(<a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a>' reference.</div>
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
<section class="detail" id="getTemplateParameter()">
<h3>getTemplateParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></span> <span class="element-name">getTemplateParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>Template Parameter</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="TemplateParameter.html#getParameteredElement()"><code><em>Parametered Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The TemplateParameter that exposes this ParameterableElement as a formal parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Template Parameter</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)"><code>setTemplateParameter(TemplateParameter)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameterableElement_TemplateParameter()"><code>UMLPackage.getParameterableElement_TemplateParameter()</code></a></li>
<li><a href="TemplateParameter.html#getParameteredElement()"><code>TemplateParameter.getParameteredElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="parameteredElement" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">
<h3>setTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTemplateParameter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#getTemplateParameter()"><code><em>Template Parameter</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Template Parameter</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getTemplateParameter()"><code>getTemplateParameter()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningTemplateParameter()">
<h3>getOwningTemplateParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></span> <span class="element-name">getOwningTemplateParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>Owning Template Parameter</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="TemplateParameter.html#getOwnedParameteredElement()"><code><em>Owned Parametered Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The formal TemplateParameter that owns this ParameterableElement.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owning Template Parameter</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)"><code>setOwningTemplateParameter(TemplateParameter)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameterableElement_OwningTemplateParameter()"><code>UMLPackage.getParameterableElement_OwningTemplateParameter()</code></a></li>
<li><a href="TemplateParameter.html#getOwnedParameteredElement()"><code>TemplateParameter.getOwnedParameteredElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedParameteredElement" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningTemplateParameter(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">
<h3>setOwningTemplateParameter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwningTemplateParameter</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwningTemplateParameter()"><code><em>Owning Template
 Parameter</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owning Template Parameter</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwningTemplateParameter()"><code>getOwningTemplateParameter()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_templateParameterOfDefault()">
<h3>get_templateParameterOfDefault</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a>&gt;</span> <span class="element-name">get_templateParameterOfDefault</span>()</div>
<div class="block">Returns the value of the '<em><b>template Parameter Of Default</b></em>' reference list.
 The list contents are of type <a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameter</code></a>.
 It is bidirectional and its opposite is '<a href="TemplateParameter.html#getDefault()"><code><em>Default</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>template Parameter Of Default</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>template Parameter Of Default</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getParameterableElement__templateParameterOfDefault()"><code>UMLPackage.getParameterableElement__templateParameterOfDefault()</code></a></li>
<li><a href="TemplateParameter.html#getDefault()"><code>TemplateParameter.getDefault()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="default" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_templateParameterOfOwnedDefault()">
<h3>get_templateParameterOfOwnedDefault</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></span> <span class="element-name">get_templateParameterOfOwnedDefault</span>()</div>
<div class="block">Returns the value of the '<em><b>template Parameter Of Owned Default</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="TemplateParameter.html#getOwnedDefault()"><code><em>Owned Default</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>template Parameter Of Owned Default</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>template Parameter Of Owned Default</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)"><code>set_templateParameterOfOwnedDefault(TemplateParameter)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameterableElement__templateParameterOfOwnedDefault()"><code>UMLPackage.getParameterableElement__templateParameterOfOwnedDefault()</code></a></li>
<li><a href="TemplateParameter.html#getOwnedDefault()"><code>TemplateParameter.getOwnedDefault()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedDefault" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_templateParameterOfOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">
<h3>set_templateParameterOfOwnedDefault</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_templateParameterOfOwnedDefault</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_templateParameterOfOwnedDefault()"><code><em>template Parameter Of Owned Default</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>template Parameter Of Owned Default</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_templateParameterOfOwnedDefault()"><code>get_templateParameterOfOwnedDefault()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_templateParameterSubstitutionOfActual()">
<h3>get_templateParameterSubstitutionOfActual</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a>&gt;</span> <span class="element-name">get_templateParameterSubstitutionOfActual</span>()</div>
<div class="block">Returns the value of the '<em><b>template Parameter Substitution Of Actual</b></em>' reference list.
 The list contents are of type <a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a>.
 It is bidirectional and its opposite is
 '<a href="TemplateParameterSubstitution.html#getActual()"><code><em>Actual</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>template Parameter Substitution Of Actual</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>template Parameter Substitution Of Actual</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getParameterableElement__templateParameterSubstitutionOfActual()"><code>UMLPackage.getParameterableElement__templateParameterSubstitutionOfActual()</code></a></li>
<li><a href="TemplateParameterSubstitution.html#getActual()"><code>TemplateParameterSubstitution.getActual()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="actual" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_templateParameterSubstitutionOfOwnedActual()">
<h3>get_templateParameterSubstitutionOfOwnedActual</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a></span> <span class="element-name">get_templateParameterSubstitutionOfOwnedActual</span>()</div>
<div class="block">Returns the value of the '<em><b>template Parameter Substitution Of Owned Actual</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="TemplateParameterSubstitution.html#getOwnedActual()"><code><em>Owned Actual</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>template Parameter Substitution Of Owned Actual</em>' container reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>template Parameter Substitution Of Owned Actual</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)"><code>set_templateParameterSubstitutionOfOwnedActual(TemplateParameterSubstitution)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getParameterableElement__templateParameterSubstitutionOfOwnedActual()"><code>UMLPackage.getParameterableElement__templateParameterSubstitutionOfOwnedActual()</code></a></li>
<li><a href="TemplateParameterSubstitution.html#getOwnedActual()"><code>TemplateParameterSubstitution.getOwnedActual()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedActual" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_templateParameterSubstitutionOfOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameterSubstitution)">
<h3>set_templateParameterSubstitutionOfOwnedActual</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_templateParameterSubstitutionOfOwnedActual</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#get_templateParameterSubstitutionOfOwnedActual()"><code><em>template Parameter Substitution Of Owned Actual</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>template Parameter Substitution Of Owned Actual</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#get_templateParameterSubstitutionOfOwnedActual()"><code>get_templateParameterSubstitutionOfOwnedActual()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_templateParameterOfDefault()">
<h3>has_templateParameterOfDefault</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_templateParameterOfDefault</span>()
                                throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_templateParameterSubstitutionOfActual()">
<h3>has_templateParameterSubstitutionOfActual</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_templateParameterSubstitutionOfActual</span>()
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
