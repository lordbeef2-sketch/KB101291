# JAVA OPENAPI: Node (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ui/browser/Node.html
- source_path: `com/nomagic/magicdraw/ui/browser/Node.html`
- source_sha256: `acec04eb3510f0b4cf9645d1ce1f991b6765bb6fdb99222d6e60a9ec39362cba`
- captured_utc: `2026-07-14T16:52:04.385777+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.browser](package-summary.html)

## Class Node

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.tree.DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
com.nomagic.magicdraw.ui.browser.Node

All Implemented Interfaces:
`com.nomagic.magicdraw.ui.browser.Expandable`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html)`, `[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`

@OpenApipublic classNode
extends [DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
implements [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html), com.nomagic.magicdraw.ui.browser.Expandable

The base node of all tree nodes. This node has some user object.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.ui.browser.Node)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class javax.swing.tree.[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
`[allowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#allowsChildren), [EMPTY_ENUMERATION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#EMPTY_ENUMERATION), [parent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#parent), [userObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#userObject)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getUserObject](#getUserObject())()`
Returns user object of this node.
Methods inherited from class javax.swing.tree.[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
`[breadthFirstEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#breadthFirstEnumeration()), [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#clone()), [depthFirstEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#depthFirstEnumeration()), [getAllowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getAllowsChildren()), [getChildAfter](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAfter(javax.swing.tree.TreeNode)), [getChildBefore](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildBefore(javax.swing.tree.TreeNode)), [getDepth](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getDepth()), [getFirstChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstChild()), [getFirstLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstLeaf()), [getLastChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastChild()), [getLastLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastLeaf()), [getLeafCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLeafCount()), [getLevel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLevel()), [getNextLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextLeaf()), [getNextNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextNode()), [getNextSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextSibling()), [getPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPath()), [getPathToRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPathToRoot(javax.swing.tree.TreeNode,int)), [getPreviousLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousLeaf()), [getPreviousNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousNode()), [getPreviousSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousSibling()), [getRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getRoot()), [getSharedAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSharedAncestor(javax.swing.tree.DefaultMutableTreeNode)), [getSiblingCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSiblingCount()), [getUserObjectPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObjectPath()), [isLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isLeaf()), [isNodeAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeAncestor(javax.swing.tree.TreeNode)), [isNodeChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeChild(javax.swing.tree.TreeNode)), [isNodeDescendant](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeDescendant(javax.swing.tree.DefaultMutableTreeNode)), [isNodeRelated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeRelated(javax.swing.tree.DefaultMutableTreeNode)), [isNodeSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeSibling(javax.swing.tree.TreeNode)), [isRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isRoot()), [pathFromAncestorEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#pathFromAncestorEnumeration(javax.swing.tree.TreeNode)), [postorderEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#postorderEnumeration()), [preorderEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#preorderEnumeration()), [removeFromParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeFromParent()), [setAllowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setAllowsChildren(boolean)), [setParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setParent(javax.swing.tree.MutableTreeNode))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getUserObject
@CheckForNull
@OpenApipublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getUserObject()
Returns user object of this node.
Overrides:
`[getUserObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObject())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
Returns:
user object(some Element).

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.browser</a></div>
<h1 class="title" title="Class Node">Class Node</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">javax.swing.tree.DefaultMutableTreeNode</a>
<div class="inheritance">com.nomagic.magicdraw.ui.browser.Node</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.ui.browser.Expandable</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Node</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>, com.nomagic.magicdraw.ui.browser.Expandable</span></div>
<div class="block">The base node of all tree nodes. This node has some user object.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.ui.browser.Node">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-javax.swing.tree.DefaultMutableTreeNode">Fields inherited from class javax.swing.tree.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#allowsChildren" title="class or interface in javax.swing.tree">allowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#EMPTY_ENUMERATION" title="class or interface in javax.swing.tree">EMPTY_ENUMERATION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#parent" title="class or interface in javax.swing.tree">parent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#userObject" title="class or interface in javax.swing.tree">userObject</a></code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUserObject()">getUserObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns user object of this node.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.tree.DefaultMutableTreeNode">Methods inherited from class javax.swing.tree.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#breadthFirstEnumeration()" title="class or interface in javax.swing.tree">breadthFirstEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#clone()" title="class or interface in javax.swing.tree">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#depthFirstEnumeration()" title="class or interface in javax.swing.tree">depthFirstEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getAllowsChildren()" title="class or interface in javax.swing.tree">getAllowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAfter(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getChildAfter</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildBefore(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getChildBefore</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getDepth()" title="class or interface in javax.swing.tree">getDepth</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstChild()" title="class or interface in javax.swing.tree">getFirstChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstLeaf()" title="class or interface in javax.swing.tree">getFirstLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastChild()" title="class or interface in javax.swing.tree">getLastChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastLeaf()" title="class or interface in javax.swing.tree">getLastLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLeafCount()" title="class or interface in javax.swing.tree">getLeafCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLevel()" title="class or interface in javax.swing.tree">getLevel</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextLeaf()" title="class or interface in javax.swing.tree">getNextLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextNode()" title="class or interface in javax.swing.tree">getNextNode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextSibling()" title="class or interface in javax.swing.tree">getNextSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPath()" title="class or interface in javax.swing.tree">getPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPathToRoot(javax.swing.tree.TreeNode,int)" title="class or interface in javax.swing.tree">getPathToRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousLeaf()" title="class or interface in javax.swing.tree">getPreviousLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousNode()" title="class or interface in javax.swing.tree">getPreviousNode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousSibling()" title="class or interface in javax.swing.tree">getPreviousSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getRoot()" title="class or interface in javax.swing.tree">getRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSharedAncestor(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">getSharedAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSiblingCount()" title="class or interface in javax.swing.tree">getSiblingCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObjectPath()" title="class or interface in javax.swing.tree">getUserObjectPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isLeaf()" title="class or interface in javax.swing.tree">isLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeAncestor(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeChild(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeDescendant(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">isNodeDescendant</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeRelated(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">isNodeRelated</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeSibling(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isRoot()" title="class or interface in javax.swing.tree">isRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#pathFromAncestorEnumeration(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">pathFromAncestorEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#postorderEnumeration()" title="class or interface in javax.swing.tree">postorderEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#preorderEnumeration()" title="class or interface in javax.swing.tree">preorderEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeFromParent()" title="class or interface in javax.swing.tree">removeFromParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setAllowsChildren(boolean)" title="class or interface in javax.swing.tree">setAllowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setParent(javax.swing.tree.MutableTreeNode)" title="class or interface in javax.swing.tree">setParent</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getUserObject()">
<h3>getUserObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getUserObject</span>()</div>
<div class="block">Returns user object of this node.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObject()" title="class or interface in javax.swing.tree">getUserObject</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
<dt>Returns:</dt>
<dd>user object(some Element).</dd>
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
