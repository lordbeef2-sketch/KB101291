# JAVA OPENAPI: QueryAttribute (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/query/QueryAttribute.html
- source_path: `com/nomagic/reportwizard/tools/query/QueryAttribute.html`
- source_sha256: `d2a745996864b736f2ab09d37a3515d342df0e980b0c7e50faa67c5f7801fe80`
- captured_utc: `2026-07-14T16:58:40.661319+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.query](package-summary.html)

## Class QueryAttribute

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.reportwizard.tools.query.QueryAttribute

@OpenApiAllpublic classQueryAttribute
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Class for handler attribute condition of query element.

Since:
Jan 29, 2013

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[TYPE_MATCHING_ANY](#TYPE_MATCHING_ANY)`
[attr*=value] 

 Matching an element with the attr attribute whose value contains at least one instance of the substring val.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_MATCHING_ANY_PATTERN](#TYPE_MATCHING_ANY_PATTERN)`
Regular expression pattern for any.
`static final int`
`[TYPE_MATCHING_ENDWITH](#TYPE_MATCHING_ENDWITH)`
[attr$=value] 

 Matching an element with the attr attribute whose value ends with the suffix val.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_MATCHING_ENDWITH_PATTERN](#TYPE_MATCHING_ENDWITH_PATTERN)`
Regular expression pattern for endswith.
`static final int`
`[TYPE_MATCHING_MATCHALL](#TYPE_MATCHING_MATCHALL)`
[attr=value] 

 Matching an element with the attr attribute whose value exactly value.
`static final int`
`[TYPE_MATCHING_STARTWITH](#TYPE_MATCHING_STARTWITH)`
[attr^=value] 

 Matching an element with the attr attribute whose value begins with the prefix val.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TYPE_MATCHING_STARTWITH_PATTERN](#TYPE_MATCHING_STARTWITH_PATTERN)`
Regular expression pattern for startswith.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[QueryAttribute](#%3Cinit%3E())()`
Constructor.
`[QueryAttribute](#%3Cinit%3E(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int type)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Get an attribute name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRegx](#getRegx())()`
Get a regular expression for attribute matching.
`int`
`[getType](#getType())()`
Get an attribute matching type.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getTypeCharacer](#getTypeCharacer())()`
Get matching type character.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getValue](#getValue())()`
Get an attribute value.
`boolean`
`[matchAttribute](#matchAttribute(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) elementValue)`
Return true if specific value match with regular expression.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Set an attribute name.
`void`
`[setRegx](#setRegx(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) regx)`
Set a regular expression for attribute matching.
`void`
`[setType](#setType(int))(int type)`
Set an attribute matching type.
`void`
`[setValue](#setValue(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Set an attribute value.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TYPE_MATCHING_MATCHALL
public static final int TYPE_MATCHING_MATCHALL
[attr=value] 

 Matching an element with the attr attribute whose value exactly value.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_MATCHALL)
TYPE_MATCHING_STARTWITH
public static final int TYPE_MATCHING_STARTWITH
[attr^=value] 

 Matching an element with the attr attribute whose value begins with the prefix val.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_STARTWITH)
TYPE_MATCHING_STARTWITH_PATTERN
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_MATCHING_STARTWITH_PATTERN
Regular expression pattern for startswith.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_STARTWITH_PATTERN)
TYPE_MATCHING_ENDWITH
public static final int TYPE_MATCHING_ENDWITH
[attr$=value] 

 Matching an element with the attr attribute whose value ends with the suffix val.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_ENDWITH)
TYPE_MATCHING_ENDWITH_PATTERN
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_MATCHING_ENDWITH_PATTERN
Regular expression pattern for endswith.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_ENDWITH_PATTERN)
TYPE_MATCHING_ANY
public static final int TYPE_MATCHING_ANY
[attr*=value] 

 Matching an element with the attr attribute whose value contains at least one instance of the substring val.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_ANY)
TYPE_MATCHING_ANY_PATTERN
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TYPE_MATCHING_ANY_PATTERN
Regular expression pattern for any.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_ANY_PATTERN)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
QueryAttribute
public QueryAttribute()
Constructor.
QueryAttribute
public QueryAttribute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value,
 int type)
Constructor.
Parameters:
`name` - attribute name
`value` - attribute value
`type` - attribute matching type
 ============ METHOD DETAIL ========== 
Method Details
getName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Get an attribute name.
Returns:
an attribute name
setName
public void setName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Set an attribute name.
Parameters:
`name` - an attribute name
getValue
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getValue()
Get an attribute value.
Returns:
an attribute value
setValue
public void setValue([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Set an attribute value.
Parameters:
`value` - an attribute value
getRegx
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRegx()
Get a regular expression for attribute matching.
Returns:
a regular expression
setRegx
public void setRegx([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) regx)
Set a regular expression for attribute matching.
Parameters:
`regx` - a regular expression
getType
public int getType()
Get an attribute matching type.
Returns:
an attribute matching type
setType
public void setType(int type)
Set an attribute matching type.
Parameters:
`type` - an attribute matching type
getTypeCharacer
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getTypeCharacer()
Get matching type character.
Returns:
matching type character
matchAttribute
public boolean matchAttribute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) elementValue)
Return true if specific value match with regular expression.
Parameters:
`elementValue` - a specific value / MagicDraw element value
Returns:
true or false.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.query</a></div>
<h1 class="title" title="Class QueryAttribute">Class QueryAttribute</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.reportwizard.tools.query.QueryAttribute</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">QueryAttribute</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class for handler attribute condition of query element.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 29, 2013</dd>
</dl>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TYPE_MATCHING_ANY">TYPE_MATCHING_ANY</a></code></div>
<div class="col-last even-row-color">
<div class="block">[attr*=value]<br/>
 Matching an element with the attr attribute whose value contains at least one instance of the substring val.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TYPE_MATCHING_ANY_PATTERN">TYPE_MATCHING_ANY_PATTERN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Regular expression pattern for any.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TYPE_MATCHING_ENDWITH">TYPE_MATCHING_ENDWITH</a></code></div>
<div class="col-last even-row-color">
<div class="block">[attr$=value]<br/>
 Matching an element with the attr attribute whose value ends with the suffix val.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TYPE_MATCHING_ENDWITH_PATTERN">TYPE_MATCHING_ENDWITH_PATTERN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Regular expression pattern for endswith.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TYPE_MATCHING_MATCHALL">TYPE_MATCHING_MATCHALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">[attr=value]<br/>
 Matching an element with the attr attribute whose value exactly value.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TYPE_MATCHING_STARTWITH">TYPE_MATCHING_STARTWITH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">[attr^=value]<br/>
 Matching an element with the attr attribute whose value begins with the prefix val.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TYPE_MATCHING_STARTWITH_PATTERN">TYPE_MATCHING_STARTWITH_PATTERN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Regular expression pattern for startswith.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">QueryAttribute</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int)">QueryAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int type)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get an attribute name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRegx()">getRegx</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get a regular expression for attribute matching.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get an attribute matching type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeCharacer()">getTypeCharacer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get matching type character.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get an attribute value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#matchAttribute(java.lang.String)">matchAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return true if specific value match with regular expression.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an attribute name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRegx(java.lang.String)">setRegx</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> regx)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a regular expression for attribute matching.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setType(int)">setType</a><wbr/>(int type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an attribute matching type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(java.lang.String)">setValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an attribute value.</div>
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
<section class="detail" id="TYPE_MATCHING_MATCHALL">
<h3>TYPE_MATCHING_MATCHALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TYPE_MATCHING_MATCHALL</span></div>
<div class="block">[attr=value]<br/>
 Matching an element with the attr attribute whose value exactly value.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_MATCHALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_MATCHING_STARTWITH">
<h3>TYPE_MATCHING_STARTWITH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TYPE_MATCHING_STARTWITH</span></div>
<div class="block">[attr^=value]<br/>
 Matching an element with the attr attribute whose value begins with the prefix val.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_STARTWITH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_MATCHING_STARTWITH_PATTERN">
<h3>TYPE_MATCHING_STARTWITH_PATTERN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_MATCHING_STARTWITH_PATTERN</span></div>
<div class="block">Regular expression pattern for startswith.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_STARTWITH_PATTERN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_MATCHING_ENDWITH">
<h3>TYPE_MATCHING_ENDWITH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TYPE_MATCHING_ENDWITH</span></div>
<div class="block">[attr$=value]<br/>
 Matching an element with the attr attribute whose value ends with the suffix val.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_ENDWITH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_MATCHING_ENDWITH_PATTERN">
<h3>TYPE_MATCHING_ENDWITH_PATTERN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_MATCHING_ENDWITH_PATTERN</span></div>
<div class="block">Regular expression pattern for endswith.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_ENDWITH_PATTERN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_MATCHING_ANY">
<h3>TYPE_MATCHING_ANY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TYPE_MATCHING_ANY</span></div>
<div class="block">[attr*=value]<br/>
 Matching an element with the attr attribute whose value contains at least one instance of the substring val.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_ANY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_MATCHING_ANY_PATTERN">
<h3>TYPE_MATCHING_ANY_PATTERN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_MATCHING_ANY_PATTERN</span></div>
<div class="block">Regular expression pattern for any.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.query.QueryAttribute.TYPE_MATCHING_ANY_PATTERN">Constant Field Values</a></li>
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
<h3>QueryAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">QueryAttribute</span>()</div>
<div class="block">Constructor.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int)">
<h3>QueryAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">QueryAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value,
 int type)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - attribute name</dd>
<dd><code>value</code> - attribute value</dd>
<dd><code>type</code> - attribute matching type</dd>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Get an attribute name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an attribute name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Set an attribute name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - an attribute name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValue</span>()</div>
<div class="block">Get an attribute value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an attribute value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(java.lang.String)">
<h3>setValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Set an attribute value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - an attribute value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRegx()">
<h3>getRegx</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRegx</span>()</div>
<div class="block">Get a regular expression for attribute matching.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a regular expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRegx(java.lang.String)">
<h3>setRegx</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRegx</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> regx)</span></div>
<div class="block">Set a regular expression for attribute matching.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>regx</code> - a regular expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getType</span>()</div>
<div class="block">Get an attribute matching type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an attribute matching type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(int)">
<h3>setType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(int type)</span></div>
<div class="block">Set an attribute matching type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - an attribute matching type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeCharacer()">
<h3>getTypeCharacer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTypeCharacer</span>()</div>
<div class="block">Get matching type character.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>matching type character</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="matchAttribute(java.lang.String)">
<h3>matchAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">matchAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementValue)</span></div>
<div class="block">Return true if specific value match with regular expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementValue</code> - a specific value / MagicDraw element value</dd>
<dt>Returns:</dt>
<dd>true or false.</dd>
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
