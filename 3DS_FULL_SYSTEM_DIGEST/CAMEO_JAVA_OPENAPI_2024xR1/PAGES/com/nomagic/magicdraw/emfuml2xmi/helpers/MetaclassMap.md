# JAVA OPENAPI: MetaclassMap (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/emfuml2xmi/helpers/MetaclassMap.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/helpers/MetaclassMap.html`
- source_sha256: `d5e51dd79752f5e4735825e8eaf086597629cfb1650d9f38ff90eb7014e1ee5e`
- captured_utc: `2026-07-14T16:51:19.085175+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.helpers](package-summary.html)

## Interface MetaclassMap

All Superinterfaces:
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`

All Known Implementing Classes:
`[Emf2MofUml2MetaclassMap](../v3/imp0rt/convert/Emf2MofUml2MetaclassMap.html)`, `com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.Emf2MofUml2MetaclassMapImpl`, `[Mof2EmfUml2MetaclassMap](../v3/export/convert/Mof2EmfUml2MetaclassMap.html)`, `com.nomagic.magicdraw.emfuml2xmi.export.convert.Mof2EmfUml2MetaclassMapImpl`

@OpenApipublic interfaceMetaclassMapextends [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>

MagicDraw UML2 model metaclass --> Eclipse (EMF) UML2 model metaclass

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mdUml2Metaclass)`
Returns corresponding Eclipse UML2 model metaclass.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[put](#put(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mdClassName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) eClassName)`
Maps MagicDraw UML2 model metaclass to Eclipse UML2 model metaclass.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[remove](#remove(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mdClassName)`
Removes mapping between MagicDraw UML2 model metaclass and Eclipse UML2 model metaclass.
Methods inherited from interface java.util.[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)
`[clear](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#clear()), [compute](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#compute(K,java.util.function.BiFunction)), [computeIfAbsent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#computeIfAbsent(K,java.util.function.Function)), [computeIfPresent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#computeIfPresent(K,java.util.function.BiFunction)), [containsKey](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#containsKey(java.lang.Object)), [containsValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#containsValue(java.lang.Object)), [entrySet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#entrySet()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#equals(java.lang.Object)), [forEach](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#forEach(java.util.function.BiConsumer)), [get](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#get(java.lang.Object)), [getOrDefault](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#getOrDefault(java.lang.Object,V)), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#hashCode()), [isEmpty](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#isEmpty()), [keySet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#keySet()), [merge](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#merge(K,V,java.util.function.BiFunction)), [putAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#putAll(java.util.Map)), [putIfAbsent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#putIfAbsent(K,V)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#remove(java.lang.Object)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#remove(java.lang.Object,java.lang.Object)), [replace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replace(K,V)), [replace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replace(K,V,V)), [replaceAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replaceAll(java.util.function.BiFunction)), [size](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#size()), [values](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#values())`

============ METHOD DETAIL ========== 
Method Details
get
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) get([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mdUml2Metaclass)
Returns corresponding Eclipse UML2 model metaclass.
Parameters:
`mdUml2Metaclass` -
Returns:
Eclipse UML2 metaclass name
put
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) put([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mdClassName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) eClassName)
Maps MagicDraw UML2 model metaclass to Eclipse UML2 model metaclass.
Specified by:
`[put](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#put(K,V))` in interface `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
Parameters:
`mdClassName` - MagicDraw UML2 model metaclass name
`eClassName` - Eclipse UML2 model metaclass name
remove
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) remove([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mdClassName)
Removes mapping between MagicDraw UML2 model metaclass and Eclipse UML2 model metaclass.
Parameters:
`mdClassName` - MagicDraw UML2 model metaclass name

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.helpers</a></div>
<h1 class="title" title="Interface MetaclassMap">Interface MetaclassMap</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../v3/imp0rt/convert/Emf2MofUml2MetaclassMap.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert">Emf2MofUml2MetaclassMap</a></code>, <code>com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.Emf2MofUml2MetaclassMapImpl</code>, <code><a href="../v3/export/convert/Mof2EmfUml2MetaclassMap.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.export.convert">Mof2EmfUml2MetaclassMap</a></code>, <code>com.nomagic.magicdraw.emfuml2xmi.export.convert.Mof2EmfUml2MetaclassMapImpl</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MetaclassMap</span><span class="extends-implements">
extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span></div>
<div class="block">MagicDraw UML2 model metaclass --&gt; Eclipse (EMF) UML2 model metaclass</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mdUml2Metaclass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns corresponding Eclipse UML2 model metaclass.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#put(java.lang.String,java.lang.String)">put</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mdClassName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> eClassName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Maps MagicDraw UML2 model metaclass to Eclipse UML2 model metaclass.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#remove(java.lang.String)">remove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mdClassName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes mapping between MagicDraw UML2 model metaclass and Eclipse UML2 model metaclass.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Map">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#compute(K,java.util.function.BiFunction)" title="class or interface in java.util">compute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#computeIfAbsent(K,java.util.function.Function)" title="class or interface in java.util">computeIfAbsent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#computeIfPresent(K,java.util.function.BiFunction)" title="class or interface in java.util">computeIfPresent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#containsKey(java.lang.Object)" title="class or interface in java.util">containsKey</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#containsValue(java.lang.Object)" title="class or interface in java.util">containsValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#entrySet()" title="class or interface in java.util">entrySet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#forEach(java.util.function.BiConsumer)" title="class or interface in java.util">forEach</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#get(java.lang.Object)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#getOrDefault(java.lang.Object,V)" title="class or interface in java.util">getOrDefault</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#isEmpty()" title="class or interface in java.util">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#keySet()" title="class or interface in java.util">keySet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#merge(K,V,java.util.function.BiFunction)" title="class or interface in java.util">merge</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#putAll(java.util.Map)" title="class or interface in java.util">putAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#putIfAbsent(K,V)" title="class or interface in java.util">putIfAbsent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#remove(java.lang.Object,java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replace(K,V)" title="class or interface in java.util">replace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replace(K,V,V)" title="class or interface in java.util">replace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replaceAll(java.util.function.BiFunction)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#size()" title="class or interface in java.util">size</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#values()" title="class or interface in java.util">values</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mdUml2Metaclass)</span></div>
<div class="block">Returns corresponding Eclipse UML2 model metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdUml2Metaclass</code> - </dd>
<dt>Returns:</dt>
<dd>Eclipse UML2 metaclass name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="put(java.lang.String,java.lang.String)">
<h3>put</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">put</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mdClassName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> eClassName)</span></div>
<div class="block">Maps MagicDraw UML2 model metaclass to Eclipse UML2 model metaclass.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#put(K,V)" title="class or interface in java.util">put</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>mdClassName</code> - MagicDraw UML2 model metaclass name</dd>
<dd><code>eClassName</code> - Eclipse UML2 model metaclass name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(java.lang.String)">
<h3>remove</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">remove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mdClassName)</span></div>
<div class="block">Removes mapping between MagicDraw UML2 model metaclass and Eclipse UML2 model metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdClassName</code> - MagicDraw UML2 model metaclass name</dd>
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
