# JAVA OPENAPI: ElementNode (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/dependencymatrix/datamodel/ElementNode.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/ElementNode.html`
- source_sha256: `6f2e10d2b9fd3238bdd0f295d36069b480ef5dc1a00ddb6e340ecf3d11ebbd55`
- captured_utc: `2026-07-14T16:57:53.434484+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel](package-summary.html)

## Class ElementNode

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.tree.DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode

All Implemented Interfaces:
`com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)`, `[MutableTreeNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html)`, `[TreeNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`

@OpenApipublic classElementNode
extends [DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
implements com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>, [Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)

Tree node which represents instance of an [`Element`](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)
 Note: children of the node often does NOT represent the owned elements of the model Element, tree model can be constructed by different criteria

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class javax.swing.tree.[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
`[allowsChildren](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#allowsChildren), [children](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children), [EMPTY_ENUMERATION](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#EMPTY_ENUMERATION), [parent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#parent), [userObject](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#userObject)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ElementNode](ElementNode.html)>`
`[getChildren](#getChildren())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`

`[ElementNode](ElementNode.html)`
`[getParent](#getParent())()`

`boolean`
`[isExpanded](#isExpanded())()`

`boolean`
`[isInfinityNode](#isInfinityNode())()`
Nodes which represent recursive branches are marked as
 infinite nodes, meaning the rest of the infinite branch is cut off bellow this node
`boolean`
`[isReal](#isReal())()`
Tells if this node belongs to the model represented by the tree
Methods inherited from class javax.swing.tree.[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
`[breadthFirstEnumeration](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#breadthFirstEnumeration()), [children](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children()), [clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#clone()), [depthFirstEnumeration](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#depthFirstEnumeration()), [getAllowsChildren](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getAllowsChildren()), [getChildAfter](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAfter(javax.swing.tree.TreeNode)), [getChildAt](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAt(int)), [getChildBefore](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildBefore(javax.swing.tree.TreeNode)), [getChildCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildCount()), [getDepth](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getDepth()), [getFirstChild](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstChild()), [getFirstLeaf](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstLeaf()), [getIndex](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getIndex(javax.swing.tree.TreeNode)), [getLastChild](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastChild()), [getLastLeaf](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastLeaf()), [getLeafCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLeafCount()), [getLevel](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLevel()), [getNextLeaf](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextLeaf()), [getNextNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextNode()), [getNextSibling](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextSibling()), [getPath](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPath()), [getPathToRoot](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPathToRoot(javax.swing.tree.TreeNode,int)), [getPreviousLeaf](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousLeaf()), [getPreviousNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousNode()), [getPreviousSibling](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousSibling()), [getRoot](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getRoot()), [getSharedAncestor](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSharedAncestor(javax.swing.tree.DefaultMutableTreeNode)), [getSiblingCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSiblingCount()), [getUserObject](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObject()), [getUserObjectPath](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObjectPath()), [insert](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#insert(javax.swing.tree.MutableTreeNode,int)), [isLeaf](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isLeaf()), [isNodeAncestor](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeAncestor(javax.swing.tree.TreeNode)), [isNodeChild](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeChild(javax.swing.tree.TreeNode)), [isNodeDescendant](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeDescendant(javax.swing.tree.DefaultMutableTreeNode)), [isNodeRelated](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeRelated(javax.swing.tree.DefaultMutableTreeNode)), [isNodeSibling](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeSibling(javax.swing.tree.TreeNode)), [isRoot](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isRoot()), [pathFromAncestorEnumeration](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#pathFromAncestorEnumeration(javax.swing.tree.TreeNode)), [postorderEnumeration](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#postorderEnumeration()), [preorderEnumeration](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#preorderEnumeration()), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(javax.swing.tree.MutableTreeNode)), [removeAllChildren](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeAllChildren()), [removeFromParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeFromParent()), [setAllowsChildren](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setAllowsChildren(boolean)), [setParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setParent(javax.swing.tree.MutableTreeNode)), [setUserObject](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setUserObject(java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.grouping.GroupNode
`getChildCount, removeAllChildren`

============ METHOD DETAIL ========== 
Method Details
getElement
@CheckForNull
@OpenApipublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Specified by:
`getElement` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
Returns:
model element represented by this node
getParent
@OpenApipublic [ElementNode](ElementNode.html) getParent()
Specified by:
`[getParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getParent())` in interface `[TreeNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`
Overrides:
`[getParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getParent())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
getChildren
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ElementNode](ElementNode.html)> getChildren()
Returns:
direct children of this node
isReal
@OpenApipublic boolean isReal()
Tells if this node belongs to the model represented by the tree
Specified by:
`isReal` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
Returns:
true if this node truly belongs to the model represented by the tree 

 false if this node is only a grouping node for viewing and collapsing purposes
isExpanded
@OpenApipublic boolean isExpanded()
Returns:
true if node is currently expanded, meaning child nodes are visible
isInfinityNode
@OpenApipublic boolean isInfinityNode()
Nodes which represent recursive branches are marked as
 infinite nodes, meaning the rest of the infinite branch is cut off bellow this node
Specified by:
`isInfinityNode` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
Returns:
true if the branch is infinitely recursive and is cut below this node.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel</a></div>
<h1 class="title" title="Class ElementNode">Class ElementNode</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">javax.swing.tree.DefaultMutableTreeNode</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementNode</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a>
implements com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></span></div>
<div class="block">Tree node which represents instance of an <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>
 Note: children of the node often does NOT represent the owned elements of the model Element, tree model can be constructed by different criteria</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-javax.swing.tree.DefaultMutableTreeNode">Fields inherited from class javax.swing.tree.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#allowsChildren" title="class or interface in javax.swing.tree">allowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children" title="class or interface in javax.swing.tree">children</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#EMPTY_ENUMERATION" title="class or interface in javax.swing.tree">EMPTY_ENUMERATION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#parent" title="class or interface in javax.swing.tree">parent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#userObject" title="class or interface in javax.swing.tree">userObject</a></code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildren()">getChildren</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExpanded()">isExpanded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInfinityNode()">isInfinityNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Nodes which represent recursive branches are marked as
 infinite nodes, meaning the rest of the infinite branch is cut off bellow this node</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isReal()">isReal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tells if this node belongs to the model represented by the tree</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.tree.DefaultMutableTreeNode">Methods inherited from class javax.swing.tree.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#breadthFirstEnumeration()" title="class or interface in javax.swing.tree">breadthFirstEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children()" title="class or interface in javax.swing.tree">children</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#clone()" title="class or interface in javax.swing.tree">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#depthFirstEnumeration()" title="class or interface in javax.swing.tree">depthFirstEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getAllowsChildren()" title="class or interface in javax.swing.tree">getAllowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAfter(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getChildAfter</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAt(int)" title="class or interface in javax.swing.tree">getChildAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildBefore(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getChildBefore</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildCount()" title="class or interface in javax.swing.tree">getChildCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getDepth()" title="class or interface in javax.swing.tree">getDepth</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstChild()" title="class or interface in javax.swing.tree">getFirstChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstLeaf()" title="class or interface in javax.swing.tree">getFirstLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getIndex(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getIndex</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastChild()" title="class or interface in javax.swing.tree">getLastChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastLeaf()" title="class or interface in javax.swing.tree">getLastLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLeafCount()" title="class or interface in javax.swing.tree">getLeafCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLevel()" title="class or interface in javax.swing.tree">getLevel</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextLeaf()" title="class or interface in javax.swing.tree">getNextLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextNode()" title="class or interface in javax.swing.tree">getNextNode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextSibling()" title="class or interface in javax.swing.tree">getNextSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPath()" title="class or interface in javax.swing.tree">getPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPathToRoot(javax.swing.tree.TreeNode,int)" title="class or interface in javax.swing.tree">getPathToRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousLeaf()" title="class or interface in javax.swing.tree">getPreviousLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousNode()" title="class or interface in javax.swing.tree">getPreviousNode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousSibling()" title="class or interface in javax.swing.tree">getPreviousSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getRoot()" title="class or interface in javax.swing.tree">getRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSharedAncestor(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">getSharedAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSiblingCount()" title="class or interface in javax.swing.tree">getSiblingCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObject()" title="class or interface in javax.swing.tree">getUserObject</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObjectPath()" title="class or interface in javax.swing.tree">getUserObjectPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#insert(javax.swing.tree.MutableTreeNode,int)" title="class or interface in javax.swing.tree">insert</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isLeaf()" title="class or interface in javax.swing.tree">isLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeAncestor(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeChild(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeDescendant(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">isNodeDescendant</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeRelated(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">isNodeRelated</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeSibling(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isRoot()" title="class or interface in javax.swing.tree">isRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#pathFromAncestorEnumeration(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">pathFromAncestorEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#postorderEnumeration()" title="class or interface in javax.swing.tree">postorderEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#preorderEnumeration()" title="class or interface in javax.swing.tree">preorderEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(javax.swing.tree.MutableTreeNode)" title="class or interface in javax.swing.tree">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeAllChildren()" title="class or interface in javax.swing.tree">removeAllChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeFromParent()" title="class or interface in javax.swing.tree">removeFromParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setAllowsChildren(boolean)" title="class or interface in javax.swing.tree">setAllowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setParent(javax.swing.tree.MutableTreeNode)" title="class or interface in javax.swing.tree">setParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setUserObject(java.lang.Object)" title="class or interface in javax.swing.tree">setUserObject</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.grouping.GroupNode">Methods inherited from interface com.nomagic.magicdraw.grouping.GroupNode</h3>
<code>getChildCount, removeAllChildren</code></div>
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
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getElement</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>model element represented by this node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParent()">
<h3>getParent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getParent</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getParent()" title="class or interface in javax.swing.tree">getParent</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getParent()" title="class or interface in javax.swing.tree">getParent</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildren()">
<h3>getChildren</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getChildren</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>direct children of this node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isReal()">
<h3>isReal</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isReal</span>()</div>
<div class="block">Tells if this node belongs to the model represented by the tree</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isReal</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>true if this node truly belongs to the model represented by the tree<br/>
 false if this node is only a grouping node for viewing and collapsing purposes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExpanded()">
<h3>isExpanded</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExpanded</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if node is currently expanded, meaning child nodes are visible</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInfinityNode()">
<h3>isInfinityNode</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInfinityNode</span>()</div>
<div class="block">Nodes which represent recursive branches are marked as
 infinite nodes, meaning the rest of the infinite branch is cut off bellow this node</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isInfinityNode</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>true if the branch is infinitely recursive and is cut below this node.</dd>
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
