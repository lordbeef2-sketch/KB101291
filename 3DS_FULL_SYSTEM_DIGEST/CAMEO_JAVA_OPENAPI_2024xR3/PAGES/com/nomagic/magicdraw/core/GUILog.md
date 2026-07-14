# JAVA OPENAPI: GUILog (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/GUILog.html
- source_path: `com/nomagic/magicdraw/core/GUILog.html`
- source_sha256: `82bf8c6d87d2085a41798611564eb35fc84e6c6d5ff82e8de045795ccd14f23a`
- captured_utc: `2026-07-14T16:55:12.338976+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Class GUILog

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.GUILog

@OpenApiAllpublic classGUILog
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Utility class for displaying messages, questions, warnings and dialogs. It also used to output some text into Message Window.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[GUILog.DefaultURLActionHandler](GUILog.DefaultURLActionHandler.html)`
Default implementation for URLActionHandler
`static interface`
`[GUILog.URLActionHandler](GUILog.URLActionHandler.html)`
An URL handler
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[GUILog](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[addHyperlinkedText](#addHyperlinkedText(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)> callbacks)`
Display text with hyperlinks.
`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)>`
`[addURLCallBack](#addURLCallBack(java.util.Map,java.lang.String,java.lang.String))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)> map,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href)`
Adds callback to open href to the map.
`void`
`[clearLog](#clearLog())()`
Clear message window.
`void`
`[clearMessageWindow](#clearMessageWindow())()`
Clear message window.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createActionURL](#createActionURL(com.nomagic.actions.NMAction))([NMAction](../../actions/NMAction.html) action)`
A utility method to create URL to some action.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createActionURLWithText](#createActionURLWithText(com.nomagic.actions.NMAction))([NMAction](../../actions/NMAction.html) action)`
A utility method to create URL to some action with
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createActionURLWithText](#createActionURLWithText(com.nomagic.actions.NMAction,java.lang.String))([NMAction](../../actions/NMAction.html) action,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
A utility method to create URL to some action with
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLoggedMessages](#getLoggedMessages())()`
A utility method get all logged messages
 (This GUILog class provides a method to get the LogDialog, but the LogDialog is not part of the OpenAPI
 and therefore not accessible by code that will want to use it.)
`void`
`[log](#log(com.nomagic.magicdraw.ui.notification.Notification,boolean))([Notification](../ui/notification/Notification.html) notification,
 boolean openWindow)`
Logs notification
`void`
`[log](#log(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Writes message to message window.
`void`
`[log](#log(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean open)`
Writes message to log window.
`void`
`[logNotification](#logNotification(java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [NotificationSeverity](../ui/notification/NotificationSeverity.html) severity,
 [Notification.Context](../ui/notification/Notification.Context.html) context)`
Logs notification
`void`
`[logNotification](#logNotification(java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [HRefRunnable](../ui/notification/HRefRunnable.html)[] actions,
 [NotificationSeverity](../ui/notification/NotificationSeverity.html) severity,
 [Notification.Context](../ui/notification/Notification.Context.html) context)`
Logs notification
`void`
`[logNotification](#logNotification(java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [NotificationSeverity](../ui/notification/NotificationSeverity.html) severity,
 [Notification.Context](../ui/notification/Notification.Context.html) context)`
Logs notification
`void`
`[openLog](#openLog())()`
Opens message window.
`void`
`[openMessageWindow](#openMessageWindow())()`
Opens message window.
`boolean`
`[showCustomizedQuestion](#showCustomizedQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)`
Show customized Cancel/Ok question in a model dialog
`void`
`[showError](#showError(java.awt.Dialog,java.lang.String))([Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Method shows Error dialog.
`void`
`[showError](#showError(java.awt.Dialog,java.lang.String,java.lang.Throwable))([Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)`
Method shows Error and stack trace dialog
`void`
`[showError](#showError(java.awt.Frame,java.lang.String))([Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Method shows Error dialog.
`void`
`[showError](#showError(java.awt.Frame,java.lang.String,java.lang.String))([Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`
Shows error dialog
`void`
`[showError](#showError(java.awt.Frame,java.lang.String,java.lang.Throwable))([Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)`
Method shows Error and stack trace dialog.
`void`
`[showError](#showError(java.awt.Window,java.lang.String))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Method shows Error dialog.
`void`
`[showError](#showError(java.awt.Window,java.lang.String,java.lang.String))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`
Shows error dialog
`void`
`[showError](#showError(java.awt.Window,java.lang.String,java.lang.Throwable))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)`
Method shows Error and stack trace dialog.
`void`
`[showError](#showError(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the error dialog with given message
`void`
`[showError](#showError(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`
Shows the error dialog with given message and title
`void`
`[showError](#showError(java.lang.String,java.lang.Throwable))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)`
Method shows Error and stack trace dialog
`void`
`[showErrorWithHelp](#showErrorWithHelp(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)`
Shows the error dialog with given message.
`int`
`[showErrorWithRetry](#showErrorWithRetry(java.lang.String,java.lang.String,java.lang.Throwable))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exp)`
Method shows Error and stack trace dialog with Submit, Export, Cancel and
 Retry buttons.
`int`
`[showErrorWithRetryButtonAsTheDefault](#showErrorWithRetryButtonAsTheDefault(java.lang.String,java.lang.String,java.lang.Throwable))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exp)`
Method shows Error and stack trace dialog with the `Retry`
 button being the default and the first one in the array of buttons.
`void`
`[showHTMLError](#showHTMLError(java.awt.Frame,java.lang.String,java.lang.Throwable))([Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)`
Method shows Error as html text and stack trace dialog
`void`
`[showHTMLError](#showHTMLError(java.awt.Window,java.lang.String,java.lang.Throwable))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)`
Method shows Error as html text and stack trace dialog
`void`
`[showHTMLError](#showHTMLError(java.lang.String,java.lang.Throwable))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)`
Method shows Error as html text and stack trace dialog
`void`
`[showHTMLMessage](#showHTMLMessage(java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [GUILog.URLActionHandler](GUILog.URLActionHandler.html) handler)`
Shows the message dialog with given message.
`void`
`[showHTMLMessage](#showHTMLMessage(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 [GUILog.URLActionHandler](GUILog.URLActionHandler.html) handler)`
Shows the message dialog with given message.
`void`
`[showHTMLMessage](#showHTMLMessage(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 [GUILog.URLActionHandler](GUILog.URLActionHandler.html) handler)`
Shows the message dialog with given message.
`void`
`[showHTMLMessage](#showHTMLMessage(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 [GUILog.URLActionHandler](GUILog.URLActionHandler.html) handler,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)`
Shows the message dialog with given message.
`int`
`[showHTMLQuestion](#showHTMLQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) yesLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) noLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)`
Shows html dialogs with given button text
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[showInputTextDialog](#showInputTextDialog(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Show dialog for text input.
`void`
`[showMessage](#showMessage(java.awt.Dialog,java.lang.String))([Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the message dialog with the given message.
`void`
`[showMessage](#showMessage(java.awt.Window,java.lang.String))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the message dialog with the given message.
`void`
`[showMessage](#showMessage(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the message dialog with given message.
`void`
`[showMessage](#showMessage(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)`
Shows the message dialog with the given message.
`boolean`
`[showMessage](#showMessage(java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) checkBoxMsg,
 boolean checkBoxValue)`
Shows the message dialog with given message.
`void`
`[showMessage](#showMessage(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)`
Shows the message dialog with given message.
`void`
`[showMessage](#showMessage(java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)`
Shows the message dialog with given message.
`void`
`[showMessageWithShowNextTime](#showMessageWithShowNextTime(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyId)`
Shows the message dialog with given message and with label to show next time.
`void`
`[showOutOfMemoryError](#showOutOfMemoryError(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Display out of memory error.
`boolean`
`[showQuestion](#showQuestion(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the yes-no dialog with given message.
`int`
`[showQuestion](#showQuestion(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean cancel)`
Shows the yes-no dialog with given message.
`int`
`[showQuestion](#showQuestion(java.lang.String,boolean,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean cancel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dialogTitle)`
Shows the yes-no dialog with given message.
`int`
`[showQuestion](#showQuestion(java.lang.String,boolean,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean cancel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dialogTitle,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) defaultAction)`
Shows the yes-no dialog with given message.
`boolean`
`[showQuestion](#showQuestion(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)`
Shows the yes-no-help dialog with given message.
`int`
`[showQuestion](#showQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) yesLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) noLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)`
Shows dialogs with given button text
`int`
`[showQuestion](#showQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) yesLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) noLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)`
Shows dialogs with given button text
`int`
`[showQuestionForAll](#showQuestionForAll(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the yes-no-all dialog with given message.
`int`
`[showQuestionForAll](#showQuestionForAll(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean cancel)`
Shows the yes-no-all dialog with given message.
`int`
`[showQuestionForAll](#showQuestionForAll(java.lang.String,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean yesToAll,
 boolean cancel)`
Shows the yes-no-all dialog with given message.
`boolean`
`[showQuestionOkCancel](#showQuestionOkCancel(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the ok-cancel dialog with given message.
`boolean`
`[showQuestionWithHelp](#showQuestionWithHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)`
Show customized Ok/Cancel/Help question in a modal dialog.
`boolean`
`[showQuestionWithHelp](#showQuestionWithHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) notificationMsg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)`
Show customized Ok/Cancel/Help question in a modal dialog.
`int`
`[showRetryQuestion](#showRetryQuestion(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the yes-no dialog with given message
`void`
`[showWarning](#showWarning(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Shows the warning dialog with given message.
`void`
`[showWarning](#showWarning(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`
Shows the warning dialog with given message and title.
`boolean`
`[showWarning](#showWarning(java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) checkBoxMsg,
 boolean checkBoxValue)`
Shows the warning dialog with given message.
`void`
`[showWarning](#showWarning(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey)`
Shows the warning dialog with given message, title and button.
`boolean`
`[showWarningQuestion](#showWarningQuestion(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`
Show customized Cancel/Ok question in a modal dialog.
`boolean`
`[showWarningQuestion](#showWarningQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)`
Show customized Cancel/Ok question in a model dialog
`boolean`
`[showYesNoHelp](#showYesNoHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)`
Shows the yes-no-help dialog with given message.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[wrapForHeyperlinkText](#wrapForHeyperlinkText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Deprecated.
Misspelled - use [`wrapForHyperlinkText(String)`](#wrapForHyperlinkText(java.lang.String))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[wrapForHyperlinkText](#wrapForHyperlinkText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str)`
Helper method to wrap given string into string suitable to use for hyperlinked log.
`void`
`[writeLogText](#writeLogText(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean open)`
Writes message to log window.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
GUILog
protected GUILog()
 ============ METHOD DETAIL ========== 
Method Details
showError
public void showError(@CheckForNull
 [Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Method shows Error dialog.
Parameters:
`parent` - parent of error dialog
`message` - Error message
showError
public void showError(@CheckForNull
 [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Method shows Error dialog.
Parameters:
`parent` - parent of error dialog
`message` - Error message
showError
public void showError(@CheckForNull
 [Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Method shows Error dialog.
Parameters:
`parent` - parent of error dialog
`message` - Error message
showError
public void showError(@CheckForNull
 [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
Shows error dialog
Parameters:
`parent` - the parent of error dialog
`message` - the error message
`title` - the dialog title
showError
public void showError(@CheckForNull
 [Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
Shows error dialog
Parameters:
`parent` - the parent of error dialog
`message` - the error message
`title` - the dialog title
showError
public void showError(@CheckForNull
 [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)
Method shows Error and stack trace dialog.
Parameters:
`parent` - parent of error dialog
`message` - error message
`throwable` - throwable provides stack trace to display
showError
public void showError([Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)
Method shows Error and stack trace dialog
Parameters:
`parent` - parent of error dialog
`message` - error message
`throwable` - throwable provides stack trace to display
showError
public void showError(@CheckForNull
 [Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)
Method shows Error and stack trace dialog.
Parameters:
`parent` - parent of error dialog
`message` - error message
`throwable` - throwable provides stack trace to display
showError
public void showError([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the error dialog with given message
Parameters:
`message` - error message
showError
public void showError([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
Shows the error dialog with given message and title
Parameters:
`message` - error message
`title` - the dialog title
showError
public void showError([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)
Method shows Error and stack trace dialog
Parameters:
`message` - error message.
`throwable` - throwable provides stack trace to display
showHTMLError
public void showHTMLError([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)
Method shows Error as html text and stack trace dialog
Parameters:
`message` - error message
`throwable` - throwable provides stack trace to display
showHTMLError
public void showHTMLError(@CheckForNull
 [Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)
Method shows Error as html text and stack trace dialog
Parameters:
`parent` - parent of error dialog
`message` - error message
`throwable` - throwable provides stack trace to display
showHTMLError
public void showHTMLError(@CheckForNull
 [Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) throwable)
Method shows Error as html text and stack trace dialog
Parameters:
`parent` - parent of error dialog
`message` - error message
`throwable` - throwable provides stack trace to display
showErrorWithRetry
public int showErrorWithRetry([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exp)
Method shows Error and stack trace dialog with Submit, Export, Cancel and
 Retry buttons. If Retry button is pressed then method returns
 `DialogConstants.OK`, if Cancel - `DialogConstants.CANCEL`.
Parameters:
`message` - error message
`title` - dialog title
`exp` - throwable provides stack trace to display
Returns:
pressed button identifier
showErrorWithRetryButtonAsTheDefault
public int showErrorWithRetryButtonAsTheDefault([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) exp)
Method shows Error and stack trace dialog with the `Retry`
 button being the default and the first one in the array of buttons.
 If `Retry` button is pressed then method returns
 `DialogConstants.OK`, if `Cancel` - `DialogConstants.CANCEL`.
Parameters:
`message` - error message
`title` - dialog title
`exp` - stack trace to display
Returns:
pressed button identifier
showMessage
public void showMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the message dialog with given message.
Parameters:
`message` - message text
showHTMLMessage
public void showHTMLMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [GUILog.URLActionHandler](GUILog.URLActionHandler.html) handler)
Shows the message dialog with given message.
Parameters:
`message` - message text
`handler` - handler
showMessage
public void showMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)
Shows the message dialog with the given message.
Parameters:
`message` - message text
`helpID` - help item ID in help system
showHTMLMessage
public void showHTMLMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 @CheckForNull
 [GUILog.URLActionHandler](GUILog.URLActionHandler.html) handler)
Shows the message dialog with given message.
Parameters:
`message` - message text.
`helpID` - help item ID in help system
`handler` - handler
showMessage
public void showMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)
Shows the message dialog with given message.
Parameters:
`message` - message text
`title` - title of the dialog
`helpID` - help item ID in help system
`icon` - path to icon image (for example "/com/company/icon.gif")
showMessage
public void showMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)
Shows the message dialog with given message.
Parameters:
`message` - message text
`title` - title of the dialog
`helpID` - help item ID in help system
showHTMLMessage
public void showHTMLMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 @CheckForNull
 [GUILog.URLActionHandler](GUILog.URLActionHandler.html) handler)
Shows the message dialog with given message.
Parameters:
`message` - message text.
`title` - title of the dialog.
`helpID` - help item ID in help system
`handler` - url action handler
showHTMLMessage
public void showHTMLMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 @CheckForNull
 [GUILog.URLActionHandler](GUILog.URLActionHandler.html) handler,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)
Shows the message dialog with given message.
Parameters:
`message` - message text
`title` - title of the dialog
`helpID` - help item ID in help system
`handler` - url action handler
`icon` - path to icon image (for example "/com/company/icon.gif")
showMessage
public boolean showMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) checkBoxMsg,
 boolean checkBoxValue)
Shows the message dialog with given message. Shows another message with a checkbox before like "Show next time" option.
Parameters:
`message` - message text.
`checkBoxMsg` - check box message
`checkBoxValue` - check box state
Returns:
check box state
showMessage
public void showMessage([Dialog](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the message dialog with the given message.
Parameters:
`parent` - dialog parent
`message` - message text
showMessage
public void showMessage([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) parent,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the message dialog with the given message.
Parameters:
`parent` - dialog parent
`message` - message text
showMessageWithShowNextTime
public void showMessageWithShowNextTime([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyId)
Shows the message dialog with given message and with label to show next time.
Parameters:
`message` - message text
`propertyId` - **registered** invisible property id in the GeneralOptions with default value true
See Also:
`GeneralOptionsGroup`
showQuestion
public boolean showQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the yes-no dialog with given message.
Parameters:
`message` - message of question.
Returns:
true if answer was yes.
showQuestion
public int showQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean cancel)
Shows the yes-no dialog with given message.
Parameters:
`cancel` - true if cancel button needed
`message` - message of question.
Returns:
result constant form DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showInputTextDialog
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) showInputTextDialog([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Show dialog for text input.
Parameters:
`title` - dialog title.
`message` - message to show in dialog.
Returns:
entered text.
showQuestion
public int showQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean cancel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dialogTitle)
Shows the yes-no dialog with given message.
Parameters:
`cancel` - true if cancel button needed.
`message` - message of question.
`dialogTitle` - title of the dialog.
Returns:
result constant form DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showQuestion
public int showQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean cancel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dialogTitle,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) defaultAction)
Shows the yes-no dialog with given message.
Parameters:
`cancel` - true if cancel button needed.
`message` - message of question.
`dialogTitle` - title of the dialog.
`defaultAction` - default selected action (button) in the question dialog.
Returns:
result constant form DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showQuestion
public int showQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) yesLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) noLabel,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)
Shows dialogs with given button text
Parameters:
`message` - message of question.
`yesLabel` - label key in dialog resources used instead of "Yes" text.
`noLabel` - label key in dialog resources used instead of "No" text.
`cancelLabel` - label key in dialog resources used instead of "Cancel" text, can be null.
`icon` - path to icon image (for example "/com/company/icon.gif")
Returns:
result constant form DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showQuestion
public int showQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) yesLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) noLabel,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)
Shows dialogs with given button text
Parameters:
`message` - message of question.
`yesLabel` - label key in dialog resources used instead of "Yes" text.
`noLabel` - label key in dialog resources used instead of "No" text.
`cancelLabel` - label key in dialog resources used instead of "Cancel" text, can be null.
`title` - title of the dialog.
`icon` - path to icon image (for example "/com/company/icon.gif")
Returns:
result constant form DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showHTMLQuestion
public int showHTMLQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) yesLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) noLabel,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabel,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)
Shows html dialogs with given button text
Parameters:
`message` - message of question.
`yesLabel` - label key in dialog resources used instead of "Yes" text.
`noLabel` - label key in dialog resources used instead of "No" text.
`cancelLabel` - label key in dialog resources used instead of "Cancel" text, can be null.
`title` - title of the dialog.
`icon` - path to icon image (for example "/com/company/icon.gif")
Returns:
result constant form DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showQuestionOkCancel
public boolean showQuestionOkCancel([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the ok-cancel dialog with given message.
Parameters:
`message` - message of question.
Returns:
result constant form DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showQuestion
public boolean showQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)
Shows the yes-no-help dialog with given message.
Parameters:
`message` - message of question.
`helpID` - help item ID in help system
Returns:
true if answer was yes.
showYesNoHelp
public boolean showYesNoHelp([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)
Shows the yes-no-help dialog with given message.
Parameters:
`message` - message of question.
`helpID` - help item ID in help system
`title` - title
`icon` - path to icon image (for example "/com/company/icon.gif")
Returns:
true if answer was yes.
showQuestionForAll
public int showQuestionForAll([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the yes-no-all dialog with given message.
Parameters:
`message` - message text.
Returns:
result constant form DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showQuestionForAll
public int showQuestionForAll([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean cancel)
Shows the yes-no-all dialog with given message.
Parameters:
`message` - message
`cancel` - true if cancel button needed
Returns:
one of the result constants in DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showQuestionForAll
public int showQuestionForAll([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean yesToAll,
 boolean cancel)
Shows the yes-no-all dialog with given message.
Parameters:
`message` - message
`yesToAll` - true if Yes to ALL button needed
`cancel` - true if cancel button needed
Returns:
one of the result constants in DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showRetryQuestion
public int showRetryQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the yes-no dialog with given message
Parameters:
`message` - Message Text
Returns:
one of the result constants in DialogConstants.
See Also:
[`DialogConstants`](../../ui/DialogConstants.html)
showWarning
public void showWarning([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Shows the warning dialog with given message.
Parameters:
`message` - warning text.
showWarning
public void showWarning([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
Shows the warning dialog with given message and title.
Parameters:
`message` - warning text.
`title` - warning title
showWarning
public void showWarning([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey)
Shows the warning dialog with given message, title and button.
Parameters:
`message` - warning text.
`title` - warning title
`okLabelKey` - button label
showWarning
public boolean showWarning([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) checkBoxMsg,
 boolean checkBoxValue)
Shows the warning dialog with given message. Shows another message with a checkbox before like "Show next time" option.
Parameters:
`message` - message text.
`checkBoxMsg` - check box message
`checkBoxValue` - check box state
Returns:
check box state
log
public void log([Notification](../ui/notification/Notification.html) notification,
 boolean openWindow)
Logs notification
Parameters:
`notification` - notification
`openWindow` - flag, if true opens notification window
logNotification
public void logNotification(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [NotificationSeverity](../ui/notification/NotificationSeverity.html) severity,
 [Notification.Context](../ui/notification/Notification.Context.html) context)
Logs notification
Parameters:
`text` - notification text
`severity` - notification severity
`context` - notification context
logNotification
public void logNotification(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [NotificationSeverity](../ui/notification/NotificationSeverity.html) severity,
 [Notification.Context](../ui/notification/Notification.Context.html) context)
Logs notification
Parameters:
`title` - notification title
`text` - notification text
`severity` - notification severity
`context` - notification context
logNotification
public void logNotification(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 @CheckForNull
 [HRefRunnable](../ui/notification/HRefRunnable.html)[] actions,
 [NotificationSeverity](../ui/notification/NotificationSeverity.html) severity,
 [Notification.Context](../ui/notification/Notification.Context.html) context)
Logs notification
Parameters:
`title` - notification title
`text` - notification text
`severity` - notification severity
`actions` - list of actions
`context` - notification context
openMessageWindow
public void openMessageWindow()
Opens message window.
openLog
public void openLog()
Opens message window.
clearLog
public void clearLog()
Clear message window.
clearMessageWindow
public void clearMessageWindow()
Clear message window.
log
public void log([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Writes message to message window.
Parameters:
`message` - message text.
log
public void log([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean open)
Writes message to log window.
Parameters:
`message` - message text.
`open` - true if closed window should be reopened.
writeLogText
public void writeLogText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 boolean open)
Writes message to log window.
Parameters:
`message` - message text.
`open` - true if closed window should be reopened.
showOutOfMemoryError
public void showOutOfMemoryError([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Display out of memory error.
Parameters:
`message` - message
showErrorWithHelp
public void showErrorWithHelp([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)
Shows the error dialog with given message.
Parameters:
`message` - message text
`helpID` - help item ID in help system
addHyperlinkedText
public void addHyperlinkedText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)> callbacks)
Display text with hyperlinks. Each hyperlink must have entry in callback.
 Hyperlink in the text must be surrounded by <A> </A> tags. Callback is taken from the parameter callbacks using hyperlink text as key.
Parameters:
`text` - text with hyperlinks for example "Best modeling <A>hyperlink text to display</A> tool." text can contain any number of href.
`callbacks` - map where is mapped hyperlinked text to the callback runnable. Map must contain String key and Runnable value.
See Also:
[`wrapForHyperlinkText(String)`](#wrapForHyperlinkText(java.lang.String))
wrapForHyperlinkText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) wrapForHyperlinkText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str)
Helper method to wrap given string into string suitable to use for hyperlinked log.
 Simply wrap with <A></A> tags
Parameters:
`str` - target string for hyperlink
Returns:
string wrapped into <A></A>
See Also:
[`addHyperlinkedText(String, java.util.Map)`](#addHyperlinkedText(java.lang.String,java.util.Map))
wrapForHeyperlinkText
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) wrapForHeyperlinkText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Deprecated.
Misspelled - use [`wrapForHyperlinkText(String)`](#wrapForHyperlinkText(java.lang.String))
Wrap text for hyperlink
Parameters:
`text` - text to wrap
Returns:
wrapped text
addURLCallBack
public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)> addURLCallBack(@CheckForNull
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html)> map,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) href)
Adds callback to open href to the map. call back is used in [`addHyperlinkedText(String, Map)`](#addHyperlinkedText(java.lang.String,java.util.Map))
Parameters:
`map` - map to which callback is
`string` - text fragment which is hyperlinked
`href` - reference
Returns:
map with url call backs
createActionURL
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createActionURL(@Nonnull
 [NMAction](../../actions/NMAction.html) action)
A utility method to create URL to some action.
Parameters:
`action` - action
Returns:
url to this action
createActionURLWithText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createActionURLWithText([NMAction](../../actions/NMAction.html) action)
A utility method to create URL to some action with
Parameters:
`action` - action
Returns:
url to this action
createActionURLWithText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createActionURLWithText([NMAction](../../actions/NMAction.html) action,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
A utility method to create URL to some action with
Parameters:
`action` - action
`text` - url text
Returns:
url to this action
getLoggedMessages
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLoggedMessages()
A utility method get all logged messages
 (This GUILog class provides a method to get the LogDialog, but the LogDialog is not part of the OpenAPI
 and therefore not accessible by code that will want to use it.)
Returns:
the messages visible in the LogDialog
showQuestionWithHelp
public boolean showQuestionWithHelp([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) notificationMsg,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)
Show customized Ok/Cancel/Help question in a modal dialog.
Parameters:
`message` - message to show
`notificationMsg` - notification message to show if silent mode is on
`okLabelKey` - label key in DialogResource.properties for the Ok button
`title` - dialog title
`helpID` - help item ID in help system
Returns:
true - if Ok was pressed, false - if canceled.
showQuestionWithHelp
public boolean showQuestionWithHelp([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) helpID)
Show customized Ok/Cancel/Help question in a modal dialog.
Parameters:
`message` - message to show
`okLabelKey` - label key in DialogResource.properties for the Ok button
`title` - dialog title
`helpID` - help item ID in help system
Returns:
true - if Ok was pressed, false - if canceled.
showWarningQuestion
public boolean showWarningQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
Show customized Cancel/Ok question in a modal dialog.
Parameters:
`message` - message to show
`okLabelKey` - label key in DialogResource.properties for the Ok button
`title` - dialog title
Returns:
true - if Ok was pressed, false - if canceled.
showWarningQuestion
public boolean showWarningQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title)
Show customized Cancel/Ok question in a model dialog
Parameters:
`message` - the message to show
`okLabelKey` - the label key in DialogResource.properties for the Ok button
`cancelLabelKey` - the label key in DialogResource.properties for the Cancel
 button
`title` - the dialog title
Returns:
`true` if Ok was pressed, `false` otherwise
showCustomizedQuestion
public boolean showCustomizedQuestion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) okLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cancelLabelKey,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) title,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) icon)
Show customized Cancel/Ok question in a model dialog
Parameters:
`message` - the message to show
`okLabelKey` - the label key in DialogResource.properties for the Ok button
`cancelLabelKey` - the label key in DialogResource.properties for the Cancel
 button
`title` - the dialog title
`icon` - the dialog icon
Returns:
`true` if Ok was pressed, `false` otherwise

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Class GUILog">Class GUILog</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.GUILog</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">GUILog</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class for displaying messages, questions, warnings and dialogs. It also used to output some text into Message Window.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="GUILog.DefaultURLActionHandler.html" title="class in com.nomagic.magicdraw.core">GUILog.DefaultURLActionHandler</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default implementation for URLActionHandler</div>
</div>
<div class="col-first odd-row-color"><code>static interface </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An URL handler</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">GUILog</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addHyperlinkedText(java.lang.String,java.util.Map)">addHyperlinkedText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; callbacks)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display text with hyperlinks.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addURLCallBack(java.util.Map,java.lang.String,java.lang.String)">addURLCallBack</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; map,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds callback to open href to the map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearLog()">clearLog</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear message window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearMessageWindow()">clearMessageWindow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear message window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionURL(com.nomagic.actions.NMAction)">createActionURL</a><wbr/>(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">A utility method to create URL to some action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionURLWithText(com.nomagic.actions.NMAction)">createActionURLWithText</a><wbr/>(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">A utility method to create URL to some action with</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createActionURLWithText(com.nomagic.actions.NMAction,java.lang.String)">createActionURLWithText</a><wbr/>(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">A utility method to create URL to some action with</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoggedMessages()">getLoggedMessages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A utility method get all logged messages
 (This GUILog class provides a method to get the LogDialog, but the LogDialog is not part of the OpenAPI
 and therefore not accessible by code that will want to use it.)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#log(com.nomagic.magicdraw.ui.notification.Notification,boolean)">log</a><wbr/>(<a href="../ui/notification/Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 boolean openWindow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Logs notification</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#log(java.lang.String)">log</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Writes message to message window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#log(java.lang.String,boolean)">log</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean open)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Writes message to log window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#logNotification(java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">logNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../ui/notification/NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="../ui/notification/Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Logs notification</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#logNotification(java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable%5B%5D,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">logNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../ui/notification/HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="../ui/notification/NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="../ui/notification/Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Logs notification</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#logNotification(java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">logNotification</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../ui/notification/NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="../ui/notification/Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Logs notification</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openLog()">openLog</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens message window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openMessageWindow()">openMessageWindow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens message window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showCustomizedQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showCustomizedQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show customized Cancel/Ok question in a model dialog</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.awt.Dialog,java.lang.String)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error dialog.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.awt.Dialog,java.lang.String,java.lang.Throwable)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error and stack trace dialog</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.awt.Frame,java.lang.String)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error dialog.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.awt.Frame,java.lang.String,java.lang.String)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows error dialog</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.awt.Frame,java.lang.String,java.lang.Throwable)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error and stack trace dialog.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.awt.Window,java.lang.String)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error dialog.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.awt.Window,java.lang.String,java.lang.String)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows error dialog</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.awt.Window,java.lang.String,java.lang.Throwable)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error and stack trace dialog.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.lang.String)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the error dialog with given message</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.lang.String,java.lang.String)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the error dialog with given message and title</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showError(java.lang.String,java.lang.Throwable)">showError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error and stack trace dialog</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showErrorWithHelp(java.lang.String,java.lang.String)">showErrorWithHelp</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the error dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showErrorWithRetry(java.lang.String,java.lang.String,java.lang.Throwable)">showErrorWithRetry</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exp)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error and stack trace dialog with Submit, Export, Cancel and
 Retry buttons.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showErrorWithRetryButtonAsTheDefault(java.lang.String,java.lang.String,java.lang.Throwable)">showErrorWithRetryButtonAsTheDefault</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exp)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error and stack trace dialog with the <code>Retry</code>
 button being the default and the first one in the array of buttons.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showHTMLError(java.awt.Frame,java.lang.String,java.lang.Throwable)">showHTMLError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error as html text and stack trace dialog</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showHTMLError(java.awt.Window,java.lang.String,java.lang.Throwable)">showHTMLError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error as html text and stack trace dialog</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showHTMLError(java.lang.String,java.lang.Throwable)">showHTMLError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method shows Error as html text and stack trace dialog</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showHTMLMessage(java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler)">showHTMLMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a> handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showHTMLMessage(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler)">showHTMLMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a> handler)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showHTMLMessage(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler)">showHTMLMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a> handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showHTMLMessage(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler,java.lang.String)">showHTMLMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a> handler,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showHTMLQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showHTMLQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> yesLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows html dialogs with given button text</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#showInputTextDialog(java.lang.String,java.lang.String)">showInputTextDialog</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Show dialog for text input.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMessage(java.awt.Dialog,java.lang.String)">showMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with the given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMessage(java.awt.Window,java.lang.String)">showMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with the given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMessage(java.lang.String)">showMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMessage(java.lang.String,java.lang.String)">showMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with the given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMessage(java.lang.String,java.lang.String,boolean)">showMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> checkBoxMsg,
 boolean checkBoxValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMessage(java.lang.String,java.lang.String,java.lang.String)">showMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMessage(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showMessageWithShowNextTime(java.lang.String,java.lang.String)">showMessageWithShowNextTime</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the message dialog with given message and with label to show next time.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showOutOfMemoryError(java.lang.String)">showOutOfMemoryError</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Display out of memory error.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestion(java.lang.String)">showQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestion(java.lang.String,boolean)">showQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean cancel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestion(java.lang.String,boolean,java.lang.String)">showQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean cancel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dialogTitle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestion(java.lang.String,boolean,java.lang.String,java.lang.String)">showQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean cancel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dialogTitle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> defaultAction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestion(java.lang.String,java.lang.String)">showQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no-help dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> yesLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows dialogs with given button text</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> yesLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows dialogs with given button text</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestionForAll(java.lang.String)">showQuestionForAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no-all dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestionForAll(java.lang.String,boolean)">showQuestionForAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean cancel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no-all dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestionForAll(java.lang.String,boolean,boolean)">showQuestionForAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean yesToAll,
 boolean cancel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no-all dialog with given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestionOkCancel(java.lang.String)">showQuestionOkCancel</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the ok-cancel dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestionWithHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showQuestionWithHelp</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show customized Ok/Cancel/Help question in a modal dialog.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showQuestionWithHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showQuestionWithHelp</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationMsg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show customized Ok/Cancel/Help question in a modal dialog.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showRetryQuestion(java.lang.String)">showRetryQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no dialog with given message</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showWarning(java.lang.String)">showWarning</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the warning dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showWarning(java.lang.String,java.lang.String)">showWarning</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the warning dialog with given message and title.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showWarning(java.lang.String,java.lang.String,boolean)">showWarning</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> checkBoxMsg,
 boolean checkBoxValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the warning dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showWarning(java.lang.String,java.lang.String,java.lang.String)">showWarning</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the warning dialog with given message, title and button.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showWarningQuestion(java.lang.String,java.lang.String,java.lang.String)">showWarningQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show customized Cancel/Ok question in a modal dialog.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showWarningQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showWarningQuestion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Show customized Cancel/Ok question in a model dialog</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showYesNoHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">showYesNoHelp</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows the yes-no-help dialog with given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#wrapForHeyperlinkText(java.lang.String)">wrapForHeyperlinkText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Misspelled - use <a href="#wrapForHyperlinkText(java.lang.String)"><code>wrapForHyperlinkText(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#wrapForHyperlinkText(java.lang.String)">wrapForHyperlinkText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Helper method to wrap given string into string suitable to use for hyperlinked log.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeLogText(java.lang.String,boolean)">writeLogText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean open)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Writes message to log window.</div>
</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>GUILog</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">GUILog</span>()</div>
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
<section class="detail" id="showError(java.awt.Dialog,java.lang.String)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Method shows Error dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent of error dialog</dd>
<dd><code>message</code> - Error message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.awt.Frame,java.lang.String)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Method shows Error dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent of error dialog</dd>
<dd><code>message</code> - Error message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.awt.Window,java.lang.String)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Method shows Error dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent of error dialog</dd>
<dd><code>message</code> - Error message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.awt.Frame,java.lang.String,java.lang.String)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
<div class="block">Shows error dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent of error dialog</dd>
<dd><code>message</code> - the error message</dd>
<dd><code>title</code> - the dialog title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.awt.Window,java.lang.String,java.lang.String)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
<div class="block">Shows error dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - the parent of error dialog</dd>
<dd><code>message</code> - the error message</dd>
<dd><code>title</code> - the dialog title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.awt.Frame,java.lang.String,java.lang.Throwable)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</span></div>
<div class="block">Method shows Error and stack trace dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent of error dialog</dd>
<dd><code>message</code> - error message</dd>
<dd><code>throwable</code> - throwable provides stack trace to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.awt.Dialog,java.lang.String,java.lang.Throwable)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</span></div>
<div class="block">Method shows Error and stack trace dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent of error dialog</dd>
<dd><code>message</code> - error message</dd>
<dd><code>throwable</code> - throwable provides stack trace to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.awt.Window,java.lang.String,java.lang.Throwable)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</span></div>
<div class="block">Method shows Error and stack trace dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent of error dialog</dd>
<dd><code>message</code> - error message</dd>
<dd><code>throwable</code> - throwable provides stack trace to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.lang.String)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the error dialog with given message</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - error message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.lang.String,java.lang.String)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
<div class="block">Shows the error dialog with given message and title</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - error message</dd>
<dd><code>title</code> - the dialog title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showError(java.lang.String,java.lang.Throwable)">
<h3>showError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showError</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</span></div>
<div class="block">Method shows Error and stack trace dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - error message.</dd>
<dd><code>throwable</code> - throwable provides stack trace to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showHTMLError(java.lang.String,java.lang.Throwable)">
<h3>showHTMLError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showHTMLError</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</span></div>
<div class="block">Method shows Error as html text and stack trace dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - error message</dd>
<dd><code>throwable</code> - throwable provides stack trace to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showHTMLError(java.awt.Frame,java.lang.String,java.lang.Throwable)">
<h3>showHTMLError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showHTMLError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</span></div>
<div class="block">Method shows Error as html text and stack trace dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent of error dialog</dd>
<dd><code>message</code> - error message</dd>
<dd><code>throwable</code> - throwable provides stack trace to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showHTMLError(java.awt.Window,java.lang.String,java.lang.Throwable)">
<h3>showHTMLError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showHTMLError</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> throwable)</span></div>
<div class="block">Method shows Error as html text and stack trace dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent of error dialog</dd>
<dd><code>message</code> - error message</dd>
<dd><code>throwable</code> - throwable provides stack trace to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showErrorWithRetry(java.lang.String,java.lang.String,java.lang.Throwable)">
<h3>showErrorWithRetry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showErrorWithRetry</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exp)</span></div>
<div class="block">Method shows Error and stack trace dialog with Submit, Export, Cancel and
 Retry buttons. If Retry button is pressed then method returns
 <code>DialogConstants.OK</code>, if Cancel - <code>DialogConstants.CANCEL</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - error message</dd>
<dd><code>title</code> - dialog title</dd>
<dd><code>exp</code> - throwable provides stack trace to display</dd>
<dt>Returns:</dt>
<dd>pressed button identifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showErrorWithRetryButtonAsTheDefault(java.lang.String,java.lang.String,java.lang.Throwable)">
<h3>showErrorWithRetryButtonAsTheDefault</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showErrorWithRetryButtonAsTheDefault</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> exp)</span></div>
<div class="block">Method shows Error and stack trace dialog with the <code>Retry</code>
 button being the default and the first one in the array of buttons.
 If <code>Retry</code> button is pressed then method returns
 <code>DialogConstants.OK</code>, if <code>Cancel</code> - <code>DialogConstants.CANCEL</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - error message</dd>
<dd><code>title</code> - dialog title</dd>
<dd><code>exp</code> - stack trace to display</dd>
<dt>Returns:</dt>
<dd>pressed button identifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMessage(java.lang.String)">
<h3>showMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the message dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showHTMLMessage(java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler)">
<h3>showHTMLMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showHTMLMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a> handler)</span></div>
<div class="block">Shows the message dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text</dd>
<dd><code>handler</code> - handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMessage(java.lang.String,java.lang.String)">
<h3>showMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</span></div>
<div class="block">Shows the message dialog with the given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showHTMLMessage(java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler)">
<h3>showHTMLMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showHTMLMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 @CheckForNull
 <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a> handler)</span></div>
<div class="block">Shows the message dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text.</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
<dd><code>handler</code> - handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMessage(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</span></div>
<div class="block">Shows the message dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text</dd>
<dd><code>title</code> - title of the dialog</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
<dd><code>icon</code> - path to icon image (for example "/com/company/icon.gif")</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMessage(java.lang.String,java.lang.String,java.lang.String)">
<h3>showMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</span></div>
<div class="block">Shows the message dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text</dd>
<dd><code>title</code> - title of the dialog</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showHTMLMessage(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler)">
<h3>showHTMLMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showHTMLMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 @CheckForNull
 <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a> handler)</span></div>
<div class="block">Shows the message dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text.</dd>
<dd><code>title</code> - title of the dialog.</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
<dd><code>handler</code> - url action handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showHTMLMessage(java.lang.String,java.lang.String,java.lang.String,com.nomagic.magicdraw.core.GUILog.URLActionHandler,java.lang.String)">
<h3>showHTMLMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showHTMLMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 @CheckForNull
 <a href="GUILog.URLActionHandler.html" title="interface in com.nomagic.magicdraw.core">GUILog.URLActionHandler</a> handler,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</span></div>
<div class="block">Shows the message dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text</dd>
<dd><code>title</code> - title of the dialog</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
<dd><code>handler</code> - url action handler</dd>
<dd><code>icon</code> - path to icon image (for example "/com/company/icon.gif")</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMessage(java.lang.String,java.lang.String,boolean)">
<h3>showMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> checkBoxMsg,
 boolean checkBoxValue)</span></div>
<div class="block">Shows the message dialog with given message. Shows another message with a checkbox before like "Show next time" option.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text.</dd>
<dd><code>checkBoxMsg</code> - check box message</dd>
<dd><code>checkBoxValue</code> - check box state</dd>
<dt>Returns:</dt>
<dd>check box state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMessage(java.awt.Dialog,java.lang.String)">
<h3>showMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dialog.html" title="class or interface in java.awt">Dialog</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the message dialog with the given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - dialog parent</dd>
<dd><code>message</code> - message text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMessage(java.awt.Window,java.lang.String)">
<h3>showMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the message dialog with the given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - dialog parent</dd>
<dd><code>message</code> - message text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showMessageWithShowNextTime(java.lang.String,java.lang.String)">
<h3>showMessageWithShowNextTime</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showMessageWithShowNextTime</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyId)</span></div>
<div class="block">Shows the message dialog with given message and with label to show next time.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text</dd>
<dd><code>propertyId</code> - <strong>registered</strong> invisible property id in the GeneralOptions with default value true</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><code>GeneralOptionsGroup</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestion(java.lang.String)">
<h3>showQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the yes-no dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message of question.</dd>
<dt>Returns:</dt>
<dd>true if answer was yes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestion(java.lang.String,boolean)">
<h3>showQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean cancel)</span></div>
<div class="block">Shows the yes-no dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cancel</code> - true if cancel button needed</dd>
<dd><code>message</code> - message of question.</dd>
<dt>Returns:</dt>
<dd>result constant form DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showInputTextDialog(java.lang.String,java.lang.String)">
<h3>showInputTextDialog</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">showInputTextDialog</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Show dialog for text input.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>title</code> - dialog title.</dd>
<dd><code>message</code> - message to show in dialog.</dd>
<dt>Returns:</dt>
<dd>entered text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestion(java.lang.String,boolean,java.lang.String)">
<h3>showQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean cancel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dialogTitle)</span></div>
<div class="block">Shows the yes-no dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cancel</code> - true if cancel button needed.</dd>
<dd><code>message</code> - message of question.</dd>
<dd><code>dialogTitle</code> - title of the dialog.</dd>
<dt>Returns:</dt>
<dd>result constant form DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestion(java.lang.String,boolean,java.lang.String,java.lang.String)">
<h3>showQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean cancel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dialogTitle,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> defaultAction)</span></div>
<div class="block">Shows the yes-no dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cancel</code> - true if cancel button needed.</dd>
<dd><code>message</code> - message of question.</dd>
<dd><code>dialogTitle</code> - title of the dialog.</dd>
<dd><code>defaultAction</code> - default selected action (button) in the question dialog.</dd>
<dt>Returns:</dt>
<dd>result constant form DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> yesLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noLabel,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</span></div>
<div class="block">Shows dialogs with given button text</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message of question.</dd>
<dd><code>yesLabel</code> - label key in dialog resources used instead of "Yes" text.</dd>
<dd><code>noLabel</code> - label key in dialog resources used instead of "No" text.</dd>
<dd><code>cancelLabel</code> - label key in dialog resources used instead of "Cancel" text, can be null.</dd>
<dd><code>icon</code> - path to icon image (for example "/com/company/icon.gif")</dd>
<dt>Returns:</dt>
<dd>result constant form DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> yesLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noLabel,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</span></div>
<div class="block">Shows dialogs with given button text</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message of question.</dd>
<dd><code>yesLabel</code> - label key in dialog resources used instead of "Yes" text.</dd>
<dd><code>noLabel</code> - label key in dialog resources used instead of "No" text.</dd>
<dd><code>cancelLabel</code> - label key in dialog resources used instead of "Cancel" text, can be null.</dd>
<dd><code>title</code> - title of the dialog.</dd>
<dd><code>icon</code> - path to icon image (for example "/com/company/icon.gif")</dd>
<dt>Returns:</dt>
<dd>result constant form DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showHTMLQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showHTMLQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showHTMLQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> yesLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> noLabel,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabel,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</span></div>
<div class="block">Shows html dialogs with given button text</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message of question.</dd>
<dd><code>yesLabel</code> - label key in dialog resources used instead of "Yes" text.</dd>
<dd><code>noLabel</code> - label key in dialog resources used instead of "No" text.</dd>
<dd><code>cancelLabel</code> - label key in dialog resources used instead of "Cancel" text, can be null.</dd>
<dd><code>title</code> - title of the dialog.</dd>
<dd><code>icon</code> - path to icon image (for example "/com/company/icon.gif")</dd>
<dt>Returns:</dt>
<dd>result constant form DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestionOkCancel(java.lang.String)">
<h3>showQuestionOkCancel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showQuestionOkCancel</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the ok-cancel dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message of question.</dd>
<dt>Returns:</dt>
<dd>result constant form DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestion(java.lang.String,java.lang.String)">
<h3>showQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</span></div>
<div class="block">Shows the yes-no-help dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message of question.</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
<dt>Returns:</dt>
<dd>true if answer was yes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showYesNoHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showYesNoHelp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showYesNoHelp</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</span></div>
<div class="block">Shows the yes-no-help dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message of question.</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
<dd><code>title</code> - title</dd>
<dd><code>icon</code> - path to icon image (for example "/com/company/icon.gif")</dd>
<dt>Returns:</dt>
<dd>true if answer was yes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestionForAll(java.lang.String)">
<h3>showQuestionForAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showQuestionForAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the yes-no-all dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text.</dd>
<dt>Returns:</dt>
<dd>result constant form DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestionForAll(java.lang.String,boolean)">
<h3>showQuestionForAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showQuestionForAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean cancel)</span></div>
<div class="block">Shows the yes-no-all dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dd><code>cancel</code> - true if cancel button needed</dd>
<dt>Returns:</dt>
<dd>one of the result constants in DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestionForAll(java.lang.String,boolean,boolean)">
<h3>showQuestionForAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showQuestionForAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean yesToAll,
 boolean cancel)</span></div>
<div class="block">Shows the yes-no-all dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
<dd><code>yesToAll</code> - true if Yes to ALL button needed</dd>
<dd><code>cancel</code> - true if cancel button needed</dd>
<dt>Returns:</dt>
<dd>one of the result constants in DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showRetryQuestion(java.lang.String)">
<h3>showRetryQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">showRetryQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the yes-no dialog with given message</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - Message Text</dd>
<dt>Returns:</dt>
<dd>one of the result constants in DialogConstants.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ui/DialogConstants.html" title="class in com.nomagic.ui"><code>DialogConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showWarning(java.lang.String)">
<h3>showWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showWarning</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Shows the warning dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - warning text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showWarning(java.lang.String,java.lang.String)">
<h3>showWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showWarning</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
<div class="block">Shows the warning dialog with given message and title.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - warning text.</dd>
<dd><code>title</code> - warning title</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showWarning(java.lang.String,java.lang.String,java.lang.String)">
<h3>showWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showWarning</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey)</span></div>
<div class="block">Shows the warning dialog with given message, title and button.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - warning text.</dd>
<dd><code>title</code> - warning title</dd>
<dd><code>okLabelKey</code> - button label</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showWarning(java.lang.String,java.lang.String,boolean)">
<h3>showWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showWarning</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> checkBoxMsg,
 boolean checkBoxValue)</span></div>
<div class="block">Shows the warning dialog with given message. Shows another message with a checkbox before like "Show next time" option.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text.</dd>
<dd><code>checkBoxMsg</code> - check box message</dd>
<dd><code>checkBoxValue</code> - check box state</dd>
<dt>Returns:</dt>
<dd>check box state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="log(com.nomagic.magicdraw.ui.notification.Notification,boolean)">
<h3>log</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">log</span><wbr/><span class="parameters">(<a href="../ui/notification/Notification.html" title="class in com.nomagic.magicdraw.ui.notification">Notification</a> notification,
 boolean openWindow)</span></div>
<div class="block">Logs notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>notification</code> - notification</dd>
<dd><code>openWindow</code> - flag, if true opens notification window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logNotification(java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">
<h3>logNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">logNotification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../ui/notification/NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="../ui/notification/Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</span></div>
<div class="block">Logs notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - notification text</dd>
<dd><code>severity</code> - notification severity</dd>
<dd><code>context</code> - notification context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logNotification(java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">
<h3>logNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">logNotification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a href="../ui/notification/NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="../ui/notification/Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</span></div>
<div class="block">Logs notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>severity</code> - notification severity</dd>
<dd><code>context</code> - notification context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="logNotification(java.lang.String,java.lang.String,com.nomagic.magicdraw.ui.notification.HRefRunnable[],com.nomagic.magicdraw.ui.notification.NotificationSeverity,com.nomagic.magicdraw.ui.notification.Notification.Context)">
<h3>logNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">logNotification</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 @CheckForNull
 <a href="../ui/notification/HRefRunnable.html" title="class in com.nomagic.magicdraw.ui.notification">HRefRunnable</a>[] actions,
 <a href="../ui/notification/NotificationSeverity.html" title="class in com.nomagic.magicdraw.ui.notification">NotificationSeverity</a> severity,
 <a href="../ui/notification/Notification.Context.html" title="enum class in com.nomagic.magicdraw.ui.notification">Notification.Context</a> context)</span></div>
<div class="block">Logs notification</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>title</code> - notification title</dd>
<dd><code>text</code> - notification text</dd>
<dd><code>severity</code> - notification severity</dd>
<dd><code>actions</code> - list of actions</dd>
<dd><code>context</code> - notification context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openMessageWindow()">
<h3>openMessageWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">openMessageWindow</span>()</div>
<div class="block">Opens message window.</div>
</section>
</li>
<li>
<section class="detail" id="openLog()">
<h3>openLog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">openLog</span>()</div>
<div class="block">Opens message window.</div>
</section>
</li>
<li>
<section class="detail" id="clearLog()">
<h3>clearLog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearLog</span>()</div>
<div class="block">Clear message window.</div>
</section>
</li>
<li>
<section class="detail" id="clearMessageWindow()">
<h3>clearMessageWindow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearMessageWindow</span>()</div>
<div class="block">Clear message window.</div>
</section>
</li>
<li>
<section class="detail" id="log(java.lang.String)">
<h3>log</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">log</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Writes message to message window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="log(java.lang.String,boolean)">
<h3>log</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">log</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean open)</span></div>
<div class="block">Writes message to log window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text.</dd>
<dd><code>open</code> - true if closed window should be reopened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="writeLogText(java.lang.String,boolean)">
<h3>writeLogText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">writeLogText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 boolean open)</span></div>
<div class="block">Writes message to log window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text.</dd>
<dd><code>open</code> - true if closed window should be reopened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showOutOfMemoryError(java.lang.String)">
<h3>showOutOfMemoryError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showOutOfMemoryError</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Display out of memory error.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showErrorWithHelp(java.lang.String,java.lang.String)">
<h3>showErrorWithHelp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showErrorWithHelp</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</span></div>
<div class="block">Shows the error dialog with given message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message text</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addHyperlinkedText(java.lang.String,java.util.Map)">
<h3>addHyperlinkedText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addHyperlinkedText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; callbacks)</span></div>
<div class="block">Display text with hyperlinks. Each hyperlink must have entry in callback.
 Hyperlink in the text must be surrounded by &lt;A&gt; &lt;/A&gt; tags. Callback is taken from the parameter callbacks using hyperlink text as key.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text with hyperlinks for example "Best modeling &lt;A&gt;hyperlink text to display&lt;/A&gt;  tool." text can contain any number of href.</dd>
<dd><code>callbacks</code> - map where is mapped hyperlinked text to the callback runnable. Map must contain String key and Runnable value.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#wrapForHyperlinkText(java.lang.String)"><code>wrapForHyperlinkText(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapForHyperlinkText(java.lang.String)">
<h3>wrapForHyperlinkText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapForHyperlinkText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</span></div>
<div class="block">Helper method to wrap given string into string suitable to use for hyperlinked log.
 Simply wrap with &lt;A&gt;&lt;/A&gt; tags</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str</code> - target string for hyperlink</dd>
<dt>Returns:</dt>
<dd>string wrapped into &lt;A&gt;&lt;/A&gt;</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#addHyperlinkedText(java.lang.String,java.util.Map)"><code>addHyperlinkedText(String, java.util.Map)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wrapForHeyperlinkText(java.lang.String)">
<h3>wrapForHeyperlinkText</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">wrapForHeyperlinkText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Misspelled - use <a href="#wrapForHyperlinkText(java.lang.String)"><code>wrapForHyperlinkText(String)</code></a></div>
</div>
<div class="block">Wrap text for hyperlink</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text to wrap</dd>
<dt>Returns:</dt>
<dd>wrapped text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addURLCallBack(java.util.Map,java.lang.String,java.lang.String)">
<h3>addURLCallBack</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt;</span> <span class="element-name">addURLCallBack</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; map,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> href)</span></div>
<div class="block">Adds callback to open href to the map. call back is used in <a href="#addHyperlinkedText(java.lang.String,java.util.Map)"><code>addHyperlinkedText(String, Map)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>map</code> - map to which callback is</dd>
<dd><code>string</code> - text fragment which is hyperlinked</dd>
<dd><code>href</code> - reference</dd>
<dt>Returns:</dt>
<dd>map with url call backs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionURL(com.nomagic.actions.NMAction)">
<h3>createActionURL</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createActionURL</span><wbr/><span class="parameters">(@Nonnull
 <a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">A utility method to create URL to some action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action</dd>
<dt>Returns:</dt>
<dd>url to this action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionURLWithText(com.nomagic.actions.NMAction)">
<h3>createActionURLWithText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createActionURLWithText</span><wbr/><span class="parameters">(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action)</span></div>
<div class="block">A utility method to create URL to some action with</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action</dd>
<dt>Returns:</dt>
<dd>url to this action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActionURLWithText(com.nomagic.actions.NMAction,java.lang.String)">
<h3>createActionURLWithText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createActionURLWithText</span><wbr/><span class="parameters">(<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a> action,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">A utility method to create URL to some action with</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>action</code> - action</dd>
<dd><code>text</code> - url text</dd>
<dt>Returns:</dt>
<dd>url to this action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLoggedMessages()">
<h3>getLoggedMessages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLoggedMessages</span>()</div>
<div class="block">A utility method get all logged messages
 (This GUILog class provides a method to get the LogDialog, but the LogDialog is not part of the OpenAPI
 and therefore not accessible by code that will want to use it.)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the messages visible in the LogDialog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestionWithHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showQuestionWithHelp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showQuestionWithHelp</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> notificationMsg,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</span></div>
<div class="block">Show customized Ok/Cancel/Help question in a modal dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to show</dd>
<dd><code>notificationMsg</code> - notification message to show if silent mode is on</dd>
<dd><code>okLabelKey</code> - label key in DialogResource.properties for the Ok button</dd>
<dd><code>title</code> - dialog title</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
<dt>Returns:</dt>
<dd>true - if Ok was pressed, false - if canceled.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showQuestionWithHelp(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showQuestionWithHelp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showQuestionWithHelp</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> helpID)</span></div>
<div class="block">Show customized Ok/Cancel/Help question in a modal dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to show</dd>
<dd><code>okLabelKey</code> - label key in DialogResource.properties for the Ok button</dd>
<dd><code>title</code> - dialog title</dd>
<dd><code>helpID</code> - help item ID in help system</dd>
<dt>Returns:</dt>
<dd>true - if Ok was pressed, false - if canceled.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showWarningQuestion(java.lang.String,java.lang.String,java.lang.String)">
<h3>showWarningQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showWarningQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
<div class="block">Show customized Cancel/Ok question in a modal dialog.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to show</dd>
<dd><code>okLabelKey</code> - label key in DialogResource.properties for the Ok button</dd>
<dd><code>title</code> - dialog title</dd>
<dt>Returns:</dt>
<dd>true - if Ok was pressed, false - if canceled.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showWarningQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showWarningQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showWarningQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
<div class="block">Show customized Cancel/Ok question in a model dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message to show</dd>
<dd><code>okLabelKey</code> - the label key in DialogResource.properties for the Ok button</dd>
<dd><code>cancelLabelKey</code> - the label key in DialogResource.properties for the Cancel
                       button</dd>
<dd><code>title</code> - the dialog title</dd>
<dt>Returns:</dt>
<dd><code>true</code> if Ok was pressed, <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showCustomizedQuestion(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>showCustomizedQuestion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">showCustomizedQuestion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> okLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cancelLabelKey,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> icon)</span></div>
<div class="block">Show customized Cancel/Ok question in a model dialog</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the message to show</dd>
<dd><code>okLabelKey</code> - the label key in DialogResource.properties for the Ok button</dd>
<dd><code>cancelLabelKey</code> - the label key in DialogResource.properties for the Cancel
                       button</dd>
<dd><code>title</code> - the dialog title</dd>
<dd><code>icon</code> - the dialog icon</dd>
<dt>Returns:</dt>
<dd><code>true</code> if Ok was pressed, <code>false</code> otherwise</dd>
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
