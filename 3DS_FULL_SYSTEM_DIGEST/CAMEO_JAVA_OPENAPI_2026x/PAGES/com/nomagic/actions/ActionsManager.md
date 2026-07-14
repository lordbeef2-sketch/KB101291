# JAVA OPENAPI: ActionsManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/actions/ActionsManager.html
- source_path: `com/nomagic/actions/ActionsManager.html`
- source_sha256: `f55531e2da3ff619eb29a60ea2d303b5688dfd22e334fcb276f3b9f776b70986`
- captured_utc: `2026-07-14T16:57:42.271358+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Class ActionsManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.actions.ActionsManager

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[MDActionsManager](../magicdraw/actions/MDActionsManager.html)`

@OpenApiAllpublic classActionsManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)

The class responsible for managing the actions and categories.
 It has a list of categories and the helper maps where actions are registered by shortcuts and by id.

See Also:
[`ActionsCategory`](ActionsCategory.html)
[`NMAction`](NMAction.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ActionsManager.ActionPropertyChangeListener](ActionsManager.ActionPropertyChangeListener.html)`
The action property change listener class.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SHORTCUTS_MODIFIED](#SHORTCUTS_MODIFIED)`
A key for Boolean which marks action with modified shortcuts in UI
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ActionsManager](#%3Cinit%3E())()`
Creates the actions manager.
`[ActionsManager](#%3Cinit%3E(com.nomagic.actions.ActionsManager))([ActionsManager](ActionsManager.html) parent)`
Creates the actions manager.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addActionNearTheGiven](#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) givenID,
 boolean addAfter,
 [NMAction](NMAction.html) action)`
Adds given action near the action with the given id.
`void`
`[addActionNearTheGiven](#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction,com.nomagic.actions.ActionsCategory))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) givenID,
 boolean addAfter,
 [NMAction](NMAction.html) action,
 [ActionsCategory](ActionsCategory.html) defaultCategory)`
Adds given action near the action with the given id.
`void`
`[addCategory](#addCategory(int,com.nomagic.actions.ActionsCategory))(int index,
 [ActionsCategory](ActionsCategory.html) category)`
Adds the given category to the manager.
`void`
`[addCategory](#addCategory(com.nomagic.actions.ActionsCategory))([ActionsCategory](ActionsCategory.html) category)`
Adds the given category to the manager.
`void`
`[addCategory](#addCategory(com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory,boolean))([ActionsCategory](ActionsCategory.html) relatedCategory,
 [ActionsCategory](ActionsCategory.html) category,
 boolean addAfter)`
Adds the given category to the manager.
`void`
`[addCategory](#addCategory(java.lang.String,com.nomagic.actions.ActionsCategory,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) relatedCategoryID,
 [ActionsCategory](ActionsCategory.html) category,
 boolean addAfter)`
Adds the given category to the manager.
`[ActionsManager](ActionsManager.html)`
`[clone](#clone())()`
Clones the manager.
`static [MDAction](../magicdraw/actions/MDAction.html)`
`[constructNoneAction](#constructNoneAction())()`
Constructs a none action.
`void`
`[dropCache](#dropCache())()`

`void`
`[forEach](#forEach(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)`
Performs the given consumer for each owned action.
`void`
`[forEachIncludingSelf](#forEachIncludingSelf(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)`
Performs the given consumer for each owned action including self.
`[NMAction](NMAction.html)`
`[getActionFor](#getActionFor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Returns the action for given id.
`[NMAction](NMAction.html)`
`[getActionFor](#getActionFor(javax.swing.KeyStroke))([KeyStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke)`
Returns the action for given stroke.
`[NMAction](NMAction.html)`
`[getActionParent](#getActionParent(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Returns parent action for given action.
`[ActionsCategory](ActionsCategory.html)`
`[getActionsCategoryRecursively](#getActionsCategoryRecursively(java.util.List,java.lang.String))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionsCategory](ActionsCategory.html)> categories,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Recursively finds an action category with a given id.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)>`
`[getAllActions](#getAllActions())()`
Returns the list of all actions registered in this manager.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)>`
`[getAllOrderedActions](#getAllOrderedActions(boolean))(boolean includeCategories)`
Returns the list if all ordered actions registered in this manager.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionsCategory](ActionsCategory.html)>`
`[getCategories](#getCategories())()`
Returns the list of the categories.
`[ActionsCategory](ActionsCategory.html)`
`[getCategory](#getCategory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Returns the category with given id.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[NMAction](NMAction.html)>`
`[getIdToActionMap](#getIdToActionMap())()`

`[ActionsCategory](ActionsCategory.html)`
`[getLastActionsCategory](#getLastActionsCategory())()`
Returns last category by order.
`[ActionsManager](ActionsManager.html)`
`[getParent](#getParent())()`
Returns the actions manager parent.
`boolean`
`[isEmpty](#isEmpty())()`

`[ActionsManager](ActionsManager.html)`
`[makeCopy](#makeCopy())()`
Copies this manager and adds property change listeners to all actions in
 order to have the same action state in source and copy.
`static void`
`[markShortcutsModified](#markShortcutsModified(javax.swing.Action))([Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html) action)`
Add a mark that shortcuts are modified externally in UI
`void`
`[removeAction](#removeAction(com.nomagic.actions.NMAction))([NMAction](NMAction.html) action)`
Removes action from this manager.
`void`
`[removeAction](#removeAction(com.nomagic.actions.NMAction,com.nomagic.actions.NMAction))([NMAction](NMAction.html) action,
 [NMAction](NMAction.html) parent)`
Removes action with given ID from this manager.
`void`
`[removeAction](#removeAction(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) actionID)`
Removes action with given ID from this manager.
`void`
`[removeAllActions](#removeAllActions())()`
Removes all actions.
`void`
`[removeCategory](#removeCategory(com.nomagic.actions.ActionsCategory))([ActionsCategory](ActionsCategory.html) category)`
Removes the given category from the manager.
`void`
`[removeIf](#removeIf(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[NMAction](NMAction.html)> filter)`
Removes all of the actions of this manager that satisfy the given predicate
`void`
`[setCategories](#setCategories(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [ActionsCategory](ActionsCategory.html)> list)`
Sets the list of the categories.
`void`
`[setParent](#setParent(com.nomagic.actions.ActionsManager))([ActionsManager](ActionsManager.html) parent)`
Sets the actions manager parent.
`void`
`[updateCommandKeysFrom](#updateCommandKeysFrom(com.nomagic.actions.ActionsManager))([ActionsManager](ActionsManager.html) manager)`
Deprecated.
use [`updateShortcutsFrom(ActionsManager)`](#updateShortcutsFrom(com.nomagic.actions.ActionsManager))
`void`
`[updateShortcutsFrom](#updateShortcutsFrom(com.nomagic.actions.ActionsManager))([ActionsManager](ActionsManager.html) manager)`
Takes all action from the given manager with modified shortcuts and overwrites the shortcuts for actions in this manager.
`void`
`[updateStateForAllActions](#updateStateForAllActions())()`
Calls updateState() method for all inner actions.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SHORTCUTS_MODIFIED
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SHORTCUTS_MODIFIED
A key for Boolean which marks action with modified shortcuts in UI
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.actions.ActionsManager.SHORTCUTS_MODIFIED)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ActionsManager
public ActionsManager(@CheckForNull
 [ActionsManager](ActionsManager.html) parent)
Creates the actions manager.
Parameters:
`parent` - the parent of the actions manager. May be null.
ActionsManager
public ActionsManager()
Creates the actions manager.
 ============ METHOD DETAIL ========== 
Method Details
markShortcutsModified
public static void markShortcutsModified([Action](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html) action)
Add a mark that shortcuts are modified externally in UI
Parameters:
`action` - action
getCategories
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionsCategory](ActionsCategory.html)> getCategories()
Returns the list of the categories.
Returns:
the cloned list of the categories.
getActionsCategoryRecursively
@CheckForNullpublic [ActionsCategory](ActionsCategory.html) getActionsCategoryRecursively([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ActionsCategory](ActionsCategory.html)> categories,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Recursively finds an action category with a given id.
Parameters:
`categories` - categories to search.
`id` - id of a category to find.
Returns:
found action category or null if it is not found.
setCategories
public void setCategories([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [ActionsCategory](ActionsCategory.html)> list)
Sets the list of the categories.
 All old actions will be unregistered and new registered.
Parameters:
`list` - the list of the categories.
addCategory
public void addCategory([ActionsCategory](ActionsCategory.html) category)
Adds the given category to the manager. The actions from the given
 category will be registered.
Parameters:
`category` - the given category.
addCategory
public void addCategory(int index,
 [ActionsCategory](ActionsCategory.html) category)
Adds the given category to the manager. The actions from the given
 category will be registered.
Parameters:
`index` - index where category will be added.
`category` - the given category.
removeCategory
public void removeCategory([ActionsCategory](ActionsCategory.html) category)
Removes the given category from the manager.
 The actions from the given category will be unregistered.
Parameters:
`category` - the given category.
addCategory
public void addCategory([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) relatedCategoryID,
 [ActionsCategory](ActionsCategory.html) category,
 boolean addAfter)
Adds the given category to the manager. The actions from the given
 category will be registered.
Parameters:
`relatedCategoryID` - related category id
`category` - the given category
`addAfter` - add after related category or before related category
addCategory
public void addCategory(@CheckForNull
 [ActionsCategory](ActionsCategory.html) relatedCategory,
 [ActionsCategory](ActionsCategory.html) category,
 boolean addAfter)
Adds the given category to the manager. The actions from the given
 category will be registered.
Parameters:
`relatedCategory` - related category
`category` - the given category
`addAfter` - add after related category or before related category
getCategory
@CheckForNullpublic [ActionsCategory](ActionsCategory.html) getCategory([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Returns the category with given id.
Parameters:
`id` - the id of the category.
Returns:
the category with given id or null if this manager does not have such category.
updateCommandKeysFrom
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void updateCommandKeysFrom([ActionsManager](ActionsManager.html) manager)
Deprecated.
use [`updateShortcutsFrom(ActionsManager)`](#updateShortcutsFrom(com.nomagic.actions.ActionsManager))
updateShortcutsFrom
public void updateShortcutsFrom([ActionsManager](ActionsManager.html) manager)
Takes all action from the given manager with modified shortcuts and overwrites the shortcuts for actions in this manager.
Parameters:
`manager` - the given manager.
See Also:
[`SHORTCUTS_MODIFIED`](#SHORTCUTS_MODIFIED)
getAllActions
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)> getAllActions()
Returns the list of all actions registered in this manager.
Returns:
the list of all registered actions.
removeIf
public void removeIf([Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[NMAction](NMAction.html)> filter)
Removes all of the actions of this manager that satisfy the given predicate
Parameters:
`filter` - given predicate
forEachIncludingSelf
public void forEachIncludingSelf([Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)
Performs the given consumer for each owned action including self. Owned actions should not be added/removed inside consumer.
Parameters:
`consumer` - the action to be performed for each NMAction
See Also:
[`NMAction.forEachIncludingSelf(Consumer)`](NMAction.html#forEachIncludingSelf(java.util.function.Consumer))
forEach
public void forEach([Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[NMAction](NMAction.html)> consumer)
Performs the given consumer for each owned action. Owned actions should not be added/removed inside consumer.
Parameters:
`consumer` - the action to be performed for each NMAction
See Also:
[`NMAction.forEach(Consumer)`](NMAction.html#forEach(java.util.function.Consumer))
isEmpty
public boolean isEmpty()
Returns:
true if this manager currently contains no actions, false if there are actions.
 Parent actions are not considered
getAllOrderedActions
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[NMAction](NMAction.html)> getAllOrderedActions(boolean includeCategories)
Returns the list if all ordered actions registered in this manager.
Parameters:
`includeCategories` - If true, then ActionsCategories will be included in the list
Returns:
the list of all registered actions.
removeAllActions
public void removeAllActions()
Removes all actions.
getActionFor
@CheckForNullpublic [NMAction](NMAction.html) getActionFor(@CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html) stroke)
Returns the action for given stroke. If this manager does not have such
 action, it looks in the parent.
Parameters:
`stroke` - stroke
Returns:
the action for given stroke or null if there are no action with such stroke.
getActionFor
@CheckForNullpublic [NMAction](NMAction.html) getActionFor([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Returns the action for given id. If this manager does not have such
 action, it looks in the parent.
Parameters:
`id` - action id
Returns:
the action for given id or null if there are no action with such id.
getIdToActionMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[NMAction](NMAction.html)> getIdToActionMap()
clone
public [ActionsManager](ActionsManager.html) clone()
Clones the manager.
 Does deep clone.
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
cloned instance
dropCache
public void dropCache()
setParent
public void setParent(@CheckForNull
 [ActionsManager](ActionsManager.html) parent)
Sets the actions manager parent.
Parameters:
`parent` - the new parent.
getParent
@CheckForNullpublic [ActionsManager](ActionsManager.html) getParent()
Returns the actions manager parent.
Returns:
parent.
getActionParent
@CheckForNullpublic [NMAction](NMAction.html) getActionParent([NMAction](NMAction.html) action)
Returns parent action for given action. Searches for the action object itself, if a provided object is not found actions are compared
 using equals(by action ID).
Parameters:
`action` - the given action.
Returns:
parent of given action.
makeCopy
public [ActionsManager](ActionsManager.html) makeCopy()
Copies this manager and adds property change listeners to all actions in
 order to have the same action state in source and copy.
Returns:
copied manager.
updateStateForAllActions
public void updateStateForAllActions()
Calls updateState() method for all inner actions.
See Also:
[`NMAction.updateState()`](NMAction.html#updateState())
getLastActionsCategory
@CheckForNullpublic [ActionsCategory](ActionsCategory.html) getLastActionsCategory()
Returns last category by order.
Returns:
last category
removeAction
public void removeAction([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) actionID)
Removes action with given ID from this manager. Searches for action parent, removes action from it's parent
 and removes parent if it does not have any more actions.
 If given ID is id of root category(added into manager), removes this category.
Parameters:
`actionID` - actionID id of action to remove.
removeAction
public void removeAction([NMAction](NMAction.html) action)
Removes action from this manager.
Parameters:
`action` - action to remove.
removeAction
public void removeAction([NMAction](NMAction.html) action,
 @CheckForNull
 [NMAction](NMAction.html) parent)
Removes action with given ID from this manager. Takes given parent, removes action from it's parent
 and removes parent if it does not have any more actions.
 If given ID is id of root category(added into manager), removes this category.
Parameters:
`action` - action to remove.
`parent` - parent of action to remove from.
addActionNearTheGiven
public void addActionNearTheGiven(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) givenID,
 boolean addAfter,
 @CheckForNull
 [NMAction](NMAction.html) action)
Adds given action near the action with the given id. The given action will be added into the same parent as action with givenID.
 The position of the given action will be above or below the "givenID".
Parameters:
`givenID` - the id of action to add near
`addAfter` - add after or before "givenID"
`action` - the action to add.
addActionNearTheGiven
public void addActionNearTheGiven(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) givenID,
 boolean addAfter,
 @CheckForNull
 [NMAction](NMAction.html) action,
 @CheckForNull
 [ActionsCategory](ActionsCategory.html) defaultCategory)
Adds given action near the action with the given id. The given action will be added into the same parent as action with givenID.
 The position of the given action will be above or below the "givenID".
Parameters:
`givenID` - the id of action to add near
`addAfter` - add after or before "givenID"
`action` - the action to add
`defaultCategory` - category to add action into if action with givenID does not exist. Last category from manager is used if defaultCategory is null
constructNoneAction
public static [MDAction](../magicdraw/actions/MDAction.html) constructNoneAction()
Constructs a none action.
Returns:
created none action.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Class ActionsManager">Class ActionsManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.actions.ActionsManager</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../magicdraw/actions/MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ActionsManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
<div class="block">The class responsible for managing the actions and categories.
 It has a list of categories and the helper maps where actions are registered by shortcuts and by id.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="ActionsCategory.html" title="class in com.nomagic.actions"><code>ActionsCategory</code></a></li>
<li><a href="NMAction.html" title="class in com.nomagic.actions"><code>NMAction</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ActionsManager.ActionPropertyChangeListener.html" title="class in com.nomagic.actions">ActionsManager.ActionPropertyChangeListener</a></code></div>
<div class="col-last even-row-color">
<div class="block">The action property change listener class.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHORTCUTS_MODIFIED">SHORTCUTS_MODIFIED</a></code></div>
<div class="col-last even-row-color">
<div class="block">A key for Boolean which marks action with modified shortcuts in UI</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ActionsManager</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates the actions manager.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.actions.ActionsManager)">ActionsManager</a><wbr/>(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> parent)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates the actions manager.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)">addActionNearTheGiven</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> givenID,
 boolean addAfter,
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds given action near the action with the given id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction,com.nomagic.actions.ActionsCategory)">addActionNearTheGiven</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> givenID,
 boolean addAfter,
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> defaultCategory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds given action near the action with the given id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCategory(int,com.nomagic.actions.ActionsCategory)">addCategory</a><wbr/>(int index,
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the given category to the manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCategory(com.nomagic.actions.ActionsCategory)">addCategory</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the given category to the manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCategory(com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory,boolean)">addCategory</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> relatedCategory,
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 boolean addAfter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the given category to the manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCategory(java.lang.String,com.nomagic.actions.ActionsCategory,boolean)">addCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> relatedCategoryID,
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 boolean addAfter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the given category to the manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clones the manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../magicdraw/actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#constructNoneAction()">constructNoneAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs a none action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dropCache()">dropCache</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forEach(java.util.function.Consumer)">forEach</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs the given consumer for each owned action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Performs the given consumer for each owned action including self.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionFor(java.lang.String)">getActionFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the action for given id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionFor(javax.swing.KeyStroke)">getActionFor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the action for given stroke.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionParent(com.nomagic.actions.NMAction)">getActionParent</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns parent action for given action.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionsCategoryRecursively(java.util.List,java.lang.String)">getActionsCategoryRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Recursively finds an action category with a given id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllActions()">getAllActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of all actions registered in this manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllOrderedActions(boolean)">getAllOrderedActions</a><wbr/>(boolean includeCategories)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list if all ordered actions registered in this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCategories()">getCategories</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of the categories.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCategory(java.lang.String)">getCategory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the category with given id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIdToActionMap()">getIdToActionMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastActionsCategory()">getLastActionsCategory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last category by order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the actions manager parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEmpty()">isEmpty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#makeCopy()">makeCopy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copies this manager and adds property change listeners to all actions in
 order to have the same action state in source and copy.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#markShortcutsModified(javax.swing.Action)">markShortcutsModified</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Add a mark that shortcuts are modified externally in UI</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAction(com.nomagic.actions.NMAction)">removeAction</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes action from this manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAction(com.nomagic.actions.NMAction,com.nomagic.actions.NMAction)">removeAction</a><wbr/>(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  action with given ID from this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAction(java.lang.String)">removeAction</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes  action with given ID from this manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAllActions()">removeAllActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCategory(com.nomagic.actions.ActionsCategory)">removeCategory</a><wbr/>(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the given category from the manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeIf(java.util.function.Predicate)">removeIf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; filter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes all of the actions of this manager that satisfy the given predicate</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCategories(java.util.List)">setCategories</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>&gt; list)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the list of the categories.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParent(com.nomagic.actions.ActionsManager)">setParent</a><wbr/>(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> parent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the actions manager parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#updateCommandKeysFrom(com.nomagic.actions.ActionsManager)">updateCommandKeysFrom</a><wbr/>(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#updateShortcutsFrom(com.nomagic.actions.ActionsManager)"><code>updateShortcutsFrom(ActionsManager)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateShortcutsFrom(com.nomagic.actions.ActionsManager)">updateShortcutsFrom</a><wbr/>(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Takes all action from the given manager with modified shortcuts and overwrites the shortcuts for actions in this manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateStateForAllActions()">updateStateForAllActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls updateState() method for all inner actions.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="SHORTCUTS_MODIFIED">
<h3>SHORTCUTS_MODIFIED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHORTCUTS_MODIFIED</span></div>
<div class="block">A key for Boolean which marks action with modified shortcuts in UI</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../constant-values.html#com.nomagic.actions.ActionsManager.SHORTCUTS_MODIFIED">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.actions.ActionsManager)">
<h3>ActionsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsManager</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> parent)</span></div>
<div class="block">Creates the actions manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent of the actions manager. May be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ActionsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ActionsManager</span>()</div>
<div class="block">Creates the actions manager.</div>
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
<section class="detail" id="markShortcutsModified(javax.swing.Action)">
<h3>markShortcutsModified</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">markShortcutsModified</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Action.html" title="class or interface in javax.swing">Action</a> action)</span></div>
<div class="block">Add a mark that shortcuts are modified externally in UI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategories()">
<h3>getCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>&gt;</span> <span class="element-name">getCategories</span>()</div>
<div class="block">Returns the list of the categories.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the cloned list of the categories.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionsCategoryRecursively(java.util.List,java.lang.String)">
<h3>getActionsCategoryRecursively</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></span> <span class="element-name">getActionsCategoryRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>&gt; categories,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Recursively finds an action category with a given id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>categories</code> - categories to search.</dd>
<dd><code>id</code> - id of a category to find.</dd>
<dt>Returns:</dt>
<dd>found action category or null if it is not found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCategories(java.util.List)">
<h3>setCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCategories</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a>&gt; list)</span></div>
<div class="block">Sets the list of the categories.
 All old actions will be unregistered and new registered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>list</code> - the list of the categories.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCategory(com.nomagic.actions.ActionsCategory)">
<h3>addCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCategory</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</span></div>
<div class="block">Adds the given category to the manager. The actions from the given
 category will be registered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - the given category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCategory(int,com.nomagic.actions.ActionsCategory)">
<h3>addCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCategory</span><wbr/><span class="parameters">(int index,
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</span></div>
<div class="block">Adds the given category to the manager. The actions from the given
 category will be registered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - index where category will be added.</dd>
<dd><code>category</code> - the given category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeCategory(com.nomagic.actions.ActionsCategory)">
<h3>removeCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCategory</span><wbr/><span class="parameters">(<a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</span></div>
<div class="block">Removes the given category from the manager.
 The actions from the given category will be unregistered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - the given category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCategory(java.lang.String,com.nomagic.actions.ActionsCategory,boolean)">
<h3>addCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCategory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> relatedCategoryID,
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 boolean addAfter)</span></div>
<div class="block">Adds the given category to the manager. The actions from the given
 category will be registered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relatedCategoryID</code> - related category id</dd>
<dd><code>category</code> - the given category</dd>
<dd><code>addAfter</code> - add after related category or before related category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCategory(com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory,boolean)">
<h3>addCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCategory</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> relatedCategory,
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category,
 boolean addAfter)</span></div>
<div class="block">Adds the given category to the manager. The actions from the given
 category will be registered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relatedCategory</code> - related category</dd>
<dd><code>category</code> - the given category</dd>
<dd><code>addAfter</code> - add after related category or before related category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategory(java.lang.String)">
<h3>getCategory</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></span> <span class="element-name">getCategory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Returns the category with given id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the id of the category.</dd>
<dt>Returns:</dt>
<dd>the category with given id or null if this manager does not have such category.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateCommandKeysFrom(com.nomagic.actions.ActionsManager)">
<h3>updateCommandKeysFrom</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateCommandKeysFrom</span><wbr/><span class="parameters">(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#updateShortcutsFrom(com.nomagic.actions.ActionsManager)"><code>updateShortcutsFrom(ActionsManager)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="updateShortcutsFrom(com.nomagic.actions.ActionsManager)">
<h3>updateShortcutsFrom</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateShortcutsFrom</span><wbr/><span class="parameters">(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block">Takes all action from the given manager with modified shortcuts and overwrites the shortcuts for actions in this manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the given manager.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#SHORTCUTS_MODIFIED"><code>SHORTCUTS_MODIFIED</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllActions()">
<h3>getAllActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</span> <span class="element-name">getAllActions</span>()</div>
<div class="block">Returns the list of all actions registered in this manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the list of all registered actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeIf(java.util.function.Predicate)">
<h3>removeIf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeIf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; filter)</span></div>
<div class="block">Removes all of the actions of this manager that satisfy the given predicate</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filter</code> - given predicate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEachIncludingSelf(java.util.function.Consumer)">
<h3>forEachIncludingSelf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEachIncludingSelf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</span></div>
<div class="block">Performs the given consumer for each owned action including self. Owned actions should not be added/removed inside consumer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>consumer</code> - the action to be performed for each NMAction</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="NMAction.html#forEachIncludingSelf(java.util.function.Consumer)"><code>NMAction.forEachIncludingSelf(Consumer)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEach(java.util.function.Consumer)">
<h3>forEach</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEach</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt; consumer)</span></div>
<div class="block">Performs the given consumer for each owned action. Owned actions should not be added/removed inside consumer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>consumer</code> - the action to be performed for each NMAction</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="NMAction.html#forEach(java.util.function.Consumer)"><code>NMAction.forEach(Consumer)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty()">
<h3>isEmpty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEmpty</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this manager currently contains no actions, false if there are actions.
 Parent actions are not considered</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllOrderedActions(boolean)">
<h3>getAllOrderedActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</span> <span class="element-name">getAllOrderedActions</span><wbr/><span class="parameters">(boolean includeCategories)</span></div>
<div class="block">Returns the list if all ordered actions registered in this manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>includeCategories</code> - If true, then ActionsCategories will be included in the list</dd>
<dt>Returns:</dt>
<dd>the list of all registered actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAllActions()">
<h3>removeAllActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAllActions</span>()</div>
<div class="block">Removes all actions.</div>
</section>
</li>
<li>
<section class="detail" id="getActionFor(javax.swing.KeyStroke)">
<h3>getActionFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></span> <span class="element-name">getActionFor</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> stroke)</span></div>
<div class="block">Returns the action for given stroke. If this manager does not have such
 action, it looks in the parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stroke</code> - stroke</dd>
<dt>Returns:</dt>
<dd>the action for given stroke or null if there are no action with such stroke.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionFor(java.lang.String)">
<h3>getActionFor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></span> <span class="element-name">getActionFor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Returns the action for given id. If this manager does not have such
 action, it looks in the parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - action id</dd>
<dt>Returns:</dt>
<dd>the action for given id or null if there are no action with such id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIdToActionMap()">
<h3>getIdToActionMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</span> <span class="element-name">getIdToActionMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">clone</span>()</div>
<div class="block">Clones the manager.
 Does deep clone.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>cloned instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dropCache()">
<h3>dropCache</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dropCache</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setParent(com.nomagic.actions.ActionsManager)">
<h3>setParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> parent)</span></div>
<div class="block">Sets the actions manager parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the new parent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParent()">
<h3>getParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">getParent</span>()</div>
<div class="block">Returns the actions manager parent.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionParent(com.nomagic.actions.NMAction)">
<h3>getActionParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a></span> <span class="element-name">getActionParent</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Returns parent action for given action. Searches for the action object itself, if a provided object is not found actions are compared
 using equals(by action ID).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - the given action.</dd>
<dt>Returns:</dt>
<dd>parent of given action.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeCopy()">
<h3>makeCopy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">makeCopy</span>()</div>
<div class="block">Copies this manager and adds property change listeners to all actions in
 order to have the same action state in source and copy.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>copied manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateStateForAllActions()">
<h3>updateStateForAllActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateStateForAllActions</span>()</div>
<div class="block">Calls updateState() method for all inner actions.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="NMAction.html#updateState()"><code>NMAction.updateState()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastActionsCategory()">
<h3>getLastActionsCategory</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a></span> <span class="element-name">getLastActionsCategory</span>()</div>
<div class="block">Returns last category by order.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>last category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAction(java.lang.String)">
<h3>removeAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAction</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> actionID)</span></div>
<div class="block">Removes  action with given ID from this manager. Searches for action parent, removes action from it's parent
 and removes parent if it does not have any more actions.
 If given ID is id of root category(added into manager), removes this category.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionID</code> - actionID id of action to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAction(com.nomagic.actions.NMAction)">
<h3>removeAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAction</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Removes action from this manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAction(com.nomagic.actions.NMAction,com.nomagic.actions.NMAction)">
<h3>removeAction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAction</span><wbr/><span class="parameters">(<a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 @CheckForNull
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> parent)</span></div>
<div class="block">Removes  action with given ID from this manager. Takes given parent, removes action from it's parent
 and removes parent if it does not have any more actions.
 If given ID is id of root category(added into manager), removes this category.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action to remove.</dd>
<dd><code>parent</code> - parent of action to remove from.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)">
<h3>addActionNearTheGiven</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addActionNearTheGiven</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> givenID,
 boolean addAfter,
 @CheckForNull
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">Adds given action near the action with the given id. The given action will be added into the same parent as action with givenID.
 The position of the given action will be above or below the "givenID".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>givenID</code> - the id of action to add near</dd>
<dd><code>addAfter</code> - add after or before "givenID"</dd>
<dd><code>action</code> - the action to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction,com.nomagic.actions.ActionsCategory)">
<h3>addActionNearTheGiven</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addActionNearTheGiven</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> givenID,
 boolean addAfter,
 @CheckForNull
 <a href="NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 @CheckForNull
 <a href="ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> defaultCategory)</span></div>
<div class="block">Adds given action near the action with the given id. The given action will be added into the same parent as action with givenID.
 The position of the given action will be above or below the "givenID".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>givenID</code> - the id of action to add near</dd>
<dd><code>addAfter</code> - add after or before "givenID"</dd>
<dd><code>action</code> - the action to add</dd>
<dd><code>defaultCategory</code> - category to add action into if action with givenID does not exist. Last category from manager is used if defaultCategory is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="constructNoneAction()">
<h3>constructNoneAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../magicdraw/actions/MDAction.html" title="class in com.nomagic.magicdraw.actions">MDAction</a></span> <span class="element-name">constructNoneAction</span>()</div>
<div class="block">Constructs a none action.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created none action.</dd>
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
