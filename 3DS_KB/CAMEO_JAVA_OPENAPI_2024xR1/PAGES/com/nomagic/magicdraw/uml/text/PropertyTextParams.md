# JAVA OPENAPI: PropertyTextParams (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/text/PropertyTextParams.html
- source_path: `com/nomagic/magicdraw/uml/text/PropertyTextParams.html`
- source_sha256: `8acf6f5d601a3ff477e107bf7a1576e149137be7c52ee0c0e944ef44ad08f75b`
- captured_utc: `2026-07-14T16:52:16.070934+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.text](package-summary.html)

## Class PropertyTextParams

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.text.MemberTextParams](MemberTextParams.html)
com.nomagic.magicdraw.uml.text.PropertyTextParams

@OpenApiAllpublic classPropertyTextParams
extends [MemberTextParams](MemberTextParams.html)
Configuration for creating Property element text with [`ModelTextCreator`](ModelTextCreator.html).

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PropertyTextParams](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[isPureText](#isPureText())()`

`boolean`
`[isShowDerived](#isShowDerived())()`

`boolean`
`[isShowFullType](#isShowFullType())()`

`boolean`
`[isShowInitValue](#isShowInitValue())()`

`boolean`
`[isShowMultiplicity](#isShowMultiplicity())()`

`boolean`
`[isShowType](#isShowType())()`

`boolean`
`[isShowTypeNameIfEmptyName](#isShowTypeNameIfEmptyName())()`

`boolean`
`[isShowTypeTaggedValues](#isShowTypeTaggedValues())()`

`[PropertyTextParams](PropertyTextParams.html)`
`[setInvisibleFilter](#setInvisibleFilter(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> invisibleFilter)`
Set filter to accept elements represented in the text (like stereotypes, constraints, tagged values).
`[PropertyTextParams](PropertyTextParams.html)`
`[setPureText](#setPureText(boolean))(boolean pureText)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowAdditionalSlotText](#setShowAdditionalSlotText(boolean))(boolean showAdditionalSlotText)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowConstraintName](#setShowConstraintName(boolean))(boolean showConstraintName)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowConstraintSpecification](#setShowConstraintSpecification(boolean))(boolean showConstraintSpecification)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowDerived](#setShowDerived(boolean))(boolean showDerived)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowFullType](#setShowFullType(boolean))(boolean showFullType)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowInheritedSign](#setShowInheritedSign(boolean))(boolean showInheritedSign)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowInitValue](#setShowInitValue(boolean))(boolean showInitValue)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowMultiplicity](#setShowMultiplicity(boolean))(boolean showMultiplicity)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowName](#setShowName(boolean))(boolean showName)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowProperties](#setShowProperties(boolean))(boolean showProperties)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowStereotype](#setShowStereotype(boolean))(boolean showStereotype)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowTaggedValues](#setShowTaggedValues(boolean))(boolean showTaggedValues)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowType](#setShowType(boolean))(boolean showType)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowTypeNameIfNameEmpty](#setShowTypeNameIfNameEmpty(boolean))(boolean showTypeName)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowTypeTaggedValues](#setShowTypeTaggedValues(boolean))(boolean showTypeTaggedValues)`

`[PropertyTextParams](PropertyTextParams.html)`
`[setShowVisibility](#setShowVisibility(boolean))(boolean showVisibility)`
Methods inherited from class com.nomagic.magicdraw.uml.text.[MemberTextParams](MemberTextParams.html)
`[getInvisibleFilter](MemberTextParams.html#getInvisibleFilter()), [isShowAdditionalSlotText](MemberTextParams.html#isShowAdditionalSlotText()), [isShowConstraintName](MemberTextParams.html#isShowConstraintName()), [isShowConstraintSpecification](MemberTextParams.html#isShowConstraintSpecification()), [isShowInheritedSign](MemberTextParams.html#isShowInheritedSign()), [isShowName](MemberTextParams.html#isShowName()), [isShowProperties](MemberTextParams.html#isShowProperties()), [isShowStereotype](MemberTextParams.html#isShowStereotype()), [isShowTaggedValues](MemberTextParams.html#isShowTaggedValues()), [isShowVisibility](MemberTextParams.html#isShowVisibility())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PropertyTextParams
public PropertyTextParams()
 ============ METHOD DETAIL ========== 
Method Details
setShowName
public [PropertyTextParams](PropertyTextParams.html) setShowName(boolean showName)
Overrides:
`[setShowName](MemberTextParams.html#setShowName(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowVisibility
public [PropertyTextParams](PropertyTextParams.html) setShowVisibility(boolean showVisibility)
Overrides:
`[setShowVisibility](MemberTextParams.html#setShowVisibility(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowStereotype
public [PropertyTextParams](PropertyTextParams.html) setShowStereotype(boolean showStereotype)
Overrides:
`[setShowStereotype](MemberTextParams.html#setShowStereotype(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowProperties
public [PropertyTextParams](PropertyTextParams.html) setShowProperties(boolean showProperties)
Overrides:
`[setShowProperties](MemberTextParams.html#setShowProperties(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowTaggedValues
public [PropertyTextParams](PropertyTextParams.html) setShowTaggedValues(boolean showTaggedValues)
Overrides:
`[setShowTaggedValues](MemberTextParams.html#setShowTaggedValues(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowConstraintName
public [PropertyTextParams](PropertyTextParams.html) setShowConstraintName(boolean showConstraintName)
Overrides:
`[setShowConstraintName](MemberTextParams.html#setShowConstraintName(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowConstraintSpecification
public [PropertyTextParams](PropertyTextParams.html) setShowConstraintSpecification(boolean showConstraintSpecification)
Overrides:
`[setShowConstraintSpecification](MemberTextParams.html#setShowConstraintSpecification(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowInheritedSign
public [PropertyTextParams](PropertyTextParams.html) setShowInheritedSign(boolean showInheritedSign)
Overrides:
`[setShowInheritedSign](MemberTextParams.html#setShowInheritedSign(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setShowAdditionalSlotText
public [PropertyTextParams](PropertyTextParams.html) setShowAdditionalSlotText(boolean showAdditionalSlotText)
Overrides:
`[setShowAdditionalSlotText](MemberTextParams.html#setShowAdditionalSlotText(boolean))` in class `[MemberTextParams](MemberTextParams.html)`
setInvisibleFilter
public [PropertyTextParams](PropertyTextParams.html) setInvisibleFilter([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> invisibleFilter)
Set filter to accept elements represented in the text (like stereotypes, constraints, tagged values). By default all elements are accepted
Overrides:
`[setInvisibleFilter](MemberTextParams.html#setInvisibleFilter(java.util.function.Predicate))` in class `[MemberTextParams](MemberTextParams.html)`
Parameters:
`invisibleFilter` - filter
Returns:
filter for elements represented in the text
setPureText
public [PropertyTextParams](PropertyTextParams.html) setPureText(boolean pureText)
setShowType
public [PropertyTextParams](PropertyTextParams.html) setShowType(boolean showType)
setShowDerived
public [PropertyTextParams](PropertyTextParams.html) setShowDerived(boolean showDerived)
setShowFullType
public [PropertyTextParams](PropertyTextParams.html) setShowFullType(boolean showFullType)
setShowInitValue
public [PropertyTextParams](PropertyTextParams.html) setShowInitValue(boolean showInitValue)
setShowTypeTaggedValues
public [PropertyTextParams](PropertyTextParams.html) setShowTypeTaggedValues(boolean showTypeTaggedValues)
setShowMultiplicity
public [PropertyTextParams](PropertyTextParams.html) setShowMultiplicity(boolean showMultiplicity)
setShowTypeNameIfNameEmpty
public [PropertyTextParams](PropertyTextParams.html) setShowTypeNameIfNameEmpty(boolean showTypeName)
isShowType
public boolean isShowType()
isShowDerived
public boolean isShowDerived()
isShowFullType
public boolean isShowFullType()
isShowInitValue
public boolean isShowInitValue()
isShowMultiplicity
public boolean isShowMultiplicity()
isShowTypeNameIfEmptyName
public boolean isShowTypeNameIfEmptyName()
isShowTypeTaggedValues
public boolean isShowTypeTaggedValues()
isPureText
public boolean isPureText()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.text</a></div>
<h1 class="title" title="Class PropertyTextParams">Class PropertyTextParams</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">com.nomagic.magicdraw.uml.text.MemberTextParams</a>
<div class="inheritance">com.nomagic.magicdraw.uml.text.PropertyTextParams</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PropertyTextParams</span>
<span class="extends-implements">extends <a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></span></div>
<div class="block">Configuration for creating Property element text with <a href="ModelTextCreator.html" title="class in com.nomagic.magicdraw.uml.text"><code>ModelTextCreator</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PropertyTextParams</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPureText()">isPureText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowDerived()">isShowDerived</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowFullType()">isShowFullType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowInitValue()">isShowInitValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowMultiplicity()">isShowMultiplicity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowType()">isShowType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowTypeNameIfEmptyName()">isShowTypeNameIfEmptyName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowTypeTaggedValues()">isShowTypeTaggedValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInvisibleFilter(java.util.function.Predicate)">setInvisibleFilter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; invisibleFilter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set filter to accept elements represented in the text (like stereotypes, constraints, tagged values).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPureText(boolean)">setPureText</a><wbr/>(boolean pureText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowAdditionalSlotText(boolean)">setShowAdditionalSlotText</a><wbr/>(boolean showAdditionalSlotText)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowConstraintName(boolean)">setShowConstraintName</a><wbr/>(boolean showConstraintName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowConstraintSpecification(boolean)">setShowConstraintSpecification</a><wbr/>(boolean showConstraintSpecification)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowDerived(boolean)">setShowDerived</a><wbr/>(boolean showDerived)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowFullType(boolean)">setShowFullType</a><wbr/>(boolean showFullType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowInheritedSign(boolean)">setShowInheritedSign</a><wbr/>(boolean showInheritedSign)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowInitValue(boolean)">setShowInitValue</a><wbr/>(boolean showInitValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowMultiplicity(boolean)">setShowMultiplicity</a><wbr/>(boolean showMultiplicity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowName(boolean)">setShowName</a><wbr/>(boolean showName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowProperties(boolean)">setShowProperties</a><wbr/>(boolean showProperties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowStereotype(boolean)">setShowStereotype</a><wbr/>(boolean showStereotype)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowTaggedValues(boolean)">setShowTaggedValues</a><wbr/>(boolean showTaggedValues)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowType(boolean)">setShowType</a><wbr/>(boolean showType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowTypeNameIfNameEmpty(boolean)">setShowTypeNameIfNameEmpty</a><wbr/>(boolean showTypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowTypeTaggedValues(boolean)">setShowTypeTaggedValues</a><wbr/>(boolean showTypeTaggedValues)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></code></div>
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
<h3>PropertyTextParams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PropertyTextParams</span>()</div>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowName</span><wbr/><span class="parameters">(boolean showName)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowName(boolean)">setShowName</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowVisibility(boolean)">
<h3>setShowVisibility</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowVisibility</span><wbr/><span class="parameters">(boolean showVisibility)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowVisibility(boolean)">setShowVisibility</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowStereotype(boolean)">
<h3>setShowStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowStereotype</span><wbr/><span class="parameters">(boolean showStereotype)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowStereotype(boolean)">setShowStereotype</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowProperties(boolean)">
<h3>setShowProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowProperties</span><wbr/><span class="parameters">(boolean showProperties)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowProperties(boolean)">setShowProperties</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowTaggedValues(boolean)">
<h3>setShowTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowTaggedValues</span><wbr/><span class="parameters">(boolean showTaggedValues)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowTaggedValues(boolean)">setShowTaggedValues</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowConstraintName(boolean)">
<h3>setShowConstraintName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowConstraintName</span><wbr/><span class="parameters">(boolean showConstraintName)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowConstraintName(boolean)">setShowConstraintName</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowConstraintSpecification(boolean)">
<h3>setShowConstraintSpecification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowConstraintSpecification</span><wbr/><span class="parameters">(boolean showConstraintSpecification)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowConstraintSpecification(boolean)">setShowConstraintSpecification</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowInheritedSign(boolean)">
<h3>setShowInheritedSign</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowInheritedSign</span><wbr/><span class="parameters">(boolean showInheritedSign)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowInheritedSign(boolean)">setShowInheritedSign</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowAdditionalSlotText(boolean)">
<h3>setShowAdditionalSlotText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowAdditionalSlotText</span><wbr/><span class="parameters">(boolean showAdditionalSlotText)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setShowAdditionalSlotText(boolean)">setShowAdditionalSlotText</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInvisibleFilter(java.util.function.Predicate)">
<h3>setInvisibleFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setInvisibleFilter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; invisibleFilter)</span></div>
<div class="block">Set filter to accept elements represented in the text (like stereotypes, constraints, tagged values). By default all elements are accepted</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="MemberTextParams.html#setInvisibleFilter(java.util.function.Predicate)">setInvisibleFilter</a></code> in class <code><a href="MemberTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MemberTextParams</a></code></dd>
<dt>Parameters:</dt>
<dd><code>invisibleFilter</code> - filter</dd>
<dt>Returns:</dt>
<dd>filter for elements represented in the text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPureText(boolean)">
<h3>setPureText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setPureText</span><wbr/><span class="parameters">(boolean pureText)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowType(boolean)">
<h3>setShowType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowType</span><wbr/><span class="parameters">(boolean showType)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowDerived(boolean)">
<h3>setShowDerived</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowDerived</span><wbr/><span class="parameters">(boolean showDerived)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowFullType(boolean)">
<h3>setShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowFullType</span><wbr/><span class="parameters">(boolean showFullType)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowInitValue(boolean)">
<h3>setShowInitValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowInitValue</span><wbr/><span class="parameters">(boolean showInitValue)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowTypeTaggedValues(boolean)">
<h3>setShowTypeTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowTypeTaggedValues</span><wbr/><span class="parameters">(boolean showTypeTaggedValues)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowMultiplicity(boolean)">
<h3>setShowMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowMultiplicity</span><wbr/><span class="parameters">(boolean showMultiplicity)</span></div>
</section>
</li>
<li>
<section class="detail" id="setShowTypeNameIfNameEmpty(boolean)">
<h3>setShowTypeNameIfNameEmpty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PropertyTextParams.html" title="class in com.nomagic.magicdraw.uml.text">PropertyTextParams</a></span> <span class="element-name">setShowTypeNameIfNameEmpty</span><wbr/><span class="parameters">(boolean showTypeName)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowType()">
<h3>isShowType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowDerived()">
<h3>isShowDerived</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowDerived</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowFullType()">
<h3>isShowFullType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowFullType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowInitValue()">
<h3>isShowInitValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowInitValue</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowMultiplicity()">
<h3>isShowMultiplicity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowMultiplicity</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowTypeNameIfEmptyName()">
<h3>isShowTypeNameIfEmptyName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowTypeNameIfEmptyName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isShowTypeTaggedValues()">
<h3>isShowTypeTaggedValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowTypeTaggedValues</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isPureText()">
<h3>isPureText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPureText</span>()</div>
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
