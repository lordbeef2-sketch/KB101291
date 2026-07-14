# JAVA OPENAPI: MainFrame (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/MainFrame.html
- source_path: `com/nomagic/magicdraw/ui/MainFrame.html`
- source_sha256: `8a73e180121f5b881de31d1d54061151dbaf276091fed58dbc508fd498ce52b9`
- captured_utc: `2026-07-14T16:55:50.864405+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class MainFrame

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.awt.Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)
[java.awt.Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html)
[java.awt.Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)
[java.awt.Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html)
[javax.swing.JFrame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html)
com.jidesoft.docking.DefaultDockableHolder
com.jidesoft.action.DefaultDockableBarDockableHolder
com.nomagic.magicdraw.ui.MainFrame

All Implemented Interfaces:
`com.jidesoft.action.DockableBarDockableHolder`, `com.jidesoft.action.DockableBarHolder`, `com.jidesoft.docking.DockableHolder`, `[ActionsGroups](../actions/ActionsGroups.html)`, `[EnvironmentOptions.EnvironmentChangeListener](../core/options/EnvironmentOptions.EnvironmentChangeListener.html)`, `com.nomagic.ui.CursorOwner`, `[ImageObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html)`, `[MenuContainer](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html)`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`, `[Accessible](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/accessibility/Accessible.html)`, `[RootPaneContainer](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/RootPaneContainer.html)`, `[WindowConstants](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html)`

@OpenApipublic final classMainFrame
extends com.jidesoft.action.DefaultDockableBarDockableHolder
implements [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html), com.nomagic.ui.CursorOwner, [ActionsGroups](../actions/ActionsGroups.html), [EnvironmentOptions.EnvironmentChangeListener](../core/options/EnvironmentOptions.EnvironmentChangeListener.html)

The `MainFrame` class represents main window of the MagicDraw application.
 Also it has a set of inner classes- event listeners to handle all menu and toolbar events.

See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.magicdraw.ui.MainFrame)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MAIN_TOOLBAR_EXPERT](#MAIN_TOOLBAR_EXPERT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MAIN_TOOLBAR_STANDARD](#MAIN_TOOLBAR_STANDARD)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RECENT_PROJECT_NAME_CHANGE](#RECENT_PROJECT_NAME_CHANGE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[RECENT_WINDOWS](#RECENT_WINDOWS)`
Fields inherited from class com.jidesoft.docking.DefaultDockableHolder
`_autoDispose, _contentContainer, _dockingManager`
Fields inherited from class javax.swing.[JFrame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html)
`[accessibleContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#accessibleContext), [rootPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#rootPane), [rootPaneCheckingEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#rootPaneCheckingEnabled)`
Fields inherited from class java.awt.[Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html)
`[CROSSHAIR_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#CROSSHAIR_CURSOR), [DEFAULT_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#DEFAULT_CURSOR), [E_RESIZE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#E_RESIZE_CURSOR), [HAND_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#HAND_CURSOR), [ICONIFIED](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#ICONIFIED), [MAXIMIZED_BOTH](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#MAXIMIZED_BOTH), [MAXIMIZED_HORIZ](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#MAXIMIZED_HORIZ), [MAXIMIZED_VERT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#MAXIMIZED_VERT), [MOVE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#MOVE_CURSOR), [N_RESIZE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#N_RESIZE_CURSOR), [NE_RESIZE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#NE_RESIZE_CURSOR), [NORMAL](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#NORMAL), [NW_RESIZE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#NW_RESIZE_CURSOR), [S_RESIZE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#S_RESIZE_CURSOR), [SE_RESIZE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#SE_RESIZE_CURSOR), [SW_RESIZE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#SW_RESIZE_CURSOR), [TEXT_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#TEXT_CURSOR), [W_RESIZE_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#W_RESIZE_CURSOR), [WAIT_CURSOR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#WAIT_CURSOR)`
Fields inherited from class java.awt.[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)
`[BOTTOM_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#BOTTOM_ALIGNMENT), [CENTER_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#CENTER_ALIGNMENT), [LEFT_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#LEFT_ALIGNMENT), [RIGHT_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#RIGHT_ALIGNMENT), [TOP_ALIGNMENT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#TOP_ALIGNMENT)`
Fields inherited from interface com.nomagic.magicdraw.actions.[ActionsGroups](../actions/ActionsGroups.html)
`[ANY_DIAGRAM_EDIT_RELATED](../actions/ActionsGroups.html#ANY_DIAGRAM_EDIT_RELATED), [ANY_DIAGRAM_OPENED_RELATED](../actions/ActionsGroups.html#ANY_DIAGRAM_OPENED_RELATED), [ANY_PROJECT_EDIT_RELATED](../actions/ActionsGroups.html#ANY_PROJECT_EDIT_RELATED), [ANY_PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#ANY_PROJECT_OPENED_RELATED), [ANY_PROJECT_SAVING_RELATED](../actions/ActionsGroups.html#ANY_PROJECT_SAVING_RELATED), [ANY_REMOTE_ANY_PROJECT_EDIT_RELATED](../actions/ActionsGroups.html#ANY_REMOTE_ANY_PROJECT_EDIT_RELATED), [ANY_REMOTE_PROJECT_EDIT_RELATED](../actions/ActionsGroups.html#ANY_REMOTE_PROJECT_EDIT_RELATED), [ANY_REMOTE_PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#ANY_REMOTE_PROJECT_OPENED_RELATED), [ANY_REMOTE_UML_PROJECT_EDIT_RELATED](../actions/ActionsGroups.html#ANY_REMOTE_UML_PROJECT_EDIT_RELATED), [ANY_SERVER_LOGIN_RELATED](../actions/ActionsGroups.html#ANY_SERVER_LOGIN_RELATED), [APPLICATION_RELATED](../actions/ActionsGroups.html#APPLICATION_RELATED), [DIAGRAM_EDIT_RELATED](../actions/ActionsGroups.html#DIAGRAM_EDIT_RELATED), [DIAGRAM_OPENED_RELATED](../actions/ActionsGroups.html#DIAGRAM_OPENED_RELATED), [DIAGRAM_RELATED_ELEMENTS](../actions/ActionsGroups.html#DIAGRAM_RELATED_ELEMENTS), [DIAGRAM_ZOOMIN_RELATED](../actions/ActionsGroups.html#DIAGRAM_ZOOMIN_RELATED), [DIAGRAM_ZOOMOUT_RELATED](../actions/ActionsGroups.html#DIAGRAM_ZOOMOUT_RELATED), [DIAGRAM_ZOOMTO11_RELATED](../actions/ActionsGroups.html#DIAGRAM_ZOOMTO11_RELATED), [EDITOR_OPENED_RELATED](../actions/ActionsGroups.html#EDITOR_OPENED_RELATED), [ESI_ANY_PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#ESI_ANY_PROJECT_OPENED_RELATED), [ESI_PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#ESI_PROJECT_OPENED_RELATED), [ESI_SERVER_LOGIN_RELATED](../actions/ActionsGroups.html#ESI_SERVER_LOGIN_RELATED), [ESI_UML_PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#ESI_UML_PROJECT_OPENED_RELATED), [LAYOUT_SHAPES_RELATED](../actions/ActionsGroups.html#LAYOUT_SHAPES_RELATED), [LOCAL_PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#LOCAL_PROJECT_OPENED_RELATED), [LOCAL_UML_PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#LOCAL_UML_PROJECT_OPENED_RELATED), [NOT_EMPTY_ANY_DIAGRAM_RELATED](../actions/ActionsGroups.html#NOT_EMPTY_ANY_DIAGRAM_RELATED), [NOT_EMPTY_CLASS_DIAGRAM_RELATED](../actions/ActionsGroups.html#NOT_EMPTY_CLASS_DIAGRAM_RELATED), [NOT_EMPTY_DIAGRAM_RELATED](../actions/ActionsGroups.html#NOT_EMPTY_DIAGRAM_RELATED), [OPENED_MODULE_AS_PROJECT](../actions/ActionsGroups.html#OPENED_MODULE_AS_PROJECT), [PATH_STYLE_EDIT_RELATED](../actions/ActionsGroups.html#PATH_STYLE_EDIT_RELATED), [PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED](../actions/ActionsGroups.html#PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED), [PRESENTATION_ELEMENT_ALIGN_RELATED](../actions/ActionsGroups.html#PRESENTATION_ELEMENT_ALIGN_RELATED), [PRESENTATION_ELEMENT_SELECTION_RELATED](../actions/ActionsGroups.html#PRESENTATION_ELEMENT_SELECTION_RELATED), [PROJECT_EDIT_RELATED](../actions/ActionsGroups.html#PROJECT_EDIT_RELATED), [PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#PROJECT_OPENED_RELATED), [PROJECT_SAVING_RELATED](../actions/ActionsGroups.html#PROJECT_SAVING_RELATED), [REDO_COMMAND_RELATED](../actions/ActionsGroups.html#REDO_COMMAND_RELATED), [STANDARD_SYSTEM_PROFILE_OPENED_RELATED](../actions/ActionsGroups.html#STANDARD_SYSTEM_PROFILE_OPENED_RELATED), [UML_PROJECT_EDIT_RELATED](../actions/ActionsGroups.html#UML_PROJECT_EDIT_RELATED), [UML_PROJECT_OPENED_RELATED](../actions/ActionsGroups.html#UML_PROJECT_OPENED_RELATED), [UNDO_COMMAND_RELATED](../actions/ActionsGroups.html#UNDO_COMMAND_RELATED)`
Fields inherited from interface java.awt.image.[ImageObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html)
`[ABORT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ABORT), [ALLBITS](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ALLBITS), [ERROR](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ERROR), [FRAMEBITS](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#FRAMEBITS), [HEIGHT](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#HEIGHT), [PROPERTIES](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#PROPERTIES), [SOMEBITS](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#SOMEBITS), [WIDTH](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#WIDTH)`
Fields inherited from interface javax.swing.[WindowConstants](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html)
`[DISPOSE_ON_CLOSE](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html#DISPOSE_ON_CLOSE), [DO_NOTHING_ON_CLOSE](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html#DO_NOTHING_ON_CLOSE), [EXIT_ON_CLOSE](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html#EXIT_ON_CLOSE), [HIDE_ON_CLOSE](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html#HIDE_ON_CLOSE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MainFrame](#%3Cinit%3E(com.nomagic.magicdraw.core.Application.MainFrameController))(com.nomagic.magicdraw.core.Application.MainFrameController controller)`
Constructs MainFrame window, adds menu and popup buttons toolbar to it.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addRecentWindow](#addRecentWindow(com.nomagic.magicdraw.ui.editorwindows.EditorWindow))(com.nomagic.magicdraw.ui.editorwindows.EditorWindow window)`
Adds diagram window name to the recent window list.
`static void`
`[addStateListener](#addStateListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Adds listener for listening changes of recent windows, projects or files.
`void`
`[createCommandBar](#createCommandBar())()`
Deprecated.
use [`createMenuAndToolbars()`](#createMenuAndToolbars()).
`void`
`[createMenuAndToolbars](#createMenuAndToolbars())()`
Create (or recreate) all menu and toolbars.
`[Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)`
`[createStartupActivity](#createStartupActivity())()`
Creates startup activity for setting APPLICATION_STARTED flag.
`[Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html)`
`[getActiveFrame](#getActiveFrame())()`

`[Browser](browser/Browser.html)`
`[getBrowser](#getBrowser())()`
Returns model browser.
`[CookieSet](../cookies/CookieSet.html)`
`[getCookieSet](#getCookieSet())()`

`[Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[getCurrentCursor](#getCurrentCursor())()`

`[JMenuBar](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuBar.html)`
`[getMainMenuBar](#getMainMenuBar())()`
Returns main menu bar.
`com.nomagic.magicdraw.ui.ProgressBar`
`[getProgressBar](#getProgressBar())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getProjectTitle](#getProjectTitle(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Returns project title suitable for application title bar
`[ProjectWindowsManager](ProjectWindowsManager.html)`
`[getProjectWindowsManager](#getProjectWindowsManager())()`
Returns ProjectWindowsManager.
`[Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[getSpecificCursor](#getSpecificCursor())()`

`com.nomagic.awt.StatusLine`
`[getStatusLine](#getStatusLine())()`

`com.nomagic.magicdraw.ui.toolbar.ToolbarsManager`
`[getToolbarsManager](#getToolbarsManager())()`

`com.nomagic.magicdraw.ui.UIInstaller`
`[getUIInstaller](#getUIInstaller())()`

`[Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)>`
`[getWindowFullScreenCustomizer](#getWindowFullScreenCustomizer())()`

`com.nomagic.magicdraw.ui.WindowsManagerImpl`
`[getWindowsManager](#getWindowsManager())()`

`void`
`[init](#init())()`
Creates GUI elements in MainFrame: menu and toolbar, browser and desktop.
`static boolean`
`[isLFUpdateRequired](#isLFUpdateRequired(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lf,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) themeID,
 int jideStyle)`

`static boolean`
`[isSilentMode](#isSilentMode())()`
Returns, flag, which shows if MF is working in silent mode.
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)`
Handles Property changing event, fired by `PropertyChangeSupport`
`void`
`[setActiveFrame](#setActiveFrame(java.awt.Frame))([Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) activeFrame)`

`void`
`[setBounds](#setBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`

`boolean`
`[setLF](#setLF(java.lang.String,java.lang.String,int,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lf,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) theme,
 int jideStyle,
 boolean explicitlyUpdateUI)`

`void`
`[setRecentWindowsList](#setRecentWindowsList(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.ui.editorwindows.EditorWindow<?>> windows)`
Sets the list of the recent windows.
`static void`
`[setSilentMode](#setSilentMode(boolean))(boolean silentMode)`
Set flag, which shows if MF is working in silent mode.
`void`
`[setSpecificCursor](#setSpecificCursor(java.awt.Cursor))([Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) c)`

`void`
`[setStatusLine](#setStatusLine(com.nomagic.awt.StatusLine))(com.nomagic.awt.StatusLine statusLine)`

`void`
`[setUIInstaller](#setUIInstaller(com.nomagic.magicdraw.ui.UIInstaller))(com.nomagic.magicdraw.ui.UIInstaller installer)`

`void`
`[setVisible](#setVisible(boolean))(boolean visible)`

`void`
`[setWindowFullScreenCustomizer](#setWindowFullScreenCustomizer(java.util.function.Consumer))([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)> windowFullScreenCustomizer)`

`void`
`[sSetLF](#sSetLF(java.lang.String,java.lang.String,int,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lf,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) themeID,
 int jideStyle,
 boolean explicitlyUpdateUI)`
Set look and feel without handling errors
`void`
`[updateByEnvironmentProperties](#updateByEnvironmentProperties(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../properties/Property.html)> properties)`
Update environment by given properties.
`void`
`[updateFrameUI](#updateFrameUI(boolean))(boolean forceUpdate)`
Updates all elements ui
`void`
`[updateRecentProject](#updateRecentProject(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) prj)`
Updates project label in projects choice.
`void`
`[updateTitle](#updateTitle(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Methods inherited from class com.jidesoft.action.DefaultDockableBarDockableHolder
`createContentContainer, createDockableBarManager, dispose, getDockableBarManager, getJMenuBar, getLayoutPersistence, initFrame`
Methods inherited from class com.jidesoft.docking.DefaultDockableHolder
`createDockingManager, getDockingManager, isAutoDispose, isContentPaneCheckingEnabled, setAutoDispose, setContentPaneCheckingEnabled`
Methods inherited from class javax.swing.[JFrame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html)
`[addImpl](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#addImpl(java.awt.Component,java.lang.Object,int)), [createRootPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#createRootPane()), [frameInit](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#frameInit()), [getAccessibleContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getAccessibleContext()), [getContentPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getContentPane()), [getDefaultCloseOperation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getDefaultCloseOperation()), [getGlassPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getGlassPane()), [getGraphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getGraphics()), [getLayeredPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getLayeredPane()), [getRootPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getRootPane()), [getTransferHandler](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getTransferHandler()), [isDefaultLookAndFeelDecorated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#isDefaultLookAndFeelDecorated()), [isRootPaneCheckingEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#isRootPaneCheckingEnabled()), [paramString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#paramString()), [processWindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#processWindowEvent(java.awt.event.WindowEvent)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#remove(java.awt.Component)), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#repaint(long,int,int,int,int)), [setContentPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setContentPane(java.awt.Container)), [setDefaultCloseOperation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setDefaultCloseOperation(int)), [setDefaultLookAndFeelDecorated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setDefaultLookAndFeelDecorated(boolean)), [setGlassPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setGlassPane(java.awt.Component)), [setIconImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setIconImage(java.awt.Image)), [setJMenuBar](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setJMenuBar(javax.swing.JMenuBar)), [setLayeredPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setLayeredPane(javax.swing.JLayeredPane)), [setLayout](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setLayout(java.awt.LayoutManager)), [setRootPane](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setRootPane(javax.swing.JRootPane)), [setRootPaneCheckingEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setRootPaneCheckingEnabled(boolean)), [setTransferHandler](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setTransferHandler(javax.swing.TransferHandler)), [update](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#update(java.awt.Graphics))`
Methods inherited from class java.awt.[Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html)
`[addNotify](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#addNotify()), [getCursorType](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getCursorType()), [getExtendedState](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getExtendedState()), [getFrames](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getFrames()), [getIconImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getIconImage()), [getMaximizedBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getMaximizedBounds()), [getMenuBar](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getMenuBar()), [getState](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getState()), [getTitle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getTitle()), [isResizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#isResizable()), [isUndecorated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#isUndecorated()), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#remove(java.awt.MenuComponent)), [removeNotify](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#removeNotify()), [setBackground](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setBackground(java.awt.Color)), [setCursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setCursor(int)), [setExtendedState](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setExtendedState(int)), [setMaximizedBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setMaximizedBounds(java.awt.Rectangle)), [setMenuBar](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setMenuBar(java.awt.MenuBar)), [setOpacity](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setOpacity(float)), [setResizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setResizable(boolean)), [setShape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setShape(java.awt.Shape)), [setState](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setState(int)), [setTitle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setTitle(java.lang.String)), [setUndecorated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setUndecorated(boolean))`
Methods inherited from class java.awt.[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)
`[addPropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addPropertyChangeListener(java.beans.PropertyChangeListener)), [addPropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)), [addWindowFocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addWindowFocusListener(java.awt.event.WindowFocusListener)), [addWindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addWindowListener(java.awt.event.WindowListener)), [addWindowStateListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addWindowStateListener(java.awt.event.WindowStateListener)), [applyResourceBundle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#applyResourceBundle(java.lang.String)), [applyResourceBundle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#applyResourceBundle(java.util.ResourceBundle)), [createBufferStrategy](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#createBufferStrategy(int)), [createBufferStrategy](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#createBufferStrategy(int,java.awt.BufferCapabilities)), [getBackground](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getBackground()), [getBufferStrategy](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getBufferStrategy()), [getFocusableWindowState](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getFocusableWindowState()), [getFocusCycleRootAncestor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getFocusCycleRootAncestor()), [getFocusOwner](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getFocusOwner()), [getFocusTraversalKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getFocusTraversalKeys(int)), [getIconImages](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getIconImages()), [getInputContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getInputContext()), [getListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getListeners(java.lang.Class)), [getLocale](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getLocale()), [getModalExclusionType](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getModalExclusionType()), [getMostRecentFocusOwner](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getMostRecentFocusOwner()), [getOpacity](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getOpacity()), [getOwnedWindows](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getOwnedWindows()), [getOwner](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getOwner()), [getOwnerlessWindows](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getOwnerlessWindows()), [getShape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getShape()), [getToolkit](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getToolkit()), [getType](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getType()), [getWarningString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWarningString()), [getWindowFocusListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWindowFocusListeners()), [getWindowListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWindowListeners()), [getWindows](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWindows()), [getWindowStateListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWindowStateListeners()), [hide](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#hide()), [isActive](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isActive()), [isAlwaysOnTop](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isAlwaysOnTop()), [isAlwaysOnTopSupported](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isAlwaysOnTopSupported()), [isAutoRequestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isAutoRequestFocus()), [isFocusableWindow](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isFocusableWindow()), [isFocusCycleRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isFocusCycleRoot()), [isFocused](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isFocused()), [isLocationByPlatform](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isLocationByPlatform()), [isOpaque](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isOpaque()), [isShowing](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isShowing()), [isValidateRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isValidateRoot()), [pack](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#pack()), [paint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#paint(java.awt.Graphics)), [postEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#postEvent(java.awt.Event)), [processEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#processEvent(java.awt.AWTEvent)), [processWindowFocusEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#processWindowFocusEvent(java.awt.event.WindowEvent)), [processWindowStateEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#processWindowStateEvent(java.awt.event.WindowEvent)), [removeWindowFocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#removeWindowFocusListener(java.awt.event.WindowFocusListener)), [removeWindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#removeWindowListener(java.awt.event.WindowListener)), [removeWindowStateListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#removeWindowStateListener(java.awt.event.WindowStateListener)), [reshape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#reshape(int,int,int,int)), [setAlwaysOnTop](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setAlwaysOnTop(boolean)), [setAutoRequestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setAutoRequestFocus(boolean)), [setBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setBounds(int,int,int,int)), [setCursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setCursor(java.awt.Cursor)), [setFocusableWindowState](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setFocusableWindowState(boolean)), [setFocusCycleRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setFocusCycleRoot(boolean)), [setIconImages](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setIconImages(java.util.List)), [setLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setLocation(int,int)), [setLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setLocation(java.awt.Point)), [setLocationByPlatform](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setLocationByPlatform(boolean)), [setLocationRelativeTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setLocationRelativeTo(java.awt.Component)), [setMinimumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setMinimumSize(java.awt.Dimension)), [setModalExclusionType](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setModalExclusionType(java.awt.Dialog.ModalExclusionType)), [setSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setSize(int,int)), [setSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setSize(java.awt.Dimension)), [setType](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setType(java.awt.Window.Type)), [show](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#show()), [toBack](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#toBack()), [toFront](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#toFront())`
Methods inherited from class java.awt.[Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html)
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,int)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,java.lang.Object)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,java.lang.Object,int)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.lang.String,java.awt.Component)), [addContainerListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addContainerListener(java.awt.event.ContainerListener)), [applyComponentOrientation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#applyComponentOrientation(java.awt.ComponentOrientation)), [areFocusTraversalKeysSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#areFocusTraversalKeysSet(int)), [countComponents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#countComponents()), [deliverEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#deliverEvent(java.awt.Event)), [doLayout](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#doLayout()), [findComponentAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#findComponentAt(int,int)), [findComponentAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#findComponentAt(java.awt.Point)), [getAlignmentX](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getAlignmentX()), [getAlignmentY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getAlignmentY()), [getComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponent(int)), [getComponentAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentAt(int,int)), [getComponentAt](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentAt(java.awt.Point)), [getComponentCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentCount()), [getComponents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponents()), [getComponentZOrder](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentZOrder(java.awt.Component)), [getContainerListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getContainerListeners()), [getFocusTraversalPolicy](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getFocusTraversalPolicy()), [getInsets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getInsets()), [getLayout](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getLayout()), [getMaximumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getMaximumSize()), [getMinimumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getMinimumSize()), [getMousePosition](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getMousePosition(boolean)), [getPreferredSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getPreferredSize()), [insets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#insets()), [invalidate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#invalidate()), [isAncestorOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isAncestorOf(java.awt.Component)), [isFocusCycleRoot](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusCycleRoot(java.awt.Container)), [isFocusTraversalPolicyProvider](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusTraversalPolicyProvider()), [isFocusTraversalPolicySet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusTraversalPolicySet()), [layout](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#layout()), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#list(java.io.PrintStream,int)), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#list(java.io.PrintWriter,int)), [locate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#locate(int,int)), [minimumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#minimumSize()), [paintComponents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#paintComponents(java.awt.Graphics)), [preferredSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#preferredSize()), [print](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#print(java.awt.Graphics)), [printComponents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#printComponents(java.awt.Graphics)), [processContainerEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#processContainerEvent(java.awt.event.ContainerEvent)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#remove(int)), [removeAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#removeAll()), [removeContainerListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#removeContainerListener(java.awt.event.ContainerListener)), [setComponentZOrder](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setComponentZOrder(java.awt.Component,int)), [setFocusTraversalKeys](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalKeys(int,java.util.Set)), [setFocusTraversalPolicy](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)), [setFocusTraversalPolicyProvider](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalPolicyProvider(boolean)), [setFont](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFont(java.awt.Font)), [transferFocusDownCycle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#transferFocusDownCycle()), [validate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#validate()), [validateTree](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#validateTree())`
Methods inherited from class java.awt.[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)
`[action](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#action(java.awt.Event,java.lang.Object)), [add](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#add(java.awt.PopupMenu)), [addComponentListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addComponentListener(java.awt.event.ComponentListener)), [addFocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addFocusListener(java.awt.event.FocusListener)), [addHierarchyBoundsListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)), [addHierarchyListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addHierarchyListener(java.awt.event.HierarchyListener)), [addInputMethodListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addInputMethodListener(java.awt.event.InputMethodListener)), [addKeyListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addKeyListener(java.awt.event.KeyListener)), [addMouseListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseListener(java.awt.event.MouseListener)), [addMouseMotionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseMotionListener(java.awt.event.MouseMotionListener)), [addMouseWheelListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseWheelListener(java.awt.event.MouseWheelListener)), [bounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#bounds()), [checkImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#checkImage(java.awt.Image,int,int,java.awt.image.ImageObserver)), [checkImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#checkImage(java.awt.Image,java.awt.image.ImageObserver)), [coalesceEvents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#coalesceEvents(java.awt.AWTEvent,java.awt.AWTEvent)), [contains](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#contains(int,int)), [contains](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#contains(java.awt.Point)), [createImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createImage(int,int)), [createImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createImage(java.awt.image.ImageProducer)), [createVolatileImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createVolatileImage(int,int)), [createVolatileImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createVolatileImage(int,int,java.awt.ImageCapabilities)), [disable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#disable()), [disableEvents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#disableEvents(long)), [dispatchEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#dispatchEvent(java.awt.AWTEvent)), [enable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enable()), [enable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enable(boolean)), [enableEvents](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enableEvents(long)), [enableInputMethods](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enableInputMethods(boolean)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,boolean,boolean)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,byte,byte)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,char,char)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,double,double)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,float,float)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,int,int)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,long,long)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,short,short)), [firePropertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)), [getBaseline](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBaseline(int,int)), [getBaselineResizeBehavior](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBaselineResizeBehavior()), [getBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBounds()), [getBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBounds(java.awt.Rectangle)), [getColorModel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getColorModel()), [getComponentListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getComponentListeners()), [getComponentOrientation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getComponentOrientation()), [getCursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getCursor()), [getDropTarget](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getDropTarget()), [getFocusListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusListeners()), [getFocusTraversalKeysEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusTraversalKeysEnabled()), [getFont](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFont()), [getFontMetrics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFontMetrics(java.awt.Font)), [getForeground](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getForeground()), [getGraphicsConfiguration](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getGraphicsConfiguration()), [getHeight](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHeight()), [getHierarchyBoundsListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHierarchyBoundsListeners()), [getHierarchyListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHierarchyListeners()), [getIgnoreRepaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getIgnoreRepaint()), [getInputMethodListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputMethodListeners()), [getInputMethodRequests](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputMethodRequests()), [getKeyListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getKeyListeners()), [getLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocation()), [getLocation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocation(java.awt.Point)), [getLocationOnScreen](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocationOnScreen()), [getMouseListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseListeners()), [getMouseMotionListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseMotionListeners()), [getMousePosition](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMousePosition()), [getMouseWheelListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseWheelListeners()), [getName](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getName()), [getParent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getParent()), [getPropertyChangeListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getPropertyChangeListeners()), [getPropertyChangeListeners](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getPropertyChangeListeners(java.lang.String)), [getSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getSize()), [getSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getSize(java.awt.Dimension)), [getTreeLock](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getTreeLock()), [getWidth](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getWidth()), [getX](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getX()), [getY](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getY()), [gotFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#gotFocus(java.awt.Event,java.lang.Object)), [handleEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#handleEvent(java.awt.Event)), [hasFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#hasFocus()), [imageUpdate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#imageUpdate(java.awt.Image,int,int,int,int,int)), [inside](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#inside(int,int)), [isBackgroundSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isBackgroundSet()), [isCursorSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isCursorSet()), [isDisplayable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isDisplayable()), [isDoubleBuffered](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isDoubleBuffered()), [isEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isEnabled()), [isFocusable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusable()), [isFocusOwner](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusOwner()), [isFocusTraversable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusTraversable()), [isFontSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFontSet()), [isForegroundSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isForegroundSet()), [isLightweight](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isLightweight()), [isMaximumSizeSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isMaximumSizeSet()), [isMinimumSizeSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isMinimumSizeSet()), [isPreferredSizeSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isPreferredSizeSet()), [isValid](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isValid()), [isVisible](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isVisible()), [keyDown](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#keyDown(java.awt.Event,int)), [keyUp](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#keyUp(java.awt.Event,int)), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list()), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list(java.io.PrintStream)), [list](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list(java.io.PrintWriter)), [location](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#location()), [lostFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#lostFocus(java.awt.Event,java.lang.Object)), [mouseDown](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseDown(java.awt.Event,int,int)), [mouseDrag](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseDrag(java.awt.Event,int,int)), [mouseEnter](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseEnter(java.awt.Event,int,int)), [mouseExit](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseExit(java.awt.Event,int,int)), [mouseMove](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseMove(java.awt.Event,int,int)), [mouseUp](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseUp(java.awt.Event,int,int)), [move](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#move(int,int)), [nextFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#nextFocus()), [paintAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#paintAll(java.awt.Graphics)), [prepareImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#prepareImage(java.awt.Image,int,int,java.awt.image.ImageObserver)), [prepareImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#prepareImage(java.awt.Image,java.awt.image.ImageObserver)), [printAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#printAll(java.awt.Graphics)), [processComponentEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processComponentEvent(java.awt.event.ComponentEvent)), [processFocusEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processFocusEvent(java.awt.event.FocusEvent)), [processHierarchyBoundsEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processHierarchyBoundsEvent(java.awt.event.HierarchyEvent)), [processHierarchyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processHierarchyEvent(java.awt.event.HierarchyEvent)), [processInputMethodEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processInputMethodEvent(java.awt.event.InputMethodEvent)), [processKeyEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processKeyEvent(java.awt.event.KeyEvent)), [processMouseEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processMouseEvent(java.awt.event.MouseEvent)), [processMouseMotionEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processMouseMotionEvent(java.awt.event.MouseEvent)), [processMouseWheelEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processMouseWheelEvent(java.awt.event.MouseWheelEvent)), [removeComponentListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeComponentListener(java.awt.event.ComponentListener)), [removeFocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeFocusListener(java.awt.event.FocusListener)), [removeHierarchyBoundsListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)), [removeHierarchyListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeHierarchyListener(java.awt.event.HierarchyListener)), [removeInputMethodListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeInputMethodListener(java.awt.event.InputMethodListener)), [removeKeyListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeKeyListener(java.awt.event.KeyListener)), [removeMouseListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseListener(java.awt.event.MouseListener)), [removeMouseMotionListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseMotionListener(java.awt.event.MouseMotionListener)), [removeMouseWheelListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseWheelListener(java.awt.event.MouseWheelListener)), [removePropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removePropertyChangeListener(java.beans.PropertyChangeListener)), [removePropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint()), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint(int,int,int,int)), [repaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint(long)), [requestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus()), [requestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(boolean)), [requestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(boolean,java.awt.event.FocusEvent.Cause)), [requestFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(java.awt.event.FocusEvent.Cause)), [requestFocusInWindow](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocusInWindow()), [requestFocusInWindow](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocusInWindow(boolean)), [requestFocusInWindow](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocusInWindow(java.awt.event.FocusEvent.Cause)), [resize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#resize(int,int)), [resize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#resize(java.awt.Dimension)), [revalidate](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#revalidate()), [setComponentOrientation](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setComponentOrientation(java.awt.ComponentOrientation)), [setDropTarget](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setDropTarget(java.awt.dnd.DropTarget)), [setEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setEnabled(boolean)), [setFocusable](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setFocusable(boolean)), [setFocusTraversalKeysEnabled](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setFocusTraversalKeysEnabled(boolean)), [setForeground](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setForeground(java.awt.Color)), [setIgnoreRepaint](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setIgnoreRepaint(boolean)), [setLocale](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setLocale(java.util.Locale)), [setMaximumSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setMaximumSize(java.awt.Dimension)), [setMixingCutoutShape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setMixingCutoutShape(java.awt.Shape)), [setName](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setName(java.lang.String)), [setPreferredSize](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setPreferredSize(java.awt.Dimension)), [show](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#show(boolean)), [size](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#size()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#toString()), [transferFocus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocus()), [transferFocusBackward](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocusBackward()), [transferFocusUpCycle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocusUpCycle())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.jidesoft.docking.DockableHolder
`getDockingManager`
Methods inherited from interface java.awt.[MenuContainer](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html)
`[getFont](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html#getFont()), [postEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html#postEvent(java.awt.Event))`

============ FIELD DETAIL =========== 
Field Details
MAIN_TOOLBAR_EXPERT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MAIN_TOOLBAR_EXPERT
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.MainFrame.MAIN_TOOLBAR_EXPERT)
MAIN_TOOLBAR_STANDARD
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MAIN_TOOLBAR_STANDARD
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.MainFrame.MAIN_TOOLBAR_STANDARD)
RECENT_PROJECT_NAME_CHANGE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RECENT_PROJECT_NAME_CHANGE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.MainFrame.RECENT_PROJECT_NAME_CHANGE)
RECENT_WINDOWS
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) RECENT_WINDOWS
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.MainFrame.RECENT_WINDOWS)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MainFrame
public MainFrame(com.nomagic.magicdraw.core.Application.MainFrameController controller)
Constructs MainFrame window, adds menu and popup buttons toolbar to it.
 Also this method sets event listeners for each menu item and toolbar button.
Parameters:
`controller` - controller
 ============ METHOD DETAIL ========== 
Method Details
setBounds
public void setBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
Overrides:
`[setBounds](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setBounds(java.awt.Rectangle))` in class `[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)`
getMainMenuBar
@OpenApipublic [JMenuBar](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuBar.html) getMainMenuBar()
Returns main menu bar.
Returns:
main menu bar.
setActiveFrame
public void setActiveFrame(@CheckForNull
 [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) activeFrame)
getActiveFrame
public [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) getActiveFrame()
init
public void init()
Creates GUI elements in MainFrame: menu and toolbar, browser and desktop.
 And adds action listeners to menu items and toolbar buttons
createCommandBar
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public void createCommandBar()
Deprecated.
use [`createMenuAndToolbars()`](#createMenuAndToolbars()). Some people use this api, because we had no way
createMenuAndToolbars
@OpenApipublic void createMenuAndToolbars()
Create (or recreate) all menu and toolbars.
 It will invoke all registered [`AMConfigurator`](../../actions/AMConfigurator.html) in [`ActionsConfiguratorsManager`](../actions/ActionsConfiguratorsManager.html)
getBrowser
@CheckForNull
@OpenApipublic [Browser](browser/Browser.html) getBrowser()
Returns model browser.
Returns:
model browser.
updateByEnvironmentProperties
public void updateByEnvironmentProperties([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../properties/Property.html)> properties)
Update environment by given properties.
Specified by:
`[updateByEnvironmentProperties](../core/options/EnvironmentOptions.EnvironmentChangeListener.html#updateByEnvironmentProperties(java.util.List))` in interface `[EnvironmentOptions.EnvironmentChangeListener](../core/options/EnvironmentOptions.EnvironmentChangeListener.html)`
Parameters:
`properties` - properties
isSilentMode
public static boolean isSilentMode()
Returns, flag, which shows if MF is working in silent mode.
Returns:
flag, which shows if MF is working in silent mode.
setSilentMode
public static void setSilentMode(boolean silentMode)
Set flag, which shows if MF is working in silent mode.
 
 Used by Forte Integration.
Parameters:
`silentMode` - flag, which shows if MF is working in silent mode.
getSpecificCursor
public [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) getSpecificCursor()
Specified by:
`getSpecificCursor` in interface `com.nomagic.ui.CursorOwner`
getCurrentCursor
public [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) getCurrentCursor()
Specified by:
`getCurrentCursor` in interface `com.nomagic.ui.CursorOwner`
setSpecificCursor
public void setSpecificCursor([Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) c)
Specified by:
`setSpecificCursor` in interface `com.nomagic.ui.CursorOwner`
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) evt)
Handles Property changing event, fired by `PropertyChangeSupport`
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
Parameters:
`evt` - PropertyChangeEvent, which has to be handled.
See Also:
[`PropertyChangeListener`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)
[`PropertyChangeEvent`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)
[`PropertyChangeListener`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)
[`PropertyChangeSupport`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html)
setLF
public boolean setLF([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lf,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) theme,
 int jideStyle,
 boolean explicitlyUpdateUI)
sSetLF
public void sSetLF([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lf,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) themeID,
 int jideStyle,
 boolean explicitlyUpdateUI)
 throws [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html)
Set look and feel without handling errors
Parameters:
`lf` - lf name
`themeID` - theme id
`jideStyle` - jide style
`explicitlyUpdateUI` - update ui flag
Throws:
`[Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html)` - exception
isLFUpdateRequired
public static boolean isLFUpdateRequired([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lf,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) themeID,
 int jideStyle)
updateFrameUI
public void updateFrameUI(boolean forceUpdate)
Updates all elements ui
Parameters:
`forceUpdate` - set true to force update even if L&F did not change
addRecentWindow
public void addRecentWindow(com.nomagic.magicdraw.ui.editorwindows.EditorWindow window)
Adds diagram window name to the recent window list.
Parameters:
`window` - the window to add.
setRecentWindowsList
public void setRecentWindowsList([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.ui.editorwindows.EditorWindow<?>> windows)
Sets the list of the recent windows.
Parameters:
`windows` - the new list of the recent windows.
updateRecentProject
public void updateRecentProject([Project](../core/Project.html) prj)
Updates project label in projects choice.
Parameters:
`prj` - - project to update
getProjectWindowsManager
@OpenApipublic [ProjectWindowsManager](ProjectWindowsManager.html) getProjectWindowsManager()
Returns ProjectWindowsManager.
Returns:
project windows manager.
getWindowsManager
public com.nomagic.magicdraw.ui.WindowsManagerImpl getWindowsManager()
addStateListener
public static void addStateListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Adds listener for listening changes of recent windows, projects or files.
Parameters:
`listener` - listener for listening changes of recent windows, projects or files.
updateTitle
public void updateTitle(@CheckForNull
 [Project](../core/Project.html) project)
getProjectTitle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getProjectTitle([Project](../core/Project.html) project)
Returns project title suitable for application title bar
Parameters:
`project` - project instance of [`Project`](../core/Project.html)
Returns:
project title suitable for application title bar
setStatusLine
public void setStatusLine(com.nomagic.awt.StatusLine statusLine)
getStatusLine
public com.nomagic.awt.StatusLine getStatusLine()
getCookieSet
public [CookieSet](../cookies/CookieSet.html) getCookieSet()
getProgressBar
public com.nomagic.magicdraw.ui.ProgressBar getProgressBar()
Returns:
Returns the progressBar.
getUIInstaller
public com.nomagic.magicdraw.ui.UIInstaller getUIInstaller()
Returns:
Returns the uIInstaller.
setUIInstaller
public void setUIInstaller(com.nomagic.magicdraw.ui.UIInstaller installer)
Parameters:
`installer` - The uIInstaller to set.
setVisible
public void setVisible(boolean visible)
Overrides:
`[setVisible](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setVisible(boolean))` in class `[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)`
getToolbarsManager
public com.nomagic.magicdraw.ui.toolbar.ToolbarsManager getToolbarsManager()
createStartupActivity
public [Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) createStartupActivity()
Creates startup activity for setting APPLICATION_STARTED flag.
Returns:
runnable
getWindowFullScreenCustomizer
public [Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)> getWindowFullScreenCustomizer()
setWindowFullScreenCustomizer
public void setWindowFullScreenCustomizer([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html)<[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)> windowFullScreenCustomizer)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class MainFrame">Class MainFrame</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">java.awt.Component</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">java.awt.Container</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">java.awt.Window</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">java.awt.Frame</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html" title="class or interface in javax.swing">javax.swing.JFrame</a>
<div class="inheritance">com.jidesoft.docking.DefaultDockableHolder
<div class="inheritance">com.jidesoft.action.DefaultDockableBarDockableHolder
<div class="inheritance">com.nomagic.magicdraw.ui.MainFrame</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.jidesoft.action.DockableBarDockableHolder</code>, <code>com.jidesoft.action.DockableBarHolder</code>, <code>com.jidesoft.docking.DockableHolder</code>, <code><a href="../actions/ActionsGroups.html" title="interface in com.nomagic.magicdraw.actions">ActionsGroups</a></code>, <code><a href="../core/options/EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a></code>, <code>com.nomagic.ui.CursorOwner</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html" title="class or interface in java.awt.image">ImageObserver</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html" title="class or interface in java.awt">MenuContainer</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/accessibility/Accessible.html" title="class or interface in javax.accessibility">Accessible</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/RootPaneContainer.html" title="class or interface in javax.swing">RootPaneContainer</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html" title="class or interface in javax.swing">WindowConstants</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">MainFrame</span>
<span class="extends-implements">extends com.jidesoft.action.DefaultDockableBarDockableHolder
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a>, com.nomagic.ui.CursorOwner, <a href="../actions/ActionsGroups.html" title="interface in com.nomagic.magicdraw.actions">ActionsGroups</a>, <a href="../core/options/EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a></span></div>
<div class="block">The <code>MainFrame</code> class represents main window of the MagicDraw application.
 Also it has a set of inner classes- event listeners to handle all menu and toolbar events.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../serialized-form.html#com.nomagic.magicdraw.ui.MainFrame">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MAIN_TOOLBAR_EXPERT">MAIN_TOOLBAR_EXPERT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MAIN_TOOLBAR_STANDARD">MAIN_TOOLBAR_STANDARD</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RECENT_PROJECT_NAME_CHANGE">RECENT_PROJECT_NAME_CHANGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RECENT_WINDOWS">RECENT_WINDOWS</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.jidesoft.docking.DefaultDockableHolder">Fields inherited from class com.jidesoft.docking.DefaultDockableHolder</h3>
<code>_autoDispose, _contentContainer, _dockingManager</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.JFrame">Fields inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html" title="class or interface in javax.swing">JFrame</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#accessibleContext" title="class or interface in javax.swing">accessibleContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#rootPane" title="class or interface in javax.swing">rootPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#rootPaneCheckingEnabled" title="class or interface in javax.swing">rootPaneCheckingEnabled</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.awt.Frame">Fields inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#CROSSHAIR_CURSOR" title="class or interface in java.awt">CROSSHAIR_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#DEFAULT_CURSOR" title="class or interface in java.awt">DEFAULT_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#E_RESIZE_CURSOR" title="class or interface in java.awt">E_RESIZE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#HAND_CURSOR" title="class or interface in java.awt">HAND_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#ICONIFIED" title="class or interface in java.awt">ICONIFIED</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#MAXIMIZED_BOTH" title="class or interface in java.awt">MAXIMIZED_BOTH</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#MAXIMIZED_HORIZ" title="class or interface in java.awt">MAXIMIZED_HORIZ</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#MAXIMIZED_VERT" title="class or interface in java.awt">MAXIMIZED_VERT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#MOVE_CURSOR" title="class or interface in java.awt">MOVE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#N_RESIZE_CURSOR" title="class or interface in java.awt">N_RESIZE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#NE_RESIZE_CURSOR" title="class or interface in java.awt">NE_RESIZE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#NORMAL" title="class or interface in java.awt">NORMAL</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#NW_RESIZE_CURSOR" title="class or interface in java.awt">NW_RESIZE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#S_RESIZE_CURSOR" title="class or interface in java.awt">S_RESIZE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#SE_RESIZE_CURSOR" title="class or interface in java.awt">SE_RESIZE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#SW_RESIZE_CURSOR" title="class or interface in java.awt">SW_RESIZE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#TEXT_CURSOR" title="class or interface in java.awt">TEXT_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#W_RESIZE_CURSOR" title="class or interface in java.awt">W_RESIZE_CURSOR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#WAIT_CURSOR" title="class or interface in java.awt">WAIT_CURSOR</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.awt.Component">Fields inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#BOTTOM_ALIGNMENT" title="class or interface in java.awt">BOTTOM_ALIGNMENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#CENTER_ALIGNMENT" title="class or interface in java.awt">CENTER_ALIGNMENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#LEFT_ALIGNMENT" title="class or interface in java.awt">LEFT_ALIGNMENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#RIGHT_ALIGNMENT" title="class or interface in java.awt">RIGHT_ALIGNMENT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#TOP_ALIGNMENT" title="class or interface in java.awt">TOP_ALIGNMENT</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.actions.ActionsGroups">Fields inherited from interface com.nomagic.magicdraw.actions.<a href="../actions/ActionsGroups.html" title="interface in com.nomagic.magicdraw.actions">ActionsGroups</a></h3>
<code><a href="../actions/ActionsGroups.html#ANY_DIAGRAM_EDIT_RELATED">ANY_DIAGRAM_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_DIAGRAM_OPENED_RELATED">ANY_DIAGRAM_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_PROJECT_EDIT_RELATED">ANY_PROJECT_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_PROJECT_OPENED_RELATED">ANY_PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_PROJECT_SAVING_RELATED">ANY_PROJECT_SAVING_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_REMOTE_ANY_PROJECT_EDIT_RELATED">ANY_REMOTE_ANY_PROJECT_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_REMOTE_PROJECT_EDIT_RELATED">ANY_REMOTE_PROJECT_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_REMOTE_PROJECT_OPENED_RELATED">ANY_REMOTE_PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_REMOTE_UML_PROJECT_EDIT_RELATED">ANY_REMOTE_UML_PROJECT_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#ANY_SERVER_LOGIN_RELATED">ANY_SERVER_LOGIN_RELATED</a>, <a href="../actions/ActionsGroups.html#APPLICATION_RELATED">APPLICATION_RELATED</a>, <a href="../actions/ActionsGroups.html#DIAGRAM_EDIT_RELATED">DIAGRAM_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#DIAGRAM_OPENED_RELATED">DIAGRAM_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#DIAGRAM_RELATED_ELEMENTS">DIAGRAM_RELATED_ELEMENTS</a>, <a href="../actions/ActionsGroups.html#DIAGRAM_ZOOMIN_RELATED">DIAGRAM_ZOOMIN_RELATED</a>, <a href="../actions/ActionsGroups.html#DIAGRAM_ZOOMOUT_RELATED">DIAGRAM_ZOOMOUT_RELATED</a>, <a href="../actions/ActionsGroups.html#DIAGRAM_ZOOMTO11_RELATED">DIAGRAM_ZOOMTO11_RELATED</a>, <a href="../actions/ActionsGroups.html#EDITOR_OPENED_RELATED">EDITOR_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#ESI_ANY_PROJECT_OPENED_RELATED">ESI_ANY_PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#ESI_PROJECT_OPENED_RELATED">ESI_PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#ESI_SERVER_LOGIN_RELATED">ESI_SERVER_LOGIN_RELATED</a>, <a href="../actions/ActionsGroups.html#ESI_UML_PROJECT_OPENED_RELATED">ESI_UML_PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#LAYOUT_SHAPES_RELATED">LAYOUT_SHAPES_RELATED</a>, <a href="../actions/ActionsGroups.html#LOCAL_PROJECT_OPENED_RELATED">LOCAL_PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#LOCAL_UML_PROJECT_OPENED_RELATED">LOCAL_UML_PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#NOT_EMPTY_ANY_DIAGRAM_RELATED">NOT_EMPTY_ANY_DIAGRAM_RELATED</a>, <a href="../actions/ActionsGroups.html#NOT_EMPTY_CLASS_DIAGRAM_RELATED">NOT_EMPTY_CLASS_DIAGRAM_RELATED</a>, <a href="../actions/ActionsGroups.html#NOT_EMPTY_DIAGRAM_RELATED">NOT_EMPTY_DIAGRAM_RELATED</a>, <a href="../actions/ActionsGroups.html#OPENED_MODULE_AS_PROJECT">OPENED_MODULE_AS_PROJECT</a>, <a href="../actions/ActionsGroups.html#PATH_STYLE_EDIT_RELATED">PATH_STYLE_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED">PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#PRESENTATION_ELEMENT_ALIGN_RELATED">PRESENTATION_ELEMENT_ALIGN_RELATED</a>, <a href="../actions/ActionsGroups.html#PRESENTATION_ELEMENT_SELECTION_RELATED">PRESENTATION_ELEMENT_SELECTION_RELATED</a>, <a href="../actions/ActionsGroups.html#PROJECT_EDIT_RELATED">PROJECT_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#PROJECT_OPENED_RELATED">PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#PROJECT_SAVING_RELATED">PROJECT_SAVING_RELATED</a>, <a href="../actions/ActionsGroups.html#REDO_COMMAND_RELATED">REDO_COMMAND_RELATED</a>, <a href="../actions/ActionsGroups.html#STANDARD_SYSTEM_PROFILE_OPENED_RELATED">STANDARD_SYSTEM_PROFILE_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#UML_PROJECT_EDIT_RELATED">UML_PROJECT_EDIT_RELATED</a>, <a href="../actions/ActionsGroups.html#UML_PROJECT_OPENED_RELATED">UML_PROJECT_OPENED_RELATED</a>, <a href="../actions/ActionsGroups.html#UNDO_COMMAND_RELATED">UNDO_COMMAND_RELATED</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.awt.image.ImageObserver">Fields inherited from interface java.awt.image.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html" title="class or interface in java.awt.image">ImageObserver</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ABORT" title="class or interface in java.awt.image">ABORT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ALLBITS" title="class or interface in java.awt.image">ALLBITS</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#ERROR" title="class or interface in java.awt.image">ERROR</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#FRAMEBITS" title="class or interface in java.awt.image">FRAMEBITS</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#HEIGHT" title="class or interface in java.awt.image">HEIGHT</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#PROPERTIES" title="class or interface in java.awt.image">PROPERTIES</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#SOMEBITS" title="class or interface in java.awt.image">SOMEBITS</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html#WIDTH" title="class or interface in java.awt.image">WIDTH</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.WindowConstants">Fields inherited from interface javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html" title="class or interface in javax.swing">WindowConstants</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html#DISPOSE_ON_CLOSE" title="class or interface in javax.swing">DISPOSE_ON_CLOSE</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html#DO_NOTHING_ON_CLOSE" title="class or interface in javax.swing">DO_NOTHING_ON_CLOSE</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html#EXIT_ON_CLOSE" title="class or interface in javax.swing">EXIT_ON_CLOSE</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/WindowConstants.html#HIDE_ON_CLOSE" title="class or interface in javax.swing">HIDE_ON_CLOSE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Application.MainFrameController)">MainFrame</a><wbr/>(com.nomagic.magicdraw.core.Application.MainFrameController controller)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs MainFrame window, adds menu and popup buttons toolbar to it.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRecentWindow(com.nomagic.magicdraw.ui.editorwindows.EditorWindow)">addRecentWindow</a><wbr/>(com.nomagic.magicdraw.ui.editorwindows.EditorWindow window)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds diagram window name to the recent window list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addStateListener(java.beans.PropertyChangeListener)">addStateListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds listener for listening changes of recent windows, projects or files.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createCommandBar()">createCommandBar</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createMenuAndToolbars()"><code>createMenuAndToolbars()</code></a>.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMenuAndToolbars()">createMenuAndToolbars</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create (or recreate) all menu and toolbars.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStartupActivity()">createStartupActivity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates startup activity for setting APPLICATION_STARTED flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveFrame()">getActiveFrame</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBrowser()">getBrowser</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model browser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../cookies/CookieSet.html" title="class in com.nomagic.magicdraw.cookies">CookieSet</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCookieSet()">getCookieSet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentCursor()">getCurrentCursor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuBar.html" title="class or interface in javax.swing">JMenuBar</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainMenuBar()">getMainMenuBar</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns main menu bar.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.ProgressBar</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProgressBar()">getProgressBar</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectTitle(com.nomagic.magicdraw.core.Project)">getProjectTitle</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns project title suitable for application title bar</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ProjectWindowsManager.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProjectWindowsManager()">getProjectWindowsManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns ProjectWindowsManager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSpecificCursor()">getSpecificCursor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.awt.StatusLine</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStatusLine()">getStatusLine</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.toolbar.ToolbarsManager</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getToolbarsManager()">getToolbarsManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.UIInstaller</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUIInstaller()">getUIInstaller</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWindowFullScreenCustomizer()">getWindowFullScreenCustomizer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.WindowsManagerImpl</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWindowsManager()">getWindowsManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init()">init</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates GUI elements in MainFrame: menu and toolbar, browser and desktop.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isLFUpdateRequired(java.lang.String,java.lang.String,int)">isLFUpdateRequired</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lf,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> themeID,
 int jideStyle)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSilentMode()">isSilentMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns, flag, which shows if MF is working in silent mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handles Property changing event, fired by <code>PropertyChangeSupport</code></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setActiveFrame(java.awt.Frame)">setActiveFrame</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> activeFrame)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBounds(java.awt.Rectangle)">setBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLF(java.lang.String,java.lang.String,int,boolean)">setLF</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lf,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> theme,
 int jideStyle,
 boolean explicitlyUpdateUI)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRecentWindowsList(java.util.Collection)">setRecentWindowsList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;?&gt;&gt; windows)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the list of the recent windows.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSilentMode(boolean)">setSilentMode</a><wbr/>(boolean silentMode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set flag, which shows if MF is working in silent mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSpecificCursor(java.awt.Cursor)">setSpecificCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStatusLine(com.nomagic.awt.StatusLine)">setStatusLine</a><wbr/>(com.nomagic.awt.StatusLine statusLine)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUIInstaller(com.nomagic.magicdraw.ui.UIInstaller)">setUIInstaller</a><wbr/>(com.nomagic.magicdraw.ui.UIInstaller installer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisible(boolean)">setVisible</a><wbr/>(boolean visible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWindowFullScreenCustomizer(java.util.function.Consumer)">setWindowFullScreenCustomizer</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a>&gt; windowFullScreenCustomizer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sSetLF(java.lang.String,java.lang.String,int,boolean)">sSetLF</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lf,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> themeID,
 int jideStyle,
 boolean explicitlyUpdateUI)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set look and feel without handling errors</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateByEnvironmentProperties(java.util.List)">updateByEnvironmentProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update environment by given properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateFrameUI(boolean)">updateFrameUI</a><wbr/>(boolean forceUpdate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates all elements ui</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateRecentProject(com.nomagic.magicdraw.core.Project)">updateRecentProject</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates project label in projects choice.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateTitle(com.nomagic.magicdraw.core.Project)">updateTitle</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.jidesoft.action.DefaultDockableBarDockableHolder">Methods inherited from class com.jidesoft.action.DefaultDockableBarDockableHolder</h3>
<code>createContentContainer, createDockableBarManager, dispose, getDockableBarManager, getJMenuBar, getLayoutPersistence, initFrame</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.jidesoft.docking.DefaultDockableHolder">Methods inherited from class com.jidesoft.docking.DefaultDockableHolder</h3>
<code>createDockingManager, getDockingManager, isAutoDispose, isContentPaneCheckingEnabled, setAutoDispose, setContentPaneCheckingEnabled</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.JFrame">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html" title="class or interface in javax.swing">JFrame</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#addImpl(java.awt.Component,java.lang.Object,int)" title="class or interface in javax.swing">addImpl</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#createRootPane()" title="class or interface in javax.swing">createRootPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#frameInit()" title="class or interface in javax.swing">frameInit</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getAccessibleContext()" title="class or interface in javax.swing">getAccessibleContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getContentPane()" title="class or interface in javax.swing">getContentPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getDefaultCloseOperation()" title="class or interface in javax.swing">getDefaultCloseOperation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getGlassPane()" title="class or interface in javax.swing">getGlassPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getGraphics()" title="class or interface in javax.swing">getGraphics</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getLayeredPane()" title="class or interface in javax.swing">getLayeredPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getRootPane()" title="class or interface in javax.swing">getRootPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#getTransferHandler()" title="class or interface in javax.swing">getTransferHandler</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#isDefaultLookAndFeelDecorated()" title="class or interface in javax.swing">isDefaultLookAndFeelDecorated</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#isRootPaneCheckingEnabled()" title="class or interface in javax.swing">isRootPaneCheckingEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#paramString()" title="class or interface in javax.swing">paramString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#processWindowEvent(java.awt.event.WindowEvent)" title="class or interface in javax.swing">processWindowEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#remove(java.awt.Component)" title="class or interface in javax.swing">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#repaint(long,int,int,int,int)" title="class or interface in javax.swing">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setContentPane(java.awt.Container)" title="class or interface in javax.swing">setContentPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setDefaultCloseOperation(int)" title="class or interface in javax.swing">setDefaultCloseOperation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setDefaultLookAndFeelDecorated(boolean)" title="class or interface in javax.swing">setDefaultLookAndFeelDecorated</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setGlassPane(java.awt.Component)" title="class or interface in javax.swing">setGlassPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setIconImage(java.awt.Image)" title="class or interface in javax.swing">setIconImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setJMenuBar(javax.swing.JMenuBar)" title="class or interface in javax.swing">setJMenuBar</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setLayeredPane(javax.swing.JLayeredPane)" title="class or interface in javax.swing">setLayeredPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setLayout(java.awt.LayoutManager)" title="class or interface in javax.swing">setLayout</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setRootPane(javax.swing.JRootPane)" title="class or interface in javax.swing">setRootPane</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setRootPaneCheckingEnabled(boolean)" title="class or interface in javax.swing">setRootPaneCheckingEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#setTransferHandler(javax.swing.TransferHandler)" title="class or interface in javax.swing">setTransferHandler</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JFrame.html#update(java.awt.Graphics)" title="class or interface in javax.swing">update</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.awt.Frame">Methods inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#addNotify()" title="class or interface in java.awt">addNotify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getCursorType()" title="class or interface in java.awt">getCursorType</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getExtendedState()" title="class or interface in java.awt">getExtendedState</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getFrames()" title="class or interface in java.awt">getFrames</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getIconImage()" title="class or interface in java.awt">getIconImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getMaximizedBounds()" title="class or interface in java.awt">getMaximizedBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getMenuBar()" title="class or interface in java.awt">getMenuBar</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getState()" title="class or interface in java.awt">getState</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#getTitle()" title="class or interface in java.awt">getTitle</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#isResizable()" title="class or interface in java.awt">isResizable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#isUndecorated()" title="class or interface in java.awt">isUndecorated</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#remove(java.awt.MenuComponent)" title="class or interface in java.awt">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#removeNotify()" title="class or interface in java.awt">removeNotify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setBackground(java.awt.Color)" title="class or interface in java.awt">setBackground</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setCursor(int)" title="class or interface in java.awt">setCursor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setExtendedState(int)" title="class or interface in java.awt">setExtendedState</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setMaximizedBounds(java.awt.Rectangle)" title="class or interface in java.awt">setMaximizedBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setMenuBar(java.awt.MenuBar)" title="class or interface in java.awt">setMenuBar</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setOpacity(float)" title="class or interface in java.awt">setOpacity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setResizable(boolean)" title="class or interface in java.awt">setResizable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setShape(java.awt.Shape)" title="class or interface in java.awt">setShape</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setState(int)" title="class or interface in java.awt">setState</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setTitle(java.lang.String)" title="class or interface in java.awt">setTitle</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html#setUndecorated(boolean)" title="class or interface in java.awt">setUndecorated</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.awt.Window">Methods inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addPropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in java.awt">addPropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)" title="class or interface in java.awt">addPropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addWindowFocusListener(java.awt.event.WindowFocusListener)" title="class or interface in java.awt">addWindowFocusListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addWindowListener(java.awt.event.WindowListener)" title="class or interface in java.awt">addWindowListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#addWindowStateListener(java.awt.event.WindowStateListener)" title="class or interface in java.awt">addWindowStateListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#applyResourceBundle(java.lang.String)" title="class or interface in java.awt">applyResourceBundle</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#applyResourceBundle(java.util.ResourceBundle)" title="class or interface in java.awt">applyResourceBundle</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#createBufferStrategy(int)" title="class or interface in java.awt">createBufferStrategy</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#createBufferStrategy(int,java.awt.BufferCapabilities)" title="class or interface in java.awt">createBufferStrategy</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getBackground()" title="class or interface in java.awt">getBackground</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getBufferStrategy()" title="class or interface in java.awt">getBufferStrategy</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getFocusableWindowState()" title="class or interface in java.awt">getFocusableWindowState</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getFocusCycleRootAncestor()" title="class or interface in java.awt">getFocusCycleRootAncestor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getFocusOwner()" title="class or interface in java.awt">getFocusOwner</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getFocusTraversalKeys(int)" title="class or interface in java.awt">getFocusTraversalKeys</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getIconImages()" title="class or interface in java.awt">getIconImages</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getInputContext()" title="class or interface in java.awt">getInputContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getListeners(java.lang.Class)" title="class or interface in java.awt">getListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getLocale()" title="class or interface in java.awt">getLocale</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getModalExclusionType()" title="class or interface in java.awt">getModalExclusionType</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getMostRecentFocusOwner()" title="class or interface in java.awt">getMostRecentFocusOwner</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getOpacity()" title="class or interface in java.awt">getOpacity</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getOwnedWindows()" title="class or interface in java.awt">getOwnedWindows</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getOwner()" title="class or interface in java.awt">getOwner</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getOwnerlessWindows()" title="class or interface in java.awt">getOwnerlessWindows</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getShape()" title="class or interface in java.awt">getShape</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getToolkit()" title="class or interface in java.awt">getToolkit</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getType()" title="class or interface in java.awt">getType</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWarningString()" title="class or interface in java.awt">getWarningString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWindowFocusListeners()" title="class or interface in java.awt">getWindowFocusListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWindowListeners()" title="class or interface in java.awt">getWindowListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWindows()" title="class or interface in java.awt">getWindows</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#getWindowStateListeners()" title="class or interface in java.awt">getWindowStateListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#hide()" title="class or interface in java.awt">hide</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isActive()" title="class or interface in java.awt">isActive</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isAlwaysOnTop()" title="class or interface in java.awt">isAlwaysOnTop</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isAlwaysOnTopSupported()" title="class or interface in java.awt">isAlwaysOnTopSupported</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isAutoRequestFocus()" title="class or interface in java.awt">isAutoRequestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isFocusableWindow()" title="class or interface in java.awt">isFocusableWindow</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isFocusCycleRoot()" title="class or interface in java.awt">isFocusCycleRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isFocused()" title="class or interface in java.awt">isFocused</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isLocationByPlatform()" title="class or interface in java.awt">isLocationByPlatform</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isOpaque()" title="class or interface in java.awt">isOpaque</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isShowing()" title="class or interface in java.awt">isShowing</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#isValidateRoot()" title="class or interface in java.awt">isValidateRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#pack()" title="class or interface in java.awt">pack</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#paint(java.awt.Graphics)" title="class or interface in java.awt">paint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#postEvent(java.awt.Event)" title="class or interface in java.awt">postEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#processEvent(java.awt.AWTEvent)" title="class or interface in java.awt">processEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#processWindowFocusEvent(java.awt.event.WindowEvent)" title="class or interface in java.awt">processWindowFocusEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#processWindowStateEvent(java.awt.event.WindowEvent)" title="class or interface in java.awt">processWindowStateEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#removeWindowFocusListener(java.awt.event.WindowFocusListener)" title="class or interface in java.awt">removeWindowFocusListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#removeWindowListener(java.awt.event.WindowListener)" title="class or interface in java.awt">removeWindowListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#removeWindowStateListener(java.awt.event.WindowStateListener)" title="class or interface in java.awt">removeWindowStateListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#reshape(int,int,int,int)" title="class or interface in java.awt">reshape</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setAlwaysOnTop(boolean)" title="class or interface in java.awt">setAlwaysOnTop</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setAutoRequestFocus(boolean)" title="class or interface in java.awt">setAutoRequestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setBounds(int,int,int,int)" title="class or interface in java.awt">setBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setCursor(java.awt.Cursor)" title="class or interface in java.awt">setCursor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setFocusableWindowState(boolean)" title="class or interface in java.awt">setFocusableWindowState</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setFocusCycleRoot(boolean)" title="class or interface in java.awt">setFocusCycleRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setIconImages(java.util.List)" title="class or interface in java.awt">setIconImages</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setLocation(int,int)" title="class or interface in java.awt">setLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setLocation(java.awt.Point)" title="class or interface in java.awt">setLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setLocationByPlatform(boolean)" title="class or interface in java.awt">setLocationByPlatform</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setLocationRelativeTo(java.awt.Component)" title="class or interface in java.awt">setLocationRelativeTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setMinimumSize(java.awt.Dimension)" title="class or interface in java.awt">setMinimumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setModalExclusionType(java.awt.Dialog.ModalExclusionType)" title="class or interface in java.awt">setModalExclusionType</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setSize(int,int)" title="class or interface in java.awt">setSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setSize(java.awt.Dimension)" title="class or interface in java.awt">setSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setType(java.awt.Window.Type)" title="class or interface in java.awt">setType</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#show()" title="class or interface in java.awt">show</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#toBack()" title="class or interface in java.awt">toBack</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#toFront()" title="class or interface in java.awt">toFront</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.awt.Container">Methods inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,int)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,java.lang.Object)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.awt.Component,java.lang.Object,int)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#add(java.lang.String,java.awt.Component)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#addContainerListener(java.awt.event.ContainerListener)" title="class or interface in java.awt">addContainerListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#applyComponentOrientation(java.awt.ComponentOrientation)" title="class or interface in java.awt">applyComponentOrientation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#areFocusTraversalKeysSet(int)" title="class or interface in java.awt">areFocusTraversalKeysSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#countComponents()" title="class or interface in java.awt">countComponents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#deliverEvent(java.awt.Event)" title="class or interface in java.awt">deliverEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#doLayout()" title="class or interface in java.awt">doLayout</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#findComponentAt(int,int)" title="class or interface in java.awt">findComponentAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#findComponentAt(java.awt.Point)" title="class or interface in java.awt">findComponentAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getAlignmentX()" title="class or interface in java.awt">getAlignmentX</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getAlignmentY()" title="class or interface in java.awt">getAlignmentY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponent(int)" title="class or interface in java.awt">getComponent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentAt(int,int)" title="class or interface in java.awt">getComponentAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentAt(java.awt.Point)" title="class or interface in java.awt">getComponentAt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentCount()" title="class or interface in java.awt">getComponentCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponents()" title="class or interface in java.awt">getComponents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getComponentZOrder(java.awt.Component)" title="class or interface in java.awt">getComponentZOrder</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getContainerListeners()" title="class or interface in java.awt">getContainerListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getFocusTraversalPolicy()" title="class or interface in java.awt">getFocusTraversalPolicy</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getInsets()" title="class or interface in java.awt">getInsets</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getLayout()" title="class or interface in java.awt">getLayout</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getMaximumSize()" title="class or interface in java.awt">getMaximumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getMinimumSize()" title="class or interface in java.awt">getMinimumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getMousePosition(boolean)" title="class or interface in java.awt">getMousePosition</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#getPreferredSize()" title="class or interface in java.awt">getPreferredSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#insets()" title="class or interface in java.awt">insets</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#invalidate()" title="class or interface in java.awt">invalidate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isAncestorOf(java.awt.Component)" title="class or interface in java.awt">isAncestorOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusCycleRoot(java.awt.Container)" title="class or interface in java.awt">isFocusCycleRoot</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusTraversalPolicyProvider()" title="class or interface in java.awt">isFocusTraversalPolicyProvider</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#isFocusTraversalPolicySet()" title="class or interface in java.awt">isFocusTraversalPolicySet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#layout()" title="class or interface in java.awt">layout</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#list(java.io.PrintStream,int)" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#list(java.io.PrintWriter,int)" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#locate(int,int)" title="class or interface in java.awt">locate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#minimumSize()" title="class or interface in java.awt">minimumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#paintComponents(java.awt.Graphics)" title="class or interface in java.awt">paintComponents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#preferredSize()" title="class or interface in java.awt">preferredSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#print(java.awt.Graphics)" title="class or interface in java.awt">print</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#printComponents(java.awt.Graphics)" title="class or interface in java.awt">printComponents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#processContainerEvent(java.awt.event.ContainerEvent)" title="class or interface in java.awt">processContainerEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#remove(int)" title="class or interface in java.awt">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#removeAll()" title="class or interface in java.awt">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#removeContainerListener(java.awt.event.ContainerListener)" title="class or interface in java.awt">removeContainerListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setComponentZOrder(java.awt.Component,int)" title="class or interface in java.awt">setComponentZOrder</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalKeys(int,java.util.Set)" title="class or interface in java.awt">setFocusTraversalKeys</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)" title="class or interface in java.awt">setFocusTraversalPolicy</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFocusTraversalPolicyProvider(boolean)" title="class or interface in java.awt">setFocusTraversalPolicyProvider</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#setFont(java.awt.Font)" title="class or interface in java.awt">setFont</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#transferFocusDownCycle()" title="class or interface in java.awt">transferFocusDownCycle</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#validate()" title="class or interface in java.awt">validate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html#validateTree()" title="class or interface in java.awt">validateTree</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.awt.Component">Methods inherited from class java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#action(java.awt.Event,java.lang.Object)" title="class or interface in java.awt">action</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#add(java.awt.PopupMenu)" title="class or interface in java.awt">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addComponentListener(java.awt.event.ComponentListener)" title="class or interface in java.awt">addComponentListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addFocusListener(java.awt.event.FocusListener)" title="class or interface in java.awt">addFocusListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)" title="class or interface in java.awt">addHierarchyBoundsListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addHierarchyListener(java.awt.event.HierarchyListener)" title="class or interface in java.awt">addHierarchyListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addInputMethodListener(java.awt.event.InputMethodListener)" title="class or interface in java.awt">addInputMethodListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addKeyListener(java.awt.event.KeyListener)" title="class or interface in java.awt">addKeyListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseListener(java.awt.event.MouseListener)" title="class or interface in java.awt">addMouseListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseMotionListener(java.awt.event.MouseMotionListener)" title="class or interface in java.awt">addMouseMotionListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#addMouseWheelListener(java.awt.event.MouseWheelListener)" title="class or interface in java.awt">addMouseWheelListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#bounds()" title="class or interface in java.awt">bounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#checkImage(java.awt.Image,int,int,java.awt.image.ImageObserver)" title="class or interface in java.awt">checkImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#checkImage(java.awt.Image,java.awt.image.ImageObserver)" title="class or interface in java.awt">checkImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#coalesceEvents(java.awt.AWTEvent,java.awt.AWTEvent)" title="class or interface in java.awt">coalesceEvents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#contains(int,int)" title="class or interface in java.awt">contains</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#contains(java.awt.Point)" title="class or interface in java.awt">contains</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createImage(int,int)" title="class or interface in java.awt">createImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createImage(java.awt.image.ImageProducer)" title="class or interface in java.awt">createImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createVolatileImage(int,int)" title="class or interface in java.awt">createVolatileImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#createVolatileImage(int,int,java.awt.ImageCapabilities)" title="class or interface in java.awt">createVolatileImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#disable()" title="class or interface in java.awt">disable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#disableEvents(long)" title="class or interface in java.awt">disableEvents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#dispatchEvent(java.awt.AWTEvent)" title="class or interface in java.awt">dispatchEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enable()" title="class or interface in java.awt">enable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enable(boolean)" title="class or interface in java.awt">enable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enableEvents(long)" title="class or interface in java.awt">enableEvents</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#enableInputMethods(boolean)" title="class or interface in java.awt">enableInputMethods</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,boolean,boolean)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,byte,byte)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,char,char)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,double,double)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,float,float)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,int,int)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,long,long)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,short,short)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object)" title="class or interface in java.awt">firePropertyChange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBaseline(int,int)" title="class or interface in java.awt">getBaseline</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBaselineResizeBehavior()" title="class or interface in java.awt">getBaselineResizeBehavior</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBounds()" title="class or interface in java.awt">getBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBounds(java.awt.Rectangle)" title="class or interface in java.awt">getBounds</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getColorModel()" title="class or interface in java.awt">getColorModel</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getComponentListeners()" title="class or interface in java.awt">getComponentListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getComponentOrientation()" title="class or interface in java.awt">getComponentOrientation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getCursor()" title="class or interface in java.awt">getCursor</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getDropTarget()" title="class or interface in java.awt">getDropTarget</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusListeners()" title="class or interface in java.awt">getFocusListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFocusTraversalKeysEnabled()" title="class or interface in java.awt">getFocusTraversalKeysEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFont()" title="class or interface in java.awt">getFont</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getFontMetrics(java.awt.Font)" title="class or interface in java.awt">getFontMetrics</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getForeground()" title="class or interface in java.awt">getForeground</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getGraphicsConfiguration()" title="class or interface in java.awt">getGraphicsConfiguration</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHeight()" title="class or interface in java.awt">getHeight</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHierarchyBoundsListeners()" title="class or interface in java.awt">getHierarchyBoundsListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getHierarchyListeners()" title="class or interface in java.awt">getHierarchyListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getIgnoreRepaint()" title="class or interface in java.awt">getIgnoreRepaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputMethodListeners()" title="class or interface in java.awt">getInputMethodListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getInputMethodRequests()" title="class or interface in java.awt">getInputMethodRequests</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getKeyListeners()" title="class or interface in java.awt">getKeyListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocation()" title="class or interface in java.awt">getLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocation(java.awt.Point)" title="class or interface in java.awt">getLocation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getLocationOnScreen()" title="class or interface in java.awt">getLocationOnScreen</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseListeners()" title="class or interface in java.awt">getMouseListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseMotionListeners()" title="class or interface in java.awt">getMouseMotionListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMousePosition()" title="class or interface in java.awt">getMousePosition</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getMouseWheelListeners()" title="class or interface in java.awt">getMouseWheelListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getName()" title="class or interface in java.awt">getName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getParent()" title="class or interface in java.awt">getParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getPropertyChangeListeners()" title="class or interface in java.awt">getPropertyChangeListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getPropertyChangeListeners(java.lang.String)" title="class or interface in java.awt">getPropertyChangeListeners</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getSize()" title="class or interface in java.awt">getSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getSize(java.awt.Dimension)" title="class or interface in java.awt">getSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getTreeLock()" title="class or interface in java.awt">getTreeLock</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getWidth()" title="class or interface in java.awt">getWidth</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getX()" title="class or interface in java.awt">getX</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getY()" title="class or interface in java.awt">getY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#gotFocus(java.awt.Event,java.lang.Object)" title="class or interface in java.awt">gotFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#handleEvent(java.awt.Event)" title="class or interface in java.awt">handleEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#hasFocus()" title="class or interface in java.awt">hasFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#imageUpdate(java.awt.Image,int,int,int,int,int)" title="class or interface in java.awt">imageUpdate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#inside(int,int)" title="class or interface in java.awt">inside</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isBackgroundSet()" title="class or interface in java.awt">isBackgroundSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isCursorSet()" title="class or interface in java.awt">isCursorSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isDisplayable()" title="class or interface in java.awt">isDisplayable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isDoubleBuffered()" title="class or interface in java.awt">isDoubleBuffered</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isEnabled()" title="class or interface in java.awt">isEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusable()" title="class or interface in java.awt">isFocusable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusOwner()" title="class or interface in java.awt">isFocusOwner</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFocusTraversable()" title="class or interface in java.awt">isFocusTraversable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isFontSet()" title="class or interface in java.awt">isFontSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isForegroundSet()" title="class or interface in java.awt">isForegroundSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isLightweight()" title="class or interface in java.awt">isLightweight</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isMaximumSizeSet()" title="class or interface in java.awt">isMaximumSizeSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isMinimumSizeSet()" title="class or interface in java.awt">isMinimumSizeSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isPreferredSizeSet()" title="class or interface in java.awt">isPreferredSizeSet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isValid()" title="class or interface in java.awt">isValid</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#isVisible()" title="class or interface in java.awt">isVisible</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#keyDown(java.awt.Event,int)" title="class or interface in java.awt">keyDown</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#keyUp(java.awt.Event,int)" title="class or interface in java.awt">keyUp</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list()" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list(java.io.PrintStream)" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#list(java.io.PrintWriter)" title="class or interface in java.awt">list</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#location()" title="class or interface in java.awt">location</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#lostFocus(java.awt.Event,java.lang.Object)" title="class or interface in java.awt">lostFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseDown(java.awt.Event,int,int)" title="class or interface in java.awt">mouseDown</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseDrag(java.awt.Event,int,int)" title="class or interface in java.awt">mouseDrag</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseEnter(java.awt.Event,int,int)" title="class or interface in java.awt">mouseEnter</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseExit(java.awt.Event,int,int)" title="class or interface in java.awt">mouseExit</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseMove(java.awt.Event,int,int)" title="class or interface in java.awt">mouseMove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#mouseUp(java.awt.Event,int,int)" title="class or interface in java.awt">mouseUp</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#move(int,int)" title="class or interface in java.awt">move</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#nextFocus()" title="class or interface in java.awt">nextFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#paintAll(java.awt.Graphics)" title="class or interface in java.awt">paintAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#prepareImage(java.awt.Image,int,int,java.awt.image.ImageObserver)" title="class or interface in java.awt">prepareImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#prepareImage(java.awt.Image,java.awt.image.ImageObserver)" title="class or interface in java.awt">prepareImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#printAll(java.awt.Graphics)" title="class or interface in java.awt">printAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processComponentEvent(java.awt.event.ComponentEvent)" title="class or interface in java.awt">processComponentEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processFocusEvent(java.awt.event.FocusEvent)" title="class or interface in java.awt">processFocusEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processHierarchyBoundsEvent(java.awt.event.HierarchyEvent)" title="class or interface in java.awt">processHierarchyBoundsEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processHierarchyEvent(java.awt.event.HierarchyEvent)" title="class or interface in java.awt">processHierarchyEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processInputMethodEvent(java.awt.event.InputMethodEvent)" title="class or interface in java.awt">processInputMethodEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processKeyEvent(java.awt.event.KeyEvent)" title="class or interface in java.awt">processKeyEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processMouseEvent(java.awt.event.MouseEvent)" title="class or interface in java.awt">processMouseEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processMouseMotionEvent(java.awt.event.MouseEvent)" title="class or interface in java.awt">processMouseMotionEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#processMouseWheelEvent(java.awt.event.MouseWheelEvent)" title="class or interface in java.awt">processMouseWheelEvent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeComponentListener(java.awt.event.ComponentListener)" title="class or interface in java.awt">removeComponentListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeFocusListener(java.awt.event.FocusListener)" title="class or interface in java.awt">removeFocusListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)" title="class or interface in java.awt">removeHierarchyBoundsListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeHierarchyListener(java.awt.event.HierarchyListener)" title="class or interface in java.awt">removeHierarchyListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeInputMethodListener(java.awt.event.InputMethodListener)" title="class or interface in java.awt">removeInputMethodListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeKeyListener(java.awt.event.KeyListener)" title="class or interface in java.awt">removeKeyListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseListener(java.awt.event.MouseListener)" title="class or interface in java.awt">removeMouseListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseMotionListener(java.awt.event.MouseMotionListener)" title="class or interface in java.awt">removeMouseMotionListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removeMouseWheelListener(java.awt.event.MouseWheelListener)" title="class or interface in java.awt">removeMouseWheelListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removePropertyChangeListener(java.beans.PropertyChangeListener)" title="class or interface in java.awt">removePropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)" title="class or interface in java.awt">removePropertyChangeListener</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint()" title="class or interface in java.awt">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint(int,int,int,int)" title="class or interface in java.awt">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#repaint(long)" title="class or interface in java.awt">repaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus()" title="class or interface in java.awt">requestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(boolean)" title="class or interface in java.awt">requestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(boolean,java.awt.event.FocusEvent.Cause)" title="class or interface in java.awt">requestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocus(java.awt.event.FocusEvent.Cause)" title="class or interface in java.awt">requestFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocusInWindow()" title="class or interface in java.awt">requestFocusInWindow</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocusInWindow(boolean)" title="class or interface in java.awt">requestFocusInWindow</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#requestFocusInWindow(java.awt.event.FocusEvent.Cause)" title="class or interface in java.awt">requestFocusInWindow</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#resize(int,int)" title="class or interface in java.awt">resize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#resize(java.awt.Dimension)" title="class or interface in java.awt">resize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#revalidate()" title="class or interface in java.awt">revalidate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setComponentOrientation(java.awt.ComponentOrientation)" title="class or interface in java.awt">setComponentOrientation</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setDropTarget(java.awt.dnd.DropTarget)" title="class or interface in java.awt">setDropTarget</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setEnabled(boolean)" title="class or interface in java.awt">setEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setFocusable(boolean)" title="class or interface in java.awt">setFocusable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setFocusTraversalKeysEnabled(boolean)" title="class or interface in java.awt">setFocusTraversalKeysEnabled</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setForeground(java.awt.Color)" title="class or interface in java.awt">setForeground</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setIgnoreRepaint(boolean)" title="class or interface in java.awt">setIgnoreRepaint</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setLocale(java.util.Locale)" title="class or interface in java.awt">setLocale</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setMaximumSize(java.awt.Dimension)" title="class or interface in java.awt">setMaximumSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setMixingCutoutShape(java.awt.Shape)" title="class or interface in java.awt">setMixingCutoutShape</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setName(java.lang.String)" title="class or interface in java.awt">setName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#setPreferredSize(java.awt.Dimension)" title="class or interface in java.awt">setPreferredSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#show(boolean)" title="class or interface in java.awt">show</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#size()" title="class or interface in java.awt">size</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#toString()" title="class or interface in java.awt">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocus()" title="class or interface in java.awt">transferFocus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocusBackward()" title="class or interface in java.awt">transferFocusBackward</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#transferFocusUpCycle()" title="class or interface in java.awt">transferFocusUpCycle</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.jidesoft.docking.DockableHolder">Methods inherited from interface com.jidesoft.docking.DockableHolder</h3>
<code>getDockingManager</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.awt.MenuContainer">Methods inherited from interface java.awt.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html" title="class or interface in java.awt">MenuContainer</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html#getFont()" title="class or interface in java.awt">getFont</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/MenuContainer.html#postEvent(java.awt.Event)" title="class or interface in java.awt">postEvent</a></code></div>
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
<section class="detail" id="MAIN_TOOLBAR_EXPERT">
<h3>MAIN_TOOLBAR_EXPERT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MAIN_TOOLBAR_EXPERT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.MainFrame.MAIN_TOOLBAR_EXPERT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MAIN_TOOLBAR_STANDARD">
<h3>MAIN_TOOLBAR_STANDARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MAIN_TOOLBAR_STANDARD</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.MainFrame.MAIN_TOOLBAR_STANDARD">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RECENT_PROJECT_NAME_CHANGE">
<h3>RECENT_PROJECT_NAME_CHANGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECENT_PROJECT_NAME_CHANGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.MainFrame.RECENT_PROJECT_NAME_CHANGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RECENT_WINDOWS">
<h3>RECENT_WINDOWS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECENT_WINDOWS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.MainFrame.RECENT_WINDOWS">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Application.MainFrameController)">
<h3>MainFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MainFrame</span><wbr/><span class="parameters">(com.nomagic.magicdraw.core.Application.MainFrameController controller)</span></div>
<div class="block">Constructs MainFrame window, adds menu and popup buttons toolbar to it.
 Also this method sets event listeners for each menu item and toolbar button.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>controller</code> - controller</dd>
</dl>
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
<section class="detail" id="setBounds(java.awt.Rectangle)">
<h3>setBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setBounds(java.awt.Rectangle)" title="class or interface in java.awt">setBounds</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainMenuBar()">
<h3>getMainMenuBar</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuBar.html" title="class or interface in javax.swing">JMenuBar</a></span> <span class="element-name">getMainMenuBar</span>()</div>
<div class="block">Returns main menu bar.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>main menu bar.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActiveFrame(java.awt.Frame)">
<h3>setActiveFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActiveFrame</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> activeFrame)</span></div>
</section>
</li>
<li>
<section class="detail" id="getActiveFrame()">
<h3>getActiveFrame</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a></span> <span class="element-name">getActiveFrame</span>()</div>
</section>
</li>
<li>
<section class="detail" id="init()">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span>()</div>
<div class="block">Creates GUI elements in MainFrame: menu and toolbar, browser and desktop.
 And adds action listeners to menu items and toolbar buttons</div>
</section>
</li>
<li>
<section class="detail" id="createCommandBar()">
<h3>createCommandBar</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createCommandBar</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createMenuAndToolbars()"><code>createMenuAndToolbars()</code></a>. Some people use this api, because we had no way</div>
</div>
</section>
</li>
<li>
<section class="detail" id="createMenuAndToolbars()">
<h3>createMenuAndToolbars</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createMenuAndToolbars</span>()</div>
<div class="block">Create (or recreate) all menu and toolbars.
 It will invoke all registered <a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions"><code>AMConfigurator</code></a> in <a href="../actions/ActionsConfiguratorsManager.html" title="class in com.nomagic.magicdraw.actions"><code>ActionsConfiguratorsManager</code></a></div>
</section>
</li>
<li>
<section class="detail" id="getBrowser()">
<h3>getBrowser</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="browser/Browser.html" title="class in com.nomagic.magicdraw.ui.browser">Browser</a></span> <span class="element-name">getBrowser</span>()</div>
<div class="block">Returns model browser.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>model browser.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateByEnvironmentProperties(java.util.List)">
<h3>updateByEnvironmentProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateByEnvironmentProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; properties)</span></div>
<div class="block">Update environment by given properties.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../core/options/EnvironmentOptions.EnvironmentChangeListener.html#updateByEnvironmentProperties(java.util.List)">updateByEnvironmentProperties</a></code> in interface <code><a href="../core/options/EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>properties</code> - properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSilentMode()">
<h3>isSilentMode</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSilentMode</span>()</div>
<div class="block">Returns, flag, which shows if MF is working in silent mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flag, which shows if MF is working in silent mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSilentMode(boolean)">
<h3>setSilentMode</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSilentMode</span><wbr/><span class="parameters">(boolean silentMode)</span></div>
<div class="block">Set flag, which shows if MF is working in silent mode.
 <p></p>
 Used by Forte Integration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>silentMode</code> - flag, which shows if MF is working in silent mode.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpecificCursor()">
<h3>getSpecificCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">getSpecificCursor</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getSpecificCursor</code> in interface <code>com.nomagic.ui.CursorOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentCursor()">
<h3>getCurrentCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">getCurrentCursor</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getCurrentCursor</code> in interface <code>com.nomagic.ui.CursorOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpecificCursor(java.awt.Cursor)">
<h3>setSpecificCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSpecificCursor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> c)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setSpecificCursor</code> in interface <code>com.nomagic.ui.CursorOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> evt)</span></div>
<div class="block">Handles Property changing event, fired by <code>PropertyChangeSupport</code>
<p></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>evt</code> - PropertyChangeEvent, which has to be handled.
            <p></p></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans"><code>PropertyChangeListener</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans"><code>PropertyChangeEvent</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans"><code>PropertyChangeListener</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeSupport.html" title="class or interface in java.beans"><code>PropertyChangeSupport</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLF(java.lang.String,java.lang.String,int,boolean)">
<h3>setLF</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setLF</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lf,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> theme,
 int jideStyle,
 boolean explicitlyUpdateUI)</span></div>
</section>
</li>
<li>
<section class="detail" id="sSetLF(java.lang.String,java.lang.String,int,boolean)">
<h3>sSetLF</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sSetLF</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lf,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> themeID,
 int jideStyle,
 boolean explicitlyUpdateUI)</span>
            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></span></div>
<div class="block">Set look and feel without handling errors</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lf</code> - lf name</dd>
<dd><code>themeID</code> - theme id</dd>
<dd><code>jideStyle</code> - jide style</dd>
<dd><code>explicitlyUpdateUI</code> - update ui flag</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLFUpdateRequired(java.lang.String,java.lang.String,int)">
<h3>isLFUpdateRequired</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLFUpdateRequired</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lf,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> themeID,
 int jideStyle)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateFrameUI(boolean)">
<h3>updateFrameUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateFrameUI</span><wbr/><span class="parameters">(boolean forceUpdate)</span></div>
<div class="block">Updates all elements ui</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>forceUpdate</code> - set true to force update even if L&amp;F did not change</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addRecentWindow(com.nomagic.magicdraw.ui.editorwindows.EditorWindow)">
<h3>addRecentWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addRecentWindow</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.editorwindows.EditorWindow window)</span></div>
<div class="block">Adds diagram window name to the recent window list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>window</code> - the window to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRecentWindowsList(java.util.Collection)">
<h3>setRecentWindowsList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRecentWindowsList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;?&gt;&gt; windows)</span></div>
<div class="block">Sets the list of the recent windows.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>windows</code> - the new list of the recent windows.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateRecentProject(com.nomagic.magicdraw.core.Project)">
<h3>updateRecentProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateRecentProject</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> prj)</span></div>
<div class="block">Updates project label in projects choice.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prj</code> - - project to update</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectWindowsManager()">
<h3>getProjectWindowsManager</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="ProjectWindowsManager.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowsManager</a></span> <span class="element-name">getProjectWindowsManager</span>()</div>
<div class="block">Returns ProjectWindowsManager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project windows manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWindowsManager()">
<h3>getWindowsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.WindowsManagerImpl</span> <span class="element-name">getWindowsManager</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addStateListener(java.beans.PropertyChangeListener)">
<h3>addStateListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addStateListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Adds listener for listening changes of recent windows, projects or files.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener for listening changes of recent windows, projects or files.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateTitle(com.nomagic.magicdraw.core.Project)">
<h3>updateTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateTitle</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
</section>
</li>
<li>
<section class="detail" id="getProjectTitle(com.nomagic.magicdraw.core.Project)">
<h3>getProjectTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectTitle</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns project title suitable for application title bar</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project instance of <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core"><code>Project</code></a></dd>
<dt>Returns:</dt>
<dd>project title suitable for application title bar</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStatusLine(com.nomagic.awt.StatusLine)">
<h3>setStatusLine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStatusLine</span><wbr/><span class="parameters">(com.nomagic.awt.StatusLine statusLine)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStatusLine()">
<h3>getStatusLine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.awt.StatusLine</span> <span class="element-name">getStatusLine</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCookieSet()">
<h3>getCookieSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../cookies/CookieSet.html" title="class in com.nomagic.magicdraw.cookies">CookieSet</a></span> <span class="element-name">getCookieSet</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getProgressBar()">
<h3>getProgressBar</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.ProgressBar</span> <span class="element-name">getProgressBar</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns the progressBar.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUIInstaller()">
<h3>getUIInstaller</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.UIInstaller</span> <span class="element-name">getUIInstaller</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns the uIInstaller.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUIInstaller(com.nomagic.magicdraw.ui.UIInstaller)">
<h3>setUIInstaller</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUIInstaller</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.UIInstaller installer)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>installer</code> - The uIInstaller to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisible(boolean)">
<h3>setVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisible</span><wbr/><span class="parameters">(boolean visible)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html#setVisible(boolean)" title="class or interface in java.awt">setVisible</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getToolbarsManager()">
<h3>getToolbarsManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.toolbar.ToolbarsManager</span> <span class="element-name">getToolbarsManager</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createStartupActivity()">
<h3>createStartupActivity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></span> <span class="element-name">createStartupActivity</span>()</div>
<div class="block">Creates startup activity for setting APPLICATION_STARTED flag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>runnable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWindowFullScreenCustomizer()">
<h3>getWindowFullScreenCustomizer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a>&gt;</span> <span class="element-name">getWindowFullScreenCustomizer</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setWindowFullScreenCustomizer(java.util.function.Consumer)">
<h3>setWindowFullScreenCustomizer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWindowFullScreenCustomizer</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a>&gt; windowFullScreenCustomizer)</span></div>
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
