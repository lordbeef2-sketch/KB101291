# JAVA OPENAPI: BehaviorTextParams (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/text/BehaviorTextParams.html
- source_path: `com/nomagic/magicdraw/uml/text/BehaviorTextParams.html`
- source_sha256: `0c23f4ceb84c7d55aae078dc77c7d898271548843583a40277bcb693e95a7e0e`
- captured_utc: `2026-07-14T16:56:05.530570+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.text](package-summary.html)

## Class BehaviorTextParams

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.text.MemberTextParams](MemberTextParams.html)
com.nomagic.magicdraw.uml.text.BehaviorTextParams

@OpenApiAllpublic classBehaviorTextParams
extends [MemberTextParams](MemberTextParams.html)
Configuration for creating Behavior element text with [`ModelTextCreator`](ModelTextCreator.html).

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BehaviorTextParams](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[isShowFullType](#isShowFullType())()`

`boolean`
`[isShowOpaqueBehaviorBody](#isShowOpaqueBehaviorBody())()`

`boolean`
`[isShowParameterDirectionKind](#isShowParameterDirectionKind())()`

`boolean`
`[isShowParameters](#isShowParameters())()`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setInvisibleFilter](#setInvisibleFilter(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> invisibleFilter)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowAdditionalSlotText](#setShowAdditionalSlotText(boolean))(boolean showAdditionalSlotText)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowConstraintName](#setShowConstraintName(boolean))(boolean showConstraintName)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowConstraintSpecification](#setShowConstraintSpecification(boolean))(boolean showConstraintSpecification)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowFullType](#setShowFullType(boolean))(boolean showFullType)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowInheritedSign](#setShowInheritedSign(boolean))(boolean showInheritedSign)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowName](#setShowName(boolean))(boolean showName)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowOpaqueBehaviorBody](#setShowOpaqueBehaviorBody(boolean))(boolean showOpaqueBehaviorBody)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowParameterDirectionKind](#setShowParameterDirectionKind(boolean))(boolean showDirectionKind)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowParameters](#setShowParameters(boolean))(boolean showParameters)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowProperties](#setShowProperties(boolean))(boolean showProperties)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowStereotype](#setShowStereotype(boolean))(boolean showStereotype)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowTaggedValues](#setShowTaggedValues(boolean))(boolean showTaggedValues)`

`[BehaviorTextParams](BehaviorTextParams.html)`
`[setShowVisibility](#setShowVisibility(boolean))(boolean showVisibility)`
Methods inherited from class com.nomagic.magicdraw.uml.text.[MemberTextParams](MemberTextParams.html)
`[getInvisibleFilter](MemberTextParams.html#getInvisibleFilter()), [isShowAdditionalSlotText](MemberTextParams.html#isShowAdditionalSlotText()), [isShowConstraintName](MemberTextParams.html#isShowConstraintName()), [isShowConstraintSpecification](MemberTextParams.html#isShowConstraintSpecification()), [isShowInheritedSign](MemberTextParams.html#isShowInheritedSign()), [isShowName](MemberTextParams.html#isShowName()), [isShowProperties](MemberTextParams.html#isShowProperties()), [isShowStereotype](MemberTextParams.html#isShowStereotype()), [isShowTaggedValues](MemberTextParams.html#isShowTaggedValues()), [isShowVisibility](MemberTextParams.html#isShowVisibility())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BehaviorTextParams
public BehaviorTextParams()
 ============ METHOD DETAIL ========== 
Method Details
setShowName
public [BehaviorTextParams](BehaviorTextParams.html) setShowName(boolean showName)
Overrides:
`[setShowName](MemberTextParams.html#setShowName(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowVisibility
public [BehaviorTextParams](BehaviorTextParams.html) setShowVisibility(boolean showVisibility)
Overrides:
`[setShowVisibility](MemberTextParams.html#setShowVisibility(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowStereotype
public [BehaviorTextParams](BehaviorTextParams.html) setShowStereotype(boolean showStereotype)
Overrides:
`[setShowStereotype](MemberTextParams.html#setShowStereotype(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowProperties
public [BehaviorTextParams](BehaviorTextParams.html) setShowProperties(boolean showProperties)
Overrides:
`[setShowProperties](MemberTextParams.html#setShowProperties(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowTaggedValues
public [BehaviorTextParams](BehaviorTextParams.html) setShowTaggedValues(boolean showTaggedValues)
Overrides:
`[setShowTaggedValues](MemberTextParams.html#setShowTaggedValues(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowConstraintName
public [BehaviorTextParams](BehaviorTextParams.html) setShowConstraintName(boolean showConstraintName)
Overrides:
`[setShowConstraintName](MemberTextParams.html#setShowConstraintName(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowConstraintSpecification
public [BehaviorTextParams](BehaviorTextParams.html) setShowConstraintSpecification(boolean showConstraintSpecification)
Overrides:
`[setShowConstraintSpecification](MemberTextParams.html#setShowConstraintSpecification(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowInheritedSign
public [BehaviorTextParams](BehaviorTextParams.html) setShowInheritedSign(boolean showInheritedSign)
Overrides:
`[setShowInheritedSign](MemberTextParams.html#setShowInheritedSign(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowAdditionalSlotText
public [BehaviorTextParams](BehaviorTextParams.html) setShowAdditionalSlotText(boolean showAdditionalSlotText)
Overrides:
`[setShowAdditionalSlotText](MemberTextParams.html#setShowAdditionalSlotText(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setInvisibleFilter
public [BehaviorTextParams](BehaviorTextParams.html) setInvisibleFilter([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> invisibleFilter)
Overrides:
`[setInvisibleFilter](MemberTextParams.html#setInvisibleFilter(java.util.function.Predicate))` in class `[MemberTextParams](MemberTextParams.html)`
setShowParameters
public [BehaviorTextParams](BehaviorTextParams.html) setShowParameters(boolean showParameters)
setShowFullType
public [BehaviorTextParams](BehaviorTextParams.html) setShowFullType(boolean showFullType)
setShowParameterDirectionKind
public [BehaviorTextParams](BehaviorTextParams.html) setShowParameterDirectionKind(boolean showDirectionKind)
setShowOpaqueBehaviorBody
public [BehaviorTextParams](BehaviorTextParams.html) setShowOpaqueBehaviorBody(boolean showOpaqueBehaviorBody)
isShowFullType
public boolean isShowFullType()
isShowParameterDirectionKind
public boolean isShowParameterDirectionKind()
isShowParameters
public boolean isShowParameters()
isShowOpaqueBehaviorBody
public boolean isShowOpaqueBehaviorBody()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.text</a></div>
<h1 class="title" title="Class BehaviorTextParams">Class BehaviorTextParams</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">com.nomagic.magicdraw.uml.text.MemberTextParams</a>
<div class="inheritance">com.nomagic.magicdraw.uml.text.BehaviorTextParams</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">BehaviorTextParams</span>
<span class="extends-implements">extends <a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></span></div>
<div class="block">Configuration for creating Behavior element text with <a href="ModelTextCreator.html" title="class in com.nomagic.magicdraw.uml.text"><code>ModelTextCreator</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">BehaviorTextParams</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowFullType()">isShowFullType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowOpaqueBehaviorBody()">isShowOpaqueBehaviorBody</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowParameterDirectionKind()">isShowParameterDirectionKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowParameters()">isShowParameters</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInvisibleFilter(java.util.function.Predicate)">setInvisibleFilter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; invisibleFilter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowAdditionalSlotText(boolean)">setShowAdditionalSlotText</a><wbr/>(boolean showAdditionalSlotText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowConstraintName(boolean)">setShowConstraintName</a><wbr/>(boolean showConstraintName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowConstraintSpecification(boolean)">setShowConstraintSpecification</a><wbr/>(boolean showConstraintSpecification)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowFullType(boolean)">setShowFullType</a><wbr/>(boolean showFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowInheritedSign(boolean)">setShowInheritedSign</a><wbr/>(boolean showInheritedSign)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowName(boolean)">setShowName</a><wbr/>(boolean showName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowOpaqueBehaviorBody(boolean)">setShowOpaqueBehaviorBody</a><wbr/>(boolean showOpaqueBehaviorBody)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowParameterDirectionKind(boolean)">setShowParameterDirectionKind</a><wbr/>(boolean showDirectionKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowParameters(boolean)">setShowParameters</a><wbr/>(boolean showParameters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowProperties(boolean)">setShowProperties</a><wbr/>(boolean showProperties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowStereotype(boolean)">setShowStereotype</a><wbr/>(boolean showStereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowTaggedValues(boolean)">setShowTaggedValues</a><wbr/>(boolean showTaggedValues)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowVisibility(boolean)">setShowVisibility</a><wbr/>(boolean showVisibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.text.MemberTextParams">Methods inherited from class com.nomagic.magicdraw.uml.text.<a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></h3>
<code><a href="MemberTextParams.html#getInvisibleFilter()">getInvisibleFilter</a>, <a href="MemberTextParams.html#isShowAdditionalSlotText()">isShowAdditionalSlotText</a>, <a href="MemberTextParams.html#isShowConstraintName()">isShowConstraintName</a>, <a href="MemberTextParams.html#isShowConstraintSpecification()">isShowConstraintSpecification</a>, <a href="MemberTextParams.html#isShowInheritedSign()">isShowInheritedSign</a>, <a href="MemberTextParams.html#isShowName()">isShowName</a>, <a href="MemberTextParams.html#isShowProperties()">isShowProperties</a>, <a href="MemberTextParams.html#isShowStereotype()">isShowStereotype</a>, <a href="MemberTextParams.html#isShowTaggedValues()">isShowTaggedValues</a>, <a href="MemberTextParams.html#isShowVisibility()">isShowVisibility</a></code></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>BehaviorTextParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BehaviorTextParams</span>()</div>
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
<section class="detail" id="setShowName(boolean)">
<h3>setShowName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowName</span><wbr/><span class="parameters">(boolean showName)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowName(boolean)">setShowName</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowVisibility(boolean)">
<h3>setShowVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowVisibility</span><wbr/><span class="parameters">(boolean showVisibility)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowVisibility(boolean)">setShowVisibility</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowStereotype(boolean)">
<h3>setShowStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowStereotype</span><wbr/><span class="parameters">(boolean showStereotype)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowStereotype(boolean)">setShowStereotype</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowProperties(boolean)">
<h3>setShowProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowProperties</span><wbr/><span class="parameters">(boolean showProperties)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowProperties(boolean)">setShowProperties</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowTaggedValues(boolean)">
<h3>setShowTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowTaggedValues</span><wbr/><span class="parameters">(boolean showTaggedValues)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowTaggedValues(boolean)">setShowTaggedValues</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowConstraintName(boolean)">
<h3>setShowConstraintName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowConstraintName</span><wbr/><span class="parameters">(boolean showConstraintName)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowConstraintName(boolean)">setShowConstraintName</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowConstraintSpecification(boolean)">
<h3>setShowConstraintSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowConstraintSpecification</span><wbr/><span class="parameters">(boolean showConstraintSpecification)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowConstraintSpecification(boolean)">setShowConstraintSpecification</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowInheritedSign(boolean)">
<h3>setShowInheritedSign</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowInheritedSign</span><wbr/><span class="parameters">(boolean showInheritedSign)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowInheritedSign(boolean)">setShowInheritedSign</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowAdditionalSlotText(boolean)">
<h3>setShowAdditionalSlotText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowAdditionalSlotText</span><wbr/><span class="parameters">(boolean showAdditionalSlotText)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowAdditionalSlotText(boolean)">setShowAdditionalSlotText</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInvisibleFilter(java.util.function.Predicate)">
<h3>setInvisibleFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setInvisibleFilter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; invisibleFilter)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setInvisibleFilter(java.util.function.Predicate)">setInvisibleFilter</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowParameters(boolean)">
<h3>setShowParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowParameters</span><wbr/><span class="parameters">(boolean showParameters)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowFullType(boolean)">
<h3>setShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowFullType</span><wbr/><span class="parameters">(boolean showFullType)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowParameterDirectionKind(boolean)">
<h3>setShowParameterDirectionKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowParameterDirectionKind</span><wbr/><span class="parameters">(boolean showDirectionKind)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowOpaqueBehaviorBody(boolean)">
<h3>setShowOpaqueBehaviorBody</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BehaviorTextParams.html" title="class in com.nomagic.magicdraw.uml.text">BehaviorTextParams</a></span> <span class="element-name">setShowOpaqueBehaviorBody</span><wbr/><span class="parameters">(boolean showOpaqueBehaviorBody)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowFullType()">
<h3>isShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowFullType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowParameterDirectionKind()">
<h3>isShowParameterDirectionKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowParameterDirectionKind</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowParameters()">
<h3>isShowParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowParameters</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowOpaqueBehaviorBody()">
<h3>isShowOpaqueBehaviorBody</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowOpaqueBehaviorBody</span>()</div>
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
