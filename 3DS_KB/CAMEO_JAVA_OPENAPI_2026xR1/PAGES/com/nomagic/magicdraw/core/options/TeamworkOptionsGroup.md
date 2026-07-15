# JAVA OPENAPI: TeamworkOptionsGroup (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/options/TeamworkOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/TeamworkOptionsGroup.html`
- source_sha256: `deda821a2ef83f92f6d57964c62ee5e0ee068df48b26ae58841059b2f5c82f97`
- captured_utc: `2026-07-14T16:45:31.686424+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class TeamworkOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
com.nomagic.magicdraw.core.options.VersionedOptionsGroup
com.nomagic.magicdraw.core.options.TeamworkOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classTeamworkOptionsGroup
extends com.nomagic.magicdraw.core.options.VersionedOptionsGroup

Teamwork options.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final boolean`
`[DEFAULT_NEW_PROJECT_VERSION_CHECK](#DEFAULT_NEW_PROJECT_VERSION_CHECK)`
Default value for *New Project Version Notification*
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS](#DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS)`

`static final int`
`[DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX](#DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX)`
Default setting when to show notification about available project usages updates to latest version
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INCLUDE_VERSION_INTO_ELEMENT_URL_ASK](#INCLUDE_VERSION_INTO_ELEMENT_URL_ASK)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE](#INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE](#INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE)`

`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)`
`[PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES](#PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES)`
List of options when to show notification about available project usages updates to latest version
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROJECTS_TREE_TABLE_MODE_FLAT](#PROJECTS_TREE_TABLE_MODE_FLAT)`
Mode of teamwork projects tree table when only projects are displayed in
 flat list.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROJECTS_TREE_TABLE_MODE_ORIGINAL](#PROJECTS_TREE_TABLE_MODE_ORIGINAL)`
Mode of teamwork projects tree table when categories and projects are
 displayed in tree form, no presentation modifications are made to
 original structure
`static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)`
`[USERS_REPRESENTATION_CHOICES](#USERS_REPRESENTATION_CHOICES)`
List of options how to display users
`static final int`
`[USERS_REPRESENTATION_EMAIL](#USERS_REPRESENTATION_EMAIL)`
Display user email option
`static final int`
`[USERS_REPRESENTATION_FULL_NAME](#USERS_REPRESENTATION_FULL_NAME)`
Display full user name option
`static final int`
`[USERS_REPRESENTATION_USER_NAME](#USERS_REPRESENTATION_USER_NAME)`
Display user name option
Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`CURRENT_EXPORTER_VERSION`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TeamworkOptionsGroup](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[afterLoad](#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean))(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)`

`void`
`[clearMUUserPassword](#clearMUUserPassword())()`
Clears user password to MU server
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getAuthServerName](#getAuthServerName())()`
gets Last used authentication server name
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getAuthServerNames](#getAuthServerNames())()`
Returns the list of authentication server names, which where entered by user, and successfully connected.
`com.nomagic.ui.banners.Banner`
`[getBanner](#getBanner())()`

`boolean`
`[getCreateMountRelationshipsOnImportToCEDW](#getCreateMountRelationshipsOnImportToCEDW())()`
Gets value of this property.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getDefaultServerNames](#getDefaultServerNames())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getIncludeVersionIntoURLMode](#getIncludeVersionIntoURLMode())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getLastCameoResourceId](#getLastCameoResourceId())()`
Returns last cameo resource ID.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getLastExpandedCategories](#getLastExpandedCategories())()`
Gets collection of identifiers of categories that were recently expanded.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getLastExpandedProjectUsagesCategories](#getLastExpandedProjectUsagesCategories())()`
Gets collection of identifiers of project usages categories that were recently expanded.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getLastSelectedEsiOfflineServerID](#getLastSelectedEsiOfflineServerID())()`
Gets last selected esi offline server.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getLastUsedEsiBranches](#getLastUsedEsiBranches())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getLoginToken](#getLoginToken())()`
gets login token to server
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMUServerName](#getMUServerName())()`
gets Last used server name
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMUUserLogin](#getMUUserLogin())()`
gets user login to MU server
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMUUserPassword](#getMUUserPassword())()`
gets user password to MU server
`int`
`[getNewProjectVersionCheckInterval](#getNewProjectVersionCheckInterval())()`
Returns currently selected interval between version checks.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getProjectsTreeTableMode](#getProjectsTreeTableMode())()`
Gets the teamwork projects tree table display mode.
`int`
`[getProjectUsagesUpdateNotification](#getProjectUsagesUpdateNotification())()`
Gets when to show notification about available project usages updates to latest version.
`int`
`[getRepresentationOfUsers](#getRepresentationOfUsers())()`
Gets how to display users
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getServerNames](#getServerNames())()`
Returns the list of server names, which where entered by user, and successfully connected.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getWebAppServerUrl](#getWebAppServerUrl())()`
Gets WebApp URL.
`boolean`
`[isAutoCommitOnProjectMigration](#isAutoCommitOnProjectMigration())()`
Determines whether projects should be auto-commit after project migration
 to a new version.
`boolean`
`[isAutoLoginToMU](#isAutoLoginToMU())()`
is login to MU server auto
`boolean`
`[isEmptyTeamworkProjectsCategoriesVisible](#isEmptyTeamworkProjectsCategoriesVisible())()`
Indicates if teamwork projects tree table shall display an empty
 categories as well.
`boolean`
`[isEnable3DExperience](#isEnable3DExperience())()`

`boolean`
`[isEnableLockingWithoutForceUpdate](#isEnableLockingWithoutForceUpdate())()`
Determines whether elements can be locked without update project.
`boolean`
`[isKeepLocks](#isKeepLocks())()`

`boolean`
`[isNewProjectVersionCheckEnabled](#isNewProjectVersionCheckEnabled())()`
Method checks whether the *New Project Version Notification*
 property is enabled
`boolean`
`[isRememberServerBetweenSessions](#isRememberServerBetweenSessions())()`
Is server will be remembered between sessions
`boolean`
`[isRememberUserNameBetweenSessions](#isRememberUserNameBetweenSessions())()`
Is entered user login name will be remembered between sessions.
`boolean`
`[isShowModuleVersionsConflictWarning](#isShowModuleVersionsConflictWarning())()`

`boolean`
`[isSSOLoginTabVisible](#isSSOLoginTabVisible())()`
Determines whether sso login tab should be visible.
`boolean`
`[isUseSecureConnection](#isUseSecureConnection())()`

`void`
`[setAuthServerName](#setAuthServerName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
sets server name as a last used server name.
`void`
`[setAuthServerNames](#setAuthServerNames(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> serverNames)`
Setter for Single Sign On server list (server names)
`void`
`[setAutoCommitOnProjectMigration](#setAutoCommitOnProjectMigration(boolean))(boolean autoCommit)`
Sets new value for the [`autoCommitOnProjectMigration`](#isAutoCommitOnProjectMigration()) property
`void`
`[setAutoLoginToMU](#setAutoLoginToMU(boolean))(boolean log)`
sets auto login to MU server
`void`
`[setCreateMountRelationshipsOnImportToCEDW](#setCreateMountRelationshipsOnImportToCEDW(boolean))(boolean enable)`
Sets new value for this property.
`void`
`[setDefaultValues](#setDefaultValues())()`
Sets default values for the properties contained in this group.
`void`
`[setEmptyTeamworkProjectsCategoriesVisible](#setEmptyTeamworkProjectsCategoriesVisible(boolean))(boolean visible)`
Sets if teamwork projects tree table shall display an empty categories as
 well
`void`
`[setEnable3DExperience](#setEnable3DExperience(boolean))(boolean value)`

`void`
`[setEnableLockingWithoutForceUpdate](#setEnableLockingWithoutForceUpdate(boolean))(boolean enable)`
Sets new value for the [`isEnableLockingWithoutForceUpdate()`](#isEnableLockingWithoutForceUpdate()) property
`void`
`[setIncludeVersionIntoURLMode](#setIncludeVersionIntoURLMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setKeepLocks](#setKeepLocks(boolean))(boolean keepLocks)`

`void`
`[setLastCameoResourceId](#setLastCameoResourceId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Sets last used cameo resource(project) ID.
`void`
`[setLastExpandedCategories](#setLastExpandedCategories(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> categoryIds)`
Sets collection of identifiers of categories that were recently expanded.
`void`
`[setLastExpandedProjectUsagesCategories](#setLastExpandedProjectUsagesCategories(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> categoryIds)`
Sets collection of identifiers of project usages categories that were recently expanded.
`void`
`[setLastSelectedEsiOfflineServerID](#setLastSelectedEsiOfflineServerID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) serverId)`
Sets server identifiers that was last selected as offline server.
`void`
`[setLastUsedEsiBranches](#setLastUsedEsiBranches(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) info)`

`void`
`[setLoginToken](#setLoginToken(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token)`
sets login token to server
`void`
`[setMUServerName](#setMUServerName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
sets server name as a last used server name.
`void`
`[setMUUserLogin](#setMUUserLogin(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
sets user login to MU server
`void`
`[setMUUserPassword](#setMUUserPassword(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
sets user password to MU server
`void`
`[setMUUserPasswordAndEncrypt](#setMUUserPasswordAndEncrypt(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) psw)`
set encrypted password
`void`
`[setNewProjectVersionCheckInterval](#setNewProjectVersionCheckInterval(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) initialValue)`
Sets the initial interval between version checks for.
`void`
`[setNewProjectVersionNotification](#setNewProjectVersionNotification(boolean))(boolean value)`
Sets whether the *New Project Version Notification*
 should be set to enabled or not.
`void`
`[setProjectsTreeTableMode](#setProjectsTreeTableMode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Sets the teamwork projects tree table display mode.
`void`
`[setProjectUsagesUpdateNotification](#setProjectUsagesUpdateNotification(int))(int choice)`
Sets when to show notification about available project usages updates to latest version.
`void`
`[setRememberServerBetweenSessions](#setRememberServerBetweenSessions(boolean))(boolean remember)`
Sets that server will be remembered during sessions.
`void`
`[setRememberUserNameBetweenSessions](#setRememberUserNameBetweenSessions(boolean))(boolean remember)`
Sets that login will be remembered during sessions.
`void`
`[setRepresentationOfUsers](#setRepresentationOfUsers(int))(int choice)`
Sets how to display users
`void`
`[setServerNames](#setServerNames(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> serverNames)`
Setter for team server list (server names)
`void`
`[setShowModuleVersionsConflictWarning](#setShowModuleVersionsConflictWarning(boolean))(boolean show)`

`void`
`[setSSOLoginTabVisible](#setSSOLoginTabVisible(boolean))(boolean visible)`
Sets new value for the [`SSOLoginTabVisible`](#isSSOLoginTabVisible()) property
`void`
`[setUseSecureConnection](#setUseSecureConnection(boolean))(boolean use)`

`void`
`[setWebAppServerUrl](#setWebAppServerUrl(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url)`
Sets WebApp URL.
Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`beforeLoad, getExporterVersion, getOptionsToSave, isExporterVersionEarlier, isExporterVersionEarlier, loadOptions`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [getOptions](AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](AbstractPropertyOptionsGroup.html#getVisibleOptions()), [removeProperty](AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[getGroupIcon](OptionsGroup.html#getGroupIcon()), [getName](OptionsGroup.html#getName())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ID
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ID
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.ID)
DEFAULT_NEW_PROJECT_VERSION_CHECK
public static final boolean DEFAULT_NEW_PROJECT_VERSION_CHECK
Default value for *New Project Version Notification*
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.DEFAULT_NEW_PROJECT_VERSION_CHECK)
DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS)
DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX
public static final int DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX
Default setting when to show notification about available project usages updates to latest version
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX)
INCLUDE_VERSION_INTO_ELEMENT_URL_ASK
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INCLUDE_VERSION_INTO_ELEMENT_URL_ASK
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.INCLUDE_VERSION_INTO_ELEMENT_URL_ASK)
INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE)
INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE)
PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES
List of options when to show notification about available project usages updates to latest version
PROJECTS_TREE_TABLE_MODE_ORIGINAL
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROJECTS_TREE_TABLE_MODE_ORIGINAL
Mode of teamwork projects tree table when categories and projects are
 displayed in tree form, no presentation modifications are made to
 original structure
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.PROJECTS_TREE_TABLE_MODE_ORIGINAL)
PROJECTS_TREE_TABLE_MODE_FLAT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROJECTS_TREE_TABLE_MODE_FLAT
Mode of teamwork projects tree table when only projects are displayed in
 flat list.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.PROJECTS_TREE_TABLE_MODE_FLAT)
USERS_REPRESENTATION_CHOICES
public static final [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) USERS_REPRESENTATION_CHOICES
List of options how to display users
USERS_REPRESENTATION_USER_NAME
public static final int USERS_REPRESENTATION_USER_NAME
Display user name option
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.USERS_REPRESENTATION_USER_NAME)
USERS_REPRESENTATION_FULL_NAME
public static final int USERS_REPRESENTATION_FULL_NAME
Display full user name option
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.USERS_REPRESENTATION_FULL_NAME)
USERS_REPRESENTATION_EMAIL
public static final int USERS_REPRESENTATION_EMAIL
Display user email option
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.USERS_REPRESENTATION_EMAIL)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TeamworkOptionsGroup
public TeamworkOptionsGroup()
 ============ METHOD DETAIL ========== 
Method Details
setDefaultValues
public void setDefaultValues()
Description copied from class: `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html#setDefaultValues())`
Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.
Overrides:
`setDefaultValues` in class `com.nomagic.magicdraw.core.options.VersionedOptionsGroup`
setEnable3DExperience
public void setEnable3DExperience(boolean value)
isEnable3DExperience
public boolean isEnable3DExperience()
afterLoad
protected void afterLoad(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)
Overrides:
`afterLoad` in class `com.nomagic.magicdraw.core.options.VersionedOptionsGroup`
setAutoLoginToMU
public void setAutoLoginToMU(boolean log)
sets auto login to MU server
isAutoLoginToMU
public boolean isAutoLoginToMU()
is login to MU server auto
setMUServerName
public void setMUServerName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
sets server name as a last used server name.
setAuthServerName
public void setAuthServerName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
sets server name as a last used server name.
Parameters:
`name` - server name
getMUServerName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMUServerName()
gets Last used server name
getAuthServerName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getAuthServerName()
gets Last used authentication server name
setMUUserLogin
public void setMUUserLogin([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
sets user login to MU server
getMUUserLogin
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMUUserLogin()
gets user login to MU server
setLoginToken
public void setLoginToken([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) token)
sets login token to server
Parameters:
`token` - authentication token
getLoginToken
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getLoginToken()
gets login token to server
getMUUserPassword
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMUUserPassword()
gets user password to MU server
Returns:
secret password
setMUUserPasswordAndEncrypt
public void setMUUserPasswordAndEncrypt([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) psw)
set encrypted password
setMUUserPassword
public void setMUUserPassword([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
sets user password to MU server
clearMUUserPassword
public void clearMUUserPassword()
Clears user password to MU server
setShowModuleVersionsConflictWarning
public void setShowModuleVersionsConflictWarning(boolean show)
isShowModuleVersionsConflictWarning
public boolean isShowModuleVersionsConflictWarning()
setLastUsedEsiBranches
public void setLastUsedEsiBranches([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) info)
getLastUsedEsiBranches
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getLastUsedEsiBranches()
getServerNames
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getServerNames()
Returns the list of server names, which where entered by user, and successfully connected.
getAuthServerNames
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getAuthServerNames()
Returns the list of authentication server names, which where entered by user, and successfully connected.
Returns:
list of servers used earlier
setAuthServerNames
public void setAuthServerNames([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> serverNames)
Setter for Single Sign On server list (server names)
getDefaultServerNames
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getDefaultServerNames()
setServerNames
public void setServerNames([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> serverNames)
Setter for team server list (server names)
getIncludeVersionIntoURLMode
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getIncludeVersionIntoURLMode()
setIncludeVersionIntoURLMode
public void setIncludeVersionIntoURLMode([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getLastExpandedCategories
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getLastExpandedCategories()
Gets collection of identifiers of categories that were recently expanded.
Returns:
collection of category id.
setLastExpandedCategories
public void setLastExpandedCategories([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> categoryIds)
Sets collection of identifiers of categories that were recently expanded.
getLastExpandedProjectUsagesCategories
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getLastExpandedProjectUsagesCategories()
Gets collection of identifiers of project usages categories that were recently expanded.
Returns:
collection of category id.
setLastExpandedProjectUsagesCategories
public void setLastExpandedProjectUsagesCategories([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> categoryIds)
Sets collection of identifiers of project usages categories that were recently expanded.
getLastSelectedEsiOfflineServerID
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getLastSelectedEsiOfflineServerID()
Gets last selected esi offline server.
Returns:
server id
setLastSelectedEsiOfflineServerID
public void setLastSelectedEsiOfflineServerID([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) serverId)
Sets server identifiers that was last selected as offline server.
Parameters:
`serverId` - server ID (esi server cluster ID)
getProjectsTreeTableMode
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getProjectsTreeTableMode()
Gets the teamwork projects tree table display mode.
Returns:
mode
See Also:
[`PROJECTS_TREE_TABLE_MODE_ORIGINAL`](#PROJECTS_TREE_TABLE_MODE_ORIGINAL)
[`PROJECTS_TREE_TABLE_MODE_FLAT`](#PROJECTS_TREE_TABLE_MODE_FLAT)
setProjectsTreeTableMode
public void setProjectsTreeTableMode([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Sets the teamwork projects tree table display mode.
See Also:
[`PROJECTS_TREE_TABLE_MODE_ORIGINAL`](#PROJECTS_TREE_TABLE_MODE_ORIGINAL)
[`PROJECTS_TREE_TABLE_MODE_FLAT`](#PROJECTS_TREE_TABLE_MODE_FLAT)
isEmptyTeamworkProjectsCategoriesVisible
public boolean isEmptyTeamworkProjectsCategoriesVisible()
Indicates if teamwork projects tree table shall display an empty
 categories as well.
Returns:
true to show empty, otherwise false
setEmptyTeamworkProjectsCategoriesVisible
public void setEmptyTeamworkProjectsCategoriesVisible(boolean visible)
Sets if teamwork projects tree table shall display an empty categories as
 well
setUseSecureConnection
public void setUseSecureConnection(boolean use)
isUseSecureConnection
public boolean isUseSecureConnection()
getBanner
public com.nomagic.ui.banners.Banner getBanner()
setRememberServerBetweenSessions
public void setRememberServerBetweenSessions(boolean remember)
Sets that server will be remembered during sessions.
Parameters:
`remember` - - true to remember, false not to remember.
isRememberServerBetweenSessions
public boolean isRememberServerBetweenSessions()
Is server will be remembered between sessions
setRememberUserNameBetweenSessions
public void setRememberUserNameBetweenSessions(boolean remember)
Sets that login will be remembered during sessions.
Parameters:
`remember` - - true to remember, false not to remember.
isRememberUserNameBetweenSessions
public boolean isRememberUserNameBetweenSessions()
Is entered user login name will be remembered between sessions.
setLastCameoResourceId
public void setLastCameoResourceId([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Sets last used cameo resource(project) ID.
Parameters:
`id` - unique id of resource.
getLastCameoResourceId
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getLastCameoResourceId()
Returns last cameo resource ID.
setKeepLocks
public void setKeepLocks(boolean keepLocks)
isKeepLocks
public boolean isKeepLocks()
setAutoCommitOnProjectMigration
public void setAutoCommitOnProjectMigration(boolean autoCommit)
Sets new value for the [`autoCommitOnProjectMigration`](#isAutoCommitOnProjectMigration()) property
Parameters:
`autoCommit` - the value to set
isAutoCommitOnProjectMigration
public boolean isAutoCommitOnProjectMigration()
Determines whether projects should be auto-commit after project migration
 to a new version. It is a general setting, however it is up to every
 different migration to decide whether it should conform to it
Returns:
`true` if project should be auto-committed after
 migration, `false` if not
setSSOLoginTabVisible
public void setSSOLoginTabVisible(boolean visible)
Sets new value for the [`SSOLoginTabVisible`](#isSSOLoginTabVisible()) property
Parameters:
`visible` - the value to set
isSSOLoginTabVisible
public boolean isSSOLoginTabVisible()
Determines whether sso login tab should be visible.
Returns:
`true` if login tab should be visible, `false` if not
setNewProjectVersionCheckInterval
public void setNewProjectVersionCheckInterval([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) initialValue)
Sets the initial interval between version checks for.
Parameters:
`initialValue` - value to select in the choice box
getNewProjectVersionCheckInterval
public int getNewProjectVersionCheckInterval()
Returns currently selected interval between version checks.
Returns:
interval between version checks in seconds
setNewProjectVersionNotification
public void setNewProjectVersionNotification(boolean value)
Sets whether the *New Project Version Notification*
 should be set to enabled or not.
Parameters:
`value` - identifies the state of the property(`true` means enabled)
isNewProjectVersionCheckEnabled
public boolean isNewProjectVersionCheckEnabled()
Method checks whether the *New Project Version Notification*
 property is enabled
Returns:
`true` if the property is enabled
setProjectUsagesUpdateNotification
public void setProjectUsagesUpdateNotification(int choice)
Sets when to show notification about available project usages updates to latest version. Default option is 0 (on open).
Parameters:
`choice` - when to show notification about available project usages updates to latest version (open = 0, open, update and save = 1, never = 2).
getProjectUsagesUpdateNotification
public int getProjectUsagesUpdateNotification()
Gets when to show notification about available project usages updates to latest version. Default option is 0 (on open).
Returns:
when to show notification about available project usages updates to latest version (open = 0, open, update and save = 1, never = 2).
setEnableLockingWithoutForceUpdate
public void setEnableLockingWithoutForceUpdate(boolean enable)
Sets new value for the [`isEnableLockingWithoutForceUpdate()`](#isEnableLockingWithoutForceUpdate()) property
Parameters:
`enable` - enable lock without update
isEnableLockingWithoutForceUpdate
public boolean isEnableLockingWithoutForceUpdate()
Determines whether elements can be locked without update project. Locking without update
 can be done only if there is no changes done with elements in upcoming server versions.
Returns:
`false` if project if forced to update
setCreateMountRelationshipsOnImportToCEDW
public void setCreateMountRelationshipsOnImportToCEDW(boolean enable)
Sets new value for this property.
Parameters:
`enable` - new value
getCreateMountRelationshipsOnImportToCEDW
public boolean getCreateMountRelationshipsOnImportToCEDW()
Gets value of this property.
Returns:
true if property value is true, or if property does not exist at all.
setWebAppServerUrl
public void setWebAppServerUrl([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url)
Sets WebApp URL.
Parameters:
`url` - new URL
getWebAppServerUrl
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getWebAppServerUrl()
Gets WebApp URL.
Returns:
WebApp URL
setRepresentationOfUsers
public void setRepresentationOfUsers(int choice)
Sets how to display users
Parameters:
`choice` - field to show (user name = 0, full name = 1, email = 2)
getRepresentationOfUsers
public int getRepresentationOfUsers()
Gets how to display users
Returns:
field to show (user name = 0, full name = 1, email = 2)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class TeamworkOptionsGroup">Class TeamworkOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.VersionedOptionsGroup
<div class="inheritance">com.nomagic.magicdraw.core.options.TeamworkOptionsGroup</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TeamworkOptionsGroup</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.options.VersionedOptionsGroup</span></div>
<div class="block">Teamwork options.</div>
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
<div class="col-first even-row-color"><code>static final boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_NEW_PROJECT_VERSION_CHECK">DEFAULT_NEW_PROJECT_VERSION_CHECK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default value for <em>New Project Version Notification</em></div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS">DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX">DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default setting when to show notification about available project usages updates to latest version</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INCLUDE_VERSION_INTO_ELEMENT_URL_ASK">INCLUDE_VERSION_INTO_ELEMENT_URL_ASK</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE">INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE">INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES">PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of options when to show notification about available project usages updates to latest version</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROJECTS_TREE_TABLE_MODE_FLAT">PROJECTS_TREE_TABLE_MODE_FLAT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Mode of teamwork projects tree table when only projects are displayed in
 flat list.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECTS_TREE_TABLE_MODE_ORIGINAL">PROJECTS_TREE_TABLE_MODE_ORIGINAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Mode of teamwork projects tree table when categories and projects are
 displayed in tree form, no presentation modifications are made to
 original structure</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USERS_REPRESENTATION_CHOICES">USERS_REPRESENTATION_CHOICES</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of options how to display users</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USERS_REPRESENTATION_EMAIL">USERS_REPRESENTATION_EMAIL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Display user email option</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USERS_REPRESENTATION_FULL_NAME">USERS_REPRESENTATION_FULL_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Display full user name option</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USERS_REPRESENTATION_USER_NAME">USERS_REPRESENTATION_USER_NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Display user name option</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>CURRENT_EXPORTER_VERSION</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TeamworkOptionsGroup</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">afterLoad</a><wbr/>(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearMUUserPassword()">clearMUUserPassword</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clears user password to MU server</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAuthServerName()">getAuthServerName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">gets Last used authentication server name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAuthServerNames()">getAuthServerNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of authentication server names, which where entered by user, and successfully connected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.banners.Banner</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBanner()">getBanner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreateMountRelationshipsOnImportToCEDW()">getCreateMountRelationshipsOnImportToCEDW</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets value of this property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultServerNames()">getDefaultServerNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIncludeVersionIntoURLMode()">getIncludeVersionIntoURLMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastCameoResourceId()">getLastCameoResourceId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns last cameo resource ID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastExpandedCategories()">getLastExpandedCategories</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets collection of identifiers of categories that were recently expanded.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastExpandedProjectUsagesCategories()">getLastExpandedProjectUsagesCategories</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets collection of identifiers of project usages categories that were recently expanded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastSelectedEsiOfflineServerID()">getLastSelectedEsiOfflineServerID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets last selected esi offline server.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastUsedEsiBranches()">getLastUsedEsiBranches</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoginToken()">getLoginToken</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">gets login token to server</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMUServerName()">getMUServerName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">gets Last used server name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMUUserLogin()">getMUUserLogin</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">gets user login to MU server</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMUUserPassword()">getMUUserPassword</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">gets user password to MU server</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNewProjectVersionCheckInterval()">getNewProjectVersionCheckInterval</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns currently selected interval between version checks.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectsTreeTableMode()">getProjectsTreeTableMode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the teamwork projects tree table display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectUsagesUpdateNotification()">getProjectUsagesUpdateNotification</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets when to show notification about available project usages updates to latest version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRepresentationOfUsers()">getRepresentationOfUsers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets how to display users</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getServerNames()">getServerNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the list of server names, which where entered by user, and successfully connected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWebAppServerUrl()">getWebAppServerUrl</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets WebApp URL.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoCommitOnProjectMigration()">isAutoCommitOnProjectMigration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether projects should be auto-commit after project migration
 to a new version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoLoginToMU()">isAutoLoginToMU</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">is login to MU server auto</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEmptyTeamworkProjectsCategoriesVisible()">isEmptyTeamworkProjectsCategoriesVisible</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if teamwork projects tree table shall display an empty
 categories as well.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnable3DExperience()">isEnable3DExperience</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnableLockingWithoutForceUpdate()">isEnableLockingWithoutForceUpdate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether elements can be locked without update project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isKeepLocks()">isKeepLocks</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNewProjectVersionCheckEnabled()">isNewProjectVersionCheckEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method checks whether the <em>New Project Version Notification</em>
 property is enabled</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRememberServerBetweenSessions()">isRememberServerBetweenSessions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Is server will be remembered between sessions</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRememberUserNameBetweenSessions()">isRememberUserNameBetweenSessions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Is entered user login name will be remembered between sessions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowModuleVersionsConflictWarning()">isShowModuleVersionsConflictWarning</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSSOLoginTabVisible()">isSSOLoginTabVisible</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether sso login tab should be visible.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseSecureConnection()">isUseSecureConnection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAuthServerName(java.lang.String)">setAuthServerName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets server name as a last used server name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAuthServerNames(java.util.List)">setAuthServerNames</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; serverNames)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Setter for Single Sign On server list (server names)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoCommitOnProjectMigration(boolean)">setAutoCommitOnProjectMigration</a><wbr/>(boolean autoCommit)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new value for the <a href="#isAutoCommitOnProjectMigration()"><code>autoCommitOnProjectMigration</code></a> property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoLoginToMU(boolean)">setAutoLoginToMU</a><wbr/>(boolean log)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets auto login to MU server</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateMountRelationshipsOnImportToCEDW(boolean)">setCreateMountRelationshipsOnImportToCEDW</a><wbr/>(boolean enable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new value for this property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultValues()">setDefaultValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default values for the properties contained in this group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEmptyTeamworkProjectsCategoriesVisible(boolean)">setEmptyTeamworkProjectsCategoriesVisible</a><wbr/>(boolean visible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets if teamwork projects tree table shall display an empty categories as
 well</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnable3DExperience(boolean)">setEnable3DExperience</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnableLockingWithoutForceUpdate(boolean)">setEnableLockingWithoutForceUpdate</a><wbr/>(boolean enable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new value for the <a href="#isEnableLockingWithoutForceUpdate()"><code>isEnableLockingWithoutForceUpdate()</code></a> property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIncludeVersionIntoURLMode(java.lang.String)">setIncludeVersionIntoURLMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setKeepLocks(boolean)">setKeepLocks</a><wbr/>(boolean keepLocks)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastCameoResourceId(java.lang.String)">setLastCameoResourceId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets last used cameo resource(project) ID.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastExpandedCategories(java.util.Collection)">setLastExpandedCategories</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; categoryIds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets collection of identifiers of categories that were recently expanded.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastExpandedProjectUsagesCategories(java.util.Collection)">setLastExpandedProjectUsagesCategories</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; categoryIds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets collection of identifiers of project usages categories that were recently expanded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastSelectedEsiOfflineServerID(java.lang.String)">setLastSelectedEsiOfflineServerID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> serverId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets server identifiers that was last selected as offline server.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastUsedEsiBranches(java.lang.String)">setLastUsedEsiBranches</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoginToken(java.lang.String)">setLoginToken</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets login token to server</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMUServerName(java.lang.String)">setMUServerName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets server name as a last used server name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMUUserLogin(java.lang.String)">setMUUserLogin</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets user login to MU server</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMUUserPassword(java.lang.String)">setMUUserPassword</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">sets user password to MU server</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMUUserPasswordAndEncrypt(java.lang.String)">setMUUserPasswordAndEncrypt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> psw)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set encrypted password</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNewProjectVersionCheckInterval(java.lang.String)">setNewProjectVersionCheckInterval</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> initialValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the initial interval between version checks for.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNewProjectVersionNotification(boolean)">setNewProjectVersionNotification</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether the <em>New Project Version Notification</em>
 should be set to enabled or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProjectsTreeTableMode(java.lang.String)">setProjectsTreeTableMode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the teamwork projects tree table display mode.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProjectUsagesUpdateNotification(int)">setProjectUsagesUpdateNotification</a><wbr/>(int choice)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets when to show notification about available project usages updates to latest version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRememberServerBetweenSessions(boolean)">setRememberServerBetweenSessions</a><wbr/>(boolean remember)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets that server will be remembered during sessions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRememberUserNameBetweenSessions(boolean)">setRememberUserNameBetweenSessions</a><wbr/>(boolean remember)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets that login will be remembered during sessions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRepresentationOfUsers(int)">setRepresentationOfUsers</a><wbr/>(int choice)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets how to display users</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setServerNames(java.util.List)">setServerNames</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; serverNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Setter for team server list (server names)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowModuleVersionsConflictWarning(boolean)">setShowModuleVersionsConflictWarning</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSSOLoginTabVisible(boolean)">setSSOLoginTabVisible</a><wbr/>(boolean visible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets new value for the <a href="#isSSOLoginTabVisible()"><code>SSOLoginTabVisible</code></a> property</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseSecureConnection(boolean)">setUseSecureConnection</a><wbr/>(boolean use)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWebAppServerUrl(java.lang.String)">setWebAppServerUrl</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets WebApp URL.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>beforeLoad, getExporterVersion, getOptionsToSave, isExporterVersionEarlier, isExporterVersionEarlier, loadOptions</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="OptionsGroup.html#getGroupIcon()">getGroupIcon</a>, <a href="OptionsGroup.html#getName()">getName</a></code></div>
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
<section class="detail" id="ID">
<h3>ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_NEW_PROJECT_VERSION_CHECK">
<h3>DEFAULT_NEW_PROJECT_VERSION_CHECK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">boolean</span> <span class="element-name">DEFAULT_NEW_PROJECT_VERSION_CHECK</span></div>
<div class="block">Default value for <em>New Project Version Notification</em></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.DEFAULT_NEW_PROJECT_VERSION_CHECK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS">
<h3>DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.DEFAULT_NEW_PROJECT_VERSION_CHECK_INTERVAL_IN_SECONDS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX">
<h3>DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX</span></div>
<div class="block">Default setting when to show notification about available project usages updates to latest version</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.DEFAULT_PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INCLUDE_VERSION_INTO_ELEMENT_URL_ASK">
<h3>INCLUDE_VERSION_INTO_ELEMENT_URL_ASK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INCLUDE_VERSION_INTO_ELEMENT_URL_ASK</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.INCLUDE_VERSION_INTO_ELEMENT_URL_ASK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE">
<h3>INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.INCLUDE_VERSION_INTO_ELEMENT_URL_INCLUDE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE">
<h3>INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.INCLUDE_VERSION_INTO_ELEMENT_URL_DO_NOT_INCLUDE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES">
<h3>PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">PROJECT_USAGES_UPDATE_SHOW_NOTIFICATION_OPTION_CHOICES</span></div>
<div class="block">List of options when to show notification about available project usages updates to latest version</div>
</section>
</li>
<li>
<section class="detail" id="PROJECTS_TREE_TABLE_MODE_ORIGINAL">
<h3>PROJECTS_TREE_TABLE_MODE_ORIGINAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECTS_TREE_TABLE_MODE_ORIGINAL</span></div>
<div class="block">Mode of teamwork projects tree table when categories and projects are
 displayed in tree form, no presentation modifications are made to
 original structure</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.PROJECTS_TREE_TABLE_MODE_ORIGINAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECTS_TREE_TABLE_MODE_FLAT">
<h3>PROJECTS_TREE_TABLE_MODE_FLAT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECTS_TREE_TABLE_MODE_FLAT</span></div>
<div class="block">Mode of teamwork projects tree table when only projects are displayed in
 flat list.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.PROJECTS_TREE_TABLE_MODE_FLAT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USERS_REPRESENTATION_CHOICES">
<h3>USERS_REPRESENTATION_CHOICES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">USERS_REPRESENTATION_CHOICES</span></div>
<div class="block">List of options how to display users</div>
</section>
</li>
<li>
<section class="detail" id="USERS_REPRESENTATION_USER_NAME">
<h3>USERS_REPRESENTATION_USER_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">USERS_REPRESENTATION_USER_NAME</span></div>
<div class="block">Display user name option</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.USERS_REPRESENTATION_USER_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USERS_REPRESENTATION_FULL_NAME">
<h3>USERS_REPRESENTATION_FULL_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">USERS_REPRESENTATION_FULL_NAME</span></div>
<div class="block">Display full user name option</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.USERS_REPRESENTATION_FULL_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USERS_REPRESENTATION_EMAIL">
<h3>USERS_REPRESENTATION_EMAIL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">USERS_REPRESENTATION_EMAIL</span></div>
<div class="block">Display user email option</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.TeamworkOptionsGroup.USERS_REPRESENTATION_EMAIL">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>TeamworkOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TeamworkOptionsGroup</span>()</div>
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
<section class="detail" id="setDefaultValues()">
<h3>setDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultValues</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="AbstractPropertyOptionsGroup.html#setDefaultValues()">AbstractPropertyOptionsGroup</a></code></span></div>
<div class="block">Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>setDefaultValues</code> in class <code>com.nomagic.magicdraw.core.options.VersionedOptionsGroup</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnable3DExperience(boolean)">
<h3>setEnable3DExperience</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnable3DExperience</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="isEnable3DExperience()">
<h3>isEnable3DExperience</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnable3DExperience</span>()</div>
</section>
</li>
<li>
<section class="detail" id="afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">
<h3>afterLoad</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">afterLoad</span><wbr/><span class="parameters">(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>afterLoad</code> in class <code>com.nomagic.magicdraw.core.options.VersionedOptionsGroup</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAutoLoginToMU(boolean)">
<h3>setAutoLoginToMU</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoLoginToMU</span><wbr/><span class="parameters">(boolean log)</span></div>
<div class="block">sets auto login to MU server</div>
</section>
</li>
<li>
<section class="detail" id="isAutoLoginToMU()">
<h3>isAutoLoginToMU</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutoLoginToMU</span>()</div>
<div class="block">is login to MU server auto</div>
</section>
</li>
<li>
<section class="detail" id="setMUServerName(java.lang.String)">
<h3>setMUServerName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMUServerName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">sets server name as a last used server name.</div>
</section>
</li>
<li>
<section class="detail" id="setAuthServerName(java.lang.String)">
<h3>setAuthServerName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAuthServerName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">sets server name as a last used server name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - server name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMUServerName()">
<h3>getMUServerName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMUServerName</span>()</div>
<div class="block">gets Last used server name</div>
</section>
</li>
<li>
<section class="detail" id="getAuthServerName()">
<h3>getAuthServerName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAuthServerName</span>()</div>
<div class="block">gets Last used authentication server name</div>
</section>
</li>
<li>
<section class="detail" id="setMUUserLogin(java.lang.String)">
<h3>setMUUserLogin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMUUserLogin</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">sets user login to MU server</div>
</section>
</li>
<li>
<section class="detail" id="getMUUserLogin()">
<h3>getMUUserLogin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMUUserLogin</span>()</div>
<div class="block">gets user login to MU server</div>
</section>
</li>
<li>
<section class="detail" id="setLoginToken(java.lang.String)">
<h3>setLoginToken</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoginToken</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> token)</span></div>
<div class="block">sets login token to server</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>token</code> - authentication token</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLoginToken()">
<h3>getLoginToken</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLoginToken</span>()</div>
<div class="block">gets login token to server</div>
</section>
</li>
<li>
<section class="detail" id="getMUUserPassword()">
<h3>getMUUserPassword</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMUUserPassword</span>()</div>
<div class="block">gets user password to MU server</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>secret password</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMUUserPasswordAndEncrypt(java.lang.String)">
<h3>setMUUserPasswordAndEncrypt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMUUserPasswordAndEncrypt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> psw)</span></div>
<div class="block">set encrypted password</div>
</section>
</li>
<li>
<section class="detail" id="setMUUserPassword(java.lang.String)">
<h3>setMUUserPassword</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMUUserPassword</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">sets user password to MU server</div>
</section>
</li>
<li>
<section class="detail" id="clearMUUserPassword()">
<h3>clearMUUserPassword</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearMUUserPassword</span>()</div>
<div class="block">Clears user password to MU server</div>
</section>
</li>
<li>
<section class="detail" id="setShowModuleVersionsConflictWarning(boolean)">
<h3>setShowModuleVersionsConflictWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowModuleVersionsConflictWarning</span><wbr/><span class="parameters">(boolean show)</span></div>
</section>
</li>
<li>
<section class="detail" id="isShowModuleVersionsConflictWarning()">
<h3>isShowModuleVersionsConflictWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowModuleVersionsConflictWarning</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setLastUsedEsiBranches(java.lang.String)">
<h3>setLastUsedEsiBranches</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastUsedEsiBranches</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> info)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLastUsedEsiBranches()">
<h3>getLastUsedEsiBranches</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastUsedEsiBranches</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getServerNames()">
<h3>getServerNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getServerNames</span>()</div>
<div class="block">Returns the list of server names, which where entered by user, and successfully connected.</div>
</section>
</li>
<li>
<section class="detail" id="getAuthServerNames()">
<h3>getAuthServerNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAuthServerNames</span>()</div>
<div class="block">Returns the list of authentication server names, which where entered by user, and successfully connected.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of servers used earlier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAuthServerNames(java.util.List)">
<h3>setAuthServerNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAuthServerNames</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; serverNames)</span></div>
<div class="block">Setter for Single Sign On server list (server names)</div>
</section>
</li>
<li>
<section class="detail" id="getDefaultServerNames()">
<h3>getDefaultServerNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getDefaultServerNames</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setServerNames(java.util.List)">
<h3>setServerNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setServerNames</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; serverNames)</span></div>
<div class="block">Setter for team server list (server names)</div>
</section>
</li>
<li>
<section class="detail" id="getIncludeVersionIntoURLMode()">
<h3>getIncludeVersionIntoURLMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIncludeVersionIntoURLMode</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setIncludeVersionIntoURLMode(java.lang.String)">
<h3>setIncludeVersionIntoURLMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIncludeVersionIntoURLMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLastExpandedCategories()">
<h3>getLastExpandedCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getLastExpandedCategories</span>()</div>
<div class="block">Gets collection of identifiers of categories that were recently expanded.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of category id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLastExpandedCategories(java.util.Collection)">
<h3>setLastExpandedCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastExpandedCategories</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; categoryIds)</span></div>
<div class="block">Sets collection of identifiers of categories that were recently expanded.</div>
</section>
</li>
<li>
<section class="detail" id="getLastExpandedProjectUsagesCategories()">
<h3>getLastExpandedProjectUsagesCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getLastExpandedProjectUsagesCategories</span>()</div>
<div class="block">Gets collection of identifiers of project usages categories that were recently expanded.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of category id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLastExpandedProjectUsagesCategories(java.util.Collection)">
<h3>setLastExpandedProjectUsagesCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastExpandedProjectUsagesCategories</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; categoryIds)</span></div>
<div class="block">Sets collection of identifiers of project usages categories that were recently expanded.</div>
</section>
</li>
<li>
<section class="detail" id="getLastSelectedEsiOfflineServerID()">
<h3>getLastSelectedEsiOfflineServerID</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastSelectedEsiOfflineServerID</span>()</div>
<div class="block">Gets last selected esi offline server.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>server id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLastSelectedEsiOfflineServerID(java.lang.String)">
<h3>setLastSelectedEsiOfflineServerID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastSelectedEsiOfflineServerID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> serverId)</span></div>
<div class="block">Sets server identifiers that was last selected as offline server.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>serverId</code> - server ID (esi server cluster ID)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectsTreeTableMode()">
<h3>getProjectsTreeTableMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectsTreeTableMode</span>()</div>
<div class="block">Gets the teamwork projects tree table display mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>mode</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#PROJECTS_TREE_TABLE_MODE_ORIGINAL"><code>PROJECTS_TREE_TABLE_MODE_ORIGINAL</code></a></li>
<li><a href="#PROJECTS_TREE_TABLE_MODE_FLAT"><code>PROJECTS_TREE_TABLE_MODE_FLAT</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProjectsTreeTableMode(java.lang.String)">
<h3>setProjectsTreeTableMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProjectsTreeTableMode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets the teamwork projects tree table display mode.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#PROJECTS_TREE_TABLE_MODE_ORIGINAL"><code>PROJECTS_TREE_TABLE_MODE_ORIGINAL</code></a></li>
<li><a href="#PROJECTS_TREE_TABLE_MODE_FLAT"><code>PROJECTS_TREE_TABLE_MODE_FLAT</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmptyTeamworkProjectsCategoriesVisible()">
<h3>isEmptyTeamworkProjectsCategoriesVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEmptyTeamworkProjectsCategoriesVisible</span>()</div>
<div class="block">Indicates if teamwork projects tree table shall display an empty
 categories as well.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true to show empty, otherwise false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEmptyTeamworkProjectsCategoriesVisible(boolean)">
<h3>setEmptyTeamworkProjectsCategoriesVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEmptyTeamworkProjectsCategoriesVisible</span><wbr/><span class="parameters">(boolean visible)</span></div>
<div class="block">Sets if teamwork projects tree table shall display an empty categories as
 well</div>
</section>
</li>
<li>
<section class="detail" id="setUseSecureConnection(boolean)">
<h3>setUseSecureConnection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseSecureConnection</span><wbr/><span class="parameters">(boolean use)</span></div>
</section>
</li>
<li>
<section class="detail" id="isUseSecureConnection()">
<h3>isUseSecureConnection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseSecureConnection</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getBanner()">
<h3>getBanner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.ui.banners.Banner</span> <span class="element-name">getBanner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setRememberServerBetweenSessions(boolean)">
<h3>setRememberServerBetweenSessions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRememberServerBetweenSessions</span><wbr/><span class="parameters">(boolean remember)</span></div>
<div class="block">Sets that server will be remembered during sessions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>remember</code> - - true to remember, false not to remember.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRememberServerBetweenSessions()">
<h3>isRememberServerBetweenSessions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRememberServerBetweenSessions</span>()</div>
<div class="block">Is server will be remembered between sessions</div>
</section>
</li>
<li>
<section class="detail" id="setRememberUserNameBetweenSessions(boolean)">
<h3>setRememberUserNameBetweenSessions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRememberUserNameBetweenSessions</span><wbr/><span class="parameters">(boolean remember)</span></div>
<div class="block">Sets that login will be remembered during sessions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>remember</code> - - true to remember, false not to remember.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRememberUserNameBetweenSessions()">
<h3>isRememberUserNameBetweenSessions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRememberUserNameBetweenSessions</span>()</div>
<div class="block">Is entered user login name will be remembered between sessions.</div>
</section>
</li>
<li>
<section class="detail" id="setLastCameoResourceId(java.lang.String)">
<h3>setLastCameoResourceId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLastCameoResourceId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sets last used cameo resource(project) ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - unique id of resource.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastCameoResourceId()">
<h3>getLastCameoResourceId</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLastCameoResourceId</span>()</div>
<div class="block">Returns last cameo resource ID.</div>
</section>
</li>
<li>
<section class="detail" id="setKeepLocks(boolean)">
<h3>setKeepLocks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setKeepLocks</span><wbr/><span class="parameters">(boolean keepLocks)</span></div>
</section>
</li>
<li>
<section class="detail" id="isKeepLocks()">
<h3>isKeepLocks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isKeepLocks</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setAutoCommitOnProjectMigration(boolean)">
<h3>setAutoCommitOnProjectMigration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoCommitOnProjectMigration</span><wbr/><span class="parameters">(boolean autoCommit)</span></div>
<div class="block">Sets new value for the <a href="#isAutoCommitOnProjectMigration()"><code>autoCommitOnProjectMigration</code></a> property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>autoCommit</code> - the value to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAutoCommitOnProjectMigration()">
<h3>isAutoCommitOnProjectMigration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutoCommitOnProjectMigration</span>()</div>
<div class="block">Determines whether projects should be auto-commit after project migration
 to a new version. It is a general setting, however it is up to every
 different migration to decide whether it should conform to it</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if project should be auto-committed after
 migration, <code>false</code> if not</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSSOLoginTabVisible(boolean)">
<h3>setSSOLoginTabVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSSOLoginTabVisible</span><wbr/><span class="parameters">(boolean visible)</span></div>
<div class="block">Sets new value for the <a href="#isSSOLoginTabVisible()"><code>SSOLoginTabVisible</code></a> property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visible</code> - the value to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSSOLoginTabVisible()">
<h3>isSSOLoginTabVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSSOLoginTabVisible</span>()</div>
<div class="block">Determines whether sso login tab should be visible.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if login tab should be visible, <code>false</code> if not</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNewProjectVersionCheckInterval(java.lang.String)">
<h3>setNewProjectVersionCheckInterval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNewProjectVersionCheckInterval</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> initialValue)</span></div>
<div class="block">Sets the initial interval between version checks for.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initialValue</code> - value to select in the choice box</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNewProjectVersionCheckInterval()">
<h3>getNewProjectVersionCheckInterval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNewProjectVersionCheckInterval</span>()</div>
<div class="block">Returns currently selected interval between version checks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>interval between version checks in seconds</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNewProjectVersionNotification(boolean)">
<h3>setNewProjectVersionNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNewProjectVersionNotification</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block">Sets whether the <em>New Project Version Notification</em>
 should be set to enabled or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - identifies the state of the property(<code>true</code> means enabled)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNewProjectVersionCheckEnabled()">
<h3>isNewProjectVersionCheckEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNewProjectVersionCheckEnabled</span>()</div>
<div class="block">Method checks whether the <em>New Project Version Notification</em>
 property is enabled</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if the property is enabled</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProjectUsagesUpdateNotification(int)">
<h3>setProjectUsagesUpdateNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProjectUsagesUpdateNotification</span><wbr/><span class="parameters">(int choice)</span></div>
<div class="block">Sets when to show notification about available project usages updates to latest version. Default option is 0 (on open).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>choice</code> - when to show notification about available project usages updates to latest version (open = 0, open, update and save = 1, never = 2).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectUsagesUpdateNotification()">
<h3>getProjectUsagesUpdateNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getProjectUsagesUpdateNotification</span>()</div>
<div class="block">Gets when to show notification about available project usages updates to latest version. Default option is 0 (on open).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>when to show notification about available project usages updates to latest version (open = 0, open, update and save = 1, never = 2).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnableLockingWithoutForceUpdate(boolean)">
<h3>setEnableLockingWithoutForceUpdate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnableLockingWithoutForceUpdate</span><wbr/><span class="parameters">(boolean enable)</span></div>
<div class="block">Sets new value for the <a href="#isEnableLockingWithoutForceUpdate()"><code>isEnableLockingWithoutForceUpdate()</code></a> property</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enable</code> - enable lock without update</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnableLockingWithoutForceUpdate()">
<h3>isEnableLockingWithoutForceUpdate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnableLockingWithoutForceUpdate</span>()</div>
<div class="block">Determines whether elements can be locked without update project. Locking without update
 can be done only if there is no changes done with elements in upcoming server versions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>false</code> if project if forced to update</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateMountRelationshipsOnImportToCEDW(boolean)">
<h3>setCreateMountRelationshipsOnImportToCEDW</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateMountRelationshipsOnImportToCEDW</span><wbr/><span class="parameters">(boolean enable)</span></div>
<div class="block">Sets new value for this property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enable</code> - new value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreateMountRelationshipsOnImportToCEDW()">
<h3>getCreateMountRelationshipsOnImportToCEDW</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">getCreateMountRelationshipsOnImportToCEDW</span>()</div>
<div class="block">Gets value of this property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if property value is true, or if property does not exist at all.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWebAppServerUrl(java.lang.String)">
<h3>setWebAppServerUrl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWebAppServerUrl</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</span></div>
<div class="block">Sets WebApp URL.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - new URL</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWebAppServerUrl()">
<h3>getWebAppServerUrl</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getWebAppServerUrl</span>()</div>
<div class="block">Gets WebApp URL.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>WebApp URL</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRepresentationOfUsers(int)">
<h3>setRepresentationOfUsers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRepresentationOfUsers</span><wbr/><span class="parameters">(int choice)</span></div>
<div class="block">Sets how to display users</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>choice</code> - field to show (user name = 0, full name = 1, email = 2)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentationOfUsers()">
<h3>getRepresentationOfUsers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getRepresentationOfUsers</span>()</div>
<div class="block">Gets how to display users</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>field to show (user name = 0, full name = 1, email = 2)</dd>
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
