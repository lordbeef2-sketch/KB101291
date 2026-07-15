# NI DOCUMENT BUNDLE: labwindows-cvi

<!--NI_BUNDLE_CHUNK bundle=labwindows-cvi start=1001 end=1250 -->
<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidisplayimagefile.htm language=enus -->
## TOPIC 01001: DisplayImageFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidisplayimagefile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidisplayimagefile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DisplayImageFile

int DisplayImageFile (int panelHandle, int controlID, char filename[]);

#### Purpose

Displays the contents of an image file on a picture control.

This function supports the following image types: .tif, .pcx, .bmp, .dib, .rle, .ico, .jpg, .png, .wmf, and .emf.

(Linux) This function supports the following image types: .pcx, .xwd, and .jpg.

To display an image, first create a picture control in the User Interface Editor or using [NewCtrl](../../cvi/uiref/cvinewctrl.htm). Then call DisplayImageFile using the control ID for that picture control.

To replace the current image with another image, call DisplayImageFile with the same control ID but a different image file.

To delete the image, call [DeleteImage](../../cvi/uiref/cvideleteimage.htm), which also removes the image from memory.

#### Supported Controls

You can use DisplayImageFile with [picture controls](../../cvi/uiref/cviprogramming_with_picture_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| filename | char [] | Pathname of the file that contains the image. You can use a complete pathname or a simple filename. If the name is a simple filename, the file is loaded from the directory that contains the executable. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\custctrl\ComboBox\combodemo.cws for an example of using the DisplayImageFile function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidisplaypanel.htm language=enus -->
## TOPIC 01002: DisplayPanel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidisplaypanel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidisplaypanel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DisplayPanel

int DisplayPanel (int panelHandle);

#### Purpose

Displays a panel on the screen.

When a panel is visible and not dimmed, the user can operate it and generate
events from it. Calling DisplayPanel when a panel is already displayed causes the panel to be completely redrawn.

Refer to the [LoadPanel](../../cvi/uiref/cviloadpanel.htm) function reference for an example of how to use this and other panel functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the DisplayPanel function:

- userint\panels.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\splash.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidisplaypcxfile.htm language=enus -->
## TOPIC 01003: DisplayPCXFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidisplaypcxfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidisplaypcxfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DisplayPCXFile

int DisplayPCXFile (char filename[], int top, int left);

#### Purpose

|  | Note This function has been superseded by DisplayImageFile. Repeated use of DisplayPCXFile clutters the panel with redundant controls and causes other unpredictable behavior. |
| --- | --- |

Displays the contents of an image file in a new picture control on the DOS Compatibility window at the given x- and y-coordinates. Use DisplayPCXFile to create the DOS Compatibility window if it has not yet been created.

This function supports the following image types: .tif, .pcx, .bmp, .dib, .rle, .ico, .jpg, .png, .wmf, and .emf.

(Linux) This function supports the following image types: .pcx, .jpg, and .xwd.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | char [] | Name of the image file that contains the image. If the name is a simple filename with no directory path, the file is loaded from the directory that contains the executable. |
| top | int | Coordinate of the top edge of the image. The coordinates can be any value between 0 and 32,767. The origin is in the upper-left corner directly beneath the title bar before the panel is scrolled. |
| left | int | Coordinate of the left edge of the image. The coordinates can be any value between 0 and 32,767. The origin is in the upper-left corner directly beneath the title bar before the panel is scrolled. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| pictureID | int | The picture ID you can use to specify this control in subsequent function calls. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidoscolortorgb.htm language=enus -->
## TOPIC 01004: DOSColorToRGB

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidoscolortorgb.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidoscolortorgb.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DOSColorToRGB

int DOSColorToRGB (int labWindowsDOSColor);

#### Purpose

Translates the 16 standard color values from LabWindows for DOS to RGB values as
shown in the following table. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value.

| LabWindows for DOS | LabWindows/CVI |
| --- | --- |
| 0 (black) | VAL_BLACK = 0x000000L |
| 1 (dark blue) | VAL_DK_BLUE = 0x000080L |
| 2 (dark green) | VAL_DK_GREEN = 0x008000L |
| 3 (dark cyan) | VAL_DK_CYAN = 0x008080L |
| 4 (dark red) | VAL_DK_RED = 0x800000L |
| 5 (dark magenta) | VAL_DK_MAGENTA = 0x800080L |
| 6 (brown) | VAL_DK_YELLOW = 0x808000L |
| 7 (gray) | VAL_LT_GRAY = 0xC0C0C0L |
| 8 (dark gray) | VAL_DK_GRAY = 0x808080L |
| 9 (blue) | VAL_BLUE = 0x0000FFL |
| 10 (green) | VAL_GREEN = 0x00FF00L |
| 11 (cyan) | VAL_CYAN = 0x00FFFFL |
| 12 (red) | VAL_RED = 0xFF0000L |
| 13 (magenta) | VAL_MAGENTA = 0xFF00FFL |
| 14 (yellow) | VAL_YELLOW = 0xFFFF00L |
| 15 (white) | VAL_WHITE = 0xFFFFFFL |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| labWindowsDOSColor | int | One of the 16 standard colors from LabWindows for DOS. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| RGBValue | int | Value indicating the RGB value. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidoscompatwindow.htm language=enus -->
## TOPIC 01005: DOSCompatWindow

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidoscompatwindow.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidoscompatwindow.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DOSCompatWindow

int DOSCompatWindow (void);

#### Purpose

|  | Note This function is obsolete. |
| --- | --- |

Displays a window that serves as a parent panel for panels you created in a LabWindows for DOS program.

You can use the return value as the **parentPanelHandle** parameter to the [LoadPanel](../../cvi/uiref/cviloadpanel.htm) function. You can use DOSCompatWindow with LabWindows for DOS .uir files to retain the appearance of the DOS User Interface screen.

DOSCompatWindow exists as an aid for converting LabWindows for DOS applications. Do not use it when developing new applications in LabWindows/CVI.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| DOSCompatibilityWindowHandle | int | Returns the panel handle for the DOS Compatibility Window. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidsbindctrl.htm language=enus -->
## TOPIC 01006: DSBindCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidsbindctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidsbindctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DSBindCtrl

int DSBindCtrl (int panelHandle, int controlID, char *URL, int accessMode, DSHandle *DSHandle, HRESULT *dataSocketError);

#### Purpose

Binds a control to the DataSocket connection specified in the URL parameter. Call DSUnbind to close the connection.

|  | Note This function is not supported for 64-bit applications. |
| --- | --- |

(Linux) This function is not supported.

Each control can have only one DataSocket connection. Use a URL to specify the location and format of the DataSocket data source. For each DataSocket object that you connect to a DataSocket data source, specify whether the connection is a READ connection or a WRITE connection. If you specify a READ connection, you can use the DataSocket object to get data from the data source. If you specify a WRITE connection, you can use the DataSocket object to send data to the data source.

For some protocols such as dstp, the DataSocket server must be launched on the machine referenced in the URL.

|  | NoteBinding to Tables—If you have not specified a cell range in the User Interface Editor, the bound range defaults to the full table size. Use DSBindTableCellRange instead of DSBindCtrl to specify a cell range programmatically. Binding to Graphs—If a graph is bound in READ mode, it automatically creates a plot when it first receives data from DataSocket. That plot will be reused for all data received from DataSocket. Call DSGetBoundPlotID to get the plot ID that is bound. Call DSBindPlot instead of DSBindCtrl to bind to an existing plot instead of having a new one created. If a graph is bound in write mode, all plots to the graph will be written to DataSocket. |
| --- | --- |

#### Supported Controls

You can use DSBindCtrl with the following controls:

- Graphs
- Numerics
- Text messages
- Text boxes
- Tables
- Strings
- Numeric slides
- Strip charts

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| URL | char * | The URL of the data source for the DataSocket object's connection. The URL you pass can resolve to different types of data sources. A URL consists of a scheme and a data source path. The scheme specifies the type of data. The DataSocket library supports the following URL schemes: http—hypertext transfer protocol ftp—file transfer protocol file—local files dstp—DataSocket transfer protocol opc—OPC (OLE for Process control) servers logos—an internal National Instruments technology for transmitting data between the network and your local computer fieldpoint—a protocol that uses the National Instrument logos protocol to send and receive live data to and from a National Instruments Fieldpoint module The data source path specifies the exact location of the data. The format of the data source path depends on the URL scheme. URL examples http://www.natinst.com/cworks/datasocket/chirp.dsd ftp://ftp.natinst.com/support/compworks/datasocket/chirp.wav dstp://localhost/wave dstp://weather.natinst.com/weather/current file://datafiles/newwave.txt opc://machine/National Instruments.OPCDemo/SINE:0.0..8.0:2.0 logos://computer_name/process/data_item_name fieldpoint://computer_name/process/data_item_name |
| accessMode | int | The access mode constant for the DataSocket object's connection. The access mode determines whether the DataSocket object can read from the DataSocket data source or write to the DataSocket data source. VAL_DS_READ—Configures the DataSocket connection for automatic reading. The DataSocket object gets data from the DataSocket data source at the time that the connection is established, when the data value changes, and when any of the data attributes change. VAL_DS_WRITE—Configures the DataSocket connection for automatic writing. The DataSocket object transfers data to the DataSocket data source at the time that the connection is established and when the data value changes. |
| Output |  |  |
| Name | Type | Description |
| DSHandle | DSHandle | A handle that you can use to identify the DataSocket object in subsequent function calls. The handle is never 0. The status of the connection between a bound control and its DataSocket data source can be obtained by passing the DSHandle to DS_GetStatus. The DSHandle received from DSBindCtrl should never be passed to DS_DiscardObjHandle. Call DSUnbind to unbind the control. |
| dataSocketError | HRESULT | The HRESULT if this function causes a DataSocket error. A value of NULL can be passed in if the HRESULT is not needed. In the event of a DataSocket error, this function returns a value of UIEDataSocketError. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidsbindplot.htm language=enus -->
## TOPIC 01007: DSBindPlot

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidsbindplot.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidsbindplot.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DSBindPlot

int DSBindPlot (int panelHandle, int controlID, int plotID, char *URL, DSHandle *DSHandle, HRESULT *dataSocketError);

#### Purpose

Binds a graph plot to the DataSocket connection specified in the **URL** parameter.

|  | Note This function is not supported for 64-bit applications. |
| --- | --- |

(Linux) This function is not supported.

A plot can be bound only in READ mode. If you pass -1 for **plotID**, LabWindows/CVI creates a new plot.

For some protocols such as dstp, the DataSocket server must be launched on the machine referenced in the URL.

#### Supported Controls

You can use DSBindPlot with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| plotID | int | The ID of the graph plot to be bound to the data source. If you pass -1, LabWindows/CVI creates a new plot. If plotID is invalid, DSBindPlot returns an error. If you specify a plot ID at bind time, the access mode must be READ. In this case, the type of plot you specify must be compatible with the data type in the DataSocket source. Valid plot types are X, Y, waveform, point, intensity, scaled intensity, and text. If you do not specify a plot ID at bind time, and the access mode is READ, the graph control creates a plot dynamically that matches the data type in the DataSocket source. Use ATTR_DS_BIND... attributes to set initial preferences for this plot. |
| URL | char * | The URL of the data source for the DataSocket object's connection. The URL you pass can resolve to different types of data sources. A URL consists of a scheme and a data source path. The scheme specifies the type of data. The DataSocket library supports the following URL schemes: http—hypertext transfer protocol ftp—file transfer protocol file—local files dstp—DataSocket transfer protocol opc—OPC (OLE for Process control) servers logos—an internal National Instruments technology for transmitting data between the network and your local computer fieldpoint—a protocol that uses the National Instrument logos protocol to send and receive live data to and from a National Instruments Fieldpoint module The data source path specifies the exact location of the data. The format of the data source path depends on the URL scheme. URL examples http://www.natinst.com/cworks/datasocket/chirp.dsd ftp://ftp.natinst.com/support/compworks/datasocket/chirp.wav dstp://localhost/wave dstp://weather.natinst.com/weather/current file://datafiles/newwave.txt opc://machine/National Instruments.OPCDemo/SINE:0.0..8.0:2.0 logos://computer_name/process/data_item_name fieldpoint://computer_name/process/data_item_name |
| Output |  |  |
| Name | Type | Description |
| DSHandle | DSHandle | A handle that you can use to identify the DataSocket object in subsequent function calls. The handle is never 0. The status of the connection between a bound control and its DataSocket data source can be obtained by passing the DSHandle to DS_GetStatus. The DSHandle received from DSBindCtrl should never be passed to DS_DiscardObjHandle. Call DSUnbind to unbind the control. |
| dataSocketError | HRESULT | The HRESULT if this function causes a DataSocket error. A value of NULL can be passed in if the HRESULT is not needed. In the event of a DataSocket error, this function returns a value of UIEDataSocketError. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\databinding.cws for an example of using the DSBindPlot function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidsbindtablecellrange.htm language=enus -->
## TOPIC 01008: DSBindTableCellRange

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidsbindtablecellrange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidsbindtablecellrange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DSBindTableCellRange

int DSBindTableCellRange (int panelHandle, int controlID, Rect cellRange, char *URL, int accessMode, DSHandle *dsHandle, HRESULT *dataSocketError);

#### Purpose

Binds a control to the DataSocket connection specified in the **URL** parameter. Call [DSUnbind](../../cvi/uiref/cvidsunbind.htm) to close the connection.

|  | Note This function is not supported for 64-bit applications. |
| --- | --- |

(Linux) This function is not supported.

Each control can have only one DataSocket connection. Use a URL to specify the location and format of the DataSocket data source. For each DataSocket object that you connect to a DataSocket data source, specify whether the connection is a READ connection or a WRITE connection. If you specify a READ connection, you can use the DataSocket object to get data from the data source. If you specify a WRITE connection, you can use the DataSocket object to send data to the data source.

For some protocols such as dstp, the DataSocket server must be launched on the machine referenced in the URL.

#### Supported Controls

You can use DSBindTableCellRange with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cellRange | Rect | A Rect structure specifying the cell range for which you want to set the values. To use this function, you must specify a cell range consisting of a homogeneous cell type. If the cell type is VAL_CELL_NUMERIC, all cells in the range also must share an identical data type. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; Pass the one-based row and column indices of the first cell in the range as the top and left fields of the structure, respectively. Pass the number of columns in the range as the width field of the structure, and the number of rows in the range as the height field of the structure. You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example FillTableCellRange (panelHandle, controlID, MakeRect (2, 3, 5, 5), value); |
| URL | char * | The URL of the data source for the DataSocket object's connection. The URL you pass can resolve to different types of data sources. A URL consists of a scheme and a data source path. The scheme specifies the type of data. The DataSocket library supports the following URL schemes: http—hypertext transfer protocol ftp—file transfer protocol file—local files dstp—DataSocket transfer protocol opc—OPC (OLE for Process control) servers logos—an internal National Instruments technology for transmitting data between the network and your local computer fieldpoint—a protocol that uses the National Instrument logos protocol to send and receive live data to and from a National Instruments Fieldpoint module The data source path specifies the exact location of the data. The format of the data source path depends on the URL scheme. URL examples http://www.natinst.com/cworks/datasocket/chirp.dsd ftp://ftp.natinst.com/support/compworks/datasocket/chirp.wav dstp://localhost/wave dstp://weather.natinst.com/weather/current file://datafiles/newwave.txt opc://machine/National Instruments.OPCDemo/SINE:0.0..8.0:2.0 logos://computer_name/process/data_item_name fieldpoint://computer_name/process/data_item_name |
| accessMode | int | The access mode constant for the DataSocket object's connection. The access mode determines whether the DataSocket object can read from the DataSocket data source or write to the DataSocket data source. VAL_DS_READ—Configures the DataSocket connection for automatic reading. The DataSocket object gets data from the DataSocket data source at the time that the connection is established, when the data value changes, and when any of the data attributes change. VAL_DS_WRITE—Configures the DataSocket connection for automatic writing. The DataSocket object transfers data to the DataSocket data source at the time that the connection is established and when the data value changes. |
| Output |  |  |
| Name | Type | Description |
| dsHandle | DSHandle | A handle that you can use to identify the DataSocket object in subsequent function calls. The handle is never 0. The status of the connection between a bound control and its DataSocket data source can be obtained by passing the DSHandle to DS_GetStatus. The DSHandle received from DSBindCtrl should never be passed to DS_DiscardObjHandle. Call DSUnbind to unbind the control. |
| dataSocketError | HRESULT | The HRESULT if this function causes a DataSocket error. A value of NULL can be passed in if the HRESULT is not needed. In the event of a DataSocket error, this function returns a value of UIEDataSocketError. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\databinding.cws for an example of using the DSBindTableCellRange function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidsgetboundplotid.htm language=enus -->
## TOPIC 01009: DSGetBoundPlotID

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidsgetboundplotid.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidsgetboundplotid.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DSGetBoundPlotID

int DSGetBoundPlotID (int panelHandle, int controlID, int *plotID);

#### Purpose

Returns the ID of the graph plot that is bound to a DataSocket connection.

|  | Note This function is not supported for 64-bit applications. |
| --- | --- |

(Linux) This function is not supported.

#### Supported Controls

You can use DSGetBoundPlotID with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| plotID | int | Returns the plot ID of the graph plot that is bound to a DataSocket connection. A plot ID of zero indicates that the graph has not been bound. A plot ID of -1 indicates that the graph has been bound but a plot has not yet been created because no data has been received through data binding. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvidsunbind.htm language=enus -->
## TOPIC 01010: DSUnbind

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvidsunbind.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvidsunbind.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DSUnbind

int DSUnbind (int panelHandle, int controlID, HRESULT *dataSocketError);

#### Purpose

Unbinds a control from a DataSocket object and frees the resources used by it.

|  | Note This function is not supported for 64-bit applications. |
| --- | --- |

(Linux) This function is not supported.

If the control being unbound is a graph, and you did not specify a **plotID** at the time the graph was bound, LabWindows/CVI deletes the plot. If the graph is in discard mode, the plot will not be deleted.

#### Supported Controls

You can use DSUnbind with the following controls:

- Graphs
- Numerics
- Text messages
- Text boxes
- Tables
- Strings
- Numeric slides
- Strip charts

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| dataSocketError | HRESULT | The HRESULT if this function causes a DataSocket error. A value of NULL can be passed in if the HRESULT is not needed. In the event of a DataSocket error, this function returns a value of UIEDataSocketError. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\databinding.cws for an example of using the DSUnbind function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviduplicatebitmap.htm language=enus -->
## TOPIC 01011: DuplicateBitmap

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviduplicatebitmap.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviduplicatebitmap.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DuplicateBitmap

int DuplicateBitmap (int bitmapID, int *newBitmapID);

#### Purpose

Creates an exact copy of a bitmap created using [functions that return a bitmap ID](../../cvi/uiref/cviusing_bitmap_objects.htm#bitmapids), such as [NewBitmapEx](../../cvi/uiref/cvinewbitmapex.htm) and [GetCtrlBitmap](../../cvi/uiref/cvigetctrlbitmap.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| bitmapID | int | ID of the bitmap object that contains the image. You can obtain the ID from functions such as NewBitmapEx and GetCtrlBitmap. |
| Output |  |  |
| Name | Type | Description |
| newBitmapID | int | ID that serves as a handle to the bitmap object. You can pass the ID to CanvasDrawBitmap, ClipboardPutBitmap, or any other function that accepts a bitmap. To discard the bitmap, pass the ID to DiscardBitmap. Zero is not a valid bitmap ID. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviduplicatectrl.htm language=enus -->
## TOPIC 01012: DuplicateCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviduplicatectrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviduplicatectrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DuplicateCtrl

int DuplicateCtrl (int sourcePanelHandle, int controlID, int destinationPanelHandle, char duplicateLabel[], int controlTop, int controlLeft);

#### Purpose

Copies an existing control from the source panel to the destination panel and returns a control ID. You can use the control ID to reference the control in subsequent function calls.

#### Supported Controls

You can use DuplicateCtrl with all LabWindows/CVI [user interface controls](../../cvi/uiref/cvioperating_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourcePanelHandle | int | Handle of the source panel containing the control to duplicate. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| destinationPanelHandle | int | The parent panel into which to copy the duplicate control. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| duplicateLabel | char [] | Label for the duplicate control. Pass "" for no label. Pass 0 to use the label of the source control. |
| controlTop | int | Vertical coordinate at which to place the upper left corner of the control, not including labels. The valid range for controlTop is –32,768 to 32,767 or VAL_KEEP_SAME_POSITION. The origin (0,0) is at the upper-left corner of the panel, directly below the title bar, before the panel is scrolled. |
| controlLeft | int | Horizontal coordinate at which to place the upper left corner of the control, not including labels. The valid range for controlLeft is –32,768 to 32,767 or VAL_KEEP_SAME_POSITION. The origin (0,0) is at the upper-left corner of the panel, directly below the title bar, before the panel is scrolled. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| duplicateControlID | int | Returns the ID you use to specify the new (duplicate) control in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\tabpanels.cws for an example of using the DuplicateCtrl function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviduplicatepanel.htm language=enus -->
## TOPIC 01013: DuplicatePanel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviduplicatepanel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviduplicatepanel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DuplicatePanel

int DuplicatePanel (int destParentPanelHandle, int originalPanelHandle, char duplicatePanelTitle[], int panelTop, int panelLeft);

#### Purpose

Duplicates a panel into the specified destination parent panel and returns the
duplicate (new) panel handle.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| destParentPanelHandle | int | Handle for the parent panel into which to copy the duplicate panel. To make the panel a top-level panel, pass 0. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| originalPanelHandle | int | Handle of the original panel to duplicate. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| duplicatePanelTitle | char [] | Title of the duplicate (new) panel. Pass "" for no title. Pass 0 to use the title of the original panel. |
| panelTop | int | Vertical coordinate at which to place the upper left corner of the panel, directly below the title bar. Pass VAL_KEEP_SAME_POSITION to keep the same top coordinate as the original panel. The coordinates must be integer values from –32,768 to 32,767 or VAL_AUTO_CENTER to center the panel. For a top-level panel, (0,0) is the upper-left corner of the screen. For a child panel, (0,0) is the upper-left corner of the parent panel, directly below the title bar, before the parent panel is scrolled. |
| panelLeft | int | Horizontal coordinate at which to place the upper left corner of the panel, directly below the title bar. Pass VAL_KEEP_SAME_POSITION to keep the same left coordinate as the original panel. The coordinates must be integer values from –32,768 to 32,767 or VAL_AUTO_CENTER to center the panel. For a top-level panel, (0,0) is the upper-left corner of the screen. For a child panel, (0,0) is the upper-left corner of the parent panel, directly below the title bar, before the parent panel is scrolled. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| panelHandle | int | Value you can use in subsequent function calls to specify this panel. Negative values indicate that an error occurred. Zero is not a valid panel handle. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviduplicatepaneltree.htm language=enus -->
## TOPIC 01014: DuplicatePanelTree

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviduplicatepaneltree.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviduplicatepaneltree.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### DuplicatePanelTree

int DuplicatePanelTree (int destParentPanelHandle, int originalPanelHandle, char duplicatePanelTitle[], int panelTop, int panelLeft);

#### Purpose

Duplicates a panel and its descendents into the specified destination parent panel and returns the
duplicate (new) panel handle.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| destParentPanelHandle | int | Handle for the parent panel into which to copy the duplicate panel. To make the panel a top-level panel, pass 0. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| originalPanelHandle | int | Handle of the original panel to duplicate. You obtain this handle from LoadPanel, NewPanel, or DuplicatePanel. |
| duplicatePanelTitle | char [] | Title of the duplicate (new) panel. Pass "" for no title. Pass 0 to use the title of the original panel. |
| panelTop | int | Vertical coordinate at which to place the upper left corner of the panel, directly below the title bar. The coordinates must be integer values from –32,768 to 32,767, or VAL_AUTO_CENTER to center the panel. For a top-level panel, (0,0) is the upper-left corner of the screen. For a child panel, (0,0) is the upper-left corner of the parent panel, directly below the title bar, before the parent panel is scrolled. |
| panelLeft | int | Horizontal coordinate at which to place the upper left corner of the panel, directly below the title bar. The coordinates must be integer values from –32,768 to 32,767, or VAL_AUTO_CENTER to center the panel. For a top-level panel, (0,0) is the upper-left corner of the screen. For a child panel, (0,0) is the upper-left corner of the parent panel, directly below the title bar, before the parent panel is scrolled. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| panelHandle | int | Value you can use in subsequent function calls to specify this panel. Negative values indicate that an error occurred. Zero is not a valid panel handle. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviemptymenu.htm language=enus -->
## TOPIC 01015: EmptyMenu

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviemptymenu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviemptymenu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EmptyMenu

int EmptyMenu (int menuBarHandle, int menuID);

#### Purpose

Removes all submenus and menu items from a specified menu.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |
| menuID | int | ID for a particular menu within a menu bar. The ID must be a constant name, located in the .uir header file, that you assign in the User Interface Editor or a value that you obtain from functions such as NewMenu and NewSubMenu. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviemptymenubar.htm language=enus -->
## TOPIC 01016: EmptyMenuBar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviemptymenubar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviemptymenubar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EmptyMenuBar

int EmptyMenuBar (int menuBarHandle);

#### Purpose

Removes all menus and menu items from a specific menu bar but retains the
menubar handle in memory.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvierror_conditions.htm language=enus -->
## TOPIC 01017: User Interface Library Error Codes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvierror_conditions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvierror_conditions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### User Interface Library Error Codes

The User Interface Library routines return negative values when they detect error codes. Some functions, such as LoadPanel, return positive values for a successful completion. The following table lists the [error codes](../programmerref/statusreportinginuilib.htm)error codes, defined constants, and error messages associated with functions in the LabWindows/CVI User Interface Library.

Use the [GetUILErrorString](cvigetuilerrorstring.htm) function to convert the error code, returned in the **status** parameter of User Interface Library functions, into meaningful error messages.

Error codes are defined in the cvi\include\userint.h file.

| Code | Defined Constant | Error Message |
| --- | --- | --- |
| 0 | UIENoError | Success |
| -1 | UIEManagerCouldNotOpen | The Interface Manager could not be opened. |
| -2 | UIESystemFontCouldNotBeLoaded | The system font could not be loaded. |
| -3 | UIEOperationInvalidDuringPopUp | The operation attempted cannot be performed while a pop-up menu is active. |
| -4 | UIEHandleInvalid | Panel, pop-up, menu bar, or plot ID is invalid. |
| -5 | UIEAttemptToMovePanelToInvalidLocation | Attempted to position panel at an invalid location |
| -6 | UIEAttemptedToMakeInoperableCtrlActive | Attempted to make an inoperable control the active control. |
| -7 | UIEOperationRequirePanelBeLoaded | The operation requires that a panel be loaded. |
| -8 | UIEOperationRequiresPopUpBeActive | The operation requires that a pop-up menu be active. |
| -9 | UIEOperationRequiresMenuBeLoaded | The operation requires that a menu bar be loaded. |
| -10 | UIEControlNotTypeExpectedByFunction | The control is not the type expected by the function. |
| -11 | UIEInvalidMenuItemId | Invalid menu item ID. |
| -12 | UIEOutOfMemory | Out of memory |
| -13 | UIEInvalidControlId | Invalid control ID. |
| -14 | UIEValueIsInvalidOrOutOfRange | Value is invalid or out of range. |
| -15 | UIEFileIsNotUserInterfaceFileOrIsBad | File is not a User Interface file or has been corrupted. |
| -16 | UIEFileFormatIsOutOfDate | File format is out-of-date. |
| -17 | UIEImageIsBadOrNotSupported | PCX image is corrupted or incompatible with current display type. |
| -18 | UIENoUserEventPossibleWithCurrentSetup | No user event possible in current configuration. |
| -19 | UIEUnableToOpenFile | Unable to open UIR file. |
| -20 | UIEErrorReadingFile | Error reading UIR file. |
| -21 | UIEErrorWritingFile | Error writing UIR file. |
| -22 | UIEErrorClosingFile | Error closing UIR file. |
| -23 | UIEPanelStateFileHasInvalidFormat | Panel state file has invalid format. |
| -24 | UIEInvalidIDinResourceFile | Invalid panel ID or menu bar ID in resource file. |
| -25 | UIEHardCopyError | Error occurred during hardcopy output. |
| -26 | UIEInvalidDefaultDirSelectedInFSPopup | Invalid default directory specified in FileSelectPopup or FileSelectPopupEx function. |
| -27 | UIEOperationIsInvalidForSpecifiedObject | Operation is invalid for specified object. |
| -28 | UIECantFindMenuString | Unable to find specified string in menu. |
| -29 | UIECantFindMenuString | Palette menu items can only be added to the end of the menu. |
| -30 | UIEMaxNumberOfMenusPerBarExceeded | Too many menus in the menu bar. |
| -31 | UIECantSetSeparatorCheckMark | Separators cannot have checkmarks. |
| -32 | UIESeparatorCantHaveSubMenu | Separators cannot have submenus. |
| -33 | UIEItemMustBeASeparator | The menu item must be a separator. |
| -34 | UIEItemCantBeASeparator | The menu item cannot be a separator. |
| -35 | UIEItemAlreadyHasSubMenu | The menu item already has a submenu. |
| -36 | UIEItemDoesNotHaveASubMenu | The menu item does not have a submenu. |
| -37 | UIECtrlIdIsNotAMenuOrMenuItemIdOrNull | The control ID passed must be a menu ID, a menu item ID, or NULL. |
| -38 | UIECtrlIdIsNotAMenuOrMenuItemId | The control ID passed must be a menu ID, or a menu item ID. |
| -39 | UIENotASubMenuId | The control ID passed was not a submenu ID. |
| -40 | UIEInvalidMenuId | The control ID passed was not a valid ID. |
| -41 | UIENotAMenuBarHandle | The ID is not a menu bar ID. |
| -42 | UIENotAPanelHandle | The ID is not a panel ID. |
| -43 | UIEOperationInvalidWhileThisPopupIsActive | This operation cannot be performed while this pop-up panel is active. |
| -44 | UIEAttributeNotAppropriateForSpecifiedControlOrPanelOrMenu | This control/panel/menu does not have the specified attribute. |
| -45 | UIEInvalidControlType | The control type passed was not a valid type. |
| -46 | UIEInvalidAttribute | The attribute passed is invalid. |
| -47 | UIESlideMustHaveFillAboveOrBelow | The fill option must be set to fill above or fill below to paint ring slide's fill color. |
| -48 | UIEScaleMustHaveFillAboveOrBelow | The fill option must be set to fill above or fill below to paint numeric slide's fill color. |
| -49 | UIESlideMustBeLinear | The control passed is not a ring slide. |
| -50 | UIEScaleMustBeLinear | The control passed is not a numeric slide. |
| -51 | UIESlideDoesntHaveIncDecArrows | The control passed is not a ring slide with inc/dec arrows. |
| -52 | UIEScaleDoesntHaveIncDecArrows | The control passed is not a numeric slide with inc/dec arrows. |
| -53 | UIEInvalidDataType | The data type passed in is not a valid data type for the control. |
| -54 | UIEInvalidAttrForDataType | The attribute passed is not valid for the data type of the control. |
| -55 | UIEIndexOutOfRange | The index passed is out of range. |
| -56 | UIENoItemsInList | There are no items in the list control. |
| -57 | UIEBufTooSmall | The buffer passed was to small for the operation. |
| -58 | UIECtrlDoesNotHaveAValue | The control does not have a value. |
| -59 | UIEValueNotInListCtrl | The value passed is not in the list control. |
| -60 | UIENotListCtrl | The control passed must be a list control. |
| -61 | UIENotListCtrlOrBinary | The control passed must be a list control or a binary switch. |
| -62 | UIENotStringDataType | The data type of the control passed must be set to a string. |
| -63 | UIEAttributeNotSettable | That attribute is not a settable attribute. |
| -64 | UIEInvalidCtrlMode | The value passed is not a valid mode for this control. |
| -65 | UIENullPointerPassed | A NULL pointer was passed when a non-NULL pointer was expected. |
| -66 | UIECantSetGetTextBGColorOfMenuRing | The text background color on a menu ring cannot be set or gotten. |
| -67 | UIERingMustBeMenuStyle | The ring control passed must be one of the menu ring styles. |
| -68 | UIECantColorTextTransparent | Text cannot be colored transparent. |
| -69 | UIEInvalidValueInListControl | A value cannot be converted to the specified data type. |
| -70 | UIEInvalidTabbingOrderPosition | Invalid tab order position for control. |
| -71 | UIECantSetTabOrderOfAnIndicator | The tab order position of an indicator-only control cannot be set. |
| -72 | UIENotAValidNumber | Invalid number. |
| -73 | UIEPanelDoesntHaveAMenuBar | There is no menu bar installed for the panel. |
| -74 | UIENotTextBox | The control passed is not a text box. |
| -75 | UIEInvalidChartStyle | Invalid scroll mode for chart. |
| -76 | UIEInvalidImageType | Invalid image type for picture. |
| -77 | UIENotATopLevelPanelAttribute | The attribute is valid for child panels only. Some attributes of top level panels are determined by the host operating system. |
| -78 | UIEListCtrlNotInCheckMode | The list control passed is not in check mode. |
| -79 | UIEPanelDataDoesNotFitIntoPanel | The control values could not be completely loaded into the panel because the panel has changed. |
| -80 | UIEAxisRangeError | Maximum value must be greater than minimum value. |
| -81 | UIENonExistantCursor | Graph does not have that many cursors. |
| -82 | UIENotAValidPlot | Invalid plot. |
| -83 | UIEOutsidePlotArea | New cursor position is outside plot area. |
| -84 | UIEStringTooLarge | The length of the string exceeds the limit. |
| -85 | UIECallbackFuncIsWrongType | The specified callback function does not have the required prototype. |
| -86 | UIECantFindCallbackFunc | The specified callback function is not a known function. For external compilers, the UIR callbacks object file cannot be in the executable or DLL. |
| -87 | UIEZeroCursors | Graph cannot be in this mode without cursors. |
| -88 | UIEInvalidChartScaling | Invalid axis scaling mode for chart. |
| -89 | UIEFontNotInFontTable | The font passed is not in font table. |
| -90 | UIEBadAttributeValue | The attribute value passed is not valid. |
| -91 | UIETooManyFilesOpen | Too many files are open. |
| -92 | UIEfEOF | Unexpectedly reached end of file. |
| -93 | UIEIOError | Input/Output error. |
| -94 | UIEFileWasNotFound | File not found. |
| -95 | UIEAccessDenied | File access permission denied. |
| -96 | UIEFileAccessNotEnabled | File access is not enabled. |
| -97 | UIEDiskFull | Disk is full. |
| -98 | UIEFileAlreadyExists | File already exists. |
| -99 | UIEFileAlreadyOpen | File already open. |
| -100 | UIEBadPathnameMsg | Badly formed pathname. |
| -101 | UIEResourceNotFound | File is damaged. |
| -102 | UIEOldUnsupportedUIResourceFormat | The format of the resource file is too old to read. |
| -103 | UIEFileIsCorrupted | File is corrupted. |
| -104 | UIEOperationFailed | The operation could not be performed. |
| -105 | UIESlideMustBeRound | The control passed is not a ring knob, dial, or gauge. |
| -106 | UIEScaleMustBeRound | The control passed is not a numeric knob, dial, or gauge. |
| -107 | UIECountOutOfRange | The count passed is out of range. |
| -108 | UIENotAValidKeycode | The keycode is not valid. |
| -109 | UIESlideDoesntHaveFrame | The control passed is not a ring slide with a frame. |
| -110 | UIECantColorPanelBGTransparent | Panel background cannot be colored transparent. |
| -111 | UIECantColorTitleBGTransparent | Title background cannot be colored transparent. |
| -112 | UIEMemPrintError | Not enough memory for printing. |
| -113 | UIEReservedHotKey | The shortcut key passed is reserved. |
| -114 | UIEFileFormatIsTooNew | The format of the file is newer than this version of CVI. |
| -115 | UIESystemPrintError | System printing error. |
| -116 | UIEDriverPrintError | Driver printing error. |
| -117 | UIEDefCallBackQueueFull | The deferred callback queue is full. |
| -118 | UIEInvalidMouseCursor | The mouse cursor passed is invalid. |
| -119 | UIEPrintReentranceError | Printing functions are not reentrant. |
| -120 | UIEOutOfGDISpace | Out of Windows GDI space. |
| -121 | UIEHiddenPanelError | The panel must be visible. |
| -122 | UIEHiddenCtrlError | The control must be visible. |
| -123 | UIEInvalidAttrForPlot | The attribute not valid for the type of plot. |
| -124 | UIECantColorPlotTransparent | Intensity plots cannot use transparent colors. |
| -125 | UIEInvalidColor | Color is invalid. |
| -126 | UIECallbackNameIsAmbiguous | The specified callback function differs only by a leading underscore from another function or variable. Change one of the names for proper linking. |
| -127 | UIEInvalidBitmap | Bitmap is invalid. |
| -128 | UIENoImagePresent | There is no image in the control. |
| -129 | UIEMustBeInTopLevelPanelThread | The specified operation can be performed only in the thread in which the top-level panel was created. |
| -130 | UIEPanelNotInTUIFile | The specified panel was not found in the .tui file. |
| -131 | UIEMenuBarNotInTUIFile | The specified menu bar was not found in the .tui file. |
| -132 | UIECtrlStyleNotInTUIFile | The specified control style was not found in the .tui file. |
| -133 | UIETagOrValueMissingInTUIFile | A tag or value is missing in the .tui file. |
| -134 | UIESubFileReadingOrParsingError | Error reading or parsing .sub file. |
| -135 | UIENoPrintersInstalled | There are no printers installed in the system. |
| -136 | UIEInitialCellOutOfRange | The beginning cell must be in the search range. |
| -137 | UIEInvalidCellType | The cell type passed is not valid for this operation |
| -138 | UIECellTypeMismatch | Cell type or data type is mismatched. |
| -139 | UIECtrlDoesNotHaveMenu | Controls of the type passed do not have a menu. |
| -140 | UIECannotDiscardBuiltInCtrlMenuItem | Built-in control menu items cannot be discarded. |
| -141 | UIECantSetSeparatorBold | You cannot set this attribute on menu item separators. |
| -142 | UIEMustPassEventData2 | You must pass your callback function's eventData2 parameter to this function. |
| -143 | UIEActiveXError | ActiveX error. |
| -144 | UIEObjHandleDoesNotReferToActiveXCtrl | The specified object handle does not refer to an ActiveX control. |
| -145 | UIEActiveXCtrlNotRegistered | ActiveX control not registered on this computer. |
| -146 | UIEActiveXPersistenceError | ActiveX control does not support persistence. |
| -147 | UIEInvalidMenuButtonId | The id passed was not a valid menu button id. |
| -148 | UIECannotModifyBuiltInCtrlMenuItem | Cannot set or get the attributes of built-in control menu items. |
| -149 | UIEDataSocketError | DataSocket Error. |
| -150 | UIECtrlAlreadyBound | Control already has an active data binding. |
| -151 | UIECtrlNeedsActiveBinding | Control must have an active data binding. |
| -152 | UIEAttachedPanelMustBeChild | The panel to be attached must be a direct child of the panel containing the splitter control. |
| -153 | UIEItemIsAttached | Item is already attached to splitter control. |
| -154 | UIEItemIsNotAttached | Item is not attached to splitter control. |
| -155 | UIECannotSizeCtrl | Attached control cannot be sized in this direction. |
| -156 | UIECannotSelfAttach | Splitter control cannot be attached to itself. |
| -157 | UIEOperationInvalidOnMaskedBitmap | Operation cannot be performed on a bitmap with a transparency mask. |
| -158 | UIEOperationInvalidOnAlphaBitmap | Operation cannot be performed on a bitmap with an alpha channel. |
| -159 | UIEOperationRequiresMaskedBitmap | Operation can be performed only on a bitmap with a transparency mask. |
| -160 | UIEOperationRequiresAlphaBitmap | Operation can be performed only on a bitmap with an alpha channel. |
| -161 | UIENonExistantAnnotation | Graph does not have that many annotations. |
| -162 | UIEOperationInvalidOnTabPanel | Operation cannot be performed on a tab panel. |
| -163 | UIEAttrValidOnMenubarOnly | The attribute passed is only valid for menu bars. |
| -164 | UIEAttrValidOnMenuItemOnly | The attribute passed is only valid for menu items. |
| -165 | UIEAttrValidOnMenuAndSubmenusOnly | The attribute passed is only valid for menus and submenus. |
| -166 | UIEImageFeatureNotSupported | The image contains an unsupported feature and could not be loaded. |
| -167 | UIEImageCompressionSchemeNotSupported | The image compression scheme is not supported. |
| -168 | UIEActiveXCtrlNotLicensed | ActiveX control is not licensed for this operation. |
| -169 | UIEMXBFileFormatNotRecognized | MXB file format not recognized |
| -170 | UIEAttrValidOnMenuItemAndSubmenuOnly | The attribute passed is only valid for menu items and submenus |
| -171 | UIECannotAssignContextMenuItemShortcutKey | You cannot assign a shortcut key to this context menu item |
| -172 | UIECannotPauseUnlessContinuousMode | The strip chart can only be paused when the scroll mode is set to continuous |
| -173 | UIEAttrFixedPlotAreaNotEnabled | ATTR_FIXED_PLOT_AREA must be set to TRUE before setting the position of the plot area |
| -174 | UIEStaleData | Data is stale and is no longer valid. |
| -175 | UIEDataBindingNotSupportedIn64Bit | Data binding is not available in 64-bit mode. |
| -176 | UIEActiveXWrongConcurrencyModelForThread | ActiveX controls cannot be created in a thread whose concurrency model is multithread apartment (MTA). |
| -177 | UIECtrlNotOnPanelAssocWithCtrlArray | The control passed is not on the panel associated with the control array. |
| -178 | UIEInvalidAngleInMetaFont | The angle in the specified metafont is not valid. |
| -179 | UIECellCannotBeMadeActive | The specified cell cannot be made active. |
| -180 | UIEFileDialogWrongConcurrencyModel | The dialog cannot be displayed in a thread whose concurrency model is multithread apartment (MTA). |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvievent_processing_and_multithread.htm language=enus -->
## TOPIC 01018: Event Processing and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvievent_processing_and_multithread.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvievent_processing_and_multithread.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Event Processing and Multithreading

In general, LabWindows/CVI invokes user interface [callbacks](cviusing_callback_functions_to_resp.htm) in the same [thread](cvidifferent_approaches_to_multithr.htm) in which you [create](cvinewpanel.htm) the [panel](cvioperating_panels.htm) or [menu bar](cvioperating_menu_bars.htm) to which the callback [event](cvievents_overview.htm) applies. This applies to all [controls](cvioperating_controls.htm) on a panel, including [timer](cvitimer_control_overview.htm) controls. The following exceptions exist:

- DiscardCtrl invokes the control callback with the EVENT_DISCARD message. You can call DiscardCtrl in any thread.
- For the EVENT_IDLE message, LabWindows/CVI invokes the main callback in the thread in which you
call InstallMainCallback .

|  | Note Additionally, for events that are associated with a panel, you must process events in the same thread in which you create the panel. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventactivecellchange.htm language=enus -->
## TOPIC 01019: EVENT_ACTIVE_CELL_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventactivecellchange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventactivecellchange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_ACTIVE_CELL_CHANGE

#### Description

When the active cell item changes as a result of an interactive action, LabWindows/CVI generates an EVENT_ACTIVE_CELL_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the table control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Tables](cvitable_control_overview.htm)

#### Event Data Parameters

eventData1 = 0 (not used)

eventData2 = 0 (not used)

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventactivetabchange.htm language=enus -->
## TOPIC 01020: EVENT_ACTIVE_TAB_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventactivetabchange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventactivetabchange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_ACTIVE_TAB_CHANGE

#### Description

When a user selects a different tab than the currently active tab or close a tab page, LabWindows/CVI generates an EVENT_ACTIVE_TAB_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tab control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Tabs](cvitab_control_overview.htm)

#### Event Data Parameters:

eventData1 = Tab index of the tab that was previously active

eventData2 = Tab index of the tab that the user selected

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventaxisvalchange.htm language=enus -->
## TOPIC 01021: EVENT_AXIS_VAL_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventaxisvalchange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventaxisvalchange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_AXIS_VAL_CHANGE

#### Description

After a user interactively edits a graph axis value, LabWindows/CVI generates an EVENT_AXIS_VAL_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the graph control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Graphs](cvigraph_control_overview.htm)

#### Event Data Parameters

eventData1 = Axis that changed

eventData2 = Not used

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventbeginedittreecell.htm language=enus -->
## TOPIC 01022: EVENT_BEGIN_EDIT_TREE_CELL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventbeginedittreecell.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventbeginedittreecell.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_BEGIN_EDIT_TREE_CELL

#### Description

When a user edits a cell in a tree, LabWindows/CVI generates an EVENT_BEGIN_EDIT_TREE_CELL event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree control.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_BEGIN_EDIT_TREE_CELL.

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = Row of cell where event was generated

eventData2 = Column of cell where event was generated

#### LabWindows/CVI Compatibility

LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventclose.htm language=enus -->
## TOPIC 01023: EVENT_CLOSE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventclose.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventclose.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_CLOSE

#### Description

When a user executes the **Close** command from the **System** menu or clicks the Close button in the upper right corner of the panel titlebar, LabWindows/CVI generates an EVENT_CLOSE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the top-level panel.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Panels](cvioperating_panels.htm)

#### Event Data Parameters

Not used

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventcollapse.htm language=enus -->
## TOPIC 01024: EVENT_COLLAPSE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventcollapse.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventcollapse.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_COLLAPSE

#### Description

When a user collapses a tree item, LabWindows/CVI generates an EVENT_COLLAPSE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree control.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_COLLAPSE.

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

| Action | Event Data Values |
| --- | --- |
| Right-clicking and selecting Collapse All | eventData1 = VAL_ALL eventData2 = 0 |
| Right-clicking and selecting Collapse Subtree | eventData1 = VAL_DESCENDENT eventData2 = itemIndex |
| Clicking the minus sign or pressing the left arrow | eventData1 = 0 eventData2 = itemIndex |

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventcolumnsizechange.htm language=enus -->
## TOPIC 01025: EVENT_COLUMN_SIZE_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventcolumnsizechange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventcolumnsizechange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_COLUMN_SIZE_CHANGE

#### Description

When a user sizes a column interactively, LabWindows/CVI generates an 
EVENT_COLUMN_SIZE_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the table or tree control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Tables](cvitable_control_overview.htm) and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = 0

eventData2 = Index of the affected column

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventcomboboxinsert.htm language=enus -->
## TOPIC 01026: EVENT_COMBO_BOX_INSERT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventcomboboxinsert.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventcomboboxinsert.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_COMBO_BOX_INSERT

#### Description

When a user types a value that does not already exist in the text input area of a combo box cell, LabWindows/CVI generates an EVENT_COMBO_BOX_INSERT event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the table or tree control. LabWindows/CVI adds the item to the list automatically.

This event is sent to the callback function prior to inserting the new item in the list, which means that you can override this behavior by [swallowing](cviswallowing_events.htm) the event.

#### Applies To

[Tables](cvitable_control_overview.htm) and [trees](cvitree_control_events.htm)

#### Event Data Parameters

eventData1 = Row index of the affected cell

eventData2 = Column index of the affected cell

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventcommit.htm language=enus -->
## TOPIC 01027: EVENT_COMMIT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventcommit.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventcommit.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_COMMIT

#### Description

When a user actually commits to an operation, such as selecting a menu or typing in a number and pressing
<Enter>, LabWindows/CVI generates an EVENT_COMMIT event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control. LabWindows/CVI also places commit events in the [GetUserEvent queue](cviusing_getuserevent_to_respond_to.htm), unless you [swallow](cviswallowing_events.htm) the event.

#### Applies To

[Binary switches](cvibinary_switch_control_overview.htm), [color numerics](cvicolor_numeric_control_overview.htm), [command buttons](cvicommand_button_control_overview.htm), [graphs](cvigraph_control_overview.htm), [LEDs](cviled_control_overview.htm), [list boxes](cvilist_box_control_overview.htm), [menus](cvioperating_menu_bars.htm), [numeric slides](cvinumeric_slide_control_overview.htm), [numerics](cvinumeric_control_overview.htm), [picture buttons](cvipicture_button_control_overview.htm), [picture rings](cvipicture_ring_control_overview.htm), [radio buttons](cviradio_button_control_overview.htm), [ring slides](cviring_slide_control_overview.htm), [rings](cviring_control_overview.htm), [strings](cvistring_control_overview.htm), [tables](cvitable_control_overview.htm), [text boxes](cvitext_box_control_overview.htm), [text buttons](cvitext_button_control_overview.htm), [toggle buttons](cvitoggle_button_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Action | Event Data Values |
| --- | --- | --- |
| Menus (menu selection events calling the main callback) | Selecting items from a menu | eventData1 = Panel for menu selections eventData2 = callbackData for menu item (cast to an integer) |
| Tables (table events calling the control callback) | All table commit actions | eventData1 = Row of cell where event was generated. If the event affected multiple cells, such as when you sort or paste a range of cells, eventData1 is set to 0. eventData2 = Column of cell where event was generated. If the event affected multiple cells, such as when you sort or paste a range of cells, eventData2 is set to 0. |
| Trees (tree events calling the control callback) | Changing the state of a tree item | eventData1 = MARK_STATE_CHANGE eventData2 = Not used |
| Finishing label changes | eventData1 = LABEL_CHANGE eventData2 = itemIndex |  |
| Double-clicking | eventData1 = LEFT_DOUBLE_CLICK eventData2 = itemIndex |  |
| Pressing the <Enter> key | eventData1 = ENTER_KEY eventData2 = itemIndex |  |
| Clicking a column label | eventData1 = COLUMN_LABEL_CLICK eventData2 = Index of the column where the event was generated |  |
| Graphs | All graph commit actions | eventData1 = The index of the cursor or the annotation, depending on which one the user moved eventData2 = VAL_CURSOR or VAL_ANNOTATION, as appropriate to eventData1 |

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventctrlmenu.htm language=enus -->
## TOPIC 01028: EVENT_CTRL_MENU

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventctrlmenu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventctrlmenu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_CTRL_MENU

#### Description

When a user displays the context menu of a control, LabWindows/CVI generates an EVENT_CTRL_MENU event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

Send the mouse coordinates in eventData1 and eventData2 to the following functions to get the cell, ID, or index location of the mouse-click.

- GetIndexFromPoint —Use for trees. Gets the tree index, cell, and area of the tree that corresponds to a coordinate.
- GetTableCellFromPoint —Use for tables. Gets the table cell.
- GetLegendItemFromPoint —Use for graphs and strip charts. Gets the trace index or plot handle for graphs or strip charts.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_CTRL_MENU.

#### Applies To

[Graphs](cvigraph_control_overview.htm), [strip charts](cvistrip_chart_control_overview.htm), [tables](cvitable_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters:

| Action | Event Data Values |
| --- | --- |
| Right-clicking to display menu | eventData1 = Mouse vertical position eventData2 = Mouse horizontal position |
| Clicking menu key to display menu | eventData1 = VAL_INVALID_COORDINATE eventData2 = VAL_INVALID_COORDINATE |

#### LabWindows/CVI Compatibility

LabWindows/CVI 2010 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventdiscard.htm language=enus -->
## TOPIC 01029: EVENT_DISCARD

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventdiscard.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventdiscard.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_DISCARD

#### Description

When a panel or control is discarded from memory, LabWindows/CVI generates an EVENT_DISCARD event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel or control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

Not used

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventdrag.htm language=enus -->
## TOPIC 01030: EVENT_DRAG

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventdrag.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventdrag.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_DRAG

#### Description

**Tree and Tab Controls**—When a user drags a tree item or tab page, LabWindows/CVI generates an EVENT_DRAG event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

**Splitter Controls**—LabWindows/CVI generates and sends an EVENT_DRAG event at the beginning of the splitter operation.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_DRAG.

#### Applies To

[Splitters](cvisplitter_control_overview.htm), [tabs](cvitab_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Event Data Values |
| --- | --- |
| Trees and tabs | eventData1 = Not used eventData2 = itemIndex |
| Splitters | eventData1 = Vertical coordinates of the current drag line position eventData2 = Horizontal coordinates of the current drag line position |

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventdrop.htm language=enus -->
## TOPIC 01031: EVENT_DROP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventdrop.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventdrop.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_DROP

#### Description

**Tree and Tab Controls**—LabWindows/CVI generates drop events while a user drags a tree item or tab page. This event is sent to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control when the potential drop location changes. The purpose of the event is to allow or disallow the item to be dropped to the new location.

**Splitter Controls**—LabWindows/CVI generates and sends drop events during the splitter operation.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_DROP. If you swallow EVENT_DROP for splitter control events, the drag line will not move and attached items will not be sized for that particular incremental movement of the mouse cursor. If you alternate between swallowing and not swallowing this event during an operation, the first time you do not swallow the event negates the previous iterations when you did swallow the event. When EVENT_DROP is swallowed, the cursor changes from the default cursor to the "not allowed" cursor [IMAGE alt='image' src='../notallwd.gif']. The "not allowed" cursor remains visible until a subsequent EVENT_DROP is not swallowed or the sizing operation stops.

#### Applies To

[Splitters](cvisplitter_control_overview.htm), [tabs](cvitab_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Event Data Values |
| --- | --- |
| Trees | eventData1 = Position and relation. The eventData1 parameter contains both the new potential position and relation of the dragged item. The position and relation values are relative to the tree item at the index contained in eventData2. Position defines whether the item will be inserted before or after the tree item. The low order word contains the relation and will either be VAL_CHILD or VAL_SIBLING. The high order word contains the position and will either be VAL_PREV, VAL_NEXT, or VAL_FIRST. eventData2 = relativeIndex. relativeIndex is the index of the relative of the new potential drop location. |
| Tabs | eventData1 = Not used. eventData2 = destinationIndex. destinationIndex is the index of the new drop location. |
| Splitters | eventData1 = Vertical coordinates of the current drag line position. eventData2 = Horizontal coordinates of the current drag line position. |

##### Example Code

int CVICALLBACK TreeCallback (int panel, int control, int event, void *callbackData, int eventData1, int eventData2)

{

int retval = 0; 

 int relation, position; 
 

 
 switch (event) 

 { 

 case EVENT_DROP:

relation = LoWord(eventData1); 

 position = HiWord(eventData1); 

 if (VAL_CHILD == relation) 

    retval = 1; /* disallow dropping as a child */ 

 break;

} 
 

 return retval;

}

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventdropcopy.htm language=enus -->
## TOPIC 01032: EVENT_DROP_COPY

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventdropcopy.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventdropcopy.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_DROP_COPY

#### Description

As a user copies a tree item by dragging and dropping the tree item to a new location in the tree control, LabWindows/CVI generates an EVENT_DROP_COPY and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_DROP_COPY.

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = Position and relation. The **eventData1** parameter contains both the new potential position and relation of the dragged item. The position and relation values are relative to the tree item at the index contained in **eventData2**. Position defines whether the item will be inserted before or after the tree item. The low order word contains the relation and will either be VAL_CHILD or VAL_SIBLING. The high order word contains the position and will either be VAL_PREV, VAL_NEXT, or VAL_FIRST.

eventData2 = destinationIndex. destinationIndex is the index of the new drop location.

#### LabWindows/CVI Compatibility

LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventdropped.htm language=enus -->
## TOPIC 01033: EVENT_DROPPED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventdropped.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventdropped.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_DROPPED

#### Description

**Tree and Tab Controls**—After a user drops a tree item or tab page, LabWindows/CVI generates an EVENT_DROPPED event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

**Splitter Controls**—At the end of the splitter operation, LabWindows/CVI generates an EVENT_DROPPED event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Splitters](cvisplitter_control_overview.htm), [tabs](cvitab_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Event Data Values |
| --- | --- |
| Trees and tabs | eventData1 = Not used eventData2 = itemIndex |
| Splitters | eventData1 = Vertical coordinates of the current drag line position eventData2 = Horizontal coordinates of the current drag line position |

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventeditmodestatechange.htm language=enus -->
## TOPIC 01034: EVENT_EDIT_MODE_STATE_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventeditmodestatechange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventeditmodestatechange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_EDIT_MODE_STATE_CHANGE

#### Description

When a tree control or a table cell enters or leaves edit mode, LabWindows/CVI generates an EVENT_EDIT_MODE_STATE_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Tables](cvitable_control_overview.htm) and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Event Data Values |
| --- | --- |
| Trees | eventData1 = TRUE if entering edit mode; FALSE if leaving edit mode eventData2 = The item being edited |
| Tables | eventData1 = TRUE if entering edit mode; FALSE if leaving edit mode eventData2 = Not used |

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventendtask.htm language=enus -->
## TOPIC 01035: EVENT_END_TASK

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventendtask.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventendtask.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_END_TASK

#### Description

When a user tries to shut down Windows or tries to terminate the application, LabWindows/CVI generates an EVENT_END_TASK event and sends the event to the main [callback function](cviusing_callback_functions_to_resp.htm). [Swallow](cviswallowing_events.htm) the event to abort the termination.

#### Applies To

None.

#### Event Data Parameters

| Action | Event Data Values |
| --- | --- |
| Closing the application | eventData1 = APP_CLOSE (0) eventData2 = Not used |
| Shutting down the computer | eventData1 = SYSTEM_CLOSE (1) eventData2 = Not used |

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventexpand.htm language=enus -->
## TOPIC 01036: EVENT_EXPAND

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventexpand.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventexpand.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_EXPAND

#### Description

When a user expands a tree item, LabWindows/CVI generates an EVENT_EXPAND event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree control.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_EXPAND.

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

| Action | Event Data Values |
| --- | --- |
| Right-clicking and selecting Expand All | eventData1 = VAL_ALL eventData2 = 0 |
| Right-clicking and selecting Expand Subtree | eventData1 = VAL_DESCENDENT eventData2 = itemIndex |
| Clicking the plus sign or pressing the right arrow | eventData1 = 0 eventData2 = itemIndex |

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventgotfocus.htm language=enus -->
## TOPIC 01037: EVENT_GOT_FOCUS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventgotfocus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventgotfocus.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_GOT_FOCUS

#### Description

If a control is not the active control (does not have the input focus), actions such as clicking the control or pressing <Tab> or <Shift-Tab> can make it the active control. When a control receives the input focus, LabWindows/CVI generates an EVENT_GOT_FOCUS event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control or panel.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[ActiveX controls](cviactivex_control_overview.htm), [binary switches](cvibinary_switch_control_overview.htm), [canvases](cvicanvas_control_overview.htm), [color numerics](cvicolor_numeric_control_overview.htm), [command buttons](cvicommand_button_control_overview.htm), [graphs](cvigraph_control_overview.htm), [LEDs](cviled_control_overview.htm), [list boxes](cvilist_box_control_overview.htm), [numeric slides](cvinumeric_slide_control_overview.htm), [numerics](cvinumeric_control_overview.htm), [panels](cvioperating_panels.htm), [picture buttons](cvipicture_button_control_overview.htm), [picture rings](cvipicture_ring_control_overview.htm), [radio buttons](cviradio_button_control_overview.htm), [ring slides](cviring_slide_control_overview.htm), [rings](cviring_control_overview.htm), [splitters](cvisplitter_control_overview.htm), [strings](cvistring_control_overview.htm), [tables](cvitable_control_overview.htm), [tabs](cvitab_control_overview.htm), [text boxes](cvitext_box_control_overview.htm), [text buttons](cvitext_button_control_overview.htm), [toggle buttons](cvitoggle_button_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = Old control with focus

eventData2 = 0

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventhscroll.htm language=enus -->
## TOPIC 01038: EVENT_HSCROLL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventhscroll.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventhscroll.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_HSCROLL

#### Description

**Panels and Strip Chart, Text Box, Table, and Tree Controls**—When a user scrolls a panel or strip chart, text box, table, or tree control horizontally, LabWindows/CVI generates an EVENT_HSCROLL event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel or control.

**Tab Controls**—When a user scrolls through the tab control, LabWindows/CVI generates an EVENT_HSCROLL event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tab control.

This event is [swallowable](cviswallowing_events.htm) for tab controls. Return 1 to swallow EVENT_HSCROLL.

#### Applies To

[Panels](cvioperating_panels.htm), [strip charts](cvistrip_chart_control_overview.htm), [tables](cvitable_control_overview.htm), [tabs](cvitab_control_overview.htm), [text boxes](cvitext_box_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Event Data Values |
| --- | --- |
| Panels, strip charts, text boxes, tables, and tree controls | eventData1 = oldScrollOffset, in pixels eventData2 = newScrollOffset, in pixels |
| Tabs | eventData1 = oldFirstIndex eventData2 = newFirstIndex |

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventidle.htm language=enus -->
## TOPIC 01039: EVENT_IDLE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventidle.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventidle.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_IDLE

#### Description

|  | Note This event is obsolete; National Instruments recommends that you use timer controls instead. |
| --- | --- |

Idle events are sent to the main [callback function](cviusing_callback_functions_to_resp.htm) on a regular basis, as long as LabWindows/CVI [processes events](cviprocessing_events.htm). You can set the rate at which idle events occur using [SetIdleEventRate](cvisetidleeventrate.htm).

#### Applies To

None.

#### Event Data Parameters

Not used.

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventinteractivelegend.htm language=enus -->
## TOPIC 01040: EVENT_INTERACTIVE_LEGEND

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventinteractivelegend.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventinteractivelegend.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_INTERACTIVE_LEGEND

#### Description

When a user right-clicks the graph or strip chart legend and selects an item from the interactive legend menu, LabWindows/CVI generates an EVENT_INTERACTIVE_LEGEND event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Graphs](cvigraph_control_overview.htm) and [strip charts](cvistrip_chart_control_overview.htm)

#### Event Data Parameters

eventData1 = The plot ID for graphs or the trace index for strip charts

|  | Note Although trace indices for strip charts are 1-based, the values for trace indices returned by eventData1 are 0-based. For example, for an event that refers to trace 3, the value returned by eventData1 is 2. For backwards-compatibility purposes, National Instruments is not correcting this behavior. |
| --- | --- |

eventData2 = The menu item that the user selects, such as VAL_PLOT_COLOR, VAL_PLOT_STYLE, and so on

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventkeypress.htm language=enus -->
## TOPIC 01041: EVENT_KEYPRESS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventkeypress.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventkeypress.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_KEYPRESS

#### Description

When a user presses a key on the keyboard, LabWindows/CVI generates an EVENT_KEYPRESS event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control that has the input focus and to the callback function associated with the control’s panel. If you [swallow](cviswallowing_events.htm) the event, LabWindows/CVI does not continue processing the event.

For ANSI panels, if a user enters a [dual-byte character](../programmerref/programmingmultibytechars.htm) in a control, two EVENT_KEYPRESS events are sent to the callback function. To process the character as a single event, ignore the first event. You can use [KeyPressEventIsLeadByte](cvikeypresseventisleadbyte.htm) to determine when you receive the first event of a dual-byte character. When you receive the second event, [KeyPressEventIsTrailByte](cvikeypresseventistrailbyte.htm) returns TRUE. You can then use [GetKeyPressEventCharacter](cvigetkeypresseventcharacter.htm) to obtain the full dual-byte character. Additionally, you can use [SetKeyPressEventKey](cvisetkeypresseventkey.htm) to change the character that the user entered. Do not use SetKeyPressEventKey in the first EVENT_KEYPRESS event of a dual-byte character.

For UTF-8 panels, a single EVENT_KEYPRESS event is sent to the callback function per character. Both [KeyPressEventIsLeadByte](cvikeypresseventisleadbyte.htm) and [KeyPressEventIsTrailByte](cvikeypresseventistrailbyte.htm) functions return FALSE. You can use [GetKeyPressEventCharacter](cvigetkeypresseventcharacter.htm) to obtain the UTF-8 character. Additionally, you can use [SetKeyPressEventKey](cvisetkeypresseventkey.htm) to change the character that the user entered.

|  | Note UTF-8 panels are only compatible with LabWindows/CVI 2020 and later. |
| --- | --- |

#### Applies To

[ActiveX controls](cviactivex_control_overview.htm), [binary switches](cvibinary_switch_control_overview.htm), [canvases](cvicanvas_control_overview.htm), [color numerics](cvicolor_numeric_control_overview.htm), [command buttons](cvicommand_button_control_overview.htm), [graphs](cvigraph_control_overview.htm), [LEDs](cviled_control_overview.htm), [list boxes](cvilist_box_control_overview.htm), [numeric slides](cvinumeric_slide_control_overview.htm), [numerics](cvinumeric_control_overview.htm), [panels](cvioperating_panels.htm), [picture buttons](cvipicture_button_control_overview.htm), [picture rings](cvipicture_ring_control_overview.htm), [radio buttons](cviradio_button_control_overview.htm), [ring slides](cviring_slide_control_overview.htm), [rings](cviring_control_overview.htm), [splitters](cvisplitter_control_overview.htm), [strings](cvistring_control_overview.htm), [tables](cvitable_control_overview.htm), [tabs](cvitab_control_overview.htm), [text boxes](cvitext_box_control_overview.htm), [text buttons](cvitext_button_control_overview.htm), [toggle buttons](cvitoggle_button_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = [key code](#keycode)

|  | Note For UTF-8 panels, the key code returned in eventData1 is a Unicode key code. This Unicode key code is packed, and you must unpack it using the UnpackKeyCodeUnicode function. |
| --- | --- |

eventData2 = Value to pass to the following functions: [KeyPressEventIsLeadByte](cvikeypresseventisleadbyte.htm), [KeyPressEventIsTrailByte](cvikeypresseventistrailbyte.htm), [GetKeyPressEventVirtualKey](cvigetkeypresseventvirtualkey.htm), [GetKeyPressEventCharacter](cvigetkeypresseventcharacter.htm), [GetKeyPressEventModifiers](cvigetkeypresseventmodifiers.htm), and [SetKeyPressEventKey](cvisetkeypresseventkey.htm).

Refer to the KeyCallback function in the samples\userint\multikey.cws sample program for an example of a callback that uses these functions.

#### Key Codes

For ANSI panels, key codes are formed by a logical OR operation on values representing a modifier key and either an ASCII character or a virtual key.

ASCII characters can be represented by a literal character, for example, 'A' or 'D', or an ASCII value. There is no distinction between upper and lower case ASCII characters.

For UTF-8 panels, key codes are Unicode key codes. Unicode key codes are formed by packing a Unicode code point, virtual key, and modifier. You must unpack Unicode key codes into the individual values representing these three elements using the [UnpackKeyCodeUnicode](../libref/cviunpackkeycodeunicode.htm) function.

The Unicode code point can represent any character.

A modifier key is a <Shift> key, <Alt> key, or menu modifier key (<Ctrl> key). The following constants represent the modifier key.

VAL_SHIFT_MODIFIER = 0x010000 

VAL_UNDERLINE_MODIFIER = 0x020000 

VAL_MENUKEY_MODIFIER = 0x040000 

VAL_SHIFT_AND_MENUKEY = 0x050000

Virtual keys are non-ASCII keys represented by the following key codes:

VAL_FWD_DELETE_VKEY = 0x0100 

 VAL_BACKSPACE_VKEY = 0x0200 

 VAL_ESC_VKEY = 0x0300 
 
 VAL_TAB_VKEY = 0x0400 
 
 VAL_ENTER_VKEY = 0x0500 
 
 VAL_UP_ARROW_VKEY = 0x0600 

 VAL_DOWN_ARROW_VKEY = 0x0700 

 VAL_LEFT_ARROW_VKEY = 0x0800 

 VAL_RIGHT_ARROW_VKEY = 0x0900 

 VAL_INSERT_VKEY = 0x0A00 

 VAL_HOME_VKEY = 0x0B00 

 VAL_END_VKEY = 0x0C00 

 VAL_PAGE_UP_VKEY = 0x0D00 

 VAL_PAGE_DOWN_VKEY = 0x0E00 

 VAL_F1_VKEY = 0x0F00 

 VAL_F2_VKEY = 0x1000 

 VAL_F3_VKEY = 0x1100 

 VAL_F4_VKEY = 0x1200 

 VAL_F5_VKEY = 0x1300 

 VAL_F6_VKEY = 0x1400 

 VAL_F7_VKEY = 0x1500 

 VAL_F8_VKEY = 0x1600 

 VAL_F9_VKEY = 0x1700 

 VAL_F10_VKEY = 0x1800 

 VAL_F11_VKEY = 0x1900 

 VAL_F12_VKEY = 0x1A00

You cannot use ASCII with a virtual key code. You can use virtual key codes with or without a modifier, and you can use the shift and menu modifier keys together. For example, the expression VAL_MENUKEY_MODIFIER | 'A' specifies <Ctrl-A>. Other valid key codes include the following:

VAL_TAB_VKEY 

VAL_SHIFT_MODIFIER | VAL_F5_VKEY

The result of the logical OR operation is a 4-byte integer consisting of three bit fields, 0x00MMVVAA, where

MM = the modifier key 

 VV = the virtual key 

 AA = the ASCII key

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventleftclick.htm language=enus -->
## TOPIC 01042: EVENT_LEFT_CLICK

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventleftclick.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventleftclick.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_LEFT_CLICK

#### Description

When a user clicks with the left mouse button anywhere or on a panel, LabWindows/CVI generates an EVENT_LEFT_CLICK event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel, as well as to the callback function associated with the control over which the mouse click took place.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_LEFT_CLICK.

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

eventData1 = Mouse vertical position

eventData2 = Mouse horizontal position

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventleftclickup.htm language=enus -->
## TOPIC 01043: EVENT_LEFT_CLICK_UP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventleftclickup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventleftclickup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_LEFT_CLICK_UP

#### Description

When a user releases the left mouse button over a control or panel, LabWindows/CVI generates an EVENT_LEFT_CLICK_UP event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control or panel.

This event is not [swallowable](cviswallowing_events.htm).

|  | Note If a user releases the left mouse button outside of a LabWindows/CVI panel, this event is not generated. If you need this information, you can use extended mouse events. |
| --- | --- |

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

eventData1 = Mouse vertical position

eventData2 = Mouse horizontal position

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventleftdoubleclick.htm language=enus -->
## TOPIC 01044: EVENT_LEFT_DOUBLE_CLICK

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventleftdoubleclick.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventleftdoubleclick.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_LEFT_DOUBLE_CLICK

#### Description

When a user double-clicks with the left mouse button anywhere or a panel, LabWindows/CVI generates an EVENT_LEFT_DOUBLE_CLICK event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel, as well as to the callback function associated with the control over which the mouse click took place.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_LEFT_DOUBLE_CLICK.

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

eventData1 = Mouse vertical position

eventData2 = Mouse horizontal position

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventlostfocus.htm language=enus -->
## TOPIC 01045: EVENT_LOST_FOCUS

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventlostfocus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventlostfocus.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_LOST_FOCUS

#### Description

If a control is the active control (has the input focus), actions such as clicking a different control or a different panel or pressing <Tab> or <Shift-Tab> change only the active panel. The previous panel will receive the EVENT_LOST_FOCUS event, but the control on that panel will not. When a control loses the input focus, LabWindows/CVI generates an EVENT_LOST_FOCUS event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel or control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[ActiveX controls](cviactivex_control_overview.htm), [binary switches](cvibinary_switch_control_overview.htm), [canvases](cvicanvas_control_overview.htm), [color numerics](cvicolor_numeric_control_overview.htm), [command buttons](cvicommand_button_control_overview.htm), [graphs](cvigraph_control_overview.htm), [LEDs](cviled_control_overview.htm), [list boxes](cvilist_box_control_overview.htm), [numeric slides](cvinumeric_slide_control_overview.htm), [numerics](cvinumeric_control_overview.htm), [panels](cvioperating_panels.htm), [picture buttons](cvipicture_button_control_overview.htm), [picture rings](cvipicture_ring_control_overview.htm), [radio buttons](cviradio_button_control_overview.htm), [ring slides](cviring_slide_control_overview.htm), [rings](cviring_control_overview.htm), [splitters](cvisplitter_control_overview.htm), [strings](cvistring_control_overview.htm), [tables](cvitable_control_overview.htm), [tabs](cvitab_control_overview.htm), [text boxes](cvitext_box_control_overview.htm), [text buttons](cvitext_button_control_overview.htm), [toggle buttons](cvitoggle_button_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = New control with focus

eventData2 = 0

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventmarkstatechange.htm language=enus -->
## TOPIC 01046: EVENT_MARK_STATE_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventmarkstatechange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventmarkstatechange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_MARK_STATE_CHANGE

#### Description

Mark state change events are sent to the callback function When the check state changes for a list box item or tree item, LabWindows/CVI generates an EVENT_MARK_STATE_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

For list box controls, this event is [swallowable](cviswallowing_events.htm) if you set ATTR_DRAGGABLE_MARKS to on. This event is not swallowable if you set ATTR_DRAGGABLE_MARKS to off.

For tree controls, any mark state event that is generated as a result of a [mark reflect change](cviattrmarkreflect.htm) is not swallowable.

Return 1 to swallow EVENT_MARK_STATE_CHANGE.

For tree items with radio buttons, the event that is swallowable is the event that is generated when you select an item. If, when you select an item, another item becomes deselected as a result, then that event is not swallowable.

#### Applies To

[List boxes](cvilist_box_control_overview.htm) and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = The new mark state of the list item

eventData2 = itemIndex of the item whose mark state is being changed

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventmousepointermove.htm language=enus -->
## TOPIC 01047: EVENT_MOUSE_POINTER_MOVE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventmousepointermove.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventmousepointermove.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_MOUSE_POINTER_MOVE

#### Description

When a user moves the mouse over a control or panel, LabWindows/CVI generates an EVENT_MOUSE_POINTER_MOVE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control or panel.

This event is not [swallowable](cviswallowing_events.htm).

|  | Note This event does not appear in the upper right corner of the User Interface Editor in operate mode. |
| --- | --- |

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

eventData1 = Mouse vertical position

eventData2 = Mouse horizontal position

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventmousewheelscroll.htm language=enus -->
## TOPIC 01048: EVENT_MOUSE_WHEEL_SCROLL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventmousewheelscroll.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventmousewheelscroll.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_MOUSE_WHEEL_SCROLL

#### Description

When a user scrolls the mouse wheel, LabWindows/CVI generates an EVENT_MOUSE_WHEEL_SCROLL event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control that has the input focus or panel.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_MOUSE_WHEEL_SCROLL.

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

eventData1 = The scroll action (MOUSE_WHEEL_SCROLL_UP, 
MOUSE_WHEEL_SCROLL_DOWN, MOUSE_WHEEL_PAGE_UP, 
MOUSE_WHEEL_PAGE_DOWN, MOUSE_WHEEL_SCROLL_LEFT, or MOUSE_WHEEL_SCROLL_RIGHT)

eventData2 = 0 if eventData1 is MOUSE_WHEEL_PAGE_UP or MOUSE_WHEEL_PAGE_DOWN. If eventData1 is MOUSE_WHEEL_SCROLL_UP, MOUSE_WHEEL_SCROLL_DOWN, MOUSE_WHEEL_SCROLL_LEFT, or MOUSE_WHEEL_SCROLL_RIGHT eventData2 is the amount to scroll, such as the number of lines the user scrolled

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventpanelmaximize.htm language=enus -->
## TOPIC 01049: EVENT_PANEL_MAXIMIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventpanelmaximize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventpanelmaximize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_PANEL_MAXIMIZE

#### Description

When a user maximizes the panel, LabWindows/CVI generates an EVENT_PANEL_MAXIMIZE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel.

This event is not [swallowable](cviswallowing_events.htm).

|  | Note When you click a panel's button on the taskbar to minimize the panel, the window is minimized and the EVENT_PANEL_MINIMIZE event is sent. This is equivalent to clicking the minimize button in the upper right corner. However, when you minimize by clicking the application's button on the taskbar, the entire application is minimized which causes all its windows to disappear. The individual windows have not been minimized by this action and an EVENT_PANEL_MINIMIZE event is not sent. |
| --- | --- |

#### Applies To

[Panels](cvioperating_panels.htm)

#### Event Data Parameters

eventData1 = 0 (not used)

eventData2 = 0 (not used)

#### LabWindows/CVI Compatibility

LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventpanelminimize.htm language=enus -->
## TOPIC 01050: EVENT_PANEL_MINIMIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventpanelminimize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventpanelminimize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_PANEL_MINIMIZE

#### Description

When a user minimizes the panel to the taskbar, LabWindows/CVI generates an EVENT_PANEL_MINIMIZE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel.

This event is not [swallowable](cviswallowing_events.htm).

|  | Note When you click a panel's button on the taskbar to minimize the panel, the window is minimized and the event is sent. This is equivalent to clicking the minimize button in the upper right corner. However, when you minimize by clicking the application's button on the taskbar, the entire application is minimized which causes all its windows to disappear. The individual windows have not been minimized by this action and an event is not sent. |
| --- | --- |

#### Applies To

[Panels](cvioperating_panels.htm)

#### Event Data Parameters

eventData1 = 0 (not used)

eventData2 = 0 (not used)

#### LabWindows/CVI Compatibility

LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventpanelmove.htm language=enus -->
## TOPIC 01051: EVENT_PANEL_MOVE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventpanelmove.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventpanelmove.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_PANEL_MOVE

#### Description

After a user or program moves a panel, LabWindows/CVI generates an EVENT_PANEL_MOVE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel. The [EVENT_PANEL_MOVING](cvieventpanelmoving.htm) event is generated as the user or program moves the panel.

(Linux) For parent panels, LabWindows/CVI continuously generates EVENT_PANEL_MOVE events instead of EVENT_PANEL_MOVING events as the user or program moves the panel.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Panels](cvioperating_panels.htm)

#### Event Data Parameters:

Not used.

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventpanelmoving.htm language=enus -->
## TOPIC 01052: EVENT_PANEL_MOVING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventpanelmoving.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventpanelmoving.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_PANEL_MOVING

#### Description

As a user or program moves a panel, LabWindows/CVI generates an EVENT_PANEL_MOVING event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel.

This event is not [swallowable](cviswallowing_events.htm); however, you can use eventData2 to restrict the size or position of the panel.

|  | Note Consider the following caveats when using this event: For all panels on Windows and for child panels on Linux, the EVENT_PANEL_MOVE event is generated after the user or program has moved the panel, and the EVENT_PANEL_MOVING event is generated as the user or progam moves the panel. (Linux) For parent panels, LabWindows/CVI continuously generates EVENT_PANEL_MOVE events instead of EVENT_PANEL_MOVING events as the user or program moves the panel. LabWindows/CVI does not generate EVENT_PANEL_MOVING events for parent panels. The GetPanelEventRect function returns the panel bounds that includes the titlebar and frame. GetPanelAttribute and SetPanelAttribute with ATTR_TOP, ATTR_LEFT, ATTR_HEIGHT, and ATTR_WIDTH refer to the panel bounds not including the titlebar and frame. Use the panel attributes ATTR_TITLEBAR_ACTUAL_THICKNESS, ATTR_FRAME_ACTUAL_WIDTH, and ATTR_FRAME_ACTUAL_HEIGHT to go from one bounding rectangle to the other. |
| --- | --- |

#### Applies To

[Panels](cvioperating_panels.htm)

#### Event Data Parameters

eventData1 = Not used.

eventData2 = Value that the user passes into [GetPanelEventRect](cvigetpaneleventrect.htm) to extract a Rect structure containing the new size and position of the panel. Call [SetPanelEventRect](cvisetpaneleventrect.htm) on eventData2 to force the panel to a different size or position.

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventpanelrestore.htm language=enus -->
## TOPIC 01053: EVENT_PANEL_RESTORE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventpanelrestore.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventpanelrestore.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_PANEL_RESTORE

#### Description

When a user returns the panel to its original size, LabWindows/CVI generates an EVENT_PANEL_RESTORE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel.

This event is not [swallowable](cviswallowing_events.htm).

|  | Note When you click a panel's button on the taskbar to minimize the panel, the window is minimized and the EVENT_PANEL_MINIMIZE event is sent. This is equivalent to clicking the minimize button in the upper right corner. However, when you minimize by clicking the application's button on the taskbar, the entire application is minimized which causes all its windows to disappear. The individual windows have not been minimized by this action and an an EVENT_PANEL_MINIMIZE event is not sent. |
| --- | --- |

#### Applies To

[Panels](cvioperating_panels.htm)

#### Event Data Parameters

eventData1 = 0 (not used)

eventData2 = 0 (not used)

#### LabWindows/CVI Compatibility

LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventpanelsize.htm language=enus -->
## TOPIC 01054: EVENT_PANEL_SIZE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventpanelsize.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventpanelsize.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_PANEL_SIZE

#### Description

After a user or program changes the size of a panel, LabWindows/CVI generates an EVENT_PANEL_SIZE event and sends the event to the 
[callback function](cviusing_callback_functions_to_resp.htm) associated with the panel. The [EVENT_PANEL_SIZING](cvieventpanelsize.htm) event is generated as the user or program resizes the panel.

(Linux) For parent panels, LabWindows/CVI continuously generates EVENT_PANEL_SIZE events instead of EVENT_PANEL_SIZING events as the user or program resizes the panel.

|  | Note If ATTR_DISABLE_PROG_PANEL_SIZE_EVENTS is set to true, you cannot programmatically change the size of a panel. |
| --- | --- |

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Panels](cvioperating_panels.htm)

#### Event Data Parameters

Not used.

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventpanelsizing.htm language=enus -->
## TOPIC 01055: EVENT_PANEL_SIZING

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventpanelsizing.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventpanelsizing.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_PANEL_SIZING

#### Description

As a user or program sizes a panel, LabWindows/CVI generates an EVENT_PANEL_SIZING event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel.

This event is not [swallowable](cviswallowing_events.htm); however, you can use eventData2 to restrict the size or position of the panel.

|  | Note Consider the following caveats when using this event: For all panels on Windows and for child panels on Linux, the EVENT_PANEL_SIZE event is generated after the user or program has resized the panel, and the EVENT_PANEL_SIZING event is generated as the user or program resizes the panel. (Linux) For parent panels, LabWindows/CVI continuously generates EVENT_PANEL_SIZE events instead of EVENT_PANEL_SIZING events as the user or program resizes the panel. LabWindows/CVI does not generate EVENT_PANEL_SIZING events for parent panels. The GetPanelEventRect function returns the panel bounds that includes the titlebar and frame. GetPanelAttribute and SetPanelAttribute with ATTR_TOP, ATTR_LEFT, ATTR_HEIGHT, and ATTR_WIDTH refer to the panel bounds not including the titlebar and frame. Use the panel attributes ATTR_TITLEBAR_ACTUAL_THICKNESS, ATTR_FRAME_ACTUAL_WIDTH, and ATTR_FRAME_ACTUAL_HEIGHT to go from one bounding rectangle to the other. |
| --- | --- |

#### Applies To

[Panels](cvioperating_panels.htm)

#### Event Data Parameters

eventData1 = The edge of the panel that the user is sizing, such as PANEL_SIZING_TOPLEFT, 
PANEL_SIZING_TOP, PANEL_SIZING_BOTTOM, and so on.

eventData2 = Value that the user passes into [GetPanelEventRect](cvigetpaneleventrect.htm) to extract a Rect structure containing the new size and position of the panel. Call [SetPanelEventRect](cvisetpaneleventrect.htm) on eventData2 to force the panel to a different size or position.

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventradixchange.htm language=enus -->
## TOPIC 01056: EVENT_RADIX_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventradixchange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventradixchange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_RADIX_CHANGE

#### Description

When a user changes the format of the radix, LabWindows/CVI generates an EVENT_RADIX_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Numeric slides](cvinumeric_slide_control_overview.htm) and [numerics](cvinumeric_control_overview.htm)

#### Event Data Parameters

eventData1 = The new format of the radix (VAL_DECIMAL_FORMAT, 
VAL_HEX_FORMAT, VAL_OCTAL_FORMAT, or 
VAL_BINARY_FORMAT)

eventData2 = Not used

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventrightclick.htm language=enus -->
## TOPIC 01057: EVENT_RIGHT_CLICK

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventrightclick.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventrightclick.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_RIGHT_CLICK

#### Description

When a user clicks with the right mouse button anywhere or on a panel, LabWindows/CVI generates an EVENT_RIGHT_CLICK event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel, as well as to the callback function associated with the control over which the mouse click took place.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_RIGHT_CLICK.

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

eventData1 = Mouse vertical position

eventData2 = Mouse horizontal position

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventrightclickup.htm language=enus -->
## TOPIC 01058: EVENT_RIGHT_CLICK_UP

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventrightclickup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventrightclickup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_RIGHT_CLICK_UP

#### Description

When a user releases the right mouse button over a control or panel, LabWindows/CVI generates an EVENT_RIGHT_CLICK_UP event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control or panel.

This event is not [swallowable](cviswallowing_events.htm).

|  | Note If a user releases the right mouse button outside of a LabWindows/CVI panel, this event is not generated. If you need this information, you can use extended mouse events. |
| --- | --- |

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

eventData1 = Mouse vertical position

eventData2 = Mouse horizontal position

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventrightdoubleclick.htm language=enus -->
## TOPIC 01059: EVENT_RIGHT_DOUBLE_CLICK

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventrightdoubleclick.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventrightdoubleclick.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_RIGHT_DOUBLE_CLICK

#### Description

When a user double-clicks with the right mouse button anywhere or a panel, LabWindows/CVI generates an EVENT_RIGHT_DOUBLE_CLICK event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel, as well as to the callback function associated with the control over which the mouse click took place.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_RIGHT_DOUBLE_CLICK.

#### Applies To

[Panels](cvioperating_panels.htm) and all [control](cvioperating_controls.htm) types

#### Event Data Parameters

eventData1 = Mouse vertical position

eventData2 = Mouse horizontal position

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventringbeginmenu.htm language=enus -->
## TOPIC 01060: EVENT_RING_BEGIN_MENU

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventringbeginmenu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventringbeginmenu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_RING_BEGIN_MENU

#### Description

When a user displays the menu of a ring control, LabWindows/CVI generates an EVENT_RING_BEGIN_MENU event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the ring control.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_RING_BEGIN_MENU.

#### Applies To

[Rings](cviring_control_overview.htm)

#### Event Data Parameters

Not used

#### LabWindows/CVI Compatibility

LabWindows/CVI 2013 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventrowsizechange.htm language=enus -->
## TOPIC 01061: EVENT_ROW_SIZE_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventrowsizechange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventrowsizechange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_ROW_SIZE_CHANGE

#### Description

When a user sizes a row interactively, LabWindows/CVI generates an EVENT_ROW_SIZE_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the table control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Tables](cvitable_control_overview.htm)

#### Event Data Parameters

eventData1 = Index of the affected row

eventData2 = 0

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvievents_overview.htm language=enus -->
## TOPIC 01062: Events Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvievents_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvievents_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Events Overview

Certain user operations on the GUI, such as selecting a [menu](cvioperating_menu_bars.htm) item on the GUI or typing a value in a [control](cvioperating_controls.htm), are called *events*. The User Interface Library provides the link between events and the code files in your project.

By implementing event [callback functions](cviusing_callback_functions_to_resp.htm), your program can recognize events and execute the code in response to them. The following table shows all of the events that are generated from the GUI.

#### Events

- EVENT_ACTIVE_CELL_CHANGE
- EVENT_ACTIVE_TAB_CHANGE
- EVENT_AXIS_VAL_CHANGE
- EVENT_BEGIN_EDIT_TREE_CELL
- EVENT_CLOSE
- EVENT_COLLAPSE
- EVENT_COLUMN_SIZE_CHANGE
- EVENT_COMBO_BOX_INSERT
- EVENT_COMMIT
- EVENT_CTRL_MENU
- EVENT_DISCARD
- EVENT_DRAG
- EVENT_DROP
- EVENT_DROPPED
- EVENT_DROP_COPY
- EVENT_EDIT_MODE_STATE_CHANGE
- EVENT_END_TASK
- EVENT_EXPAND
- EVENT_GOT_FOCUS
- EVENT_HSCROLL
- EVENT_IDLE
- EVENT_INTERACTIVE_LEGEND
- EVENT_KEYPRESS
- EVENT_LEFT_CLICK
- EVENT_LEFT_CLICK_UP
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_LOST_FOCUS
- EVENT_MARK_STATE_CHANGE
- EVENT_MOUSE_POINTER_MOVE
- EVENT_MOUSE_WHEEL_CLICK
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_PANEL_MAXIMIZE
- EVENT_PANEL_MINIMIZE
- EVENT_PANEL_MOVE
- EVENT_PANEL_MOVING
- EVENT_PANEL_RESTORE
- EVENT_PANEL_SIZE
- EVENT_PANEL_SIZING
- EVENT_RADIX_CHANGE
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_CLICK_UP
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_RING_BEGIN_MENU
- EVENT_ROW_SIZE_CHANGE
- EVENT_SELECTION_CHANGE
- EVENT_SORT
- EVENT_TABLE_ROW_COL_LABEL_CLICK
- EVENT_TAB_PAGE_CLOSE
- EVENT_TIMER_TICK
- EVENT_TREE_CELL_ACTIVE_ITEM_CHANGE
- EVENT_TREE_CELL_BEGIN_MENU
- EVENT_TREE_CELL_COMMIT
- EVENT_TREE_CELL_VAL_CHANGED
- EVENT_VAL_CHANGED
- EVENT_VAL_COERCED
- EVENT_VSCROLL
- EVENT_ZOOM

##### Related Topics

[Callback Schemes](cvicallback_function_schemes.htm)

[Callback Precedence](cviprecedence_of_callback_functions.htm)

[Receiving Events](cvireceivingevents.htm)

[Swallowing Events](cviswallowing_events.htm)

[Processing Events](cviprocessing_events.htm)

[Posting Events](cviposting_events.htm)

[Queueing Events](cviqueueing_events.htm)

[Simulating Events](cvisimulating_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventselectionchange.htm language=enus -->
## TOPIC 01063: EVENT_SELECTION_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventselectionchange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventselectionchange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_SELECTION_CHANGE

#### Description

**Tree Controls**—When a user makes a selection change on a tree item, LabWindows/CVI generates an EVENT_SELECTION_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree control. This event is sent only when the tree is set to multiple selection mode.

This event is [swallowable](cviswallowing_events.htm) for tree controls only. Return 1 to swallow EVENT_SELECTION_CHANGE.

**Table Controls**—When the cell selection changes as a result of an interactive action, LabWindows/CVI generates an EVENT_SELECTION_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the table control.

This event is not swallowable for table controls.

#### Applies To

[Tables](cvitable_control_overview.htm) and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Event Data Values |
| --- | --- |
| Trees | eventData1 = 1 (selection toggle on) eventData2 = itemIndex eventData1 = 0 (selection toggle off) eventData2 = itemIndex |
| Tables | eventData1 = 0 (not used) eventData2 = 0 (not used) |

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventsort.htm language=enus -->
## TOPIC 01064: EVENT_SORT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventsort.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventsort.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_SORT

#### Description

When a user sorts tree items, LabWindows/CVI generates an EVENT_SORT event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree control.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_SORT.

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = Boolean values for descending and sorting subtrees options. The eventData1 parameter contains information that specifies whether the sort is ascending or descending and whether the subtrees also will be sorted. The low order word is nonzero if the sort is descending; the low word order is zero if the sort is ascending. The high order word is nonzero if the subtrees also will be sorted; high order word is zero if the subtrees will not be sorted.

eventData2 = Key column

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventtablerowcollabelclick.htm language=enus -->
## TOPIC 01065: EVENT_TABLE_ROW_COL_LABEL_CLICK

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventtablerowcollabelclick.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventtablerowcollabelclick.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_TABLE_ROW_COL_LABEL_CLICK

#### Description

When a user clicks a row or column label, LabWindows/CVI generates an EVENT_TABLE_ROW_COL_LABEL_CLICK event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the table control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Tables](cvitable_control_overview.htm)

#### Event Data Parameters

eventData1 = The index of the row label that the user clicked or 0 if the user clicked the column label or the upper left area of the table

eventData2 = The index of the column label that the user clicked or 0 if the user clicked the row label or the upper left area of the table

#### LabWindows/CVI Compatibility

LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventtabpageclose.htm language=enus -->
## TOPIC 01066: EVENT_TAB_PAGE_CLOSE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventtabpageclose.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventtabpageclose.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_TAB_PAGE_CLOSE

#### Description

When you close a tab page, LabWindows/CVI generates an EVENT_TAB_PAGE_CLOSE event. Use middle click to close a tab.

This event is [swallowable](cviswallowing_events.htm).

#### Applies To

[Tabs](cvitab_control_overview.htm)

#### Event Data Parameters

eventData1 = the index of the closed page

eventData2 = 0 (not used)

#### LabWindows/CVI Compatibility

LabWindows/CVI 2017 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventtimertick.htm language=enus -->
## TOPIC 01067: EVENT_TIMER_TICK

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventtimertick.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventtimertick.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_TIMER_TICK

#### Description

LabWindows/CVI generates an EVENT_TIMER_TICK event when the [callback function](cviusing_callback_functions_to_resp.htm) associated with a [timer control](cviprogramming_with_timer_controls.htm) is called at the end of a timer interval.

|  | Note National Instruments recommends that you use the GetTimerTickData function to obtain the time of the current EVENT_TIMER_TICK callback and the time elapsed since the last EVENT_TIMER_TICK callback instead of using the values returned in the eventData1 and eventData2 parameters. GetTimerTickData is the only way to get the time values from an EVENT_TIMER_TICK event in a 64-bit executable. If you are creating a 32-bit only application, you can use the values returned by eventData1 and eventData2. |
| --- | --- |

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Timers](cvitimer_control_overview.htm)

#### Event Data Parameters

eventData1 = Pointer (double*) to the current time, in seconds.

eventData2 = Pointer (double*) to the time elapsed since the last EVENT_TIMER_TICK, in seconds.

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventtreecellactiveitemchange.htm language=enus -->
## TOPIC 01068: EVENT_TREE_CELL_ACTIVE_ITEM_CHANGE

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventtreecellactiveitemchange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventtreecellactiveitemchange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_TREE_CELL_ACTIVE_ITEM_CHANGE

#### Description

When a user changes the active item of a ring or combo box cell in a tree, LabWindows/CVI generates an EVENT_TREE_CELL_ACTIVE_ITEM_CHANGE event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree control.

**String Cells**—Not used.

**Ring Cells**—Event sent when the active ring item changes.

**Combo Box Cells**—Event sent when the active ring item changes.

**Checkbox Cells**—Not used.

**Button Cells**—Not used.

**Color Picker Cells**—Not used.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = Tree item index of the cell where the event was generated

eventData2 = Column index of the cell where the event was generated

#### LabWindows/CVI Compatibility

LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventtreecellbeginmenu.htm language=enus -->
## TOPIC 01069: EVENT_TREE_CELL_BEGIN_MENU

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventtreecellbeginmenu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventtreecellbeginmenu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_TREE_CELL_BEGIN_MENU

#### Description

When a user displays the menu of a ring or combo box tree cell, LabWindows/CVI generates an EVENT_TREE_CELL_BEGIN_MENU event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree.

**String Cells**—Not used.

**Ring Cells**—Event sent when the menu is in the process of displaying.

**Combo Box Cells**—Event sent when the menu is in the process of displaying.

**Checkbox Cells**—Not used.

**Button Cells**—Not used.

**Color Picker Cells**—Event sent when the color palette is in the process of displaying.

This event is [swallowable](cviswallowing_events.htm). Return 1 to swallow EVENT_TREE_CELL_BEGIN_MENU.

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = Tree item index of the cell where the event was generated

eventData2 = Column index of the cell where the event was generated

#### LabWindows/CVI Compatibility

LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventtreecellcommit.htm language=enus -->
## TOPIC 01070: EVENT_TREE_CELL_COMMIT

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventtreecellcommit.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventtreecellcommit.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_TREE_CELL_COMMIT

#### Description

When a user edits a cell in a tree and commits the change, usually by pressing the <Enter> key, LabWindows/CVI generates an EVENT_TREE_CELL_COMMIT event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree control. If the user changes the value of the cell and then presses the <Esc> key, LabWindows/CVI reverts the value and the event is not sent.

**String Cells**—Event sent when the user changes text in the string cell and commits to the change.

**Ring Cells**—Event sent when the user changes the active item in the ring cell and commits to the change.

**Combo Box Cells**—Event sent when the user selects or adds a new value in the combo box cell and commits to the change.

**Checkbox Cells**—Event sent when the user changes the value of the checkbox cell.

**Button Cells**—Event sent when the user selects the button or presses the <Spacebar> key when the cell is in edit mode.

**Color Picker Cells**—Event sent when the user selects a color from the palette.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = Tree item index of the cell where the event was generated

eventData2 = Column index of the cell where the event was generated

#### LabWindows/CVI Compatibility

LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventtreecellvalchanged.htm language=enus -->
## TOPIC 01071: EVENT_TREE_CELL_VAL_CHANGED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventtreecellvalchanged.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventtreecellvalchanged.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_TREE_CELL_VAL_CHANGED

#### Description

When a user changes the label of a cell in a tree, LabWindows/CVI generates an EVENT_TREE_CELL_VAL_CHANGED event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the tree control.

**String Cells**—Event sent when the label changes as a result of a keypress.

**Ring Cells**—Not used.

**Combo Box Cells**—Event sent when the label changes as a result of a keypress.

**Checkbox Cells**—Not used.

**Button Cells**—Not used.

**Color Picker Cells**—Event sent when the color changes while tracking the popup.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Trees](cvitree_control_overview.htm)

#### Event Data Parameters

eventData1 = Tree item index of the cell where the event was generated

eventData2 = Column index of the cell where the event was generated

#### LabWindows/CVI Compatibility

LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventvalchanged.htm language=enus -->
## TOPIC 01072: EVENT_VAL_CHANGED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventvalchanged.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventvalchanged.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_VAL_CHANGED

#### Description

LabWindows/CVI generates and sends an EVENT_VAL_CHANGED event continuously while a user performs an ongoing action that results in the value of a control changing. Examples of these actions are operating the up/down arrows of a numeric control, a ring control, or a table cell; holding the left mouse button down while selecting different items of a list box control; and dragging a graph control cursor.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Binary switches](cvibinary_switch_control_overview.htm), [color numerics](cvicolor_numeric_control_overview.htm), [graphs](cvigraph_control_overview.htm), [LEDs](cviled_control_overview.htm), [list boxes](cvilist_box_control_overview.htm), [numeric slides](cvinumeric_slide_control_overview.htm), [numerics](cvinumeric_control_overview.htm), [picture buttons](cvipicture_button_control_overview.htm), [picture rings](cvipicture_ring_control_overview.htm), [radio buttons](cviradio_button_control_overview.htm), [ring slides](cviring_slide_control_overview.htm), [rings](cviring_control_overview.htm), [strings](cvistring_control_overview.htm), [tables](cvitable_control_overview.htm), [text boxes](cvitext_box_control_overview.htm), [text buttons](cvitext_button_control_overview.htm), [toggle buttons](cvitoggle_button_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Action | Event Data Values |
| --- | --- | --- |
| Tables (events calling the control callback function) | All table event value change actions | eventData1 = Row of cell where event was generated. If the event affected multiple cells, such as when you sort or paste a range of cells, eventData1 is set to 0. eventData2 = Column of cell where event was generated. If the event affected multiple cells, such as when you sort or paste a range of cells, eventData2 is set to 0. |
| Trees (events calling the control callback function) | Changing the active item | eventData1 = ACTIVE_ITEM_CHANGE eventData2 = oldItemIndex |
| Label-changing keypresses | eventData1 = LABEL_CHANGE eventData2 = keyPressed |  |
| Graphs (events calling the control callback function) | All graph event value change actions | eventData1 = The index of the cursor or the annotation, depending on which one the user moved eventData2 = VAL_CURSOR or VAL_ANNOTATION, as appropriate to eventData1 |

#### LabWindows/CVI Compatibility

LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventvalcoerced.htm language=enus -->
## TOPIC 01073: EVENT_VAL_COERCED

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventvalcoerced.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventvalcoerced.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_VAL_COERCED

#### Description

When [a value is coerced](cviattrcheckrange_control.htm) to the upper or lower range boundary of the control, whichever is closer, LabWindows/CVI generates an EVENT_VAL_COERCED event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the control.

|  | Note EVENT_VAL_COERCED events are not generated when LabWindows/CVI coerces values to stay within the minimum or maximum value of the specified data type of the control. |
| --- | --- |

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Numeric slides](cvinumeric_slide_control_overview.htm), [numerics](cvinumeric_control_overview.htm), and [tables](cvitable_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Event Data Values |
| --- | --- |
| Numerics and numeric slides | eventData1 = 0 eventData2 = 0 |
| Tables | eventData1 = Row of cell where event was generated; 0 if the event affected multiple cells eventData2 = Column of cell where event was generated; 0 if event affected multiple cells |

#### LabWindows/CVI Compatibility

LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventvscroll.htm language=enus -->
## TOPIC 01074: EVENT_VSCROLL

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventvscroll.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventvscroll.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_VSCROLL

#### Description

When a user scrolls the control or panel vertically, LabWindows/CVI generates an EVENT_VSCROLL event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the panel or control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[List boxes](cvilist_box_control_overview.htm), [panels](cvioperating_panels.htm), [tables](cvitable_control_overview.htm), [text boxes](cvitext_box_control_overview.htm), and [trees](cvitree_control_overview.htm)

#### Event Data Parameters

| User Interface Object | Event Data Values |
| --- | --- |
| Panels, trees, text boxes, and tables | eventData1 = oldScrollOffset, in pixels eventData2 = newScrollOffset, in pixels |
| List boxes | eventData1 = oldTopIndex eventData2 = newTopIndex |

#### LabWindows/CVI Compatibility

LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvieventzoom.htm language=enus -->
## TOPIC 01075: EVENT_ZOOM

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvieventzoom.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvieventzoom.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### EVENT_ZOOM

#### Description

When a user [zooms in or out](cvioperating_graph_controls.htm#zoompan) of a graph or [changes the viewable area](cvioperating_graph_controls.htm#zoompan) of a graph, LabWindows/CVI generates an EVENT_ZOOM event and sends the event to the [callback function](cviusing_callback_functions_to_resp.htm) associated with the graph control.

This event is not [swallowable](cviswallowing_events.htm).

#### Applies To

[Graphs](cvigraph_control_overview.htm)

#### Event Data Parameters

eventData1 = The action that the user performed (ZOOM_IN, ZOOM_OUT, 
ZOOM_PAN, or ZOOM_RESTORE)

eventData2 = Not used

#### LabWindows/CVI Compatibility

LabWindows/CVI 8.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifakekeystroke.htm language=enus -->
## TOPIC 01076: FakeKeystroke

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifakekeystroke.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifakekeystroke.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FakeKeystroke

int FakeKeystroke (int keyCode);

#### Purpose

Simulates a keystroke by posting a keystroke event to the currently 
active panel.

This function has the same effect as actually pressing a key at the keyboard.

|  | Note The order in which you receive the keystroke event in relation to other events is not defined, so you must use FakeKeystroke with care. |
| --- | --- |

|  | Note If you want to send a fake keystroke consisting of a dual-byte characterdual-byte character, you must call this function twice. First you must pass it the lead byte of the dual-byte character, in place of the ASCII character; then you must pass it the trail byte, also in place of the ASCII character. You cannot use a virtual key code on either call. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| keyCode | int | Form key codes by a logical OR operation on values representing a modifier key and either an ASCII character or a virtual key. A modifier key is a <Shift> key, <Alt> key, or menu modifier key (the <Ctrl> key). The following constants represent the modifier key. VAL_SHIFT_MODIFIER = 0x010000 VAL_UNDERLINE_MODIFIER = 0x020000 VAL_MENUKEY_MODIFIER = 0x040000 VAL_SHIFT_AND_MENUKEY = 0x050000 ASCII characters can be represented by a literal character, for example, 'A' or 'D', or an ASCII value. There is no distinction between upper and lower case ASCII characters. Virtual keys are non-ASCII keys represented by the following key codes: VAL_FWD_DELETE_VKEY = 0x0100 VAL_BACKSPACE_VKEY = 0x0200 VAL_ESC_VKEY = 0x0300 VAL_TAB_VKEY = 0x0400 VAL_ENTER_VKEY = 0x0500 VAL_UP_ARROW_VKEY = 0x0600 VAL_DOWN_ARROW_VKEY = 0x0700 VAL_LEFT_ARROW_VKEY = 0x0800 VAL_RIGHT_ARROW_VKEY = 0x0900 VAL_INSERT_VKEY = 0x0A00 VAL_HOME_VKEY = 0x0B00 VAL_END_VKEY = 0x0C00 VAL_PAGE_UP_VKEY = 0x0D00 VAL_PAGE_DOWN_VKEY = 0x0E00 VAL_F1_VKEY = 0x0F00 VAL_F2_VKEY = 0x1000 VAL_F3_VKEY = 0x1100 VAL_F4_VKEY = 0x1200 VAL_F5_VKEY = 0x1300 VAL_F6_VKEY = 0x1400 VAL_F7_VKEY = 0x1500 VAL_F8_VKEY = 0x1600 VAL_F9_VKEY = 0x1700 VAL_F10_VKEY = 0x1800 VAL_F11_VKEY = 0x1900 VAL_F12_VKEY = 0x1A00 VAL_POPUP_MENUBAR_VKEY = 0x2500 VAL_POPUP_MENU_VKEY = 0x2700 ASCII cannot be used with a virtual key code. Virtual key codes can be used with or without a modifier. The shift and menu modifier keys can be used together. For example, the expression VAL_MENUKEY_MODIFIER \| 'A' specifies <Ctrl-A>. Other valid key codes include the following: VAL_TAB_VKEY VAL_SHIFT_MODIFIER \| VAL_F5_VKEY The result of the logical OR operation is a 4-byte integer consisting of three bit fields, 0x00MMVVAA, where MM = the modifier key VV = the virtual key AA = the ASCII key |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\gridview.cws for an example of using the FakeKeystroke function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifakekeystrokeunicode.htm language=enus -->
## TOPIC 01077: FakeKeystrokeUnicode

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifakekeystrokeunicode.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifakekeystrokeunicode.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FakeKeystrokeUnicode

int FakeKeystrokeUnicode (KeyCodeUnicode keyCode);

#### Purpose

Simulates a Unicode keystroke by posting a keystroke event to the 
active panel.

This function has the same effect as pressing a key on the keyboard.

|  | Note Unicode key codes are formed by packing a Unicode code point, a virtual key, and a modifier key. You must pack the values from these Unicode key code elements using the PackKeyCodeUnicode function before passing them into FakeKeystrokeUnicode. |
| --- | --- |

|  | Note The order in which you receive the keystroke event in relation to other events is not defined, so use FakeKeystrokeUnicode with care. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| keyCode | KeyCodeUnicode | The value representing a Unicode key code. Unicode key codes are formed by packing a Unicode code point, a virtual key, and a modifier key. A modifier key is a <Shift> key, <Alt> key, or <Ctrl> key. Note Use PackKeyCodeUnicode to pack a Unicode code point, a virtual key, and a modifier key and obtain a Unicode key code. In order to use this function, you must include userint.h and utility.h in your program. |
|  | Note Use PackKeyCodeUnicode to pack a Unicode code point, a virtual key, and a modifier key and obtain a Unicode key code. In order to use this function, you must include userint.h and utility.h in your program. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2020 and later

#### Example

Refer to userint\FakeKeystrokeUnicode.cws for an example of using the FakeKeystrokeUnicode function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifile_dialogs_and_multithreading.htm language=enus -->
## TOPIC 01078: File Dialog Boxes and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifile_dialogs_and_multithreading.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifile_dialogs_and_multithreading.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### File Dialog Boxes and Multithreading

You can display multiple [file dialog](cvifileselectpopup.htm) boxes from different [threads](cvidifferent_approaches_to_multithr.htm) at the same time.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifileselectpopup.htm language=enus -->
## TOPIC 01079: FileSelectPopup

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifileselectpopup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifileselectpopup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FileSelectPopup

int FileSelectPopup (char defaultDirectory[], char defaultFileSpec[], char fileTypeList[], char title[], int buttonLabel, int restrictDirectory, int restrictExtension, int allowCancel, int allowMakeDirectory, char pathName[]);

#### Purpose

|  | Note This function has been superseded by FileSelectPopupEx. Use FileSelectPopupEx to display a Windows Vista and later style dialog box. |
| --- | --- |

Displays a file selection dialog box and waits for the user to select 
a file or cancel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| defaultFileSpec | char [] | String that specifies which value is displayed by default in the file type list of the dialog box. For example, "*.c" causes all files with the .c extension to be displayed. LabWindows/CVI adds a new file type item if needed. If an actual file name is specified, such as "test.c", that name appears in the file name box when the dialog box is displayed and the extension of the file, "*.c", is selected by default in the file type list. The default file specification (spec) cannot contain a directory path. The maximum length of the default file spec is 255 bytes. |
| fileTypeList | char [] | List of file types, separated by semicolons, to display in the file type list of the dialog box when restrictExtension is FALSE. For example, "*.c; *.h" allows the user to select "*.c" or "*.h" from the file type list. The all files, *.*, option is always available. You can group multiple file types under one entry in the drop-down list by enclosing the file types in parentheses and separating the file types by semicolons. You can include descriptive text along with the file types. For example, "JPEG Files (*.jpg;*.jpeg);PNG Files (*.png);*.bmp;" allows the user to see all JPEG file types at once, or to select "*.png" or "*.bmp" from the file type list. |
| title | char [] | Title of the dialog box. |
| buttonLabel | int | The label for the file select button. You can select from the following choices: Button Label Value Description OK VAL_OK_BUTTON Allows users to select a file Save VAL_SAVE_BUTTON Allows users to save a file Select VAL_SELECT_BUTTON (affects existing files only) Confirms the selected file exists Load VAL_LOAD_BUTTON (affects existing files only) Displays an existing file Note If VAL_SELECT_BUTTON or VAL_LOAD_BUTTON is passed to the buttonLabel parameter, the FileSelectPopup function confirms the selected file exists. If the file does not exist, the function prompts the user to select an existing file. |
| Button Label | Value | Description |
| OK | VAL_OK_BUTTON | Allows users to select a file |
| Save | VAL_SAVE_BUTTON | Allows users to save a file |
| Select | VAL_SELECT_BUTTON (affects existing files only) | Confirms the selected file exists |
| Load | VAL_LOAD_BUTTON (affects existing files only) | Displays an existing file |
|  | Note If VAL_SELECT_BUTTON or VAL_LOAD_BUTTON is passed to the buttonLabel parameter, the FileSelectPopup function confirms the selected file exists. If the file does not exist, the function prompts the user to select an existing file. |  |
| restrictDirectory | int | Specify a nonzero value or select yes in the function panel to restrict the user from changing directories or drives. Specify 0 or select no in the function panel to allow the user to change directories or drives. |
| restrictExtension | int | Specify a nonzero value or select yes in the function panel to limit the user to files with the default extension. Specify 0 or select no in the function panel to allow the user to select files with any extension. |
| allowCancel | int | Specify a nonzero value or select yes in the function panel to allow the user to cancel out of the dialog box. Specify 0 or select no in the function panel to force the user to make a selection before exiting the dialog box. |
| allowMakeDirectory | int | Specify a nonzero value or select yes in the function panel to display a new directory icon that allows the user to create a new directory from the dialog box. This option is useful when a user wants to save a file into a new directory. Specify 0 or select no in the function panel to not include the icon in the dialog box. Note Specifying 0 or selecting no in the function panel does not prevent users from right-clicking in the file list of the dialog box and selecting New»Folder to create a new directory. |
|  | Note Specifying 0 or selecting no in the function panel does not prevent users from right-clicking in the file list of the dialog box and selecting New»Folder to create a new directory. |  |
| Output |  |  |
| Name | Type | Description |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| selectionStatus | int | The selection status or error codes generated during the function call. 0 VAL_NO_FILE_SELECTED 1 VAL_EXISTING_FILE_SELECTED 2 VAL_NEW_FILE_SELECTED Negative values indicate that an error occurred. |
| 0 | VAL_NO_FILE_SELECTED |  |
| 1 | VAL_EXISTING_FILE_SELECTED |  |
| 2 | VAL_NEW_FILE_SELECTED |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifileselectpopupex.htm language=enus -->
## TOPIC 01080: FileSelectPopupEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifileselectpopupex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifileselectpopupex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FileSelectPopupEx

int FileSelectPopupEx (char defaultDirectory[], char defaultFileSpec[], char fileTypeList[], char title[], int buttonLabel, int restrictDirectory, int restrictExtension, char pathName[]);

#### Purpose

Displays a file selection dialog box and waits for the user to select a file or cancel.

(Linux) The dialog box displayed with FileSelectPopupEx includes a **Make Directory** button, while the dialog box displayed with [FileSelectPopup](../../cvi/uiref/cvifileselectpopup.htm) does not.

|  | Note The underlying Windows SDK function used to create and run the FileSelectPopupEx dialog box does not work properly when the threading modelthreading model is multithread apartment (MTA). ActiveX functions use this thread type by default, and calling any ActiveX function initializes the thread to MTA. This might cause subsequent calls to the FileSelectPopupEx function to return an error. To ensure the FileSelectPopupEx dialog box works properly, LabWindows/CVI initializes the thread calling the FileSelectPopupEx function to COINIT_APARTMENTTHREADED prior to creating the dialog box. If you want to run in the default MTA threading model, consider calling the FileSelectPopupEx function from a different thread that does not call any ActiveX functions. You can explicitly set the ActiveX threading model for a thread using the CA_InitActiveXThreadStyleForCurrentThreadCA_InitActiveXThreadStyleForCurrentThread function. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| defaultFileSpec | char [] | String that specifies which value is displayed by default in the file type list of the dialog box. For example, "*.c" causes all files with the .c extension to be displayed. LabWindows/CVI adds a new file type item if needed. If an actual file name is specified, such as "test.c", that name appears in the file name box when the dialog box is displayed and the extension of the file, "*.c", is selected by default in the file type list. The default file specification (spec) cannot contain a directory path. The maximum length of the default file spec is 255 bytes. |
| fileTypeList | char [] | List of file types, separated by semicolons, to display in the file type list of the dialog box when restrictExtension is FALSE. For example, "*.c; *.h" allows the user to select "*.c" or "*.h" from the file type list. The all files, "*.*", option is always available. You can group multiple file types under one entry in the drop-down list by enclosing the file types in parentheses and separating the file types by semicolons. You can include descriptive text along with the file types. For example, "JPEG Files (*.jpg;*.jpeg);PNG Files (*.png);*.bmp;" allows the user to see all JPEG file types at once, or to select "*.png" or "*.bmp" from the file type list. |
| title | char [] | Title of the dialog box. |
| buttonLabel | int | The label for the file select button. You can select from the following choices: Button Label Value Description OK VAL_OK_BUTTON Allows users to select a file Save VAL_SAVE_BUTTON Allows users to save a file Select VAL_SELECT_BUTTON (affects existing files only) Confirms the selected file exists Load VAL_LOAD_BUTTON (affects existing files only) Displays an existing file Note If VAL_SELECT_BUTTON or VAL_LOAD_BUTTON is passed to the buttonLabel parameter, the FileSelectPopupEx function confirms the selected file exists. If the file does not exist, the function prompts the user to select an existing file. |
| Button Label | Value | Description |
| OK | VAL_OK_BUTTON | Allows users to select a file |
| Save | VAL_SAVE_BUTTON | Allows users to save a file |
| Select | VAL_SELECT_BUTTON (affects existing files only) | Confirms the selected file exists |
| Load | VAL_LOAD_BUTTON (affects existing files only) | Displays an existing file |
|  | Note If VAL_SELECT_BUTTON or VAL_LOAD_BUTTON is passed to the buttonLabel parameter, the FileSelectPopupEx function confirms the selected file exists. If the file does not exist, the function prompts the user to select an existing file. |  |
| restrictDirectory | int | Specify a nonzero value or select yes in the function panel to restrict the user from changing directories or drives. Specify 0 or select no in the function panel to allow the user to change directories or drives. |
| restrictExtension | int | Specify a nonzero value or select yes in the function panel to limit the user to files with the default extension. Specify 0 or select no in the function panel to allow the user to select files with any extension. |
| Output |  |  |
| Name | Type | Description |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| selectionStatus | int | The selection status or error codes generated during the function call. 0 VAL_NO_FILE_SELECTED 1 VAL_EXISTING_FILE_SELECTED 2 VAL_NEW_FILE_SELECTED Negative values indicate that an error occurred. |
| 0 | VAL_NO_FILE_SELECTED |  |
| 1 | VAL_EXISTING_FILE_SELECTED |  |
| 2 | VAL_NEW_FILE_SELECTED |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

#### Examples

Refer to the following examples that use the FileSelectPopupEx function:

- apps\daqmthread\daqMT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- internet\sendmail\sendmail.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\ICOViewer.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\popups.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\custctrl\cviogl\ogldemo.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifilltablecellrange.htm language=enus -->
## TOPIC 01081: FillTableCellRange

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifilltablecellrange.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifilltablecellrange.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FillTableCellRange

int FillTableCellRange (int panelHandle, int controlID, Rect cellRange, ...);

#### Purpose

Sets the values of a table control cell range to the same specified value.

#### Supported Controls

You can use FillTableCellRange with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cellRange | Rect | A Rect structure specifying the cell range for which you want to set the values. To use this function, you must specify a cell range in which all cells are of compatible types. Cells are of compatible types if they are all of type VAL_CELL_NUMERIC, or if they are all of type VAL_CELL_PICTURE, or if they are a combination of the other cell types. If the cell type is VAL_CELL_NUMERIC, all cells in the range also must share an identical data type. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; Pass the one-based row and column indices of the first cell in the range as the top and left fields of the structure, respectively. Pass the number of columns in the range as the width field of the structure, and the number of rows in the range as the height field of the structure. You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example FillTableCellRange (panelHandle, controlID, MakeRect (2, 3, 5, 5), value); |
| value | ... | The new value of each cell in the range. The value that this function expects depends on the cell type. If the cell type is VAL_CELL_PICTURE, the function expects an ID of the bitmap containing the new image. The ID must be a value obtained from NewBitmapEx, GetBitmapFromFile, GetCtrlBitmap, ClipboardGetBitmap, GetCtrlDisplayBitmap, GetPanelDisplayBitmap, GetScaledPanelDisplayBitmap, GetScaledCtrlDisplayBitmap, or DuplicateBitmap. A value of 0 indicates that there is no image. You can use this to delete an existing image. If the cell type is VAL_CELL_STRING, VAL_CELL_RING, VAL_CELL_COMBO_BOX, or VAL_CELL_BUTTON, the function expects a NUL-terminated string. If the cell type is VAL_CELL_NUMERIC, the function expects a number of a data type matching the data type of the cell. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifont_popup_defaults_and_multithr.htm language=enus -->
## TOPIC 01082: Font Pop-Up Defaults and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifont_popup_defaults_and_multithr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifont_popup_defaults_and_multithr.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Font Pop-Up Defaults and Multithreading

[SetFontPopupDefaults](cvisetfontpopupdefaults.htm) maintains separate values for each [thread](cvidifferent_approaches_to_multithr.htm).

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifontselectpopup.htm language=enus -->
## TOPIC 01083: FontSelectPopup

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifontselectpopup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifontselectpopup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FontSelectPopup

int FontSelectPopup (char title[], char sampleText[], int monospacedFontsOnly, char typefaceName[], int *bold, int *underline, int *strikeOut, int *italic, int *justification, int *textColor, int *fontSize, int minimumFontSize, int maximumFontSize, int showDefaultButton, int allowMetaFonts);

#### Purpose

|  | Note This function has been superseded by FontSelectPopupEx. Use FontSelectPopupEx to include Angle and Character Set options in the pop-up dialog box. |
| --- | --- |

Opens a pop-up dialog box in which a user can specify font settings.

If the user cancels out of the pop-up dialog box or an error occurs, the function does not 
modify any of the input or output parameters.

|  | Note You can pass 0 to any of the output parameters to hide the selection of that parameter in the font pop-up dialog box. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| title | char [] | Title of the dialog box. |
| sampleText | char [] | Sample text to display in the pop-up dialog box as demonstration of how the settings affect the appearance of text. |
| monospacedFontsOnly | int | Specify a nonzero value or select On in the function panel to list only monospaced, fixed width fonts. Specify 0 or select Off in the function panel to list all fonts. |
| minimumFontSize | int | Minimum value allowed in the Size control. |
| maximumFontSize | int | Maximum value allowed in the Size control. |
| showDefaultButton | int | Specifies whether to add a default button to the font pop-up dialog box. When the user presses the Default button, the controls on the font pop-up dialog box change to the values you specified in your most recent call to SetFontPopupDefaults or SetFontPopupDefaultsEx. Specify a nonzero value or select On in the function panel to add a default button. Specify 0 or select Off in the function panel to omit the default button. |
| allowMetaFonts | int | Specify a nonzero value or select On in the function panel to list the NI-supplied metafonts in the font pop-up dialog box. Specify 0 or select Off in the function panel to omit the metafonts from the font pop-up dialog box. |
| Output |  |  |
| Name | Type | Description |
| typefaceName | char [] | On input, the typeface name, such as Courier, that initially appears in the Font ring control. On output, the typeface name the user selects. The buffer must be at least 256 bytes long. Pass 0 to hide the Font ring control and prevent the user from changing the typeface. |
| bold | int | On input, the value that initially appears in the Bold checkbox. On output, the final value in the Bold checkbox. Pass 0 to hide the Bold checkbox. |
| underline | int | On input, the value that initially appears in the Underline checkbox. On output, the final value in the Underline checkbox. Pass 0 to hide the Underline checkbox. |
| strikeOut | int | On input, the value that initially appears in the Strikeout checkbox. On output, the final value in the Strikeout checkbox. Pass 0 to hide the Strikeout checkbox. |
| italic | int | On input, the value that initially appears in the Italic checkbox. On output, the final value in the Italic checkbox. Pass 0 to hide the Italic checkbox. |
| justification | int | On input, the value that initially appears in the Justification ring control. On output, the final value in the Justification ring control. Valid values for this parameter are as follows: VAL_LEFT_JUSTIFIED VAL_RIGHT_JUSTIFIED VAL_CENTER_JUSTIFIED Note Not all text can be justified. For example, text in a text box can be justified, but the text in a panel title cannot. Pass 0 to hide the Justification ring control. |
|  | Note Not all text can be justified. For example, text in a text box can be justified, but the text in a panel title cannot. |  |
| textColor | int | On input, the value that initially appears in the Text Color control. On output, the final value in the Text Color control. textColor is a 4-byte RGB value. An RGB value is an integer in the hexadecimal format 0x00RRGGBB, where RR, GG, and BB are the respective red, green, and blue components of the color value. Pass 0 to hide the Text Color control. |
| fontSize | int | On input, the value that initially appears in the Size control. On output, the final value in the Size control. Specify fontSize in units of points. Pass 0 to hide the Size control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| selectionStatus | int | The selection status or error codes generated during the function call. 0 User canceled out of dialog box. 1 User modified the settings. Negative values indicate that an error occurred. |
| 0 | User canceled out of dialog box. |  |
| 1 | User modified the settings. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\graphlegend.cws for an example of using the FontSelectPopup function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifontselectpopupex.htm language=enus -->
## TOPIC 01084: FontSelectPopupEx

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifontselectpopupex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifontselectpopupex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FontSelectPopupEx

int FontSelectPopupEx (char title[], char sampleText[], int monospacedFontsOnly, char typefaceName[], int *bold, int *underline, int *strikeOut, int *italic, int *justification, int *textColor, int *angle, int *characterSet, int *fontSize, int minimumFontSize, int maximumFontSize, int showDefaultButton, int allowMetaFonts);

#### Purpose

Opens a pop-up dialog box in which a user can specify font settings. FontSelectPopupEx is similar to [FontSelectPopup](../../cvi/uiref/cvifontselectpopup.htm), except that FontSelectPopupEx provides **angle** and **charSet** parameters.

If the user cancels out of the pop-up dialog box or an error occurs, the function does not 
modify any of the input or output parameters.

|  | Note You can pass 0 to any of the output parameters to hide the selection of that parameter in the font pop-up dialog box. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| title | char [] | Title of the dialog box. |
| sampleText | char [] | Sample text to display in the pop-up dialog box as demonstration of how the settings affect the appearance of text. |
| monospacedFontsOnly | int | Specify a nonzero value or select On in the function panel to list only monospaced, fixed width fonts. Specify 0 or select Off in the function panel to list all fonts. |
| minimumFontSize | int | Minimum value allowed in the Size control. |
| maximumFontSize | int | Maximum value allowed in the Size control. |
| showDefaultButton | int | Specifies whether to add a default button to the font pop-up dialog box. When the user presses the Default button, the controls on the font pop-up dialog box change to the values you specified in your most recent call to SetFontPopupDefaults or SetFontPopupDefaultsEx. Specify a nonzero value or select On in the function panel to add a default button. Specify 0 or select Off in the function panel to omit the default button. |
| allowMetaFonts | int | Specify a nonzero value or select On in the function panel to list the NI-supplied metafonts in the font pop-up dialog box. Specify 0 or select Off in the function panel to omit the metafonts from the font pop-up dialog box. |
| Output |  |  |
| Name | Type | Description |
| typefaceName | char [] | On input, the typeface name, such as Courier, that initially appears in the Font ring control. On output, the typeface name the user selects. The buffer must be at least 256 bytes long. Pass 0 to hide the Font ring control and prevent the user from changing the typeface. |
| bold | int | On input, the value that initially appears in the Bold checkbox. On output, the final value in the Bold checkbox. Pass 0 to hide the Bold checkbox. |
| underline | int | On input, the value that initially appears in the Underline checkbox. On output, the final value in the Underline checkbox. Pass 0 to hide the Underline checkbox. |
| strikeOut | int | On input, the value that initially appears in the Strikeout checkbox. On output, the final value in the Strikeout checkbox. Pass 0 to hide the Strikeout checkbox. |
| italic | int | On input, the value that initially appears in the Italic checkbox. On output, the final value in the Italic checkbox. Pass 0 to hide the Italic checkbox. |
| justification | int | On input, the value that initially appears in the Justification ring control. On output, the final value in the Justification ring control. Valid values for this parameter are as follows: VAL_LEFT_JUSTIFIED VAL_RIGHT_JUSTIFIED VAL_CENTER_JUSTIFIED Note Not all text can be justified. For example, text in a text box can be justified, but the text in a panel title cannot. Pass 0 to hide the Justification ring control. |
|  | Note Not all text can be justified. For example, text in a text box can be justified, but the text in a panel title cannot. |  |
| textColor | int | On input, the value that initially appears in the Text Color control. On output, the final value in the Text Color control. textColor is a 4-byte RGB value. An RGB value is an integer in the hexadecimal format 0x00RRGGBB, where RR, GG, and BB are the respective red, green, and blue components of the color value. Pass 0 to hide the Text Color control. |
| angle | int | On input, the value that initially appears in the Angle control. On output, the final value in the Angle control. angle is in tenths of a degree. Pass 0 to hide the Angle control. Linux The available values for this control are 0, 900, 1800, and 2700. |
| characterSet | int | On input, the value that initially appears in the Character Set control. On output, the final value in the Character Set control. Pass 0 to hide the Character Set control. (Linux) This parameter is ignored, and the control does not appear on font selection pop-up dialog boxes. |
| fontSize | int | On input, the value that initially appears in the Size control. On output, the final value in the Size control. Specify fontSize in units of points. Pass 0 to hide the Size control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| selectionStatus | int | The selection status or error codes generated during the function call. 0 User canceled out of dialog box. 1 User modified the settings. Negative values indicate that an error occurred. |
| 0 | User canceled out of dialog box. |  |
| 1 | User modified the settings. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviformatdatetimestring.htm language=enus -->
## TOPIC 01085: FormatDateTimeString

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviformatdatetimestring.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviformatdatetimestring.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FormatDateTimeString

int FormatDateTimeString (double dateTime, char formatString[], char outputBuffer[], int outputBufferSize);

#### Purpose

Formats a given date/time into a string buffer according to descriptions in the **formatString** parameter.

FormatDateTimeString supports the same [absolute date/time format specifiers](../../cvi/usermanual/datetimespecifierslist.htm#absolute) as the strftime function with the %*n*f extension.

##### Example Code

The following code demonstrates how to get the current date and time and then format them according to the specified format string.

#define DATETIME_FORMATSTRING "%I:%M%p %A, %B %d, %Y"

...

double currDateTime;

int bufferLen;

char *dateTimeBuffer = NULL;

GetCurrentDateTime (&currDateTime);

bufferLen = FormatDateTimeString (currDateTime, DATETIME_FORMATSTRING, NULL, 0);

dateTimeBuffer = malloc (bufferLen + 1);

FormatDateTimeString (currDateTime, DATETIME_FORMATSTRING, dateTimeBuffer, bufferLen + 1 );

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| dateTime | double | The date/time to format. The value is the number of seconds since midnight, January 1, 1900. You can call MakeDateTime to retrieve a specified time in this format, or you can call GetCurrentDateTime to retrieve the current date/time. |
| formatString | char [] | The format string that specifies how to convert the date/time for output. The formatString is similar to the format string used in printf. The formatString supports the same absolute date/time format specifiers as the strftime function with the %nf extension. |
| outputBufferSize | int | The maximum number of characters, including a terminating NUL character, to be written into outputBuffer. |
| Output |  |  |
| Name | Type | Description |
| outputBuffer | char [] | The destination buffer for the formatted output. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Returns the size of the buffer required to hold the entire formatted string, not including the terminating NUL byte. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

#### Examples

Refer to the following examples that use the FormatDateTimeString function:

- udp\UDPChat.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\TimeDateUnits.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifreetablevalstrings.htm language=enus -->
## TOPIC 01086: FreeTableValStrings

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifreetablevalstrings.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifreetablevalstrings.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### FreeTableValStrings

int FreeTableValStrings (char * valueArray[], int count);

#### Purpose

Frees the memory associated with any strings returned by [GetTableCellRangeVals](../../cvi/uiref/cvigettablecellrangevals.htm).

Call this function only if the type of the cells in the 
cell range you passed to GetTableCellRangeVals is VAL_CELL_STRING, VAL_CELL_RING, VAL_CELL_COMBO_BOX, or VAL_CELL_BUTTON.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| valueArray | char *[] | The array containing the pointers you want to free. This array must be the same array you passed to GetTableCellRangeVals. |
| count | int | The number of elements in valueArray. This value must match the number of cells in the cell range you passed to GetTableCellRangeVals. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvifunctions_for_hard_copy_output.htm language=enus -->
## TOPIC 01087: Functions for Hard Copy Output

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvifunctions_for_hard_copy_output.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvifunctions_for_hard_copy_output.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Functions for Hard Copy Output

The User Interface Library functions that you can use to [generate hard copy](cvigenerating_hard_copy_output.htm) output appear in the following lists.

**Printing Functions**

| GetPrintAttribute | PrintTextBuffer |
| --- | --- |
| PrintCtrl | PrintTextFile |
| PrintPanel | SetPrintAttribute |

In addition, the following functions can produce hard copy output if you
select the hard copy option from the following [pop-ups](cvioperating_popup_panels.htm):

| WaveformGraphPopup | XYGraphPopup |
| --- | --- |
| XGraphPopup | YGraphPopup |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigenerating_hard_copy_output.htm language=enus -->
## TOPIC 01088: Generating Hard Copy Output

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigenerating_hard_copy_output.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigenerating_hard_copy_output.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Generating Hard Copy Output

You can generate hard copy output of [panels](cvioperating_panels.htm) or individual [controls](cvioperating_controls.htm) to a graphics printer or a file.

LabWindows/CVI can print to any graphics printer with a Windows compatible
driver. You select the printer through the Printers utility in the Windows Control
Panel, through the LabWindows/CVI print dialog box or the [ATTR_PRINTER_NAME](cviattrprintername.htm) attribute.

[Printing Functions](cvifunctions_for_hard_copy_output.htm)

[Printing Attributes](cvilist_of_print_attributes.htm)

[Printer Settings](cviusing_printer_settings_under_win.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigenericmessagepopup.htm language=enus -->
## TOPIC 01089: GenericMessagePopup

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigenericmessagepopup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigenericmessagepopup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GenericMessagePopup

int GenericMessagePopup (char title[], char message[], char buttonLabel1[], char buttonLabel2[], char buttonLabel3[], char responseBuffer[], size_t maxResponseLength, int buttonAlignment, int activeControl, int enterButton, int escapeButton);

#### Purpose

Displays a dialog box with a defined message and optionally accepts a 
response string.

You can use up to three buttons and specify their labels. 
GenericMessagePopup returns a value indicating which button the user pressed.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| title | char [] | Title of the dialog box. |
| message | char [] | Message to display in the dialog box. To display a multi-line message, embed newline characters (\\n) in the message string. |
| buttonLabel1 | char [] | Label on button 1. |
| buttonLabel2 | char [] | Label on button 2. To hide buttons 2 and 3, pass 0 to buttonLabel2. |
| buttonLabel3 | char [] | Label on button 3. To hide button 3, pass 0 to buttonLabel3. |
| maxResponseLength | size_t | Maximum number of bytes the user is allowed to enter. The responseBuffer must be large enough to contain all of the user input plus one ASCII NUL byte. |
| buttonAlignment | int | Determines the location of the buttons. Specify a nonzero value or select side in the function panel to align the buttons along the right-hand side of the dialog box. Specify 0 or select bottom in the function panel to align the buttons along the bottom of the dialog box. |
| activeControl | int | Selects one of the buttons or the input string as the active control. The active control is the control that accepts keystrokes. The following values apply to activeControl: VAL_GENERIC_POPUP_BTN1 VAL_GENERIC_POPUP_BTN2 VAL_GENERIC_POPUP_BTN3 VAL_GENERIC_POPUP_INPUT_STRING |
| enterButton | int | Selects which button has <Enter> as its shortcut key. Pass VAL_GENERIC_POPUP_NO_CTRL if no button uses <Enter> as its shortcut key. |
| escapeButton | int | Selects which button has <Esc> as its shortcut key. Pass VAL_GENERIC_POPUP_NO_CTRL if no button uses <Esc> as its shortcut key. |
| Output |  |  |
| Name | Type | Description |
| responseBuffer | char [] | Buffer in which to store the user response. The buffer must be large enough to hold maxResponseLength bytes plus one ASCII NUL byte. To hide the input string, pass 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| selectedButton | int | Returns an indication of which button the user clicked. 1 VAL_GENERIC_POPUP_BTN1 2 VAL_GENERIC_POPUP_BTN2 3 VAL_GENERIC_POPUP_BTN3 Negative values indicate that an error occurred. |
| 1 | VAL_GENERIC_POPUP_BTN1 |  |
| 2 | VAL_GENERIC_POPUP_BTN2 |  |
| 3 | VAL_GENERIC_POPUP_BTN3 |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the GenericMessagePopup function:

- toolbox\ini.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\clipbord.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviget3dbordercolors.htm language=enus -->
## TOPIC 01090: Get3dBorderColors

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviget3dbordercolors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviget3dbordercolors.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Get3dBorderColors

int Get3dBorderColors (int baseColor, int *highlightColor, int *lightColor, int *shadowColor, int *darkShadowColor);

#### Purpose

Takes an RGB value for the base color of an object and returns the RGB values
for colors that you can use to make the object look three-dimensional.

The colors that Get3dBorderColors returns are similar to the colors that Windows uses to draw three-dimensional objects.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| baseColor | int | RGB value for the color of an object. |
| Output |  |  |
| Name | Type | Description |
| highlightColor | int | The RGB value for the highlight color. Use this color to indicate the edges of the object that are in the most direct light. You can pass NULL. |
| lightColor | int | The RGB value for the light color. Use this color to indicate the transition between the highlight color and the base color of the object. Currently, lightColor is always the same as baseColor. You can pass NULL. |
| shadowColor | int | The RGB value for the shadow color. Use this color to indicate the edges of the object that are angled away from the light. You can pass NULL. |
| darkShadowColor | int | The RGB value for the dark shadow color. Use this color to indicate the edges of the object that are angled farthest away from the light. Currently, darkShadowColor is always black. You can pass NULL. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetactivectrl.htm language=enus -->
## TOPIC 01091: GetActiveCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetactivectrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetactivectrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetActiveCtrl

int GetActiveCtrl (int panelHandle);

#### Purpose

Obtains the ID of the active control on the specified panel.

The active control is the control that receives keyboard events when the panel
is the active panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| controlID | int | Returns the control ID of the active control. If the panel has no controls, GetActiveCtrl returns zero. GetActiveCtrl can return the following error code: –4—Panel, pop-up, menu bar, or plot ID is invalid. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\clipbord.cws for an example of using the GetActiveCtrl function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetactivegraphcursor.htm language=enus -->
## TOPIC 01092: GetActiveGraphCursor

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetactivegraphcursor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetactivegraphcursor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetActiveGraphCursor

int GetActiveGraphCursor (int panelHandle, int controlID, int *activeCursorNumber);

#### Purpose

Obtains the active cursor on the specified graph control.

#### Supported Controls

You can use GetActiveGraphCursor with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| activeCursorNumber | int | The number of the active cursor. The value ranges from 1 to the number of defined cursors for the specified graph. You can set the number of cursors in the User Interface Editor or through SetCtrlAttribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\2yaxis.cws for an example of using the GetActiveGraphCursor function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetactivelegenditem.htm language=enus -->
## TOPIC 01093: GetActiveLegendItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetactivelegenditem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetactivelegenditem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetActiveLegendItem

int GetActiveLegendItem (int panelHandle, int controlID, int *item);

#### Purpose

Returns the index of the active trace item on the strip chart legend or the handle of the active plot on the graph legend.

The legend has an active item when the interactive legend context menu is active.

#### Supported Controls

You can use GetActiveLegendItem with the following controls:

- Graphs
- Strip charts

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| item | int | If the control is a strip chart, this is the index of the active trace item. If the control is a graph, this is the handle of the active plot. Returns zero if there is no active legend item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetnumtablecellringitems.htm language=enus -->
## TOPIC 01094: GetNumTableCellRingItems

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetnumtablecellringitems.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetnumtablecellringitems.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumTableCellRingItems

int GetNumTableCellRingItems (int panelHandle, int controlID, Point cell, int *numberOfItems);

#### Purpose

Returns the number of items in the list of values of a specified ring or combo-box cell of a table control.

#### Supported Controls

You can use GetNumTableCellRingItems with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cell | Point | A Point structure specifying the cell from which you want to obtain the number of values. The specified cell must be of type VAL_CELL_RING or VAL_CELL_COMBO_BOX. The Point structure is defined as follows: typedef struct { int x; int y; } Point; Pass the one-based column index of the cell in the x field of the structure, and the one-based row index of the cell in the y field of the structure. You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example GetNumTableCellRingItems (panelHandle, controlID, MakePoint (2, 3), &count); |
| Output |  |  |
| Name | Type | Description |
| numberOfItems | int | The number of items in the values list. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetnumtablecolumns.htm language=enus -->
## TOPIC 01095: GetNumTableColumns

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetnumtablecolumns.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetnumtablecolumns.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumTableColumns

int GetNumTableColumns (int panelHandle, int controlID, int *numberOfColumns);

#### Purpose

Returns the number of columns in the specified table control.

#### Supported Controls

You can use GetNumTableColumns with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| numberOfColumns | int | The number of columns in the specified table control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetnumtablerows.htm language=enus -->
## TOPIC 01096: GetNumTableRows

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetnumtablerows.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetnumtablerows.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumTableRows

int GetNumTableRows (int panelHandle, int controlID, int *numberOfRows);

#### Purpose

Returns the number of rows in the specified table control.

#### Supported Controls

You can use GetNumTableRows with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| numberOfRows | int | The number of rows in the specified table control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the GetNumTableRows function:

- userint\colview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\tablecells.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\ParallelTestInit\ParallelTestInit.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetnumtabpages.htm language=enus -->
## TOPIC 01097: GetNumTabPages

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetnumtabpages.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetnumtabpages.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumTabPages

int GetNumTabPages (int panelHandle, int controlID, int *count);

#### Purpose

Returns the number of tab pages in the tab control.

#### Supported Controls

You can use GetNumTabPages with [tab controls](../../cvi/uiref/cviprogramming_with_tab_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| count | int | The number of tab pages in the tab control. Because the indices are zero based, this value is one greater than the index of the last item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

#### Examples

Refer to the following examples that use the GetNumTabPages function:

- udp\UDPChat.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\events.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetnumtextboxlines.htm language=enus -->
## TOPIC 01098: GetNumTextBoxLines

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetnumtextboxlines.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetnumtextboxlines.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumTextBoxLines

int GetNumTextBoxLines (int panelHandle, int controlID, int *count);

#### Purpose

Returns the number of lines of text in the specified text box, including lines not
currently in the viewing area of the text box.

#### Supported Controls

You can use GetNumTextBoxLines with [text box controls](../../cvi/uiref/cviprogramming_with_text_box_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| count | int | The number of lines of text in the text box. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetnumtreecellringitems.htm language=enus -->
## TOPIC 01099: GetNumTreeCellRingItems

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetnumtreecellringitems.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetnumtreecellringitems.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumTreeCellRingItems

int GetNumTreeCellRingItems (int panelHandle, int controlID, int itemIndex, int columnIndex, int *numberOfItems);

#### Purpose

Returns the number of items in the list of values of a specified ring or combo box cell of a tree control.

#### Supported Controls

You can use GetNumTreeCellRingItems with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item containing the cell for which you want to get the number of ring or combo box items. |
| columnIndex | int | Zero-based index of the tree column that contains the cell for which you want to get the number of ring or combo box items. |
| Output |  |  |
| Name | Type | Description |
| numberOfItems | int | The number of items in the list of values. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetnumtreecolumns.htm language=enus -->
## TOPIC 01100: GetNumTreeColumns

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetnumtreecolumns.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetnumtreecolumns.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumTreeColumns

int GetNumTreeColumns (int panelHandle, int controlID, int *count);

#### Purpose

Returns the number of columns in the tree control.

#### Supported Controls

You can use GetNumTreeColumns with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| count | int | The number of columns in the tree control. Because the indices are zero based, this value is one greater than the index of the last column. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetnumtreeitems.htm language=enus -->
## TOPIC 01101: GetNumTreeItems

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetnumtreeitems.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetnumtreeitems.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetNumTreeItems

int GetNumTreeItems (int panelHandle, int controlID, int relation, int relativeIndex, int beginIndex, int direction, int stateCriteria, int *count);

#### Purpose

Counts the number of items that have the specified relation to the relative index. The count starts at **beginIndex** and proceeds in the specified direction. Counts only those items that meet the **stateCriteria**.

To get the number of all the items in the tree, use [GetNumListItems](../../cvi/uiref/cvigetnumlistitems.htm).

#### Supported Controls

You can use GetNumTreeItems with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| relation | int | Defines the relationship between the relative item and the items to be counted. You can select the following values: VAL_ALL—Count all items regardless of their relationship to the relative item. VAL_SIBLING—Count only items that are siblings of the relative item. VAL_CHILD—Count only items that are children of the relative item. VAL_DESCENDENT—Count all items that are descendents of the relative item. VAL_ANCESTOR—Count all items that are ancestors of the relative item. |
| relativeIndex | int | Identifies the relative of the items to be counted. All items in the specified direction that match the relationship to the relative item will be counted. |
| beginIndex | int | Zero-based index of the item where the count begins. If beginIndex does not equal relativeIndex, the item at beginIndex must be related to the item at relativeIndex as specified by relation. Use VAL_FIRST to start at the first item that meets the relation requirement to the relative index. The first ancestor is the parent. |
| direction | int | Defines the direction of the items from beginIndex to count. You can select the following values: VAL_NEXT—Include the items below beginIndex in the count. VAL_NEXT_PLUS_SELF—Include the items below beginIndex, along with the item at beginIndex, in the count. VAL_PREV—Include the items above beginIndex in the count. VAL_PREV_PLUS_SELF—Include the items above beginIndex, along with the item at beginIndex, in the count. |
| stateCriteria | int | Defines the state of the items to be counted. Use any combination of the following masks to define the state of the items to be counted: VAL_SELECTED Item that is selected VAL_UNSELECTED Item that is unselected VAL_EXPOSED Item with all ancestors expanded VAL_UNEXPOSED Item with at least one ancestor collapsed VAL_MARKED Item whose radio button or check box is marked VAL_UNMARKED Item whose radio button or check box is not marked VAL_PARTIALLY_MARKED Item whose radio button or check box is partially marked VAL_EXPANDED Item that has children and is expanded VAL_COLLAPSED Item that has children and is collapsed VAL_LEAF Item that does not have children VAL_NON_LEAF Item that has children For example, if you pass (VAL_SELECTED \| VAL_MARKED) the function will only count items that are selected as well as marked. Pass 0 to count items regardless of their state. |
| VAL_SELECTED | Item that is selected |  |
| VAL_UNSELECTED | Item that is unselected |  |
| VAL_EXPOSED | Item with all ancestors expanded |  |
| VAL_UNEXPOSED | Item with at least one ancestor collapsed |  |
| VAL_MARKED | Item whose radio button or check box is marked |  |
| VAL_UNMARKED | Item whose radio button or check box is not marked |  |
| VAL_PARTIALLY_MARKED | Item whose radio button or check box is partially marked |  |
| VAL_EXPANDED | Item that has children and is expanded |  |
| VAL_COLLAPSED | Item that has children and is collapsed |  |
| VAL_LEAF | Item that does not have children |  |
| VAL_NON_LEAF | Item that has children |  |
| Output |  |  |
| Name | Type | Description |
| count | int | The number of items in the tree control that match the specified relationship to the relative index that also meet the requirements of stateCriteria. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetobjhandlefromactivexctrl.htm language=enus -->
## TOPIC 01102: GetObjHandleFromActiveXCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetobjhandlefromactivexctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetobjhandlefromactivexctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetObjHandleFromActiveXCtrl

int GetObjHandleFromActiveXCtrl (int panelHandle, int controlID, CAObjHandle *objectHandle);

#### Purpose

Obtains the CAObjHandle that is created when the ActiveX control is created.

(Linux) This function is not supported.

The CAObjHandle is created with multithreading support and LOCALE_NEUTRAL. Refer to CA_SetSupportForMultithreading and CA_SetLocale to change these default settings.

#### Supported Controls

You can use GetObjHandleFromActiveXCtrl with [ActiveX controls](../../cvi/uiref/cviprogramming_with_activex_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| objectHandle | CAObjHandle | The CAObjHandle associated with the specified ActiveX control. Use this handle to call methods or get and set properties of this Automation object. If the control does not have any methods or properties, this handle is set to 0. This handle is cached by the ActiveX control and will be discarded when the control is discarded. You do not need to discard the handle. Note If you call RecallPanelState after obtaining the CAObjHandle, that handle is no longer valid. You must obtain a new handle after each time you call RecallPanelState. |
|  | Note If you call RecallPanelState after obtaining the CAObjHandle, that handle is no longer valid. You must obtain a new handle after each time you call RecallPanelState. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

#### Examples

Refer to the following examples that use the GetObjHandleFromActiveXCtrl function:

- userint\activex\3DGraph.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\activex\3DGraphAxis.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\activex\3DGraphColorMap.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\activex\richTextbox.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\activex\WebBrowser.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetpanelattribute.htm language=enus -->
## TOPIC 01103: GetPanelAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetpanelattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetpanelattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetPanelAttribute

int GetPanelAttribute (int panelHandle, int panelAttribute, void *attributeValue);

#### Purpose

Returns the value of a specific panel attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| panelAttribute | int | The panel attribute value to obtain. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help is shown for each attribute. Select an attribute by double-clicking it or by selecting it and then pressing <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. If there is a value shown in the bottom half of the Attribute Value control, the corresponding named constant is marked in the displayed list. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | Current value of the panel attribute. The data type for this parameter depends on the data type of the attribute you specify for the panelAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to panelAttribute. If the attribute shown in this control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the GetPanelAttribute function:

- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\tabpanels.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetplotattribute.htm language=enus -->
## TOPIC 01104: GetPlotAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetplotattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetplotattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetPlotAttribute

int GetPlotAttribute (int panelHandle, int controlID, int plotHandle, int plotAttribute, void *attributeValue);

#### Purpose

Obtains the value of a graph plot attribute.

#### Supported Controls

You can use GetPlotAttribute with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| plotHandle | int | Handle for a particular plot in the graph. You obtain the handle from one of the following functions. PlotX PlotY PlotXY PlotWaveform PlotPoint PlotText PlotLine PlotRectangle PlotPolygon PlotOval PlotArc PlotIntensity PlotScaledIntensity PlotBitmap |
| plotAttribute | int | The plot attribute value to obtain. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified plot attribute. The data type for this parameter depends on the data type of the attribute you specify for the plotAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to plotAttribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attributes Value dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the GetPlotAttribute function:

- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\GraphZooming.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetprintattribute.htm language=enus -->
## TOPIC 01105: GetPrintAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetprintattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetprintattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetPrintAttribute

int GetPrintAttribute (int printAttribute, void *attributeValue);

#### Purpose

Returns the value of a specific print attribute.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| printAttribute | int | The print attribute value to obtain. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified print attribute. The data type for this parameter depends on the data type of the attribute you specify for the printAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to printAttribute. If the attribute shown in this control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetrealfonttypefacename.htm language=enus -->
## TOPIC 01106: GetRealFontTypefaceName

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetrealfonttypefacename.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetrealfonttypefacename.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetRealFontTypefaceName

int GetRealFontTypefaceName (char *fontName, char typefaceName[]);

#### Purpose

Returns the name of the actual typeface used by the operating system.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fontName | char * | The name of an existing font.The font can be a predefined font; a predefined NI metafont; a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx; or a font, such as Courier New, supplied by the operating system. Predefined fonts—Contain typeface information only and use typefaces native to the operating system. The predefined fonts are VAL_MENU_FONT, VAL_DIALOG_FONT, VAL_EDITOR_FONT, VAL_APP_FONT, and VAL_MESSAGE_BOX_FONT. Predefined metafonts—Contain typeface information, point size, and text styles such as bold, underline, italic, and strikeout. These metafonts are used in the LabWindows/CVI environment. The predefined metafonts are VAL_MENU_META_FONT, VAL_DIALOG_META_FONT, VAL_EDITOR_META_FONT, VAL_APP_META_FONT, and VAL_MESSAGE_BOX_META_FONT. LabWindows/CVI-supplied metafonts—Use typefaces that are not native to the operating system. These metafonts are installed while LabWindows/CVI is running. The LabWindows/CVI-supplied metafonts are VAL_7SEG_META_FONT and VAL_SYSTEM_META_FONT. |
| Output |  |  |
| Name | Type | Description |
| typefaceName | char [] | The corresponding typeface name string. You must pass a buffer large enough to hold the corresponding typeface name string, plus the terminating NUL byte. Use GetRealFontTypefaceNameLength to obtain the length, in bytes, of the string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetrealfonttypefacenamelength.htm language=enus -->
## TOPIC 01107: GetRealFontTypefaceNameLength

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetrealfonttypefacenamelength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetrealfonttypefacenamelength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetRealFontTypefaceNameLength

int GetRealFontTypefaceNameLength (char *fontName, int *typefaceNameLength);

#### Purpose

Returns the length, in bytes, of the string containing the name of the actual typeface used by the operating system.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fontName | char * | The name of an existing font.The font can be a predefined font; a predefined NI metafont; a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx; or a font, such as Courier New, supplied by the operating system. Predefined fonts—Contain typeface information only and use typefaces native to the operating system. The predefined fonts are VAL_MENU_FONT, VAL_DIALOG_FONT, VAL_EDITOR_FONT, VAL_APP_FONT, and VAL_MESSAGE_BOX_FONT. Predefined metafonts—Contain typeface information, point size, and text styles such as bold, underline, italic, and strikeout. These metafonts are used in the LabWindows/CVI environment. The predefined metafonts are VAL_MENU_META_FONT, VAL_DIALOG_META_FONT, VAL_EDITOR_META_FONT, VAL_APP_META_FONT, and VAL_MESSAGE_BOX_META_FONT. LabWindows/CVI-supplied metafonts—Use typefaces that are not native to the operating system. These metafonts are installed while LabWindows/CVI is running. The LabWindows/CVI-supplied metafonts are VAL_7SEG_META_FONT and VAL_SYSTEM_META_FONT. |
| Output |  |  |
| Name | Type | Description |
| typefaceNameLength | int | The length, in bytes, of the typeface name string corresponding to the font specified. The length does not include the terminating NUL byte. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetrelativemousestate.htm language=enus -->
## TOPIC 01108: GetRelativeMouseState

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetrelativemousestate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetrelativemousestate.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetRelativeMouseState

int GetRelativeMouseState (int panelHandle, int controlID, int *xCoordinate, int *yCoordinate, int *leftButtonDown, int *rightButtonDown, int *keyModifiers);

#### Purpose

Obtains information about the state of the mouse cursor. **xCoordinate** and **yCoordinate** return the position of the mouse relative to the top and left coordinates of
a specific control. If you pass zero as the **controlID**, the coordinate information references the top and left coordinates of the panel, excluding the panel frame and title bar. GetRelativeMouseState returns the coordinates even if the mouse is not over the control or the
panel.

#### Supported Controls

You can use GetRelativeMouseState with all LabWindows/CVI [user interface controls](../../cvi/uiref/cvioperating_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | Defined constant, located in the .uir header file, that you assign to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. You can pass 0 if you want the coordinate information to be relative to the top and left coordinates of the panel, excluding the frame and title bar. |
| Output |  |  |
| Name | Type | Description |
| xCoordinate | int | X-coordinate of the mouse cursor relative to the left edge of the control, or panel, if controlID is 0. You can pass NULL. |
| yCoordinate | int | Y-coordinate of the mouse cursor relative to the top of the control, or panel, if controlID is 0. You can pass NULL. |
| leftButtonDown | int | The state of the left mouse button. 0 if the left button is up. 1 if the left button is down. You can pass NULL. |
| rightButtonDown | int | The state of the right mouse button. 0 if the right button is up. 1 if the right button is down. You can pass NULL. |
| keyModifiers | int | State of the keyboard modifiers, in other words, the <Ctrl>, <Alt>, and <Shift> keys. If no keys are down, the value is 0. Otherwise, the value is the bitwise OR of the appropriate key masks: VAL_MENUKEY_MODIFIER, VAL_UNDERLINE_MODIFIER, VAL_SHIFT_MODIFIER, and VAL_SHIFT_AND_MENUKEY. You can pass NULL. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Examples

Refer to the following examples that use the GetRelativeMouseState function:

- apps\life\life.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvas.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\moustate.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\custctrl\cviogl\oglarm.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetringitemattribute.htm language=enus -->
## TOPIC 01109: GetRingItemAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetringitemattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetringitemattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetRingItemAttribute

int GetRingItemAttribute (int panelHandle, int controlID, int itemIndex, int itemAttribute, void *attributeValue);

#### Purpose

Obtains the value of a ring control item attribute.

#### Supported Controls

You can use GetRingItemAttribute with [ring controls](../../cvi/uiref/cviprogramming_with_ring_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the ring control item from which the function obtains the attribute value. |
| itemAttribute | int | The ring item attribute value to obtain. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified ring item attribute. The data type for this parameter depends on the data type of the attribute you specify for the itemAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to itemAttribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetscaledpaneldisplaybitmap.htm language=enus -->
## TOPIC 01110: GetScaledPanelDisplayBitmap

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetscaledpaneldisplaybitmap.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetscaledpaneldisplaybitmap.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetScaledPanelDisplayBitmap

int GetScaledPanelDisplayBitmap (int panelHandle, int scope, Rect area, int newHeight, int newWidth, int *bitmapID);

#### Purpose

Creates a bitmap object that contains a screenshot image of the current appearance of a panel. **newHeight** and **newWidth** determine the dimensions of the bitmap. The image stretches or shrinks to fit the specified dimensions.

You can use GetScaledPanelDisplayBitmap to retrieve a scaled bitmap that you can pass to [ClipboardPutBitmap](../../cvi/uiref/cviclipboardputbitmap.htm). From the clipboard, you can paste the picture of the control into another application in the size you want for that application.

To discard the bitmap object, pass its ID to [DiscardBitmap](../../cvi/uiref/cvidiscardbitmap.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| scope | int | Specifies which portions of the panel to copy to the bitmap. Select one of the following values: VAL_VISIBLE_AREA—Copies the visible area of the panel to the bitmap, including the frame, menu bar, and scroll bars. VAL_FULL_PANEL—Copies the entire contents of the panel to the bitmap, excluding the frame, menu bar, and scroll bars. This includes contents that might currently be scrolled off the visible area. Note If you select VAL_VISIBLE_AREA, the panel title bar and frame have the appearance of child panels in the bitmap. This behavior occurs for both top-level panels and child panels. Regardless of the scope, objects within child panels are clipped to the frame of the child panel. |
|  | Note If you select VAL_VISIBLE_AREA, the panel title bar and frame have the appearance of child panels in the bitmap. This behavior occurs for both top-level panels and child panels. |  |
| area | Rect | Restricts the area of the panel to copy into the bitmap. You must pass a Rect structure. The rectangle coordinates, specified in pixels, are relative to the upper-left corner of the panel, directly below the title bar, before the panel is scrolled. Use VAL_ENTIRE_OBJECT if you do not want to restrict the area to copy. |
| newHeight | int | The height, in pixels, of the bitmap image. Values: 1 to 32,767, or pass –1 to use the height of the panel on the screen. If you pass VAL_ENTIRE_OBJECT for the area parameter, newHeight specifies the exact height of the scaled bitmap. Otherwise, GetScaledPanelDisplayBitmap calculates the bitmap height as follows: bitmap height = newHeight/height of panel on screen × area.height |
| newWidth | int | The width, in pixels, of the bitmap image. Values: 1 to 32,767, or pass –1 to use the width of the panel on the screen. If you pass VAL_ENTIRE_OBJECT for the area parameter, newWidth specifies the exact width of the scaled bitmap. Otherwise, GetScaledPanelDisplayBitmap calculates the bitmap width as follows: bitmap width = newWidth/width of panel on screen × area.width |
| Output |  |  |
| Name | Type | Description |
| bitmapID | int | ID that serves as a handle to the bitmap object. You can pass the ID to functions that accept a bitmap, such as CanvasDrawBitmap and ClipboardPutBitmap. To discard the bitmap, pass the ID to DiscardBitmap. Zero is not a valid bitmap ID. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettablecellringitemattribute.htm language=enus -->
## TOPIC 01111: GetTableCellRingItemAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettablecellringitemattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettablecellringitemattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTableCellRingItemAttribute

int GetTableCellRingItemAttribute (int panelHandle, int controlID, Point cell, int index, int itemAttribute, void *attributeValue);

#### Purpose

Obtains the value of a ring item attribute. Use this function to interact with table cells whose [type](../../cvi/uiref/cviattrcelltype_cell.htm) is ring or combo box.

#### Supported Controls

You can use GetTableCellRingItemAttribute with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cell | Point | A Point structure specifying the cell that contains the ring item. The specified cell must be of type VAL_CELL_RING or VAL_CELL_COMBO_BOX. The Point structure is defined as follows: typedef struct { int x; int y; } Point; Pass the one-based column index of the cell in the x field of the structure, and the one-based row index of the cell in the y field of the structure. You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example GetTableCellRingAttribute (panelHandle, controlID, MakePoint (2, 3), 0, ATTR_BOLD, &isBold); |
| index | int | The zero-based index into the list of values. |
| itemAttribute | int | The ring item attribute value to get. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified ring item attribute. The data type for this parameter depends on the data type of the attribute you specify for the itemAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to itemAttribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettablecellringvaluefromindex.htm language=enus -->
## TOPIC 01112: GetTableCellRingValueFromIndex

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettablecellringvaluefromindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettablecellringvaluefromindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTableCellRingValueFromIndex

int GetTableCellRingValueFromIndex (int panelHandle, int controlID, Point cell, int index, char value[]);

#### Purpose

Returns the value of a specified item of the list of values of a specified ring or combo-box cell of a table control.

#### Supported Controls

You can use GetTableCellRingValueFromIndex with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cell | Point | A Point structure specifying the cell from which you want to obtain the value. The specified cell must be of type VAL_CELL_RING or VAL_CELL_COMBO_BOX. The Point structure is defined as follows: typedef struct { int x; int y; } Point; Pass the one-based column index of the cell in the x field of the structure, and the one-based row index of the cell in the y field of the structure. You can create a Point without having to declare a variable by using the following function: Point MakePoint (int x, int y); Example GetTableCellRingValueFromIndex (panelHandle, controlID, MakePoint (2, 3), 0, buffer); |
| index | int | The zero-based index into the list of values. |
| Output |  |  |
| Name | Type | Description |
| value | char [] | Buffer into which the value of the specified item is stored. The number of bytes in this buffer must be at least one byte greater than the value returned by GetTableCellRingValueLengthFromIndex for this list item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettablerowfromlabel.htm language=enus -->
## TOPIC 01113: GetTableRowFromLabel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettablerowfromlabel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettablerowfromlabel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTableRowFromLabel

int GetTableRowFromLabel (int panelHandle, int controlID, int beginningRowIndex, int *rowIndex, char label[], int visibleLabelsOnly);

#### Purpose

Returns the index of the first row with a label matching the 
specified label.

The function searches the labels you set using the [ATTR_LABEL_TEXT](../../cvi/uiref/cviattruselabeltext_row.htm) row attribute, not the string representations of the numerical indices of the rows, which are the row labels you see by 
default.

This function returns an index of –1 if the label is not found.

#### Supported Controls

You can use GetTableRowFromLabel with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| beginningRowIndex | int | The one-based index of the first row you want the function to search. |
| label | char [] | The label you want to locate in the table rows. You can pass an empty string if you want the function to return the index of the first row not containing a label. |
| visibleLabelsOnly | int | Specify a nonzero value or select Yes in the function panel to include in the search only rows with visible labels. Specify 0 or select No in the function panel to include in the search rows for which labels are not visible. For the labels to be visible, you must set the row attributes ATTR_USE_LABEL_TEXT and ATTR_LABEL_VISIBLE to TRUE. ATTR_USE_LABEL_TEXT is set to FALSE by default. |
| Output |  |  |
| Name | Type | Description |
| rowIndex | int | The one-based index of the first row with the specified label. The function searches the labels you set using the ATTR_LABEL_TEXT row attribute, not the string representations of the numerical indices of the rows, which are the row labels you see by default. The function returns an index of –1 if the value is not found. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettableselection.htm language=enus -->
## TOPIC 01114: GetTableSelection

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettableselection.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettableselection.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTableSelection

int GetTableSelection (int panelHandle, int controlID, Rect *cellRange);

#### Purpose

Returns the cells in the current cell selection.

#### Supported Controls

You can use GetTableSelection with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| Output |  |  |
| Name | Type | Description |
| cellRange | Rect | A Rect structure containing the location and size of the current cell selection. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; The function writes the one-based row and column indices of the first cell in the selection into the top and left fields of the structure, respectively. The function writes the number of columns in the selection into the width field of the structure, and it writes the number of rows in the selection into the height field of the structure. The function returns an empty rect (VAL_EMPTY_RECT) if the cell selection is empty (the default state). Note that the table selection is distinct from the active cell, and whereas there always exists an active cell (i.e. the cell holding the keyboard focus), the selection consists of a rectangular cell range that can be empty. The only relationship between the active cell and the selection is that, if the selection is non-empty, the active cell is always contained within the selection |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Example

Refer to userint\databinding.cws for an example of using the GetTableSelection function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettextboxlineoffset.htm language=enus -->
## TOPIC 01115: GetTextBoxLineOffset

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettextboxlineoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettextboxlineoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTextBoxLineOffset

int GetTextBoxLineOffset (int panelHandle, int controlID, int lineIndex, int *offsetOfFirstCharacter);

#### Purpose

Returns the byte offset of the first character in the specified line of the text box.

#### Supported Controls

You can use GetTextBoxLineOffset with [text box controls](../../cvi/uiref/cviprogramming_with_text_box_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| lineIndex | int | Zero-based index into the text box. |
| Output |  |  |
| Name | Type | Description |
| offsetOfFirstCharacter | int | The offset of the first character in the specified line of the text box. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettimertickdata.htm language=enus -->
## TOPIC 01116: GetTimerTickData

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettimertickdata.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettimertickdata.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTimerTickData

int GetTimerTickData (double *eventTime, double *timeSinceLastCallback);

#### Purpose

Returns the time of the current [EVENT_TIMER_TICK](../../cvi/uiref/cvieventtimertick.htm) callback and the time elapsed since the last EVENT_TIMER_TICK callback.

You must call GetTimerTickData inside the timer's callback function when it receives an EVENT_TIMER_TICK event. If you call GetTimerTickData outside of an EVENT_TIMER_TICK callback event, LabWindows/CVI returns a stale data error.

GetTimerTickData is the only way to get the time values from an EVENT_TIMER_TICK event in a 64-bit executable.

You can pass NULL for either parameter but not for both.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventTime | double | The time value when the EVENT_TIMER_TICK event was generated. |
| timeSinceLastCallback | double | The time elapsed since the last EVENT_TIMER_TICK event was generated. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

#### Example

Refer to toolbox\asyncdem.cws for an example of using the GetTimerTickData function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettraceattribute.htm language=enus -->
## TOPIC 01117: GetTraceAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettraceattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettraceattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTraceAttribute

int GetTraceAttribute (int panelHandle, int controlID, int traceNumber, int traceAttribute, void *attributeValue);

#### Purpose

Obtains the value of a strip chart trace attribute.

#### Supported Controls

You can use GetTraceAttribute with [strip chart controls](../../cvi/uiref/cviprogramming_with_strip_chart_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| traceNumber | int | Identifies a strip chart trace. traceNumber can be from 1 to the number of defined strip chart traces. You can set the number of strip chart traces in the User Interface Editor or through SetCtrlAttribute. |
| traceAttribute | int | The strip chart trace attribute value to obtain. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified trace attribute. The data type for this parameter depends on the data type of the attribute you specify for the traceAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to traceAttribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreecellattribute.htm language=enus -->
## TOPIC 01118: GetTreeCellAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreecellattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreecellattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeCellAttribute

int GetTreeCellAttribute (int panelHandle, int controlID, int itemIndex, int columnIndex, int cellAttribute, void *attributeValue);

#### Purpose

Obtains an attribute of a tree cell.

#### Supported Controls

You can use GetTreeCellAttribute with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item that contains the cell for which you want to get the attribute value. Pass VAL_DFLT_FOR_NEW_OBJECTS to get the default attribute for cells created in the future in the specified column. |
| columnIndex | int | Zero-based index of the tree column that contains the cell for which you want to get the attribute value. |
| cellAttribute | int | The cell attribute whose value you want to obtain. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified cell attribute. The data type for this parameter depends on the data type of the attribute you specify for the cellAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to cellAttribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreecellringindexfromvalue.htm language=enus -->
## TOPIC 01119: GetTreeCellRingIndexFromValue

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreecellringindexfromvalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreecellringindexfromvalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeCellRingIndexFromValue

int GetTreeCellRingIndexFromValue (int panelHandle, int controlID, int itemIndex, int columnIndex, int beginningRingIndex, int *index, char value[]);

#### Purpose

Searches the list of values of a specified ring or combo box cell of a tree control and returns the index of the first item in the list with a value matching the specified value.

This function returns the index –1 if the value is not found.

#### Supported Controls

You can use GetTreeCellRingIndexFromValue with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item containing the cell in which you want to search. |
| columnIndex | int | Zero-based index of the tree column that contains the cell in which you want to search. |
| beginningRingIndex | int | The zero-based index specifying the first item the function searches. |
| value | char [] | The value you want to locate in the list. The comparison is case-sensitive. |
| Output |  |  |
| Name | Type | Description |
| index | int | The zero-based index of the item matching the specified value. Returns –1 if no match is found. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreecellringitemattribute.htm language=enus -->
## TOPIC 01120: GetTreeCellRingItemAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreecellringitemattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreecellringitemattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeCellRingItemAttribute

int GetTreeCellRingItemAttribute (int panelHandle, int controlID, int itemIndex, int columnIndex, int ringIndex, int itemAttribute, void *attributeValue);

#### Purpose

Obtains the value of a ring item attribute. Use this function to interact with tree cells whose [type](../../cvi/uiref/cviattrcelltype_tree cell.htm) is ring or combo box.

#### Supported Controls

You can use GetTreeCellRingItemAttribute with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item that contains the cell of the ring item. |
| columnIndex | int | Zero-based index of the tree column that contains the cell of the ring item. |
| ringIndex | int | The zero-based index specifying the ring item. |
| itemAttribute | int | The ring item attribute value to get. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified ring item attribute. The data type for this parameter depends on the data type of the attribute you specify for the itemAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to itemAttribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreecellringvaluefromindex.htm language=enus -->
## TOPIC 01121: GetTreeCellRingValueFromIndex

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreecellringvaluefromindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreecellringvaluefromindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeCellRingValueFromIndex

int GetTreeCellRingValueFromIndex (int panelHandle, int controlID, int itemIndex, int columnIndex, int ringIndex, char value[]);

#### Purpose

Returns the value of a specified item of the list of values of a specified ring or combo box cell of a tree control.

#### Supported Controls

You can use GetTreeCellRingValueFromIndex with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item containing the cell from which you want to obtain the value. |
| columnIndex | int | The zero-based index of the tree column containing the cell from which you want to obtain the value. |
| ringIndex | int | The zero-based index of the item in the list of values. |
| Output |  |  |
| Name | Type | Description |
| value | char [] | Buffer into which the value of the specified item is stored. The number of bytes in this buffer must be at least one byte greater than the value returned by GetTreeCellRingValueLengthFromIndex for this list item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreecellringvaluelengthfromindex.htm language=enus -->
## TOPIC 01122: GetTreeCellRingValueLengthFromIndex

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreecellringvaluelengthfromindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreecellringvaluelengthfromindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeCellRingValueLengthFromIndex

int GetTreeCellRingValueLengthFromIndex (int panelHandle, int controlID, int itemIndex, int columnIndex, int ringIndex, int *length);

#### Purpose

Returns the value length, in bytes, of a specified item of the list of values of a specified ring or combo box cell of a tree control.

#### Supported Controls

You can use GetTreeCellRingValueLengthFromIndex with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item containing the cell from which you want to obtain the value length. |
| columnIndex | int | The zero-based index of the tree column containing the cell from which you want to obtain the value length. |
| ringIndex | int | The zero-based index of the item in the list of values. |
| Output |  |  |
| Name | Type | Description |
| length | int | The number of bytes in the value of the specified item. The length does not include the terminating NUL byte. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreecolumnattribute.htm language=enus -->
## TOPIC 01123: GetTreeColumnAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreecolumnattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreecolumnattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeColumnAttribute

int GetTreeColumnAttribute (int panelHandle, int controlID, int columnIndex, int columnAttribute, void *attributeValue);

#### Purpose

Obtains an attribute of a tree column.

#### Supported Controls

You can use GetTreeColumnAttribute with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| columnIndex | int | Zero-based index of the tree column from which the function obtains the attribute. |
| columnAttribute | int | The column attribute whose value you want to obtain. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified column attribute. The data type for this parameter depends on the data type of the attribute you specify for the columnAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to columnAttribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitem.htm language=enus -->
## TOPIC 01124: GetTreeItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItem

int GetTreeItem (int panelHandle, int controlID, int relation, int relativeIndex, int beginIndex, int direction, int stateCriteria, int *item);

#### Purpose

Searches for an item that is **relation** to **relativeIndex**. The search starts at **beginIndex** and proceeds in the direction specified by **direction**.

Returns in the **item** parameter the index of the first item that meets **stateCriteria**.

Refer to the [GetTreeItemFromLabel](../../cvi/uiref/cvigettreeitemfromlabel.htm) function reference for an example of how to use this and other tree control functions.

#### Supported Controls

You can use GetTreeItem with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| relation | int | Defines the relationship between the relative index and the items to be searched. You can select the following values. VAL_ALL—Search all items regardless of their relationship to the relative item. VAL_SIBLING—Search only items that are siblings of the relative item. VAL_CHILD—Search only items that are children of the relative item. VAL_DESCENDENT—Search all items that are descendents of the relative item. VAL_ANCESTOR—Search all items that are ancestors of the relative item. |
| relativeIndex | int | Zero-based index of the item whose relatives defined by the relation parameter will be searched. |
| beginIndex | int | Zero-based index of the item where the search begins. If beginIndex does not equal relativeIndex, the item at beginIndex must be related to the item at relativeIndex as specified by relation. Use VAL_FIRST to start at the first item that meets the relation requirement to the relative index. The first ancestor is the parent of the relative item. Use VAL_LAST to start at the last item that meets the relation requirement to the relative index. The last ancestor is the ancestor of the relative item that is on level zero. |
| direction | int | Defines the direction of the items from beginIndex to search. You can select the following values: VAL_NEXT—Include the items below beginIndex in the search. The exception to this is when relation is VAL_ANCESTOR, in which case next means towards the root. VAL_NEXT_PLUS_SELF—Same as VAL_NEXT, except that the item at beginIndex is included in the search. VAL_PREV—Include the items above beginIndex in the search. The exception to this is when relation is VAL_ANCESTOR, in which case previous means towards the relative index. VAL_PREV_PLUS_SELF—Same as VAL_PREV, except that the item at beginIndex is included in the search. |
| stateCriteria | int | Defines the state of the searched for item. Use any combination of the following masks to define the state of the searched for item: VAL_SELECTED Item that is selected VAL_UNSELECTED Item that is unselected VAL_EXPOSED Item with all ancestors expanded VAL_UNEXPOSED Item with at least one ancestor collapsed VAL_MARKED Item whose radio button or check box is marked VAL_UNMARKED Item whose radio button or check box is not marked VAL_PARTIALLY_MARKED Item whose radio button or check box is partially marked VAL_EXPANDED Item that has children and is expanded VAL_COLLAPSED Item that has children and is collapsed VAL_LEAF Item that does not have children VAL_NON_LEAF Item that has children For example, if you pass (VAL_SELECTED \| VAL_MARKED) the function will search for an item that is selected as well as marked. Pass 0 to count items regardless of their state. |
| VAL_SELECTED | Item that is selected |  |
| VAL_UNSELECTED | Item that is unselected |  |
| VAL_EXPOSED | Item with all ancestors expanded |  |
| VAL_UNEXPOSED | Item with at least one ancestor collapsed |  |
| VAL_MARKED | Item whose radio button or check box is marked |  |
| VAL_UNMARKED | Item whose radio button or check box is not marked |  |
| VAL_PARTIALLY_MARKED | Item whose radio button or check box is partially marked |  |
| VAL_EXPANDED | Item that has children and is expanded |  |
| VAL_COLLAPSED | Item that has children and is collapsed |  |
| VAL_LEAF | Item that does not have children |  |
| VAL_NON_LEAF | Item that has children |  |
| Output |  |  |
| Name | Type | Description |
| item | int | The index of the first item in the tree control that has the specified relationship with the relative index that also meets the requirements of stateCriteria. –1 indicates that no item meets the search requirements. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to apps\uirview\uirview.cws for an example of using the GetTreeItem function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemattribute.htm language=enus -->
## TOPIC 01125: GetTreeItemAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemAttribute

int GetTreeItemAttribute (int panelHandle, int controlID, int itemIndex, int itemAttribute, void *attributeValue);

#### Purpose

Obtains an attribute of a tree item.

#### Supported Controls

You can use GetTreeItemAttribute with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item from which the function obtains the attribute. Pass VAL_DFLT_FOR_NEW_OBJECTS to get the default attribute for items that are created in the future. |
| itemAttribute | int | The item attribute whose value you want to obtain. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| Output |  |  |
| Name | Type | Description |
| attributeValue | void * | The value of the specified item attribute. The data type for this parameter depends on the data type of the attribute you specify for the itemAttribute parameter. Pass the address of a variable of the same data type of the attribute you pass to itemAttribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Examples

Refer to the following examples that use the GetTreeItemAttribute function:

- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\TreeBusDigitalGraph.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemfromlabel.htm language=enus -->
## TOPIC 01126: GetTreeItemFromLabel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemfromlabel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemfromlabel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemFromLabel

int GetTreeItemFromLabel (int panelHandle, int controlID, int relation, int relativeIndex, int beginIndex, int direction, int stateCriteria, char itemLabel[], int *item);

#### Purpose

Searches for an item with the specified label. The search range is defined by the **relation** and the **relativeIndex**. The search starts at **beginIndex** and proceeds in the direction specified by **direction**.

Returns in the **item** parameter the index of the first item that has the specified label and that meets **stateCriteria**.

##### Example Code

The following example code demonstrates how to search for and select tree items that have the specified label text. The example assumes that the **Selection Mode** for the tree is set to **Multiple**.

int CVICALLBACK SearchTree (int panel, int control, int event,
 void *callbackData, int eventData1, int eventData2)

{

char label[256];

int  item = 0, 

      beginIndex = VAL_FIRST, 

      direction = VAL_NEXT_PLUS_SELF, 

      firstIteration = 1;

switch (event)

{

case EVENT_COMMIT:

/* Get the search string from the user interface */

GetCtrlVal (panelHandle, PANEL_SEARCH_STRING, label);

/* Iterate from the active tree item until there are no more matches to find */

while (item!=-1)

{

GetTreeItemFromLabel (panelHandle, PANEL_TREE, VAL_ALL, 0, beginIndex,
 direction, 0, label, &item);

/* On the next iteration, start from current item */

beginIndex = item;

if (item!=-1)

{

/* Select the tree item if its label matches the specified search string */

SetTreeItemAttribute (panelHandle, PANEL_TREE, item, ATTR_SELECTED, 1);

}

/* If the item is not found on the first iteration, pop up a message indicating there are no matches */

else if (firstIteration)

{

MessagePopup ("No match", "The search string does not match any tree item labels.");

}

/* After the first iteration, no longer include the beginIndex item in the search */

if (firstIteration)

{

direction = VAL_NEXT;

firstIteration = 0;

}

}

break;

}

return 0;

}

#### Supported Controls

You can use GetTreeItemFromLabel with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| relation | int | Defines the relationship between the relative index and the items to be searched. You can select the following values: VAL_ALL—Search all items regardless of their relationship to the relative item. VAL_SIBLING—Search only items that are siblings of the relative item. VAL_CHILD—Search only items that are children of the relative item. VAL_DESCENDENT—Search all items that are descendents of the relative item. VAL_ANCESTOR—Search all items that are ancestors of the relative item. |
| relativeIndex | int | Zero-based index of the item whose relatives defined by the relation parameter will be searched. |
| beginIndex | int | Zero-based index of the item where the search begins. If beginIndex does not equal relativeIndex, the item at beginIndex must be related to the item at relativeIndex as specified by relation. Use VAL_FIRST to start at the first item that meets the relation requirement to the relative index. The first ancestor is the parent of the relative item. Use VAL_LAST to start at the last item that meets the relation requirement to the relative index. The last ancestor is the ancestor of the relative item that is on level zero. |
| direction | int | Defines the direction of the items from beginIndex to search. You can select the following items: VAL_NEXT—Include the items below beginIndex in the search. VAL_NEXT_PLUS_SELF—Include the items below beginIndex, along with the item at beginIndex, in the search. VAL_PREV—Include the items above beginIndex in the search. VAL_PREV_PLUS_SELF—Include the items above beginIndex, along with the item at beginIndex, in the search. |
| stateCriteria | int | Defines the state of the searched for item. Use any combination of the following masks to define the state of the searched for item: VAL_SELECTED Item that is selected VAL_UNSELECTED Item that is unselected VAL_EXPOSED Item with all ancestors expanded VAL_UNEXPOSED Item with at least one ancestor collapsed VAL_MARKED Item whose radio button or check box is marked VAL_UNMARKED Item whose radio button or check box is not marked VAL_PARTIALLY_MARKED Item whose radio button or check box is partially marked VAL_EXPANDED Item that has children and is expanded VAL_COLLAPSED Item that has children and is collapsed VAL_LEAF Item that does not have children VAL_NON_LEAF Item that has children For example, if you pass (VAL_SELECTED \| VAL_MARKED) the function will only search among items that are selected as well as marked. Pass 0 to count items regardless of their state. |
| VAL_SELECTED | Item that is selected |  |
| VAL_UNSELECTED | Item that is unselected |  |
| VAL_EXPOSED | Item with all ancestors expanded |  |
| VAL_UNEXPOSED | Item with at least one ancestor collapsed |  |
| VAL_MARKED | Item whose radio button or check box is marked |  |
| VAL_UNMARKED | Item whose radio button or check box is not marked |  |
| VAL_PARTIALLY_MARKED | Item whose radio button or check box is partially marked |  |
| VAL_EXPANDED | Item that has children and is expanded |  |
| VAL_COLLAPSED | Item that has children and is collapsed |  |
| VAL_LEAF | Item that does not have children |  |
| VAL_NON_LEAF | Item that has children |  |
| itemLabel | char [] | The label to search for among the tree items. |
| Output |  |  |
| Name | Type | Description |
| item | int | The index of the first item in the search range of the tree control that matches the specified label. –1 indicates that no item has the specified label. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\treesearch.cws for an example of using the GetTreeItemFromLabel function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemfromtag.htm language=enus -->
## TOPIC 01127: GetTreeItemFromTag

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemfromtag.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemfromtag.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemFromTag

int GetTreeItemFromTag (int panelHandle, int controlID, char tag[], int *item);

#### Purpose

Searches for the item with the specified tag.

Returns in the **item** parameter the index of the item that has the specified tag.

#### Supported Controls

You can use GetTreeItemFromTag with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| tag | char [] | The tag to search for among the tree items. |
| Output |  |  |
| Name | Type | Description |
| item | int | The index of the item that has the specified tag. –1 indicates that no item has the specified tag. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemfromvalue.htm language=enus -->
## TOPIC 01128: GetTreeItemFromValue

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemfromvalue.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemfromvalue.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemFromValue

int GetTreeItemFromValue (int panelHandle, int controlID, int relation, int relativeIndex, int beginIndex, int direction, int stateCriteria, int *item, ...);

#### Purpose

Searches for an item with the specified value. The search range is defined by the **relation** and the **relativeIndex**. The search starts at **beginIndex** and proceeds in the direction specified by **direction**.

Returns in the **item** parameter the index of the first item that has the specified value and that meets **stateCriteria**.

Refer to the [GetTreeItemFromLabel](../../cvi/uiref/cvigettreeitemfromlabel.htm) function reference for an example of how to use this and other tree control functions.

#### Supported Controls

You can use GetTreeItemFromValue with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| relation | int | Defines the relationship between the relative index and the items to be searched. You can select the following values. VAL_ALL—Search all items regardless of their relationship to the relative item. VAL_SIBLING—Search only items that are siblings of the relative item. VAL_CHILD—Search only items that are children of the relative item. VAL_DESCENDENT—Search all items that are descendents of the relative item. VAL_ANCESTOR—Search all items that are ancestors of the relative item. |
| relativeIndex | int | Zero-based index of the item whose relatives defined by the relation parameter will be searched. |
| beginIndex | int | Zero-based index of the item where the search begins. If beginIndex does not equal relativeIndex, the item at beginIndex must be related to the item at relativeIndex as specified by relation. Use VAL_FIRST to start at the first item that meets the relation requirement to the relative index. The first ancestor is the parent of the relative item. Use VAL_LAST to start at the last item that meets the relation requirement to the relative index. The last ancestor is the ancestor of the relative item that is on level zero. |
| direction | int | Defines the direction of the items from beginIndex to search. You can select the following values: VAL_NEXT—Include the items below beginIndex in the search. VAL_NEXT_PLUS_SELF—Include the items below beginIndex, along with the item at beginIndex, in the search. VAL_PREV—Include the items above beginIndex in the search. VAL_PREV_PLUS_SELF—Include the items above beginIndex, along with the item at beginIndex, in the search. |
| stateCriteria | int | Defines the state of the searched for item. Use any combination of the following masks to define the state of the searched for item: VAL_SELECTED Item that is selected VAL_UNSELECTED Item that is unselected VAL_EXPOSED Item with all ancestors expanded VAL_UNEXPOSED Item with at least one ancestor collapsed VAL_MARKED Item whose radio button or check box is marked VAL_UNMARKED Item whose radio button or check box is not marked VAL_PARTIALLY_MARKED Item whose radio button or check box is partially marked VAL_EXPANDED Item that has children and is expanded VAL_COLLAPSED Item that has children and is collapsed VAL_LEAF Item that does not have children VAL_NON_LEAF Item that has children For example, if you pass (VAL_SELECTED \| VAL_MARKED) the function will only search among items that are selected as well as marked. Pass 0 to count items regardless of their state. |
| VAL_SELECTED | Item that is selected |  |
| VAL_UNSELECTED | Item that is unselected |  |
| VAL_EXPOSED | Item with all ancestors expanded |  |
| VAL_UNEXPOSED | Item with at least one ancestor collapsed |  |
| VAL_MARKED | Item whose radio button or check box is marked |  |
| VAL_UNMARKED | Item whose radio button or check box is not marked |  |
| VAL_PARTIALLY_MARKED | Item whose radio button or check box is partially marked |  |
| VAL_EXPANDED | Item that has children and is expanded |  |
| VAL_COLLAPSED | Item that has children and is collapsed |  |
| VAL_LEAF | Item that does not have children |  |
| VAL_NON_LEAF | Item that has children |  |
| itemValue | ... | The value to search for among the tree items. |
| Output |  |  |
| Name | Type | Description |
| item | int | The index of the first item in the search range of the tree control that matches the specified value. –1 indicates that no item has the specified value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\events.cws for an example of using the GetTreeItemFromValue function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemlevel.htm language=enus -->
## TOPIC 01129: GetTreeItemLevel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemlevel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemlevel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemLevel

int GetTreeItemLevel (int panelHandle, int controlID, int itemIndex, int *level);

#### Purpose

Returns the level of the specified tree item. The level of an item is the same as the number of ancestors it has.

#### Supported Controls

You can use GetTreeItemLevel with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |
| Output |  |  |
| Name | Type | Description |
| level | int | The level of the specified tree item. The first level is level 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemnumchildren.htm language=enus -->
## TOPIC 01130: GetTreeItemNumChildren

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemnumchildren.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemnumchildren.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemNumChildren

int GetTreeItemNumChildren (int panelHandle, int controlID, int itemIndex, int *numberOfChildren);

#### Purpose

Returns the number of children of the specified tree item.

#### Supported Controls

You can use GetTreeItemNumChildren with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |
| Output |  |  |
| Name | Type | Description |
| numberOfChildren | int | The number of child items of the specified tree item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\treeevent.cws for an example of using the GetTreeItemNumChildren function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemnumdescendents.htm language=enus -->
## TOPIC 01131: GetTreeItemNumDescendents

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemnumdescendents.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemnumdescendents.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemNumDescendents

int GetTreeItemNumDescendents (int panelHandle, int controlID, int itemIndex, int *numberOfDescendents);

#### Purpose

Returns the number of descendents of the specified tree item.

#### Supported Controls

You can use GetTreeItemNumDescendents with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |
| Output |  |  |
| Name | Type | Description |
| numberOfDescendents | int | The number of descendent items of the specified tree item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemparent.htm language=enus -->
## TOPIC 01132: GetTreeItemParent

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemparent.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemparent.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemParent

int GetTreeItemParent (int panelHandle, int controlID, int itemIndex, int *parentIndex);

#### Purpose

Returns the parent item index of the specified tree item.

#### Supported Controls

You can use GetTreeItemParent with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |
| Output |  |  |
| Name | Type | Description |
| parentIndex | int | Zero-based index of the parent tree item of the specified item. –1 indicates that the item does not have a parent. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to apps\uirview\uirview.cws for an example of using the GetTreeItemParent function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitempath.htm language=enus -->
## TOPIC 01133: GetTreeItemPath

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitempath.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitempath.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemPath

int GetTreeItemPath (int panelHandle, int controlID, int itemIndex, char separator[], char path[]);

#### Purpose

Returns the path of the specified tree item.

The path of an item consists of the labels of its ancestors concatenated together, starting at level zero. The labels are separated by the **separator** string.

#### Supported Controls

You can use GetTreeItemPath with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |
| separator | char [] | The string used to separate the labels of each ancestor item. |
| Output |  |  |
| Name | Type | Description |
| path | char [] | Buffer into which the path of the specified tree item is stored. The number of bytes in this buffer must be at least one byte greater than the value returned by GetTreeItemPathLength for this tree item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitempathlength.htm language=enus -->
## TOPIC 01134: GetTreeItemPathLength

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitempathlength.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitempathlength.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemPathLength

int GetTreeItemPathLength (int panelHandle, int controlID, int itemIndex, char separator[], int *length);

#### Purpose

Returns the length, in bytes, of the path of the specified tree item.

The length returned does not include the terminating NUL byte.

The path of an item consists of the labels of its ancestors concatenated together, starting at level zero. The labels are separated by the **separator** string.

#### Supported Controls

You can use GetTreeItemPathLength with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |
| separator | char [] | The string used to separate the labels of each ancestor item. |
| Output |  |  |
| Name | Type | Description |
| length | int | The length, in bytes, of the path of the specified tree item. The length does not include the terminating NUL byte. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigettreeitemtag.htm language=enus -->
## TOPIC 01135: GetTreeItemTag

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigettreeitemtag.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigettreeitemtag.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetTreeItemTag

int GetTreeItemTag (int panelHandle, int controlID, int itemIndex, char tag[]);

#### Purpose

Returns the tag of the specified tree item.

#### Supported Controls

You can use GetTreeItemTag with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |
| Output |  |  |
| Name | Type | Description |
| tag | char [] | Buffer into which the tag of the specified tree item is stored. The number of bytes in this buffer must be at least MAX_TREE_ITEM_TAG_LEN. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetuilerrorstring.htm language=enus -->
## TOPIC 01136: GetUILErrorString

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetuilerrorstring.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetuilerrorstring.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetUILErrorString

char *GetUILErrorString (int errorNumber);

#### Purpose

Returns the [error message](../../cvi/uiref/cvierror_conditions.htm) associated with the User Interface Library error code specified in the **errorNumber** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| errorNumber | int | An error code returned by a User Interface Library function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| errorMessage | char * | The error message associated with the error code. Do not modify or free this string. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetuserevent.htm language=enus -->
## TOPIC 01137: GetUserEvent

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetuserevent.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetuserevent.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetUserEvent

int GetUserEvent (int waitMode, int *panelOrMenuBarHandle, int *controlOrMenuItemID);

#### Purpose

Obtains the next commit event or programmer-defined event from the GetUserEvent queue. A commit event occurs when the user changes the state of a hot or validate control or selects a menu item.

Place programmer-defined events in the GetUserEvent queue by calling QueueUserEvent. Refer to [QueueUserEvent](../../cvi/uiref/cviqueueuserevent.htm) for the range of valid programmer-defined event codes.

|  | Notes When the User Interface Library handles an event that starts a tracking loop, such as the user pulling down a menu, GetUserEvent does not return until the tracking loop completes, even if you pass 0 as the waitMode parameter. In the case of pulling down a menu, the tracking loop does not complete until the user dismisses the menu. Consequently, do not call GetUserEvent in your program if you want to continue executing the subsequent lines of code even during a tracking loop. To increase the speed with which the GetUserEvent function executes, consider calling the SetSleepPolicy function prior to calling the GetUserEvent function. Set the value of the sleepPolicy input of the SetSleepPolicy function to VAL_SLEEP_NONE. |
| --- | --- |

##### Example Code

The following example code demonstrates how to use this function to respond to commit events.

. 

. 

.

InstallPopup (panelHandle);

while (done == FALSE)

{

/* Wait for a commit event to occur on one of the user interface controls */

GetUserEvent (1, &eventPanel, &eventCtrl);

/* Run code corresponding to what button the user clicked */

switch (eventCtrl)

{

case PANEL_OKBUTTON:

SaveFunc ();

done = TRUE;

break;

case PANEL_QUITBUTTON:

QuitFunc ();

done = TRUE;

break;

}

}

. 

. 

.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| waitMode | int | If you specify a nonzero value or select wait in the function panel, GetUserEvent does not return until a commit event or programmer-defined event occurs. If you specify 0 or select no wait in the function pane, GetUserEvent returns immediately, whether or not a commit event or programmer-defined event has occurred. |
| Output |  |  |
| Name | Type | Description |
| panelOrMenuBarHandle | int | The handle of the panel or menu bar on which the event occurred. Returns –1 if waitMode is zero and no event has occurred. |
| controlOrMenuItemID | int | Returns the ID of the control or menu item on which the commit event occurred. Returns –1 if waitMode is zero and no event has occurred. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| eventStatus | int | The event, if any, that occurred. 0 No event. 1 Commit event occurred. 1,000-10,000 Event queued by QueueUserEvent. Negative values indicate that an error occurred. |
| 0 | No event. |  |
| 1 | Commit event occurred. |  |
| 1,000-10,000 | Event queued by QueueUserEvent. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the GetUserEvent function:

- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\clipbord.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\getuserevent.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigetvaluefromindex.htm language=enus -->
## TOPIC 01138: GetValueFromIndex

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigetvaluefromindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigetvaluefromindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### GetValueFromIndex

int GetValueFromIndex (int panelHandle, int controlID, int itemIndex, void *itemValue);

#### Purpose

Returns the value for the specified list index.

#### Supported Controls

You can use GetValueFromIndex with the following controls:

- Rings
- Picture rings
- Ring slides
- List boxes
- Trees
- Binary switches

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index into the list. |
| Output |  |  |
| Name | Type | Description |
| itemValue | void * | The value of the list item you specify. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the GetValueFromIndex function:

- toolbox\XMLSample.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\events.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\listbox.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treeevent.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigraph_attributes.htm language=enus -->
## TOPIC 01139: Graph Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigraph_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigraph_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Graph Control Attributes

The User Interface Library attributes that are valid for
[graph](cvigraph_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Edge Style
- Enable Anti-Aliasing
- Fixed Plot Area
- Graph Background Color
- Grid Color
- Grid Style
- Plot Area Height
- Plot Area Left
- Plot Area Top
- Plot Area Width
- Plot Background Color
- Visible
- Axis Names
- Show/Hide Parts
- Size/Position

#### Control Settings

- Control Mode
- Control Style
- Copy Original Plot Data
- Data Mode
- Dimmed
- Disable Control Tooltip
- Enable Editable Axes
- First Graph Plot
- Next Panel Control
- Number of Annotations
- Number of Cursors
- Number of Graph Plots
- Refresh Graph
- Shift Text Plots
- Smooth Update
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Zoom Style
- Zooming and Panning
- Z-Plane Position
- DataSocket Settings
- X-Axis
- Y-Axis

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

#### Legend

- Auto Display in Legend
- Auto Size Graph Legend
- Legend Background Color
- Legend Frame Color
- Legend Height
- Legend Interactive
- Legend Left
- Legend Top
- Legend Visible
- Legend Width
- Number of Visible Legend Items
- Show Legend Sample Plots

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvigraphical_user_interface.htm language=enus -->
## TOPIC 01140: Graphical User Interface

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvigraphical_user_interface.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvigraphical_user_interface.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Graphical User Interface

A LabWindows/CVI graphical user interface (GUI) can consist of panels, 
pull-down menus, graphs, meters, and [many other
controls and indicators](cvioperating_controls.htm). The following figure shows a typical GUI created with
LabWindows/CVI. You can build a GUI in LabWindows/CVI interactively using the 
[User Interface Editor](../usermanual/uiovrvw.htm)User Interface Editor, a drag-and-drop editor 
with tools for designing, arranging, and customizing [user interface objects](cvigraphical_user_interface.htm#2b6a8961). With the interactive User Interface
Editor, you can build an extensive GUI for your program without writing any code. The User Interface Library also has functions for creating or altering the appearance 
of the controls on your GUI during run time, so you can [programmatically](cviuser_interface_library_function_tree.htm) add to, change, or build your 
entire GUI. When you are finished designing the GUI in the User Interface Editor, [save the GUI](../usermanual/prjfilesaveas.htm)save the GUI as a 
User Interface Resource (.uir) file.

[IMAGE alt='image' src='typuir2.gif']

**Objects in a Typical LabWindows/CVI GUI**

Here are some of the graphical objects that are available for creating a GUI using 
LabWindows/CVI and how they operate:

- A panel is a rectangular region of the screen that contains the controls and menu bars.
Panels provide the backdrop for many different activities, such as representing
the front panel instrument. You can also select from a group of pop-up panels .
- A menu bar appears at the top of a panel and contains a set of menu titles.
- A control accepts input from the user and displays information. Controls can have a data type associated with them.

##### Related Topics

[Developing and Running a Program](cvisteps_for_developing_and_running.htm)

[Creating Objects for a Graphical User Interface](cvicreating_objects_for_a_graphical.htm)

[Responding to Events in a Graphical User Interface](cviresponding_to_events_in_a_graphi.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinsertlistitem.htm language=enus -->
## TOPIC 01141: InsertListItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinsertlistitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinsertlistitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertListItem

int InsertListItem (int panelHandle, int controlID, int itemIndex, char itemLabel[], ...);

#### Purpose

Inserts a label/value pair into a control at a specific zero-based index.

Inserting the new pair causes the indices of existing label/value pairs at and
beyond the insertion point to increase by one.

You can create columns in a list box control by embedding escape codes in the itemLabel parameter.

#### Supported Controls

You can use InsertListItem with the following controls:

- Rings
- Picture rings
- Ring slides
- List boxes
- Trees

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index into the list where InsertListItem places the item. Pass –1 to insert the item at the end of the list. |
| itemLabel | char [] | Label to associate with itemValue. For picture rings, the label is actually an image, and you pass the pathname of the image as the itemLabel parameter. The image pathname can be a complete pathname or a simple filename. For simple filenames, the image file must be in the directory of the executable. If you pass NULL or an empty string, LabWindows/CVI creates a placeholder for the image that you can fill using ReplaceListitem, NewBitmapEx, or SetCtrlBitmap. You can create columns in a list box control by embedding escape codes in the itemLabel parameter. Use \\033 to indicate an escape code, followed by p (for pixel), followed by a justification code of l (left), c (center), or r (right). For example, the following code sets a left-justified column at the 100- and 200-pixel positions: InsertListItem (handle, ctrlID, 0, "Chevrolet\\033p100lCorvette\\033p200lRed", 0); InsertListItem (handle, ctrlID, 1, "Ford\\033p100lProbe\\033p200lBlack", 0); In the following example, the code segment sets a centered column at the 32-, 130-, and 230-pixel positions: InsertListItem (handle, ctrlID, 0, "\\033p32cChevrolet\\033p130cCorvette\\033p230cRed", 0); InsertListItem (handle, cID, 1, "\\033p32cFord\\033p130cProbe\\033p230cBlack", 0); To insert a vertical line at the current position in the label, the code is \\033vline. You also can use escape codes to change the foreground and background colors of characters in a list box. The escape codes affect only the label in which they are embedded. The new color affects subsequent characters in the label until you change the color again or until you reach the end of the line. To change the foreground color for a list box control, the code is \\033fgXXXXXX where XXXXXX is a 6-digit RGB value specified in hex. To change the background color for a list box control, the code is \\033bgXXXXXX where XXXXXX is a 6-digit RGB value specified in hex. To restore either color to the default color for the text of a list box control, insert default instead of the 6-digit RGB value. To insert a separator bar into a ring control (ring, menu ring, recessed menu ring, or pop-up menu ring), specify the escape code \\033m- as the itemLabel parameter. The following code inserts a separator bar between two items. InsertListItem (handle, ctrlID, 0, "Item1", 0); InsertListItem (handle, ctrlID, 1, "\\033m-", 1); InsertListItem (handle, ctrlID, 2, "Item2", 2); The first item in a list cannot be a separator bar. |
| itemValue | ... | Value to associate with itemLabel. The data type must be the same as the data type of the control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the InsertListItem function:

- toolbox\XMLSample.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\GraphAnnotations.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\GraphZooming.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\imagedit.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\listbox.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\Tooltips.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treecopy.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinsertpanelastabpage.htm language=enus -->
## TOPIC 01142: InsertPanelAsTabPage

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinsertpanelastabpage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinsertpanelastabpage.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertPanelAsTabPage

int InsertPanelAsTabPage (int panelHandle, int controlID, int index, int panelToInsert);

#### Purpose

Copies a panel you specify and inserts the panel onto a tab control at the index you specify.

#### Supported Controls

You can use InsertPanelAsTabPage with [tab controls](../../cvi/uiref/cviprogramming_with_tab_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| index | int | Zero-based index into the list where InsertPanelAsTabPage places the new tab page. Pass –1 to insert the new tab page at the end of the list. |
| panelToInsert | int | The panelHandle of the panel to copy and insert onto the tab control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| newTabIndex | int | Returns the index of the new tab page. Use this index to specify the tab page index in subsequent function calls. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Example

Refer to userint\tabpanels.cws for an example of using the InsertPanelAsTabPage function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinsertseparator.htm language=enus -->
## TOPIC 01143: InsertSeparator

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinsertseparator.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinsertseparator.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertSeparator

int InsertSeparator (int menuBarHandle, int menuID, int beforeMenuItemID);

#### Purpose

Inserts a new separator bar in a menu, and returns a menu item ID you 
can use in subsequent function calls to specify the separator.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |
| menuID | int | ID for a particular menu within a menu bar. The ID must be a constant name, located in the .uir header file, that you assign in the User Interface Editor or a value that you obtain from functions such as NewMenu and NewSubMenu. |
| beforeMenuItemID | int | Menu item ID above which to insert the separator bar. To place the separator at the bottom of the menu item list, pass –1. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| menuItemID | int | Returns the ID that you use to specify this menu item in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\uirview\uirview.cws for an example of using the InsertSeparator function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinserttablecellrangeringitem.htm language=enus -->
## TOPIC 01144: InsertTableCellRangeRingItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinserttablecellrangeringitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinserttablecellrangeringitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertTableCellRangeRingItem

int InsertTableCellRangeRingItem (int panelHandle, int controlID, Rect cellRange, int index, char value[]);

#### Purpose

Inserts a new item into the list of values of a specified range of ring or combo-box cells of a table control.

The indexes of existing values at and beyond the specified index are increased by one.

#### Supported Controls

You can use InsertTableCellRangeRingItem with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cellRange | Rect | A Rect structure specifying the range of cells into which you want to insert the new value. The cells in the specified range must be of type VAL_CELL_RING, or VAL_CELL_COMBO_BOX, or a mixture of the two. If the range includes cells of any other type, an error is returned and the results are unspecified. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; Pass the one-based row and column indices of the first cell in the range as the top and left fields of the structure, respectively. Pass the number of columns in the range as the width field of the structure, and the number of rows in the range as the height field of the structure. You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example InsertTableCellRangeRingItem (panelHandle, controlID, MakeRect (2, 3, 5, 5), -1, "new value"); |
| index | int | The zero-based index into the value list of the cells where the new item is placed. Pass –1 to insert the new item at the end of the value list. This index must be valid for every cell in the specified range. If it is not valid for one or more cells, an error is returned and the results are unspecified. |
| value | char [] | The new value to insert in the value list. If ATTR_RING_ITEMS_UNIQUE is enabled and this value matches an existing value in the list, then a new item will not be added to the list. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

#### Example

Refer to userint\tablecells.cws for an example of using the InsertTableCellRangeRingItem function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinserttablerows.htm language=enus -->
## TOPIC 01145: InsertTableRows

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinserttablerows.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinserttablerows.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertTableRows

int InsertTableRows (int panelHandle, int controlID, int rowIndex, int numberOfRows, int cellType);

#### Purpose

Inserts new rows into a table control at the specified one-based index.

The indexes of existing rows at and beyond the specified index are increased
by the number of rows inserted.

This function creates a new cell for each column in the table.

##### Example Code

Refer to the [SetTableColumnAttribute](../../cvi/uiref/cvisettablecolumnattribute.htm) function reference for an example of how to use this and other table functions to insert cells into a table control and modify the attributes of new and existing cells.

#### Supported Controls

You can use InsertTableRows with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| rowIndex | int | The one-based index into the table where the function inserts the first new row. Pass –1 to insert the first new rows at the end of the table. |
| numberOfRows | int | The number of new rows to insert. |
| cellType | int | The cell type of the cells that might be created as a result of creating the new rows. The following table lists the possible cell types. Constant Name Constant Value VAL_CELL_NUMERIC 0 VAL_CELL_STRING 1 VAL_CELL_PICTURE 2 VAL_CELL_RING 3 VAL_CELL_COMBO_BOX 4 VAL_CELL_BUTTON 5 Pass VAL_USE_MASTER_CELL_TYPE (–1) if you want the cell types to be the default cell types for each column. Refer to ATTR_TABLE_MODE. |
| Constant Name | Constant Value |  |
| VAL_CELL_NUMERIC | 0 |  |
| VAL_CELL_STRING | 1 |  |
| VAL_CELL_PICTURE | 2 |  |
| VAL_CELL_RING | 3 |  |
| VAL_CELL_COMBO_BOX | 4 |  |
| VAL_CELL_BUTTON | 5 |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the InsertTableRows function:

- userint\colview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\gridview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\tablecells.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\threading\ThreadPool\ParallelTestInit\ParallelTestInit.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinserttabpage.htm language=enus -->
## TOPIC 01146: InsertTabPage

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinserttabpage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinserttabpage.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertTabPage

int InsertTabPage (int panelHandle, int controlID, int index, char tabLabel[]);

#### Purpose

Inserts a tab page into the tab control.

Inserting the new tab page causes the indices of existing tab pages at and
beyond the insertion point to increase by one.

The function returns the index of the new tab page or an error.

##### Example Code

The following code demonstrates how to create a tab control, insert tab pages, and add a command button to each tab page.

int tabCtrl, tab1, tab2, tabPanel1, tabPanel2, testButton, quitButton, 

    panelHeight = 0, panelWidth = 0;

/* Create a new tab control */

tabCtrl = NewCtrl (parentPanel, CTRL_TABS, "Test Control", 100, 100);

/* Insert two tab pages */

tab1 = InsertTabPage (parentPanel, tabCtrl, 0, "Test Tab One");

tab2 = InsertTabPage (parentPanel, tabCtrl, 1, "Test Tab Two");

/* Get the panel handle for the first tab page */

GetPanelHandleFromTabPage (parentPanel, tabCtrl, 0, &tabPanel1);

/* Get the height & width of the first tab page using the panel handle you obtained in the previous function */

GetPanelAttribute (tabPanel1, ATTR_HEIGHT, &panelHeight);

GetPanelAttribute (tabPanel1, ATTR_WIDTH, &panelWidth);

/* Add a command button to the first tab page using its panel handle */

testButton = NewCtrl (tabPanel1, CTRL_SQUARE_COMMAND_BUTTON_LS,
 "Test Button", panelHeight - 50, panelWidth - 100);

/* Get the panel handle for the second tab page */

GetPanelHandleFromTabPage (parentPanel, tabCtrl, 1, &tabPanel2);

/* Add a command button to the second tab page using its panel handle */

quitButton = NewCtrl (tabPanel2, CTRL_SQUARE_COMMAND_BUTTON_LS,
 "Quit", panelHeight - 50, panelWidth - 75);

/* Make the second tab page the active tab page */

SetActiveTabPage (parentPanel, tabCtrl, 1);

#### Supported Controls

You can use InsertTabPage with [tab controls](../../cvi/uiref/cviprogramming_with_tab_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| index | int | Zero-based index into the list where InsertTabPage places the new tab page. Pass –1 to insert the new tab page at the end of the list. |
| tabLabel | char [] | Label of the new tab page. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| newTabIndex | int | Returns the index of the new tab page. Use this index to specify the tab page index in subsequent function calls. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinserttextboxline.htm language=enus -->
## TOPIC 01147: InsertTextBoxLine

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinserttextboxline.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinserttextboxline.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertTextBoxLine

int InsertTextBoxLine (int panelHandle, int controlID, int lineIndex, char text[]);

#### Purpose

Inserts a string as a new line in a text box.

|  | Note The function inserts a newline character at the end of the text that you specify. |
| --- | --- |

#### Supported Controls

You can use InsertTextBoxLine with [text box controls](../../cvi/uiref/cviprogramming_with_text_box_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| lineIndex | int | Zero-based index of the text box line above which to insert the string. Pass –1 to insert the new string at the end of the text box. |
| text | char [] | Text to insert at the specified lineIndex. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the InsertTextBoxLine function:

- toolbox\msgdemo.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\docking.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\textbox.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinserttreecellringitem.htm language=enus -->
## TOPIC 01148: InsertTreeCellRingItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinserttreecellringitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinserttreecellringitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertTreeCellRingItem

int InsertTreeCellRingItem (int panelHandle, int controlID, int itemIndex, int columnIndex, int ringIndex, char value[]);

#### Purpose

Inserts a new item into the list of values of a specified ring or combo box cell of a tree control.

LabWindows/CVI increases the indexes of existing values at and beyond the specified index by one.

#### Supported Controls

You can use InsertTreeCellRingItem with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item containing the cell for which you want to insert the new value. |
| columnIndex | int | Zero-based index of the tree column that contains the cell for which you want to insert the new value. |
| ringIndex | int | The zero-based index of the location in the list of values of the cell where you want the new item placed. Pass –1 to insert the new item at the end of the list of values. |
| value | char [] | The new value to insert in the list of values. If this value matches an existing value in the list, then a new item will not be added to the list. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| newItemIndex | int | Returns the index of the inserted ring item. If the value already exists in the list, the value is not added and the function returns the index of the existing value. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviinserttreecolumn.htm language=enus -->
## TOPIC 01149: InsertTreeColumn

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviinserttreecolumn.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviinserttreecolumn.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### InsertTreeColumn

int InsertTreeColumn (int panelHandle, int controlID, int columnIndex, char columnLabel[]);

#### Purpose

Inserts a column into the tree control at the specified zero-based index.

Inserting a new column causes the indices of existing columns at and beyond the insertion point to increase by one.

The function returns the index of the new column or an error.

#### Supported Controls

You can use InsertTreeColumn with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| columnIndex | int | Zero-based index into the tree where InsertTreeColumn places the new column. You cannot insert a column at index 0. Pass –1 to insert the column as the last column. |
| columnLabel | char [] | Label of the new tree column. You can pass NULL for the label. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| columnIndex | int | Returns the index of the inserted column. Use the index to specify the tree column in subsequent function calls. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\TreeBusDigitalGraph.cws for an example of using the InsertTreeColumn function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviistreeitemexposed.htm language=enus -->
## TOPIC 01150: IsTreeItemExposed

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviistreeitemexposed.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviistreeitemexposed.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### IsTreeItemExposed

int IsTreeItemExposed (int panelHandle, int controlID, int itemIndex, int *isExposed);

#### Purpose

Returns a Boolean value indicating whether the specified item is exposed. An exposed item is one whose ancestors are all expanded. Items that do not have a parent are always exposed.

#### Supported Controls

You can use IsTreeItemExposed with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |
| Output |  |  |
| Name | Type | Description |
| isExposed | int | A Boolean value indicating whether all of the ancestors of the specified tree item are expanded. 0 = not exposed (at least one ancestor is collapsed) 1 = exposed (all ancestors are expanded) |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvikeypresseventisleadbyte.htm language=enus -->
## TOPIC 01151: KeyPressEventIsLeadByte

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvikeypresseventisleadbyte.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvikeypresseventisleadbyte.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### KeyPressEventIsLeadByte

int KeyPressEventIsLeadByte (int eventData2);

#### Purpose

Call this function when you receive an [EVENT_KEYPRESS](../../cvi/uiref/cvieventkeypress.htm) in a panel or control callback to determine if the callback's eventData1 parameter contains the first byte of a two-byte character. If the callback's eventData1 parameter contains a lead byte, the trail byte will be in the next EVENT_KEYPRESS event for that panel or control. National Instruments recommends that you ignore EVENT_KEYPRESS events that contain the first byte of a two-byte character.

Refer to the [GetKeyPressEventCharacter](../../cvi/uiref/cvigetkeypresseventcharacter.htm) function reference for an example of how to use this and other key press event functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventData2 | int | The panel or control callback's eventData2 parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| isLeadByte | int | > 0 if the EVENT_KEYPRESS event is for a lead byte of a two-byte character. 0 if the EVENT_KEYPRESS event is not for a lead byte of a two-byte character. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

#### Example

Refer to userint\multikey.cws for an example of using the KeyPressEventIsLeadByte function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvikeypresseventistrailbyte.htm language=enus -->
## TOPIC 01152: KeyPressEventIsTrailByte

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvikeypresseventistrailbyte.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvikeypresseventistrailbyte.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### KeyPressEventIsTrailByte

int KeyPressEventIsTrailByte (int eventData2);

#### Purpose

Call this function when you receive an [EVENT_KEYPRESS](../../cvi/uiref/cvieventkeypress.htm) in a panel or control callback to determine if the callback's eventData1 parameter contains the second byte of a two-byte character. If the callback's eventData1 parameter contains a trail byte, you can call [GetKeyPressEventCharacter](../../cvi/uiref/cvigetkeypresseventcharacter.htm) to get both bytes of the character.

Refer to the [GetKeyPressEventCharacter](../../cvi/uiref/cvigetkeypresseventcharacter.htm) function reference for an example of how to use this and other key press event functions.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventData2 | int | The panel or control callback's eventData2 parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| isTrailByte | int | > 0 if the EVENT_KEYPRESS event is for a trail byte of a two-byte character. 0 if the EVENT_KEYPRESS event is not for a trail byte of a two-byte character. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvilifetime_of_secondary_threads.htm language=enus -->
## TOPIC 01153: Lifetime of Secondary Threads

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvilifetime_of_secondary_threads.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvilifetime_of_secondary_threads.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Lifetime of Secondary Threads

Make sure to always terminate every [thread](cvidifferent_approaches_to_multithr.htm) other than the main thread before your program terminates. Otherwise, under Windows, the LabWindows/CVI Runtime cannot perform all of its
cleanup operations. In addition, if your code is contained within a DLL and an
application dynamically loads and unloads the DLL, the application might lose
resources that were allocated in the threads you did not terminate.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvilist_box_control_events.htm language=enus -->
## TOPIC 01154: List Box Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvilist_box_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvilist_box_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### List Box Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [list box](cvilist_box_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

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
- EVENT_VSCROLL
- EVENT_MARK_STATE_CHANGE
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvilist_box_control_functions.htm language=enus -->
## TOPIC 01155: List Box Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvilist_box_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvilist_box_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### List Box Control Functions

The following User Interface Library functions operate on [list box](cvilist_box_control_overview.htm) controls.

- AddCtrlToSplitter
- CheckListItem
- ClearListCtrl
- DefaultCtrl
- DeleteListItem
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlIndex
- GetCtrlVal
- GetIndexFromPoint
- GetIndexFromValue
- GetLabelFromIndex
- GetLabelLengthFromIndex
- GetListItemImage
- GetNumCheckedItems
- GetNumListItems
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- GetValueFromIndex
- GetValueLengthFromIndex
- InsertCtrlArrayItem
- InsertListItem
- InstallCtrlCallback
- IsListItemChecked
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- ReplaceListItem
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlIndex
- SetCtrlVal
- SetInputMode
- SetListItemImage

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvilist_of_trace_attributes.htm language=enus -->
## TOPIC 01156: List of Trace Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvilist_of_trace_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvilist_of_trace_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### List of Trace Attributes

Trace attributes are used to configure individual traces on
 [strip chart](cvistrip_chart_control_overview.htm)
 controls. You can set and get trace attributes using
 [SetTraceAttribute](cvisettraceattribute.htm), [SetTraceAttributeEx](cvisettraceattributeex.htm), and
 [GetTraceAttribute](cvigettraceattribute.htm). The 
 following is a list of all trace attributes:

[Color](cviattrtracecolor_trace.htm)

[Legend Trace Text](cviattrtracelgtext.htm)

[Legend Trace Text Color](cviattrtracelgtextcolor.htm)

[Legend Trace Text Font](cviattrtracelgfont.htm)

[Legend Trace Text Font Name Length](cviattrtracelgfontnamelength.htm)

[Legend Trace Text Length](cviattrtracelgtextlength.htm)

[Legend Trace Visible](cviattrtracelgvisible.htm)

[Line Style](cviattrlinestyle_trace.htm)

[Opacity](cviattrtraceopacity.htm)

[Plot Style](cviattrplotstyle_trace.htm)

[Point Style](cviattrtracepointstyle_trace.htm)

[Thickness](cviattrtracethickness.htm)

[Visible](cviattrtracevisible_trace.htm)

[Y-Axis](cviattrtraceyaxis.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvilist_of_tree_cell_attributes.htm language=enus -->
## TOPIC 01157: List of Tree Cell Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvilist_of_tree_cell_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvilist_of_tree_cell_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### List of Tree Cell Attributes

Use tree cell attributes to configure individual cells on [tree](cvitree_control_overview.htm) controls. You can get and set tree cell attributes using [GetTreeCellAttribute](cvigettreecellattribute.htm) and [SetTreeCellAttribute](cvisettreecellattribute.htm). The following is a list of all tree cell attributes:

[Cell Type](cviattrcelltype_tree%20cell.htm)

[Color Picker Value](cviattrcolorpickervalue.htm)

[Dimmed](cviattrcelldimmed_tree%20cell.htm)

[Horizontal Bar Color](cviattrhorizontalbarcolor.htm)

[Horizontal Bar Value](cviattrhorizontalbarvalue.htm)

[Label Background Color](cviattrlabelbgcolor_tree%20cell.htm)

[Label Bold](cviattrlabelbold_tree%20cell.htm)

[Label Character Set](cviattrlabelcharacterset_tree%20cell.htm)

[Label Color](cviattrlabelcolor_tree%20cell.htm)

[Label Font](cviattrlabelfont_tree%20cell.htm)

[Label Font Name Length](cviattrlabelfontnamelength_tree%20cell.htm)

[Label Italics](cviattrlabelitalic_tree%20cell.htm)

[Label Justification](cviattrlabeljustify_tree%20cell.htm)

[Label Point Size](cviattrlabelpointsize_tree%20cell.htm)

[Label Strikeout](cviattrlabelstrikeout_tree%20cell.htm)

[Label Text](cviattrlabeltext_tree%20cell.htm)

[Label Text Length](cviattrlabeltextlength_tree%20cell.htm)

[Label Underline](cviattrlabelunderline_tree%20cell.htm)

[Label Visible](cviattrlabelvisible_tree%20cell.htm)

[Mark State](cviattrmarkstate_tree%20cell.htm)

[Maximum Entry Characters](cviattrmaxentrychars_tree%20cell.htm)

[Maximum Entry Length](cviattrmaxentrylength_tree%20cell.htm)

[Show Transparent](cviattrshowtransparent_tree%20cell.htm)

[Tooltip Text](cviattrtooltiptext_tree%20cell.htm)

[Tooltip Text Length](cviattrtooltiptextlength_tree%20cell.htm)

[Tree Run State](cviattrtreerunstate_tree%20cell.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvimakeapplicationactive.htm language=enus -->
## TOPIC 01158: MakeApplicationActive

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvimakeapplicationactive.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvimakeapplicationactive.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MakeApplicationActive

int MakeApplicationActive (void);

#### Purpose

Activates your application and brings its topmost panel to the front. MakeApplicationActive has no effect if you have not displayed any panels.

(Linux) This function is not supported.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvimakecolor.htm language=enus -->
## TOPIC 01159: MakeColor

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvimakecolor.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvimakecolor.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MakeColor

int MakeColor (int red, int green, int blue);

#### Purpose

Generates a color (RGB) value from the individual constituent red, 
green, and blue intensity levels.

An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors listed are the sixteen standard colors.

0xFF0000L = VAL_RED 

0x00FF00L = VAL_GREEN 

0x0000FFL = VAL_BLUE 

0x00FFFFL = VAL_CYAN 

0xFF00FFL = VAL_MAGENTA 

0xFFFF00L = VAL_YELLOW 

0x800000L = VAL_DK_RED 

0x000080L = VAL_DK_BLUE 

0x008000L = VAL_DK_GREEN 

0x008080L = VAL_DK_CYAN 

0x800080L = VAL_DK_MAGENTA 

0x808000L = VAL_DK_YELLOW 

0xC0C0C0L = VAL_LT_GRAY 

0x808080L = VAL_DK_GRAY 

0x000000L = VAL_BLACK 

0xFFFFFFL = VAL_WHITE 
 

0xA0A0A0L = VAL_GRAY 

0xE0E0E0L = VAL_OFFWHITE 

VAL_PANEL_GRAY = VAL_LT_GRAY

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| red | int | Red level of the new color. Any integer value between 0 and 255 is valid. 0 = No red component 255 = Maximum red component |
| green | int | Green level of the new color. Any integer value between 0 and 255 is valid. 0 = No green component 255 = Maximum green component |
| blue | int | Blue level of the new color. Any integer value between 0 and 255 is valid. 0 = No blue component 255 = Maximum blue component |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| RGBValue | int | Return value indicating the RGB value. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the MakeColor function:

- userint\canvas.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\canvsbmk.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\GraphZooming.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\gridview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\intgraph.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvimakerect.htm language=enus -->
## TOPIC 01160: MakeRect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvimakerect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvimakerect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MakeRect

Rect MakeRect (int top, int left, int height, int width);

#### Purpose

Returns a Rect structure with the values you specify. The Rect structure defines the location and size of a rectangle.

This function is useful when you call canvas control functions that require Rect structures as input parameters. You can embed a call to MakeRect in calls to these functions, eliminating the need to declare a Rect variable.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| top | int | Location of the top edge of the rectangle. |
| left | int | Location of the left edge of the rectangle. |
| height | int | Height of the rectangle. |
| width | int | Width of the rectangle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| newRectangle | Rect | Rect structure containing the coordinate values you specify. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\clipbord.cws for an example of using the MakeRect function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvimaketreeitemvisible.htm language=enus -->
## TOPIC 01161: MakeTreeItemVisible

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvimaketreeitemvisible.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvimaketreeitemvisible.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MakeTreeItemVisible

int MakeTreeItemVisible (int panelHandle, int controlID, int itemIndex);

#### Purpose

Makes the specified tree item visible. Expands the ancestors of the item and scrolls the item into view.

#### Supported Controls

You can use MakeTreeItemVisible with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Examples

Refer to the following examples that use the MakeTreeItemVisible function:

- userint\events.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treeimage.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treesearch.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvimenubaroverview.htm language=enus -->
## TOPIC 01162: Menu Bar Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvimenubaroverview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvimenubaroverview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Menu Bar Overview

A *menu bar* encapsulates a set of commands in menu form. A menu bar appears as a bar at
the top of a [panel](cvioperating_panels.htm) and contains a set of menu titles. The following example is a menu bar in the CVI environment:

[IMAGE alt='image' src='menpull.gif']

A menu title ending in an exclamation point is called an *immediate action menu* and does not have an associated pull-down menu. When the user clicks an immediate action menu, a command executes immediately.

A menu title without an exclamation point has a pull-down menu. The menu can contain menu items and submenu titles. When you select a submenu title, submenu items appear on the side. The following example is a submenu bar in the CVI environment:

[IMAGE alt='image' src='mensubme.gif']

You can create menu bars in LabWindows/CVI using the [Edit Menu Bar](../usermanual/uiedit_menu_bar.htm)Edit Menu Bar dialog box or programmatically using the [User Interface Library functions](cvimenu_bar_functions.htm).

[Operating Menu Bars](cvioperating_menu_bars.htm)

[Programming Menu Bars](cviprogramming_with_menu_bars.htm)

[Menu Bar Attributes](cvimenu_attributes.htm)

[Menu Bar Functions](cvimenu_bar_functions.htm)

[Menu Bar Events](cvimenu_bar_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvimessagepopup.htm language=enus -->
## TOPIC 01163: MessagePopup

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvimessagepopup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvimessagepopup.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MessagePopup

int MessagePopup (char title[], char message[]);

#### Purpose

Displays a message in a dialog box and waits for the user to select the **OK** button.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| title | char [] | Title of the dialog box. |
| message | char [] | Message to display in the dialog box. To display a multi-line message, embed newline characters (\\n) in the message string. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the MessagePopup function:

- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\ClockDigitalGraph.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\databinding.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\ICOViewer.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\popups.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\custctrl\password\pwsample.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- utility\oneinst.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviminimizeallwindows.htm language=enus -->
## TOPIC 01164: MinimizeAllWindows

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviminimizeallwindows.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviminimizeallwindows.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MinimizeAllWindows

void MinimizeAllWindows (void);

#### Purpose

Hides all the panels that you created in the current thread, other than panels that have their own taskbar buttons. To restore the panels, click the taskbar button for the thread.

|  | Note If you enable the ATTR_HAS_TASKBAR_BUTTON attribute on your panels, MinimizeAllWindows hides all the taskbar buttons for the panels. To minimize each panel to its own taskbar button, set the ATTR_WINDOW_ZOOM attribute to VAL_MINIMIZE on each panel. |
| --- | --- |

#### Parameters

None.

#### Return Value

None.

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvimovectrlarray.htm language=enus -->
## TOPIC 01165: MoveCtrlArray

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvimovectrlarray.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvimovectrlarray.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MoveCtrlArray

int MoveCtrlArray (int controlArrayHandle, int xDelta, int yDelta);

#### Purpose

Moves all controls in the specified control array to another position. The new position is defined by the **xDelta** and **yDelta** parameters.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| controlArrayHandle | int | Specifier for a particular control array that is currently in memory. You obtain this handle from GetCtrlArrayFromResourceID or NewCtrlArray. |
| xDelta | int | The number of pixels to horizontally shift the position of all controls in the specified control array. |
| yDelta | int | The number of pixels to vertically shift the position of all controls in the specified control array. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2010 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvimovetabpage.htm language=enus -->
## TOPIC 01166: MoveTabPage

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvimovetabpage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvimovetabpage.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### MoveTabPage

int MoveTabPage (int panelHandle, int controlID, int index, int destinationIndex);

#### Purpose

Moves a tab page to another position in the tab control. The new position is defined by the destination index.

Moving a tab page changes the indices of the existing tab pages between the original index and the final index of the tab page to be moved.

The function returns the new index of the moved tab page or an error.

#### Supported Controls

You can use MoveTabPage with [tab controls](../../cvi/uiref/cviprogramming_with_tab_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| index | int | Zero-based index of the tab page to move. |
| destinationIndex | int | Identifies the new position of the tab page to be moved. Pass –1 to move the tab page to the end of the list. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| movedToIndex | int | Returns the index of the moved tab page. Use the index to specify the tab page in subsequent function calls. Negative values indicate that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewactivexctrl.htm language=enus -->
## TOPIC 01167: NewActiveXCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewactivexctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewactivexctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewActiveXCtrl

int NewActiveXCtrl (int panelHandle, char controlLabel[], int controlTop, int controlLeft, const GUID *classID, const IID *interfaceID, char license[], HRESULT *activeXError);

#### Purpose

Creates a new ActiveX control and returns a control ID used to specify the control in subsequent function calls.

This function also creates and caches a CAObjHandle for the ActiveX control object. Use GetObjHandleFromActiveXCtrl to get the CAObjHandle.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlLabel | char [] | The label of the new control. Pass "" or 0 for no label. |
| controlTop | int | The vertical coordinate at which the upper left corner of the control (not including labels) is placed. The coordinate must be an integer value from –32,768 to 32,767. The origin (0,0) is at the upper-left corner of the panel directly below the title bar before the panel is scrolled. |
| controlLeft | int | The horizontal coordinate at which the upper left corner of the control (not including labels) is placed. The coordinate must be an integer value from –32,768 to 32,767. The origin (0,0) is at the upper-left corner of the panel directly below the title bar before the panel is scrolled. |
| classID | const GUID * | The Class ID of the ActiveX control object. |
| interfaceID | const IID * | The interface ID specifying the type of the interface pointer that is associated with the CAObjHandle of the ActiveX control. Pass 0 to specify the default dispatch interface of the ActiveX control. |
| license | char [] | Run-time license string for the ActiveX control. Pass 0 if the ActiveX control does not support licensing. |
| Output |  |  |
| Name | Type | Description |
| activeXError | HRESULT | The HRESULT if this function causes an ActiveX error. In the event of an ActiveX error, this function returns a value of UIActiveXError. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| controlID | int | Returns the ID used to specify this control in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewactivexctrlfromfile.htm language=enus -->
## TOPIC 01168: NewActiveXCtrlFromFile

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewactivexctrlfromfile.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewactivexctrlfromfile.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewActiveXCtrlFromFile

int NewActiveXCtrlFromFile (int panelHandle, char controlLabel[], int controlTop, int controlLeft, char filename[], const IID *interfaceID, HRESULT *activeXError);

#### Purpose

Creates a new ActiveX control from a file and returns a control ID used to specify the control in subsequent function calls.

This function also creates and caches a CAObjHandle for the ActiveX
control object. Use [GetObjHandleFromActiveXCtrl](../../cvi/uiref/cvigetobjhandlefromactivexctrl.htm) to get the CAObjHandle.

(Linux) This function is not supported.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlLabel | char [] | The label of the new control. Pass "" or 0 for no label. |
| controlTop | int | The vertical coordinate at which the upper left corner of the control (not including labels) is placed. The coordinate must be an integer value from –32,768 to 32,767. The origin (0,0) is at the upper-left corner of the panel directly below the title bar before the panel is scrolled. |
| controlLeft | int | The horizontal coordinate at which the upper left corner of the control (not including labels) is placed. The coordinate must be an integer value from –32,768 to 32,767. The origin (0,0) is at the upper-left corner of the panel directly below the title bar before the panel is scrolled. |
| filename | char [] | The full path of the file from which the object is initialized. |
| interfaceID | const IID * | The interface ID specifying the type of the interface pointer that is associated with the CAObjHandle for the ActiveX control. Pass 0 to specify the default dispatch interface of the ActiveX control. |
| Output |  |  |
| Name | Type | Description |
| activeXError | HRESULT | The HRESULT if this function causes an ActiveX error. In the event of an ActiveX error, this function returns a value of UIActiveXError. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| controlID | int | Returns the ID used to specify this control in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 6.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewctrl.htm language=enus -->
## TOPIC 01169: NewCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewCtrl

int NewCtrl (int panelHandle, int controlStyle, char controlLabel[], int controlTop, int controlLeft);

#### Purpose

Creates a new control and returns a control ID that you can use to specify the control in subsequent function calls.

If you call this function to add a timer control to a panel, you must do so in
the same thread in which you create or load the panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlStyle | int | Select one of the following control styles. Type Style Numeric CTRL_NUMERIC CTRL_NUMERIC_LS Color Numeric CTRL_COLOR_NUMERIC CTRL_COLOR_NUMERIC_LS Numeric Slide CTRL_NUMERIC_THERMOMETER CTRL_NUMERIC_THERMOMETER_LS CTRL_NUMERIC_TANK CTRL_NUMERIC_TANK_LS CTRL_NUMERIC_GAUGE CTRL_NUMERIC_GAUGE_LS CTRL_NUMERIC_METER CTRL_NUMERIC_METER_LS CTRL_NUMERIC_KNOB CTRL_NUMERIC_KNOB_LS CTRL_NUMERIC_DIAL CTRL_NUMERIC_DIAL_LS CTRL_NUMERIC_VSLIDE CTRL_NUMERIC_HSLIDE CTRL_NUMERIC_FLAT_VSLIDE CTRL_NUMERIC_FLAT_HSLIDE CTRL_NUMERIC_LEVEL_VSLIDE CTRL_NUMERIC_LEVEL_VSLIDE_LS CTRL_NUMERIC_LEVEL_HSLIDE CTRL_NUMERIC_LEVEL_HSLIDE_LS CTRL_NUMERIC_POINTER_VSLIDE CTRL_NUMERIC_POINTER_VSLIDE_LS CTRL_NUMERIC_POINTER_HSLIDE CTRL_NUMERIC_POINTER_HSLIDE_LS String CTRL_STRING CTRL_STRING_LS Text Message CTRL_TEXT_MSG Text Box CTRL_TEXT_BOX CTRL_TEXT_BOX_LS Command Button CTRL_SQUARE_COMMAND_BUTTON CTRL_SQUARE_COMMAND_BUTTON_LS CTRL_OBLONG_COMMAND_BUTTON CTRL_ROUND_COMMAND_BUTTON CTRL_ROUNDED_COMMAND_BUTTON Picture Button CTRL_PICTURE_COMMAND_BUTTON CTRL_PICTURE_COMMAND_BUTTON_LS CTRL_PICTURE_TOGGLE_BUTTON CTRL_PICTURE_TOGGLE_BUTTON_LS Toggle Button CTRL_ROUND_BUTTON CTRL_SQUARE_BUTTON CTRL_SQUARE_BUTTON_LS CTRL_ROUND_FLAT_BUTTON CTRL_SQUARE_FLAT_BUTTON CTRL_ROUND_PUSH_BUTTON CTRL_SQUARE_PUSH_BUTTON CTRL_SQUARE_PUSH_BUTTON_LS CTRL_ROUND_PUSH_BUTTON2 CTRL_SQUARE_PUSH_BUTTON2 Text Button CTRL_SQUARE_TEXT_BUTTON CTRL_SQUARE_TEXT_BUTTON_LS CTRL_OBLONG_TEXT_BUTTON CTRL_ROUND_TEXT_BUTTON CTRL_ROUNDED_TEXT_BUTTON Radio Button CTRL_ROUND_RADIO_BUTTON CTRL_SQUARE_RADIO_BUTTON CTRL_CHECK_BOX LED CTRL_ROUND_LIGHT CTRL_SQUARE_LIGHT CTRL_ROUND_LED CTRL_ROUND_LED_LS CTRL_SQUARE_LED CTRL_SQUARE_LED_LS Binary Switch CTRL_HSWITCH CTRL_VSWITCH CTRL_GROOVED_HSWITCH CTRL_GROOVED_VSWITCH CTRL_TOGGLE_HSWITCH CTRL_TOGGLE_HSWITCH_LS CTRL_TOGGLE_VSWITCH CTRL_TOGGLE_VSWITCH_LS Ring CTRL_RING CTRL_RING_LS CTRL_RECESSED_MENU_RING CTRL_RECESSED_MENU_RING_LS CTRL_MENU_RING CTRL_MENU_RING_LS CTRL_POPUP_MENU_RING CTRL_POPUP_MENU_RING_LS Ring Slide CTRL_RING_VSLIDE CTRL_RING_HSLIDE CTRL_RING_FLAT_VSLIDE CTRL_RING_FLAT_HSLIDE CTRL_RING_LEVEL_VSLIDE CTRL_RING_LEVEL_VSLIDE_LS CTRL_RING_LEVEL_HSLIDE CTRL_RING_LEVEL_HSLIDE_LS CTRL_RING_POINTER_VSLIDE CTRL_RING_POINTER_VSLIDE_LS CTRL_RING_POINTER_HSLIDE CTRL_RING_POINTER_HSLIDE_LS CTRL_RING_THERMOMETER CTRL_RING_THERMOMETER_LS CTRL_RING_TANK CTRL_RING_TANK_LS CTRL_RING_GAUGE CTRL_RING_GAUGE_LS CTRL_RING_METER CTRL_RING_METER_LS CTRL_RING_KNOB CTRL_RING_KNOB_LS CTRL_RING_DIAL CTRL_RING_DIAL_LS Picture Ring CTRL_PICTURE_RING CTRL_PICTURE_RING_LS List Box CTRL_LIST CTRL_LIST_LS Decoration CTRL_RAISED_BOX CTRL_RAISED_BOX_LS CTRL_RECESSED_BOX CTRL_RECESSED_BOX_LS CTRL_FLAT_BOX CTRL_RAISED_CIRCLE CTRL_RECESSED_CIRCLE CTRL_FLAT_CIRCLE CTRL_RAISED_FRAME CTRL_RECESSED_FRAME CTRL_RECESSED_NARROW_FRAME CTRL_FLAT_FRAME CTRL_RAISED_ROUND_FRAME CTRL_RECESSED_ROUND_FRAME CTRL_FLAT_ROUND_FRAME CTRL_RAISED_ROUNDED_BOX CTRL_RECESSED_ROUNDED_BOX CTRL_FLAT_ROUNDED_BOX CTRL_SMOOTH_VERTICAL_BOX_LS CTRL_SMOOTH_HORIZONTAL_BOX_LS Graph CTRL_GRAPH CTRL_GRAPH_LS Digital Graph CTRL_DIGITAL_GRAPH CTRL_DIGITAL_GRAPH_LS Strip Chart CTRL_STRIP_CHART CTRL_STRIP_CHART_LS Picture CTRL_PICTURE CTRL_PICTURE_LS Timer CTRL_TIMER Canvas CTRL_CANVAS Table CTRL_TABLE CTRL_TABLE_LS ActiveX CTRL_ACTIVEX Tree CTRL_TREE CTRL_TREE_LS Splitter CTRL_HORIZONTAL_SPLITTER CTRL_HORIZONTAL_SPLITTER_LS CTRL_VERTICAL_SPLITTER CTRL_VERTICAL_SPLITTER_LS Tab CTRL_TABS |
| Type | Style |  |
| Numeric | CTRL_NUMERIC CTRL_NUMERIC_LS |  |
| Color Numeric | CTRL_COLOR_NUMERIC CTRL_COLOR_NUMERIC_LS |  |
| Numeric Slide | CTRL_NUMERIC_THERMOMETER CTRL_NUMERIC_THERMOMETER_LS CTRL_NUMERIC_TANK CTRL_NUMERIC_TANK_LS CTRL_NUMERIC_GAUGE CTRL_NUMERIC_GAUGE_LS CTRL_NUMERIC_METER CTRL_NUMERIC_METER_LS CTRL_NUMERIC_KNOB CTRL_NUMERIC_KNOB_LS CTRL_NUMERIC_DIAL CTRL_NUMERIC_DIAL_LS CTRL_NUMERIC_VSLIDE CTRL_NUMERIC_HSLIDE CTRL_NUMERIC_FLAT_VSLIDE CTRL_NUMERIC_FLAT_HSLIDE CTRL_NUMERIC_LEVEL_VSLIDE CTRL_NUMERIC_LEVEL_VSLIDE_LS CTRL_NUMERIC_LEVEL_HSLIDE CTRL_NUMERIC_LEVEL_HSLIDE_LS CTRL_NUMERIC_POINTER_VSLIDE CTRL_NUMERIC_POINTER_VSLIDE_LS CTRL_NUMERIC_POINTER_HSLIDE CTRL_NUMERIC_POINTER_HSLIDE_LS |  |
| String | CTRL_STRING CTRL_STRING_LS |  |
| Text Message | CTRL_TEXT_MSG |  |
| Text Box | CTRL_TEXT_BOX CTRL_TEXT_BOX_LS |  |
| Command Button | CTRL_SQUARE_COMMAND_BUTTON CTRL_SQUARE_COMMAND_BUTTON_LS CTRL_OBLONG_COMMAND_BUTTON CTRL_ROUND_COMMAND_BUTTON CTRL_ROUNDED_COMMAND_BUTTON |  |
| Picture Button | CTRL_PICTURE_COMMAND_BUTTON CTRL_PICTURE_COMMAND_BUTTON_LS CTRL_PICTURE_TOGGLE_BUTTON CTRL_PICTURE_TOGGLE_BUTTON_LS |  |
| Toggle Button | CTRL_ROUND_BUTTON CTRL_SQUARE_BUTTON CTRL_SQUARE_BUTTON_LS CTRL_ROUND_FLAT_BUTTON CTRL_SQUARE_FLAT_BUTTON CTRL_ROUND_PUSH_BUTTON CTRL_SQUARE_PUSH_BUTTON CTRL_SQUARE_PUSH_BUTTON_LS CTRL_ROUND_PUSH_BUTTON2 CTRL_SQUARE_PUSH_BUTTON2 |  |
| Text Button | CTRL_SQUARE_TEXT_BUTTON CTRL_SQUARE_TEXT_BUTTON_LS CTRL_OBLONG_TEXT_BUTTON CTRL_ROUND_TEXT_BUTTON CTRL_ROUNDED_TEXT_BUTTON |  |
| Radio Button | CTRL_ROUND_RADIO_BUTTON CTRL_SQUARE_RADIO_BUTTON CTRL_CHECK_BOX |  |
| LED | CTRL_ROUND_LIGHT CTRL_SQUARE_LIGHT CTRL_ROUND_LED CTRL_ROUND_LED_LS CTRL_SQUARE_LED CTRL_SQUARE_LED_LS |  |
| Binary Switch | CTRL_HSWITCH CTRL_VSWITCH CTRL_GROOVED_HSWITCH CTRL_GROOVED_VSWITCH CTRL_TOGGLE_HSWITCH CTRL_TOGGLE_HSWITCH_LS CTRL_TOGGLE_VSWITCH CTRL_TOGGLE_VSWITCH_LS |  |
| Ring | CTRL_RING CTRL_RING_LS CTRL_RECESSED_MENU_RING CTRL_RECESSED_MENU_RING_LS CTRL_MENU_RING CTRL_MENU_RING_LS CTRL_POPUP_MENU_RING CTRL_POPUP_MENU_RING_LS |  |
| Ring Slide | CTRL_RING_VSLIDE CTRL_RING_HSLIDE CTRL_RING_FLAT_VSLIDE CTRL_RING_FLAT_HSLIDE CTRL_RING_LEVEL_VSLIDE CTRL_RING_LEVEL_VSLIDE_LS CTRL_RING_LEVEL_HSLIDE CTRL_RING_LEVEL_HSLIDE_LS CTRL_RING_POINTER_VSLIDE CTRL_RING_POINTER_VSLIDE_LS CTRL_RING_POINTER_HSLIDE CTRL_RING_POINTER_HSLIDE_LS CTRL_RING_THERMOMETER CTRL_RING_THERMOMETER_LS CTRL_RING_TANK CTRL_RING_TANK_LS CTRL_RING_GAUGE CTRL_RING_GAUGE_LS CTRL_RING_METER CTRL_RING_METER_LS CTRL_RING_KNOB CTRL_RING_KNOB_LS CTRL_RING_DIAL CTRL_RING_DIAL_LS |  |
| Picture Ring | CTRL_PICTURE_RING CTRL_PICTURE_RING_LS |  |
| List Box | CTRL_LIST CTRL_LIST_LS |  |
| Decoration | CTRL_RAISED_BOX CTRL_RAISED_BOX_LS CTRL_RECESSED_BOX CTRL_RECESSED_BOX_LS CTRL_FLAT_BOX CTRL_RAISED_CIRCLE CTRL_RECESSED_CIRCLE CTRL_FLAT_CIRCLE CTRL_RAISED_FRAME CTRL_RECESSED_FRAME CTRL_RECESSED_NARROW_FRAME CTRL_FLAT_FRAME CTRL_RAISED_ROUND_FRAME CTRL_RECESSED_ROUND_FRAME CTRL_FLAT_ROUND_FRAME CTRL_RAISED_ROUNDED_BOX CTRL_RECESSED_ROUNDED_BOX CTRL_FLAT_ROUNDED_BOX CTRL_SMOOTH_VERTICAL_BOX_LS CTRL_SMOOTH_HORIZONTAL_BOX_LS |  |
| Graph | CTRL_GRAPH CTRL_GRAPH_LS |  |
| Digital Graph | CTRL_DIGITAL_GRAPH CTRL_DIGITAL_GRAPH_LS |  |
| Strip Chart | CTRL_STRIP_CHART CTRL_STRIP_CHART_LS |  |
| Picture | CTRL_PICTURE CTRL_PICTURE_LS |  |
| Timer | CTRL_TIMER |  |
| Canvas | CTRL_CANVAS |  |
| Table | CTRL_TABLE CTRL_TABLE_LS |  |
| ActiveX | CTRL_ACTIVEX |  |
| Tree | CTRL_TREE CTRL_TREE_LS |  |
| Splitter | CTRL_HORIZONTAL_SPLITTER CTRL_HORIZONTAL_SPLITTER_LS CTRL_VERTICAL_SPLITTER CTRL_VERTICAL_SPLITTER_LS |  |
| Tab | CTRL_TABS |  |
| controlLabel | char [] | Label of the new control. Pass "" or 0 for no label. Note: This parameter is ignored for splitters, tabs, and decorations. |
| controlTop | int | Vertical coordinate at which to place the upper left corner of the control, not including labels. The coordinate must be an integer value from –32,768 to 32,767. The origin (0,0) is at the upper-left corner of the panel, directly below the title bar, before the panel is scrolled. |
| controlLeft | int | Horizontal coordinate at which to place the upper left corner of the control, not including labels. The coordinate must be an integer value from –32,768 to 32,767. The origin (0,0) is at the upper-left corner of the panel, directly below the title bar, before the panel is scrolled. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| controlID | int | Returns the ID you can use to specify the control in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the NewCtrl function:

- userint\buildui.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\ICOViewer.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewctrlmenuitem.htm language=enus -->
## TOPIC 01170: NewCtrlMenuItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewctrlmenuitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewctrlmenuitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewCtrlMenuItem

int NewCtrlMenuItem (int panelHandle, int controlID, char itemLabel[], int beforeMenuItemID, CtrlMenuCallbackPtr eventFunction, void *eventCallbackData);

#### Purpose

Adds a new menu item to the menu owned by the specified control and returns the new menu item ID that you can use in subsequent calls to specify the menu item.

#### Supported Controls

You can use NewCtrlMenuItem with the following controls:

- Tables
- Trees
- Graphs
- Strip charts

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemLabel | char [] | The name of the new menu item. To add an underline accelerator to an item name, precede the letter to be underlined with two underscores; for example __Open. |
| beforeMenuItemID | int | The menu item ID above which to insert the new menu item. Use a menuItemID you obtained from NewCtrlMenuItem or NewCtrlMenuSeparator, or use a constant that identifies one of the built-in control menu items. The following lists the built-in menu item constants: Constant Name Constant Value Control Type VAL_GOTO –2 Table VAL_FIND –3 Table, tree VAL_SORT –4 Table, tree VAL_EXPAND_SUBTREE –5 Tree VAL_COLLAPSE_SUBTREE –6 Tree VAL_EXPAND_ALL –7 Tree VAL_COLLAPSE_ALL –8 Tree VAL_PLOT_COLOR –9 Graph, strip chart VAL_PLOT_STYLE –10 Graph, strip chart VAL_PLOT_POINT_STYLE –11 Graph, strip chart VAL_PLOT_LINE_STYLE –12 Graph, strip chart VAL_PLOT_BGCOLOR –13 Graph VAL_PLOT_ORIGIN –14 Graph VAL_PLOT_FONT –15 Graph VAL_PLOT_FILL_COLOR –16 Graph VAL_PLOT_VISIBLE –17 Graph, strip chart VAL_PLOT_RENAME –18 Graph, strip chart VAL_PLOT_LINE_THICKNESS –19 Graph, strip chart VAL_FIND_NEXT –20 Table, tree VAL_FIND_PREV –21 Table, tree To place the new menu item at the bottom of the menu item list, pass –1. |
| Constant Name | Constant Value | Control Type |
| VAL_GOTO | –2 | Table |
| VAL_FIND | –3 | Table, tree |
| VAL_SORT | –4 | Table, tree |
| VAL_EXPAND_SUBTREE | –5 | Tree |
| VAL_COLLAPSE_SUBTREE | –6 | Tree |
| VAL_EXPAND_ALL | –7 | Tree |
| VAL_COLLAPSE_ALL | –8 | Tree |
| VAL_PLOT_COLOR | –9 | Graph, strip chart |
| VAL_PLOT_STYLE | –10 | Graph, strip chart |
| VAL_PLOT_POINT_STYLE | –11 | Graph, strip chart |
| VAL_PLOT_LINE_STYLE | –12 | Graph, strip chart |
| VAL_PLOT_BGCOLOR | –13 | Graph |
| VAL_PLOT_ORIGIN | –14 | Graph |
| VAL_PLOT_FONT | –15 | Graph |
| VAL_PLOT_FILL_COLOR | –16 | Graph |
| VAL_PLOT_VISIBLE | –17 | Graph, strip chart |
| VAL_PLOT_RENAME | –18 | Graph, strip chart |
| VAL_PLOT_LINE_THICKNESS | –19 | Graph, strip chart |
| VAL_FIND_NEXT | –20 | Table, tree |
| VAL_FIND_PREV | –21 | Table, tree |
| eventFunction | CtrlMenuCallbackPtr | The name of the function that processes the menu callback. This event function, type CtrlMenuCallbackPtr, takes the following form: void CVICALLBACK FunctionName (int panelHandle, int controlID, int MenuItemID, void *callbackData); When a menu selection generates a commit event, this function receives the panelHandle and controlID of the control that owns the menu generating the event and the Menu Item ID corresponding to the menu item selected. This function also receives the value you pass to eventCallbackData. |
| eventCallbackData | void * | Points to data that you define. The callback function receives the pointer. If you do not need to pass user-defined data to the callback function, or if you are not using a callback function to process the menu item event, you can use a value of zero. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| menuItemID | int | Returns the ID that you use to specify this menu item in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the NewCtrlMenuItem function:

- userint\databinding.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\events.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\TreeBusDigitalGraph.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treeList.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treemenu.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewctrlmenuseparator.htm language=enus -->
## TOPIC 01171: NewCtrlMenuSeparator

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewctrlmenuseparator.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewctrlmenuseparator.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewCtrlMenuSeparator

int NewCtrlMenuSeparator (int panelHandle, int controlID, int beforeMenuItemID);

#### Purpose

Inserts a new separator bar in the menu owned by the specified control and
returns the new menu item ID that you can use in subsequent calls to specify the separator.

#### Supported Controls

You can use NewCtrlMenuSeparator with the following controls:

- Tables
- Trees
- Graphs
- Strip charts

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| beforeMenuItemID | int | The menu item ID above which to insert the separator bar. Use a menuItemID you obtained from NewCtrlMenuItem or NewCtrlMenuSeparator, or use a constant that identifies one of the built-in control menu items. The following lists the built-in menu item constants. Constant Name Constant Value Control Type VAL_GOTO –2 Table VAL_FIND –3 Table, tree VAL_SORT –4 Table, tree VAL_EXPAND_SUBTREE –5 Tree VAL_COLLAPSE_SUBTREE –6 Tree VAL_EXPAND_ALL –7 Tree VAL_COLLAPSE_ALL –8 Tree VAL_PLOT_COLOR –9 Graph, strip chart VAL_PLOT_STYLE –10 Graph, strip chart VAL_PLOT_POINT_STYLE –11 Graph, strip chart VAL_PLOT_LINE_STYLE –12 Graph, strip chart VAL_PLOT_BGCOLOR –13 Graph VAL_PLOT_ORIGIN –14 Graph VAL_PLOT_FONT –15 Graph VAL_PLOT_FILL_COLOR –16 Graph VAL_PLOT_VISIBLE –17 Graph, strip chart VAL_PLOT_RENAME –18 Graph, strip chart VAL_PLOT_LINE_THICKNESS –19 Graph, strip chart VAL_FIND_NEXT –20 Table, tree VAL_FIND_PREV –21 Table, tree To place the separator at the bottom of the menu item list, pass –1. |
| Constant Name | Constant Value | Control Type |
| VAL_GOTO | –2 | Table |
| VAL_FIND | –3 | Table, tree |
| VAL_SORT | –4 | Table, tree |
| VAL_EXPAND_SUBTREE | –5 | Tree |
| VAL_COLLAPSE_SUBTREE | –6 | Tree |
| VAL_EXPAND_ALL | –7 | Tree |
| VAL_COLLAPSE_ALL | –8 | Tree |
| VAL_PLOT_COLOR | –9 | Graph, strip chart |
| VAL_PLOT_STYLE | –10 | Graph, strip chart |
| VAL_PLOT_POINT_STYLE | –11 | Graph, strip chart |
| VAL_PLOT_LINE_STYLE | –12 | Graph, strip chart |
| VAL_PLOT_BGCOLOR | –13 | Graph |
| VAL_PLOT_ORIGIN | –14 | Graph |
| VAL_PLOT_FONT | –15 | Graph |
| VAL_PLOT_FILL_COLOR | –16 | Graph |
| VAL_PLOT_VISIBLE | –17 | Graph, strip chart |
| VAL_PLOT_RENAME | –18 | Graph, strip chart |
| VAL_PLOT_LINE_THICKNESS | –19 | Graph, strip chart |
| VAL_FIND_NEXT | –20 | Table, tree |
| VAL_FIND_PREV | –21 | Table, tree |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| menuItemID | int | Returns the ID that you use to specify this menu item in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Examples

Refer to the following examples that use the NewCtrlMenuSeparator function:

- userint\databinding.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\TreeBusDigitalGraph.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\treemenu.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewmenu.htm language=enus -->
## TOPIC 01172: NewMenu

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewmenu.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewmenu.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewMenu

int NewMenu (int menuBarHandle, char menuName[], int beforeMenuID);

#### Purpose

Adds a new menu to a menu bar and returns a menu ID that you can use to specify the menu in subsequent function calls.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |
| menuName | char [] | New menu name to add to the menu bar. To add an underline accelerator to a menu name, precede the letter to underline with two underscores; for example, __File. |
| beforeMenuID | int | ID of the menu above which to insert the new menu. To place the new menu at the end of the menu bar, pass –1. You can obtain this ID from functions such as NewMenu and NewSubMenu. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| menuID | int | ID you use to reference the menu in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\uirview\uirview.cws for an example of using the NewMenu function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewmenubar.htm language=enus -->
## TOPIC 01173: NewMenuBar

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewmenubar.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewmenubar.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewMenuBar

int NewMenuBar (int destinationPanelHandle);

#### Purpose

Creates a new menu bar to reside on a specific panel and returns a handle to the new menu bar.

Use the new menu bar handle in subsequent function calls to specify the menu bar.

If the destination panel is not currently in memory, pass a zero as the **destinationPanelHandle**. You can later assign the menu bar to a panel using [SetPanelMenuBar](../../cvi/uiref/cvisetpanelmenubar.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| destinationPanelHandle | int | Handle of the panel on which to place the menu bar. You obtain destinationPanelHandle from LoadPanel, NewPanel, or DuplicatePanel. If the destination panel is not currently in memory, or if the menu bar is used only as a popup menu, pass a zero as the destination panel handle. You can later assign the menu bar to a panel using SetPanelMenuBar. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| menuBarHandle | int | The handle you can use in subsequent function calls to specify this menu bar. Negative values indicate that an error occurred. Zero is not a valid handle. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\uirview\uirview.cws for an example of using the NewMenuBar function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewmenuitem.htm language=enus -->
## TOPIC 01174: NewMenuItem

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewmenuitem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewmenuitem.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewMenuItem

int NewMenuItem (int menuBarHandle, int menuID, char itemName[], int beforeMenuItemID, int shortCutKey, MenuCallbackPtr eventFunction, void *eventCallbackData);

#### Purpose

Adds a new menu item to the specified menu and returns a new menu item ID that you can use in subsequent calls to specify the menu item.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| menuBarHandle | int | Specifier for a particular menu bar that is currently in memory. You can obtain this handle from functions such as LoadMenuBar and NewMenuBar. If the menu bar was automatically loaded through LoadPanel, use GetPanelMenuBar to get the menu bar handle. |
| menuID | int | ID for a particular menu within a menu bar. The ID must be a constant name, located in the .uir header file, that you assign in the User Interface Editor or a value that you obtain from functions such as NewMenu and NewSubMenu. |
| itemName | char [] | Name of the new menu item. To add an underline accelerator to an item name, precede the letter to be underlined with two underscores; for example __Open. |
| beforeMenuItemID | int | Menu item ID above which to insert the new item. To place the new menu item at the bottom of the menu item list, pass –1. |
| shortCutKey | int | The key or key combination the user can press to automatically select the menu item. Shortcut keys are 4-byte integers consisting of three bit-fields, 0x00MMVVAA, where: MM = the modifier key VV = the virtual key AA = the ASCII key You cannot use a dual-byte character as a shortcut key. When you construct a shortcut key, you can bitwise OR modifier keys with a virtual key or with an ASCII key. Either the ASCII field or the virtual key field must be all zeros. For example, the following construct produces a shortcut key of <Shift-F1>: VAL_SHIFT_MODIFIER \| VAL_F1_VKEY Similarly, the following construct produces a shortcut key of <Ctrl-D>: VAL_MENUKEY_MODIFIER \| 'D' Virtual keys do not require modifiers, but ASCII keys require at least one modifier. The following modifier keys are available: VAL_SHIFT_MODIFIER VAL_UNDERLINE_MODIFIER (the <Alt> key) VAL_MENUKEY_MODIFIER (the <Ctrl> key) VAL_SHIFT_AND_MENUKEY VAL_POPUP_MENU_VKEY The following virtual keys are available: VAL_FWD_DELETE_VKEY VAL_BACKSPACE_VKEY VAL_ESC_VKEY VAL_TAB_VKEY VAL_ENTER_VKEY VAL_UP_ARROW_VKEY VAL_DOWN_ARROW_VKEY VAL_LEFT_ARROW_VKEY VAL_RIGHT_ARROW_VKEY VAL_INSERT_VKEY VAL_HOME_VKEY VAL_END_VKEY VAL_PAGE_UP_VKEY VAL_PAGE_DOWN_VKEY VAL_F1_VKEY VAL_F2_VKEY VAL_F3_VKEY VAL_F4_VKEY VAL_F5_VKEY VAL_F6_VKEY VAL_F7_VKEY VAL_F8_VKEY VAL_F9_VKEY VAL_F10_VKEY VAL_F11_VKEY VAL_F12_VKEY The following lists the possible ASCII keys: 'A' or 'a' 'B' or 'b' 'C' or 'c' . . . 'Z' or 'z' Note There is no distinction between upper and lower case ASCII keys. |
|  | Note There is no distinction between upper and lower case ASCII keys. |  |
| eventFunction | MenuCallbackPtr | Name of the user function that processes the menu item callback. If you want to process the menu item event through a callback function, supply the name of that function as the eventFunction parameter. The event function, type MenuCallbackPtr, is prototyped as follows: void CVICALLBACK EventFunctionName (int menuBarHandle, int menuItemID, void *callbackData, int panelHandle); The event function receives the menu bar handle, itemID, and panel handle of the menu item that generates the callback. It also receives a pointer to callback data that you define. If you do not want to process the menu item event through a callback function, supply a value of zero for the eventFunction parameter. |
| eventCallbackData | void * | Points to data that you define. The callback function receives the pointer. If you do not need to pass user-defined data to the callback function, or if you are not using a callback function to process the menu item event, you can use a value of zero. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| menuItemID | int | Returns the ID that you use to specify this menu item in subsequent function calls. Negative values indicate that an error occurred. Zero is not a valid ID. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to apps\uirview\uirview.cws for an example of using the NewMenuItem function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinewpanel.htm language=enus -->
## TOPIC 01175: NewPanel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinewpanel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinewpanel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### NewPanel

int NewPanel (int parentPanelHandle, char panelTitle[], int panelTop, int panelLeft, int panelHeight, int panelWidth);

#### Purpose

Creates a new top-level panel or a new child panel inside a specific parent
panel. This function returns a panel handle that you use to specify the new panel in
subsequent function calls.

To make the panel a top-level panel, enter 0 for the **parentPanelHandle** parameter.

If you call this function to create a child panel, you must do so in the same
thread in which you create the parent panel.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parentPanelHandle | int | Handle of the panel into which to load the panel as a child panel. Pass 0 to load the panel as a top-level window. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| panelTitle | char [] | Title for the new panel. |
| panelTop | int | Vertical coordinate at which to place the upper left corner of the panel, directly below the title bar. The coordinates must be integer values from –32,768 to 32,767, or VAL_AUTO_CENTER to center the panel. For a top-level panel, (0,0) is the upper-left corner of the screen. For a child panel, (0,0) is the upper-left corner of the parent panel, directly below the title bar, before the parent panel is scrolled. |
| panelLeft | int | Horizontal coordinate at which to place the upper left corner of the panel, directly below the title bar. The coordinates must be integer values from –32,768 to 32,767, or VAL_AUTO_CENTER to center the panel. For a top-level panel, (0,0) is the upper-left corner of the screen. For a child panel, (0,0) is the upper-left corner of the parent panel, directly below the title bar, before the parent panel is scrolled. |
| panelHeight | int | Vertical size of the new panel. The height of the panel does not include the title bar or panel frame. panelHeight can be any integer value from 0 to 32,767. |
| panelWidth | int | Horizontal size of the new panel in window coordinates. The width of the panel does not include the panel frame. panelWidth can be any integer value from 0 to 32,767. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| panelHandle | int | Value you can use in subsequent function calls to specify this panel. Negative values indicate that an error occurred. Zero is not a valid panel handle. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\buildui.cws for an example of using the NewPanel function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinumeric_control_overview.htm language=enus -->
## TOPIC 01176: Numeric Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinumeric_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinumeric_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Numeric Controls Overview

Use *numeric [controls](cvioperating_controls.htm)* to input or 
view numeric values, such as voltage values. A sample numeric control appears in the following figure.

[IMAGE alt='image' src='numctrl.gif']

[Operating Numeric Controls](cvioperating_numeric_controls.htm)

[Programming Numeric Controls](cviprogramming_with_numeric_controls.htm)

[Numeric Control Attributes](cvinumeric_attributes.htm)

[Numeric Control Functions](cvinumeric_control_functions.htm)

[Numeric Control Events](cvinumeric_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinumeric_slide_attributes.htm language=enus -->
## TOPIC 01177: Numeric Slide Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinumeric_slide_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinumeric_slide_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Numeric Slide Control Attributes

The User Interface Library attributes that are valid for
[numeric slide](cvinumeric_slide_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Color Ramp Interpolate
- Color Ramp Width
- Digital Display Height
- Digital Display Left
- Digital Display Top
- Digital Display Width
- Disable Panel Theme
- Fill Color
- Fill Housing Color
- Frame Color
- Inc/Dec Arrow Width
- Marker End Angle
- Marker Start Angle
- Marker Style
- Needle Color
- Number of Color Ramp Values
- Number of Divisions
- Slide Inc/Dec Arrow Length
- Slider Color
- Slider Height
- Slider Left
- Slider Top
- Slider Width
- Tick Style
- Use Progress Bar Visual Styles
- Visible
- Show/Hide Parts
- Size/Position
- Text Style

#### Control Settings

- Control Mode
- Control Style
- Control Value
- Data Type
- Default Value
- Dimmed
- Disable Control Tooltip
- Disable Radix
- Force Smooth Dragging
- Incremental Value
- Maximum Value
- Minimum Value
- Next Panel Control
- Range Checking
- Tab Position
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinumeric_slide_control_events.htm language=enus -->
## TOPIC 01178: Numeric Slide Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinumeric_slide_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinumeric_slide_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Numeric Slide Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [numeric slide](cvinumeric_slide_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

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
- EVENT_RADIX_CHANGE
- EVENT_VAL_COERCED

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvinumeric_slide_control_overview.htm language=enus -->
## TOPIC 01179: Numeric Slide Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvinumeric_slide_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvinumeric_slide_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Numeric Slide Controls Overview

Use *numeric slide [controls](cvioperating_controls.htm)* to 
input or view numeric values, such as voltage
values. Numeric slide controls have many different graphical representations,
including knobs, meters, gauges, and dials.

Numeric slide controls include a numeric scale representing the range of
values that the control can display or that you can enter into the control. Depending on the
 [style](cvicontrol_styles.htm) of numeric slide, the 
scale can be linear or circular.

A color ramp is a gradient of colors displayed along the numeric scale of a numeric slide control. 
The image of the Numeric Dial Control in the following figure shows how a color ramp looks when implemented on a control.

Numeric slides can also include a digital display that operates like a [numeric](cvinumeric_control_overview.htm) control; 
the value of the digital display is always synchronized to the value
indicated by the scale.

The following figure shows of a sampling of different numeric slide styles.

[IMAGE alt='image' src='numslide.gif']

[Operating Numeric Slide Controls](cvioperating_numeric_slide_controls.htm)

[Programming Numeric Slide Controls](cviprogramming_with_numeric_slide_controls.htm)

[Numeric Slide Control Attributes](cvinumeric_slide_attributes.htm)

[Numeric Slide Control Functions](cvinumeric_slide_control_functions.htm)

[Numeric Slide Control Events](cvinumeric_slide_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_activex_controls.htm language=enus -->
## TOPIC 01180: Operating ActiveX Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_activex_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_activex_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating ActiveX Controls

You can operate [ActiveX controls](cviactivex_control_overview.htm) in a variety of different ways, depending on which ActiveX control you use. For more information about how to operate a particular control, refer to the documentation supplied with the control.

#### Configuring ActiveX Controls

When you create an ActiveX control in the User Interface Editor, the context menu of the ActiveX control contains a list of actions supported by the control, in addition to the standard items that are included for all built-in LabWindows/CVI controls. This menu might include shortcuts for configuring a control using its property pages or browsing its online help.

You also can configure an ActiveX control using the standard LabWindows/CVI **Edit Control** dialog box. To do this, double-click the control, as you would on any other LabWindows/CVI control.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_binary_switch_controls.htm language=enus -->
## TOPIC 01181: Operating Binary Switch Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_binary_switch_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_binary_switch_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Binary Switch Controls

Whenever you set a [binary switch](cvibinary_switch_control_overview.htm) control to a 
mode other than [indicator mode](cvicontrol_modes_for_generating_eve.htm), you can change 
its state from the keyboard or with the mouse.

You can operate a binary switch from the keyboard in the following ways:

- Press the up arrow key or <Home> to turn the switch on.
- Press the down arrow key or <End> to turn the switch off.
- Press <spacebar> or <Enter> to change the state of the switch.

To operate a binary switch with the mouse, click the switch to change its
state, or click the label corresponding to the desired state.

If the control mode of the binary switch is hot or validate, 
a [commit event](cvieventcommit.htm) is generated when the binary switch is active and 
you change its state.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_canvas_controls.htm language=enus -->
## TOPIC 01182: Operating Canvas Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_canvas_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_canvas_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Canvas Controls

Although you can set [canvas](cvioperating_controls.htm) controls to modes other than [indicator mode](cvicontrol_modes_for_generating_eve.htm), you cannot operate these controls from the keyboard or with the mouse.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_color_numeric_controls.htm language=enus -->
## TOPIC 01183: Operating Color Numeric Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_color_numeric_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_color_numeric_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Color Numeric Controls

When you set a [color numeric](cvicolor_numeric_control_overview.htm) control to any mode other than [indicator mode](cvicontrol_modes_for_generating_eve.htm), you can change its [color](cviusing_colors.htm) value from the keyboard or with the mouse.

You select the color with the aid of a color palette that you can display next
to the control. This color palette contains a set of predefined standard
colors. If the desired color is not included in the predefined colors, you can
select a button which displays a second dialog box where you can specify
any RGB value.

To display the color palette, press the spacebar or use the mouse to click anywhere within the client area of the
control.

You can navigate the color palette by selecting the desired color with the mouse
or by moving among the color choices with the arrow keys.

If the [control mode](cviattrctrlmode.htm) of a color numeric control is hot or validate, a [commit event](cvieventcommit.htm) is generated when you select a new color from the color palette.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_command_button_control.htm language=enus -->
## TOPIC 01184: Operating Command Button Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_command_button_control.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_command_button_control.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Command Button Controls

When you set a [command button](cvicommand_button_control_overview.htm) control to any mode 
other than [indicator mode](cvicontrol_modes_for_generating_eve.htm), you can operate it 
from the keyboard or with the mouse.

To operate a command button from the keyboard, press <Enter> or <spacebar> to
activate the button. If the [control mode](cviattrctrlmode.htm) of the command button is hot or validate, a [commit event](cvieventcommit.htm) is generated when you press the <Enter> key or <spacebar>. The button changes
appearance momentarily to indicate that you selected it.

To operate a command button with the mouse, click the button. The button
remains depressed until the user releases the mouse or moves off the button.
If the control mode of the command button is hot or validate, a commit event is
generated when the user clicks and releases the mouse over the command button
area. If the user releases the mouse outside of the button area, a commit event
is not generated.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_controls.htm language=enus -->
## TOPIC 01185: Operating Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Controls

A *control* is an object that resides on a [panel](cvioperating_panels.htm) to accept input from the user and to display information. The User Interface
Library supports the following control types:

| ActiveX Binary Switch Canvas Color Numeric Command Button Digital Graph Decoration Graph LED List Box Numeric Numeric Slide Picture Picture Button Picture Ring | Radio Button Ring Ring Slide Splitter String Strip Chart Tab Table Text Box Text Button Text Message Timer Toggle Button Tree |
| --- | --- |

To make a control ready to accept input, click the control
or press <Tab> or <Shift-Tab> to move from one control to the next. 
Pressing <Alt>
and the underlined letter in the label of the control makes that control ready to
accept input, provided that no accessible [menu bars](cvioperating_menu_bars.htm) contain a menu with the same underlined letter. On some controls, such as
command buttons, pressing <Alt> and the underlined letter generates a [commit event](cvieventcommit.htm).

#### Data Types of Controls

Every control has a *data type* associated with it. The data type of the control 
determines the data type of variables used to set and obtain the value of the control. The following 
list shows LabWindows/CVI control data types, but keep in mind that not all data 
types are valid for each type of control.

unsigned char 

char 

char * 

unsigned short int 

short int 

unsigned long int 

long int 

float 

double 

unsigned long long int 

long long int 

size_t 

signed size_t 

pointer difference 

unsigned pointer-sized integer 

pointer-sized integer

**Related Topics**

[Programming Controls](cviprogramming_with_controls.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_decoration_controls.htm language=enus -->
## TOPIC 01186: Operating Decoration Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_decoration_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_decoration_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Decoration Controls

You can set [decoration](cvidecoration_control_overview.htm) controls only 
to [indicator mode](cvicontrol_modes_for_generating_eve.htm). For that reason, you cannot 
operate them from the keyboard or with the mouse.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_digital_graph_controls.htm language=enus -->
## TOPIC 01187: Operating Digital Graph Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_digital_graph_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_digital_graph_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Digital Graph Controls

[Digital graph](cvidigital_graph_control_overview.htm) controls are always [indicators](cvicontrol_modes_for_generating_eve.htm). For this reason, you cannot operate them from the keyboard or with the mouse.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_graph_controls.htm language=enus -->
## TOPIC 01188: Operating Graph Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_graph_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_graph_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Graph Controls

When you set a [graph](cvigraph_control_overview.htm) control to any mode other than [indicator 
mode](cvicontrol_modes_for_generating_eve.htm), you can operate graph cursors and zoom and pan the viewport from the keyboard or with the mouse. You also can use the mouse to operate graph annotations 
or access a customization menu from the graph legend.

#### Graph Cursors

You can associate [one or more cursors](cviattrnumcursors.htm) with graph controls. 
Use cursors to select a point or region of the graph for more processing or analysis. If you set the mode of the graph control
to hot, cursors generate [commit events](cvieventcommit.htm). If you want to use cursors in a graph control, 
set the graph control to a mode other than indicator.

You can traverse the graph with both [free-form and snap-to-point](cviattrcursormode.htm) cursors. 
By default, graph cursors for which [ATTR_CURSOR_MODE](cviattrcursormode.htm)
is VAL_SNAP_TO_POINT snap to the closest [point](cviplotpoint.htm), 
[polygon](cviplotpolygon.htm), [waveform](cviplotwaveform.htm), [X](cviplotx.htm), [XY](cviplotxy.htm)
, or [Y](cviploty.htm) plot. If you want to prevent cursors from snapping to a certain plot, set 
[ATTR_PLOT_SNAPPABLE](cviattrplotsnappable.htm) for the plot to FALSE.

You can use the keyboard to operate a graph as described in the following table:

**Keyboard Actions for Cursors**

| Type of Cursor | When you press... | You select... |
| --- | --- | --- |
| Free-form and snap-to-point | <Page-Up> | Previous cursor. |
|  | <Page-Down> | Next cursor. |
| Free-form | Left arrow key | Left 10 pixels. |
|  | Right arrow key | Right 10 pixels. |
|  | Up arrow key | Up 10 pixels. |
|  | Down arrow key | Down 10 pixels. |
|  | <Shift>-left arrow key | Left 1 pixel. |
|  | <Shift>-right arrow key | Right 1 pixel. |
|  | <Shift>-up arrow key | Up 1 pixel. |
|  | <Shift>-down arrow key | Down 1 pixel. |
|  | <Ctrl>-left arrow key | To the left edge of the plot area. |
|  | <Ctrl>-right arrow key | To the right edge of the plot area. |
|  | <Ctrl>-up arrow key | To the top edge of the plot area. |
|  | <Ctrl>-down arrow key | To the bottom edge of the plot area. |
|  | <Home> | To the lower left corner of the plot area. |
|  | <End> | To the upper right corner of the plot area. |
| Snap-to-point | Left arrow key | To the previous point on the current plot. |
|  | Right arrow key | To the next point on the current plot. |
|  | Up arrow key | To the next point on the current plot. |
|  | Down arrow key | To the previous point on the current plot. |
|  | <Shift>-left arrow key | Back 10 points on the current plot. |
|  | <Shift>-right arrow key | Forward 10 points on the current plot. |
|  | <Shift>-up arrow key | Forward 10 points on the current plot. |
|  | <Shift>-down arrow key | Back 10 points on the current plot. |
|  | <Ctrl>-left arrow key | Left to the closest point in the x direction on the current plot. |
|  | <Ctrl>-right arrow key | Right to the closest point in the x direction on the current plot. |
|  | <Ctrl>-up arrow key | Up to the closest point in the y direction on the current plot. |
|  | <Ctrl>-down arrow key | Down to the closest point in the y direction on the current plot. |
|  | <Home> | To the first visible point on the current plot. |
|  | <End> | To the last visible point on the current plot. |
|  | <Shift-Page Up> | To the previous plot. |
|  | <Shift-Page Down> | To the next plot. |

If you configure the graph as a hot control, you generate an event whenever
you press one of the keys in the preceding table.

You can use the mouse to operate a graph with cursors in the following ways:

- Drag a cursor to move it. If the cursor is in snap-to-point mode, the cursor
tracks the mouse until you release the mouse button, and then the cursor snaps
to the nearest data point. If the cursor is in free-form mode, the cursor tracks
the mouse until you release the mouse button, and then the cursor stays at the
new position.
- Move a cursor left and right by holding down <Shift> and dragging the vertical cross hair line projecting outward from the cursor position. Likewise, you can move a cursor up and down by dragging the horizontal cross hair line.

The following behaviors generate a commit event in a graph control that you
set to hot mode:

- When the user moves the cursor with the arrow keys
- When the user releases the mouse after moving a cursor

[Value changed events](cvieventvalchanged.htm) are generated continuously while a user drags a graph cursor.

#### Graph Annotations

You can add annotations to graph controls to mark specific data points on the graph. If you want to operate annotations in a graph control, set the graph control to a mode other than [indicator](cviattrctrlmode.htm). Use the mouse to move an annotation caption. This action generates [value changed events](cvieventvalchanged.htm) continuously. You generate a commit event when you release the mouse after moving an annotation caption. When you drag an annotation caption, the caption moves to the front of the z-plane order. The caption moves back to its original z-plane position when you release the mouse.

#### Interactive Graph Legend

If you enable [ATTR_LEGEND_INTERACTIVE](cviattrlegendinteractive.htm) or enable the **Interactive Legend** option in the User Interface Editor **Legend Settings** dialog box, you give users the ability to edit various plot attributes at run time. When you enable this attribute or option, a user can right-click a graph legend at run time to launch a customization menu, which includes items such as plot color, plot style, and so on. You also can use the customization menu to rename the selected plot. Some customization menu items are not available for all plot styles.

|  | Note The customization menu is unavailable if the graph is in indicator mode. |
| --- | --- |

#### Editing Axis Labels

If you enable [ATTR_ENABLE_EDITABLE_AXES](cviattrenableeditableaxes.htm) or enable the **Editable graph axes** option in the User Interface Editor **Edit Graph** dialog box, you give users the ability to edit graph axis labels at run time.

|  | Note This functionality is available only if the graph is in normal or hot mode and the axis scaling mode is set to VAL_MANUAL or VAL_LOCK. If you enable the ATTR_XUSE_LABEL_STRINGS or ATTR_YUSE_LABEL_STRINGS attribute, you cannot use editable axis labels. If you set ATTR_XFORMAT or ATTR_YFORMAT to VAL_RELATIVE_TIME_FORMAT or VAL_ABSOLUTE_TIME_FORMAT, you also cannot use editable axis labels. |
| --- | --- |

If you enable this attribute, a user can double-click the minimum or maximum axis label value to edit it. When the user modifies the value, the axis range changes based on the new value and LabWindows/CVI generates an [EVENT_AXIS_VAL_CHANGE](cvieventaxisvalchange.htm) event. If the user double-clicks a label value that is not the minimum or maximum, the graph does not change.

If the user modifies a label value so that the minimum value becomes greater than or equal to the maximum value (or so that the maximum value becomes less than or equal to the minimum value), LabWindows/CVI pans the axis range. For example, if a graph has an x-axis range with 0 as the minimum and 10 as the maximum, and the user changes the minimum to 20, LabWindows/CVI displays the graph so that its x-axis ranges from 20 to 30. If the user enters an invalid number or string, LabWindows/CVI ignores the input and reverts the label to its original value.

If you set [ATTR_XMAP_MODE](cviattrxmapmode.htm) or [ATTR_YMAP_MODE](cviattrymapmode.htm) to VAL_LOG or if you enable the **Log Scale** option in the User Interface Editor **Edit Axis Settings** dialog box, LabWindows/CVI will coerce the value the user enters to a valid log value. If the user modifies a label value so that the new minimum value becomes greater than the existing maximum value or the new maximum value becomes less than the existing minimum value, LabWindows/CVI pans the log scales by the difference in power between the original minimum and maximum values. For example, if the graph has an x-axis range with 1 as the minimum and 100 as the maximum, and the user changes the minimum to 1,000, the new maximum is the new value (1,000) times the original difference in power (100) for a result of 100,000.

|  | Note Refer to the ATTR_XLOOSE_FIT_AUTOSCALING_UNIT or ATTR_YLOOSE_FIT_AUTOSCALING_UNIT topics for more information about how LabWindows/CVI determines new minimum and maximum values using loose fit linear and logarithmic autoscaling units. |
| --- | --- |

##### Editing Axis Labels in the User Interface Editor

You also can edit graph axis values in the User Interface Editor using the Operate Tool, Edit Text Tool, or Quick Edit Window. When you edit graph axis values in the User Interface Editor, the graph must be in normal or hot mode, but you do not have to enable ATTR_ENABLE_EDITABLE_AXES or set the axis scaling mode to VAL_MANUAL or VAL_LOCK. LabWindows/CVI saves the new graph axis values if you use the Edit Text Tool or Quick Edit Window but does not save the new values if you use the Operate Tool.

#### Zooming and Panning on Graphs

You can use *zooming*—the ability to expand or contract the viewport around a particular point or area—in graph controls. When you zoom *in*, 
the logical area contained in the viewport gets smaller, showing the area with more resolution. When you zoom *out*, the viewport shows a wider area. 
You can also use *panning*, the ability to shift the viewport.

By default, zooming and panning are disabled. To [enable zooming and panning](cviattrenablezoomandpan.htm) in a graph control, 
set the graph control to a mode other than indicator. Then set one of the following available zooming modes in the Edit Graph dialog box or programmatically:

- If you set Zoom style to Zoom to rectangle in the Edit Graph dialog box or set ATTR_ZOOM_STYLE to VAL_ZOOM_TO_RECT , 
users can define a rectangular zone that will become the new limits of the graph. To select these bounds, press <Ctrl> and 
click and hold the left mouse button to define the first corner of the box. Drag the mouse to define the opposite corner of the rectangle. 
When you are satisfied with the new boundaries of the graph, release the mouse button.
- If you set Zoom style to X-zoom or Y-zoom in the Edit Graph dialog box or set 
 ATTR_ZOOM_STYLE to VAL_ZOOM_XAXIS or 
 VAL_ZOOM_YAXIS , 
users can zoom along a single axis. Select a rectangle as you do with Zoom to rectangle and within this zone, the view will zoom in along the specified
axis.
- If you set Zoom style to Zoom around point in the Edit Graph dialog box or set 
 ATTR_ZOOM_STYLE to VAL_ZOOM_AROUND_PT , 
users can select a point around which to zoom. Press <Ctrl> and click and hold the left mouse button to select a point. The resolution in the viewport increases 
dynamically until you release the mouse; you can release <Ctrl> anytime. If you drag the mouse, the zooming continues recentered on the new point 
under the cursor. To stop zooming, release the left mouse button.

To pan, press <Ctrl-Shift>, click and hold the left mouse button, and drag the mouse to new point. The graph viewport scrolls so that a new portion of the 
graph is visible. You can drag the mouse anywhere on the screen, even beyond the viewport. Panning is available whenever you enable zooming.

To zoom out, press <Ctrl> and click and hold the right mouse button. In **Zoom around point** mode, the resolution in the viewport decreases 
dynamically until you release the mouse. In all other modes, the resolution incrementally decreases by 10% along the zoomed axes. You also can undo up to 25 of the 
most recent pans or zooms by pressing <Ctrl-Space> to reverse each successive change.

|  | Note If you enable autoscaling for the graph, autoscaling is disabled while you zoom or pan. If you plot additional data during zooming or panning, LabWindows/CVI completes the zooming or panning and then displays the new data with autoscaling. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_led_controls.htm language=enus -->
## TOPIC 01189: Operating LED Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_led_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_led_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating LED Controls

By default, [LED](cviled_control_overview.htm) controls are indicators and therefore are not operable. However, you can
change the [control mode](cvicontrol_modes_for_generating_eve.htm) of the LED to normal, hot,
 or validate, and consequently render them operable.

You can operate an LED control from the keyboard by pressing the <Spacebar> or
<Enter> key to change the state of the LED.

To operate an LED with the mouse, click the LED to change its state.

If the control mode of the LED is hot or validate, a [commit event](cvieventcommit.htm) is generated when the LED is active and you change its state.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_list_box_controls.htm language=enus -->
## TOPIC 01190: Operating List Box Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_list_box_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_list_box_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating List Box Controls

When you set a [list box](cvilist_box_control_overview.htm) control to any mode other 
than [indicator mode](cvicontrol_modes_for_generating_eve.htm), you can select items from 
the keyboard or with the mouse.

You can operate a list box control from the keyboard in the following ways:

- Press the up arrow key to highlight the previous list item.
- Press the down arrow key to highlight the next list item.
- Press <Home> to scroll to the top of the list.
- Press <End> to scroll to the bottom of the list.
- Press <Page Up> to scroll up one page.
- Press <Page Down> to scroll down one page.
- Use the Quick Type feature to locate a list item. For example, when you press
the <M> key, Quick Type takes you to the first occurrence of an item beginning
with "M." When you type a complete item name Quick Type takes you to that item.
When you delay one second or more and then press a key, the Quick Type buffer
is flushed.
- Press the left arrow key to go to the previous item in the Quick Type buffer.
- Press the right arrow key to go to the next item in the Quick Type buffer.
- If the list box is in check mode , 
press <spacebar> to toggle the check mark of the current item.

You can operate a list box control with the mouse in the following ways:

- Click an item to highlight it; this action toggles the check mark when in
check mode.
- Hold the mouse button down on either arrow to scroll through the list.
- Drag the scroll bar marker to a new position.
- Click above the scroll bar marker to scroll up one page.
- Click below the scroll bar marker to scroll down one page.

You can generate a [commit event](cvieventcommit.htm) when a list 
box is set to hot or validate mode in the following ways:

- When the control is set to Check Mode, select an item in the list box and
press <spacebar> or click it.
- When the control is not set to Check Mode, select an item in the list box and
press <Enter> or double-click it.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_menu_bars.htm language=enus -->
## TOPIC 01191: Operating Menu Bars

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_menu_bars.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_menu_bars.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Menu Bars

You can operate a menu bar from the keyboard in the following ways:

- Press <Alt> and the underlined letter of the menu title to display a menu or
execute an immediate action menu. When a menu appears, its title is highlighted.
- Press the right or left arrow key to display adjacent menus.
- Press the up or down arrow key or the underlined letter of the menu item to
select items in a menu. When an item is selected, its label is highlighted.
- Press <Enter> to execute the highlighted item and remove the menu.
- Press <Esc> to remove the menu without executing a menu item.

You can operate a menu bar with the mouse in the following ways:

- Click the menu title to display a menu or execute an immediate menu.
- Click the menu item to execute an item within a menu. The menu disappears.
- Click anywhere outside the menu to remove the menu without executing the menu item.

You cannot select menu titles and menu items that are dimmed.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_numeric_controls.htm language=enus -->
## TOPIC 01192: Operating Numeric Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_numeric_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_numeric_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Numeric Controls

When you set a [numeric](cvinumeric_control_overview.htm) control to any mode other than [indicator mode](cvicontrol_modes_for_generating_eve.htm), you can change its value from the keyboard or with the mouse.

|  | Note When you enter a number in scientific notation into controls of type int64 or unsigned int64, LabWindows/CVI converts the number to a double and then to a 64-bit integer. This conversion may cause a loss of precision after 15 decimal digits. |
| --- | --- |

You can operate a numeric control from the keyboard in the following ways:

- Press the left or right arrow key to move the cursor within the control.
- Press the up or down arrow key to increase or decrease the value displayed in
the control.
- Press <Home> to move the cursor to the beginning of the text.
- Press <End> to move the cursor to the end of the text.
- Press <Shift-Home> to highlight all text to the left of the cursor.
- Press <Shift-End> to highlight all text to the right of the cursor.

You can operate a numeric control with the mouse by clicking the up or down
arrow buttons to change the value of the control.

If the [control mode](cviattrctrlmode.htm) of a numeric control is hot or validate, a [commit event](cvieventcommit.htm) is generated when you press the up or down arrow keys, or when you enter a
new value and then press the <Enter> or <Tab> key, or click another object
with the mouse.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_splitter_controls.htm language=enus -->
## TOPIC 01193: Operating Splitter Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_splitter_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_splitter_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Splitter Controls

When you set a [splitter](cvisplitter_control_overview.htm) control to any [mode](cvicontrol_modes_for_generating_eve.htm) other than indicator mode, you can move or resize elements on a panel using the mouse or keyboard.

In order to use a splitter control to move or resize elements on a panel, you must attach other controls or panels to the splitter control. You can attach multiple controls and child panels to each side of the splitter—left and right or above and below.

Panels that you operate with a splitter control must be child panels.

When you hover over the splitter control, the cursor becomes a different icon, which you can specify. Click and drag the splitter either horizontally or vertically. When you drag the splitter, a drag line appears, parallel to the splitter and of the same length, that shows where the splitter is being dragged.

If you specify that the attached control or panel be resized, the controls and panels are sized so that the edge nearest to the splitter control preserves its distance from the splitter control. If you attach a control or panel to the right side of the splitter control and drag to the right, the control or panel becomes smaller. If you attach a control or panel to the left side of the splitter control and drag to the right, the control or panel becomes larger. You cannot size the control or panel past the point where any attached control or panel is reduced to its standard minimum size.

If you specify that the attached control or panel be moved, the controls and panels move so that the edge nearest to the splitter control preserves its distance from the splitter control. By default you cannot move the splitter control past the edge of the panel.

You also can operate the splitter using the keyboard. Make sure that the splitter has the keyboard focus and use the arrow keys. If you hold down the <Shift> key, you can move the splitter one pixel at a time.

To use a splitter control as a line decoration, select a classic-style splitter (CTRL_HORIZONTAL_SPLITTER or CTRL_VERTICAL_SPLITTER), set the color with ATTR_FRAME_COLOR, set the thickness with ATTR_FRAME_THICKNESS, and then set ATTR_OPERABLE_AS_INDICATOR to FALSE.

If you set the splitter control to indicator mode, you must enable the **Operable as an Indicator** option or set the [ATTR_OPERABLE_AS_INDICATOR](cviattroperableasindicator.htm) attribute to TRUE to interact with the control using the mouse. Setting the splitter to indicator mode prevents it from having the keyboard focus.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_tab_controls.htm language=enus -->
## TOPIC 01194: Operating Tab Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_tab_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_tab_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Tab Controls

When you set a [tab](cvitab_control_overview.htm) control to any [mode](cvicontrol_modes_for_generating_eve.htm) other than indicator mode, you can use the keyboard and mouse to interact with the tab control and the controls on the tab control. Interactions with the tab control do not generate commit events.

To select a page from the tab control, click the tab. Selecting a tab makes the tab page active, and you can interact with all of the controls on that tab page. LabWindows/CVI automatically includes the controls on the active page of the tab control when you tab through the controls on the parent panel.

You also can use the keyboard to select tabs. Use the arrow keys to move between tabs. The left and right arrow keys move through tabs located on the top and bottom sides of the tab control; the up and down arrow keys move through tabs located on the left and right sides of the tab control. You also can change the active tab by pressing <Ctrl-Tab> or <Ctrl-Shift-Tab> when the keyboard focus is on a control in a tab page or when the focus is on the tab control itself. If you assigned an accelerator key to the tab, you can press <Alt> plus the underlined letter to select the tab.

If you select **Multiple Rows** as the **Tabs Fit Mode**, selecting a tab on any row besides the first row moves the entire row that contains that tab to the first row.

To create controls on a tab page, you can right-click inside the tab page to access the Controls palette. You also can right-click the panel, select a control, and then copy or cut and paste the control onto the tab page.

You can edit the tab order of the controls within a page by selecting **Tab Order** in the Edit Tab dialog box. You also can click inside the tab control and select **Edit»Tab Order**

To drag a tab control in the User Interface Editor, click the the active tab or click the empty space past the last tab.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvioperating_toggle_button_controls.htm language=enus -->
## TOPIC 01195: Operating Toggle Button Controls

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvioperating_toggle_button_controls.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvioperating_toggle_button_controls.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Operating Toggle Button Controls

When you set a [toggle button](cvitoggle_button_control_overview.htm) control to any mode 
other than [indicator mode](cvicontrol_modes_for_generating_eve.htm), you can operate it from 
the keyboard or with the mouse.

You can operate a toggle button control from the keyboard by pressing the
<spacebar> or <Enter> key to change the state of the button.

To operate a toggle button with the mouse, click the button to change its state.

If the [control mode](cviattrctrlmode.htm) of the toggle button is hot or validate, a [commit event](cvieventcommit.htm) is generated when the button is active and you change its state.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipanel_attributes.htm language=enus -->
## TOPIC 01196: Panel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipanel_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipanel_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Panel

#### Panel Appearance

- Background Color
- Dimmed
- Frame Actual Height
- Frame Actual Width
- Frame Color
- Frame Style
- Frame Thickness
- Horizontal Scroll Bar Offset
- Horizontal Scroll Bar Offset Max
- Menu Height
- Menu Width
- Menubar Visible
- Scroll Bar Color
- Scroll Bar Size
- Scroll Bar Style
- Scroll Bars
- System Menu Visible
- Vertical Scroll Bar Offset
- Vertical Scroll Bar Offset Max
- Visible
- Window Zoom
- Size/Position

#### Panel Settings

- Activate When Clicked On
- Can Maximize
- Can Minimize
- Close Control
- Close Item Visible
- Conform to System Colors
- Conform to System Theme
- Encoding
- First Child Panel
- First Panel Control
- Floating Panel
- Has Taskbar Button
- Menubar Constant Name
- Menubar Constant Name Length
- Minimize Other Panels
- Minimum Height for Scaling
- Minimum Width for Scaling
- Mouse Cursor
- Movable
- Next Panel
- Number of Child Panels
- Number of Controls
- Owner Thread
- Panel or Its Child is Active
- Parent Panel
- Parent Shares Shortcut Keys
- Resolution Adjustment
- Scale Contents on Resize
- Sizable
- System Window Handle
- Z-Plane Position

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

#### Title and Titlebar Appearance

- Title
- Title Background Color
- Title Bold
- Title Character Set
- Title Color
- Title Font
- Title Font Name Length
- Title Italics
- Title Length
- Title Point Size
- Title Size to Font
- Title Strikeout
- Title Underline
- Titlebar Actual Thickness
- Titlebar Style
- Titlebar Thickness
- Titlebar Visible

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipanel_events.htm language=enus -->
## TOPIC 01197: Panel Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipanel_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipanel_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Panel Events

The User Interface Library [events](cvievents_overview.htm) that are sent to [panel](cvioperating_panels.htm) [callback](cviusing_callback_functions_to_resp.htm) functions appear in the following list.

[EVENT_CLOSE](cvieventclose.htm)

[EVENT_DISCARD](cvieventdiscard.htm)

[EVENT_GOT_FOCUS](cvieventgotfocus.htm)

[EVENT_HSCROLL](cvieventhscroll.htm)

[EVENT_KEYPRESS](cvieventkeypress.htm)

[EVENT_LEFT_CLICK](cvieventleftclick.htm)

[EVENT_LEFT_CLICK_UP](cvieventleftclickup.htm)

[EVENT_LEFT_DOUBLE_CLICK](cvieventleftdoubleclick.htm)

[EVENT_LOST_FOCUS](cvieventlostfocus.htm)

[EVENT_MOUSE_POINTER_MOVE](cvieventmousepointermove.htm)

[EVENT_MOUSE_WHEEL_SCROLL](cvieventmousewheelscroll.htm)

[EVENT_PANEL_MAXIMIZE](cvieventpanelmaximize.htm)

[EVENT_PANEL_MINIMIZE](cvieventpanelminimize.htm)

[EVENT_PANEL_MOVE](cvieventpanelmove.htm)

[EVENT_PANEL_MOVING](cvieventpanelmoving.htm)

[EVENT_PANEL_RESTORE](cvieventpanelrestore.htm)

[EVENT_PANEL_SIZE](cvieventpanelsize.htm)

[EVENT_PANEL_SIZING](cvieventpanelsizing.htm)

[EVENT_RIGHT_CLICK](cvieventrightclick.htm)

[EVENT_RIGHT_CLICK_UP](cvieventrightclickup.htm)

[EVENT_RIGHT_DOUBLE_CLICK](cvieventrightdoubleclick.htm)

[EVENT_VSCROLL](cvieventvscroll.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipanel_functions.htm language=enus -->
## TOPIC 01198: Panel Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipanel_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipanel_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Panel Functions

The User Interface Library functions that operate on [panels](cvioperating_panels.htm) appear in the following list:

| DefaultPanel | LoadPanel |
| --- | --- |
| DiscardPanel | LoadPanelEx |
| DisplayPanel | NewCtrl |
| DuplicatePanel | NewPanel |
| DuplicatePanelTree | PrintPanel |
| GetActivePanel | RecallPanelState |
| GetPanelAttribute | SavePanelState |
| GetPanelDisplayBitmap | SetActivePanel |
| GetScaledPanelDisplayBitmap | SetPanelAttribute |
| GetSharedMenuBarEventPanel | SetPanelMenuBar |
| HidePanel | SetPanelPos |
| InstallPanelCallback | SetPanelSize |
| LoadMenuBar | ValidatePanel |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipanels_and_multithreading.htm language=enus -->
## TOPIC 01199: Panels and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipanels_and_multithreading.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipanels_and_multithreading.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Panels and Multithreading

You must [discard](cvidiscardpanel.htm) a [panel](cvioperating_panels.htm) in the same [thread](cvidifferent_approaches_to_multithr.htm) in which you [load](cviloadpanel.htm) or [create](cvinewpanel.htm) it. Before a thread terminates, explicitly discard all panels you loaded or
created in that thread.

If you create a [child panel](cvichild_panels.htm), you must do so in the same thread in which you create or load the top-level
panel. You can create [controls](cvioperating_controls.htm) other than [timer](cvitimer_control_overview.htm) controls in any thread.

If you call [InstallPopup](cviinstallpopup.htm) on a panel, you must do so in the same thread in which you create or load the
panel. The [pop-up](cvioperating_popup_panels.htm) is [modal](../bp_glossary.htm#modal) only with respect to other panels you load or create in the same
thread. You must call [RemovePopup](cviremovepopup.htm) in the same thread.

You can call [SetPanelPos](cvisetpanelpos.htm) and [SetPanelSize](cvisetpanelsize.htm) on a top-level panel only in the thread in which you load or create it.

The following panel attributes, when applied to a top-level panel, can be set
only in the thread in which you load or create the panel:

- ATTR_FLOATING
- ATTR_SIZABLE
- ATTR_MOVABLE
- ATTR_CAN_MINIMIZE
- ATTR_CAN_MAXIMIZE
- ATTR_CLOSE_ITEM_VISIBLE
- ATTR_SYSTEM_MENU_VISIBLE
- ATTR_TITLEBAR_VISIBLE
- ATTR_WIDTH
- ATTR_HEIGHT
- ATTR_TOP
- ATTR_LEFT
- ATTR_TITLE
- ATTR_HAS_TASKBAR_BUTTON
- ATTR_ENCODING

If you enable the ATTR_FLOATING attribute on a panel, the panel floats only with respect to panels that you
load or create in the same thread.

|  | Note Keep in mind the restrictions mentioned in this topic whenever you create a DLL that displays one or more LabWindows/CVI panels; in particular, DLL functions that you call from different threads are affected by these restrictions. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_attributes.htm language=enus -->
## TOPIC 01200: Picture Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Control Attributes

The User Interface Library attributes that are valid for
[picture](cvipicture_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Frame Color
- Frame Thickness
- Picture Background Color
- Visible
- Show/Hide Parts
- Size/Position

#### Control Settings

- Control Style
- Dimmed
- Disable Control Tooltip
- Fit Mode
- Next Panel Control
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

- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_button_attributes.htm language=enus -->
## TOPIC 01201: Picture Button Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_button_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_button_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Button Control Attributes

The User Interface Library attributes that are valid for
[picture button](cvipicture_button_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Command Button Color
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
- Fast Draw Picture Button (Obsolete)
- Fit Mode
- Image File
- Image File Name Length
- Next Panel Control
- Shortcut Key
- Subimage Enable
- Subimage Height
- Subimage Left
- Subimage Top
- Subimage Width
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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_button_control_events.htm language=enus -->
## TOPIC 01202: Picture Button Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_button_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_button_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Button Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [picture button](cvipicture_button_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_button_control_functions.htm language=enus -->
## TOPIC 01203: Picture Button Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_button_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_button_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Button Control Functions

The following User Interface Library functions operate on [picture button](cvipicture_button_control_overview.htm) controls.

- AddCtrlToSplitter
- AllocImageBits
- DefaultCtrl
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBitmap
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlVal
- GetImageBits
- GetImageInfo
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlBitmap
- SetCtrlVal
- SetImageBits
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_button_control_overview.htm language=enus -->
## TOPIC 01204: Picture Button Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_button_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_button_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Button Controls Overview

Use *picture button* [*controls*](cvioperating_controls.htm) to
 trigger an action or to select between two different states. They differ from
 [command buttons](cvicommand_button_control_overview.htm) or
 [toggle buttons](cvitoggle_button_control_overview.htm) in that a picture button
 can display a [bitmap](cviusing_bitmap_objects.htm) instead of a label.

There are two [styles](cvicontrol_styles.htm) of picture button control: 
picture command button (CTRL_PICTURE_COMMAND_BUTTON) and picture toggle button (CTRL_PICTURE_TOGGLE_BUTTON).

A sample picture button control appears in the following figure.

[IMAGE alt='image' src='picbutcl.gif']

[Operating Picture Button Controls](cvioperating_picture_button_control.htm)

[Programming Picture Button Controls](cviprogramming_with_picture_button_controls.htm)

[Picture Button Control Attributes](cvipicture_button_attributes.htm)

[Picture Button Control Functions](cvipicture_button_control_functions.htm)

[Picture Button Control Events](cvipicture_button_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_control_events.htm language=enus -->
## TOPIC 01205: Picture Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [picture](cvipicture_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_DISCARD
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_control_functions.htm language=enus -->
## TOPIC 01206: Picture Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Control Functions

The following User Interface Library functions operate on [picture](cvipicture_control_overview.htm) controls.

- AddCtrlToSplitter
- AllocImageBits
- DeleteImage
- DiscardCtrl
- DisplayImageFile
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBitmap
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetImageBits
- GetImageInfo
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- InsertCtrlArrayItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlBitmap
- SetImageBits
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_control_overview.htm language=enus -->
## TOPIC 01207: Picture Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Controls Overview

Use a *picture [control](cvioperating_controls.htm)* to place images on [panels](cvioperating_panels.htm), such as logos and diagrams. For example, you can use a picture control to
place a schematic that instructs the user how to connect a unit for testing. A
sample picture control appears in the following figure.

[IMAGE alt='image' src='piccontr.gif']

**Picture Control**

[Operating Picture Controls](cvioperating_picture_controls.htm)

[Programming Picture Controls](cviprogramming_with_picture_controls.htm)

[Picture Control Attributes](cvipicture_attributes.htm)

[Picture Control Functions](cvipicture_control_functions.htm)

[Picture Control Events](cvipicture_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_ring_attributes.htm language=enus -->
## TOPIC 01208: Picture Ring Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_ring_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_ring_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Ring Control Attributes

The User Interface Library attributes that are valid for
[picture ring](cvipicture_ring_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Frame Color
- Inc/Dec Arrow Width
- Picture Background Color
- Visible
- Show/Hide Parts
- Size/Position

#### Control Settings

- Control Mode
- Control Style
- Control Value
- Data Type
- Default Value
- Default Value Length
- Dimmed
- Disable Control Tooltip
- Fit Mode
- Next Panel Control
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position
- Index

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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_ring_control_events.htm language=enus -->
## TOPIC 01209: Picture Ring Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_ring_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_ring_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Ring Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [picture ring](cvipicture_ring_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_ring_control_functions.htm language=enus -->
## TOPIC 01210: Picture Ring Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_ring_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_ring_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Ring Control Functions

The following User Interface Library functions operate on [picture ring](cvipicture_ring_control_overview.htm) controls.

- AddCtrlToSplitter
- AllocImageBits
- ClearListCtrl
- DefaultCtrl
- DeleteListItem
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBitmap
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlIndex
- GetCtrlVal
- GetImageBits
- GetImageInfo
- GetIndexFromValue
- GetLabelFromIndex
- GetLabelLengthFromIndex
- GetNumListItems
- GetRelativeMouseState
- GetScaledCtrlDisplayBitmap
- GetValueFromIndex
- GetValueLengthFromIndex
- InsertCtrlArrayItem
- InsertListItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- ReplaceListItem
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlBitmap
- SetCtrlIndex
- SetCtrlVal
- SetImageBits
- SetInputMode

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvipicture_ring_control_overview.htm language=enus -->
## TOPIC 01211: Picture Ring Controls Overview

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvipicture_ring_control_overview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvipicture_ring_control_overview.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Picture Ring Controls Overview

Use *picture ring [controls](cvioperating_controls.htm)* to select 
from a group of items. Each item is stored in the ring control in the form of an image/value pair, 
where the image is a [bitmap](cviusing_bitmap_objects.htm) displayed by the control when 
the item is selected, and the value is the numeric or string value corresponding to that 
item. A sample picture ring control appears in the following figure.

[IMAGE alt='image' src='picring.gif']

[Operating Picture Ring Controls](cvioperating_picture_ring_controls.htm)

[Programming Picture Ring Controls](cviprogramming_with_picture_ring_controls.htm)

[Picture Ring Control Attributes](cvipicture_ring_attributes.htm)

[Picture Ring Control Functions](cvipicture_ring_control_functions.htm)

[Picture Ring Control Events](cvipicture_ring_control_events.htm)

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotarc.htm language=enus -->
## TOPIC 01212: PlotArc

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotarc.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotarc.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotArc

int PlotArc (int panelHandle, int controlID, double x1, double y1, double x2, double y2, int beginAngle, int arcAngle, int color, int fillColor);

#### Purpose

Plots an arc onto a graph control.

Define the arc by specifying two opposing corners of a rectangle that enclose the arc, along with a beginning angle, in tenths of degrees, and an arc angle, in tenths of degrees.

For example, if **x1**=0.0, **y1**=0.0, **x2**=200.0, **y2**=200.0, **beginAngle**=0, and **arcAngle**=3600, then PlotArc plots a circle centered on coordinates (100.0,100.0).

#### Supported Controls

You can use PlotArc with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| x1 | double | Horizontal coordinate of one corner of the rectangle that encloses the arc. (X1,Y1) is one corner and (X2,Y2) is the opposing corner. |
| y1 | double | Vertical coordinate of one corner of the rectangle that encloses the arc. (X1,Y1) is one corner and (X2,Y2) is the opposing corner. |
| x2 | double | Horizontal coordinate of the opposing corner of the rectangle that encloses the arc. (X1,Y1) is one corner and (X2,Y2) is the opposing corner. |
| y2 | double | Vertical coordinate of the opposing corner of the rectangle that encloses the arc. (X1,Y1) is one corner and (X2,Y2) is the opposing corner. |
| beginAngle | int | Starting angle of the arc, in tenths of degrees. Positive angles proceed counter-clockwise and negative angles proceed clockwise, from 0 to 3,600. |
| arcAngle | int | Sweep angle of the arc, in tenths of degrees. Positive angles proceed counter-clockwise and negative angles proceed clockwise, from 0 to 3,600. |
| color | int | Specifies the color of the data to plot. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |
| fillColor | int | The fill color of the figure. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| plotHandle | int | The handle of the new plot that you can use in subsequent function calls to reference the plot. If the handle is positive, the new plot was successfully added to the graph. Negative values indicate that an error occurred. Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |
|  | Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the PlotArc function:

- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphs.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotbitmap.htm language=enus -->
## TOPIC 01213: PlotBitmap

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotbitmap.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotbitmap.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotBitmap

int PlotBitmap (int panelHandle, int controlID, double x, double y, double width, double height, char filename[]);

#### Purpose

Plots a bitmapped image from a file onto a graph control.

The origin of the image is expressed in terms of the x and y coordinates of the graph. The origin pinpoints the lower left corner of the image.

#### Supported Controls

You can use PlotBitmap with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| x | double | X-coordinate of the lower left corner of the bitmapped image. |
| y | double | Y-coordinate of the lower left corner of the bitmapped image. |
| width | double | Width, in graph units, of the area in which to fit the bitmapped image. If zero, then the width is the width of the image. If nonzero, the image stretches or shrinks to fit. When nonzero, width should be positive. If width is negative, the function interprets x as applying to the right edge instead of the left edge of the image. |
| height | double | Height, in graph units, of the area in which to fit the bitmap image. If zero, then the height is the height of the image. If nonzero, the image stretches or shrinks to fit. When nonzero, height should be positive. If height is negative, the function interprets y as applying to the top edge instead of the bottom edge of the image. |
| filename | char [] | Name of the file that contains the image. filename can be a complete pathname or a simple filename. For simple filenames that contain no directory path, the file is loaded from the directory that contains the executable. Valid image types are .tif, .pcx, .bmp, .dib, .rle, .ico, .jpg, .png, .wmf, and .emf. (Linux) Valid image types are .pcx, .jpg, and .xwd. You can pass NULL or an empty string for filename. This capability is useful when you want to define the image at a later point in your program by calling SetCtrlBitmap on the plot handle this function returns. The plot is not visible until you specify a valid image. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| plotHandle | int | The handle of the new plot that you can use in subsequent function calls to reference the plot. If the handle is positive, the new plot was successfully added to the graph. Negative values indicate that an error occurred. Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |
|  | Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\graphlegend.cws for an example of using the PlotBitmap function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotdigitallines.htm language=enus -->
## TOPIC 01214: PlotDigitalLines

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotdigitallines.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotdigitallines.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotDigitalLines

int PlotDigitalLines (int panelHandle, int controlID, void *dataArray, size_t numberOfPoints, int dataType, unsigned char numberOfLines);

#### Purpose

Plots data from a single bus to a [digital graph](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm). Use [PlotDigitalLinesMultiBus](../../cvi/uiref/cviplotdigitallinesmultibus.htm) to plot data from multiple buses.

Use PlotDigitalLines to send each data sample from each line as a separate data array value. Call [PlotPackedDigitalLines](../../cvi/uiref/cviplotpackeddigitallines.htm) to send packed data in which each data array element contains data values for multiple lines.

If you use NI-DAQmx to acquire the data you plot with PlotDigitalLines, you must call DAQmxReadDigitalLines as the read function.

#### Supported Controls

You can use PlotDigitalLines with [digital graph controls](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| dataArray | void * | Array that contains the values to plot on the digital graph. The data type must be of the type specified by dataType. If the value of a data item is non-zero, then the line is high; if the value is 0, then the line is low. The data in the array must be interleaved. To pass all the data samples for each line sequentially, call the PlotDigitalLinesMultiBus function and assign each line to its own bus. |
| numberOfPoints | size_t | The number of points to plot. This value controls the number of points to plot even if the number of elements in the dataArray is greater than the numPoints. numPoints must be greater than zero and not greater than INT_MAX. |
| dataType | int | The data type of dataArray. The data must be one of the following valid integer data types: VAL_CHAR A single byte character VAL_INTEGER A 4 byte integer VAL_SHORT_INTEGER A 2 byte integer VAL_UNSIGNED_CHAR An unsigned single byte character VAL_UNSIGNED_INTEGER An unsigned 4 byte integer VAL_UNSIGNED_SHORT_INTEGER An unsigned 2 byte integer |
| VAL_CHAR | A single byte character |  |
| VAL_INTEGER | A 4 byte integer |  |
| VAL_SHORT_INTEGER | A 2 byte integer |  |
| VAL_UNSIGNED_CHAR | An unsigned single byte character |  |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer |  |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer |  |
| numberOfLines | unsigned char | The number of lines to plot. LabWindows/CVI divides the dataArray evenly among the lines. You cannot mask out a particular line to keep LabWindows/CVI from plotting it. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Examples

Refer to the following examples that use the PlotDigitalLines function:

- userint\ClockDigitalGraph.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\plotDigLine.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotdigitallinesmultibus.htm language=enus -->
## TOPIC 01215: PlotDigitalLinesMultiBus

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotdigitallinesmultibus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotdigitallinesmultibus.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotDigitalLinesMultiBus

int PlotDigitalLinesMultiBus (int panelHandle, int controlID, void *dataArray, size_t numberOfPoints, int numberOfBuses, int dataType, int dataSequence, unsigned char numberOfPlotLinesArray[]);

#### Purpose

Plots data for multiple buses to a [digital graph](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm).

Use PlotDigitalLinesMultiBus to send in each data sample from each line as a separate value of the data array. Call [PlotPackedDigitalLinesMultiBus](../../cvi/uiref/cviplotpackeddigitallinesmultibus.htm) to send packed data in which each data array element contains data values for multiple lines within a bus.

If you use NI-DAQmx to acquire the data you plot with PlotDigitalLinesMultiBus, you must call DAQmxReadDigitalLines as the read function. You also must [group the lines](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm#daqmxmultbuseschanconfig) from each bus into a channel to ensure that PlotDigitalLinesMultiBus can plot the data correctly.

#### Supported Controls

You can use PlotDigitalLinesMultiBus with [digital graph controls](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| dataArray | void * | Array that contains the values to plot on the digital graph. The data type must be of the type specified by dataType. If the value of a data item is non-zero, then the line is high; if the value is 0, then the line is low. You can group the data into multiple buses, as specified in numBuses. If you plot data for more than one bus, all of the buses must have the same number of samples. Otherwise, the displayed data will be incorrect. |
| numberOfPoints | size_t | The number of points to plot. This value controls the number of points to plot even if the number of elements in dataArray is greater than the numPoints. numPoints must be greater than zero and not greater than INT_MAX. |
| numberOfBuses | int | The number of data buses to plot. If you specify more than one bus in numBuses, all of the buses must contain the same number of lines. However, some of the lines can be invalid. You must pad the data in dataArray to ensure the buses have the same total number of lines, even if you want to plot only some of the lines for a particular bus. Use the numPlotLinesArray parameter to specify which lines to plot for each bus. |
| dataType | int | The data type of dataArray. The data must be one of the following valid integer data types: VAL_CHAR A single byte character VAL_INTEGER A 4 byte integer VAL_SHORT_INTEGER A 2 byte integer VAL_UNSIGNED_CHAR An unsigned single byte character VAL_UNSIGNED_INTEGER An unsigned 4 byte integer VAL_UNSIGNED_SHORT_INTEGER An unsigned 2 byte integer |
| VAL_CHAR | A single byte character |  |
| VAL_INTEGER | A 4 byte integer |  |
| VAL_SHORT_INTEGER | A 2 byte integer |  |
| VAL_UNSIGNED_CHAR | An unsigned single byte character |  |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer |  |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer |  |
| dataSequence | int | Determines the order in which LabWindows/CVI plots the dataArray values. If numBuses is 1, LabWindows/CVI ignores this value. The data within an individual bus is always interleaved. VAL_INTERLEAVED—LabWindows/CVI plots the data values for the first sample of the first bus, then the data values for the first sample of the second bus, and so on. VAL_NON_INTERLEAVED—LabWindows/CVI plots all of the data values for the first bus, then all of the data values for the second bus, and so on. If you use NI-DAQmx to acquire the data array, you must use the appropriate dataSequence. Example Code You can use the following code to plot two buses on a digital graph: short int data[20] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; unsigned char lines[2] = {2,2}; PlotDigitalLinesMultiBus (panelHandle, PANEL_DGRAPH, data, 20, 2, VAL_SHORT_INTEGER, VAL_NON_INTERLEAVED, lines); In this example, LabWindows/CVI plots two buses, each of which has two lines. Because the data is not interleaved, LabWindows/CVI plots the first 10 values as the data values for Bus 0 and the last 10 values as the data values for Bus 1. Given the data values, Bus 0 would contain all high values, and Bus 1 would contain all low values. If you pass the following code instead: short int data[20] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; unsigned char lines[2] = {2,2}; PlotDigitalLinesMultiBus (panelHandle, PANEL_DGRAPH, data, 20, 2, VAL_SHORT_INTEGER, VAL_INTERLEAVED, lines); LabWindows/CVI plots the first two values in Bus 0, the next two values in Bus 1, the next two values in Bus 0, and so on. Given the data values, Bus 0 and Bus 1 would both contain high and low values. |
| numberOfPlotLinesArray | unsigned char [] | Array that contains the number of lines to plot per bus. Because each bus must have the same total number of lines, you can use numPlotLinesArray to specify how many lines are valid. Example Code You can use the following code to plot two buses on a digital graph: short int data[20] = {1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0}; unsigned char lines[2] = {2,1}; PlotDigitalLinesMultiBus (panelHandle, PANEL_DGRAPH, data, 20, 2, VAL_SHORT_INTEGER, VAL_NON_INTERLEAVED, lines); LabWindows/CVI separates the data into four lines, with two lines in each bus. However, LabWindows/CVI plots data for only three of the lines because only three of the lines are valid. As specified by the value of {2, 1} for numPlotLinesArray, Bus 0 contains two valid lines, and Bus 1 contains one valid line. The second line in Bus 1 is a padding line, which ensures the buses have the same total number of lines. The padding line is not plotted. LabWindows/CVI divides the 20 data elements between the four total lines, plotting five data samples for each of the valid lines in Bus 0, plotting five data samples for the valid line in Bus 1, and ignoring the remaining five data samples as padding data. Only 15 of the 20 data elements are actually plotted on the digital graph. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotline.htm language=enus -->
## TOPIC 01216: PlotLine

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotline.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotline.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotLine

int PlotLine (int panelHandle, int controlID, double x1, double y1, double x2, double y2, int color);

#### Purpose

Plots a line onto a graph control.

Specify the starting and ending points of the line in terms of x- and
y-coordinates of the graph.

#### Supported Controls

You can use PlotLine with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| x1 | double | Horizontal coordinate of the starting point of the line. |
| y1 | double | Vertical coordinate of the starting point of the line. |
| x2 | double | Horizontal coordinate of the ending point of the line. |
| y2 | double | Vertical coordinate of the ending point of the line. |
| color | int | Specifies the color of the data to plot. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| plotHandle | int | The handle of the new plot that you can use in subsequent function calls to reference the plot. If the handle is positive, the new plot was successfully added to the graph. Negative values indicate that an error occurred. Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |
|  | Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the PlotLine function:

- userint\canvsbmk.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotoval.htm language=enus -->
## TOPIC 01217: PlotOval

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotoval.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotoval.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotOval

int PlotOval (int panelHandle, int controlID, double x1, double y1, double x2, double y2, int color, int fillColor);

#### Purpose

Plots an oval onto a graph control.

Define the oval in terms of a rectangle that encloses it. You can define the rectangle by specifying two opposing corners, which you express in terms of x- and y-coordinates of the graph.

#### Supported Controls

You can use PlotOval with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| x1 | double | Horizontal coordinate of one corner of the rectangle that encloses the oval. (X1,Y1) is one corner and (X2,Y2) is the opposing corner. |
| y1 | double | Vertical coordinate of one corner of the rectangle that encloses the oval. (X1,Y1) is one corner and (X2,Y2) is the opposing corner. |
| x2 | double | Horizontal coordinate of the opposing corner of the rectangle that encloses the oval. (X1,Y1) is one corner and (X2,Y2) is the opposing corner. |
| y2 | double | Vertical coordinate of the opposing corner of the rectangle that encloses the oval. (X1,Y1) is one corner and (X2,Y2) is the opposing corner. |
| color | int | Specifies the color of the data to plot. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |
| fillColor | int | The fill color of the figure. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| plotHandle | int | The handle of the new plot that you can use in subsequent function calls to reference the plot. If the handle is positive, the new plot was successfully added to the graph. Negative values indicate that an error occurred. Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |
|  | Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the PlotOval function:

- analysis\stabilty.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphs.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotpackeddigitallines.htm language=enus -->
## TOPIC 01218: PlotPackedDigitalLines

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotpackeddigitallines.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotpackeddigitallines.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotPackedDigitalLines

int PlotPackedDigitalLines (int panelHandle, int controlID, void *dataArray, size_t numberOfElements, int dataType, void *mask);

#### Purpose

Plots packed data from a single bus to a [digital graph](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm). To plot packed data from multiple buses, call [PlotPackedDigitalLinesMultiBus](../../cvi/uiref/cviplotpackeddigitallinesmultibus.htm).

The data you send to PlotPackedDigitalLines is packed, which means you can send data samples for more than one digital line per **dataArray** element. Each **dataArray** element corresponds to one data sample. The individual bits in each **dataArray** element correspond to data samples for individual lines. Use the **mask** parameter to specify which bits in the **dataArray** element refer to valid lines.

If you use NI-DAQmx to acquire the data you plot with PlotPackedDigitalLines, you must call DAQmxReadDigU8 as the read function.

#### Supported Controls

You can use PlotPackedDigitalLines with [digital graph controls](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| dataArray | void * | Array that contains the values to plot on the digital graph. The data type must be of the type specified by dataType. Each element in the dataArray corresponds to one sample. Each bit within the dataArray element corresponds to a data value for a line within the bus. Use the mask parameter to specify which lines to plot on the digital graph. |
| numberOfElements | size_t | Number of dataArray elements to plot. This value controls the number of elements to plot even if the total number of elements in dataArray is greater than numElements. numElements must be greater than zero and not greater than INT_MAX. |
| dataType | int | The data type of dataArray. The data must be one of the following valid integer data types: VAL_CHAR A single byte character VAL_INTEGER A 4 byte integer VAL_SHORT_INTEGER A 2 byte integer VAL_UNSIGNED_CHAR An unsigned single byte character VAL_UNSIGNED_INTEGER An unsigned 4 byte integer VAL_UNSIGNED_SHORT_INTEGER An unsigned 2 byte integer |
| VAL_CHAR | A single byte character |  |
| VAL_INTEGER | A 4 byte integer |  |
| VAL_SHORT_INTEGER | A 2 byte integer |  |
| VAL_UNSIGNED_CHAR | An unsigned single byte character |  |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer |  |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer |  |
| mask | void * | Pass a pointer to the mask. The mask itself must be of the type specified in dataType. The mask specifies which bits in each data element are valid lines. The digital graph displays the result of a bitwise AND on mask and dataArray. For example, the dataArray you pass in to PlotPackedDigitalLines is of type VAL_SHORT_INTEGER. A mask referencing a value of 0x00F8 specifies that only lines three through seven are valid for the bus. If you pass in VAL_SINGLE_LINE for the mask, then PlotPackedDigitalLines plots only one line. LabWindows/CVI plots the data in the least significant bit of the dataArray element. This is equivalent to passing in a pointer to a value of 0x0001 for the mask. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to userint\DigGraphDAQmx.cws for an example of using the PlotPackedDigitalLines function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotpackeddigitallinesmultibus.htm language=enus -->
## TOPIC 01219: PlotPackedDigitalLinesMultiBus

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotpackeddigitallinesmultibus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotpackeddigitallinesmultibus.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotPackedDigitalLinesMultiBus

int PlotPackedDigitalLinesMultiBus (int panelHandle, int controlID, void *dataArray, size_t numberOfElements, int numberOfBuses, int dataType, int dataSequence, void *maskArray);

#### Purpose

Plots packed data from multiple buses to a [digital graph](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm).

The data you send to PlotPackedDigitalLinesMultiBus is packed, which means you can send data samples for more than one digital line per **dataArray** element. Each **dataArray** element corresponds to one data sample for a bus. The individual bits in each **dataArray** element correspond to individual lines within the bus. Use the **maskArray** parameter to specify which bits in the **dataArray** refer to valid lines.

If you use NI-DAQmx to acquire the data you plot with PlotPackedDigitalLinesMultiBus, you must call DAQmxReadDigU8 as the read function. You also must [group the lines](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm#daqmxmultbuseschanconfig) from each bus into a channel to ensure that PlotPackedDigitalLinesMultiBus can plot the data correctly.

#### Supported Controls

You can use PlotPackedDigitalLinesMultiBus with [digital graph controls](../../cvi/uiref/cviprogramming_with_digital_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| dataArray | void * | Array that contains the values to plot on the digital graph. The data type must be of the type specified by dataType. Each element in the dataArray corresponds to one sample for a bus. Each bit within the dataArray element corresponds to a data value for a line within the bus. Use maskArray to specify which lines to plot on the digital graph. You can group the data into multiple buses, as specified in numBuses. If you plot data for more than one bus, all of the buses must have the same number of samples. Otherwise, the displayed data will be incorrect. |
| numberOfElements | size_t | Number of dataArray elements to plot. This value controls the number of elements to plot even if the total number of elements in dataArray is greater than numElements. numElements must be greater than zero and not greater than INT_MAX. |
| numberOfBuses | int | The number of data buses to plot. maskArray specifies the valid lines in each bus to plot. |
| dataType | int | The data type of dataArray. The data must be one of the following valid integer data types: VAL_CHAR A single byte character VAL_INTEGER A 4 byte integer VAL_SHORT_INTEGER A 2 byte integer VAL_UNSIGNED_CHAR An unsigned single byte character VAL_UNSIGNED_INTEGER An unsigned 4 byte integer VAL_UNSIGNED_SHORT_INTEGER An unsigned 2 byte integer |
| VAL_CHAR | A single byte character |  |
| VAL_INTEGER | A 4 byte integer |  |
| VAL_SHORT_INTEGER | A 2 byte integer |  |
| VAL_UNSIGNED_CHAR | An unsigned single byte character |  |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer |  |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer |  |
| dataSequence | int | Determines the order in which LabWindows/CVI plots the dataArray values. VAL_INTERLEAVED—LabWindows/CVI plots the data values for the first data sample of the first bus, then the data values for the first data sample of the second bus, and so on. VAL_NON_INTERLEAVED—LabWindows/CVI plots all of the data values for the first bus, then all of the data values for the second bus, and so on. If you use NI-DAQmx to acquire the data array, you must use the appropriate dataSequence. |
| maskArray | void * | Array that specifies which bits in each data element correspond to valid lines. The digital graph displays the result of a bitwise AND on maskArray and dataArray. For example, the dataArray you pass to PlotPackedDigitalLinesMultiBus has three buses of type VAL_SHORT_INTEGER. A maskArray that contains the values {0x00FF, 0x0001, 0x0001} indicates that the first bus has eight valid lines, and the second and third buses have one valid line each. If you pass in VAL_SINGLE_LINE for the maskArray, then PlotPackedDigitalLinesMultiBus plots only one line per bus. LabWindows/CVI plots the data in the least significant bit of each element. If there are multiple buses, VAL_SINGLE_LINE applies to all of them. The data type of maskArray must be the type specified in dataType. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.1 and later

#### Example

Refer to userint\TreeBusDigitalGraph.cws for an example of using the PlotPackedDigitalLinesMultiBus function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotpoint.htm language=enus -->
## TOPIC 01220: PlotPoint

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotpoint.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotpoint.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotPoint

int PlotPoint (int panelHandle, int controlID, double xCoordinate, double yCoordinate, int pointStyle, int color);

#### Purpose

Plots a point onto a graph control.

Specify the position of the point in terms of x- and y-coordinates of the
graph.

#### Supported Controls

You can use PlotPoint with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| xCoordinate | double | Horizontal position at which to plot the point. |
| yCoordinate | double | Vertical coordinate at which to plot the point. |
| pointStyle | int | Point style to use when plotting the array. The point style determines the type of marker to draw when the plot style is VAL_CONNECTED_POINTS or VAL_SCATTER. The default value is VAL_EMPTY_SQUARE. VAL_EMPTY_SQUARE An empty square. VAL_SOLID_SQUARE A solid square. VAL_ASTERISK An asterisk type character. VAL_DOTTED_EMPTY_SQUARE An empty square with a dot in its center. VAL_DOTTED_SOLID_SQUARE A solid square with a dot in its center. VAL_SOLID_DIAMOND A diamond shape (similar to a cross). VAL_EMPTY_SQUARE_WITH_X An empty square with an X-like shape in its center. VAL_EMPTY_SQUARE_WITH_CROSS An empty square with a cross in its center. VAL_BOLD_X A bold X-like shape. VAL_SMALL_SOLID_SQUARE A small solid square. VAL_SIMPLE_DOT A small dot. VAL_EMPTY_CIRCLE An empty circle. VAL_SOLID_CIRCLE A solid circle. VAL_DOTTED_SOLID_CIRCLE A circle with a dot in its center. VAL_DOTTED_EMPTY_CIRCLE A solid circle with a a dot in its center. VAL_BOLD_CROSS A bold cross of equal height and width. VAL_CROSS A cross of equal height and width. VAL_SMALL_CROSS A small cross of equal height and width. VAL_X An X-like shape. VAL_SMALL_X A small X-like shape. VAL_DOTTED_SOLID_DIAMOND A solid diamond shape with a dot in its center. VAL_EMPTY_DIAMOND An empty diamond shape. VAL_DOTTED_EMPTY_DIAMOND An empty solid diamond shape with a dot in its center. VAL_SMALL_EMPTY_SQUARE A small empty square. VAL_NO_POINT No cursor point. |
| VAL_EMPTY_SQUARE | An empty square. |  |
| VAL_SOLID_SQUARE | A solid square. |  |
| VAL_ASTERISK | An asterisk type character. |  |
| VAL_DOTTED_EMPTY_SQUARE | An empty square with a dot in its center. |  |
| VAL_DOTTED_SOLID_SQUARE | A solid square with a dot in its center. |  |
| VAL_SOLID_DIAMOND | A diamond shape (similar to a cross). |  |
| VAL_EMPTY_SQUARE_WITH_X | An empty square with an X-like shape in its center. |  |
| VAL_EMPTY_SQUARE_WITH_CROSS | An empty square with a cross in its center. |  |
| VAL_BOLD_X | A bold X-like shape. |  |
| VAL_SMALL_SOLID_SQUARE | A small solid square. |  |
| VAL_SIMPLE_DOT | A small dot. |  |
| VAL_EMPTY_CIRCLE | An empty circle. |  |
| VAL_SOLID_CIRCLE | A solid circle. |  |
| VAL_DOTTED_SOLID_CIRCLE | A circle with a dot in its center. |  |
| VAL_DOTTED_EMPTY_CIRCLE | A solid circle with a a dot in its center. |  |
| VAL_BOLD_CROSS | A bold cross of equal height and width. |  |
| VAL_CROSS | A cross of equal height and width. |  |
| VAL_SMALL_CROSS | A small cross of equal height and width. |  |
| VAL_X | An X-like shape. |  |
| VAL_SMALL_X | A small X-like shape. |  |
| VAL_DOTTED_SOLID_DIAMOND | A solid diamond shape with a dot in its center. |  |
| VAL_EMPTY_DIAMOND | An empty diamond shape. |  |
| VAL_DOTTED_EMPTY_DIAMOND | An empty solid diamond shape with a dot in its center. |  |
| VAL_SMALL_EMPTY_SQUARE | A small empty square. |  |
| VAL_NO_POINT | No cursor point. |  |
| color | int | Specifies the color of the data to plot. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| plotHandle | int | The handle of the new plot that you can use in subsequent function calls to reference the plot. If the handle is positive, the new plot was successfully added to the graph. Negative values indicate that an error occurred. Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |
|  | Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the PlotPoint function:

- apps\freqresp\freqresp.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphs.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplotpolygon.htm language=enus -->
## TOPIC 01221: PlotPolygon

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplotpolygon.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplotpolygon.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotPolygon

int PlotPolygon (int panelHandle, int controlID, void *xArray, void *yArray, size_t pointsInPolygon, int xDataType, int yDataType, int color, int fillColor);

#### Purpose

Plots a polygon onto a graph control.

Define the polygon by a set of connected x-y points. The last point is automatically connected to the first point to close the polygon.

#### Supported Controls

You can use PlotPolygon with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| xArray | void * | Array that contains the values to plot along the x-axis. The data type must be of the type you specify in xDataType. |
| yArray | void * | Array that contains the values to plot along the y-axis. The data type must be of the type specified by yDataType. |
| pointsInPolygon | size_t | Number of connected points, or corners, in the polygon. At least three corners must exist. pointsInPolygon controls the number of corners plotted, even if the number of elements in the x and y arrays is greater than the value of pointsInPolygon. |
| xDataType | int | The data type of the x array. The following table lists the valid data types. VAL_CHAR A single byte character. VAL_SHORT_INTEGER A 2 byte integer. VAL_INTEGER A 4 byte integer. VAL_FLOAT A 4 byte floating point value. VAL_DOUBLE An 8 byte floating point value. VAL_64BIT_INTEGER An 8 byte integer. VAL_UNSIGNED_SHORT_INTEGER An unsigned 2 byte integer. VAL_UNSIGNED_INTEGER An unsigned 4 byte integer. VAL_UNSIGNED_CHAR An unsigned single byte character. VAL_UNSIGNED_64BIT_INTEGER An unsigned 8 byte integer. VAL_SIZE_T An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). VAL_SSIZE_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). VAL_PTRDIFF_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). VAL_UINTPTR_T An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). VAL_INTPTR_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |
| VAL_CHAR | A single byte character. |  |
| VAL_SHORT_INTEGER | A 2 byte integer. |  |
| VAL_INTEGER | A 4 byte integer. |  |
| VAL_FLOAT | A 4 byte floating point value. |  |
| VAL_DOUBLE | An 8 byte floating point value. |  |
| VAL_64BIT_INTEGER | An 8 byte integer. |  |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer. |  |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer. |  |
| VAL_UNSIGNED_CHAR | An unsigned single byte character. |  |
| VAL_UNSIGNED_64BIT_INTEGER | An unsigned 8 byte integer. |  |
| VAL_SIZE_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |  |
| VAL_SSIZE_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| VAL_PTRDIFF_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| VAL_UINTPTR_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |  |
| VAL_INTPTR_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| yDataType | int | The data type of the y array. The following table lists the valid data types. VAL_CHAR A single byte character. VAL_SHORT_INTEGER A 2 byte integer. VAL_INTEGER A 4 byte integer. VAL_FLOAT A 4 byte floating point value. VAL_DOUBLE An 8 byte floating point value. VAL_64BIT_INTEGER An 8 byte integer. VAL_UNSIGNED_SHORT_INTEGER An unsigned 2 byte integer. VAL_UNSIGNED_INTEGER An unsigned 4 byte integer. VAL_UNSIGNED_CHAR An unsigned single byte character. VAL_UNSIGNED_64BIT_INTEGER An unsigned 8 byte integer. VAL_SIZE_T An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). VAL_SSIZE_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). VAL_PTRDIFF_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). VAL_UINTPTR_T An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). VAL_INTPTR_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |
| VAL_CHAR | A single byte character. |  |
| VAL_SHORT_INTEGER | A 2 byte integer. |  |
| VAL_INTEGER | A 4 byte integer. |  |
| VAL_FLOAT | A 4 byte floating point value. |  |
| VAL_DOUBLE | An 8 byte floating point value. |  |
| VAL_64BIT_INTEGER | An 8 byte integer. |  |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer. |  |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer. |  |
| VAL_UNSIGNED_CHAR | An unsigned single byte character. |  |
| VAL_UNSIGNED_64BIT_INTEGER | An unsigned 8 byte integer. |  |
| VAL_SIZE_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |  |
| VAL_SSIZE_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| VAL_PTRDIFF_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| VAL_UINTPTR_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |  |
| VAL_INTPTR_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| color | int | Specifies the color of the data to plot. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |
| fillColor | int | The fill color of the figure. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| plotHandle | int | The handle of the new plot that you can use in subsequent function calls to reference the plot. If the handle is positive, the new plot was successfully added to the graph. Negative values indicate that an error occurred. Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |
|  | Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the PlotPolygon function:

- userint\clipbord.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviplottext.htm language=enus -->
## TOPIC 01222: PlotText

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviplottext.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviplottext.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotText

int PlotText (int panelHandle, int controlID, double xCoordinate, double yCoordinate, char text[], char metaFont[], int textColor, int backgroundColor);

#### Purpose

Plots a text string onto a graph control.

The origin of the text is the lower left corner of the string. You specify the origin of the text in terms of the x- and y-coordinates of the graph.

If the ATTR_SHIFT_TEXT_PLOTS graph attribute is non-zero, the text origin is within the graph area, and the text does not entirely fit within the graph, the text shifts to the left and/or down until it is completely visible. If ATTR_SHIFT_TEXT_PLOTS is zero, the text does not shift.

#### Supported Controls

You can use PlotText with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| xCoordinate | double | Horizontal position at which to place the left edge of the text within the graph. The default value is 0.0. Normally, the xCoordinate corresponds to the left edge of the text. However, if the text origin is within the graph area and the complete text cannot fit within the plot area, the text shifts to the left until it is completely visible. |
| yCoordinate | double | Vertical position at which to place the bottom edge of the text within the graph. The default value is 0.0. Normally, the yCoordinate corresponds to the bottom edge of the text. However, if the text origin is within the graph area and the complete text cannot fit within the plot area, the text shifts down until it is completely visible. |
| text | char [] | String to plot. |
| metaFont | char [] | The font to use for the text string. metaFont can be a predefined NI metafont or a user-defined metafont saved by a previous call to functions such as CreateMetaFont and CreateMetaFontEx. The following are NI metafonts: Predefined metafonts—Contain typeface information, point size, and text styles such as bold, underline, italic, and strikeout. These metafonts are used in the LabWindows/CVI environment. The predefined metafonts are VAL_MENU_META_FONT, VAL_DIALOG_META_FONT, VAL_EDITOR_META_FONT, VAL_APP_META_FONT, and VAL_MESSAGE_BOX_META_FONT. LabWindows/CVI-supplied metafonts—Use typefaces that are not native to the operating system. These metafonts are installed while LabWindows/CVI is running. The LabWindows/CVI-supplied metafonts are VAL_7SEG_META_FONT and VAL_SYSTEM_META_FONT. |
| textColor | int | The color of the plotted text. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| backgroundColor | int | The background color of the plotted text. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| plotHandle | int | The handle of the new plot that you can use in subsequent function calls to reference the plot. If the handle is positive, the new plot was successfully added to the graph. Negative values indicate that an error occurred. Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |
|  | Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the PlotText function:

- userint\events.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphs.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\RotatedText.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviploty.htm language=enus -->
## TOPIC 01223: PlotY

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviploty.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviploty.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PlotY

int PlotY (int panelHandle, int controlID, void *yArray, size_t numberOfPoints, int yDataType, int plotStyle, int pointStyle, int lineStyle, int pointFrequency, int color);

#### Purpose

Plots an array of y values against its indices along the x-axis on a graph control.

This function displays the plot in a graph control on the specified panel.

#### Supported Controls

You can use PlotY with [graph controls](../../cvi/uiref/cviprogramming_with_graph_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| yArray | void * | Array that contains the values to plot along the y-axis. The data type must be of the type specified by yDataType. |
| numberOfPoints | size_t | Number of points to plot. This value controls the number of points to plot even if the number of elements in xArray is greater than the numberOfPoints. numberOfPoints must be greater than zero and not greater than INT_MAX. |
| yDataType | int | The data type of the y array. The following table lists the valid data types. VAL_CHAR A single byte character. VAL_SHORT_INTEGER A 2 byte integer. VAL_INTEGER A 4 byte integer. VAL_FLOAT A 4 byte floating point value. VAL_DOUBLE An 8 byte floating point value. VAL_64BIT_INTEGER An 8 byte integer. VAL_UNSIGNED_SHORT_INTEGER An unsigned 2 byte integer. VAL_UNSIGNED_INTEGER An unsigned 4 byte integer. VAL_UNSIGNED_CHAR An unsigned single byte character. VAL_UNSIGNED_64BIT_INTEGER An unsigned 8 byte integer. VAL_SIZE_T An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). VAL_SSIZE_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). VAL_PTRDIFF_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). VAL_UINTPTR_T An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). VAL_INTPTR_T A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |
| VAL_CHAR | A single byte character. |  |
| VAL_SHORT_INTEGER | A 2 byte integer. |  |
| VAL_INTEGER | A 4 byte integer. |  |
| VAL_FLOAT | A 4 byte floating point value. |  |
| VAL_DOUBLE | An 8 byte floating point value. |  |
| VAL_64BIT_INTEGER | An 8 byte integer. |  |
| VAL_UNSIGNED_SHORT_INTEGER | An unsigned 2 byte integer. |  |
| VAL_UNSIGNED_INTEGER | An unsigned 4 byte integer. |  |
| VAL_UNSIGNED_CHAR | An unsigned single byte character. |  |
| VAL_UNSIGNED_64BIT_INTEGER | An unsigned 8 byte integer. |  |
| VAL_SIZE_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |  |
| VAL_SSIZE_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| VAL_PTRDIFF_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| VAL_UINTPTR_T | An unsigned 4 byte integer (32-bit applications). An unsigned 8 byte integer (64-bit applications). |  |
| VAL_INTPTR_T | A 4 byte integer (32-bit applications). An 8 byte integer (64-bit applications). |  |
| plotStyle | int | Curve style to use when plotting the data points. The default value is VAL_THIN_LINE. The following table lists valid styles. VAL_THIN_LINE A single thin line. The data points are plotted as a sequence of connected line segments, drawn from point to point. The line segments are 1 pixel wide. No marker symbols are drawn at any of the data points. VAL_FAT_LINE A fat line. The data points are plotted as a sequence of connected line segments, drawn from point to point. The line segments are 3 pixels wide. No marker symbols are drawn at any of the data points. VAL_FAT_LINE forces lineStyle to solid. VAL_CONNECTED_POINTS A single thin line with asterisk characters at each plotted point. Similar to VAL_THIN_LINE except that marker symbols are drawn at some or all of the data points, depending on the selected point frequency. VAL_SCATTER Asterisk characters at each plotted point with no lines connecting each point. VAL_THIN_STEP A thin line stepping from one point to the next. The data points are connected by two 1-pixel wide lines at right angles to each other, the vertical drawn first, then the horizontal. VAL_FAT_STEP A fat line stepping from one point to the next. The data points are connected by two 3-pixel wide lines at right angles to each other, the vertical drawn first, then the horizontal. VAL_VERTICAL_BAR Vertical bars are plotted for each plotted point. The bars extend upward from the minimum value, where the height of the bar represents the magnitude of the data point. VAL_HORIZONTAL_BAR Horizontal bars are plotted for each plotted point. The bars extend to the right from the minimum value, where the length of the bar represents the magnitude of the data point. VAL_BASE_ZERO_VERTICAL_BAR Vertical bars are plotted for each plotted point. The bars extend upward and downward from zero, depending on whether the data value is positive or negative. VAL_BASE_ZERO_HORIZONTAL_BAR Horizontal bars are plotted for each plotted point. The bars extend to the left and right from zero, depending on whether the data value is positive or negative. |
| VAL_THIN_LINE | A single thin line. The data points are plotted as a sequence of connected line segments, drawn from point to point. The line segments are 1 pixel wide. No marker symbols are drawn at any of the data points. |  |
| VAL_FAT_LINE | A fat line. The data points are plotted as a sequence of connected line segments, drawn from point to point. The line segments are 3 pixels wide. No marker symbols are drawn at any of the data points. VAL_FAT_LINE forces lineStyle to solid. |  |
| VAL_CONNECTED_POINTS | A single thin line with asterisk characters at each plotted point. Similar to VAL_THIN_LINE except that marker symbols are drawn at some or all of the data points, depending on the selected point frequency. |  |
| VAL_SCATTER | Asterisk characters at each plotted point with no lines connecting each point. |  |
| VAL_THIN_STEP | A thin line stepping from one point to the next. The data points are connected by two 1-pixel wide lines at right angles to each other, the vertical drawn first, then the horizontal. |  |
| VAL_FAT_STEP | A fat line stepping from one point to the next. The data points are connected by two 3-pixel wide lines at right angles to each other, the vertical drawn first, then the horizontal. |  |
| VAL_VERTICAL_BAR | Vertical bars are plotted for each plotted point. The bars extend upward from the minimum value, where the height of the bar represents the magnitude of the data point. |  |
| VAL_HORIZONTAL_BAR | Horizontal bars are plotted for each plotted point. The bars extend to the right from the minimum value, where the length of the bar represents the magnitude of the data point. |  |
| VAL_BASE_ZERO_VERTICAL_BAR | Vertical bars are plotted for each plotted point. The bars extend upward and downward from zero, depending on whether the data value is positive or negative. |  |
| VAL_BASE_ZERO_HORIZONTAL_BAR | Horizontal bars are plotted for each plotted point. The bars extend to the left and right from zero, depending on whether the data value is positive or negative. |  |
| pointStyle | int | Point style to use when plotting the array. The point style determines the type of marker to draw when the plot style is VAL_CONNECTED_POINTS or VAL_SCATTER. The default value is VAL_EMPTY_SQUARE. VAL_EMPTY_SQUARE An empty square. VAL_SOLID_SQUARE A solid square. VAL_ASTERISK An asterisk type character. VAL_DOTTED_EMPTY_SQUARE An empty square with a dot in its center. VAL_DOTTED_SOLID_SQUARE A solid square with a dot in its center. VAL_SOLID_DIAMOND A diamond shape (similar to a cross). VAL_EMPTY_SQUARE_WITH_X An empty square with an X-like shape in its center. VAL_EMPTY_SQUARE_WITH_CROSS An empty square with a cross in its center. VAL_BOLD_X A bold X-like shape. VAL_SMALL_SOLID_SQUARE A small solid square. VAL_SIMPLE_DOT A small dot. VAL_EMPTY_CIRCLE An empty circle. VAL_SOLID_CIRCLE A solid circle. VAL_DOTTED_SOLID_CIRCLE A circle with a dot in its center. VAL_DOTTED_EMPTY_CIRCLE A solid circle with a a dot in its center. VAL_BOLD_CROSS A bold cross of equal height and width. VAL_CROSS A cross of equal height and width. VAL_SMALL_CROSS A small cross of equal height and width. VAL_X An X-like shape. VAL_SMALL_X A small X-like shape. VAL_DOTTED_SOLID_DIAMOND A solid diamond shape with a dot in its center. VAL_EMPTY_DIAMOND An empty diamond shape. VAL_DOTTED_EMPTY_DIAMOND An empty solid diamond shape with a dot in its center. VAL_SMALL_EMPTY_SQUARE A small empty square. VAL_NO_POINT No cursor point. |
| VAL_EMPTY_SQUARE | An empty square. |  |
| VAL_SOLID_SQUARE | A solid square. |  |
| VAL_ASTERISK | An asterisk type character. |  |
| VAL_DOTTED_EMPTY_SQUARE | An empty square with a dot in its center. |  |
| VAL_DOTTED_SOLID_SQUARE | A solid square with a dot in its center. |  |
| VAL_SOLID_DIAMOND | A diamond shape (similar to a cross). |  |
| VAL_EMPTY_SQUARE_WITH_X | An empty square with an X-like shape in its center. |  |
| VAL_EMPTY_SQUARE_WITH_CROSS | An empty square with a cross in its center. |  |
| VAL_BOLD_X | A bold X-like shape. |  |
| VAL_SMALL_SOLID_SQUARE | A small solid square. |  |
| VAL_SIMPLE_DOT | A small dot. |  |
| VAL_EMPTY_CIRCLE | An empty circle. |  |
| VAL_SOLID_CIRCLE | A solid circle. |  |
| VAL_DOTTED_SOLID_CIRCLE | A circle with a dot in its center. |  |
| VAL_DOTTED_EMPTY_CIRCLE | A solid circle with a a dot in its center. |  |
| VAL_BOLD_CROSS | A bold cross of equal height and width. |  |
| VAL_CROSS | A cross of equal height and width. |  |
| VAL_SMALL_CROSS | A small cross of equal height and width. |  |
| VAL_X | An X-like shape. |  |
| VAL_SMALL_X | A small X-like shape. |  |
| VAL_DOTTED_SOLID_DIAMOND | A solid diamond shape with a dot in its center. |  |
| VAL_EMPTY_DIAMOND | An empty diamond shape. |  |
| VAL_DOTTED_EMPTY_DIAMOND | An empty solid diamond shape with a dot in its center. |  |
| VAL_SMALL_EMPTY_SQUARE | A small empty square. |  |
| VAL_NO_POINT | No cursor point. |  |
| lineStyle | int | The line style. VAL_SOLID A solid line. VAL_DASH A dashed line. VAL_DOT A dotted line. VAL_DASH_DOT_DOT A line alternating between one dash and two dots. VAL_DASH_DOT A line with alternating dashes and dots. |
| VAL_SOLID | A solid line. |  |
| VAL_DASH | A dashed line. |  |
| VAL_DOT | A dotted line. |  |
| VAL_DASH_DOT_DOT | A line alternating between one dash and two dots. |  |
| VAL_DASH_DOT | A line with alternating dashes and dots. |  |
| pointFrequency | int | The point interval at which to draw marker symbols when the curve style is VAL_CONNECTED_POINTS or VAL_SCATTER. The default value is 1 and can be as large as the number of points in the plot. |
| color | int | Specifies the color of the data to plot. An RGB value is a 4-byte integer with the hexadecimal format 0x00RRGGBB. RR, GG, and BB are the respective red, green, and blue components of the color value. The first sixteen colors in the table are the sixteen standard colors. Value Code VAL_RED 0xFF0000L VAL_GREEN 0x00FF00L VAL_BLUE 0x0000FFL VAL_CYAN 0x00FFFFL VAL_MAGENTA 0xFF00FFL VAL_YELLOW 0xFFFF00L VAL_DK_RED 0x800000L VAL_DK_BLUE 0x000080L VAL_DK_GREEN 0x008000L VAL_DK_CYAN 0x008080L VAL_DK_MAGENTA 0x800080L VAL_DK_YELLOW 0x808000L VAL_LT_GRAY 0xC0C0C0L VAL_DK_GRAY 0x808080L VAL_BLACK 0x000000L VAL_WHITE 0xFFFFFFL VAL_PANEL_GRAY 0xC0C0C0L VAL_GRAY 0xA0A0A0L VAL_OFFWHITE 0xE0E0E0L VAL_TRANSPARENT 0x1000000L You also can use the User Interface Library function, MakeColor, to create an RGB value from red, green, and blue color components. To enter user-defined color values, select Options»Toggle Control Style in the function panel and manually enter the color value. |
| Value | Code |  |
| VAL_RED | 0xFF0000L |  |
| VAL_GREEN | 0x00FF00L |  |
| VAL_BLUE | 0x0000FFL |  |
| VAL_CYAN | 0x00FFFFL |  |
| VAL_MAGENTA | 0xFF00FFL |  |
| VAL_YELLOW | 0xFFFF00L |  |
| VAL_DK_RED | 0x800000L |  |
| VAL_DK_BLUE | 0x000080L |  |
| VAL_DK_GREEN | 0x008000L |  |
| VAL_DK_CYAN | 0x008080L |  |
| VAL_DK_MAGENTA | 0x800080L |  |
| VAL_DK_YELLOW | 0x808000L |  |
| VAL_LT_GRAY | 0xC0C0C0L |  |
| VAL_DK_GRAY | 0x808080L |  |
| VAL_BLACK | 0x000000L |  |
| VAL_WHITE | 0xFFFFFFL |  |
| VAL_PANEL_GRAY | 0xC0C0C0L |  |
| VAL_GRAY | 0xA0A0A0L |  |
| VAL_OFFWHITE | 0xE0E0E0L |  |
| VAL_TRANSPARENT | 0x1000000L |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| plotHandle | int | The handle of the new plot that you can use in subsequent function calls to reference the plot. If the handle is positive, the new plot was successfully added to the graph. Negative values indicate that an error occurred. Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |
|  | Note If ATTR_DATA_MODE is set to VAL_DISCARD, the function returns 0. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the PlotY function:

- apps\scopedemo\scopedem.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- apps\screenupdate\update.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\callback.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphlegend.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\graphs.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\timeaxis.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviposting_events.htm language=enus -->
## TOPIC 01224: Posting Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviposting_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviposting_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Posting Events

[PostDeferredCall](cvipostdeferredcall.htm) tells LabWindows/CVI to call a specific function the next time LabWindows/CVI [processes events](cviprocessing_events.htm).

You typically call PostDeferredCall in a function you install as an asynchronous interrupt handler. The types of operations you can perform in an asynchronous interrupt handler are limited. For example, you cannot freely access global variables. Pass to PostDeferredCall the name of a function that contains the code you cannot include in the asynchronous interrupt handler.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviprintctrl.htm language=enus -->
## TOPIC 01225: PrintCtrl

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviprintctrl.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviprintctrl.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PrintCtrl

int PrintCtrl (int panelHandle, int controlID, char filename[], int scaling, int confirmDialogBox);

#### Purpose

Prints the selected control.

While this function is printing, it blocks any other thread in your 
program that attempts to print.

Remember that LabWindows/CVI maintains only one copy of the print 
attributes you set with [SetPrintAttribute](../../cvi/uiref/cvisetprintattribute.htm). Thus, when you change a 
print attribute in one thread, the change affects printing functions 
you subsequently call in other threads.

#### Supported Controls

You can use PrintCtrl with all LabWindows/CVI [user interface controls](../../cvi/uiref/cvioperating_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| filename | char [] | Name of the output file. If the name is not empty, the output is redirected to the file. If the name is not a complete pathname, the file is created relative to the current working directory. The format of the generated output file depends on the printer driver. This obsolete parameter is only for backwards compatibility. |
| scaling | int | Selects the scaling mode for printing. Specify a nonzero value or select full size in the function panel to expand the object to full size. Specify 0 or select size to screen in the function panel to print the object at the same relative location and size on paper as displayed on the screen. Note By default, PrintCtrl uses the following settings: ATTR_PRINT_AREA_WIDTH is set to VAL_INTEGRAL_SCALE. ATTR_PRINT_AREA_HEIGHT is set to VAL_INTEGRAL_SCALE. If ATTR_PAPER_HEIGHT or ATTR_PAPER_WIDTH is set to VAL_INTEGRAL_SCALE, this parameter is forced to full size. |
|  | Note By default, PrintCtrl uses the following settings: ATTR_PRINT_AREA_WIDTH is set to VAL_INTEGRAL_SCALE. ATTR_PRINT_AREA_HEIGHT is set to VAL_INTEGRAL_SCALE. If ATTR_PAPER_HEIGHT or ATTR_PAPER_WIDTH is set to VAL_INTEGRAL_SCALE, this parameter is forced to full size. |  |
| confirmDialogBox | int | Determines whether to display a dialog box before printing to confirm print attributes. This dialog box shows the current print attribute values and to what extent the current printer supports them. The user can change the attribute values during run time. Specify a nonzero value or select show in the function panel to display the dialog box. Specify 0 or select hide in the function panel to omit the dialog box. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| printStatus | int | The status of the print operation. The PrintCtrl function returns a value that contains bit-fields. Defined Constant Value VAL_TOO_MANY_COPIES (1<<0) VAL_NO_MULTIPLE_COPIES (1<<1) VAL_NO_DUPLEX (1<<2) VAL_NO_LANDSCAPE (1<<3) VAL_CANT_FORCE_MONO (1<<4) VAL_NO_SUCH_XRESOLUTION (1<<5) VAL_NO_MULTIPLE_XRESOLUTIONS (1<<6) VAL_NO_SUCH_YRESOLUTION (1<<7) VAL_NO_MULTIPLE_YRESOLUTIONS (1<<8) VAL_NO_SEPARATE_YRESOLUTION (1<<9) VAL_USER_CANCEL (1<<10) A negative value indicates that an error occurred. |
| Defined Constant | Value |  |
| VAL_TOO_MANY_COPIES | (1<<0) |  |
| VAL_NO_MULTIPLE_COPIES | (1<<1) |  |
| VAL_NO_DUPLEX | (1<<2) |  |
| VAL_NO_LANDSCAPE | (1<<3) |  |
| VAL_CANT_FORCE_MONO | (1<<4) |  |
| VAL_NO_SUCH_XRESOLUTION | (1<<5) |  |
| VAL_NO_MULTIPLE_XRESOLUTIONS | (1<<6) |  |
| VAL_NO_SUCH_YRESOLUTION | (1<<7) |  |
| VAL_NO_MULTIPLE_YRESOLUTIONS | (1<<8) |  |
| VAL_NO_SEPARATE_YRESOLUTION | (1<<9) |  |
| VAL_USER_CANCEL | (1<<10) |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Example

Refer to userint\custctrl\cviogl\ogldemo.cws for an example of using the PrintCtrl function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviprinting_and_multithreading.htm language=enus -->
## TOPIC 01226: Printing and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviprinting_and_multithreading.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviprinting_and_multithreading.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Printing and Multithreading

When you use [PrintPanel](cviprintpanel.htm), [PrintCtrl](cviprintctrl.htm), [PrintTextBuffer](cviprinttextbuffer.htm), or [PrintTextFile](cviprinttextfile.htm) to print from a given [thread](cvidifferent_approaches_to_multithr.htm), these functions [block](cvithread_blocking.htm) other threads that attempt to print until the active print function returns.
This blocking occurs even when the print function displays a dialog box and
waits for user events.

If you set [ATTR_EJECT_AFTER](cviattrejectafter.htm) to zero in one thread, the paper is not ejected even when the next call to a
print function comes from another thread. For this reason, use caution when you
print from multiple threads.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviprintpanel.htm language=enus -->
## TOPIC 01227: PrintPanel

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviprintpanel.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviprintpanel.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### PrintPanel

int PrintPanel (int panelHandle, char filename[], int scaling, int scope, int confirmDialogBox);

#### Purpose

Prints the selected panel.

While this function is printing, it blocks any other thread in your 
program that attempts to print.

Remember that LabWindows/CVI maintains only one copy of the print 
attributes you set with [SetPrintAttribute](../../cvi/uiref/cvisetprintattribute.htm). Thus, when you change a 
print attribute in one thread, the change affects printing functions 
you subsequently call in other threads.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| filename | char [] | Name of the output file. If the name is not empty, the output is redirected to the file. If the name is not a complete pathname, the file is created relative to the current working directory. |
| scaling | int | Selects the scaling mode for printing. Specify a nonzero value or select full size in the function panel to expand the panel to full size. Specify 0 or select relative to screen in the function panel to print the panel at the same relative location and size on paper as displayed on the screen. Note If ATTR_PAPER_HEIGHT or ATTR_PAPER_WIDTH is set to VAL_INTEGRAL_SCALE, this parameter is forced to full size. |
|  | Note If ATTR_PAPER_HEIGHT or ATTR_PAPER_WIDTH is set to VAL_INTEGRAL_SCALE, this parameter is forced to full size. |  |
| scope | int | Selects the portion of the panel to print: VAL_VISIBLE_AREA or VAL_FULL_PANEL. VAL_VISIBLE_AREA—Prints only the portion of the panel that is visible on the screen. Menu bars, scroll bars, and a frame are printed along with the visible portion. VAL_FULL_PANEL—Prints the entire panel. No menu bars, scroll bars, or frames print. Note If you select VAL_VISIBLE_AREA, the panel title bar and frame have the appearance of child panels in the bitmap. This behavior occurs for both top-level panels and child panels. Regardless of the scope, objects within child panels are clipped to the frame of the child panel. Note If the printout does not fit on the page, call SetPrintAttribute before PrintPanel to change the settings as follows: Set ATTR_PRINT_AREA_WIDTH to VAL_INTEGRAL_SCALE. Set ATTR_PRINT_AREA_HEIGHT to VAL_USE_ENTIRE_PAPER. |
|  | Note If you select VAL_VISIBLE_AREA, the panel title bar and frame have the appearance of child panels in the bitmap. This behavior occurs for both top-level panels and child panels. |  |
|  | Note If the printout does not fit on the page, call SetPrintAttribute before PrintPanel to change the settings as follows: Set ATTR_PRINT_AREA_WIDTH to VAL_INTEGRAL_SCALE. Set ATTR_PRINT_AREA_HEIGHT to VAL_USE_ENTIRE_PAPER. |  |
| confirmDialogBox | int | Determines whether to display a dialog box before printing to confirm print attributes. The dialog box shows the current print attribute values and to what extent the current printer supports them. The end-user can change the attribute values during run time. Specify a nonzero value or select show in the function panel to display the dialog box. Specify 0 or select hide in the function panel to omit the dialog box. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| printStatus | int | The status of the print operation. The PrintCtrl function returns a value that contains bit-fields. Defined Constant Value VAL_TOO_MANY_COPIES (1<<0) VAL_NO_MULTIPLE_COPIES (1<<1) VAL_NO_DUPLEX (1<<2) VAL_NO_LANDSCAPE (1<<3) VAL_CANT_FORCE_MONO (1<<4) VAL_NO_SUCH_XRESOLUTION (1<<5) VAL_NO_MULTIPLE_XRESOLUTIONS (1<<6) VAL_NO_SUCH_YRESOLUTION (1<<7) VAL_NO_MULTIPLE_YRESOLUTIONS (1<<8) VAL_NO_SEPARATE_YRESOLUTION (1<<9) VAL_USER_CANCEL (1<<10) A negative value indicates that an error occurred. |
| Defined Constant | Value |  |
| VAL_TOO_MANY_COPIES | (1<<0) |  |
| VAL_NO_MULTIPLE_COPIES | (1<<1) |  |
| VAL_NO_DUPLEX | (1<<2) |  |
| VAL_NO_LANDSCAPE | (1<<3) |  |
| VAL_CANT_FORCE_MONO | (1<<4) |  |
| VAL_NO_SUCH_XRESOLUTION | (1<<5) |  |
| VAL_NO_MULTIPLE_XRESOLUTIONS | (1<<6) |  |
| VAL_NO_SUCH_YRESOLUTION | (1<<7) |  |
| VAL_NO_MULTIPLE_YRESOLUTIONS | (1<<8) |  |
| VAL_NO_SEPARATE_YRESOLUTION | (1<<9) |  |
| VAL_USER_CANCEL | (1<<10) |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

#### Examples

Refer to the following examples that use the PrintPanel function:

- apps\uirview\uirview.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- userint\custctrl\cviogl\simple.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviqueueuserevent.htm language=enus -->
## TOPIC 01228: QueueUserEvent

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviqueueuserevent.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviqueueuserevent.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### QueueUserEvent

int QueueUserEvent (int eventNumber, int panelHandle, int controlID);

#### Purpose

Inserts a programmer-defined event in the [GetUserEvent](../../cvi/uiref/cvigetuserevent.htm) queue. You can later retrieve the event by calling GetUserEvent.

Event numbers 1,000 to 10,000 are reserved for programmer-defined events. You
can assign any meaning you choose to the event number.

#### Supported Controls

You can use QueueUserEvent with all LabWindows/CVI [user interface controls](../../cvi/uiref/cvioperating_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventNumber | int | An integer value between 1,000 and 10,000 that this function places in the event queue and that you can later retrieve from GetUserEvent. |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. Pass 0 when the event does not apply to a particular panel. |
| controlID | int | Defined constant, located in the .uir header file, that you assign to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. Pass 0 when the event does not apply to a particular control. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 3.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvirectcontainspoint.htm language=enus -->
## TOPIC 01229: RectContainsPoint

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvirectcontainspoint.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvirectcontainspoint.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RectContainsPoint

int RectContainsPoint (Rect rect, Point point);

#### Purpose

Returns 1 if the specified rectangle encloses the point you specify. The function returns 0 otherwise.

The rectangle is considered to enclose the point if the point is in the interior of the rectangle or on its frame.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rect | Rect | The location and size of a rectangle. |
| point | Point | The location of the center of the rectangle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| containsPoint | int | Indicates if rect contains point. Code Description 1 point is in the interior or on the frame of the rectangle specified by rect. 0 point is outside the frame of the rectangle specified by rect. |
| Code | Description |  |
| 1 | point is in the interior or on the frame of the rectangle specified by rect. |  |
| 0 | point is outside the frame of the rectangle specified by rect. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

#### Example

Refer to userint\colview.cws for an example of using the RectContainsPoint function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvirectcontainsrect.htm language=enus -->
## TOPIC 01230: RectContainsRect

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvirectcontainsrect.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvirectcontainsrect.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RectContainsRect

int RectContainsRect (Rect containerRect, Rect containedRect);

#### Purpose

Returns 1 if the first rectangle you specify encloses the second 
rectangle you specify. The function returns 0 otherwise.

A rectangle is considered to enclose another rectangle if every point of the second rectangle is in the interior or on the frame of the first rectangle. A rectangle encloses itself.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| containerRect | Rect | The rectangle tested to determine whether it encloses another rectangle. |
| containedRect | Rect | The rectangle tested to determine whether it is enclosed by another rectangle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| containsRect | int | Indicates if containerRect encloses containedRect. Code Description 1 The first rectangle encloses the second rectangle. 0 The first rectangle does not enclose the second rectangle. |
| Code | Description |  |
| 1 | The first rectangle encloses the second rectangle. |  |
| 0 | The first rectangle does not enclose the second rectangle. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvirectempty.htm language=enus -->
## TOPIC 01231: RectEmpty

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvirectempty.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvirectempty.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RectEmpty

int RectEmpty (Rect rect);

#### Purpose

Returns 1 if the rectangle you specify is empty. The function returns 0 otherwise.

A rectangle is considered empty if either its height or width 
is less than or equal to zero.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rect | Rect | The location and size of a rectangle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| empty | int | Indicates if the specified rectangle is empty. Code Description 1 Either rect.height or rect.width is less than or equal to zero. 0 Both rect.height and rect.width are greater than zero. |
| Code | Description |  |
| 1 | Either rect.height or rect.width is less than or equal to zero. |  |
| 0 | Both rect.height and rect.width are greater than zero. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvirectequal.htm language=enus -->
## TOPIC 01232: RectEqual

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvirectequal.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvirectequal.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RectEqual

int RectEqual (Rect rect1, Rect rect2);

#### Purpose

Returns 1 if the top, left, height, and width of the two rectangles you specify 
are identical. Returns 0 otherwise.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rect1 | Rect | The location and size of a rectangle. |
| rect2 | Rect | The location and size of a rectangle. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| equal | int | Indicates if the top, left, height, and width values in rect1 are identical to those of rect2. Code Description 1 rect1 and rect2 have the identical top, left, height, and width values. 0 rect1 and rect2 do not have the identical top, left, height, and width values. |
| Code | Description |  |
| 1 | rect1 and rect2 have the identical top, left, height, and width values. |  |
| 0 | rect1 and rect2 do not have the identical top, left, height, and width values. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvirectgrow.htm language=enus -->
## TOPIC 01233: RectGrow

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvirectgrow.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvirectgrow.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RectGrow

void RectGrow (Rect *rectangle, int dx, int dy);

#### Purpose

Modifies the values in a Rect structure so that the rectangle it 
defines grows or shrinks around its current center point.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| dx | int | Amount to grow the rectangle horizontally. Use a negative value to shrink the rectangle horizontally. |
| dy | int | Amount to grow the rectangle vertically. Use a negative value to shrink the rectangle vertically. |
| Output |  |  |
| Name | Type | Description |
| rectangle | Rect | On input, the size and location of a rectangle. On output, a rectangle of a different size but the same center point. |

#### Return Value

None.

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvirectintersection.htm language=enus -->
## TOPIC 01234: RectIntersection

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvirectintersection.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvirectintersection.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RectIntersection

int RectIntersection (Rect rect1, Rect rect2, Rect *intersectionRect);

#### Purpose

Returns an indication of whether the two rectangles you specify intersect. If they do, the function fills in a Rect structure describing the intersection area.

This function also calculates the largest rectangle that is enclosed by the two specified rectangles.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rect1 | Rect | The location and size of a rectangle. |
| rect2 | Rect | The location and size of a rectangle. |
| Output |  |  |
| Name | Type | Description |
| intersectionRect | Rect | Rect structure that specifies the largest rectangle enclosed by both rect1 and rect2. If rect1 and rect2 do not intersect, this parameter is set to an empty rectangle with height and width less than or equal to zero. You can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| rectsIntersect | int | Indicates if rect1 and rect2 intersect, in other words, have any points in common. Code Description 1 rect1 and rect2 intersect. 0 rect1 and rect2 do not intersect. |
| Code | Description |  |
| 1 | rect1 and rect2 intersect. |  |
| 0 | rect1 and rect2 do not intersect. |  |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvirectmove.htm language=enus -->
## TOPIC 01235: RectMove

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvirectmove.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvirectmove.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RectMove

void RectMove (Rect *rectangle, Point point);

#### Purpose

Modifies a Rect structure so that the top, left corner of the 
rectangle it defines is at the point you specify.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | Point | Point structure specifying the new location of the top, left corner of the rectangle. |
| Output |  |  |
| Name | Type | Description |
| rectangle | Rect | On input, the size and location of a rectangle. On output, a rectangle of the same size but a different location. |

#### Return Value

None.

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvirectoffset.htm language=enus -->
## TOPIC 01236: RectOffset

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvirectoffset.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvirectoffset.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### RectOffset

void RectOffset (Rect *rectangle, int dx, int dy);

#### Purpose

Modifies the values in a Rect structure to shift the location of the 
rectangle it defines.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| dx | int | Amount to shift the rectangle horizontally. Use a positive value to shift the rectangle to the right. Use a negative value to shift the rectangle to the left. |
| dy | int | Amount to shift the rectangle vertically. Use a positive value to shift the rectangle down. Use a negative value to shift the rectangle up. |
| Output |  |  |
| Name | Type | Description |
| rectangle | Rect | On input, the size and location of a rectangle. On output, a rectangle of the same size but a different location. |

#### Return Value

None.

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviresponding_to_events_in_a_graphi.htm language=enus -->
## TOPIC 01237: Responding to Events in a Graphical User Interface

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviresponding_to_events_in_a_graphi.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviresponding_to_events_in_a_graphi.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Responding to Events in a Graphical User Interface

When designing a user interface, you set up 
[controls](cvioperating_controls.htm) to generate [events](cvievents_overview.htm). 
For example, selecting a [command button](cvicommand_button_control_overview.htm) 
generates a user interface event that LabWindows/CVI passes
to your C program. In fact, a single action on a LabWindows/CVI control can generate multiple user
interface events. For example, selecting a command button can pass
the following user interface events to your program for processing:

1. EVENT_GOT_FOCUS —If the command button is not the 
active control (i.e., it does not have the input
focus), selecting the button makes it the active control. When a control
receives the input focus, an EVENT_GOT_FOCUS occurs.
2. EVENT_LEFT_CLICK —When users click with the left 
mouse button on the command button, an EVENT_LEFT_CLICK occurs. 
LabWindows/CVI user interface controls can recognize left,
right, single, and double mouse clicks.
3. EVENT_COMMIT —When the user releases the mouse button, 
an EVENT_COMMIT occurs signifying that the user has performed a commit event on the
control.

|  | Note Each control can have one or more control modes that determine how the control responds to the events. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviresumetimercallbacks.htm language=enus -->
## TOPIC 01238: ResumeTimerCallbacks

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviresumetimercallbacks.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviresumetimercallbacks.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### ResumeTimerCallbacks

int ResumeTimerCallbacks (void);

#### Purpose

Cancels the effect of a call to [SuspendTimerCallbacks](../../cvi/uiref/cvisuspendtimercallbacks.htm).

Callbacks resume using the ongoing interval schedules, which are not affected by SuspendTimerCallbacks.

This function affects only timer controls you loaded or created in the active thread.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 4.0 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviring_attributes.htm language=enus -->
## TOPIC 01239: Ring Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviring_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviring_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Ring Control Attributes

The User Interface Library attributes that are valid for
[ring](cviring_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Frame Color
- Frame Thickness
- Inc/Dec Arrow Width
- Menu Arrow Color
- Menu Arrow Height
- Menu Arrow Width
- Visible
- Size/Position
- Text Style

#### Control Settings

- Control Mode
- Control Style
- Control Value
- Data Type
- Default Value
- Default Value Length
- Dimmed
- Disable Check Mark
- Disable Control Tooltip
- Next Panel Control
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position
- Index

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

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviring_control_events.htm language=enus -->
## TOPIC 01240: Ring Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviring_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviring_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Ring Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [ring](cviring_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

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
- EVENT_RING_BEGIN_MENU

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cviring_control_functions.htm language=enus -->
## TOPIC 01241: Ring Control Functions

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cviring_control_functions.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cviring_control_functions.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Ring Control Functions

The following User Interface Library functions operate on [ring](cviring_control_overview.htm) controls.

- AddCtrlToSplitter
- ClearListCtrl
- DefaultCtrl
- DeleteListItem
- DiscardCtrl
- DuplicateCtrl
- GetCtrlArrayIndex
- GetCtrlAttribute
- GetCtrlBoundingRect
- GetCtrlDisplayBitmap
- GetCtrlIndex
- GetCtrlVal
- GetIndexFromValue
- GetLabelFromIndex
- GetLabelLengthFromIndex
- GetNumListItems
- GetRelativeMouseState
- GetRingItemAttribute
- GetScaledCtrlDisplayBitmap
- GetValueFromIndex
- GetValueLengthFromIndex
- InsertCtrlArrayItem
- InsertListItem
- InstallCtrlCallback
- PrintCtrl
- QueueUserEvent
- RemoveCtrlFromSplitter
- ReplaceListItem
- SetActiveCtrl
- SetCtrlAttribute
- SetCtrlIndex
- SetCtrlVal
- SetInputMode
- SetRingItemAttribute

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvisettreecellringitemattribute.htm language=enus -->
## TOPIC 01242: SetTreeCellRingItemAttribute

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvisettreecellringitemattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvisettreecellringitemattribute.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetTreeCellRingItemAttribute

int SetTreeCellRingItemAttribute (int panelHandle, int controlID, int itemIndex, int columnIndex, int ringIndex, int itemAttribute, ...);

#### Purpose

Sets the value of a ring item attribute. Use this function to interact with tree cells whose [type](../../cvi/uiref/cviattrcelltype_tree cell.htm) is ring or combo box.

#### Supported Controls

You can use SetTreeCellRingItemAttribute with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item containing the cell of the ring item. |
| columnIndex | int | Zero-based index of the tree column that contains the cell of the ring item. |
| ringIndex | int | The zero-based index specifying the ring item. |
| itemAttribute | int | The ring item attribute value to set. In the function panel, when you click the control or press <Enter>, <Spacebar>, or <Ctrl-down arrow>, a dialog box appears containing a hierarchical list of the available attributes. Attributes whose values cannot be obtained are dimmed. Help text is shown for each attribute. To select an attribute, double-click it or select it and then press <Enter>. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by moving to the Attribute Value control and pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |
| attributeValue | ... | The value to which to set the ring item attribute. If the attribute shown in this ring control has named constants as valid values, you can open a list of them by pressing <Enter>. The Attribute Values dialog box displays the values and value help for the constants. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvisettreecellringvaluefromindex.htm language=enus -->
## TOPIC 01243: SetTreeCellRingValueFromIndex

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvisettreecellringvaluefromindex.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvisettreecellringvaluefromindex.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SetTreeCellRingValueFromIndex

int SetTreeCellRingValueFromIndex (int panelHandle, int controlID, int itemIndex, int columnIndex, int ringIndex);

#### Purpose

Sets the value of a tree control ring or combo box cell to the specified item of the list of values of the cell.

#### Supported Controls

You can use SetTreeCellRingValueFromIndex with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| itemIndex | int | Zero-based index of the tree item containing the cell for which you want to set the value. |
| columnIndex | int | The zero-based index of the tree column containing the cell for which you want to set the value. |
| ringIndex | int | The zero-based index of the item in the list of values. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2009 and later

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvisorttablecells.htm language=enus -->
## TOPIC 01244: SortTableCells

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvisorttablecells.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvisorttablecells.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SortTableCells

int SortTableCells (int panelHandle, int controlID, Rect cellRange, int sortingDirection, int keyIndex, int descending, CellCompareCallbackPtr comparisonFunction, void *callbackData);

#### Purpose

Sorts a group of cells in a table control. You must specify a row, or 
column, as the sort key and a cell range indicating what other rows, or columns, the function should move as the values in the key row, or column, move.

When the function swaps the values of two cells, it also swaps all 
attributes, such as colors, fonts, and types, of the two cells.

#### Supported Controls

You can use SortTableCells with [table controls](../../cvi/uiref/cviprogramming_with_table_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| cellRange | Rect | A Rect structure specifying the cell range you want to sort. The Rect structure is defined as follows: typedef struct { int top; int left; int height; int width; } Rect; Pass the one-based row and column indices of the first cell in the range as the top and left fields of the structure, respectively. Pass the number of columns in the range as the width field of the structure, and the number of rows in the range as the height field of the structure. You can create a Rect without having to declare a variable by using the following function: Rect MakeRect (int top, int left, int height, int width); Example SetTableCellRangeVals (panelHandle, controlID, MakeRect (2, 3, 5, 5), valueArray, direction); |
| sortingDirection | int | Determines whether the function sorts the values in a row or the values in a column. If you pass VAL_ROW_MAJOR, the function interprets keyIndex as a row index and sorts the values in that row. As the function moves the value of a given cell in the key row from one column to another, to match the sort criteria, the values of all other cells in the same column that are contained in the specified cell range also are moved to the same target column. If you pass VAL_COLUMN_MAJOR, the function interprets keyIndex as a column index and sorts the values in that column. As the function moves the value of a given cell in the key column from one row to another, to match the sort criteria, the values of all other cells in the same row that are contained in the specified cell range also are moved to the same target row. |
| keyIndex | int | The index of the row, or column, that contains the key values. The function interprets this index as that of a row or a column depending on the value of sortingDirection. The row, or column, specified must be included in cellRange. If comparisonFunction is NULL, all cells in the specified row, or column, and that also are contained in cellRange must be of the same cell type. In addition, their cell type cannot be VAL_CELL_PICTURE. |
| descending | int | Specify a nonzero value or select Yes in the function panel to sort the values in descending order. Specify 0 or select No in the function panel to sort the values in ascending order. |
| comparisonFunction | CellCompareCallbackPtr | The name of an optional cell comparison function that you can use to perform custom sorts. This function (type CellCompareCallbackPtr) takes the following form: int CVICALLBACK FunctionName (int panelHandle, int controlID, Point item1, Point item2, void *callbackData); When SortTableCells needs to compare two cells, it calls your function and allows you to perform the comparison. Your function receives the panelHandle and controlID of the table control and two point structures corresponding to the two cells you need to compare. The Point structure is defined as follows: typedef struct { int x; int y; } Point; typedef struct { int x; int y; } Point; The x field of the structure contains the one-based column index of the cell, and the y field of the structure contains the one-based row index of the cell. This function also receives the value you pass to callbackData. To perform the comparison you can, if you choose, obtain the values of the two cells using GetTableCellVal, or of any other cells you can choose to use as secondary sort keys. Return –1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if item1 and item2 are equivalent. If you choose not to use a custom comparison function, you can pass NULL and SortTableCells performs the comparisons. In this case, all cells referenced by keyIndex that are also contained in cellRange must be of the same cell type. In addition, their cell type cannot be VAL_CELL_PICTURE. If the cell type is VAL_CELL_NUMERIC, SortTableCells promotes values of different data types to doubles before comparing them. |
| callbackData | void * | If you perform the cell comparisons through a callback function, you can provide a pointer to user-defined data. If you do not need to pass user-defined data to the callback function, or if you are not using a callback function to perform the comparisons, you can use a value of zero. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 5.5 and later

#### Example

Refer to userint\colview.cws for an example of using the SortTableCells function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvisorttreeitems.htm language=enus -->
## TOPIC 01245: SortTreeItems

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvisorttreeitems.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvisorttreeitems.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### SortTreeItems

int SortTreeItems (int panelHandle, int controlID, int siblingIndex, int keyColumnIndex, int descending, int sortSubTrees, TreeCellCompareCallbackPtr comparisonFunction, void *callbackData);

#### Purpose

Sorts all the siblings of a specified tree item. You must specify a column as the sort key.

When the function swaps the two items, it also swaps all attributes, such as colors, fonts, and types, of the two items and the cells they contain.

#### Supported Controls

You can use SortTreeItems with [tree controls](../../cvi/uiref/cviprogramming_with_tree_controls.htm).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| panelHandle | int | Specifier for a particular panel that is currently in memory. You can obtain this handle from functions such as LoadPanel and NewPanel. |
| controlID | int | The defined constant, located in the .uir header file, that you assigned to the control in the User Interface Editor, or the ID returned by functions such as NewCtrl and DuplicateCtrl. |
| siblingIndex | int | Zero-based index of an item whose siblings you want to sort. |
| keyColumnIndex | int | The index of the column that contains the key values. |
| descending | int | Specify a nonzero value or select Yes in the function panel to sort the items in descending order. Specify 0 or select No in the function panel to sort the items in ascending order. |
| sortSubTrees | int | Specify a nonzero value or select Yes in the function panel to sort the subtree of each sorted item. Specify 0 or select No in the function panel if you do not want to sort subtrees. |
| comparisonFunction | TreeCellCompareCallbackPtr | The name of an optional tree cell comparison function that you can use to perform custom sorts. This function (type TreeCellCompareCallbackPtr) takes the following form: int CVICALLBACK FunctionName (int panelHandle, int controlID, int item1, int item2, int keyCol, void *callbackData); When SortTreeItems needs to compare two cells, it calls your function and allows you to perform the comparison. Your function receives the panelHandle and controlID of the tree control and two item indices corresponding to the two items you need to compare. This function also receives the value you pass to callbackData. To perform the comparison you can, if you choose, obtain the labels of the two cells using GetTreeCellAttribute and ATTR_LABEL_TEXT, or of any other cells you choose to use as secondary sort keys. Return –1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if item1 and item2 are equivalent. If you choose not to use a custom comparison function, you can pass NULL and SortTreeItems performs a case-sensitive string comparison on the labels. |
| callbackData | void * | If you perform the cell comparisons through a callback function, you can provide a pointer to user-defined data. If you do not need to pass user-defined data to the callback function, or if you are not using a callback function to perform the comparisons, you can use a value of zero. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. A negative number indicates that an error occurred. |

#### Additional Information

**Library:** [User Interface Library](../../cvi/uiref/cviuser_interface_library_function_tree.htm)

**Include file:** userint.h

**LabWindows/CVI compatibility:** LabWindows/CVI 7.0 and later

#### Example

Refer to userint\treeList.cws for an example of using the SortTreeItems function.

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvisplitter_control_events.htm language=enus -->
## TOPIC 01246: Splitter Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvisplitter_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvisplitter_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Splitter Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [splitter](cvisplitter_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

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
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvistrip_chart_attributes.htm language=enus -->
## TOPIC 01247: Strip Chart Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvistrip_chart_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvistrip_chart_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Strip Chart Control Attributes

The User Interface Library attributes that are valid for
[strip chart](cvistrip_chart_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Chart Horizontal Scroll Offset
- Disable Panel Theme
- Edge Style
- Enable Anti-Aliasing
- Fixed Plot Area
- Graph Background Color
- Grid Color
- Grid Style
- Plot Area Height
- Plot Area Left
- Plot Area Top
- Plot Area Width
- Plot Background Color
- Visible
- Axis Names
- Show/Hide Parts
- Size/Position

#### Control Settings

- Control Style
- Dimmed
- Disable Control Tooltip
- History Buffer Size
- Next Panel Control
- Number of Traces
- Points Per Screen
- Scroll Mode
- Show Chart Division Labels
- Strip Chart Paused
- Sweep Line Color
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position
- DataSocket Settings
- X-Axis
- Y-Axis

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

#### Legend

- Auto Size Graph Legend
- Legend Background Color
- Legend Frame Color
- Legend Height
- Legend Interactive
- Legend Left
- Legend Top
- Legend Visible
- Legend Width
- Number of Visible Legend Items
- Show Legend Sample Plots

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvistrip_chart_control_events.htm language=enus -->
## TOPIC 01248: Strip Chart Control Events

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvistrip_chart_control_events.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvistrip_chart_control_events.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Strip Chart Control Events

The following User Interface Library [events](cvievents_overview.htm) are sent to [strip chart](cvistrip_chart_control_overview.htm) control [callback](cviusing_callback_functions_to_resp.htm) functions.

- EVENT_LEFT_CLICK
- EVENT_LEFT_DOUBLE_CLICK
- EVENT_RIGHT_CLICK
- EVENT_RIGHT_DOUBLE_CLICK
- EVENT_DISCARD
- EVENT_HSCROLL
- EVENT_MOUSE_POINTER_MOVE
- EVENT_LEFT_CLICK_UP
- EVENT_RIGHT_CLICK_UP
- EVENT_MOUSE_WHEEL_SCROLL
- EVENT_MOUSE_WHEEL_CLICK
- EVENT_INTERACTIVE_LEGEND
- EVENT_CTRL_MENU

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvisystem_attributes_and_multithrea.htm language=enus -->
## TOPIC 01249: System Attributes and Multithreading

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvisystem_attributes_and_multithrea.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvisystem_attributes_and_multithrea.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### System Attributes and Multithreading

The following table indicates, for each [system attribute](cvilist_of_system_attributes.htm), whether the User Interface Library maintains separate values for each [thread](cvidifferent_approaches_to_multithr.htm), or one global value for the entire process.

| System Attribute | Values Maintained |
| --- | --- |
| ATTR_RESOLUTION_ADJUSTMENT | Separate value for each thread. |
| ATTR_TASKBAR_BUTTON_VISIBLE | Separate value for each thread. |
| ATTR_TASKBAR_BUTTON_TEXT | Separate value for each thread. |
| ATTR_REPORT_LOAD_FAILURE | One global value. |
| ATTR_ALLOW_MISSING_CALLBACKS | One global value. |
| ATTR_ALLOW_UNSAFE_TIMER_EVENTS | One global value. |
| ATTR_SUPPRESS_EVENT_PROCESSING | Separate value for each thread. |

<!--NI_TOPIC bundle=labwindows-cvi path=cvi/uiref/cvitab_attributes.htm language=enus -->
## TOPIC 01250: Tab Control Attributes

- bundle_id: `labwindows-cvi`
- source_path: `cvi/uiref/cvitab_attributes.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi/raw/resource/enus/cvi/uiref/cvitab_attributes.htm
- document_id: `labwindows-cvi`
- page_type: `leaf`
- content_type: ``

### Tab Control Attributes

The User Interface Library attributes that are valid for
[tab](cvitab_control_overview.htm)
controls appear in the following list:

#### Control Appearance

- Disable Panel Theme
- Maximum Tab Width
- Tabs End Offset
- Tabs Fit Mode
- Tabs Location
- Tabs Start Offset
- Visible
- Show/Hide Parts
- Size/Position

#### Control Settings

- Control Mode
- Control Style
- Dimmed
- Disable Control Tooltip
- Enable Drag Drop
- Next Panel Control
- Tab Position
- Tooltip Delay
- Tooltip Hide Delay
- Tooltip Text
- Tooltip Text Length
- Z-Plane Position
- Index

#### Source Code Connection

- Callback Data
- Callback Function Name
- Callback Function Name Length
- Callback Function Pointer
- Constant Name
- Constant Name Length
