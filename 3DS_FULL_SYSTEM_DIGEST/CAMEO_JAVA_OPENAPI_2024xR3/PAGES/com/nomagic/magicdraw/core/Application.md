# JAVA OPENAPI: Application (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/Application.html
- source_path: `com/nomagic/magicdraw/core/Application.html`
- source_sha256: `2755851d975f1d9673b643ac1d63f2efb6aa5b67f143d6fdcaeced9384f1b70b`
- captured_utc: `2026-07-14T16:55:11.486966+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class Application

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.Application

@OpenApipublic classApplication
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Main class which connects main parts of MagicDraw.
 This class is singleton, only one instance of this class can exist.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[Application.Environment](Application.Environment.html)`
Contains application environment specific constants and utility methods.
`static class`
`[Application.Runtime](Application.Runtime.html)`
Contains application runtime related constants and utility methods.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final byte`
`[STARTUP_CANCELED](#STARTUP_CANCELED)`

`static final byte`
`[STARTUP_ERROR](#STARTUP_ERROR)`

`static final byte`
`[STARTUP_SUCCESSFUL](#STARTUP_SUCCESSFUL)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[Application](#%3Cinit%3E())()`
Constructor of Application.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addActivityAfterStartup](#addActivityAfterStartup(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) activity)`
Registered runnable is executed right after MagicDraw application startup.
`void`
`[addActivityOnUICreation](#addActivityOnUICreation(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) activity)`
[`Runnable`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) which will be run on UI creation.
`void`
`[addAlias](#addAlias(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) alias,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[addApplicationEventListener](#addApplicationEventListener(com.nomagic.magicdraw.core.ApplicationEventListener))(com.nomagic.magicdraw.core.ApplicationEventListener listener)`
Adds application event listener to application listeners.
`void`
`[addNewDiagramType](#addNewDiagramType(com.nomagic.magicdraw.uml.DiagramDescriptor))([DiagramDescriptor](../uml/DiagramDescriptor.html) descriptor)`
Registers new diagram type in the MagicDraw application.
`final void`
`[addProjectEventListener](#addProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener))([ProjectEventListener](project/ProjectEventListener.html) listener)`
Method adds new ProjectEventListener.
`void`
`[addSaveParticipant](#addSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant))([SaveParticipant](SaveParticipant.html) participant)`
Registers SaveParticipant for custom actions on project saving.
`static [Application.Environment](Application.Environment.html)`
`[environment](#environment())()`
Gets application environment.
`static com.nomagic.magicdraw.core.Application.EnvironmentInternal`
`[environmentInternal](#environmentInternal())()`

`final void`
`[executeActivitiesOnUICreation](#executeActivitiesOnUICreation())()`
Executes registered UI activities.
`void`
`[exit](#exit())()`
Exits the application with Application.STARTUP_ERROR exit code.
`void`
`[exit](#exit(byte))(byte exitStatus)`
Exits the application.
`com.nomagic.magicdraw.actions.ActionsManager`
`[getActionsManager](#getActionsManager())()`
Returns the actionsManager.
`com.nomagic.magicdraw.core.Alias`
`[getAlias](#getAlias())()`

`final [CookieSet](../cookies/CookieSet.html)`
`[getCookieSet](#getCookieSet())()`
Returns cookie set of the application.
`[DiagramDescriptor](../uml/DiagramDescriptor.html)`
`[getDiagramDescriptor](#getDiagramDescriptor(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)`

`[EnvironmentOptions](options/EnvironmentOptions.html)`
`[getEnvironmentOptions](#getEnvironmentOptions())()`
Gets application environment options.
`com.nomagic.rcpf.product.lic.floating.client.internal.FLManager`
`[getFLManager](#getFLManager())()`
Method getFLManager.
`[GUILog](GUILog.html)`
`[getGUILog](#getGUILog())()`
Returns the interface to log window.
`static [Application](Application.html)`
`[getInstance](#getInstance())()`
Returns single instance of Application.
`com.nomagic.magicdraw.integrations.IntegratorsManager`
`[getIntegrationsManager](#getIntegrationsManager())()`

`[MainFrame](../ui/MainFrame.html)`
`[getMainFrame](#getMainFrame())()`
Returns the mainFrame - main MagicDraw GUI component.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getOpenAPIVersion](#getOpenAPIVersion())()`
Version of OpenAPI
`com.nomagic.magicdraw.plugins.PluginsManager`
`[getPluginManager](#getPluginManager())()`
Method getPluginManager.
`[Project](Project.html)`
`[getProject](#getProject())()`
Returns current active Project.
`[ProjectsManager](project/ProjectsManager.html)`
`[getProjectsManager](#getProjectsManager())()`
Returns the projectsManager.
`com.nomagic.magicdraw.properties.PropertyResourceManager`
`[getPropertyResourceManager](#getPropertyResourceManager())()`
Returns propertyResourceManager for managing property resources.
`com.nomagic.magicdraw.ui.RecentFilesManager`
`[getRecentFilesManager](#getRecentFilesManager())()`
Returns the recentFilesManager.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SaveParticipant](SaveParticipant.html)>`
`[getSaveParticipants](#getSaveParticipants())()`
List of registered SaveParticipants.
`com.nomagic.magicdraw.core.TipsManager`
`[getTipsManager](#getTipsManager())()`
Returns the tipsManager.
`com.nomagic.magicdraw.lic.MDVersionManager`
`[getVersionManager](#getVersionManager())()`

`void`
`[insertActivityAfterStartup](#insertActivityAfterStartup(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) activity)`

`byte`
`[internalStart](#internalStart(com.nomagic.magicdraw.core.Application.MainFrameController,boolean,boolean,com.nomagic.magicdraw.core.StartupParticipant))(com.nomagic.magicdraw.core.Application.MainFrameController mfController,
 boolean silentMode,
 boolean tryToLoadProject,
 [StartupParticipant](StartupParticipant.html) participant)`
Starts the application.
`boolean`
`[isCanCreateNewProject](#isCanCreateNewProject())()`

`boolean`
`[isPluginsInitialized](#isPluginsInitialized())()`
Checks if plug-ins already initialized.
`boolean`
`[isShowFirstStartupDlg](#isShowFirstStartupDlg())()`
Checks if first startup dialog should be shown.
`boolean`
`[isTryToLoadProject](#isTryToLoadProject())()`
Checks if it is allowed to load project on startup.
`void`
`[loadAliases](#loadAliases())()`
Loads alias.properties file into memory.
`void`
`[notifyPluginsInitialized](#notifyPluginsInitialized())()`
Notifies application event listeners that plugins were initialized.
`void`
`[removeProjectEventListener](#removeProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener))([ProjectEventListener](project/ProjectEventListener.html) listener)`
Method removes ProjectEventListener.
`void`
`[removeSaveParticipant](#removeSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant))([SaveParticipant](SaveParticipant.html) participant)`
Unregister custom SaveParticipant.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[resolveAlias](#resolveAlias(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`

`static [Application.Runtime](Application.Runtime.html)`
`[runtime](#runtime())()`
Gets application runtime.
`static com.nomagic.magicdraw.core.Application.RuntimeInternal`
`[runtimeInternal](#runtimeInternal())()`

`void`
`[saveEnvironmentOptions](#saveEnvironmentOptions())()`
Saves environment options to file.
`void`
`[setApplicationName](#setApplicationName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Set the name of the application.
`void`
`[setApplicationTitleConfigurator](#setApplicationTitleConfigurator(java.util.function.Function))([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> configurator)`

`void`
`[setCanCreateNewProject](#setCanCreateNewProject(boolean))(boolean canCreateNewProject)`

`void`
`[setGUILog](#setGUILog(com.nomagic.magicdraw.core.GUILog))([GUILog](GUILog.html) log)`

`void`
`[setInitialLF](#setInitialLF())()`
Set initial L&F
`void`
`[setShowFirstStartupDlg](#setShowFirstStartupDlg(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> showFirstStartupDlg)`
Sets flag which indicates if first startup dialog should be shown.
`void`
`[setTryToLoadProject](#setTryToLoadProject(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> tryToLoadProject)`
Sets flag which indicates if it is allowed to load project on startup.
`void`
`[shutdown](#shutdown())()`
Shutdowns the application.
`void`
`[shutdown](#shutdown(boolean))(boolean force)`
Shutdowns the application.
`void`
`[shutdown](#shutdown(byte,boolean))(byte exitStatus,
 boolean force)`

`void`
`[start](#start(boolean,boolean,boolean,java.lang.String%5B%5D,com.nomagic.magicdraw.core.StartupParticipant))(boolean visible,
 boolean silentMode,
 boolean tryToLoadProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args,
 [StartupParticipant](StartupParticipant.html) participant)`
Starts the application.
`void`
`[start](#start(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)`
Starts the application.
`static com.nomagic.magicdraw.core.Application.WebInternal`
`[webInternal](#webInternal())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
STARTUP_SUCCESSFUL
public static final byte STARTUP_SUCCESSFUL
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Application.STARTUP_SUCCESSFUL)
STARTUP_CANCELED
public static final byte STARTUP_CANCELED
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Application.STARTUP_CANCELED)
STARTUP_ERROR
public static final byte STARTUP_ERROR
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.core.Application.STARTUP_ERROR)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Application
@OpenApiprotected Application()
Constructor of Application.
 ============ METHOD DETAIL ========== 
Method Details
resolveAlias
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resolveAlias([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
loadAliases
@OpenApipublic void loadAliases()
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Loads alias.properties file into memory. If alias were already loaded reload it.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - in case of some error
addAlias
public void addAlias([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) alias,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
setApplicationTitleConfigurator
public void setApplicationTitleConfigurator([Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> configurator)
getEnvironmentOptions
@OpenApipublic [EnvironmentOptions](options/EnvironmentOptions.html) getEnvironmentOptions()
Gets application environment options.
Returns:
application environment options.
saveEnvironmentOptions
public void saveEnvironmentOptions()
Saves environment options to file.
getInstance
@OpenApipublic static [Application](Application.html) getInstance()
Returns single instance of Application.
Returns:
single instance of Application.
getPluginManager
public com.nomagic.magicdraw.plugins.PluginsManager getPluginManager()
Method getPluginManager.
Returns:
PluginsManager manager for loading, starting stopping plugins.
getPropertyResourceManager
public com.nomagic.magicdraw.properties.PropertyResourceManager getPropertyResourceManager()
Returns propertyResourceManager for managing property resources.
Returns:
manager for providing custom property resources.
getFLManager
public com.nomagic.rcpf.product.lic.floating.client.internal.FLManager getFLManager()
Method getFLManager.
Returns:
PluginsManager manager for loading, starting stopping plugins.
getProject
@CheckForNull
@OpenApipublic [Project](Project.html) getProject()
Returns current active Project.
Returns:
current project, null if there is no current project.
getProjectsManager
@OpenApipublic [ProjectsManager](project/ProjectsManager.html) getProjectsManager()
Returns the projectsManager.
Returns:
ProjectsManager
getMainFrame
@OpenApipublic [MainFrame](../ui/MainFrame.html) getMainFrame()
Returns the mainFrame - main MagicDraw GUI component.
Returns:
MainFrame
setApplicationName
@OpenApipublic void setApplicationName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Set the name of the application.
Parameters:
`name` - application name
getActionsManager
public com.nomagic.magicdraw.actions.ActionsManager getActionsManager()
Returns the actionsManager.
Returns:
ActionsManager
getTipsManager
public com.nomagic.magicdraw.core.TipsManager getTipsManager()
Returns the tipsManager.
Returns:
TipsManager
start
@OpenApipublic void start([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)
 throws [ApplicationExitedException](../../runtime/ApplicationExitedException.html)
Starts the application.
Parameters:
`args` - command line arguments passed to MagicDraw.
Throws:
`[ApplicationExitedException](../../runtime/ApplicationExitedException.html)` - in case of some error
start
@OpenApipublic void start(boolean visible,
 boolean silentMode,
 boolean tryToLoadProject,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args,
 @CheckForNull
 [StartupParticipant](StartupParticipant.html) participant)
 throws [ApplicationExitedException](../../runtime/ApplicationExitedException.html)
Starts the application.
Parameters:
`visible` - start MagicDraw as visible frame?
`silentMode` - true if GUI must be in silent mode(batch mode).
`tryToLoadProject` - true if application should try to load file passed as argument.
`args` - command line arguments passed to MagicDraw.
`participant` - the participant of startup process. May be null.
Throws:
`[ApplicationExitedException](../../runtime/ApplicationExitedException.html)` - if application exists during the startup.
setInitialLF
public void setInitialLF()
Set initial L&F
internalStart
public byte internalStart(com.nomagic.magicdraw.core.Application.MainFrameController mfController,
 boolean silentMode,
 boolean tryToLoadProject,
 @CheckForNull
 [StartupParticipant](StartupParticipant.html) participant)
Starts the application.
Parameters:
`mfController` - the controller for controlling the main window appearance.
`silentMode` - true if GUI must be in silent mode.
`tryToLoadProject` - true if application should try to load file passed as argument.
`participant` - the participant of startup process. May be null.
Returns:
STARTUP_SUCCESSFUL if starting was without fatal errors,
 STARTUP_CANCELED - canceled by the user on dialogs, STARTUP_ERROR - on any error
executeActivitiesOnUICreation
public final void executeActivitiesOnUICreation()
Executes registered UI activities.
shutdown
@OpenApipublic void shutdown()
 throws [ApplicationExitedException](../../runtime/ApplicationExitedException.html)
Shutdowns the application. User will be asked to save all opened projects before
 exiting the application.
Throws:
`[ApplicationExitedException](../../runtime/ApplicationExitedException.html)` - in case of some error
shutdown
public void shutdown(boolean force)
Shutdowns the application. User will be asked to save all opened projects before
 exiting the application.
Parameters:
`force` - exit the application in any case (ignore if project is not saved if plugin is not closed).
shutdown
public void shutdown(byte exitStatus,
 boolean force)
getGUILog
@OpenApipublic [GUILog](GUILog.html) getGUILog()
Returns the interface to log window.
Returns:
window for writing messages.
setGUILog
public void setGUILog([GUILog](GUILog.html) log)
getOpenAPIVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOpenAPIVersion()
Version of OpenAPI
Returns:
version of OpenAPI.
getRecentFilesManager
public com.nomagic.magicdraw.ui.RecentFilesManager getRecentFilesManager()
Returns the recentFilesManager.
Returns:
RecentFilesManager
addProjectEventListener
@OpenApipublic final void addProjectEventListener([ProjectEventListener](project/ProjectEventListener.html) listener)
Method adds new ProjectEventListener.
Parameters:
`listener` - listener to be added.
removeProjectEventListener
@OpenApipublic void removeProjectEventListener([ProjectEventListener](project/ProjectEventListener.html) listener)
Method removes ProjectEventListener.
Parameters:
`listener` - to be removed.
addActivityAfterStartup
@OpenApipublic void addActivityAfterStartup([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) activity)
Registered runnable is executed right after MagicDraw application startup.
Parameters:
`activity` - runnable to execute.
addActivityOnUICreation
public void addActivityOnUICreation([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) activity)
[`Runnable`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) which will be run on UI creation.
Parameters:
`activity` - instance of [`Runnable`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)
insertActivityAfterStartup
public void insertActivityAfterStartup([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) activity)
getCookieSet
@OpenApipublic final [CookieSet](../cookies/CookieSet.html) getCookieSet()
Returns cookie set of the application. 
This cookie set may be used for example to replace standard application
 CloseCookie with some other. 

 The example: 

 CookieSet set = application.getCookieSet(); 

 CloseCookie newCloseCookie = ...; 

 CloseCookie close = (CloseCookie) set.getCookie(CloseCookie.class); 

 set.remove(close); 

 set.add(newCloseCookie);
Returns:
cookie set of the application.
exit
public void exit(byte exitStatus)
Exits the application. Calls close method for registered CloseCookie.
Parameters:
`exitStatus` - exit code
exit
public void exit()
Exits the application with Application.STARTUP_ERROR exit code. Calls close method for registered CloseCookie.
addNewDiagramType
@OpenApipublic void addNewDiagramType([DiagramDescriptor](../uml/DiagramDescriptor.html) descriptor)
Registers new diagram type in the MagicDraw application.
Parameters:
`descriptor` - descriptor of the new diagram.
getAlias
public com.nomagic.magicdraw.core.Alias getAlias()
getSaveParticipants
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[SaveParticipant](SaveParticipant.html)> getSaveParticipants()
List of registered SaveParticipants.
Returns:
list of registered Save Participants.
addSaveParticipant
@OpenApipublic void addSaveParticipant([SaveParticipant](SaveParticipant.html) participant)
Registers SaveParticipant for custom actions on project saving.
Parameters:
`participant` - the custom SaveParticipant.
removeSaveParticipant
@OpenApipublic void removeSaveParticipant([SaveParticipant](SaveParticipant.html) participant)
Unregister custom SaveParticipant.
Parameters:
`participant` - the custom SaveParticipant.
getVersionManager
public com.nomagic.magicdraw.lic.MDVersionManager getVersionManager()
isCanCreateNewProject
public boolean isCanCreateNewProject()
setCanCreateNewProject
public void setCanCreateNewProject(boolean canCreateNewProject)
getDiagramDescriptor
@CheckForNullpublic [DiagramDescriptor](../uml/DiagramDescriptor.html) getDiagramDescriptor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagramType)
Parameters:
`diagramType` - diagram type to get its descriptor.
Returns:
DiagramDescriptor for given type. If type is unknown return null.
getIntegrationsManager
public com.nomagic.magicdraw.integrations.IntegratorsManager getIntegrationsManager()
Returns:
an Integrations manager.
addApplicationEventListener
public void addApplicationEventListener(com.nomagic.magicdraw.core.ApplicationEventListener listener)
Adds application event listener to application listeners.
Parameters:
`listener` - listener to add.
notifyPluginsInitialized
public void notifyPluginsInitialized()
Notifies application event listeners that plugins were initialized.
isTryToLoadProject
@OpenApipublic boolean isTryToLoadProject()
Checks if it is allowed to load project on startup. Under integrations loading may cause deadlock and is disabled.
Returns:
true if project may be loaded on application startup.
setTryToLoadProject
public void setTryToLoadProject([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> tryToLoadProject)
Sets flag which indicates if it is allowed to load project on startup.
Parameters:
`tryToLoadProject` - flag which indicates if it is allowed to load project on startup
isShowFirstStartupDlg
public boolean isShowFirstStartupDlg()
Checks if first startup dialog should be shown.
Returns:
true if first startup dialog should be shown.
setShowFirstStartupDlg
public void setShowFirstStartupDlg([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> showFirstStartupDlg)
Sets flag which indicates if first startup dialog should be shown.
Parameters:
`showFirstStartupDlg` - flag which indicates if first startup dialog should be shown.
isPluginsInitialized
public boolean isPluginsInitialized()
Checks if plug-ins already initialized.
Returns:
true if plug-ins already initialized.
runtimeInternal
public static com.nomagic.magicdraw.core.Application.RuntimeInternal runtimeInternal()
runtime
@OpenApipublic static [Application.Runtime](Application.Runtime.html) runtime()
Gets application runtime.
Returns:
application runtime.
environmentInternal
public static com.nomagic.magicdraw.core.Application.EnvironmentInternal environmentInternal()
environment
@OpenApipublic static [Application.Environment](Application.Environment.html) environment()
Gets application environment.
Returns:
application environment.
webInternal
public static com.nomagic.magicdraw.core.Application.WebInternal webInternal()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Class Application">Class Application</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.Application</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Application</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Main class which  connects main parts of MagicDraw.
 This class is singleton, only one instance of this class can exist.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="Application.Environment.html" title="class in com.nomagic.magicdraw.core">Application.Environment</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains application environment specific constants and utility methods.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Application.Runtime.html" title="class in com.nomagic.magicdraw.core">Application.Runtime</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains application runtime related constants and utility methods.</div>
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
<div class="col-first even-row-color"><code>static final byte</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STARTUP_CANCELED">STARTUP_CANCELED</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final byte</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STARTUP_ERROR">STARTUP_ERROR</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final byte</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STARTUP_SUCCESSFUL">STARTUP_SUCCESSFUL</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Application</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor of Application.</div>
</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addActivityAfterStartup(java.lang.Runnable)">addActivityAfterStartup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> activity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registered runnable is executed right after MagicDraw application startup.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addActivityOnUICreation(java.lang.Runnable)">addActivityOnUICreation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> activity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a> which will be run on UI creation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAlias(java.lang.String,java.lang.String,java.lang.String)">addAlias</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> alias,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addApplicationEventListener(com.nomagic.magicdraw.core.ApplicationEventListener)">addApplicationEventListener</a><wbr/>(com.nomagic.magicdraw.core.ApplicationEventListener listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds application event listener to application listeners.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addNewDiagramType(com.nomagic.magicdraw.uml.DiagramDescriptor)">addNewDiagramType</a><wbr/>(<a href="../uml/DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a> descriptor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers new diagram type in the MagicDraw application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">addProjectEventListener</a><wbr/>(<a href="project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method adds new ProjectEventListener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant)">addSaveParticipant</a><wbr/>(<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a> participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers SaveParticipant for custom actions on project saving.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Application.Environment.html" title="class in com.nomagic.magicdraw.core">Application.Environment</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#environment()">environment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets application environment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.core.Application.EnvironmentInternal</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#environmentInternal()">environmentInternal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executeActivitiesOnUICreation()">executeActivitiesOnUICreation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Executes registered UI activities.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exit()">exit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Exits the application with Application.STARTUP_ERROR exit code.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exit(byte)">exit</a><wbr/>(byte exitStatus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Exits the application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.actions.ActionsManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActionsManager()">getActionsManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the actionsManager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.Alias</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAlias()">getAlias</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a href="../cookies/CookieSet.html" title="class in com.nomagic.magicdraw.cookies">CookieSet</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCookieSet()">getCookieSet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns cookie set of the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramDescriptor(java.lang.String)">getDiagramDescriptor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="options/EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options">EnvironmentOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnvironmentOptions()">getEnvironmentOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets application environment options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.rcpf.product.lic.floating.client.internal.FLManager</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFLManager()">getFLManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method getFLManager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="GUILog.html" title="class in com.nomagic.magicdraw.core">GUILog</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGUILog()">getGUILog</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the interface to log window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Application.html" title="class in com.nomagic.magicdraw.core">Application</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns single instance of Application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.integrations.IntegratorsManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIntegrationsManager()">getIntegrationsManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ui/MainFrame.html" title="class in com.nomagic.magicdraw.ui">MainFrame</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainFrame()">getMainFrame</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the mainFrame - main MagicDraw GUI component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpenAPIVersion()">getOpenAPIVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Version of OpenAPI</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.plugins.PluginsManager</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPluginManager()">getPluginManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method getPluginManager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns current active Project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="project/ProjectsManager.html" title="class in com.nomagic.magicdraw.core.project">ProjectsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectsManager()">getProjectsManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the projectsManager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.properties.PropertyResourceManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyResourceManager()">getPropertyResourceManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns propertyResourceManager for managing property resources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.RecentFilesManager</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRecentFilesManager()">getRecentFilesManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the recentFilesManager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSaveParticipants()">getSaveParticipants</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">List of registered SaveParticipants.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.TipsManager</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTipsManager()">getTipsManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the tipsManager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.lic.MDVersionManager</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersionManager()">getVersionManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#insertActivityAfterStartup(java.lang.Runnable)">insertActivityAfterStartup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> activity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>byte</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalStart(com.nomagic.magicdraw.core.Application.MainFrameController,boolean,boolean,com.nomagic.magicdraw.core.StartupParticipant)">internalStart</a><wbr/>(com.nomagic.magicdraw.core.Application.MainFrameController mfController,
 boolean silentMode,
 boolean tryToLoadProject,
 <a href="StartupParticipant.html" title="interface in com.nomagic.magicdraw.core">StartupParticipant</a> participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCanCreateNewProject()">isCanCreateNewProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPluginsInitialized()">isPluginsInitialized</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if plug-ins already initialized.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowFirstStartupDlg()">isShowFirstStartupDlg</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if first startup dialog should be shown.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTryToLoadProject()">isTryToLoadProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if it is allowed to load project on startup.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadAliases()">loadAliases</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads alias.properties file into memory.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyPluginsInitialized()">notifyPluginsInitialized</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies application event listeners that plugins were initialized.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">removeProjectEventListener</a><wbr/>(<a href="project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method removes ProjectEventListener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant)">removeSaveParticipant</a><wbr/>(<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a> participant)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Unregister custom SaveParticipant.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resolveAlias(java.lang.String,java.lang.String)">resolveAlias</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Application.Runtime.html" title="class in com.nomagic.magicdraw.core">Application.Runtime</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#runtime()">runtime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets application runtime.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.core.Application.RuntimeInternal</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#runtimeInternal()">runtimeInternal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveEnvironmentOptions()">saveEnvironmentOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves environment options to file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setApplicationName(java.lang.String)">setApplicationName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the name of the application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setApplicationTitleConfigurator(java.util.function.Function)">setApplicationTitleConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCanCreateNewProject(boolean)">setCanCreateNewProject</a><wbr/>(boolean canCreateNewProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGUILog(com.nomagic.magicdraw.core.GUILog)">setGUILog</a><wbr/>(<a href="GUILog.html" title="class in com.nomagic.magicdraw.core">GUILog</a> log)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInitialLF()">setInitialLF</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set initial L&amp;F</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowFirstStartupDlg(java.util.function.Supplier)">setShowFirstStartupDlg</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; showFirstStartupDlg)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets flag which indicates if first startup dialog should be shown.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTryToLoadProject(java.util.function.Supplier)">setTryToLoadProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; tryToLoadProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets flag which indicates if it is allowed to load project on startup.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shutdown()">shutdown</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shutdowns the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shutdown(boolean)">shutdown</a><wbr/>(boolean force)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shutdowns the application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shutdown(byte,boolean)">shutdown</a><wbr/>(byte exitStatus,
 boolean force)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(boolean,boolean,boolean,java.lang.String%5B%5D,com.nomagic.magicdraw.core.StartupParticipant)">start</a><wbr/>(boolean visible,
 boolean silentMode,
 boolean tryToLoadProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args,
 <a href="StartupParticipant.html" title="interface in com.nomagic.magicdraw.core">StartupParticipant</a> participant)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts the application.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(java.lang.String%5B%5D)">start</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static com.nomagic.magicdraw.core.Application.WebInternal</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#webInternal()">webInternal</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="STARTUP_SUCCESSFUL">
<h3>STARTUP_SUCCESSFUL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">byte</span> <span class="element-name">STARTUP_SUCCESSFUL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Application.STARTUP_SUCCESSFUL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STARTUP_CANCELED">
<h3>STARTUP_CANCELED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">byte</span> <span class="element-name">STARTUP_CANCELED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Application.STARTUP_CANCELED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STARTUP_ERROR">
<h3>STARTUP_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">byte</span> <span class="element-name">STARTUP_ERROR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.core.Application.STARTUP_ERROR">Constant Field Values</a></li>
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
<h3>Application</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="element-name">Application</span>()</div>
<div class="block">Constructor of Application.</div>
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
<section class="detail" id="resolveAlias(java.lang.String,java.lang.String)">
<h3>resolveAlias</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">resolveAlias</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="loadAliases()">
<h3>loadAliases</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadAliases</span>()
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Loads alias.properties file into memory. If alias were already loaded reload it.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAlias(java.lang.String,java.lang.String,java.lang.String)">
<h3>addAlias</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addAlias</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> alias,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="setApplicationTitleConfigurator(java.util.function.Function)">
<h3>setApplicationTitleConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setApplicationTitleConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; configurator)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEnvironmentOptions()">
<h3>getEnvironmentOptions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="options/EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options">EnvironmentOptions</a></span> <span class="element-name">getEnvironmentOptions</span>()</div>
<div class="block">Gets application environment options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application environment options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveEnvironmentOptions()">
<h3>saveEnvironmentOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">saveEnvironmentOptions</span>()</div>
<div class="block">Saves environment options to file.</div>
</section>
</li>
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Application.html" title="class in com.nomagic.magicdraw.core">Application</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns single instance of Application.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>single instance of Application.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPluginManager()">
<h3>getPluginManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.plugins.PluginsManager</span> <span class="element-name">getPluginManager</span>()</div>
<div class="block">Method getPluginManager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>PluginsManager manager for loading, starting stopping plugins.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyResourceManager()">
<h3>getPropertyResourceManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.properties.PropertyResourceManager</span> <span class="element-name">getPropertyResourceManager</span>()</div>
<div class="block">Returns propertyResourceManager for managing property resources.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>manager for providing custom property resources.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFLManager()">
<h3>getFLManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.rcpf.product.lic.floating.client.internal.FLManager</span> <span class="element-name">getFLManager</span>()</div>
<div class="block">Method getFLManager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>PluginsManager manager for loading, starting stopping plugins.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Returns current active Project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>current project, null if there is no current project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectsManager()">
<h3>getProjectsManager</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="project/ProjectsManager.html" title="class in com.nomagic.magicdraw.core.project">ProjectsManager</a></span> <span class="element-name">getProjectsManager</span>()</div>
<div class="block">Returns the projectsManager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ProjectsManager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainFrame()">
<h3>getMainFrame</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../ui/MainFrame.html" title="class in com.nomagic.magicdraw.ui">MainFrame</a></span> <span class="element-name">getMainFrame</span>()</div>
<div class="block">Returns the mainFrame - main MagicDraw GUI component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>MainFrame</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplicationName(java.lang.String)">
<h3>setApplicationName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setApplicationName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Set the name of the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - application name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActionsManager()">
<h3>getActionsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.actions.ActionsManager</span> <span class="element-name">getActionsManager</span>()</div>
<div class="block">Returns the actionsManager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ActionsManager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTipsManager()">
<h3>getTipsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.TipsManager</span> <span class="element-name">getTipsManager</span>()</div>
<div class="block">Returns the tipsManager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>TipsManager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(java.lang.String[])">
<h3>start</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</span>
           throws <span class="exceptions"><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></span></div>
<div class="block">Starts the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>args</code> - command line arguments passed to MagicDraw.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(boolean,boolean,boolean,java.lang.String[],com.nomagic.magicdraw.core.StartupParticipant)">
<h3>start</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(boolean visible,
 boolean silentMode,
 boolean tryToLoadProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args,
 @CheckForNull
 <a href="StartupParticipant.html" title="interface in com.nomagic.magicdraw.core">StartupParticipant</a> participant)</span>
           throws <span class="exceptions"><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></span></div>
<div class="block">Starts the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visible</code> - start MagicDraw as visible frame?</dd>
<dd><code>silentMode</code> - true if GUI must be in silent mode(batch mode).</dd>
<dd><code>tryToLoadProject</code> - true if application should try to load file passed as argument.</dd>
<dd><code>args</code> - command line arguments passed to MagicDraw.</dd>
<dd><code>participant</code> - the participant of startup process. May be null.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></code> - if application exists during the startup.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInitialLF()">
<h3>setInitialLF</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInitialLF</span>()</div>
<div class="block">Set initial L&amp;F</div>
</section>
</li>
<li>
<section class="detail" id="internalStart(com.nomagic.magicdraw.core.Application.MainFrameController,boolean,boolean,com.nomagic.magicdraw.core.StartupParticipant)">
<h3>internalStart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">byte</span> <span class="element-name">internalStart</span><wbr/><span class="parameters">(com.nomagic.magicdraw.core.Application.MainFrameController mfController,
 boolean silentMode,
 boolean tryToLoadProject,
 @CheckForNull
 <a href="StartupParticipant.html" title="interface in com.nomagic.magicdraw.core">StartupParticipant</a> participant)</span></div>
<div class="block">Starts the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mfController</code> - the controller for controlling the main window appearance.</dd>
<dd><code>silentMode</code> - true if GUI must be in silent mode.</dd>
<dd><code>tryToLoadProject</code> - true if application should try to load file passed as argument.</dd>
<dd><code>participant</code> - the participant of startup process. May be null.</dd>
<dt>Returns:</dt>
<dd>STARTUP_SUCCESSFUL if starting was without fatal errors,
 STARTUP_CANCELED - canceled by the user on dialogs, STARTUP_ERROR - on any error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executeActivitiesOnUICreation()">
<h3>executeActivitiesOnUICreation</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">executeActivitiesOnUICreation</span>()</div>
<div class="block">Executes registered UI activities.</div>
</section>
</li>
<li>
<section class="detail" id="shutdown()">
<h3>shutdown</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">shutdown</span>()
              throws <span class="exceptions"><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></span></div>
<div class="block">Shutdowns the application. User will be asked to save all opened projects before
 exiting the application.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="../../runtime/ApplicationExitedException.html" title="class in com.nomagic.runtime">ApplicationExitedException</a></code> - in case of some error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shutdown(boolean)">
<h3>shutdown</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">shutdown</span><wbr/><span class="parameters">(boolean force)</span></div>
<div class="block">Shutdowns the application. User will be asked to save all opened projects before
 exiting the application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>force</code> - exit the application in any case (ignore if project is not saved if plugin is not closed).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shutdown(byte,boolean)">
<h3>shutdown</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">shutdown</span><wbr/><span class="parameters">(byte exitStatus,
 boolean force)</span></div>
</section>
</li>
<li>
<section class="detail" id="getGUILog()">
<h3>getGUILog</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="GUILog.html" title="class in com.nomagic.magicdraw.core">GUILog</a></span> <span class="element-name">getGUILog</span>()</div>
<div class="block">Returns the interface to log window.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>window for writing messages.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGUILog(com.nomagic.magicdraw.core.GUILog)">
<h3>setGUILog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGUILog</span><wbr/><span class="parameters">(<a href="GUILog.html" title="class in com.nomagic.magicdraw.core">GUILog</a> log)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOpenAPIVersion()">
<h3>getOpenAPIVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOpenAPIVersion</span>()</div>
<div class="block">Version of OpenAPI</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>version of OpenAPI.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRecentFilesManager()">
<h3>getRecentFilesManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.RecentFilesManager</span> <span class="element-name">getRecentFilesManager</span>()</div>
<div class="block">Returns the recentFilesManager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>RecentFilesManager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">
<h3>addProjectEventListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">addProjectEventListener</span><wbr/><span class="parameters">(<a href="project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</span></div>
<div class="block">Method adds new ProjectEventListener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeProjectEventListener(com.nomagic.magicdraw.core.project.ProjectEventListener)">
<h3>removeProjectEventListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeProjectEventListener</span><wbr/><span class="parameters">(<a href="project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a> listener)</span></div>
<div class="block">Method removes ProjectEventListener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addActivityAfterStartup(java.lang.Runnable)">
<h3>addActivityAfterStartup</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addActivityAfterStartup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> activity)</span></div>
<div class="block">Registered runnable is executed right after MagicDraw application startup.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activity</code> - runnable to execute.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addActivityOnUICreation(java.lang.Runnable)">
<h3>addActivityOnUICreation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addActivityOnUICreation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> activity)</span></div>
<div class="block"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a> which will be run on UI creation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activity</code> - instance of <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insertActivityAfterStartup(java.lang.Runnable)">
<h3>insertActivityAfterStartup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">insertActivityAfterStartup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> activity)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCookieSet()">
<h3>getCookieSet</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a href="../cookies/CookieSet.html" title="class in com.nomagic.magicdraw.cookies">CookieSet</a></span> <span class="element-name">getCookieSet</span>()</div>
<div class="block">Returns cookie set of the application. <br/>This cookie set may be used for example to replace standard application
 CloseCookie with some other.<br/>
 The example:<br/>
 CookieSet set = application.getCookieSet();<br/>
 CloseCookie newCloseCookie = ...;<br/>
 CloseCookie close = (CloseCookie) set.getCookie(CloseCookie.class);<br/>
 set.remove(close);<br/>
 set.add(newCloseCookie);<br/></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>cookie set of the application.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exit(byte)">
<h3>exit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">exit</span><wbr/><span class="parameters">(byte exitStatus)</span></div>
<div class="block">Exits the application. Calls close method for registered CloseCookie.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exitStatus</code> - exit code</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exit()">
<h3>exit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">exit</span>()</div>
<div class="block">Exits the application with Application.STARTUP_ERROR exit code. Calls close method for registered CloseCookie.</div>
</section>
</li>
<li>
<section class="detail" id="addNewDiagramType(com.nomagic.magicdraw.uml.DiagramDescriptor)">
<h3>addNewDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addNewDiagramType</span><wbr/><span class="parameters">(<a href="../uml/DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a> descriptor)</span></div>
<div class="block">Registers new diagram type in the MagicDraw application.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - descriptor of the new diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAlias()">
<h3>getAlias</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.Alias</span> <span class="element-name">getAlias</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSaveParticipants()">
<h3>getSaveParticipants</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a>&gt;</span> <span class="element-name">getSaveParticipants</span>()</div>
<div class="block">List of registered SaveParticipants.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of registered Save Participants.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant)">
<h3>addSaveParticipant</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSaveParticipant</span><wbr/><span class="parameters">(<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a> participant)</span></div>
<div class="block">Registers SaveParticipant for custom actions on project saving.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>participant</code> - the custom SaveParticipant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSaveParticipant(com.nomagic.magicdraw.core.SaveParticipant)">
<h3>removeSaveParticipant</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSaveParticipant</span><wbr/><span class="parameters">(<a href="SaveParticipant.html" title="interface in com.nomagic.magicdraw.core">SaveParticipant</a> participant)</span></div>
<div class="block">Unregister custom SaveParticipant.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>participant</code> - the custom SaveParticipant.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersionManager()">
<h3>getVersionManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.lic.MDVersionManager</span> <span class="element-name">getVersionManager</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isCanCreateNewProject()">
<h3>isCanCreateNewProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCanCreateNewProject</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCanCreateNewProject(boolean)">
<h3>setCanCreateNewProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCanCreateNewProject</span><wbr/><span class="parameters">(boolean canCreateNewProject)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDiagramDescriptor(java.lang.String)">
<h3>getDiagramDescriptor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/DiagramDescriptor.html" title="class in com.nomagic.magicdraw.uml">DiagramDescriptor</a></span> <span class="element-name">getDiagramDescriptor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type to get its descriptor.</dd>
<dt>Returns:</dt>
<dd>DiagramDescriptor for given type. If type is unknown return null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntegrationsManager()">
<h3>getIntegrationsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.integrations.IntegratorsManager</span> <span class="element-name">getIntegrationsManager</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an Integrations manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addApplicationEventListener(com.nomagic.magicdraw.core.ApplicationEventListener)">
<h3>addApplicationEventListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addApplicationEventListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.core.ApplicationEventListener listener)</span></div>
<div class="block">Adds application event listener to application listeners.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notifyPluginsInitialized()">
<h3>notifyPluginsInitialized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">notifyPluginsInitialized</span>()</div>
<div class="block">Notifies application event listeners that plugins were initialized.</div>
</section>
</li>
<li>
<section class="detail" id="isTryToLoadProject()">
<h3>isTryToLoadProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTryToLoadProject</span>()</div>
<div class="block">Checks if it is allowed to load project on startup. Under integrations loading may cause deadlock and is disabled.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if project may be loaded on application startup.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTryToLoadProject(java.util.function.Supplier)">
<h3>setTryToLoadProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTryToLoadProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; tryToLoadProject)</span></div>
<div class="block">Sets flag which indicates if it is allowed to load project on startup.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tryToLoadProject</code> - flag which indicates if it is allowed to load project on startup</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowFirstStartupDlg()">
<h3>isShowFirstStartupDlg</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowFirstStartupDlg</span>()</div>
<div class="block">Checks if first startup dialog should be shown.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if first startup dialog should be shown.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowFirstStartupDlg(java.util.function.Supplier)">
<h3>setShowFirstStartupDlg</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowFirstStartupDlg</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; showFirstStartupDlg)</span></div>
<div class="block">Sets flag which indicates if first startup dialog should be shown.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>showFirstStartupDlg</code> - flag which indicates if first startup dialog should be shown.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPluginsInitialized()">
<h3>isPluginsInitialized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPluginsInitialized</span>()</div>
<div class="block">Checks if plug-ins already initialized.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if plug-ins already initialized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runtimeInternal()">
<h3>runtimeInternal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.core.Application.RuntimeInternal</span> <span class="element-name">runtimeInternal</span>()</div>
</section>
</li>
<li>
<section class="detail" id="runtime()">
<h3>runtime</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Application.Runtime.html" title="class in com.nomagic.magicdraw.core">Application.Runtime</a></span> <span class="element-name">runtime</span>()</div>
<div class="block">Gets application runtime.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application runtime.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="environmentInternal()">
<h3>environmentInternal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.core.Application.EnvironmentInternal</span> <span class="element-name">environmentInternal</span>()</div>
</section>
</li>
<li>
<section class="detail" id="environment()">
<h3>environment</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="Application.Environment.html" title="class in com.nomagic.magicdraw.core">Application.Environment</a></span> <span class="element-name">environment</span>()</div>
<div class="block">Gets application environment.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>application environment.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="webInternal()">
<h3>webInternal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">com.nomagic.magicdraw.core.Application.WebInternal</span> <span class="element-name">webInternal</span>()</div>
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
