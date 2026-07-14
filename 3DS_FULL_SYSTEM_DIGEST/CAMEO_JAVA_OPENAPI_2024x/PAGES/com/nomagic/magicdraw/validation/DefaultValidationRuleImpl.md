# JAVA OPENAPI: DefaultValidationRuleImpl (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/validation/DefaultValidationRuleImpl.html
- source_path: `com/nomagic/magicdraw/validation/DefaultValidationRuleImpl.html`
- source_sha256: `febb29dcde5c53b15c3e4fa01952a04ba46daef89bfe5e2ced31d7166c64e966`
- captured_utc: `2026-07-14T16:52:27.202082+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Class DefaultValidationRuleImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.validation.DefaultValidationRuleImpl

All Implemented Interfaces:
`[ElementValidationRuleImpl](ElementValidationRuleImpl.html)`, `[SmartListenerConfigProvider](../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html)`

@OpenApiAllpublic classDefaultValidationRuleImpl
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ElementValidationRuleImpl](ElementValidationRuleImpl.html), [SmartListenerConfigProvider](../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html)

The class implements validating of a model elements by using OCL or binary implementation.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DefaultValidationRuleImpl](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [Annotation](../annotation/Annotation.html)`
`[createAnnotation](#createAnnotation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Default implementation creates an annotation without actions.
`void`
`[dispose](#dispose())()`
Cleans up used resources of the object.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getInvalidElements](#getInvalidElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection))([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Returns invalid elements from the specified collection of elements.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)>>`
`[getListenerConfigurations](#getListenerConfigurations())()`
Returns configurations for the rule's expression.
`void`
`[init](#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)`
Initializes the instance from specified parameters.
`protected void`
`[initializeSingleRun](#initializeSingleRun())()`
Single run specific rule data can be initialized here.
`final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)>`
`[run](#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection))([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Performs validation on the specified model elements by using specified constraint.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.validation.[ElementValidationRuleImpl](ElementValidationRuleImpl.html)
`[postRun](ElementValidationRuleImpl.html#postRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)), [preRun](ElementValidationRuleImpl.html#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)), [preRun](ElementValidationRuleImpl.html#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DefaultValidationRuleImpl
public DefaultValidationRuleImpl()
 ============ METHOD DETAIL ========== 
Method Details
init
public void init([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Initializes the instance from specified parameters.
Specified by:
`[init](ElementValidationRuleImpl.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint))` in interface `[ElementValidationRuleImpl](ElementValidationRuleImpl.html)`
Parameters:
`project` - project on which model elements the validation rule applies.
`constraint` - a constraint object.
getListenerConfigurations
@CheckForNullpublic [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>,[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html)>> getListenerConfigurations()
Returns configurations for the rule's expression.
 When it returns null - the validation rule is interested in all model element changes.
Specified by:
`[getListenerConfigurations](../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html#getListenerConfigurations())` in interface `[SmartListenerConfigProvider](../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html)`
Returns:
map of listener configurations by element class type
run
@CheckForNullpublic final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Annotation](../annotation/Annotation.html)> run([Project](../core/Project.html) project,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Performs validation on the specified model elements by using specified constraint.
Specified by:
`[run](ElementValidationRuleImpl.html#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection))` in interface `[ElementValidationRuleImpl](ElementValidationRuleImpl.html)`
Parameters:
`project` - a project of the constraint.
`constraint` - constraint that should be used to validate model elements.
`elements` - a collection of model elements that needs to be validated.
Returns:
collection of `Annotation` objects that describes violations of the rule.
initializeSingleRun
protected void initializeSingleRun()
Single run specific rule data can be initialized here.
createAnnotation
protected [Annotation](../annotation/Annotation.html) createAnnotation([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint)
Default implementation creates an annotation without actions. Derived classes can override the
 method and return an `Annotation` object with actions.
Parameters:
`element` - a model element for which `Annotation` object should be created.
`constraint` - the constraint that is violated.
Returns:
`Annotation` object.
getInvalidElements
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getInvalidElements([Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html) constraint,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Returns invalid elements from the specified collection of elements.
Parameters:
`constraint` - constraint that specifies validation rules.
`elements` - a collection of elements that need to be validated.
Returns:
a collection of invalid elements.
dispose
public void dispose()
Cleans up used resources of the object.
Specified by:
`[dispose](ElementValidationRuleImpl.html#dispose())` in interface `[ElementValidationRuleImpl](ElementValidationRuleImpl.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Class DefaultValidationRuleImpl">Class DefaultValidationRuleImpl</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.validation.DefaultValidationRuleImpl</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ElementValidationRuleImpl.html" title="interface in com.nomagic.magicdraw.validation">ElementValidationRuleImpl</a></code>, <code><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfigProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DefaultValidationRuleImpl</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ElementValidationRuleImpl.html" title="interface in com.nomagic.magicdraw.validation">ElementValidationRuleImpl</a>, <a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfigProvider</a></span></div>
<div class="block">The class implements validating of a model elements by using OCL or binary implementation.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DefaultValidationRuleImpl</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAnnotation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">createAnnotation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Default implementation creates an annotation without actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Cleans up used resources of the object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInvalidElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">getInvalidElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns invalid elements from the specified collection of elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getListenerConfigurations()">getListenerConfigurations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns configurations for the rule's expression.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initializes the instance from specified parameters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initializeSingleRun()">initializeSingleRun</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Single run specific rule data can be initialized here.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">run</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs validation on the specified model elements by using specified constraint.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.validation.ElementValidationRuleImpl">Methods inherited from interface com.nomagic.magicdraw.validation.<a href="ElementValidationRuleImpl.html" title="interface in com.nomagic.magicdraw.validation">ElementValidationRuleImpl</a></h3>
<code><a href="ElementValidationRuleImpl.html#postRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">postRun</a>, <a href="ElementValidationRuleImpl.html#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">preRun</a>, <a href="ElementValidationRuleImpl.html#preRun(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">preRun</a></code></div>
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
<h3>DefaultValidationRuleImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DefaultValidationRuleImpl</span>()</div>
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
<section class="detail" id="init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">Initializes the instance from specified parameters.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ElementValidationRuleImpl.html#init(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">init</a></code> in interface <code><a href="ElementValidationRuleImpl.html" title="interface in com.nomagic.magicdraw.validation">ElementValidationRuleImpl</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project on which model elements the validation rule applies.</dd>
<dd><code>constraint</code> - a constraint object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getListenerConfigurations()">
<h3>getListenerConfigurations</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;&gt;</span> <span class="element-name">getListenerConfigurations</span>()</div>
<div class="block">Returns configurations for the rule's expression.
 When it returns null - the validation rule is interested in all model element changes.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html#getListenerConfigurations()">getListenerConfigurations</a></code> in interface <code><a href="../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfigProvider</a></code></dd>
<dt>Returns:</dt>
<dd>map of listener configurations by element class type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">
<h3>run</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">run</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Performs validation on the specified model elements by using specified constraint.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ElementValidationRuleImpl.html#run(com.nomagic.magicdraw.core.Project,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">run</a></code> in interface <code><a href="ElementValidationRuleImpl.html" title="interface in com.nomagic.magicdraw.validation">ElementValidationRuleImpl</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - a project of the constraint.</dd>
<dd><code>constraint</code> - constraint that should be used to validate model elements.</dd>
<dd><code>elements</code> - a collection of model elements that needs to be validated.</dd>
<dt>Returns:</dt>
<dd>collection of <code>Annotation</code> objects that describes violations of the rule.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="initializeSingleRun()">
<h3>initializeSingleRun</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">initializeSingleRun</span>()</div>
<div class="block">Single run specific rule data can be initialized here.</div>
</section>
</li>
<li>
<section class="detail" id="createAnnotation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint)">
<h3>createAnnotation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../annotation/Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a></span> <span class="element-name">createAnnotation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint)</span></div>
<div class="block">Default implementation creates an annotation without actions. Derived classes can override the
 method and return an <code>Annotation</code> object with actions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - a model element for which <code>Annotation</code> object should be created.</dd>
<dd><code>constraint</code> - the constraint that is violated.</dd>
<dt>Returns:</dt>
<dd><code>Annotation</code> object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInvalidElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Constraint,java.util.Collection)">
<h3>getInvalidElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getInvalidElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a> constraint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Returns invalid elements from the specified collection of elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - constraint that specifies validation rules.</dd>
<dd><code>elements</code> - a collection of elements that need to be validated.</dd>
<dt>Returns:</dt>
<dd>a collection of invalid elements.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Cleans up used resources of the object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ElementValidationRuleImpl.html#dispose()">dispose</a></code> in interface <code><a href="ElementValidationRuleImpl.html" title="interface in com.nomagic.magicdraw.validation">ElementValidationRuleImpl</a></code></dd>
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
