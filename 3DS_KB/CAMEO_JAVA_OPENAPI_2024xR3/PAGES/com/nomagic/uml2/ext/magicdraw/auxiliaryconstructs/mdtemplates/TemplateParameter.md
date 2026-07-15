# JAVA OPENAPI: TemplateParameter (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html
- source_path: `com/nomagic/uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameter.html`
- source_sha256: `30531b189912232f434c25cd0cf75da948e868a27aba01810d5c8a747e8c6954`
- captured_utc: `2026-07-14T16:56:20.757743+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates](package-summary.html)

## Interface TemplateParameter

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

All Known Subinterfaces:
`[ClassifierTemplateParameter](ClassifierTemplateParameter.html)`, `[ConnectableElementTemplateParameter](ConnectableElementTemplateParameter.html)`, `[OperationTemplateParameter](OperationTemplateParameter.html)`

public interfaceTemplateParameterextends [Element](../../classes/mdkernel/Element.html)

begin-user-doc 
 A representation of the model object '***Template Parameter***'.
 end-user-doc 
begin-model-doc 
 A TemplateParameter exposes a ParameterableElement as a formal parameter of a template.
 end-model-doc 
The following features are supported:
 [`*Default*`](#getDefault())
[`*Owned Default*`](#getOwnedDefault())
[`*Parametered Element*`](#getParameteredElement())
[`*Signature*`](#getSignature())
[`*template Signature Of Parameter*`](#get_templateSignatureOfParameter())
[`*template Parameter Substitution Of Formal*`](#get_templateParameterSubstitutionOfFormal())
[`*Owned Parametered Element*`](#getOwnedParameteredElement())

See Also:
[`UMLPackage.getTemplateParameter()`](../../metadata/UMLPackage.html#getTemplateParameter())
Model:
annotation="MOF package='auxiliaryconstructs.mdtemplates'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[TemplateParameterSubstitution](TemplateParameterSubstitution.html)>`
`[get_templateParameterSubstitutionOfFormal](#get_templateParameterSubstitutionOfFormal())()`
Returns the value of the '***template Parameter Substitution Of Formal***' reference list.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[TemplateSignature](TemplateSignature.html)>`
`[get_templateSignatureOfParameter](#get_templateSignatureOfParameter())()`
Returns the value of the '***template Signature Of Parameter***' reference list.
`[ParameterableElement](ParameterableElement.html)`
`[getDefault](#getDefault())()`
Returns the value of the '***Default***' reference.
`[ParameterableElement](ParameterableElement.html)`
`[getOwnedDefault](#getOwnedDefault())()`
Returns the value of the '***Owned Default***' containment reference.
`[ParameterableElement](ParameterableElement.html)`
`[getOwnedParameteredElement](#getOwnedParameteredElement())()`
Returns the value of the '***Owned Parametered Element***' containment reference.
`[ParameterableElement](ParameterableElement.html)`
`[getParameteredElement](#getParameteredElement())()`
Returns the value of the '***Parametered Element***' reference.
`[TemplateSignature](TemplateSignature.html)`
`[getSignature](#getSignature())()`
Returns the value of the '***Signature***' container reference.
`boolean`
`[has_templateParameterSubstitutionOfFormal](#has_templateParameterSubstitutionOfFormal())()`

`boolean`
`[has_templateSignatureOfParameter](#has_templateSignatureOfParameter())()`

`void`
`[setDefault](#setDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))([ParameterableElement](ParameterableElement.html) value)`
Sets the value of the '[`*Default*`](#getDefault())' reference.
`void`
`[setOwnedDefault](#setOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))([ParameterableElement](ParameterableElement.html) value)`
Sets the value of the '[`*Owned Default*`](#getOwnedDefault())'
 containment reference.
`void`
`[setOwnedParameteredElement](#setOwnedParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))([ParameterableElement](ParameterableElement.html) value)`
Sets the value of the '[`*Owned Parametered
 Element*`](#getOwnedParameteredElement())' containment reference.
`void`
`[setParameteredElement](#setParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))([ParameterableElement](ParameterableElement.html) value)`
Sets the value of the
 '[`*Parametered Element*`](#getParameteredElement())' reference.
`void`
`[setSignature](#setSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))([TemplateSignature](TemplateSignature.html) value)`
Sets the value of the '[`*Signature*`](#getSignature())' container
 reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [atInsert](../../../../../magicdraw/uml/BaseElement.html#atInsert()), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canAddInstance](../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [canChangeParent](../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)), [canDeleteChild](../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)), [clone](../../../../../magicdraw/uml/BaseElement.html#clone()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isParentOf](../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removeAllPropertyChangeListeners](../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID`
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
getDefault
@CheckForNull[ParameterableElement](ParameterableElement.html) getDefault()
Returns the value of the '***Default***' reference.
 It is bidirectional and its opposite is '`.mdtemplates.ParameterableElement#get_templateParameterOfDefault *template Parameter Of Default*`'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ParameterableElement that is the default for this formal TemplateParameter.
 end-model-doc
Returns:
the value of the '*Default*' reference.
See Also:
[`setDefault(ParameterableElement)`](#setDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))
[`UMLPackage.getTemplateParameter_Default()`](../../metadata/UMLPackage.html#getTemplateParameter_Default())
[`ParameterableElement.get_templateParameterOfDefault()`](ParameterableElement.html#get_templateParameterOfDefault())
Model:
opposite="_templateParameterOfDefault" ordered="false"
Generated:
setDefault
void setDefault(@CheckForNull
 [ParameterableElement](ParameterableElement.html) value)
Sets the value of the '[`*Default*`](#getDefault())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Default*' reference.
See Also:
[`getDefault()`](#getDefault())
Generated:
getOwnedDefault
@CheckForNull[ParameterableElement](ParameterableElement.html) getOwnedDefault()
Returns the value of the '***Owned Default***' containment reference.
 It is bidirectional and its opposite is '[`.ParameterableElement#get_templateParameterOfOwnedDefault *template Parameter Of Owned Default*`](package-summary.html)'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ParameterableElement that is owned by this TemplateParameter for the purpose of providing a default.
 end-model-doc
Returns:
the value of the '*Owned Default*' containment reference.
See Also:
[`setOwnedDefault(ParameterableElement)`](#setOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))
[`UMLPackage.getTemplateParameter_OwnedDefault()`](../../metadata/UMLPackage.html#getTemplateParameter_OwnedDefault())
[`ParameterableElement.get_templateParameterOfOwnedDefault()`](ParameterableElement.html#get_templateParameterOfOwnedDefault())
Model:
opposite="_templateParameterOfOwnedDefault" containment="true" resolveProxies="true" ordered="false"
Generated:
setOwnedDefault
void setOwnedDefault(@CheckForNull
 [ParameterableElement](ParameterableElement.html) value)
Sets the value of the '[`*Owned Default*`](#getOwnedDefault())'
 containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owned Default*' containment reference.
See Also:
[`getOwnedDefault()`](#getOwnedDefault())
Generated:
getParameteredElement
@CheckForNull[ParameterableElement](ParameterableElement.html) getParameteredElement()
Returns the value of the '***Parametered Element***' reference.
 It is bidirectional and its opposite is
 '[`*Template Parameter*`](ParameterableElement.html#getTemplateParameter())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ParameterableElement exposed by this TemplateParameter.
 end-model-doc
Returns:
the value of the '*Parametered Element*' reference.
See Also:
[`setParameteredElement(ParameterableElement)`](#setParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))
[`UMLPackage.getTemplateParameter_ParameteredElement()`](../../metadata/UMLPackage.html#getTemplateParameter_ParameteredElement())
[`ParameterableElement.getTemplateParameter()`](ParameterableElement.html#getTemplateParameter())
Model:
opposite="templateParameter" required="true" ordered="false"
Generated:
setParameteredElement
void setParameteredElement(@CheckForNull
 [ParameterableElement](ParameterableElement.html) value)
Sets the value of the
 '[`*Parametered Element*`](#getParameteredElement())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Parametered Element*' reference.
See Also:
[`getParameteredElement()`](#getParameteredElement())
Generated:
getSignature
@CheckForNull[TemplateSignature](TemplateSignature.html) getSignature()
Returns the value of the '***Signature***' container reference.
 It is bidirectional and its opposite is
 '[`*Owned Parameter*`](TemplateSignature.html#getOwnedParameter())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The TemplateSignature that owns this TemplateParameter.
 end-model-doc
Returns:
the value of the '*Signature*' container reference.
See Also:
[`setSignature(TemplateSignature)`](#setSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature))
[`UMLPackage.getTemplateParameter_Signature()`](../../metadata/UMLPackage.html#getTemplateParameter_Signature())
[`TemplateSignature.getOwnedParameter()`](TemplateSignature.html#getOwnedParameter())
Model:
opposite="ownedParameter" required="true" transient="false" ordered="false"
Generated:
setSignature
void setSignature(@CheckForNull
 [TemplateSignature](TemplateSignature.html) value)
Sets the value of the '[`*Signature*`](#getSignature())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Signature*' container reference.
See Also:
[`getSignature()`](#getSignature())
Generated:
get_templateSignatureOfParameter
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[TemplateSignature](TemplateSignature.html)> get_templateSignatureOfParameter()
Returns the value of the '***template Signature Of Parameter***' reference list.
 The list contents are of type [`TemplateSignature`](TemplateSignature.html).
 It is bidirectional and its opposite is
 '[`*Parameter*`](TemplateSignature.html#getParameter())'.
 begin-user-doc 
If the meaning of the '*template Signature Of Parameter*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*template Signature Of Parameter*' reference list.
See Also:
[`UMLPackage.getTemplateParameter__templateSignatureOfParameter()`](../../metadata/UMLPackage.html#getTemplateParameter__templateSignatureOfParameter())
[`TemplateSignature.getParameter()`](TemplateSignature.html#getParameter())
Model:
opposite="parameter" ordered="false"
Generated:
get_templateParameterSubstitutionOfFormal
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[TemplateParameterSubstitution](TemplateParameterSubstitution.html)> get_templateParameterSubstitutionOfFormal()
Returns the value of the '***template Parameter Substitution Of Formal***' reference list.
 The list contents are of type [`TemplateParameterSubstitution`](TemplateParameterSubstitution.html).
 It is bidirectional and its opposite is
 '[`*Formal*`](TemplateParameterSubstitution.html#getFormal())'.
 begin-user-doc 
If the meaning of the '*template Parameter Substitution Of Formal*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*template Parameter Substitution Of Formal*' reference list.
See Also:
[`UMLPackage.getTemplateParameter__templateParameterSubstitutionOfFormal()`](../../metadata/UMLPackage.html#getTemplateParameter__templateParameterSubstitutionOfFormal())
[`TemplateParameterSubstitution.getFormal()`](TemplateParameterSubstitution.html#getFormal())
Model:
opposite="formal" ordered="false"
Generated:
getOwnedParameteredElement
@CheckForNull[ParameterableElement](ParameterableElement.html) getOwnedParameteredElement()
Returns the value of the '***Owned Parametered Element***' containment reference.
 It is bidirectional and its opposite is
 '[`*Owning Template Parameter*`](ParameterableElement.html#getOwningTemplateParameter())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ParameterableElement that is owned by this TemplateParameter for the purpose of exposing it as the parameteredElement.
 end-model-doc
Returns:
the value of the '*Owned Parametered Element*' containment reference.
See Also:
[`setOwnedParameteredElement(ParameterableElement)`](#setOwnedParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))
[`UMLPackage.getTemplateParameter_OwnedParameteredElement()`](../../metadata/UMLPackage.html#getTemplateParameter_OwnedParameteredElement())
[`ParameterableElement.getOwningTemplateParameter()`](ParameterableElement.html#getOwningTemplateParameter())
Model:
opposite="owningTemplateParameter" containment="true" resolveProxies="true" ordered="false"
Generated:
setOwnedParameteredElement
void setOwnedParameteredElement(@CheckForNull
 [ParameterableElement](ParameterableElement.html) value)
Sets the value of the '[`*Owned Parametered
 Element*`](#getOwnedParameteredElement())' containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owned Parametered Element*' containment reference.
See Also:
[`getOwnedParameteredElement()`](#getOwnedParameteredElement())
Generated:
has_templateSignatureOfParameter
boolean has_templateSignatureOfParameter()
 throws javax.jmi.reflect.JmiException
Throws:
`javax.jmi.reflect.JmiException`
Generated:
has_templateParameterSubstitutionOfFormal
boolean has_templateParameterSubstitutionOfFormal()
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
<h1 class="title" title="Interface TemplateParameter">Interface TemplateParameter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ClassifierTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ClassifierTemplateParameter</a></code>, <code><a href="ConnectableElementTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ConnectableElementTemplateParameter</a></code>, <code><a href="OperationTemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">OperationTemplateParameter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TemplateParameter</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Template Parameter</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A TemplateParameter exposes a ParameterableElement as a formal parameter of a template.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getDefault()"><code><em>Default</em></code></a></li>
<li><a href="#getOwnedDefault()"><code><em>Owned Default</em></code></a></li>
<li><a href="#getParameteredElement()"><code><em>Parametered Element</em></code></a></li>
<li><a href="#getSignature()"><code><em>Signature</em></code></a></li>
<li><a href="#get_templateSignatureOfParameter()"><code><em>template Signature Of Parameter</em></code></a></li>
<li><a href="#get_templateParameterSubstitutionOfFormal()"><code><em>template Parameter Substitution Of Formal</em></code></a></li>
<li><a href="#getOwnedParameteredElement()"><code><em>Owned Parametered Element</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getTemplateParameter()"><code>UMLPackage.getTemplateParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='auxiliaryconstructs.mdtemplates'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_templateParameterSubstitutionOfFormal()">get_templateParameterSubstitutionOfFormal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>template Parameter Substitution Of Formal</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_templateSignatureOfParameter()">get_templateSignatureOfParameter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>template Signature Of Parameter</b></em>' reference list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefault()">getDefault</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Default</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedDefault()">getOwnedDefault</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Default</b></em>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedParameteredElement()">getOwnedParameteredElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Parametered Element</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParameteredElement()">getParameteredElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Parametered Element</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSignature()">getSignature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Signature</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_templateParameterSubstitutionOfFormal()">has_templateParameterSubstitutionOfFormal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#has_templateSignatureOfParameter()">has_templateSignatureOfParameter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">setDefault</a><wbr/>(<a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getDefault()"><code><em>Default</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">setOwnedDefault</a><wbr/>(<a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwnedDefault()"><code><em>Owned Default</em></code></a>'
 containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwnedParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">setOwnedParameteredElement</a><wbr/>(<a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwnedParameteredElement()"><code><em>Owned Parametered
 Element</em></code></a>' containment reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">setParameteredElement</a><wbr/>(<a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#getParameteredElement()"><code><em>Parametered Element</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)">setSignature</a><wbr/>(<a href="TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getSignature()"><code><em>Signature</em></code></a>' container
 reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#atInsert()">atInsert</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canAddInstance(com.nomagic.magicdraw.uml.BaseElement)">canAddInstance</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canChangeParent(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">canChangeParent</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#canDeleteChild(com.nomagic.magicdraw.uml.BaseElement)">canDeleteChild</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#clone()">clone</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isParentOf(com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removeAllPropertyChangeListeners()">removeAllPropertyChangeListeners</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
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
<code>canChangeElementOwner, dispose, eDynamicGet, getElementOwner, getLocalID, getObjectParent, selfDispose, setLocalID, sGetLocalID</code></div>
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
<section class="detail" id="getDefault()">
<h3>getDefault</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></span> <span class="element-name">getDefault</span>()</div>
<div class="block">Returns the value of the '<em><b>Default</b></em>' reference.
 It is bidirectional and its opposite is '<code>.mdtemplates.ParameterableElement#get_templateParameterOfDefault <em>template Parameter Of Default</em></code>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ParameterableElement that is the default for this formal TemplateParameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Default</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)"><code>setDefault(ParameterableElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameter_Default()"><code>UMLPackage.getTemplateParameter_Default()</code></a></li>
<li><a href="ParameterableElement.html#get_templateParameterOfDefault()"><code>ParameterableElement.get_templateParameterOfDefault()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_templateParameterOfDefault" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">
<h3>setDefault</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDefault</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getDefault()"><code><em>Default</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Default</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getDefault()"><code>getDefault()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedDefault()">
<h3>getOwnedDefault</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></span> <span class="element-name">getOwnedDefault</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Default</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="package-summary.html"><code>.ParameterableElement#get_templateParameterOfOwnedDefault <em>template Parameter Of Owned Default</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ParameterableElement that is owned by this TemplateParameter for the purpose of providing a default.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Default</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)"><code>setOwnedDefault(ParameterableElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameter_OwnedDefault()"><code>UMLPackage.getTemplateParameter_OwnedDefault()</code></a></li>
<li><a href="ParameterableElement.html#get_templateParameterOfOwnedDefault()"><code>ParameterableElement.get_templateParameterOfOwnedDefault()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_templateParameterOfOwnedDefault" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedDefault(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">
<h3>setOwnedDefault</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwnedDefault</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwnedDefault()"><code><em>Owned Default</em></code></a>'
 containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owned Default</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwnedDefault()"><code>getOwnedDefault()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParameteredElement()">
<h3>getParameteredElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></span> <span class="element-name">getParameteredElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Parametered Element</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="ParameterableElement.html#getTemplateParameter()"><code><em>Template Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ParameterableElement exposed by this TemplateParameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Parametered Element</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)"><code>setParameteredElement(ParameterableElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameter_ParameteredElement()"><code>UMLPackage.getTemplateParameter_ParameteredElement()</code></a></li>
<li><a href="ParameterableElement.html#getTemplateParameter()"><code>ParameterableElement.getTemplateParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="templateParameter" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">
<h3>setParameteredElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setParameteredElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#getParameteredElement()"><code><em>Parametered Element</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Parametered Element</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getParameteredElement()"><code>getParameteredElement()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignature()">
<h3>getSignature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a></span> <span class="element-name">getSignature</span>()</div>
<div class="block">Returns the value of the '<em><b>Signature</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="TemplateSignature.html#getOwnedParameter()"><code><em>Owned Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The TemplateSignature that owns this TemplateParameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Signature</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)"><code>setSignature(TemplateSignature)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameter_Signature()"><code>UMLPackage.getTemplateParameter_Signature()</code></a></li>
<li><a href="TemplateSignature.html#getOwnedParameter()"><code>TemplateSignature.getOwnedParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="ownedParameter" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSignature(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateSignature)">
<h3>setSignature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSignature</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getSignature()"><code><em>Signature</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Signature</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getSignature()"><code>getSignature()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_templateSignatureOfParameter()">
<h3>get_templateSignatureOfParameter</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateSignature</a>&gt;</span> <span class="element-name">get_templateSignatureOfParameter</span>()</div>
<div class="block">Returns the value of the '<em><b>template Signature Of Parameter</b></em>' reference list.
 The list contents are of type <a href="TemplateSignature.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateSignature</code></a>.
 It is bidirectional and its opposite is
 '<a href="TemplateSignature.html#getParameter()"><code><em>Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>template Signature Of Parameter</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>template Signature Of Parameter</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getTemplateParameter__templateSignatureOfParameter()"><code>UMLPackage.getTemplateParameter__templateSignatureOfParameter()</code></a></li>
<li><a href="TemplateSignature.html#getParameter()"><code>TemplateSignature.getParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="parameter" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_templateParameterSubstitutionOfFormal()">
<h3>get_templateParameterSubstitutionOfFormal</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameterSubstitution</a>&gt;</span> <span class="element-name">get_templateParameterSubstitutionOfFormal</span>()</div>
<div class="block">Returns the value of the '<em><b>template Parameter Substitution Of Formal</b></em>' reference list.
 The list contents are of type <a href="TemplateParameterSubstitution.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates"><code>TemplateParameterSubstitution</code></a>.
 It is bidirectional and its opposite is
 '<a href="TemplateParameterSubstitution.html#getFormal()"><code><em>Formal</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>template Parameter Substitution Of Formal</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>template Parameter Substitution Of Formal</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../metadata/UMLPackage.html#getTemplateParameter__templateParameterSubstitutionOfFormal()"><code>UMLPackage.getTemplateParameter__templateParameterSubstitutionOfFormal()</code></a></li>
<li><a href="TemplateParameterSubstitution.html#getFormal()"><code>TemplateParameterSubstitution.getFormal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="formal" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedParameteredElement()">
<h3>getOwnedParameteredElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></span> <span class="element-name">getOwnedParameteredElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Parametered Element</b></em>' containment reference.
 It is bidirectional and its opposite is
 '<a href="ParameterableElement.html#getOwningTemplateParameter()"><code><em>Owning Template Parameter</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ParameterableElement that is owned by this TemplateParameter for the purpose of exposing it as the parameteredElement.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Parametered Element</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setOwnedParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)"><code>setOwnedParameteredElement(ParameterableElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameter_OwnedParameteredElement()"><code>UMLPackage.getTemplateParameter_OwnedParameteredElement()</code></a></li>
<li><a href="ParameterableElement.html#getOwningTemplateParameter()"><code>ParameterableElement.getOwningTemplateParameter()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="owningTemplateParameter" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedParameteredElement(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">
<h3>setOwnedParameteredElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwnedParameteredElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwnedParameteredElement()"><code><em>Owned Parametered
 Element</em></code></a>' containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owned Parametered Element</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getOwnedParameteredElement()"><code>getOwnedParameteredElement()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_templateSignatureOfParameter()">
<h3>has_templateSignatureOfParameter</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_templateSignatureOfParameter</span>()
                                  throws <span class="exceptions">javax.jmi.reflect.JmiException</span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>javax.jmi.reflect.JmiException</code></dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="has_templateParameterSubstitutionOfFormal()">
<h3>has_templateParameterSubstitutionOfFormal</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">has_templateParameterSubstitutionOfFormal</span>()
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
