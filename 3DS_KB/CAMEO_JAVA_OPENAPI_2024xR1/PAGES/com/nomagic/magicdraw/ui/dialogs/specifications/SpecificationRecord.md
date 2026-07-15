# JAVA OPENAPI: SpecificationRecord (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/dialogs/specifications/SpecificationRecord.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/specifications/SpecificationRecord.html`
- source_sha256: `7bfa43460d627df451fbc00a57b7ae33282a2102d52d9e82fbc5519c8ce1222c`
- captured_utc: `2026-07-14T16:52:03.151766+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.specifications](package-summary.html)

## Class SpecificationRecord

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationSelection
com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord

@OpenApiAllpublic classSpecificationRecord
extends com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationSelection

This class defines a reference to some page inside an Element specification window.
 **To reference "Attributes" or "Tagged Values" panels inside specification dialog use such constructors**
`new SpecificationRecord(element, new String[]{element.getID(), IConfigurableNode.ATTRIBUTES})
 new SpecificationRecord(element, new String[]{element.getID(), IConfigurableNode.TAGS})`

See Also:
[`IConfigurableNode`](tree/node/IConfigurableNode.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[element](#element)`
Fields inherited from class com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationSelection
`path, property`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SpecificationRecord](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] path)`
Constructs a reference to a specification dialog page
`[SpecificationRecord](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D,java.lang.String))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] path,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property)`
Constructs a reference to a specification dialog page
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
element
public [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SpecificationRecord
public SpecificationRecord([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] path)
Constructs a reference to a specification dialog page
 `new SpecificationRecord(element, new String[]{element.getID(), IConfigurableNode.ATTRIBUTES})
 new SpecificationRecord(element, new String[]{element.getID(), IConfigurableNode.TAGS})`
Parameters:
`element` - element
`path` - inner node path (null means root node)
SpecificationRecord
public SpecificationRecord([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] path,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property)
Constructs a reference to a specification dialog page
 `new SpecificationRecord(element, null, PropertyNames.OWNER)`
Parameters:
`element` - element
`path` - inner node path (null means root node)
`property` - id of property to select and activate inside a property pane referenced by path
See Also:
[`PropertyNames`](../../../../uml2/impl/PropertyNames.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.specifications</a></div>
<h1 class="title" title="Class SpecificationRecord">Class SpecificationRecord</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationSelection
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SpecificationRecord</span>
<span class="extends-implements">extends com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationSelection</span></div>
<div class="block">This class defines a reference to some page inside an Element specification window.
 <p>
<b>To reference "Attributes" or "Tagged Values" panels inside specification dialog use such constructors</b>
<p>
<pre> <code>
  new SpecificationRecord(element, new String[]{element.getID(), IConfigurableNode.ATTRIBUTES})
  new SpecificationRecord(element, new String[]{element.getID(), IConfigurableNode.TAGS})
 </code></pre>
</p>
</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="tree/node/IConfigurableNode.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node"><code>IConfigurableNode</code></a></li>
</ul>
</dd>
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
<div class="col-first even-row-color"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#element">element</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationSelection">Fields inherited from class com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationSelection</h3>
<code>path, property</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D)">SpecificationRecord</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] path)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a reference to a specification dialog page</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String%5B%5D,java.lang.String)">SpecificationRecord</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a reference to a specification dialog page</div>
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
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="element">
<h3>element</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">element</span></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String[])">
<h3>SpecificationRecord</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SpecificationRecord</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] path)</span></div>
<div class="block">Constructs a reference to a specification dialog page
 <p>
<pre> <code>
  new SpecificationRecord(element, new String[]{element.getID(), IConfigurableNode.ATTRIBUTES})
  new SpecificationRecord(element, new String[]{element.getID(), IConfigurableNode.TAGS})
 </code></pre>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>path</code> - inner node path (null means root node)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String[],java.lang.String)">
<h3>SpecificationRecord</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SpecificationRecord</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] path,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property)</span></div>
<div class="block">Constructs a reference to a specification dialog page
 <p>
<pre> <code>
  new SpecificationRecord(element, null, PropertyNames.OWNER)
 </code></pre>
</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>path</code> - inner node path (null means root node)</dd>
<dd><code>property</code> - id of property to select and activate inside a property pane referenced by path</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../uml2/impl/PropertyNames.html" title="class in com.nomagic.uml2.impl"><code>PropertyNames</code></a></li>
</ul>
</dd>
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
