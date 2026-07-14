# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=1 end=250 -->
<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/instrument-i-o-vis-and-functions.html language=enus -->
## TOPIC 00001: Instrument I/O VIs and Functions

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/instrument-i-o-vis-and-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/instrument-i-o-vis-and-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the TestStand Instrument I/O VIs and functions to share instrument sessions among VIs and other code modules. The VIs and functions on this palette return general LabVIEW error codes . Palette Object Description Refnum to Session Returns the underlying viSession handle from a LabVIEW IVI or VISA

### Instrument I/O VIs and Functions

Use the TestStand Instrument I/O VIs and functions to share instrument sessions among VIs and other code modules.

The VIs and functions on this palette return
 [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes)
 .

| Palette Object | Description |
| --- | --- |
| Refnum to Session | Returns the underlying viSession handle from a LabVIEW IVI or VISA refnum. You can use the viSession handle in an environment other than LabVIEW. |
| Session Manager - Get Instrument Session | Returns an ActiveX session object that represents the connection to the instrument driver or I/O resource for the logical name Session Name . Instrument session objects are named ActiveX objects that enable software modules to easily share instrument driver instances or instrument connection handles. If a session object already exists for the logical name, the VI returns a reference to it. Otherwise, the VI creates and returns a new session object. |
| Session to Refnum | Converts a viSession handle from an environment other than LabVIEW into a LabVIEW IVI or VISA refnum. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/layout-vis.html language=enus -->
## TOPIC 00002: Layout VIs

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/layout-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/layout-vis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the TestStand Layout VIs to position and resize user interface controls. Palette Object Description Create Control Info Collects the bounds, size, and position information from an ActiveX control or LabVIEW tab control. The data type you wire to the AXCont Refnum In input determines the polymorp

### Layout VIs

Use the TestStand Layout VIs to position and resize user interface controls.

| Palette Object | Description |
| --- | --- |
| Create Control Info | Collects the bounds, size, and position information from an ActiveX control or LabVIEW tab control. The data type you wire to the AXCont Refnum In input determines the polymorphic instance to use. |
| Divide Space Between Panes | Use this VI to divide an area between two or more panes. If the area is larger or smaller than the current sum of the pane sizes, LabVIEW distributes the available area among the open panes in proportion to their current relative sizes. This VI might require modification for use with more than one border per control. |
| Drag Splitter | Use this VI from the BorderDragged event for a TestStand control that has a drag border enabled to resize the master control that owns the drag border and the slave control that shares the area the border splits. This VI might require modification for use with more than one border per control. |
| Load Bounds | Loads the bounds for a set of controls from the TestStand application configuration file. Use the TestStand - Save Bounds VI to save the bounds. You must use this VI and the TestStand - Save Bounds VI with the same set of controls in the same order. |
| Load Sizes | Loads the height and width for each control you specify from a TestStand application configuration file. You must use this VI and the TestStand - Save Sizes VI with the same set of controls in the same order. |
| Save Bounds | Saves the bounds for a set of controls to the TestStand application configuration file. |
| Save Sizes | Saves the height and width for each control you specify to the TestStand application configuration file. |
| Update Control Position and Size | Updates the size and position of the control to the values in the Control Info parameter. The data type you wire to the AXCont Refnum In input determines the polymorphic instance to use. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/legacy-vi.html language=enus -->
## TOPIC 00003: Legacy VI

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/legacy-vi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/legacy-vi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the TestStand Legacy VI to create test VIs with legacy connector panes. Palette Object Description Create Test Data Cluster Bundles together the data necessary to create the Test Data cluster the TestStand LabVIEW Adapter requires for legacy test VIs.

### Legacy VI

Use the TestStand Legacy VI to create test VIs with legacy connector panes.

| Palette Object | Description |
| --- | --- |
| Create Test Data Cluster | Bundles together the data necessary to create the Test Data cluster the TestStand LabVIEW Adapter requires for legacy test VIs. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/localization-vis.html language=enus -->
## TOPIC 00004: Localization VIs

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/localization-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/localization-vis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the TestStand Localization VIs to localize user interface controls and menus and to obtain localized strings from TestStand. Palette Object Description Get Resource String Returns a string in the TestStand string resource files for the current language. Specify the string by Category and Symbol

### Localization VIs

Use the TestStand Localization VIs to localize user interface controls and menus and to obtain localized strings from TestStand.

| Palette Object | Description |
| --- | --- |
| Get Resource String | Returns a string in the TestStand string resource files for the current language. Specify the string by Category and Symbol , which are the section and item labels, respectively, for the string in the string resource files. |
| Localize Front Panel | Converts all labels or text that begin with TS_ to a string in the TestStand string resource files for the current language. Specify the string by Category and the label or text, which are the section and item labels, respectively, for the string in the string resource files. Optionally, this VI can also convert the text in free labels. |
| Localize Menu | Converts all menu items with names that begin with TS__ to a string in the TestStand string resource files for the current language. Specify the string by Category and the menu item name, which are the section and item labels, respectively, for the string in the string resource files. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/menus-vis.html language=enus -->
## TOPIC 00005: Menus VIs

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/menus-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/menus-vis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the TestStand Menus VIs to edit a custom run-time menu by adding or removing menu items or groups of menu items associated with TestStand commands. Palette Object Description Cleanup Menus Removes any duplicate menu shortcut keys or redundant menu separator bars that result from multiple calls t

### Menus VIs

Use the TestStand Menus VIs to edit a custom run-time menu by adding or removing menu items or groups of menu items associated with TestStand commands.

| Palette Object | Description |
| --- | --- |
| Cleanup Menus | Removes any duplicate menu shortcut keys or redundant menu separator bars that result from multiple calls to the TestStand - Insert Commands in Menu VI or from inserting TestStand menu items into a menu with pre-existing items. Use this VI after you rebuild the menu bar in response to the < This VI >:Menu Activation? event in the main TestStand User Interface VI. |
| Execute Menu Command | Executes the command associated with a menu item previously inserted with the TestStand - Insert Commands in Menu VI. Use this VI in response to the < This VI >:Menu Selection (User) event in the main TestStand User Interface VI. |
| Insert Commands in Menu | Inserts a menu item or group of menu items associated with TestStand commands into a custom run-time menu. The data type you wire to the Application Manager input determines the polymorphic instance to use. Use this VI to rebuild the menu bar in response to the < This VI >:Menu Activation? event in the main TestStand User Interface VI to populate the menu bar with the commands that apply to the current state of the application. Before you use this VI, use the TestStand - Remove Commands from Menus VI to remove any pre-existing TestStand menu items. |
| Remove Commands from Menus | Removes menu items previously inserted with the TestStand - Insert Commands in Menu VI. Optionally, this VI can also remove menu items inserted with the LabVIEW Menu Editor dialog box or the Insert Menu Items function. Use this VI in response to the < This VI >:Menu Activation? event in the main TestStand User Interface VI to clear the menu bar before you use the TestStand - Insert Commands in Menu VI. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/ni-teststand-vis-and-functions-help.html language=enus -->
## TOPIC 00006: NI TestStand VIs and Functions Help

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/ni-teststand-vis-and-functions-help.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/ni-teststand-vis-and-functions-help.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI TestStand VIs, functions, and controls to create user interfaces and test VIs to use with TestStand. The VIs and functions on this palette return general LabVIEW error codes . Palette Object Description Close Termination Monitor Closes the execution and termination monitor data property o

### NI TestStand VIs and Functions Help

Use the NI TestStand VIs, functions, and
 [controls](teststand-controls.html)
 to create user interfaces and test VIs to use with TestStand.

The VIs and functions on this palette return
 [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes)
 .

| Palette Object | Description |
| --- | --- |
| Close Termination Monitor | Closes the execution and termination monitor data property objects the TestStand - Initialize Termination Monitor VI creates. |
| End Modal Dialog | Makes the calling dialog box VI non-modal to the TestStand main application window after a previous call to the TestStand - Start Modal Dialog VI. |
| Get Property Value | Returns the value of the SequenceContext property the Lookup String parameter specifies. You must manually select the polymorphic instance you want to use. |
| Get Termination Monitor Status | Monitors the execution in which the VI is currently running so the VI can stop if the user terminates or aborts the execution. Use this VI after you call the TestStand - Initialize Termination Monitor VI. |
| Initialize Termination Monitor | Creates the termination monitor data property and execution objects the TestStand - Get Termination Monitor Status VI uses. Use the TestStand - Close Termination Monitor VI to release the termination monitor data property and execution objects. |
| Set Property Value | Sets the value of the SequenceContext property the Lookup String parameter specifies. The data type you wire to the New Value input determines the polymorphic instance to use. This VI does not return an error if the Lookup String parameter is invalid and the Insert If Missing parameter is TRUE. |
| Set TestStand Application Window | Sets the TestStand main application window as the VI the VI Refnum parameter specifies. Use this VI once in the main TestStand User Interface VI to ensure that modal dialogs TestStand sequences display are modal to that VI. |
| Set Thread Externally Suspended | Sets the value of the Thread.ExternallySuspended property for the thread that executes this VI. Use this property to enable an execution to break while the VI performs a lengthy operation or waits an indeterminate period of time. Refer to the NI TestStand Help for more information about the Thread.ExternallySuspended property. |
| Start Modal Dialog | Makes the calling dialog box VI modal to the TestStand main application window. When you call this VI, you must then use the TestStand - End Modal Dialog VI to make the dialog box non-modal to the TestStand main application window before you attempt to interact with the TestStand main application window. If you do not call the TestStand - End Modal Dialog VI after you call the TestStand - Start Modal Dialog VI, the calling dialog box remains modal and you cannot use the TestStand main application window. You must manually select the polymorphic instance you want to use. |
| TestStand API Numeric Constants | Returns the value associated with a numeric constant or enumeration in the TestStand API. The constants are organized into groups that correspond to different TestStand API methods. Use this VI and the NI TestStand Help to select the appropriate constant or enumeration to use for a specific method. |
| TestStand API String Constants | Returns the value associated with a string constant in the TestStand API. The constants are organized into groups that correspond to different TestStand API methods. Use this VI and the NI TestStand Help to select the appropriate constant to use for a specific method. |

| Subpalette | Description |
| --- | --- |
| Instrument I/O VIs and Functions | Use the TestStand Instrument I/O VIs and functions to share instrument sessions among VIs and other code modules. |
| Layout VIs | Use the TestStand Layout VIs to position and resize user interface controls. |
| Legacy VI | Use the TestStand Legacy VI to create test VIs with legacy connector panes. |
| Localization VIs | Use the TestStand Localization VIs to localize user interface controls and menus and to obtain localized strings from TestStand. |
| Menus VIs | Use the TestStand Menus VIs to edit a custom run-time menu by adding or removing menu items or groups of menu items associated with TestStand commands. |

Copyright © National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/refnum-to-session.html language=enus -->
## TOPIC 00007: Refnum to Session

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/refnum-to-session.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/refnum-to-session.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Returns the underlying viSession handle from a LabVIEW IVI or VISA refnum. You can use the viSession handle in an environment other than LabVIEW. For the Refnum parameter of the Refnum to Session VI and the Session to Refnum VI, pass only a VISA or IVI refnum created using

### Refnum to Session

Owning Palette:
 [TestStand](instrument-i-o-vis-and-functions.html)

Returns the underlying viSession handle from a LabVIEW IVI or VISA refnum. You can use the viSession handle in an environment other than LabVIEW. For the
 Refnum
 parameter of the Refnum to Session VI and the Session to Refnum VI, pass only a VISA or IVI refnum created using the LabVIEW VISA Open function or the IVI New Session function. Passing an invalid refnum or a refnum constant can lead to undefined behavior and is not supported.

Details

[IMAGE alt='image' src='images/Refnum_to_Session.gif']

|  | Refnum specifies the LabVIEW IVI or VISA refnum. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Session returns the underlying viSession handle for the Refnum parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Details

In a TestStand sequence, you can use a VI to create a LabVIEW IVI or VISA refnum, use the Refnum to Session function to convert the refnum to a viSession handle, and store the viSession handle in a TestStand variable. You can use the viSession handle in VIs that subsequent steps in a sequence call. You must use the
 [Session to Refnum](session-to-refnum.html)
 function to convert the viSession handle back to a LabVIEW IVI or VISA refnum. Close the session when you no longer need the refnum.

You cannot use a viSession or a LabVIEW IVI or VISA refnum in a process other than the process in which you created it.

Parent topic:

Instrument I/O VIs and Functions

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/session-manager-get-instrument-session.html language=enus -->
## TOPIC 00008: Session Manager - Get Instrument Session

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/session-manager-get-instrument-session.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/session-manager-get-instrument-session.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Returns an ActiveX session object that represents the connection to the instrument driver or I/O resource for the logical name Session Name . Instrument session objects are named ActiveX objects that enable software modules to easily share instrument driver instances or ins

### Session Manager - Get Instrument Session

Owning Palette:
 [TestStand](instrument-i-o-vis-and-functions.html)

Returns an ActiveX session object that represents the connection to the instrument driver or I/O resource for the logical name
 Session Name
 . Instrument session objects are named ActiveX objects that enable software modules to easily share instrument driver instances or instrument connection handles. If a session object already exists for the logical name, the VI returns a reference to it. Otherwise, the VI creates and returns a new session object.

Details

[IMAGE alt='image' src='images/Session_Manager_-_Get_Instrument_Session.gif']

|  | Session Name specifies the name of the instrument session for which to return the session object and driver handle. If Session Name refers to an IVI session, it must match the name in the IVI Configuration Store file exactly, without any variations in the case of the characters in the name. All other instrument session names are case-insensitive. |
| --- | --- |
|  | Interface Level specifies the type of API handle to return. Valid values include 0 for DefaultInterface , 1 for ClassDriver , 2 for SpecificOwner , and 3 for IODriver . |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Driver Handle returns the the C-based instrument API handle to the driver for the interface level the Interface Level parameter specifies. The driver initializes if necessary. If the session does not support the interface level you request, the VI returns a zero-valued handle. |
|  | Instrument Session returns the ActiveX session object. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Details

This VI also returns an integer driver handle you pass to the
 [Session to Refnum](session-to-refnum.html)
 function to obtain a LabVIEW refnum you can use to call instrument driver or I/O VIs. As long as a reference to a session object exists, any number of VIs or other code modules can independently access the driver handle of the session. The driver initializes only once and then closes automatically when the last reference to the session object releases. You can call the SessionMgr ActiveX server directly to perform more advanced operations, such as querying for a list of available session names.

Parent topic:

Instrument I/O VIs and Functions

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/session-to-refnum.html language=enus -->
## TOPIC 00009: Session to Refnum

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/session-to-refnum.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/session-to-refnum.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Converts a viSession handle from an environment other than LabVIEW into a LabVIEW IVI or VISA refnum. For the Refnum parameter of the Refnum to Session VI and the Session to Refnum VI, pass only a VISA or IVI refnum created using the LabVIEW VISA Open function or the IVI Ne

### Session to Refnum

Owning Palette:
 [TestStand](instrument-i-o-vis-and-functions.html)

Converts a viSession handle from an environment other than LabVIEW into a LabVIEW IVI or VISA refnum. For the
 Refnum
 parameter of the Refnum to Session VI and the Session to Refnum VI, pass only a VISA or IVI refnum created using the LabVIEW VISA Open function or the IVI New Session function. Passing an invalid refnum or a refnum constant can lead to undefined behavior and is not supported.

Details

[IMAGE alt='image' src='images/Session_to_Refnum.gif']

|  | Class Type specifies the IVI or VISA class of the underlying viSession handle you wire to the Session parameter. The function uses this parameter for type information only. |
| --- | --- |
|  | Session specifies a viSession handle from an environment other than LabVIEW. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Refnum returns the LabVIEW IVI or VISA refnum for the underlying viSession handle Session . |
|  | error out contains error information. This output provides standard error out functionality. |

#### Details

In a TestStand sequence, you can use a VI to create a LabVIEW IVI or VISA refnum, use the
 [Refnum to Session](refnum-to-session.html)
 function to convert the refnum to a viSession handle, and store the viSession handle in a TestStand variable. You can use the viSession handle in VIs that subsequent steps in a sequence call. You must use the Session to Refnum function to convert the viSession handle back to a LabVIEW IVI or VISA refnum. Close the session when you no longer need the refnum.

You cannot use a viSession or a LabVIEW IVI or VISA refnum in a process other than the process in which you created it.

Parent topic:

Instrument I/O VIs and Functions

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-api-numeric-constants.html language=enus -->
## TOPIC 00010: TestStand API Numeric Constants

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-api-numeric-constants.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-api-numeric-constants.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Returns the value associated with a numeric constant or enumeration in the TestStand API. The constants are organized into groups that correspond to different TestStand API methods. Use this VI and the NI TestStand Help to select the appropriate constant or enumeration to u

### TestStand API Numeric Constants

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Returns the value associated with a numeric constant or enumeration in the TestStand API. The constants are organized into groups that correspond to different TestStand API methods. Use this VI and the
 NI TestStand Help
 to select the appropriate constant or enumeration to use for a specific method.

[IMAGE alt='image' src='images/TestStand_API_Numeric_Constants.gif']

|  | Constant specifies the names of the TestStand API numeric constants and enumerations. |
| --- | --- |
|  | Value returns the value of the TestStand API numeric constant or enumeration the Constant parameter specifies. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-api-string-constants.html language=enus -->
## TOPIC 00011: TestStand API String Constants

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-api-string-constants.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-api-string-constants.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Returns the value associated with a string constant in the TestStand API. The constants are organized into groups that correspond to different TestStand API methods. Use this VI and the NI TestStand Help to select the appropriate constant to use for a specific method. Const

### TestStand API String Constants

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Returns the value associated with a string constant in the TestStand API. The constants are organized into groups that correspond to different TestStand API methods. Use this VI and the
 NI TestStand Help
 to select the appropriate constant to use for a specific method.

[IMAGE alt='image' src='images/TestStand_API_String_Constants.gif']

|  | Constant specifies the names of the TestStand API string constants. |
| --- | --- |
|  | Value returns the value of the TestStand API string constant the Constant parameter specifies. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-cleanup-menus.html language=enus -->
## TOPIC 00012: TestStand - Cleanup Menus

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-cleanup-menus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-cleanup-menus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Removes any duplicate menu shortcut keys or redundant menu separator bars that result from multiple calls to the TestStand - Insert Commands in Menu VI or from inserting TestStand menu items into a menu with pre-existing items. Use this VI after you rebuild the menu bar in

### TestStand - Cleanup Menus

Owning Palette:
 [TestStand](menus-vis.html)

Removes any duplicate menu shortcut keys or redundant menu separator bars that result from multiple calls to the
 [TestStand - Insert Commands in Menu](teststand-insert-commands-in-menu.html)
 VI or from inserting TestStand menu items into a menu with pre-existing items. Use this VI after you rebuild the menu bar in response to the <
 This VI
 >:Menu Activation? event in the main TestStand User Interface VI.

[IMAGE alt='image' src='images/TestStand_-_Cleanup_Menus.gif']

|  | Menu Refnum In specifies the reference to a menu bar in a VI. Use the Current VI's Menubar function to obtain this reference number. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Menu Refnum Out returns the Menu Refnum In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Menus VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-close-termination-monitor.html language=enus -->
## TOPIC 00013: TestStand - Close Termination Monitor

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-close-termination-monitor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-close-termination-monitor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Closes the execution and termination monitor data property objects the TestStand - Initialize Termination Monitor VI creates. Status Monitor In specifies references to the TestStand objects required for monitoring the status of the parent execution. error in (no error) desc

### TestStand - Close Termination Monitor

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Closes the execution and termination monitor data property objects the
 [TestStand - Initialize Termination Monitor](teststand-initialize-termination-monitor.html)
 VI creates.

[IMAGE alt='image' src='images/TestStand_-_Close_Termination_Monitor.gif']

|  | Status Monitor In specifies references to the TestStand objects required for monitoring the status of the parent execution. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-controls.html language=enus -->
## TOPIC 00014: TestStand Controls

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-controls.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-controls.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following controls to create user interfaces and test VIs to use with TestStand. Refer to the NI TestStand Help for more information about each control. TestStand UI Application Manager —The Application Manager control performs the following basic operations, which facilitate using the TestS

### TestStand Controls

Use the following controls to create user interfaces and test VIs to use with TestStand. Refer to the
 NI TestStand Help
 for more information about each control.

- TestStand UI Application Manager 
 —The Application Manager control performs the following basic operations, which facilitate using the TestStand Engine in an application:
 
 An application that uses the TestStand User Interface (UI) Controls must have a single Application Manager control that exists for the duration of the application.
  - Processes command-line arguments.
  - Maintains an application configuration file.
  - Initializes and shuts down the TestStand Engine.
  - Logs users in and out.
  - Loads and unloads files.
  - Launches executions.
  - Tracks existing sequence files and executions.
  - Manages licensing.
- TestStand UI SequenceFileView Manager 
 —A SequenceFileView Manager control performs the following tasks to manage how other visible TestStand UI Controls view and interact with a selected sequence file:
 
 An application must have one SequenceFileView Manager control for each location, such as a window, form, or panel, in which you display a sequence file or let the user select a current sequence file.
  - Designates a sequence file as the selected sequence file.
  - Tracks which sequence, step groups, and steps are selected in the selected sequence file and tracks the expansion of the step groups.
  - Displays aspects of the selected file in the visible TestStand UI Controls to which it connects.
  - Enables visible TestStand UI Controls to which it connects to change the selected file, sequence, step group, and steps.
  - Provides methods for executing the selected sequence file.
- TestStand UI ExecutionView Manager 
 —An ExecutionView Manager control performs the following tasks to manage how other visible TestStand UI Controls view and interact with a selected TestStand execution:
 
 An application must have one ExecutionView Manager control for each location, such as a window, form, or panel, in which you display an execution or let the user select a current execution.
  - Designates an execution as the selected execution.
  - Tracks which thread, stack frame, sequence, step group, and steps are selected in the selected execution.
  - Displays aspects of the selected execution in the visible TestStand UI Controls to which the control connects.
  - Enables visible TestStand UI Controls to which the control connects to change the selected thread, stack frame, sequence, step group, and steps.
  - Generates events to notify the application of the progress and state of the selected execution.
  - Provides debugging commands
  - Updates the ReportView control to show the current report for the selected execution.
- TestStand UI Button 
 —Connect a manager control to a Button control to specify that the button performs a common user interface command, such as
 Open Sequence File 
 . The Button control uses a localized caption and automatically enables or disables depending on the application state.
- TestStand UI CheckBox 
 —Connect a manager control to a CheckBox control so users can toggle the state of a common user interface command, such as
 Break on Step Failure 
 When you connect to a command, the CheckBox control automatically updates the caption text, visibility, and enabled state. When you enable the checkbox, the checkbox executes the command, which toggles the state of the command.
- TestStand UI ComboBox 
 —Connect a SequenceFileView Manager or ExecutionView Manager control to a ComboBox control so users can view or select from a list of sequence files, sequences, step groups, steps, executions, threads, or stack frames. Connect an Application Manager control to a ComboBox control so users can view or select the default adapter of the TestStand Engine.
- TestStand UI Label 
 —Connect a manager control to a Label control to display text information about the application state in the label, such as the name of the current user or the status of the current unit under test.
- TestStand UI ListBar 
 —Use a ListBar control to display multiple pages, where each page contains a list of items users can view or select. Connect a SequenceFileView Manager or ExecutionView Manager control to a ListBar page so users can view and select from a list, such as the active sequence file or execution. Connect an Application Manager control to a ListBar page so users can view or select the default adapter of the TestStand Engine.
- TestStand UI VariablesView 
 —Connect a SequenceFileView Manager or an ExecutionView Manager control to a VariablesView control to display the variables and properties in the selected file or execution. You can modify values of existing properties and variables, and you can insert and delete variables when editing a sequence file.
- TestStand UI ExpressionEdit 
 —Use an ExpressionEdit control so users can edit a TestStand expression with syntax coloring, context help, and statement completion. Although you typically do not need to edit expressions in a user interface application, you can connect a manager control to a read-only ExpressionEdit control to display text information about the application state, such as the pathname of the sequence file selection or the name of the current user.
You can also use ExpressionEdit controls in dialog boxes for step types and in tools in which you prompt users to enter a TestStand expression.
- TestStand UI ListBox 
 —Connect a SequenceFileView Manager or ExecutionView Manager control to a ListBox control so users can view or select from a list of sequence files, sequences, step groups, steps, executions, threads, or stack frames. Connect an Application Manager control to a ListBox control so users can view or select the default adapter of the TestStand Engine. Use a ListBox control to display multiple pages, where each page contains a list of items that users can view or select.
- TestStand UI ReportView 
 —Connect an ExecutionView Manager control to a ReportView control to display the report for the selected execution.
- TestStand UI SequenceView 
 —Connect a SequenceFileView Manager control or an ExecutionView Manager control to a SequenceView control to display the steps of a sequence from a selected file or execution. The SequenceView control displays the steps in a list with columns you specify when you configure the control.
The SequenceView control maintains a cursor that indicates the last active item you clicked using the mouse or highlighted using the arrow keys. The control denotes the cursor using a dotted box that outlines the step. Use the SequenceView control to select one or more steps at a time. 
Use the SequenceFileView Manager control connected to the SequenceView control to control which sequence, step groups, and steps are selected in the file and to track the expansion of the step groups.
- TestStand UI StatusBar 
 —Connect a manager control to panes of a StatusBar control to display text, image, or progress information about the application state. You can programmatically control individual
 StatusBar 
 panes to display custom information.
You can connect the panes to CaptionSources, NumericSources, and ImageSources on the Application Manager, ExecutionView Manager, and SequenceFileView Manager controls.
- TestStand UI InsertionPalette 
 —Connect a SequenceFileView Manager control to an InsertionPalette control so users can insert steps and template items into a sequence file by dragging or double-clicking.
- Legacy 
 —Use the controls on the
 Legacy 
 palette for previous versions of TestStand and the LabVIEW Test Executive Toolkit.
 Note 
 TestStand 2012 or later no longer includes support for converting a LabVIEW Test Executive Toolkit sequence file to a TestStand sequence file. Visit
 ni.com/info
 and enter the Info Code
 exgin9
 for more information about
 [converting a LabVIEW Test Executive Toolkit sequence file to a TestStand sequence file](http://digital.ni.com/express.nsf/bycode/exgin9)
 .
  - Input Buffer 
 —Use only for compatibility with the LabVIEW Test Executive Toolkit as a string control to pass parameters to VIs.
  - Invocation Info 
 —Use only for compatibility with the LabVIEW Test Executive Toolkit as a cluster that contains information about the execution state. If you are creating new tests, use the sequence context instead.
  - Sequence Context 
 —A sequence context is an object in the TestStand API that represents the execution state of a sequence. For each active sequence, TestStand maintains a sequence context you can use to access all the objects, variables, and properties that relate to the execution of the sequence.
  - Test Data 
 —Specifies the standard data the TestStand LabVIEW Adapter requires for legacy test VIs.

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-create-control-info.html language=enus -->
## TOPIC 00015: TestStand - Create Control Info

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-create-control-info.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-create-control-info.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Collects the bounds, size, and position information from an ActiveX control or LabVIEW tab control. The data type you wire to the AXCont Refnum In input determines the polymorphic instance to use. TestStand - Create Control Info from AX Control TSUI.Borders In specifies an

### TestStand - Create Control Info

Owning Palette:
 [TestStand](layout-vis.html)

Collects the bounds, size, and position information from an ActiveX control or LabVIEW tab control. The data type you wire to the
 AXCont Refnum In
 input determines the polymorphic instance to use.

#### TestStand - Create Control Info from AX Control

[IMAGE alt='image' src='images/TestStand_-_Create_Control_Info_from_AX_Control.gif']

|  | TSUI.Borders In specifies an ActiveX reference to the borders from the user interface control. |
| --- | --- |
|  | AXCont Refnum In specifies the refnum for the LabVIEW ActiveX container that contains the user interface control. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | TSUI.Borders Out returns the TSUI.Borders In parameter unchanged. |
|  | AXCont Refnum Out returns the AXCont Refnum In parameter unchanged. |
|  | Control Info Out contains position and border information for the user interface control. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TestStand - Create Control Info from LV Tab Control

[IMAGE alt='image' src='images/TestStand_-_Create_Control_Info_from_LV_Tab_Control.gif']

|  | TabCtl Refnum In specifies a reference to a LabVIEW tab control. |
| --- | --- |
|  | Visible Borders specifies the visible borders of the user interface control. Use 8 for the right border, 4 for the left border, 1 for the top border, 2 for the bottom border, and 0 for no border. Use the bitwise-OR operator to specify more than one value. |
|  | Border Width specifies the width of the borders of the user interface control. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | TabCtl Refnum Out returns the TabCtl Refnum In parameter unchanged. |
|  | Control Info Out contains position and border information for the user interface control. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Layout VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-create-test-data-cluster.html language=enus -->
## TOPIC 00016: TestStand - Create Test Data Cluster

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-create-test-data-cluster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-create-test-data-cluster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Bundles together the data necessary to create the Test Data cluster the TestStand LabVIEW Adapter requires for legacy test VIs. PASS/FAIL Flag specifies whether the test passed or failed for Pass/Fail Test steps. Numeric Measurement specifies the data for Numeric Limit Test

### TestStand - Create Test Data Cluster

Owning Palette:
 [TestStand](legacy-vi.html)

Bundles together the data necessary to create the
 Test Data
 cluster the TestStand LabVIEW Adapter requires for legacy test VIs.

[IMAGE alt='image' src='images/TestStand_-_Create_Test_Data_Cluster.gif']

|  | PASS/FAIL Flag specifies whether the test passed or failed for Pass/Fail Test steps. |
| --- | --- |
|  | Numeric Measurement specifies the data for Numeric Limit Test steps. |
|  | String Measurement specifies the data for String Value Test steps. |
|  | Report Text specifies a message to display in the test report for all step types. |
|  | Test Data returns result data from the VI for the LabVIEW Adapter to use in TestStand. TestStand uses the data to make a PASS/FAIL determination. PASS/FAIL Flag returns the value the adapter copies into the Step.Result.PassFail property if the property exists. Numeric Measurement returns the data the adapter copies into the Step.Result.Numeric property if the property exists. String Measurement returns the data the adapter copes into the Step.Result.String property if the property exists. Report Text returns the data the adapter copies into the Step.Result.ReportText property if the property exists. |
|  | PASS/FAIL Flag returns the value the adapter copies into the Step.Result.PassFail property if the property exists. |
|  | Numeric Measurement returns the data the adapter copies into the Step.Result.Numeric property if the property exists. |
|  | String Measurement returns the data the adapter copes into the Step.Result.String property if the property exists. |
|  | Report Text returns the data the adapter copies into the Step.Result.ReportText property if the property exists. |

Parent topic:

Legacy VI

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-divide-space-between-panes.html language=enus -->
## TOPIC 00017: TestStand - Divide Space Between Panes

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-divide-space-between-panes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-divide-space-between-panes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Use this VI to divide an area between two or more panes. If the area is larger or smaller than the current sum of the pane sizes, LabVIEW distributes the available area among the open panes in proportion to their current relative sizes. This VI might require modification fo

### TestStand - Divide Space Between Panes

Owning Palette:
 [TestStand](layout-vis.html)

Use this VI to divide an area between two or more panes. If the area is larger or smaller than the current sum of the pane sizes, LabVIEW distributes the available area among the open panes in proportion to their current relative sizes. This VI might require modification for use with more than one border per control.

[IMAGE alt='image' src='images/TestStand_-_Divide_Space_Between_Panes.gif']

|  | Space End specifies the last pixel available, vertically or horizontally, for the panes to share. |
| --- | --- |
|  | Control Info In specifies position and border information for the user interface control. |
|  | Vertical Splitter specifies whether the splitter is vertical or horizontal. |
|  | Space Start specifies the first pixel, vertically or horizontally, the panes can share. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Control Info Out contains position and border information for the user interface control. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Layout VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-drag-splitter.html language=enus -->
## TOPIC 00018: TestStand - Drag Splitter

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-drag-splitter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-drag-splitter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Use this VI from the BorderDragged event for a TestStand control that has a drag border enabled to resize the master control that owns the drag border and the slave control that shares the area the border splits. This VI might require modification for use with more than one

### TestStand - Drag Splitter

Owning Palette:
 [TestStand](layout-vis.html)

Use this VI from the BorderDragged event for a TestStand control that has a drag border enabled to resize the master control that owns the drag border and the slave control that shares the area the border splits. This VI might require modification for use with more than one border per control.

[IMAGE alt='image' src='images/TestStand_-_Drag_Splitter.gif']

|  | New Width specifies the new width of the master control. |
| --- | --- |
|  | New X specifies the new origin for the horizontal axis of the master control. |
|  | Master Control Info In specifies all the position and border information for the master control before the drag operation. The drag operation can resize and move the master control depending on which border the master control shares with the slave control. |
|  | Slave Control Info In specifies all the position and border information for the slave control before the drag operation. The drag operation typically resizes and moves the slave control. |
|  | New Height specifies the new height of the master control. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Y specifies the new origin for the vertical axis of the master control. |
|  | Borders Changed specifies the borders that change. Use 8 for the right border, 4 for the left border, 1 for the top border, and 2 for the bottom border. |
|  | Master Control Info Out returns the updated sizes and positions of the master control. |
|  | Slave Control Info Out returns the updated sizes and positions of the slave control. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Layout VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-end-modal-dialog.html language=enus -->
## TOPIC 00019: TestStand - End Modal Dialog

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-end-modal-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-end-modal-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Makes the calling dialog box VI non-modal to the TestStand main application window after a previous call to the TestStand - Start Modal Dialog VI. Call this VI at the end of the dialog box VI to ensure that the dialog remains modal until it is dismissed. You must manually s

### TestStand - End Modal Dialog

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

TestStand - Start Modal Dialog

manually select the polymorphic instance

Note

#### Sequence Context

[IMAGE alt='image' src='images/TestStand_-_End_Modal_Dialog.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Modal ID specifies the value the TestStand - Start Modal Dialog VI returns in the Modal ID output. |
|  | VI Originally Open specifies the value the TestStand - Start Modal Dialog VI returns in the VI Originally Open output. |
|  | VI to make non-Modal A reference to the VI for which you want to end TestStand modality. This reference must be the same reference as previously passed into the TestStand - Start Modal Dialog VI. If you do not specify this parameter, the VI that calls the End Modal Dialog VI is made non-modal. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Engine

[IMAGE alt='image' src='images/TestStand_-_End_Modal_Dialog_Engine.gif']

|  | Engine specifies an ActiveX reference to a TestStand Engine object. |
| --- | --- |
|  | Modal ID specifies the value the TestStand - Start Modal Dialog VI returns in the Modal ID output. |
|  | VI Originally Open specifies the value the TestStand - Start Modal Dialog VI returns in the VI Originally Open output. |
|  | VI to make non-Modal A reference to the VI for which you want to end TestStand modality. This reference must be the same reference as previously passed into the TestStand - Start Modal Dialog VI. If you do not specify this parameter, the VI that calls the End Modal Dialog VI is made non-modal. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-execute-menu-command.html language=enus -->
## TOPIC 00020: TestStand - Execute Menu Command

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-execute-menu-command.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-execute-menu-command.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Executes the command associated with a menu item previously inserted with the TestStand - Insert Commands in Menu VI. Use this VI in response to the < This VI >:Menu Selection (User) event in the main TestStand User Interface VI. Menu Tag In specifies the tag of the menu it

### TestStand - Execute Menu Command

Owning Palette:
 [TestStand](menus-vis.html)

Executes the command associated with a menu item previously inserted with the
 [TestStand - Insert Commands in Menu](teststand-insert-commands-in-menu.html)
 VI. Use this VI in response to the <
 This VI
 >:Menu Selection (User) event in the main TestStand User Interface VI.

[IMAGE alt='image' src='images/TestStand_-_Execute_Menu_Command.gif']

|  | Menu Tag In specifies the tag of the menu item the user selected. You can obtain this value from the ItemTag data of the < This VI >:Menu Selection (User) event. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Menu Tag Out returns the Menu Tag In parameter unchanged. |
|  | User Menu Selected returns TRUE if the menu item the Menu Tag In parameter specifies is not a TestStand menu item. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Menus VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-get-property-value.html language=enus -->
## TOPIC 00021: TestStand - Get Property Value

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-get-property-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-get-property-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Returns the value of the SequenceContext property the Lookup String parameter specifies. You must manually select the polymorphic instance you want to use. Boolean Array Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. Lookup String

### TestStand - Get Property Value

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Returns the value of the
 SequenceContext
 property the
 Lookup String
 parameter specifies. You must
 [manually select the polymorphic instance](/csh?context=lvcore_lvhowto_selectingdefaultinstpolyvi)
 you want to use.

#### Boolean Array

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Boolean_Array.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Boolean

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Boolean.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Signed 8-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Unsigned 8-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Signed 16-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Unsigned 16-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Signed 32-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Unsigned 32-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Signed 64-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Unsigned 64-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Signed 8-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Unsigned 8-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Signed 16-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Unsigned 16-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Signed 32-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Unsigned 32-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Signed 64-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Unsigned 64-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Object

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Object.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reference

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_Reference.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### String Array

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_String_Array.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

#### String

[IMAGE alt='image' src='images/TestStand_-_Get_Property_Value_String.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Value Returns the value of the SequenceContext property the Lookup String parameter specifies. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-get-resource-string.html language=enus -->
## TOPIC 00022: TestStand - Get Resource String

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-get-resource-string.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-get-resource-string.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Returns a string in the TestStand string resource files for the current language. Specify the string by Category and Symbol , which are the section and item labels, respectively, for the string in the string resource files. Default String specifies the string for the VI to

### TestStand - Get Resource String

Owning Palette:
 [TestStand](localization-vis.html)

Returns a string in the TestStand string resource files for the current language. Specify the string by
 Category
 and
 Symbol
 , which are the section and item labels, respectively, for the string in the string resource files.

[IMAGE alt='image' src='images/TestStand_-_Get_Resource_String.gif']

|  | Default String specifies the string for the VI to return in the Resource String output if the string the Category and Symbol parameters specify does not exist. |
| --- | --- |
|  | Engine Reference In specifies an ActiveX reference to the TestStand Engine object. |
|  | Category specifies the category of the resource string in the TestStand string resource files. |
|  | Symbol specifies the symbol of the resource string in the TestStand string resource files. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Engine Reference Out returns the Engine Reference In parameter unchanged. |
|  | Resource String returns the value of the resource string in the TestStand string resource files. |
|  | Found returns TRUE if the resource string exists in the TestStand string resource files. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Localization VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-get-termination-monitor-status.html language=enus -->
## TOPIC 00023: TestStand - Get Termination Monitor Status

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-get-termination-monitor-status.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-get-termination-monitor-status.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Monitors the execution in which the VI is currently running so the VI can stop if the user terminates or aborts the execution. Use this VI after you call the TestStand - Initialize Termination Monitor VI. Status Monitor In specifies references to the TestStand objects requi

### TestStand - Get Termination Monitor Status

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Monitors the execution in which the VI is currently running so the VI can stop if the user terminates or aborts the execution. Use this VI after you call the
 [TestStand - Initialize Termination Monitor](teststand-initialize-termination-monitor.html)
 VI.

[IMAGE alt='image' src='images/TestStand_-_Get_Termination_Monitor_Status.gif']

|  | Status Monitor In specifies references to the TestStand objects required for monitoring the status of the parent execution. Wire the Status Monitor Out output of the TestStand - Initialize Termination Monitor VI to this input. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Status Monitor Out returns the Status Monitor In parameter unchanged. |
|  | Terminating or Aborting returns TRUE if the user terminates or aborts the execution the VI is monitoring. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-initialize-termination-monitor.html language=enus -->
## TOPIC 00024: TestStand - Initialize Termination Monitor

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-initialize-termination-monitor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-initialize-termination-monitor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Creates the termination monitor data property and execution objects the TestStand - Get Termination Monitor Status VI uses. Use the TestStand - Close Termination Monitor VI to release the termination monitor data property and execution objects. Sequence Context In specifies

### TestStand - Initialize Termination Monitor

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Creates the termination monitor data property and execution objects the
 [TestStand - Get Termination Monitor Status](teststand-get-termination-monitor-status.html)
 VI uses. Use the
 [TestStand - Close Termination Monitor](teststand-close-termination-monitor.html)
 VI to release the termination monitor data property and execution objects.

[IMAGE alt='image' src='images/TestStand_-_Initialize_Termination_Monitor.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Status Monitor Out returns references to the TestStand objects required for monitoring the status of the parent execution. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-insert-commands-in-menu.html language=enus -->
## TOPIC 00025: TestStand - Insert Commands in Menu

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-insert-commands-in-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-insert-commands-in-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Inserts a menu item or group of menu items associated with TestStand commands into a custom run-time menu. The data type you wire to the Application Manager input determines the polymorphic instance to use. Use this VI to rebuild the menu bar in response to the < This VI >:

### TestStand - Insert Commands in Menu

Owning Palette:
 [TestStand](menus-vis.html)

Inserts a menu item or group of menu items associated with TestStand commands into a custom run-time menu. The data type you wire to the
 Application Manager
 input determines the polymorphic instance to use. Use this VI to rebuild the menu bar in response to the <
 This VI
 >:Menu Activation? event in the main TestStand User Interface VI to populate the menu bar with the commands that apply to the current state of the application. Before you use this VI, use the
 [TestStand - Remove Commands from Menus](teststand-remove-commands-from-menus.html)
 VI to remove any pre-existing TestStand menu items.

#### TestStand - Insert Commands in Menu (Application Manager)

[IMAGE alt='image' src='images/TestStand_-_Insert_Commands_in_Menu_Application_Manager.gif']

|  | TestStand UI Control Has Focus specifies whether the active control on the LabVIEW front panel is a TestStand User Interface (UI) Control. Set the TestStand UI Control Has Focus parameter to FALSE when you insert the CommandKind_Edit_Copy , CommandKind_Edit_Cut , or CommandKind_Edit_Paste commands and the active control is not a TestStand UI Control. The TestStand menu commands operate only on TestStand UI Controls, not LabVIEW controls. In addition, the LabVIEW application menu items for copy, cut, paste, and clear operate only on LabVIEW controls, not TestStand UI Controls. When you set this input to FALSE and the Top-Level Menu to Insert Into input to Edit , this VI inserts the corresponding LabVIEW application menu item instead of the TestStand menu command. |
| --- | --- |
|  | Top-Level Menu to Insert Into specifies the tag of the menu item you want to insert command items into. |
|  | Menu Refnum In specifies the reference to a menu bar in a VI. Use the Current VI's Menubar function to obtain this reference number. |
|  | Commands specifies an array of TestStand command types. For each element in the array, the VI inserts the corresponding menu item(s) into the menu. |
|  | Application Manager specifies the reference to the TestStand Application Manager control to which the menu items apply. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Index of Menu Item to Insert After specifies the position at which to insert the items. To insert at the beginning of the menu, wire a number less than 0. To insert at the end of the menu, wire a number greater than the number of items in the menu. |
|  | Menu Refnum Out returns the Menu Refnum In parameter unchanged. |
|  | Number of Menu Items Inserted returns the number of items this VI inserted into the menu. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TestStand - Insert Commands in Menu (SequenceFileView Manager)

[IMAGE alt='image' src='images/TestStand_-_Insert_Commands_in_Menu_SequenceFileView_Manager.gif']

|  | TestStand UI Control Has Focus specifies whether the active control on the LabVIEW front panel is a TestStand UI Control. Set the TestStand UI Control Has Focus parameter to FALSE when you insert the CommandKind_Edit_Copy , CommandKind_Edit_Cut , or CommandKind_Edit_Paste commands and the active control is not a TestStand UI Control. The TestStand menu commands operate only on TestStand UI Controls, not LabVIEW controls. In addition, the LabVIEW application menu items for copy, cut, paste, and clear operate only on LabVIEW controls, not TestStand UI Controls. When you set this input to FALSE and the Top-Level Menu to Insert Into input to Edit , this VI inserts the corresponding LabVIEW application menu item instead of the TestStand menu command. |
| --- | --- |
|  | Top-Level Menu to Insert Into specifies the tag of the menu item you want to insert command items into. |
|  | Menu Refnum In specifies the reference to a menu bar in a VI. Use the Current VI's Menubar function to obtain this reference number. |
|  | Commands specifies an array of TestStand command types. For each element in the array, the VI inserts the corresponding menu item(s) into the menu. |
|  | SequenceFileView Manager specifies the reference to the TestStand SequenceFileView Manager control to which the menu items apply. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Index of Menu Item to Insert After specifies the position at which to insert the items. To insert at the beginning of the menu, wire a number less than 0. To insert at the end of the menu, wire a number greater than the number of items in the menu. |
|  | Menu Refnum Out returns the Menu Refnum In parameter unchanged. |
|  | Number of Menu Items Inserted returns the number of items this VI inserted into the menu. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TestStand - Insert Commands in Menu (ExecutionView Manager)

[IMAGE alt='image' src='images/TestStand_-_Insert_Commands_in_Menu_ExecutionView_Manager.gif']

|  | TestStand UI Control Has Focus specifies whether the active control on the LabVIEW front panel is a TestStand UI Control. Set the TestStand UI Control Has Focus parameter to FALSE when you insert the CommandKind_Edit_Copy , CommandKind_Edit_Cut , or CommandKind_Edit_Paste commands and the active control is not a TestStand UI Control. The TestStand menu commands operate only on TestStand UI Controls, not LabVIEW controls. In addition, the LabVIEW application menu items for copy, cut, paste, and clear operate only on LabVIEW controls, not TestStand UI Controls. When you set this input to FALSE and the Top-Level Menu to Insert Into input to Edit , this VI inserts the corresponding LabVIEW application menu item instead of the TestStand menu command. |
| --- | --- |
|  | Top-Level Menu to Insert Into specifies the tag of the menu item you want to insert command items into. |
|  | Menu Refnum In specifies the reference to a menu bar in a VI. Use the Current VI's Menubar function to obtain this reference number. |
|  | Commands specifies an array of TestStand command types. For each element in the array, the VI inserts the corresponding menu item(s) into the menu. |
|  | ExecutionView Manager specifies the reference to the TestStand ExecutionView Manager control to which the menu items apply. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Index of Menu Item to Insert After specifies the position at which to insert the items. To insert at the beginning of the menu, wire a number less than 0. To insert at the end of the menu, wire a number greater than the number of items in the menu. |
|  | Menu Refnum Out returns the Menu Refnum In parameter unchanged. |
|  | Number of Menu Items Inserted returns the number of items this VI inserted into the menu. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Menus VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-load-bounds.html language=enus -->
## TOPIC 00026: TestStand - Load Bounds

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-load-bounds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-load-bounds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Loads the bounds for a set of controls from the TestStand application configuration file. Use the TestStand - Save Bounds VI to save the bounds. You must use this VI and the TestStand - Save Bounds VI with the same set of controls in the same order. Application Manager Ref

### TestStand - Load Bounds

Owning Palette:
 [TestStand](layout-vis.html)

Loads the bounds for a set of controls from the TestStand application configuration file. Use the
 [TestStand - Save Bounds](teststand-save-bounds.html)
 VI to save the bounds. You must use this VI and the TestStand - Save Bounds VI with the same set of controls in the same order.

[IMAGE alt='image' src='images/TestStand_-_Load_Bounds.gif']

|  | Application Manager Ref specifies the reference to the Application Manager Object. |
| --- | --- |
|  | Configuration Property Name specifies the property from which to load the bounds information. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Bounds out contains the bounds information the VI loaded. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Layout VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-load-sizes.html language=enus -->
## TOPIC 00027: TestStand - Load Sizes

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-load-sizes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-load-sizes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Loads the height and width for each control you specify from a TestStand application configuration file. You must use this VI and the TestStand - Save Sizes VI with the same set of controls in the same order. Application Manager Ref specifies the reference to the Applicatio

### TestStand - Load Sizes

Owning Palette:
 [TestStand](layout-vis.html)

Loads the height and width for each control you specify from a TestStand application configuration file. You must use this VI and the
 [TestStand - Save Sizes](teststand-save-sizes.html)
 VI with the same set of controls in the same order.

[IMAGE alt='image' src='images/TestStand_-_Load_Sizes.gif']

|  | Application Manager Ref specifies the reference to the Application Manager Object. |
| --- | --- |
|  | Configuration Property Name specifies the property from which to load the size information. |
|  | Refnums specifies an array of clusters with an ActiveX container reference or a LabVIEW tab control reference. The VI resizes these controls to the loaded sizes. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Layout VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-localize-front-panel.html language=enus -->
## TOPIC 00028: TestStand - Localize Front Panel

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-localize-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-localize-front-panel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Converts all labels or text that begin with TS_ to a string in the TestStand string resource files for the current language. Specify the string by Category and the label or text, which are the section and item labels, respectively, for the string in the string resource file

### TestStand - Localize Front Panel

Owning Palette:
 [TestStand](localization-vis.html)

Converts all labels or text that begin with
 TS_
 to a string in the TestStand string resource files for the current language. Specify the string by
 Category
 and the label or text, which are the section and item labels, respectively, for the string in the string resource files. Optionally, this VI can also convert the text in free labels.

[IMAGE alt='image' src='images/TestStand_-_Localize_Front_Panel.gif']

|  | Localize Free Labels (False) specifies to convert the text in free labels. The default is FALSE. If the VI converts the text in free labels and you save the VI after the conversion, LabVIEW saves the new localized text in the labels instead of the original text. |
| --- | --- |
|  | Engine Reference In specifies an ActiveX reference to the TestStand Engine object. |
|  | Category specifies the category in the TestStand string resource files that contains the strings for the front panel. |
|  | VI Refnum (Caller's Refnum) specifies the reference to the VI for which to localize the front panel. The default is the reference to the calling VI. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Engine Reference Out returns the Engine Reference In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Localization VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-localize-menu.html language=enus -->
## TOPIC 00029: TestStand - Localize Menu

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-localize-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-localize-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Converts all menu items with names that begin with TS__ to a string in the TestStand string resource files for the current language. Specify the string by Category and the menu item name, which are the section and item labels, respectively, for the string in the string reso

### TestStand - Localize Menu

Owning Palette:
 [TestStand](localization-vis.html)

Converts all menu items with names that begin with
 TS__
 to a string in the TestStand string resource files for the current language. Specify the string by
 Category
 and the menu item name, which are the section and item labels, respectively, for the string in the string resource files.

[IMAGE alt='image' src='images/TestStand_-_Localize_Menu.gif']

|  | Engine Reference In specifies an ActiveX reference to the TestStand Engine object. |
| --- | --- |
|  | Menu Refnum In specifies the reference to a menu bar in a VI. Use the Current VI's Menubar function to obtain this reference number. |
|  | Category specifies the category in the TestStand string resource files that contains the strings for the menu. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Engine Reference Out returns the Engine Reference In parameter unchanged. |
|  | Menu Refnum Out returns the Menu Refnum In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Localization VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-remove-commands-from-menus.html language=enus -->
## TOPIC 00030: TestStand - Remove Commands from Menus

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-remove-commands-from-menus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-remove-commands-from-menus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Removes menu items previously inserted with the TestStand - Insert Commands in Menu VI. Optionally, this VI can also remove menu items inserted with the LabVIEW Menu Editor dialog box or the Insert Menu Items function. Use this VI in response to the < This VI >:Menu Activat

### TestStand - Remove Commands from Menus

Owning Palette:
 [TestStand](menus-vis.html)

Removes menu items previously inserted with the
 [TestStand - Insert Commands in Menu](teststand-insert-commands-in-menu.html)
 VI. Optionally, this VI can also remove menu items inserted with the LabVIEW
 [Menu Editor](/csh?context=lvcore_lvdialog_menu_editor_dialog_box)
 dialog box or the Insert Menu Items function. Use this VI in response to the <
 This VI
 >:Menu Activation? event in the main TestStand User Interface VI to clear the menu bar before you use the TestStand - Insert Commands in Menu VI.

[IMAGE alt='image' src='images/TestStand_-_Remove_Commands_from_Menus.gif']

|  | Menu Refnum In specifies the reference to a menu bar in a VI. Use the Current VI's Menubar function to obtain this reference number. |
| --- | --- |
|  | Remove User Menu Items specifies whether the VI removes non-TestStand items from the menus. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Menu Refnum Out returns the Menu Refnum In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Menus VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-save-bounds.html language=enus -->
## TOPIC 00031: TestStand - Save Bounds

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-save-bounds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-save-bounds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Saves the bounds for a set of controls to the TestStand application configuration file. Application Manager Ref specifies the reference to the Application Manager Object. Configuration Property Name specifies the property name under which to save the size information. Bound

### TestStand - Save Bounds

Owning Palette:
 [TestStand](layout-vis.html)

Saves the bounds for a set of controls to the TestStand application configuration file.

[IMAGE alt='image' src='images/TestStand_-_Save_Bounds.gif']

|  | Application Manager Ref specifies the reference to the Application Manager Object. |
| --- | --- |
|  | Configuration Property Name specifies the property name under which to save the size information. |
|  | Bounds specifies the left, top, right, and bottom bounds information. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Layout VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-save-sizes.html language=enus -->
## TOPIC 00032: TestStand - Save Sizes

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-save-sizes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-save-sizes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Saves the height and width for each control you specify to the TestStand application configuration file. Application Manager Ref specifies the reference to the Application Manager Object. Configuration Property Name specifies the property name under which to save the bounds

### TestStand - Save Sizes

Owning Palette:
 [TestStand](layout-vis.html)

Saves the height and width for each control you specify to the TestStand application configuration file.

[IMAGE alt='image' src='images/TestStand_-_Save_Sizes.gif']

|  | Application Manager Ref specifies the reference to the Application Manager Object. |
| --- | --- |
|  | Configuration Property Name specifies the property name under which to save the bounds information. |
|  | Refnums specifies an array of clusters with an ActiveX container reference or a LabVIEW tab control reference. The VI saves the sizes of these controls. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Layout VIs

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-set-property-value.html language=enus -->
## TOPIC 00033: TestStand - Set Property Value

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-set-property-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-set-property-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Sets the value of the SequenceContext property the Lookup String parameter specifies. The data type you wire to the New Value input determines the polymorphic instance to use. This VI does not return an error if the Lookup String parameter is invalid and the Insert If Missi

### TestStand - Set Property Value

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Sets the value of the SequenceContext property the
 Lookup String
 parameter specifies. The data type you wire to the
 New Value
 input determines the polymorphic instance to use. This VI does not return an error if the
 Lookup String
 parameter is invalid and the
 Insert If Missing
 parameter is TRUE.

#### Boolean Array

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Boolean_Array.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Boolean

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Boolean.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Signed 8-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Unsigned 8-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Signed 16-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Unsigned 16-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Signed 32-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Unsigned 32-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Signed 64-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Numeric Array {Unsigned 64-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Numeric_Array_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Signed 8-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Unsigned 8-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Signed 16-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Unsigned 16-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Signed 32-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Unsigned 32-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Signed 64-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Number {Unsigned 64-bit Integer}

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Number_Integer.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Object

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Object.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reference

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_Reference.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### String Array

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_String_Array.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### String

[IMAGE alt='image' src='images/TestStand_-_Set_Property_Value_String.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | Lookup String is a chain of period-delimited subproperties that specifies a particular subproperty of the SequenceContext object the Sequence Context In parameter specifies. The property cannot be empty and must contain only letters, numbers, and underscores. Property names cannot contain spaces or start with a number. For example, Locals.MyVariableName_2000 is a valid property name. Names of elements in a property object array can contain any character. Sequence names and step names are examples of valid named array elements. |
|  | New Value specifies the new value for the SequenceContext property the Lookup String parameter specifies. |
|  | Insert If Missing specifies to insert the SequenceContext property the Lookup String parameter specifies if the property does not currently exist. The default is FALSE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-set-teststand-application-window.html language=enus -->
## TOPIC 00034: TestStand - Set TestStand Application Window

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-set-teststand-application-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-set-teststand-application-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Sets the TestStand main application window as the VI the VI Refnum parameter specifies. Use this VI once in the main TestStand User Interface VI to ensure that modal dialogs TestStand sequences display are modal to that VI. Application Manager specifies the reference to the

### TestStand - Set TestStand Application Window

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Sets the TestStand main application window as the VI the
 VI Refnum
 parameter specifies. Use this VI once in the main TestStand User Interface VI to ensure that modal dialogs TestStand sequences display are modal to that VI.

[IMAGE alt='image' src='images/TestStand_-_Set_TestStand_Application_Window.gif']

|  | Application Manager specifies the reference to the TestStand Application Manager control on the VI that is the main application window. |
| --- | --- |
|  | VI Refnum (Caller's Refnum) specifies the reference to the VI to set as the TestStand main application window. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-set-thread-externally-suspended.html language=enus -->
## TOPIC 00035: TestStand - Set Thread Externally Suspended

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-set-thread-externally-suspended.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-set-thread-externally-suspended.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Sets the value of the Thread.ExternallySuspended property for the thread that executes this VI. Use this property to enable an execution to break while the VI performs a lengthy operation or waits an indeterminate period of time. Refer to the NI TestStand Help for more info

### TestStand - Set Thread Externally Suspended

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

Sets the value of the
 Thread.ExternallySuspended
 property for the thread that executes this VI. Use this property to enable an execution to break while the VI performs a lengthy operation or waits an indeterminate period of time. Refer to the
 NI TestStand Help
 for more information about the
 Thread.ExternallySuspended
 property.

[IMAGE alt='image' src='images/TestStand_-_Set_Thread_Externally_Suspended.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object for the thread to externally suspend. |
| --- | --- |
|  | Externally Suspended specifies whether you can externally suspend this thread. The default is TRUE. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-start-modal-dialog.html language=enus -->
## TOPIC 00036: TestStand - Start Modal Dialog

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-start-modal-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-start-modal-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Makes the calling dialog box VI modal to the TestStand main application window. When you call this VI, you must then use the TestStand - End Modal Dialog VI to make the dialog box non-modal to the TestStand main application window before you attempt to interact with the Tes

### TestStand - Start Modal Dialog

Owning Palette:
 [TestStand](ni-teststand-vis-and-functions-help.html)

TestStand - End Modal Dialog

manually select the polymorphic instance

Note

SequenceContext

Engine

SequenceContext

#### Sequence Context

[IMAGE alt='image' src='images/TestStand_-_Start_Modal_Dialog.gif']

|  | Sequence Context In specifies an ActiveX reference to a TestStand SequenceContext object. |
| --- | --- |
|  | VI to make Modal (Current VI) A reference to the VI you want to make modal. If you do not specify this parameter, the VI that calls the Start Modal Dialog VI is made modal. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sequence Context Out returns the Sequence Context In parameter unchanged. |
|  | Modal ID returns the ID you pass to the TestStand - End Modal Dialog VI. |
|  | VI Originally Open returns TRUE if the front panel of the calling VI was open before it called the TestStand - Start Modal Dialog VI. Pass this value to the TestStand - End Modal Dialog VI. |
|  | Should Abort returns TRUE if the user terminated or aborted the calling execution while this VI was running. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Engine

[IMAGE alt='image' src='images/TestStand_-_Start_Modal_Dialog_Engine.gif']

|  | Engine in specifies an ActiveX reference to a TestStand Engine object. |
| --- | --- |
|  | VI to make Modal (Current VI) A reference to the VI you want to make modal. If you do not specify this parameter, the VI that calls the Start Modal Dialog VI is made modal. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Engine out returns the Engine in parameter unchanged. |
|  | Modal ID returns the ID you pass to the TestStand - End Modal Dialog VI. |
|  | VI Originally Open returns TRUE if the front panel of the calling VI was open before it called the TestStand - Start Modal Dialog VI. Pass this value to the TestStand - End Modal Dialog VI. |
|  | Should Abort returns TRUE if the user terminated or aborted the calling execution while this VI was running. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

NI TestStand VIs and Functions Help

<!--NI_TOPIC bundle=teststand-api-reference path=lvteststand/teststand-update-control-position-and-size.html language=enus -->
## TOPIC 00037: TestStand - Update Control Position and Size

- bundle_id: `teststand-api-reference`
- source_path: `lvteststand/teststand-update-control-position-and-size.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/lvteststand/teststand-update-control-position-and-size.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: TestStand Updates the size and position of the control to the values in the Control Info parameter. The data type you wire to the AXCont Refnum In input determines the polymorphic instance to use. TestStand - Update AX Control Position and Size from Control Info AXCont Refnum In spec

### TestStand - Update Control Position and Size

Owning Palette:
 [TestStand](layout-vis.html)

Updates the size and position of the control to the values in the
 Control Info
 parameter. The data type you wire to the
 AXCont Refnum In
 input determines the polymorphic instance to use.

#### TestStand - Update AX Control Position and Size from Control Info

[IMAGE alt='image' src='images/TestStand_-_Update_AX_Control_Position_and_Size_from_Control_Info.gif']

|  | AXCont Refnum In specifies the refnum for the LabVIEW ActiveX container that contains the user interface control. |
| --- | --- |
|  | Control Info specifies the position and size information for the user interface control. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | AXCont Refnum Out returns the AXCont Refnum In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

#### TestStand - Update LabView Tab Control Position and Size from Control Info

[IMAGE alt='image' src='images/TestStand_-_Update_LabView_Tab_Control_Position_and_Size_from_Control_Info.gif']

|  | TabCtl Refnum In specifies a reference to a LabVIEW tab control. |
| --- | --- |
|  | Control Info specifies the position and size information for the user interface control. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | TabCtl Refnum Out returns the TabCtl Refnum In parameter unchanged. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

Layout VIs

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/color.html language=enus -->
## TOPIC 00038: Color

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/color.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/color.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Color values are typically four-byte integers and commonly use little-endian and big-endian format. Microsoft Windows and ActiveX use the little-endian format, which stores red, green, and blue color components in the 0x00BBGGRR byte positions. LabVIEW and LabWindows/CVI use the big-endian format, w

### Color

Color values are typically four-byte integers and commonly use little-endian and big-endian format. Microsoft Windows and ActiveX use the little-endian format, which stores red, green, and blue color components in the 0x00BBGGRR byte positions. LabVIEW and LabWindows/CVI use the big-endian format, which stores the color components in the 0x00RRGGBB byte positions.

If you are specifying a color value in an expression, you can use a predefined little-endian color constant, such as tsRed or tsDarkBlue. Refer to
 Constants»Color
 on the Operators/Functions tab of the Expression Browser dialog box for the list of available expression color constants. Use the
 ConvertColor
 expression function to convert the two color value formats.

Some Windows and ActiveX functions support specifying a system color using the 0x800000xx byte format, where
 xx
 is a valid Win32
 GetSysColor
 index. The possible values are listed below.

- 0x00bbggrr—Where
 bb 
 specifies the intensity of the color blue,
 gg 
 specifies the intensity of the color green, and
 rr 
 specifies the intensity of the color red.
- 0x800000xx—Where
 xx 
 is a valid Win32
 GetSysColor 
 index. The possible values are listed below.
 Constant
 ValueCOLOR_SCROLLBAR
 0
 COLOR_BACKGROUND
 1
 COLOR_ACTIVECAPTION
 2
 COLOR_INACTIVECAPTION
 3
 COLOR_MENU
 4
 COLOR_WINDOW
 5
 COLOR_WINDOWFRAME
 6
 COLOR_MENUTEXT
 7
 COLOR_WINDOWTEXT
 8
 COLOR_CAPTIONTEXT
 9
 COLOR_ACTIVEBORDER
 10
 COLOR_INACTIVEBORDER
 11
 COLOR_APPWORKSPACE
 12
 COLOR_HIGHLIGHT
 13
 COLOR_HIGHLIGHTEXT
 14
 COLOR_BTNFACE
 15
 COLOR_BTNSHADOW
 16
 COLOR_GRAYTEXT
 17
 COLOR_BTNTEXT
 18
 COLOR_INACTIVECAPTIONTEXT
 19
 COLOR_BTNHIGHLIGHT
 20
 COLOR_3DDKSHADOW
 21
 COLOR_3DLIGHT
 22
 COLOR_INFOTEXT
 23
 COLOR_INFOBK
 24
 COLOR_HOTLIGHT
 26
 COLOR_GRADIENTACTIVECAPTION
 27
 COLOR_GRADIENTINACTIVECAPTION
 28
 COLOR_MENUHILIGHT
 29
 COLOR_MENUBAR
 30

Parent topic:

Data Types for Session Manager

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/data-types-for-session-manager.html language=enus -->
## TOPIC 00039: Data Types for Session Manager

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/data-types-for-session-manager.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/data-types-for-session-manager.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Type OLE Automation Type Description Boolean VARIANT_BOOL Has the value True ( -1 ) or False ( 0 ). Byte Array SAFEARRAY(unsigned char) An array of bytes. Color OLE_COLOR A color. Many containers treat colors as 32-bit integers. Date DATE DATE is a variant time that is stored as an 8-byte real value

### Data Types for Session Manager

| Type | OLE Automation Type | Description |
| --- | --- | --- |
| Boolean | VARIANT_BOOL | Has the value True ( -1 ) or False ( 0 ). |
| Byte Array | SAFEARRAY(unsigned char) | An array of bytes. |
| Color | OLE_COLOR | A color. Many containers treat colors as 32-bit integers. |
| Date | DATE | DATE is a variant time that is stored as an 8-byte real value (double) and represents a date between January 1, 100 and December 31, 9999, inclusive. The value 0 represents December 30, 1899. Adding 1 to the value increments the date by a day. The fractional part of the value represents the time of day. Negative numbers represent the dates before December 30, 1899. LabWindows/CVI users can use the VariantTimeToSystemTime Microsoft Windows Software Development Kit (SDK) function to convert the variant date to a system time value and then use the GetDateFormat and GetTimeFormat Windows SDK functions to generate display strings. LabVIEW automatically converts the DATE data type to a timestamp. |
| Double | double | 64-bit floating point number. |
| Float | float | 32-bit floating point number. |
| Font | IFontDisp | An Object Linking and Embedding (OLE) Automation Interface to a font . |
| Integer | short | 16-bit signed integer. |
| IUnknown | IUnknown | A generic OLE interface. |
| Long | Long | 32-bit signed integer. |
| long | OLE_YPOS_PIXELS | Position on the Y-axis in pixels. |
| Long | LCID | A locale identifier. |
| long | OLE_XPOS_PIXELS | Position on the X-axis in pixels. |
| Long Array | SAFEARRAY(long) | An array of longs. |
| long long | LONGLONG | 64-bit signed integer. |
| Object | IDispatch | A generic OLE Automation interface. |
| Object Array | SAFEARRAY | An array of objects. |
| Picture | IPicture | An OLE Automation Interface to a Picture object or image. |
| Picture | IPictureDisp | An OLE Automation Interface to a Picture object or image. |
| String | BSTR | A string. |
| String Array | SAFEARRAY(BSTR) | An array of strings. |
| unsigned long long | ULONGLONG | 64-bit unsigned integer. |
| Variant | VARIANT | A variant. |
| VARTYPE | VARTYPE | An enumeration type used to describe a data type of a VARIANT or safearray value. Refer to VARTYPE for more information about VARTYPE enumeration values. |

Parent topic:

Session Manager Objects

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/font.html language=enus -->
## TOPIC 00040: Font

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Font object specifies a wrapper around a Microsoft Windows font. Microsoft defines this standard Font object implementation in the Object Linking and Embedding (OLE) Automation version 2.0 type library file, stdole2.tlb . Refer to Microsoft documentation for more information about this interface.

### Font

A Font object specifies a wrapper around a Microsoft Windows font. Microsoft defines this standard Font object implementation in the Object Linking and Embedding (OLE) Automation version 2.0 type library file,
 stdole2.tlb
 . Refer to Microsoft documentation for more information about this interface.

The Font interface specifies the following properties and methods:

#### Properties

- Name 
 —Name for the font.
- Size 
 —Point size for the font.
- Bold 
 —Bold property for the font.
- Italic 
 —Italic property for the font.
- Underline 
 —Underline property for the font.
- Strikethrough 
 —Strikethrough property for the font.
- Weight 
 —Weight (bold) for the font.
- Charset 
 —Character set of the font.
- hFont 
 —Returns a Windows HFONT handle for the font this Font object describes.

#### Methods

- Clone 
 —Creates a duplicate Font object with a state identical to the current font.
- IsEqual 
 —Compares this Font object to another for equality.
- SetRatio 
 —Converts the scaling factor for this font between logical units and HIMETRIC units, which the point size in the Size property specifies.
- QueryTextMetrics 
 —Fills a TEXTMETRIC structure describing the font.
- AddRefHfont 
 —Notifies the Font object that the previously realized font hFont identified remains valid until the ReleaseHfont method is called or the Font object itself is released.
- ReleaseHfont 
 —Notifies the Font object that the caller that previously locked this font in the cache with AddRefHfont no longer requires the lock.
- SetHdc 
 —Provides a device context handle to the font that describes the logical mapping mode.

LabVIEW

The LabVIEW development environment automatically recognizes Font ActiveX references. Use the Invoke Node and Property Node VIs to access the methods and properties of a Font ActiveX reference.

Note

LabWindows/CVI

LabWindows/CVI creates and accesses ActiveX objects using functions in a LabWindows/CVI-generated driver. You must create a driver for the OLE Automation ActiveX server using the ActiveX Controller Wizard. Select
 Tools»Create ActiveX Controller
 to launch the wizard. Select
 OLE Automation
 in the ActiveX Server list control and proceed to build the driver. Use the functions for the Font class to access the methods and properties.

Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can access Font objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

Imports stdole.StdFontClass

The IFontDisp class methods and properties are available in the Microsoft Visual Studio object browser and are accessible from the Visual Basic .NET source code.

C#

In C#, you can access Font objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

using stdole.StdFontClass;

The IFontDisp class methods and properties are available in the Visual Studio object browser and are accessible from the C# source code.

Microsoft Visual C++/#import

In C++, you can access Font objects by adding the include file
 ocidl.h
 and using the CComPtr template to manage IFontDisp COM interface pointers.

Parent topic:

Data Types for Session Manager

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/getnamesoptions.html language=enus -->
## TOPIC 00041: GetNamesOptions

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/getnamesoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/getnamesoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants in the flags parameter to specify the types of names and the format of the names the InstrSessionMgr.GetNames method returns. IncludeCategoryPrefix –(Value: 0x08) Specifies that the names the InstrSessionMgr.GetNames method returns include a category prefix. ReturnHiddenNames –(V

### GetNamesOptions

Use these constants in the
 flags
 parameter to specify the types of names and the format of the names the
 [InstrSessionMgr.GetNames](instrsessionmgr-getnames.html)
 method returns.

- IncludeCategoryPrefix 
 –(Value: 0x08) Specifies that the names the
 InstrSessionMgr.GetNames 
 method returns include a category prefix.
- ReturnHiddenNames 
 –(Value: 0x04) Specifies that the
 InstrSessionMgr.GetNames 
 method returns names Session Manager recognizes but that you typically do not display to users. Specifically, the
 InstrSessionMgr.GetNames 
 method returns full virtual instrument names, such as
 "VPPVInstr->FlukeDMM" 
 or
 "VInstr->tk252xg" 
 .
- ReturnLogicalNames 
 –(Value: 0x01) Specifies that the
 InstrSessionMgr.GetNames 
 method returns logical names.
- ReturnRouteGroups 
 –(Value: 0x10) Specifies that the
 InstrSessionMgr.GetNames 
 method returns switch execution route group names.
- ReturnRoutes 
 –(Value: 0x20) Specifies that the
 InstrSessionMgr.GetNames 
 method returns NI Switch Executive route names.
- ReturnVirtualInstruments 
 –(Value: 0x02) Specifies that the
 InstrSessionMgr.GetNames 
 method returns IVI virtual instrument names, VXI
 plug&play 
 virtual instrument names, VISA resource names, and NI Switch Executive virtual device names.

#### See Also

[InstrSessionMgr.GetNames](instrsessionmgr-getnames.html)

Parent topic:

Session Manager API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-attachlong.html language=enus -->
## TOPIC 00042: InstrSession.AttachLong

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-attachlong.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-attachlong.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.AttachLong( uniqueId, value) Purpose Attaches a user-defined long integer value to the session. Call the InstrSession.GetLong method to retrieve the value. Remarks Parameters uniqueId As String [In] Pass a unique string to use when you retrieve the value. Call the InstrSession.Ge

### InstrSession.AttachLong

#### Syntax

[InstrSession](instrsession.html).AttachLong( uniqueId, value)

#### Purpose

Attaches a user-defined long integer value to the session. Call the
 [InstrSession.GetLong](instrsession-getlong.html)
 method to retrieve the value.

#### Remarks

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass a unique string to use when you retrieve the value. Call the
 [InstrSession.GenerateUniqueID](instrsession-generateuniqueid.html)
 method to obtain a unique string.

value
 As
 [Long](data-types-for-session-manager.html)

[In] Pass the long integer value to attach to the session.

#### See Also

[InstrSession.GenerateUniqueID](instrsession-generateuniqueid.html)

[InstrSession.GetLong](instrsession-getlong.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-attachlongptr.html language=enus -->
## TOPIC 00043: InstrSession.AttachLongPtr

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-attachlongptr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-attachlongptr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.AttachLongPtr( uniqueId, value) Purpose Attaches a user-defined pointer-sized integer value to the session. Call the InstrSession.GetLongPtr method to retrieve the value. Parameters uniqueId As String [In] Pass a unique string to use when you retrieve the value. Call the InstrSes

### InstrSession.AttachLongPtr

#### Syntax

[InstrSession](instrsession.html).AttachLongPtr( uniqueId, value)

#### Purpose

Attaches a user-defined pointer-sized integer value to the session. Call the
 [InstrSession.GetLongPtr](instrsession-getlongptr.html)
 method to retrieve the value.

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass a unique string to use when you retrieve the value. Call the
 [InstrSession.GenerateUniqueID](instrsession-generateuniqueid.html)
 method to obtain a unique string.

value
 As
 [Variant](data-types-for-session-manager.html)

[In] Pass the integer value to attach to the session. The type of the variant must match the architecture of the session instance. For 32-bit applications, the variant type must be a 32-bit integer (
 VT_I4
 or
 VT_UI4
 ). For 64-bit applications, the variant type must be a 64-bit integer (
 VT_I8
 or
 VT_UI8
 ).

#### See Also

[InstrSession.GenerateUniqueID](instrsession-generateuniqueid.html)

[InstrSession.GetLongPtr](instrsession-getlongptr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-attachobject.html language=enus -->
## TOPIC 00044: InstrSession.AttachObject

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-attachobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-attachobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.AttachObject( uniqueId, iPtr, clsid, releaseOnClose) Purpose Attaches an object to the session. Remarks Instead of attaching an existing object, you can specify that the session creates a particular object when you first call the InstrSession.GetObject method to request the sessi

### InstrSession.AttachObject

#### Syntax

[InstrSession](instrsession.html).AttachObject( uniqueId, iPtr, clsid, releaseOnClose)

#### Purpose

Attaches an object to the session.

#### Remarks

Instead of attaching an existing object, you can specify that the session creates a particular object when you first call the
 [InstrSession.GetObject](instrsession-getobject.html)
 method to request the session to return the object. To specify the object to create, pass the
 NULL
 pointer,
 Nothing
 , as the
 iPtr
 parameter and pass the GUID (COM globally unique identifier) of the object as the
 clsid
 parameter. Otherwise, pass the object to attach to the session as the
 iPtr
 parameter and pass an empty string as the
 clsid
 parameter.

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass a unique string to use when you retrieve the object. Call the
 [InstrSession.GenerateUniqueID](instrsession-generateuniqueid.html)
 method to obtain a unique string.

iPtr
 As
 [IUnknown](data-types-for-session-manager.html)

[In] Pass an ActiveX pointer to the object you attach to the session. You can pass a
 NULL
 pointer if you also pass the GUID of the object that you want to create as the
 clsid
 parameter.

clsid
 As
 [String](data-types-for-session-manager.html)

[In] Pass the GUID of the object to create or pass an empty string to attach an existing object. The format of the
 clsid
 string is
 {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}
 .

releaseOnClose
 As
 [Boolean](data-types-for-session-manager.html)

[In] Pass
 True
 to release the attached object when you explicitly call the
 [InstrSession.Close](instrsession-close.html)
 method on the session. The session always releases the attached object when you release the final reference to the session.

#### See Also

[Attaching Additional Data to a Session](/csh?context=ts_smgrref_attaching_additional_data_to_a_session)

[InstrSession.Close](instrsession-close.html)

[InstrSession.GenerateUniqueID](instrsession-generateuniqueid.html)

[InstrSession.GetObject](instrsession-getobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-attachstring.html language=enus -->
## TOPIC 00045: InstrSession.AttachString

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-attachstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-attachstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.AttachString( uniqueId, value) Purpose Attaches a user-defined string value to the session. Call the InstrSession.GetString method to retrieve the value. Parameters uniqueId As String [In] Pass a unique string to use when you retrieve the value. Call the InstrSession.GenerateUniq

### InstrSession.AttachString

#### Syntax

[InstrSession](instrsession.html).AttachString( uniqueId, value)

#### Purpose

Attaches a user-defined string value to the session. Call the
 [InstrSession.GetString](instrsession-getstring.html)
 method to retrieve the value.

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass a unique string to use when you retrieve the value. Call the
 [InstrSession.GenerateUniqueID](instrsession-generateuniqueid.html)
 method to obtain a unique string.

value
 As
 [String](data-types-for-session-manager.html)

[In] Pass the string value to attach to the session.

#### See Also

[Attaching Additional Data to a Session](/csh?context=ts_smgrref_attaching_additional_data_to_a_session)

[InstrSession.GenerateUniqueID](instrsession-generateuniqueid.html)

[InstrSession.GetString](instrsession-getstring.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-category.html language=enus -->
## TOPIC 00046: InstrSession.Category

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-category.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-category.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.Category Data Type String Purpose Returns the session category. See Also InstrSession.Name Instrument Session Categories

### InstrSession.Category

#### Syntax

[InstrSession](instrsession.html).Category

#### Data Type

[String](data-types-for-session-manager.html)

#### Purpose

Returns the session category.

#### See Also

[InstrSession.Name](instrsession-name.html)

[Instrument Session Categories](/csh?context=ts_smgrref_instrument_session_categories)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-close.html language=enus -->
## TOPIC 00047: InstrSession.Close

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-close.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-close.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.Close Purpose This method is obsolete. Use the InstrSession.CloseFunctionEx method instead. Remarks Closes (uninitializes) the driver for the session. A session automatically closes when its last reference releases. Typically, you do not call this method. See Also InstrSession.In

### InstrSession.Close

#### Syntax

[InstrSession](instrsession.html).Close

#### Purpose

Note

InstrSession.CloseFunctionEx

#### Remarks

Closes (uninitializes) the driver for the session. A session automatically closes when its last reference releases. Typically, you do not call this method.

#### See Also

[InstrSession.Initialize](instrsession-initialize.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-closeenabled.html language=enus -->
## TOPIC 00048: InstrSession.CloseEnabled

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-closeenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-closeenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.CloseEnabled Data Type Boolean Purpose Controls whether to honor calls to the InstrSession.Close method. The default value of this property is True . Setting this property to False ignores calls to the InstrSession.Close method. The session does not close (uninitialize) until the

### InstrSession.CloseEnabled

#### Syntax

[InstrSession](instrsession.html).CloseEnabled

#### Data Type

[Boolean](data-types-for-session-manager.html)

#### Purpose

Controls whether to honor calls to the
 [InstrSession.Close](instrsession-close.html)
 method. The default value of this property is
 True
 . Setting this property to
 False
 ignores calls to the
 InstrSession.Close
 method. The session does not close (uninitialize) until the final reference to it releases. Typically, you do not access this property.

#### See Also

[InstrSession.Close](instrsession-close.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-closefunction.html language=enus -->
## TOPIC 00049: InstrSession.CloseFunction

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-closefunction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-closefunction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.CloseFunction Data Type Long Purpose This property is obsolete. Use the InstrSession.CloseFunctionEx property instead. Calling this property in a 64-bit application returns an error. Remarks Stores the address of a function the session calls when it closes. If the function addres

### InstrSession.CloseFunction

#### Syntax

[InstrSession](instrsession.html).CloseFunction

#### Data Type

[Long](data-types-for-session-manager.html)

#### Purpose

Note

InstrSession.CloseFunctionEx

#### Remarks

Stores the address of a function the session calls when it closes. If the function address is zero, the session does not call the function. The prototype of the function is
 void __cdecl CloseFunction(IUnknown *session)
 , where
 *session
 is the session that is closing. Within the close function, you can access data items you added to the session.

Parent topic:

Obsolete InstrSession Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-closefunctionex.html language=enus -->
## TOPIC 00050: InstrSession.CloseFunctionEx

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-closefunctionex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-closefunctionex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.CloseFunctionEx Data Type Variant Purpose Stores the address of a function the session calls when it closes. If the function address is zero, the session does not call the function. The prototype of the function is void __cdecl CloseFunction(IUnknown *session) , where *session is

### InstrSession.CloseFunctionEx

#### Syntax

[InstrSession](instrsession.html).CloseFunctionEx

#### Data Type

[Variant](data-types-for-session-manager.html)

#### Purpose

Stores the address of a function the session calls when it closes. If the function address is zero, the session does not call the function. The prototype of the function is
 void __cdecl CloseFunction(IUnknown *session)
 , where
 *session
 is the session that is closing. Within the close function, you can access data items you added to the session.

#### Remarks

The type of the variant must match the pointer size for the current platform. For example, use
 VT_UI4
 for 32-bit TestStand and
 VT_UI8
 for 64-bit TestStand.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-detachdata.html language=enus -->
## TOPIC 00051: InstrSession.DetachData

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-detachdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-detachdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.DetachData( uniqueId) Purpose Removes a user-defined data item from the session and disposes of the data. Pass an empty string as the uniqueId parameter to detach all user-defined data items. Remarks A session automatically detaches all its data items when it destroys itself. Par

### InstrSession.DetachData

#### Syntax

[InstrSession](instrsession.html).DetachData( uniqueId)

#### Purpose

Removes a user-defined data item from the session and disposes of the data. Pass an empty string as the
 uniqueId
 parameter to detach all user-defined data items.

#### Remarks

A session automatically detaches all its data items when it destroys itself.

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass the unique string that identifies the data to remove and dispose. Pass an empty string to remove and dispose all data items.

#### See Also

[Attaching Additional Data to a Session](/csh?context=ts_smgrref_attaching_additional_data_to_a_session)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-generateuniqueid.html language=enus -->
## TOPIC 00052: InstrSession.GenerateUniqueID

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-generateuniqueid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-generateuniqueid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GenerateUniqueID Return Value String Purpose Returns the unique string you use to attach a data item to the session. Use the ID to retrieve the data item from the session. Remarks You can create a custom ID string or call this method to obtain a guaranteed unique string for the s

### InstrSession.GenerateUniqueID

#### Syntax

[InstrSession](instrsession.html).GenerateUniqueID

#### Return Value

[String](data-types-for-session-manager.html)

#### Purpose

Returns the unique string you use to attach a data item to the session. Use the ID to retrieve the data item from the session.

#### Remarks

You can create a custom ID string or call this method to obtain a guaranteed unique string for the session. This method generates a unique ID string each time you call it. This method does not allocate or reserve any data in the session.

#### See Also

[Attaching Additional Data to a Session](/csh?context=ts_smgrref_attaching_additional_data_to_a_session)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-getcomdriver.html language=enus -->
## TOPIC 00053: InstrSession.GetCOMDriver

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-getcomdriver.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-getcomdriver.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetCOMDriver( level) Return Value IUnknown Returns a pointer to the driver API object. Purpose Returns a COM pointer to the driver API object for the interface level you specify. The driver initializes, if necessary. Session Manager does not support IVI-COM drivers. This function

### InstrSession.GetCOMDriver

#### Syntax

[InstrSession](instrsession.html).GetCOMDriver( level)

#### Return Value

[IUnknown](data-types-for-session-manager.html)

Returns a pointer to the driver API object.

#### Purpose

Returns a COM pointer to the driver API object for the interface level you specify. The driver initializes, if necessary.

Note

#### Remarks

If the session does not support the interface level you specify, this method returns an error. Call QueryInterface on the driver to obtain a particular interface. You must release the driver interface when you are done with it. The session stores a reference to the driver object so the object does not destroy itself until the session closes.

#### Parameters

level
 As
 [InterfaceLevel](interfacelevel.html)

[In] Specifies the type of API reference to return.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-gethandle.html language=enus -->
## TOPIC 00054: InstrSession.GetHandle

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-gethandle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-gethandle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetHandle( level) Return Value Long Returns the instrument API handle. Purpose This method is obsolete. Use the InstrSession.GetHandleEx method instead. NI Session Manager supports InstrSession.GetHandle to maintain compatibility. However, calling this method in a 64-bit applicat

### InstrSession.GetHandle

#### Syntax

[InstrSession](instrsession.html).GetHandle( level)

#### Return Value

[Long](data-types-for-session-manager.html)

Returns the instrument API handle.

#### Purpose

Note

InstrSession.GetHandleEx

InstrSession.GetHandle

#### Remarks

Returns the C-based instrument API handle to the driver for a specific interface level. The driver initializes, if necessary. If the session does not support the interface level you request, this method returns a zero-valued handle as an error. The session stores the API handle and manages its lifetime.

Note

#### Parameters

level
 As
 [InterfaceLevel](interfacelevel.html)

[In] Specifies the type of API handle to return.

Parent topic:

Obsolete InstrSession Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-gethandleex.html language=enus -->
## TOPIC 00055: InstrSession.GetHandleEx

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-gethandleex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-gethandleex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetHandleEx( level) Return Value Variant Returns a variant that contains the instrument API handle. The type of the variant matches the handle size the session uses for the current architecture ( VT_UI4 for 32-bit handles and VT_UI8 for 64-bit handles). VISA, IVI, and VXI plug&pl

### InstrSession.GetHandleEx

#### Syntax

[InstrSession](instrsession.html).GetHandleEx( level)

#### Return Value

[Variant](data-types-for-session-manager.html)

Returns a variant that contains the instrument API handle. The type of the variant matches the handle size the session uses for the current architecture (
 VT_UI4
 for 32-bit handles and
 VT_UI8
 for 64-bit handles). VISA, IVI, and VXI
 plug&play
 handles are always 32-bit handles. NI Switch Executive and custom handles match the architecture.

#### Purpose

Returns the C-based instrument API handle to the driver for a specific interface level. The driver initializes, if necessary. If the session does not support the interface level you request, this method returns a zero-valued handle as an error.

#### Remarks

The session stores the API handle and manages its lifetime.

Note

#### Parameters

level
 As
 [InterfaceLevel](interfacelevel.html)

[In] Specifies the type of API handle to return.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-getlockstate.html language=enus -->
## TOPIC 00056: InstrSession.GetLockState

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-getlockstate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-getlockstate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetLockState( ownerKey, nestingLevel) Purpose Returns the key that owns the lock and the number of times the key acquired the lock. Parameters ownerKey As String [Out] Returns the key that owns the lock. Returns an empty string for unlocked sessions. nestingLevel As Long [Out] Re

### InstrSession.GetLockState

#### Syntax

[InstrSession](instrsession.html).GetLockState( ownerKey, nestingLevel)

#### Purpose

Returns the key that owns the lock and the number of times the key acquired the lock.

#### Parameters

ownerKey
 As
 [String](data-types-for-session-manager.html)

[Out] Returns the key that owns the lock. Returns an empty string for unlocked sessions.

nestingLevel
 As
 [Long](data-types-for-session-manager.html)

[Out] Returns the number of times the owning key acquired the lock without a balancing call to the
 [InstrSession.UnlockSession](instrsession-unlocksession.html)
 method. The owning key retains the lock until you call the
 InstrSession.UnlockSession
 method once for each successful call to the
 [InstrSession.LockSession](instrsession-locksession.html)
 method.

#### See Also

[InstrSession.LockSession](instrsession-locksession.html)

[InstrSession.UnlockSession](instrsession-unlocksession.html)

[Session Locking](/csh?context=ts_smgrref_session_locking)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-getlong.html language=enus -->
## TOPIC 00057: InstrSession.GetLong

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-getlong.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-getlong.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetLong( uniqueId) Return Value Long Returns the long integer value that the string you pass identifies. Purpose Returns the long integer value attached to the session with the string ID you specify. Parameters uniqueId As String [In] Pass the unique string that identifies the va

### InstrSession.GetLong

#### Syntax

[InstrSession](instrsession.html).GetLong( uniqueId)

#### Return Value

[Long](data-types-for-session-manager.html)

Returns the long integer value that the string you pass identifies.

#### Purpose

Returns the long integer value attached to the session with the string ID you specify.

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass the unique string that identifies the value to obtain.

#### See Also

[Attaching Additional Data to a Session](/csh?context=ts_smgrref_attaching_additional_data_to_a_session)

[InstrSession.AttachLong](instrsession-attachlong.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-getlongptr.html language=enus -->
## TOPIC 00058: InstrSession.GetLongPtr

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-getlongptr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-getlongptr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetLongPtr( uniqueId) Return Value Variant Returns the pointer-sized integer value that the string you pass identifies. Purpose Returns the pointer-sized integer value attached to the session with the string ID you specify. Remarks The type of the variant returned matches the arc

### InstrSession.GetLongPtr

#### Syntax

[InstrSession](instrsession.html).GetLongPtr( uniqueId)

#### Return Value

[Variant](data-types-for-session-manager.html)

Returns the pointer-sized integer value that the string you pass identifies.

#### Purpose

Returns the pointer-sized integer value attached to the session with the string ID you specify.

#### Remarks

The type of the variant returned matches the architecture of the session instance (
 VT_I4
 for 32-bit instances and
 VT_I8
 for 64-bit instances).

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass the unique string that identifies the value to obtain.

#### See Also

[Attaching Additional Data to a Session](/csh?context=ts_smgrref_attaching_additional_data_to_a_session)

[InstrSession.AttachLongPtr](instrsession-attachlongptr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-getobject.html language=enus -->
## TOPIC 00059: InstrSession.GetObject

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-getobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-getobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetObject( uniqueId) Return Value IUnknown Returns a reference to the object that the string you pass identifies. Purpose Returns the ActiveX object attached to the session with the string ID you specify. Call QueryInterface on the object to obtain a specific interface. Parameter

### InstrSession.GetObject

#### Syntax

[InstrSession](instrsession.html).GetObject( uniqueId)

#### Return Value

[IUnknown](data-types-for-session-manager.html)

Returns a reference to the object that the string you pass identifies.

#### Purpose

Returns the ActiveX object attached to the session with the string ID you specify. Call QueryInterface on the object to obtain a specific interface.

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass the unique string that identifies the object to obtain.

#### See Also

[Attaching Additional Data to a Session](/csh?context=ts_smgrref_attaching_additional_data_to_a_session)

[InstrSession.AttachObject](instrsession-attachobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-getstring.html language=enus -->
## TOPIC 00060: InstrSession.GetString

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-getstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-getstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetString( uniqueId) Return Value String Returns the string value that the string you pass identifies. Purpose Returns the string value attached to the session with the string ID you specify. Parameters uniqueId As String [In] Pass the unique string that identifies the value to o

### InstrSession.GetString

#### Syntax

[InstrSession](instrsession.html).GetString( uniqueId)

#### Return Value

[String](data-types-for-session-manager.html)

Returns the string value that the string you pass identifies.

#### Purpose

Returns the string value attached to the session with the string ID you specify.

#### Parameters

uniqueId
 As
 [String](data-types-for-session-manager.html)

[In] Pass the unique string that identifies the value to obtain.

#### See Also

[InstrSession.AttachString](instrsession-attachstring.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-getvppbaseinterface.html language=enus -->
## TOPIC 00061: InstrSession.GetVPPBaseInterface

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-getvppbaseinterface.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-getvppbaseinterface.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.GetVPPBaseInterface Return Value VPPBase Returns a VPPBase interface for the session. Purpose Returns an interface that provides the standard VXI plug&play functions, except for init and close , on a session to a VXI plug&play -compliant driver. If the session does not connect to

### InstrSession.GetVPPBaseInterface

#### Syntax

[InstrSession](instrsession.html).GetVPPBaseInterface

#### Return Value

[VPPBase](vppbase.html)

Returns a
 [VPPBase](vppbase.html)
 interface for the session.

#### Purpose

Returns an interface that provides the standard VXI
 plug&play
 functions, except for
 init
 and
 close
 , on a session to a VXI
 plug&play
 -compliant driver. If the session does not connect to a VXI
 plug&play
 -compliant driver, this method returns an
 E_NOTIMPL
 error.

#### See Also

[VPPBase](vppbase.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-inexternalprocess.html language=enus -->
## TOPIC 00062: InstrSession.InExternalProcess

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-inexternalprocess.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-inexternalprocess.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.InExternalProcess Data Type Boolean Purpose Indicates if the session exists in the shared external process or in the current process. Remarks National Instruments recommends that you use this property only when debugging. See Also Limitations with Sharing Instrument Sessions Amon

### InstrSession.InExternalProcess

#### Syntax

[InstrSession](instrsession.html).InExternalProcess

#### Data Type

[Boolean](data-types-for-session-manager.html)

#### Purpose

Indicates if the session exists in the shared external process or in the current process.

#### Remarks

Note

#### See Also

[Limitations with Sharing Instrument Sessions Among Processes](/csh?context=ts_smgrref_sharing_instrument_sessions_between_processes)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-initialize.html language=enus -->
## TOPIC 00063: InstrSession.Initialize

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-initialize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-initialize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.Initialize( options = "") Purpose Initializes the driver or I/O resource for the session. This method does nothing if the session is already initialized. Typically, you do not call this method directly. The InstrSession.GetHandle and InstrSession.GetCOMDriver methods automaticall

### InstrSession.Initialize

#### Syntax

[InstrSession](instrsession.html).Initialize( options = "")

#### Purpose

Initializes the driver or I/O resource for the session. This method does nothing if the session is already initialized. Typically, you do not call this method directly. The
 [InstrSession.GetHandle](instrsession-gethandle.html)
 and
 [InstrSession.GetCOMDriver](instrsession-getcomdriver.html)
 methods automatically call this method.

#### Remarks

If the driver is not initialized, this method
 [initializes it with the specified options](/csh?context=ts_smgrref_initialize_with_options)
 . The format of the options string is driver-dependent. Pass an empty string as the
 options
 parameter to use the default options.

#### Parameters

options
 As
 [String](data-types-for-session-manager.html)

[In] Specifies initialization options in a driver-dependent format. Pass an empty string to use the default initialization options. Session Manager provides IVI sessions with additional initialization options. You can specify whether the driver performs an ID query when it initializes by using the following syntax:
 IdQuery = True | False, Reset = True | False
 . Additional options are case insensitive. You can place these options anywhere in the option string.

This parameter has a default value of
 ""
 .

#### See Also

[Initialize with Options](/csh?context=ts_smgrref_initialize_with_options)

[InstrSession.Close](instrsession-close.html)

[InstrSession.GetCOMDriver](instrsession-getcomdriver.html)

[InstrSession.GetHandle](instrsession-gethandle.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-isinitialized.html language=enus -->
## TOPIC 00064: InstrSession.IsInitialized

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-isinitialized.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-isinitialized.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.IsInitialized Return Value Boolean Purpose Returns a value that indicates whether the driver or I/O resource for the session is currently initialized. See Also InstrSession.Close InstrSession.Initialize

### InstrSession.IsInitialized

#### Syntax

[InstrSession](instrsession.html).IsInitialized

#### Return Value

[Boolean](data-types-for-session-manager.html)

#### Purpose

Returns a value that indicates whether the driver or I/O resource for the session is currently initialized.

#### See Also

[InstrSession.Close](instrsession-close.html)

[InstrSession.Initialize](instrsession-initialize.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-locksession.html language=enus -->
## TOPIC 00065: InstrSession.LockSession

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-locksession.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-locksession.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.LockSession( keyName, timeout, reserved) Purpose Locks the session with the case-insensitive key name you specify. If the session is locked with a different key name, the method waits until the session becomes available or returns an error when the timeout period expires. Paramet

### InstrSession.LockSession

#### Syntax

[InstrSession](instrsession.html).LockSession( keyName, timeout, reserved)

#### Purpose

Locks the session with the case-insensitive key name you specify. If the session is locked with a different key name, the method waits until the session becomes available or returns an error when the timeout period expires.

#### Parameters

keyName
 As
 [String](data-types-for-session-manager.html)

[In] Pass the key name with which to lock the session.

timeout
 As
 [Double](data-types-for-session-manager.html)

[In] Pass the number of seconds to wait for the lock to become available before timing out. Pass a timeout value of
 -1.0
 to wait indefinitely.

reserved
 As
 [Long](data-types-for-session-manager.html)

[In] Pass a zero value to this reserved parameter.

#### See Also

[InstrSession.UnlockSession](instrsession-unlocksession.html)

[Session Locking](/csh?context=ts_smgrref_session_locking)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-name.html language=enus -->
## TOPIC 00066: InstrSession.Name

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.Name Data Type String Purpose Returns the session name, which does not include a category prefix. See Also InstrSession.Category

### InstrSession.Name

#### Syntax

[InstrSession](instrsession.html).Name

#### Data Type

[String](data-types-for-session-manager.html)

#### Purpose

Returns the session name, which does not include a category prefix.

#### See Also

[InstrSession.Category](instrsession-category.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-statedescription.html language=enus -->
## TOPIC 00067: InstrSession.StateDescription

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-statedescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-statedescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.StateDescription Data Type String Purpose Returns a string that describes the session properties and all attached data.

### InstrSession.StateDescription

#### Syntax

[InstrSession](instrsession.html).StateDescription

#### Data Type

[String](data-types-for-session-manager.html)

#### Purpose

Returns a string that describes the session properties and all attached data.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession-unlocksession.html language=enus -->
## TOPIC 00068: InstrSession.UnlockSession

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession-unlocksession.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession-unlocksession.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSession.UnlockSession Purpose Releases the most recent lock. You must call this method to balance each successful call to the InstrSession.LockSession method. See Also InstrSession.LockSession Session Locking

### InstrSession.UnlockSession

#### Syntax

[InstrSession](instrsession.html).UnlockSession

#### Purpose

Releases the most recent lock. You must call this method to balance each successful call to the
 [InstrSession.LockSession](instrsession-locksession.html)
 method.

#### See Also

[InstrSession.LockSession](instrsession-locksession.html)

[Session Locking](/csh?context=ts_smgrref_session_locking)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsession.html language=enus -->
## TOPIC 00069: InstrSession

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsession.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsession.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the InstrSession class to share instrument driver API handles or I/O resource handles among software modules. Each InstrSession object has a unique name you use to retrieve the session from Session Manager. Properties Category CloseEnabled CloseFunctionEx InExternalProcess Name StateDescription

### InstrSession

Use the
 InstrSession
 class to share instrument driver API handles or I/O resource handles among software modules. Each
 InstrSession
 object has a unique name you use to retrieve the session from Session Manager.

#### Properties

| Category |
| --- |
| CloseEnabled |
| CloseFunctionEx |
| InExternalProcess |
| Name |
| StateDescription (Read Only) |

#### Methods

| AttachLong |
| --- |
| AttachLongPtr |
| AttachObject |
| AttachString |
| Close |
| DetachData |
| GenerateUniqueID |
| GetCOMDriver |
| GetHandleEx |
| GetLockState |
| GetLong |
| GetLongPtr |
| GetObject |
| GetString |
| GetVPPBaseInterface |
| Initialize |
| IsInitialized |
| LockSession |
| UnlockSession |

Parent topic:

Session Manager Objects

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-audiblelifetimealerts.html language=enus -->
## TOPIC 00070: InstrSessionMgr.AudibleLifeTimeAlerts

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-audiblelifetimealerts.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-audiblelifetimealerts.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.AudibleLifeTimeAlerts Data Type Boolean Purpose Specifies whether a beep signifies the creation and destruction of session manager and individual sessions. Enable this property when debugging to help monitor the lifetime of session manager objects. Remarks National Instruments

### InstrSessionMgr.AudibleLifeTimeAlerts

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).AudibleLifeTimeAlerts

#### Data Type

[Boolean](data-types-for-session-manager.html)

#### Purpose

Specifies whether a beep signifies the creation and destruction of session manager and individual sessions. Enable this property when debugging to help monitor the lifetime of session manager objects.

#### Remarks

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-getcategories.html language=enus -->
## TOPIC 00071: InstrSessionMgr.GetCategories

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-getcategories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-getcategories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.GetCategories( baseCategory) Return Value String Array Purpose Returns an array of category names. Parameters baseCategory As String [In] Pass "?" or an empty string to obtain all top-level categories. Pass a top-level category to obtain the subcategories of that category. See

### InstrSessionMgr.GetCategories

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).GetCategories( baseCategory)

#### Return Value

[String Array](data-types-for-session-manager.html)

#### Purpose

Returns an array of category names.

#### Parameters

baseCategory
 As
 [String](data-types-for-session-manager.html)

[In] Pass
 "?"
 or an empty string to obtain all top-level categories. Pass a top-level category to obtain the subcategories of that category.

#### See Also

[Instrument Session Categories](/csh?context=ts_smgrref_instrument_session_categories)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-getinstrsession.html language=enus -->
## TOPIC 00072: InstrSessionMgr.GetInstrSession

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-getinstrsession.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-getinstrsession.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.GetInstrSession( name, newSession) Return Value InstrSession Returns the instrument session you specify. Purpose Returns the instrument session you specify or creates the session if it does not already exist. For typical applications that use sessions that are valid only in-pr

### InstrSessionMgr.GetInstrSession

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).GetInstrSession( name, newSession)

#### Return Value

[InstrSession](instrsession.html)

Returns the instrument session you specify.

#### Purpose

Returns the instrument session you specify or creates the session if it does not already exist. For typical applications that use sessions that are valid only in-process, pass
 False
 as the
 newSession
 parameter for the server to return an existing session the application previously opened. Pass
 True
 as the
 newSession
 parameter when the application requires a new session independent of whether the application previously opened a session.

#### Remarks

IVI name resource descriptors are case sensitive and must match the entry in the IVI Configuration Store. All other instrument session names are case insensitive.

#### Parameters

name
 As
 [String](data-types-for-session-manager.html)

[In] Pass the name of the session to return.

newSession
 As
 [Boolean](data-types-for-session-manager.html)

[In] Pass
 False
 for Session Manager to return the existing session with the name you specify or, if no session exists, to create a new session with the specified name. Pass
 True
 for Session Manager to always create a new session whether a session with the name you specify already exists. Session Manager always appends a unique numeric suffix to the name you specify.

#### See Also

[Instrument Session Names](/csh?context=ts_smgrref_instrument_session_names)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-getnames.html language=enus -->
## TOPIC 00073: InstrSessionMgr.GetNames

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-getnames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-getnames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.GetNames( category, flags, filter) Return Value String Array Returns the array of session names. Purpose Returns an array of the names for which you can obtain sessions. Parameters category As String [In] Pass a category name to restrict the list so it contains only names in a

### InstrSessionMgr.GetNames

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).GetNames( category, flags, filter)

#### Return Value

[String Array](data-types-for-session-manager.html)

Returns the array of session names.

#### Purpose

Returns an array of the names for which you can obtain sessions.

#### Parameters

category
 As
 [String](data-types-for-session-manager.html)

[In] Pass a category name to restrict the list so it contains only names in a specific category. Pass an empty string or
 "?"
 to retrieve names from all categories.

flags
 As
 [GetNamesOptions](getnamesoptions.html)

[In] Pass any combination of
 GetNamesOptions
 bit flags. Typically, applications pass
 ReturnLogicalNames
 .

filter
 As
 [String](data-types-for-session-manager.html)

[In] Pass a filter string to exclude names from the list. Use the filter string to return only names of sessions that connect to drivers that use the prefix you specify. The filter string uses the following syntax:
 "SpecificPrefix=driver prefix, SpecificPrefix=driver prefix 2, ..."
 . Pass an empty string to return all sessions, regardless of the specific driver.

#### See Also

[GetNamesOptions](getnamesoptions.html)

[Instrument Session Categories](/csh?context=ts_smgrref_instrument_session_categories)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-getsessions.html language=enus -->
## TOPIC 00074: InstrSessionMgr.GetSessions

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-getsessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-getsessions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.GetSessions( category) Return Value Object Array Purpose Returns an array of all existing session objects that are in the category you specify. Remarks National Instruments recommends that you use this property only when debugging. Parameters category As String [In] Pass "*" t

### InstrSessionMgr.GetSessions

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).GetSessions( category)

#### Return Value

[Object Array](data-types-for-session-manager.html)

#### Purpose

Returns an array of all existing session objects that are in the category you specify.

#### Remarks

Note

#### Parameters

category
 As
 [String](data-types-for-session-manager.html)

[In] Pass
 "*"
 to obtain a list of the sessions in the external process.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-getuniquekeyname.html language=enus -->
## TOPIC 00075: InstrSessionMgr.GetUniqueKeyName

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-getuniquekeyname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-getuniquekeyname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.GetUniqueKeyName( keyName) Purpose Generates a unique key name you can pass to the InstrSession.LockSession method of a session object. Parameters keyName As String [Out] Returns a unique key name. See Also InstrSession.LockSession Session Locking

### InstrSessionMgr.GetUniqueKeyName

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).GetUniqueKeyName( keyName)

#### Purpose

Generates a unique key name you can pass to the
 [InstrSession.LockSession](instrsession-locksession.html)
 method of a session object.

#### Parameters

keyName
 As
 [String](data-types-for-session-manager.html)

[Out] Returns a unique key name.

#### See Also

[InstrSession.LockSession](instrsession-locksession.html)

[Session Locking](/csh?context=ts_smgrref_session_locking)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-hidecategory.html language=enus -->
## TOPIC 00076: InstrSessionMgr.HideCategory

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-hidecategory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-hidecategory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.HideCategory( category, hide) Purpose Hides a top-level category. For example, if you do not use VISA sessions, you can hide the "VISA" category to avoid retrieving VISA logical names and to avoid spending the time it takes VISA to initially query for available resource names

### InstrSessionMgr.HideCategory

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).HideCategory( category, hide)

#### Purpose

Hides a top-level category. For example, if you do not use VISA sessions, you can hide the "VISA" category to avoid retrieving VISA logical names and to avoid spending the time it takes VISA to initially query for available resource names the first time you call the
 [InstrSessionMgr.GetNames](instrsessionmgr-getnames.html)
 method.

#### Parameters

category
 As
 [String](data-types-for-session-manager.html)

[In] Pass the name of the top-level category to hide or show.

hide
 As
 [Boolean](data-types-for-session-manager.html)

[In] Pass
 True
 or
 False
 to specify whether to hide the category.

#### See Also

[InstrSessionMgr.GetNames](instrsessionmgr-getnames.html)

[Instrument Session Categories](/csh?context=ts_smgrref_instrument_session_categories)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-inexternalprocess.html language=enus -->
## TOPIC 00077: InstrSessionMgr.InExternalProcess

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-inexternalprocess.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-inexternalprocess.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.InExternalProcess Data Type Boolean Purpose Indicates whether Session Manager exists in the external process or in the current process. Remarks National Instruments recommends that you use this property only when debugging. See Also Limitations with Sharing Instrument Sessions

### InstrSessionMgr.InExternalProcess

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).InExternalProcess

#### Data Type

[Boolean](data-types-for-session-manager.html)

#### Purpose

Indicates whether Session Manager exists in the external process or in the current process.

#### Remarks

Note

#### See Also

[Limitations with Sharing Instrument Sessions Between Processes](/csh?context=ts_smgrref_sharing_instrument_sessions_between_processes)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-installinstrsession.html language=enus -->
## TOPIC 00078: InstrSessionMgr.InstallInstrSession

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-installinstrsession.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-installinstrsession.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.InstallInstrSession( name, instrSession) Purpose This method is reserved for future use. Parameters name As String [In] Reserved for future use. instrSession As InstrSession [In] Reserved for future use.

### InstrSessionMgr.InstallInstrSession

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).InstallInstrSession( name, instrSession)

#### Purpose

This method is reserved for future use.

#### Parameters

name
 As
 [String](data-types-for-session-manager.html)

[In] Reserved for future use.

instrSession
 As
 [InstrSession](instrsession.html)

[In] Reserved for future use.

Parent topic:

Obsolete InstrSessionMgr Method

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-invalidatevisaresourcelist.html language=enus -->
## TOPIC 00079: InstrSessionMgr.InvalidateVisaResourceList

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-invalidatevisaresourcelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-invalidatevisaresourcelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.InvalidateVisaResourceList Purpose Invalidates the Session Manager internal list of VISA resources, causing VISA to rescan the system for the list of available resources the next time you request a list of available session names that include VISA sessions. Call this method wh

### InstrSessionMgr.InvalidateVisaResourceList

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).InvalidateVisaResourceList

#### Purpose

Invalidates the Session Manager internal list of VISA resources, causing VISA to rescan the system for the list of available resources the next time you request a list of available session names that include VISA sessions. Call this method when you alter the system hardware configuration.

Note

#### See Also

[InstrSessionMgr.GetNames](instrsessionmgr-getnames.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr-statedescription.html language=enus -->
## TOPIC 00080: InstrSessionMgr.StateDescription

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr-statedescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr-statedescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InstrSessionMgr.StateDescription Data Type String Purpose Returns a string that describes all session names and all session objects for the current process and the shared external process. Remarks National Instruments recommends that you use this property only when debugging.

### InstrSessionMgr.StateDescription

#### Syntax

[InstrSessionMgr](instrsessionmgr.html).StateDescription

#### Data Type

[String](data-types-for-session-manager.html)

#### Purpose

Returns a string that describes all session names and all session objects for the current process and the shared external process.

#### Remarks

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/instrsessionmgr.html language=enus -->
## TOPIC 00081: InstrSessionMgr

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/instrsessionmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/instrsessionmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the InstrSessionMgr class to provide lists of the available logical and virtual instrument names and to return an instrument session interface for a logical or virtual instrument name you specify. Properties AudibleLifeTimeAlerts InExternalProcess StateDescription (Read Only) Methods GetCategori

### InstrSessionMgr

Use the
 InstrSessionMgr
 class to provide lists of the available logical and virtual instrument names and to return an instrument session interface for a logical or virtual instrument name you specify.

#### Properties

| AudibleLifeTimeAlerts |
| --- |
| InExternalProcess |
| StateDescription (Read Only) |

#### Methods

| GetCategories |
| --- |
| GetInstrSession |
| GetNames |
| GetSessions |
| GetUniqueKeyName |
| HideCategory |
| InvalidateVisaResourceList |

Parent topic:

Session Manager Objects

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/interfacelevel.html language=enus -->
## TOPIC 00082: InterfaceLevel

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/interfacelevel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/interfacelevel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants in the level parameter of the InstrSession.GetHandle and the InstrSession.GetCOMDriver methods to specify what kind of instrument API instance handle or ActiveX interface to return. Session Manager assumes that a VXI plug&play -specific driver handle is also the I/O handle, which

### InterfaceLevel

Use these constants in the
 level
 parameter of the
 [InstrSession.GetHandle](instrsession-gethandle.html)
 and the
 [InstrSession.GetCOMDriver](instrsession-getcomdriver.html)
 methods to specify what kind of instrument API instance handle or ActiveX interface to return.

Session Manager assumes that a VXI
 plug&play
 -specific driver handle is also the I/O handle, which is a valid assumption for the majority of VXI
 plug&play
 drivers. For VXI
 plug&play
 drivers for which this assumption is not true, no standard way exists to obtain the I/O handle.

- ClassDriver 
 –(Value: 1) Specifies that only IVI sessions can return a class API handle. Use a class handle to control an instrument using an IVI class driver or an IVI class COM interface. VXI
 plug&play 
 and VISA are not applicable.
- DefaultInterface 
 –(Value: 0) Specifies that IVI returns a class API handle, VXI
 plug&play 
 returns a specific API handle, and VISA returns the I/O handle.
- IODriver 
 –(Value: 3) Specifies that IVI, VXI
 plug&play 
 , and VISA sessions can return an API handle. Use an API handle to control an instrument communication library, such as VISA.
- SpecificDriver 
 –(Value: 2) Specifies that IVI and VXI
 plug&play 
 sessions can return a specific API handle. Use a specific API handle to control an instrument using an instrument-specific driver. VISA is not applicable.

#### See Also

[InstrSession.GetCOMDriver](instrsession-getcomdriver.html)

[InstrSession.GetHandle](instrsession-gethandle.html)

Parent topic:

Session Manager API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/methods.html language=enus -->
## TOPIC 00083: Methods

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

InstrSession

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/methods_2.html language=enus -->
## TOPIC 00084: Methods

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/methods_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/methods_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

InstrSessionMgr

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/methods_3.html language=enus -->
## TOPIC 00085: Methods

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/methods_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/methods_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

VPPBase

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/obsolete-instrsession-methods.html language=enus -->
## TOPIC 00086: Obsolete InstrSession Methods

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/obsolete-instrsession-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/obsolete-instrsession-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method GetHandle InstrSession.GetHandleEx method

### Obsolete InstrSession Methods

The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| GetHandle | InstrSession.GetHandleEx method |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/obsolete-instrsession-properties.html language=enus -->
## TOPIC 00087: Obsolete InstrSession Properties

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/obsolete-instrsession-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/obsolete-instrsession-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following properties are now obsolete. National Instruments supports these properties but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Property Preferred Property or Method CloseFunction InstrSession.CloseFunctionEx

### Obsolete InstrSession Properties

The following properties are now obsolete. National Instruments supports these properties but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Property | Preferred Property or Method |
| --- | --- |
| CloseFunction | InstrSession.CloseFunctionEx property |

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/obsolete-instrsessionmgr-method.html language=enus -->
## TOPIC 00088: Obsolete InstrSessionMgr Method

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/obsolete-instrsessionmgr-method.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/obsolete-instrsessionmgr-method.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Property or Method InstallInstrSession —

### Obsolete InstrSessionMgr Method

The following methods are now obsolete. National Instruments supports these methods but recommends that you update files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Property or Method |
| --- | --- |
| InstallInstrSession | — |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/omitting-optional-parameters.html language=enus -->
## TOPIC 00089: Omitting Optional Parameters

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/omitting-optional-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/omitting-optional-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: LabVIEW To omit an optional parameter in LabVIEW, do not wire the input terminal for the parameter on the method Invoke Node. LabWindows/CVI Pass the value CA_DEFAULT_VAL to omit an optional input parameter. You cannot pass CA_DEFAULT_VAL to an output or in/out parameter. To omit an optional output

### Omitting Optional Parameters

LabVIEW

To omit an optional parameter in LabVIEW, do not wire the input terminal for the parameter on the method Invoke Node.

LabWindows/CVI

CA_DEFAULT_VAL

CA_DEFAULT_VAL

CA_DEFAULT_VAL

Note

[Com Threading]

CA_InitActiveXThreadStyleForCurrentThread

COINIT_APARTMENTTHREADED

Microsoft Visual Basic and Microsoft Visual Basic .NET

In Microsoft Visual Basic and Microsoft Visual Basic .NET, do not specify the parameter.

C Sharp

Pass
 System.Type.Missing
 to omit an optional input parameter. You cannot pass
 System.Type.Missing
 to an out or ref parameter. To omit an out or ref parameter, initialize a local variable using an object type to the value
 System.Type.Missing
 and pass the local variable.

C++ (Using Compiler COM)

Pass the value
 vtMissing
 to omit an optional input parameter. Pass
 &vtMissing
 to omit an optional output or in/out parameter.

Parent topic:

Session Manager Objects

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/picture.html language=enus -->
## TOPIC 00090: Picture

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/picture.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/picture.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Picture object specifies an image. Microsoft defines this standard Picture object implementation in the Object Linking and Embedding (OLE) Automation Version 2.0 type library file, stdole2.tlb . Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles. Refer to Micr

### Picture

A Picture object specifies an image. Microsoft defines this standard Picture object implementation in the Object Linking and Embedding (OLE) Automation Version 2.0 type library file,
 stdole2.tlb
 . Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles. Refer to Microsoft documentation for more information about this interface.

The Picture interface specifies the following properties and methods:

#### Properties

- Handle (Read Only) 
 —Returns the Microsoft Windows graphics device interface (GDI) handle of the image managed within the Picture object.
- Attributes (Read Only) 
 —Returns the attributes of the image.
- CurDC 
 —Specifies the current device context into which this image is selected.
- Height (Read Only) 
 —Returns the current height of the image in the Picture object.
- Hpal 
 —Specifies the current palette the Picture object uses.
- Type (Read Only) 
 —Returns the current type of the image.
- Width (Read Only) 
 —Returns the current width of the image in the Picture object.
- KeepOriginalFormat 
 —Specifies whether the image maintains the original format.

#### Methods

- Render 
 —Draws the specified portion of the image onto the specified device context, positioned at the specified location.
- SelectPicture 
 —Selects a bitmap image into a given device context, returning the device context in which the image was previously selected as well as the GDI handle of the image.
- PictureChanged 
 —Notifies the Picture object that its image resource changed.
- SaveAsFile 
 —Saves the image data into a stream in the same format as it would save itself into a file.

LabVIEW

The LabVIEW development environment automatically recognizes Picture ActiveX references. Use the Invoke Node and Property Node VIs to access the methods and properties of a Picture ActiveX reference.

Note

LabWindows/CVI

LabWindows/CVI creates and accesses ActiveX objects using functions in a LabWindows/CVI-generated driver. You must create a driver for the OLE Automation ActiveX server using the ActiveX Controller Wizard. Select
 Tools»Create ActiveX Controller
 to launch the wizard, select
 OLE Automation
 in the ActiveX Server list control, and proceed to build the driver. Use the functions for the Picture class to access the methods and properties.

Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can access Picture objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

Imports stdole.StdPictureClass

The IPictureDisp class and its methods and properties are available in the Microsoft Visual Studio object browser and are accessible from the Visual Basic .NET source code.

C#

In C#, you can access Picture objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

using stdole.StdPictureClass;

The IPictureDisp class and its methods and properties are available in the Visual Studio object browser and are accessible from the C# source code.

Microsoft Visual C++/#import

In C++, you can access Picture objects by adding the include file
 ocidl.h
 and using the CComPtr template to manage IPictureDisp COM interface pointers.

Parent topic:

Data Types for Session Manager

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/properties.html language=enus -->
## TOPIC 00091: Properties

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

InstrSession

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/properties_2.html language=enus -->
## TOPIC 00092: Properties

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/properties_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/properties_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

InstrSessionMgr

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/session-manager-api-enumerations.html language=enus -->
## TOPIC 00093: Session Manager API Enumerations

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/session-manager-api-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/session-manager-api-enumerations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about the Session Manager API enumerations.

### Session Manager API Enumerations

This book contains information about the Session Manager API enumerations.

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/session-manager-objects.html language=enus -->
## TOPIC 00094: Session Manager Objects

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/session-manager-objects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/session-manager-objects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Object and Description InstrSession Use the InstrSession class to share instrument driver API handles or I/O resource handles among software modules. Each InstrSession object has a unique name you use to retrieve the session from Session Manager. InstrSessionMgr Use the InstrSessionMgr class to prov

### Session Manager Objects

| Object and Description |
| --- |
| InstrSession |
| Use the InstrSession class to share instrument driver API handles or I/O resource handles among software modules. Each InstrSession object has a unique name you use to retrieve the session from Session Manager. |
| InstrSessionMgr |
| Use the InstrSessionMgr class to provide lists of the available logical and virtual instrument names and to return an instrument session interface for a logical or virtual instrument name you specify. |
| VPPBase |
| The VPPBase class includes the standard VXI plug&play functions, except for init and close , for a session of a VXI plug&play -compliant driver. You obtain this interface from a session for a VXI plug&play driver or an IVI driver. |

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/vartype.html language=enus -->
## TOPIC 00095: VARTYPE

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/vartype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/vartype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following list identifies the VARTYPE enumeration values: Constant Value Description VT_EMPTY 0 Not specified VT_NULL 1 SQL-style NULL VT_I2 2 2-byte signed int VT_I4 3 4-byte-signed int VT_R4 4 4-byte real VT_R8 5 8-byte real VT_CY 6 Currency VT_DATE 7 Date VT_BSTR 8 Automation string VT_DISPAT

### VARTYPE

The following list identifies the VARTYPE enumeration values:

| Constant | Value | Description |
| --- | --- | --- |
| VT_EMPTY | 0 | Not specified |
| VT_NULL | 1 | SQL-style NULL |
| VT_I2 | 2 | 2-byte signed int |
| VT_I4 | 3 | 4-byte-signed int |
| VT_R4 | 4 | 4-byte real |
| VT_R8 | 5 | 8-byte real |
| VT_CY | 6 | Currency |
| VT_DATE | 7 | Date |
| VT_BSTR | 8 | Automation string |
| VT_DISPATCH | 9 | IDispatch* |
| VT_ERROR | 10 | Scodes |
| VT_BOOL | 11 | Boolean ( True = -1 , False = 0 ) |
| VT_VARIANT | 12 | VARIANT* |
| VT_UNKNOWN | 13 | IUnknown* |
| VT_DECIMAL | 14 | 16-byte fixed point |
| VT_Record | 15 | User-defined type |
| VT_I1 | 16 | Char |
| VT_UI1 | 17 | Unsigned char |
| VT_UI2 | 18 | 2-byte unsigned char |
| VT_UI4 | 19 | 4-byte unsigned char |
| VT_I8 | 20 | 8-byte signed int |
| VT_UI8 | 21 | 8-byte unsigned int |
| VT_INT | 22 | Signed machine int |
| VT_UINT | 23 | Unsigned machine int |
| VT_ARRAY | 0x2000 | SAFEARRAY* |
| VT_BYREF | 0x4000 | — |

Parent topic:

Data Types for Session Manager

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/vppbase-error-message.html language=enus -->
## TOPIC 00096: VPPBase.Error_Message

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/vppbase-error-message.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/vppbase-error-message.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax VPPBase.Error_Message( errorCode, errorMessage) Return Value Long Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred. Purpose Converts a status code an instrument dr

### VPPBase.Error_Message

#### Syntax

[VPPBase](vppbase.html).Error_Message( errorCode, errorMessage)

#### Return Value

[Long](data-types-for-session-manager.html)

Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred.

#### Purpose

Converts a status code an instrument driver function returns into a user-readable message string.

#### Parameters

errorCode
 As
 [Long](data-types-for-session-manager.html)

[In] Pass the status parameter that any of the instrument driver functions return.

errorMessage
 As
 [String](data-types-for-session-manager.html)

[Out] Returns the user-readable message string that corresponds to the status code you specify.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/vppbase-error-query.html language=enus -->
## TOPIC 00097: VPPBase.Error_Query

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/vppbase-error-query.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/vppbase-error-query.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax VPPBase.Error_Query( errorCode, errorMessage) Return Value Long Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred. Purpose Reads an error code and a message from th

### VPPBase.Error_Query

#### Syntax

[VPPBase](vppbase.html).Error_Query( errorCode, errorMessage)

#### Return Value

[Long](data-types-for-session-manager.html)

Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred.

#### Purpose

Reads an error code and a message from the instrument error queue.

#### Parameters

errorCode
 As
 [Long](data-types-for-session-manager.html)

[Out] Returns the error code read from the instrument error queue.

errorMessage
 As
 [String](data-types-for-session-manager.html)

[Out] Returns the error message string read from the instrument error message queue.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/vppbase-reset.html language=enus -->
## TOPIC 00098: VPPBase.Reset

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/vppbase-reset.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/vppbase-reset.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax VPPBase.Reset Return Value Long Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred. Purpose Resets the instrument to a known state and sends initialization commands

### VPPBase.Reset

#### Syntax

[VPPBase](vppbase.html).Reset

#### Return Value

[Long](data-types-for-session-manager.html)

Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred.

#### Purpose

Resets the instrument to a known state and sends initialization commands to the instrument.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/vppbase-revision-query.html language=enus -->
## TOPIC 00099: VPPBase.Revision_Query

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/vppbase-revision-query.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/vppbase-revision-query.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax VPPBase.Revision_Query( instrumentDriverRevision, firmwareRevision) Return Value Long Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred. Purpose Returns the revisio

### VPPBase.Revision_Query

#### Syntax

[VPPBase](vppbase.html).Revision_Query( instrumentDriverRevision, firmwareRevision)

#### Return Value

[Long](data-types-for-session-manager.html)

Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred.

#### Purpose

Returns the revision numbers of the instrument driver and instrument firmware.

#### Parameters

instrumentDriverRevision
 As
 [String](data-types-for-session-manager.html)

[Out] Returns the instrument driver software revision numbers.

firmwareRevision
 As
 [String](data-types-for-session-manager.html)

[Out] Returns the instrument firmware revision numbers.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/vppbase-self-test.html language=enus -->
## TOPIC 00100: VPPBase.Self_Test

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/vppbase-self-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/vppbase-self-test.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax VPPBase.Self_Test( selfTestResult, selfTestMessage) Return Value Long Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred. Purpose Runs the instrument self test routi

### VPPBase.Self_Test

#### Syntax

[VPPBase](vppbase.html).Self_Test( selfTestResult, selfTestMessage)

#### Return Value

[Long](data-types-for-session-manager.html)

Returns the driver-defined status code for this operation. A return value of zero indicates success. Positive values indicate warnings. Negative values indicate an error occurred.

#### Purpose

Runs the instrument self test routine and the test result(s).

#### Parameters

selfTestResult
 As
 [Integer](data-types-for-session-manager.html)

[Out] Returns the value from the instrument self test. A zero value indicates success, and a value of
 1
 indicates failure. Refer to the operator manual for the third-party device for information about any other code.

selfTestMessage
 As
 [String](data-types-for-session-manager.html)

[Out] Returns the self test response string from the instrument. Refer to the operator manual for the third-party device for information about the string contents.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=smgrref/vppbase.html language=enus -->
## TOPIC 00101: VPPBase

- bundle_id: `teststand-api-reference`
- source_path: `smgrref/vppbase.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/smgrref/vppbase.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The VPPBase class includes the standard VXI plug&play functions, except for init and close , for a session of a VXI plug&play -compliant driver. You obtain this interface from a session for a VXI plug&play driver or an IVI driver. Methods Error_Message Error_Query Reset Revision_Query Self_Test

### VPPBase

The
 VPPBase
 class includes the standard VXI
 plug&play
 functions, except for
 init
 and
 close
 , for a session of a VXI
 plug&play
 -compliant driver. You obtain this interface from a session for a VXI
 plug&play
 driver or an IVI driver.

#### Methods

| Error_Message |
| --- |
| Error_Query |
| Reset |
| Revision_Query |
| Self_Test |

Parent topic:

Session Manager Objects

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-analysisid.html language=enus -->
## TOPIC 00102: AnalysisContext.AnalysisId

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-analysisid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-analysisid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.AnalysisId Data Type Long Purpose Use this property in an analysis module to obtain the unique ID of the current analysis session. Remarks The TestStand Sequence Analyzer can perform multiple analysis sessions simultaneously. Each session specifies a unique analysis ID. In gen

### AnalysisContext.AnalysisId

#### Syntax

[AnalysisContext](analysiscontext.html).AnalysisId

#### Data Type

[Long](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this property in an analysis module to obtain the unique ID of the current analysis session.

#### Remarks

The TestStand Sequence Analyzer can perform multiple analysis sessions simultaneously. Each session specifies a unique analysis ID. In general, National Instruments recommends that you use the
 [AnalysisContext.GetRuleAnalysisData](analysiscontext-getruleanalysisdata.html)
 method to store global data generated during analysis. You can also store data in a global table that you index using the analysis session unique ID. Because the sequence analyzer can use multiple threads to perform analysis, you must implement locks around code that accesses the global table data.

#### See Also

[AnalysisContext.GetRuleAnalysisData](analysiscontext-getruleanalysisdata.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-editcontext.html language=enus -->
## TOPIC 00103: AnalysisContext.EditContext

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-editcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-editcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.EditContext Data Type SequenceContext Purpose Use this property in an analysis module to obtain a sequence context that corresponds to the object under analysis. This property is NULL when the TestStand Sequence Analyzer calls an analysis module for analysis transitions. See A

### AnalysisContext.EditContext

#### Syntax

[AnalysisContext](analysiscontext.html).EditContext

#### Data Type

[SequenceContext](../tsapiref/sequencecontext.html)

#### Purpose

Use this property in an analysis module to obtain a
 [sequence context](/csh?context=ts_tsfundamentals_seq_con)
 that corresponds to the object under analysis. This property is
 NULL
 when the TestStand Sequence Analyzer calls an analysis module for analysis transitions.

#### See Also

[AnalysisContext.Object](analysiscontext-object.html)

[AnalysisContext.Transition](analysiscontext-transition.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-engine.html language=enus -->
## TOPIC 00104: AnalysisContext.Engine

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-engine.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-engine.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.Engine Data Type Engine Purpose Use this property in an analysis module to access methods and properties in the TestStand Engine class. See Also AnalysisContext.EditContext TestStand Engine

### AnalysisContext.Engine

#### Syntax

[AnalysisContext](analysiscontext.html).Engine

#### Data Type

[Engine](../tsapiref/engine.html)

#### Purpose

Use this property in an analysis module to access methods and properties in the TestStand
 
 [Engine](../tsapiref/engine.html)
 class.

#### See Also

[AnalysisContext.EditContext](analysiscontext-editcontext.html)

TestStand
 [Engine](../tsapiref/engine.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-file.html language=enus -->
## TOPIC 00105: AnalysisContext.File

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-file.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.File Data Type PropertyObjectFile Purpose Use this property in an analysis module to access the file the TestStand Sequence Analyzer is currently analyzing. Remarks This property is NULL when the sequence analyzer calls an analysis module for the AnalysisTransition_BeforeSyste

### AnalysisContext.File

#### Syntax

[AnalysisContext](analysiscontext.html).File

#### Data Type

[PropertyObjectFile](../tsapiref/propertyobjectfile.html)

#### Purpose

Use this property in an analysis module to access the file the TestStand Sequence Analyzer is currently analyzing.

#### Remarks

This property is
 NULL
 when the sequence analyzer calls an analysis module for the
 [AnalysisTransition_BeforeSystem](analysistransition.html)
 and
 [AnalysisTransition_AfterSystem](analysistransition.html)
 analysis transitions.

#### See Also

[AnalysisContext.Transition](analysiscontext-transition.html)

[AnalysisTransition](analysistransition.html)

[Relationships among AnalysisContext Transition, File, and Object Properties](relationships-among-analysiscontext-transitio.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-getruleanalysisdata.html language=enus -->
## TOPIC 00106: AnalysisContext.GetRuleAnalysisData

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-getruleanalysisdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-getruleanalysisdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.GetRuleAnalysisData( RuleId, RuleAnalysisDataScope, options) Return Value PropertyObject Purpose Use this method in an analysis module to store and retrieve data to share among multiple calls to analysis modules. Remarks The TestStand Sequence Analyzer creates empty PropertyOb

### AnalysisContext.GetRuleAnalysisData

#### Syntax

[AnalysisContext](analysiscontext.html).GetRuleAnalysisData( RuleId, RuleAnalysisDataScope, options)

#### Return Value

[PropertyObject](../tsapiref/propertyobject.html)

#### Purpose

Use this method in an analysis module to store and retrieve data to share among multiple calls to analysis modules.

#### Remarks

The TestStand Sequence Analyzer creates empty
 
 [PropertyObject](../tsapiref/propertyobject.html)
 containers for each rule to store data that analysis modules generate during analysis. Analysis modules use this method to obtain references to these containers. An analysis module can use the container to store and retrieve data associated with the rule, such as cumulative item counts.

#### Parameters

RuleId
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the unique rule ID of the rule.

RuleAnalysisDataScope
 As
 [RuleAnalysisDataScope](ruleanalysisdatascope.html)

[In] Pass the scope of the data to access. Use file scope to access data associated with the file currently under analysis. The sequence analyzer destroys the file data when it completes the analysis of the file and after it calls the analysis modules for the After file transition. Use global scope to access data associated with the current analysis session. The sequence analyzer destroys the global data when analysis of the project completes.

options
 As
 [Long](data-types-for-teststand-sequence-analyzer.html)

[In] Use one of the
 [GetRuleAnalysisDataOptions](getruleanalysisdataoptions.html)
 . You must use the
 GetRuleAnalysisDataOption_Lock
 option if the analysis module modifies the rule analysis data.

#### See Also

[GetRuleAnalysisDataOptions](getruleanalysisdataoptions.html)

[PropertyObject](../tsapiref/propertyobject.html)

[Relationships among AnalysisContext Transition, File, and Object Properties](relationships-among-analysiscontext-transitio.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-getruleconfiguration.html language=enus -->
## TOPIC 00107: AnalysisContext.GetRuleConfiguration

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-getruleconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-getruleconfiguration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.GetRuleConfiguration( RuleId) Return Value RuleConfiguration Purpose Use this method in an analysis module to obtain a rule configuration. A rule configuration contains the enabled state, severity, description, and other information for a specific rule. Remarks The analysis pr

### AnalysisContext.GetRuleConfiguration

#### Syntax

[AnalysisContext](analysiscontext.html).GetRuleConfiguration( RuleId)

#### Return Value

[RuleConfiguration](ruleconfiguration.html)

#### Purpose

Use this method in an analysis module to obtain a rule configuration. A rule configuration contains the enabled state, severity, description, and other information for a specific rule.

#### Remarks

The analysis project stores the rule configurations. Analysis modules must not modify rule configurations. Only rule configuration modules and the TestStand Sequence Analyzer should modify rule configurations.

To improve analysis performance, configure analysis modules to check the enabled state of the rule before performing checks or reporting messages for the rule.

This method returns
 NULL
 if the
 RuleId
 parameter is not a valid rule ID.

#### Parameters

RuleId
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the unique rule ID of the rule.

#### See Also

[RuleConfigurationContext.RuleConfiguration](ruleconfigurationcontext-ruleconfiguration.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-newmessage.html language=enus -->
## TOPIC 00108: AnalysisContext.NewMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-newmessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-newmessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.NewMessage( RuleId, messageText, locationObject) Return Value AnalysisMessage Purpose Use this method in an analysis module to create a new analysis message to report during analysis. Remarks After you create the message you can modify the message properties. You must call the

### AnalysisContext.NewMessage

#### Syntax

[AnalysisContext](analysiscontext.html).NewMessage( RuleId, messageText, locationObject)

#### Return Value

[AnalysisMessage](analysismessage.html)

#### Purpose

Use this method in an analysis module to create a new analysis message to report during analysis.

#### Remarks

After you create the message you can modify the message properties. You must call the
 [AnalysisContext.ReportMessage](analysiscontext-reportmessage.html)
 method after calling this method to report the message to the TestStand Sequence Analyzer, which adds the message to the analyzer project.

#### Parameters

RuleId
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the unique rule ID of the rule to which the message corresponds.

messageText
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the message text. The sequence analyzer displays this text on the
 [Analyzer Messages](../tsref/analyzer-messages-tab-analysis-results-pane.html)
 tab of the
 [Analysis Results](../tsref/analysis-results-pane.html)
 pane.

locationObject
 As
 
 [PropertyObject](../tsapiref/propertyobject.html)

[In] Pass the object associated with the message. The sequence analyzer uses this object to initialize the
 [AnalysisMessage.Locations](analysismessage-locations.html)
 property, which specifies the location that the sequence analyzer uses when you go to the location associated with a message. Pass
 NULL
 if no specific object exists.

#### See Also

[AnalysisMessage.Locations](analysismessage-locations.html)

[Analysis Results](../tsref/analysis-results-pane.html)

[AnalysisContext.ReportMessage](analysiscontext-reportmessage.html)

[Analyzer Messages tab](../tsref/analyzer-messages-tab-analysis-results-pane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-object.html language=enus -->
## TOPIC 00109: AnalysisContext.Object

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-object.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-object.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.Object Data Type PropertyObject Purpose Use this property in an analysis module to access the object the TestStand Sequence Analyzer is currently analyzing. Remarks This property is NULL when the sequence analyzer calls an analysis module for certain analysis transitions . Ana

### AnalysisContext.Object

#### Syntax

[AnalysisContext](analysiscontext.html).Object

#### Data Type

[PropertyObject](../tsapiref/propertyobject.html)

#### Purpose

Use this property in an analysis module to access the object the TestStand Sequence Analyzer is currently analyzing.

#### Remarks

This property is
 NULL
 when the sequence analyzer calls an analysis module for certain
 
 [analysis transitions](relationships-among-analysiscontext-transitio.html)
 . Analysis modules must not hold a reference to the object this property returns because the sequence analyzer unloads each file from memory after analysis completes.

#### See Also

[AnalysisContext.Transition](analysiscontext-transition.html)

[AnalysisTransition](analysistransition.html)

[Relationships among AnalysisContext Transition, File, and Object Properties](relationships-among-analysiscontext-transitio.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-reportmessage.html language=enus -->
## TOPIC 00110: AnalysisContext.ReportMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-reportmessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-reportmessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.ReportMessage( message) Purpose Use this method in an analysis module to report and add an analysis message to the list of messages in the project. Remarks Use the AnalysisContext.NewMessage method to create a message. Do not call this method more than once for a message. Do n

### AnalysisContext.ReportMessage

#### Syntax

[AnalysisContext](analysiscontext.html).ReportMessage( message)

#### Purpose

Use this method in an analysis module to report and add an analysis message to the list of messages in the project.

#### Remarks

Use the
 [AnalysisContext.NewMessage](analysiscontext-newmessage.html)
 method to create a message. Do not call this method more than once for a message. Do not change message properties after calling this method. Because this method makes a copy of the message you pass to the method, all changes to the message after calling this method do not affect the reported message.

The TestStand Sequence Analyzer discards the message if you disable the rule that corresponds to the message.

#### Parameters

message
 As
 [AnalysisMessage](analysismessage.html)

[In] Pass the message to report.

#### See Also

[AnalysisContext.NewMessage](analysiscontext-newmessage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-stopanalysis.html language=enus -->
## TOPIC 00111: AnalysisContext.StopAnalysis

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-stopanalysis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-stopanalysis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.StopAnalysis Purpose Use this method in an analysis module to stop the current analysis session. After you call this method, the TestStand Sequence Analyzer calls analysis modules for the remaining transitions, closes all files, and stops analyzing.

### AnalysisContext.StopAnalysis

#### Syntax

[AnalysisContext](analysiscontext.html).StopAnalysis

#### Purpose

Use this method in an analysis module to stop the current analysis session. After you call this method, the TestStand Sequence Analyzer calls analysis modules for the remaining transitions, closes all files, and stops analyzing.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-stoprequested.html language=enus -->
## TOPIC 00112: AnalysisContext.StopRequested

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-stoprequested.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-stoprequested.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.StopRequested Data Type Boolean Purpose Use this property in an analysis module to determine whether the user or another analysis module has requested to stop the current analysis session. Remarks When the user stops analysis, the TestStand Sequence Analyzer stops calling anal

### AnalysisContext.StopRequested

#### Syntax

[AnalysisContext](analysiscontext.html).StopRequested

#### Data Type

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this property in an analysis module to determine whether the user or another analysis module has requested to stop the current analysis session.

#### Remarks

When the user stops analysis, the TestStand Sequence Analyzer stops calling analysis modules to analyze objects but continues to call analysis modules for the remaining transitions. You can choose not to report messages if analysis stops.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-transition.html language=enus -->
## TOPIC 00113: AnalysisContext.Transition

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-transition.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-transition.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.Transition Data Type AnalysisTransition Purpose Use this property in an analysis module to access the file that the TestStand Sequence Analyzer is currently analyzing. Remarks This property has the value AnalysisTransition_None when the sequence analyzer calls an analysis modu

### AnalysisContext.Transition

#### Syntax

[AnalysisContext](analysiscontext.html).Transition

#### Data Type

[AnalysisTransition](analysistransition.html)

#### Purpose

Use this property in an analysis module to access the file that the TestStand Sequence Analyzer is currently analyzing.

#### Remarks

This property has the value
 [AnalysisTransition_None](analysistransition.html)
 when the sequence analyzer calls an analysis module to analyze an object.

#### See Also

[AnalysisTransition](analysistransition.html)

[Relationships among AnalysisContext Transition, File, and Object Properties](relationships-among-analysiscontext-transitio.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext-utilities.html language=enus -->
## TOPIC 00114: AnalysisContext.Utilities

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext-utilities.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext-utilities.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisContext.Utilities Data Type AnalysisUtilities Purpose Use this property in an analysis module to access utility methods that help you implement a rule.

### AnalysisContext.Utilities

#### Syntax

[AnalysisContext](analysiscontext.html).Utilities

#### Data Type

[AnalysisUtilities](analysisutilities.html)

#### Purpose

Use this property in an analysis module to access utility methods that help you implement a rule.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysiscontext.html language=enus -->
## TOPIC 00115: AnalysisContext

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysiscontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysiscontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the AnalysisContext class in an analysis module to access information about the current object being analyzed or about the current analysis transition. The TestStand Sequence Analyzer passes an instance of this class as a parameter to the analysis module. Properties AnalysisId (Read Only) EditCo

### AnalysisContext

Use the AnalysisContext class in an analysis module to access information about the current object being analyzed or about the current analysis transition. The TestStand Sequence Analyzer passes an instance of this class as a parameter to the analysis module.

#### Properties

| AnalysisId (Read Only) |
| --- |
| EditContext (Read Only) |
| Engine (Read Only) |
| File (Read Only) |
| Object (Read Only) |
| StopRequested (Read Only) |
| Transition (Read Only) |
| Utilities (Read Only) |

#### Methods

| GetRuleAnalysisData |
| --- |
| GetRuleConfiguration |
| NewMessage |
| ReportMessage |
| StopAnalysis |

#### See Also

[Creating Analysis Modules](/csh?context=ts_tsref_sa_creating_analysis_modules)

Parent topic:

TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysismessage-locations.html language=enus -->
## TOPIC 00116: AnalysisMessage.Locations

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysismessage-locations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysismessage-locations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisMessage.Locations Data Type Locations Purpose Use this property in an analysis module to obtain the location associated with the message. You can call methods on this property to specify the location the TestStand Sequence Analyzer uses when you go to the location associated with a me

### AnalysisMessage.Locations

#### Syntax

[AnalysisMessage](analysismessage.html).Locations

#### Data Type

[Locations](../tsapiref/locations.html)

#### Purpose

Use this property in an analysis module to obtain the location associated with the message. You can call methods on this property to specify the location the TestStand Sequence Analyzer uses when you go to the location associated with a message.

#### Remarks

Do not set this property after calling the
 [AnalysisContext.ReportMessage](analysiscontext-reportmessage.html)
 method because the
 AnalysisContext.ReportMessage
 method makes a copy of the message you pass to the method. Changes to this property after calling the
 AnalysisContext.ReportMessage
 method do not affect the reported message.

The sequence analyzer recognizes only the first location this property contains.

#### See Also

[AnalysisContext.NewMessage](analysiscontext-newmessage.html)

[AnalysisContext.ReportMessage](analysiscontext-reportmessage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysismessage-ruleid.html language=enus -->
## TOPIC 00117: AnalysisMessage.RuleId

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysismessage-ruleid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysismessage-ruleid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisMessage.RuleId Data Type String Purpose Use this property in an analysis module to obtain or specify the unique rule ID associated with the message. Remarks Do not set this property after calling the AnalysisContext.ReportMessage method because the AnalysisContext.ReportMessage method

### AnalysisMessage.RuleId

#### Syntax

[AnalysisMessage](analysismessage.html).RuleId

#### Data Type

[String](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this property in an analysis module to obtain or specify the unique rule ID associated with the message.

#### Remarks

Do not set this property after calling the
 [AnalysisContext.ReportMessage](analysiscontext-reportmessage.html)
 method because the
 AnalysisContext.ReportMessage
 method makes a copy of the message you pass to the method. Changes to this property after calling the
 AnalysisContext.ReportMessage
 method do not affect the reported message.

#### See Also

[AnalysisContext.ReportMessage](analysiscontext-reportmessage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysismessage-text.html language=enus -->
## TOPIC 00118: AnalysisMessage.Text

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysismessage-text.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysismessage-text.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisMessage.Text Data Type String Purpose Use this property in an analysis module to obtain or specify the message text. Remarks Do not set this property after calling the AnalysisContext.ReportMessage method because the AnalysisContext.ReportMessage method makes a copy of the message you

### AnalysisMessage.Text

#### Syntax

[AnalysisMessage](analysismessage.html).Text

#### Data Type

[String](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this property in an analysis module to obtain or specify the message text.

#### Remarks

Do not set this property after calling the
 [AnalysisContext.ReportMessage](analysiscontext-reportmessage.html)
 method because the
 AnalysisContext.ReportMessage
 method makes a copy of the message you pass to the method. Changes to this property after calling the
 AnalysisContext.ReportMessage
 method do not affect the reported message.

#### See Also

[AnalysisContext.ReportMessage](analysiscontext-reportmessage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysismessage.html language=enus -->
## TOPIC 00119: AnalysisMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysismessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysismessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An object of the AnalysisMessage class represents a message an analysis module creates while performing an analysis. The message displays in the TestStand Sequence Editor or the stand-alone sequence analyzer application and is stored in a TestStand Sequence Analyzer project. Use the AnalysisContext.

### AnalysisMessage

An object of the
 AnalysisMessage
 class represents a message an analysis module creates while performing an analysis. The message displays in the TestStand Sequence Editor or the stand-alone sequence analyzer application and is stored in a TestStand Sequence Analyzer project. Use the
 [AnalysisContext.NewMessage](analysiscontext-newmessage.html)
 method in an analysis module to create a new instance of this class.

#### Properties

| Locations (Read Only) |
| --- |
| RuleId |
| Text |

#### See Also

[AnalysisContext.NewMessage](analysiscontext-newmessage.html)

[Creating Analysis Modules](/csh?context=ts_tsref_sa_creating_analysis_modules)

Parent topic:

TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysistransition.html language=enus -->
## TOPIC 00120: AnalysisTransition

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysistransition.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysistransition.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration with the AnalysisContext.Transition property to determine the current analysis transition of the TestStand Sequence Analyzer. AnalysisTransition_AfterCleanupStepGroup –(Value: 39) Indicates that the sequence analyzer finished analyzing the Cleanup step group in a sequence. Use t

### AnalysisTransition

Use this enumeration with the
 [AnalysisContext.Transition](analysiscontext-transition.html)
 property to determine the current
 
 [analysis transition](relationships-among-analysiscontext-transitio.html)
 of the TestStand Sequence Analyzer.

- AnalysisTransition_AfterCleanupStepGroup 
 –(Value: 39) Indicates that the sequence analyzer finished analyzing the Cleanup step group in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_AfterFileTypes 
 –(Value: 48) Indicates that the sequence analyzer finished analyzing the types defined in a TestStand file, including type palette files, sequence files, and workspace files. Use the
 AnalysisContext.File 
 property to obtain a reference to the file.
- AnalysisTransition_AfterMainStepGroup 
 –(Value: 37) Indicates that the sequence analyzer finished analyzing the Main step group in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_AfterSequence 
 –(Value: 41) Indicates that the sequence analyzer finished analyzing one sequence in a sequence file. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_AfterSequenceFile 
 –(Value: 43) Indicates that the sequence analyzer finished analyzing a sequence file. Use the
 AnalysisContext.File 
 property to obtain a reference to the sequence file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_AfterSequenceFileGlobals 
 –(Value: 24) Indicates that the sequence analyzer finished analyzing the global variables in a sequence file.
- AnalysisTransition_AfterSequenceLocals 
 –(Value: 29) Indicates that the sequence analyzer finished analyzing the local variables in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_AfterSequenceParameters 
 –(Value: 31) Indicates that the sequence analyzer finished analyzing the parameters in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_AfterSequences 
 –(Value: 42) Indicates that the sequence analyzer finished analyzing the sequences in a sequence file.
- AnalysisTransition_AfterSequenceVariables 
 –(Value: 32) Indicates that the sequence analyzer finished analyzing the variables in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_AfterSetupStepGroup 
 –(Value: 35) Indicates that the sequence analyzer finished analyzing the Setup step group in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_AfterStationGlobals 
 –(Value: 14) Indicates that the sequence analyzer finished analyzing the global variables in the station global variables file. Use the
 AnalysisContext.File 
 property to obtain a reference to the station global variables file.
- AnalysisTransition_AfterStationGlobalsFile 
 –(Value: 15) Indicates that the sequence analyzer finished analyzing the station global variables file. Use the
 AnalysisContext.File 
 property to obtain a reference to the station global variables file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_AfterStep 
 –(Value: 46) Indicates that the sequence analyzer finished analyzing a step. Use the
 AnalysisContext.Object 
 property to obtain a reference to the step.
- AnalysisTransition_AfterSteps 
 –(Value: 40) Indicates that the sequence analyzer finished analyzing the steps in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_AfterSystem 
 –(Value: 44) Indicates that the sequence analyzer finished analyzing all files.
- AnalysisTransition_AfterTemplates 
 –(Value: 18) Indicates that the sequence analyzer finished analyzing the templates in the templates file.
- AnalysisTransition_AfterTemplatesFile 
 –(Value: 19) Indicates that the sequence analyzer finished analyzing the templates file. The templates file contains the configuration settings for the Templates list on the
 Insertion Palette 
 . Use the
 AnalysisContext.File 
 property to obtain a reference to the templates file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_AfterTypePalette 
 –(Value: 4) Indicates that the sequence analyzer finished analyzing a specific type palette file. Use the
 AnalysisContext.File 
 property to obtain a reference to the type palette file that was analyzed. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_AfterTypePalettes 
 –(Value: 5) Indicates that the sequence analyzer finished analyzing the type palette files.
- AnalysisTransition_AfterUserGroups 
 –(Value: 10) Indicates that the sequence analyzer finished analyzing the user groups in the users file.
- AnalysisTransition_AfterUsers 
 –(Value: 8) Indicates that the sequence analyzer finished analyzing the users in the users file. Use the
 AnalysisContext.File 
 property to obtain a reference to the users file.
- AnalysisTransition_AfterUsersFile 
 –(Value: 11) Indicates that the sequence analyzer finished analyzing the users file. Use the
 AnalysisContext.File 
 property to obtain a reference to the users file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_AfterWorkspaceFile 
 –(Value: 21) Indicates that the sequence analyzer finished analyzing the workspace file. Use the
 AnalysisContext.File 
 property to obtain a reference to the workspace file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_BeforeCleanupStepGroup 
 –(Value: 38) Indicates that the sequence analyzer is preparing to analyze the Cleanup step group in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_BeforeFileTypes 
 –(Value: 47) Indicates that the sequence analyzer is preparing to analyze the types defined in a TestStand file, including type palette files, sequence files, and workspace files. Use the
 AnalysisContext.File 
 property to obtain a reference to the file.
- AnalysisTransition_BeforeMainStepGroup 
 –(Value: 36) Indicates that the sequence analyzer is preparing to analyze the Main step group in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_BeforeSequence 
 –(Value: 26) Indicates that the sequence analyzer is preparing to analyze one sequence in a sequence file. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_BeforeSequenceFile 
 –(Value: 22) Indicates that the sequence analyzer is preparing to analyze a sequence file. Use the
 AnalysisContext.File 
 property to obtain a reference to the sequence file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_BeforeSequenceFileGlobals 
 –(Value: 23) Indicates that the sequence analyzer is preparing to analyze the global variables in a sequence file.
- AnalysisTransition_BeforeSequenceLocals 
 –(Value: 28) Indicates that the sequence analyzer is preparing to analyze the local variables in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_BeforeSequenceParameters 
 –(Value: 30) Indicates that the sequence analyzer is preparing to analyze the parameters in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_BeforeSequences 
 –(Value: 25) Indicates that the sequence analyzer is preparing to analyze the sequences in a sequence file.
- AnalysisTransition_BeforeSequenceVariables 
 –(Value: 27) Indicates that the sequence analyzer is preparing to analyze the variables in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_BeforeSetupStepGroup 
 –(Value: 34) Indicates that the sequence analyzer is preparing to analyze the Setup step group in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_BeforeStationGlobals 
 –(Value: 13) Indicates that the sequence analyzer is preparing to analyze the global variables in the station global variables file.
- AnalysisTransition_BeforeStationGlobalsFile 
 –(Value: 12) Indicates that the sequence analyzer is preparing to analyze the station global variables file. Use the
 AnalysisContext.File 
 property to obtain a reference to the station global variables file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_BeforeStep 
 –(Value: 45) Indicates that the sequence analyzer is preparing to analyze a step. Use the
 AnalysisContext.Object 
 property to obtain a reference to the step.
- AnalysisTransition_BeforeSteps 
 –(Value: 33) Indicates that the sequence analyzer is preparing to analyze the steps in a sequence. Use the
 AnalysisContext.Object 
 property to obtain a reference to the sequence.
- AnalysisTransition_BeforeSystem 
 –(Value: 1) Indicates that the sequence analyzer is preparing to start analyzing.
- AnalysisTransition_BeforeTemplates 
 –(Value: 17) Indicates that the sequence analyzer is preparing to analyze the templates in the templates file.
- AnalysisTransition_BeforeTemplatesFile 
 –(Value: 16) Indicates that the sequence analyzer is preparing to analyze the templates file. The templates file contains the configuration settings for the Templates list. Use the
 AnalysisContext.File 
 property to obtain a reference to the templates file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_BeforeTypePalette 
 –(Value: 3) Indicates that the sequence analyzer is preparing to analyze a specific type palette file. Use the
 AnalysisContext.File 
 property to obtain a reference to the type palette file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_BeforeTypePalettes 
 –(Value: 2) Indicates that the sequence analyzer is preparing to analyze type palette files.
- AnalysisTransition_BeforeUserGroups 
 –(Value: 9) Indicates that the sequence analyzer is preparing to analyze the user groups in the users file.
- AnalysisTransition_BeforeUsers 
 –(Value: 7) Indicates that the sequence analyzer is preparing to analyze the users in the users file.
- AnalysisTransition_BeforeUsersFile 
 –(Value: 6) Indicates that the sequence analyzer is preparing to analyze the users file. Use the
 AnalysisContext.File 
 property to obtain a reference to the users file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_BeforeWorkspaceFile 
 –(Value: 20) Indicates that the sequence analyzer is preparing to analyze the workspace file. Use the
 AnalysisContext.File 
 property to obtain a reference to the workspace file. The
 AnalysisContext.Object 
 property also contains a reference to the file.
- AnalysisTransition_None 
 –(Value: 0) Indicates that the sequence analyzer is not in a transition.

#### See Also

[AnalysisContext.File](analysiscontext-file.html)

[AnalysisContext.Object](analysiscontext-object.html)

[AnalysisContext.Transition](analysiscontext-transition.html)

[Insertion Palette](../tsref/insertion-palette-pane.html)

[Relationships among AnalysisContext Transition, File, and Object Properties](relationships-among-analysiscontext-transitio.html)

Parent topic:

Sequence Analyzer API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysisutilities-automaticpropertycheckingen.html language=enus -->
## TOPIC 00121: AnalysisUtilities.AutomaticPropertyCheckingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysisutilities-automaticpropertycheckingen.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysisutilities-automaticpropertycheckingen.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisUtilities.AutomaticPropertyCheckingEnabled Data Type Boolean Purpose Set this property to False in an analysis module to prevent the sequence analyzer built-in analysis modules from performing automatic checks on step properties that are instances of the Path and Expression data types

### AnalysisUtilities.AutomaticPropertyCheckingEnabled

#### Syntax

[AnalysisUtilities](analysisutilities.html).AutomaticPropertyCheckingEnabled

#### Data Type

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Set this property to
 False
 in an analysis module to prevent the sequence analyzer built-in analysis modules from performing automatic checks on step properties that are instances of the Path and Expression data types. An analysis module typically sets this property to
 False
 when analyzing a step instance for a custom step type. The analysis module must perform all expression and path property checking for the step when you disable this property. The analysis module can perform more specific expression checking than the built-in analysis modules, including type validation, and can selectively analyze properties based on other property values.

The sequence analyzer automatically resets this property to
 True
 before analyzing each step. The sequence analyzer always checks all built-in expression and path properties, such as pre-expressions and preconditions, even if an analysis module sets this property to
 False
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysisutilities-validatecodemoduleuptodate.html language=enus -->
## TOPIC 00122: AnalysisUtilities.ValidateCodeModuleUpToDate

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysisutilities-validatecodemoduleuptodate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysisutilities-validatecodemoduleuptodate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisUtilities.ValidateCodeModuleUpToDate( codeModulePath, sourcePath, baseLocation, apiLocation, reserved) Return Value Boolean Purpose Use this method in an analysis module to verify that a source file has not been modified more recently than the code module. Parameters codeModulePath As

### AnalysisUtilities.ValidateCodeModuleUpToDate

#### Syntax

[AnalysisUtilities](analysisutilities.html).ValidateCodeModuleUpToDate( codeModulePath, sourcePath, baseLocation, apiLocation, reserved)

#### Return Value

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this method in an analysis module to verify that a source file has not been modified more recently than the code module.

#### Parameters

codeModulePath
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the path of the code module that needs to be validated.

sourcePath
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the path of the source file containing the code module.

baseLocation
 As
 
 [PropertyObject](../tsapiref/propertyobject.html)

[In] Pass the base object to use with the
 apiLocation
 parameter as the location associated with any analysis messages this method reports.

apiLocation
 As
 
 [APILocations](../tsapiref/apilocations.html)

[In] Pass the
 
 [APILocations](../tsapiref/apilocations.html)
 enumeration to use as the location associated with any analysis messages this method reports. To use the
 baseLocation
 as the location, pass
 APILocation_None
 .

reserved
 As
 [Long](data-types-for-teststand-sequence-analyzer.html)

[In] Not used.

#### See Also

[APILocations](../tsapiref/apilocations.html)

[AnalysisUtilities.AutomaticPropertyCheckingEnabled](analysisutilities-automaticpropertycheckingen.html)

[ValidateExpressionOptions](validateexpressionoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysisutilities-validateexpression.html language=enus -->
## TOPIC 00123: AnalysisUtilities.ValidateExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysisutilities-validateexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysisutilities-validateexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisUtilities.ValidateExpression( expression, baseLocation, apiLocation, validTypes, evaluationOptions, additionalConstants, evaluationFlags) Return Value Boolean Purpose Use this method in an analysis module to validate an expression. An analysis module can call this method to perform ex

### AnalysisUtilities.ValidateExpression

#### Syntax

[AnalysisUtilities](analysisutilities.html).ValidateExpression( expression, baseLocation, apiLocation, validTypes, evaluationOptions, additionalConstants, evaluationFlags)

#### Return Value

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this method in an analysis module to validate an expression. An analysis module can call this method to perform expression validation on any property that is not an instance of the Expression data type or to perform custom expression validation beyond syntax errors, such as type checking.

If the analysis module calls this method on expression properties within a step, the analysis module must set the
 [AnalysisUtilities.AutomaticPropertyCheckingEnabled](analysisutilities-automaticpropertycheckingen.html)
 property to
 False
 to ensure that the sequence analyzer does not report duplicate messages, and the analysis module must perform all path and expression property checking for the step.

If the rules are enabled, this method reports analysis messages for the
 NI_ExpressionEvaluationError
 ,
 NI_DynamicPropertyDoesNotExist
 , and
 NI_EscapeSequenceValid
 rules. This method also finds variables in the expression to determine which variables are used for the
 NI_UnusedVariables
 rule.

If you set the
 AnalysisUtilities.AutomaticPropertyCheckingEnabled
 property to
 True
 , the built-in analysis modules call this method with the
 evaluationFlags
 parameter set to
 [ValidateExpressionOption_NoOptions](validateexpressionoptions.html)
 for all properties of type Expression.

#### Parameters

expression
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the expression to validate.

baseLocation
 As
 
 [PropertyObject](../tsapiref/propertyobject.html)

[In] Pass the base object to use with the
 apiLocation
 parameter as the location associated with any analysis messages this method reports.

apiLocation
 As
 
 [APILocations](../tsapiref/apilocations.html)

[In] Pass the
 
 [APILocations](../tsapiref/apilocations.html)
 enumeration to use as the location associated with any analysis messages this method reports. To use the
 baseLocation
 as the location, pass
 APILocation_None
 .

validTypes
 As
 
 [EvaluationTypes](../tsapiref/evaluationtypes.html)

[In] Pass the type or types to which you expect the expression to evaluate.

evaluationOptions
 As
 [Long](data-types-for-teststand-sequence-analyzer.html)

[In] Pass any combination of the
 
 [EvaluationOptions](../tsapiref/evaluationoptions.html)
 constants. You do not need to pass the
 EvalOption_DoNotAlterValues
 constant because this method never changes values.

additionalConstants
 As
 [Object Array](data-types-for-teststand-sequence-analyzer.html)

[In] Pass additional variables the expression might contain that are not part of the context. This parameter is useful if the expression contains a constant from an enumeration, such as a parameter value of a module call when the parameter type is an enumeration. You can pass
 NULL
 for this parameter if no additional constants you want to use exist when evaluating the expression.

evaluationFlags
 As
 [Long](data-types-for-teststand-sequence-analyzer.html)

[In] Pass a combination of the
 [ValidateExpressionOptions](validateexpressionoptions.html)
 constants.

#### See Also

[ActiveXParameter.GetEnumValues](../tsapiref/activexparameter-getenumvalues.html)

ActiveXParameter.Valid
 [EvaluationTypes](../tsapiref/evaluationtypes.html)

[AnalysisUtilities.AutomaticPropertyCheckingEnabled](analysisutilities-automaticpropertycheckingen.html)

[APILocations](../tsapiref/apilocations.html)

[CommonCParameter.GetEnumValues](../tsapiref/commoncparameter-getenumvalues.html)

CommonCParameter.Valid
 [EvaluationTypes](../tsapiref/evaluationtypes.html)

[DotNetParameter.GetEnumValues](../tsapiref/dotnetparameter-getenumvalues.html)

DotNetParameter.Valid
 [EvaluationTypes](../tsapiref/evaluationtypes.html)

[EvaluationOptions](../tsapiref/evaluationoptions.html)

[LabVIEWParameter.GetEnumValues](../tsapiref/labviewparameter-getenumvalues.html)

LabVIEWParameter.Valid
 [EvaluationTypes](../tsapiref/evaluationtypes.html)

[LabVIEWParameterElement.GetEnumValues](../tsapiref/labviewparameterelement-getenumvalues.html)

LabVIEWParameterElement.Valid
 [EvaluationTypes](../tsapiref/evaluationtypes.html)

SequenceCallParameter.Valid
 [EvaluationTypes](../tsapiref/evaluationtypes.html)

[ValidateExpressionOptions](validateexpressionoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysisutilities-validatepath.html language=enus -->
## TOPIC 00124: AnalysisUtilities.ValidatePath

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysisutilities-validatepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysisutilities-validatepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisUtilities.ValidatePath( Path, baseLocation, apiLocation, validationOptions) Return Value Boolean Purpose Use this method in an analysis module to validate a path. An analysis module can call this method to perform path validation on any property that is not an instance of the Path dat

### AnalysisUtilities.ValidatePath

#### Syntax

[AnalysisUtilities](analysisutilities.html).ValidatePath( Path, baseLocation, apiLocation, validationOptions)

#### Return Value

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this method in an analysis module to validate a path. An analysis module can call this method to perform path validation on any property that is not an instance of the Path data type or to validate a path with a different validation option than the built-in analysis modules.

If the analysis module calls this method on path properties within a step, the analysis module must set the
 [AnalysisUtilities.AutomaticPropertyCheckingEnabled](analysisutilities-automaticpropertycheckingen.html)
 property to
 False
 to ensure that the sequence analyzer does not report duplicate messages, and the analysis module must perform all path and expression property checking for the step

If the rules are enabled, this method reports analysis messages for the
 NI_ValidPath
 rule, the
 NI_FileNotFoundWarning
 rule, and the
 NI_FileNotFound
 rule.

If you set the
 AnalysisUtilities.AutomaticPropertyCheckingEnabled
 property to
 True
 , the built-in analysis modules call this method with the
 validationOptions
 parameter set to
 [ValidatePathOption_DoNotCheckIfExists](validateexpressionoptions.html)
 for all properties that use the Path type.

For path expression properties, analysis modules must instead call the
 [AnalysisUtilities.ValidateExpression](analysisutilities-validateexpression.html)
 method and pass
 ValidateExpressionOption_Path
 for the
 evaluationFlags
 parameter.

#### Parameters

Path
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the path to validate. This path can be a relative or absolute path.

baseLocation
 As
 
 [PropertyObject](../tsapiref/propertyobject.html)

[In] Pass the base object to use with the
 apiLocation
 parameter as the location associated with any analysis messages this method reports.

apiLocation
 As
 
 [APILocations](../tsapiref/apilocations.html)

[In] Pass the
 
 [APILocations](../tsapiref/apilocations.html)
 enumeration to use as the location associated with any analysis messages this method reports. To use the
 baseLocation
 as the location, pass
 APILocation_None
 .

validationOptions
 As
 [Long](data-types-for-teststand-sequence-analyzer.html)

[In] Pass any of the
 [ValidatePathOptions](validatepathoptions.html)
 constants.

#### See Also

[AnalysisUtilities.AutomaticPropertyCheckingEnabled](analysisutilities-automaticpropertycheckingen.html)

[AnalysisUtilities.ValidateExpression](analysisutilities-validateexpression.html)

[APILocations](../tsapiref/apilocations.html)

[ValidatePathOptions](validatepathoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysisutilities-validateremotehost.html language=enus -->
## TOPIC 00125: AnalysisUtilities.ValidateRemoteHost

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysisutilities-validateremotehost.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysisutilities-validateremotehost.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax AnalysisUtilities.ValidateRemoteHost( remoteHost, baseLocation, apiLocation) Return Value Boolean Purpose Use this method in an analysis module to validate whether a remote host can be located on the network. This method reports analysis messages for the NI_RemoteHostExists rule if the rule i

### AnalysisUtilities.ValidateRemoteHost

#### Syntax

[AnalysisUtilities](analysisutilities.html).ValidateRemoteHost( remoteHost, baseLocation, apiLocation)

#### Return Value

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this method in an analysis module to validate whether a remote host can be located on the network. This method reports analysis messages for the
 NI_RemoteHostExists
 rule if the rule is enabled.

#### Parameters

remoteHost
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the name of the remote host to validate.

baseLocation
 As
 
 [PropertyObject](../tsapiref/propertyobject.html)

[In] Pass the base object to use with the
 apiLocation
 parameter as the location associated with any analysis messages this method reports.

apiLocation
 As
 
 [APILocations](../tsapiref/apilocations.html)

[In] Pass the
 
 [APILocations](../tsapiref/apilocations.html)
 enumeration to use as the location associated with any analysis messages this method reports. To use the
 baseLocation
 as the location, pass
 APILocation_None
 .

#### See Also

[APILocations](../tsapiref/apilocations.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/analysisutilities.html language=enus -->
## TOPIC 00126: AnalysisUtilities

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/analysisutilities.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/analysisutilities.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the objects of the AnalysisUtilities class in an analysis module to perform common analysis functions. Use the AnalysisContext.Utilities property to obtain an instance of this class. Property AutomaticPropertyCheckingEnabled Methods ValidateExpression ValidatePath ValidateRemoteHost ValidateCode

### AnalysisUtilities

Use the objects of the
 AnalysisUtilities
 class in an analysis module to perform common analysis functions. Use the
 [AnalysisContext.Utilities](analysiscontext-utilities.html)
 property to obtain an instance of this class.

#### Property

| AutomaticPropertyCheckingEnabled |
| --- |

#### Methods

| ValidateExpression |
| --- |
| ValidatePath |
| ValidateRemoteHost |
| ValidateCodeModuleUpToDate |

#### See Also

[AnalysisContext.Utilities](analysiscontext-utilities.html)

[Creating Analysis Modules](/csh?context=ts_tsref_sa_creating_analysis_modules)

Parent topic:

TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/color.html language=enus -->
## TOPIC 00127: Color

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/color.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/color.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Color values are typically four-byte integers and commonly use little-endian and big-endian format. Microsoft Windows and ActiveX use the little-endian format, which stores red, green, and blue color components in the 0x00BBGGRR byte positions. LabVIEW and LabWindows/CVI use the big-endian format, w

### Color

Color values are typically four-byte integers and commonly use little-endian and big-endian format. Microsoft Windows and ActiveX use the little-endian format, which stores red, green, and blue color components in the 0x00BBGGRR byte positions. LabVIEW and LabWindows/CVI use the big-endian format, which stores the color components in the 0x00RRGGBB byte positions.

If you are specifying a color value in an expression, you can use a predefined little-endian color constant, such as tsRed or tsDarkBlue. Refer to
 Constants»Color
 on the
 [Operators/Functions tab](../tsref/operators-functions-tab-expression-browser-di.html)
 of the
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box for the list of available expression color constants. Use the
 ConvertColor
 expression function to convert the two color value formats.

Some Windows and ActiveX functions support specifying a system color using the 0x800000xx byte format, where
 xx
 is a valid Win32
 GetSysColor
 index. The possible values are listed below.

- 0x00bbggrr—Where
 bb 
 specifies the intensity of the color blue,
 gg 
 specifies the intensity of the color green, and
 rr 
 specifies the intensity of the color red.
- 0x800000xx—Where
 xx 
 is a valid Win32
 GetSysColor 
 index. The possible values are listed below.
 Constant
 ValueCOLOR_SCROLLBAR
 0
 COLOR_BACKGROUND
 1
 COLOR_ACTIVECAPTION
 2
 COLOR_INACTIVECAPTION
 3
 COLOR_MENU
 4
 COLOR_WINDOW
 5
 COLOR_WINDOWFRAME
 6
 COLOR_MENUTEXT
 7
 COLOR_WINDOWTEXT
 8
 COLOR_CAPTIONTEXT
 9
 COLOR_ACTIVEBORDER
 10
 COLOR_INACTIVEBORDER
 11
 COLOR_APPWORKSPACE
 12
 COLOR_HIGHLIGHT
 13
 COLOR_HIGHLIGHTEXT
 14
 COLOR_BTNFACE
 15
 COLOR_BTNSHADOW
 16
 COLOR_GRAYTEXT
 17
 COLOR_BTNTEXT
 18
 COLOR_INACTIVECAPTIONTEXT
 19
 COLOR_BTNHIGHLIGHT
 20
 COLOR_3DDKSHADOW
 21
 COLOR_3DLIGHT
 22
 COLOR_INFOTEXT
 23
 COLOR_INFOBK
 24
 COLOR_HOTLIGHT
 26
 COLOR_GRADIENTACTIVECAPTION
 27
 COLOR_GRADIENTINACTIVECAPTION
 28
 COLOR_MENUHILIGHT
 29
 COLOR_MENUBAR
 30

Parent topic:

Data Types for TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/data-types-for-teststand-sequence-analyzer.html language=enus -->
## TOPIC 00128: Data Types for TestStand Sequence Analyzer

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/data-types-for-teststand-sequence-analyzer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/data-types-for-teststand-sequence-analyzer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Type OLE Automation Type Description Boolean VARIANT_BOOL Has the value True ( -1 ) or False ( 0 ). Byte Array SAFEARRAY(unsigned char) An array of bytes. Color OLE_COLOR A color. Many containers treat colors as 32-bit integers. Date DATE DATE is a variant time that is stored as an 8-byte real value

### Data Types for TestStand Sequence Analyzer

| Type | OLE Automation Type | Description |
| --- | --- | --- |
| Boolean | VARIANT_BOOL | Has the value True ( -1 ) or False ( 0 ). |
| Byte Array | SAFEARRAY(unsigned char) | An array of bytes. |
| Color | OLE_COLOR | A color. Many containers treat colors as 32-bit integers. |
| Date | DATE | DATE is a variant time that is stored as an 8-byte real value (double) and represents a date between January 1, 100 and December 31, 9999, inclusive. The value 0 represents December 30, 1899. Adding 1 to the value increments the date by a day. The fractional part of the value represents the time of day. Negative numbers represent the dates before December 30, 1899. LabWindows/CVI users can use the VariantTimeToSystemTime Microsoft Windows Software Development Kit (SDK) function to convert the variant date to a system time value and then use the GetDateFormat and GetTimeFormat Windows SDK functions to generate display strings. LabVIEW automatically converts the DATE data type to a timestamp. |
| Double | double | 64-bit floating point number. |
| Float | float | 32-bit floating point number. |
| Font | IFontDisp | An Object Linking and Embedding (OLE) Automation Interface to a font . |
| Integer | short | 16-bit signed integer. |
| IUnknown | IUnknown | A generic OLE interface. |
| Long | Long | 32-bit signed integer. |
| long | OLE_YPOS_PIXELS | Position on the Y-axis in pixels. |
| Long | LCID | A locale identifier. |
| long | OLE_XPOS_PIXELS | Position on the X-axis in pixels. |
| Long Array | SAFEARRAY(long) | An array of longs. |
| long long | LONGLONG | 64-bit signed integer. |
| Object | IDispatch | A generic OLE Automation interface. |
| Object Array | SAFEARRAY | An array of objects. |
| Picture | IPicture | An OLE Automation Interface to a Picture object or image. |
| Picture | IPictureDisp | An OLE Automation Interface to a Picture object or image. |
| String | BSTR | A string. |
| String Array | SAFEARRAY(BSTR) | An array of strings. |
| unsigned long long | ULONGLONG | 64-bit unsigned integer. |
| Variant | VARIANT | A variant. |
| VARTYPE | VARTYPE | An enumeration type used to describe a data type of a VARIANT or safearray value. Refer to VARTYPE for more information about VARTYPE enumeration values. |

Parent topic:

NI TestStand Sequence Analyzer Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/font.html language=enus -->
## TOPIC 00129: Font

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Font object specifies a wrapper around a Microsoft Windows font. Microsoft defines this standard Font object implementation in the Object Linking and Embedding (OLE) Automation version 2.0 type library file, stdole2.tlb . Refer to Microsoft documentation for more information about this interface.

### Font

A Font object specifies a wrapper around a Microsoft Windows font. Microsoft defines this standard Font object implementation in the Object Linking and Embedding (OLE) Automation version 2.0 type library file,
 stdole2.tlb
 . Refer to Microsoft documentation for more information about this interface.

The Font interface specifies the following properties and methods:

#### Properties

- Name 
 —Name for the font.
- Size 
 —Point size for the font.
- Bold 
 —Bold property for the font.
- Italic 
 —Italic property for the font.
- Underline 
 —Underline property for the font.
- Strikethrough 
 —Strikethrough property for the font.
- Weight 
 —Weight (bold) for the font.
- Charset 
 —Character set of the font.
- hFont 
 —Returns a Windows HFONT handle for the font this Font object describes.

#### Methods

- Clone 
 —Creates a duplicate Font object with a state identical to the current font.
- IsEqual 
 —Compares this Font object to another for equality.
- SetRatio 
 —Converts the scaling factor for this font between logical units and HIMETRIC units, which the point size in the Size property specifies.
- QueryTextMetrics 
 —Fills a TEXTMETRIC structure describing the font.
- AddRefHfont 
 —Notifies the Font object that the previously realized font hFont identified remains valid until the ReleaseHfont method is called or the Font object itself is released.
- ReleaseHfont 
 —Notifies the Font object that the caller that previously locked this font in the cache with AddRefHfont no longer requires the lock.
- SetHdc 
 —Provides a device context handle to the font that describes the logical mapping mode.

LabVIEW

The LabVIEW development environment automatically recognizes Font ActiveX references. Use the Invoke Node and Property Node VIs to access the methods and properties of a Font ActiveX reference.

Note

LabWindows/CVI

LabWindows/CVI creates and accesses ActiveX objects using functions in a LabWindows/CVI-generated driver. You must create a driver for the OLE Automation ActiveX server using the ActiveX Controller Wizard. Select
 Tools»Create ActiveX Controller
 to launch the wizard. Select
 OLE Automation
 in the ActiveX Server list control and proceed to build the driver. Use the functions for the Font class to access the methods and properties.

Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can access Font objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

Imports stdole.StdFontClass

The IFontDisp class methods and properties are available in the Microsoft Visual Studio object browser and are accessible from the Visual Basic .NET source code.

C#

In C#, you can access Font objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

using stdole.StdFontClass;

The IFontDisp class methods and properties are available in the Visual Studio object browser and are accessible from the C# source code.

Microsoft Visual C++/#import

In C++, you can access Font objects by adding the include file
 ocidl.h
 and using the CComPtr template to manage IFontDisp COM interface pointers.

Parent topic:

Data Types for TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/getruleanalysisdataoptions.html language=enus -->
## TOPIC 00130: GetRuleAnalysisDataOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/getruleanalysisdataoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/getruleanalysisdataoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration with the AnalysisContext.GetRuleAnalysisData method. GetRuleAnalysisDataOption_Lock –(Value: 0x1) Locks the data and prevents other threads from accessing the data. You must use this option if you change any of the rule analysis data. The TestStand Sequence Analyzer unlocks the

### GetRuleAnalysisDataOptions

Use this enumeration with the
 [AnalysisContext.GetRuleAnalysisData](analysiscontext-getruleanalysisdata.html)
 method.

- GetRuleAnalysisDataOption_Lock 
 –(Value: 0x1) Locks the data and prevents other threads from accessing the data. You must use this option if you change any of the rule analysis data. The TestStand Sequence Analyzer unlocks the data after the call to the analysis module completes.
- GetRuleAnalysisDataOption_NoOptions 
 –(Value: 0x0) No options.

#### See Also

[AnalysisContext.GetRuleAnalysisData](analysiscontext-getruleanalysisdata.html)

Parent topic:

Sequence Analyzer API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/methods.html language=enus -->
## TOPIC 00131: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

AnalysisContext

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/methods_2.html language=enus -->
## TOPIC 00132: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/methods_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/methods_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

AnalysisUtilities

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/methods_3.html language=enus -->
## TOPIC 00133: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/methods_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/methods_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

RuleSettingValues

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ni-teststand-sequence-analyzer-reference-help.html language=enus -->
## TOPIC 00134: NI TestStand Sequence Analyzer Reference Help

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ni-teststand-sequence-analyzer-reference-help.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ni-teststand-sequence-analyzer-reference-help.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This help file contains detailed information about the properties, methods, constants, and enumerations of the TestStand Sequence Analyzer API. Refer to the NI TestStand Environment Reference Help for information about the sequence analyzer window , panes , and dialog boxes and the stand-alone TestS

### NI TestStand Sequence Analyzer Reference Help

TestStand Sequence Analyzer

NI TestStand Environment Reference Help

window

panes

stand-alone TestStand Sequence Analyzer application

Note

<TestStand>

TSHelp.chm

To navigate this help file, use the
 Contents
 ,
 Index
 , and
 Search
 tabs to the left of this window.

Refer to the
 [National Instruments website](http://digital.ni.com/express.nsf/bycode/feedback)
 to comment on National Instruments documentation.

Copyright © National Instruments Corporation. All rights reserved.

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/picture.html language=enus -->
## TOPIC 00135: Picture

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/picture.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/picture.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Picture object specifies an image. Microsoft defines this standard Picture object implementation in the Object Linking and Embedding (OLE) Automation Version 2.0 type library file, stdole2.tlb . Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles. Refer to Micr

### Picture

A Picture object specifies an image. Microsoft defines this standard Picture object implementation in the Object Linking and Embedding (OLE) Automation Version 2.0 type library file,
 stdole2.tlb
 . Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles. Refer to Microsoft documentation for more information about this interface.

The Picture interface specifies the following properties and methods:

#### Properties

- Handle (Read Only) 
 —Returns the Microsoft Windows graphics device interface (GDI) handle of the image managed within the Picture object.
- Attributes (Read Only) 
 —Returns the attributes of the image.
- CurDC 
 —Specifies the current device context into which this image is selected.
- Height (Read Only) 
 —Returns the current height of the image in the Picture object.
- Hpal 
 —Specifies the current palette the Picture object uses.
- Type (Read Only) 
 —Returns the current type of the image.
- Width (Read Only) 
 —Returns the current width of the image in the Picture object.
- KeepOriginalFormat 
 —Specifies whether the image maintains the original format.

#### Methods

- Render 
 —Draws the specified portion of the image onto the specified device context, positioned at the specified location.
- SelectPicture 
 —Selects a bitmap image into a given device context, returning the device context in which the image was previously selected as well as the GDI handle of the image.
- PictureChanged 
 —Notifies the Picture object that its image resource changed.
- SaveAsFile 
 —Saves the image data into a stream in the same format as it would save itself into a file.

LabVIEW

The LabVIEW development environment automatically recognizes Picture ActiveX references. Use the Invoke Node and Property Node VIs to access the methods and properties of a Picture ActiveX reference.

Note

LabWindows/CVI

LabWindows/CVI creates and accesses ActiveX objects using functions in a LabWindows/CVI-generated driver. You must create a driver for the OLE Automation ActiveX server using the ActiveX Controller Wizard. Select
 Tools»Create ActiveX Controller
 to launch the wizard, select
 OLE Automation
 in the ActiveX Server list control, and proceed to build the driver. Use the functions for the Picture class to access the methods and properties.

Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can access Picture objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

Imports stdole.StdPictureClass

The IPictureDisp class and its methods and properties are available in the Microsoft Visual Studio object browser and are accessible from the Visual Basic .NET source code.

C#

In C#, you can access Picture objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

using stdole.StdPictureClass;

The IPictureDisp class and its methods and properties are available in the Visual Studio object browser and are accessible from the C# source code.

Microsoft Visual C++/#import

In C++, you can access Picture objects by adding the include file
 ocidl.h
 and using the CComPtr template to manage IPictureDisp COM interface pointers.

Parent topic:

Data Types for TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/properties.html language=enus -->
## TOPIC 00136: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

AnalysisContext

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/properties_2.html language=enus -->
## TOPIC 00137: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/properties_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/properties_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

AnalysisMessage

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/properties_3.html language=enus -->
## TOPIC 00138: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/properties_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/properties_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

AnalysisUtilities

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/properties_4.html language=enus -->
## TOPIC 00139: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/properties_4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/properties_4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

RuleConfiguration

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/properties_5.html language=enus -->
## TOPIC 00140: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/properties_5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/properties_5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

RuleConfigurationContext

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/relationships-among-analysiscontext-transitio.html language=enus -->
## TOPIC 00141: Relationships among AnalysisContext Transition, File, and Object Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/relationships-among-analysiscontext-transitio.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/relationships-among-analysiscontext-transitio.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows the relationships among the AnalysisContext.Transition , AnalysisContext.File , and AnalysisContext.Object properties. Each analysis transition constant name in the AnalysisTransition enumeration (except AnalysisTransition_None ) is of the form AnalysisTransition_BeforeAnal

### Relationships among AnalysisContext Transition, File, and Object Properties

The following table shows the relationships among the
 [AnalysisContext.Transition](analysiscontext-transition.html)
 ,
 [AnalysisContext.File](analysiscontext-file.html)
 , and
 [AnalysisContext.Object](analysiscontext-object.html)
 properties. Each analysis transition constant name in the
 [AnalysisTransition](analysistransition.html)
 enumeration (except
 AnalysisTransition_None
 ) is of the form
 AnalysisTransition_BeforeAnalysisGroup
 or
 AnalysisTransition_AfterAnalysisGroup
 , where AnalysisGroup is the name of the group of objects that are about to be analyzed or have just been analyzed.

| Transition Property(AnalysisGroup) | File Property | Object Property |
| --- | --- | --- |
| CleanupStepGroup | Sequence file | Sequence |
| FileTypes | TestStand file(workspace file, type palette file,users file, station globals file,templates file, or sequence file) | NULL |
| MainStepGroup | Sequence file | Sequence |
| Sequence | Sequence file | Sequence |
| SequenceFile | Sequence file | Sequence file |
| SequenceFileGlobals | Sequence file | NULL |
| SequenceLocals | Sequence file | Sequence |
| SequenceParameters | Sequence file | Sequence |
| Sequences | Sequence file | NULL |
| SequenceVariables | Sequence file | Sequence |
| SetupStepGroup | Sequence file | Sequence |
| StationGlobals | Station globals file | NULL |
| StationGlobalsFile | Station globals file | Station globals file |
| Step | Sequence file | Step |
| Steps | Sequence file | Sequence |
| System | NULL | NULL |
| Templates | Templates file | NULL |
| TemplatesFile | Templates file | Templates file |
| TypePalette | Type palette file | Type palette file |
| TypePalettes | Type palette file | NULL |
| UserGroups | Users file | NULL |
| Users | Users file | NULL |
| UsersFile | Users file | Users file |
| WorkspaceFile | Workspace file | Workspace file |

Parent topic:

Sequence Analyzer API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleanalysisdatascope.html language=enus -->
## TOPIC 00142: RuleAnalysisDataScope

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleanalysisdatascope.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleanalysisdatascope.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration with the AnalysisContext.GetRuleAnalysisData method. RuleAnalysisDataScope_File –(Value: 1) Specifies the rule analysis data that is specific to the file being analyzed. The TestStand Sequence Analyzer creates the file data the first time you call the AnalysisContext.GetRuleAnal

### RuleAnalysisDataScope

Use this enumeration with the
 [AnalysisContext.GetRuleAnalysisData](analysiscontext-getruleanalysisdata.html)
 method.

- RuleAnalysisDataScope_File 
 –(Value: 1) Specifies the rule analysis data that is specific to the file being analyzed. The TestStand Sequence Analyzer creates the file data the first time you call the
 AnalysisContext.GetRuleAnalysisData 
 method while analyzing the file and destroys it after the analysis of the file completes and after calling analysis modules for the after file transition. Do not use this option for the
 AnalysisTransition_BeforeSystem 
 and
 AnalysisTransition_AfterSystem 
 transitions.
- RuleAnalysisDataScope_Global 
 –(Value: 0) Specifies the rule analysis data that is global to the analysis session. The sequence analyzer creates the global data before the analysis begins and destroys it after the analysis completes.

#### See Also

[AnalysisContext.GetRuleAnalysisData](analysiscontext-getruleanalysisdata.html)

[AnalysisTransition](analysistransition.html)

Parent topic:

Sequence Analyzer API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfiguration-configurationdata.html language=enus -->
## TOPIC 00143: RuleConfiguration.ConfigurationData

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfiguration-configurationdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfiguration-configurationdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfiguration.ConfigurationData Data Type PropertyObject Purpose In a rule configuration module, use this property to store configuration data for the rule. In an analysis module, use this property to obtain the configuration data stored for the rule. Remarks Use only rule configuration m

### RuleConfiguration.ConfigurationData

#### Syntax

[RuleConfiguration](ruleconfiguration.html).ConfigurationData

#### Data Type

[PropertyObject](../tsapiref/propertyobject.html)

#### Purpose

In a rule configuration module, use this property to store configuration data for the rule. In an analysis module, use this property to obtain the configuration data stored for the rule.

#### Remarks

Use only rule configuration modules to modify configuration data. Do not make changes to the data in an analysis module.

The TestStand Sequence Analyzer creates an empty container property object for each rule when it creates a new analyzer project. Use a rule configuration module to save rule data in the property object.

When you save configuration data to this property in a rule configuration module, also set the
 [RuleConfiguration.Description](ruleconfiguration-description.html)
 property to include a description of the configuration data so that generated reports contain information about the configuration data and so that users can easily view the rule settings by viewing the rule description on the
 [Rules](../tsref/rules-pane-current-sequence-analyzer-project.html)
 pane of the
 [Current Sequence Analyzer Project](../tsref/current-sequence-analyzer-project-window.html)
 window in the TestStand Sequence Editor or on the
 [Rules](../tsref/rules-pane-current-sequence-analyzer-project.html)
 tab of the
 [stand-alone sequence analyzer application](../tsref/teststand-sequence-analyzer-application.html)
 .

#### See Also

[Creating Analysis Modules](/csh?context=ts_tsref_sa_creating_analysis_modules)

[Creating Rule Configuration Modules](/csh?context=ts_tsref_sa_creating_rule_config_modules)

[RuleConfiguration.Description](ruleconfiguration-description.html)

[Rules pane of current sequence analyzer project](../tsref/rules-pane-current-sequence-analyzer-project.html)

Rules tab of
 [stand-alone sequence analyzer application](../tsref/teststand-sequence-analyzer-application.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfiguration-description.html language=enus -->
## TOPIC 00144: RuleConfiguration.Description

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfiguration-description.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfiguration-description.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfiguration.Description Data Type String Purpose Use this property in an analysis module to obtain the rule description. Use this property in a rule configuration module to save a custom rule description. Remarks When you save configuration data to the RuleConfiguration.ConfigurationDat

### RuleConfiguration.Description

#### Syntax

[RuleConfiguration](ruleconfiguration.html).Description

#### Data Type

[String](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this property in an analysis module to obtain the rule description. Use this property in a rule configuration module to save a custom rule description.

#### Remarks

When you save configuration data to the
 [RuleConfiguration.ConfigurationData](ruleconfiguration-configurationdata.html)
 property in a rule configuration module, also set this property to include a description of the configuration data so that generated reports contain information about the configuration data and so that users can easily view the rule settings by viewing the rule description on the
 [Rules](../tsref/rules-pane-current-sequence-analyzer-project.html)
 pane of the
 [Current Sequence Analyzer Project](../tsref/current-sequence-analyzer-project-window.html)
 window in the TestStand Sequence Editor or on the
 [Rules](../tsref/rules-pane-current-sequence-analyzer-project.html)
 tab of the
 [stand-alone sequence analyzer application](../tsref/teststand-sequence-analyzer-application.html)
 .

#### See Also

[RuleConfiguration.ConfigurationData](ruleconfiguration-configurationdata.html)

[Rules pane of current sequence analyzer project](../tsref/rules-pane-current-sequence-analyzer-project.html)

Rules tab of
 [stand-alone sequence analyzer application](../tsref/teststand-sequence-analyzer-application.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfiguration-enabled.html language=enus -->
## TOPIC 00145: RuleConfiguration.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfiguration-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfiguration-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfiguration.Enabled Data Type Boolean Purpose Use this property in an analysis module to determine whether the rule is enabled. Do not set this property. Do not perform any analysis in the analysis module if this property is False . Remarks The TestStand Sequence Analyzer sets this prop

### RuleConfiguration.Enabled

#### Syntax

[RuleConfiguration](ruleconfiguration.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this property in an analysis module to determine whether the rule is enabled. Do not set this property. Do not perform any analysis in the analysis module if this property is
 False
 .

#### Remarks

The TestStand Sequence Analyzer sets this property when a user enables or disables a rule on the
 [Rules](../tsref/rules-pane-current-sequence-analyzer-project.html)
 pane of the
 [Current Sequence Analyzer Project](../tsref/current-sequence-analyzer-project-window.html)
 window in the TestStand Sequence Editor or on the
 [Rules](../tsref/rules-pane-current-sequence-analyzer-project.html)
 tab of the
 [stand-alone sequence analyzer application](../tsref/teststand-sequence-analyzer-application.html)
 .

#### See Also

[Rules pane of current sequence analyzer project](../tsref/rules-pane-current-sequence-analyzer-project.html)

Rules tab of
 [stand-alone sequence analyzer application](../tsref/teststand-sequence-analyzer-application.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfiguration-ruleid.html language=enus -->
## TOPIC 00146: RuleConfiguration.RuleId

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfiguration-ruleid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfiguration-ruleid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfiguration.RuleId Data Type String Purpose Use this property in an analysis module or rule configuration module to obtain the unique ID of the rule.

### RuleConfiguration.RuleId

#### Syntax

[RuleConfiguration](ruleconfiguration.html).RuleId

#### Data Type

[String](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this property in an analysis module or rule configuration module to obtain the unique ID of the rule.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfiguration-rulesettingvalues.html language=enus -->
## TOPIC 00147: RuleConfiguration.RuleSettingValues

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfiguration-rulesettingvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfiguration-rulesettingvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfiguration.RuleSettingValues Data Type RuleSettingValues Purpose Use this property in an analysis module to obtain the values for rule settings. Use this property only for rules for which you enable the Use Rule Settings configuration option on the Advanced tab of the Edit Rule dialog

### RuleConfiguration.RuleSettingValues

#### Syntax

[RuleConfiguration](ruleconfiguration.html).RuleSettingValues

#### Data Type

[RuleSettingValues](rulesettingvalues.html)

#### Purpose

Use this property in an analysis module to obtain the values for rule settings. Use this property only for rules for which you enable the Use Rule Settings configuration option on the
 [Advanced](../tsref/advanced-tab-edit-rule-dialog-box.html)
 tab of the
 [Edit Rule](../tsref/edit-rule-dialog-box.html)
 dialog box. Do not use this property in a rule configuration module. Rule configuration modules store rule data in the
 [RuleConfiguration.ConfigurationData](ruleconfiguration-configurationdata.html)
 property.

#### See Also

[Advanced tab of Edit Rule dialog box](../tsref/advanced-tab-edit-rule-dialog-box.html)

[Creating Analysis Modules](/csh?context=ts_tsref_sa_creating_analysis_modules)

[Creating Rule Configuration Modules](/csh?context=ts_tsref_sa_creating_rule_config_modules)

[RuleConfiguration.ConfigurationData](ruleconfiguration-configurationdata.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfiguration-severity.html language=enus -->
## TOPIC 00148: RuleConfiguration.Severity

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfiguration-severity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfiguration-severity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfiguration.Severity Data Type RuleSeverity Use the following constants with this data type: RuleSeverity_Default –(Value: 3) Specifies the default severity the rule defines. RuleSeverity_Error –(Value: 0) Indicates that the analysis message reflects an error. RuleSeverity_Information –

### RuleConfiguration.Severity

#### Syntax

[RuleConfiguration](ruleconfiguration.html).Severity

#### Data Type

[RuleSeverity](ruleseverity.html)

Use the following constants with this data type:

- RuleSeverity_Default 
 –(Value: 3) Specifies the default severity the rule defines.
- RuleSeverity_Error 
 –(Value: 0) Indicates that the analysis message reflects an error.
- RuleSeverity_Information 
 –(Value: 2) Indicates that the analysis message contains information that is neither a warning nor an error.
- RuleSeverity_Unknown 
 –(Value: 4) Do not use this value.
- RuleSeverity_Warning 
 –(Value: 1) Indicates that the analysis message reflects a warning.

#### Purpose

Use this property in an analysis module or rule configuration module to obtain the rule severity. Do not set this property.

#### Remarks

The TestStand Sequence Analyzer sets this property when a user changes the setting in the Severity column for a rule on the
 [Rules](../tsref/rules-pane-current-sequence-analyzer-project.html)
 pane of the
 [Current Sequence Analyzer Project](../tsref/current-sequence-analyzer-project-window.html)
 window in the TestStand Sequence Editor or on the
 [Rules](../tsref/rules-pane-current-sequence-analyzer-project.html)
 tab of the
 [stand-alone sequence analyzer application](../tsref/teststand-sequence-analyzer-application.html)
 .

#### See Also

[Rules pane of current sequence analyzer project](../tsref/rules-pane-current-sequence-analyzer-project.html)

Rules tab of
 [stand-alone sequence analyzer application](../tsref/teststand-sequence-analyzer-application.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfiguration.html language=enus -->
## TOPIC 00149: RuleConfiguration

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfiguration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the objects of the RuleConfiguration class to access the configuration information of a rule. A rule configuration contains the enabled state, severity, description, and other information for a specific rule. The sequence analyzer stores the configuration information of a rule in an analyzer pro

### RuleConfiguration

Use the objects of the
 RuleConfiguration
 class to access the configuration information of a rule. A rule configuration contains the enabled state, severity, description, and other information for a specific rule. The sequence analyzer stores the configuration information of a rule in an analyzer project.

In a rule configuration module, use the
 [RuleConfigurationContext.RuleConfiguration](ruleconfigurationcontext-ruleconfiguration.html)
 property to obtain an instance of this class.

In an analysis module, use the
 [AnalysisContext.GetRuleConfiguration](analysiscontext-getruleconfiguration.html)
 method to obtain an instance of this class.

#### Properties

| ConfigurationData (Read Only) |
| --- |
| Description |
| Enabled |
| RuleId (Read Only) |
| RuleSettingValues (Read Only) |
| Severity |

#### See Also

[Accessing Rule Configuration Data in Rule Configuration Modules and Analysis Modules](/csh?context=ts_tsref_sa_accessing_rule_config_data)

[AnalysisContext.GetRuleConfiguration](analysiscontext-getruleconfiguration.html)

[Creating Analysis Modules](/csh?context=ts_tsref_sa_creating_analysis_modules)

[Creating Rule Configuration Modules](/csh?context=ts_tsref_sa_creating_rule_config_modules)

[RuleConfigurationContext.RuleConfiguration](ruleconfigurationcontext-ruleconfiguration.html)

Parent topic:

TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfigurationcontext-engine.html language=enus -->
## TOPIC 00150: RuleConfigurationContext.Engine

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfigurationcontext-engine.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfigurationcontext-engine.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfigurationContext.Engine Data Type Engine Purpose Use this property in a rule configuration module to access methods and properties on the TestStand Engine class. See Also TestStand Engine

### RuleConfigurationContext.Engine

#### Syntax

[RuleConfigurationContext](ruleconfigurationcontext.html).Engine

#### Data Type

[Engine](../tsapiref/engine.html)

#### Purpose

Use this property in a rule configuration module to access methods and properties on the TestStand
 
 [Engine](../tsapiref/engine.html)
 class.

#### See Also

TestStand
 [Engine](../tsapiref/engine.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfigurationcontext-ismodified.html language=enus -->
## TOPIC 00151: RuleConfigurationContext.IsModified

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfigurationcontext-ismodified.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfigurationcontext-ismodified.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfigurationContext.IsModified Data Type Boolean Purpose Set this property in a rule configuration module to True if the module makes a change to the rule configuration. The TestStand Sequence Analyzer uses this property to determine whether the rule configuration module modified the pro

### RuleConfigurationContext.IsModified

#### Syntax

[RuleConfigurationContext](ruleconfigurationcontext.html).IsModified

#### Data Type

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Set this property in a rule configuration module to
 True
 if the module makes a change to the rule configuration. The TestStand Sequence Analyzer uses this property to determine whether the rule configuration module modified the project file.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfigurationcontext-ruleconfiguration.html language=enus -->
## TOPIC 00152: RuleConfigurationContext.RuleConfiguration

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfigurationcontext-ruleconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfigurationcontext-ruleconfiguration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleConfigurationContext.RuleConfiguration Data Type RuleConfiguration Purpose Use this property in a rule configuration module to access the rule configuration. The rule configuration stores settings specific to a rule. See Also AnalysisContext.GetRuleConfiguration

### RuleConfigurationContext.RuleConfiguration

#### Syntax

[RuleConfigurationContext](ruleconfigurationcontext.html).RuleConfiguration

#### Data Type

[RuleConfiguration](ruleconfiguration.html)

#### Purpose

Use this property in a rule configuration module to access the rule configuration. The rule configuration stores settings specific to a rule.

#### See Also

[AnalysisContext.GetRuleConfiguration](analysiscontext-getruleconfiguration.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleconfigurationcontext.html language=enus -->
## TOPIC 00153: RuleConfigurationContext

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleconfigurationcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleconfigurationcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the objects of the RuleConfigurationContext class in a rule configuration module to access the rule configuration data. The TestStand Sequence Analyzer passes an instance of this class as a parameter to the rule configuration module. Properties Engine (Read Only) IsModified RuleConfiguration (Re

### RuleConfigurationContext

Use the objects of the
 RuleConfigurationContext
 class in a rule configuration module to access the rule configuration data. The TestStand Sequence Analyzer passes an instance of this class as a parameter to the rule configuration module.

#### Properties

| Engine (Read Only) |
| --- |
| IsModified |
| RuleConfiguration (Read Only) |

#### See Also

[Creating Rule Configuration Modules](/csh?context=ts_tsref_sa_creating_rule_config_modules)

Parent topic:

TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/rulesettingvalues-getbooleanvalue.html language=enus -->
## TOPIC 00154: RuleSettingValues.GetBooleanValue

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/rulesettingvalues-getbooleanvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/rulesettingvalues-getbooleanvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleSettingValues.GetBooleanValue( settingName) Return Value Boolean Purpose Use this method in an analysis module to obtain the value for a Boolean rule setting. Parameters settingName As String [In] Pass the name of the rule setting.

### RuleSettingValues.GetBooleanValue

#### Syntax

[RuleSettingValues](rulesettingvalues.html).GetBooleanValue( settingName)

#### Return Value

[Boolean](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this method in an analysis module to obtain the value for a Boolean rule setting.

#### Parameters

settingName
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the name of the rule setting.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/rulesettingvalues-getnumbervalue.html language=enus -->
## TOPIC 00155: RuleSettingValues.GetNumberValue

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/rulesettingvalues-getnumbervalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/rulesettingvalues-getnumbervalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleSettingValues.GetNumberValue( settingName) Return Value Double Purpose Use this method in an analysis module to obtain the value for a number or enumeration rule setting. Parameters settingName As String [In] Pass the name of the rule setting.

### RuleSettingValues.GetNumberValue

#### Syntax

[RuleSettingValues](rulesettingvalues.html).GetNumberValue( settingName)

#### Return Value

[Double](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this method in an analysis module to obtain the value for a number or enumeration rule setting.

#### Parameters

settingName
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the name of the rule setting.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/rulesettingvalues-getstringvalue.html language=enus -->
## TOPIC 00156: RuleSettingValues.GetStringValue

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/rulesettingvalues-getstringvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/rulesettingvalues-getstringvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RuleSettingValues.GetStringValue( settingName) Return Value String Purpose Use this method in an analysis module to obtain the value for a string rule setting. Parameters settingName As String [In] Pass the name of the rule setting.

### RuleSettingValues.GetStringValue

#### Syntax

[RuleSettingValues](rulesettingvalues.html).GetStringValue( settingName)

#### Return Value

[String](data-types-for-teststand-sequence-analyzer.html)

#### Purpose

Use this method in an analysis module to obtain the value for a string rule setting.

#### Parameters

settingName
 As
 [String](data-types-for-teststand-sequence-analyzer.html)

[In] Pass the name of the rule setting.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/rulesettingvalues.html language=enus -->
## TOPIC 00157: RuleSettingValues

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/rulesettingvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/rulesettingvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects of the RuleSettingValues class to obtain rule setting values. Use the RuleConfiguration.RuleSettingValues property to obtain an instance of the RuleSettingValues class. Use this class only for rules for which you enable the Use Rule Settings configuration option on the Advanced tab of th

### RuleSettingValues

Use objects of the
 RuleSettingValues
 class to obtain rule setting values. Use the
 [RuleConfiguration.RuleSettingValues](ruleconfiguration-rulesettingvalues.html)
 property to obtain an instance of the
 RuleSettingValues
 class. Use this class only for rules for which you enable the Use Rule Settings configuration option on the
 [Advanced](../tsref/advanced-tab-edit-rule-dialog-box.html)
 tab of the
 [Edit Rule](../tsref/edit-rule-dialog-box.html)
 dialog box.

#### Methods

| GetBooleanValue |
| --- |
| GetNumberValue |
| GetStringValue |

#### See Also

[Accessing Rule Settings in Analysis Modules](/csh?context=ts_tsref_sa_accessing_rule_settings)

[Advanced tab of Edit Rule dialog box](../tsref/advanced-tab-edit-rule-dialog-box.html)

[Creating Analysis Modules](/csh?context=ts_tsref_sa_creating_analysis_modules)

[Creating Rule Configuration Modules](/csh?context=ts_tsref_sa_creating_rule_config_modules)

[RuleConfiguration.RuleSettingValues](ruleconfiguration-rulesettingvalues.html)

Parent topic:

TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/ruleseverity.html language=enus -->
## TOPIC 00158: RuleSeverity

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/ruleseverity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/ruleseverity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the RuleConfiguration.Severity property. RuleSeverity_Default –(Value: 3) Specifies the default severity the rule defines. RuleSeverity_Error –(Value: 0) Indicates that the analysis message reflects an error. RuleSeverity_Information –(Value: 2) Indicates that the analysis m

### RuleSeverity

Use these constants with the
 [RuleConfiguration.Severity](ruleconfiguration-severity.html)
 property.

- RuleSeverity_Default 
 –(Value: 3) Specifies the default severity the rule defines.
- RuleSeverity_Error 
 –(Value: 0) Indicates that the analysis message reflects an error.
- RuleSeverity_Information 
 –(Value: 2) Indicates that the analysis message contains information that is neither a warning nor an error.
- RuleSeverity_Unknown 
 –(Value: 4) Do not use this value.
- RuleSeverity_Warning 
 –(Value: 1) Indicates that the analysis message reflects a warning.

#### See Also

[RuleConfiguration.Severity](ruleconfiguration-severity.html)

Parent topic:

Sequence Analyzer API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/sequence-analyzer-api-constants.html language=enus -->
## TOPIC 00159: Sequence Analyzer API Constants

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/sequence-analyzer-api-constants.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/sequence-analyzer-api-constants.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about each TestStand Sequence Analyzer API constant.

### Sequence Analyzer API Constants

This book contains information about each TestStand Sequence Analyzer API constant.

Parent topic:

NI TestStand Sequence Analyzer Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/sequence-analyzer-api-enumerations.html language=enus -->
## TOPIC 00160: Sequence Analyzer API Enumerations

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/sequence-analyzer-api-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/sequence-analyzer-api-enumerations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains information about each TestStand Sequence Analyzer API enumeration.

### Sequence Analyzer API Enumerations

This book contains information about each TestStand Sequence Analyzer API enumeration.

Parent topic:

NI TestStand Sequence Analyzer Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/teststand-sequence-analyzer.html language=enus -->
## TOPIC 00161: TestStand Sequence Analyzer

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/teststand-sequence-analyzer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/teststand-sequence-analyzer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Object and Description AnalysisContext Use the AnalysisContext class in an analysis module to access information about the current object being analyzed or about the current analysis transition. The TestStand Sequence Analyzer passes an instance of this class as a parameter to the analysis module. A

### TestStand Sequence Analyzer

| Object and Description |
| --- |
| AnalysisContext |
| Use the AnalysisContext class in an analysis module to access information about the current object being analyzed or about the current analysis transition. The TestStand Sequence Analyzer passes an instance of this class as a parameter to the analysis module. |
| AnalysisMessage |
| An object of the AnalysisMessage class represents a message an analysis module creates while performing an analysis. The message displays in the TestStand Sequence Editor or the stand-alone sequence analyzer application and is stored in a TestStand Sequence Analyzer project. Use the AnalysisContext.NewMessage method in an analysis module to create a new instance of this class. |
| AnalysisUtilities |
| Use the objects of the AnalysisUtilities class in an analysis module to perform common analysis functions. Use the AnalysisContext.Utilities property to obtain an instance of this class. |
| RuleConfiguration |
| Use the objects of the RuleConfiguration class to access the configuration information of a rule. A rule configuration contains the enabled state, severity, description, and other information for a specific rule. The sequence analyzer stores the configuration information of a rule in an analyzer project. In a rule configuration module, use the RuleConfigurationContext.RuleConfiguration property to obtain an instance of this class. In an analysis module, use the AnalysisContext.GetRuleConfiguration method to obtain an instance of this class. |
| RuleConfigurationContext |
| Use the objects of the RuleConfigurationContext class in a rule configuration module to access the rule configuration data. The TestStand Sequence Analyzer passes an instance of this class as a parameter to the rule configuration module. |
| RuleSettingValues |
| Use objects of the RuleSettingValues class to obtain rule setting values. Use the RuleConfiguration.RuleSettingValues property to obtain an instance of the RuleSettingValues class. Use this class only for rules for which you enable the Use Rule Settings configuration option on the Advanced tab of the Edit Rule dialog box. |

Parent topic:

NI TestStand Sequence Analyzer Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/validateexpressionoptions.html language=enus -->
## TOPIC 00162: ValidateExpressionOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/validateexpressionoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/validateexpressionoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration with the AnalysisUtilities.ValidateExpression method. ValidateExpressionOption_MustEvaluateToProperty –(Value: 0x2) Specifies that an expression must evaluate to a property location. ValidateExpressionOption_NoOptions –(Value: 0x0) No options. ValidateExpressionOption_Path –(Val

### ValidateExpressionOptions

Use this enumeration with the
 [AnalysisUtilities.ValidateExpression](analysisutilities-validateexpression.html)
 method.

- ValidateExpressionOption_MustEvaluateToProperty 
 –(Value: 0x2) Specifies that an expression must evaluate to a property location.
- ValidateExpressionOption_NoOptions 
 –(Value: 0x0) No options.
- ValidateExpressionOption_Path 
 –(Value: 0x1) Specifies to expect a path in the expression the TestStand Sequence Analyzer validates.

#### See Also

[AnalysisUtilities.ValidateExpression](analysisutilities-validateexpression.html)

Parent topic:

Sequence Analyzer API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/validatepathoptions.html language=enus -->
## TOPIC 00163: ValidatePathOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/validatepathoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/validatepathoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration with the AnalysisUtilities.ValidatePath method. ValidatePathOption_DoNotCheckIfExists –(Value: 0x2) Specifies that a path does not have to exist. You typically use this option when a path refers to a directory or the location of a file to create at run time. ValidatePathOption_I

### ValidatePathOptions

Use this enumeration with the
 [AnalysisUtilities.ValidatePath](analysisutilities-validatepath.html)
 method.

- ValidatePathOption_DoNotCheckIfExists 
 –(Value: 0x2) Specifies that a path does not have to exist. You typically use this option when a path refers to a directory or the location of a file to create at run time.
- ValidatePathOption_IgnoreAbsolutePath 
 –(Value: 0x1) Specifies that the validation does not generate messages from the
 NI_AbsolutePaths 
 rule. Pass this flag when you pass an absolute path to the
 AnalysisUtilities.ValidatePath 
 method and do not want the validation to generate a message.
- ValidatePathOption_IsCommand 
 –(Value: 0x8) Specifies that the path is an executable command. When you use this option and the path has no file extension, the
 AnalysisUtilities.ValidatePath 
 method searches for files with the same basename that end in the
 .exe 
 ,
 .com 
 , and
 .bat 
 common command extensions.
- ValidatePathOption_NoOptions 
 –(Value: 0x0) No options.
- ValidatePathOption_NotRequiredForExecution 
 –(Value: 0x4) Use this option to indicate that a file is not required for execution. If you use this option, the
 AnalysisUtilities.ValidatePath 
 method generates a warning instead of an error if the file you specified is missing.
- ValidatePathOption_DoNotAllowEmpty 
 (Value: 0x20) Specifies that empty paths are not allowed.
- ValidatePathOption_IsDirectory 
 (Value: 0x10) Specifies that the path is a directory.

#### See Also

[AnalysisUtilities.ValidatePath](analysisutilities-validatepath.html)

Parent topic:

Sequence Analyzer API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsanalyzer/vartype.html language=enus -->
## TOPIC 00164: VARTYPE

- bundle_id: `teststand-api-reference`
- source_path: `tsanalyzer/vartype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsanalyzer/vartype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following list identifies the VARTYPE enumeration values: Constant Value Description VT_EMPTY 0 Not specified VT_NULL 1 SQL-style NULL VT_I2 2 2-byte signed int VT_I4 3 4-byte-signed int VT_R4 4 4-byte real VT_R8 5 8-byte real VT_CY 6 Currency VT_DATE 7 Date VT_BSTR 8 Automation string VT_DISPAT

### VARTYPE

The following list identifies the VARTYPE enumeration values:

| Constant | Value | Description |
| --- | --- | --- |
| VT_EMPTY | 0 | Not specified |
| VT_NULL | 1 | SQL-style NULL |
| VT_I2 | 2 | 2-byte signed int |
| VT_I4 | 3 | 4-byte-signed int |
| VT_R4 | 4 | 4-byte real |
| VT_R8 | 5 | 8-byte real |
| VT_CY | 6 | Currency |
| VT_DATE | 7 | Date |
| VT_BSTR | 8 | Automation string |
| VT_DISPATCH | 9 | IDispatch* |
| VT_ERROR | 10 | Scodes |
| VT_BOOL | 11 | Boolean ( True = -1 , False = 0 ) |
| VT_VARIANT | 12 | VARIANT* |
| VT_UNKNOWN | 13 | IUnknown* |
| VT_DECIMAL | 14 | 16-byte fixed point |
| VT_Record | 15 | User-defined type |
| VT_I1 | 16 | Char |
| VT_UI1 | 17 | Unsigned char |
| VT_UI2 | 18 | 2-byte unsigned char |
| VT_UI4 | 19 | 4-byte unsigned char |
| VT_I8 | 20 | 8-byte signed int |
| VT_UI8 | 21 | 8-byte unsigned int |
| VT_INT | 22 | Signed machine int |
| VT_UINT | 23 | Unsigned machine int |
| VT_ARRAY | 0x2000 | SAFEARRAY* |
| VT_BYREF | 0x4000 | — |

Parent topic:

Data Types for TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/acquirelicenseoptions.html language=enus -->
## TOPIC 00165: AcquireLicenseOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/acquirelicenseoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/acquirelicenseoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the options parameter of the Engine.AcquireLicense method. AcquireLicenseOption_NoOptions –(Value: 0x0) Does not specify any options. AcquireLicenseOption_ShowExitButton –(Value: 0x4) Pass this option if you want the startup dialog box to display an Exit button instead of a

### AcquireLicenseOptions

Use these constants with the
 options
 parameter of the
 [Engine.AcquireLicense](engine-acquirelicense.html)
 method.

- AcquireLicenseOption_NoOptions 
 –(Value: 0x0) Does not specify any options.
- AcquireLicenseOption_ShowExitButton 
 –(Value: 0x4) Pass this option if you want the startup dialog box to display an Exit button instead of a Close button. The application exits if the call to the
 Engine.AcquireLicense 
 method fails, and error messages reflect this behavior.
- AcquireLicenseOption_SuppressStartupDialog 
 –(Value: 0x1) Instructs TestStand not to launch a dialog box for evaluating, activating, or purchasing TestStand when the
 
 license 
 is not properly activated.
- AcquireLicenseOption_SuppressStartupDialogIfAlreadyShown 
 –(Value: 0x2) Instructs TestStand not to launch a dialog box for evaluating, activating, or purchasing TestStand when a currently running process has already launched the dialog box and the user activated a license or selected to evaluate TestStand. If the license cannot be acquired and the user did not previously select to evaluate TestStand in an already running process, TestStand launches the dialog box.

#### See Also

[Engine.AcquireLicense](engine-acquirelicense.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexadapter-asadapter.html language=enus -->
## TOPIC 00166: ActiveXAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexadapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexadapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXAdapter.AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter object that represents the ActiveXAdapter object. Remarks Use the underlying module Adapter object to access properties and methods common to all adapters. See Also Adapter

### ActiveXAdapter.AsAdapter

#### Syntax

[ActiveXAdapter](activexadapter.html).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter object that represents the ActiveXAdapter object.

#### Remarks

Use the underlying module Adapter object to access properties and methods common to all adapters.

#### See Also

[Adapter](adapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexadapter-servers.html language=enus -->
## TOPIC 00167: ActiveXAdapter.Servers

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexadapter-servers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexadapter-servers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXAdapter.Servers Data Type ActiveXServers Purpose Returns the list of ActiveX Automation servers registered on this computer. See Also ActiveXServers

### ActiveXAdapter.Servers

#### Syntax

[ActiveXAdapter](activexadapter.html).Servers

#### Data Type

[ActiveXServers](activexservers.html)

#### Purpose

Returns the list of ActiveX Automation servers registered on this computer.

#### See Also

[ActiveXServers](activexservers.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexadapter-showactivexcontrolswhenspecify.html language=enus -->
## TOPIC 00168: ActiveXAdapter.ShowActiveXControlsWhenSpecifyingModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexadapter-showactivexcontrolswhenspecify.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexadapter-showactivexcontrolswhenspecify.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXAdapter.ShowActiveXControlsWhenSpecifyingModule Data Type Boolean Purpose Specifies that the Specify Module dialog box for the ActiveX/COM Adapter includes ActiveX controls in the list of available servers. See Also Specify Module dialog box

### ActiveXAdapter.ShowActiveXControlsWhenSpecifyingModule

#### Syntax

[ActiveXAdapter](activexadapter.html).ShowActiveXControlsWhenSpecifyingModule

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the
 [Specify Module](../tsref/edit-activex-com-call-dialog-box.html)
 dialog box for the ActiveX/COM Adapter includes ActiveX controls in the list of available servers.

#### See Also

[Specify Module dialog box](../tsref/edit-activex-com-call-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexadapter-unloadunusedactivexserversafte.html language=enus -->
## TOPIC 00169: ActiveXAdapter.UnloadUnusedActiveXServersAfterExec

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexadapter-unloadunusedactivexserversafte.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexadapter-unloadunusedactivexserversafte.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXAdapter.UnloadUnusedActiveXServersAfterExec Data Type Boolean Purpose Specifies that the ActiveX/COM Adapter requests the operating system to unload in-process (DLL) servers after every execution. The operating system only unloads servers you are no longer using. Disable this option to

### ActiveXAdapter.UnloadUnusedActiveXServersAfterExec

#### Syntax

[ActiveXAdapter](activexadapter.html).UnloadUnusedActiveXServersAfterExec

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the ActiveX/COM Adapter requests the operating system to unload in-process (DLL) servers after every execution. The operating system only unloads servers you are no longer using. Disable this option to improve execution speed.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexadapter-updateautomationids.html language=enus -->
## TOPIC 00170: ActiveXAdapter.UpdateAutomationIDs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexadapter-updateautomationids.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexadapter-updateautomationids.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXAdapter.UpdateAutomationIDs( seqFileToUpdate, numStepsModified, numStepUpdatesFailed, errorDescription) Purpose When you update the interface for an ActiveX Automation server and the object and member identifiers have changed, you must respecify any step that uses the server. Use the U

### ActiveXAdapter.UpdateAutomationIDs

#### Syntax

[ActiveXAdapter](activexadapter.html).UpdateAutomationIDs( seqFileToUpdate, numStepsModified, numStepUpdatesFailed, errorDescription)

#### Purpose

When you update the interface for an ActiveX Automation server and the object and member identifiers have changed, you must respecify any step that uses the server. Use the UpdateAutomationIDs method to update the identifiers in a sequence file based on the name of the object or member.

For steps that create an object, this method updates the object identifiers CLSID and IID. For steps that call a method or property, this method updates the member identifier MEMBERID.

#### Remarks

This method applies only when you configure the ActiveX/COM Adapter to use early binding.

#### Parameters

seqFileToUpdate
 As
 
 [SequenceFile](sequencefile.html)

[In] Specifies a reference to the sequence file that contains ActiveX steps to update.

numStepsModified
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the number of steps the method updated.

numStepUpdatesFailed
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the number of steps the method failed to update.

errorDescription
 As
 [String](data-types-for-teststand.html)

[Out] When a syntax error exists, this parameter returns an error message describing the type of error.

#### See Also

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexadapter-uselatebinding.html language=enus -->
## TOPIC 00171: ActiveXAdapter.UseLateBinding

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexadapter-uselatebinding.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexadapter-uselatebinding.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXAdapter.UseLateBinding Data Type Boolean Purpose Specifies whether the ActiveX/COM Adapter uses late binding or early binding. When you specify the module for an ActiveX/COM step, TestStand stores the IDs and names of the object and member the step calls. During execution, the ActiveX/

### ActiveXAdapter.UseLateBinding

#### Syntax

[ActiveXAdapter](activexadapter.html).UseLateBinding

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether the ActiveX/COM Adapter uses late binding or early binding. When you specify the module for an ActiveX/COM step, TestStand stores the IDs and names of the object and member the step calls. During execution, the ActiveX/COM Adapter must invoke the ActiveX Automation server and specify which object to create and which member to call.

You can use one of the following options to specify how the server performs operations on the objects:

- Early Binding 
 —Configures the module adapter to use IDs.
- Late Binding 
 —Configures the module adapter to use names.

While early binding is more efficient, it requires that the IDs for objects and methods exposed by automation servers do not change. If you are developing an automation server in an application development environment (ADE) that does not provide direct control over IDs, National Instruments recommends using late binding during development so inadvertent changes to IDs do not invalidate the module information for the step. When you finish developing the automation server, set the
 Use Late Binding
 option in the
 [ActiveX/COM Adapter Configuration](../tsref/activex-com-adapter-configuration-dialog-box.html)
 dialog box to
 False
 and update the IDs in the client sequences.

To update the IDs in the client sequences, edit the module information for each step that references the server or select
 Tools»Update Automation Identifiers
 in each sequence file that contains ActiveX/COM steps that reference the server.

#### Remarks

If you are using a third-party or release version of an automation server, or if you are developing a server in an ADE in which you can control the server IDs, National Instruments recommends disabling the Use Late Binding option.

When you configure the ActiveX/COM Adapter to use late binding, the adapter uses the stored names to determine the proper IDs to use at run time.

The ActiveX/COM Adapter looks at the most recent version of type information for the server.

Servers can also specify type information in different languages. If the ActiveX/COM Adapter cannot find a version of the type information that uses the system default language ID, it attempts to find type information that uses the English or Neutral language IDs, in that order.

#### See Also

[ActiveX/COM Adapter Configuration dialog box](../tsref/activex-com-adapter-configuration-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexadapter.html language=enus -->
## TOPIC 00172: ActiveXAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the ActiveXAdapter class to configure and obtain ActiveX/COM Adapter-specific information about the module adapter. Call Engine.GetAdapter or Engine.GetAdapterByKeyName to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use AsAdap

### ActiveXAdapter

Use objects from the ActiveXAdapter class to configure and obtain ActiveX/COM Adapter-specific information about the module adapter. Call
 
 [Engine.GetAdapter](engine-getadapter.html)
 or
 
 [Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)
 to obtain a reference to the adapter object.

To access the properties and methods of the Adapter class, use
 [AsAdapter](activexadapter-asadapter.html)
 to obtain an object.

#### Properties

| Servers (Read Only) |
| --- |
| ShowActiveXControlsWhenSpecifyingModule |
| UnloadUnusedActiveXServersAfterExec |
| UseLateBinding |

#### Methods

| AsAdapter |
| --- |
| UpdateAutomationIDs |

#### See Also

[Adapter](adapter.html)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass-documentation.html language=enus -->
## TOPIC 00173: ActiveXCoClass.Documentation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass-documentation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass-documentation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClass.Documentation Data Type String Purpose Returns the brief description of the coclass.

### ActiveXCoClass.Documentation

#### Syntax

[ActiveXCoClass](activexcoclass.html).Documentation

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the brief description of the coclass.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass-getinterfaceimplementationtype.html language=enus -->
## TOPIC 00174: ActiveXCoClass.GetInterfaceImplementationTypeFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass-getinterfaceimplementationtype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass-getinterfaceimplementationtype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClass.GetInterfaceImplementationTypeFlags( interfaceIndex) Return Value Long Returns any combination of TYPEFLAGS defined in the Microsoft Windows Software Development Kit. Purpose Returns flags associated with a specified interface in the ActiveXCoClass.Interfaces property. Paramete

### ActiveXCoClass.GetInterfaceImplementationTypeFlags

#### Syntax

[ActiveXCoClass](activexcoclass.html).GetInterfaceImplementationTypeFlags( interfaceIndex)

#### Return Value

[Long](data-types-for-teststand.html)

Returns any combination of TYPEFLAGS defined in the Microsoft Windows Software Development Kit.

#### Purpose

Returns flags associated with a specified interface in the
 [ActiveXCoClass.Interfaces](activexcoclass-interfaces.html)
 property.

#### Parameters

interfaceIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index of an interface in the
 [ActiveXCoClass.Interfaces](activexcoclass-interfaces.html)
 property.

#### See Also

[ActiveXCoClass.Interfaces](activexcoclass-interfaces.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass-helpcontext.html language=enus -->
## TOPIC 00175: ActiveXCoClass.HelpContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass-helpcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass-helpcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClass.HelpContext Data Type Long Purpose Returns the ID of the help topic for the coclass in the help file the ActiveXCoClass.HelpFilePath property specifies. See Also ActiveXCoClass.HelpFilePath

### ActiveXCoClass.HelpContext

#### Syntax

[ActiveXCoClass](activexcoclass.html).HelpContext

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the ID of the help topic for the coclass in the help file the
 [ActiveXCoClass.HelpFilePath](activexcoclass-helpfilepath.html)
 property specifies.

#### See Also

[ActiveXCoClass.HelpFilePath](activexcoclass-helpfilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass-helpfilepath.html language=enus -->
## TOPIC 00176: ActiveXCoClass.HelpFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass-helpfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass-helpfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClass.HelpFilePath Data Type String Purpose Returns the absolute path of the help file of the coclass. See Also ActiveXCoClass.HelpContext

### ActiveXCoClass.HelpFilePath

#### Syntax

[ActiveXCoClass](activexcoclass.html).HelpFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path of the help file of the coclass.

#### See Also

[ActiveXCoClass.HelpContext](activexcoclass-helpcontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass-id.html language=enus -->
## TOPIC 00177: ActiveXCoClass.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClass.Id Data Type String Purpose Returns the GUID of the coclass. See Also ActiveXCoClass.Name

### ActiveXCoClass.Id

#### Syntax

[ActiveXCoClass](activexcoclass.html).Id

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the GUID of the coclass.

#### See Also

[ActiveXCoClass.Name](activexcoclass-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass-interfaces.html language=enus -->
## TOPIC 00178: ActiveXCoClass.Interfaces

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass-interfaces.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClass.Interfaces Data Type ActiveXInterfaces Purpose Returns the interfaces this coclass implements. See Also ActiveXCoClass.GetInterfaceImplementationTypeFlags ActiveXInterfaces

### ActiveXCoClass.Interfaces

#### Syntax

[ActiveXCoClass](activexcoclass.html).Interfaces

#### Data Type

[ActiveXInterfaces](activexinterfaces.html)

#### Purpose

Returns the interfaces this coclass implements.

#### See Also

[ActiveXCoClass.GetInterfaceImplementationTypeFlags](activexcoclass-getinterfaceimplementationtype.html)

[ActiveXInterfaces](activexinterfaces.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass-name.html language=enus -->
## TOPIC 00179: ActiveXCoClass.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClass.Name Data Type String Purpose Returns the name of the coclass. See Also ActiveXCoClass.Id

### ActiveXCoClass.Name

#### Syntax

[ActiveXCoClass](activexcoclass.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the coclass.

#### See Also

[ActiveXCoClass.Id](activexcoclass-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass-typeflags.html language=enus -->
## TOPIC 00180: ActiveXCoClass.TypeFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass-typeflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass-typeflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClass.TypeFlags Data Type Long Purpose Returns the type flags of the coclass. This property can be any combination of TYPEFLAGS defined in the Microsoft Windows Software Development Kit.

### ActiveXCoClass.TypeFlags

#### Syntax

[ActiveXCoClass](activexcoclass.html).TypeFlags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the type flags of the coclass. This property can be any combination of TYPEFLAGS defined in the Microsoft Windows Software Development Kit.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclass.html language=enus -->
## TOPIC 00181: ActiveXCoClass

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclass.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclass.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an ActiveXCoClass object to obtain information about a coclass defined in a type library. Use the ActiveXServer.CoClasses property to obtain a collection of coclasses the type library for the server defines. You must call the ActiveXServer.LoadTypeLibrary method before accessing any coclass info

### ActiveXCoClass

Use an ActiveXCoClass object to obtain information about a coclass defined in a type library. Use the
 [ActiveXServer.CoClasses](activexserver-coclasses.html)
 property to obtain a collection of coclasses the type library for the server defines. You must call the
 [ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)
 method before accessing any coclass information for the server.

#### Properties

| Documentation (Read Only) |
| --- |
| HelpContext (Read Only) |
| HelpFilePath (Read Only) |
| Id (Read Only) |
| Interfaces (Read Only) |
| Name (Read Only) |
| TypeFlags (Read Only) |

#### Method

| GetInterfaceImplementationTypeFlags |
| --- |

#### See Also

[ActiveXServer.CoClasses](activexserver-coclasses.html)

[ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclasses-count.html language=enus -->
## TOPIC 00182: ActiveXCoClasses.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclasses-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclasses-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClasses.Count Data Type Long Purpose Returns the number of items in the collection.

### ActiveXCoClasses.Count

#### Syntax

[ActiveXCoClasses](activexcoclasses.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclasses-item.html language=enus -->
## TOPIC 00183: ActiveXCoClasses.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclasses-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclasses-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXCoClasses.Item( index) Data Type ActiveXCoClass Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also ActiveXCoClass

### ActiveXCoClasses.Item

#### Syntax

[ActiveXCoClasses](activexcoclasses.html).Item( index)

#### Data Type

[ActiveXCoClass](activexcoclass.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[ActiveXCoClass](activexcoclass.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexcoclasses.html language=enus -->
## TOPIC 00184: ActiveXCoClasses

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexcoclasses.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexcoclasses.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ActiveXCoClass objects. Use the ActiveXServer.CoClasses property to obtain a collection of ActiveXCoClass objects the type library for the server defines. You must call the ActiveXServer.LoadTypeLibrary method before accessing any coclass information for the server. Properties Count

### ActiveXCoClasses

A collection of
 [ActiveXCoClass](activexcoclass.html)
 objects.

Use the
 [ActiveXServer.CoClasses](activexserver-coclasses.html)
 property to obtain a collection of ActiveXCoClass objects the type library for the server defines. You must call the
 [ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)
 method before accessing any coclass information for the server.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[ActiveXCoClass](activexcoclass.html)

[ActiveXServer.CoClasses](activexserver-coclasses.html)

[ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-dispatchmembers.html language=enus -->
## TOPIC 00185: ActiveXInterface.DispatchMembers

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-dispatchmembers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-dispatchmembers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.DispatchMembers Data Type ActiveXMembers Purpose Returns the members of the interface that supports IDispatch bindings. See Also ActiveXInterface.VTableMembers ActiveXMembers

### ActiveXInterface.DispatchMembers

#### Syntax

[ActiveXInterface](activexinterface.html).DispatchMembers

#### Data Type

[ActiveXMembers](activexmembers.html)

#### Purpose

Returns the members of the interface that supports IDispatch bindings.

#### See Also

[ActiveXInterface.VTableMembers](activexinterface-vtablemembers.html)

[ActiveXMembers](activexmembers.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-documentation.html language=enus -->
## TOPIC 00186: ActiveXInterface.Documentation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-documentation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-documentation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.Documentation Data Type String Purpose Returns the brief description of the interface.

### ActiveXInterface.Documentation

#### Syntax

[ActiveXInterface](activexinterface.html).Documentation

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the brief description of the interface.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-fortypedefonly.html language=enus -->
## TOPIC 00187: ActiveXInterface.ForTypedefOnly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-fortypedefonly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-fortypedefonly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.ForTypedefOnly Data Type Boolean Purpose Returns True if this interface is an alias for another interface.

### ActiveXInterface.ForTypedefOnly

#### Syntax

[ActiveXInterface](activexinterface.html).ForTypedefOnly

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if this interface is an alias for another interface.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-helpcontext.html language=enus -->
## TOPIC 00188: ActiveXInterface.HelpContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-helpcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-helpcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.HelpContext Data Type Long Purpose Returns the ID of the help topic for the interface in the help file the ActiveXInterface.HelpFilePath property specifies. See Also ActiveXInterface.HelpFilePath

### ActiveXInterface.HelpContext

#### Syntax

[ActiveXInterface](activexinterface.html).HelpContext

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the ID of the help topic for the interface in the help file the
 [ActiveXInterface.HelpFilePath](activexinterface-helpfilepath.html)
 property specifies.

#### See Also

[ActiveXInterface.HelpFilePath](activexinterface-helpfilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-helpfilepath.html language=enus -->
## TOPIC 00189: ActiveXInterface.HelpFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-helpfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-helpfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.HelpFilePath Data Type String Purpose Returns the absolute path of the help file of the interface. See Also ActiveXInterface.HelpContext

### ActiveXInterface.HelpFilePath

#### Syntax

[ActiveXInterface](activexinterface.html).HelpFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path of the help file of the interface.

#### See Also

[ActiveXInterface.HelpContext](activexinterface-helpcontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-id.html language=enus -->
## TOPIC 00190: ActiveXInterface.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.Id Data Type String Purpose Returns the GUID of the interface. See Also ActiveXInterface.Name

### ActiveXInterface.Id

#### Syntax

[ActiveXInterface](activexinterface.html).Id

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the GUID of the interface.

#### See Also

[ActiveXInterface.Name](activexinterface-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-name.html language=enus -->
## TOPIC 00191: ActiveXInterface.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.Name Data Type String Purpose Returns the name of the interface. See Also ActiveXInterface.Id

### ActiveXInterface.Name

#### Syntax

[ActiveXInterface](activexinterface.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the interface.

#### See Also

[ActiveXInterface.Id](activexinterface-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-typeflags.html language=enus -->
## TOPIC 00192: ActiveXInterface.TypeFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-typeflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-typeflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.TypeFlags Data Type Long Purpose Returns the type flags of the interface. This property can be any combination of TYPEFLAGS defined in the Microsoft Windows Software Development Kit.

### ActiveXInterface.TypeFlags

#### Syntax

[ActiveXInterface](activexinterface.html).TypeFlags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the type flags of the interface. This property can be any combination of TYPEFLAGS defined in the Microsoft Windows Software Development Kit.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface-vtablemembers.html language=enus -->
## TOPIC 00193: ActiveXInterface.VTableMembers

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface-vtablemembers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface-vtablemembers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterface.VTableMembers Data Type ActiveXMembers Purpose Returns the members of the interface that supports virtual table bindings. See Also ActiveXMembers DispatchMembers

### ActiveXInterface.VTableMembers

#### Syntax

[ActiveXInterface](activexinterface.html).VTableMembers

#### Data Type

[ActiveXMembers](activexmembers.html)

#### Purpose

Returns the members of the interface that supports virtual table bindings.

#### See Also

[ActiveXMembers](activexmembers.html)

[DispatchMembers](activexinterface-dispatchmembers.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterface.html language=enus -->
## TOPIC 00194: ActiveXInterface

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterface.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterface.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an ActiveXInterface object to obtain information about an interface defined in a type library. Use the ActiveXServer.Interfaces property to obtain a collection of interfaces the type library for the server defines. You must call the ActiveXServer.LoadTypeLibrary method before accessing any inter

### ActiveXInterface

Use an ActiveXInterface object to obtain information about an interface defined in a type library. Use the
 [ActiveXServer.Interfaces](activexserver-interfaces.html)
 property to obtain a collection of interfaces the type library for the server defines. You must call the
 [ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)
 method before accessing any interface information for the server.

#### Properties

| DispatchMembers (Read Only) |
| --- |
| Documentation (Read Only) |
| ForTypedefOnly (Read Only) |
| HelpContext (Read Only) |
| HelpFilePath (Read Only) |
| Id (Read Only) |
| Name (Read Only) |
| TypeFlags (Read Only) |
| VTableMembers (Read Only) |

#### See Also

[ActiveXServer.Interfaces](activexserver-interfaces.html)

[ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterfaces-count.html language=enus -->
## TOPIC 00195: ActiveXInterfaces.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterfaces-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterfaces-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterfaces.Count Data Type Long Purpose Returns the number of items in the collection.

### ActiveXInterfaces.Count

#### Syntax

[ActiveXInterfaces](activexinterfaces.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterfaces-item.html language=enus -->
## TOPIC 00196: ActiveXInterfaces.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterfaces-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterfaces-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXInterfaces.Item( index) Data Type ActiveXInterface Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also ActiveXInterface

### ActiveXInterfaces.Item

#### Syntax

[ActiveXInterfaces](activexinterfaces.html).Item( index)

#### Data Type

[ActiveXInterface](activexinterface.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[ActiveXInterface](activexinterface.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexinterfaces.html language=enus -->
## TOPIC 00197: ActiveXInterfaces

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexinterfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexinterfaces.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ActiveXInterface objects. Use the ActiveXServer.Interfaces property to obtain a collection of interfaces the type library for the server defines. You must call the ActiveXServer.LoadTypeLibrary method before accessing any interface information for the server. Properties Count (Read O

### ActiveXInterfaces

A collection of
 [ActiveXInterface](activexinterface.html)
 objects. Use the
 [ActiveXServer.Interfaces](activexserver-interfaces.html)
 property to obtain a collection of interfaces the type library for the server defines. You must call the
 [ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)
 method before accessing any interface information for the server.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[ActiveXInterface](activexinterface.html)

[ActiveXServer.Interfaces](activexserver-interfaces.html)

[ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-dispatchid.html language=enus -->
## TOPIC 00198: ActiveXMember.DispatchId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-dispatchid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-dispatchid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.DispatchId Data Type Long Purpose Returns the ID of the member. See Also ActiveXMember.Name

### ActiveXMember.DispatchId

#### Syntax

[ActiveXMember](activexmember.html).DispatchId

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the ID of the member.

#### See Also

[ActiveXMember.Name](activexmember-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-documentation.html language=enus -->
## TOPIC 00199: ActiveXMember.Documentation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-documentation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-documentation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.Documentation Data Type String Purpose Returns the brief description of the member.

### ActiveXMember.Documentation

#### Syntax

[ActiveXMember](activexmember.html).Documentation

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the brief description of the member.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-functionflags.html language=enus -->
## TOPIC 00200: ActiveXMember.FunctionFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-functionflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-functionflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.FunctionFlags Data Type Long Purpose Returns the function flags of the member. This property can be any combination of FUNCFLAGS defined in the Microsoft Windows Software Development Kit.

### ActiveXMember.FunctionFlags

#### Syntax

[ActiveXMember](activexmember.html).FunctionFlags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the function flags of the member. This property can be any combination of FUNCFLAGS defined in the Microsoft Windows Software Development Kit.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-helpcontext.html language=enus -->
## TOPIC 00201: ActiveXMember.HelpContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-helpcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-helpcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.HelpContext Data Type Long Purpose Returns the ID of the help topic for the member in the help file the ActiveXMember.HelpFilePath property specifies. See Also ActiveXMember.HelpFilePath

### ActiveXMember.HelpContext

#### Syntax

[ActiveXMember](activexmember.html).HelpContext

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the ID of the help topic for the member in the help file the
 [ActiveXMember.HelpFilePath](activexmember-helpfilepath.html)
 property specifies.

#### See Also

[ActiveXMember.HelpFilePath](activexmember-helpfilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-helpfilepath.html language=enus -->
## TOPIC 00202: ActiveXMember.HelpFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-helpfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-helpfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.HelpFilePath Data Type String Purpose Returns the absolute path of the help file of the member. See Also ActiveXMember.HelpContext

### ActiveXMember.HelpFilePath

#### Syntax

[ActiveXMember](activexmember.html).HelpFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path of the help file of the member.

#### See Also

[ActiveXMember.HelpContext](activexmember-helpcontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-membertype.html language=enus -->
## TOPIC 00203: ActiveXMember.MemberType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-membertype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-membertype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.MemberType Data Type ActiveXModuleMemberTypes Use the following constants with this data type: ActiveXMember_CallMethod –(Value: 1) Specifies that the module calls a method. ActiveXMember_DoNotCall –(Value: -1) Specifies that the module does not call a method or access a propert

### ActiveXMember.MemberType

#### Syntax

[ActiveXMember](activexmember.html).MemberType

#### Data Type

[ActiveXModuleMemberTypes](activexmodulemembertypes.html)

Use the following constants with this data type:

- ActiveXMember_CallMethod 
 –(Value: 1) Specifies that the module calls a method.
- ActiveXMember_DoNotCall 
 –(Value: -1) Specifies that the module does not call a method or access a property.
- ActiveXMember_GetProperty 
 –(Value: 2) Specifies that the module gets a property.
- ActiveXMember_SetProperty 
 –(Value: 4) Specifies that the module sets a property.
- ActiveXMember_SetPropertyByRef 
 –(Value: 8) Specifies that the module sets a reference to a property.

#### Purpose

Returns a value that indicates whether the member is a method or property.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-name.html language=enus -->
## TOPIC 00204: ActiveXMember.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.Name Data Type String Purpose Returns the name of the member. See Also ActiveXMember.DispatchId

### ActiveXMember.Name

#### Syntax

[ActiveXMember](activexmember.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the member.

#### See Also

[ActiveXMember.DispatchId](activexmember-dispatchid.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-parametertypewarnings.html language=enus -->
## TOPIC 00205: ActiveXMember.ParameterTypeWarnings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-parametertypewarnings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-parametertypewarnings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.ParameterTypeWarnings Data Type String Purpose Returns a warning message if the type of any parameter or the type of the return value of this member is incompatible with TestStand types.

### ActiveXMember.ParameterTypeWarnings

#### Syntax

[ActiveXMember](activexmember.html).ParameterTypeWarnings

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a warning message if the type of any parameter or the type of the return value of this member is incompatible with TestStand types.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember-vtableoffset.html language=enus -->
## TOPIC 00206: ActiveXMember.VTableOffset

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember-vtableoffset.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember-vtableoffset.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMember.VTableOffset Data Type Long Purpose Returns the offset of the member in the virtual table.

### ActiveXMember.VTableOffset

#### Syntax

[ActiveXMember](activexmember.html).VTableOffset

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the offset of the member in the virtual table.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmember.html language=enus -->
## TOPIC 00207: ActiveXMember

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmember.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmember.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an ActiveXMember object to obtain information about a method or property defined in a type library. Use the ActiveXInterface.VTableMembers and ActiveXInterface.DispatchMembers properties to obtain a collection of members the type library for an interface of the server defines. Properties Dispatc

### ActiveXMember

Use an ActiveXMember object to obtain information about a method or property defined in a type library. Use the
 [ActiveXInterface.VTableMembers](activexinterface-vtablemembers.html)
 and
 [ActiveXInterface.DispatchMembers](activexinterface-dispatchmembers.html)
 properties to obtain a collection of members the type library for an interface of the server defines.

#### Properties

| DispatchId (Read Only) |
| --- |
| Documentation (Read Only) |
| FunctionFlags (Read Only) |
| HelpContext (Read Only) |
| HelpFilePath (Read Only) |
| MemberType (Read Only) |
| Name (Read Only) |
| ParameterTypeWarnings (Read Only) |
| VTableOffset (Read Only) |

#### See Also

[ActiveXInterface.DispatchMembers](activexinterface-dispatchmembers.html)

[ActiveXInterface.VTableMembers](activexinterface-vtablemembers.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmembers-count.html language=enus -->
## TOPIC 00208: ActiveXMembers.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmembers-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmembers-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMembers.Count Data Type Long Purpose Returns the number of items in the collection.

### ActiveXMembers.Count

#### Syntax

[ActiveXMembers](activexmembers.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmembers-item.html language=enus -->
## TOPIC 00209: ActiveXMembers.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmembers-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmembers-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXMembers.Item( index) Data Type ActiveXMember Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also ActiveXMember

### ActiveXMembers.Item

#### Syntax

[ActiveXMembers](activexmembers.html).Item( index)

#### Data Type

[ActiveXMember](activexmember.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[ActiveXMember](activexmember.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmembers.html language=enus -->
## TOPIC 00210: ActiveXMembers

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmembers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmembers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ActiveXMember objects. Use the ActiveXInterface.VTableMembers and ActiveXInterface.DispatchMembers properties to obtain a collection of ActiveXMember objects defined for an interface in the type library of the server. Properties Count (Read Only) Item (Read Only) See Also ActiveXInte

### ActiveXMembers

A collection of
 [ActiveXMember](activexmember.html)
 objects.

Use the
 [ActiveXInterface.VTableMembers](activexinterface-vtablemembers.html)
 and
 [ActiveXInterface.DispatchMembers](activexinterface-dispatchmembers.html)
 properties to obtain a collection of ActiveXMember objects defined for an interface in the type library of the server.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[ActiveXInterface.DispatchMembers](activexinterface-dispatchmembers.html)

[ActiveXInterface.VTableMembers](activexinterface-vtablemembers.html)

[ActiveXMember](activexmember.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-activexreferenceexpr.html language=enus -->
## TOPIC 00211: ActiveXModule.ActiveXReferenceExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-activexreferenceexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-activexreferenceexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.ActiveXReferenceExpr Data Type String Purpose Specifies a variable or property using the ActiveX Reference type. Remarks When an ActiveX module creates an object, it assigns the object reference to the variable or property, if specified. Otherwise, the module automatically relea

### ActiveXModule.ActiveXReferenceExpr

#### Syntax

[ActiveXModule](activexmodule.html).ActiveXReferenceExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a variable or property using the ActiveX Reference type.

#### Remarks

When an ActiveX module creates an object, it assigns the object reference to the variable or property, if specified. Otherwise, the module automatically releases the object reference after executing. If the module does not create an object, but calls a method or accesses a property instead, the ActiveXReferenceExpr property must contain the value of a valid ActiveX reference that refers to the object on which to call the method or access the property.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-asmodule.html language=enus -->
## TOPIC 00212: ActiveXModule.AsModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-asmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-asmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.AsModule Return Value Module Purpose Returns the underlying module that represents the ActiveXModule object. Remarks Use the module to access properties and methods common to all modules. See Also Module

### ActiveXModule.AsModule

#### Syntax

[ActiveXModule](activexmodule.html).AsModule

#### Return Value

[Module](module.html)

#### Purpose

Returns the underlying module that represents the ActiveXModule object.

#### Remarks

Use the module to access properties and methods common to all modules.

#### See Also

[Module](module.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-coclassname.html language=enus -->
## TOPIC 00213: ActiveXModule.CoClassName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-coclassname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-coclassname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.CoClassName Data Type String The name of the class object. Purpose Specifies the name of the server class the module uses when it creates an object of the class. Remarks An ActiveX module can access two groups of server objects. The first group includes all top-level objects the

### ActiveXModule.CoClassName

#### Syntax

[ActiveXModule](activexmodule.html).CoClassName

#### Data Type

[String](data-types-for-teststand.html)

The name of the class object.

#### Purpose

Specifies the name of the server class the module uses when it creates an object of the class.

#### Remarks

An ActiveX module can access two groups of server objects. The first group includes all top-level objects the module can create. The second group includes all other objects the server creates as a result of an invocation of a method or a property call. Because objects in this second group do not have a class name, ensure the CoClassName remains empty when specifying a module that accesses them. For either group of objects, ensure the
 [ActiveXModule.InterfaceName](activexmodule-interfacename.html)
 property contains the name of the interface with which the module accesses the object.

#### See Also

[ActiveXModule.InterfaceName](activexmodule-interfacename.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-createoption.html language=enus -->
## TOPIC 00214: ActiveXModule.CreateOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-createoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-createoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.CreateOption Data Type ActiveXModuleCreateOptions Use the following constants with this data type: ActiveXCreate_AttachToActive –(Value: 1) Specifies that the module obtains a reference to an active Application object. ActiveXCreate_DoNotCreate –(Value: 3) Specifies that the mod

### ActiveXModule.CreateOption

#### Syntax

[ActiveXModule](activexmodule.html).CreateOption

#### Data Type

[ActiveXModuleCreateOptions](activexmodulecreateoptions.html)

Use the following constants with this data type:

- ActiveXCreate_AttachToActive 
 –(Value: 1) Specifies that the module obtains a reference to an active Application object.
- ActiveXCreate_DoNotCreate 
 –(Value: 3) Specifies that the module does not create a new instance of the object class.
- ActiveXCreate_FromFile 
 –(Value: 2) Specifies that the module loads an existing object from a file and obtains a reference to the object. If the server application is already running, this option might launch another copy of the application. The server application determines when to launch multiple copies of itself. When you make this selection, the
 Specify Module 
 dialog box displays a File Selection control and a Browse button. Use these controls to specify the file path.
- ActiveXCreate_New 
 –(Value: 0) Specifies that the module creates a new object and obtains a reference to the object. If the server application is already running, the module might launch another copy of the application. The server application determines when to launch multiple copies of itself.

#### Purpose

Specifies how a module creates a new instance of the specified object class when it executes.

#### See Also

[Specify Module dialog box](../tsref/edit-activex-com-call-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-filepath.html language=enus -->
## TOPIC 00215: ActiveXModule.FilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-filepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-filepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.FilePath Data Type String The path of the file from which to load the object. Purpose When the ActiveXModule.CreateOption property specifies ActiveXCreate_FromFile , this property specifies the path of the file from which the module loads the object and obtains a reference. Rema

### ActiveXModule.FilePath

#### Syntax

[ActiveXModule](activexmodule.html).FilePath

#### Data Type

[String](data-types-for-teststand.html)

The path of the file from which to load the object.

#### Purpose

When the
 [ActiveXModule.CreateOption](activexmodule-createoption.html)
 property specifies
 ActiveXCreate_FromFile
 , this property specifies the path of the file from which the module loads the object and obtains a reference.

#### Remarks

You can specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

If a server application is already running, the module might launch another copy of the application. The server application determines when to launch multiple copies of itself.

#### See Also

[ActiveXModule.CreateOption](activexmodule-createoption.html)

[Search Directory Paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-interfacename.html language=enus -->
## TOPIC 00216: ActiveXModule.InterfaceName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-interfacename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-interfacename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.InterfaceName Data Type String The name of the interface. Purpose Specifies the name of the interface the module uses when it invokes a server object. Remarks An ActiveX module can access two groups of server objects. The first group includes all top-level objects the module can

### ActiveXModule.InterfaceName

#### Syntax

[ActiveXModule](activexmodule.html).InterfaceName

#### Data Type

[String](data-types-for-teststand.html)

The name of the interface.

#### Purpose

Specifies the name of the interface the module uses when it invokes a server object.

#### Remarks

An ActiveX module can access two groups of server objects. The first group includes all top-level objects the module can create. The second group includes all other objects the server creates as a result of an invocation of a method or a property call. Because objects in this second group do not have a class name, ensure the
 [ActiveXModule.CoClassName](activexmodule-coclassname.html)
 property remains empty when specifying a module that accesses them. For either group of objects, ensure this property contains the name of the interface with which the module accesses the object.

#### See Also

[ActiveXModule.CoClassName](activexmodule-coclassname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-loadmemberinfo.html language=enus -->
## TOPIC 00217: ActiveXModule.LoadMemberInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-loadmemberinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-loadmemberinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.LoadMemberInfo( discardParameterValues = False) Return Value Boolean Returns a value that indicates whether the member information of the module was loaded. This method usually returns True . Purpose This method is obsolete. Use the Module.LoadPrototype method instead. Remarks L

### ActiveXModule.LoadMemberInfo

#### Syntax

[ActiveXModule](activexmodule.html).LoadMemberInfo( discardParameterValues = False)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the member information of the module was loaded. This method usually returns
 True
 .

#### Purpose

Note

Module.LoadPrototype

#### Remarks

Loads information for the parameters of the specified member of the module.

You must set the
 [ActiveXModule.ServerId](activexmodule-serverid.html)
 ,
 [ActiveXModule.InterfaceName](activexmodule-interfacename.html)
 ,
 [ActiveXModule.MemberType](activexmodule-membertype.html)
 , and
 [ActiveXModule.MemberName](activexmodule-membername.html)
 properties for the module before calling this module to access the
 [ActiveXModule.Parameters](activexmodule-parameters.html)
 property.

#### Parameters

discardParameterValues
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to reset the
 [ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)
 property of existing parameter values when loading a new prototype.

This parameter has a default value of
 False
 .

#### See Also

[ActiveXModule.InterfaceName](activexmodule-interfacename.html)

[ActiveXModule.MemberName](activexmodule-membername.html)

[ActiveXModule.MemberType](activexmodule-membertype.html)

[ActiveXModule.Parameters](activexmodule-parameters.html)

[ActiveXModule.ServerId](activexmodule-serverid.html)

[ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Obsolete ActiveXModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-membername.html language=enus -->
## TOPIC 00218: ActiveXModule.MemberName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-membername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-membername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.MemberName Data Type String The name of the method or property. Purpose Specifies the name of the class method to invoke or the class property to access. See Also ActiveXModule.MemberType ActiveXModule.Parameters

### ActiveXModule.MemberName

#### Syntax

[ActiveXModule](activexmodule.html).MemberName

#### Data Type

[String](data-types-for-teststand.html)

The name of the method or property.

#### Purpose

Specifies the name of the class method to invoke or the class property to access.

#### See Also

[ActiveXModule.MemberType](activexmodule-membertype.html)

[ActiveXModule.Parameters](activexmodule-parameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-membertype.html language=enus -->
## TOPIC 00219: ActiveXModule.MemberType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-membertype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-membertype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.MemberType Data Type ActiveXModuleMemberTypes Use the following constants with this data type: ActiveXMember_CallMethod –(Value: 1) Specifies that the module calls a method. ActiveXMember_DoNotCall –(Value: -1) Specifies that the module does not call a method or access a propert

### ActiveXModule.MemberType

#### Syntax

[ActiveXModule](activexmodule.html).MemberType

#### Data Type

[ActiveXModuleMemberTypes](activexmodulemembertypes.html)

Use the following constants with this data type:

- ActiveXMember_CallMethod 
 –(Value: 1) Specifies that the module calls a method.
- ActiveXMember_DoNotCall 
 –(Value: -1) Specifies that the module does not call a method or access a property.
- ActiveXMember_GetProperty 
 –(Value: 2) Specifies that the module gets a property.
- ActiveXMember_SetProperty 
 –(Value: 4) Specifies that the module sets a property.
- ActiveXMember_SetPropertyByRef 
 –(Value: 8) Specifies that the module sets a reference to a property.

#### Purpose

Specifies whether the module calls a method or accesses a property.

#### See Also

[ActiveXModule.MemberName](activexmodule-membername.html)

[ActiveXModule.Parameters](activexmodule-parameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-parameters.html language=enus -->
## TOPIC 00220: ActiveXModule.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.Parameters Data Type ActiveXParameters Collection of parameters. Purpose Returns the ActiveXParameters collection that contains a list of the current parameters used as inputs and outputs of the corresponding module. Remarks Call the Module.LoadPrototype method before you access

### ActiveXModule.Parameters

#### Syntax

[ActiveXModule](activexmodule.html).Parameters

#### Data Type

[ActiveXParameters](activexparameters.html)

Collection of parameters.

#### Purpose

Returns the
 [ActiveXParameters](activexparameters.html)
 collection that contains a list of the current parameters used as inputs and outputs of the corresponding module.

#### Remarks

Call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before you access this property.

#### See Also

[ActiveXParameters](activexparameters.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-reloadserver.html language=enus -->
## TOPIC 00221: ActiveXModule.ReloadServer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-reloadserver.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-reloadserver.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.ReloadServer Return Value Boolean Returns True if the ActiveXModule updates the type library information. Purpose Call this method to direct the ActiveXModule to update type library information it stores internally. Remarks The ActiveXModule stores the type library information o

### ActiveXModule.ReloadServer

#### Syntax

[ActiveXModule](activexmodule.html).ReloadServer

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the ActiveXModule updates the type library information.

#### Purpose

Call this method to direct the ActiveXModule to update type library information it stores internally.

#### Remarks

The ActiveXModule stores the type library information of the server specified by
 [ActiveXModule.ServerId](activexmodule-serverid.html)
 internally. The ActiveXModule uses this type library information when you access properties and methods of ActiveXModule or
 [Module](module.html)
 . For example, when you call
 [Module.LoadPrototype](module-loadprototype.html)
 the ActiveXModule uses this type library information to read the prototype of a property or method. The ActiveXModule obtains this type library information the first time you access a property or method that needs it. Use this method to force the ActiveXModule to update the type library information if the type library information might have changed. When you call this method, the ActiveXModule updates the type library information only if the type library has been modified on disk since the last time the ActiveXModule read the type library.

#### See Also

[ActiveXModule.ServerId](activexmodule-serverid.html)

[Module](module.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-remotehost.html language=enus -->
## TOPIC 00222: ActiveXModule.RemoteHost

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-remotehost.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-remotehost.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.RemoteHost Data Type String Specifies the name of the remote system. Purpose Specifies a remote system on which to create the object. Set the ActiveXModule.SpecifyHostByExpression property to True if the value of RemoteHost contains an expression. Otherwise, set the ActiveXModul

### ActiveXModule.RemoteHost

#### Syntax

[ActiveXModule](activexmodule.html).RemoteHost

#### Data Type

[String](data-types-for-teststand.html)

Specifies the name of the remote system.

#### Purpose

Specifies a remote system on which to create the object. Set the
 [ActiveXModule.SpecifyHostByExpression](activexmodule-specifyhostbyexpression.html)
 property to
 True
 if the value of
 RemoteHost
 contains an expression. Otherwise, set the
 ActiveXModule.SpecifyHostByExpression
 property to
 False
 to indicate that this property contains a literal value.

#### Remarks

The module ignores this property when the
 [ActiveXModule.CreateOption](activexmodule-createoption.html)
 property specifies
 ActiveXCreate_AttachToActive
 or
 ActiveXCreate_DoNotCreate
 .

Note

#### See Also

[ActiveXModule.CreateOption](activexmodule-createoption.html)

[ActiveXModule.SpecifyHostByExpression](activexmodule-specifyhostbyexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-serverid.html language=enus -->
## TOPIC 00223: ActiveXModule.ServerId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-serverid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-serverid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.ServerId Data Type String The name of the server. Purpose Specifies the name of the ActiveX Automation server the module uses. Remarks The server must be registered with Microsoft Windows before the module executes, unless the ActiveXModule.CreateOption property specifies Active

### ActiveXModule.ServerId

#### Syntax

[ActiveXModule](activexmodule.html).ServerId

#### Data Type

[String](data-types-for-teststand.html)

The name of the server.

#### Purpose

Specifies the name of the ActiveX Automation server the module uses.

#### Remarks

The server must be registered with Microsoft Windows before the module executes, unless the
 [ActiveXModule.CreateOption](activexmodule-createoption.html)
 property specifies
 ActiveXCreate_FromFile
 and the
 [ActiveXModule.FilePath](activexmodule-filepath.html)
 property specifies a path from which to load the object.

#### See Also

[ActiveXModule.CreateOption](activexmodule-createoption.html)

[ActiveXModule.FilePath](activexmodule-filepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-specifyhostbyexpression.html language=enus -->
## TOPIC 00224: ActiveXModule.SpecifyHostByExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-specifyhostbyexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-specifyhostbyexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.SpecifyHostByExpression Data Type Boolean Purpose Specifies if the ActiveXModule.RemoteHost property contains an expression the module evaluates at run time to determine the name of the remote host. Otherwise, the ActiveXModule.RemoteHost property contains a literal value. Remar

### ActiveXModule.SpecifyHostByExpression

#### Syntax

[ActiveXModule](activexmodule.html).SpecifyHostByExpression

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the
 [ActiveXModule.RemoteHost](activexmodule-remotehost.html)
 property contains an expression the module evaluates at run time to determine the name of the remote host. Otherwise, the
 ActiveXModule.RemoteHost
 property contains a literal value.

#### Remarks

The module ignores this property if RemoteHost is blank.

#### See Also

[ActiveXModule.RemoteHost](activexmodule-remotehost.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule-usesteploadoptions.html language=enus -->
## TOPIC 00225: ActiveXModule.UseStepLoadOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule-usesteploadoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule-usesteploadoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXModule.UseStepLoadOptions Data Type Boolean Purpose Controls the lifetime of an object that the module creates. If this property is False , the module creates the object when it begins executing. The module then releases its internal reference to the object when it completes executing.

### ActiveXModule.UseStepLoadOptions

#### Syntax

[ActiveXModule](activexmodule.html).UseStepLoadOptions

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Controls the lifetime of an object that the module creates. If this property is
 False
 , the module creates the object when it begins executing. The module then releases its internal reference to the object when it completes executing. If this property is
 True
 , the module creates the object when the step loads according to the
 [Step.ModuleLoadOption](step-moduleloadoption.html)
 property and then holds an internal reference to the object until the step unloads according to the
 [Step.ModuleUnloadOption](step-moduleunloadoption.html)
 property.

#### See Also

[Step.ModuleLoadOption](step-moduleloadoption.html)

[Step.ModuleUnloadOption](step-moduleunloadoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodule.html language=enus -->
## TOPIC 00226: ActiveXModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the ActiveXModule class to specify and obtain ActiveX/COM Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to an ActiveXModule object. To access the properties and methods of a specific mo

### ActiveXModule

Use objects from the ActiveXModule class to specify and obtain ActiveX/COM Adapter-specific information about the code module that steps or step type substeps execute. Use the
 
 [Step.Module](step-module.html)
 property to obtain a reference to an ActiveXModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the Module class, use the
 [ActiveXModule.AsModule](activexmodule-asmodule.html)
 method to obtain an object.

You can use the
 
 [Module.LoadPrototype](module-loadprototype.html)
 method to load the prototype for the module the step specifies.

#### Properties

| ActiveXReferenceExpr |
| --- |
| CoClassName |
| CreateOption |
| FilePath |
| InterfaceName |
| MemberName |
| MemberType |
| Parameters (Read Only) |
| RemoteHost |
| ServerId |
| SpecifyHostByExpression |
| UseStepLoadOptions |

#### Methods

| AsModule |
| --- |
| ReloadServer |

#### See Also

[Module](module.html)

[Module.LoadPrototype](module-loadprototype.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodulecreateoptions.html language=enus -->
## TOPIC 00227: ActiveXModuleCreateOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodulecreateoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodulecreateoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ActiveXModule.CreateOption method to specify how an ActiveX module creates a new instance of the specified object class when it executes. ActiveXCreate_AttachToActive –(Value: 1) Specifies that the module obtains a reference to an active Application object. ActiveXCreate

### ActiveXModuleCreateOptions

Use these constants with the
 [ActiveXModule.CreateOption](activexmodule-createoption.html)
 method to specify how an ActiveX module creates a new instance of the specified object class when it executes.

- ActiveXCreate_AttachToActive 
 –(Value: 1) Specifies that the module obtains a reference to an active Application object.
- ActiveXCreate_DoNotCreate 
 –(Value: 3) Specifies that the module does not create a new instance of the object class.
- ActiveXCreate_FromFile 
 –(Value: 2) Specifies that the module loads an existing object from a file and obtains a reference to the object. If the server application is already running, this option might launch another copy of the application. The server application determines when to launch multiple copies of itself. When you make this selection, the
 Specify Module 
 dialog box displays a File Selection control and a Browse button. Use these controls to specify the file path.
- ActiveXCreate_New 
 –(Value: 0) Specifies that the module creates a new object and obtains a reference to the object. If the server application is already running, the module might launch another copy of the application. The server application determines when to launch multiple copies of itself.

#### See Also

[ActiveXModule.CreateOption](activexmodule-createoption.html)

[Specify Module dialog box](../tsref/edit-activex-com-call-dialog-box.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexmodulemembertypes.html language=enus -->
## TOPIC 00228: ActiveXModuleMemberTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexmodulemembertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexmodulemembertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ActiveXModule.MemberType property to specify the type of member the module accesses when it executes. ActiveXMember_CallMethod –(Value: 1) Specifies that the module calls a method. ActiveXMember_DoNotCall –(Value: -1) Specifies that the module does not call a method or a

### ActiveXModuleMemberTypes

Use these constants with the
 [ActiveXModule.MemberType](activexmodule-membertype.html)
 property to specify the type of member the module accesses when it executes.

- ActiveXMember_CallMethod 
 –(Value: 1) Specifies that the module calls a method.
- ActiveXMember_DoNotCall 
 –(Value: -1) Specifies that the module does not call a method or access a property.
- ActiveXMember_GetProperty 
 –(Value: 2) Specifies that the module gets a property.
- ActiveXMember_SetProperty 
 –(Value: 4) Specifies that the module sets a property.
- ActiveXMember_SetPropertyByRef 
 –(Value: 8) Specifies that the module sets a reference to a property.

#### See Also

[ActiveXModule.MemberType](activexmodule-membertype.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-aspropertyobject.html language=enus -->
## TOPIC 00229: ActiveXParameter.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the ActiveXParameter object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### ActiveXParameter.AsPropertyObject

#### Syntax

[ActiveXParameter](activexparameter.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the ActiveXParameter object.

#### Remarks

Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-defaultvalue.html language=enus -->
## TOPIC 00230: ActiveXParameter.DefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-defaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.DefaultValue Data Type String Purpose Returns a display string that represents the default value defined for the parameter.

### ActiveXParameter.DefaultValue

#### Syntax

[ActiveXParameter](activexparameter.html).DefaultValue

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a display string that represents the default value defined for the parameter.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-direction.html language=enus -->
## TOPIC 00231: ActiveXParameter.Direction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-direction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-direction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.Direction Data Type Long Purpose Returns a value that indicates whether the parameter is input, output, or both. Refer to ActiveXParameterDirections for all the possible values. Remarks For input parameters that have default values, optional input parameters, and output param

### ActiveXParameter.Direction

#### Syntax

[ActiveXParameter](activexparameter.html).Direction

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the parameter is input, output, or both. Refer to
 [ActiveXParameterDirections](activexparameterdirections.html)
 for all the possible values.

#### Remarks

For input parameters that have default values, optional input parameters, and output parameters, you can leave the
 [ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)
 property empty. Otherwise, you must specify the name of a variable, parameter, or property.

#### See Also

[ActiveXParameterDirections](activexparameterdirections.html)

[ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-displaytype.html language=enus -->
## TOPIC 00232: ActiveXParameter.DisplayType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-displaytype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-displaytype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.DisplayType Data Type String The display value of the data type of the parameter. Purpose Returns a localized string that describes the ActiveX data type for the parameter. See Also ActiveXParameter.EnumTypeName ActiveXParameter.Type

### ActiveXParameter.DisplayType

#### Syntax

[ActiveXParameter](activexparameter.html).DisplayType

#### Data Type

[String](data-types-for-teststand.html)

The display value of the data type of the parameter.

#### Purpose

Returns a localized string that describes the ActiveX data type for the parameter.

#### See Also

[ActiveXParameter.EnumTypeName](activexparameter-enumtypename.html)

[ActiveXParameter.Type](activexparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-enumtypename.html language=enus -->
## TOPIC 00233: ActiveXParameter.EnumTypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-enumtypename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-enumtypename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.EnumTypeName Data Type String Purpose Returns the name of the enumeration type for a parameter that is an enumeration. See Also ActiveXParameter.DisplayType ActiveXParameter.GetEnumValues

### ActiveXParameter.EnumTypeName

#### Syntax

[ActiveXParameter](activexparameter.html).EnumTypeName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the enumeration type for a parameter that is an enumeration.

#### See Also

[ActiveXParameter.DisplayType](activexparameter-displaytype.html)

[ActiveXParameter.GetEnumValues](activexparameter-getenumvalues.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-getenumvalues.html language=enus -->
## TOPIC 00234: ActiveXParameter.GetEnumValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-getenumvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-getenumvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.GetEnumValues Return Value Object Array Returns an array of property objects where each property object represents an enumeration value. Purpose Returns the enumeration constants for a parameter that is an enumeration. Remarks The property objects in the array that this metho

### ActiveXParameter.GetEnumValues

#### Syntax

[ActiveXParameter](activexparameter.html).GetEnumValues

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns an array of property objects where each property object represents an enumeration value.

#### Purpose

Returns the enumeration constants for a parameter that is an enumeration.

#### Remarks

The property objects in the array that this method returns have a name and value that corresponds to the name and value of the enumeration constant.

Pass the return value of this method as the
 additionalConstants
 parameter of
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 when checking the
 [ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)
 property for errors.

If you are using an ExpressionEdit control to specify the
 ActiveXParameter.ValueExpr
 property, pass the return value of this method to
 
 [ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)
 to direct the ExpressionEdit control to recognize the enumeration constants.

#### See Also

[ActiveXParameter.EnumTypeName](activexparameter-enumtypename.html)

[ActiveXParameter.ValidEvaluationTypes](activexparameter-validevaluationtypes.html)

[ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-isoptional.html language=enus -->
## TOPIC 00235: ActiveXParameter.IsOptional

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-isoptional.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-isoptional.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.IsOptional Data Type Boolean Purpose This property is True if the parameter has the COM optional attribute.

### ActiveXParameter.IsOptional

#### Syntax

[ActiveXParameter](activexparameter.html).IsOptional

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

This property is
 True
 if the parameter has the COM optional attribute.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-isparametermappinginvalid.html language=enus -->
## TOPIC 00236: ActiveXParameter.IsParameterMappingInvalid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-isparametermappinginvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-isparametermappinginvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.IsParameterMappingInvalid( reasonNotValid) Return Value Boolean Returns true if the parameter in the code module is an enum, the argument expression is valid and non-empty, and the mapping of the argument to the parameter in the code module is invalid. Returns false otherwise

### ActiveXParameter.IsParameterMappingInvalid

#### Syntax

[ActiveXParameter](activexparameter.html).IsParameterMappingInvalid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns true if the parameter in the code module is an enum, the argument expression is valid and non-empty, and the mapping of the argument to the parameter in the code module is invalid. Returns false otherwise.

#### Purpose

Indicates if the TestStand enumeration data type of the argument conflicts with the definition of the corresponding enum parameter in the code module.

#### Remarks

The primary purpose of this method is to support error reporting. Therefore, cases where the mapping is not well defined, for example when the argument expression is empty, are not considered invalid. If an empty expression is considered an error condition, the application must check for it separately.

This method does not load the specified assembly. The method relies on the type information stored for the parameter when the module was last specified.

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] If the mapping is invalid,
 reasonNotValid
 contains an error message explaining why the type definitions do not match. If the mapping is valid,
 reasonNotValid
 is set to an empty string.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-parametername.html language=enus -->
## TOPIC 00237: ActiveXParameter.ParameterName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-parametername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-parametername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.ParameterName Data Type String The name of the parameter. Purpose Returns the name of the parameter.

### ActiveXParameter.ParameterName

#### Syntax

[ActiveXParameter](activexparameter.html).ParameterName

#### Data Type

[String](data-types-for-teststand.html)

The name of the parameter.

#### Purpose

Returns the name of the parameter.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-type.html language=enus -->
## TOPIC 00238: ActiveXParameter.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.Type Data Type VARTYPE The data type of the parameter. Purpose Returns the ActiveX data type of the parameter. Remarks The standard ActiveX Automation VARTYPE enumeration defines the ActiveX parameter types. See Also ActiveXParameter.DisplayType

### ActiveXParameter.Type

#### Syntax

[ActiveXParameter](activexparameter.html).Type

#### Data Type

[VARTYPE](data-types-for-teststand.html)

The data type of the parameter.

#### Purpose

Returns the ActiveX data type of the parameter.

#### Remarks

The standard ActiveX Automation VARTYPE enumeration defines the ActiveX parameter types.

#### See Also

[ActiveXParameter.DisplayType](activexparameter-displaytype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-usedefault.html language=enus -->
## TOPIC 00239: ActiveXParameter.UseDefault

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-usedefault.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-usedefault.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.UseDefault Data Type Boolean Purpose Specifies that the parameter must use the default value when available.

### ActiveXParameter.UseDefault

#### Syntax

[ActiveXParameter](activexparameter.html).UseDefault

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the parameter must use the default value when available.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-userdata.html language=enus -->
## TOPIC 00240: ActiveXParameter.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.UserData Data Type PropertyObject Purpose Holds a data item you associate with the parameter object. Remarks Typically, you do not use this property. See Also PropertyObject

### ActiveXParameter.UserData

#### Syntax

[ActiveXParameter](activexparameter.html).UserData

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Holds a data item you associate with the parameter object.

#### Remarks

Typically, you do not use this property.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-validevaluationtypes.html language=enus -->
## TOPIC 00241: ActiveXParameter.ValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-validevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-validevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.ValidEvaluationTypes Data Type EvaluationTypes Purpose Returns the valid types that this parameter can evaluate to. Remarks You can pass the value of this property to the validEvaluationTypes parameter of the Expression.ValidateEvaluationType method to determine whether the v

### ActiveXParameter.ValidEvaluationTypes

#### Syntax

[ActiveXParameter](activexparameter.html).ValidEvaluationTypes

#### Data Type

[EvaluationTypes](evaluationtypes.html)

#### Purpose

Returns the valid types that this parameter can evaluate to.

#### Remarks

You can pass the value of this property to the
 validEvaluationTypes
 parameter of the
 Expression.ValidateEvaluationType
 method to determine whether the value of the
 [ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)
 property contains errors.

If you are using an ExpressionEdit control to display the value of the
 ActiveXParameter.ValueExpr
 property, pass the value of this property to the
 
 [ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)
 method.

#### See Also

[ActiveXParameter.GetEnumValues](activexparameter-getenumvalues.html)

[ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)

[EvaluationTypes](evaluationtypes.html)

[EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.GetValidEvaluationTypes](../tsuiref/expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-valueexpr.html language=enus -->
## TOPIC 00242: ActiveXParameter.ValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-valueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-valueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.ValueExpr Data Type String Purpose Specifies an expression defining the argument to pass as the parameter when calling the member.

### ActiveXParameter.ValueExpr

#### Syntax

[ActiveXParameter](activexparameter.html).ValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression defining the argument to pass as the parameter when calling the member.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-valueexprisignored.html language=enus -->
## TOPIC 00243: ActiveXParameter.ValueExprIsIgnored

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-valueexprisignored.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-valueexprisignored.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.ValueExprIsIgnored Data Type Boolean Purpose Use this property to determine whether the ActiveX Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameters that use default values. See Also ActiveXPa

### ActiveXParameter.ValueExprIsIgnored

#### Syntax

[ActiveXParameter](activexparameter.html).ValueExprIsIgnored

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the ActiveX Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameters that use default values.

#### See Also

[ActiveXParameter.UseDefault](activexparameter-usedefault.html)

[ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter-valueexprisoptional.html language=enus -->
## TOPIC 00244: ActiveXParameter.ValueExprIsOptional

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter-valueexprisoptional.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter-valueexprisoptional.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameter.ValueExprIsOptional Data Type Boolean Purpose Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for return values, output parameters, and

### ActiveXParameter.ValueExprIsOptional

#### Syntax

[ActiveXParameter](activexparameter.html).ValueExprIsOptional

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for return values, output parameters, and parameters with the COM optional attribute are optional.

#### See Also

[ActiveXParameter.Direction](activexparameter-direction.html)

[ActiveXParameter.IsOptional](activexparameter-isoptional.html)

[ActiveXParameter.ValueExpr](activexparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameter.html language=enus -->
## TOPIC 00245: ActiveXParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the ActiveXParameter class to configure and obtain parameter-specific information for an item in the ActiveXParameters collection class. Properties DefaultValue (Read Only) Direction (Read Only) DisplayType (Read Only) EnumTypeName (Read Only) IsOptional (Read Only) ParameterName (R

### ActiveXParameter

Use objects from the ActiveXParameter class to configure and obtain parameter-specific information for an item in the ActiveXParameters collection class.

#### Properties

| DefaultValue (Read Only) |
| --- |
| Direction (Read Only) |
| DisplayType (Read Only) |
| EnumTypeName (Read Only) |
| IsOptional (Read Only) |
| ParameterName (Read Only) |
| Type (Read Only) |
| UseDefault |
| UserData (Read Only) |
| ValidEvaluationTypes (Read Only) |
| ValueExpr |
| ValueExprIsIgnored (Read Only) |
| ValueExprIsOptional (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| GetEnumValues |
| IsParameterMappingInvalid |

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameterdirections.html language=enus -->
## TOPIC 00246: ActiveXParameterDirections

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameterdirections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameterdirections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ActiveXParameter.Direction property returns one or more of the following constants to indicate how the module passes the parameter when it executes. Use the bitwise-AND operator to determine whether any of these flags are set when obtaining the property value. ActiveXParamDirection_In –(Value: 0

### ActiveXParameterDirections

The
 [ActiveXParameter.Direction](activexparameter-direction.html)
 property returns one or more of the following constants to indicate how the module passes the parameter when it executes. Use the bitwise-AND operator to determine whether any of these flags are set when obtaining the property value.

- ActiveXParamDirection_In 
 –(Value: 0x1) Indicates that the parameter is an input parameter.
- ActiveXParamDirection_Out 
 –(Value: 0x2) Indicates that the parameter is an output parameter.
- ActiveXParamDirection_Unknown 
 –(Value: 0x0) Indicates that the module does not have enough information to determine the parameter direction.

#### See Also

[ActiveXParameter.Direction](activexparameter-direction.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameters-count.html language=enus -->
## TOPIC 00247: ActiveXParameters.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameters-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameters-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameters.Count Data Type Long Purpose Returns the number of items in the collection.

### ActiveXParameters.Count

#### Syntax

[ActiveXParameters](activexparameters.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameters-item.html language=enus -->
## TOPIC 00248: ActiveXParameters.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameters-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameters-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXParameters.Item( index) Data Type ActiveXParameter Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the parameter to retrieve. See Also ActiveXParameter

### ActiveXParameters.Item

#### Syntax

[ActiveXParameters](activexparameters.html).Item( index)

#### Data Type

[ActiveXParameter](activexparameter.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to retrieve.

#### See Also

[ActiveXParameter](activexparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexparameters.html language=enus -->
## TOPIC 00249: ActiveXParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the ActiveXParameters class to configure and obtain parameters for a module that uses the ActiveX/COM Adapter. Use the ActiveXModule.Parameters property to obtain the collection of parameters for a module. Properties Count (Read Only) Item (Read Only) See Also ActiveXModule.Paramete

### ActiveXParameters

Use objects from the ActiveXParameters class to configure and obtain parameters for a module that uses the ActiveX/COM Adapter. Use the
 [ActiveXModule.Parameters](activexmodule-parameters.html)
 property to obtain the collection of parameters for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[ActiveXModule.Parameters](activexmodule-parameters.html)

[ActiveXParameter](activexparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/activexserver-coclasses.html language=enus -->
## TOPIC 00250: ActiveXServer.CoClasses

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/activexserver-coclasses.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/activexserver-coclasses.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ActiveXServer.CoClasses Data Type ActiveXCoClasses Purpose Returns the coclasses defined in this server. Remarks You must call the ActiveXServer.LoadTypeLibrary method to load the coclasses from the type library and populate this collection. See Also ActiveXCoClasses ActiveXServer.Interfaces

### ActiveXServer.CoClasses

#### Syntax

[ActiveXServer](activexserver.html).CoClasses

#### Data Type

[ActiveXCoClasses](activexcoclasses.html)

#### Purpose

Returns the coclasses defined in this server.

#### Remarks

You must call the
 [ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)
 method to load the coclasses from the type library and populate this collection.

#### See Also

[ActiveXCoClasses](activexcoclasses.html)

[ActiveXServer.Interfaces](activexserver-interfaces.html)

[ActiveXServer.LoadTypeLibrary](activexserver-loadtypelibrary.html)

Parent topic:

Properties
