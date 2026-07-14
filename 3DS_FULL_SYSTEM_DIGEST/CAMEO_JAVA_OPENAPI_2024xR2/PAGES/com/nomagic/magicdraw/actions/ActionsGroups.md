# JAVA OPENAPI: ActionsGroups (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/actions/ActionsGroups.html
- source_path: `com/nomagic/magicdraw/actions/ActionsGroups.html`
- source_sha256: `9a0355d36d593efa0120053ba90df92d35a6d83b19e299d57473ce2471a35e1d`
- captured_utc: `2026-07-14T16:55:02.463865+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Interface ActionsGroups

All Known Implementing Classes:
`[MainFrame](../ui/MainFrame.html)`

@OpenApiAllpublic interfaceActionsGroups

The constants file which defines the names of the related actions groups.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_DIAGRAM_EDIT_RELATED](#ANY_DIAGRAM_EDIT_RELATED)`
These actions will be available when any diagram (not just UML) is opened and is not read only.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_DIAGRAM_OPENED_RELATED](#ANY_DIAGRAM_OPENED_RELATED)`
These actions will be available when any (not just UML) diagram is opened.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_PROJECT_EDIT_RELATED](#ANY_PROJECT_EDIT_RELATED)`
These actions will be available if UML or any other kind of project is opened and is not read only(can be edited).
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_PROJECT_OPENED_RELATED](#ANY_PROJECT_OPENED_RELATED)`
These actions will be available when UML or any other kind of project is opened.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_PROJECT_SAVING_RELATED](#ANY_PROJECT_SAVING_RELATED)`
These actions will be available when current project is any kind of project and can be saved
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_REMOTE_ANY_PROJECT_EDIT_RELATED](#ANY_REMOTE_ANY_PROJECT_EDIT_RELATED)`
These actions will be available when any kind of project is opened from TeamworkCloud/PowerBy and user has right to edit model.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_REMOTE_PROJECT_EDIT_RELATED](#ANY_REMOTE_PROJECT_EDIT_RELATED)`
Deprecated.
use [`ANY_REMOTE_UML_PROJECT_EDIT_RELATED`](#ANY_REMOTE_UML_PROJECT_EDIT_RELATED) or [`ANY_REMOTE_ANY_PROJECT_EDIT_RELATED`](#ANY_REMOTE_ANY_PROJECT_EDIT_RELATED)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_REMOTE_PROJECT_OPENED_RELATED](#ANY_REMOTE_PROJECT_OPENED_RELATED)`
Deprecated.
use [`ESI_UML_PROJECT_OPENED_RELATED`](#ESI_UML_PROJECT_OPENED_RELATED) or [`ESI_ANY_PROJECT_OPENED_RELATED`](#ESI_ANY_PROJECT_OPENED_RELATED)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_REMOTE_UML_PROJECT_EDIT_RELATED](#ANY_REMOTE_UML_PROJECT_EDIT_RELATED)`
These actions will be available when UML project is opened from TeamworkCloud/PowerBy and user has right to edit model.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ANY_SERVER_LOGIN_RELATED](#ANY_SERVER_LOGIN_RELATED)`
These actions will be available when user is logged into TeamworkCloud/PowerBy
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[APPLICATION_RELATED](#APPLICATION_RELATED)`
These actions will be available when MagicDraw application is running.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_EDIT_RELATED](#DIAGRAM_EDIT_RELATED)`
These actions will be available when UML diagram is opened and is not read only.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_OPENED_RELATED](#DIAGRAM_OPENED_RELATED)`
These actions will be available when UML diagram is opened.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_RELATED_ELEMENTS](#DIAGRAM_RELATED_ELEMENTS)`
Deprecated.
do not use it.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_ZOOMIN_RELATED](#DIAGRAM_ZOOMIN_RELATED)`
These actions will be available when any kind of diagram is opened and can be zoomed in.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_ZOOMOUT_RELATED](#DIAGRAM_ZOOMOUT_RELATED)`
These actions will be available when any kind of diagram is opened and can be zoomed out.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DIAGRAM_ZOOMTO11_RELATED](#DIAGRAM_ZOOMTO11_RELATED)`
These actions will be available when any kind of diagram is opened and can be zoomed to 1:1.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EDITOR_OPENED_RELATED](#EDITOR_OPENED_RELATED)`
These actions will be available when any Editor is opened.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ESI_ANY_PROJECT_OPENED_RELATED](#ESI_ANY_PROJECT_OPENED_RELATED)`
These actions will be available when any kind of project is opened from TeamworkCloud/PowerBy.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ESI_PROJECT_OPENED_RELATED](#ESI_PROJECT_OPENED_RELATED)`
Deprecated.
use [`ESI_UML_PROJECT_OPENED_RELATED`](#ESI_UML_PROJECT_OPENED_RELATED) or [`ESI_ANY_PROJECT_OPENED_RELATED`](#ESI_ANY_PROJECT_OPENED_RELATED)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ESI_SERVER_LOGIN_RELATED](#ESI_SERVER_LOGIN_RELATED)`
These actions will be available when user is logged in into TeamworkCloud/PowerBy and server is ready.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ESI_UML_PROJECT_OPENED_RELATED](#ESI_UML_PROJECT_OPENED_RELATED)`
These actions will be available when UML project is opened from TeamworkCloud/PowerBy.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUT_SHAPES_RELATED](#LAYOUT_SHAPES_RELATED)`
These actions will be available when any kind of diagram is opened and more than one shape is selected.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOCAL_PROJECT_OPENED_RELATED](#LOCAL_PROJECT_OPENED_RELATED)`
Deprecated.
use [`LOCAL_UML_PROJECT_OPENED_RELATED`](#LOCAL_UML_PROJECT_OPENED_RELATED)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LOCAL_UML_PROJECT_OPENED_RELATED](#LOCAL_UML_PROJECT_OPENED_RELATED)`
These actions will be available when current project is opened from file system (not from some server) and is UML project
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NOT_EMPTY_ANY_DIAGRAM_RELATED](#NOT_EMPTY_ANY_DIAGRAM_RELATED)`
These actions will be available when not empty any diagram (not just UML) is opened.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NOT_EMPTY_CLASS_DIAGRAM_RELATED](#NOT_EMPTY_CLASS_DIAGRAM_RELATED)`
These actions will be available when not empty UML class diagram is opened.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NOT_EMPTY_DIAGRAM_RELATED](#NOT_EMPTY_DIAGRAM_RELATED)`
These actions will be available when not empty UML diagram is opened.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OPENED_MODULE_AS_PROJECT](#OPENED_MODULE_AS_PROJECT)`
Actions are disabled, when opened project is module
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PATH_STYLE_EDIT_RELATED](#PATH_STYLE_EDIT_RELATED)`
These actions will be available when current project is opened, diagram is opened and path is selected.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED](#PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED)`
These actions will be available when current project is opened from teamwork server and
 user has right to edit model and symbols are selected in opened diagram.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PRESENTATION_ELEMENT_ALIGN_RELATED](#PRESENTATION_ELEMENT_ALIGN_RELATED)`
These actions will be available when diagram is opened and selected presentation elements can be aligned.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PRESENTATION_ELEMENT_SELECTION_RELATED](#PRESENTATION_ELEMENT_SELECTION_RELATED)`
These actions will be available when diagram is opened and symbol is selected in diagram.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROJECT_EDIT_RELATED](#PROJECT_EDIT_RELATED)`
Deprecated.
use [`UML_PROJECT_EDIT_RELATED`](#UML_PROJECT_EDIT_RELATED) or [`ANY_PROJECT_EDIT_RELATED`](#ANY_PROJECT_EDIT_RELATED)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROJECT_OPENED_RELATED](#PROJECT_OPENED_RELATED)`
Deprecated.
use [`UML_PROJECT_OPENED_RELATED`](#UML_PROJECT_OPENED_RELATED) or[`ANY_PROJECT_OPENED_RELATED`](#ANY_PROJECT_OPENED_RELATED)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROJECT_SAVING_RELATED](#PROJECT_SAVING_RELATED)`
Deprecated.
use [`ANY_PROJECT_SAVING_RELATED`](#ANY_PROJECT_SAVING_RELATED)
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REDO_COMMAND_RELATED](#REDO_COMMAND_RELATED)`
These actions will be available when there is a command ready for redo.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UML_PROJECT_EDIT_RELATED](#UML_PROJECT_EDIT_RELATED)`
These actions will be available if UML project is opened and is not read only(can be edited).
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UML_PROJECT_OPENED_RELATED](#UML_PROJECT_OPENED_RELATED)`
These actions will be available when UML project is opened.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[UNDO_COMMAND_RELATED](#UNDO_COMMAND_RELATED)`
These actions will be available when there is a command ready for undo.

============ FIELD DETAIL =========== 
Field Details
APPLICATION_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) APPLICATION_RELATED
These actions will be available when MagicDraw application is running.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.APPLICATION_RELATED)
PROJECT_OPENED_RELATED
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROJECT_OPENED_RELATED
Deprecated.
use [`UML_PROJECT_OPENED_RELATED`](#UML_PROJECT_OPENED_RELATED) or[`ANY_PROJECT_OPENED_RELATED`](#ANY_PROJECT_OPENED_RELATED)
These actions will be available when UML project is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PROJECT_OPENED_RELATED)
UML_PROJECT_OPENED_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UML_PROJECT_OPENED_RELATED
These actions will be available when UML project is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.UML_PROJECT_OPENED_RELATED)
ANY_PROJECT_OPENED_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_PROJECT_OPENED_RELATED
These actions will be available when UML or any other kind of project is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_PROJECT_OPENED_RELATED)
EDITOR_OPENED_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EDITOR_OPENED_RELATED
These actions will be available when any Editor is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.EDITOR_OPENED_RELATED)
DIAGRAM_OPENED_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_OPENED_RELATED
These actions will be available when UML diagram is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_OPENED_RELATED)
ANY_DIAGRAM_OPENED_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_DIAGRAM_OPENED_RELATED
These actions will be available when any (not just UML) diagram is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_DIAGRAM_OPENED_RELATED)
NOT_EMPTY_DIAGRAM_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NOT_EMPTY_DIAGRAM_RELATED
These actions will be available when not empty UML diagram is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.NOT_EMPTY_DIAGRAM_RELATED)
NOT_EMPTY_ANY_DIAGRAM_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NOT_EMPTY_ANY_DIAGRAM_RELATED
These actions will be available when not empty any diagram (not just UML) is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.NOT_EMPTY_ANY_DIAGRAM_RELATED)
PROJECT_SAVING_RELATED
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROJECT_SAVING_RELATED
Deprecated.
use [`ANY_PROJECT_SAVING_RELATED`](#ANY_PROJECT_SAVING_RELATED)
These actions will be available when current project can be saved and is any kind of project
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PROJECT_SAVING_RELATED)
ANY_PROJECT_SAVING_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_PROJECT_SAVING_RELATED
These actions will be available when current project is any kind of project and can be saved
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_PROJECT_SAVING_RELATED)
PRESENTATION_ELEMENT_SELECTION_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PRESENTATION_ELEMENT_SELECTION_RELATED
These actions will be available when diagram is opened and symbol is selected in diagram.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PRESENTATION_ELEMENT_SELECTION_RELATED)
PRESENTATION_ELEMENT_ALIGN_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PRESENTATION_ELEMENT_ALIGN_RELATED
These actions will be available when diagram is opened and selected presentation elements can be aligned.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PRESENTATION_ELEMENT_ALIGN_RELATED)
REDO_COMMAND_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REDO_COMMAND_RELATED
These actions will be available when there is a command ready for redo.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.REDO_COMMAND_RELATED)
UNDO_COMMAND_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UNDO_COMMAND_RELATED
These actions will be available when there is a command ready for undo.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.UNDO_COMMAND_RELATED)
DIAGRAM_ZOOMIN_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_ZOOMIN_RELATED
These actions will be available when any kind of diagram is opened and can be zoomed in.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_ZOOMIN_RELATED)
DIAGRAM_ZOOMOUT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_ZOOMOUT_RELATED
These actions will be available when any kind of diagram is opened and can be zoomed out.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_ZOOMOUT_RELATED)
DIAGRAM_ZOOMTO11_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_ZOOMTO11_RELATED
These actions will be available when any kind of diagram is opened and can be zoomed to 1:1.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_ZOOMTO11_RELATED)
PROJECT_EDIT_RELATED
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROJECT_EDIT_RELATED
Deprecated.
use [`UML_PROJECT_EDIT_RELATED`](#UML_PROJECT_EDIT_RELATED) or [`ANY_PROJECT_EDIT_RELATED`](#ANY_PROJECT_EDIT_RELATED)
These actions will be available if UML project is opened and is not read only(can be edited).
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PROJECT_EDIT_RELATED)
UML_PROJECT_EDIT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) UML_PROJECT_EDIT_RELATED
These actions will be available if UML project is opened and is not read only(can be edited).
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.UML_PROJECT_EDIT_RELATED)
ANY_PROJECT_EDIT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_PROJECT_EDIT_RELATED
These actions will be available if UML or any other kind of project is opened and is not read only(can be edited).
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_PROJECT_EDIT_RELATED)
NOT_EMPTY_CLASS_DIAGRAM_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NOT_EMPTY_CLASS_DIAGRAM_RELATED
These actions will be available when not empty UML class diagram is opened.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.NOT_EMPTY_CLASS_DIAGRAM_RELATED)
LAYOUT_SHAPES_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUT_SHAPES_RELATED
These actions will be available when any kind of diagram is opened and more than one shape is selected.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.LAYOUT_SHAPES_RELATED)
ESI_SERVER_LOGIN_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ESI_SERVER_LOGIN_RELATED
These actions will be available when user is logged in into TeamworkCloud/PowerBy and server is ready.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ESI_SERVER_LOGIN_RELATED)
ANY_SERVER_LOGIN_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_SERVER_LOGIN_RELATED
These actions will be available when user is logged into TeamworkCloud/PowerBy
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_SERVER_LOGIN_RELATED)
ANY_REMOTE_PROJECT_OPENED_RELATED
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_REMOTE_PROJECT_OPENED_RELATED
Deprecated.
use [`ESI_UML_PROJECT_OPENED_RELATED`](#ESI_UML_PROJECT_OPENED_RELATED) or [`ESI_ANY_PROJECT_OPENED_RELATED`](#ESI_ANY_PROJECT_OPENED_RELATED)
These actions will be available when UML project is opened from TeamworkCloud/PowerBy.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_REMOTE_PROJECT_OPENED_RELATED)
ESI_PROJECT_OPENED_RELATED
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ESI_PROJECT_OPENED_RELATED
Deprecated.
use [`ESI_UML_PROJECT_OPENED_RELATED`](#ESI_UML_PROJECT_OPENED_RELATED) or [`ESI_ANY_PROJECT_OPENED_RELATED`](#ESI_ANY_PROJECT_OPENED_RELATED)
These actions will be available when UML project is opened from TeamworkCloud/PowerBy.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ESI_PROJECT_OPENED_RELATED)
ESI_ANY_PROJECT_OPENED_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ESI_ANY_PROJECT_OPENED_RELATED
These actions will be available when any kind of project is opened from TeamworkCloud/PowerBy.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ESI_ANY_PROJECT_OPENED_RELATED)
ESI_UML_PROJECT_OPENED_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ESI_UML_PROJECT_OPENED_RELATED
These actions will be available when UML project is opened from TeamworkCloud/PowerBy.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ESI_UML_PROJECT_OPENED_RELATED)
ANY_REMOTE_PROJECT_EDIT_RELATED
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_REMOTE_PROJECT_EDIT_RELATED
Deprecated.
use [`ANY_REMOTE_UML_PROJECT_EDIT_RELATED`](#ANY_REMOTE_UML_PROJECT_EDIT_RELATED) or [`ANY_REMOTE_ANY_PROJECT_EDIT_RELATED`](#ANY_REMOTE_ANY_PROJECT_EDIT_RELATED)
These actions will be available when UML project is opened from TeamworkCloud/PowerBy and user has right to edit model.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_REMOTE_PROJECT_EDIT_RELATED)
ANY_REMOTE_UML_PROJECT_EDIT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_REMOTE_UML_PROJECT_EDIT_RELATED
These actions will be available when UML project is opened from TeamworkCloud/PowerBy and user has right to edit model.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_REMOTE_UML_PROJECT_EDIT_RELATED)
ANY_REMOTE_ANY_PROJECT_EDIT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_REMOTE_ANY_PROJECT_EDIT_RELATED
These actions will be available when any kind of project is opened from TeamworkCloud/PowerBy and user has right to edit model.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_REMOTE_ANY_PROJECT_EDIT_RELATED)
LOCAL_PROJECT_OPENED_RELATED
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOCAL_PROJECT_OPENED_RELATED
Deprecated.
use [`LOCAL_UML_PROJECT_OPENED_RELATED`](#LOCAL_UML_PROJECT_OPENED_RELATED)
These actions will be available when current project is opened from file system (not from some server) and is UML project
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.LOCAL_PROJECT_OPENED_RELATED)
LOCAL_UML_PROJECT_OPENED_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LOCAL_UML_PROJECT_OPENED_RELATED
These actions will be available when current project is opened from file system (not from some server) and is UML project
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.LOCAL_UML_PROJECT_OPENED_RELATED)
PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED
These actions will be available when current project is opened from teamwork server and
 user has right to edit model and symbols are selected in opened diagram.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED)
PATH_STYLE_EDIT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PATH_STYLE_EDIT_RELATED
These actions will be available when current project is opened, diagram is opened and path is selected.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PATH_STYLE_EDIT_RELATED)
DIAGRAM_EDIT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_EDIT_RELATED
These actions will be available when UML diagram is opened and is not read only.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_EDIT_RELATED)
ANY_DIAGRAM_EDIT_RELATED
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ANY_DIAGRAM_EDIT_RELATED
These actions will be available when any diagram (not just UML) is opened and is not read only.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_DIAGRAM_EDIT_RELATED)
OPENED_MODULE_AS_PROJECT
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OPENED_MODULE_AS_PROJECT
Actions are disabled, when opened project is module
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.OPENED_MODULE_AS_PROJECT)
DIAGRAM_RELATED_ELEMENTS
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DIAGRAM_RELATED_ELEMENTS
Deprecated.
do not use it. Will be removed in future versions.
Diagram -> Related elements' subgroup.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_RELATED_ELEMENTS)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Interface ActionsGroups">Interface ActionsGroups</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../ui/MainFrame.html" title="class in com.nomagic.magicdraw.ui">MainFrame</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ActionsGroups</span></div>
<div class="block">The constants file which defines the names of the related actions groups.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANY_DIAGRAM_EDIT_RELATED">ANY_DIAGRAM_EDIT_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when any diagram (not just UML) is opened and is not read only.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANY_DIAGRAM_OPENED_RELATED">ANY_DIAGRAM_OPENED_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when  any (not just UML) diagram is opened.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANY_PROJECT_EDIT_RELATED">ANY_PROJECT_EDIT_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available if UML or any other kind of project is opened and is not read only(can be edited).</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANY_PROJECT_OPENED_RELATED">ANY_PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when UML or any other kind of project is opened.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANY_PROJECT_SAVING_RELATED">ANY_PROJECT_SAVING_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when current project is any kind of project and can be saved</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANY_REMOTE_ANY_PROJECT_EDIT_RELATED">ANY_REMOTE_ANY_PROJECT_EDIT_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when any kind of project is opened from TeamworkCloud/PowerBy and user has right to edit model.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANY_REMOTE_PROJECT_EDIT_RELATED">ANY_REMOTE_PROJECT_EDIT_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ANY_REMOTE_UML_PROJECT_EDIT_RELATED"><code>ANY_REMOTE_UML_PROJECT_EDIT_RELATED</code></a> or <a href="#ANY_REMOTE_ANY_PROJECT_EDIT_RELATED"><code>ANY_REMOTE_ANY_PROJECT_EDIT_RELATED</code></a></div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANY_REMOTE_PROJECT_OPENED_RELATED">ANY_REMOTE_PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ESI_UML_PROJECT_OPENED_RELATED"><code>ESI_UML_PROJECT_OPENED_RELATED</code></a> or <a href="#ESI_ANY_PROJECT_OPENED_RELATED"><code>ESI_ANY_PROJECT_OPENED_RELATED</code></a></div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANY_REMOTE_UML_PROJECT_EDIT_RELATED">ANY_REMOTE_UML_PROJECT_EDIT_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when UML project is opened from TeamworkCloud/PowerBy and user has right to edit model.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANY_SERVER_LOGIN_RELATED">ANY_SERVER_LOGIN_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when user is logged into TeamworkCloud/PowerBy</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#APPLICATION_RELATED">APPLICATION_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when MagicDraw application  is running.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_EDIT_RELATED">DIAGRAM_EDIT_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when UML diagram is opened and is not read only.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_OPENED_RELATED">DIAGRAM_OPENED_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when  UML diagram is opened.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_RELATED_ELEMENTS">DIAGRAM_RELATED_ELEMENTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">do not use it.</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_ZOOMIN_RELATED">DIAGRAM_ZOOMIN_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when any kind of diagram is opened and can be zoomed in.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_ZOOMOUT_RELATED">DIAGRAM_ZOOMOUT_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when any kind of diagram is opened and can be zoomed out.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DIAGRAM_ZOOMTO11_RELATED">DIAGRAM_ZOOMTO11_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when any kind of diagram is opened and can be zoomed to 1:1.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EDITOR_OPENED_RELATED">EDITOR_OPENED_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when  any Editor is opened.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ESI_ANY_PROJECT_OPENED_RELATED">ESI_ANY_PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when any kind of project is opened from TeamworkCloud/PowerBy.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ESI_PROJECT_OPENED_RELATED">ESI_PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ESI_UML_PROJECT_OPENED_RELATED"><code>ESI_UML_PROJECT_OPENED_RELATED</code></a> or <a href="#ESI_ANY_PROJECT_OPENED_RELATED"><code>ESI_ANY_PROJECT_OPENED_RELATED</code></a></div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ESI_SERVER_LOGIN_RELATED">ESI_SERVER_LOGIN_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when user is logged in into TeamworkCloud/PowerBy and server is ready.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ESI_UML_PROJECT_OPENED_RELATED">ESI_UML_PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when UML project is opened from TeamworkCloud/PowerBy.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LAYOUT_SHAPES_RELATED">LAYOUT_SHAPES_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when any kind of diagram is opened and more than one shape is selected.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOCAL_PROJECT_OPENED_RELATED">LOCAL_PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#LOCAL_UML_PROJECT_OPENED_RELATED"><code>LOCAL_UML_PROJECT_OPENED_RELATED</code></a></div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOCAL_UML_PROJECT_OPENED_RELATED">LOCAL_UML_PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when current project is opened from file system (not from some server) and is UML project</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NOT_EMPTY_ANY_DIAGRAM_RELATED">NOT_EMPTY_ANY_DIAGRAM_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when  not empty any diagram (not just UML)  is opened.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NOT_EMPTY_CLASS_DIAGRAM_RELATED">NOT_EMPTY_CLASS_DIAGRAM_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when not empty UML class diagram is opened.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NOT_EMPTY_DIAGRAM_RELATED">NOT_EMPTY_DIAGRAM_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when not empty UML diagram is opened.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPENED_MODULE_AS_PROJECT">OPENED_MODULE_AS_PROJECT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Actions are disabled, when opened project is module</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PATH_STYLE_EDIT_RELATED">PATH_STYLE_EDIT_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when current project is opened, diagram is opened and path is selected.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED">PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when current project is opened from teamwork server and
 user has right to edit model and symbols are selected in opened diagram.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PRESENTATION_ELEMENT_ALIGN_RELATED">PRESENTATION_ELEMENT_ALIGN_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when diagram is opened and selected presentation elements can be aligned.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PRESENTATION_ELEMENT_SELECTION_RELATED">PRESENTATION_ELEMENT_SELECTION_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when diagram is opened and symbol is selected in diagram.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECT_EDIT_RELATED">PROJECT_EDIT_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#UML_PROJECT_EDIT_RELATED"><code>UML_PROJECT_EDIT_RELATED</code></a> or <a href="#ANY_PROJECT_EDIT_RELATED"><code>ANY_PROJECT_EDIT_RELATED</code></a></div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROJECT_OPENED_RELATED">PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#UML_PROJECT_OPENED_RELATED"><code>UML_PROJECT_OPENED_RELATED</code></a> or<a href="#ANY_PROJECT_OPENED_RELATED"><code>ANY_PROJECT_OPENED_RELATED</code></a></div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECT_SAVING_RELATED">PROJECT_SAVING_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ANY_PROJECT_SAVING_RELATED"><code>ANY_PROJECT_SAVING_RELATED</code></a></div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REDO_COMMAND_RELATED">REDO_COMMAND_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when there is a command ready for redo.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UML_PROJECT_EDIT_RELATED">UML_PROJECT_EDIT_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available if UML project is opened and is not read only(can be edited).</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#UML_PROJECT_OPENED_RELATED">UML_PROJECT_OPENED_RELATED</a></code></div>
<div class="col-last even-row-color">
<div class="block">These actions will be available when UML project is opened.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UNDO_COMMAND_RELATED">UNDO_COMMAND_RELATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">These actions will be available when there is a command ready for undo.</div>
</div>
</div>
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
<section class="detail" id="APPLICATION_RELATED">
<h3>APPLICATION_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">APPLICATION_RELATED</span></div>
<div class="block">These actions will be available when MagicDraw application  is running.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.APPLICATION_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_OPENED_RELATED">
<h3>PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECT_OPENED_RELATED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#UML_PROJECT_OPENED_RELATED"><code>UML_PROJECT_OPENED_RELATED</code></a> or<a href="#ANY_PROJECT_OPENED_RELATED"><code>ANY_PROJECT_OPENED_RELATED</code></a></div>
</div>
<div class="block">These actions will be available when UML project is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UML_PROJECT_OPENED_RELATED">
<h3>UML_PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UML_PROJECT_OPENED_RELATED</span></div>
<div class="block">These actions will be available when UML project is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.UML_PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_PROJECT_OPENED_RELATED">
<h3>ANY_PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_PROJECT_OPENED_RELATED</span></div>
<div class="block">These actions will be available when UML or any other kind of project is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EDITOR_OPENED_RELATED">
<h3>EDITOR_OPENED_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EDITOR_OPENED_RELATED</span></div>
<div class="block">These actions will be available when  any Editor is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.EDITOR_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_OPENED_RELATED">
<h3>DIAGRAM_OPENED_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_OPENED_RELATED</span></div>
<div class="block">These actions will be available when  UML diagram is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_DIAGRAM_OPENED_RELATED">
<h3>ANY_DIAGRAM_OPENED_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_DIAGRAM_OPENED_RELATED</span></div>
<div class="block">These actions will be available when  any (not just UML) diagram is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_DIAGRAM_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NOT_EMPTY_DIAGRAM_RELATED">
<h3>NOT_EMPTY_DIAGRAM_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NOT_EMPTY_DIAGRAM_RELATED</span></div>
<div class="block">These actions will be available when not empty UML diagram is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.NOT_EMPTY_DIAGRAM_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NOT_EMPTY_ANY_DIAGRAM_RELATED">
<h3>NOT_EMPTY_ANY_DIAGRAM_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NOT_EMPTY_ANY_DIAGRAM_RELATED</span></div>
<div class="block">These actions will be available when  not empty any diagram (not just UML)  is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.NOT_EMPTY_ANY_DIAGRAM_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_SAVING_RELATED">
<h3>PROJECT_SAVING_RELATED</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECT_SAVING_RELATED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ANY_PROJECT_SAVING_RELATED"><code>ANY_PROJECT_SAVING_RELATED</code></a></div>
</div>
<div class="block">These actions will be available when current project can be saved and is any kind of project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PROJECT_SAVING_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_PROJECT_SAVING_RELATED">
<h3>ANY_PROJECT_SAVING_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_PROJECT_SAVING_RELATED</span></div>
<div class="block">These actions will be available when current project is any kind of project and can be saved</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_PROJECT_SAVING_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRESENTATION_ELEMENT_SELECTION_RELATED">
<h3>PRESENTATION_ELEMENT_SELECTION_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PRESENTATION_ELEMENT_SELECTION_RELATED</span></div>
<div class="block">These actions will be available when diagram is opened and symbol is selected in diagram.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PRESENTATION_ELEMENT_SELECTION_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PRESENTATION_ELEMENT_ALIGN_RELATED">
<h3>PRESENTATION_ELEMENT_ALIGN_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PRESENTATION_ELEMENT_ALIGN_RELATED</span></div>
<div class="block">These actions will be available when diagram is opened and selected presentation elements can be aligned.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PRESENTATION_ELEMENT_ALIGN_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REDO_COMMAND_RELATED">
<h3>REDO_COMMAND_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REDO_COMMAND_RELATED</span></div>
<div class="block">These actions will be available when there is a command ready for redo.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.REDO_COMMAND_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UNDO_COMMAND_RELATED">
<h3>UNDO_COMMAND_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UNDO_COMMAND_RELATED</span></div>
<div class="block">These actions will be available when there is a command ready for undo.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.UNDO_COMMAND_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_ZOOMIN_RELATED">
<h3>DIAGRAM_ZOOMIN_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_ZOOMIN_RELATED</span></div>
<div class="block">These actions will be available when any kind of diagram is opened and can be zoomed in.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_ZOOMIN_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_ZOOMOUT_RELATED">
<h3>DIAGRAM_ZOOMOUT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_ZOOMOUT_RELATED</span></div>
<div class="block">These actions will be available when any kind of diagram is opened and can be zoomed out.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_ZOOMOUT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_ZOOMTO11_RELATED">
<h3>DIAGRAM_ZOOMTO11_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_ZOOMTO11_RELATED</span></div>
<div class="block">These actions will be available when any kind of diagram is opened and can be zoomed to 1:1.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_ZOOMTO11_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT_EDIT_RELATED">
<h3>PROJECT_EDIT_RELATED</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECT_EDIT_RELATED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#UML_PROJECT_EDIT_RELATED"><code>UML_PROJECT_EDIT_RELATED</code></a> or <a href="#ANY_PROJECT_EDIT_RELATED"><code>ANY_PROJECT_EDIT_RELATED</code></a></div>
</div>
<div class="block">These actions will be available if UML project is opened and is not read only(can be edited).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PROJECT_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UML_PROJECT_EDIT_RELATED">
<h3>UML_PROJECT_EDIT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">UML_PROJECT_EDIT_RELATED</span></div>
<div class="block">These actions will be available if UML project is opened and is not read only(can be edited).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.UML_PROJECT_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_PROJECT_EDIT_RELATED">
<h3>ANY_PROJECT_EDIT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_PROJECT_EDIT_RELATED</span></div>
<div class="block">These actions will be available if UML or any other kind of project is opened and is not read only(can be edited).</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_PROJECT_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NOT_EMPTY_CLASS_DIAGRAM_RELATED">
<h3>NOT_EMPTY_CLASS_DIAGRAM_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NOT_EMPTY_CLASS_DIAGRAM_RELATED</span></div>
<div class="block">These actions will be available when not empty UML class diagram is opened.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.NOT_EMPTY_CLASS_DIAGRAM_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LAYOUT_SHAPES_RELATED">
<h3>LAYOUT_SHAPES_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUT_SHAPES_RELATED</span></div>
<div class="block">These actions will be available when any kind of diagram is opened and more than one shape is selected.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.LAYOUT_SHAPES_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ESI_SERVER_LOGIN_RELATED">
<h3>ESI_SERVER_LOGIN_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ESI_SERVER_LOGIN_RELATED</span></div>
<div class="block">These actions will be available when user is logged in into TeamworkCloud/PowerBy and server is ready.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ESI_SERVER_LOGIN_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_SERVER_LOGIN_RELATED">
<h3>ANY_SERVER_LOGIN_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_SERVER_LOGIN_RELATED</span></div>
<div class="block">These actions will be available when user is logged into TeamworkCloud/PowerBy</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_SERVER_LOGIN_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_REMOTE_PROJECT_OPENED_RELATED">
<h3>ANY_REMOTE_PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_REMOTE_PROJECT_OPENED_RELATED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ESI_UML_PROJECT_OPENED_RELATED"><code>ESI_UML_PROJECT_OPENED_RELATED</code></a> or <a href="#ESI_ANY_PROJECT_OPENED_RELATED"><code>ESI_ANY_PROJECT_OPENED_RELATED</code></a></div>
</div>
<div class="block">These actions will be available when UML project is opened from TeamworkCloud/PowerBy.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_REMOTE_PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ESI_PROJECT_OPENED_RELATED">
<h3>ESI_PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ESI_PROJECT_OPENED_RELATED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ESI_UML_PROJECT_OPENED_RELATED"><code>ESI_UML_PROJECT_OPENED_RELATED</code></a> or <a href="#ESI_ANY_PROJECT_OPENED_RELATED"><code>ESI_ANY_PROJECT_OPENED_RELATED</code></a></div>
</div>
<div class="block">These actions will be available when UML project is opened from TeamworkCloud/PowerBy.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ESI_PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ESI_ANY_PROJECT_OPENED_RELATED">
<h3>ESI_ANY_PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ESI_ANY_PROJECT_OPENED_RELATED</span></div>
<div class="block">These actions will be available when any kind of project is opened from TeamworkCloud/PowerBy.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ESI_ANY_PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ESI_UML_PROJECT_OPENED_RELATED">
<h3>ESI_UML_PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ESI_UML_PROJECT_OPENED_RELATED</span></div>
<div class="block">These actions will be available when UML project is opened from TeamworkCloud/PowerBy.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ESI_UML_PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_REMOTE_PROJECT_EDIT_RELATED">
<h3>ANY_REMOTE_PROJECT_EDIT_RELATED</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_REMOTE_PROJECT_EDIT_RELATED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#ANY_REMOTE_UML_PROJECT_EDIT_RELATED"><code>ANY_REMOTE_UML_PROJECT_EDIT_RELATED</code></a> or <a href="#ANY_REMOTE_ANY_PROJECT_EDIT_RELATED"><code>ANY_REMOTE_ANY_PROJECT_EDIT_RELATED</code></a></div>
</div>
<div class="block">These actions will be available when UML project is opened from TeamworkCloud/PowerBy and user has right to edit model.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_REMOTE_PROJECT_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_REMOTE_UML_PROJECT_EDIT_RELATED">
<h3>ANY_REMOTE_UML_PROJECT_EDIT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_REMOTE_UML_PROJECT_EDIT_RELATED</span></div>
<div class="block">These actions will be available when UML project is opened from TeamworkCloud/PowerBy and user has right to edit model.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_REMOTE_UML_PROJECT_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_REMOTE_ANY_PROJECT_EDIT_RELATED">
<h3>ANY_REMOTE_ANY_PROJECT_EDIT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_REMOTE_ANY_PROJECT_EDIT_RELATED</span></div>
<div class="block">These actions will be available when any kind of project is opened from TeamworkCloud/PowerBy and user has right to edit model.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_REMOTE_ANY_PROJECT_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCAL_PROJECT_OPENED_RELATED">
<h3>LOCAL_PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOCAL_PROJECT_OPENED_RELATED</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#LOCAL_UML_PROJECT_OPENED_RELATED"><code>LOCAL_UML_PROJECT_OPENED_RELATED</code></a></div>
</div>
<div class="block">These actions will be available when current project is opened from file system (not from some server) and is UML project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.LOCAL_PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCAL_UML_PROJECT_OPENED_RELATED">
<h3>LOCAL_UML_PROJECT_OPENED_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOCAL_UML_PROJECT_OPENED_RELATED</span></div>
<div class="block">These actions will be available when current project is opened from file system (not from some server) and is UML project</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.LOCAL_UML_PROJECT_OPENED_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED">
<h3>PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED</span></div>
<div class="block">These actions will be available when current project is opened from teamwork server and
 user has right to edit model and symbols are selected in opened diagram.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PE_SELECTION_AND_TEAMWORK_PROJECT_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PATH_STYLE_EDIT_RELATED">
<h3>PATH_STYLE_EDIT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PATH_STYLE_EDIT_RELATED</span></div>
<div class="block">These actions will be available when current project is opened, diagram is opened and path is selected.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.PATH_STYLE_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_EDIT_RELATED">
<h3>DIAGRAM_EDIT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_EDIT_RELATED</span></div>
<div class="block">These actions will be available when UML diagram is opened and is not read only.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANY_DIAGRAM_EDIT_RELATED">
<h3>ANY_DIAGRAM_EDIT_RELATED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ANY_DIAGRAM_EDIT_RELATED</span></div>
<div class="block">These actions will be available when any diagram (not just UML) is opened and is not read only.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.ANY_DIAGRAM_EDIT_RELATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPENED_MODULE_AS_PROJECT">
<h3>OPENED_MODULE_AS_PROJECT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPENED_MODULE_AS_PROJECT</span></div>
<div class="block">Actions are disabled, when opened project is module</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.OPENED_MODULE_AS_PROJECT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_RELATED_ELEMENTS">
<h3>DIAGRAM_RELATED_ELEMENTS</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DIAGRAM_RELATED_ELEMENTS</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">do not use it. Will be removed in future versions.</div>
</div>
<div class="block">Diagram -&gt; Related elements' subgroup.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.actions.ActionsGroups.DIAGRAM_RELATED_ELEMENTS">Constant Field Values</a></li>
</ul>
</dd>
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
