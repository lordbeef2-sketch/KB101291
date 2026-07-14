# JAVA OPENAPI: RepresentationTextParams (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/RepresentationTextParams.html
- source_path: `com/nomagic/magicdraw/uml/RepresentationTextParams.html`
- source_sha256: `1ef6651603ecc42bc799fc80ca1dc8a72aee0e8d762e146abefc2833fad8b010`
- captured_utc: `2026-07-14T16:52:10.874865+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class RepresentationTextParams

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.RepresentationTextParams

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic final classRepresentationTextParams
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)

Configuration for getting element's text from [`RepresentationTextCreator`](RepresentationTextCreator.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RepresentationTextParams](#%3Cinit%3E())()`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[RepresentationTextParams](RepresentationTextParams.html)`
`[clone](#clone())()`

`static [RepresentationTextParams](RepresentationTextParams.html)`
`[createByEnvironmentOptions](#createByEnvironmentOptions())()`
Creates new instance of representation params and sets fields depending on [`EnvironmentOptions`](../core/options/EnvironmentOptions.html).
`static [RepresentationTextParams](RepresentationTextParams.html)`
`[createByOptions](#createByOptions(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Creates new instance of representation params and sets fields depending on both Environment and Project options.
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[LocationInTool](../ui/LocationInTool.html)`
`[getLocationInTool](#getLocationInTool())()`
Invocation information.
`int`
`[getMaxTextLength](#getMaxTextLength())()`

`int`
`[hashCode](#hashCode())()`

`boolean`
`[isAddColor](#isAddColor())()`
Defines if color information should be added to the representation text.
`boolean`
`[isAddHumanType](#isAddHumanType())()`
Checks if we need to add human type to name
`boolean`
`[isForceShowTypeName](#isForceShowTypeName())()`
Defines if element auto numbers (IDs) should be included to the representation text.
`boolean`
`[isShowElementNumber](#isShowElementNumber())()`
Defines if element auto numbers (IDs) should be included to the representation text.
`boolean`
`[isShowFullType](#isShowFullType())()`
Defines how text of some elements should be constructed.
`boolean`
`[isShowPostfix](#isShowPostfix())()`

`boolean`
`[isShowPrefix](#isShowPrefix())()`

`[RepresentationTextParams](RepresentationTextParams.html)`
`[setAddColor](#setAddColor(boolean))(boolean addColor)`

`[RepresentationTextParams](RepresentationTextParams.html)`
`[setAddHumanType](#setAddHumanType(boolean))(boolean addHumanType)`
Set to add human type to name
`[RepresentationTextParams](RepresentationTextParams.html)`
`[setForceShowTypeName](#setForceShowTypeName(boolean))(boolean forceShowTypeName)`

`[RepresentationTextParams](RepresentationTextParams.html)`
`[setLocationInTool](#setLocationInTool(com.nomagic.magicdraw.ui.LocationInTool))([LocationInTool](../ui/LocationInTool.html) locationInTool)`

`[RepresentationTextParams](RepresentationTextParams.html)`
`[setMaxTextLength](#setMaxTextLength(int))(int maxTextLength)`
Set max expected text length.
`[RepresentationTextParams](RepresentationTextParams.html)`
`[setShowElementNumber](#setShowElementNumber(boolean))(boolean showElementNumber)`

`[RepresentationTextParams](RepresentationTextParams.html)`
`[setShowFullType](#setShowFullType(boolean))(boolean showFullType)`

`[RepresentationTextParams](RepresentationTextParams.html)`
`[setShowPostfix](#setShowPostfix(boolean))(boolean showPostfix)`
Set to show or hide prefix
`[RepresentationTextParams](RepresentationTextParams.html)`
`[setShowPrefix](#setShowPrefix(boolean))(boolean showPrefix)`
Set to show or hide prefix
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RepresentationTextParams
public RepresentationTextParams()
Constructor
 ============ METHOD DETAIL ========== 
Method Details
createByEnvironmentOptions
public static [RepresentationTextParams](RepresentationTextParams.html) createByEnvironmentOptions()
Creates new instance of representation params and sets fields depending on [`EnvironmentOptions`](../core/options/EnvironmentOptions.html).
 Only [`isShowFullType()`](#isShowFullType()) value is affected.
Returns:
new text params instance pre-configured by environment options
createByOptions
public static [RepresentationTextParams](RepresentationTextParams.html) createByOptions([Project](../core/Project.html) project)
Creates new instance of representation params and sets fields depending on both Environment and Project options.
 [`isShowFullType()`](#isShowFullType()) and [`isShowElementNumber()`](#isShowElementNumber()) values are affected.
Returns:
new text params instance pre-configured by environment and project options
setAddColor
public [RepresentationTextParams](RepresentationTextParams.html) setAddColor(boolean addColor)
Parameters:
`addColor` - if true, color information will be added to the text
isAddColor
public boolean isAddColor()
Defines if color information should be added to the representation text. Default is `false`.
 Color information should be added when rendering colored text in UI.
Returns:
true if color information should be added
isForceShowTypeName
public boolean isForceShowTypeName()
Defines if element auto numbers (IDs) should be included to the representation text. Default is `false`.
Returns:
true if element auto numbers (IDs) should be included
setForceShowTypeName
public [RepresentationTextParams](RepresentationTextParams.html) setForceShowTypeName(boolean forceShowTypeName)
Parameters:
`forceShowTypeName` - true if element need to show type name if it's name is empty
isShowElementNumber
public boolean isShowElementNumber()
Defines if element auto numbers (IDs) should be included to the representation text. Default is `false`.
Returns:
true if element auto numbers (IDs) should be included
setShowElementNumber
public [RepresentationTextParams](RepresentationTextParams.html) setShowElementNumber(boolean showElementNumber)
Parameters:
`showElementNumber` - true if element auto numbers (IDs) should be included
setShowFullType
public [RepresentationTextParams](RepresentationTextParams.html) setShowFullType(boolean showFullType)
Parameters:
`showFullType` - if Type of TypedElement should be represented by full qualified name.
 Also affects text of relationship end elements.
getMaxTextLength
public int getMaxTextLength()
Returns:
max text length.
setMaxTextLength
public [RepresentationTextParams](RepresentationTextParams.html) setMaxTextLength(int maxTextLength)
Set max expected text length. There is no guarantee this option will be respected by [`RepresentationTextCreator`](RepresentationTextCreator.html)
Parameters:
`maxTextLength` - max text length.
setAddHumanType
public [RepresentationTextParams](RepresentationTextParams.html) setAddHumanType(boolean addHumanType)
Set to add human type to name
Parameters:
`addHumanType` - flag to indicate if we add or not humann type to text (default is true)
isAddHumanType
public boolean isAddHumanType()
Checks if we need to add human type to name
Returns:
true if we need to add, else false
isShowFullType
public boolean isShowFullType()
Defines how text of some elements should be constructed.
 Affects Type text for [`TypedElement`](../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) and end element text
 for [`Relationship`](../../uml2/ext/magicdraw/classes/mdkernel/Relationship.html) elements. Default value is `false`.
Returns:
true if specific elements will be represented by full qualified name, false if name will be used
setLocationInTool
public [RepresentationTextParams](RepresentationTextParams.html) setLocationInTool([LocationInTool](../ui/LocationInTool.html) locationInTool)
Parameters:
`locationInTool` - describes GUI location for which text is being created
See Also:
[`LocationInTool`](../ui/LocationInTool.html)
getLocationInTool
public [LocationInTool](../ui/LocationInTool.html) getLocationInTool()
Invocation information. See [`LocationInTool`](../ui/LocationInTool.html). Default is [`LocationInTool.unknown`](../ui/LocationInTool.html#unknown)
Returns:
location in tool
isShowPrefix
public boolean isShowPrefix()
Returns:
true if prefix should be added
setShowPrefix
public [RepresentationTextParams](RepresentationTextParams.html) setShowPrefix(boolean showPrefix)
Set to show or hide prefix
Parameters:
`showPrefix` - false if prefix should not be added
isShowPostfix
public boolean isShowPostfix()
Returns:
true if postfix should be added
setShowPostfix
public [RepresentationTextParams](RepresentationTextParams.html) setShowPostfix(boolean showPostfix)
Set to show or hide prefix
Parameters:
`showPostfix` - false if postfix should not be added
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
clone
public [RepresentationTextParams](RepresentationTextParams.html) clone()
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class RepresentationTextParams">Class RepresentationTextParams</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.RepresentationTextParams</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">RepresentationTextParams</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
<div class="block">Configuration for getting element's text from <a href="RepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextCreator</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">RepresentationTextParams</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createByEnvironmentOptions()">createByEnvironmentOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates new instance of representation params and sets fields depending on <a href="../core/options/EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options"><code>EnvironmentOptions</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createByOptions(com.nomagic.magicdraw.core.Project)">createByOptions</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates new instance of representation params and sets fields depending on both Environment and Project options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocationInTool()">getLocationInTool</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invocation information.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMaxTextLength()">getMaxTextLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAddColor()">isAddColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Defines if color information should be added to the representation text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAddHumanType()">isAddHumanType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if we need to add human type to name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isForceShowTypeName()">isForceShowTypeName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Defines if  element auto numbers (IDs) should be included to the representation text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowElementNumber()">isShowElementNumber</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Defines if  element auto numbers (IDs) should be included to the representation text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowFullType()">isShowFullType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Defines how text of some elements should be constructed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowPostfix()">isShowPostfix</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowPrefix()">isShowPrefix</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAddColor(boolean)">setAddColor</a><wbr/>(boolean addColor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAddHumanType(boolean)">setAddHumanType</a><wbr/>(boolean addHumanType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set to add human type to name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setForceShowTypeName(boolean)">setForceShowTypeName</a><wbr/>(boolean forceShowTypeName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocationInTool(com.nomagic.magicdraw.ui.LocationInTool)">setLocationInTool</a><wbr/>(<a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a> locationInTool)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMaxTextLength(int)">setMaxTextLength</a><wbr/>(int maxTextLength)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set max expected text length.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowElementNumber(boolean)">setShowElementNumber</a><wbr/>(boolean showElementNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowFullType(boolean)">setShowFullType</a><wbr/>(boolean showFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowPostfix(boolean)">setShowPostfix</a><wbr/>(boolean showPostfix)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set to show or hide prefix</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowPrefix(boolean)">setShowPrefix</a><wbr/>(boolean showPrefix)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set to show or hide prefix</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>RepresentationTextParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RepresentationTextParams</span>()</div>
<div class="block">Constructor</div>
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
<section class="detail" id="createByEnvironmentOptions()">
<h3>createByEnvironmentOptions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">createByEnvironmentOptions</span>()</div>
<div class="block">Creates new instance of representation params and sets fields depending on <a href="../core/options/EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options"><code>EnvironmentOptions</code></a>.
 Only <a href="#isShowFullType()"><code>isShowFullType()</code></a>  value is affected.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>new text params instance pre-configured by environment options</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createByOptions(com.nomagic.magicdraw.core.Project)">
<h3>createByOptions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">createByOptions</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Creates new instance of representation params and sets fields depending on both Environment and Project options.
 <a href="#isShowFullType()"><code>isShowFullType()</code></a> and <a href="#isShowElementNumber()"><code>isShowElementNumber()</code></a> values are affected.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>new text params instance pre-configured by environment and project options</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAddColor(boolean)">
<h3>setAddColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setAddColor</span><wbr/><span class="parameters">(boolean addColor)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>addColor</code> - if true, color information will be added to the text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAddColor()">
<h3>isAddColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAddColor</span>()</div>
<div class="block">Defines if color information should be added to the representation text. Default is <code>false</code>.
 Color information should be added when rendering colored text in UI.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if color information should be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isForceShowTypeName()">
<h3>isForceShowTypeName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isForceShowTypeName</span>()</div>
<div class="block">Defines if  element auto numbers (IDs) should be included to the representation text. Default is <code>false</code>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if element auto numbers (IDs) should be included</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setForceShowTypeName(boolean)">
<h3>setForceShowTypeName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setForceShowTypeName</span><wbr/><span class="parameters">(boolean forceShowTypeName)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>forceShowTypeName</code> - true if element need to show type name if it's name is empty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowElementNumber()">
<h3>isShowElementNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowElementNumber</span>()</div>
<div class="block">Defines if  element auto numbers (IDs) should be included to the representation text. Default is <code>false</code>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if element auto numbers (IDs) should be included</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowElementNumber(boolean)">
<h3>setShowElementNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setShowElementNumber</span><wbr/><span class="parameters">(boolean showElementNumber)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showElementNumber</code> - true if element auto numbers (IDs) should be included</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowFullType(boolean)">
<h3>setShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setShowFullType</span><wbr/><span class="parameters">(boolean showFullType)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showFullType</code> - if Type of TypedElement should be represented by full qualified name.
                     Also affects text of relationship end elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMaxTextLength()">
<h3>getMaxTextLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getMaxTextLength</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>max text length.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMaxTextLength(int)">
<h3>setMaxTextLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setMaxTextLength</span><wbr/><span class="parameters">(int maxTextLength)</span></div>
<div class="block">Set max expected text length. There is no guarantee this option will be respected by <a href="RepresentationTextCreator.html" title="class in com.nomagic.magicdraw.uml"><code>RepresentationTextCreator</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>maxTextLength</code> - max text length.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAddHumanType(boolean)">
<h3>setAddHumanType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setAddHumanType</span><wbr/><span class="parameters">(boolean addHumanType)</span></div>
<div class="block">Set to add human type to name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>addHumanType</code> - flag to indicate if we add or not humann type to text (default is true)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAddHumanType()">
<h3>isAddHumanType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAddHumanType</span>()</div>
<div class="block">Checks if we need to add human type to name</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if we need to add, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowFullType()">
<h3>isShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowFullType</span>()</div>
<div class="block">Defines how text of some elements should be constructed.
 Affects Type text for <a href="../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>TypedElement</code></a> and end element text
 for <a href="../../uml2/ext/magicdraw/classes/mdkernel/Relationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Relationship</code></a> elements. Default value is <code>false</code>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if specific elements will be represented by full qualified name, false if name will be used</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocationInTool(com.nomagic.magicdraw.ui.LocationInTool)">
<h3>setLocationInTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setLocationInTool</span><wbr/><span class="parameters">(<a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a> locationInTool)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationInTool</code> - describes GUI location for which text is being created</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui"><code>LocationInTool</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocationInTool()">
<h3>getLocationInTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">getLocationInTool</span>()</div>
<div class="block">Invocation information. See <a href="../ui/LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui"><code>LocationInTool</code></a>. Default is <a href="../ui/LocationInTool.html#unknown"><code>LocationInTool.unknown</code></a></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>location in tool</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowPrefix()">
<h3>isShowPrefix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowPrefix</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if prefix should be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowPrefix(boolean)">
<h3>setShowPrefix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setShowPrefix</span><wbr/><span class="parameters">(boolean showPrefix)</span></div>
<div class="block">Set to show or hide prefix</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showPrefix</code> - false if prefix should not be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowPostfix()">
<h3>isShowPostfix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowPostfix</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if postfix should be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowPostfix(boolean)">
<h3>setShowPostfix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">setShowPostfix</span><wbr/><span class="parameters">(boolean showPostfix)</span></div>
<div class="block">Set to show or hide prefix</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showPostfix</code> - false if postfix should not be added</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RepresentationTextParams.html" title="class in com.nomagic.magicdraw.uml">RepresentationTextParams</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
