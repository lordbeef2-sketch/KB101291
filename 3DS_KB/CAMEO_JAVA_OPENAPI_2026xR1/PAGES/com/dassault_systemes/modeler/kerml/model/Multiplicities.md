# JAVA OPENAPI: Multiplicities (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Multiplicities.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Multiplicities.html`
- source_sha256: `862614760c9f13066a795092681071f6d1f03072b3091c1d9f2c354381afdb12`
- captured_utc: `2026-07-14T16:44:47.732838+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Multiplicities

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Multiplicities

@OpenApiAllpublic classMultiplicities
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Multiplicity`](kerml/Multiplicity.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[INFINITIVE_AS_INT](#INFINITIVE_AS_INT)`
Integer value representing a null multiplicity bound.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[LOWER_UPPER_MULTIPLICITY_REGEX](#LOWER_UPPER_MULTIPLICITY_REGEX)`
^ - Anchors the pattern to the start of the string.
`static final int`
`[NULL_AS_INT](#NULL_AS_INT)`
Integer value representing a null multiplicity bound.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SINGLE_MULTIPLICITY_REGEX](#SINGLE_MULTIPLICITY_REGEX)`
^ - Anchors the pattern to the start of the string.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Multiplicities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Multiplicity](kerml/Multiplicity.html)`
`[createMultiplicity](#createMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Creates a new [`Multiplicity`](kerml/Multiplicity.html) owned by the given type.
`static [MultiplicityRange](kerml/MultiplicityRange.html)`
`[createMultiplicityRange](#createMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Creates a new [`MultiplicityRange`](kerml/MultiplicityRange.html) owned by the given type.
`static [MultiplicityRange](kerml/MultiplicityRange.html)`
`[getEffectiveMultiplicityRange](#getEffectiveMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity))([Multiplicity](kerml/Multiplicity.html) multiplicity)`
Returns the effective multiplicity range for the given multiplicity.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MultiplicityRange](kerml/MultiplicityRange.html)>`
`[getMultiplicityRangesOf](#getMultiplicityRangesOf(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns all multiplicity ranges associated with the given type.
`static [Multiplicity](kerml/Multiplicity.html)`
`[getOwnedOrInheritedMultiplicity](#getOwnedOrInheritedMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the owned or inherited multiplicity of the given type.
`static boolean`
`[isExactlyOne](#isExactlyOne(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity))([Multiplicity](kerml/Multiplicity.html) multiplicity)`
Checks whether the multiplicity represents exactly one.
`static boolean`
`[isImplicitMultiplicity](#isImplicitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity))([Multiplicity](kerml/Multiplicity.html) multiplicity)`
Checks whether the multiplicity is implicit (i.e., has no explicit subsettings).
`static boolean`
`[isInfinitive](#isInfinitive(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Checks whether the given value represents an infinite multiplicity.
`static boolean`
`[isMultiple](#isMultiple(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange))([MultiplicityRange](kerml/MultiplicityRange.html) range)`
Checks whether the multiplicity range allows more than one value.
`static boolean`
`[isMultiple](#isMultiple(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) feature)`
Checks whether the given type has a multiplicity greater than one.
`static boolean`
`[isMultiplicityRangeZero](#isMultiplicityRangeZero(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange))([MultiplicityRange](kerml/MultiplicityRange.html) range)`
Checks whether the multiplicity range represents exactly zero.
`static boolean`
`[isNullValue](#isNullValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Checks whether the given value represents a null multiplicity.
`static boolean`
`[isPositive](#isPositive(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Checks whether the given value represents a positive multiplicity bound.
`static void`
`[setMultiplicity](#setMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.String))([Type](kerml/Type.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stringValue)`
Sets the multiplicity of the given type from a string value.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
NULL_AS_INT
public static final int NULL_AS_INT
Integer value representing a null multiplicity bound.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Multiplicities.NULL_AS_INT)
INFINITIVE_AS_INT
public static final int INFINITIVE_AS_INT
Integer value representing a null multiplicity bound.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Multiplicities.INFINITIVE_AS_INT)
LOWER_UPPER_MULTIPLICITY_REGEX
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) LOWER_UPPER_MULTIPLICITY_REGEX
^ - Anchors the pattern to the start of the string.
 \\d+ - Matches one or more digits (natural number).
 \\.\\. - Matches two literal dots. Since . is a special character in regex, it's escaped with double backslashes.
 ( ) - Captures the part after the two dots.
 \\d+ - Matches one or more digits (natural number).
 | - Acts as an "OR" operator, allowing for an alternative match.
 \\* - Matches the literal * symbol. The asterisk is also a special character in regex, so it is escaped.
 $ - Anchors the pattern to the end of the string.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Multiplicities.LOWER_UPPER_MULTIPLICITY_REGEX)
SINGLE_MULTIPLICITY_REGEX
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SINGLE_MULTIPLICITY_REGEX
^ - Anchors the pattern to the start of the string.
 \\d+ - Matches one or more digits (natural number).
 | - Acts as an "OR" operator, allowing for an alternative match.
 \\* - Matches the literal * symbol. The asterisk is also a special character in regex, so it is escaped.
 $ - Anchors the pattern to the end of the string.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Multiplicities.SINGLE_MULTIPLICITY_REGEX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Multiplicities
public Multiplicities()
 ============ METHOD DETAIL ========== 
Method Details
getOwnedOrInheritedMultiplicity
@CheckForNullpublic static [Multiplicity](kerml/Multiplicity.html) getOwnedOrInheritedMultiplicity([Type](kerml/Type.html) type)
Returns the owned or inherited multiplicity of the given type.
Parameters:
`type` - the type whose multiplicity is requested
Returns:
owned or inherited multiplicity, or null if none exists
createMultiplicity
public static [Multiplicity](kerml/Multiplicity.html) createMultiplicity([Type](kerml/Type.html) type)
Creates a new [`Multiplicity`](kerml/Multiplicity.html) owned by the given type.
Parameters:
`type` - the owning type
Returns:
the created multiplicity
createMultiplicityRange
public static [MultiplicityRange](kerml/MultiplicityRange.html) createMultiplicityRange([Type](kerml/Type.html) type)
Creates a new [`MultiplicityRange`](kerml/MultiplicityRange.html) owned by the given type.
Parameters:
`type` - the owning type
Returns:
the created multiplicity range
isPositive
public static boolean isPositive([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Checks whether the given value represents a positive multiplicity bound.
Parameters:
`value` - the value to check
Returns:
true if the value is non-negative or infinite
isNullValue
public static boolean isNullValue([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Checks whether the given value represents a null multiplicity.
Parameters:
`value` - the value to check
Returns:
true if the value represents a null bound
isInfinitive
public static boolean isInfinitive([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Checks whether the given value represents an infinite multiplicity.
Parameters:
`value` - the value to check
Returns:
true if the value represents infinity
getMultiplicityRangesOf
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[MultiplicityRange](kerml/MultiplicityRange.html)> getMultiplicityRangesOf([Type](kerml/Type.html) type)
Returns all multiplicity ranges associated with the given type.
Parameters:
`type` - the type to inspect
Returns:
list of multiplicity ranges
getEffectiveMultiplicityRange
@CheckForNullpublic static [MultiplicityRange](kerml/MultiplicityRange.html) getEffectiveMultiplicityRange([Multiplicity](kerml/Multiplicity.html) multiplicity)
Returns the effective multiplicity range for the given multiplicity.
 If the multiplicity is itself a range, it is returned directly.
Parameters:
`multiplicity` - the multiplicity to inspect
Returns:
effective multiplicity range, or null if none found
isImplicitMultiplicity
public static boolean isImplicitMultiplicity([Multiplicity](kerml/Multiplicity.html) multiplicity)
Checks whether the multiplicity is implicit (i.e., has no explicit subsettings).
Parameters:
`multiplicity` - the multiplicity to inspect
Returns:
true if the multiplicity is implicit
isMultiplicityRangeZero
public static boolean isMultiplicityRangeZero([MultiplicityRange](kerml/MultiplicityRange.html) range)
Checks whether the multiplicity range represents exactly zero.
Parameters:
`range` - the multiplicity range
Returns:
true if both bounds evaluate to zero
isExactlyOne
public static boolean isExactlyOne([Multiplicity](kerml/Multiplicity.html) multiplicity)
Checks whether the multiplicity represents exactly one.
Parameters:
`multiplicity` - the multiplicity to inspect
Returns:
true if the multiplicity is exactly one
isMultiple
public static boolean isMultiple([Type](kerml/Type.html) feature)
Checks whether the given type has a multiplicity greater than one.
Parameters:
`feature` - the type to inspect
Returns:
true if the multiplicity is multiple
isMultiple
public static boolean isMultiple([MultiplicityRange](kerml/MultiplicityRange.html) range)
Checks whether the multiplicity range allows more than one value.
Parameters:
`range` - the multiplicity range
Returns:
true if the upper bound is infinite or greater than one
setMultiplicity
public static void setMultiplicity([Type](kerml/Type.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) stringValue)
Sets the multiplicity of the given type from a string value.
 Supports both "lower..upper" and single-value formats.
Parameters:
`type` - the type to modify
`stringValue` - the multiplicity string

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Multiplicities">Class Multiplicities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Multiplicities</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Multiplicities</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Multiplicity</code></a></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INFINITIVE_AS_INT">INFINITIVE_AS_INT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Integer value representing a null multiplicity bound.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOWER_UPPER_MULTIPLICITY_REGEX">LOWER_UPPER_MULTIPLICITY_REGEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">^ - Anchors the pattern to the start of the string.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NULL_AS_INT">NULL_AS_INT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Integer value representing a null multiplicity bound.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SINGLE_MULTIPLICITY_REGEX">SINGLE_MULTIPLICITY_REGEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">^ - Anchors the pattern to the start of the string.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Multiplicities</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type)">createMultiplicity</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new <a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Multiplicity</code></a> owned by the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.Type)">createMultiplicityRange</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new <a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MultiplicityRange</code></a> owned by the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEffectiveMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity)">getEffectiveMultiplicityRange</a><wbr/>(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> multiplicity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the effective multiplicity range for the given multiplicity.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMultiplicityRangesOf(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getMultiplicityRangesOf</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all multiplicity ranges associated with the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedOrInheritedMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedOrInheritedMultiplicity</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned or inherited multiplicity of the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isExactlyOne(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity)">isExactlyOne</a><wbr/>(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> multiplicity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the multiplicity represents exactly one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isImplicitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity)">isImplicitMultiplicity</a><wbr/>(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> multiplicity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the multiplicity is implicit (i.e., has no explicit subsettings).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInfinitive(java.lang.Object)">isInfinitive</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given value represents an infinite multiplicity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMultiple(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange)">isMultiple</a><wbr/>(<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a> range)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the multiplicity range allows more than one value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMultiple(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isMultiple</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given type has a multiplicity greater than one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMultiplicityRangeZero(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange)">isMultiplicityRangeZero</a><wbr/>(<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a> range)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the multiplicity range represents exactly zero.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNullValue(java.lang.Object)">isNullValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given value represents a null multiplicity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPositive(java.lang.Object)">isPositive</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given value represents a positive multiplicity bound.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.String)">setMultiplicity</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stringValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the multiplicity of the given type from a string value.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="NULL_AS_INT">
<h3>NULL_AS_INT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">NULL_AS_INT</span></div>
<div class="block">Integer value representing a null multiplicity bound.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Multiplicities.NULL_AS_INT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INFINITIVE_AS_INT">
<h3>INFINITIVE_AS_INT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">INFINITIVE_AS_INT</span></div>
<div class="block">Integer value representing a null multiplicity bound.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Multiplicities.INFINITIVE_AS_INT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOWER_UPPER_MULTIPLICITY_REGEX">
<h3>LOWER_UPPER_MULTIPLICITY_REGEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOWER_UPPER_MULTIPLICITY_REGEX</span></div>
<div class="block">^ - Anchors the pattern to the start of the string.
 \\d+ - Matches one or more digits (natural number).
 \\.\\. - Matches two literal dots. Since . is a special character in regex, it's escaped with double backslashes.
 ( ) - Captures the part after the two dots.
 \\d+ - Matches one or more digits (natural number).
 | - Acts as an "OR" operator, allowing for an alternative match.
 \\* - Matches the literal * symbol. The asterisk is also a special character in regex, so it is escaped.
 $ - Anchors the pattern to the end of the string.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Multiplicities.LOWER_UPPER_MULTIPLICITY_REGEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SINGLE_MULTIPLICITY_REGEX">
<h3>SINGLE_MULTIPLICITY_REGEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SINGLE_MULTIPLICITY_REGEX</span></div>
<div class="block">^ - Anchors the pattern to the start of the string.
 \\d+ - Matches one or more digits (natural number).
 | - Acts as an "OR" operator, allowing for an alternative match.
 \\* - Matches the literal * symbol. The asterisk is also a special character in regex, so it is escaped.
 $ - Anchors the pattern to the end of the string.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Multiplicities.SINGLE_MULTIPLICITY_REGEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Multiplicities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Multiplicities</span>()</div>
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
<section class="detail" id="getOwnedOrInheritedMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedOrInheritedMultiplicity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></span> <span class="element-name">getOwnedOrInheritedMultiplicity</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the owned or inherited multiplicity of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose multiplicity is requested</dd>
<dt>Returns:</dt>
<dd>owned or inherited multiplicity, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>createMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a></span> <span class="element-name">createMultiplicity</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Creates a new <a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Multiplicity</code></a> owned by the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the owning type</dd>
<dt>Returns:</dt>
<dd>the created multiplicity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>createMultiplicityRange</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></span> <span class="element-name">createMultiplicityRange</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Creates a new <a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MultiplicityRange</code></a> owned by the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the owning type</dd>
<dt>Returns:</dt>
<dd>the created multiplicity range</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPositive(java.lang.Object)">
<h3>isPositive</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPositive</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Checks whether the given value represents a positive multiplicity bound.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the value to check</dd>
<dt>Returns:</dt>
<dd>true if the value is non-negative or infinite</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNullValue(java.lang.Object)">
<h3>isNullValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNullValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Checks whether the given value represents a null multiplicity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the value to check</dd>
<dt>Returns:</dt>
<dd>true if the value represents a null bound</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInfinitive(java.lang.Object)">
<h3>isInfinitive</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInfinitive</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Checks whether the given value represents an infinite multiplicity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - the value to check</dd>
<dt>Returns:</dt>
<dd>true if the value represents infinity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMultiplicityRangesOf(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getMultiplicityRangesOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a>&gt;</span> <span class="element-name">getMultiplicityRangesOf</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all multiplicity ranges associated with the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>list of multiplicity ranges</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEffectiveMultiplicityRange(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity)">
<h3>getEffectiveMultiplicityRange</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a></span> <span class="element-name">getEffectiveMultiplicityRange</span><wbr/><span class="parameters">(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> multiplicity)</span></div>
<div class="block">Returns the effective multiplicity range for the given multiplicity.
 If the multiplicity is itself a range, it is returned directly.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>multiplicity</code> - the multiplicity to inspect</dd>
<dt>Returns:</dt>
<dd>effective multiplicity range, or null if none found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isImplicitMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity)">
<h3>isImplicitMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isImplicitMultiplicity</span><wbr/><span class="parameters">(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> multiplicity)</span></div>
<div class="block">Checks whether the multiplicity is implicit (i.e., has no explicit subsettings).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>multiplicity</code> - the multiplicity to inspect</dd>
<dt>Returns:</dt>
<dd>true if the multiplicity is implicit</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMultiplicityRangeZero(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange)">
<h3>isMultiplicityRangeZero</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMultiplicityRangeZero</span><wbr/><span class="parameters">(<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a> range)</span></div>
<div class="block">Checks whether the multiplicity range represents exactly zero.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>range</code> - the multiplicity range</dd>
<dt>Returns:</dt>
<dd>true if both bounds evaluate to zero</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExactlyOne(com.dassault_systemes.modeler.kerml.model.kerml.Multiplicity)">
<h3>isExactlyOne</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExactlyOne</span><wbr/><span class="parameters">(<a href="kerml/Multiplicity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Multiplicity</a> multiplicity)</span></div>
<div class="block">Checks whether the multiplicity represents exactly one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>multiplicity</code> - the multiplicity to inspect</dd>
<dt>Returns:</dt>
<dd>true if the multiplicity is exactly one</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMultiple(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isMultiple</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMultiple</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> feature)</span></div>
<div class="block">Checks whether the given type has a multiplicity greater than one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>true if the multiplicity is multiple</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMultiple(com.dassault_systemes.modeler.kerml.model.kerml.MultiplicityRange)">
<h3>isMultiple</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMultiple</span><wbr/><span class="parameters">(<a href="kerml/MultiplicityRange.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MultiplicityRange</a> range)</span></div>
<div class="block">Checks whether the multiplicity range allows more than one value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>range</code> - the multiplicity range</dd>
<dt>Returns:</dt>
<dd>true if the upper bound is infinite or greater than one</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMultiplicity(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.String)">
<h3>setMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setMultiplicity</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stringValue)</span></div>
<div class="block">Sets the multiplicity of the given type from a string value.
 Supports both "lower..upper" and single-value formats.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to modify</dd>
<dd><code>stringValue</code> - the multiplicity string</dd>
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
