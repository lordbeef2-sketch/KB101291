# NI DOCUMENT BUNDLE: labwindows-cvi

<!--NI_BUNDLE_CHUNK bundle=labwindows-cvi start=1251 end=1352 -->
<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitab_control_events.htm language=enus -->
## TOPIC 01251: Tab Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitab_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitab_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Tab Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [tab](cvitab_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_KEYPRESS
- EVENT_GOT_FOCUS
- EVENT_LOST_FOCUS
- EVENT_DISCARD
- EVENT_DRAG
- EVENT_DROP
- EVENT_DROPPED
- EVENT_HSCROLL
- EVENT_ACTIVE_TAB_CHANGE
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK
- EVENT_TAB_PAGE_CLOSE

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitab_control_functions.htm language=enus -->
## TOPIC 01252: Tab Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitab_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitab_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Tab Control Functions

The following User Interface Library functions operate on [tab](cvitab_control_overview.htm) controls.

- AddCtrlToSplitter
- CopyTabPage
- DefaultCtrl
- DeleteTabPage
- DiscardCtrl
- DuplicateCtrl
- GetActiveTabPage
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBitmap
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlIndex
- GetNumTabPages
- GetPanelHandleFromTabPage
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- GetTabPageAttribute
- GetTabPageFromPoint
- InsertCtrlArrayItem
- InsertPanelAsTabPage
- InsertTabPage
- InstallCtrlCallback
- MoveTabPage
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetActiveTabPage
- SetCtrlAttribute
- SetCtrlBitmap
- SetCtrlIndex
- SetInputMode
- SetTabPageAttribute

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitab_control_overview.htm language=enus -->
## TOPIC 01253: Tab Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitab_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitab_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Tab Controls Overview

Use *tab [controls](cvioperating_controls.htm)* to organize user interface panels into multiple tabbed pages. Tabs can contain any control that you can place on a user interface panel, including another tab control. You can arrange the tabs in a single row or in multiple rows. You also can add images to tabs. A sample tab control appears in the following figure:

|  | Note LabWindows/CVI displays images in the tab control at 16 x 16 pixels, regardless of the original size of the image. |
| --- | --- |

[IMAGE alt='image' src='tabctrl.gif']

**Tab Control**

[Operating Tab Controls](cvioperating_tab_controls.htm)

[Programming Tab Controls](cviprogramming_with_tab_controls.htm)

[Tab Control Attributes](cvitab_attributes.htm)

[Tab Control Functions](cvitab_control_functions.htm)

[Tab Control Events](cvitab_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitable_attributes.htm language=enus -->
## TOPIC 01254: Table Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitable_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitable_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Table Control Attributes

The User Interface Library attributes that are valid for
[table](cvitable_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Cell Frame Color
- Column Labels Color
- Column Labels Height
- Command Button Color
- Disable Panel Theme
- First Visible Column
- First Visible Row
- Frame Color
- Grid Area Height
- Grid Area Left
- Grid Area Top
- Grid Area Width
- Hide Hilite
- Hilite Only When Panel Active
- Horizontal Grid Color
- Horizontal Grid Visible
- Horizontal Scroll Offset
- Horizontal Scroll Offset Max
- Inc/Dec Arrow Width
- Justification
- Minimum Number of Lines Visible
- Number of Visible Columns
- Number of Visible Rows
- Ring Arrow Location
- Row Labels Color
- Row Labels Width
- Scroll Bar Color
- Scroll Bar Size
- Show Ring Arrow
- Table Background Color
- Unique Ring Items
- Upper Left Corner Color
- Vertical Grid Color
- Vertical Grid Visible
- Vertical Scroll Offset
- Vertical Scroll Offset Max
- Visible
- Wrap Mode
- Show/Hide Parts
- Size/Position
- Text Style

#### Control Settings

- Auto Edit
- Case Sensitive Compare
- Cell Dimmed
- Cell Mode
- Cell Shortcut Key
- Cell Type
- Column Offset
- Control Mode
- Control Style
- Data Type
- Default Numeric Cell Value
- Default Text Cell Value
- Default Text Cell Value Length
- Dimmed
- Disable Control Tooltip
- Enable Column Sizing
- Enable Popup Menu
- Enable Row Sizing
- Enter Key Causes Newline
- Fit Mode
- Inc/Dec Arrow Color
- Incremental Value
- Maximum Entry Characters
- Maximum Entry Length
- Maximum Value
- Minimum Value
- Next Panel Control
- No Edit Text
- Range Checking
- Row Offset
- Tab Position
- Table Mode
- Table Run State
- Text Selection Length
- Text Selection Start
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position
- DataSocket Settings
- Format and Precision

#### Label Appearance

- Label Background Color
- Label Height
- Label Left
- Label Raised
- Label Size to Text
- Label Text
- Label Text Length
- Label Top
- Label Visible
- Label Width
- Label Style

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitable_control_events.htm language=enus -->
## TOPIC 01255: Table Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitable_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitable_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Table Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [table](cvitable_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_COMMIT
- EVENT_VAL_CHANGED
- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_KEYPRESS
- EVENT_GOT_FOCUS
- EVENT_LOST_FOCUS
- EVENT_DISCARD
- EVENT_SORT
- EVENT_SELECTION_CHANGE
- EVENT_HSCROLL
- EVENT_VSCROLL
- EVENT_COMBO_BOX_INSERT
- EVENT_ACTIVE_CELL_CHANGE
- EVENT_ROW_SIZE_CHANGE
- EVENT_COLUMN_SIZE_CHANGE
- EVENT_EDIT_MODE_STATE_CHANGE
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK
- EVENT_TABLE_ROW_COL_LABEL_CLICK
- EVENT_CTRL_MENU
- EVENT_VAL_COERCED

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitable_control_functions.htm language=enus -->
## TOPIC 01256: Table Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitable_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitable_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Table Control Functions

The following User Interface Library functions operate on [table](cvitable_control_overview.htm) controls.

- AddCtrlToSplitter
- ClipboardGetTableVals
- ClipboardPutTableVals
- DSBindCtrl
- DSBindTableCellRange
- DSUnbind
- DefaultCtrl
- DeleteTableCellRangeRingItems
- DeleteTableCellRingItems
- DeleteTableColumns
- DeleteTableRows
- DiscardCtrl
- DiscardCtrlMenuItem
- DuplicateCtrl
- FillTableCellRange
- GetActiveTableCell
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlMenuAttribute
- GetNumTableCellRingItems
- GetNumTableColumns
- GetNumTableRows
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- GetTableCellAttribute
- GetTableCellFromPoint
- GetTableCellFromValue
- GetTableCellRangeRect
- GetTableCellRangeVals
- GetTableCellRingIndexFromValue
- GetTableCellRingItemAttribute
- GetTableCellRingValueFromIndex
- GetTableCellRingValueLengthFromIndex
- GetTableCellVal
- GetTableCellValLength
- GetTableColumnAttribute
- GetTableColumnFromLabel
- GetTableRowAttribute
- GetTableRowFromLabel
- GetTableSelection
- HideBuiltInCtrlMenuItem
- InsertCtrlArrayItem
- InsertTableCellRangeRingItem
- InsertTableCellRingItem
- InsertTableColumns
- InsertTableRows
- InstallCtrlCallback
- NewCtrlMenuItem
- NewCtrlMenuSeparator
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetActiveTableCell
- SetColumnWidthToWidestCellContents
- SetCtrlAttribute
- SetCtrlMenuAttribute
- SetInputMode
- SetRowHeightToTallestCellContents
- SetTableCellAttribute
- SetTableCellRangeAttribute
- SetTableCellRangeVals
- SetTableCellRingItemAttribute
- SetTableCellVal
- SetTableCellValFromIndex
- SetTableColumnAttribute
- SetTableRowAttribute
- SetTableSelection
- ShowBuiltInCtrlMenuItem
- SortTableCells

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitable_control_overview.htm language=enus -->
## TOPIC 01257: Table Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitable_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitable_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Table Controls Overview

Use *table [controls](cvioperating_controls.htm)* to enter or view data arrays. Each individual table cell can be one of six types: numeric, string, picture, ring, combo box, or button. The table cells can contain numeric, text, or image data. A sample table control appears in the following figure:

[IMAGE alt='image' src='tblctrl.gif']

[Operating Table Controls](cvioperating_table_controls.htm)

[Programming Table Controls](cviprogramming_with_table_controls.htm)

[Table Control Attributes](cvitable_attributes.htm)

[Table Control Functions](cvitable_control_functions.htm)

[Table Control Events](cvitable_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_box_attributes.htm language=enus -->
## TOPIC 01258: Text Box Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_box_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_box_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Box Control Attributes

The User Interface Library attributes that are valid for
[text box](cvitext_box_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- First Visible Line
- Frame Color
- Frame Thickness
- Horizontal Scroll Offset
- Horizontal Scroll Offset Max
- Scroll Bar Color
- Scroll Bar Size
- Visible
- Visible Lines
- Wrap Mode
- Show/Hide Parts
- Size/Position
- Text Style

#### Control Settings

- Control Mode
- Control Style
- Control Value
- Default Value
- Default Value Length
- Dimmed
- Disable Control Tooltip
- Enter Key Causes Newline
- Extra Lines
- Maximum Entry Characters
- Maximum Entry Length
- Next Panel Control
- No Edit Text
- String Text Length
- Tab Position
- Text Selection Length
- Text Selection Start
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Total Lines
- Z-Plane Position
- DataSocket Settings

#### Label Appearance

- Label Background Color
- Label Height
- Label Left
- Label Raised
- Label Size to Text
- Label Text
- Label Text Length
- Label Top
- Label Visible
- Label Width
- Label Style

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_box_control_events.htm language=enus -->
## TOPIC 01259: Text Box Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_box_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_box_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Box Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [text box](cvitext_box_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_COMMIT
- EVENT_VAL_CHANGED
- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_KEYPRESS
- EVENT_GOT_FOCUS
- EVENT_LOST_FOCUS
- EVENT_DISCARD
- EVENT_HSCROLL
- EVENT_VSCROLL
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_button_control_events.htm language=enus -->
## TOPIC 01260: Text Button Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_button_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_button_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Button Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [text button](cvitext_button_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_COMMIT
- EVENT_VAL_CHANGED
- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_KEYPRESS
- EVENT_GOT_FOCUS
- EVENT_LOST_FOCUS
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_button_control_functions.htm language=enus -->
## TOPIC 01261: Text Button Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_button_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_button_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Button Control Functions

The following User Interface Library functions operate on [text button](cvitext_button_control_overview.htm) controls.

- AddCtrlToSplitter
- DefaultCtrl
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlVal
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlVal
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_button_control_overview.htm language=enus -->
## TOPIC 01262: Text Button Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_button_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_button_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Button Controls Overview

Use *text button [controls](cvioperating_controls.htm)* to select between two different states. A text button has two positions:
pressed or unpressed. You can associate a text label with each state of a text
button.

When the button is pressed its value is 1; when it is not pressed its value is 0.

A sample text button control appears in the figure below.

[IMAGE alt='image' src='txtbutcl.gif']

[Operating Text Button Controls](cvioperating_text_button_controls.htm)

[Programming Text Button Controls](cviprogramming_with_text_button_controls.htm)

[Text Button Control Attributes](cvitext_button_attributes.htm)

[Text Button Control Functions](cvitext_button_control_functions.htm)

[Text Button Control Events](cvitext_button_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_message_attributes.htm language=enus -->
## TOPIC 01263: Text Message Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_message_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_message_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Message Control Attributes

The User Interface Library attributes that are valid for
[text message](cvitext_message_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Size to Text
- Text Raised
- Visible
- Size/Position
- Text Style

#### Control Settings

- Control Style
- Control Value
- Default Value
- Default Value Length
- Dimmed
- Disable Control Tooltip
- Next Panel Control
- String Text Length
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_message_control_events.htm language=enus -->
## TOPIC 01264: Text Message Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_message_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_message_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Message Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [text message](cvitext_message_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_message_control_functions.htm language=enus -->
## TOPIC 01265: Text Message Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_message_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_message_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Message Control Functions

The following User Interface Library functions operate on [text message](cvitext_message_control_overview.htm) controls.

- AddCtrlToSplitter
- DSBindCtrl
- DSUnbind
- DefaultCtrl
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlVal
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlVal
- SetInputMode
- SetTextCtrlHeight

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitext_message_control_overview.htm language=enus -->
## TOPIC 01266: Text Message Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitext_message_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitext_message_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Text Message Controls Overview

*Text messages* are indicator [controls](cvioperating_controls.htm) that 
programmatically display strings of text. You cannot operate text message controls
using the keyboard, but you can assign [callback](cviusing_callback_functions_to_resp.htm) 
functions to them so that they respond to mouse click events. A sample text
message control appears in the following figure.

[IMAGE alt='image' src='txtmsgct.gif']

[Operating Text Message Controls](cvioperating_text_message_controls.htm)

[Programming Text Message Controls](cviprogramming_with_text_message_controls.htm)

[Text Message Control Attributes](cvitext_message_attributes.htm)

[Text Message Control Functions](cvitext_message_control_functions.htm)

[Text Message Control Events](cvitext_message_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvithread_blocking.htm language=enus -->
## TOPIC 01267: Thread Blocking

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvithread_blocking.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvithread_blocking.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Thread Blocking

Generally, each User Interface Library function blocks access to the library
from other [threads](cvidifferent_approaches_to_multithr.htm) until it returns. Other threads that attempt to call the library must wait
until the active call returns. However, the library functions do not block while
they wait for events from the operating system, nor do they block when they
invoke [callback functions](cviusing_callback_functions_to_resp.htm).

Normally, the period of time in which the blocking occurs is short. However,
some functions, such as [graph plotting functions](cviprogramming_with_graph_controls.htm), might take a considerable amount of time to complete, even though they do
not [process events](cviprocessing_events.htm) or invoke callbacks.

Other functions in the User Interface Library do *not* block [PostDeferredCall](cvipostdeferredcall.htm) and [PostDeferredCallToThread](cvipostdeferredcalltothread.htm). Thus, you can call PostDeferredCall or PostDeferredCallToThread in an asynchronous callback, without a long delay. If calls to these
functions occur at the same time in different threads, they might block for a short
time to protect the global list of deferred calls.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitimer_attributes.htm language=enus -->
## TOPIC 01268: Timer Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitimer_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitimer_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Timer Control Attributes

The User Interface Library attributes that are valid for
[timer](cvitimer_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Visible
- Size/Position

#### Control Settings

- Control Style
- Dimmed
- Disable Control Tooltip
- Next Panel Control
- Timer Enable
- Timer Interval
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position

#### Label Appearance

- Label Background Color
- Label Height
- Label Left
- Label Raised
- Label Size to Text
- Label Text
- Label Text Length
- Label Top
- Label Visible
- Label Width
- Label Style

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitoggle_button_attributes.htm language=enus -->
## TOPIC 01269: Toggle Button Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitoggle_button_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitoggle_button_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Toggle Button Control Attributes

The User Interface Library attributes that are valid for
[toggle button](cvitoggle_button_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Off Color
- On Color
- Visible
- Size/Position

#### Control Settings

- Control Mode
- Control Style
- Control Value
- Default Value
- Dimmed
- Disable Control Tooltip
- Next Panel Control
- Shortcut Key
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position

#### Label Appearance

- Label Background Color
- Label Height
- Label Left
- Label Raised
- Label Size to Text
- Label Text
- Label Text Length
- Label Top
- Label Visible
- Label Width
- Label Style

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitoggle_button_control_events.htm language=enus -->
## TOPIC 01270: Toggle Button Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitoggle_button_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitoggle_button_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Toggle Button Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [toggle button](cvitoggle_button_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_COMMIT
- EVENT_VAL_CHANGED
- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_KEYPRESS
- EVENT_GOT_FOCUS
- EVENT_LOST_FOCUS
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitoggle_button_control_functions.htm language=enus -->
## TOPIC 01271: Toggle Button Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitoggle_button_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitoggle_button_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Toggle Button Control Functions

The following User Interface Library functions operate on [toggle button](cvitoggle_button_control_overview.htm) controls.

- AddCtrlToSplitter
- DefaultCtrl
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlVal
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlVal
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitoggle_button_control_overview.htm language=enus -->
## TOPIC 01272: Toggle Button Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitoggle_button_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitoggle_button_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Toggle Button Controls Overview

Use *toggle button* [*controls*](cvioperating_controls.htm) to select between two different states. A toggle button has two positions:
pressed or unpressed. When the button is pressed its value is 1; when it is not pressed its value is 0.

A sample toggle button control appears in the following figure.

[IMAGE alt='image' src='togctrl.gif']

[Operating Toggle Button Controls](cvioperating_toggle_button_controls.htm)

[Programming Toggle Button Controls](cviprogramming_with_toggle_button_controls.htm)

[Toggle Button Control Attributes](cvitoggle_button_attributes.htm)

[Toggle Button Control Functions](cvitoggle_button_control_functions.htm)

[Toggle Button Control Events](cvitoggle_button_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappattachdebuggertoprocess.htm language=enus -->
## TOPIC 01273: AttachDebuggerToProcess

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappattachdebuggertoprocess.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappattachdebuggertoprocess.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### AttachDebuggerToProcess

*LabWindows/CVI ActiveX Server Interface*

CVI_AppAttachDebuggerToProcess (CAObjHandle objectHandle, ERRORINFO *errorInfo, long processID, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Attaches the LabWindows/CVI debugger to a process.

To receive the most useful debugging information, the DLL or EXE you want to attach to and debug must be built in LabWindows/CVI 2013 and later as well as in [debug configuration](settingprojconfigs.htm). You also can [attach to a process interactively](sieattachtoprocess.htm) in the LabWindows/CVI environment.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| processID | long | The ID of the process to which you want to attach the debugger. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappattachdebuggertoprocesssync.htm language=enus -->
## TOPIC 01274: AttachDebuggerToProcessSync

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappattachdebuggertoprocesssync.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappattachdebuggertoprocesssync.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### AttachDebuggerToProcessSync

*LabWindows/CVI ActiveX Server Interface*

CVI_AppAttachDebuggerToProcessSync (CAObjHandle objectHandle, ERRORINFO *errorInfo, long processID, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Performs the same operation as [AttatchDebuggerToProcess](actxappattachdebuggertoprocess.htm), but waits until the attach process is complete before returning.

To receive the most useful debugging information, the DLL or EXE you want to attach to and debug must be built in LabWindows/CVI 2013 and later as well as in [debug configuration](settingprojconfigs.htm). You also can [attach to a process interactively](sieattachtoprocess.htm) in the LabWindows/CVI environment.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| processID | long | The ID of the process to which you want to attach the debugger. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. Returns TRUE on successful attach. Returns FALSE if attach process failed without a specific error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappcontinueexecution.htm language=enus -->
## TOPIC 01275: ContinueExecution

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappcontinueexecution.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappcontinueexecution.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ContinueExecution

*LabWindows/CVI ActiveX Server Interface*

CVI_AppContinueExecution (CAObjHandle objectHandle, ERRORINFO *errorInfo, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Resumes the currently suspended execution.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappconvertfptofpx.htm language=enus -->
## TOPIC 01276: ConvertFPToFPX

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappconvertfptofpx.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappconvertfptofpx.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ConvertFPToFPX

*LabWindows/CVI ActiveX Server Interface*

CVI_AppConvertFPToFPX (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFileName, const char *fpxFileName, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Converts the specified .fp file into a .fpx file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFileName | const char * | The .fp file to convert into a .fpx file. You must pass an absolute pathname for this parameter. |
| fpxFileName | const char * | The generated .fpx file. You must pass an absolute pathname for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappconvertfpxtofp.htm language=enus -->
## TOPIC 01277: ConvertFPXToFP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappconvertfpxtofp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappconvertfpxtofp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ConvertFPXToFP

*LabWindows/CVI ActiveX Server Interface*

CVI_AppConvertFPXToFP (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpxFileName, const char *fpFileName, long *warningDuringConvert, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Converts the specified .fpx file into a .fp file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpxFileName | const char * | The .fpx file to convert into a .fp file. You must pass an absolute pathname for this parameter. |
| fpFileName | const char * | The generated .fp file. You must pass an absolute pathname for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| warningDuringConvert | long * | Indicates whether a non-fatal warning (such as string truncation, integer out of range, and so on) occurred during the conversion. 0 = a warning did not occur 1 = a warning occurred |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappcreatedllprojectfromfpfile.htm language=enus -->
## TOPIC 01278: CreateDLLProjectFromFPFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappcreatedllprojectfromfpfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappcreatedllprojectfromfpfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateDLLProjectFromFPFile

*LabWindows/CVI ActiveX Server Interface*

CVI_AppCreateDLLProjectFromFPFile (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFilePath, const char *projectPath, long loadProject, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Creates a DLL project for the specified instrument driver.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFilePath | const char * | The instrument driver for which to create a DLL project. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |
| projectPath | const char * | The pathname of the DLL project to create. You must pass an absolute pathname for this parameter. |
| loadProject | long | Specifies whether to load the DLL project after it is created. 0 = do not load the project after it is created 1 = load the project after it is created |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of an LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappcreateobjectfile.htm language=enus -->
## TOPIC 01279: CreateObjectFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappcreateobjectfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappcreateobjectfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateObjectFile

*LabWindows/CVI ActiveX Server Interface*

CVI_AppCreateObjectFile (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long reserved, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Compiles the contents of a source file into an object file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The source file from which to create the object file(s). You can pass a simple filename or absolute pathname. |
| reserved | long | Reserved for internal use. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of an LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappcreateprojecttarget.htm language=enus -->
## TOPIC 01280: CreateProjectTarget

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappcreateprojecttarget.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappcreateprojecttarget.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CreateProjectTarget

*LabWindows/CVI ActiveX Server Interface*

CVI_AppCreateProjectTarget (CAObjHandle objectHandle, ERRORINFO *errorInfo, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Creates the target file for the current project. For DLL projects, this function builds the target for the [active configuration](settingprojconfigs.htm). For executable or library projects, this function builds the target for the release configuration.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of an LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappcutfpfunction.htm language=enus -->
## TOPIC 01281: CutFPFunction

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappcutfpfunction.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappcutfpfunction.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### CutFPFunction

*LabWindows/CVI ActiveX Server Interface*

CVI_AppCutFPFunction (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, const char *functionName, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Cuts the specified function panel, its controls, and all associated help and stores it in the clipboard.

Panels you cut do not accumulate on the clipboard. This function replaces the existing panel in the clipboard every time you cut a panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file that contains the function panel to cut. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |
| functionName | const char * | The name of the function whose function panel you want to cut. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of an LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappdeletelinesfromfile.htm language=enus -->
## TOPIC 01282: DeleteLinesFromFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappdeletelinesfromfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappdeletelinesfromfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DeleteLinesFromFile

*LabWindows/CVI ActiveX Server Interface*

CVI_AppDeleteLinesFromFile (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *sourceFile, long firstLine, long numberOfLines, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Deletes lines from the specified source file, starting with the **firstLine**.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| sourceFile | const char * | The source file from which to delete the specified lines. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .c file in the project. |
| firstLine | long | The first line to delete. This parameter is one-based. |
| numberOfLines | long | The number of lines to delete. To delete lines from the firstLine to the end of the file, pass –1 for numberOfLines. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of an LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappdetachdebugger.htm language=enus -->
## TOPIC 01283: DetachDebugger

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappdetachdebugger.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappdetachdebugger.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DetachDebugger

*LabWindows/CVI ActiveX Server Interface*

CVI_AppDetachDebugger (CAObjHandle objectHandle, ERRORINFO *errorInfo, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Detaches the LabWindows/CVI debugger from the process to which it is [currently attached](actxappattachdebuggertoprocess.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| Output |  |  |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappdifftextfiles.htm language=enus -->
## TOPIC 01284: DiffTextFiles

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappdifftextfiles.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappdifftextfiles.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DiffTextFiles

*LabWindows/CVI ActiveX Server Interface*

CVI_AppDiffTextFiles (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *file1, const char *file2, long options, long numMatchLines, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Finds the differences between two text files by running an interactive diffing tool.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| file1 | const char * | The text file to compare to file2. You must pass an absolute pathname for this parameter. |
| file2 | const char * | The text file to compare to file1. You must pass an absolute pathname for this parameter. |
| options | long | Options for comparing text files. Use the bitwise OR operator (\|) to combine multiple flags. The following flag is currently available: CVI_DIFF_OPTION_IGNORE_WHITE_SPACE (1)—Specifies to ignore spaces, tabs, or other text control characters when comparing files. |
| numMatchLines | long | The number of lines that must match to mark the end of differing sections in a file. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of an LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappexcludefilefrombuild.htm language=enus -->
## TOPIC 01285: ExcludeFileFromBuild

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappexcludefilefrombuild.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappexcludefilefrombuild.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ExcludeFileFromBuild

*LabWindows/CVI ActiveX Server Interface*

CVI_AppExcludeFileFromBuild (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *absoluteOrSimplePathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Excludes the specified file from the build. LabWindows/CVI does not compile or link excluded files into the project.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| absoluteOrSimplePathname | const char * | The file to exclude from the build. You can pass a simple filename or absolute path. The file must be a .c, .obj, or .lib file. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of an LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappexitcvi.htm language=enus -->
## TOPIC 01286: ExitCVI

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappexitcvi.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappexitcvi.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ExitCVI

*LabWindows/CVI ActiveX Server Interface*

CVI_AppExitCVI (CAObjHandle objectHandle, ERRORINFO *errorInfo, long promptToSaveChanges, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Exits LabWindows/CVI and optionally prompts the user to save any unsaved changes.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| promptToSaveChanges | long | Specifies whether to prompt the user to save any unsaved changes before exiting LabWindows/CVI. 0 = discard unsaved changes 1 = prompt to save unsaved changes |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of an LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappfpgengetnodeindexfromfunctionname.htm language=enus -->
## TOPIC 01287: FPGenGetNodeIndexFromFunctionName

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappfpgengetnodeindexfromfunctionname.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappfpgengetnodeindexfromfunctionname.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FPGenGetNodeIndexFromFunctionName

*LabWindows/CVI ActiveX Server Interface*

CVI_AppFPGenGetNodeIndexFromFunctionName (CAObjHandle objectHandle, ERRORINFO *errorInfo, long treeId, const char *functionName, long *nodeIdx, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the node index for the specified function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| treeId | long | Specifier for a particular function tree that is currently in memory. Obtain this ID from FPGenCreateFunctionTree or FPGenOpenFunctionTree. |
| functionName | const char * | The name of the function whose node index you want to get. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| nodeIdx | long * | The zero-based node index of the specified function. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappfpgengetparam.htm language=enus -->
## TOPIC 01288: FPGenGetParam

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappfpgengetparam.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappfpgengetparam.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FPGenGetParam

*LabWindows/CVI ActiveX Server Interface*

CVI_AppFPGenGetParam (CAObjHandle objectHandle, ERRORINFO *errorInfo, long treeId, long nodeIdx, const char *paramName, long *paramId, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the parameter ID for the specified parameter. Call [FPGenDiscardParamCtrl](actxappfpgendiscardparamctrl.htm) to discard the parameter ID when it is no longer needed.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| treeId | long | Specifier for a particular function tree that is currently in memory. Obtain this ID from FPGenCreateFunctionTree or FPGenOpenFunctionTree. |
| nodeIdx | long | The one-based index of the node whose parameter ID you want to get. |
| paramName | const char * | The name of the parameter whose parameter ID you want to get. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| paramId | long * | The defined constant assigned to the specified parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappfpgenopenfunctiontree.htm language=enus -->
## TOPIC 01289: FPGenOpenFunctionTree

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappfpgenopenfunctiontree.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappfpgenopenfunctiontree.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FPGenOpenFunctionTree

*LabWindows/CVI ActiveX Server Interface*

CVI_AppFPGenOpenFunctionTree (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFilePathname, long *treeId, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Opens and returns a **treeId** for an existing function tree.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFilePathname | const char * | The absolute pathname of the function tree to open. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| treeId | long * | The ID of the opened function tree. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgeneratefunctiontreefromheaderfile.htm language=enus -->
## TOPIC 01290: GenerateFunctionTreeFromHeaderFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgeneratefunctiontreefromheaderfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgeneratefunctiontreefromheaderfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GenerateFunctionTreeFromHeaderFile

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGenerateFunctionTreeFromHeaderFile (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *instrName, const char *fnPrefix, const char *fnQualifier, const char *inputHeaderPath, const char *functionTreePath, const char *cleanedUpHeaderPath, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Generates a function tree from a header file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| instrName | const char * | The name of the function tree to generate. |
| fnPrefix | const char * | The common prefix for functions in the function tree. The first character in the prefix can be a letter or an underscore only. All of the rest of the characters in the prefix can be an alphanumeric character or an underscore. If you use an underscore in the header file to separate the prefix from the function name, you also must include an underscore in fnPrefix. |
| fpQualifier | const char * | The default qualifier for functions in the function tree. |
| inputHeaderPath | const char * | The absolute pathname of the header file from which to create the function tree. |
| functionTreePath | const char * | The absolute pathname of the generated function panel file. |
| cleanedUpHeaderPath | const char * | The absolute pathname of the generated header file. This header file is identical to the one used to generate the function tree except that all of the special tags used to specify function tree generation options are removed. LabWindows/CVI preserves white space from the input header file in the generated header file. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetexecutiontarget.htm language=enus -->
## TOPIC 01291: GetExecutionTarget

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetexecutiontarget.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetexecutiontarget.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetExecutionTarget

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetExecutionTarget (CAObjHandle objectHandle, ERRORINFO *errorInfo, enum CVIEnum_CVIExecutionTargetType *type, char **machineNameOrIP, long *port, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Returns the settings for the current execution target.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| type | enumCVIEnum_CVIExecutionTargetType | Indicates the execution target type. This function returns one of the following constants: CVIConst_CVI_EXECUTION_TARGET_LOCAL (0)—Target is the local computer. CVIConst_CVI_EXECUTION_TARGET_REMOTE (1)—Target is an external target. You may pass NULL for this parameter. |
| machineNameOrIP | char ** | The network address of the computer on which the debug executable or DLL is running. LabWindows/CVI rejects debug connections that do not originate from this network address. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. You may pass NULL for this parameter. |
| port | long * | The network port for the debug session. The LabWindows/CVI debugger accepts network connections from debuggees on this network port. The default is 3291. You may pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfileexclusionstate.htm language=enus -->
## TOPIC 01292: GetFileExclusionState

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfileexclusionstate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfileexclusionstate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFileExclusionState

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFileExclusionState (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long *isExcluded, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Indicates whether the specified file has been excluded from the build.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The file in the current project to evaluate. You can pass a simple filename or an absolute pathname for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| isExcluded | long * | Indicates whether the specified file has been excluded from the project. 1 = file has been excluded 0 = file has not been excluded |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfilenamebyindex.htm language=enus -->
## TOPIC 01293: GetFileNameByIndex

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfilenamebyindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfilenamebyindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFileNameByIndex

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFileNameByIndex (CAObjHandle objectHandle, ERRORINFO *errorInfo, long index, char **fileName, long *fileFound, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the name of a file in the project given the zero-based index of the file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| index | long | The zero-based index of the file whose name you want to get. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| fileName | char ** | The name of the specified file. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| fileFound | long * | Indicates whether this function found the specified file in the project. This parameter is set to 0 if the index is out of range. 0 = file not found 1 = file found |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetformattingoptions.htm language=enus -->
## TOPIC 01294: GetFormattingOptions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetformattingoptions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetformattingoptions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFormattingOptions

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFormattingOptions (CAObjHandle objectHandle, ERRORINFO *errorInfo, enum CVIEnum_CVIFormattingBracketStyle *bracketStyle, long *indentSwitch, long *indentCase, long *indentLabels, long *indentPreprocessor, long *indentComment, long *breakClosingBrackets, long *breakElseIfs, long *alignPointer, long *tabLength, long *expandTAB, long *reserved1, long *reserved2, long *reserved3, long *reserved4,long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Returns the existing indentation formatting for the source file and lines specified in the [FormatFileSelection](actxappformatfileselection.htm) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| Output |  |  |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| bracketStyle | enumCVIEnum_CVIFormattingBracketStyle * | The bracket style in the specified file and on the specified lines. This function returns one of the following constants: CVI_FORMATTING_STYLE_ALLMAN CVI_FORMATTING_STYLE_JAVA CVI_FORMATTING_STYLE_KR CVI_FORMATTING_STYLE_WHITESMITH CVI_FORMATTING_STYLE_BANNER CVI_FORMATTING_STYLE_1TBS |
| indentSwitch | long * | Indicates whether to indent the case statements within a switch statement. |
| indentCase | long * | Indicates whether to indent the case statement in relation to the case header. LabWindows/CVI does not indent case statements without enclosing brackets. |
| indentLabels | long * | Indicates whether to indent labels one indentation level less than the current indentation level instead of being flushed left. |
| indentPreprocessor | long * | Indicates whether to indent multiline preprocessor definitions that end with a backslash. |
| indentComment | long * | Indicates whether to indent comments that begin in the first column. |
| breakClosingBrackets | long * | Indicates whether to break closing headers, such as else, from the immediately preceding closing brackets. |
| breakElseIfs | long * | Indicates whether to break else if headers into separate lines. |
| alignPointer | long * | Indicates whether to align the pointer or reference operator to the data type, the variable name, or the space between. |
| tabLength | long * | Indicates the number of spaces to use for a tab character. |
| expandTAB | long * | Indicates whether to replace tab characters with spaces as you edit the file. |
| reserved1 | long * | This parameter is reserved. |
| reserved2 | long * | This parameter is reserved. |
| reserved3 | long * | This parameter is reserved. |
| reserved4 | long * | This parameter is reserved. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfpfunctionbyindex.htm language=enus -->
## TOPIC 01295: GetFPFunctionByIndex

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfpfunctionbyindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfpfunctionbyindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFPFunctionByIndex

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFPFunctionByIndex (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, long index, char **functionName, long *functionFound, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the name of a function in a .fp file given the zero-based index of the function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file that contains the function whose name you want to get. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |
| index | long | The zero-based index of the function whose name you want to get. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| functionName | char ** | The name of the function that corresponds to the given index. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| functionFound | long * | Indicates whether the specified function was found. 0 = specified function was not found 1 = specified function was found |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfpfunctionhelp.htm language=enus -->
## TOPIC 01296: GetFPFunctionHelp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfpfunctionhelp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfpfunctionhelp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFPFunctionHelp

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFPFunctionHelp (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, const char *functionName, char **helpStr, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the help string for the specified function panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file that contains the function panel whose help string you want to get. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |
| functionName | const char * | The name of the function whose function panel help you want to get. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| helpStr | char ** | The help string for the specified function panel. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfpinstrumenthelp.htm language=enus -->
## TOPIC 01297: GetFPInstrumentHelp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfpinstrumenthelp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfpinstrumenthelp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFPInstrumentHelp

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFPInstrumentHelp (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, char **helpStr, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the help string for the specified instrument.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file whose instrument help you want to get. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| helpStr | char ** | The help string for the specified instrument. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfpinstrumentprefix.htm language=enus -->
## TOPIC 01298: GetFPInstrumentPrefix

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfpinstrumentprefix.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfpinstrumentprefix.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFPInstrumentPrefix

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFPInstrumentPrefix (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, char **prefix, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the prefix of the specified instrument. LabWindows/CVI adds this prefix to the beginning of each function name in the instrument.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file whose instrument prefix you want to get. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| prefix | char ** | The prefix of the specified instrument. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfpnodenamebyindex.htm language=enus -->
## TOPIC 01299: GetFPNodeNameByIndex

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfpnodenamebyindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfpnodenamebyindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFPNodeNameByIndex

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFPNodeNameByIndex (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, long index, char **nodeName, long *found, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the name of the specified function node in a .fp file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file that contains the function node whose name you want to get. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |
| index | long | The zero-based index of the function node whose name you want to get. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| nodeName | char ** | The name of the specified function node. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| found | long * | Indicates whether the function found the specified function node. 0 = node not found 1 = node found |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfpparamdatatype.htm language=enus -->
## TOPIC 01300: GetFPParamDataType

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfpparamdatatype.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfpparamdatatype.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFPParamDataType

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFPParamDataType (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, const char *functionName, long paramIndex, char **dataType, long *paramFound, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the data type of the specified function parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file that contains the function parameter whose data type you want to get. The file must be opened currently. This parameter can be either an absolute pathname or the simple filename of a .fp file in the project. |
| functionName | const char * | The function that contains the parameter whose data type you want to get. |
| paramIndex | long | Either –1 for the return value or the zero-based position of the parameter. If paramIndex is less than –1 or greater than 99, this function returns an error. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| dataType | char ** | The data type of the specified parameter. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| paramFound | long * | Indicates whether the specified function parameter was found. 0 = parameter not found 1 = parameter found |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetfpparamvalue.htm language=enus -->
## TOPIC 01301: GetFPParamValue

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetfpparamvalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetfpparamvalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetFPParamValue

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetFPParamValue (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, const char *functionName, long paramIndex, char **value, long *paramFound, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets the value of the specified function parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file that contains the function parameter whose value you want to get. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |
| functionName | const char * | The function that contains the parameter whose value you want to get. |
| paramIndex | long | Either –1 for the return value or the zero-based position of the parameter. If paramIndex is less than –1 or greater than 99, this function returns an error. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| value | char ** | The value of the specified parameter. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| paramFound | long * | Indicates whether the specified function parameter was found. 0 = parameter not found 1 = parameter found |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetlinesfromfile.htm language=enus -->
## TOPIC 01302: GetLinesFromFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetlinesfromfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetlinesfromfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetLinesFromFile

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetLinesFromFile (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *sourceFile, long firstLine, long numberOfLines, char **text, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Gets lines of text from the specified source file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| sourceFile | const char * | The source file from which to get the lines. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .c file in the project. |
| firstLine | long | The first line of text to get from the specified source file. This parameter is one-based. |
| numberOfLines | long | The number of lines of text to get from the specified source file, starting with the firstLine. To obtain the lines from the firstLine to the end of the file, pass –1 for numberOfLines. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| text | char ** | The lines this function obtained from the source file. When you no longer need the string returned in this parameter, you must free it by calling the LabWindows/CVI ActiveX Library CA_FreeMemory function. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappgetnumberoflinesinfile.htm language=enus -->
## TOPIC 01303: GetNumberOfLinesInFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappgetnumberoflinesinfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappgetnumberoflinesinfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumberOfLinesInFile

*LabWindows/CVI ActiveX Server Interface*

CVI_AppGetNumberOfLinesInFile (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *sourceFile, long *numberOfLines, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Returns the number of lines in a source file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| sourceFile | const char * | The source file whose number of lines you want to return. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .c file in the project. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| numberOfLines | long * | The number of lines in the specified source file. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxapphidefunctionpanel.htm language=enus -->
## TOPIC 01304: HideFunctionPanel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxapphidefunctionpanel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxapphidefunctionpanel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### HideFunctionPanel

*LabWindows/CVI ActiveX Server Interface*

CVI_AppHideFunctionPanel (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, const char *functionName, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Hides the specified function panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file that contains the function panel to hide. The file must be opened currently. You can pass either the absolute pathname or the simple filename of a .fp file in the project. |
| functionName | const char * | The name of the function whose function panel you want to hide. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappincludefileinbuild.htm language=enus -->
## TOPIC 01305: IncludeFileInBuild

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappincludefileinbuild.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappincludefileinbuild.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### IncludeFileInBuild

*LabWindows/CVI ActiveX Server Interface*

CVI_AppIncludeFileInBuild (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Includes a file in the project that had been previously excluded. The file must be a .c, .obj, or .lib file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The .c, .obj, or .lib file to include in the project. You can pass a simple filename or an absolute pathname for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappinsertlinesinfile.htm language=enus -->
## TOPIC 01306: InsertLinesInFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappinsertlinesinfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappinsertlinesinfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertLinesInFile

*LabWindows/CVI ActiveX Server Interface*

CVI_AppInsertLinesInFile (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *sourceFile, long lineToInsertBefore, const char *text, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Inserts the specified text in a source file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| sourceFile | const char * | The source file in which to insert the specified text. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .c file in the project. |
| lineToInsertBefore | long | The line in the source file before which to insert the specified text. This parameter is one-based. |
| text | const char * | The text to insert in the source file. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxapploadinstrument.htm language=enus -->
## TOPIC 01307: LoadInstrument

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxapploadinstrument.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxapploadinstrument.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### LoadInstrument

*LabWindows/CVI ActiveX Server Interface*

CVI_AppLoadInstrument (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Loads the specified instrument.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The pathname of the instrument to load. You must pass an absolute pathname for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxapplockproject.htm language=enus -->
## TOPIC 01308: LockProject

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxapplockproject.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxapplockproject.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### LockProject

*LabWindows/CVI ActiveX Server Interface*

CVI_AppLockProject (CAObjHandle objectHandle, ERRORINFO *errorInfo, long enabled, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Disallows the use of the **New»Project**, **New»Project from Template**, **Open»Project**, and **Save Project As** commands from the LabWindows/CVI **File** menu. You can still change the project using the [OpenProject](actxappopenproject.htm) and [NewProject](actxappnewproject.htm) methods.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| enabled | long | Specifies whether to lock the project. 0 = unlock project 1 = lock project |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappmakecviactive.htm language=enus -->
## TOPIC 01309: MakeCVIActive

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappmakecviactive.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappmakecviactive.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MakeCVIActive

*LabWindows/CVI ActiveX Server Interface*

CVI_AppMakeCVIActive (CAObjHandle objectHandle, ERRORINFO *errorInfo, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Makes LabWindows/CVI the active application.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappnewapp.htm language=enus -->
## TOPIC 01310: NewApp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappnewapp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappnewapp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewApp

*LabWindows/CVI ActiveX Server Interface*

CVI_NewApp (const char *server, int supportMultithreading, LCID locale, int reserved, CAObjHandle *objectHandle);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Creates a new Application object and obtains a handle to the object.

If the server application is already running, this function may or may not start another copy of the application. This is determined by the server application.

You must call [CA_InitActiveXThreadStyleForCurrentThread](../libref/cvica_initactivexthreadstyleforcurrentthread.htm) with COINIT_APARTMENTTHREADED if you register any ActiveX event callbacks and want the callbacks to be called from the same thread in which they were registered. If you do not call CA_InitActiveXThreadStyleForCurrentThread with COINIT_APARTMENTTHREADED your callbacks will be called from a system thread.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| server | const char * | The name or IP address of the machine on which you want to run the ActiveX server. The name can be either a UNC name ("\\\\playdough") or DNS name ("plato.natinst.com"). If you pass NULL for this parameter and there is a RemoteServerName registry entry for this server, the server runs on the machine specified by the RemoteServerName entry. If you pass NULL for this parameter and there is no RemoteServerName registry entry for this server, the server runs on the same machine as your program. |
| supportMultithreading | int | Pass 0 if you use the object only from the thread that calls this function. Pass 1 if you use the object from multiple threads. The LabWindows/CVI ActiveX library uses the COM Global Interface Table (GIT) to marshal interface pointers between threads. There is overhead associated with using the GIT that you should avoid when possible, therefore if you do not pass the CAObjHandle between threads in your application, you do not need to use the GIT. |
| locale | LCID | Pass the locale for the object. This value tells the object how to interpret arguments to its methods. Pass LOCALE_NEUTRAL to indicate the default language-neutral locale. This value is not used by the server when you call it through a dual interface method. The LabWindows/CVI ActiveX Library passes this value to the IDispatch::Invoke method. |
| reserved | int | This parameter is reserved. You must pass 0 for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | A handle to the requested ActiveX object. Use this handle to call methods and get/set properties of this ActiveX object. When it is no longer needed, you must discard this handle using CA_DiscardObjHandle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappnewproject.htm language=enus -->
## TOPIC 01311: NewProject

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappnewproject.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappnewproject.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewProject

*LabWindows/CVI ActiveX Server Interface*

CVI_AppNewProject (CAObjHandle objectHandle, ERRORINFO *errorInfo, long promptToSaveChanges, long *return value);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Creates a new project and optionally prompts the user to save changes in the current project.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| promptToSaveChanges | long | Specifies whether to prompt the user to save changes in files in the current project before creating the new project. 0 = discard the unsaved changes in files in the current project 1 = save the unsaved changes in files in the current project |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappopenapp.htm language=enus -->
## TOPIC 01312: OpenApp

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappopenapp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappopenapp.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### OpenApp

*LabWindows/CVI ActiveX Server Interface*

CVI_OpenApp (const char *fileName, const char *server, int supportMultithreading, LCID locale, int reserved, CAObjHandle *objectHandle);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Loads an existing Application object from a file and obtains a handle to the object.

If the server application is already running, this function may or may not start another copy of the application. This is determined by the server application.

You must call [CA_InitActiveXThreadStyleForCurrentThread](../libref/cvica_initactivexthreadstyleforcurrentthread.htm) with COINIT_APARTMENTTHREADED if you register any ActiveX event callbacks and want the callbacks to be called from the same thread in which they were registered. If you do not call CA_InitActiveXThreadStyleForCurrentThread with COINIT_APARTMENTTHREADED your callbacks will be called from a system thread.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fileName | const char * | A file containing the data for an ActiveX server object. |
| server | const char * | The name or IP address of the machine on which you want to run the ActiveX server. The name can be either a UNC name ("\\\\playdough") or DNS name ("plato.natinst.com"). If you pass NULL for this parameter and there is a RemoteServerName registry entry for this server, the server runs on the machine specified by the RemoteServerName entry. If you pass NULL for this parameter and there is no RemoteServerName registry entry for this server, the server runs on the same machine as your program. |
| supportMultithreading | int | Pass 0 if you use the object only from the thread that calls this function. Pass 1 if you use the object from multiple threads. The LabWindows/CVI ActiveX library uses the COM Global Interface Table (GIT) to marshal interface pointers between threads. There is overhead associated with using the GIT that you should avoid when possible, therefore if you do not pass the CAObjHandle between threads in your application, you do not need to use the GIT. |
| locale | LCID | Pass the locale for the object. This value tells the object how to interpret arguments to its methods. Pass LOCALE_NEUTRAL to indicate the default language-neutral locale. This value is not used by the server when you call it through a dual interface method. The LabWindows/CVI ActiveX Library passes this value to the IDispatch::Invoke method. |
| reserved | int | This parameter is reserved. You must pass 0 for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | A handle to the requested ActiveX object. Use this handle to call methods and get/set properties of this ActiveX object. When it is no longer needed, you must discard this handle using CA_DiscardObjHandle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappopenproject.htm language=enus -->
## TOPIC 01313: OpenProject

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappopenproject.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappopenproject.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### OpenProject

*LabWindows/CVI ActiveX Server Interface*

CVI_AppOpenProject (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fullPathname, long promptToSaveChanges, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Opens the specified project or workspace. If you specify a project in the current workspace, LabWindows/CVI sets that project as the active project.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fullPathname | const char * | The absolute pathname of the project or workspace to open. |
| promptToSaveChanges | long | Specifies whether to prompt the user to save changes in files in the current project before opening the specified project or workspace. 0 = discard the unsaved changes in files in the current project 1 = save the unsaved changes in files in the current project |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappopenwindow.htm language=enus -->
## TOPIC 01314: OpenWindow

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappopenwindow.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappopenwindow.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### OpenWindow

*LabWindows/CVI ActiveX Server Interface*

CVI_AppOpenWindow (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Loads a file into a window. The file can be a text, .uir, or .fp file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The absolute pathname of the file to load. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappopenworkspacewindow.htm language=enus -->
## TOPIC 01315: OpenWorkspaceWindow

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappopenworkspacewindow.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappopenworkspacewindow.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### OpenWorkspaceWindow

*LabWindows/CVI ActiveX Server Interface*

CVI_AppOpenWorkspaceWindow (CAObjHandle objectHandle, ERRORINFO *errorInfo, enum CVIEnum_CVIWorkspaceWindow wndType, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Opens one of the following workspace windows:

- Variables and Call Stack window
- Watch window
- Threads window
- Modules window
- Memory window
- Run-time Errors window
- Resources window

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| wndType | enum CVIEnum_CVIWorkspaceWindow | The type of workspace window to open. You can specify one of the following constants: CVI_WORKSPACE_WND_VARIABLES (0)—Opens the Variables and Call Stack window. CVI_WORKSPACE_WND_WATCH (1)—Opens the Watch window. CVI_WORKSPACE_WND_THREADS (2)—Opens the Threads window. CVI_WORKSPACE_WND_MODULES (3)—Opens the Modules window. CVI_WORKSPACE_WND_MEMORY (4)—Opens the Memory window. CVI_WORKSPACE_WND_RUNTIMEERRORS (5)—Opens the Run-time Errors window. CVI_WORKSPACE_WND_RESOURCES (6)—Opens the Resources window. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappoverview.htm language=enus -->
## TOPIC 01316: LabWindows/CVI ActiveX Server Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappoverview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappoverview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### LabWindows/CVI ActiveX Server Overview

LabWindows/CVI provides an ActiveX server interface, which you can use to access LabWindows/CVI development environment functionality from other applications. The LabWindows/CVI ActiveX server interface consists of functions and events that expose a subset of the LabWindows/CVI development environment functionality.

How you access the LabWindows/CVI ActiveX server interface depends on the development environment that you use to create the ActiveX controller. To generate a new instrument driver wrapper for the LabWindows/CVI ActiveX server from LabWindows/CVI, use the [ActiveX Controller Wizard](../usermanual/prjcreateactivexcontroller.htm).

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappremovelineexclusion.htm language=enus -->
## TOPIC 01317: RemoveLineExclusion

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappremovelineexclusion.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappremovelineexclusion.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RemoveLineExclusion

*LabWindows/CVI ActiveX Server Interface*

CVI_AppRemoveLineExclusion (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *sourceFile, long lineNumber, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Removes the line exclusion from the specified line in the Source window.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| sourceFile | const char * | The source file from which to remove the line exclusion. The source file must be open. You can pass either an absolute pathname or the simple filename of a .c file in the project. |
| lineNumber | long | The one-based index of the line of previously excluded code to include. Pass –1 to remove all the line exclusions in the specified file. |

| Output |  |  |
| --- | --- | --- |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappremoveprojectfromworkspace.htm language=enus -->
## TOPIC 01318: RemoveProjectFromWorkspace

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappremoveprojectfromworkspace.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappremoveprojectfromworkspace.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RemoveProjectFromWorkspace

*LabWindows/CVI ActiveX Server Interface*

CVI_AppRemoveProjectFromWorkspace (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Removes the specified project from the current workspace.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The absolute pathname of the project to remove from the current workspace. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxapprenamefpfunction.htm language=enus -->
## TOPIC 01319: RenameFPFunction

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxapprenamefpfunction.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxapprenamefpfunction.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RenameFPFunction

*LabWindows/CVI ActiveX Server Interface*

CVI_AppRenameFPFunction (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, const char *oldFunctionName, const char *newFunctionName, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Renames the specified function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file that contains the function whose name you want to change. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |
| oldFunctionName | const char * | The function name to change. |
| newFunctionName | const char * | The new name of the specified function. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxapprenamefpinstrument.htm language=enus -->
## TOPIC 01320: RenameFPInstrument

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxapprenamefpinstrument.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxapprenamefpinstrument.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RenameFPInstrument

*LabWindows/CVI ActiveX Server Interface*

CVI_AppRenameFPInstrument (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *fpFile, const char *newInstrumentName, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Renames the specified instrument.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| fpFile | const char * | The .fp file to rename. The file must be opened currently. You can pass either an absolute pathname or the simple filename of a .fp file in the project. |
| newInstrumentName | const char * | The new name of the specified instrument. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappreservedfunc1.htm language=enus -->
## TOPIC 01321: ReservedFunc1

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappreservedfunc1.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappreservedfunc1.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ReservedFunc1

*LabWindows/CVI ActiveX Server Interface*

CVI_AppReservedFunc1 (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *arg1, const char *arg2, const char *arg3, long arg4, long *returnValue);

#### Purpose

This is a reserved function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappreservedfunc3.htm language=enus -->
## TOPIC 01322: ReservedFunc3

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappreservedfunc3.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappreservedfunc3.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ReservedFunc3

*LabWindows/CVI ActiveX Server Interface*

CVI_AppReservedFunc3 (CAObjHandle objectHandle, ERRORINFO *errorInfo, long *arg, long *returnValue);

#### Purpose

This is a reserved function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxapprunintwinprogram.htm language=enus -->
## TOPIC 01323: RunIntWinProgram

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxapprunintwinprogram.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxapprunintwinprogram.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RunIntWinProgram

*LabWindows/CVI ActiveX Server Interface*

CVI_AppRunIntWinProgram (CAObjHandle objectHandle, ERRORINFO *errorInfo, long promptToSaveChanges, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Runs the code in the Interactive Execution window and optionally prompts the user to save any unsaved changes.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| promptToSaveChanges | long | Specifies whether to prompt the user to save any unsaved changes before running the code in the Interactive Execution window. 0 = do not prompt the user to save unsaved changes 1 = prompt the user to save unsaved changes |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxapprunproject.htm language=enus -->
## TOPIC 01324: RunProject

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxapprunproject.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxapprunproject.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RunProject

*LabWindows/CVI ActiveX Server Interface*

CVI_AppRunProject (CAObjHandle objectHandle, ERRORINFO *errorInfo, long promptToSaveChanges, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Runs the current project and optionally prompts the user to save any unsaved changes.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| promptToSaveChanges | long | Specifies whether to prompt the user to save changes before running the project. This parameter has an effect only if the Save changes before debugging option in the Environment dialog box is set to Ask. 0 = disable prompting to save changes 1 = enable prompting to save changes |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappsaveall.htm language=enus -->
## TOPIC 01325: SaveAll

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappsaveall.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappsaveall.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SaveAll

*LabWindows/CVI ActiveX Server Interface*

CVI_AppSaveAll (CAObjHandle objectHandle, ERRORINFO *errorInfo, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Saves all open files that have unsaved changes.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappsavefile.htm language=enus -->
## TOPIC 01326: SaveFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappsavefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappsavefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SaveFile

*LabWindows/CVI ActiveX Server Interface*

CVI_AppSaveFile (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Saves the specified file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The pathname of the file to save. You must pass an absolute pathname for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappsaveproject.htm language=enus -->
## TOPIC 01327: SaveProject

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappsaveproject.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappsaveproject.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SaveProject

*LabWindows/CVI ActiveX Server Interface*

CVI_AppSaveProject (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *projectPathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Saves the current project to the specified file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| projectPathname | const char * | The absolute pathname of the file to which to save the current project. Pass an empty string to use the current project path. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappscrolltofuncinsrcwindow.htm language=enus -->
## TOPIC 01328: ScrollToFuncInSrcWindow

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappscrolltofuncinsrcwindow.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappscrolltofuncinsrcwindow.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ScrollToFuncInSrcWindow

*LabWindows/CVI ActiveX Server Interface*

CVI_AppScrollToFuncInSrcWindow (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *absolutePathname, const char *funcName, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Scrolls to the specified function in a source file.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| absolutePathname | const char * | The source file in which to scroll to the specified function. You must pass an absolute pathname for this parameter. |
| funcName | const char * | The function to which to scroll in the specified source file. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappsetbrowseinformationpolicy.htm language=enus -->
## TOPIC 01329: SetBrowseInformationPolicy

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappsetbrowseinformationpolicy.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappsetbrowseinformationpolicy.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetBrowseInformationPolicy

*LabWindows/CVI ActiveX Server Interface*

CVI_AppSetBrowseInformationPolicy (CAObjHandle objectHandle, ERRORINFO *errorInfo, enum CVIEnum_CVIBrowseInformationPolicy policy, *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Sets the policy for when LabWindows/CVI generates source browsing information.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| policy | enumCVIEnum_CVIBrowseInformationPolicy | Specifies the browse information policy. You can specify one of the following constants: CVI_BROWSEINFO_POLICY_DISABLED—LabWindows/CVI never generates source browse information. CVI_BROWSEINFO_POLICY_ONSAVE—LabWindows/CVI generates source browse information when a file is saved. CVI_BROWSEINFO_POLICY_ONEDIT—LabWindows/CVI generates source browse information when a file is being edited. CVI_BROWSEINFO_POLICY_ONCOMPILE—LabWindows/CVI generates source browse information when the file is compiled. |
| Output |  |  |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappsuspendexecution.htm language=enus -->
## TOPIC 01330: SuspendExecution

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappsuspendexecution.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappsuspendexecution.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SuspendExecution

*LabWindows/CVI ActiveX Server Interface*

CVI_AppSuspendExecution (CAObjHandle objectHandle, ERRORINFO *errorInfo, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Suspends the current execution. Call [ContinueExecution](actxappcontinueexecution.htm) to resume the current execution.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
|  |  |  |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappterminateexecution.htm language=enus -->
## TOPIC 01331: TerminateExecution

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappterminateexecution.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappterminateexecution.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### TerminateExecution

*LabWindows/CVI ActiveX Server Interface*

CVI_AppTerminateExecution (CAObjHandle objectHandle, ERRORINFO *errorInfo, long runAtExitFunctions, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Terminates the current execution and optionally runs the functions registered with the ANSI C atexit function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| runAtExitFunctions | long | Specifies whether to run the functions registered with the atexit function. 0 = do not run the registered functions 1 = run the registered functions |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappunloadinstrument.htm language=enus -->
## TOPIC 01332: UnloadInstrument

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappunloadinstrument.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappunloadinstrument.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### UnloadInstrument

*LabWindows/CVI ActiveX Server Interface*

CVI_AppUnloadInstrument (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Unloads the specified instrument.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The pathname of the instrument to unload. You must pass an absolute pathname for this parameter. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxappupdatefilefromdisk.htm language=enus -->
## TOPIC 01333: UpdateFileFromDisk

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxappupdatefilefromdisk.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxappupdatefilefromdisk.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### UpdateFileFromDisk

*LabWindows/CVI ActiveX Server Interface*

CVI_AppUpdateFileFromDisk (CAObjHandle objectHandle, ERRORINFO *errorInfo, const char *pathname, long *returnValue);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, this function might be exposed differently. Some of the parameters documented here, such as objectHandle or errorInfo, are not applicable if you write a client using a different development environment. |
| --- | --- |

#### Purpose

Updates the contents of the specified file from disk.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| objectHandle | CAObjHandle | Specifier for a particular ActiveX object that is currently in memory. Obtain this handle from CVI_NewApp, CVI_OpenApp, CVI_ActiveApp, or an ActiveX method or property. All of the methods that you can apply to a particular object are grouped under a single class in the function tree. The name of the class corresponds to the type of the object to which this handle refers. |
| pathname | const char * | The pathname of the file whose contents you want to update from disk. You can pass a simple filename or an absolute path. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorInfo | ERRORINFO * | When an ActiveX server function fails with the error code DISP_E_EXCEPTION, descriptive information about the error code is stored in this parameter. The information can include the error code, source, and description. It also can include a help file and help file context ID. When an ActiveX server function fails with the error codes DISP_E_PARAMNOTFOUND, DISP_E_TYPEMISMATCH, or E_INVALIDARG, the parameter position of the invalid argument may be stored in the errorParamPos member of this parameter. You can pass NULL for this parameter. |
| returnValue | long * | The value that the LabWindows/CVI ActiveX server function returns. A negative value indicates that the LabWindows/CVI ActiveX server function returned an error. You can use GetCVIAutomationServerErrorString to get the description of a LabWindows/CVI ActiveX server error code. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an error occurred. A negative error code indicates function failure. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxerrorcodes.htm language=enus -->
## TOPIC 01334: LabWindows/CVI ActiveX Server Error Codes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxerrorcodes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxerrorcodes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### LabWindows/CVI ActiveX Server Error Codes

The LabWindows/CVI ActiveX server functions return error codes, which are defined in cvisrvr.h. You can call [GetCVIAutomationServerErrorString](actxappgetcviautomationservererrorstring.htm) to get a textual description of an error code.

The following table lists the currently defined error codes and their associated meanings.

| Defined Constant | Hexadecimal Value | Decimal Value | Description |
| --- | --- | --- | --- |
| CVIConst_CVI_SRVR_E_NO_ERROR | 0x0 | 0 | The function succeeded. |
| CVIConst_CVI_SRVR_E_INVALID_PATHNAME | 0x80040001 | -2147221503 | Invalid pathname syntax. |
| CVIConst_CVI_SRVR_E_PATHNAME_NOT_ABSOLUTE | 0x80040002 | -2147221502 | Pathname not absolute. |
| CVIConst_CVI_SRVR_E_PATHNAME_IS_RELATIVE | 0x80040003 | -2147221501 | Pathname must be absolute or simple. |
| CVIConst_CVI_SRVR_E_FILE_NOT_IN_PROJECT | 0x80040004 | -2147221500 | The specified file is not listed in the currently loaded project. |
| CVIConst_CVI_SRVR_E_FILE_DOES_NOT_EXIST | 0x80040005 | -2147221499 | The specified file does not exist on disk. |
| CVIConst_CVI_SRVR_E_FILE_NOT_LOADED | 0x80040006 | -2147221498 | The specified file is not already loaded into a window or loaded as an instrument. |
| CVIConst_CVI_SRVR_E_PROGRAM_RUNNING | 0x80040007 | -2147221497 | The operation cannot be performed because a user program is currently running. |
| CVIConst_CVI_SRVR_E_PROGRAM_SUSPENDED | 0x80040008 | -2147221496 | The operation cannot be performed because a user program is currently suspended. |
| CVIConst_CVI_SRVR_E_NO_PROGRAM_RUNNING | 0x80040009 | -2147221495 | The operation cannot be performed because no user program is currently running. |
| CVIConst_CVI_SRVR_E_NO_PROGRAM_SUSPENDED | 0x8004000a | -2147221494 | The operation cannot be performed because no user program is currently suspended. |
| CVIConst_CVI_SRVR_E_NO_RUNNING_OR_SUSPENDED | 0x8004000b | -2147221493 | The operation cannot be performed because no user program is currently running or suspended. |
| CVIConst_CVI_SRVR_E_FILE_NOT_EXCLUDABLE | 0x8004000c | -2147221492 | The file is not a .c, .obj, or .lib file, or is not in the project. |
| CVIConst_CVI_SRVR_E_NOT_A_LOADED_INSTRUMENT | 0x8004000d | -2147221491 | The specified file is not a .fp file for a loaded instrument. |
| CVIConst_CVI_SRVR_E_NOT_A_C_FILE | 0x8004000e | -2147221490 | The specified file is not a .c file. |
| CVIConst_CVI_SRVR_E_NOT_A_SRC_OR_TEXT_FILE | 0x8004000f | -2147221489 | The file specified is not a source or text file. |
| CVIConst_CVI_SRVR_E_CANNOT_CLOSE_WINDOW | 0x80040010 | -2147221488 | The window cannot be closed because execution is suspended in the file and the Workspace window is not open. |
| CVIConst_CVI_SRVR_E_LINE_TOO_LONG | 0x80040011 | -2147221487 | The line being appended to the window is too long; lines are limited to 254 characters. |
| CVIConst_CVI_SRVR_E_OUT_OF_MEMORY | 0x80040012 | -2147221486 | Insufficient memory available. |
| CVIConst_CVI_SRVR_E_WAITING_FOR_RESPONSE | 0x80040013 | -2147221485 | LabWindows/CVI is waiting for the user to respond to a modal dialog box. |
| CVIConst_CVI_SRVR_E_NOT_AN_FP_FILE | 0x80040014 | -2147221484 | The file specified is not a .fp file. |
| CVIConst_CVI_SRVR_E_FUNCTION_NOT_IN_FILE | 0x80040015 | -2147221483 | The function name is not in the .fp file. |
| CVIConst_CVI_SRVR_E_INVALID_FP_PARAM_INDEX | 0x80040016 | -2147221482 | The parameter index is either less than –1 or greater than 99. |
| CVIConst_CVI_SRVR_E_ERROR_READING_FP_FILE | 0x80040017 | -2147221481 | An error occurred reading the .fp file. |
| CVIConst_CVI_SRVR_E_ERROR_REPORTED_TO_USER | 0x80040018 | -2147221480 | An action-specific error was reported to the end user through a dialog box, compile error window, or link error window, or the user canceled the operation. |
| CVIConst_CVI_SRVR_E_INVALID_PROJ_FILE_INDEX | 0x80040019 | -2147221479 | The index into the project list is less than zero. |
| CVIConst_CVI_SRVR_E_PROJECT_IS_UNTITLED | 0x8004001a | -2147221478 | The current project has never been saved and does not have a pathname. |
| CVIConst_CVI_SRVR_E_NOT_A_PROJECT_FILE | 0x8004001b | -2147221477 | The file specified is not a project file. |
| CVIConst_CVI_SRVR_E_KEYSTROKE_OVERFLOW | 0x8004001c | -2147221476 | The maximum number of unprocessed fake keystrokes (256) has been exceeded. |
| CVIConst_CVI_SRVR_E_INVALID_KS_INTERVAL | 0x8004001d | -2147221475 | The keystroke interval must be between 1 and 100,000 milliseconds. |
| CVIConst_CVI_SRVR_E_IS_A_PROJECT_FILE | 0x8004001f | -2147221473 | To open a project file, use the OpenProject function instead of the OpenWindow function. |
| CVIConst_CVI_SRVR_E_FILE_NOT_PRINTABLE | 0x80040020 | -2147221472 | The file specified for printing is not printable. Only text files and user interface resource files are printable. |
| CVIConst_CVI_SRVR_E_INVALID_TARGET_TYPE | 0x80040021 | -2147221471 | The targetType parameter passed to the SetProjectTargetType function is not one of the values in the CVITargetType enum. |
| CVIConst_CVI_SRVR_E_INVALID_FP_FUNC_INDEX | 0x80040022 | -2147221470 | The index passed is either less than zero or greater than 31,999. |
| CVIConst_CVI_SRVR_E_MULTI_DIM_ARRAY | 0x80040024 | -2147221468 | A multidimensional array was passed to a function that expects a one-dimensional array. |
| CVIConst_CVI_SRVR_E_INVALID_SAFEARRAY | 0x80040025 | -2147221467 | A parameter that is supposed to be a safe array cannot be interpreted as such by system functions. |
| CVIConst_CVI_SRVR_E_INVALID_NULL_PARAM | 0x80040026 | -2147221466 | A pointer parameter that is supposed to contain a value was instead passed as NULL. |
| CVIConst_CVI_SRVR_E_INVALID_ZOOM_VALUE | 0x80040027 | -2147221465 | An invalid zoom value was passed. |
| CVIConst_CVI_SRVR_E_INVALID_STRING_VALUE | 0x80040028 | -2147221464 | An invalid string value was passed. |
| CVIConst_CVI_SRVR_E_NOT_EXECUTABLE_PROJECT | 0x80040029 | -2147221463 | The RunProject function was called on a non-executable project. |
| CVIConst_CVI_SRVR_E_INVALID_EXTERNAL_PROCESS | 0x8004002A | -2147221462 | The stand-alone executable that is specified to call the DLL is invalid. |
| CVIConst_CVI_SRVR_E_CANNOT_WRITE_TO_FILE | 0x8004002B | -2147221461 | An error occurred while writing data to a file. |
| CVIConst_CVI_SRVR_E_NOTHING_TO_SAVE | 0x8004002C | -2147221460 | There is nothing to save in the Build Output window. |
| CVIConst_CVI_SRVR_E_INVALID_VERSION_INFO_SELECTOR | 0x8004002D | -2147221459 | Invalid project version info selector. |
| CVIConst_CVI_SRVR_E_INVALID_PARAM | 0x8004002E | -2147221458 | An invalid parameter was passed. |
| CVIConst_CVI_SRVR_E_FAILED_TO_LOAD_TUI_FILE | 0x8004002F | -2147221457 | Could not load the specified .tui file. |
| CVIConst_CVI_SRVR_E_FAILED_TO_SAVE_UIR_FILE | 0x80040030 | -2147221456 | Could not save the .uir file. |
| CVIConst_CVI_SRVR_E_FAILED_TO_CREATE_DIST_KIT | 0x80040031 | -2147221455 | Could not create the distribution. |
| CVIConst_CVI_SRVR_E_FAILED_TO_LOAD_UIR_FILE | 0x80040032 | -2147221454 | Could not load the specified .uir file. |
| CVIConst_CVI_SRVR_E_FAILED_TO_SAVE_TUI_FILE | 0x80040033 | -2147221453 | Could not save the .tui file. |
| CVIConst_CVI_SRVR_E_NAME_TOO_LONG | 0x80040034 | -2147221452 | The name passed is too long. |
| CVIConst_CVI_SRVR_E_INVALID_DATA_TYPE | 0x80040035 | -2147221451 | An invalid data type was passed. |
| CVIConst_CVI_SRVR_E_INVALID_FP_INSERT_LOCATION | 0x80040036 | -2147221450 | Could not insert a function panel at the specified location. |
| CVIConst_CVI_SRVR_E_RETVAL_ALREADY_SET | 0x80040037 | -2147221449 | A return value for the function panel has already been set. |
| CVIConst_CVI_SRVR_E_PROJECT_NOT_IN_WORKSPACE | 0x80040038 | -2147221448 | The specified project is not in the current workspace and cannot be removed. |
| CVIConst_CVI_SRVR_E_NOT_FOUND | 0x80040039 | -2147221447 | The function or parameter was not found. |
| CVIConst_CVI_SRVR_E_FAILED_TO_LOAD_FP_FILE | 0x8004003A | -2147221446 | Could not load the specified .fp file. |
| CVIConst_CVI_SRVR_E_FAILED_TO_SAVE_FPX_FILE | 0x8004003B | -2147221445 | Could not save the .fpx file. |
| CVIConst_CVI_SRVR_E_FAILED_TO_SAVE_FP_FILE | 0x8004003C | -2147221444 | Could not save the .fp file. |
| CVIConst_CVI_SRVR_E_FAILED_TO_LOAD_FPX_FILE | 0x8004003D | -2147221443 | Could not load the specified .fpx file. |
| CVIConst_CVI_SRVR_E_CANNOT_GENERATE_FP | 0x8004003E | -2147221442 | Could not generate the function tree. |
| CVIConst_CVI_SRVR_E_CLASS_NOT_IN_FILE | 0x8004003F | -2147221441 | The class name is not in the .fp file. |
| CVIConst_CVI_SRVR_E_INVALID_EXEC_TARGET_TYPE | 0x80040040 | -2147221440 | An invalid execution target type was passed. |
| CVIConst_CVI_SRVR_E_COULD_NOT_ADD_EXEC_TARGET | 0x80040041 | -2147221439 | Could not add the execution target. |
| CVIConst_CVI_SRVR_E_INVALID_RUNTIME_SUPPORT_TYPE | 0x80040042 | -2147221438 | The run-time support type is not valid for the current project settings. |
| CVIConst_CVI_SRVR_E_CANNOT_SET_RUNTIME_SUPPORT_TYPE | 0x80040043 | -2147221437 | The run-time support type cannot be set. This may be because the target type is static library. |
| CVIConst_CVI_SRVR_E_BKPT_DOES_NOT_EXIST | 0x80040044 | -2147221436 | Breakpoint does not exist. |
| CVIConst_CVI_SRVR_E_NO_LINE_TAG_AVAILABLE | 0x80040045 | -2147221435 | No line tag available. |
| CVIConst_CVI_SRVR_E_TLB_NOT_FOUND | 0x80040046 | -2147221434 | Type library not found. |
| CVIConst_CVI_SRVR_E_INVALID_TLB | 0x80040047 | -2147221433 | Type library is not valid. |
| CVIConst_CVI_SRVR_E_INVALID_PREFIX | 0x80040048 | -2147221432 | An invalid prefix value was passed. |
| CVIConst_CVI_SRVR_E_MUST_USE_ADVANCED_DIALOG | 0x80040049 | -2147221431 | You must use the LabWindows/CVI ActiveX Controller Advanced Options dialog box. |
| CVIConst_CVI_SRVR_E_METHOD_OBSOLETE | 0x8004004A | -2147221430 | The method you called is obsolete. |
| CVIConst_CVI_SRVR_E_INVALID_RUNTIME_BINDING | 0x8004004B | -2147221429 | The run-time binding value is not valid for the current project settings. |
| CVIConst_CVI_SRVR_E_CANNOT_SET_RUNTIME_BINDING | 0x8004004C | -2147221428 | The run-time binding value cannot be set. This may be because the target type is static library. |
| CVIConst_CVI_SRVR_E_INVALID_WORKSPACE_WINDOW | 0x8004004D | -2147221427 | An invalid Workspace window type value was passed. |
| CVIConst_CVI_SRVR_E_BUILDING_THE_PROJECT | 0x8004004E | -2147221426 | Building project files. |
| CVIConst_CVI_SRVR_E_INVALID_CONFIGURATION | 0x8004004F | -2147221425 | Invalid configuration. |
| CVIConst_CVI_SRVR_E_INVALID_WARNING_LEVEL | 0x80040050 | -2147221424 | Invalid warning level. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxeventactiveprojectchange.htm language=enus -->
## TOPIC 01335: ActiveProjectChange Event

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxeventactiveprojectchange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxeventactiveprojectchange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ActiveProjectChange Event

*LabWindows/CVI ActiveX Server Interface*

The ActiveProjectChange event is generated when the active project changes.

If you create a client for the LabWindows/CVI ActiveX server interface using the LabWindows/CVI ActiveX Controller Wizard, call [RegOnActiveProjectChange](actxregonactiveprojectchange.htm) to use this event. If you create the client using a different development environment, the method you use to register ActiveProjectChange events might differ.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxeventdebugsuspend.htm language=enus -->
## TOPIC 01336: DebugSuspend Event

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxeventdebugsuspend.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxeventdebugsuspend.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DebugSuspend Event

*LabWindows/CVI ActiveX Server Interface*

The DebugSuspend event is generated when LabWindows/CVI suspends execution of a debugee.

If you create a client for the LabWindows/CVI ActiveX server interface using the LabWindows/CVI ActiveX Controller Wizard, call [RegOnDebugSuspend](actxregondebugsuspend.htm) to use this event. If you create the client using a different development environment, the method you use to register DebugSuspend events might differ.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxeventexit.htm language=enus -->
## TOPIC 01337: Exit Event

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxeventexit.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxeventexit.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Exit Event

*LabWindows/CVI ActiveX Server Interface*

The Exit event is generated when LabWindows/CVI exits.

If you create a client for the LabWindows/CVI ActiveX server interface using the LabWindows/CVI ActiveX Controller Wizard, call [RegOnExit](actxregonexit.htm) to use this event. If you create the client using a different development environment, the method you use to register EventExit events might differ.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxeventworkspaceload.htm language=enus -->
## TOPIC 01338: WorkspaceLoad Event

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxeventworkspaceload.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxeventworkspaceload.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### WorkspaceLoad Event

*LabWindows/CVI ActiveX Server Interface*

The WorkspaceLoad event is generated when LabWindows/CVI loads a workspace.

If you create a client for the LabWindows/CVI ActiveX server interface using the LabWindows/CVI ActiveX Controller Wizard, call [RegOnWorkspaceLoad](actxregonworkspaceload.htm) to use this event. If you create the client using a different development environment, the method you use to register WorkspaceLoad events might differ.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxregonactiveprojectchange.htm language=enus -->
## TOPIC 01339: RegOnActiveProjectChange

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxregonactiveprojectchange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxregonactiveprojectchange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RegOnActiveProjectChange

*LabWindows/CVI ActiveX Server Interface*

CVI_ApplicationEventsRegOnActiveProjectChange (CAObjHandle serverObject, ApplicationEventsRegOnActiveProjectChange_CallbackType callbackFunction, void *callbackData, int enableCallbacks, int *callbackId);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, the method you use to register events might differ. |
| --- | --- |

#### Purpose

Call this function to register a callback for the [ActiveProjectChange](actxeventactiveprojectchange.htm) event of the ApplicationEvents event class. When you register the callback, you must specify the CAObjHandle of the server object from which you want to receive events.

The callback function that you specify must have the following prototype:

HRESULT CVICALLBACK Callback (CAObjHandle caServerObjHandle, void *caCallbackData, char *newActiveProjectPath, char *oldActiveProjectPath);

where **newActiveProjectPath** is the path to the new active project, and **oldActiveProjectPath** is the path to the previous active project.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| serverObject | CAObjHandle | Pass the CAObjHandle of the server object from which you want to receive events. You must pass a CAObjHandle to a server object that supports ApplicationEvents events. |
| callbackFunction | ApplicationEventsRegOnActiveProjectChange_CallbackType | Pass the function that the LabWindows/CVI ActiveX Library calls when the server fires an ActiveProjectChange event. The callback function that you specify must have the following prototype: HRESULT CVICALLBACK Callback (CAObjHandle caServerObjHandle, void *caCallbackData, char *newActiveProjectPath, char *oldActiveProjectPath); where newActiveProjectPath is the path to the new active project, and oldActiveProjectPath is the path to the previous active project. |
| callbackData | void * | Pass a value that you want the LabWindows/CVI ActiveX Library to pass to the callback as the caCallbackData parameter. Do not pass the address of a local variable or any other variable that might not be valid when the callback is executed. |
| enableCallbacks | integer | Specifies whether this registration function enables the registered callbacks for the server. Pass 1 to enable all of the registered callbacks in the ApplicationEvents class associated with the server object passed in the serverObject parameter of this function. Pass 0 to specify that this call to the registration function will not enable the callbacks. Once the callbacks in the ApplicationEvents class have been enabled for a particular server object, the value of this parameter is ignored for subsequent callback registration functions in the ApplicationEvents class. Typically, you pass 1 to enable callbacks immediately. Pass 0 when you have a set of callbacks that must be enabled simultaneously for you to properly respond to the server events. In this case, you must explicitly advise the server when you are ready to begin receiving events. You can advise the server either by passing 1 for this parameter when you register the final callback or by calling CA_EnableEventsForServerObject when you are ready to enable the callbacks. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| callbackId | integer * | A unique identifier for the callback. Pass this identifier to CA_UnregisterEventCallback to unregister the callback. Pass NULL if you do not want the callbackId. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an ActiveX Library error occurred. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/actxregonbuildbegin.htm language=enus -->
## TOPIC 01340: RegOnBuildBegin

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/actxregonbuildbegin.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/actxregonbuildbegin.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RegOnBuildBegin

*LabWindows/CVI ActiveX Server Interface*

CVI_ApplicationEventsRegOnBuildBegin (CAObjHandle serverObject, ApplicationEventsRegOnBuildBegin_CallbackType callbackFunction, void *callbackData, int enableCallbacks, int *callbackId);

|  | Note This function signature is shown as it appears when you create a client using the LabWindows/CVI ActiveX Controller Wizard. If you create a client for the LabWindows/CVI ActiveX server interface using a different development environment, the method you use to register events might differ. |
| --- | --- |

#### Purpose

Call this function to register a callback for the [BuildBegin](actxeventbuildbegin.htm) event of the ApplicationEvents event class. When you register the callback, you must specify the CAObjHandle of the server object from which you want to receive events.

The callback function that you specify must have the following prototype:

HRESULT CVICALLBACK Callback (CAObjHandle caServerObjHandle, void *caCallbackData, char *projectPath, char *targetPath);

where **projectPath** is the path to the project being built, and **targetPath** is the path to the target file, such as an executable or DLL, that is created during the build.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| serverObject | CAObjHandle | Pass the CAObjHandle of the server object from which you want to receive events. You must pass a CAObjHandle to a server object that supports ApplicationEvents events. |
| callbackFunction | ApplicationEventsRegOnBuildBegin_CallbackType | Pass the function that the LabWindows/CVI ActiveX Library calls when the server fires a BuildBegin event. The callback function that you specify must have the following prototype: HRESULT CVICALLBACK Callback (CAObjHandle caServerObjHandle, void *caCallbackData, char *projectPath, char *targetPath); where projectPath is the path to the project being built, and targetPath is the path to the target file, such as an executable or DLL, that is created during the build. |
| callbackData | void * | Pass a value that you want the LabWindows/CVI ActiveX Library to pass to the callback as the caCallbackData parameter. Do not pass the address of a local variable or any other variable that might not be valid when the callback is executed. |
| enableCallbacks | integer | Specifies whether this registration function enables the registered callbacks for the server. Pass 1 to enable all of the registered callbacks in the ApplicationEvents class associated with the server object passed in the serverObject parameter of this function. Pass 0 to specify that this call to the registration function will not enable the callbacks. Once the callbacks in the ApplicationEvents class have been enabled for a particular server object, the value of this parameter is ignored for subsequent callback registration functions in the ApplicationEvents class. Typically, you pass 1 to enable callbacks immediately. Pass 0 when you have a set of callbacks that must be enabled simultaneously for you to properly respond to the server events. In this case, you must explicitly advise the server when you are ready to begin receiving events. You can advise the server either by passing 1 for this parameter when you register the final callback or by calling CA_EnableEventsForServerObject when you are ready to enable the callbacks. |

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| callbackId | integer * | A unique identifier for the callback. Pass this identifier to CA_UnregisterEventCallback to unregister the callback. Pass NULL if you do not want the callbackId. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | HRESULT | A value indicating whether an ActiveX Library error occurred. Error codes are defined in CVIversion\\include\\cviauto.h and <Program Files>\\National Instruments\\Shared\\MSDTRedistributables\\SDKHeaderFiles\\8.1\\winerror.h. You can use CA_GetAutomationErrorString to get the description of an ActiveX Library error code. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/addinghelpinfo.htm language=enus -->
## TOPIC 01341: Adding Help to Instrument Drivers

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/addinghelpinfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/addinghelpinfo.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Adding Help to Instrument Drivers

Use the Help Editor to add help to instrument drivers that you create. The Help Editor is a text editor in which you can enter help, with HTML tags or without. The Help Editor also provides menu options to cut and copy text, undo the last action, search within the text, and so on. This section describes the types of help available from an instrument driver and how you can create help.

|  | Note You can use HTML tags, but you must enclose the tags in <HTML><BODY><‌/BODY><‌/HTML> tags. To specify a style sheet, move the style sheet to the same directory as your .fp file and use %FP_PATH% in the HTML link element, as shown in the following example: <link rel="stylesheet" href="%fp_path%/stylesheet.css" type="text/css"> |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/compilinghelpfortypelibraries.htm language=enus -->
## TOPIC 01342: Linking to Help Files for Type Library Resources

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/compilinghelpfortypelibraries.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/compilinghelpfortypelibraries.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Linking to Help Files for Type Library Resources

You can create Microsoft Compiled Help files (.chm), from function trees, then use the .chm file to link help topics to a type library resource. Complete the following steps to link a .chm file to a type library resource.

1. Generate documentation from the function tree using the Options»Generate Documentation»HTML command.
2. Compile the generated HTML Help project file ( .hhp ), using an HTML Help compiler application such as the HTML Help Workshop or FAR. [IMAGE alt='Note' src='note.gif']
**Note** The .hhp file and the InstrumentDriverFilename_files folder, that contains the HTML files, are generated into the directory containing the function tree.
3. Select Build»Target Settings to open the Target Settings dialog box.
4. Select Type Library to open the Type Library dialog box.
5. Enable the Include links to help file checkbox, then select .chm from the pull-down menu.
 [IMAGE alt='Note' src='note.gif']
**Note** If you have a .hlp file, you can link a .hlp help file to a type library resource; however, LabWindows/CVI does not generate .hlp files for you.
6. Select the function panel to which you want to link the .chm file.
 [IMAGE alt='Note' src='note.gif']
**Note** 
Make sure that the .chm or .hlp filename is the same as the function panel filename.
7. Select OK in both the Type Library and Target Settings dialog boxes.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configcvistartupoptions.htm language=enus -->
## TOPIC 01343: LabWindows/CVI Startup Options

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configcvistartupoptions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configcvistartupoptions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### LabWindows/CVI Startup Options

You can append certain options to the cvi command line, separating various parameters by spaces. The valid startup options appear in the following table.

| Option | Purpose |
| --- | --- |
| <filename> | LabWindows/CVI automatically loads the file at startup. The file can be any of the types available under the File»Open command. |
| -run | This option automatically invokes the Run»Debug command. |
| -run_then_exit | This option automatically invokes Run»Debug and then automatically invokes File»Exit LabWindows/CVI when the project terminates. This option also suppresses the LabWindows/CVI startup screen. |
| -newproject | LabWindows/CVI starts with an empty Workspace window. |
| -pProcessID | LabWindows/CVI attaches to the process that ProcessID identifies. You can express ProcessID as a decimal number or as a hexadecimal number that you precede with 0x. |
| -noSccConnection | This option disables source code control connection at startup. LabWindows/CVI does not attempt to connect to the source code control provider you configured. You can enable source code connection again in the Source Code Control Options dialog box. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configdatetimeopt.htm language=enus -->
## TOPIC 01344: DSTRules

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configdatetimeopt.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configdatetimeopt.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Date and Time Option—DSTRules

Use the [DSTRules](../libref/cviconfiguring_the_dst_rules_string.htm) option to specify the portions of the year in which daylight saving time is in effect in your area. This option affects ANSI C Library functions such as [mktime and localtime](../libref/cvitime_and_date_functions.htm). You can [configure LabWindows/CVI DSTRules options in the Registry](confighowtosetconfigoptions.htm).

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configdirectoryopts.htm language=enus -->
## TOPIC 01345: Directory Options

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configdirectoryopts.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configdirectoryopts.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Directory Options

You can [configure LabWindows/CVI directory options in the Registry](confighowtosetconfigoptions.htm). The directory options available in LabWindows/CVI are the cvidir option and the tmpdir option.

#### cvidir

The cvidir option specifies the directory that contains the following subdirectories. You should set the cvidir option only if the subdirectories that LabWindows/CVI requires, shown in the following table, are not in the directory that contains the LabWindows/CVI executable.

| Name of Directory | Contents |
| --- | --- |
| bin | Resource files (cvi.rsc, cvimsgs.txt), NI function panels (.lfp files), NI libraries (.obj and .lib) (Linux) The NI library files use the .o and .a extensions |
| fonts | Font description files |
| include | C header files for NI libraries |

If you do not specify a directory, LabWindows/CVI assumes that the directory that contains the executable file, cvi.exe or cvi, also contains the directories in the preceding table.

#### tmpdir

tmpdir sets the location for temporary files.

If you do not specify a directory, LabWindows/CVI uses the value of the environment variable TMP. If the value of TMP is not defined or is invalid, LabWindows/CVI uses the value of the environment variable TEMP. If the value of TEMP is not defined or is invalid, LabWindows/CVI uses the directory that contains cvi.exe.

If you run LabWindows/CVI across a network, you must set tmpdir to one of your local directories.

(Linux) If you do not specify a directory, LabWindows/CVI uses the value of the environment variable TMPDIR. If LabWindows/CVI does not find TMPDIR or the environment variable is invalid, LabWindows/CVI uses /tmp as the location for temporary files.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configfontoptions.htm language=enus -->
## TOPIC 01346: Font Options

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configfontoptions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configfontoptions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Font Options

LabWindows/CVI provides configuration options to set the fonts used throughout the environment. You can [configure LabWindows/CVI font options in the Registry](confighowtosetconfigoptions.htm).

|  | Notes All font configuration options are string values (type REG_SZ). You also can set these options for the LabWindows/CVI runtime. |
| --- | --- |

#### DialogFontName

DialogFontName specifies the font that LabWindows/CVI uses in dialog boxes and built-in panels such as the [Variables and Call Stack window](variablescallstackwind.htm), [Watch window](vwwatchwind.htm) and so on, as shown in the following example, DialogFontName=Courier.

#### DialogFontSize

DialogFontSize specifies the font size that LabWindows/CVI uses in dialog boxes and built-in panels such as the Variables and Call Stack window, Watch window and so on, as shown in the following example, DialogFontSize=30.

#### DialogFontBold

DialogFontBold specifies whether the font that LabWindows/CVI uses in dialog boxes and built-in panels such as the Variables and Call Stack window, Watch window and so on, as shown in the following example, 
DialogFontBold=Yes.

#### MenuFontName

MenuFontName specifies the font that LabWindows/CVI uses in menus, as shown in the following example, MenuFontName=Courier.

#### MenuFontSize

MenuFontSize specifies the font size that LabWindows/CVI uses in menus, as shown in the following example, MenuFontSize=30.

#### MenuFontBold

MenuFontBold specifies whether the font that LabWindows/CVI uses in menus is bold, as shown in the following example, MenuFontBold=Yes.

#### EditorFontName

EditorFontName specifies the default font that LabWindows/CVI uses in Source windows, as shown in the following example, EditorFontName=Courier.

#### EditorFontSize

EditorFontSize specifies the font size that LabWindows/CVI uses in Source windows, as shown in the following example, EditorFontSize=30.

#### EditorFontBold

EditorFontBold specifies whether the font that LabWindows/CVI uses in Source windows is bold, as shown in the following example, EditorFontBold=Yes.

#### MessageBoxFontName

MessageBoxFontName specifies the font that LabWindows/CVI uses in simple message boxes, as shown in the following example, MessageBoxFontName=Courier.

#### MessageBoxFontSize

MessageBoxFontSize specifies the font size that LabWindows/CVI uses in simple message boxes, as shown in the following example, MessageBoxFontSize=30.

#### MessageBoxFontBold

MessageBoxFontBold specifies whether the font that LabWindows/CVI uses in simple message boxes is bold, as shown in the following example, MessageBoxFontBold=Yes.

#### AppFontName

AppFontName specifies the font that LabWindows/CVI uses for dialog box labels and for function panels, as shown in the following example, AppFontName=Courier.

#### AppFontSize

AppFontSize specifies the font size that LabWindows/CVI uses in dialog box labels and for function panels, as shown in the following example, AppFontSize=30.

#### AppFontBold

AppFontBold specifies whether the font that LabWindows/CVI uses in dialog box labels and for function panels is bold, as shown in the following example, AppFontBold=Yes.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/confighowtosetconfigoptions.htm language=enus -->
## TOPIC 01347: How to Set the Configuration Options

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/confighowtosetconfigoptions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/confighowtosetconfigoptions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### How to Set the Configuration Options

LabWindows/CVI development environment configuration options are under the following key, where [version] is the version of the LabWindows/CVI development environment:

HKEY_LOCAL_MACHINE\SOFTWARE\National Instruments\CVI\[version]

|  | Note Versions of LabWindows/CVI that follow year-based versioning continue to use major.minor versioning in registry keys. Refer to the LabWindows/CVI Year-Based and Major.Minor.Tiny Version Equivalents topic for the current major.minor version equivalent. |
| --- | --- |

Use this key to set the configuration options for the LabWindows/CVI development environment.

A configuration string value is associated with each option, as shown in the following figure.

[IMAGE alt='image' src='../regstred2.gif']

You do not have to include an unused configuration string in the Registry.

You must specify an absolute pathname, including a drive letter, for configuration strings that take a directory name.

#### Runtime Configuration Options

The [LabWindows/CVI Runtime configuration options](../programmerref/configurationoptiondesc.htm) are under the following key:

HKEY_LOCAL_MACHINE\SOFTWARE\National Instruments\CVI Run-Time Engine\cvirte

|  | Note You must manually create the Registry key for a LabWindows/CVI Side-by-Side Runtime. |
| --- | --- |

Your programs, when you run them from the environment or as stand-alone applications, use the Runtime configuration options.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configoptiondescriptions.htm language=enus -->
## TOPIC 01348: Option Descriptions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configoptiondescriptions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configoptiondescriptions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Option Descriptions

When [configuring LabWindows/CVI through the Registry](confighowtosetconfigoptions.htm), you can make changes to the [directory options](configdirectoryopts.htm), [date and time options](configdatetimeopt.htm), [timer options](configtimeroptions.htm), and the [font options](configfontoptions.htm).

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configtimeroptions.htm language=enus -->
## TOPIC 01349: Timer Options - useDefaultTimer

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configtimeroptions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configtimeroptions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Timer Options—useDefaultTimer

You can [configure LabWindows/CVI timer options in the Registry](confighowtosetconfigoptions.htm). The timer option, useDefaultTimer, is a REG_SZ value. You can specify True or False.

If you set the useDefaultTimer option to True, LabWindows/CVI uses the default Windows timer to implement the LabWindows/CVI timing-related functions, such as Timer and Delay. The default Windows timer provides a resolution of 10 ms.

If you set useDefaultTimer to False, LabWindows/CVI attempts to use the performance counter timer. The performance counter timer provides a resolution of 1 μs. If the performance counter timer is not available, LabWindows/CVI uses the multimedia library timer, which provides a resolution of 1 ms.

The default value for useDefaultTimer is False.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configuringcvi.htm language=enus -->
## TOPIC 01350: Configuring LabWindows/CVI

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configuringcvi.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configuringcvi.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Configuring LabWindows/CVI

This section describes special options that override some of the configuration defaults established during the LabWindows/CVI installation or through the configuration dialog boxes within the environment.

These options inform LabWindows/CVI where to find system files, where to place temporary files, and so on. You might not need to set any of these options.

Getting Started with LabWindows/CVI contains installation instructions for LabWindows/CVI and a hands-on tutorial. It is a good idea to be familiar with the material in *Getting Started with LabWindows/CVI* before you go through *Using LabWindows/CVI* in the *LabWindows/CVI Help*.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configuringcvitousescc.htm language=enus -->
## TOPIC 01351: Configuring LabWindows/CVI to Use Source Control

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configuringcvitousescc.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configuringcvitousescc.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Configuring LabWindows/CVI to Use Source Control

Before you use source control with LabWindows/CVI, you must configure LabWindows/CVI to work with the third-party source control provider you [select](selectingsourcecontrolprovider.htm). Refer to the KnowledgeBase for the most current list of third-party source control providers that work with LabWindows/CVI.

Complete the following steps to configure LabWindows/CVI to work with a source control provider.

1. Make sure the computer on which you are running LabWindows/CVI also includes a third-party source control provider, which you must install and configure. Consult your source control administrator for additional assistance.
2. Select Environment»Options to open the Environment dialog box and click the Source Code Control button to open the Source Code Control Options dialog box. 

This option sets source code control for the LabWindows/CVI environment.
3. Click the Select button and select the source control provider you want to use with LabWindows/CVI from the Select Provider list. A dialog box from the third-party source control provider appears so you can configure connections, user information, and other settings for files under source control.
 
LabWindows/CVI scans the Windows registry to determine which source control providers are installed and uses that information to populate the Select Provider list.
4. The source control project settings you select in the source control provider dialog box appear in the Provider and Project options. Click the Select button to reconfigure the settings. If the provider does not support this functionality, the Select button is disabled.
5. Configure additional options you want in the dialog box.
6. Click the Advanced button to set advanced optional configuration options specific to the source control provider. A dialog box from the source control provider appears. If the provider does not support this functionality, the Advanced button is disabled.
7. Click OK and close the provider dialog box.
8. Click the OK button to save configuration settings and close the Source Code Control Options dialog box.

After you configure LabWindows/CVI to work with the source control provider, you can add files to source control, check out files, check in edited files, rename files, and get the latest version of files in source control within LabWindows/CVI. You also can [configure source control for individual LabWindows/CVI projects](configuringsccforindvprojects.htm). If you change the provider through the Environment dialog box, the change affects all projects you use in LabWindows/CVI.

If you want to perform source control operations that are not available in LabWindows/CVI, work directly from the source control provider for those specific functions.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/usermanual/configuringsccforindvprojects.htm language=enus -->
## TOPIC 01352: Configuring Source Control for Individual Projects

- bundle_id: `labwindows-cvi`
- source_path: `cvi/usermanual/configuringsccforindvprojects.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/usermanual/configuringsccforindvprojects.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Configuring Source Control for Individual Projects

By default, LabWindows/CVI projects use the source control configuration you specify for the LabWindows/CVI environment. Complete the following steps to configure source control settings for an individual project.

1. Select Edit»Project to open the Edit Project dialog box.
2. Click the Source Code Control button to open the Source Code Control Options dialog box.
3. Enable the Use project Source Code Control settings option.
4. Follow the same steps to configure source control options for the LabWindows/CVI environment.
5. Click the OK button to apply the source control configuration to the currently loaded LabWindows/CVI project.
