# JAVA OPENAPI: DiagramWindow (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/DiagramWindow.html
- source_path: `com/nomagic/magicdraw/ui/DiagramWindow.html`
- source_sha256: `be58b283d5f13b99a1d145afd478e2f6423cdd132b872d0d21590db591e295ef`
- captured_utc: `2026-07-14T16:55:50.637406+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class DiagramWindow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>
com.nomagic.magicdraw.ui.DiagramWindow

All Implemented Interfaces:
`com.jidesoft.document.DocumentComponentListener`, `com.nomagic.magicdraw.ui.Activatable`, `[DiagramPresentationElementGetter](DiagramPresentationElementGetter.html)`, `com.nomagic.ui.CursorOwner`, `[HiDPIScalableComponent](../../ui/HiDPIScalableComponent.html)`, `[FocusListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/FocusListener.html)`, `[WindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApipublic classDiagramWindow
extends com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>
implements [DiagramPresentationElementGetter](DiagramPresentationElementGetter.html)

This class is base class for diagram-specific windows.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CLASS_TYPE_SUFFIX](#CLASS_TYPE_SUFFIX)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CREATE_PALETTE](#CREATE_PALETTE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CREATE_TOOLBAR](#CREATE_TOOLBAR)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramWindow](#%3Cinit%3E(com.nomagic.magicdraw.ui.DiagramWindowPanel))(com.nomagic.magicdraw.ui.DiagramWindowPanel panel)`
Constructs window with a specified panel.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[activate](#activate())()`
Activate window - load diagram content if needed.
`void`
`[activateDocument](#activateDocument(com.nomagic.magicdraw.ui.editorwindows.EditorWindow,boolean))(com.nomagic.magicdraw.ui.editorwindows.EditorWindow old,
 boolean activationTrackingEnabled)`

`void`
`[closeWindow](#closeWindow())()`
Closes the window
`void`
`[createContainer](#createContainer(com.jidesoft.document.DocumentPane,com.nomagic.magicdraw.ui.ProgressBarEditorWindowZoomToolbar,com.nomagic.magicdraw.ui.presentationmode.ProgressBarEditorWindowPresentationModeToolbar))(com.jidesoft.document.DocumentPane documentPane,
 com.nomagic.magicdraw.ui.ProgressBarEditorWindowZoomToolbar zoomToolbar,
 com.nomagic.magicdraw.ui.presentationmode.ProgressBarEditorWindowPresentationModeToolbar presentationModeToolbar)`

`void`
`[createToolbars](#createToolbars(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> options)`
Created some toolbars using given options
`void`
`[customizePopupMenu](#customizePopupMenu(javax.swing.JPopupMenu))([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) popupMenu)`

`void`
`[deactivateDocument](#deactivateDocument())()`

`void`
`[dropContainer](#dropContainer())()`

`void`
`[enabledDisabledToolbar](#enabledDisabledToolbar())()`
Disable or enable the toolbar according to the checkout state of the diagram.
`static void`
`[executeWithLockedRepaint](#executeWithLockedRepaint(java.lang.Runnable,com.nomagic.magicdraw.ui.DiagramWindowPanel))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) run,
 com.nomagic.magicdraw.ui.DiagramWindowPanel diagramWindowPanel)`
Executes given runnable while not repainting a diagram window panel.
`[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)`
`[getAbstractDiagramPresentationElement](#getAbstractDiagramPresentationElement())()`
Returns the diagram of this window.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Gets the type of the class.
`com.nomagic.magicdraw.ui.DiagramFrame`
`[getContainer](#getContainer())()`

`[Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[getCurrentCursor](#getCurrentCursor())()`

`[DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html)`
`[getDiagramPresentationElement](#getDiagramPresentationElement())()`
Deprecated.
use [`getAbstractDiagramPresentationElement()`](#getAbstractDiagramPresentationElement())
`[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)`
`[getDocument](#getDocument())()`

`com.jidesoft.document.DocumentComponent`
`[getDocumentComponent](#getDocumentComponent())()`

`com.nomagic.magicdraw.ui.DrawArea`
`[getDrawArea](#getDrawArea())()`
Get draw area of the window.
`[JComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html)`
`[getFocusableComponent](#getFocusableComponent())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) document)`

`com.dassault_systemes.modeler.magic.ui.editorwindow.EditorWindowOptions`
`[getOptions](#getOptions())()`

`com.nomagic.magicdraw.ui.DiagramWindowPanel`
`[getPanel](#getPanel())()`
Returns the panel on which diagram is drawn.
`[Project](../core/Project.html)`
`[getProject](#getProject())()`
Project of activatable component
`[Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[getSpecificCursor](#getSpecificCursor())()`
Returns cursor of the tree
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTitle](#getTitle())()`

`long`
`[getWindowActivationTime](#getWindowActivationTime())()`

`void`
`[hideWindow](#hideWindow())()`

`boolean`
`[isEnableLoadOnActivation](#isEnableLoadOnActivation())()`

`boolean`
`[isUseBufferImage](#isUseBufferImage())()`

`boolean`
`[isVisible](#isVisible())()`

`void`
`[openDocument](#openDocument())()`

`void`
`[repaintWindow](#repaintWindow())()`

`void`
`[restoreOptions](#restoreOptions())()`
Restore window state from diagram view options
`void`
`[scaleForHiDPI](#scaleForHiDPI())()`

`void`
`[setBounds](#setBounds(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`

`void`
`[setContainer](#setContainer(javax.swing.JPanel))([JPanel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html) container)`

`void`
`[setDocument](#setDocument(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)`

`void`
`[setEnableLoadOnActivation](#setEnableLoadOnActivation(boolean))(boolean enableLoadOnActivation)`
Set load content on activation state
`void`
`[setFireEvents](#setFireEvents(boolean))(boolean fireEvents)`

`void`
`[setSpecificCursor](#setSpecificCursor(java.awt.Cursor))([Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) c)`
Sets cursor for documentation and tree
`void`
`[setVisible](#setVisible(boolean))(boolean visible)`

`void`
`[storeOptions](#storeOptions())()`
Remembers all view options/parameters upon close,
 so it's state could be restored when the diagram is opened again.
`void`
`[toFront](#toFront())()`

`void`
`[updateRepresentation](#updateRepresentation())()`

`void`
`[useBufferImage](#useBufferImage(boolean))(boolean use)`

`void`
`[windowActivated](#windowActivated(java.awt.event.WindowEvent))([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)`
handles window activation event
`void`
`[windowClosed](#windowClosed(java.awt.event.WindowEvent))([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)`
handles event invoked after window closing
`void`
`[windowDeactivated](#windowDeactivated(java.awt.event.WindowEvent))([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)`

`void`
`[windowDeiconified](#windowDeiconified(java.awt.event.WindowEvent))([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)`

`void`
`[windowIconified](#windowIconified(java.awt.event.WindowEvent))([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)`

`void`
`[windowOpened](#windowOpened(java.awt.event.WindowEvent))([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)`
Methods inherited from class com.nomagic.magicdraw.ui.editorwindows.EditorWindow
`createToolbarsForAllWindows, documentComponentActivated, documentComponentClosed, documentComponentClosing, documentComponentDeactivated, documentComponentDocked, documentComponentFloated, documentComponentMoved, documentComponentMoving, documentComponentOpened, executeWithoutEventFiring, firePropertyChange, focusGained, focusLost, getDocument, getID, getLocation, getLocationOnScreen, isFloating, isHiDPIScaled, isWindowClosed, renameDocumentComponent, requestFocus, setHiDPIScaled, setLocation, setMoveListener, setWindowClosed, windowClosing`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
CREATE_TOOLBAR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CREATE_TOOLBAR
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.DiagramWindow.CREATE_TOOLBAR)
CREATE_PALETTE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CREATE_PALETTE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.DiagramWindow.CREATE_PALETTE)
CLASS_TYPE_SUFFIX
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CLASS_TYPE_SUFFIX
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.DiagramWindow.CLASS_TYPE_SUFFIX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramWindow
public DiagramWindow(com.nomagic.magicdraw.ui.DiagramWindowPanel panel)
Constructs window with a specified panel.
Parameters:
`panel` - the panel to set.
 ============ METHOD DETAIL ========== 
Method Details
getTitle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTitle()
Specified by:
`getTitle` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
updateRepresentation
public void updateRepresentation()
Specified by:
`updateRepresentation` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
enabledDisabledToolbar
public void enabledDisabledToolbar()
Disable or enable the toolbar according to the checkout state of the diagram.
Specified by:
`enabledDisabledToolbar` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
setDocument
public void setDocument(@CheckForNull
 [AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)
Specified by:
`setDocument` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
setVisible
public void setVisible(boolean visible)
Specified by:
`setVisible` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getContainer
@CheckForNullpublic com.nomagic.magicdraw.ui.DiagramFrame getContainer()
Specified by:
`getContainer` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
setContainer
public void setContainer([JPanel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html) container)
Specified by:
`setContainer` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
dropContainer
public void dropContainer()
Overrides:
`dropContainer` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
windowActivated
public void windowActivated([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)
handles window activation event
Specified by:
`[windowActivated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowActivated(java.awt.event.WindowEvent))` in interface `[WindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)`
Parameters:
`e` - Window event to handle
See Also:
[`WindowListener`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)
[`WindowEvent`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html)
windowClosed
public void windowClosed([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)
handles event invoked after window closing
Specified by:
`[windowClosed](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowClosed(java.awt.event.WindowEvent))` in interface `[WindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)`
Parameters:
`e` - Window event to handle
See Also:
[`WindowListener`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)
[`WindowEvent`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html)
closeWindow
public void closeWindow()
Closes the window
Overrides:
`closeWindow` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
windowDeactivated
public void windowDeactivated([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)
Specified by:
`[windowDeactivated](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowDeactivated(java.awt.event.WindowEvent))` in interface `[WindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)`
windowDeiconified
public void windowDeiconified([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)
Specified by:
`[windowDeiconified](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowDeiconified(java.awt.event.WindowEvent))` in interface `[WindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)`
windowIconified
public void windowIconified([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)
Specified by:
`[windowIconified](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowIconified(java.awt.event.WindowEvent))` in interface `[WindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)`
windowOpened
public void windowOpened([WindowEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html) e)
Specified by:
`[windowOpened](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowOpened(java.awt.event.WindowEvent))` in interface `[WindowListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html)`
toFront
public void toFront()
Specified by:
`toFront` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getFocusableComponent
@CheckForNullpublic [JComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html) getFocusableComponent()
Specified by:
`getFocusableComponent` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
setBounds
public void setBounds([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
Specified by:
`setBounds` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getBounds
@CheckForNullpublic [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBounds()
Specified by:
`getBounds` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
hideWindow
public void hideWindow()
Specified by:
`hideWindow` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getClassType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Gets the type of the class.
Returns:
the type of the class - a `String`
getDrawArea
@CheckForNullpublic com.nomagic.magicdraw.ui.DrawArea getDrawArea()
Get draw area of the window.
 This method returns the draw area panel from DiagramWindowPanel.
Returns:
current draw area
getDiagramPresentationElement
@CheckForNull
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) getDiagramPresentationElement()
Deprecated.
use [`getAbstractDiagramPresentationElement()`](#getAbstractDiagramPresentationElement())
Returns the diagram view of this window.
 This method returns the diagram view from DiagramWindowPanel.
Specified by:
`[getDiagramPresentationElement](DiagramPresentationElementGetter.html#getDiagramPresentationElement())` in interface `[DiagramPresentationElementGetter](DiagramPresentationElementGetter.html)`
Returns:
current diagram view.
getAbstractDiagramPresentationElement
@OpenApi
@CheckForNullpublic [AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) getAbstractDiagramPresentationElement()
Returns the diagram of this window.
 This method returns the diagram from DiagramWindowPanel.
Returns:
diagram
getPanel
public com.nomagic.magicdraw.ui.DiagramWindowPanel getPanel()
Returns the panel on which diagram is drawn.
Returns:
the diagram drawing panel.
getSpecificCursor
public [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) getSpecificCursor()
Returns cursor of the tree
Specified by:
`getSpecificCursor` in interface `com.nomagic.ui.CursorOwner`
setSpecificCursor
public void setSpecificCursor([Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) c)
Sets cursor for documentation and tree
Specified by:
`setSpecificCursor` in interface `com.nomagic.ui.CursorOwner`
getCurrentCursor
@CheckForNullpublic [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) getCurrentCursor()
Specified by:
`getCurrentCursor` in interface `com.nomagic.ui.CursorOwner`
isVisible
public boolean isVisible()
Specified by:
`isVisible` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
createToolbars
public void createToolbars([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> options)
Description copied from class: `com.nomagic.magicdraw.ui.editorwindows.EditorWindow`
Created some toolbars using given options
Specified by:
`createToolbars` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
Parameters:
`options` - toolbar options
isEnableLoadOnActivation
public boolean isEnableLoadOnActivation()
Specified by:
`isEnableLoadOnActivation` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
Returns:
true if diagram should load content on activation
setEnableLoadOnActivation
public void setEnableLoadOnActivation(boolean enableLoadOnActivation)
Set load content on activation state
Specified by:
`setEnableLoadOnActivation` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
Parameters:
`enableLoadOnActivation` - true if diagram should load content on activation
activate
public void activate()
Activate window - load diagram content if needed.
Specified by:
`activate` in interface `com.nomagic.magicdraw.ui.Activatable`
storeOptions
public void storeOptions()
Remembers all view options/parameters upon close,
 so it's state could be restored when the diagram is opened again.
Specified by:
`storeOptions` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
restoreOptions
public void restoreOptions()
Restore window state from diagram view options
Specified by:
`restoreOptions` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getProject
@CheckForNullpublic [Project](../core/Project.html) getProject()
Description copied from interface: `com.nomagic.magicdraw.ui.Activatable`
Project of activatable component
Specified by:
`getProject` in interface `com.nomagic.magicdraw.ui.Activatable`
Returns:
project
scaleForHiDPI
public void scaleForHiDPI()
Specified by:
`[scaleForHiDPI](../../ui/HiDPIScalableComponent.html#scaleForHiDPI())` in interface `[HiDPIScalableComponent](../../ui/HiDPIScalableComponent.html)`
executeWithLockedRepaint
public static void executeWithLockedRepaint([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) run,
 @CheckForNull
 com.nomagic.magicdraw.ui.DiagramWindowPanel diagramWindowPanel)
Executes given runnable while not repainting a diagram window panel.
Parameters:
`run` - runnable to execute
`diagramWindowPanel` - diagram window panel which must be repainted after this runnable completing
openDocument
public void openDocument()
Specified by:
`openDocument` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getDocument
@CheckForNullpublic [AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) getDocument()
Specified by:
`getDocument` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getDocumentComponent
public com.jidesoft.document.DocumentComponent getDocumentComponent()
Specified by:
`getDocumentComponent` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
activateDocument
public void activateDocument(@CheckForNull
 com.nomagic.magicdraw.ui.editorwindows.EditorWindow old,
 boolean activationTrackingEnabled)
Specified by:
`activateDocument` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
deactivateDocument
public void deactivateDocument()
Specified by:
`deactivateDocument` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getWindowActivationTime
public long getWindowActivationTime()
Specified by:
`getWindowActivationTime` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
repaintWindow
public void repaintWindow()
Specified by:
`repaintWindow` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
isUseBufferImage
public boolean isUseBufferImage()
Specified by:
`isUseBufferImage` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
useBufferImage
public void useBufferImage(boolean use)
Specified by:
`useBufferImage` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getOptions
public com.dassault_systemes.modeler.magic.ui.editorwindow.EditorWindowOptions getOptions()
Specified by:
`getOptions` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
getID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID(@CheckForNull
 [AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) document)
Specified by:
`getID` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
createContainer
public void createContainer(com.jidesoft.document.DocumentPane documentPane,
 com.nomagic.magicdraw.ui.ProgressBarEditorWindowZoomToolbar zoomToolbar,
 com.nomagic.magicdraw.ui.presentationmode.ProgressBarEditorWindowPresentationModeToolbar presentationModeToolbar)
Overrides:
`createContainer` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
setFireEvents
public void setFireEvents(boolean fireEvents)
Overrides:
`setFireEvents` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`
customizePopupMenu
public void customizePopupMenu([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) popupMenu)
Overrides:
`customizePopupMenu` in class `com.nomagic.magicdraw.ui.editorwindows.EditorWindow<[AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class DiagramWindow">Class DiagramWindow</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.ui.DiagramWindow</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.jidesoft.document.DocumentComponentListener</code>, <code>com.nomagic.magicdraw.ui.Activatable</code>, <code><a href="DiagramPresentationElementGetter.html" title="interface in com.nomagic.magicdraw.ui">DiagramPresentationElementGetter</a></code>, <code>com.nomagic.ui.CursorOwner</code>, <code><a href="../../ui/HiDPIScalableComponent.html" title="interface in com.nomagic.ui">HiDPIScalableComponent</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/FocusListener.html" title="class or interface in java.awt.event">FocusListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event">WindowListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramWindow</span>
<span class="extends-implements">extends com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;
implements <a href="DiagramPresentationElementGetter.html" title="interface in com.nomagic.magicdraw.ui">DiagramPresentationElementGetter</a></span></div>
<div class="block">This class is base class for diagram-specific windows.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CLASS_TYPE_SUFFIX">CLASS_TYPE_SUFFIX</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CREATE_PALETTE">CREATE_PALETTE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CREATE_TOOLBAR">CREATE_TOOLBAR</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.ui.DiagramWindowPanel)">DiagramWindow</a><wbr/>(com.nomagic.magicdraw.ui.DiagramWindowPanel panel)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs window with a specified panel.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activate()">activate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Activate window - load diagram content if needed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activateDocument(com.nomagic.magicdraw.ui.editorwindows.EditorWindow,boolean)">activateDocument</a><wbr/>(com.nomagic.magicdraw.ui.editorwindows.EditorWindow old,
 boolean activationTrackingEnabled)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeWindow()">closeWindow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes the window</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createContainer(com.jidesoft.document.DocumentPane,com.nomagic.magicdraw.ui.ProgressBarEditorWindowZoomToolbar,com.nomagic.magicdraw.ui.presentationmode.ProgressBarEditorWindowPresentationModeToolbar)">createContainer</a><wbr/>(com.jidesoft.document.DocumentPane documentPane,
 com.nomagic.magicdraw.ui.ProgressBarEditorWindowZoomToolbar zoomToolbar,
 com.nomagic.magicdraw.ui.presentationmode.ProgressBarEditorWindowPresentationModeToolbar presentationModeToolbar)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createToolbars(java.util.Map)">createToolbars</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Created some toolbars using given options</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#customizePopupMenu(javax.swing.JPopupMenu)">customizePopupMenu</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> popupMenu)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#deactivateDocument()">deactivateDocument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dropContainer()">dropContainer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#enabledDisabledToolbar()">enabledDisabledToolbar</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disable or enable the toolbar according to the checkout state of the diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#executeWithLockedRepaint(java.lang.Runnable,com.nomagic.magicdraw.ui.DiagramWindowPanel)">executeWithLockedRepaint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> run,
 com.nomagic.magicdraw.ui.DiagramWindowPanel diagramWindowPanel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes given runnable while not repainting a diagram window panel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbstractDiagramPresentationElement()">getAbstractDiagramPresentationElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the diagram of this window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBounds()">getBounds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the type of the class.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.DiagramFrame</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainer()">getContainer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentCursor()">getCurrentCursor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDiagramPresentationElement()">getDiagramPresentationElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getAbstractDiagramPresentationElement()"><code>getAbstractDiagramPresentationElement()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocument()">getDocument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.jidesoft.document.DocumentComponent</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocumentComponent()">getDocumentComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.DrawArea</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDrawArea()">getDrawArea</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get draw area of the window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFocusableComponent()">getFocusableComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getID</a><wbr/>(<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> document)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.dassault_systemes.modeler.magic.ui.editorwindow.EditorWindowOptions</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.DiagramWindowPanel</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPanel()">getPanel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the panel on which diagram is drawn.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Project of activatable component</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSpecificCursor()">getSpecificCursor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns cursor of the tree</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitle()">getTitle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWindowActivationTime()">getWindowActivationTime</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hideWindow()">hideWindow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnableLoadOnActivation()">isEnableLoadOnActivation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseBufferImage()">isUseBufferImage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVisible()">isVisible</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openDocument()">openDocument</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#repaintWindow()">repaintWindow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#restoreOptions()">restoreOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Restore window state from diagram view options</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleForHiDPI()">scaleForHiDPI</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBounds(java.awt.Rectangle)">setBounds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContainer(javax.swing.JPanel)">setContainer</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html" title="class or interface in javax.swing">JPanel</a> container)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDocument(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">setDocument</a><wbr/>(<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnableLoadOnActivation(boolean)">setEnableLoadOnActivation</a><wbr/>(boolean enableLoadOnActivation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set load content on activation state</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFireEvents(boolean)">setFireEvents</a><wbr/>(boolean fireEvents)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSpecificCursor(java.awt.Cursor)">setSpecificCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets cursor for documentation and tree</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisible(boolean)">setVisible</a><wbr/>(boolean visible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#storeOptions()">storeOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remembers all view options/parameters upon close,
 so it's state could be restored when the diagram is opened again.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toFront()">toFront</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateRepresentation()">updateRepresentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#useBufferImage(boolean)">useBufferImage</a><wbr/>(boolean use)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#windowActivated(java.awt.event.WindowEvent)">windowActivated</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">handles window activation event</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#windowClosed(java.awt.event.WindowEvent)">windowClosed</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">handles event invoked after window closing</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#windowDeactivated(java.awt.event.WindowEvent)">windowDeactivated</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#windowDeiconified(java.awt.event.WindowEvent)">windowDeiconified</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#windowIconified(java.awt.event.WindowEvent)">windowIconified</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#windowOpened(java.awt.event.WindowEvent)">windowOpened</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.editorwindows.EditorWindow">Methods inherited from class com.nomagic.magicdraw.ui.editorwindows.EditorWindow</h3>
<code>createToolbarsForAllWindows, documentComponentActivated, documentComponentClosed, documentComponentClosing, documentComponentDeactivated, documentComponentDocked, documentComponentFloated, documentComponentMoved, documentComponentMoving, documentComponentOpened, executeWithoutEventFiring, firePropertyChange, focusGained, focusLost, getDocument, getID, getLocation, getLocationOnScreen, isFloating, isHiDPIScaled, isWindowClosed, renameDocumentComponent, requestFocus, setHiDPIScaled, setLocation, setMoveListener, setWindowClosed, windowClosing</code></div>
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
<section class="detail" id="CREATE_TOOLBAR">
<h3>CREATE_TOOLBAR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CREATE_TOOLBAR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.DiagramWindow.CREATE_TOOLBAR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CREATE_PALETTE">
<h3>CREATE_PALETTE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CREATE_PALETTE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.DiagramWindow.CREATE_PALETTE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLASS_TYPE_SUFFIX">
<h3>CLASS_TYPE_SUFFIX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CLASS_TYPE_SUFFIX</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.DiagramWindow.CLASS_TYPE_SUFFIX">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.ui.DiagramWindowPanel)">
<h3>DiagramWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramWindow</span><wbr/><span class="parameters">(com.nomagic.magicdraw.ui.DiagramWindowPanel panel)</span></div>
<div class="block">Constructs window with a specified panel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>panel</code> - the panel to set.</dd>
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
<section class="detail" id="getTitle()">
<h3>getTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getTitle</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateRepresentation()">
<h3>updateRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateRepresentation</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>updateRepresentation</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="enabledDisabledToolbar()">
<h3>enabledDisabledToolbar</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enabledDisabledToolbar</span>()</div>
<div class="block">Disable or enable the toolbar according to the checkout state of the diagram.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>enabledDisabledToolbar</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDocument(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>setDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDocument</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setDocument</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisible(boolean)">
<h3>setVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisible</span><wbr/><span class="parameters">(boolean visible)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setVisible</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainer()">
<h3>getContainer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.DiagramFrame</span> <span class="element-name">getContainer</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getContainer</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContainer(javax.swing.JPanel)">
<h3>setContainer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContainer</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPanel.html" title="class or interface in javax.swing">JPanel</a> container)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setContainer</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dropContainer()">
<h3>dropContainer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dropContainer</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>dropContainer</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="windowActivated(java.awt.event.WindowEvent)">
<h3>windowActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">windowActivated</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</span></div>
<div class="block">handles window activation event</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowActivated(java.awt.event.WindowEvent)" title="class or interface in java.awt.event">windowActivated</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event">WindowListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - Window event to handle</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event"><code>WindowListener</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event"><code>WindowEvent</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="windowClosed(java.awt.event.WindowEvent)">
<h3>windowClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">windowClosed</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</span></div>
<div class="block">handles event invoked after window closing</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowClosed(java.awt.event.WindowEvent)" title="class or interface in java.awt.event">windowClosed</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event">WindowListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - Window event to handle</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event"><code>WindowListener</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event"><code>WindowEvent</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeWindow()">
<h3>closeWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeWindow</span>()</div>
<div class="block">Closes the window</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>closeWindow</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="windowDeactivated(java.awt.event.WindowEvent)">
<h3>windowDeactivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">windowDeactivated</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowDeactivated(java.awt.event.WindowEvent)" title="class or interface in java.awt.event">windowDeactivated</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event">WindowListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="windowDeiconified(java.awt.event.WindowEvent)">
<h3>windowDeiconified</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">windowDeiconified</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowDeiconified(java.awt.event.WindowEvent)" title="class or interface in java.awt.event">windowDeiconified</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event">WindowListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="windowIconified(java.awt.event.WindowEvent)">
<h3>windowIconified</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">windowIconified</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowIconified(java.awt.event.WindowEvent)" title="class or interface in java.awt.event">windowIconified</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event">WindowListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="windowOpened(java.awt.event.WindowEvent)">
<h3>windowOpened</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">windowOpened</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowEvent.html" title="class or interface in java.awt.event">WindowEvent</a> e)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html#windowOpened(java.awt.event.WindowEvent)" title="class or interface in java.awt.event">windowOpened</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/event/WindowListener.html" title="class or interface in java.awt.event">WindowListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toFront()">
<h3>toFront</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">toFront</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>toFront</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFocusableComponent()">
<h3>getFocusableComponent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></span> <span class="element-name">getFocusableComponent</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getFocusableComponent</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBounds(java.awt.Rectangle)">
<h3>setBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBounds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setBounds</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBounds()">
<h3>getBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getBounds</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideWindow()">
<h3>hideWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">hideWindow</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>hideWindow</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Gets the type of the class.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the type of the class - a <code>String</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawArea()">
<h3>getDrawArea</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.DrawArea</span> <span class="element-name">getDrawArea</span>()</div>
<div class="block">Get draw area of the window.
 This method returns the draw area panel from DiagramWindowPanel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>current draw area</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramPresentationElement()">
<h3>getDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a></span> <span class="element-name">getDiagramPresentationElement</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getAbstractDiagramPresentationElement()"><code>getAbstractDiagramPresentationElement()</code></a></div>
</div>
<div class="block">Returns the diagram view of this window.
 This method returns the diagram view from DiagramWindowPanel.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="DiagramPresentationElementGetter.html#getDiagramPresentationElement()">getDiagramPresentationElement</a></code> in interface <code><a href="DiagramPresentationElementGetter.html" title="interface in com.nomagic.magicdraw.ui">DiagramPresentationElementGetter</a></code></dd>
<dt>Returns:</dt>
<dd>current diagram view.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractDiagramPresentationElement()">
<h3>getAbstractDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getAbstractDiagramPresentationElement</span>()</div>
<div class="block">Returns the diagram of this window.
 This method returns the diagram from DiagramWindowPanel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPanel()">
<h3>getPanel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.DiagramWindowPanel</span> <span class="element-name">getPanel</span>()</div>
<div class="block">Returns the panel on which diagram is drawn.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the diagram drawing panel.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpecificCursor()">
<h3>getSpecificCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">getSpecificCursor</span>()</div>
<div class="block">Returns cursor of the tree</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getSpecificCursor</code> in interface <code>com.nomagic.ui.CursorOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpecificCursor(java.awt.Cursor)">
<h3>setSpecificCursor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSpecificCursor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a> c)</span></div>
<div class="block">Sets cursor for documentation and tree</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setSpecificCursor</code> in interface <code>com.nomagic.ui.CursorOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentCursor()">
<h3>getCurrentCursor</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">getCurrentCursor</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getCurrentCursor</code> in interface <code>com.nomagic.ui.CursorOwner</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVisible()">
<h3>isVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVisible</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isVisible</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createToolbars(java.util.Map)">
<h3>createToolbars</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createToolbars</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; options)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow</code></span></div>
<div class="block">Created some toolbars using given options</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>createToolbars</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>options</code> - toolbar options</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnableLoadOnActivation()">
<h3>isEnableLoadOnActivation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnableLoadOnActivation</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isEnableLoadOnActivation</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
<dt>Returns:</dt>
<dd>true if diagram should load content on activation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnableLoadOnActivation(boolean)">
<h3>setEnableLoadOnActivation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnableLoadOnActivation</span><wbr/><span class="parameters">(boolean enableLoadOnActivation)</span></div>
<div class="block">Set load content on activation state</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setEnableLoadOnActivation</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>enableLoadOnActivation</code> - true if diagram should load content on activation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="activate()">
<h3>activate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">activate</span>()</div>
<div class="block">Activate window - load diagram content if needed.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>activate</code> in interface <code>com.nomagic.magicdraw.ui.Activatable</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="storeOptions()">
<h3>storeOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">storeOptions</span>()</div>
<div class="block">Remembers all view options/parameters upon close,
 so it's state could be restored when the diagram is opened again.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>storeOptions</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="restoreOptions()">
<h3>restoreOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">restoreOptions</span>()</div>
<div class="block">Restore window state from diagram view options</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>restoreOptions</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.ui.Activatable</code></span></div>
<div class="block">Project of activatable component</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getProject</code> in interface <code>com.nomagic.magicdraw.ui.Activatable</code></dd>
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleForHiDPI()">
<h3>scaleForHiDPI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">scaleForHiDPI</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../ui/HiDPIScalableComponent.html#scaleForHiDPI()">scaleForHiDPI</a></code> in interface <code><a href="../../ui/HiDPIScalableComponent.html" title="interface in com.nomagic.ui">HiDPIScalableComponent</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executeWithLockedRepaint(java.lang.Runnable,com.nomagic.magicdraw.ui.DiagramWindowPanel)">
<h3>executeWithLockedRepaint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">executeWithLockedRepaint</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> run,
 @CheckForNull
 com.nomagic.magicdraw.ui.DiagramWindowPanel diagramWindowPanel)</span></div>
<div class="block">Executes given runnable while not repainting a diagram window panel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>run</code> - runnable to execute</dd>
<dd><code>diagramWindowPanel</code> - diagram window panel which must be repainted after this runnable completing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openDocument()">
<h3>openDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">openDocument</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>openDocument</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocument()">
<h3>getDocument</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getDocument</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getDocument</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocumentComponent()">
<h3>getDocumentComponent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.jidesoft.document.DocumentComponent</span> <span class="element-name">getDocumentComponent</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getDocumentComponent</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="activateDocument(com.nomagic.magicdraw.ui.editorwindows.EditorWindow,boolean)">
<h3>activateDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">activateDocument</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.ui.editorwindows.EditorWindow old,
 boolean activationTrackingEnabled)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>activateDocument</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deactivateDocument()">
<h3>deactivateDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deactivateDocument</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>deactivateDocument</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWindowActivationTime()">
<h3>getWindowActivationTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getWindowActivationTime</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getWindowActivationTime</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="repaintWindow()">
<h3>repaintWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">repaintWindow</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>repaintWindow</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseBufferImage()">
<h3>isUseBufferImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseBufferImage</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>isUseBufferImage</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="useBufferImage(boolean)">
<h3>useBufferImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">useBufferImage</span><wbr/><span class="parameters">(boolean use)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>useBufferImage</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.dassault_systemes.modeler.magic.ui.editorwindow.EditorWindowOptions</span> <span class="element-name">getOptions</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getOptions</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getID(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> document)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getID</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createContainer(com.jidesoft.document.DocumentPane,com.nomagic.magicdraw.ui.ProgressBarEditorWindowZoomToolbar,com.nomagic.magicdraw.ui.presentationmode.ProgressBarEditorWindowPresentationModeToolbar)">
<h3>createContainer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createContainer</span><wbr/><span class="parameters">(com.jidesoft.document.DocumentPane documentPane,
 com.nomagic.magicdraw.ui.ProgressBarEditorWindowZoomToolbar zoomToolbar,
 com.nomagic.magicdraw.ui.presentationmode.ProgressBarEditorWindowPresentationModeToolbar presentationModeToolbar)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>createContainer</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFireEvents(boolean)">
<h3>setFireEvents</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFireEvents</span><wbr/><span class="parameters">(boolean fireEvents)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>setFireEvents</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="customizePopupMenu(javax.swing.JPopupMenu)">
<h3>customizePopupMenu</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">customizePopupMenu</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> popupMenu)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>customizePopupMenu</code> in class <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow&lt;<a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt;</code></dd>
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
