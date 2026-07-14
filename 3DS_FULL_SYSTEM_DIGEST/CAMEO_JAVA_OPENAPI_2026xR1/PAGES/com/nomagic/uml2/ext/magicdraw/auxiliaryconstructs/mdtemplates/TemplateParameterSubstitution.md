# JAVA OPENAPI: TemplateParameterSubstitution (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html
- source_path: `com/nomagic/uml2/ext/magicdraw/auxiliaryconstructs/mdtemplates/TemplateParameterSubstitution.html`
- source_sha256: `731dca4a33f13e803b24ec53b5e2b1e6a534a88fba2089b1c0f6318989a0d60b`
- captured_utc: `2026-07-14T16:46:27.669168+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates](package-summary.html)

## Interface TemplateParameterSubstitution

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceTemplateParameterSubstitutionextends [Element](../../classes/mdkernel/Element.html)

begin-user-doc 
 A representation of the model object '***Template Parameter Substitution***'.
 end-user-doc 
begin-model-doc 
 A TemplateParameterSubstitution relates the actual parameter to a formal TemplateParameter as part of a template binding.
 end-model-doc 
The following features are supported:
 [`*Actual*`](#getActual())
[`*Formal*`](#getFormal())
[`*Owned Actual*`](#getOwnedActual())
[`*Template Binding*`](#getTemplateBinding())

See Also:
[`UMLPackage.getTemplateParameterSubstitution()`](../../metadata/UMLPackage.html#getTemplateParameterSubstitution())
Model:
annotation="MOF package='auxiliaryconstructs.mdtemplates'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ParameterableElement](ParameterableElement.html)`
`[getActual](#getActual())()`
Returns the value of the '***Actual***' reference.
`[TemplateParameter](TemplateParameter.html)`
`[getFormal](#getFormal())()`
Returns the value of the '***Formal***' reference.
`[ParameterableElement](ParameterableElement.html)`
`[getOwnedActual](#getOwnedActual())()`
Returns the value of the '***Owned Actual***' containment reference.
`[TemplateBinding](TemplateBinding.html)`
`[getTemplateBinding](#getTemplateBinding())()`
Returns the value of the '***Template Binding***' container reference.
`void`
`[setActual](#setActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))([ParameterableElement](ParameterableElement.html) value)`
Sets the value of the '[`*Actual*`](#getActual())' reference.
`void`
`[setFormal](#setFormal(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))([TemplateParameter](TemplateParameter.html) value)`
Sets the value of the '[`*Formal*`](#getFormal())' reference.
`void`
`[setOwnedActual](#setOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))([ParameterableElement](ParameterableElement.html) value)`
Sets the value of the '[`*Owned Actual*`](#getOwnedActual())'
 containment reference.
`void`
`[setTemplateBinding](#setTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding))([TemplateBinding](TemplateBinding.html) value)`
Sets the value of the
 '[`*Template Binding*`](#getTemplateBinding())' container
 reference.
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
getActual
@CheckForNull[ParameterableElement](ParameterableElement.html) getActual()
Returns the value of the '***Actual***' reference.
 It is bidirectional and its opposite is '[`.ParameterableElement#get_templateParameterSubstitutionOfActual *template Parameter Substitution Of Actual*`](package-summary.html)'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ParameterableElement that is the actual parameter for this TemplateParameterSubstitution.
 end-model-doc
Returns:
the value of the '*Actual*' reference.
See Also:
[`setActual(ParameterableElement)`](#setActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))
[`UMLPackage.getTemplateParameterSubstitution_Actual()`](../../metadata/UMLPackage.html#getTemplateParameterSubstitution_Actual())
[`ParameterableElement.get_templateParameterSubstitutionOfActual()`](ParameterableElement.html#get_templateParameterSubstitutionOfActual())
Model:
opposite="_templateParameterSubstitutionOfActual" required="true" ordered="false"
Generated:
setActual
void setActual(@CheckForNull
 [ParameterableElement](ParameterableElement.html) value)
Sets the value of the '[`*Actual*`](#getActual())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Actual*' reference.
See Also:
[`getActual()`](#getActual())
Generated:
getFormal
@CheckForNull[TemplateParameter](TemplateParameter.html) getFormal()
Returns the value of the '***Formal***' reference.
 It is bidirectional and its opposite is '[`.TemplateParameter#get_templateParameterSubstitutionOfFormal *template Parameter Substitution Of Formal*`](package-summary.html)'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The formal TemplateParameter that is associated with this TemplateParameterSubstitution.
 end-model-doc
Returns:
the value of the '*Formal*' reference.
See Also:
[`setFormal(TemplateParameter)`](#setFormal(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter))
[`UMLPackage.getTemplateParameterSubstitution_Formal()`](../../metadata/UMLPackage.html#getTemplateParameterSubstitution_Formal())
[`TemplateParameter.get_templateParameterSubstitutionOfFormal()`](TemplateParameter.html#get_templateParameterSubstitutionOfFormal())
Model:
opposite="_templateParameterSubstitutionOfFormal" required="true" ordered="false"
Generated:
setFormal
void setFormal(@CheckForNull
 [TemplateParameter](TemplateParameter.html) value)
Sets the value of the '[`*Formal*`](#getFormal())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Formal*' reference.
See Also:
[`getFormal()`](#getFormal())
Generated:
getOwnedActual
@CheckForNull[ParameterableElement](ParameterableElement.html) getOwnedActual()
Returns the value of the '***Owned Actual***' containment reference.
 It is bidirectional and its opposite is '[`.ParameterableElement#get_templateParameterSubstitutionOfOwnedActual *template Parameter Substitution Of Owned Actual*`](package-summary.html)'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The ParameterableElement that is owned by this TemplateParameterSubstitution as its actual parameter.
 end-model-doc
Returns:
the value of the '*Owned Actual*' containment reference.
See Also:
[`setOwnedActual(ParameterableElement)`](#setOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement))
[`UMLPackage.getTemplateParameterSubstitution_OwnedActual()`](../../metadata/UMLPackage.html#getTemplateParameterSubstitution_OwnedActual())
[`ParameterableElement.get_templateParameterSubstitutionOfOwnedActual()`](ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual())
Model:
opposite="_templateParameterSubstitutionOfOwnedActual" containment="true" resolveProxies="true" ordered="false"
Generated:
setOwnedActual
void setOwnedActual(@CheckForNull
 [ParameterableElement](ParameterableElement.html) value)
Sets the value of the '[`*Owned Actual*`](#getOwnedActual())'
 containment reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Owned Actual*' containment reference.
See Also:
[`getOwnedActual()`](#getOwnedActual())
Generated:
getTemplateBinding
@CheckForNull[TemplateBinding](TemplateBinding.html) getTemplateBinding()
Returns the value of the '***Template Binding***' container reference.
 It is bidirectional and its opposite is
 '[`*Parameter Substitution*`](TemplateBinding.html#getParameterSubstitution())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The TemplateBinding that owns this TemplateParameterSubstitution.
 end-model-doc
Returns:
the value of the '*Template Binding*' container reference.
See Also:
[`setTemplateBinding(TemplateBinding)`](#setTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding))
[`UMLPackage.getTemplateParameterSubstitution_TemplateBinding()`](../../metadata/UMLPackage.html#getTemplateParameterSubstitution_TemplateBinding())
[`TemplateBinding.getParameterSubstitution()`](TemplateBinding.html#getParameterSubstitution())
Model:
opposite="parameterSubstitution" required="true" transient="false" ordered="false"
Generated:
setTemplateBinding
void setTemplateBinding(@CheckForNull
 [TemplateBinding](TemplateBinding.html) value)
Sets the value of the
 '[`*Template Binding*`](#getTemplateBinding())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Template Binding*' container reference.
See Also:
[`getTemplateBinding()`](#getTemplateBinding())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates</a></div>
<h1 class="title" title="Interface TemplateParameterSubstitution">Interface TemplateParameterSubstitution</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TemplateParameterSubstitution</span><span class="extends-implements">
extends <a href="../../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Template Parameter Substitution</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A TemplateParameterSubstitution relates the actual parameter to a formal TemplateParameter as part of a template binding.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getActual()"><code><em>Actual</em></code></a></li>
<li><a href="#getFormal()"><code><em>Formal</em></code></a></li>
<li><a href="#getOwnedActual()"><code><em>Owned Actual</em></code></a></li>
<li><a href="#getTemplateBinding()"><code><em>Template Binding</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../metadata/UMLPackage.html#getTemplateParameterSubstitution()"><code>UMLPackage.getTemplateParameterSubstitution()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getActual()">getActual</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Actual</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFormal()">getFormal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Formal</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOwnedActual()">getOwnedActual</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Owned Actual</b></em>' containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTemplateBinding()">getTemplateBinding</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Template Binding</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">setActual</a><wbr/>(<a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getActual()"><code><em>Actual</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setFormal(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">setFormal</a><wbr/>(<a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getFormal()"><code><em>Formal</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">setOwnedActual</a><wbr/>(<a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getOwnedActual()"><code><em>Owned Actual</em></code></a>'
 containment reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)">setTemplateBinding</a><wbr/>(<a href="TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#getTemplateBinding()"><code><em>Template Binding</em></code></a>' container
 reference.</div>
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
<section class="detail" id="getActual()">
<h3>getActual</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></span> <span class="element-name">getActual</span>()</div>
<div class="block">Returns the value of the '<em><b>Actual</b></em>' reference.
 It is bidirectional and its opposite is '<a href="package-summary.html"><code>.ParameterableElement#get_templateParameterSubstitutionOfActual <em>template Parameter Substitution Of Actual</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ParameterableElement that is the actual parameter for this TemplateParameterSubstitution.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Actual</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)"><code>setActual(ParameterableElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameterSubstitution_Actual()"><code>UMLPackage.getTemplateParameterSubstitution_Actual()</code></a></li>
<li><a href="ParameterableElement.html#get_templateParameterSubstitutionOfActual()"><code>ParameterableElement.get_templateParameterSubstitutionOfActual()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_templateParameterSubstitutionOfActual" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">
<h3>setActual</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setActual</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getActual()"><code><em>Actual</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Actual</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getActual()"><code>getActual()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFormal()">
<h3>getFormal</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a></span> <span class="element-name">getFormal</span>()</div>
<div class="block">Returns the value of the '<em><b>Formal</b></em>' reference.
 It is bidirectional and its opposite is '<a href="package-summary.html"><code>.TemplateParameter#get_templateParameterSubstitutionOfFormal <em>template Parameter Substitution Of Formal</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The formal TemplateParameter that is associated with this TemplateParameterSubstitution.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Formal</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setFormal(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)"><code>setFormal(TemplateParameter)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameterSubstitution_Formal()"><code>UMLPackage.getTemplateParameterSubstitution_Formal()</code></a></li>
<li><a href="TemplateParameter.html#get_templateParameterSubstitutionOfFormal()"><code>TemplateParameter.get_templateParameterSubstitutionOfFormal()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_templateParameterSubstitutionOfFormal" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFormal(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateParameter)">
<h3>setFormal</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setFormal</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TemplateParameter.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateParameter</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getFormal()"><code><em>Formal</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Formal</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getFormal()"><code>getFormal()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedActual()">
<h3>getOwnedActual</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a></span> <span class="element-name">getOwnedActual</span>()</div>
<div class="block">Returns the value of the '<em><b>Owned Actual</b></em>' containment reference.
 It is bidirectional and its opposite is '<a href="package-summary.html"><code>.ParameterableElement#get_templateParameterSubstitutionOfOwnedActual <em>template Parameter Substitution Of Owned Actual</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The ParameterableElement that is owned by this TemplateParameterSubstitution as its actual parameter.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Owned Actual</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)"><code>setOwnedActual(ParameterableElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameterSubstitution_OwnedActual()"><code>UMLPackage.getTemplateParameterSubstitution_OwnedActual()</code></a></li>
<li><a href="ParameterableElement.html#get_templateParameterSubstitutionOfOwnedActual()"><code>ParameterableElement.get_templateParameterSubstitutionOfOwnedActual()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_templateParameterSubstitutionOfOwnedActual" containment="true" resolveProxies="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedActual(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.ParameterableElement)">
<h3>setOwnedActual</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOwnedActual</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ParameterableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">ParameterableElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getOwnedActual()"><code><em>Owned Actual</em></code></a>'
 containment reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Owned Actual</em>' containment reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getOwnedActual()"><code>getOwnedActual()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateBinding()">
<h3>getTemplateBinding</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a></span> <span class="element-name">getTemplateBinding</span>()</div>
<div class="block">Returns the value of the '<em><b>Template Binding</b></em>' container reference.
 It is bidirectional and its opposite is
 '<a href="TemplateBinding.html#getParameterSubstitution()"><code><em>Parameter Substitution</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The TemplateBinding that owns this TemplateParameterSubstitution.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Template Binding</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)"><code>setTemplateBinding(TemplateBinding)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getTemplateParameterSubstitution_TemplateBinding()"><code>UMLPackage.getTemplateParameterSubstitution_TemplateBinding()</code></a></li>
<li><a href="TemplateBinding.html#getParameterSubstitution()"><code>TemplateBinding.getParameterSubstitution()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="parameterSubstitution" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTemplateBinding(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.TemplateBinding)">
<h3>setTemplateBinding</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTemplateBinding</span><wbr/><span class="parameters">(@CheckForNull
 <a href="TemplateBinding.html" title="interface in com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates">TemplateBinding</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#getTemplateBinding()"><code><em>Template Binding</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Template Binding</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getTemplateBinding()"><code>getTemplateBinding()</code></a></li>
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
