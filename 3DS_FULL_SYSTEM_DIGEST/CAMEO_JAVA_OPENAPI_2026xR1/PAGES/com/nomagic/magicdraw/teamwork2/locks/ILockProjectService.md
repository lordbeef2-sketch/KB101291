# JAVA OPENAPI: ILockProjectService (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/teamwork2/locks/ILockProjectService.html
- source_path: `com/nomagic/magicdraw/teamwork2/locks/ILockProjectService.html`
- source_sha256: `c13624b9aea0549e8d48b0d933129d38d09430e4c96fc759e121e2d383632456`
- captured_utc: `2026-07-14T16:45:48.027641+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.teamwork2.locks](package-summary.html)

## Interface ILockProjectService

All Known Implementing Classes:
`[LockService](LockService.html)`

@OpenApiAllpublic interfaceILockProjectService

Project data locking service. Provides api to check, request and release locks on various project data

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static class`
`[ILockProjectService.LockOptions](ILockProjectService.LockOptions.html)`
Locking operation options
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`boolean`
`[canBeDecompositionLocked](#canBeDecompositionLocked(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Check if project decomposition can be locked by current user
`boolean`
`[canBeDecompositionUnlocked](#canBeDecompositionUnlocked(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Check if project decomposition can be unlocked by current user
`boolean`
`[canBeLocked](#canBeLocked(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)`
Check if given usage can be locked by current user.
`boolean`
`[canBeLocked](#canBeLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if given element can be locked by current user.
`boolean`
`[canBeOptionsLocked](#canBeOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)`
Check if options can be locked.
`boolean`
`[canBeOptionsUnlocked](#canBeOptionsUnlocked(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)`
Check if options can be unlocked.
`boolean`
`[canBeUnlocked](#canBeUnlocked(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)`
Check if given usage can be unlocked by current user.
`boolean`
`[canBeUnlocked](#canBeUnlocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if given element can be unlocked by current user.
`[LockInfo](LockInfo.html)`
`[getDecompositionLock](#getDecompositionLock(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Return decomposition lock
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getLockedBy](#getLockedBy(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) user)`
Collect all elements locked by given user
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getLockedByMe](#getLockedByMe())()`
Collect all elements locked by current user
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getLockedElements](#getLockedElements())()`
Returns collection of locked elements.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getLockedElementUsers](#getLockedElementUsers())()`
Returns collection of locked elements owners in the server.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)>`
`[getLockedModules](#getLockedModules())()`
Collect all usages locked by any user
`[LockInfo](LockInfo.html)`
`[getLockInfo](#getLockInfo(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)`
Return lock information on given usage
`[LockInfo](LockInfo.html)`
`[getLockInfo](#getLockInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return lock information on given element
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)>`
`[getModulesLockedBy](#getModulesLockedBy(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) user)`
Collect all usages locked by given user
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)>`
`[getModulesLockedByMe](#getModulesLockedByMe())()`
Collect all usages locked by current user
`[LockInfo](LockInfo.html)`
`[getOptionsLock](#getOptionsLock(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)`
Get options lock data.
`boolean`
`[hasLockedBy](#hasLockedBy(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) user)`
Checks if there are any locks for specified user
`boolean`
`[hasLockedElements](#hasLockedElements())()`
Check if project has some locked data
`boolean`
`[hasPermissionToLock](#hasPermissionToLock(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check permissions for element.
`boolean`
`[isDecompositionLocked](#isDecompositionLocked(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Check if decomposition model is locked
`boolean`
`[isDecompositionLockedByMe](#isDecompositionLockedByMe(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Checks for decomposition model lock
`boolean`
`[isLocked](#isLocked(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)`
Check if usage is locked
`boolean`
`[isLocked](#isLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if element is locked
`boolean`
`[isLockedBy](#isLockedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) user)`
Check if given element is locked by a user
`boolean`
`[isLockedByMe](#isLockedByMe(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)`
Check if the given usage has lock on it, and this lock owner is current user.
`boolean`
`[isLockedByMe](#isLockedByMe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Check if the given element has lock on it, and this lock owner is current user.
`boolean`
`[isOptionsLocked](#isOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)`
Check if given options are locked.
`boolean`
`[isOptionsLockedByMe](#isOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)`
Check if options locked by current user.
`default boolean`
`[lockElements](#lockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean lockRecursively,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Lock given elements.
`boolean`
`[lockElements](#lockElements(java.util.Collection,com.nomagic.magicdraw.teamwork2.locks.ILockProjectService.LockOptions,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [ILockProjectService.LockOptions](ILockProjectService.LockOptions.html) options,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Lock given elements.
`default boolean`
`[lockElements](#lockElements(java.util.Collection,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Lock given elements.
`boolean`
`[lockModules](#lockModules(java.util.Collection,boolean,boolean,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> moduleUsages,
 boolean checkForNewVersion,
 boolean lockAsManyAsPossible,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Lock given usages.
`boolean`
`[lockModules](#lockModules(java.util.Collection,boolean,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> moduleUsages,
 boolean checkForNewVersion,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Lock given usages.
`void`
`[setCacheOptionsLock](#setCacheOptionsLock(boolean))(boolean value)`
Sets whether options lock should be cached or not.
`boolean`
`[setDecompositionLockedByMe](#setDecompositionLockedByMe(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject project,
 boolean locked,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Lock/Unlock decomposition model.
`boolean`
`[setOptionsLockedByMe](#setOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String,boolean,com.nomagic.task.ProgressStatus))(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options,
 boolean locked,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Lock/unlock options.
`boolean`
`[unlockElements](#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean unlockRecursively,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Unlock given elements.
`boolean`
`[unlockElements](#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean unlockRecursively,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean unlockOnlyMyLocks)`
Unlock given elements.
`boolean`
`[unlockElements](#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean unlockRecursively,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementsToUnlock,
 boolean unlockOnlyMyLocks)`
Unlock given elements.
`boolean`
`[unlockElements](#unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Unlock given elements.
`boolean`
`[unlockElements](#unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean unlockOnlyMyLocks)`
Unlock given elements.
`boolean`
`[unlockModules](#unlockModules(java.util.Collection,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> moduleUsages,
 [ProgressStatus](../../../task/ProgressStatus.html) status)`
Unlock given usages.
`void`
`[updateLocks](#updateLocks(com.nomagic.task.ProgressStatus))([ProgressStatus](../../../task/ProgressStatus.html) status)`
Update local information about locks from server.

============ METHOD DETAIL ========== 
Method Details
isLocked
boolean isLocked([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if element is locked
Parameters:
`element` - element
Returns:
true if element is locked
hasLockedElements
boolean hasLockedElements()
Check if project has some locked data
Returns:
true if locked data exists in project
isLockedBy
boolean isLockedBy([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) user)
Check if given element is locked by a user
Parameters:
`element` - element
`user` - user
Returns:
true if user has lock on this element
getLockInfo
@CheckForNull[LockInfo](LockInfo.html) getLockInfo([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return lock information on given element
Parameters:
`element` - element
Returns:
lock information or null of element is not locked
getLockInfo
[LockInfo](LockInfo.html) getLockInfo([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)
Return lock information on given usage
Parameters:
`moduleUsage` - module usage
Returns:
lock information or null of usage is not locked
isLocked
boolean isLocked([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)
Check if usage is locked
Parameters:
`moduleUsage` - usage
Returns:
true is usage is locked
isLockedByMe
boolean isLockedByMe([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if the given element has lock on it, and this lock owner is current user.
Parameters:
`element` - element to check for locked user.
Returns:
true when given element is locked by the current user.
isLockedByMe
boolean isLockedByMe([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)
Check if the given usage has lock on it, and this lock owner is current user.
Parameters:
`moduleUsage` - usage to check for locked user.
Returns:
true when given usage is locked by the current user.
hasLockedBy
boolean hasLockedBy([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) user)
Checks if there are any locks for specified user
Parameters:
`user` - user
Returns:
`true - when there are locks for specified user, otherwise - false`
getLockedBy
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getLockedBy([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) user)
Collect all elements locked by given user
Parameters:
`user` - user
Returns:
locked elements
getLockedByMe
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getLockedByMe()
Collect all elements locked by current user
Returns:
locked elements
getModulesLockedBy
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> getModulesLockedBy(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) user)
Collect all usages locked by given user
Parameters:
`user` - user
Returns:
locked usages
getModulesLockedByMe
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> getModulesLockedByMe()
Collect all usages locked by current user
Returns:
locked usages
getLockedModules
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> getLockedModules()
Collect all usages locked by any user
Returns:
locked usages
canBeLocked
boolean canBeLocked([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if given element can be locked by current user. Includes checking resource lock, granularity,
 user rights and if object is locked already.
Parameters:
`element` - element
Returns:
true if user can lock given element.
canBeUnlocked
boolean canBeUnlocked([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check if given element can be unlocked by current user. Includes checking resource lock, granularity,
 user rights and if object is locked already.
Parameters:
`element` - element
Returns:
true if user can unlock given element.
canBeLocked
boolean canBeLocked([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)
Check if given usage can be locked by current user. Includes checking resource lock, granularity,
 user rights and if object is locked already.
Parameters:
`moduleUsage` - usage
Returns:
true if user can lock given usage.
canBeUnlocked
boolean canBeUnlocked([ModuleUsage](../../core/modules/ModuleUsage.html) moduleUsage)
Check if given usage can be unlocked by current user. Includes checking resource lock, granularity,
 user rights and if object is locked already.
Parameters:
`moduleUsage` - usage
Returns:
true if user can unlock given usage.
lockElements
default boolean lockElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean lockRecursively,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Lock given elements. Can lock children of given elements also.
Parameters:
`elements` - elements
`lockRecursively` - lock children recursively
`status` - progress status
Returns:
true if all given elements where locked
lockElements
default boolean lockElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Lock given elements. Children are not locked
Parameters:
`elements` - elements
`status` - progress status
Returns:
true if all elements where locked
lockElements
boolean lockElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [ILockProjectService.LockOptions](ILockProjectService.LockOptions.html) options,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Lock given elements. Children are not locked
Parameters:
`elements` - elements
`options` - lock operation options
`status` - progress status
Returns:
true if all elements where locked
unlockElements
boolean unlockElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean unlockRecursively,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean unlockOnlyMyLocks)
Unlock given elements. Can unlock children of given elements also.
Parameters:
`elements` - elements
`unlockRecursively` - children recursively
`status` - progress status
`unlockOnlyMyLocks` - unlock only my locked elements (used for ESI projects)
Returns:
true if all given elements where unlocked
unlockElements
boolean unlockElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean unlockRecursively,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elementsToUnlock,
 boolean unlockOnlyMyLocks)
Unlock given elements. Can unlock children of given elements also.
Parameters:
`elements` - elements
`unlockRecursively` - children recursively
`status` - progress status
`elementsToUnlock` - elements to unlock
`unlockOnlyMyLocks` - unlock only my locked elements (used for ESI projects)
Returns:
true if all given elements where unlocked
unlockModules
boolean unlockModules([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> moduleUsages,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Unlock given usages.
Parameters:
`moduleUsages` - elements
`status` - progress status
Returns:
true if all usages where unlocked
lockModules
boolean lockModules([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> moduleUsages,
 boolean checkForNewVersion,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Lock given usages.
Parameters:
`moduleUsages` - elements
`checkForNewVersion` - check if new project version exists on server before locking
`status` - progress status
Returns:
true if all usages where locked
lockModules
boolean lockModules([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> moduleUsages,
 boolean checkForNewVersion,
 boolean lockAsManyAsPossible,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Lock given usages.
Parameters:
`moduleUsages` - elements
`checkForNewVersion` - check if new project version exists on server before locking
`lockAsManyAsPossible` - stop without locking any usages if there is at least one usage which cannot be locked
`status` - progress status
Returns:
true if all usages where locked
updateLocks
void updateLocks(@CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Update local information about locks from server. In other words retrieve latest locks information from server.
Parameters:
`status` - progress
getLockedElements
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getLockedElements()
Returns collection of locked elements.
Returns:
locked elements
getLockedElementUsers
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getLockedElementUsers()
Returns collection of locked elements owners in the server.
Returns:
users whose have locked elements in the server
isDecompositionLockedByMe
boolean isDecompositionLockedByMe(com.nomagic.ci.persistence.IProject project)
Checks for decomposition model lock
Parameters:
`project` - project which decomposition model is locked
Returns:
true if given project decomposition model is locked by me
isDecompositionLocked
boolean isDecompositionLocked(com.nomagic.ci.persistence.IProject project)
Check if decomposition model is locked
Parameters:
`project` - project
Returns:
true if decomposition is locked by any user
setDecompositionLockedByMe
boolean setDecompositionLockedByMe(com.nomagic.ci.persistence.IProject project,
 boolean locked,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Lock/Unlock decomposition model.
Parameters:
`project` - project which decomposition model is locked
`locked` - new lock value
`status` - progress status
Returns:
true if decomposition is locked by me
getDecompositionLock
[LockInfo](LockInfo.html) getDecompositionLock(com.nomagic.ci.persistence.IProject project)
Return decomposition lock
Parameters:
`project` - project
Returns:
lock or null
canBeDecompositionLocked
boolean canBeDecompositionLocked(com.nomagic.ci.persistence.IProject project)
Check if project decomposition can be locked by current user
Parameters:
`project` - project
Returns:
true if can be locked
canBeDecompositionUnlocked
boolean canBeDecompositionUnlocked(com.nomagic.ci.persistence.IProject project)
Check if project decomposition can be unlocked by current user
Parameters:
`project` - project
Returns:
true if can be unlocked
isOptionsLocked
boolean isOptionsLocked(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)
Check if given options are locked.
Parameters:
`project` - project.
`options` - options.
Returns:
true - locked.
isOptionsLockedByMe
boolean isOptionsLockedByMe(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)
Check if options locked by current user.
Parameters:
`project` - project.
`options` - options.
Returns:
true - locked by current user.
canBeOptionsLocked
boolean canBeOptionsLocked(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)
Check if options can be locked.
Parameters:
`project` - project.
`options` - options.
Returns:
true if can be locked.
canBeOptionsUnlocked
boolean canBeOptionsUnlocked(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)
Check if options can be unlocked.
Parameters:
`project` - project.
`options` - options.
Returns:
true if can be unlocked.
setOptionsLockedByMe
boolean setOptionsLockedByMe(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options,
 boolean locked,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Lock/unlock options.
Parameters:
`project` - project.
`options` - option
`locked` - true to lock, false to unlock
`status` - status.
Returns:
true if operation succeeds.
getOptionsLock
@CheckForNull[LockInfo](LockInfo.html) getOptionsLock(com.nomagic.ci.persistence.IProject project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) options)
Get options lock data.
Parameters:
`project` - project
`options` - options
Returns:
lock.
setCacheOptionsLock
void setCacheOptionsLock(boolean value)
Sets whether options lock should be cached or not.
Parameters:
`value` - if true then options lock should be cached on the first call.
unlockElements
boolean unlockElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 boolean unlockOnlyMyLocks)
Unlock given elements. Can unlock children of given elements also.
Parameters:
`elements` - elements
`status` - progress status
`unlockOnlyMyLocks` - unlock only my locked elements (used for ESI projects)
Returns:
true if all given elements where unlocked
unlockElements
boolean unlockElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean unlockRecursively,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Unlock given elements. Can unlock children of given elements also.
Parameters:
`elements` - elements
`unlockRecursively` - children recursively
`status` - progress status
Returns:
true if all given elements where unlocked
unlockElements
boolean unlockElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status)
Unlock given elements. Children are not unlocked
Parameters:
`elements` - elements
`status` - progress status
Returns:
true if all elements where unlocked
hasPermissionToLock
boolean hasPermissionToLock([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Check permissions for element.
Parameters:
`element` - element to check
Returns:
true because of not available package permissions

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.teamwork2.locks</a></div>
<h1 class="title" title="Interface ILockProjectService">Interface ILockProjectService</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="LockService.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockService</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ILockProjectService</span></div>
<div class="block">Project data locking service. Provides api to check, request and release locks on various project data</div>
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
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ILockProjectService.LockOptions.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService.LockOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Locking operation options</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeDecompositionLocked(com.nomagic.ci.persistence.IProject)">canBeDecompositionLocked</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if project decomposition can be locked by current user</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeDecompositionUnlocked(com.nomagic.ci.persistence.IProject)">canBeDecompositionUnlocked</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if project decomposition can be unlocked by current user</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeLocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">canBeLocked</a><wbr/>(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if given usage can be locked by current user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canBeLocked</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if given element can be locked by current user.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String)">canBeOptionsLocked</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if options can be locked.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeOptionsUnlocked(com.nomagic.ci.persistence.IProject,java.lang.String)">canBeOptionsUnlocked</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if options can be unlocked.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeUnlocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">canBeUnlocked</a><wbr/>(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if given usage can be unlocked by current user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canBeUnlocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canBeUnlocked</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if given element can be unlocked by current user.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LockInfo.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDecompositionLock(com.nomagic.ci.persistence.IProject)">getDecompositionLock</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return decomposition lock</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockedBy(java.lang.String)">getLockedBy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Collect all elements locked by given user</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockedByMe()">getLockedByMe</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Collect all elements locked by current user</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockedElements()">getLockedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns collection of locked elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockedElementUsers()">getLockedElementUsers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns collection of locked elements owners in the server.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockedModules()">getLockedModules</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Collect all usages locked by any user</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LockInfo.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockInfo(com.nomagic.magicdraw.core.modules.ModuleUsage)">getLockInfo</a><wbr/>(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return lock information on given usage</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LockInfo.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getLockInfo</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return lock information on given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModulesLockedBy(java.lang.String)">getModulesLockedBy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Collect all usages locked by given user</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModulesLockedByMe()">getModulesLockedByMe</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Collect all usages locked by current user</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LockInfo.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOptionsLock(com.nomagic.ci.persistence.IProject,java.lang.String)">getOptionsLock</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get options lock data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasLockedBy(java.lang.String)">hasLockedBy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if there are any locks for specified user</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasLockedElements()">hasLockedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if project has some locked data</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPermissionToLock(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasPermissionToLock</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check permissions for element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDecompositionLocked(com.nomagic.ci.persistence.IProject)">isDecompositionLocked</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if decomposition model is locked</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDecompositionLockedByMe(com.nomagic.ci.persistence.IProject)">isDecompositionLockedByMe</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks for decomposition model lock</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">isLocked</a><wbr/>(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if usage is locked</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isLocked</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if element is locked</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLockedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isLockedBy</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if given element is locked by a user</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLockedByMe(com.nomagic.magicdraw.core.modules.ModuleUsage)">isLockedByMe</a><wbr/>(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if the given usage has lock on it, and this lock owner is current user.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isLockedByMe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isLockedByMe</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if the given element has lock on it, and this lock owner is current user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String)">isOptionsLocked</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if given options are locked.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String)">isOptionsLockedByMe</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if options locked by current user.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#lockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">lockElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean lockRecursively,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Lock given elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#lockElements(java.util.Collection,com.nomagic.magicdraw.teamwork2.locks.ILockProjectService.LockOptions,com.nomagic.task.ProgressStatus)">lockElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="ILockProjectService.LockOptions.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService.LockOptions</a> options,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Lock given elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#lockElements(java.util.Collection,com.nomagic.task.ProgressStatus)">lockElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Lock given elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#lockModules(java.util.Collection,boolean,boolean,com.nomagic.task.ProgressStatus)">lockModules</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; moduleUsages,
 boolean checkForNewVersion,
 boolean lockAsManyAsPossible,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Lock given usages.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#lockModules(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">lockModules</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; moduleUsages,
 boolean checkForNewVersion,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Lock given usages.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setCacheOptionsLock(boolean)">setCacheOptionsLock</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets whether options lock should be cached or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDecompositionLockedByMe(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.task.ProgressStatus)">setDecompositionLockedByMe</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 boolean locked,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Lock/Unlock decomposition model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String,boolean,com.nomagic.task.ProgressStatus)">setOptionsLockedByMe</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options,
 boolean locked,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Lock/unlock options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">unlockElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean unlockRecursively,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unlock given elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,boolean)">unlockElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean unlockRecursively,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean unlockOnlyMyLocks)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unlock given elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,java.util.Collection,boolean)">unlockElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean unlockRecursively,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementsToUnlock,
 boolean unlockOnlyMyLocks)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unlock given elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus)">unlockElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unlock given elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus,boolean)">unlockElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean unlockOnlyMyLocks)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unlock given elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#unlockModules(java.util.Collection,com.nomagic.task.ProgressStatus)">unlockModules</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; moduleUsages,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unlock given usages.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#updateLocks(com.nomagic.task.ProgressStatus)">updateLocks</a><wbr/>(<a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Update local information about locks from server.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="isLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLocked</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if element is locked</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element is locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasLockedElements()">
<h3>hasLockedElements</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasLockedElements</span>()</div>
<div class="block">Check if project has some locked data</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if locked data exists in project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLockedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>isLockedBy</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLockedBy</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</span></div>
<div class="block">Check if given element is locked by a user</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dd><code>user</code> - user</dd>
<dt>Returns:</dt>
<dd>true if user has lock on this element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getLockInfo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="LockInfo.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockInfo</a></span> <span class="element-name">getLockInfo</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return lock information on given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>lock information or null of element is not locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockInfo(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>getLockInfo</h3>
<div class="member-signature"><span class="return-type"><a href="LockInfo.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockInfo</a></span> <span class="element-name">getLockInfo</span><wbr/><span class="parameters">(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</span></div>
<div class="block">Return lock information on given usage</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsage</code> - module usage</dd>
<dt>Returns:</dt>
<dd>lock information or null of usage is not locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>isLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLocked</span><wbr/><span class="parameters">(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</span></div>
<div class="block">Check if usage is locked</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsage</code> - usage</dd>
<dt>Returns:</dt>
<dd>true is usage is locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLockedByMe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isLockedByMe</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLockedByMe</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if the given element has lock on it, and this lock owner is current user.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check for locked user.</dd>
<dt>Returns:</dt>
<dd>true when given element is locked by the current user.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLockedByMe(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>isLockedByMe</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isLockedByMe</span><wbr/><span class="parameters">(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</span></div>
<div class="block">Check if the given usage has lock on it, and this lock owner is current user.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsage</code> - usage to check for locked user.</dd>
<dt>Returns:</dt>
<dd>true when given usage is locked by the current user.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasLockedBy(java.lang.String)">
<h3>hasLockedBy</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasLockedBy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</span></div>
<div class="block">Checks if there are any locks for specified user</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>user</code> - user</dd>
<dt>Returns:</dt>
<dd><code>true<code></code> - when there are locks for specified user, otherwise - <code>false<code></code></code></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockedBy(java.lang.String)">
<h3>getLockedBy</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getLockedBy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</span></div>
<div class="block">Collect all elements locked by given user</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>user</code> - user</dd>
<dt>Returns:</dt>
<dd>locked elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockedByMe()">
<h3>getLockedByMe</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getLockedByMe</span>()</div>
<div class="block">Collect all elements locked by current user</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>locked elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModulesLockedBy(java.lang.String)">
<h3>getModulesLockedBy</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt;</span> <span class="element-name">getModulesLockedBy</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</span></div>
<div class="block">Collect all usages locked by given user</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>user</code> - user</dd>
<dt>Returns:</dt>
<dd>locked usages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModulesLockedByMe()">
<h3>getModulesLockedByMe</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt;</span> <span class="element-name">getModulesLockedByMe</span>()</div>
<div class="block">Collect all usages locked by current user</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>locked usages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockedModules()">
<h3>getLockedModules</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt;</span> <span class="element-name">getLockedModules</span>()</div>
<div class="block">Collect all usages locked by any user</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>locked usages</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>canBeLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canBeLocked</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if given element can be locked by current user. Includes checking resource lock, granularity,
 user rights and if object is locked already.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if user can lock given element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeUnlocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>canBeUnlocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canBeUnlocked</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check if given element can be unlocked by current user. Includes checking resource lock, granularity,
 user rights and if object is locked already.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if user can unlock given element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeLocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>canBeLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canBeLocked</span><wbr/><span class="parameters">(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</span></div>
<div class="block">Check if given usage can be locked by current user. Includes checking resource lock, granularity,
 user rights and if object is locked already.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsage</code> - usage</dd>
<dt>Returns:</dt>
<dd>true if user can lock given usage.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeUnlocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>canBeUnlocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canBeUnlocked</span><wbr/><span class="parameters">(<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage)</span></div>
<div class="block">Check if given usage can be unlocked by current user. Includes checking resource lock, granularity,
 user rights and if object is locked already.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsage</code> - usage</dd>
<dt>Returns:</dt>
<dd>true if user can unlock given usage.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">
<h3>lockElements</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">lockElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean lockRecursively,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Lock given elements. Can lock children of given elements also.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>lockRecursively</code> - lock children recursively</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if all given elements where locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lockElements(java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>lockElements</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">lockElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Lock given elements. Children are not locked</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if all elements where locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lockElements(java.util.Collection,com.nomagic.magicdraw.teamwork2.locks.ILockProjectService.LockOptions,com.nomagic.task.ProgressStatus)">
<h3>lockElements</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">lockElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="ILockProjectService.LockOptions.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService.LockOptions</a> options,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Lock given elements. Children are not locked</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>options</code> - lock operation options</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if all elements where locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,boolean)">
<h3>unlockElements</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">unlockElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean unlockRecursively,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean unlockOnlyMyLocks)</span></div>
<div class="block">Unlock given elements. Can unlock children of given elements also.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>unlockRecursively</code> - children recursively</dd>
<dd><code>status</code> - progress status</dd>
<dd><code>unlockOnlyMyLocks</code> - unlock only my locked elements (used for ESI projects)</dd>
<dt>Returns:</dt>
<dd>true if all given elements where unlocked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,java.util.Collection,boolean)">
<h3>unlockElements</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">unlockElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean unlockRecursively,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elementsToUnlock,
 boolean unlockOnlyMyLocks)</span></div>
<div class="block">Unlock given elements. Can unlock children of given elements also.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>unlockRecursively</code> - children recursively</dd>
<dd><code>status</code> - progress status</dd>
<dd><code>elementsToUnlock</code> - elements to unlock</dd>
<dd><code>unlockOnlyMyLocks</code> - unlock only my locked elements (used for ESI projects)</dd>
<dt>Returns:</dt>
<dd>true if all given elements where unlocked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unlockModules(java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>unlockModules</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">unlockModules</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; moduleUsages,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Unlock given usages.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsages</code> - elements</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if all usages where unlocked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lockModules(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">
<h3>lockModules</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">lockModules</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; moduleUsages,
 boolean checkForNewVersion,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Lock given usages.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsages</code> - elements</dd>
<dd><code>checkForNewVersion</code> - check if new project version exists on server before locking</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if all usages where locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lockModules(java.util.Collection,boolean,boolean,com.nomagic.task.ProgressStatus)">
<h3>lockModules</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">lockModules</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; moduleUsages,
 boolean checkForNewVersion,
 boolean lockAsManyAsPossible,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Lock given usages.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsages</code> - elements</dd>
<dd><code>checkForNewVersion</code> - check if new project version exists on server before locking</dd>
<dd><code>lockAsManyAsPossible</code> - stop without locking any usages if there is at least one usage which cannot be locked</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if all usages where locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateLocks(com.nomagic.task.ProgressStatus)">
<h3>updateLocks</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">updateLocks</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Update local information about locks from server. In other words retrieve latest locks information from server.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>status</code> - progress</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockedElements()">
<h3>getLockedElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getLockedElements</span>()</div>
<div class="block">Returns collection of locked elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>locked elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockedElementUsers()">
<h3>getLockedElementUsers</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getLockedElementUsers</span>()</div>
<div class="block">Returns collection of locked elements owners in the server.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>users whose have locked elements in the server</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDecompositionLockedByMe(com.nomagic.ci.persistence.IProject)">
<h3>isDecompositionLockedByMe</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDecompositionLockedByMe</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Checks for decomposition model lock</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which decomposition model is locked</dd>
<dt>Returns:</dt>
<dd>true if given project decomposition model is locked by me</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDecompositionLocked(com.nomagic.ci.persistence.IProject)">
<h3>isDecompositionLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDecompositionLocked</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Check if decomposition model is locked</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if decomposition is locked by any user</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDecompositionLockedByMe(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.task.ProgressStatus)">
<h3>setDecompositionLockedByMe</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">setDecompositionLockedByMe</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 boolean locked,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Lock/Unlock decomposition model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which decomposition model is locked</dd>
<dd><code>locked</code> - new lock value</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if decomposition is locked by me</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDecompositionLock(com.nomagic.ci.persistence.IProject)">
<h3>getDecompositionLock</h3>
<div class="member-signature"><span class="return-type"><a href="LockInfo.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockInfo</a></span> <span class="element-name">getDecompositionLock</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Return decomposition lock</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>lock or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeDecompositionLocked(com.nomagic.ci.persistence.IProject)">
<h3>canBeDecompositionLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canBeDecompositionLocked</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Check if project decomposition can be locked by current user</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if can be locked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeDecompositionUnlocked(com.nomagic.ci.persistence.IProject)">
<h3>canBeDecompositionUnlocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canBeDecompositionUnlocked</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Check if project decomposition can be unlocked by current user</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if can be unlocked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>isOptionsLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isOptionsLocked</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</span></div>
<div class="block">Check if given options are locked.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
<dd><code>options</code> - options.</dd>
<dt>Returns:</dt>
<dd>true - locked.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>isOptionsLockedByMe</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isOptionsLockedByMe</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</span></div>
<div class="block">Check if options locked by current user.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
<dd><code>options</code> - options.</dd>
<dt>Returns:</dt>
<dd>true - locked by current user.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>canBeOptionsLocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canBeOptionsLocked</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</span></div>
<div class="block">Check if options can be locked.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
<dd><code>options</code> - options.</dd>
<dt>Returns:</dt>
<dd>true if can be locked.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canBeOptionsUnlocked(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>canBeOptionsUnlocked</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canBeOptionsUnlocked</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</span></div>
<div class="block">Check if options can be unlocked.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
<dd><code>options</code> - options.</dd>
<dt>Returns:</dt>
<dd>true if can be unlocked.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String,boolean,com.nomagic.task.ProgressStatus)">
<h3>setOptionsLockedByMe</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">setOptionsLockedByMe</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options,
 boolean locked,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Lock/unlock options.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
<dd><code>options</code> - option</dd>
<dd><code>locked</code> - true to lock, false to unlock</dd>
<dd><code>status</code> - status.</dd>
<dt>Returns:</dt>
<dd>true if operation succeeds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptionsLock(com.nomagic.ci.persistence.IProject,java.lang.String)">
<h3>getOptionsLock</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="LockInfo.html" title="class in com.nomagic.magicdraw.teamwork2.locks">LockInfo</a></span> <span class="element-name">getOptionsLock</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> options)</span></div>
<div class="block">Get options lock data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>options</code> - options</dd>
<dt>Returns:</dt>
<dd>lock.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCacheOptionsLock(boolean)">
<h3>setCacheOptionsLock</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setCacheOptionsLock</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets whether options lock should be cached or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - if true then options lock should be cached on the first call.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus,boolean)">
<h3>unlockElements</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">unlockElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 boolean unlockOnlyMyLocks)</span></div>
<div class="block">Unlock given elements. Can unlock children of given elements also.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>status</code> - progress status</dd>
<dd><code>unlockOnlyMyLocks</code> - unlock only my locked elements (used for ESI projects)</dd>
<dt>Returns:</dt>
<dd>true if all given elements where unlocked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">
<h3>unlockElements</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">unlockElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean unlockRecursively,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Unlock given elements. Can unlock children of given elements also.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>unlockRecursively</code> - children recursively</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if all given elements where unlocked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>unlockElements</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">unlockElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">Unlock given elements. Children are not unlocked</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>status</code> - progress status</dd>
<dt>Returns:</dt>
<dd>true if all elements where unlocked</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPermissionToLock(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hasPermissionToLock</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPermissionToLock</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Check permissions for element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dt>Returns:</dt>
<dd>true because of not available package permissions</dd>
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
