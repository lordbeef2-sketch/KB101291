# JAVA OPENAPI: ProfileImplementation (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/profiles/ProfileImplementation.html
- source_path: `com/nomagic/profiles/ProfileImplementation.html`
- source_sha256: `302af64b3f5a695df3c3e550605598b1b98e94b7effc55766eb9e765db883a06`
- captured_utc: `2026-07-14T16:56:02.072531+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.profiles](package-summary.html)

## Class ProfileImplementation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.profiles.ProfileImplementation

Direct Known Subclasses:
`[AnalysisPatternsProfile](../magicdraw/sysml/util/AnalysisPatternsProfile.html)`, `[BPMN2Profile](../magicdraw/cbm/profiles/BPMN2Profile.html)`, `[DependencyMatrixProfile](../magicdraw/dependencymatrix/persistence/DependencyMatrixProfile.html)`, `[MagicDrawProfile](../uml2/MagicDrawProfile.html)`, `[MDCustomizationForRequirements](../requirements/util/MDCustomizationForRequirements.html)`, `[MDCustomizationForSysMLProfile](../magicdraw/sysml/util/MDCustomizationForSysMLProfile.html)`, `[ModelTransformationProfile](../magicdraw/modeltransformations/ModelTransformationProfile.html)`, `[ReportProfile](../magicdraw/magicreport/ReportProfile.html)`, `[ReportProfile](../uaf/report/ReportProfile.html)`, `[SimulationProfile](../magicdraw/simulation/SimulationProfile.html)`, `[StandardProfile](../uml2/StandardProfile.html)`, `[SysMLProfile](../magicdraw/sysml/util/SysMLProfile.html)`, `[UAF](../magicdraw/uaf/UAF.html)`, `[UIPrototypingProfile](../magicdraw/uimodeling/UIPrototypingProfile.html)`, `[UPDMProfile](../updm/utils/UPDMProfile.html)`, `[ValidationProfile](../uml2/ValidationProfile.html)`

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
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

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
<dd><code><a href="../magicdraw/sysml/util/AnalysisPatternsProfile.html" title="class in com.nomagic.magicdraw.sysml.util">AnalysisPatternsProfile</a></code>, <code><a href="../magicdraw/cbm/profiles/BPMN2Profile.html" title="class in com.nomagic.magicdraw.cbm.profiles">BPMN2Profile</a></code>, <code><a href="../magicdraw/dependencymatrix/persistence/DependencyMatrixProfile.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">DependencyMatrixProfile</a></code>, <code><a href="../uml2/MagicDrawProfile.html" title="class in com.nomagic.uml2">MagicDrawProfile</a></code>, <code><a href="../requirements/util/MDCustomizationForRequirements.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements</a></code>, <code><a href="../magicdraw/sysml/util/MDCustomizationForSysMLProfile.html" title="class in com.nomagic.magicdraw.sysml.util">MDCustomizationForSysMLProfile</a></code>, <code><a href="../magicdraw/modeltransformations/ModelTransformationProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">ModelTransformationProfile</a></code>, <code><a href="../magicdraw/magicreport/ReportProfile.html" title="class in com.nomagic.magicdraw.magicreport">ReportProfile</a></code>, <code><a href="../uaf/report/ReportProfile.html" title="class in com.nomagic.uaf.report">ReportProfile</a></code>, <code><a href="../magicdraw/simulation/SimulationProfile.html" title="class in com.nomagic.magicdraw.simulation">SimulationProfile</a></code>, <code><a href="../uml2/StandardProfile.html" title="class in com.nomagic.uml2">StandardProfile</a></code>, <code><a href="../magicdraw/sysml/util/SysMLProfile.html" title="class in com.nomagic.magicdraw.sysml.util">SysMLProfile</a></code>, <code><a href="../magicdraw/uaf/UAF.html" title="class in com.nomagic.magicdraw.uaf">UAF</a></code>, <code><a href="../magicdraw/uimodeling/UIPrototypingProfile.html" title="class in com.nomagic.magicdraw.uimodeling">UIPrototypingProfile</a></code>, <code><a href="../updm/utils/UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a></code>, <code><a href="../uml2/ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a></code></dd>
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
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
