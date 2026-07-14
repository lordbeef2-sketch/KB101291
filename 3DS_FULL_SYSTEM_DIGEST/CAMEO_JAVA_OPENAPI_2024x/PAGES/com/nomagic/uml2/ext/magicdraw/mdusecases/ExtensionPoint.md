# JAVA OPENAPI: ExtensionPoint (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/magicdraw/mdusecases/ExtensionPoint.html
- source_path: `com/nomagic/uml2/ext/magicdraw/mdusecases/ExtensionPoint.html`
- source_sha256: `e7cebd2f176e0da1b8e0a9baf7a5f0a4824e00e0b42d87800bc6078cec68346e`
- captured_utc: `2026-07-14T16:53:13.244640+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.mdusecases](package-summary.html)

## Interface ExtensionPoint

All Superinterfaces:
`[BaseElement](../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[Element](../classes/mdkernel/Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../base/ModelObject.html)`, `[NamedElement](../classes/mdkernel/NamedElement.html)`, `org.eclipse.emf.common.notify.Notifier`, `[RedefinableElement](../classes/mdkernel/RedefinableElement.html)`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`

public interfaceExtensionPointextends [RedefinableElement](../classes/mdkernel/RedefinableElement.html)

begin-user-doc 
 A representation of the model object '***Extension Point***'.
 end-user-doc 
begin-model-doc 
 An ExtensionPoint identifies a point in the behavior of a UseCase where that behavior can be extended by the behavior of some other (extending) UseCase, as
 specified by an Extend relationship.
 end-model-doc 
The following features are supported:
 [`*Extension*`](#getExtension())
[`*Use Case*`](#getUseCase())

See Also:
[`UMLPackage.getExtensionPoint()`](../metadata/UMLPackage.html#getExtensionPoint())
Model:
annotation="MOF package='mdusecases'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Extend](Extend.html)>`
`[getExtension](#getExtension())()`
Returns the value of the '***Extension***' reference list.
`[UseCase](UseCase.html)`
`[getUseCase](#getUseCase())()`
Returns the value of the '***Use Case***' container reference.
`boolean`
`[hasExtension](#hasExtension())()`

`void`
`[setUseCase](#setUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](UseCase.html) value)`
Sets the value of the '[`*Use Case*`](#getUseCase())' container reference.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../magicdraw/uml/BaseElement.html#isEditable()), [removePropertyChangeListener](../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Element](../classes/mdkernel/Element.html)
`[get_activityPartitionOfRepresents](../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()), [get_commentOfAnnotatedElement](../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()), [get_constraintOfConstrainedElement](../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()), [get_diagramOfContext](../classes/mdkernel/Element.html#get_diagramOfContext()), [get_directedRelationshipOfSource](../classes/mdkernel/Element.html#get_directedRelationshipOfSource()), [get_directedRelationshipOfTarget](../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()), [get_elementOfSyncElement](../classes/mdkernel/Element.html#get_elementOfSyncElement()), [get_elementTaggedValue](../classes/mdkernel/Element.html#get_elementTaggedValue()), [get_elementValueOfElement](../classes/mdkernel/Element.html#get_elementValueOfElement()), [get_relationshipOfRelatedElement](../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()), [getAppliedStereotype](../classes/mdkernel/Element.html#getAppliedStereotype()), [getOwnedComment](../classes/mdkernel/Element.html#getOwnedComment()), [getOwnedElement](../classes/mdkernel/Element.html#getOwnedElement()), [getOwner](../classes/mdkernel/Element.html#getOwner()), [getSyncElement](../classes/mdkernel/Element.html#getSyncElement()), [getTaggedValue](../classes/mdkernel/Element.html#getTaggedValue()), [has_activityPartitionOfRepresents](../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()), [has_commentOfAnnotatedElement](../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()), [has_constraintOfConstrainedElement](../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()), [has_diagramOfContext](../classes/mdkernel/Element.html#has_diagramOfContext()), [has_directedRelationshipOfSource](../classes/mdkernel/Element.html#has_directedRelationshipOfSource()), [has_directedRelationshipOfTarget](../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()), [has_elementOfSyncElement](../classes/mdkernel/Element.html#has_elementOfSyncElement()), [has_elementValueOfElement](../classes/mdkernel/Element.html#has_elementValueOfElement()), [has_relationshipOfRelatedElement](../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()), [hasAppliedStereotype](../classes/mdkernel/Element.html#hasAppliedStereotype()), [hasElementTaggedValue](../classes/mdkernel/Element.html#hasElementTaggedValue()), [hasOwnedComment](../classes/mdkernel/Element.html#hasOwnedComment()), [hasOwnedElement](../classes/mdkernel/Element.html#hasOwnedElement()), [hasTaggedValue](../classes/mdkernel/Element.html#hasTaggedValue()), [setOwner](../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [setSyncElement](../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.nomagic.magicdraw.foundation.[MDObject](../../../../magicdraw/foundation/MDObject.html)
`[getID](../../../../magicdraw/foundation/MDObject.html#getID()), [getMDExtension](../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)), [getMdExtensions](../../../../magicdraw/foundation/MDObject.html#getMdExtensions()), [setID](../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String))`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement
`canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.[ModelObject](../base/ModelObject.html)
`[get_representationText](../base/ModelObject.html#get_representationText()), [ignoringRefGetValue](../base/ModelObject.html#ignoringRefGetValue(java.lang.String)), [ignoringRefGetValue](../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)), [isSet](../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)), [refGetValue](../base/ModelObject.html#refGetValue(java.lang.String)), [refGetValue](../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)), [refSetValue](../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)), [refSetValue](../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)), [set_representationText](../base/ModelObject.html#set_representationText(java.lang.String))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[NamedElement](../classes/mdkernel/NamedElement.html)
`[get_considerIgnoreFragmentOfMessage](../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()), [get_durationObservationOfEvent](../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()), [get_informationFlowOfInformationSource](../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()), [get_informationFlowOfInformationTarget](../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()), [get_messageOfSignature](../classes/mdkernel/NamedElement.html#get_messageOfSignature()), [get_namespaceOfMember](../classes/mdkernel/NamedElement.html#get_namespaceOfMember()), [get_timeObservationOfEvent](../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()), [getClientDependency](../classes/mdkernel/NamedElement.html#getClientDependency()), [getName](../classes/mdkernel/NamedElement.html#getName()), [getNameExpression](../classes/mdkernel/NamedElement.html#getNameExpression()), [getNamespace](../classes/mdkernel/NamedElement.html#getNamespace()), [getQualifiedName](../classes/mdkernel/NamedElement.html#getQualifiedName()), [getSupplierDependency](../classes/mdkernel/NamedElement.html#getSupplierDependency()), [getVisibility](../classes/mdkernel/NamedElement.html#getVisibility()), [has_considerIgnoreFragmentOfMessage](../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()), [has_durationObservationOfEvent](../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()), [has_informationFlowOfInformationSource](../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()), [has_informationFlowOfInformationTarget](../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()), [has_messageOfSignature](../classes/mdkernel/NamedElement.html#has_messageOfSignature()), [has_namespaceOfMember](../classes/mdkernel/NamedElement.html#has_namespaceOfMember()), [has_timeObservationOfEvent](../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()), [hasClientDependency](../classes/mdkernel/NamedElement.html#hasClientDependency()), [hasSupplierDependency](../classes/mdkernel/NamedElement.html#hasSupplierDependency()), [setName](../classes/mdkernel/NamedElement.html#setName(java.lang.String)), [setNameExpression](../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)), [setNamespace](../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)), [setVisibility](../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[RedefinableElement](../classes/mdkernel/RedefinableElement.html)
`[get_redefinableElementOfRedefinedElement](../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()), [getRedefinedElement](../classes/mdkernel/RedefinableElement.html#getRedefinedElement()), [getRedefinitionContext](../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()), [has_redefinableElementOfRedefinedElement](../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()), [hasRedefinedElement](../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()), [hasRedefinitionContext](../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()), [isLeaf](../classes/mdkernel/RedefinableElement.html#isLeaf()), [setLeaf](../classes/mdkernel/RedefinableElement.html#setLeaf(boolean))`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`

============ METHOD DETAIL ========== 
Method Details
getUseCase
@CheckForNull[UseCase](UseCase.html) getUseCase()
Returns the value of the '***Use Case***' container reference.
 It is bidirectional and its opposite is '[`*Extension Point*`](UseCase.html#getExtensionPoint())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 The UseCase that owns this ExtensionPoint.
 end-model-doc
Returns:
the value of the '*Use Case*' container reference.
See Also:
[`setUseCase(UseCase)`](#setUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))
[`UMLPackage.getExtensionPoint_UseCase()`](../metadata/UMLPackage.html#getExtensionPoint_UseCase())
[`UseCase.getExtensionPoint()`](UseCase.html#getExtensionPoint())
Model:
opposite="extensionPoint" required="true" transient="false" ordered="false"
Generated:
setUseCase
void setUseCase(@CheckForNull
 [UseCase](UseCase.html) value)
Sets the value of the '[`*Use Case*`](#getUseCase())' container reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Use Case*' container reference.
See Also:
[`getUseCase()`](#getUseCase())
Generated:
getExtension
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Extend](Extend.html)> getExtension()
Returns the value of the '***Extension***' reference list.
 The list contents are of type [`Extend`](Extend.html).
 It is bidirectional and its opposite is '[`*Extension Location*`](Extend.html#getExtensionLocation())'.
 begin-user-doc 
If the meaning of the '*Extension*' reference list isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*Extension*' reference list.
See Also:
[`UMLPackage.getExtensionPoint_Extension()`](../metadata/UMLPackage.html#getExtensionPoint_Extension())
[`Extend.getExtensionLocation()`](Extend.html#getExtensionLocation())
Model:
opposite="extensionLocation" ordered="false"
Generated:
hasExtension
boolean hasExtension()
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.mdusecases</a></div>
<h1 class="title" title="Interface ExtensionPoint">Interface ExtensionPoint</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code><a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ExtensionPoint</span><span class="extends-implements">
extends <a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Extension Point</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An ExtensionPoint identifies a point in the behavior of a UseCase where that behavior can be extended by the behavior of some other (extending) UseCase, as
 specified by an Extend relationship.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getExtension()"><code><em>Extension</em></code></a></li>
<li><a href="#getUseCase()"><code><em>Use Case</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../metadata/UMLPackage.html#getExtensionPoint()"><code>UMLPackage.getExtensionPoint()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>annotation="MOF package='mdusecases'"</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExtension()">getExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Extension</b></em>' reference list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUseCase()">getUseCase</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Use Case</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasExtension()">hasExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">setUseCase</a><wbr/>(<a href="UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getUseCase()"><code><em>Use Case</em></code></a>' container reference.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></h3>
<code><a href="../classes/mdkernel/Element.html#get_activityPartitionOfRepresents()">get_activityPartitionOfRepresents</a>, <a href="../classes/mdkernel/Element.html#get_commentOfAnnotatedElement()">get_commentOfAnnotatedElement</a>, <a href="../classes/mdkernel/Element.html#get_constraintOfConstrainedElement()">get_constraintOfConstrainedElement</a>, <a href="../classes/mdkernel/Element.html#get_diagramOfContext()">get_diagramOfContext</a>, <a href="../classes/mdkernel/Element.html#get_directedRelationshipOfSource()">get_directedRelationshipOfSource</a>, <a href="../classes/mdkernel/Element.html#get_directedRelationshipOfTarget()">get_directedRelationshipOfTarget</a>, <a href="../classes/mdkernel/Element.html#get_elementOfSyncElement()">get_elementOfSyncElement</a>, <a href="../classes/mdkernel/Element.html#get_elementTaggedValue()">get_elementTaggedValue</a>, <a href="../classes/mdkernel/Element.html#get_elementValueOfElement()">get_elementValueOfElement</a>, <a href="../classes/mdkernel/Element.html#get_relationshipOfRelatedElement()">get_relationshipOfRelatedElement</a>, <a href="../classes/mdkernel/Element.html#getAppliedStereotype()">getAppliedStereotype</a>, <a href="../classes/mdkernel/Element.html#getOwnedComment()">getOwnedComment</a>, <a href="../classes/mdkernel/Element.html#getOwnedElement()">getOwnedElement</a>, <a href="../classes/mdkernel/Element.html#getOwner()">getOwner</a>, <a href="../classes/mdkernel/Element.html#getSyncElement()">getSyncElement</a>, <a href="../classes/mdkernel/Element.html#getTaggedValue()">getTaggedValue</a>, <a href="../classes/mdkernel/Element.html#has_activityPartitionOfRepresents()">has_activityPartitionOfRepresents</a>, <a href="../classes/mdkernel/Element.html#has_commentOfAnnotatedElement()">has_commentOfAnnotatedElement</a>, <a href="../classes/mdkernel/Element.html#has_constraintOfConstrainedElement()">has_constraintOfConstrainedElement</a>, <a href="../classes/mdkernel/Element.html#has_diagramOfContext()">has_diagramOfContext</a>, <a href="../classes/mdkernel/Element.html#has_directedRelationshipOfSource()">has_directedRelationshipOfSource</a>, <a href="../classes/mdkernel/Element.html#has_directedRelationshipOfTarget()">has_directedRelationshipOfTarget</a>, <a href="../classes/mdkernel/Element.html#has_elementOfSyncElement()">has_elementOfSyncElement</a>, <a href="../classes/mdkernel/Element.html#has_elementValueOfElement()">has_elementValueOfElement</a>, <a href="../classes/mdkernel/Element.html#has_relationshipOfRelatedElement()">has_relationshipOfRelatedElement</a>, <a href="../classes/mdkernel/Element.html#hasAppliedStereotype()">hasAppliedStereotype</a>, <a href="../classes/mdkernel/Element.html#hasElementTaggedValue()">hasElementTaggedValue</a>, <a href="../classes/mdkernel/Element.html#hasOwnedComment()">hasOwnedComment</a>, <a href="../classes/mdkernel/Element.html#hasOwnedElement()">hasOwnedElement</a>, <a href="../classes/mdkernel/Element.html#hasTaggedValue()">hasTaggedValue</a>, <a href="../classes/mdkernel/Element.html#setOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setOwner</a>, <a href="../classes/mdkernel/Element.html#setSyncElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setSyncElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.foundation.MDObject">Methods inherited from interface com.nomagic.magicdraw.foundation.<a href="../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></h3>
<code><a href="../../../../magicdraw/foundation/MDObject.html#getID()">getID</a>, <a href="../../../../magicdraw/foundation/MDObject.html#getMDExtension(java.lang.String)">getMDExtension</a>, <a href="../../../../magicdraw/foundation/MDObject.html#getMdExtensions()">getMdExtensions</a>, <a href="../../../../magicdraw/foundation/MDObject.html#setID(java.lang.String)">setID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.ModelElement</h3>
<code>canChangeElementOwner, eDynamicGet, getElementOwner, getLocalID, getObjectParent, setLocalID, sGetLocalID</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.base.ModelObject">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.base.<a href="../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></h3>
<code><a href="../base/ModelObject.html#get_representationText()">get_representationText</a>, <a href="../base/ModelObject.html#ignoringRefGetValue(java.lang.String)">ignoringRefGetValue</a>, <a href="../base/ModelObject.html#ignoringRefGetValue(java.lang.String,java.lang.Object)">ignoringRefGetValue</a>, <a href="../base/ModelObject.html#isSet(java.lang.String,java.lang.Object)">isSet</a>, <a href="../base/ModelObject.html#refGetValue(java.lang.String)">refGetValue</a>, <a href="../base/ModelObject.html#refGetValue(java.lang.String,java.lang.Object)">refGetValue</a>, <a href="../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object)">refSetValue</a>, <a href="../base/ModelObject.html#refSetValue(java.lang.String,java.lang.Object,java.lang.Object)">refSetValue</a>, <a href="../base/ModelObject.html#set_representationText(java.lang.String)">set_representationText</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.NamedElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a></h3>
<code><a href="../classes/mdkernel/NamedElement.html#get_considerIgnoreFragmentOfMessage()">get_considerIgnoreFragmentOfMessage</a>, <a href="../classes/mdkernel/NamedElement.html#get_durationObservationOfEvent()">get_durationObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationSource()">get_informationFlowOfInformationSource</a>, <a href="../classes/mdkernel/NamedElement.html#get_informationFlowOfInformationTarget()">get_informationFlowOfInformationTarget</a>, <a href="../classes/mdkernel/NamedElement.html#get_messageOfSignature()">get_messageOfSignature</a>, <a href="../classes/mdkernel/NamedElement.html#get_namespaceOfMember()">get_namespaceOfMember</a>, <a href="../classes/mdkernel/NamedElement.html#get_timeObservationOfEvent()">get_timeObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#getClientDependency()">getClientDependency</a>, <a href="../classes/mdkernel/NamedElement.html#getName()">getName</a>, <a href="../classes/mdkernel/NamedElement.html#getNameExpression()">getNameExpression</a>, <a href="../classes/mdkernel/NamedElement.html#getNamespace()">getNamespace</a>, <a href="../classes/mdkernel/NamedElement.html#getQualifiedName()">getQualifiedName</a>, <a href="../classes/mdkernel/NamedElement.html#getSupplierDependency()">getSupplierDependency</a>, <a href="../classes/mdkernel/NamedElement.html#getVisibility()">getVisibility</a>, <a href="../classes/mdkernel/NamedElement.html#has_considerIgnoreFragmentOfMessage()">has_considerIgnoreFragmentOfMessage</a>, <a href="../classes/mdkernel/NamedElement.html#has_durationObservationOfEvent()">has_durationObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationSource()">has_informationFlowOfInformationSource</a>, <a href="../classes/mdkernel/NamedElement.html#has_informationFlowOfInformationTarget()">has_informationFlowOfInformationTarget</a>, <a href="../classes/mdkernel/NamedElement.html#has_messageOfSignature()">has_messageOfSignature</a>, <a href="../classes/mdkernel/NamedElement.html#has_namespaceOfMember()">has_namespaceOfMember</a>, <a href="../classes/mdkernel/NamedElement.html#has_timeObservationOfEvent()">has_timeObservationOfEvent</a>, <a href="../classes/mdkernel/NamedElement.html#hasClientDependency()">hasClientDependency</a>, <a href="../classes/mdkernel/NamedElement.html#hasSupplierDependency()">hasSupplierDependency</a>, <a href="../classes/mdkernel/NamedElement.html#setName(java.lang.String)">setName</a>, <a href="../classes/mdkernel/NamedElement.html#setNameExpression(com.nomagic.uml2.ext.magicdraw.auxiliaryconstructs.mdtemplates.StringExpression)">setNameExpression</a>, <a href="../classes/mdkernel/NamedElement.html#setNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setNamespace</a>, <a href="../classes/mdkernel/NamedElement.html#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.RedefinableElement">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="../classes/mdkernel/RedefinableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">RedefinableElement</a></h3>
<code><a href="../classes/mdkernel/RedefinableElement.html#get_redefinableElementOfRedefinedElement()">get_redefinableElementOfRedefinedElement</a>, <a href="../classes/mdkernel/RedefinableElement.html#getRedefinedElement()">getRedefinedElement</a>, <a href="../classes/mdkernel/RedefinableElement.html#getRedefinitionContext()">getRedefinitionContext</a>, <a href="../classes/mdkernel/RedefinableElement.html#has_redefinableElementOfRedefinedElement()">has_redefinableElementOfRedefinedElement</a>, <a href="../classes/mdkernel/RedefinableElement.html#hasRedefinedElement()">hasRedefinedElement</a>, <a href="../classes/mdkernel/RedefinableElement.html#hasRedefinitionContext()">hasRedefinitionContext</a>, <a href="../classes/mdkernel/RedefinableElement.html#isLeaf()">isLeaf</a>, <a href="../classes/mdkernel/RedefinableElement.html#setLeaf(boolean)">setLeaf</a></code></div>
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
<section class="detail" id="getUseCase()">
<h3>getUseCase</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></span> <span class="element-name">getUseCase</span>()</div>
<div class="block">Returns the value of the '<em><b>Use Case</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="UseCase.html#getExtensionPoint()"><code><em>Extension Point</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 The UseCase that owns this ExtensionPoint.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Use Case</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#setUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)"><code>setUseCase(UseCase)</code></a></li>
<li><a href="../metadata/UMLPackage.html#getExtensionPoint_UseCase()"><code>UMLPackage.getExtensionPoint_UseCase()</code></a></li>
<li><a href="UseCase.html#getExtensionPoint()"><code>UseCase.getExtensionPoint()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="extensionPoint" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseCase(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>setUseCase</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUseCase</span><wbr/><span class="parameters">(@CheckForNull
 <a href="UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getUseCase()"><code><em>Use Case</em></code></a>' container reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Use Case</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#getUseCase()"><code>getUseCase()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtension()">
<h3>getExtension</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">Extend</a>&gt;</span> <span class="element-name">getExtension</span>()</div>
<div class="block">Returns the value of the '<em><b>Extension</b></em>' reference list.
 The list contents are of type <a href="Extend.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases"><code>Extend</code></a>.
 It is bidirectional and its opposite is '<a href="Extend.html#getExtensionLocation()"><code><em>Extension Location</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>Extension</em>' reference list isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Extension</em>' reference list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../metadata/UMLPackage.html#getExtensionPoint_Extension()"><code>UMLPackage.getExtensionPoint_Extension()</code></a></li>
<li><a href="Extend.html#getExtensionLocation()"><code>Extend.getExtensionLocation()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="extensionLocation" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasExtension()">
<h3>hasExtension</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasExtension</span>()
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
