# JAVA OPENAPI: RequirementsLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/libraries/standard/RequirementsLibrary.html
- source_path: `com/dassault_systemes/modeler/sysml/libraries/standard/RequirementsLibrary.html`
- source_sha256: `3080f5a1a62b7dff1a63d2b29f08cb20ab4fac60ebb39307cc4b50a5e31ac353`
- captured_utc: `2026-07-14T16:44:54.705932+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.libraries.standard](package-summary.html)

## Class RequirementsLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
[com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)
com.dassault_systemes.modeler.sysml.libraries.standard.RequirementsLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

@OpenApiAllpublic classRequirementsLibrary
extends [AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)

Access helper for the requirements standard library.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[RequirementsLibrary.ConcernCheckConcernDefinition](RequirementsLibrary.ConcernCheckConcernDefinition.html)`
Wrapper for the concern check concern definition library element.
`static class`
`[RequirementsLibrary.ConcernChecksConcernUsage](RequirementsLibrary.ConcernChecksConcernUsage.html)`
Wrapper for the concern checks concern usage library element.
`static class`
`[RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage](RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage.html)`
Wrapper for the not satisfied requirement checks requirement usage library element.
`static class`
`[RequirementsLibrary.RequirementCheckRequirementDefinition](RequirementsLibrary.RequirementCheckRequirementDefinition.html)`
Wrapper for the requirement check requirement definition library element.
`static class`
`[RequirementsLibrary.RequirementChecksRequirementUsage](RequirementsLibrary.RequirementChecksRequirementUsage.html)`
Wrapper for the requirement checks requirement usage library element.
`static class`
`[RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage](RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage.html)`
Wrapper for the satisfied requirement checks requirement usage library element.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RequirementsLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Creates a new requirements library instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[RequirementsLibrary.ConcernCheckConcernDefinition](RequirementsLibrary.ConcernCheckConcernDefinition.html)`
`[ConcernCheck](#ConcernCheck())()`
Returns concern check.
`[RequirementsLibrary.ConcernChecksConcernUsage](RequirementsLibrary.ConcernChecksConcernUsage.html)`
`[concernChecks](#concernChecks())()`
Returns concern checks.
`static [RequirementsLibrary](RequirementsLibrary.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the library instance for the project that owns the given element.
`static [RequirementsLibrary](RequirementsLibrary.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Returns the library instance for the given project.
`protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`
Returns get type wrappers.
`boolean`
`[isSemantic](#isSemantic())()`
Returns whether this library is semantic.
`[RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage](RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage.html)`
`[notSatisfiedRequirementChecks](#notSatisfiedRequirementChecks())()`
Returns not satisfied requirement checks.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Returns the names of the packages that belong to this library.
`[RequirementsLibrary.RequirementCheckRequirementDefinition](RequirementsLibrary.RequirementCheckRequirementDefinition.html)`
`[RequirementCheck](#RequirementCheck())()`
Returns requirement check.
`[RequirementsLibrary.RequirementChecksRequirementUsage](RequirementsLibrary.RequirementChecksRequirementUsage.html)`
`[requirementChecks](#requirementChecks())()`
Returns requirement checks.
`[RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage](RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage.html)`
`[satisfiedRequirementChecks](#satisfiedRequirementChecks())()`
Returns satisfied requirement checks.
Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)
`[findFunctionInLibrary](../../../kerml/libraries/AbstractLibrary.html#findFunctionInLibrary(java.lang.String)), [findLibraryPackage](../../../kerml/libraries/AbstractLibrary.html#findLibraryPackage(java.lang.String)), [findPackage](../../../kerml/libraries/AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)), [getLibraryPackages](../../../kerml/libraries/AbstractLibrary.html#getLibraryPackages()), [getNamespace](../../../kerml/libraries/AbstractLibrary.html#getNamespace()), [initialized](../../../kerml/libraries/AbstractLibrary.html#initialized())`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RequirementsLibrary
public RequirementsLibrary([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Creates a new requirements library instance.
Parameters:
`project` - the project
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [RequirementsLibrary](RequirementsLibrary.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Returns the library instance for the given project.
Parameters:
`project` - the project
Returns:
get instance by project
getInstance
public static [RequirementsLibrary](RequirementsLibrary.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the library instance for the project that owns the given element.
Parameters:
`element` - the element
Returns:
get instance
isSemantic
public boolean isSemantic()
Returns whether this library is semantic.
Specified by:
`[isSemantic](../../../kerml/libraries/AbstractLibrary.html#isSemantic())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
`true` if semantic; `false` otherwise
packagesNames
protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> packagesNames()
Returns the names of the packages that belong to this library.
Specified by:
`[packagesNames](../../../kerml/libraries/AbstractLibrary.html#packagesNames())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
packages names
RequirementCheck
public [RequirementsLibrary.RequirementCheckRequirementDefinition](RequirementsLibrary.RequirementCheckRequirementDefinition.html) RequirementCheck()
Returns requirement check.
Returns:
requirement check
ConcernCheck
public [RequirementsLibrary.ConcernCheckConcernDefinition](RequirementsLibrary.ConcernCheckConcernDefinition.html) ConcernCheck()
Returns concern check.
Returns:
concern check
requirementChecks
public [RequirementsLibrary.RequirementChecksRequirementUsage](RequirementsLibrary.RequirementChecksRequirementUsage.html) requirementChecks()
Returns requirement checks.
Returns:
requirement checks
satisfiedRequirementChecks
public [RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage](RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage.html) satisfiedRequirementChecks()
Returns satisfied requirement checks.
Returns:
satisfied requirement checks
notSatisfiedRequirementChecks
public [RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage](RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage.html) notSatisfiedRequirementChecks()
Returns not satisfied requirement checks.
Returns:
not satisfied requirement checks
concernChecks
public [RequirementsLibrary.ConcernChecksConcernUsage](RequirementsLibrary.ConcernChecksConcernUsage.html) concernChecks()
Returns concern checks.
Returns:
concern checks
getTypeWrappers
protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper> getTypeWrappers()
Returns get type wrappers.
Specified by:
`[getTypeWrappers](../../../kerml/libraries/AbstractLibrary.html#getTypeWrappers())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
get type wrappers

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.libraries.standard</a></div>
<h1 class="title" title="Class RequirementsLibrary">Class RequirementsLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance"><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.libraries.standard.RequirementsLibrary</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RequirementsLibrary</span>
<span class="extends-implements">extends <a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></span></div>
<div class="block">Access helper for the requirements standard library.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="RequirementsLibrary.ConcernCheckConcernDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.ConcernCheckConcernDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the concern check concern definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="RequirementsLibrary.ConcernChecksConcernUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.ConcernChecksConcernUsage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the concern checks concern usage library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the not satisfied requirement checks requirement usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="RequirementsLibrary.RequirementCheckRequirementDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.RequirementCheckRequirementDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the requirement check requirement definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="RequirementsLibrary.RequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.RequirementChecksRequirementUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the requirement checks requirement usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the satisfied requirement checks requirement usage library element.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">RequirementsLibrary</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new requirements library instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RequirementsLibrary.ConcernCheckConcernDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.ConcernCheckConcernDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ConcernCheck()">ConcernCheck</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns concern check.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RequirementsLibrary.ConcernChecksConcernUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.ConcernChecksConcernUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#concernChecks()">concernChecks</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns concern checks.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RequirementsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the library instance for the project that owns the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RequirementsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the library instance for the given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns get type wrappers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this library is semantic.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notSatisfiedRequirementChecks()">notSatisfiedRequirementChecks</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns not satisfied requirement checks.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the names of the packages that belong to this library.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RequirementsLibrary.RequirementCheckRequirementDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.RequirementCheckRequirementDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#RequirementCheck()">RequirementCheck</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns requirement check.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RequirementsLibrary.RequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.RequirementChecksRequirementUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#requirementChecks()">requirementChecks</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns requirement checks.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#satisfiedRequirementChecks()">satisfiedRequirementChecks</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns satisfied requirement checks.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary">Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.<a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></h3>
<code><a href="../../../kerml/libraries/AbstractLibrary.html#findFunctionInLibrary(java.lang.String)">findFunctionInLibrary</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#findLibraryPackage(java.lang.String)">findLibraryPackage</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)">findPackage</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#getLibraryPackages()">getLibraryPackages</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#getNamespace()">getNamespace</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#initialized()">initialized</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>RequirementsLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RequirementsLibrary</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Creates a new requirements library instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
</dl>
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
<section class="detail" id="getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="RequirementsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the library instance for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
<dt>Returns:</dt>
<dd>get instance by project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="RequirementsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the library instance for the project that owns the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>get instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSemantic()">
<h3>isSemantic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSemantic</span>()</div>
<div class="block">Returns whether this library is semantic.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#isSemantic()">isSemantic</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if semantic; <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="packagesNames()">
<h3>packagesNames</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">packagesNames</span>()</div>
<div class="block">Returns the names of the packages that belong to this library.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#packagesNames()">packagesNames</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>packages names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RequirementCheck()">
<h3>RequirementCheck</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RequirementsLibrary.RequirementCheckRequirementDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.RequirementCheckRequirementDefinition</a></span> <span class="element-name">RequirementCheck</span>()</div>
<div class="block">Returns requirement check.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>requirement check</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ConcernCheck()">
<h3>ConcernCheck</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RequirementsLibrary.ConcernCheckConcernDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.ConcernCheckConcernDefinition</a></span> <span class="element-name">ConcernCheck</span>()</div>
<div class="block">Returns concern check.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>concern check</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="requirementChecks()">
<h3>requirementChecks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RequirementsLibrary.RequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.RequirementChecksRequirementUsage</a></span> <span class="element-name">requirementChecks</span>()</div>
<div class="block">Returns requirement checks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>requirement checks</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="satisfiedRequirementChecks()">
<h3>satisfiedRequirementChecks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.SatisfiedRequirementChecksRequirementUsage</a></span> <span class="element-name">satisfiedRequirementChecks</span>()</div>
<div class="block">Returns satisfied requirement checks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>satisfied requirement checks</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notSatisfiedRequirementChecks()">
<h3>notSatisfiedRequirementChecks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.NotSatisfiedRequirementChecksRequirementUsage</a></span> <span class="element-name">notSatisfiedRequirementChecks</span>()</div>
<div class="block">Returns not satisfied requirement checks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>not satisfied requirement checks</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="concernChecks()">
<h3>concernChecks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RequirementsLibrary.ConcernChecksConcernUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">RequirementsLibrary.ConcernChecksConcernUsage</a></span> <span class="element-name">concernChecks</span>()</div>
<div class="block">Returns concern checks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>concern checks</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeWrappers()">
<h3>getTypeWrappers</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</span> <span class="element-name">getTypeWrappers</span>()</div>
<div class="block">Returns get type wrappers.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#getTypeWrappers()">getTypeWrappers</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>get type wrappers</dd>
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
