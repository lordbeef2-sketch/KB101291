# JAVA OPENAPI: Node (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/browser/Node.html
- source_path: `com/nomagic/magicdraw/ui/browser/Node.html`
- source_sha256: `caee4e2e6c30af7aff085177bd2454c6274efa0cd9c682ba4fc90b8db8e12f54`
- captured_utc: `2026-07-14T16:55:52.085421+00:00`

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
Fields
Modifier and Type
Field
Description
`protected boolean`
`[ignoreRootCheck](#ignoreRootCheck)`

`static final int`
`[MAX_NODE_UPDATE_RETRY_COUNT](#MAX_NODE_UPDATE_RETRY_COUNT)`
Fields inherited from class javax.swing.tree.[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
`[allowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#allowsChildren), [EMPTY_ENUMERATION](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#EMPTY_ENUMERATION), [parent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#parent), [userObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#userObject)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Node](#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon))([BaseElement](../../uml/BaseElement.html) element,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`

`[Node](#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon,javax.swing.Icon))([BaseElement](../../uml/BaseElement.html) element,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) defaultIcon)`

`[Node](#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon,javax.swing.Icon,com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams))([BaseElement](../../uml/BaseElement.html) element,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) defaultIcon,
 com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams nodeTextParams)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[acceptCopy](#acceptCopy(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`
Accepts drag and drop link action
`protected void`
`[acceptCopySpecific](#acceptCopySpecific(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> elements)`

`final void`
`[acceptLink](#acceptLink(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`
Accepts drag and drop link action
`protected void`
`[acceptLinkSpecific](#acceptLinkSpecific(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> vec)`

`void`
`[acceptMove](#acceptMove(java.lang.Object,com.nomagic.magicdraw.ui.browser.Tree,java.awt.Point))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj,
 [Tree](Tree.html) tree,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`
Accepts drag and drop link action
`protected void`
`[acceptMoveSpecific](#acceptMoveSpecific(java.util.List,com.nomagic.magicdraw.ui.browser.Tree,java.awt.Point))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> vec,
 [Tree](Tree.html) tree,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)`

`void`
`[add](#add(javax.swing.tree.MutableTreeNode))([MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html) newChild)`

`protected void`
`[addListeners](#addListeners())()`

`protected void`
`[addListeners](#addListeners(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) data)`
Adds needed listeners to the node element.
`final boolean`
`[canAcceptCopy](#canAcceptCopy(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`

`protected boolean`
`[canAcceptCopySpecific](#canAcceptCopySpecific(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) element)`

`boolean`
`[canAcceptLink](#canAcceptLink(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`

`protected boolean`
`[canAcceptLinkSpecific](#canAcceptLinkSpecific(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) obj)`

`boolean`
`[canAcceptMove](#canAcceptMove(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`

`protected boolean`
`[canAcceptMoveSpecific](#canAcceptMoveSpecific(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) o)`

`boolean`
`[canDelete](#canDelete())()`
Can delete if user object is BaseElement and can be deleted from its parent.
`[Enumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html)`
`[children](#children())()`

`void`
`[clearHiddenOwners](#clearHiddenOwners())()`
Clear all hidden owners.
`void`
`[collapse](#collapse())()`
Collapse this node.
`protected boolean`
`[compactNodes](#compactNodes(boolean))(boolean parentStructureChanged)`
Compact all children.
`void`
`[configure](#configure(com.nomagic.actions.ActionsManager))([ActionsManager](../../../actions/ActionsManager.html) manager)`
Method configure.
`void`
`[configureMultiple](#configureMultiple(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.browser.Node%5B%5D))([ActionsManager](../../../actions/ActionsManager.html) mngr,
 [Node](Node.html)[] node)`
Method to configure actions for context menu of all the provided nodes (array always includes the current node instance too).
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructHiddenOwnerText](#constructHiddenOwnerText())()`
Constructs hidden owners text.
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructText](#constructText())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructTextForSorting](#constructTextForSorting())()`
This method returns the name of the ObjectData (user's object of this node) for sorting purposes
`protected [Node](Node.html)`
`[createNodeFor](#createNodeFor(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`
Creates node for given element.
`protected com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys`
`[createNodeSortKeys](#createNodeSortKeys())()`

`com.dassault_systemes.modeler.foundation.editing.Command`
`[createRemoveCommand](#createRemoveCommand())()`

`com.nomagic.magicdraw.commands.Command`
`[createSpecificRemoveCommand](#createSpecificRemoveCommand())()`
Creates specific command for removing
`void`
`[disposeNode](#disposeNode())()`
Disposes the node - unregisters listeners, removes from nodes map and etc.
`protected <A> [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)>`
`[doUpdateNode](#doUpdateNode(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler))(boolean sortParent,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html),? super A> handler)`

`protected [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[doUpdateNodeSync](#doUpdateNodeSync(boolean))(boolean sortParent)`

`void`
`[enterClicked](#enterClicked(java.awt.AWTEvent))([AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html) event)`
Calls `mouseDoubleClicked` for user object.
`protected com.nomagic.magicdraw.ui.browser.NodeChildrenKeeper`
`[exchangeNodeChildrenKeepers](#exchangeNodeChildrenKeepers())()`

`void`
`[expand](#expand())()`
Expands the tree node.
`void`
`[expand](#expand(boolean))(boolean sortExplicitly)`
Expands the tree node.
`void`
`[expandAsync](#expandAsync())()`
Asynchronously expands the tree node.
`void`
`[expandAsync](#expandAsync(boolean))(boolean sortExplicitly)`
Asynchronously expands the tree node.
`final void`
`[forceUpdateNodeSync](#forceUpdateNodeSync(boolean))(boolean sortParent)`
Marks node as expanded which forces node to be fully updated, and initiates asynchronous node update.
`int[]`
`[getActions](#getActions())()`

`[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`
`[getChildAt](#getChildAt(int))(int index)`

`int`
`[getChildCount](#getChildCount())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Node](Node.html)>`
`[getChildren](#getChildren())()`
Returns list of children.
`com.nomagic.magicdraw.ui.browser.ChildrenOwner`
`[getChildrenOwner](#getChildrenOwner())()`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getCopyOperationTarget](#getCopyOperationTarget())()`

`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getDefaultIcon](#getDefaultIcon())()`
Returns the default icon
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getEditingText](#getEditingText())()`
Returns text which will be edited.
`[BaseElement](../../uml/BaseElement.html)`
`[getElementForCopyAction](#getElementForCopyAction())()`

`[BaseElement](../../uml/BaseElement.html)[]`
`[getElementsForDnd](#getElementsForDnd())()`

`protected [Node](Node.html)`
`[getHiddenNodeFor](#getHiddenNodeFor(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) object)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Node](Node.html)>`
`[getHiddenOwners](#getHiddenOwners())()`

`[Node](Node.html)`
`[getHiddenParent](#getHiddenParent())()`

`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon())()`
Gets the icon for this node.
`int`
`[getIndex](#getIndex(javax.swing.tree.TreeNode))([TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html) aChild)`

`[Node](Node.html)[]`
`[getNodeForObject](#getNodeForObject(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../uml/BaseElement.html) object)`
Returns the tree node which data is the same as given Element.
`protected com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams`
`[getNodeTextParams](#getNodeTextParams())()`

`[Node](Node.html)`
`[getParent](#getParent())()`

`int`
`[getPriorityInOwner](#getPriorityInOwner())()`

`[BaseElement](../../uml/BaseElement.html)[]`
`[getRepresentedElements](#getRepresentedElements())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)>`
`[getRootElements](#getRootElements())()`
Collects root elements of children
`com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys`
`[getSortKeys](#getSortKeys())()`
Returns keys' array for sorting
`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`
This method returns the name of the ObjectData (user's object of this node).
`final com.nomagic.magicdraw.ui.browser.TreeModel`
`[getTreeModel](#getTreeModel())()`
Returns the model of this node.
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getType](#getType())()`
Returns node type
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getUserObject](#getUserObject())()`
Returns user object of this node.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUserObjectBaseElementID](#getUserObjectBaseElementID())()`

`void`
`[insert](#insert(javax.swing.tree.MutableTreeNode,int))([MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html) newChild,
 int childIndex)`

`protected boolean`
`[internalUpdateNodeItself](#internalUpdateNodeItself())()`

`protected boolean`
`[internalUpdateNodeStructure](#internalUpdateNodeStructure())()`
Loads all children for this node.
`boolean`
`[isAutoExpandable](#isAutoExpandable())()`

`boolean`
`[isCanDelete](#isCanDelete())()`

`boolean`
`[isChildrenSortable](#isChildrenSortable())()`

`boolean`
`[isChildrenSortNeeded](#isChildrenSortNeeded())()`

`boolean`
`[isCompactable](#isCompactable())()`

`boolean`
`[isDirty](#isDirty())()`

`boolean`
`[isEditable](#isEditable())()`

`boolean`
`[isEnableUpdateIcon](#isEnableUpdateIcon())()`

`protected boolean`
`[isEventForUpdate](#isEventForUpdate(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`

`boolean`
`[isExpanded](#isExpanded())()`
Checks if component is expanded or not.
`boolean`
`[isForceStructureUpdateOnExpand](#isForceStructureUpdateOnExpand())()`

`boolean`
`[isHidden](#isHidden())()`

`boolean`
`[isInExpandedPath](#isInExpandedPath())()`
Checks if this node is in expanded path.
`boolean`
`[isLoading](#isLoading())()`

`static boolean`
`[isLocked](#isLocked())()`
Returns locked flag
`protected boolean`
`[isNodeLocked](#isNodeLocked(com.nomagic.magicdraw.ui.browser.TreeModel))(com.nomagic.magicdraw.ui.browser.TreeModel treeModel)`

`boolean`
`[isNodeStructureChanged](#isNodeStructureChanged())()`

`boolean`
`[isNodeUpdated](#isNodeUpdated())()`

`protected boolean`
`[isProjectReady](#isProjectReady(com.nomagic.magicdraw.ui.browser.TreeModel))(com.nomagic.magicdraw.ui.browser.TreeModel treeModel)`

`boolean`
`[isRemoveChildrenOnCollapse](#isRemoveChildrenOnCollapse())()`

`boolean`
`[isSpecificElement](#isSpecificElement())()`

`void`
`[mouseDoubleClicked](#mouseDoubleClicked(java.awt.AWTEvent))([AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html) event)`
Calls `onFind` for user object.
`protected void`
`[nodeAdded](#nodeAdded())()`

`protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html),[Node](Node.html)>`
`[prepareUserObjectNodeMap](#prepareUserObjectNodeMap())()`
Return map of user objects mapped to nodes.
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event)`
This method is called when some ObjectData has changed.
`void`
`[remove](#remove())()`
Removes node from parent.
`void`
`[remove](#remove(int))(int childIndex)`

`void`
`[remove](#remove(javax.swing.tree.MutableTreeNode))([MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html) aChild)`

`void`
`[removeAllChildren](#removeAllChildren())()`
Removes all nodes from this node.
`protected boolean`
`[removeAllChildren](#removeAllChildren(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> userObjects)`
Removes nodes from this node if theirs data objects are not in given userObjects.
`protected boolean`
`[removeIllegalNodes](#removeIllegalNodes())()`
Removes nodes from this node these nodes cannot be created with node creator.
`protected void`
`[removeListeners](#removeListeners())()`
Removes propertyChangeListener(node) from Element property change support.
`protected void`
`[removeLoadingNode](#removeLoadingNode())()`

`void`
`[removeRecursively](#removeRecursively())()`
Removes all nodes from this node recursively
`void`
`[removeRecursively](#removeRecursively(int))(int index)`
Removes all nodes from this node recursively
`void`
`[replaceChildren](#replaceChildren(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Node](Node.html)> newChildren)`

`protected [Node](Node.html)`
`[replaceCompactableNode](#replaceCompactableNode(com.nomagic.magicdraw.ui.browser.Node))([Node](Node.html) node)`
Replace given node with its compacted child if needed.
`static long`
`[resetLock](#resetLock(boolean,long))(boolean value,
 long lockingCounter)`
Sets locked flag and decrements locking counter if current locking counter is equal to the one passed as method parameter
`void`
`[setAutoExpandable](#setAutoExpandable(boolean))(boolean autoExpandable)`
Change auto-expandable flag - node will be expanded if it has only one child when expanding parent node.
`void`
`[setCanDelete](#setCanDelete(boolean))(boolean canDelete)`
Method marks node as deletable or not.
`void`
`[setChildrenOwner](#setChildrenOwner(com.nomagic.magicdraw.ui.browser.ChildrenOwner))(com.nomagic.magicdraw.ui.browser.ChildrenOwner owner)`
Set node specific children owner.
`void`
`[setChildrenSortable](#setChildrenSortable(boolean))(boolean childrenSortable)`

`void`
`[setChildrenSortNeeded](#setChildrenSortNeeded(boolean))(boolean childrenSortNeeded)`

`void`
`[setCompactable](#setCompactable(boolean))(boolean compactable)`
Make node compactable.
`void`
`[setDefaultIcon](#setDefaultIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Sets the default icon.
`void`
`[setDirty](#setDirty(boolean))(boolean dirty)`
Sets dirty flag.
`void`
`[setDirtyRecursively](#setDirtyRecursively(boolean))(boolean dirty)`

`void`
`[setEditable](#setEditable(boolean))(boolean editable)`
Method marks node as editable or not.
`void`
`[setEnableUpdateIcon](#setEnableUpdateIcon(boolean))(boolean enableUpdateIcon)`

`protected void`
`[setExpanded](#setExpanded(boolean))(boolean expanded)`
Sets expanded state of this node.
`void`
`[setForceStructureUpdateOnExpand](#setForceStructureUpdateOnExpand(boolean))(boolean value)`

`void`
`[setForceUpdate](#setForceUpdate(boolean))(boolean forceUpdate)`
Set to true to force node update, no matter if text or icon was not changed
`void`
`[setHidden](#setHidden(boolean))(boolean hidden)`
Make node "hidden"
`void`
`[setHiddenParent](#setHiddenParent(com.nomagic.magicdraw.ui.browser.Node))([Node](Node.html) hiddenParent)`
Set hidden parent.
`void`
`[setIcon](#setIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Sets the icon for this node.
`void`
`[setLoading](#setLoading(boolean))(boolean flag)`

`static long`
`[setLocked](#setLocked(boolean))(boolean value)`
Sets locked flag and increases locking counter
`void`
`[setNodeStructureChanged](#setNodeStructureChanged(boolean))(boolean nodeStructureChanged)`

`void`
`[setNodeUpdated](#setNodeUpdated(boolean))(boolean value)`

`void`
`[setPriorityInOwner](#setPriorityInOwner(int))(int priority)`
Set priority in owner for sorting
`void`
`[setRemoveChildrenOnCollapse](#setRemoveChildrenOnCollapse(boolean))(boolean value)`

`void`
`[setSortKeys](#setSortKeys(com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys))(com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys sortKeys)`

`void`
`[setText](#setText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Sets the name of the ObjectData(user's object).
`void`
`[setTreeModel](#setTreeModel(com.nomagic.magicdraw.ui.browser.TreeModel))(com.nomagic.magicdraw.ui.browser.TreeModel model)`
Sets the model for this node.
`void`
`[setUserObject](#setUserObject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
We put WeakReference with given object as user object in order to make things easier for garbage collector.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`

`protected boolean`
`[unCompactNodes](#unCompactNodes())()`
Un-compact all compacted children.
`final void`
`[updateChildren](#updateChildren(com.nomagic.magicdraw.ui.browser.Node,boolean))([Node](Node.html) node,
 boolean sortExplicitly)`
Updates children of this node depending on dirty and expand state.
`final [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<?>`
`[updateChildrenAsync](#updateChildrenAsync(com.nomagic.magicdraw.ui.browser.Node,boolean))([Node](Node.html) node,
 boolean sortExplicitly)`
Asynchronously updates children of this node depending on dirty and expand state.
`final <A> [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<?>`
`[updateChildrenAsync](#updateChildrenAsync(com.nomagic.magicdraw.ui.browser.Node,boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler))([Node](Node.html) node,
 boolean sortExplicitly,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html),? super A> handler)`
Asynchronously updates children of this node depending on dirty and expand state.
`boolean`
`[updateIcon](#updateIcon())()`
Sets icon according to the data.
`boolean`
`[updateNode](#updateNode())()`
Updates node and loads children of the node if it is necessary.
`boolean`
`[updateNode](#updateNode(boolean))(boolean sortParent)`
Updates node and loads children of the node if it is necessary.
`[Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)>`
`[updateNodeAsync](#updateNodeAsync())()`
Asynchronously updates node and loads children of the node if it is necessary.
`final [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)>`
`[updateNodeAsync](#updateNodeAsync(boolean))(boolean sortParent)`
Asynchronously updates node and loads children of the node if it is necessary.
`final <A> void`
`[updateNodeAsync](#updateNodeAsync(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler))(boolean sortParent,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html),? super A> handler)`
Asynchronously updates node and loads children of the node if it is necessary.
`final <A> void`
`[updateNodeAsync](#updateNodeAsync(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler))(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html),? super A> handler)`
Asynchronously updates node and loads children of the node if it is necessary.
`final boolean`
`[updateNodeItself](#updateNodeItself())()`
Updates text and icon of the node.
`protected boolean`
`[updateNodeStructure](#updateNodeStructure(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> objects)`
This method reloads children from given user object collection.
`void`
`[updateNodeStructureOfChildInExpandedPath](#updateNodeStructureOfChildInExpandedPath(com.nomagic.magicdraw.ui.browser.Node))([Node](Node.html) node)`

`final boolean`
`[updateNodeStructureWithRetry](#updateNodeStructureWithRetry())()`
Tries to load all children of this node.
`final [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[updateNodeSync](#updateNodeSync(boolean))(boolean sortParent)`
Synchronously updates node and loads children of the node if it is necessary.
`protected void`
`[updateSortKeys](#updateSortKeys(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`void`
`[waitForUpdateNodeCompletions](#waitForUpdateNodeCompletions())()`
Wait for pending `updateNodeAsync()` completions
Methods inherited from class javax.swing.tree.[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)
`[breadthFirstEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#breadthFirstEnumeration()), [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#clone()), [depthFirstEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#depthFirstEnumeration()), [getAllowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getAllowsChildren()), [getChildAfter](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAfter(javax.swing.tree.TreeNode)), [getChildBefore](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildBefore(javax.swing.tree.TreeNode)), [getDepth](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getDepth()), [getFirstChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstChild()), [getFirstLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getFirstLeaf()), [getLastChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastChild()), [getLastLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLastLeaf()), [getLeafCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLeafCount()), [getLevel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getLevel()), [getNextLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextLeaf()), [getNextNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextNode()), [getNextSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getNextSibling()), [getPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPath()), [getPathToRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPathToRoot(javax.swing.tree.TreeNode,int)), [getPreviousLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousLeaf()), [getPreviousNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousNode()), [getPreviousSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getPreviousSibling()), [getRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getRoot()), [getSharedAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSharedAncestor(javax.swing.tree.DefaultMutableTreeNode)), [getSiblingCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getSiblingCount()), [getUserObjectPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObjectPath()), [isLeaf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isLeaf()), [isNodeAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeAncestor(javax.swing.tree.TreeNode)), [isNodeChild](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeChild(javax.swing.tree.TreeNode)), [isNodeDescendant](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeDescendant(javax.swing.tree.DefaultMutableTreeNode)), [isNodeRelated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeRelated(javax.swing.tree.DefaultMutableTreeNode)), [isNodeSibling](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isNodeSibling(javax.swing.tree.TreeNode)), [isRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#isRoot()), [pathFromAncestorEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#pathFromAncestorEnumeration(javax.swing.tree.TreeNode)), [postorderEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#postorderEnumeration()), [preorderEnumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#preorderEnumeration()), [removeFromParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeFromParent()), [setAllowsChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setAllowsChildren(boolean)), [setParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setParent(javax.swing.tree.MutableTreeNode))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
MAX_NODE_UPDATE_RETRY_COUNT
public static final int MAX_NODE_UPDATE_RETRY_COUNT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.browser.Node.MAX_NODE_UPDATE_RETRY_COUNT)
ignoreRootCheck
protected volatile boolean ignoreRootCheck
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Node
public Node(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) element,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Node
public Node(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) element,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) defaultIcon)
Node
public Node(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) element,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) defaultIcon,
 com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams nodeTextParams)
 ============ METHOD DETAIL ========== 
Method Details
isLocked
public static boolean isLocked()
Returns locked flag
Returns:
true if it is locked, else false.
setLocked
public static long setLocked(boolean value)
Sets locked flag and increases locking counter
Parameters:
`value` - lock value
Returns:
locking counter
resetLock
public static long resetLock(boolean value,
 long lockingCounter)
Sets locked flag and decrements locking counter if current locking counter is equal to the one passed as method parameter
Parameters:
`value` - lock value
`lockingCounter` - locking counter
Returns:
locking counter
addListeners
protected void addListeners([BaseElement](../../uml/BaseElement.html) data)
Adds needed listeners to the node element.
Parameters:
`data` - instance of [`BaseElement`](../../uml/BaseElement.html)
addListeners
protected void addListeners()
getChildren
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Node](Node.html)> getChildren()
Returns list of children.
Returns:
list of [`Node`](Node.html)
getUserObjectBaseElementID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUserObjectBaseElementID()
getChildCount
public int getChildCount()
Specified by:
`[getChildCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getChildCount())` in interface `[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`
Overrides:
`[getChildCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildCount())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
getChildAt
public [TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html) getChildAt(int index)
Specified by:
`[getChildAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getChildAt(int))` in interface `[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`
Overrides:
`[getChildAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAt(int))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
children
public [Enumeration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html) children()
Specified by:
`[children](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#children())` in interface `[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`
Overrides:
`[children](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
getIndex
public int getIndex([TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html) aChild)
Specified by:
`[getIndex](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getIndex(javax.swing.tree.TreeNode))` in interface `[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`
Overrides:
`[getIndex](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getIndex(javax.swing.tree.TreeNode))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
insert
public void insert([MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html) newChild,
 int childIndex)
Specified by:
`[insert](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#insert(javax.swing.tree.MutableTreeNode,int))` in interface `[MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html)`
Overrides:
`[insert](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#insert(javax.swing.tree.MutableTreeNode,int))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
remove
public void remove(int childIndex)
Specified by:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#remove(int))` in interface `[MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html)`
Overrides:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(int))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
remove
public void remove([MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html) aChild)
Specified by:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#remove(javax.swing.tree.MutableTreeNode))` in interface `[MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html)`
Overrides:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(javax.swing.tree.MutableTreeNode))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
replaceChildren
public void replaceChildren([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Node](Node.html)> newChildren)
exchangeNodeChildrenKeepers
@CheckForNullprotected com.nomagic.magicdraw.ui.browser.NodeChildrenKeeper exchangeNodeChildrenKeepers()
getUserObject
@CheckForNull
@OpenApipublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getUserObject()
Returns user object of this node.
Overrides:
`[getUserObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getUserObject())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
Returns:
user object(some Element).
setUserObject
public void setUserObject(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
We put WeakReference with given object as user object in order to make things easier for garbage collector.
Specified by:
`[setUserObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#setUserObject(java.lang.Object))` in interface `[MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html)`
Overrides:
`[setUserObject](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setUserObject(java.lang.Object))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
getDefaultIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getDefaultIcon()
Returns the default icon
Returns:
the default icon.
setDefaultIcon
public void setDefaultIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Sets the default icon.
Parameters:
`icon` - the default icon.
getIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon()
Gets the icon for this node.
Returns:
the icon of this node.
setIcon
public void setIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Sets the icon for this node.
 If object is not editable, sets gray icon.
Parameters:
`icon` - the new icon.
updateIcon
public boolean updateIcon()
Sets icon according to the data.
Returns:
true if icon was changed
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) event)
This method is called when some ObjectData has changed.
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Parameters:
`event` - the property changed event.
isEventForUpdate
protected boolean isEventForUpdate([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
getText
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getText()
This method returns the name of the ObjectData (user's object of this node).
Returns:
the name of the ObjectData
setText
public void setText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Sets the name of the ObjectData(user's object).
 This method is called after the node's text editing.
Parameters:
`text` - the new node's text.
updateSortKeys
protected void updateSortKeys([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
internalUpdateNodeStructure
protected boolean internalUpdateNodeStructure()
Loads all children for this node.
Returns:
true if structure was changed
updateNodeStructureWithRetry
public final boolean updateNodeStructureWithRetry()
Tries to load all children of this node. In case of exception due to model changes will try multiple times
Returns:
true if structure was changed
getChildrenOwner
public com.nomagic.magicdraw.ui.browser.ChildrenOwner getChildrenOwner()
Returns:
children owner of the node. If node does not have his children owner, children owner from tree model is used
setChildrenOwner
public void setChildrenOwner(com.nomagic.magicdraw.ui.browser.ChildrenOwner owner)
Set node specific children owner.
Parameters:
`owner` - owner
getTreeModel
@CheckForNullpublic final com.nomagic.magicdraw.ui.browser.TreeModel getTreeModel()
Returns the model of this node.
Returns:
the model of this node.
setTreeModel
public void setTreeModel(com.nomagic.magicdraw.ui.browser.TreeModel model)
Sets the model for this node.
Parameters:
`model` - the TreeModel.
updateNodeStructure
protected boolean updateNodeStructure(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> objects)
This method reloads children from given user object collection.
 If children already exists, sets only text for the node.
Parameters:
`objects` - the given children
Returns:
true if node structure was changed
updateNodeStructureOfChildInExpandedPath
public void updateNodeStructureOfChildInExpandedPath([Node](Node.html) node)
unCompactNodes
protected boolean unCompactNodes()
Un-compact all compacted children.
Returns:
true if at least one child was un-compacted
compactNodes
protected boolean compactNodes(boolean parentStructureChanged)
Compact all children.
Parameters:
`parentStructureChanged` - was parent (current) node structure changed
Returns:
true if at least one child was compacted
replaceCompactableNode
@CheckForNullprotected [Node](Node.html) replaceCompactableNode([Node](Node.html) node)
Replace given node with its compacted child if needed.
Parameters:
`node` - given node
Returns:
node replaced node or null if no replacement
updateNodeItself
public final boolean updateNodeItself()
Updates text and icon of the node.
Returns:
true if text or icon was changed.
internalUpdateNodeItself
protected boolean internalUpdateNodeItself()
setForceUpdate
public void setForceUpdate(boolean forceUpdate)
Set to true to force node update, no matter if text or icon was not changed
Parameters:
`forceUpdate` - flag to indicate update status
createNodeFor
@CheckForNullprotected [Node](Node.html) createNodeFor([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Creates node for given element. Uses node creator from tree model.
Parameters:
`obj` - the given object.
Returns:
the created node or null
getRootElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../../uml/BaseElement.html)> getRootElements()
Collects root elements of children
Returns:
collection of root elements of children
getNodeForObject
@CheckForNullpublic [Node](Node.html)[] getNodeForObject([BaseElement](../../uml/BaseElement.html) object)
Returns the tree node which data is the same as given Element.
 This method is used to determine if node with given Element as
 data object exists.
Parameters:
`object` - the given Element.
Returns:
the node which data object is the same as given object
 or null such node is not found.
getHiddenNodeFor
@CheckForNullprotected [Node](Node.html) getHiddenNodeFor(@CheckForNull
 [BaseElement](../../uml/BaseElement.html) object)
prepareUserObjectNodeMap
protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html),[Node](Node.html)> prepareUserObjectNodeMap()
Return map of user objects mapped to nodes.
Returns:
map of user objects mapped to nodes.
mouseDoubleClicked
public void mouseDoubleClicked(@CheckForNull
 [AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html) event)
Calls `onFind` for user object.
 This method is called when user double clicks with mouse on the node.
Parameters:
`event` - click event
enterClicked
public void enterClicked([AWTEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html) event)
Calls `mouseDoubleClicked` for user object.
 This method is called when user double clicks with mouse on the node.
Parameters:
`event` - click event
removeListeners
protected void removeListeners()
Removes propertyChangeListener(node) from Element property change support.
remove
public void remove()
Removes node from parent.
disposeNode
public void disposeNode()
Disposes the node - unregisters listeners, removes from nodes map and etc.
removeAllChildren
protected boolean removeAllChildren([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> userObjects)
Removes nodes from this node if theirs data objects are not in given userObjects.
Parameters:
`userObjects` - the given userObjects of the DTObjects.
Returns:
true, if at least one node was removed
removeIllegalNodes
protected boolean removeIllegalNodes()
Removes nodes from this node these nodes cannot be created with node creator.
Returns:
true, if at least one node was removed
removeAllChildren
public void removeAllChildren()
Removes all nodes from this node.
Overrides:
`[removeAllChildren](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeAllChildren())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
removeRecursively
public void removeRecursively()
Removes all nodes from this node recursively
removeRecursively
public void removeRecursively(int index)
Removes all nodes from this node recursively
Parameters:
`index` - of node which should be deleted.
expand
public void expand(boolean sortExplicitly)
Expands the tree node. If children of the node are not loaded, load them.
Parameters:
`sortExplicitly` - `true`, if node children must be sorted explicitly.
expand
public void expand()
Expands the tree node. If children of the node are not loaded, load them.
expandAsync
public void expandAsync(boolean sortExplicitly)
Asynchronously expands the tree node. If children of the node are not loaded, load them.
Parameters:
`sortExplicitly` - `true`, if node children must be sorted explicitly.
expandAsync
public void expandAsync()
Asynchronously expands the tree node. If children of the node are not loaded, load them.
updateChildren
public final void updateChildren([Node](Node.html) node,
 boolean sortExplicitly)
Updates children of this node depending on dirty and expand state.
Parameters:
`node` - the given node.
`sortExplicitly` - if `true` sort children explicitly
updateChildrenAsync
public final [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<?> updateChildrenAsync([Node](Node.html) node,
 boolean sortExplicitly)
Asynchronously updates children of this node depending on dirty and expand state.
Parameters:
`node` - the given node.
`sortExplicitly` - if `true` sort children explicitly
Returns:
A `Future` object representing the pending operation
updateChildrenAsync
public final <A> [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<?> updateChildrenAsync([Node](Node.html) node,
 boolean sortExplicitly,
 @CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html),? super A> handler)
Asynchronously updates children of this node depending on dirty and expand state.
Type Parameters:
`A` - The type of the object attached to the completion handler
Parameters:
`node` - the given node.
`sortExplicitly` - if `true` sort children explicitly
`attachment` - The object to attach to the update operation; can be `null`
`handler` - The handler for consuming the operation result, which is `true`, if node
 itself was changed(not children).
collapse
public void collapse()
Collapse this node.
isInExpandedPath
public boolean isInExpandedPath()
Checks if this node is in expanded path.
Returns:
true, is this node is in expanded path(visible to user).
acceptLink
public final void acceptLink([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Accepts drag and drop link action
Parameters:
`obj` - - moved object
acceptLinkSpecific
protected void acceptLinkSpecific([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> vec)
canAcceptLink
public boolean canAcceptLink([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
canAcceptLinkSpecific
protected boolean canAcceptLinkSpecific([BaseElement](../../uml/BaseElement.html) obj)
acceptMove
public void acceptMove([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj,
 [Tree](Tree.html) tree,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
Accepts drag and drop link action
Parameters:
`obj` - moved object
acceptMoveSpecific
protected void acceptMoveSpecific([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> vec,
 [Tree](Tree.html) tree,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) location)
canAcceptMove
public boolean canAcceptMove([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
canAcceptMoveSpecific
protected boolean canAcceptMoveSpecific([BaseElement](../../uml/BaseElement.html) o)
acceptCopy
public void acceptCopy([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Accepts drag and drop link action
Parameters:
`obj` - moved object
acceptCopySpecific
protected void acceptCopySpecific([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> elements)
getCopyOperationTarget
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getCopyOperationTarget()
canAcceptCopy
public final boolean canAcceptCopy([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
canAcceptCopySpecific
protected boolean canAcceptCopySpecific([BaseElement](../../uml/BaseElement.html) element)
getSortKeys
public com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys getSortKeys()
Returns keys' array for sorting
Returns:
instance of `Node.NodeSortKeys`
setSortKeys
public void setSortKeys(com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys sortKeys)
createNodeSortKeys
protected com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys createNodeSortKeys()
getType
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getType()
Returns node type
Returns:
returns node type
updateNode
public boolean updateNode()
Updates node and loads children of the node if it is necessary.
Returns:
`true`, if node itself was changed(not children).
updateNode
public boolean updateNode(boolean sortParent)
Updates node and loads children of the node if it is necessary.
Parameters:
`sortParent` - if `true` - parent node will be sorted if this node changes text.
Returns:
`true`, if node itself was changed(not children).
updateNodeAsync
public [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> updateNodeAsync()
Asynchronously updates node and loads children of the node if it is necessary.
Returns:
`Future` which results to `true`, if node itself was
 changed(not children).
updateNodeAsync
public final <A> void updateNodeAsync(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html),? super A> handler)
Asynchronously updates node and loads children of the node if it is necessary.
Type Parameters:
`A` - The type of the object attached to the completion handler
Parameters:
`attachment` - The object to attach to the update operation; can be `null`
`handler` - The handler for consuming the operation result, which is `true`, if node
 itself was changed(not children).
updateNodeAsync
public final [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> updateNodeAsync(boolean sortParent)
Asynchronously updates node and loads children of the node if it is necessary.
Parameters:
`sortParent` - if `true` - parent node will be sorted if this node changes text.
Returns:
`Future` which results to `true`, if node itself was changed(not children).
updateNodeAsync
public final <A> void updateNodeAsync(boolean sortParent,
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html),? super A> handler)
Asynchronously updates node and loads children of the node if it is necessary.
Type Parameters:
`A` - The type of the object attached to the completion handler
Parameters:
`sortParent` - if `true` - parent node will be sorted if this node changes text.
`attachment` - The object to attach to the update operation; can be `null`
`handler` - The handler for consuming the result
forceUpdateNodeSync
public final void forceUpdateNodeSync(boolean sortParent)
Marks node as expanded which forces node to be fully updated, and initiates asynchronous node update.
Parameters:
`sortParent` - if `true` - parent node will be sorted if this node changes text.
doUpdateNode
protected <A> [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> doUpdateNode(boolean sortParent,
 @CheckForNull
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html),? super A> handler)
isProjectReady
protected boolean isProjectReady(com.nomagic.magicdraw.ui.browser.TreeModel treeModel)
isNodeLocked
protected boolean isNodeLocked(com.nomagic.magicdraw.ui.browser.TreeModel treeModel)
updateNodeSync
public final [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) updateNodeSync(boolean sortParent)
Synchronously updates node and loads children of the node if it is necessary.
Parameters:
`sortParent` - if `true` - parent node will be sorted if this node changes text.
Returns:
`true`, if node itself was changed(not children).
doUpdateNodeSync
protected [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) doUpdateNodeSync(boolean sortParent)
waitForUpdateNodeCompletions
public void waitForUpdateNodeCompletions()
Wait for pending `updateNodeAsync()` completions
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#toString())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
isExpanded
public boolean isExpanded()
Description copied from interface: `com.nomagic.magicdraw.ui.browser.Expandable`
Checks if component is expanded or not.
Specified by:
`isExpanded` in interface `com.nomagic.magicdraw.ui.browser.Expandable`
Returns:
`true` when component is expanded, `false` - otherwise
setExpanded
protected void setExpanded(boolean expanded)
Sets expanded state of this node.
Parameters:
`expanded` - true if node is expanded.
isForceStructureUpdateOnExpand
public boolean isForceStructureUpdateOnExpand()
setForceStructureUpdateOnExpand
public void setForceStructureUpdateOnExpand(boolean value)
isRemoveChildrenOnCollapse
public boolean isRemoveChildrenOnCollapse()
setRemoveChildrenOnCollapse
public void setRemoveChildrenOnCollapse(boolean value)
getNodeTextParams
protected com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams getNodeTextParams()
constructText
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructText()
constructTextForSorting
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructTextForSorting()
This method returns the name of the ObjectData (user's object of this node) for sorting purposes
Returns:
the name of the ObjectData for sorting purposes
createRemoveCommand
@CheckForNullpublic com.dassault_systemes.modeler.foundation.editing.Command createRemoveCommand()
getParent
@CheckForNullpublic [Node](Node.html) getParent()
Specified by:
`[getParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getParent())` in interface `[TreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html)`
Overrides:
`[getParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getParent())` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
setDirtyRecursively
public void setDirtyRecursively(boolean dirty)
isDirty
public boolean isDirty()
setDirty
public void setDirty(boolean dirty)
Sets dirty flag.
Parameters:
`dirty` - is dirty?
getActions
public int[] getActions()
canDelete
public boolean canDelete()
Can delete if user object is BaseElement and can be deleted from its parent.
Returns:
true if can delete, else false.
getEditingText
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getEditingText()
Returns text which will be edited.
 Since some nodes can display one text, but should be edited with other text this method return text to be edited.
Returns:
text to edit.
isEditable
public boolean isEditable()
setEditable
public void setEditable(boolean editable)
Method marks node as editable or not.
Parameters:
`editable` - is editable?
See Also:
[`isEditable()`](#isEditable())
isLoading
public boolean isLoading()
setLoading
public void setLoading(boolean flag)
configure
public void configure([ActionsManager](../../../actions/ActionsManager.html) manager)
Method configure.
Parameters:
`manager` - actions manager to be configured for this node.
configureMultiple
public void configureMultiple([ActionsManager](../../../actions/ActionsManager.html) mngr,
 [Node](Node.html)[] node)
Method to configure actions for context menu of all the provided nodes (array always includes the current node instance too).
 This method gets called only once for all nodes of the same class type, so each node instance in the provided array should be regarded.
Parameters:
`mngr` - actions manager to be configured for this node.
`node` - array of [`Node`](Node.html) for which actions are configured.
getElementsForDnd
@CheckForNullpublic [BaseElement](../../uml/BaseElement.html)[] getElementsForDnd()
getRepresentedElements
@CheckForNullpublic [BaseElement](../../uml/BaseElement.html)[] getRepresentedElements()
getElementForCopyAction
@CheckForNullpublic [BaseElement](../../uml/BaseElement.html) getElementForCopyAction()
isChildrenSortable
public boolean isChildrenSortable()
setChildrenSortable
public void setChildrenSortable(boolean childrenSortable)
nodeAdded
protected void nodeAdded()
add
public void add([MutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html) newChild)
Overrides:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#add(javax.swing.tree.MutableTreeNode))` in class `[DefaultMutableTreeNode](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html)`
isCanDelete
public boolean isCanDelete()
setCanDelete
public void setCanDelete(boolean canDelete)
Method marks node as deletable or not.
Parameters:
`canDelete` - can delete?
See Also:
[`canDelete()`](#canDelete())
isEnableUpdateIcon
public boolean isEnableUpdateIcon()
Returns:
Returns the enableUpdateIcon.
setEnableUpdateIcon
public void setEnableUpdateIcon(boolean enableUpdateIcon)
isChildrenSortNeeded
public boolean isChildrenSortNeeded()
setChildrenSortNeeded
public void setChildrenSortNeeded(boolean childrenSortNeeded)
isCompactable
public boolean isCompactable()
Returns:
true is node is compactable
setCompactable
public void setCompactable(boolean compactable)
Make node compactable.
Parameters:
`compactable` - value
isNodeStructureChanged
public boolean isNodeStructureChanged()
setNodeStructureChanged
public void setNodeStructureChanged(boolean nodeStructureChanged)
isHidden
public boolean isHidden()
Returns:
true if node is hidden
setHidden
public void setHidden(boolean hidden)
Make node "hidden"
Parameters:
`hidden` - hidden value
getHiddenParent
@CheckForNullpublic [Node](Node.html) getHiddenParent()
Returns:
hidden parent
setHiddenParent
public void setHiddenParent(@CheckForNull
 [Node](Node.html) hiddenParent)
Set hidden parent. Parent is used if node is "hidden", because normal parent is null in such case.
Parameters:
`hiddenParent` - hidden parent
clearHiddenOwners
public void clearHiddenOwners()
Clear all hidden owners. Hidden nodes becomes not hidden.
getHiddenOwners
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Node](Node.html)> getHiddenOwners()
Returns:
hidden owners or empty list
constructHiddenOwnerText
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructHiddenOwnerText()
Constructs hidden owners text.
Returns:
hidden owner text
isAutoExpandable
public boolean isAutoExpandable()
Returns:
auto-expandable node flag
setAutoExpandable
public void setAutoExpandable(boolean autoExpandable)
Change auto-expandable flag - node will be expanded if it has only one child when expanding parent node.
Parameters:
`autoExpandable` - true if node is auto-expandable
removeLoadingNode
protected void removeLoadingNode()
isNodeUpdated
public boolean isNodeUpdated()
setNodeUpdated
public void setNodeUpdated(boolean value)
getPriorityInOwner
public int getPriorityInOwner()
Returns:
priority in owner for sorting
setPriorityInOwner
public void setPriorityInOwner(int priority)
Set priority in owner for sorting
Parameters:
`priority` - priority
createSpecificRemoveCommand
@CheckForNullpublic com.nomagic.magicdraw.commands.Command createSpecificRemoveCommand()
Creates specific command for removing
Returns:
specific command for node removing
isSpecificElement
public boolean isSpecificElement()
Returns:
true if element is specific

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
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ignoreRootCheck">ignoreRootCheck</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MAX_NODE_UPDATE_RETRY_COUNT">MAX_NODE_UPDATE_RETRY_COUNT</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.tree.DefaultMutableTreeNode">Fields inherited from class javax.swing.tree.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#allowsChildren" title="class or interface in javax.swing.tree">allowsChildren</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#EMPTY_ENUMERATION" title="class or interface in javax.swing.tree">EMPTY_ENUMERATION</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#parent" title="class or interface in javax.swing.tree">parent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#userObject" title="class or interface in javax.swing.tree">userObject</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon)">Node</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon,javax.swing.Icon)">Node</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> defaultIcon)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon,javax.swing.Icon,com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams)">Node</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> defaultIcon,
 com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams nodeTextParams)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptCopy(java.lang.Object)">acceptCopy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts drag and drop link action</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptCopySpecific(java.util.List)">acceptCopySpecific</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptLink(java.lang.Object)">acceptLink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts drag and drop link action</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptLinkSpecific(java.util.List)">acceptLinkSpecific</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; vec)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptMove(java.lang.Object,com.nomagic.magicdraw.ui.browser.Tree,java.awt.Point)">acceptMove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj,
 <a href="Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Accepts drag and drop link action</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#acceptMoveSpecific(java.util.List,com.nomagic.magicdraw.ui.browser.Tree,java.awt.Point)">acceptMoveSpecific</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; vec,
 <a href="Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(javax.swing.tree.MutableTreeNode)">add</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a> newChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addListeners()">addListeners</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addListeners(com.nomagic.magicdraw.uml.BaseElement)">addListeners</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> data)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds needed listeners to the node element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAcceptCopy(java.lang.Object)">canAcceptCopy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAcceptCopySpecific(com.nomagic.magicdraw.uml.BaseElement)">canAcceptCopySpecific</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAcceptLink(java.lang.Object)">canAcceptLink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAcceptLinkSpecific(com.nomagic.magicdraw.uml.BaseElement)">canAcceptLinkSpecific</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAcceptMove(java.lang.Object)">canAcceptMove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canAcceptMoveSpecific(com.nomagic.magicdraw.uml.BaseElement)">canAcceptMoveSpecific</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canDelete()">canDelete</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Can delete if user object is BaseElement and can be deleted from its parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html" title="class or interface in java.util">Enumeration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#children()">children</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearHiddenOwners()">clearHiddenOwners</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear all hidden owners.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collapse()">collapse</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collapse this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compactNodes(boolean)">compactNodes</a><wbr/>(boolean parentStructureChanged)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compact all children.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configure(com.nomagic.actions.ActionsManager)">configure</a><wbr/>(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method configure.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureMultiple(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.browser.Node%5B%5D)">configureMultiple</a><wbr/>(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> mngr,
 <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method to configure actions for context menu of all the provided nodes (array always includes the current node instance too).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#constructHiddenOwnerText()">constructHiddenOwnerText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Constructs hidden owners text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#constructText()">constructText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#constructTextForSorting()">constructTextForSorting</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method returns the name of the ObjectData (user's object of this node) for sorting purposes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNodeFor(java.lang.Object)">createNodeFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates node for given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createNodeSortKeys()">createNodeSortKeys</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.foundation.editing.Command</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRemoveCommand()">createRemoveCommand</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.commands.Command</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSpecificRemoveCommand()">createSpecificRemoveCommand</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates specific command for removing</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeNode()">disposeNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disposes the node - unregisters listeners, removes from nodes map and etc.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected &lt;A&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doUpdateNode(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">doUpdateNode</a><wbr/>(boolean sortParent,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>,<wbr/>? super A&gt; handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doUpdateNodeSync(boolean)">doUpdateNodeSync</a><wbr/>(boolean sortParent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#enterClicked(java.awt.AWTEvent)">enterClicked</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls <code>mouseDoubleClicked</code> for user object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.ui.browser.NodeChildrenKeeper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exchangeNodeChildrenKeepers()">exchangeNodeChildrenKeepers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#expand()">expand</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Expands the tree node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#expand(boolean)">expand</a><wbr/>(boolean sortExplicitly)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Expands the tree node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#expandAsync()">expandAsync</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously expands the tree node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#expandAsync(boolean)">expandAsync</a><wbr/>(boolean sortExplicitly)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously expands the tree node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forceUpdateNodeSync(boolean)">forceUpdateNodeSync</a><wbr/>(boolean sortParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks node as expanded which forces node to be fully updated, and initiates asynchronous node update.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActions()">getActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildAt(int)">getChildAt</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildCount()">getChildCount</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildren()">getChildren</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of children.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.browser.ChildrenOwner</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildrenOwner()">getChildrenOwner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCopyOperationTarget()">getCopyOperationTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultIcon()">getDefaultIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the default icon</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEditingText()">getEditingText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns text which will be edited.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementForCopyAction()">getElementForCopyAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsForDnd()">getElementsForDnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHiddenNodeFor(com.nomagic.magicdraw.uml.BaseElement)">getHiddenNodeFor</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHiddenOwners()">getHiddenOwners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHiddenParent()">getHiddenParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the icon for this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIndex(javax.swing.tree.TreeNode)">getIndex</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a> aChild)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNodeForObject(com.nomagic.magicdraw.uml.BaseElement)">getNodeForObject</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the tree node which data is the same as given Element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNodeTextParams()">getNodeTextParams</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPriorityInOwner()">getPriorityInOwner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentedElements()">getRepresentedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootElements()">getRootElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects root elements of children</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortKeys()">getSortKeys</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns keys' array for sorting</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method returns the name of the ObjectData (user's object of this node).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final com.nomagic.magicdraw.ui.browser.TreeModel</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTreeModel()">getTreeModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns  the model of this  node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns node type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUserObject()">getUserObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns user object of this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUserObjectBaseElementID()">getUserObjectBaseElementID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#insert(javax.swing.tree.MutableTreeNode,int)">insert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a> newChild,
 int childIndex)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalUpdateNodeItself()">internalUpdateNodeItself</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalUpdateNodeStructure()">internalUpdateNodeStructure</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads all children for this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoExpandable()">isAutoExpandable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCanDelete()">isCanDelete</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChildrenSortable()">isChildrenSortable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChildrenSortNeeded()">isChildrenSortNeeded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCompactable()">isCompactable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirty()">isDirty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnableUpdateIcon()">isEnableUpdateIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEventForUpdate(java.beans.PropertyChangeEvent)">isEventForUpdate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExpanded()">isExpanded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if component is expanded or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isForceStructureUpdateOnExpand()">isForceStructureUpdateOnExpand</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHidden()">isHidden</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInExpandedPath()">isInExpandedPath</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if this node is in expanded path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoading()">isLoading</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLocked()">isLocked</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns locked flag</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNodeLocked(com.nomagic.magicdraw.ui.browser.TreeModel)">isNodeLocked</a><wbr/>(com.nomagic.magicdraw.ui.browser.TreeModel treeModel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNodeStructureChanged()">isNodeStructureChanged</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNodeUpdated()">isNodeUpdated</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isProjectReady(com.nomagic.magicdraw.ui.browser.TreeModel)">isProjectReady</a><wbr/>(com.nomagic.magicdraw.ui.browser.TreeModel treeModel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemoveChildrenOnCollapse()">isRemoveChildrenOnCollapse</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSpecificElement()">isSpecificElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mouseDoubleClicked(java.awt.AWTEvent)">mouseDoubleClicked</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls <code>onFind</code> for user object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#nodeAdded()">nodeAdded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>,<wbr/><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepareUserObjectNodeMap()">prepareUserObjectNodeMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return map of user objects mapped to nodes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is called when some ObjectData has changed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove()">remove</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes node from parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(int)">remove</a><wbr/>(int childIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(javax.swing.tree.MutableTreeNode)">remove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a> aChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllChildren()">removeAllChildren</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all nodes from this node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllChildren(java.util.Collection)">removeAllChildren</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; userObjects)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes nodes from this node if theirs data objects are not in given userObjects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeIllegalNodes()">removeIllegalNodes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes nodes from this node these nodes cannot be created with node creator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeListeners()">removeListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes propertyChangeListener(node) from Element property change support.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeLoadingNode()">removeLoadingNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRecursively()">removeRecursively</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all nodes from this node recursively</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeRecursively(int)">removeRecursively</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all nodes from this node recursively</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceChildren(java.util.List)">replaceChildren</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>&gt; newChildren)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceCompactableNode(com.nomagic.magicdraw.ui.browser.Node)">replaceCompactableNode</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replace given node with its compacted child if needed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#resetLock(boolean,long)">resetLock</a><wbr/>(boolean value,
 long lockingCounter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets locked flag and decrements locking counter if current locking counter is equal to the one passed as method parameter</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoExpandable(boolean)">setAutoExpandable</a><wbr/>(boolean autoExpandable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Change auto-expandable flag - node will be expanded if it has only one child when expanding parent node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCanDelete(boolean)">setCanDelete</a><wbr/>(boolean canDelete)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method marks node as deletable or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChildrenOwner(com.nomagic.magicdraw.ui.browser.ChildrenOwner)">setChildrenOwner</a><wbr/>(com.nomagic.magicdraw.ui.browser.ChildrenOwner owner)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set node specific children owner.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChildrenSortable(boolean)">setChildrenSortable</a><wbr/>(boolean childrenSortable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChildrenSortNeeded(boolean)">setChildrenSortNeeded</a><wbr/>(boolean childrenSortNeeded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCompactable(boolean)">setCompactable</a><wbr/>(boolean compactable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Make node compactable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultIcon(javax.swing.Icon)">setDefaultIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the default icon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirty(boolean)">setDirty</a><wbr/>(boolean dirty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets dirty flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirtyRecursively(boolean)">setDirtyRecursively</a><wbr/>(boolean dirty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEditable(boolean)">setEditable</a><wbr/>(boolean editable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method marks node as editable or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnableUpdateIcon(boolean)">setEnableUpdateIcon</a><wbr/>(boolean enableUpdateIcon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExpanded(boolean)">setExpanded</a><wbr/>(boolean expanded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets expanded state of this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setForceStructureUpdateOnExpand(boolean)">setForceStructureUpdateOnExpand</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setForceUpdate(boolean)">setForceUpdate</a><wbr/>(boolean forceUpdate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set to true to force node update, no matter if text or icon was not changed</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHidden(boolean)">setHidden</a><wbr/>(boolean hidden)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Make node "hidden"</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHiddenParent(com.nomagic.magicdraw.ui.browser.Node)">setHiddenParent</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> hiddenParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set hidden parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIcon(javax.swing.Icon)">setIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the icon for this node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoading(boolean)">setLoading</a><wbr/>(boolean flag)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocked(boolean)">setLocked</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets locked flag and increases locking counter</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNodeStructureChanged(boolean)">setNodeStructureChanged</a><wbr/>(boolean nodeStructureChanged)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNodeUpdated(boolean)">setNodeUpdated</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPriorityInOwner(int)">setPriorityInOwner</a><wbr/>(int priority)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set priority in owner for sorting</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRemoveChildrenOnCollapse(boolean)">setRemoveChildrenOnCollapse</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSortKeys(com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys)">setSortKeys</a><wbr/>(com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys sortKeys)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(java.lang.String)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the name of the ObjectData(user's object).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTreeModel(com.nomagic.magicdraw.ui.browser.TreeModel)">setTreeModel</a><wbr/>(com.nomagic.magicdraw.ui.browser.TreeModel model)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the model for this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUserObject(java.lang.Object)">setUserObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">We put WeakReference with given object as user object in order to make things easier for garbage collector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unCompactNodes()">unCompactNodes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Un-compact all compacted children.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateChildren(com.nomagic.magicdraw.ui.browser.Node,boolean)">updateChildren</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 boolean sortExplicitly)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates children of this node depending on dirty and expand state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateChildrenAsync(com.nomagic.magicdraw.ui.browser.Node,boolean)">updateChildrenAsync</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 boolean sortExplicitly)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously updates children of this node depending on dirty and expand state.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final &lt;A&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateChildrenAsync(com.nomagic.magicdraw.ui.browser.Node,boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">updateChildrenAsync</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 boolean sortExplicitly,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>,<wbr/>? super A&gt; handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously updates children of this node depending on dirty and expand state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateIcon()">updateIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets icon according to the data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNode()">updateNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates node and loads children of the node if it is necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNode(boolean)">updateNode</a><wbr/>(boolean sortParent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates node and loads children of the node if it is necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeAsync()">updateNodeAsync</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously updates node and loads children of the node if it is necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeAsync(boolean)">updateNodeAsync</a><wbr/>(boolean sortParent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously updates node and loads children of the node if it is necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final &lt;A&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeAsync(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">updateNodeAsync</a><wbr/>(boolean sortParent,
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>,<wbr/>? super A&gt; handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously updates node and loads children of the node if it is necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final &lt;A&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeAsync(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">updateNodeAsync</a><wbr/>(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>,<wbr/>? super A&gt; handler)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously updates node and loads children of the node if it is necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeItself()">updateNodeItself</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates text and icon of the node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeStructure(java.util.Collection)">updateNodeStructure</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; objects)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method reloads children from given user object collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeStructureOfChildInExpandedPath(com.nomagic.magicdraw.ui.browser.Node)">updateNodeStructureOfChildInExpandedPath</a><wbr/>(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeStructureWithRetry()">updateNodeStructureWithRetry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tries to load all children of this node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNodeSync(boolean)">updateNodeSync</a><wbr/>(boolean sortParent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Synchronously updates node and loads children of the node if it is necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateSortKeys(java.lang.String)">updateSortKeys</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#waitForUpdateNodeCompletions()">waitForUpdateNodeCompletions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Wait for pending <code>updateNodeAsync()</code> completions</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="MAX_NODE_UPDATE_RETRY_COUNT">
<h3>MAX_NODE_UPDATE_RETRY_COUNT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">MAX_NODE_UPDATE_RETRY_COUNT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.browser.Node.MAX_NODE_UPDATE_RETRY_COUNT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ignoreRootCheck">
<h3>ignoreRootCheck</h3>
<div class="member-signature"><span class="modifiers">protected volatile</span> <span class="return-type">boolean</span> <span class="element-name">ignoreRootCheck</span></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon)">
<h3>Node</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Node</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon,javax.swing.Icon)">
<h3>Node</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Node</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> defaultIcon)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.BaseElement,javax.swing.Icon,javax.swing.Icon,com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams)">
<h3>Node</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Node</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> defaultIcon,
 com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams nodeTextParams)</span></div>
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
<section class="detail" id="isLocked()">
<h3>isLocked</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLocked</span>()</div>
<div class="block">Returns locked flag</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if it is locked, else false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocked(boolean)">
<h3>setLocked</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">long</span> <span class="element-name">setLocked</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets locked flag and increases locking counter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - lock value</dd>
<dt>Returns:</dt>
<dd>locking counter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetLock(boolean,long)">
<h3>resetLock</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">long</span> <span class="element-name">resetLock</span><wbr/><span class="parameters">(boolean value,
 long lockingCounter)</span></div>
<div class="block">Sets locked flag and decrements locking counter if current locking counter is equal to the one passed as method parameter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - lock value</dd>
<dd><code>lockingCounter</code> - locking counter</dd>
<dt>Returns:</dt>
<dd>locking counter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addListeners(com.nomagic.magicdraw.uml.BaseElement)">
<h3>addListeners</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addListeners</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> data)</span></div>
<div class="block">Adds needed listeners to the node element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - instance of <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml"><code>BaseElement</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addListeners()">
<h3>addListeners</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addListeners</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getChildren()">
<h3>getChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>&gt;</span> <span class="element-name">getChildren</span>()</div>
<div class="block">Returns list of children.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser"><code>Node</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUserObjectBaseElementID()">
<h3>getUserObjectBaseElementID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUserObjectBaseElementID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getChildCount()">
<h3>getChildCount</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getChildCount</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getChildCount()" title="class or interface in javax.swing.tree">getChildCount</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildCount()" title="class or interface in javax.swing.tree">getChildCount</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildAt(int)">
<h3>getChildAt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></span> <span class="element-name">getChildAt</span><wbr/><span class="parameters">(int index)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getChildAt(int)" title="class or interface in javax.swing.tree">getChildAt</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getChildAt(int)" title="class or interface in javax.swing.tree">getChildAt</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="children()">
<h3>children</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Enumeration.html" title="class or interface in java.util">Enumeration</a></span> <span class="element-name">children</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#children()" title="class or interface in javax.swing.tree">children</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#children()" title="class or interface in javax.swing.tree">children</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndex(javax.swing.tree.TreeNode)">
<h3>getIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIndex</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a> aChild)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getIndex(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getIndex</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getIndex(javax.swing.tree.TreeNode)" title="class or interface in javax.swing.tree">getIndex</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insert(javax.swing.tree.MutableTreeNode,int)">
<h3>insert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">insert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a> newChild,
 int childIndex)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#insert(javax.swing.tree.MutableTreeNode,int)" title="class or interface in javax.swing.tree">insert</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#insert(javax.swing.tree.MutableTreeNode,int)" title="class or interface in javax.swing.tree">insert</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
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
<section class="detail" id="remove(javax.swing.tree.MutableTreeNode)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a> aChild)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#remove(javax.swing.tree.MutableTreeNode)" title="class or interface in javax.swing.tree">remove</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#remove(javax.swing.tree.MutableTreeNode)" title="class or interface in javax.swing.tree">remove</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replaceChildren(java.util.List)">
<h3>replaceChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">replaceChildren</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>&gt; newChildren)</span></div>
</section>
</li>
<li>
<section class="detail" id="exchangeNodeChildrenKeepers()">
<h3>exchangeNodeChildrenKeepers</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.NodeChildrenKeeper</span> <span class="element-name">exchangeNodeChildrenKeepers</span>()</div>
</section>
</li>
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
<li>
<section class="detail" id="setUserObject(java.lang.Object)">
<h3>setUserObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUserObject</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="block">We put WeakReference with given object as user object in order to make things easier for garbage collector.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html#setUserObject(java.lang.Object)" title="class or interface in javax.swing.tree">setUserObject</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/MutableTreeNode.html" title="class or interface in javax.swing.tree">MutableTreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#setUserObject(java.lang.Object)" title="class or interface in javax.swing.tree">setUserObject</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultIcon()">
<h3>getDefaultIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getDefaultIcon</span>()</div>
<div class="block">Returns the default icon</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the default icon.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefaultIcon(javax.swing.Icon)">
<h3>setDefaultIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Sets the default icon.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the default icon.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="block">Gets the icon for this node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the icon of this node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIcon(javax.swing.Icon)">
<h3>setIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Sets the icon for this node.
 If object is not editable, sets gray icon.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the new icon.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateIcon()">
<h3>updateIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">updateIcon</span>()</div>
<div class="block">Sets icon according to the data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if icon was changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> event)</span></div>
<div class="block">This method is called when some ObjectData has changed.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>event</code> - the property changed event.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEventForUpdate(java.beans.PropertyChangeEvent)">
<h3>isEventForUpdate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isEventForUpdate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</span></div>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
<div class="block">This method returns the name of the ObjectData (user's object of this node).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the name of the ObjectData</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setText(java.lang.String)">
<h3>setText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Sets the name of the ObjectData(user's object).
 This method is called after the node's text editing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - the new node's text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateSortKeys(java.lang.String)">
<h3>updateSortKeys</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">updateSortKeys</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="internalUpdateNodeStructure()">
<h3>internalUpdateNodeStructure</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">internalUpdateNodeStructure</span>()</div>
<div class="block">Loads all children for this node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if structure was changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNodeStructureWithRetry()">
<h3>updateNodeStructureWithRetry</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">updateNodeStructureWithRetry</span>()</div>
<div class="block">Tries to load all children of this node. In case of exception due to model changes will try multiple times</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if structure was changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildrenOwner()">
<h3>getChildrenOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.ChildrenOwner</span> <span class="element-name">getChildrenOwner</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>children owner of the node. If node does not have his children owner, children owner from tree model is used</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChildrenOwner(com.nomagic.magicdraw.ui.browser.ChildrenOwner)">
<h3>setChildrenOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChildrenOwner</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.browser.ChildrenOwner owner)</span></div>
<div class="block">Set node specific children owner.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - owner</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTreeModel()">
<h3>getTreeModel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public final</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.TreeModel</span> <span class="element-name">getTreeModel</span>()</div>
<div class="block">Returns  the model of this  node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the model of this node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTreeModel(com.nomagic.magicdraw.ui.browser.TreeModel)">
<h3>setTreeModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTreeModel</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.browser.TreeModel model)</span></div>
<div class="block">Sets the model for this node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>model</code> - the TreeModel.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNodeStructure(java.util.Collection)">
<h3>updateNodeStructure</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">updateNodeStructure</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; objects)</span></div>
<div class="block">This method reloads children from given user object collection.
 If children already exists, sets only text for the node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>objects</code> - the given children</dd>
<dt>Returns:</dt>
<dd>true if node structure was changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNodeStructureOfChildInExpandedPath(com.nomagic.magicdraw.ui.browser.Node)">
<h3>updateNodeStructureOfChildInExpandedPath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateNodeStructureOfChildInExpandedPath</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node)</span></div>
</section>
</li>
<li>
<section class="detail" id="unCompactNodes()">
<h3>unCompactNodes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">unCompactNodes</span>()</div>
<div class="block">Un-compact all compacted children.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if at least one child was un-compacted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compactNodes(boolean)">
<h3>compactNodes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">compactNodes</span><wbr/><span class="parameters">(boolean parentStructureChanged)</span></div>
<div class="block">Compact all children.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parentStructureChanged</code> - was parent (current) node structure changed</dd>
<dt>Returns:</dt>
<dd>true if at least one child was compacted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replaceCompactableNode(com.nomagic.magicdraw.ui.browser.Node)">
<h3>replaceCompactableNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">replaceCompactableNode</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node)</span></div>
<div class="block">Replace given node with its compacted child if needed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - given node</dd>
<dt>Returns:</dt>
<dd>node replaced node or null if no replacement</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNodeItself()">
<h3>updateNodeItself</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">updateNodeItself</span>()</div>
<div class="block">Updates text and icon of the node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if text or icon was changed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalUpdateNodeItself()">
<h3>internalUpdateNodeItself</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">internalUpdateNodeItself</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setForceUpdate(boolean)">
<h3>setForceUpdate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setForceUpdate</span><wbr/><span class="parameters">(boolean forceUpdate)</span></div>
<div class="block">Set to true to force node update, no matter if text or icon was not changed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>forceUpdate</code> - flag to indicate update status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNodeFor(java.lang.Object)">
<h3>createNodeFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">createNodeFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Creates node for given element. Uses node creator from tree model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - the given object.</dd>
<dt>Returns:</dt>
<dd>the created node or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootElements()">
<h3>getRootElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getRootElements</span>()</div>
<div class="block">Collects root elements of children</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of root elements of children</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNodeForObject(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getNodeForObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[]</span> <span class="element-name">getNodeForObject</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object)</span></div>
<div class="block">Returns the tree node which data is the same as given Element.
 This method is used to determine if node with given Element as
 data object exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - the given Element.</dd>
<dt>Returns:</dt>
<dd>the node which data object is the same as given object
 or null such node is not found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHiddenNodeFor(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getHiddenNodeFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">getHiddenNodeFor</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> object)</span></div>
</section>
</li>
<li>
<section class="detail" id="prepareUserObjectNodeMap()">
<h3>prepareUserObjectNodeMap</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>,<wbr/><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>&gt;</span> <span class="element-name">prepareUserObjectNodeMap</span>()</div>
<div class="block">Return map of user objects mapped to nodes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of user objects mapped to nodes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mouseDoubleClicked(java.awt.AWTEvent)">
<h3>mouseDoubleClicked</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">mouseDoubleClicked</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a> event)</span></div>
<div class="block">Calls <code>onFind</code> for user object.
 This method is called when user double clicks with mouse on the node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - click event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="enterClicked(java.awt.AWTEvent)">
<h3>enterClicked</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enterClicked</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/AWTEvent.html" title="class or interface in java.awt">AWTEvent</a> event)</span></div>
<div class="block">Calls <code>mouseDoubleClicked</code> for user object.
 This method is called when user double clicks with mouse on the node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - click event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeListeners()">
<h3>removeListeners</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">removeListeners</span>()</div>
<div class="block">Removes propertyChangeListener(node) from Element property change support.</div>
</section>
</li>
<li>
<section class="detail" id="remove()">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span>()</div>
<div class="block">Removes node from parent.</div>
</section>
</li>
<li>
<section class="detail" id="disposeNode()">
<h3>disposeNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disposeNode</span>()</div>
<div class="block">Disposes the node - unregisters listeners, removes from nodes map and etc.</div>
</section>
</li>
<li>
<section class="detail" id="removeAllChildren(java.util.Collection)">
<h3>removeAllChildren</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">removeAllChildren</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; userObjects)</span></div>
<div class="block">Removes nodes from this node if theirs data objects are not in given userObjects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>userObjects</code> - the given userObjects of the DTObjects.</dd>
<dt>Returns:</dt>
<dd>true, if at least one node was removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeIllegalNodes()">
<h3>removeIllegalNodes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">removeIllegalNodes</span>()</div>
<div class="block">Removes nodes from this node these nodes cannot be created with node creator.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if at least one node was removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllChildren()">
<h3>removeAllChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllChildren</span>()</div>
<div class="block">Removes all nodes from this node.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#removeAllChildren()" title="class or interface in javax.swing.tree">removeAllChildren</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeRecursively()">
<h3>removeRecursively</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeRecursively</span>()</div>
<div class="block">Removes all nodes from this node recursively</div>
</section>
</li>
<li>
<section class="detail" id="removeRecursively(int)">
<h3>removeRecursively</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeRecursively</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Removes all nodes from this node recursively</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - of node which should be deleted.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="expand(boolean)">
<h3>expand</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">expand</span><wbr/><span class="parameters">(boolean sortExplicitly)</span></div>
<div class="block">Expands the tree node. If children of the node are not loaded, load them.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortExplicitly</code> - <code>true</code>, if node children must be sorted explicitly.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="expand()">
<h3>expand</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">expand</span>()</div>
<div class="block">Expands the tree node. If children of the node are not loaded, load them.</div>
</section>
</li>
<li>
<section class="detail" id="expandAsync(boolean)">
<h3>expandAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">expandAsync</span><wbr/><span class="parameters">(boolean sortExplicitly)</span></div>
<div class="block">Asynchronously expands the tree node. If children of the node are not loaded, load them.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortExplicitly</code> - <code>true</code>, if node children must be sorted explicitly.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="expandAsync()">
<h3>expandAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">expandAsync</span>()</div>
<div class="block">Asynchronously expands the tree node. If children of the node are not loaded, load them.</div>
</section>
</li>
<li>
<section class="detail" id="updateChildren(com.nomagic.magicdraw.ui.browser.Node,boolean)">
<h3>updateChildren</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">updateChildren</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 boolean sortExplicitly)</span></div>
<div class="block">Updates children of this node depending on dirty and expand state.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - the given node.</dd>
<dd><code>sortExplicitly</code> - if <code>true</code> sort children explicitly</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateChildrenAsync(com.nomagic.magicdraw.ui.browser.Node,boolean)">
<h3>updateChildrenAsync</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;?&gt;</span> <span class="element-name">updateChildrenAsync</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 boolean sortExplicitly)</span></div>
<div class="block">Asynchronously updates children of this node depending on dirty and expand state.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - the given node.</dd>
<dd><code>sortExplicitly</code> - if <code>true</code> sort children explicitly</dd>
<dt>Returns:</dt>
<dd>A <code>Future</code> object representing the pending operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateChildrenAsync(com.nomagic.magicdraw.ui.browser.Node,boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">
<h3 id="updateChildrenAsync(com.nomagic.magicdraw.ui.browser.Node,boolean,java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">updateChildrenAsync</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;?&gt;</span> <span class="element-name">updateChildrenAsync</span><wbr/><span class="parameters">(<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 boolean sortExplicitly,
 @CheckForNull
 A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>,<wbr/>? super A&gt; handler)</span></div>
<div class="block">Asynchronously updates children of this node depending on dirty and expand state.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>A</code> - The type of the object attached to the completion handler</dd>
<dt>Parameters:</dt>
<dd><code>node</code> - the given node.</dd>
<dd><code>sortExplicitly</code> - if <code>true</code> sort children explicitly</dd>
<dd><code>attachment</code> - The object to attach to the update operation; can be <code>null</code></dd>
<dd><code>handler</code> - The handler for consuming the operation result, which is <code>true</code>, if node
                       itself was changed(not children).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collapse()">
<h3>collapse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">collapse</span>()</div>
<div class="block">Collapse this node.</div>
</section>
</li>
<li>
<section class="detail" id="isInExpandedPath()">
<h3>isInExpandedPath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInExpandedPath</span>()</div>
<div class="block">Checks if this node is in expanded path.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, is this node is in expanded path(visible to user).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="acceptLink(java.lang.Object)">
<h3>acceptLink</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">acceptLink</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Accepts drag and drop link action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - - moved object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="acceptLinkSpecific(java.util.List)">
<h3>acceptLinkSpecific</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">acceptLinkSpecific</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; vec)</span></div>
</section>
</li>
<li>
<section class="detail" id="canAcceptLink(java.lang.Object)">
<h3>canAcceptLink</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAcceptLink</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
</section>
</li>
<li>
<section class="detail" id="canAcceptLinkSpecific(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAcceptLinkSpecific</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canAcceptLinkSpecific</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj)</span></div>
</section>
</li>
<li>
<section class="detail" id="acceptMove(java.lang.Object,com.nomagic.magicdraw.ui.browser.Tree,java.awt.Point)">
<h3>acceptMove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">acceptMove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj,
 <a href="Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span></div>
<div class="block">Accepts drag and drop link action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - moved object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="acceptMoveSpecific(java.util.List,com.nomagic.magicdraw.ui.browser.Tree,java.awt.Point)">
<h3>acceptMoveSpecific</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">acceptMoveSpecific</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; vec,
 <a href="Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> location)</span></div>
</section>
</li>
<li>
<section class="detail" id="canAcceptMove(java.lang.Object)">
<h3>canAcceptMove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canAcceptMove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
</section>
</li>
<li>
<section class="detail" id="canAcceptMoveSpecific(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAcceptMoveSpecific</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canAcceptMoveSpecific</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="acceptCopy(java.lang.Object)">
<h3>acceptCopy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">acceptCopy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Accepts drag and drop link action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - moved object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="acceptCopySpecific(java.util.List)">
<h3>acceptCopySpecific</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">acceptCopySpecific</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCopyOperationTarget()">
<h3>getCopyOperationTarget</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getCopyOperationTarget</span>()</div>
</section>
</li>
<li>
<section class="detail" id="canAcceptCopy(java.lang.Object)">
<h3>canAcceptCopy</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">boolean</span> <span class="element-name">canAcceptCopy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
</section>
</li>
<li>
<section class="detail" id="canAcceptCopySpecific(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAcceptCopySpecific</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canAcceptCopySpecific</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSortKeys()">
<h3>getSortKeys</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys</span> <span class="element-name">getSortKeys</span>()</div>
<div class="block">Returns keys' array for sorting</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of <code>Node.NodeSortKeys</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSortKeys(com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys)">
<h3>setSortKeys</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSortKeys</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys sortKeys)</span></div>
</section>
</li>
<li>
<section class="detail" id="createNodeSortKeys()">
<h3>createNodeSortKeys</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.ui.browser.Node.NodeSortKeys</span> <span class="element-name">createNodeSortKeys</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns node type</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>returns node type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNode()">
<h3>updateNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">updateNode</span>()</div>
<div class="block">Updates node and loads children of the node if it is necessary.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code>, if node itself was changed(not children).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNode(boolean)">
<h3>updateNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">updateNode</span><wbr/><span class="parameters">(boolean sortParent)</span></div>
<div class="block">Updates node and loads children of the node if it is necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortParent</code> - if <code>true</code> - parent node will be sorted if this node changes text.</dd>
<dt>Returns:</dt>
<dd><code>true</code>, if node itself was changed(not children).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNodeAsync()">
<h3>updateNodeAsync</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</span> <span class="element-name">updateNodeAsync</span>()</div>
<div class="block">Asynchronously updates node and loads children of the node if it is necessary.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>Future</code> which results to <code>true</code>, if node itself was
 changed(not children).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNodeAsync(A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">
<h3 id="updateNodeAsync(java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">updateNodeAsync</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">void</span> <span class="element-name">updateNodeAsync</span><wbr/><span class="parameters">(A attachment,
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>,<wbr/>? super A&gt; handler)</span></div>
<div class="block">Asynchronously updates node and loads children of the node if it is necessary.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>A</code> - The type of the object attached to the completion handler</dd>
<dt>Parameters:</dt>
<dd><code>attachment</code> - The object to attach to the update operation; can be <code>null</code></dd>
<dd><code>handler</code> - The handler for consuming the operation result, which is <code>true</code>, if node
                   itself was changed(not children).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNodeAsync(boolean)">
<h3>updateNodeAsync</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</span> <span class="element-name">updateNodeAsync</span><wbr/><span class="parameters">(boolean sortParent)</span></div>
<div class="block">Asynchronously updates node and loads children of the node if it is necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortParent</code> - if <code>true</code> - parent node will be sorted if this node changes text.</dd>
<dt>Returns:</dt>
<dd><code>Future</code> which results to <code>true</code>, if node itself was changed(not children).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNodeAsync(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">
<h3 id="updateNodeAsync(boolean,java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">updateNodeAsync</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type">void</span> <span class="element-name">updateNodeAsync</span><wbr/><span class="parameters">(boolean sortParent,
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>,<wbr/>? super A&gt; handler)</span></div>
<div class="block">Asynchronously updates node and loads children of the node if it is necessary.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>A</code> - The type of the object attached to the completion handler</dd>
<dt>Parameters:</dt>
<dd><code>sortParent</code> - if <code>true</code> - parent node will be sorted if this node changes text.</dd>
<dd><code>attachment</code> - The object to attach to the update operation; can be <code>null</code></dd>
<dd><code>handler</code> - The handler for consuming the result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forceUpdateNodeSync(boolean)">
<h3>forceUpdateNodeSync</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">forceUpdateNodeSync</span><wbr/><span class="parameters">(boolean sortParent)</span></div>
<div class="block">Marks node as expanded which forces node to be fully updated, and initiates asynchronous node update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortParent</code> - if <code>true</code> - parent node will be sorted if this node changes text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doUpdateNode(boolean,A,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">
<h3 id="doUpdateNode(boolean,java.lang.Object,com.nomagic.magicdraw.utils.concurrent.CompletionHandler)">doUpdateNode</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="type-parameters">&lt;A&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html" title="class or interface in java.util.concurrent">Future</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt;</span> <span class="element-name">doUpdateNode</span><wbr/><span class="parameters">(boolean sortParent,
 @CheckForNull
 A attachment,
 @CheckForNull
 com.nomagic.magicdraw.utils.concurrent.CompletionHandler&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>,<wbr/>? super A&gt; handler)</span></div>
</section>
</li>
<li>
<section class="detail" id="isProjectReady(com.nomagic.magicdraw.ui.browser.TreeModel)">
<h3>isProjectReady</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isProjectReady</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.browser.TreeModel treeModel)</span></div>
</section>
</li>
<li>
<section class="detail" id="isNodeLocked(com.nomagic.magicdraw.ui.browser.TreeModel)">
<h3>isNodeLocked</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isNodeLocked</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.browser.TreeModel treeModel)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateNodeSync(boolean)">
<h3>updateNodeSync</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">updateNodeSync</span><wbr/><span class="parameters">(boolean sortParent)</span></div>
<div class="block">Synchronously updates node and loads children of the node if it is necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sortParent</code> - if <code>true</code> - parent node will be sorted if this node changes text.</dd>
<dt>Returns:</dt>
<dd><code>true</code>, if node itself was changed(not children).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doUpdateNodeSync(boolean)">
<h3>doUpdateNodeSync</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">doUpdateNodeSync</span><wbr/><span class="parameters">(boolean sortParent)</span></div>
</section>
</li>
<li>
<section class="detail" id="waitForUpdateNodeCompletions()">
<h3>waitForUpdateNodeCompletions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">waitForUpdateNodeCompletions</span>()</div>
<div class="block">Wait for pending <code>updateNodeAsync()</code> completions</div>
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
<li>
<section class="detail" id="isExpanded()">
<h3>isExpanded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExpanded</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.ui.browser.Expandable</code></span></div>
<div class="block">Checks if component is expanded or not.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isExpanded</code> in interface <code>com.nomagic.magicdraw.ui.browser.Expandable</code></dd>
<dt>Returns:</dt>
<dd><code>true</code> when component is expanded, <code>false</code> - otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExpanded(boolean)">
<h3>setExpanded</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setExpanded</span><wbr/><span class="parameters">(boolean expanded)</span></div>
<div class="block">Sets expanded state of this node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expanded</code> - true if node is expanded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isForceStructureUpdateOnExpand()">
<h3>isForceStructureUpdateOnExpand</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isForceStructureUpdateOnExpand</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setForceStructureUpdateOnExpand(boolean)">
<h3>setForceStructureUpdateOnExpand</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setForceStructureUpdateOnExpand</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="isRemoveChildrenOnCollapse()">
<h3>isRemoveChildrenOnCollapse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemoveChildrenOnCollapse</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setRemoveChildrenOnCollapse(boolean)">
<h3>setRemoveChildrenOnCollapse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRemoveChildrenOnCollapse</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNodeTextParams()">
<h3>getNodeTextParams</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.dassault_systemes.modeler.foundation.ui.tree.NodeTextParams</span> <span class="element-name">getNodeTextParams</span>()</div>
</section>
</li>
<li>
<section class="detail" id="constructText()">
<h3>constructText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructText</span>()</div>
</section>
</li>
<li>
<section class="detail" id="constructTextForSorting()">
<h3>constructTextForSorting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructTextForSorting</span>()</div>
<div class="block">This method returns the name of the ObjectData (user's object of this node) for sorting purposes</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the name of the ObjectData for sorting purposes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRemoveCommand()">
<h3>createRemoveCommand</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.foundation.editing.Command</span> <span class="element-name">createRemoveCommand</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getParent()">
<h3>getParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">getParent</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html#getParent()" title="class or interface in javax.swing.tree">getParent</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/TreeNode.html" title="class or interface in javax.swing.tree">TreeNode</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html#getParent()" title="class or interface in javax.swing.tree">getParent</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/tree/DefaultMutableTreeNode.html" title="class or interface in javax.swing.tree">DefaultMutableTreeNode</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirtyRecursively(boolean)">
<h3>setDirtyRecursively</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirtyRecursively</span><wbr/><span class="parameters">(boolean dirty)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDirty()">
<h3>isDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDirty(boolean)">
<h3>setDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(boolean dirty)</span></div>
<div class="block">Sets dirty flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dirty</code> - is dirty?</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActions()">
<h3>getActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int[]</span> <span class="element-name">getActions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="canDelete()">
<h3>canDelete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDelete</span>()</div>
<div class="block">Can delete if user object is BaseElement and can be deleted from its parent.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if can delete, else false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEditingText()">
<h3>getEditingText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEditingText</span>()</div>
<div class="block">Returns text which will be edited.
 Since some nodes can display one text, but should be edited with other text this method return text to be edited.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>text to edit.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setEditable(boolean)">
<h3>setEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEditable</span><wbr/><span class="parameters">(boolean editable)</span></div>
<div class="block">Method marks node as editable or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>editable</code> - is editable?</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#isEditable()"><code>isEditable()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoading()">
<h3>isLoading</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoading</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLoading(boolean)">
<h3>setLoading</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoading</span><wbr/><span class="parameters">(boolean flag)</span></div>
</section>
</li>
<li>
<section class="detail" id="configure(com.nomagic.actions.ActionsManager)">
<h3>configure</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block">Method configure.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - actions manager to be configured for this node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureMultiple(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.browser.Node[])">
<h3>configureMultiple</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configureMultiple</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> mngr,
 <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>[] node)</span></div>
<div class="block">Method to configure actions for context menu of all the provided nodes (array always includes the current node instance too).
 This method gets called only once for all nodes of the same class type, so each node instance in the provided array should be regarded.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mngr</code> - actions manager to be configured for this node.</dd>
<dd><code>node</code> - array of <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser"><code>Node</code></a> for which actions are configured.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsForDnd()">
<h3>getElementsForDnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>[]</span> <span class="element-name">getElementsForDnd</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRepresentedElements()">
<h3>getRepresentedElements</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>[]</span> <span class="element-name">getRepresentedElements</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getElementForCopyAction()">
<h3>getElementForCopyAction</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getElementForCopyAction</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isChildrenSortable()">
<h3>isChildrenSortable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChildrenSortable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setChildrenSortable(boolean)">
<h3>setChildrenSortable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChildrenSortable</span><wbr/><span class="parameters">(boolean childrenSortable)</span></div>
</section>
</li>
<li>
<section class="detail" id="nodeAdded()">
<h3>nodeAdded</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">nodeAdded</span>()</div>
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
<section class="detail" id="isCanDelete()">
<h3>isCanDelete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCanDelete</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCanDelete(boolean)">
<h3>setCanDelete</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCanDelete</span><wbr/><span class="parameters">(boolean canDelete)</span></div>
<div class="block">Method marks node as deletable or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>canDelete</code> - can delete?</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#canDelete()"><code>canDelete()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnableUpdateIcon()">
<h3>isEnableUpdateIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnableUpdateIcon</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns the enableUpdateIcon.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnableUpdateIcon(boolean)">
<h3>setEnableUpdateIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnableUpdateIcon</span><wbr/><span class="parameters">(boolean enableUpdateIcon)</span></div>
</section>
</li>
<li>
<section class="detail" id="isChildrenSortNeeded()">
<h3>isChildrenSortNeeded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChildrenSortNeeded</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setChildrenSortNeeded(boolean)">
<h3>setChildrenSortNeeded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChildrenSortNeeded</span><wbr/><span class="parameters">(boolean childrenSortNeeded)</span></div>
</section>
</li>
<li>
<section class="detail" id="isCompactable()">
<h3>isCompactable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCompactable</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true is node is compactable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCompactable(boolean)">
<h3>setCompactable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCompactable</span><wbr/><span class="parameters">(boolean compactable)</span></div>
<div class="block">Make node compactable.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>compactable</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNodeStructureChanged()">
<h3>isNodeStructureChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNodeStructureChanged</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setNodeStructureChanged(boolean)">
<h3>setNodeStructureChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNodeStructureChanged</span><wbr/><span class="parameters">(boolean nodeStructureChanged)</span></div>
</section>
</li>
<li>
<section class="detail" id="isHidden()">
<h3>isHidden</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHidden</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if node is hidden</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHidden(boolean)">
<h3>setHidden</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHidden</span><wbr/><span class="parameters">(boolean hidden)</span></div>
<div class="block">Make node "hidden"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hidden</code> - hidden value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHiddenParent()">
<h3>getHiddenParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a></span> <span class="element-name">getHiddenParent</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>hidden parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHiddenParent(com.nomagic.magicdraw.ui.browser.Node)">
<h3>setHiddenParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHiddenParent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> hiddenParent)</span></div>
<div class="block">Set hidden parent. Parent is used if node is "hidden", because normal parent is null in such case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hiddenParent</code> - hidden parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearHiddenOwners()">
<h3>clearHiddenOwners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearHiddenOwners</span>()</div>
<div class="block">Clear all hidden owners. Hidden nodes becomes not hidden.</div>
</section>
</li>
<li>
<section class="detail" id="getHiddenOwners()">
<h3>getHiddenOwners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a>&gt;</span> <span class="element-name">getHiddenOwners</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>hidden owners or empty list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="constructHiddenOwnerText()">
<h3>constructHiddenOwnerText</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructHiddenOwnerText</span>()</div>
<div class="block">Constructs hidden owners text.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>hidden owner text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAutoExpandable()">
<h3>isAutoExpandable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutoExpandable</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>auto-expandable node flag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoExpandable(boolean)">
<h3>setAutoExpandable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoExpandable</span><wbr/><span class="parameters">(boolean autoExpandable)</span></div>
<div class="block">Change auto-expandable flag - node will be expanded if it has only one child when expanding parent node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>autoExpandable</code> - true if node is auto-expandable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLoadingNode()">
<h3>removeLoadingNode</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">removeLoadingNode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isNodeUpdated()">
<h3>isNodeUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNodeUpdated</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setNodeUpdated(boolean)">
<h3>setNodeUpdated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNodeUpdated</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPriorityInOwner()">
<h3>getPriorityInOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPriorityInOwner</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>priority in owner for sorting</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPriorityInOwner(int)">
<h3>setPriorityInOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPriorityInOwner</span><wbr/><span class="parameters">(int priority)</span></div>
<div class="block">Set priority in owner for sorting</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>priority</code> - priority</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSpecificRemoveCommand()">
<h3>createSpecificRemoveCommand</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.commands.Command</span> <span class="element-name">createSpecificRemoveCommand</span>()</div>
<div class="block">Creates specific command for removing</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>specific command for node removing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSpecificElement()">
<h3>isSpecificElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSpecificElement</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if element is specific</dd>
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
