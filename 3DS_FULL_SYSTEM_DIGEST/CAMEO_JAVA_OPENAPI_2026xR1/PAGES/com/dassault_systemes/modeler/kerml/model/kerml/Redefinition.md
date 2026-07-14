# JAVA OPENAPI: Redefinition (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Redefinition.html
- source_path: `com/dassault_systemes/modeler/kerml/model/kerml/Redefinition.html`
- source_sha256: `1ed0148875f6be1cc435759c017301b478ace03bac1df726399eff9cdc42e5fb`
- captured_utc: `2026-07-14T16:44:50.258873+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model.kerml](package-summary.html)

## Interface Redefinition

All Superinterfaces:
`[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[Element](Element.html)`, `org.eclipse.emf.ecore.EObject`, `[ModelElement](../../../foundation/model/ModelElement.html)`, `com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject`, `org.eclipse.emf.common.notify.Notifier`, `[Relationship](Relationship.html)`, `[Specialization](Specialization.html)`, `[Subsetting](Subsetting.html)`

@OpenApiAllpublic interfaceRedefinitionextends [Subsetting](Subsetting.html)

`Redefinition` is a kind of `Subsetting` that requires the `redefinedFeature` and the `redefiningFeature` to have the same values (on each instance of the domain of the `redefiningFeature`). This means any restrictions on the `redefiningFeature`, such as `type` or `multiplicity`, also apply to the `redefinedFeature` (on each instance of the domain of the `redefiningFeature`), and vice versa. The `redefinedFeature` might have values for instances of the domain of the `redefiningFeature`, but only as instances of the domain of the `redefinedFeature` that happen to also be instances of the domain of the `redefiningFeature`. This is supported by the constraints inherited from `Subsetting` on the domains of the `redefiningFeature` and `redefinedFeature`. However, these constraints are narrowed for `Redefinition` to require the `owningTypes` of the `redefiningFeature` and `redefinedFeature` to be different and the `redefinedFeature` to not be inherited into the `owningNamespace` of the `redefiningFeature`.This enables the `redefiningFeature` to have the same name as the `redefinedFeature`, if desired.
 
 let anythingType: Type =
 redefiningFeature.resolveGlobal('Base::Anything').modelElement.oclAsType(Type) in 
 -- Including "Anything" accounts for implicit featuringType of Features
 -- with no explicit featuringType.
 let redefiningFeaturingTypes: Set(Type) =
 if redefiningFeature.isVariable then Set{redefiningFeature.owningType}
 else redefiningFeature.featuringTypes->asSet()->including(anythingType) 
 endif in
 let redefinedFeaturingTypes: Set(Type) =
 if redefinedFeature.isVariable then Set{redefinedFeature.owningType}
 else redefinedFeature.featuringTypes->asSet()->including(anythingType)
 endif in
 redefiningFeaturingTypes <> redefinedFeaturingType
 let featuringTypes : Sequence(Type) =
 if redefiningFeature.isVariable then Sequence{redefiningFeature.owningType}
 else redefiningFeature.featuringType
 endif in
 featuringTypes->forAll(t |
 let direction : FeatureDirectionKind = t.directionOf(redefinedFeature) in
 ((direction = FeatureDirectionKind::_'in' or 
 direction = FeatureDirectionKind::out) implies
 redefiningFeature.direction = direction)
 and 
 (direction = FeatureDirectionKind::inout implies
 redefiningFeature.direction <> null))
 redefinedFeature.isEnd implies redefiningFeature.isEnd

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Feature](Feature.html)`
`[getRedefinedFeature](#getRedefinedFeature())()`
The `Feature` that is redefined by the `redefiningFeature` of this `Redefinition`.
`[Feature](Feature.html)`
`[getRedefiningFeature](#getRedefiningFeature())()`
The `Feature` that is redefining the `redefinedFeature` of this `Redefinition`.
`void`
`[setRedefinedFeature](#setRedefinedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) value)`
The `Feature` that is redefined by the `redefiningFeature` of this `Redefinition`.
`void`
`[setRedefiningFeature](#setRedefiningFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](Feature.html) value)`
The `Feature` that is redefining the `redefinedFeature` of this `Redefinition`.
Methods inherited from interface com.nomagic.magicdraw.uml.[BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html)
`[accept](../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)), [addPropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)), [canAdd](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)), [canAddChild](../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()), [canBeDeleted](../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()), [firePropertyChange](../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getClassType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()), [getHumanName](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()), [getHumanType](../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()), [getID](../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()), [isEditable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()), [isSelfChangeable](../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()), [removePropertyChangeListener](../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [setID](../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)), [sGetID](../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID())`
Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)
`[compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Element](Element.html)
`[effectiveName](Element.html#effectiveName()), [effectiveShortName](Element.html#effectiveShortName()), [escapedName](Element.html#escapedName()), [getAliasIds](Element.html#getAliasIds()), [getDeclaredName](Element.html#getDeclaredName()), [getDeclaredShortName](Element.html#getDeclaredShortName()), [getDocumentation](Element.html#getDocumentation()), [getElementId](Element.html#getElementId()), [getName](Element.html#getName()), [getOwnedAnnotation](Element.html#getOwnedAnnotation()), [getOwnedElement](Element.html#getOwnedElement()), [getOwnedRelationship](Element.html#getOwnedRelationship()), [getOwner](Element.html#getOwner()), [getOwningMembership](Element.html#getOwningMembership()), [getOwningNamespace](Element.html#getOwningNamespace()), [getOwningRelationship](Element.html#getOwningRelationship()), [getQualifiedName](Element.html#getQualifiedName()), [getShortName](Element.html#getShortName()), [getTextualRepresentation](Element.html#getTextualRepresentation()), [isImpliedIncluded](Element.html#isImpliedIncluded()), [isLibraryElement](Element.html#isLibraryElement()), [setDeclaredName](Element.html#setDeclaredName(java.lang.String)), [setDeclaredShortName](Element.html#setDeclaredShortName(java.lang.String)), [setElementId](Element.html#setElementId(java.lang.String)), [setIsImpliedIncluded](Element.html#setIsImpliedIncluded(boolean)), [setOwner](Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)), [setOwningMembership](Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)), [setOwningRelationship](Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship))`
Methods inherited from interface org.eclipse.emf.ecore.EObject
`eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset`
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.[ModelElement](../../../foundation/model/ModelElement.html)
`[canChangeElementOwner](../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)), [dispose](../../../foundation/model/ModelElement.html#dispose()), [eDynamicGet](../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)), [getElementOwner](../../../foundation/model/ModelElement.html#getElementOwner()), [getLocalID](../../../foundation/model/ModelElement.html#getLocalID()), [getObjectParent](../../../foundation/model/ModelElement.html#getObjectParent()), [selfDispose](../../../foundation/model/ModelElement.html#selfDispose()), [setLocalID](../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)), [sGetLocalID](../../../foundation/model/ModelElement.html#sGetLocalID())`
Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject
`getModelExtension, getModelExtension`
Methods inherited from interface org.eclipse.emf.common.notify.Notifier
`eAdapters, eDeliver, eNotify, eSetDeliver`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Relationship](Relationship.html)
`[getOwnedRelatedElement](Relationship.html#getOwnedRelatedElement()), [getOwningRelatedElement](Relationship.html#getOwningRelatedElement()), [getRelatedElement](Relationship.html#getRelatedElement()), [getSource](Relationship.html#getSource()), [getTarget](Relationship.html#getTarget()), [isImplied](Relationship.html#isImplied()), [libraryNamespace](Relationship.html#libraryNamespace()), [path](Relationship.html#path()), [setIsImplied](Relationship.html#setIsImplied(boolean)), [setOwningRelatedElement](Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Specialization](Specialization.html)
`[getGeneral](Specialization.html#getGeneral()), [getOwningType](Specialization.html#getOwningType()), [getSpecific](Specialization.html#getSpecific()), [setGeneral](Specialization.html#setGeneral(com.dassault_systemes.modeler.kerml.model.kerml.Type)), [setSpecific](Specialization.html#setSpecific(com.dassault_systemes.modeler.kerml.model.kerml.Type))`
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.[Subsetting](Subsetting.html)
`[getOwningFeature](Subsetting.html#getOwningFeature()), [getSubsettedFeature](Subsetting.html#getSubsettedFeature()), [getSubsettingFeature](Subsetting.html#getSubsettingFeature()), [setSubsettedFeature](Subsetting.html#setSubsettedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)), [setSubsettingFeature](Subsetting.html#setSubsettingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))`

============ METHOD DETAIL ========== 
Method Details
getRedefiningFeature
@CheckForNull[Feature](Feature.html) getRedefiningFeature()
The `Feature` that is redefining the `redefinedFeature` of this `Redefinition`.
Returns:
the redefiningFeature value
Model:
derived="false"
 transient="false"
 oppositeRoleName="redefinition"
 redefines=[`Subsetting.getSubsettingFeature()`](Subsetting.html#getSubsettingFeature())
setRedefiningFeature
void setRedefiningFeature(@CheckForNull
 [Feature](Feature.html) value)
The `Feature` that is redefining the `redefinedFeature` of this `Redefinition`.
Parameters:
`value` - the redefiningFeature value
Model:
derived="false"
 transient="false"
 oppositeRoleName="redefinition"
 redefines=[`Subsetting.getSubsettingFeature()`](Subsetting.html#getSubsettingFeature())
getRedefinedFeature
@CheckForNull[Feature](Feature.html) getRedefinedFeature()
The `Feature` that is redefined by the `redefiningFeature` of this `Redefinition`.
Returns:
the redefinedFeature value
Model:
derived="false"
 transient="false"
 oppositeRoleName="redefining"
 redefines=[`Subsetting.getSubsettedFeature()`](Subsetting.html#getSubsettedFeature())
setRedefinedFeature
void setRedefinedFeature(@CheckForNull
 [Feature](Feature.html) value)
The `Feature` that is redefined by the `redefiningFeature` of this `Redefinition`.
Parameters:
`value` - the redefinedFeature value
Model:
derived="false"
 transient="false"
 oppositeRoleName="redefining"
 redefines=[`Subsetting.getSubsettedFeature()`](Subsetting.html#getSubsettedFeature())

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model.kerml</a></div>
<h1 class="title" title="Interface Redefinition">Interface Redefinition</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code>, <code>org.eclipse.emf.ecore.EObject</code>, <code><a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></code>, <code>com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</code>, <code>org.eclipse.emf.common.notify.Notifier</code>, <code><a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></code>, <code><a href="Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a></code>, <code><a href="Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Redefinition</span><span class="extends-implements">
extends <a href="Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a></span></div>
<div class="block"><p><code>Redefinition</code> is a kind of <code>Subsetting</code> that requires the <code>redefinedFeature</code> and the <code>redefiningFeature</code> to have the same values (on each instance of the domain of the <code>redefiningFeature</code>). This means any restrictions on the <code>redefiningFeature</code>, such as <code>type</code> or <code>multiplicity</code>, also apply to the <code>redefinedFeature</code> (on each instance of the domain of the <code>redefiningFeature</code>), and vice versa. The <code>redefinedFeature</code> might have values for instances of the domain of the <code>redefiningFeature</code>, but only as instances of the domain of the <code>redefinedFeature</code> that happen to also be instances of the domain of the <code>redefiningFeature</code>. This is supported by the constraints inherited from <code>Subsetting</code> on the domains of the <code>redefiningFeature</code> and <code>redefinedFeature</code>. However, these constraints are narrowed for <code>Redefinition</code> to require the <code>owningTypes</code> of the <code>redefiningFeature</code> and <code>redefinedFeature</code> to be different and the <code>redefinedFeature</code> to not be inherited into the <code>owningNamespace</code> of the <code>redefiningFeature</code>.This enables the <code>redefiningFeature</code> to have the same name as the <code>redefinedFeature</code>, if desired.</p>
 
 let anythingType: Type =
     redefiningFeature.resolveGlobal('Base::Anything').modelElement.oclAsType(Type) in 
 -- Including "Anything" accounts for implicit featuringType of Features
 -- with no explicit featuringType.
 let redefiningFeaturingTypes: Set(Type) =
     if redefiningFeature.isVariable then Set{redefiningFeature.owningType}
     else redefiningFeature.featuringTypes-&gt;asSet()-&gt;including(anythingType) 
     endif in
 let redefinedFeaturingTypes: Set(Type) =
     if redefinedFeature.isVariable then Set{redefinedFeature.owningType}
     else redefinedFeature.featuringTypes-&gt;asSet()-&gt;including(anythingType)
     endif in
 redefiningFeaturingTypes &lt;&gt; redefinedFeaturingType
 let featuringTypes : Sequence(Type) =
     if redefiningFeature.isVariable then Sequence{redefiningFeature.owningType}
     else redefiningFeature.featuringType
     endif in
 featuringTypes-&gt;forAll(t |
     let direction : FeatureDirectionKind = t.directionOf(redefinedFeature) in
     ((direction = FeatureDirectionKind::_'in' or 
       direction = FeatureDirectionKind::out) implies
          redefiningFeature.direction = direction)
     and 
     (direction = FeatureDirectionKind::inout implies
         redefiningFeature.direction &lt;&gt; null))
 redefinedFeature.isEnd implies redefiningFeature.isEnd</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefinedFeature()">getRedefinedFeature</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that is redefined by the <code>redefiningFeature</code> of this <code>Redefinition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRedefiningFeature()">getRedefiningFeature</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that is redefining the <code>redefinedFeature</code> of this <code>Redefinition</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRedefinedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setRedefinedFeature</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that is redefined by the <code>redefiningFeature</code> of this <code>Redefinition</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRedefiningFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setRedefiningFeature</a><wbr/>(<a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The <code>Feature</code> that is redefining the <code>redefinedFeature</code> of this <code>Redefinition</code>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.BaseElement">Methods inherited from interface com.nomagic.magicdraw.uml.<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></h3>
<code><a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#accept(com.nomagic.magicdraw.uml.AbstractVisitor)">accept</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAdd(com.nomagic.magicdraw.uml.BaseElement,boolean)">canAdd</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canAddChild()">canAddChild</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#canBeDeleted()">canBeDeleted</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)">firePropertyChange</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getClassType()">getClassType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanName()">getHumanName</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getHumanType()">getHumanType</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#getID()">getID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isEditable()">isEditable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#isSelfChangeable()">isSelfChangeable</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#setID(java.lang.String)">setID</a>, <a href="../../../../../nomagic/magicdraw/uml/BaseElement.html#sGetID()">sGetID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Comparable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Element">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></h3>
<code><a href="Element.html#effectiveName()">effectiveName</a>, <a href="Element.html#effectiveShortName()">effectiveShortName</a>, <a href="Element.html#escapedName()">escapedName</a>, <a href="Element.html#getAliasIds()">getAliasIds</a>, <a href="Element.html#getDeclaredName()">getDeclaredName</a>, <a href="Element.html#getDeclaredShortName()">getDeclaredShortName</a>, <a href="Element.html#getDocumentation()">getDocumentation</a>, <a href="Element.html#getElementId()">getElementId</a>, <a href="Element.html#getName()">getName</a>, <a href="Element.html#getOwnedAnnotation()">getOwnedAnnotation</a>, <a href="Element.html#getOwnedElement()">getOwnedElement</a>, <a href="Element.html#getOwnedRelationship()">getOwnedRelationship</a>, <a href="Element.html#getOwner()">getOwner</a>, <a href="Element.html#getOwningMembership()">getOwningMembership</a>, <a href="Element.html#getOwningNamespace()">getOwningNamespace</a>, <a href="Element.html#getOwningRelationship()">getOwningRelationship</a>, <a href="Element.html#getQualifiedName()">getQualifiedName</a>, <a href="Element.html#getShortName()">getShortName</a>, <a href="Element.html#getTextualRepresentation()">getTextualRepresentation</a>, <a href="Element.html#isImpliedIncluded()">isImpliedIncluded</a>, <a href="Element.html#isLibraryElement()">isLibraryElement</a>, <a href="Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>, <a href="Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>, <a href="Element.html#setElementId(java.lang.String)">setElementId</a>, <a href="Element.html#setIsImpliedIncluded(boolean)">setIsImpliedIncluded</a>, <a href="Element.html#setOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwner</a>, <a href="Element.html#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">setOwningMembership</a>, <a href="Element.html#setOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Relationship)">setOwningRelationship</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.EObject">Methods inherited from interface org.eclipse.emf.ecore.EObject</h3>
<code>eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eInvoke, eIsProxy, eIsSet, eResource, eSet, eUnset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.ModelElement">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.<a href="../../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a></h3>
<code><a href="../../../foundation/model/ModelElement.html#canChangeElementOwner(com.dassault_systemes.modeler.foundation.model.ModelElement,boolean)">canChangeElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#dispose()">dispose</a>, <a href="../../../foundation/model/ModelElement.html#eDynamicGet(org.eclipse.emf.ecore.EStructuralFeature)">eDynamicGet</a>, <a href="../../../foundation/model/ModelElement.html#getElementOwner()">getElementOwner</a>, <a href="../../../foundation/model/ModelElement.html#getLocalID()">getLocalID</a>, <a href="../../../foundation/model/ModelElement.html#getObjectParent()">getObjectParent</a>, <a href="../../../foundation/model/ModelElement.html#selfDispose()">selfDispose</a>, <a href="../../../foundation/model/ModelElement.html#setLocalID(java.lang.String)">setLocalID</a>, <a href="../../../foundation/model/ModelElement.html#sGetLocalID()">sGetLocalID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject">Methods inherited from interface com.dassault_systemes.modeler.modelextension.model.modelextension.ModelExtensionObject</h3>
<code>getModelExtension, getModelExtension</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.Notifier">Methods inherited from interface org.eclipse.emf.common.notify.Notifier</h3>
<code>eAdapters, eDeliver, eNotify, eSetDeliver</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Relationship">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Relationship.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Relationship</a></h3>
<code><a href="Relationship.html#getOwnedRelatedElement()">getOwnedRelatedElement</a>, <a href="Relationship.html#getOwningRelatedElement()">getOwningRelatedElement</a>, <a href="Relationship.html#getRelatedElement()">getRelatedElement</a>, <a href="Relationship.html#getSource()">getSource</a>, <a href="Relationship.html#getTarget()">getTarget</a>, <a href="Relationship.html#isImplied()">isImplied</a>, <a href="Relationship.html#libraryNamespace()">libraryNamespace</a>, <a href="Relationship.html#path()">path</a>, <a href="Relationship.html#setIsImplied(boolean)">setIsImplied</a>, <a href="Relationship.html#setOwningRelatedElement(com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwningRelatedElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Specialization">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a></h3>
<code><a href="Specialization.html#getGeneral()">getGeneral</a>, <a href="Specialization.html#getOwningType()">getOwningType</a>, <a href="Specialization.html#getSpecific()">getSpecific</a>, <a href="Specialization.html#setGeneral(com.dassault_systemes.modeler.kerml.model.kerml.Type)">setGeneral</a>, <a href="Specialization.html#setSpecific(com.dassault_systemes.modeler.kerml.model.kerml.Type)">setSpecific</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.kerml.Subsetting">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.kerml.<a href="Subsetting.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Subsetting</a></h3>
<code><a href="Subsetting.html#getOwningFeature()">getOwningFeature</a>, <a href="Subsetting.html#getSubsettedFeature()">getSubsettedFeature</a>, <a href="Subsetting.html#getSubsettingFeature()">getSubsettingFeature</a>, <a href="Subsetting.html#setSubsettedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setSubsettedFeature</a>, <a href="Subsetting.html#setSubsettingFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setSubsettingFeature</a></code></div>
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
<section class="detail" id="getRedefiningFeature()">
<h3>getRedefiningFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getRedefiningFeature</span>()</div>
<div class="block"><p>The <code>Feature</code> that is redefining the <code>redefinedFeature</code> of this <code>Redefinition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the redefiningFeature value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="redefinition"
        redefines=<a href="Subsetting.html#getSubsettingFeature()"><code>Subsetting.getSubsettingFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRedefiningFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setRedefiningFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRedefiningFeature</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</span></div>
<div class="block"><p>The <code>Feature</code> that is redefining the <code>redefinedFeature</code> of this <code>Redefinition</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the redefiningFeature value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="redefinition"
        redefines=<a href="Subsetting.html#getSubsettingFeature()"><code>Subsetting.getSubsettingFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedFeature()">
<h3>getRedefinedFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getRedefinedFeature</span>()</div>
<div class="block"><p>The <code>Feature</code> that is redefined by the <code>redefiningFeature</code> of this <code>Redefinition</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the redefinedFeature value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="redefining"
        redefines=<a href="Subsetting.html#getSubsettedFeature()"><code>Subsetting.getSubsettedFeature()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRedefinedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setRedefinedFeature</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRedefinedFeature</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> value)</span></div>
<div class="block"><p>The <code>Feature</code> that is redefined by the <code>redefiningFeature</code> of this <code>Redefinition</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the redefinedFeature value</dd>
<dt>Model:</dt>
<dd>derived="false"
        transient="false"
        oppositeRoleName="redefining"
        redefines=<a href="Subsetting.html#getSubsettedFeature()"><code>Subsetting.getSubsettedFeature()</code></a></dd>
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
