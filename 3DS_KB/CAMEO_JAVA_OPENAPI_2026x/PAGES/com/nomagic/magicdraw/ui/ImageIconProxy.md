# JAVA OPENAPI: ImageIconProxy (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/ImageIconProxy.html
- source_path: `com/nomagic/magicdraw/ui/ImageIconProxy.html`
- source_sha256: `73f5a5928cde9b9a2ebe54037415a0a323a98d6fd215ee9bedc24dd319788e94`
- captured_utc: `2026-07-14T16:58:23.920135+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class ImageIconProxy

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
com.nomagic.magicdraw.ui.ImageIconProxy

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Accessible](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/accessibility/Accessible.html)`, `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`

@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public classImageIconProxy
extends [ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)

Deprecated.
use [`IconsFactory`](../icons/IconsFactory.html)

This class is used only for reloading icons after image path is changed.

See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.magicdraw.ui.ImageIconProxy)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#component), [tracker](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#tracker)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ImageIconProxy](#%3Cinit%3E(com.nomagic.magicdraw.ui.IconControlerInterface))([IconControlerInterface](IconControlerInterface.html) iconControler)`
Deprecated.
The proxy constructor with given controller
`[ImageIconProxy](#%3Cinit%3E(java.lang.Class,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Deprecated.
Constructs a new ImageIcon instance.
`[ImageIconProxy](#%3Cinit%3E(java.lang.Class,java.lang.String,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pathToIcons)`
Deprecated.
Constructs a new ImageIcon instance.
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[getAccessibleContext](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getAccessibleContext()), [getDescription](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getDescription()), [getImageLoadStatus](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageLoadStatus()), [getImageObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageObserver()), [loadImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#loadImage(java.awt.Image)), [setDescription](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setDescription(java.lang.String)), [setImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImage(java.awt.Image)), [setImageObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ImageIconProxy
@OpenApipublic ImageIconProxy([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Deprecated.
Constructs a new ImageIcon instance.
Parameters:
`clazz` - the class to identify resources.
`name` - the name of the icon in the map.
ImageIconProxy
@OpenApipublic ImageIconProxy([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pathToIcons)
Deprecated.
Constructs a new ImageIcon instance. For icons directory uses given path
Parameters:
`clazz` - the class to indentify resources.
`name` - the name of the icon in the map.
`pathToIcons` - path to icons directory, this directory must contain subdirs icons32 and icons24. Can be empty string
 In this case it means same dir as clazz.
ImageIconProxy
@OpenApipublic ImageIconProxy([IconControlerInterface](IconControlerInterface.html) iconControler)
Deprecated.
The proxy constructor with given controller
Parameters:
`iconControler` -

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class ImageIconProxy">Class ImageIconProxy</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">javax.swing.ImageIcon</a>
<div class="inheritance">com.nomagic.magicdraw.ui.ImageIconProxy</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/accessibility/Accessible.html" title="class or interface in javax.accessibility">Accessible</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ImageIconProxy</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="../icons/IconsFactory.html" title="class in com.nomagic.magicdraw.icons"><code>IconsFactory</code></a></div>
</div>
<div class="block">This class is used only for reloading icons after image path is changed.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../serialized-form.html#com.nomagic.magicdraw.ui.ImageIconProxy">Serialized Form</a></li>
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
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.ImageIcon">Fields inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#component" title="class or interface in javax.swing">component</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#tracker" title="class or interface in javax.swing">tracker</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.ui.IconControlerInterface)">ImageIconProxy</a><wbr/>(<a href="IconControlerInterface.html" title="interface in com.nomagic.magicdraw.ui">IconControlerInterface</a> iconControler)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">The proxy constructor with given controller</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,java.lang.String)">ImageIconProxy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a new ImageIcon instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,java.lang.String,java.lang.String)">ImageIconProxy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathToIcons)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a new ImageIcon instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.ImageIcon">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getAccessibleContext()" title="class or interface in javax.swing">getAccessibleContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getDescription()" title="class or interface in javax.swing">getDescription</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageLoadStatus()" title="class or interface in javax.swing">getImageLoadStatus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageObserver()" title="class or interface in javax.swing">getImageObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#loadImage(java.awt.Image)" title="class or interface in javax.swing">loadImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setDescription(java.lang.String)" title="class or interface in javax.swing">setDescription</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImage(java.awt.Image)" title="class or interface in javax.swing">setImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver)" title="class or interface in javax.swing">setImageObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#toString()" title="class or interface in javax.swing">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Class,java.lang.String)">
<h3>ImageIconProxy</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">ImageIconProxy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a new ImageIcon instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - the class to identify resources.</dd>
<dd><code>name</code> - the name of the icon in the map.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class,java.lang.String,java.lang.String)">
<h3>ImageIconProxy</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">ImageIconProxy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathToIcons)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a new ImageIcon instance. For icons directory uses given path</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - the class to indentify resources.</dd>
<dd><code>name</code> - the name of the icon in the map.</dd>
<dd><code>pathToIcons</code> - path to icons directory, this directory must contain subdirs icons32 and icons24. Can be empty string
 In this case it means same dir as clazz.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.ui.IconControlerInterface)">
<h3>ImageIconProxy</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">ImageIconProxy</span><wbr/><span class="parameters">(<a href="IconControlerInterface.html" title="interface in com.nomagic.magicdraw.ui">IconControlerInterface</a> iconControler)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">The proxy constructor with given controller</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>iconControler</code> - </dd>
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
