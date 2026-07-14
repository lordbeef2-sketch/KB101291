# JAVA OPENAPI: ElementImport (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/magicdraw/classes/mdkernel/ElementImport.html
- source_path: `com/nomagic/uml2/ext/magicdraw/classes/mdkernel/ElementImport.html`
- source_sha256: `4b78521a6a553ddb1cc3884b4f37d0ecdff2bc5ca96df43fc96250215cdb104b`
- captured_utc: `2026-07-14T16:58:52.792456+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.magicdraw.classes.mdkernel](package-summary.html)

## Interface ElementImport

All Superinterfaces:
`[BaseElement](../../../../../magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[DirectedRelationship](DirectedRelationship.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[MDObject](../../../../../magicdraw/foundation/MDObject.html)`, `com.dassault_systemes.modeler.foundation.model.ModelElement`, `[ModelObject](../../base/ModelObject.html)`, `org.eclipse.emf.common.notify.Notifier`, `javax.jmi.reflect.RefBaseObject`, `javax.jmi.reflect.RefFeatured`, `javax.jmi.reflect.RefObject`, `[Relationship](Relationship.html)`

public interfaceElementImportextends [DirectedRelationship](DirectedRelationship.html)

begin-user-doc 
 A representation of the model object '***Element Import***'.
 end-user-doc 
begin-model-doc 
 An ElementImport identifies a NamedElement in a Namespace other than the one that owns that NamedElement and allows the NamedElement to be referenced using an
 unqualified name in the Namespace owning the ElementImport.
 end-model-doc 
The following features are supported:
 [`*Alias*`](#getAlias())
[`*Imported Element*`](#getImportedElement())
[`*Visibility*`](#getVisibility())
[`*profile Of Metaclass Reference*`](#get_profileOfMetaclassReference())
[`*Importing Namespace*`](#getImportingNamespace())

See Also:
[`UMLPackage.getElementImport()`](../../metadata/UMLPackage.html#getElementImport())
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
`[get_profileOfMetaclassReference](#get_profileOfMetaclassReference())()`
Returns the value of the '***profile Of Metaclass Reference***' reference.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getAlias](#getAlias())()`
Returns the value of the '***Alias***' attribute.
`[PackageableElement](PackageableElement.html)`
`[getImportedElement](#getImportedElement())()`
Returns the value of the '***Imported Element***' reference.
`[Namespace](Namespace.html)`
`[getImportingNamespace](#getImportingNamespace())()`
Returns the value of the '***Importing Namespace***' container reference.
`[VisibilityKind](VisibilityKind.html)`
`[getVisibility](#getVisibility())()`
Returns the value of the '***Visibility***' attribute.
`void`
`[set_profileOfMetaclassReference](#set_profileOfMetaclassReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))([Profile](../../mdprofiles/Profile.html) value)`
Sets the value of the
 '[`*profile Of Metaclass Reference*`](#get_profileOfMetaclassReference())' reference.
`void`
`[setAlias](#setAlias(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the value of the '[`*Alias*`](#getAlias())' attribute.
`void`
`[setImportedElement](#setImportedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement))([PackageableElement](PackageableElement.html) value)`
Sets the value of the '[`*Imported Element*`](#getImportedElement())' reference.
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
Methods inherited from interface com.nomagic.uml2.ext.magicdraw.classes.mdkernel.[Relationship](Relationship.html)
`[get_abstraction](Relationship.html#get_abstraction()), [getRelatedElement](Relationship.html#getRelatedElement()), [has_abstraction](Relationship.html#has_abstraction()), [hasRelatedElement](Relationship.html#hasRelatedElement())`

============ METHOD DETAIL ========== 
Method Details
getVisibility
@CheckForNull[VisibilityKind](VisibilityKind.html) getVisibility()
Returns the value of the '***Visibility***' attribute.
 The default value is `"public"`.
 The literals are from the enumeration [`VisibilityKind`](VisibilityKind.html).
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the visibility of the imported PackageableElement within the importingNamespace, i.e., whether the importedElement will in turn be visible to other
 Namespaces. If the ElementImport is public, the importedElement will be visible outside the importingNamespace while, if the ElementImport is private, it will
 not.
 end-model-doc
Returns:
the value of the '*Visibility*' attribute.
See Also:
[`VisibilityKind`](VisibilityKind.html)
[`setVisibility(VisibilityKind)`](#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))
[`UMLPackage.getElementImport_Visibility()`](../../metadata/UMLPackage.html#getElementImport_Visibility())
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
getAlias
@CheckForNull[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getAlias()
Returns the value of the '***Alias***' attribute.
 The default value is `""`.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the name that should be added to the importing Namespace in lieu of the name of the imported PackagableElement. The alias must not clash with any other
 member in the importing Namespace. By default, no alias is used.
 end-model-doc
Returns:
the value of the '*Alias*' attribute.
See Also:
[`setAlias(String)`](#setAlias(java.lang.String))
[`UMLPackage.getElementImport_Alias()`](../../metadata/UMLPackage.html#getElementImport_Alias())
Model:
default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"
Generated:
setAlias
void setAlias(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the value of the '[`*Alias*`](#getAlias())' attribute.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Alias*' attribute.
See Also:
[`getAlias()`](#getAlias())
Generated:
getImportedElement
@CheckForNull[PackageableElement](PackageableElement.html) getImportedElement()
Returns the value of the '***Imported Element***' reference.
 It is bidirectional and its opposite is
 '[`*element Import Of Imported Element*`](PackageableElement.html#get_elementImportOfImportedElement())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the PackageableElement whose name is to be added to a Namespace.
 end-model-doc
Returns:
the value of the '*Imported Element*' reference.
See Also:
[`setImportedElement(PackageableElement)`](#setImportedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement))
[`UMLPackage.getElementImport_ImportedElement()`](../../metadata/UMLPackage.html#getElementImport_ImportedElement())
[`PackageableElement.get_elementImportOfImportedElement()`](PackageableElement.html#get_elementImportOfImportedElement())
Model:
opposite="_elementImportOfImportedElement" required="true" ordered="false"
Generated:
setImportedElement
void setImportedElement(@CheckForNull
 [PackageableElement](PackageableElement.html) value)
Sets the value of the '[`*Imported Element*`](#getImportedElement())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*Imported Element*' reference.
See Also:
[`getImportedElement()`](#getImportedElement())
Generated:
get_profileOfMetaclassReference
@CheckForNull[Profile](../../mdprofiles/Profile.html) get_profileOfMetaclassReference()
Returns the value of the '***profile Of Metaclass Reference***' reference.
 It is bidirectional and its opposite is '[`*Metaclass Reference*`](../../mdprofiles/Profile.html#getMetaclassReference())'.
 begin-user-doc 
If the meaning of the '*profile Of Metaclass Reference*' reference isn't clear,
 there really should be more of a description here...
 end-user-doc
Returns:
the value of the '*profile Of Metaclass Reference*' reference.
See Also:
[`set_profileOfMetaclassReference(Profile)`](#set_profileOfMetaclassReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile))
[`UMLPackage.getElementImport__profileOfMetaclassReference()`](../../metadata/UMLPackage.html#getElementImport__profileOfMetaclassReference())
[`Profile.getMetaclassReference()`](../../mdprofiles/Profile.html#getMetaclassReference())
Model:
opposite="metaclassReference" ordered="false"
Generated:
set_profileOfMetaclassReference
void set_profileOfMetaclassReference(@CheckForNull
 [Profile](../../mdprofiles/Profile.html) value)
Sets the value of the
 '[`*profile Of Metaclass Reference*`](#get_profileOfMetaclassReference())' reference.
 begin-user-doc 
 end-user-doc
Parameters:
`value` - the new value of the '*profile Of Metaclass Reference*' reference.
See Also:
[`get_profileOfMetaclassReference()`](#get_profileOfMetaclassReference())
Generated:
getImportingNamespace
@CheckForNull[Namespace](Namespace.html) getImportingNamespace()
Returns the value of the '***Importing Namespace***' container reference.
 It is bidirectional and its opposite is '[`*Element Import*`](Namespace.html#getElementImport())'.
 begin-user-doc 
 end-user-doc 
 begin-model-doc 
 Specifies the Namespace that imports a PackageableElement from another Namespace.
 end-model-doc
Returns:
the value of the '*Importing Namespace*' container reference.
See Also:
[`setImportingNamespace(Namespace)`](#setImportingNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace))
[`UMLPackage.getElementImport_ImportingNamespace()`](../../metadata/UMLPackage.html#getElementImport_ImportingNamespace())
[`Namespace.getElementImport()`](Namespace.html#getElementImport())
Model:
opposite="elementImport" required="true" transient="false" ordered="false"
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

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.magicdraw.classes.mdkernel</a></div>
<h1 class="title" title="Interface ElementImport">Interface ElementImport</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></code>, <code><a href="Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../../../magicdraw/foundation/MDObject.html" title="interface in com.nomagic.magicdraw.foundation">MDObject</a></code>, <code>com.dassault_systemes.modeler.foundation.model.ModelElement</code>, <code><a href="../../base/ModelObject.html" title="interface in com.nomagic.uml2.ext.magicdraw.base">ModelObject</a></code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code>javax.jmi.reflect.RefBaseObject</code>, <code>javax.jmi.reflect.RefFeatured</code>, <code>javax.jmi.reflect.RefObject</code>, <code><a href="Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Relationship</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementImport</span><span class="extends-implements">
extends <a href="DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a></span></div>
<div class="block"><!-- begin-user-doc -->
 A representation of the model object '<em><b>Element Import</b></em>'.
 <!-- end-user-doc -->
<p>
<!-- begin-model-doc -->
 An ElementImport identifies a NamedElement in a Namespace other than the one that owns that NamedElement and allows the NamedElement to be referenced using an
 unqualified name in the Namespace owning the ElementImport.
 <!-- end-model-doc -->
<p>
<p>
 The following features are supported:
 <ul>
<li><a href="#getAlias()"><code><em>Alias</em></code></a></li>
<li><a href="#getImportedElement()"><code><em>Imported Element</em></code></a></li>
<li><a href="#getVisibility()"><code><em>Visibility</em></code></a></li>
<li><a href="#get_profileOfMetaclassReference()"><code><em>profile Of Metaclass Reference</em></code></a></li>
<li><a href="#getImportingNamespace()"><code><em>Importing Namespace</em></code></a></li>
</ul>
</p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../metadata/UMLPackage.html#getElementImport()"><code>UMLPackage.getElementImport()</code></a></li>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get_profileOfMetaclassReference()">get_profileOfMetaclassReference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>profile Of Metaclass Reference</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAlias()">getAlias</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Alias</b></em>' attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportedElement()">getImportedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Imported Element</b></em>' reference.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Namespace.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Namespace</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportingNamespace()">getImportingNamespace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Importing Namespace</b></em>' container reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVisibility()">getVisibility</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the value of the '<em><b>Visibility</b></em>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#set_profileOfMetaclassReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">set_profileOfMetaclassReference</a><wbr/>(<a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the
 '<a href="#get_profileOfMetaclassReference()"><code><em>profile Of Metaclass Reference</em></code></a>' reference.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAlias(java.lang.String)">setAlias</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getAlias()"><code><em>Alias</em></code></a>' attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setImportedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement)">setImportedElement</a><wbr/>(<a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the value of the '<a href="#getImportedElement()"><code><em>Imported Element</em></code></a>' reference.</div>
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
 Specifies the visibility of the imported PackageableElement within the importingNamespace, i.e., whether the  importedElement will in turn be visible to other
 Namespaces. If the ElementImport is public, the importedElement will be visible outside the importingNamespace while, if the ElementImport is private, it will
 not.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Visibility</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>VisibilityKind</code></a></li>
<li><a href="#setVisibility(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)"><code>setVisibility(VisibilityKind)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getElementImport_Visibility()"><code>UMLPackage.getElementImport_Visibility()</code></a></li>
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
<li>
<section class="detail" id="getAlias()">
<h3>getAlias</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAlias</span>()</div>
<div class="block">Returns the value of the '<em><b>Alias</b></em>' attribute.
 The default value is <code>""</code>.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the name that should be added to the importing Namespace in lieu of the name of the imported PackagableElement. The alias must not clash with any other
 member in the importing Namespace. By default, no alias is used.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Alias</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setAlias(java.lang.String)"><code>setAlias(String)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getElementImport_Alias()"><code>UMLPackage.getElementImport_Alias()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>default="" dataType="com.nomagic.uml2.ext.magicdraw.String" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAlias(java.lang.String)">
<h3>setAlias</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setAlias</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getAlias()"><code><em>Alias</em></code></a>' attribute.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Alias</em>' attribute.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getAlias()"><code>getAlias()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImportedElement()">
<h3>getImportedElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a></span> <span class="element-name">getImportedElement</span>()</div>
<div class="block">Returns the value of the '<em><b>Imported Element</b></em>' reference.
 It is bidirectional and its opposite is
 '<a href="PackageableElement.html#get_elementImportOfImportedElement()"><code><em>element Import Of Imported Element</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the PackageableElement whose name is to be added to a Namespace.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Imported Element</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setImportedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement)"><code>setImportedElement(PackageableElement)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getElementImport_ImportedElement()"><code>UMLPackage.getElementImport_ImportedElement()</code></a></li>
<li><a href="PackageableElement.html#get_elementImportOfImportedElement()"><code>PackageableElement.get_elementImportOfImportedElement()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="_elementImportOfImportedElement" required="true" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImportedElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.PackageableElement)">
<h3>setImportedElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setImportedElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="PackageableElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">PackageableElement</a> value)</span></div>
<div class="block">Sets the value of the '<a href="#getImportedElement()"><code><em>Imported Element</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>Imported Element</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getImportedElement()"><code>getImportedElement()</code></a></li>
</ul>
</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="get_profileOfMetaclassReference()">
<h3>get_profileOfMetaclassReference</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">get_profileOfMetaclassReference</span>()</div>
<div class="block">Returns the value of the '<em><b>profile Of Metaclass Reference</b></em>' reference.
 It is bidirectional and its opposite is '<a href="../../mdprofiles/Profile.html#getMetaclassReference()"><code><em>Metaclass Reference</em></code></a>'.
 <!-- begin-user-doc -->
<p>
 If the meaning of the '<em>profile Of Metaclass Reference</em>' reference isn't clear,
 there really should be more of a description here...
 </p>
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>profile Of Metaclass Reference</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#set_profileOfMetaclassReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)"><code>set_profileOfMetaclassReference(Profile)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getElementImport__profileOfMetaclassReference()"><code>UMLPackage.getElementImport__profileOfMetaclassReference()</code></a></li>
<li><a href="../../mdprofiles/Profile.html#getMetaclassReference()"><code>Profile.getMetaclassReference()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="metaclassReference" ordered="false"</dd>
<dt>Generated:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="set_profileOfMetaclassReference(com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile)">
<h3>set_profileOfMetaclassReference</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">set_profileOfMetaclassReference</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a> value)</span></div>
<div class="block">Sets the value of the
 '<a href="#get_profileOfMetaclassReference()"><code><em>profile Of Metaclass Reference</em></code></a>' reference.
 <!-- begin-user-doc -->
<!-- end-user-doc --></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the new value of the '<em>profile Of Metaclass Reference</em>' reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#get_profileOfMetaclassReference()"><code>get_profileOfMetaclassReference()</code></a></li>
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
 It is bidirectional and its opposite is '<a href="Namespace.html#getElementImport()"><code><em>Element Import</em></code></a>'.
 <!-- begin-user-doc -->
<!-- end-user-doc -->
<!-- begin-model-doc -->
 Specifies the Namespace that imports a PackageableElement from another Namespace.
 <!-- end-model-doc --></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the value of the '<em>Importing Namespace</em>' container reference.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#setImportingNamespace(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Namespace)"><code>setImportingNamespace(Namespace)</code></a></li>
<li><a href="../../metadata/UMLPackage.html#getElementImport_ImportingNamespace()"><code>UMLPackage.getElementImport_ImportingNamespace()</code></a></li>
<li><a href="Namespace.html#getElementImport()"><code>Namespace.getElementImport()</code></a></li>
</ul>
</dd>
<dt>Model:</dt>
<dd>opposite="elementImport" required="true" transient="false" ordered="false"</dd>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
