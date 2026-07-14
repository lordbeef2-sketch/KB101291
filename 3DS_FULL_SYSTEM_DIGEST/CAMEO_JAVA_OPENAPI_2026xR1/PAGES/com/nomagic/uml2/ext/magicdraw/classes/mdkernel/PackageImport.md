# JAVA OPENAPI: PackageImport (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/PackageImport.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/PackageImport.html`
- source_sha256: `7cef3a87dbd141bebb099b46715e40db912f8ec2cf6be28bdb45fc274519c580`
- captured_utc: `2026-07-14T16:46:29.642193+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface PackageImport

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[DirectedRelationship](DirectedRelationship.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `[ModelElement](../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html)`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[Relationship](Relationship.html)`

public interfacePackageImportextends [DirectedRelationship](DirectedRelationship.html)

begin-user-doc 
 A representation of the model object '***Package Import***'.
 end-user-doc 
begin-model-doc 
 A PackageImport is a Relationship that imports all the non-private members of a Package into the Namespace owning the PackageImport, so that those Elements may be
 referred to by their unqualified names in the importingNamespace.
 end-model-doc 
The following features are supported:
 [`*Importing Namespace*`](#getImportingNamespace())
[`*Visibility*`](#getVisibility())
[`*profile Of Metamodel Reference*`](#get_profileOfMetamodelReference())
[`*Imported Package*`](#getImportedPackage())

See Also:
[`UMLPackage.getPackageImport()`](../../metadata/UMLPackage.html#getPackageImport())
Model:
annotation="MOF package='classes.mdkernel'"
Generated:

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Profile](../../mdprofiles/Profile.html)`
`[get_profileOfMetamodelReference](#get_profileOfMetamodelReference())()`
Returns the value of the '***profile Of Metamodel Reference***' reference.
`[Package](Package.html)`
`[getImportedPackage](#getImportedPackage())()`
Returns the value of the '***Imported Package***' reference.
`[Namespace](Namespace.html)`
`[getImportingNamespace](#getImportingNamespace())()`
Returns the value of the '***Importing Namespace***' container reference.
`[VisibilityKind](VisibilityKind.html)`
`[getVisibility](#getVisibility())()`
Returns the value of the '***Visibility***' attribute.
`void`
`[set_profileOfMetamodelReference](#set_profileOfMetamodelReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Profile](../../mdprofiles/Profile.html) value)`
Sets the value of the
 '[`*profile Of Metamodel Reference*`](#get_profileOfMetamodelReference())' reference.
`void`
`[setImportedPackage](#setImportedPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](Package.html) value)`
Sets the value of the '[`*Imported Package*`](#getImportedPackage())' reference.
`void`
`[setImportingNamespace](#setImportingNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))([Namespace](Namespace.html) value)`
Sets the value of the '[`*Importing Namespace*`](#getImportingNamespace())' container
 reference.
`void`
`[setVisibility](#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))([VisibilityKind](VisibilityKind.html) value)`
Sets the value of the '[`*Visibility*`](#getVisibility())' attribute.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../magicdraw/uml/BaseElement.html)
`[accept](../../../../../magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../magicdraw/uml/BaseElement.html#getHumanType()), [isEditable](../../../../../magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [sGetID](../../../../../magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[DirectedRelationship](DirectedRelationship.html)
`[getSource](DirectedRelationship.html#getSource()), [getTarget](DirectedRelationship.html#getTarget()), [hasSource](DirectedRelationship.html#hasSource()), [hasTarget](DirectedRelationship.html#hasTarget())`
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
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface javax.jmi.reflect.RefBaseObject
`equals, hashCode, refImmediatePackage, refMetaObject, refMofId, refOutermostPackage, refVerifyConstraints`
Methods inherited from interface javax.jmi.reflect.RefFeatured
`refGetValue, refInvokeOperation, refInvokeOperation, refSetValue`
Methods inherited from interface javax.jmi.reflect.RefObject
`refClass, refDelete, refImmediateComposite, refIsInstanceOf, refOutermostComposite`
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Relationship](Relationship.html)
`[get_abstraction](Relationship.html#get_abstraction()), [getRelatedElement](Relationship.html#getRelatedElement()), [has_abstraction](Relationship.html#has_abstraction()), [hasRelatedElement](Relationship.html#hasRelatedElement())`

============ METHOD DETAIL ========== 
Method Details
getImportedPackage
@CheckForNull[Package](Package.html) getImportedPackage()
Returns the value of the '***Imported Package***' reference.
 It is bidirectional and its opposite is
 '[`*package Import Of Imported Package*`](Package.html#get_packageImportOfImportedPackage())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the Package whose members are imported into a Namespace.
 end-model-doc
Returns:
the value of the '*Imported Package*' reference.
See Also:
[`setImportedPackage(Package)`](#setImportedPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))
[`UMLPackage.getPackageImport_ImportedPackage()`](../../metadata/UMLPackage.html#getPackageImport_ImportedPackage())
[`Package.get_packageImportOfImportedPackage()`](Package.html#get_packageImportOfImportedPackage())
Model:
opposite="_packageImportOfImportedPackage" required="true" ordered="false"
Generated:
setImportedPackage
void setImportedPackage(@CheckForNull
 [Package](Package.html) value)
Sets the value of the '[`*Imported Package*`](#getImportedPackage())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Imported Package*' reference.
See Also:
[`getImportedPackage()`](#getImportedPackage())
Generated:
get_profileOfMetamodelReference
@CheckForNull[Profile](../../mdprofiles/Profile.html) get_profileOfMetamodelReference()
Returns the value of the '***profile Of Metamodel Reference***' reference.
 It is bidirectional and its opposite is '[`*Metamodel Reference*`](../../mdprofiles/Profile.html#getMetamodelReference())'.
 begin-user-doc 
If the meaning of the '*profile Of Metamodel Reference*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*profile Of Metamodel Reference*' reference.
See Also:
[`set_profileOfMetamodelReference(Profile)`](#set_profileOfMetamodelReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))
[`UMLPackage.getPackageImport__profileOfMetamodelReference()`](../../metadata/UMLPackage.html#getPackageImport__profileOfMetamodelReference())
[`Profile.getMetamodelReference()`](../../mdprofiles/Profile.html#getMetamodelReference())
Model:
opposite="metamodelReference" ordered="false"
Generated:
set_profileOfMetamodelReference
void set_profileOfMetamodelReference(@CheckForNull
 [Profile](../../mdprofiles/Profile.html) value)
Sets the value of the
 '[`*profile Of Metamodel Reference*`](#get_profileOfMetamodelReference())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*profile Of Metamodel Reference*' reference.
See Also:
[`get_profileOfMetamodelReference()`](#get_profileOfMetamodelReference())
Generated:
getImportingNamespace
@CheckForNull[Namespace](Namespace.html) getImportingNamespace()
Returns the value of the '***Importing Namespace***' container reference.
 It is bidirectional and its opposite is '[`*Package Import*`](Namespace.html#getPackageImport())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the Namespace that imports the members from a Package.
 end-model-doc
Returns:
the value of the '*Importing Namespace*' container reference.
See Also:
[`setImportingNamespace(Namespace)`](#setImportingNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))
[`UMLPackage.getPackageImport_ImportingNamespace()`](../../metadata/UMLPackage.html#getPackageImport_ImportingNamespace())
[`Namespace.getPackageImport()`](Namespace.html#getPackageImport())
Model:
opposite="packageImport" required="true" transient="false" ordered="false"
Generated:
setImportingNamespace
void setImportingNamespace(@CheckForNull
 [Namespace](Namespace.html) value)
Sets the value of the '[`*Importing Namespace*`](#getImportingNamespace())' container
 reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Importing Namespace*' container reference.
See Also:
[`getImportingNamespace()`](#getImportingNamespace())
Generated:
getVisibility
@CheckForNull[VisibilityKind](VisibilityKind.html) getVisibility()
Returns the value of the '***Visibility***' attribute.
 The default value is `"public"`.
 The literals are from the enumeration [`VisibilityKind`](VisibilityKind.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the visibility of the imported PackageableElements within the importingNamespace, i.e., whether imported Elements will in turn be visible to other
 Namespaces. If the PackageImport is public, the imported Elements will be visible outside the importingNamespace, while, if the PackageImport is private, they
 will not.
 end-model-doc
Returns:
the value of the '*Visibility*' attribute.
See Also:
[`VisibilityKind`](VisibilityKind.html)
[`setVisibility(VisibilityKind)`](#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))
[`UMLPackage.getPackageImport_Visibility()`](../../metadata/UMLPackage.html#getPackageImport_Visibility())
Model:
default="public" required="true" ordered="false"
Generated:
setVisibility
void setVisibility(@CheckForNull
 [VisibilityKind](VisibilityKind.html) value)
Sets the value of the '[`*Visibility*`](#getVisibility())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Visibility*' attribute.
See Also:
[`VisibilityKind`](VisibilityKind.html)
[`getVisibility()`](#getVisibility())
Generated:

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface PackageImport">Interface PackageImport</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code><a href="../../../../../../dassault_systemes/modeler/foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">PackageImport</span><span class="extends-implements">
extends <a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Package Import</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 A PackageImport is a Relationship that imports all the non-private members of a Package into the Namespace owning the PackageImport, so that those Elements may be
 referred to by their unqualified names in the importingNamespace.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getImportingNamespace()"><code><em>Importing Namespace</em></code></a></li>
<li><a href="#getVisibility()"><code><em>Visibility</em></code></a></li>
<li><a href="#get_profileOfMetamodelReference()"><code><em>profile Of Metamodel Reference</em></code></a></li>
<li><a href="#getImportedPackage()"><code><em>Imported Package</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getPackageImport()"><code>UMLPackage.getPackageImport()</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_profileOfMetamodelReference()">get_profileOfMetamodelReference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>profile Of Metamodel Reference</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportedPackage()">getImportedPackage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Imported Package</b></em>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportingNamespace()">getImportingNamespace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Importing Namespace</b></em>' container reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVisibility()">getVisibility</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Visibility</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_profileOfMetamodelReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">set_profileOfMetamodelReference</a><wbr/>(<a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_profileOfMetamodelReference()"><code><em>profile Of Metamodel Reference</em></code></a>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setImportedPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">setImportedPackage</a><wbr/>(<a href="Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getImportedPackage()"><code><em>Imported Package</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setImportingNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">setImportingNamespace</a><wbr/>(<a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getImportingNamespace()"><code><em>Importing Namespace</em></code></a>' container
 reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">setVisibility</a><wbr/>(<a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getVisibility()"><code><em>Visibility</em></code></a>' attribute.</div>
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
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.DirectedRelationship">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></h3>
<code><a href="DirectedRelationship.html#getSource()">getSource</a>, <a href="DirectedRelationship.html#getTarget()">getTarget</a>, <a href="DirectedRelationship.html#hasSource()">hasSource</a>, <a href="DirectedRelationship.html#hasTarget()">hasTarget</a></code></div>
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
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Relationship">Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.<a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></h3>
<code><a href="Relationship.html#get_abstraction()">get_abstraction</a>, <a href="Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="Relationship.html#has_abstraction()">has_abstraction</a>, <a href="Relationship.html#hasRelatedElement()">hasRelatedElement</a></code></div>
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
<section class="detail" id="getImportedPackage()">
<h3>getImportedPackage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getImportedPackage</span>()</div>
<div class="block">Returns the value of the '<em><b>Imported Package</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="Package.html#get_packageImportOfImportedPackage()"><code><em>package Import Of Imported Package</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the Package whose members are imported into a Namespace.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Imported Package</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setImportedPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)"><code>setImportedPackage(Package)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getPackageImport_ImportedPackage()"><code>UMLPackage.getPackageImport_ImportedPackage()</code></a></li>
<li><a href="Package.html#get_packageImportOfImportedPackage()"><code>Package.get_packageImportOfImportedPackage()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_packageImportOfImportedPackage" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImportedPackage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>setImportedPackage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setImportedPackage</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getImportedPackage()"><code><em>Imported Package</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Imported Package</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getImportedPackage()"><code>getImportedPackage()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_profileOfMetamodelReference()">
<h3>get_profileOfMetamodelReference</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">get_profileOfMetamodelReference</span>()</div>
<div class="block">Returns the value of the '<em><b>profile Of Metamodel Reference</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../mdprofiles/Profile.html#getMetamodelReference()"><code><em>Metamodel Reference</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>profile Of Metamodel Reference</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>profile Of Metamodel Reference</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_profileOfMetamodelReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)"><code>set_profileOfMetamodelReference(Profile)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getPackageImport__profileOfMetamodelReference()"><code>UMLPackage.getPackageImport__profileOfMetamodelReference()</code></a></li>
<li><a href="../../mdprofiles/Profile.html#getMetamodelReference()"><code>Profile.getMetamodelReference()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="metamodelReference" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_profileOfMetamodelReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>set_profileOfMetamodelReference</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_profileOfMetamodelReference</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_profileOfMetamodelReference()"><code><em>profile Of Metamodel Reference</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>profile Of Metamodel Reference</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#get_profileOfMetamodelReference()"><code>get_profileOfMetamodelReference()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImportingNamespace()">
<h3>getImportingNamespace</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></span> <span class="element-name">getImportingNamespace</span>()</div>
<div class="block">Returns the value of the '<em><b>Importing Namespace</b></em>' container reference.
 It is bidirectional and its opposite is '<a href="Namespace.html#getPackageImport()"><code><em>Package Import</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the Namespace that imports the members from a Package.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Importing Namespace</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setImportingNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)"><code>setImportingNamespace(Namespace)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getPackageImport_ImportingNamespace()"><code>UMLPackage.getPackageImport_ImportingNamespace()</code></a></li>
<li><a href="Namespace.html#getPackageImport()"><code>Namespace.getPackageImport()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="packageImport" required="true" transient="false" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImportingNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)">
<h3>setImportingNamespace</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setImportingNamespace</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getImportingNamespace()"><code><em>Importing Namespace</em></code></a>' container
 reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Importing Namespace</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getImportingNamespace()"><code>getImportingNamespace()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibility()">
<h3>getVisibility</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a></span> <span class="element-name">getVisibility</span>()</div>
<div class="block">Returns the value of the '<em><b>Visibility</b></em>' attribute.
 The default value is <code>"public"</code>.
 The literals are from the enumeration <a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>VisibilityKind</code></a>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the visibility of the imported PackageableElements within the importingNamespace, i.e., whether imported Elements will in turn be visible to other
 Namespaces. If the PackageImport is public, the imported Elements will be visible outside the importingNamespace, while, if the PackageImport is private, they
 will not.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Visibility</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>VisibilityKind</code></a></li>
<li><a href="#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)"><code>setVisibility(VisibilityKind)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getPackageImport_Visibility()"><code>UMLPackage.getPackageImport_Visibility()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="public" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">
<h3>setVisibility</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setVisibility</span><wbr/><span class="parameters">(@CheckForNull
 <a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getVisibility()"><code><em>Visibility</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Visibility</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>VisibilityKind</code></a></li>
<li><a href="#getVisibility()"><code>getVisibility()</code></a></li>
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
