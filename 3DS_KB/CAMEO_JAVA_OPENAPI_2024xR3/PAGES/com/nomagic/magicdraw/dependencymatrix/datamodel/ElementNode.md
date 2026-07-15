# JAVA OPENAPI: ElementNode (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/dependencymatrix/datamodel/ElementNode.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/ElementNode.html`
- source_sha256: `b6b57c5f1d0e6953b995283bc72c77957df7feaf8a3a38acf8d621562914fded`
- captured_utc: `2026-07-14T16:55:15.606010+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel](package-summary.html)

## Class ElementNode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.tree.DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode

All Implemented Interfaces:
`com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`, `[MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html)`, `[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`

@OpenApipublic classElementNode
extends [DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
implements com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>, [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)

Tree node which represents instance of an [`Element`](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)
 Note: children of the node often does NOT represent the owned elements of the model Element, tree model can be constructed by different criteria

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider`
`[elementNodeIDProvider](#elementNodeIDProvider)`
Fields inherited from class javax.swing.tree.[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
`[allowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#allowsChildren), [children](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children), [EMPTY_ENUMERATION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#EMPTY_ENUMERATION), [parent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#parent), [userObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#userObject)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementNode](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Creates new node, which has element inside.
`[ElementNode](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean real)`

`[ElementNode](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean real,
 com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider nodeIDProvider)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[add](#add(javax.swing.tree.MutableTreeNode))([MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html) newChild)`

`void`
`[addGroupNode](#addGroupNode(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([ElementNode](ElementNode.html) node)`

`int`
`[compareTo](#compareTo(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[Enumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html)<[ElementNode](ElementNode.html)>`
`[getBreadthFirstEnumeration](#getBreadthFirstEnumeration())()`

`[ElementNode](ElementNode.html)`
`[getChild](#getChild(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Finds node which represents provided element between this node's direct children
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ElementNode](ElementNode.html)>`
`[getChildren](#getChildren())()`

`[Enumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html)<[ElementNode](ElementNode.html)>`
`[getDepthFirstEnumeration](#getDepthFirstEnumeration())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`

`[ElementNode](ElementNode.html)`
`[getGroupNodeChildAt](#getGroupNodeChildAt(int))(int index)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ElementNode](ElementNode.html)>`
`[getGroupNodeChildren](#getGroupNodeChildren())()`
Get all children as single list
`int`
`[getGroupNodeIndex](#getGroupNodeIndex(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([ElementNode](ElementNode.html) node)`

`[ElementNode](ElementNode.html)`
`[getGroupNodeParent](#getGroupNodeParent())()`

`[ElementNode](ElementNode.html)[]`
`[getGroupNodePath](#getGroupNodePath())()`

`int`
`[getIndex](#getIndex(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getNodeID](#getNodeID())()`

`[ElementNode](ElementNode.html)`
`[getOriginal](#getOriginal())()`

`[ElementNode](ElementNode.html)`
`[getParent](#getParent())()`

`int`
`[hashCode](#hashCode())()`

`boolean`
`[isExpanded](#isExpanded())()`

`boolean`
`[isInfinityNode](#isInfinityNode())()`
Nodes which represent recursive branches are marked as
 infinite nodes, meaning the rest of the infinite branch is cut off bellow this node
`boolean`
`[isReal](#isReal())()`
Tells if this node belongs to the model represented by the tree
`void`
`[remove](#remove(int))(int childIndex)`

`void`
`[removeGroupNode](#removeGroupNode(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([ElementNode](ElementNode.html) node)`

`final void`
`[setExpanded](#setExpanded(boolean))(boolean expanded)`

`void`
`[setOriginal](#setOriginal(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([ElementNode](ElementNode.html) original)`

`final void`
`[setReal](#setReal(boolean))(boolean real)`
Does this node belong to the model or it is only as grouping element (parent node)
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class javax.swing.tree.[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
`[breadthFirstEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#breadthFirstEnumeration()), [children](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children()), [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#clone()), [depthFirstEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#depthFirstEnumeration()), [getAllowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getAllowsChildren()), [getChildAfter](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAfter(javax.swing.tree.TreeNode)), [getChildAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAt(int)), [getChildBefore](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildBefore(javax.swing.tree.TreeNode)), [getChildCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildCount()), [getDepth](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getDepth()), [getFirstChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstChild()), [getFirstLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstLeaf()), [getIndex](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getIndex(javax.swing.tree.TreeNode)), [getLastChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastChild()), [getLastLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastLeaf()), [getLeafCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLeafCount()), [getLevel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLevel()), [getNextLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextLeaf()), [getNextNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextNode()), [getNextSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextSibling()), [getPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPath()), [getPathToRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPathToRoot(javax.swing.tree.TreeNode,int)), [getPreviousLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousLeaf()), [getPreviousNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousNode()), [getPreviousSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousSibling()), [getRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getRoot()), [getSharedAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSharedAncestor(javax.swing.tree.DefaultMutableTreeNode)), [getSiblingCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSiblingCount()), [getUserObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObject()), [getUserObjectPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObjectPath()), [insert](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#insert(javax.swing.tree.MutableTreeNode,int)), [isLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isLeaf()), [isNodeAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeAncestor(javax.swing.tree.TreeNode)), [isNodeChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeChild(javax.swing.tree.TreeNode)), [isNodeDescendant](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeDescendant(javax.swing.tree.DefaultMutableTreeNode)), [isNodeRelated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeRelated(javax.swing.tree.DefaultMutableTreeNode)), [isNodeSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeSibling(javax.swing.tree.TreeNode)), [isRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isRoot()), [pathFromAncestorEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#pathFromAncestorEnumeration(javax.swing.tree.TreeNode)), [postorderEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#postorderEnumeration()), [preorderEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#preorderEnumeration()), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(javax.swing.tree.MutableTreeNode)), [removeAllChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeAllChildren()), [removeFromParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeFromParent()), [setAllowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setAllowsChildren(boolean)), [setParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setParent(javax.swing.tree.MutableTreeNode)), [setUserObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setUserObject(java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.grouping.GroupNode
`getChildCount, removeAllChildren`

============ FIELD DETAIL =========== 
Field Details
elementNodeIDProvider
@CheckForNullprotected com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider elementNodeIDProvider
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementNode
public ElementNode(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Creates new node, which has element inside.
Parameters:
`element` - tree node information
ElementNode
public ElementNode(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean real)
Parameters:
`element` - tree node information
`real` - `false` if this node does not belong to the model (is parent only)
 Default value: `true`
ElementNode
public ElementNode(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean real,
 @CheckForNull
 com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider nodeIDProvider)
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
`[getParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getParent())` in interface `[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`
Overrides:
`[getParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getParent())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
getChildren
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ElementNode](ElementNode.html)> getChildren()
Returns:
direct children of this node
getChild
@CheckForNullpublic [ElementNode](ElementNode.html) getChild([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Finds node which represents provided element between this node's direct children
Specified by:
`getChild` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
Parameters:
`element` - element for which to search node
Returns:
node which represents this element or null
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
getBreadthFirstEnumeration
public [Enumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html)<[ElementNode](ElementNode.html)> getBreadthFirstEnumeration()
Specified by:
`getBreadthFirstEnumeration` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
getDepthFirstEnumeration
public [Enumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html)<[ElementNode](ElementNode.html)> getDepthFirstEnumeration()
Specified by:
`getDepthFirstEnumeration` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
add
public void add([MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html) newChild)
Overrides:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#add(javax.swing.tree.MutableTreeNode))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
addGroupNode
public void addGroupNode([ElementNode](ElementNode.html) node)
Specified by:
`addGroupNode` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
getGroupNodeIndex
public int getGroupNodeIndex([ElementNode](ElementNode.html) node)
Specified by:
`getGroupNodeIndex` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
getIndex
public int getIndex(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Specified by:
`getIndex` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
removeGroupNode
public void removeGroupNode([ElementNode](ElementNode.html) node)
Specified by:
`removeGroupNode` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
remove
public void remove(int childIndex)
Specified by:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#remove(int))` in interface `[MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html)`
Overrides:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(int))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
getGroupNodeParent
public [ElementNode](ElementNode.html) getGroupNodeParent()
Specified by:
`getGroupNodeParent` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
getGroupNodeChildren
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ElementNode](ElementNode.html)> getGroupNodeChildren()
Get all children as single list
Specified by:
`getGroupNodeChildren` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
Returns:
children (recursive)
getGroupNodeChildAt
public [ElementNode](ElementNode.html) getGroupNodeChildAt(int index)
Specified by:
`getGroupNodeChildAt` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
setReal
public final void setReal(boolean real)
Does this node belong to the model or it is only as grouping element (parent node)
Specified by:
`setReal` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
Parameters:
`real` - `true` if this node belongs to the model
setExpanded
public final void setExpanded(boolean expanded)
getNodeID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getNodeID()
getGroupNodePath
public [ElementNode](ElementNode.html)[] getGroupNodePath()
Specified by:
`getGroupNodePath` in interface `com.nomagic.magicdraw.grouping.GroupNode<[ElementNode](ElementNode.html)>`
getOriginal
public [ElementNode](ElementNode.html) getOriginal()
setOriginal
public void setOriginal(@CheckForNull
 [ElementNode](ElementNode.html) original)
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
compareTo
public int compareTo(@Nonnull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Specified by:
`[compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T))` in interface `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#toString())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel</a></div>
<h1 class="title" title="Class ElementNode">Class ElementNode</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">javax.swing.tree.DefaultMutableTreeNode</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementNode</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a>
implements com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></span></div>
<div class="block">Tree node which represents instance of an <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a>
 Note: children of the node often does NOT represent the owned elements of the model Element, tree model can be constructed by different criteria</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
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
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#elementNodeIDProvider">elementNodeIDProvider</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.tree.DefaultMutableTreeNode">Fields inherited from class javax.swing.tree.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#allowsChildren" title="class or interface in javax.swing.tree">allowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children" title="class or interface in javax.swing.tree">children</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#EMPTY_ENUMERATION" title="class or interface in javax.swing.tree">EMPTY_ENUMERATION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#parent" title="class or interface in javax.swing.tree">parent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#userObject" title="class or interface in javax.swing.tree">userObject</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">ElementNode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates new node, which has element inside.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">ElementNode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean real)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider)">ElementNode</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean real,
 com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider nodeIDProvider)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(javax.swing.tree.MutableTreeNode)">add</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a> newChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addGroupNode(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">addGroupNode</a><wbr/>(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareTo(java.lang.Object)">compareTo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html" title="class or interface in java.util">Enumeration</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBreadthFirstEnumeration()">getBreadthFirstEnumeration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChild(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getChild</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds node which represents provided element between this node's direct children</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildren()">getChildren</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html" title="class or interface in java.util">Enumeration</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDepthFirstEnumeration()">getDepthFirstEnumeration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupNodeChildAt(int)">getGroupNodeChildAt</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupNodeChildren()">getGroupNodeChildren</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all children as single list</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupNodeIndex(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">getGroupNodeIndex</a><wbr/>(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupNodeParent()">getGroupNodeParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupNodePath()">getGroupNodePath</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndex(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getIndex</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNodeID()">getNodeID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginal()">getOriginal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(int)">remove</a><wbr/>(int childIndex)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeGroupNode(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">removeGroupNode</a><wbr/>(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExpanded(boolean)">setExpanded</a><wbr/>(boolean expanded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOriginal(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">setOriginal</a><wbr/>(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> original)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReal(boolean)">setReal</a><wbr/>(boolean real)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does this node belong to the model or it is only as grouping element (parent node)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.tree.DefaultMutableTreeNode">Methods inherited from class javax.swing.tree.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#breadthFirstEnumeration()" title="class or interface in javax.swing.tree">breadthFirstEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children()" title="class or interface in javax.swing.tree">children</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#clone()" title="class or interface in javax.swing.tree">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#depthFirstEnumeration()" title="class or interface in javax.swing.tree">depthFirstEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getAllowsChildren()" title="class or interface in javax.swing.tree">getAllowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAfter(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getChildAfter</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAt(int)" title="class or interface in javax.swing.tree">getChildAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildBefore(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getChildBefore</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildCount()" title="class or interface in javax.swing.tree">getChildCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getDepth()" title="class or interface in javax.swing.tree">getDepth</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstChild()" title="class or interface in javax.swing.tree">getFirstChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstLeaf()" title="class or interface in javax.swing.tree">getFirstLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getIndex(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getIndex</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastChild()" title="class or interface in javax.swing.tree">getLastChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastLeaf()" title="class or interface in javax.swing.tree">getLastLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLeafCount()" title="class or interface in javax.swing.tree">getLeafCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLevel()" title="class or interface in javax.swing.tree">getLevel</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextLeaf()" title="class or interface in javax.swing.tree">getNextLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextNode()" title="class or interface in javax.swing.tree">getNextNode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextSibling()" title="class or interface in javax.swing.tree">getNextSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPath()" title="class or interface in javax.swing.tree">getPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPathToRoot(javax.swing.tree.TreeNode,int)" title="class or interface in javax.swing.tree">getPathToRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousLeaf()" title="class or interface in javax.swing.tree">getPreviousLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousNode()" title="class or interface in javax.swing.tree">getPreviousNode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousSibling()" title="class or interface in javax.swing.tree">getPreviousSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getRoot()" title="class or interface in javax.swing.tree">getRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSharedAncestor(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">getSharedAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSiblingCount()" title="class or interface in javax.swing.tree">getSiblingCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObject()" title="class or interface in javax.swing.tree">getUserObject</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObjectPath()" title="class or interface in javax.swing.tree">getUserObjectPath</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#insert(javax.swing.tree.MutableTreeNode,int)" title="class or interface in javax.swing.tree">insert</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isLeaf()" title="class or interface in javax.swing.tree">isLeaf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeAncestor(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeChild(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeChild</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeDescendant(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">isNodeDescendant</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeRelated(javax.swing.tree.DefaultMutableTreeNode)" title="class or interface in javax.swing.tree">isNodeRelated</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeSibling(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">isNodeSibling</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isRoot()" title="class or interface in javax.swing.tree">isRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#pathFromAncestorEnumeration(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">pathFromAncestorEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#postorderEnumeration()" title="class or interface in javax.swing.tree">postorderEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#preorderEnumeration()" title="class or interface in javax.swing.tree">preorderEnumeration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(javax.swing.tree.MutableTreeNode)" title="class or interface in javax.swing.tree">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeAllChildren()" title="class or interface in javax.swing.tree">removeAllChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeFromParent()" title="class or interface in javax.swing.tree">removeFromParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setAllowsChildren(boolean)" title="class or interface in javax.swing.tree">setAllowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setParent(javax.swing.tree.MutableTreeNode)" title="class or interface in javax.swing.tree">setParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setUserObject(java.lang.Object)" title="class or interface in javax.swing.tree">setUserObject</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.grouping.GroupNode">Methods inherited from interface com.nomagic.magicdraw.grouping.GroupNode</h3>
<code>getChildCount, removeAllChildren</code></div>
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
<section class="detail" id="elementNodeIDProvider">
<h3>elementNodeIDProvider</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider</span> <span class="element-name">elementNodeIDProvider</span></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>ElementNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Creates new node, which has element inside.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - tree node information</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>ElementNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean real)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - tree node information</dd>
<dd><code>real</code> - <code>false</code> if this node does not belong to the model (is parent only)
                Default value: <code>true</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean,com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider)">
<h3>ElementNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementNode</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean real,
 @CheckForNull
 com.nomagic.magicdraw.dependencymatrix.datamodel.grouping.ScopeElementNodeIDProvider nodeIDProvider)</span></div>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getParent()" title="class or interface in javax.swing.tree">getParent</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getParent()" title="class or interface in javax.swing.tree">getParent</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildren()">
<h3>getChildren</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getChildren</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>direct children of this node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChild(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getChild</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getChild</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Finds node which represents provided element between this node's direct children</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getChild</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - element for which to search node</dd>
<dt>Returns:</dt>
<dd>node which represents this element or null</dd>
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
<li>
<section class="detail" id="getBreadthFirstEnumeration()">
<h3>getBreadthFirstEnumeration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html" title="class or interface in java.util">Enumeration</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getBreadthFirstEnumeration</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getBreadthFirstEnumeration</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDepthFirstEnumeration()">
<h3>getDepthFirstEnumeration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html" title="class or interface in java.util">Enumeration</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getDepthFirstEnumeration</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getDepthFirstEnumeration</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(javax.swing.tree.MutableTreeNode)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a> newChild)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#add(javax.swing.tree.MutableTreeNode)" title="class or interface in javax.swing.tree">add</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addGroupNode(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>addGroupNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addGroupNode</span><wbr/><span class="parameters">(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> node)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>addGroupNode</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroupNodeIndex(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>getGroupNodeIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getGroupNodeIndex</span><wbr/><span class="parameters">(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> node)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getGroupNodeIndex</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndex(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndex</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getIndex</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeGroupNode(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>removeGroupNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeGroupNode</span><wbr/><span class="parameters">(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> node)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>removeGroupNode</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(int)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(int childIndex)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#remove(int)" title="class or interface in javax.swing.tree">remove</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(int)" title="class or interface in javax.swing.tree">remove</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroupNodeParent()">
<h3>getGroupNodeParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getGroupNodeParent</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getGroupNodeParent</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroupNodeChildren()">
<h3>getGroupNodeChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getGroupNodeChildren</span>()</div>
<div class="block">Get all children as single list</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getGroupNodeChildren</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>children (recursive)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroupNodeChildAt(int)">
<h3>getGroupNodeChildAt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getGroupNodeChildAt</span><wbr/><span class="parameters">(int index)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getGroupNodeChildAt</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReal(boolean)">
<h3>setReal</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setReal</span><wbr/><span class="parameters">(boolean real)</span></div>
<div class="block">Does this node belong to the model or it is only as grouping element (parent node)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setReal</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>real</code> - <code>true</code> if this node belongs to the model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExpanded(boolean)">
<h3>setExpanded</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setExpanded</span><wbr/><span class="parameters">(boolean expanded)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNodeID()">
<h3>getNodeID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNodeID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getGroupNodePath()">
<h3>getGroupNodePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>[]</span> <span class="element-name">getGroupNodePath</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getGroupNodePath</code> in interface <code>com.nomagic.magicdraw.grouping.GroupNode&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginal()">
<h3>getOriginal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getOriginal</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setOriginal(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>setOriginal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOriginal</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> original)</span></div>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareTo(java.lang.Object)">
<h3>compareTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compareTo</span><wbr/><span class="parameters">(@Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#toString()" title="class or interface in javax.swing.tree">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
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
