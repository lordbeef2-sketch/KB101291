# JAVA OPENAPI: ProfileImplementation (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/profiles/ProfileImplementation.html
- source_path: `com/nomagic/profiles/ProfileImplementation.html`
- source_sha256: `b2e104b458b4d270e2837b1546092bff7e55aaa66152549a3fbf88d7dec4d3ac`
- captured_utc: `2026-07-14T16:56:08.972611+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.profiles](package-summary.html)

## Class ProfileImplementation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.profiles.ProfileImplementation

Direct Known Subclasses:
`[AnalysisPatternsProfile](../magicdraw/sysml/util/AnalysisPatternsProfile.html)`, `[BPMN2Profile](../magicdraw/cbm/profiles/BPMN2Profile.html)`, `[DependencyMatrixProfile](../magicdraw/dependencymatrix/persistence/DependencyMatrixProfile.html)`, `[MagicDrawProfile](../uml2/MagicDrawProfile.html)`, `[MDCustomizationForRequirements](../requirements/util/MDCustomizationForRequirements.html)`, `[MDCustomizationForSysMLProfile](../magicdraw/sysml/util/MDCustomizationForSysMLProfile.html)`, `[ModelTransformationProfile](../magicdraw/modeltransformations/ModelTransformationProfile.html)`, `[ReportProfile](../magicdraw/magicreport/ReportProfile.html)`, `[SimulationProfile](../magicdraw/simulation/SimulationProfile.html)`, `[StandardProfile](../uml2/StandardProfile.html)`, `[SysMLProfile](../magicdraw/sysml/util/SysMLProfile.html)`, `[SysPhSProfile](../magicdraw/sysml/util/SysPhSProfile.html)`, `[UAF](../magicdraw/uaf/UAF.html)`, `[UIPrototypingProfile](../magicdraw/uimodeling/UIPrototypingProfile.html)`, `[UPDMProfile](../updm/utils/UPDMProfile.html)`, `[ValidationProfile](../uml2/ValidationProfile.html)`

@OpenApipublic abstract classProfileImplementation
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Base class for a convenience class generated from a modeled Profile (UML), to allow quick access
 to profile's elements (Stereotypes, tag Properties, Enumerations, DataTypes)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ProfileImplementation.StereotypeWrapper](ProfileImplementation.StereotypeWrapper.html)`
Base class for generated stereotype wrapper for Stereotype from a modeled Profile (UML).
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[ProfileImplementation](#%3Cinit%3E(com.nomagic.profiles.ProfileCache))(com.nomagic.profiles.ProfileCache cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[clearCache](#clearCache())()`

`protected <T extends [Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
T`
`[findByRelativeQualifiedName](#findByRelativeQualifiedName(java.lang.String,java.lang.Class))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) relativeQName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type)`

`protected abstract [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper>`
`[generatedGetAllElementWrappers](#generatedGetAllElementWrappers())()`
Generated method for getting all stereotype wrappers contained within this profile.
`protected abstract [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[generatedGetAllStereotypes](#generatedGetAllStereotypes())()`
Generated method for getting all stereotypes contained within this profile.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[getAllStereotypes](#getAllStereotypes())()`
Gets all stereotypes contained within this profile.
`com.nomagic.profiles.ProfileCache`
`[getCache](#getCache())()`

`final [DataType](../uml2/ext/magicdraw/classes/mdkernel/DataType.html)`
`[getDataType](#getDataType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
It is recommended to avoid directly calling this method, and call method that matches the DataType name directly,
 as a separate method is generated for each DataType of the Profile.
`final [Profile](../uml2/ext/magicdraw/mdprofiles/Profile.html)`
`[getProfile](#getProfile())()`

`final [Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
It is recommended to avoid directly calling this method, and call method that matches the Stereotype name directly,
 as a separate method is generated for each Stereotype of the Profile.
`boolean`
`[isTypeOf](#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`

`boolean`
`[isTypeOf](#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`

`protected static <E extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<E> & com.nomagic.profiles.ProfileImplementation.TextProvider> 
E`
`[valueFromString](#valueFromString(java.lang.Class,java.lang.Object))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<E> enumClass,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProfileImplementation
protected ProfileImplementation(com.nomagic.profiles.ProfileCache cache)
 ============ METHOD DETAIL ========== 
Method Details
getStereotype
@CheckForNullpublic final [Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getStereotype([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
It is recommended to avoid directly calling this method, and call method that matches the Stereotype name directly,
 as a separate method is generated for each Stereotype of the Profile.
Parameters:
`name` - of the Stereotype
Returns:
Stereotype from this profile by a given name
getDataType
@CheckForNullpublic final [DataType](../uml2/ext/magicdraw/classes/mdkernel/DataType.html) getDataType([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
It is recommended to avoid directly calling this method, and call method that matches the DataType name directly,
 as a separate method is generated for each DataType of the Profile.
Parameters:
`name` - of the Stereotype
Returns:
Stereotype from this profile by a given name
getProfile
@CheckForNullpublic final [Profile](../uml2/ext/magicdraw/mdprofiles/Profile.html) getProfile()
Returns:
UML Profile element which is represented by this implementation.
 Will return null if the Profile is not used/loaded in the currently analyzed Model (Project or Resource)
findByRelativeQualifiedName
@CheckForNullprotected <T extends [Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html)> T findByRelativeQualifiedName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) relativeQName,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<T> type)
getCache
public com.nomagic.profiles.ProfileCache getCache()
Returns:
returns profile cache.
isTypeOf
public boolean isTypeOf([Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns:
true if given Element has applied the given stereotype or a stereotype derived from it
isTypeOf
public boolean isTypeOf([Element](../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
Returns:
true if given Element has applied the given stereotype or a stereotype derived from it
getAllStereotypes
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> getAllStereotypes()
Gets all stereotypes contained within this profile.
Returns:
unmodifiable collection containing all stereotypes within this profile.
generatedGetAllStereotypes
protected abstract [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> generatedGetAllStereotypes()
Generated method for getting all stereotypes contained within this profile.
Returns:
gets all stereotypes contained within this profile.
generatedGetAllElementWrappers
protected abstract [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper> generatedGetAllElementWrappers()
Generated method for getting all stereotype wrappers contained within this profile.
Returns:
gets all stereotype wrappers contained within this profile.
clearCache
protected void clearCache()
valueFromString
@CheckForNullprotected static <E extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<E> & com.nomagic.profiles.ProfileImplementation.TextProvider>
E valueFromString([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<E> enumClass,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.profiles</a></div>
<h1 class="title" title="Class ProfileImplementation">Class ProfileImplementation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.profiles.ProfileImplementation</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../magicdraw/sysml/util/AnalysisPatternsProfile.html" title="class in com.nomagic.magicdraw.sysml.util">AnalysisPatternsProfile</a></code>, <code><a href="../magicdraw/cbm/profiles/BPMN2Profile.html" title="class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile</a></code>, <code><a href="../magicdraw/dependencymatrix/persistence/DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a></code>, <code><a href="../uml2/MagicDrawProfile.html" title="class in com.nomagic.uml2">MagicDrawProfile</a></code>, <code><a href="../requirements/util/MDCustomizationForRequirements.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements</a></code>, <code><a href="../magicdraw/sysml/util/MDCustomizationForSysMLProfile.html" title="class in com.nomagic.magicdraw.sysml.util">MDCustomizationForSysMLProfile</a></code>, <code><a href="../magicdraw/modeltransformations/ModelTransformationProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationProfile</a></code>, <code><a href="../magicdraw/magicreport/ReportProfile.html" title="class in com.nomagic.magicdraw.magicreport">ReportProfile</a></code>, <code><a href="../magicdraw/simulation/SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a></code>, <code><a href="../uml2/StandardProfile.html" title="class in com.nomagic.uml2">StandardProfile</a></code>, <code><a href="../magicdraw/sysml/util/SysMLProfile.html" title="class in com.nomagic.magicdraw.sysml.util">SysMLProfile</a></code>, <code><a href="../magicdraw/sysml/util/SysPhSProfile.html" title="class in com.nomagic.magicdraw.sysml.util">SysPhSProfile</a></code>, <code><a href="../magicdraw/uaf/UAF.html" title="class in com.nomagic.magicdraw.uaf">UAF</a></code>, <code><a href="../magicdraw/uimodeling/UIPrototypingProfile.html" title="class in com.nomagic.magicdraw.uimodeling">UIPrototypingProfile</a></code>, <code><a href="../updm/utils/UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a></code>, <code><a href="../uml2/ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ProfileImplementation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Base class for a convenience class generated from a modeled Profile (UML), to allow quick access
 to profile's elements (Stereotypes, tag Properties, Enumerations, DataTypes)</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></div>
<div class="col-last even-row-color">
<div class="block">Base class for generated stereotype wrapper for Stereotype from a modeled Profile (UML).</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.profiles.ProfileCache)">ProfileImplementation</a><wbr/>(com.nomagic.profiles.ProfileCache cache)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCache()">clearCache</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected &lt;T extends <a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findByRelativeQualifiedName(java.lang.String,java.lang.Class)">findByRelativeQualifiedName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> relativeQName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Generated method for getting all stereotype wrappers contained within this profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#generatedGetAllStereotypes()">generatedGetAllStereotypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Generated method for getting all stereotypes contained within this profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllStereotypes()">getAllStereotypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets all stereotypes contained within this profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.profiles.ProfileCache</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCache()">getCache</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../uml2/ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDataType(java.lang.String)">getDataType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">It is recommended to avoid directly calling this method, and call method that matches the DataType name directly,
 as a separate method is generated for each DataType of the Profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../uml2/ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProfile()">getProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype(java.lang.String)">getStereotype</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">It is recommended to avoid directly calling this method, and  call method that matches the Stereotype name directly,
 as a separate method is generated for each Stereotype of the Profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isTypeOf</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isTypeOf</a><wbr/>(<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static &lt;E extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;E&gt; &amp; com.nomagic.profiles.ProfileImplementation.TextProvider&gt;<br/>E</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueFromString(java.lang.Class,java.lang.Object)">valueFromString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;E&gt; enumClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.profiles.ProfileCache)">
<h3>ProfileImplementation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ProfileImplementation</span><wbr/><span class="parameters">(com.nomagic.profiles.ProfileCache cache)</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getStereotype(java.lang.String)">
<h3>getStereotype</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">It is recommended to avoid directly calling this method, and  call method that matches the Stereotype name directly,
 as a separate method is generated for each Stereotype of the Profile.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - of the Stereotype</dd>
<dt>Returns:</dt>
<dd>Stereotype from this profile by a given name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDataType(java.lang.String)">
<h3>getDataType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../uml2/ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></span> <span class="element-name">getDataType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">It is recommended to avoid directly calling this method, and call method that matches the DataType name directly,
 as a separate method is generated for each DataType of the Profile.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - of the Stereotype</dd>
<dt>Returns:</dt>
<dd>Stereotype from this profile by a given name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProfile()">
<h3>getProfile</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../uml2/ext/magicdraw/mdprofiles/Profile.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Profile</a></span> <span class="element-name">getProfile</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>UML Profile element which is represented by this implementation.
 Will return null if the Profile is not used/loaded in the currently analyzed Model (Project or Resource)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findByRelativeQualifiedName(java.lang.String,java.lang.Class)">
<h3>findByRelativeQualifiedName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="type-parameters">&lt;T extends <a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">findByRelativeQualifiedName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> relativeQName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCache()">
<h3>getCache</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.profiles.ProfileCache</span> <span class="element-name">getCache</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>returns profile cache.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if given Element has applied the given stereotype or a stereotype derived from it</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if given Element has applied the given stereotype or a stereotype derived from it</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllStereotypes()">
<h3>getAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">getAllStereotypes</span>()</div>
<div class="block">Gets all stereotypes contained within this profile.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>unmodifiable collection containing all stereotypes within this profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllStereotypes()">
<h3>generatedGetAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">generatedGetAllStereotypes</span>()</div>
<div class="block">Generated method for getting all stereotypes contained within this profile.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>gets all stereotypes contained within this profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllElementWrappers()">
<h3>generatedGetAllElementWrappers</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</span> <span class="element-name">generatedGetAllElementWrappers</span>()</div>
<div class="block">Generated method for getting all stereotype wrappers contained within this profile.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>gets all stereotype wrappers contained within this profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearCache()">
<h3>clearCache</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clearCache</span>()</div>
</section>
</li>
<li>
<section class="detail" id="valueFromString(java.lang.Class,java.lang.Object)">
<h3>valueFromString</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected static</span> <span class="type-parameters-long">&lt;E extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;E&gt; &amp; com.nomagic.profiles.ProfileImplementation.TextProvider&gt;</span>
<span class="return-type">E</span> <span class="element-name">valueFromString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;E&gt; enumClass,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
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
