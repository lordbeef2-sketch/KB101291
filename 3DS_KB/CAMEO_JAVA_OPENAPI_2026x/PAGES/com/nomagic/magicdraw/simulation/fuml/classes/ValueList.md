# JAVA OPENAPI: ValueList (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/simulation/fuml/classes/ValueList.html
- source_path: `com/nomagic/magicdraw/simulation/fuml/classes/ValueList.html`
- source_sha256: `02c7b8cbec4961cbdd12a5a5cbed7c49ef9329fbf82d0897dbc35852d6edb5b5`
- captured_utc: `2026-07-14T16:58:03.092593+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.fuml.classes](package-summary.html)

## Class ValueList

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)<[Value](Value.html)>
[java.util.AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<[Value](Value.html)>
[java.util.ArrayList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html)<[Value](Value.html)>
com.nomagic.magicdraw.simulation.fuml.ArrayListListenerable<[Value](Value.html)>
com.nomagic.magicdraw.simulation.fuml.classes.ValueList

All Implemented Interfaces:
`com.nomagic.magicdraw.simulation.listener.SimulationListenerable`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)<[Value](Value.html)>`, `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Value](Value.html)>`, `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Value](Value.html)>`, `[RandomAccess](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/RandomAccess.html)`, `[SequencedCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html)<[Value](Value.html)>`

@OpenApipublic classValueList
extends com.nomagic.magicdraw.simulation.fuml.ArrayListListenerable<[Value](Value.html)>

See Also:
[Serialized Form](../../../../../../serialized-form.html#com.nomagic.magicdraw.simulation.fuml.classes.ValueList)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[modCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#modCount)`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.magicdraw.simulation.fuml.ArrayListListenerable
`add, add, addAll, addAll, addAllNoSync, addNoSync, copy, equals, firePropertyChange, forEach, get, getListeners, hashCode, indexOf, isEmpty, lastIndexOf, register, register, remove, remove, removeAll, removeLast, replaceAll, retainAll, set, size, sort, toArray, toArray, toArray, unregister`
Methods inherited from class java.util.[ArrayList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html)
`[addFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#addFirst(E)), [addLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#addLast(E)), [clear](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#clear()), [clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#clone()), [contains](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#contains(java.lang.Object)), [ensureCapacity](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#ensureCapacity(int)), [getFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#getFirst()), [getLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#getLast()), [iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#iterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#listIterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#listIterator(int)), [removeFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#removeFirst()), [removeIf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#removeIf(java.util.function.Predicate)), [removeLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#removeLast()), [removeRange](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#removeRange(int,int)), [spliterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#subList(int,int)), [trimToSize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#trimToSize())`
Methods inherited from class java.util.[AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)
`[containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()), [stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream())`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)
`[containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed())`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.fuml.classes</a></div>
<h1 class="title" title="Class ValueList">Class ValueList</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">java.util.AbstractCollection</a>&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">java.util.AbstractList</a>&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html" title="class or interface in java.util">java.util.ArrayList</a>&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.ArrayListListenerable&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.classes.ValueList</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.simulation.listener.SimulationListenerable</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/RandomAccess.html" title="class or interface in java.util">RandomAccess</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html" title="class or interface in java.util">SequencedCollection</a>&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ValueList</span>
<span class="extends-implements">extends com.nomagic.magicdraw.simulation.fuml.ArrayListListenerable&lt;<a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a>&gt;</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../serialized-form.html#com.nomagic.magicdraw.simulation.fuml.classes.ValueList">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-java.util.AbstractList">Fields inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#modCount" title="class or interface in java.util">modCount</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.ArrayListListenerable">Methods inherited from class com.nomagic.magicdraw.simulation.fuml.ArrayListListenerable</h3>
<code>add, add, addAll, addAll, addAllNoSync, addNoSync, copy, equals, firePropertyChange, forEach, get, getListeners, hashCode, indexOf, isEmpty, lastIndexOf, register, register, remove, remove, removeAll, removeLast, replaceAll, retainAll, set, size, sort, toArray, toArray, toArray, unregister</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.ArrayList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html" title="class or interface in java.util">ArrayList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#addFirst(E)" title="class or interface in java.util">addFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#addLast(E)" title="class or interface in java.util">addLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#clone()" title="class or interface in java.util">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#contains(java.lang.Object)" title="class or interface in java.util">contains</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#ensureCapacity(int)" title="class or interface in java.util">ensureCapacity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#getFirst()" title="class or interface in java.util">getFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#getLast()" title="class or interface in java.util">getLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#listIterator(int)" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#removeFirst()" title="class or interface in java.util">removeFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#removeIf(java.util.function.Predicate)" title="class or interface in java.util">removeIf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#removeLast()" title="class or interface in java.util">removeLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#removeRange(int,int)" title="class or interface in java.util">removeRange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#subList(int,int)" title="class or interface in java.util">subList</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html#trimToSize()" title="class or interface in java.util">trimToSize</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractCollection">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toString()" title="class or interface in java.util">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Collection">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()" title="class or interface in java.util">parallelStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()" title="class or interface in java.util">stream</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()" title="class or interface in java.util">reversed</a></code></div>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
