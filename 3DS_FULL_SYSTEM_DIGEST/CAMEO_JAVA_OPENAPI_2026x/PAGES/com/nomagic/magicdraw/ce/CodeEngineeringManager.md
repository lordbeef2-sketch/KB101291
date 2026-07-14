# JAVA OPENAPI: CodeEngineeringManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ce/CodeEngineeringManager.html
- source_path: `com/nomagic/magicdraw/ce/CodeEngineeringManager.html`
- source_sha256: `f41ed7e9a34fc8a422a2e86ae02c794c0e535a9bd13c556e6f6a4de0142f836e`
- captured_utc: `2026-07-14T16:57:51.413462+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ce](package-summary.html)

## Class CodeEngineeringManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ce.CodeEngineeringManager

@OpenApiAllpublic classCodeEngineeringManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Dedicated to perform Code Engineering reverse/generate task using MagicDraw OpenApi. It has
 static methods to create, remove, set some reverse settings for given code engineering set.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CodeEngineeringManager](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [CodeEngineeringSet](CodeEngineeringSet.html)`
`[createCodeEngineeringSet](#createCodeEngineeringSet(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) dialect,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Project](../core/Project.html) project,
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) workingPackage,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) workingDirectory)`
Given a language + dialect, name and working package of Code Engineering Set and project
 where to add this CES, creates new Code Engineering Set instance.
`static void`
`[generate](#generate(com.nomagic.magicdraw.ce.CodeEngineeringSet))([CodeEngineeringSet](CodeEngineeringSet.html) ces)`
Performs code engineering for given code engineering set.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CodeEngineeringSet](CodeEngineeringSet.html)>`
`[getAllCodeEngineeringSets](#getAllCodeEngineeringSets(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Given a project, returns list of all available code engineering sets.
`static [CodeEngineeringSet](CodeEngineeringSet.html)`
`[getCodeEngineeringSet](#getCodeEngineeringSet(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) dialect,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns Code engineering set from given project, which matches language, dialect and name.
`static void`
`[removeCodeEngineeringSet](#removeCodeEngineeringSet(com.nomagic.magicdraw.ce.CodeEngineeringSet))([CodeEngineeringSet](CodeEngineeringSet.html) codeEngineeringSet)`
Given a codeEngineeringSet, removes it with all inner elements.
`static void`
`[reverse](#reverse(com.nomagic.magicdraw.ce.CodeEngineeringSet,boolean))([CodeEngineeringSet](CodeEngineeringSet.html) ces,
 boolean showOptionDialog)`
Performs reverse engineering for given code engineering set.
`static void`
`[setClassFieldCreationType](#setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,boolean))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 boolean asAttribute)`
Deprecated.
use [`setClassFieldCreationType(Project, String, AttributeCreationType)`](#setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType))
`static void`
`[setClassFieldCreationType](#setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType type)`
Given a project and language of Code engineering set and, sets the default Class field creation type.
`static void`
`[setMergeModelAndCode](#setMergeModelAndCode(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean mergeCode)`
Reverse engineering option, for merging new code with model.
`static void`
`[setResetAlreadyCreatedFields](#setResetAlreadyCreatedFields(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean reset)`
Reverse engineering option, to reset already created fields.
`static void`
`[setResolveCollectionGenerics](#setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean resolve)`
Reverse engineering option, to enable resolve collection generic.
`static void`
`[setReverseAnalysisOption](#setReverseAnalysisOption(com.nomagic.magicdraw.core.Project,boolean,boolean))([Project](../core/Project.html) project,
 boolean createClassifiersDependencies,
 boolean createPackageDependencies)`
Sets reverse engineering analysis options.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CodeEngineeringManager
public CodeEngineeringManager()
 ============ METHOD DETAIL ========== 
Method Details
createCodeEngineeringSet
public static [CodeEngineeringSet](CodeEngineeringSet.html) createCodeEngineeringSet([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) dialect,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Project](../core/Project.html) project,
 @CheckForNull
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) workingPackage,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) workingDirectory)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)
Given a language + dialect, name and working package of Code Engineering Set and project
 where to add this CES, creates new Code Engineering Set instance.
Parameters:
`language` - Language of Code Engineering Set. Use [`CodeEngineeringConstants`](CodeEngineeringConstants.html) to get
 List of languages.
`dialect` - Dialect of language, this is dedicated for C++ or DDL CES. If language has no
 dialect, use null.
`name` - Name of Code Engineering Set.
`project` - project where to add new code engineering set.
`workingPackage` - Working package code engineering set.
`workingDirectory` - Directory of working files. This is path where files are located fore
 reverse, or where new files will be generated.
Returns:
created Code Engineering Set instance.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if given language is not supported.
removeCodeEngineeringSet
public static void removeCodeEngineeringSet([CodeEngineeringSet](CodeEngineeringSet.html) codeEngineeringSet)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)
Given a codeEngineeringSet, removes it with all inner elements.
Parameters:
`codeEngineeringSet` - set to be removed.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if code engineering set language is not supported.
getAllCodeEngineeringSets
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CodeEngineeringSet](CodeEngineeringSet.html)> getAllCodeEngineeringSets([Project](../core/Project.html) project)
Given a project, returns list of all available code engineering sets.
Parameters:
`project` - project of code engineering sets.
Returns:
List of available code engineering sets.
getCodeEngineeringSet
public static [CodeEngineeringSet](CodeEngineeringSet.html) getCodeEngineeringSet([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) dialect,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)
Returns Code engineering set from given project, which matches language, dialect and name.
Parameters:
`project` - MD project, where code engineering set should be.
`language` - Language of code engineering set. Use CodeEngineeringConstants.Languages to
 get constants.
`dialect` - dialect of language. Dedicated for C++ or DDL. Use
 CodeEngineeringConstants.Dialects to get constants.
`name` - name of code engineering set.
Returns:
code engineering set or null.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if given language is not supported.
setReverseAnalysisOption
public static void setReverseAnalysisOption([Project](../core/Project.html) project,
 boolean createClassifiersDependencies,
 boolean createPackageDependencies)
Sets reverse engineering analysis options. Applies to all code engineering sets for given
 project.
Parameters:
`project` - MagicDraw project, where to apply this option.
`createClassifiersDependencies` - True to create classifiers dependencies.
`createPackageDependencies` - True to create package dependencies.
setClassFieldCreationType
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static void setClassFieldCreationType([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 boolean asAttribute)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)
Deprecated.
use [`setClassFieldCreationType(Project, String, AttributeCreationType)`](#setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType))
Given a project and language of Code engineering set and, sets the default Class field
 creation as attribute if asAttribute field is true, and association if false.
Parameters:
`project` - MagicDraw project.
`language` - Code Engineering set language.
`asAttribute` - true, if creation type is Attribute, false if creation type is association.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if given language is not supported.
setClassFieldCreationType
public static void setClassFieldCreationType([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) language,
 com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType type)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)
Given a project and language of Code engineering set and, sets the default Class field creation type.
Parameters:
`project` - project.
`language` - Code Engineering set language.
`type` - class field creation type.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if given language is not supported.
setResolveCollectionGenerics
public static void setResolveCollectionGenerics([Project](../core/Project.html) project,
 boolean resolve)
Reverse engineering option, to enable resolve collection generic. Applies for all project's
 code engineering sets.
Parameters:
`project` - MD project.
`resolve` - True, to resolve, false to not resolve.
setResetAlreadyCreatedFields
public static void setResetAlreadyCreatedFields([Project](../core/Project.html) project,
 boolean reset)
Reverse engineering option, to reset already created fields.
 Applies for all project's code engineering sets.
Parameters:
`project` - MD project.
`reset` - true - reset, false - not reset.
setMergeModelAndCode
public static void setMergeModelAndCode([Project](../core/Project.html) project,
 boolean mergeCode)
Reverse engineering option, for merging new code with model. Applies for all project's code
 engineering sets.
Parameters:
`project` - MD project.
`mergeCode` - True to merge, false for not (default).
reverse
public static void reverse([CodeEngineeringSet](CodeEngineeringSet.html) ces,
 boolean showOptionDialog)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)
Performs reverse engineering for given code engineering set.
Parameters:
`ces` - code engineering set, to be reversed.
`showOptionDialog` - True to show code engineering option dialog, False for silent reverse.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if code engineering set language is not supported.
generate
public static void generate([CodeEngineeringSet](CodeEngineeringSet.html) ces)
 throws [IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)
Performs code engineering for given code engineering set.
Parameters:
`ces` - code engineering set to be generated.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if code engineering set language is not supported.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ce</a></div>
<h1 class="title" title="Class CodeEngineeringManager">Class CodeEngineeringManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ce.CodeEngineeringManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CodeEngineeringManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Dedicated to perform Code Engineering reverse/generate task using MagicDraw OpenApi. It has
 static methods to create, remove, set some reverse settings for given code engineering set.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CodeEngineeringManager</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCodeEngineeringSet(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String)">createCodeEngineeringSet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dialect,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> workingPackage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> workingDirectory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a language + dialect, name and working package of Code Engineering Set and project
 where to add this CES, creates new Code Engineering Set instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#generate(com.nomagic.magicdraw.ce.CodeEngineeringSet)">generate</a><wbr/>(<a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a> ces)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Performs code engineering for given code engineering set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllCodeEngineeringSets(com.nomagic.magicdraw.core.Project)">getAllCodeEngineeringSets</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a project, returns list of all available code engineering sets.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCodeEngineeringSet(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String)">getCodeEngineeringSet</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dialect,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns Code engineering set from given project, which matches language, dialect and name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCodeEngineeringSet(com.nomagic.magicdraw.ce.CodeEngineeringSet)">removeCodeEngineeringSet</a><wbr/>(<a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a> codeEngineeringSet)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a codeEngineeringSet, removes it with all inner elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#reverse(com.nomagic.magicdraw.ce.CodeEngineeringSet,boolean)">reverse</a><wbr/>(<a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a> ces,
 boolean showOptionDialog)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Performs reverse engineering for given code engineering set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">setClassFieldCreationType</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 boolean asAttribute)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType)"><code>setClassFieldCreationType(Project, String, AttributeCreationType)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType)">setClassFieldCreationType</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a project and language of Code engineering set and, sets the default Class field creation type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMergeModelAndCode(com.nomagic.magicdraw.core.Project,boolean)">setMergeModelAndCode</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean mergeCode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reverse engineering option, for merging new code with model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setResetAlreadyCreatedFields(com.nomagic.magicdraw.core.Project,boolean)">setResetAlreadyCreatedFields</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean reset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reverse engineering option, to reset already created fields.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean)">setResolveCollectionGenerics</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean resolve)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reverse engineering option, to enable resolve collection generic.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReverseAnalysisOption(com.nomagic.magicdraw.core.Project,boolean,boolean)">setReverseAnalysisOption</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean createClassifiersDependencies,
 boolean createPackageDependencies)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets reverse engineering analysis options.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>CodeEngineeringManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CodeEngineeringManager</span>()</div>
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
<section class="detail" id="createCodeEngineeringSet(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.lang.String)">
<h3>createCodeEngineeringSet</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a></span> <span class="element-name">createCodeEngineeringSet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dialect,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> workingPackage,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> workingDirectory)</span>
                                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Given a language + dialect, name and working package of Code Engineering Set and project
 where to add this CES, creates new Code Engineering Set instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - Language of Code Engineering Set. Use <a href="CodeEngineeringConstants.html" title="class in com.nomagic.magicdraw.ce"><code>CodeEngineeringConstants</code></a> to get
                         List of languages.</dd>
<dd><code>dialect</code> - Dialect of language, this is dedicated for C++ or DDL CES. If language has no
                         dialect, use null.</dd>
<dd><code>name</code> - Name of Code Engineering Set.</dd>
<dd><code>project</code> - project where to add new code engineering set.</dd>
<dd><code>workingPackage</code> - Working package code engineering set.</dd>
<dd><code>workingDirectory</code> - Directory of working files. This is path where files are located fore
                         reverse, or where new files will be generated.</dd>
<dt>Returns:</dt>
<dd>created Code Engineering Set instance.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if given language is not supported.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCodeEngineeringSet(com.nomagic.magicdraw.ce.CodeEngineeringSet)">
<h3>removeCodeEngineeringSet</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeCodeEngineeringSet</span><wbr/><span class="parameters">(<a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a> codeEngineeringSet)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Given a codeEngineeringSet, removes it with all inner elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>codeEngineeringSet</code> - set to be removed.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if code engineering set language is not supported.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllCodeEngineeringSets(com.nomagic.magicdraw.core.Project)">
<h3>getAllCodeEngineeringSets</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a>&gt;</span> <span class="element-name">getAllCodeEngineeringSets</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Given a project, returns list of all available code engineering sets.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project of code engineering sets.</dd>
<dt>Returns:</dt>
<dd>List of available code engineering sets.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCodeEngineeringSet(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.String,java.lang.String)">
<h3>getCodeEngineeringSet</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a></span> <span class="element-name">getCodeEngineeringSet</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dialect,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span>
                                                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Returns Code engineering set from given project, which matches language, dialect and name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MD project, where code engineering set should be.</dd>
<dd><code>language</code> - Language of code engineering set. Use CodeEngineeringConstants.Languages to
                 get constants.</dd>
<dd><code>dialect</code> - dialect of language. Dedicated for C++ or DDL. Use
                 CodeEngineeringConstants.Dialects to get constants.</dd>
<dd><code>name</code> - name of code engineering set.</dd>
<dt>Returns:</dt>
<dd>code engineering set or null.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if given language is not supported.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReverseAnalysisOption(com.nomagic.magicdraw.core.Project,boolean,boolean)">
<h3>setReverseAnalysisOption</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReverseAnalysisOption</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean createClassifiersDependencies,
 boolean createPackageDependencies)</span></div>
<div class="block">Sets reverse engineering analysis options. Applies to all code engineering sets for given
 project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MagicDraw project, where to apply this option.</dd>
<dd><code>createClassifiersDependencies</code> - True to create classifiers dependencies.</dd>
<dd><code>createPackageDependencies</code> - True to create package dependencies.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,boolean)">
<h3>setClassFieldCreationType</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setClassFieldCreationType</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 boolean asAttribute)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType)"><code>setClassFieldCreationType(Project, String, AttributeCreationType)</code></a></div>
</div>
<div class="block">Given a project and language of Code engineering set and, sets the default Class field
 creation as attribute if asAttribute field is true, and association if false.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MagicDraw project.</dd>
<dd><code>language</code> - Code Engineering set language.</dd>
<dd><code>asAttribute</code> - true, if creation type is Attribute, false if creation type is association.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if given language is not supported.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassFieldCreationType(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType)">
<h3>setClassFieldCreationType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setClassFieldCreationType</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 com.nomagic.magicdraw.ce.core.rt.options.AttributeCreationType type)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Given a project and language of Code engineering set and, sets the default Class field creation type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
<dd><code>language</code> - Code Engineering set language.</dd>
<dd><code>type</code> - class field creation type.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if given language is not supported.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean)">
<h3>setResolveCollectionGenerics</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setResolveCollectionGenerics</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean resolve)</span></div>
<div class="block">Reverse engineering option, to enable resolve collection generic. Applies for all project's
 code engineering sets.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MD project.</dd>
<dd><code>resolve</code> - True, to resolve, false to not resolve.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setResetAlreadyCreatedFields(com.nomagic.magicdraw.core.Project,boolean)">
<h3>setResetAlreadyCreatedFields</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setResetAlreadyCreatedFields</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean reset)</span></div>
<div class="block">Reverse engineering option, to reset already created fields.
 Applies for all project's code engineering sets.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MD project.</dd>
<dd><code>reset</code> - true - reset, false - not reset.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMergeModelAndCode(com.nomagic.magicdraw.core.Project,boolean)">
<h3>setMergeModelAndCode</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setMergeModelAndCode</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean mergeCode)</span></div>
<div class="block">Reverse engineering option, for merging new code with model. Applies for all project's code
 engineering sets.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MD project.</dd>
<dd><code>mergeCode</code> - True to merge, false for not (default).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reverse(com.nomagic.magicdraw.ce.CodeEngineeringSet,boolean)">
<h3>reverse</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">reverse</span><wbr/><span class="parameters">(<a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a> ces,
 boolean showOptionDialog)</span>
                    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Performs reverse engineering for given code engineering set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ces</code> - code engineering set, to be reversed.</dd>
<dd><code>showOptionDialog</code> - True to show code engineering option dialog, False for silent reverse.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if code engineering set language is not supported.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generate(com.nomagic.magicdraw.ce.CodeEngineeringSet)">
<h3>generate</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">generate</span><wbr/><span class="parameters">(<a href="CodeEngineeringSet.html" title="interface in com.nomagic.magicdraw.ce">CodeEngineeringSet</a> ces)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></span></div>
<div class="block">Performs code engineering for given code engineering set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ces</code> - code engineering set to be generated.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if code engineering set language is not supported.</dd>
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
