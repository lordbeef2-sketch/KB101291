# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=5501 end=5750 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-updatefromfile.html language=enus -->
## TOPIC 05501: ReportView.UpdateFromFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-updatefromfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-updatefromfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.UpdateFromFile( fileName) Purpose Updates the content of the control from a file. Remarks The extension of the fileName parameter determines the report style of the control. For example, if fileName is C:\Reports\MyReport.html , the style is HTML. This method returns an error if th

### ReportView.UpdateFromFile

#### Syntax

[ReportView](reportview.html).UpdateFromFile( fileName)

#### Purpose

Updates the content of the control from a file.

#### Remarks

The extension of the
 fileName
 parameter determines the report style of the control. For example, if
 fileName
 is
 C:\Reports\MyReport.html
 , the style is HTML.

Note

ReportView

#### Parameters

fileName
 As
 [String](data-types-for-teststand-user-interface.html)

Specifies the full path of the report file.

#### See Also

[Report.Format](../tsapiref/report-format.html)

[ReportView General property page](reportview-general-property-page.html)

[ReportView.UpdateFromExecution](reportview-updatefromexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview.html language=enus -->
## TOPIC 05502: ReportView

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect an ExecutionView Manager control to a ReportView control to display the report for the selected execution. Properties Borders (Read Only) ButtonsVisible LargeIcons ScaleWithDPI TextReportBackColor TextReportColor TextReportFont TextReportFontSource ToolBarTextStyle ToolBarVisible Methods Get

### ReportView

Connect an
 [ExecutionView Manager](executionviewmgr.html)
 control to a ReportView control to display the report for the selected execution.

#### Properties

| Borders (Read Only) |
| --- |
| ButtonsVisible |
| LargeIcons |
| ScaleWithDPI |
| TextReportBackColor |
| TextReportColor |
| TextReportFont |
| TextReportFontSource |
| ToolBarTextStyle |
| ToolBarVisible |

#### Methods

| GetHTMLCtrl |
| --- |
| GetRichEditCtrl |
| PrintReport |
| UpdateFromExecution |
| UpdateFromFile |

#### Events

| BorderDragged |
| --- |
| ConnectionActivity |

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConnectReportView](executionviewmgr-connectreportview.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewbuttons.html language=enus -->
## TOPIC 05503: ReportViewButtons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewbuttons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewbuttons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ReportView.ButtonsVisible property. ReportViewButton_Back –(Value: 0x1) Use this button to navigate to previously viewed reports. ReportViewButton_ExternalViewer –(Value: 0x20) Use this button to open an external viewer for this kind of report. ReportViewButton_FontSize

### ReportViewButtons

Use these constants with the
 [ReportView.ButtonsVisible](reportview-buttonsvisible.html)
 property.

- ReportViewButton_Back 
 –(Value: 0x1) Use this button to navigate to previously viewed reports.
- ReportViewButton_ExternalViewer 
 –(Value: 0x20) Use this button to open an external viewer for this kind of report.
- ReportViewButton_FontSize 
 –(Value: 0x80) Use this button to change the size of the HTML text displayed.
 Note 
 This size is a global setting for the computer and affects the size of text in the web browser when you are using Microsoft Internet Explorer.
- ReportViewButton_Forward 
 –(Value: 0x2) Use this button to navigate to previously viewed reports.
- ReportViewButton_Home 
 –(Value: 0x10) Use this button to navigate to the first report opened in the
 ReportView 
 control.
- ReportViewButton_OpenReportLocation 
 (Value: 0x200) Use this button to open File Explorer in the location where the currently displayed report is saved.
- ReportViewButton_Print 
 –(Value: 0x40) Use this button to print the currently displayed report. You can configure the Print button to launch the Print dialog box before printing on the
 
 General property page 
 of the ReportView control.
- ReportViewButton_Refresh 
 –(Value: 0x8) Use this button to refresh the currently displayed report.
- ReportViewButton_SelectActiveReport 
 –(Value: 256) Use this button to change the active report in the
 
 Reports 
 collection of an execution. The
 ReportView 
 control displays the current active report. This button is disabled if the
 Reports 
 collection is empty.
- ReportViewButton_Stop 
 –(Value: 0x4) Use this button to stop the ReportView control from displaying the current report.

#### See Also

[General property page](reportview-general-property-page.html)

[ReportView](reportview.html)

[ReportView.ButtonsVisible](reportview-buttonsvisible.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewconnection.html language=enus -->
## TOPIC 05504: ReportViewConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from the ExecutionView Manager control to a control that displays a report associated with an execution. This class currently contains no properties or methods. Properties or methods might be added to this class in future versions of TestStand. See Also ExecutionView Manager

### ReportViewConnection

Represents a connection from the
 [ExecutionView Manager](executionviewmgr.html)
 control to a control that displays a report associated with an execution.

Note

#### See Also

[ExecutionView Manager](executionviewmgr.html)

[ReportViewConnections](reportviewconnections.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewconnections-add.html language=enus -->
## TOPIC 05505: ReportViewConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportViewConnections.Add( uiObj) Return Value ReportViewConnection New ReportViewConnection. Purpose Creates and adds a new ReportViewConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also ExecutionViewMgr.ConnectReportView Repo

### ReportViewConnections.Add

#### Syntax

[ReportViewConnections](reportviewconnections.html).Add( uiObj)

#### Return Value

[ReportViewConnection](reportviewconnection.html)

New ReportViewConnection.

#### Purpose

Creates and adds a new ReportViewConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[ExecutionViewMgr.ConnectReportView](executionviewmgr-connectreportview.html)

[ReportViewConnections.Remove](reportviewconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewconnections-clear.html language=enus -->
## TOPIC 05506: ReportViewConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportViewConnections.Clear Purpose Removes all items from the collection. See Also ReportViewConnections.Remove

### ReportViewConnections.Clear

#### Syntax

[ReportViewConnections](reportviewconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[ReportViewConnections.Remove](reportviewconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewconnections-count.html language=enus -->
## TOPIC 05507: ReportViewConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportViewConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### ReportViewConnections.Count

#### Syntax

[ReportViewConnections](reportviewconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewconnections-fromcontrol.html language=enus -->
## TOPIC 05508: ReportViewConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportViewConnections.FromControl( uiObj) Return Value ReportViewConnection ReportViewConnection connected to the uiObj parameter. When no ReportViewConnection exists for this control, this method returns NULL . Purpose Returns the ReportViewConnection connected to the uiObj parameter. Parame

### ReportViewConnections.FromControl

#### Syntax

[ReportViewConnections](reportviewconnections.html).FromControl( uiObj)

#### Return Value

[ReportViewConnection](reportviewconnection.html)

ReportViewConnection connected to the
 uiObj
 parameter. When no ReportViewConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the ReportViewConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewconnections-item.html language=enus -->
## TOPIC 05509: ReportViewConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportViewConnections.Item( itemIndex) Data Type ReportViewConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also ReportViewConnect

### ReportViewConnections.Item

#### Syntax

[ReportViewConnections](reportviewconnections.html).Item( itemIndex)

#### Data Type

[ReportViewConnection](reportviewconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[ReportViewConnection](reportviewconnection.html)

[ReportViewConnections.Count](reportviewconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewconnections-remove.html language=enus -->
## TOPIC 05510: ReportViewConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportViewConnections.Remove( uiObj) Return Value Boolean Returns True when the ReportViewConnection is removed. Returns False when the ReportViewConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the user

### ReportViewConnections.Remove

#### Syntax

[ReportViewConnections](reportviewconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the ReportViewConnection is removed. Returns
 False
 when the ReportViewConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[ReportViewConnections.Add](reportviewconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportviewconnections.html language=enus -->
## TOPIC 05511: ReportViewConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportviewconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportviewconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ReportViewConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also ReportViewConnection

### ReportViewConnections

A collection of
 [ReportViewConnection](reportviewconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[ReportViewConnection](reportviewconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/scrollbars.html language=enus -->
## TOPIC 05512: ScrollBars

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/scrollbars.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/scrollbars.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ExpressionEdit.ScrollBars property. ScrollBar_Both –(Value: 1) Shows the horizontal and vertical scrollbars. ScrollBar_Horizontal –(Value: 2) Shows only the horizontal scrollbar. ScrollBar_None –(Value: 0) Does not show the horizontal or vertical scrollbars. ScrollBar_Ve

### ScrollBars

Use these constants with the
 [ExpressionEdit.ScrollBars](expressionedit-scrollbars.html)
 property.

- ScrollBar_Both 
 –(Value: 1) Shows the horizontal and vertical scrollbars.
- ScrollBar_Horizontal 
 –(Value: 2) Shows only the horizontal scrollbar.
- ScrollBar_None 
 –(Value: 0) Does not show the horizontal or vertical scrollbars.
- ScrollBar_Vertical 
 –(Value: 3) Shows only the vertical scrollbar.

#### See Also

[ExpressionEdit.ScrollBars](expressionedit-scrollbars.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedpropertyobjects-addpropertyobject.html language=enus -->
## TOPIC 05513: SelectedPropertyObjects.AddPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedpropertyobjects-addpropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedpropertyobjects-addpropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedPropertyObjects.AddPropertyObject( val) Purpose Adds a property object to the collection. Parameters val As PropertyObject [In] Specifies the property object to add. See Also SelectedPropertyObjects.Clear

### SelectedPropertyObjects.AddPropertyObject

#### Syntax

[SelectedPropertyObjects](selectedpropertyobjects.html).AddPropertyObject( val)

#### Purpose

Adds a property object to the collection.

#### Parameters

val
 As
 
 [PropertyObject](../tsapiref/propertyobject.html)

[In] Specifies the property object to add.

#### See Also

[SelectedPropertyObjects.Clear](selectedpropertyobjects-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedpropertyobjects-addpropertyobjects.html language=enus -->
## TOPIC 05514: SelectedPropertyObjects.AddPropertyObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedpropertyobjects-addpropertyobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedpropertyobjects-addpropertyobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedPropertyObjects.AddPropertyObjects( val) Purpose Adds an array of property objects to the collection. Parameters val As Object Array [In] Specifies the property objects to add. See Also SelectedPropertyObjects.Clear

### SelectedPropertyObjects.AddPropertyObjects

#### Syntax

[SelectedPropertyObjects](selectedpropertyobjects.html).AddPropertyObjects( val)

#### Purpose

Adds an array of property objects to the collection.

#### Parameters

val
 As
 [Object Array](data-types-for-teststand-user-interface.html)

[In] Specifies the property objects to add.

#### See Also

[SelectedPropertyObjects.Clear](selectedpropertyobjects-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedpropertyobjects-beginupdate.html language=enus -->
## TOPIC 05515: SelectedPropertyObjects.BeginUpdate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedpropertyobjects-beginupdate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedpropertyobjects-beginupdate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedPropertyObjects.BeginUpdate Purpose Call this method before you make multiple changes to the SelectedPropertyObjects collection. When you finish changing the collection, call the SelectedPropertyObjects.EndUpdate method to update the TestStand User Interface (UI) Controls according to

### SelectedPropertyObjects.BeginUpdate

#### Syntax

[SelectedPropertyObjects](selectedpropertyobjects.html).BeginUpdate

#### Purpose

Call this method before you make multiple changes to the SelectedPropertyObjects collection. When you finish changing the collection, call the
 [SelectedPropertyObjects.EndUpdate](selectedpropertyobjects-endupdate.html)
 method to update the TestStand User Interface (UI) Controls according to the changes.

#### Remarks

Use this method to minimize redrawing in the TestStand UI Controls when you programmatically change the selection.

#### See Also

[SelectedPropertyObjects.EndUpdate](selectedpropertyobjects-endupdate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedpropertyobjects-clear.html language=enus -->
## TOPIC 05516: SelectedPropertyObjects.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedpropertyobjects-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedpropertyobjects-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedPropertyObjects.Clear Purpose Removes all items from the collection. See Also SelectedPropertyObjects.AddPropertyObject SelectedPropertyObjects.AddPropertyObjects

### SelectedPropertyObjects.Clear

#### Syntax

[SelectedPropertyObjects](selectedpropertyobjects.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[SelectedPropertyObjects.AddPropertyObject](selectedpropertyobjects-addpropertyobject.html)

[SelectedPropertyObjects.AddPropertyObjects](selectedpropertyobjects-addpropertyobjects.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedpropertyobjects-count.html language=enus -->
## TOPIC 05517: SelectedPropertyObjects.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedpropertyobjects-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedpropertyobjects-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedPropertyObjects.Count Data Type Long Purpose Returns the number of items in the collection.

### SelectedPropertyObjects.Count

#### Syntax

[SelectedPropertyObjects](selectedpropertyobjects.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedpropertyobjects-endupdate.html language=enus -->
## TOPIC 05518: SelectedPropertyObjects.EndUpdate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedpropertyobjects-endupdate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedpropertyobjects-endupdate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedPropertyObjects.EndUpdate Purpose Updates the TestStand User Interface Controls according to the SelectedPropertyObjects collection changes you make after you call the SelectedPropertyObjects.BeginUpdate method. See Also SelectedPropertyObjects.BeginUpdate

### SelectedPropertyObjects.EndUpdate

#### Syntax

[SelectedPropertyObjects](selectedpropertyobjects.html).EndUpdate

#### Purpose

Updates the TestStand User Interface Controls according to the SelectedPropertyObjects collection changes you make after you call the
 [SelectedPropertyObjects.BeginUpdate](selectedpropertyobjects-beginupdate.html)
 method.

#### See Also

[SelectedPropertyObjects.BeginUpdate](selectedpropertyobjects-beginupdate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedpropertyobjects-item.html language=enus -->
## TOPIC 05519: SelectedPropertyObjects.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedpropertyobjects-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedpropertyobjects-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedPropertyObjects.Item( itemIndex) Data Type PropertyObject Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies a zero-based index of the item to retrieve. See Also PropertyObject SelectedPropertyObjects.Count

### SelectedPropertyObjects.Item

#### Syntax

[SelectedPropertyObjects](selectedpropertyobjects.html).Item( itemIndex)

#### Data Type

[PropertyObject](../tsapiref/propertyobject.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies a zero-based index of the item to retrieve.

#### See Also

[PropertyObject](../tsapiref/propertyobject.html)

[SelectedPropertyObjects.Count](selectedpropertyobjects-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedpropertyobjects.html language=enus -->
## TOPIC 05520: SelectedPropertyObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedpropertyobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedpropertyobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of selected property objects. Controls connected to the SequenceFileView Manager and ExecutionView Manager controls, such as the VariablesView , automatically update the collection while active. You can obtain a reference to the collection from the SequenceFileViewMgr.SelectedPropertyOb

### SelectedPropertyObjects

A collection of selected property objects. Controls connected to the
 [SequenceFileView Manager](sequencefileviewmgr.html)
 and
 [ExecutionView Manager](executionviewmgr.html)
 controls, such as the
 [VariablesView](variablesview.html)
 , automatically update the collection while active. You can obtain a reference to the collection from the
 [SequenceFileViewMgr.SelectedPropertyObjects](sequencefileviewmgr-selectedpropertyobjects.html)
 and
 [ExecutionViewMgr.SelectedPropertyObjects](executionviewmgr-selectedpropertyobjects.html)
 properties.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| AddPropertyObject |
| --- |
| AddPropertyObjects |
| BeginUpdate |
| Clear |
| EndUpdate |

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.SelectedPropertyObjects](executionviewmgr-selectedpropertyobjects.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.SelectedPropertyObjects](sequencefileviewmgr-selectedpropertyobjects.html)

[VariablesView](variablesview.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsequences-addsequence.html language=enus -->
## TOPIC 05521: SelectedSequences.AddSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsequences-addsequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsequences-addsequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSequences.AddSequence( val) Purpose Adds a sequence to the SelectedSequences collection. Parameters val As Sequence [In] Specifies the sequence to add. See Also SelectedSequences.AddSequences SelectedSequences.Clear

### SelectedSequences.AddSequence

#### Syntax

[SelectedSequences](selectedsequences.html).AddSequence( val)

#### Purpose

Adds a sequence to the SelectedSequences collection.

#### Parameters

val
 As
 
 [Sequence](../tsapiref/sequence.html)

[In] Specifies the sequence to add.

#### See Also

[SelectedSequences.AddSequences](selectedsequences-addsequences.html)

[SelectedSequences.Clear](selectedsequences-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsequences-addsequences.html language=enus -->
## TOPIC 05522: SelectedSequences.AddSequences

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsequences-addsequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsequences-addsequences.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSequences.AddSequences( val) Purpose Adds an array of sequences to the SelectedSequences collection. Parameters val As Object Array [In] Specifies the array of sequences to add. See Also SelectedSequences.AddSequence SelectedSequences.Clear

### SelectedSequences.AddSequences

#### Syntax

[SelectedSequences](selectedsequences.html).AddSequences( val)

#### Purpose

Adds an array of sequences to the SelectedSequences collection.

#### Parameters

val
 As
 [Object Array](data-types-for-teststand-user-interface.html)

[In] Specifies the array of sequences to add.

#### See Also

[SelectedSequences.AddSequence](selectedsequences-addsequence.html)

[SelectedSequences.Clear](selectedsequences-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsequences-beginupdate.html language=enus -->
## TOPIC 05523: SelectedSequences.BeginUpdate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsequences-beginupdate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsequences-beginupdate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSequences.BeginUpdate Purpose Call this method before making multiple changes to the SelectedSequences collection. When you finish changing the collection, call the SelectedSequences.EndUpdate method to update the TestStand User Interface (UI) Controls according to the changes. Remark

### SelectedSequences.BeginUpdate

#### Syntax

[SelectedSequences](selectedsequences.html).BeginUpdate

#### Purpose

Call this method before making multiple changes to the SelectedSequences collection. When you finish changing the collection, call the
 [SelectedSequences.EndUpdate](selectedsequences-endupdate.html)
 method to update the TestStand User Interface (UI) Controls according to the changes.

#### Remarks

Use this method to minimize redrawing in the TestStand UI Controls when you programmatically change the selection.

#### See Also

[SelectedSequences.EndUpdate](selectedsequences-endupdate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsequences-clear.html language=enus -->
## TOPIC 05524: SelectedSequences.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsequences-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsequences-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSequences.Clear Purpose Removes all items from the collection. See Also SelectedSequences.AddSequence SelectedSequences.AddSequences

### SelectedSequences.Clear

#### Syntax

[SelectedSequences](selectedsequences.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[SelectedSequences.AddSequence](selectedsequences-addsequence.html)

[SelectedSequences.AddSequences](selectedsequences-addsequences.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsequences-count.html language=enus -->
## TOPIC 05525: SelectedSequences.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsequences-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsequences-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSequences.Count Data Type Long Purpose Returns the number of items in the collection.

### SelectedSequences.Count

#### Syntax

[SelectedSequences](selectedsequences.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsequences-endupdate.html language=enus -->
## TOPIC 05526: SelectedSequences.EndUpdate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsequences-endupdate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsequences-endupdate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSequences.EndUpdate Purpose Updates the user interface according to all changes to the SelectedSequences collection you make after a previous call to the SelectedSequences.BeginUpdate method. See Also SelectedSequences.BeginUpdate

### SelectedSequences.EndUpdate

#### Syntax

[SelectedSequences](selectedsequences.html).EndUpdate

#### Purpose

Updates the user interface according to all changes to the SelectedSequences collection you make after a previous call to the
 [SelectedSequences.BeginUpdate](selectedsequences-beginupdate.html)
 method.

#### See Also

[SelectedSequences.BeginUpdate](selectedsequences-beginupdate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsequences-item.html language=enus -->
## TOPIC 05527: SelectedSequences.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsequences-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsequences-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSequences.Item( itemIndex) Data Type Sequence The sequence at the specified index in the collection. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also Sequence Select

### SelectedSequences.Item

#### Syntax

[SelectedSequences](selectedsequences.html).Item( itemIndex)

#### Data Type

[Sequence](../tsapiref/sequence.html)

The sequence at the specified index in the collection.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[Sequence](../tsapiref/sequence.html)

[SelectedSequences.Count](selectedsequences-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsequences.html language=enus -->
## TOPIC 05528: SelectedSequences

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsequences.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of selected sequences. You can obtain a reference to the collection from the SequenceFileViewMgr.SelectedSequences property. Properties Count (Read Only) Item (Read Only) Methods AddSequence AddSequences BeginUpdate Clear EndUpdate See Also SequenceFileViewMgr.SelectedSequences

### SelectedSequences

A collection of selected sequences. You can obtain a reference to the collection from the
 [SequenceFileViewMgr.SelectedSequences](sequencefileviewmgr-selectedsequences.html)
 property.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| AddSequence |
| --- |
| AddSequences |
| BeginUpdate |
| Clear |
| EndUpdate |

#### See Also

[SequenceFileViewMgr.SelectedSequences](sequencefileviewmgr-selectedsequences.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-addstep.html language=enus -->
## TOPIC 05529: SelectedSteps.AddStep

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-addstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-addstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.AddStep( val) Purpose Adds a step to the collection. Parameters val As Step [In] Specifies the step to add. See Also SelectedSteps.AddStepIndex SelectedSteps.AddSteps SelectedSteps.Clear

### SelectedSteps.AddStep

#### Syntax

[SelectedSteps](selectedsteps.html).AddStep( val)

#### Purpose

Adds a step to the collection.

#### Parameters

val
 As
 
 [Step](../tsapiref/step.html)

[In] Specifies the step to add.

#### See Also

[SelectedSteps.AddStepIndex](selectedsteps-addstepindex.html)

[SelectedSteps.AddSteps](selectedsteps-addsteps.html)

[SelectedSteps.Clear](selectedsteps-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-addstepindex.html language=enus -->
## TOPIC 05530: SelectedSteps.AddStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-addstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-addstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.AddStepIndex( stepIndex) Purpose Adds a step to the collection. Remarks When the SequenceFileViewMgr.StepGroupMode property is StepGroupMode_AllGroups , call the SelectedSteps.AddStep method instead of this method. Parameters stepIndex As Long [In] Specifies the index in the cur

### SelectedSteps.AddStepIndex

#### Syntax

[SelectedSteps](selectedsteps.html).AddStepIndex( stepIndex)

#### Purpose

Adds a step to the collection.

#### Remarks

When the
 [SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)
 property is
 StepGroupMode_AllGroups
 , call the
 [SelectedSteps.AddStep](selectedsteps-addstep.html)
 method instead of this method.

#### Parameters

stepIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index in the current step group of the step to add.

#### See Also

[SelectedSteps.AddStep](selectedsteps-addstep.html)

[SelectedSteps.EndSelected](selectedsteps-endselected.html)

[SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)

[SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-addsteps.html language=enus -->
## TOPIC 05531: SelectedSteps.AddSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-addsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-addsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.AddSteps( val) Purpose Adds an array of steps to the collection. Parameters val As Object Array [In] Specifies the steps to add. See Also SelectedSteps.AddStepIndex SelectedSteps.AddSteps SelectedSteps.Clear

### SelectedSteps.AddSteps

#### Syntax

[SelectedSteps](selectedsteps.html).AddSteps( val)

#### Purpose

Adds an array of steps to the collection.

#### Parameters

val
 As
 [Object Array](data-types-for-teststand-user-interface.html)

[In] Specifies the steps to add.

#### See Also

[SelectedSteps.AddStepIndex](selectedsteps-addstepindex.html)

[SelectedSteps.AddSteps](selectedsteps-addsteps.html)

[SelectedSteps.Clear](selectedsteps-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-beginupdate.html language=enus -->
## TOPIC 05532: SelectedSteps.BeginUpdate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-beginupdate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-beginupdate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.BeginUpdate Purpose Call this method before making multiple changes to the SelectedSteps collection. When you finish changing the collection, call the SelectedSteps.EndUpdate method to update the TestStand User Interface (UI) Controls according to the changes. Remarks Use this m

### SelectedSteps.BeginUpdate

#### Syntax

[SelectedSteps](selectedsteps.html).BeginUpdate

#### Purpose

Call this method before making multiple changes to the SelectedSteps collection. When you finish changing the collection, call the
 [SelectedSteps.EndUpdate](selectedsteps-endupdate.html)
 method to update the TestStand User Interface (UI) Controls according to the changes.

#### Remarks

Use this method to minimize redrawing in the TestStand UI Controls when you programmatically change the selection.

#### See Also

[SelectedSteps.EndUpdate](selectedsteps-endupdate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-clear.html language=enus -->
## TOPIC 05533: SelectedSteps.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.Clear Purpose Removes all items from the collection. See Also SelectedSteps.AddStep SelectedSteps.AddStepIndex SelectedSteps.AddSteps SelectedSteps.EndSelected

### SelectedSteps.Clear

#### Syntax

[SelectedSteps](selectedsteps.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[SelectedSteps.AddStep](selectedsteps-addstep.html)

[SelectedSteps.AddStepIndex](selectedsteps-addstepindex.html)

[SelectedSteps.AddSteps](selectedsteps-addsteps.html)

[SelectedSteps.EndSelected](selectedsteps-endselected.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-count.html language=enus -->
## TOPIC 05534: SelectedSteps.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.Count Data Type Long Purpose Returns the number of items in the collection.

### SelectedSteps.Count

#### Syntax

[SelectedSteps](selectedsteps.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-endselected.html language=enus -->
## TOPIC 05535: SelectedSteps.EndSelected

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-endselected.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-endselected.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.EndSelected Data Type Boolean Purpose Specifies whether the End step is selected.

### SelectedSteps.EndSelected

#### Syntax

[SelectedSteps](selectedsteps.html).EndSelected

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the End step is selected.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-endupdate.html language=enus -->
## TOPIC 05536: SelectedSteps.EndUpdate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-endupdate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-endupdate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.EndUpdate Purpose Updates the user interface according to all changes to the SelectedSteps collection you made after the previous call to the SelectedSteps.BeginUpdate method. See Also SelectedSteps.BeginUpdate

### SelectedSteps.EndUpdate

#### Syntax

[SelectedSteps](selectedsteps.html).EndUpdate

#### Purpose

Updates the user interface according to all changes to the SelectedSteps collection you made after the previous call to the
 [SelectedSteps.BeginUpdate](selectedsteps-beginupdate.html)
 method.

#### See Also

[SelectedSteps.BeginUpdate](selectedsteps-beginupdate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-getstepgroup.html language=enus -->
## TOPIC 05537: SelectedSteps.GetStepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-getstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-getstepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.GetStepGroup( nthSelectedStep) Return Value StepGroups Use the following constants with this data type: StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step

### SelectedSteps.GetStepGroup

#### Syntax

[SelectedSteps](selectedsteps.html).GetStepGroup( nthSelectedStep)

#### Return Value

[StepGroups](../tsapiref/stepgroups.html)

Use the following constants with this data type:

- StepGroup_Cleanup 
 –(Value: 2) Specifies the Cleanup step group.
- StepGroup_Main 
 –(Value: 1) Specifies the Main step group.
- StepGroup_Setup 
 –(Value: 0) Specifies the Setup step group.

#### Purpose

Returns the step group of the specified step in the collection.

#### Parameters

nthSelectedStep
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of a step in the collection.

#### See Also

[SelectedSteps.GetStepIndex](selectedsteps-getstepindex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-getstepindex.html language=enus -->
## TOPIC 05538: SelectedSteps.GetStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-getstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-getstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.GetStepIndex( nthSelectedStep) Return Value Long The step index of the step in the collection. Purpose Retrieves the step index within a step group of a selected step. Parameters nthSelectedStep As Long [In] Specifies the index of a step in the collection. See Also SelectedSteps

### SelectedSteps.GetStepIndex

#### Syntax

[SelectedSteps](selectedsteps.html).GetStepIndex( nthSelectedStep)

#### Return Value

[Long](data-types-for-teststand-user-interface.html)

The step index of the step in the collection.

#### Purpose

Retrieves the step index within a step group of a selected step.

#### Parameters

nthSelectedStep
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of a step in the collection.

#### See Also

[SelectedSteps.EndSelected](selectedsteps-endselected.html)

[SelectedSteps.GetStepGroup](selectedsteps-getstepgroup.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-item.html language=enus -->
## TOPIC 05539: SelectedSteps.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.Item( itemIndex) Data Type Step The step at the specified index in the collection. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also Step SelectedSteps.Count

### SelectedSteps.Item

#### Syntax

[SelectedSteps](selectedsteps.html).Item( itemIndex)

#### Data Type

[Step](../tsapiref/step.html)

The step at the specified index in the collection.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[Step](../tsapiref/step.html)

[SelectedSteps.Count](selectedsteps-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps-selectionflags.html language=enus -->
## TOPIC 05540: SelectedSteps.SelectionFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps-selectionflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps-selectionflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedSteps.SelectionFlags Data Type Long Purpose When the SequenceFileViewMgr.StepGroupMode property is StepGroupMode_AllGroups , this property indicates whether the selection includes the step group start and end markers. The property also indicates whether each step group is expanded or

### SelectedSteps.SelectionFlags

#### Syntax

[SelectedSteps](selectedsteps.html).SelectionFlags

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

When the
 [SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)
 property is
 StepGroupMode_AllGroups
 , this property indicates whether the selection includes the step group start and end markers. The property also indicates whether each step group is expanded or collapsed. The value of this property is a bitwise-OR combination of the
 [SelectionFlags](selectionflags.html)
 constants.

#### See Also

[SelectionFlags](selectionflags.html)

[SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectedsteps.html language=enus -->
## TOPIC 05541: SelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of selected steps. You can obtain a reference to the collection from the SequenceFileViewMgr.SelectedSteps and ExecutionViewMgr.SelectedSteps properties. Properties Count (Read Only) EndSelected Item (Read Only) SelectionFlags Methods AddStep AddStepIndex AddSteps BeginUpdate Clear EndU

### SelectedSteps

A collection of selected steps. You can obtain a reference to the collection from the
 [SequenceFileViewMgr.SelectedSteps](sequencefileviewmgr-selectedsteps.html)
 and
 [ExecutionViewMgr.SelectedSteps](executionviewmgr-selectedsteps.html)
 properties.

#### Properties

| Count (Read Only) |
| --- |
| EndSelected |
| Item (Read Only) |
| SelectionFlags |

#### Methods

| AddStep |
| --- |
| AddStepIndex |
| AddSteps |
| BeginUpdate |
| Clear |
| EndUpdate |
| GetStepGroup |
| GetStepIndex |

#### See Also

[ExecutionViewMgr.SelectedSteps](executionviewmgr-selectedsteps.html)

[SequenceFileViewMgr.SelectedSteps](sequencefileviewmgr-selectedsteps.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/selectionflags.html language=enus -->
## TOPIC 05542: SelectionFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/selectionflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/selectionflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to select step group start or end markers and to expand or collapse step groups. These constants apply only when the application displays more than one step group at a time. You cannot select step group start and end markers when steps are selected. You cannot select steps and st

### SelectionFlags

Use these constants to select step group start or end markers and to expand or collapse step groups. These constants apply only when the application displays more than one step group at a time.

You cannot select step group start and end markers when steps are selected. You cannot select steps and step group end markers in collapsed step groups.

- SelectionFlag_CleanupCollapsed 
 –(Value: 256) Collapses the Cleanup step group.
- SelectionFlag_CleanupEndSelected 
 –(Value: 32) Selects the end marker for the Cleanup step group.
- SelectionFlag_CleanupStartSelected 
 –(Value: 4) Selects the start marker for the Cleanup step group.
- SelectionFlag_MainCollapsed 
 –(Value: 128) Collapses the Main step group.
- SelectionFlag_MainEndSelected 
 –(Value: 16) Selects the end marker for the Main step group.
- SelectionFlag_MainStartSelected 
 –(Value: 2) Selects the start marker for the Main step group.
- SelectionFlag_NoFlags 
 –(Value: 0) No collapsed step group and no selected step group markers.
- SelectionFlag_SetupCollapsed 
 –(Value: 64) Collapses the Setup step group.
- SelectionFlag_SetupEndSelected 
 –(Value: 8) Selects the end marker for the Setup step group.
- SelectionFlag_SetupStartSelected 
 –(Value: 1) Selects the start marker for the Setup step group.

#### See Also

[ExecutionViewMgr.SelectedSteps](executionviewmgr-selectedsteps.html)

[ExecutionViewMgr.StepGroupMode](executionviewmgr-stepgroupmode.html)

[SelectedSteps.SelectionFlags](selectedsteps-selectionflags.html)

[SequenceFileViewMgr.SelectedSteps](sequencefileviewmgr-selectedsteps.html)

[SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)

Parent topic:

Support UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqlistconnectioncolumns.html language=enus -->
## TOPIC 05543: SeqListConnectionColumns

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqlistconnectioncolumns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqlistconnectioncolumns.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the column type you can use with the column parameter of the SequenceListConnection.SetColumnVisible and SequenceListConnection.GetColumnVisible methods. SeqListConnectionColumn_Comments –(Value: 1) Specifies the column that contains the comment of the sequence. SeqListConn

### SeqListConnectionColumns

These constants represent the column type you can use with the
 column
 parameter of the
 [SequenceListConnection.SetColumnVisible](sequencelistconnection-setcolumnvisible.html)
 and
 [SequenceListConnection.GetColumnVisible](sequencelistconnection-getcolumnvisible.html)
 methods.

- SeqListConnectionColumn_Comments 
 –(Value: 1) Specifies the column that contains the comment of the sequence.
- SeqListConnectionColumn_Label 
 –(Value: 0) Specifies the column that contains the name of the sequence.
- SeqListConnectionColumn_Requirements 
 –(Value: 2) Specifies the column that contains the requirements of the sequence.

#### See Also

[SequenceListConnection.GetColumnVisible](sequencelistconnection-getcolumnvisible.html)

[SequenceListConnection.SetColumnVisible](sequencelistconnection-setcolumnvisible.html)

Parent topic:

Support UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefiledisplayreasons.html language=enus -->
## TOPIC 05544: SequenceFileDisplayReasons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefiledisplayreasons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefiledisplayreasons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These values are passed as a parameter to the ApplicationMgr.DisplaySequenceFile event to provide the reason for why the event was generated. SequenceFileDisplayReason_GotoLocation –(Value: 3) The event was generated because of a request to display a location that resides in the file. SequenceFileDi

### SequenceFileDisplayReasons

These values are passed as a parameter to the
 [ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)
 event to provide the reason for why the event was generated.

- SequenceFileDisplayReason_GotoLocation 
 –(Value: 3) The event was generated because of a request to display a location that resides in the file.
- SequenceFileDisplayReason_NewSequenceFile 
 –(Value: 2) The event was generated because a new sequence file was created.
- SequenceFileDisplayReason_OpenSequenceFile 
 –(Value: 1) The event was generated because the sequence file was opened.
- SequenceFileDisplayReason_UIMessage 
 –(Value: 0) The event was generated because the TestStand Engine sent the
 UIMsg_OpenWindows 
 message for the sequence file.

#### See Also

[ApplicationMgr.DisplaySequenceFile](applicationmgr-displaysequencefile.html)

[UIMessageCodes](../tsapiref/uimessagecodes.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnection-showcommentintip.html language=enus -->
## TOPIC 05545: SequenceFileListConnection.ShowCommentInTip

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnection-showcommentintip.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnection-showcommentintip.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileListConnection.ShowCommentInTip Data Type Boolean Purpose Specifies whether the item tooltip includes the sequence file comment in controls you connect to display the list of loaded sequence files.

### SequenceFileListConnection.ShowCommentInTip

#### Syntax

[SequenceFileListConnection](sequencefilelistconnection.html).ShowCommentInTip

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the item tooltip includes the sequence file comment in controls you connect to display the list of loaded sequence files.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnection-showfullpath.html language=enus -->
## TOPIC 05546: SequenceFileListConnection.ShowFullPath

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnection-showfullpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnection-showfullpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileListConnection.ShowFullPath Data Type Boolean Purpose When this property is True , the connected control displays the full path for all sequence files. Otherwise, the connected control displays only filenames.

### SequenceFileListConnection.ShowFullPath

#### Syntax

[SequenceFileListConnection](sequencefilelistconnection.html).ShowFullPath

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the connected control displays the full path for all sequence files. Otherwise, the connected control displays only filenames.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnection.html language=enus -->
## TOPIC 05547: SequenceFileListConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from a SequenceFileView Manager control to a control that displays a list of open sequence files. Use the connected control to select a sequence file to open in the SequenceFileView Manager control from the list of sequence files. Properties ShowCommentInTip ShowFullPath See

### SequenceFileListConnection

Represents a connection from a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control to a control that displays a list of open sequence files. Use the connected control to select a sequence file to open in the SequenceFileView Manager control from the list of sequence files.

#### Properties

| ShowCommentInTip |
| --- |
| ShowFullPath |

#### See Also

[SequenceFileListConnections](sequencefilelistconnections.html)

[SequenceFileView Manager](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnections-add.html language=enus -->
## TOPIC 05548: SequenceFileListConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileListConnections.Add( uiObj) Return Value SequenceFileListConnection New SequenceFileListConnection. Purpose Creates and adds a new SequenceFileListConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also SequenceFileLis

### SequenceFileListConnections.Add

#### Syntax

[SequenceFileListConnections](sequencefilelistconnections.html).Add( uiObj)

#### Return Value

[SequenceFileListConnection](sequencefilelistconnection.html)

New SequenceFileListConnection.

#### Purpose

Creates and adds a new SequenceFileListConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[SequenceFileListConnections.Remove](sequencefilelistconnections-remove.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnections-clear.html language=enus -->
## TOPIC 05549: SequenceFileListConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileListConnections.Clear Purpose Removes all items from the collection. See Also SequenceFileListConnections.Remove

### SequenceFileListConnections.Clear

#### Syntax

[SequenceFileListConnections](sequencefilelistconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[SequenceFileListConnections.Remove](sequencefilelistconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnections-count.html language=enus -->
## TOPIC 05550: SequenceFileListConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileListConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### SequenceFileListConnections.Count

#### Syntax

[SequenceFileListConnections](sequencefilelistconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnections-fromcontrol.html language=enus -->
## TOPIC 05551: SequenceFileListConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileListConnections.FromControl( uiObj) Return Value SequenceFileListConnection SequenceFileListConnection connected to the uiObj parameter. When no SequenceFileListConnection exists for this control, this method returns NULL . Purpose Returns the SequenceFileListConnection connected

### SequenceFileListConnections.FromControl

#### Syntax

[SequenceFileListConnections](sequencefilelistconnections.html).FromControl( uiObj)

#### Return Value

[SequenceFileListConnection](sequencefilelistconnection.html)

SequenceFileListConnection connected to the
 uiObj
 parameter. When no SequenceFileListConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the SequenceFileListConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnections-item.html language=enus -->
## TOPIC 05552: SequenceFileListConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileListConnections.Item( itemIndex) Data Type SequenceFileListConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also Seque

### SequenceFileListConnections.Item

#### Syntax

[SequenceFileListConnections](sequencefilelistconnections.html).Item( itemIndex)

#### Data Type

[SequenceFileListConnection](sequencefilelistconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[SequenceFileListConnection](sequencefilelistconnection.html)

[SequenceFileListConnections.Count](sequencefilelistconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnections-remove.html language=enus -->
## TOPIC 05553: SequenceFileListConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileListConnections.Remove( uiObj) Return Value Boolean Returns True when the SequenceFileListConnection is removed. Returns False when the SequenceFileListConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] S

### SequenceFileListConnections.Remove

#### Syntax

[SequenceFileListConnections](sequencefilelistconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the SequenceFileListConnection is removed. Returns
 False
 when the SequenceFileListConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[SequenceFileListConnections.Add](sequencefilelistconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefilelistconnections.html language=enus -->
## TOPIC 05554: SequenceFileListConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefilelistconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefilelistconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of SequenceFileListConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also SequenceFileListConnection

### SequenceFileListConnections

A collection of
 [SequenceFileListConnection](sequencefilelistconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[SequenceFileListConnection](sequencefilelistconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefiles-count.html language=enus -->
## TOPIC 05555: SequenceFiles.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefiles-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefiles-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFiles.Count Data Type Long Purpose Returns the number of items in the collection.

### SequenceFiles.Count

#### Syntax

[SequenceFiles](sequencefiles.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefiles-item.html language=enus -->
## TOPIC 05556: SequenceFiles.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefiles-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefiles-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFiles.Item( fileIndex) Data Type SequenceFile Purpose Returns a reference to an item at the specified index in the collection. Parameters fileIndex As Variant [In] Specifies the zero-based index of the item to retrieve. Use a non-negative number less than the value of the SequenceFile

### SequenceFiles.Item

#### Syntax

[SequenceFiles](sequencefiles.html).Item( fileIndex)

#### Data Type

[SequenceFile](../tsapiref/sequencefile.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

fileIndex
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to retrieve. Use a non-negative number less than the value of the
 [SequenceFiles.Count](sequencefiles-count.html)
 property. Alternatively, you can pass a string with the fully qualified path of the sequence file to retrieve from the collection.

#### See Also

[SequenceFile](../tsapiref/sequencefile.html)

[SequenceFiles.Count](sequencefiles-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefiles.html language=enus -->
## TOPIC 05557: SequenceFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read-only collection of sequence files. Use the ApplicationMgr.SequenceFiles property to obtain the collection of SequenceFile objects the Application Manager control opens. Properties Count (Read Only) Item (Read Only) See Also ApplicationMgr.SequenceFiles

### SequenceFiles

Read-only collection of sequence files. Use the
 [ApplicationMgr.SequenceFiles](applicationmgr-sequencefiles.html)
 property to obtain the collection of SequenceFile objects the Application Manager control opens.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[ApplicationMgr.SequenceFiles](applicationmgr-sequencefiles.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-applicationmgr.html language=enus -->
## TOPIC 05558: SequenceFileViewMgr.ApplicationMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-applicationmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-applicationmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ApplicationMgr Data Type Object Purpose Returns a reference to the Application Manager control of the application. The value is NULL when no Application Manager control exists within the process. See Also ApplicationMgr

### SequenceFileViewMgr.ApplicationMgr

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ApplicationMgr

#### Data Type

[Object](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a reference to the Application Manager control of the application. The value is
 NULL
 when no Application Manager control exists within the process.

#### See Also

[ApplicationMgr](applicationmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-buildeditargs.html language=enus -->
## TOPIC 05559: SequenceFileViewMgr.BuildEditArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-buildeditargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-buildeditargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.BuildEditArgs Return Value EditArgs Purpose Creates an EditArgs object according to the current selection settings of the SequenceFileView Manager control. Remarks Use this method to create an EditArgs object, which you can modify before you pass it as the optional paramet

### SequenceFileViewMgr.BuildEditArgs

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).BuildEditArgs

#### Return Value

[EditArgs](../tsapiref/editargs.html)

#### Purpose

Creates an EditArgs object according to the current selection settings of the SequenceFileView Manager control.

#### Remarks

Use this method to create an EditArgs object, which you can modify before you pass it as the optional parameter to a method that starts an execution.

#### See Also

[EditArgs](../tsapiref/editargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceFileViewMgr.LoopOnSelectedSteps](sequencefileviewmgr-looponselectedsteps.html)

[SequenceFileViewMgr.Run](sequencefileviewmgr-run.html)

[SequenceFileViewMgr.RunSelectedSteps](sequencefileviewmgr-runselectedsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-buildinteractiveargs.html language=enus -->
## TOPIC 05560: SequenceFileViewMgr.BuildInteractiveArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-buildinteractiveargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-buildinteractiveargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.BuildInteractiveArgs( createLoopArgs, [cancel]) Return Value InteractiveArgs A new InteractiveArgs object. Purpose Creates an InteractiveArgs object according to the current selection settings of the SequenceFileView Manager control. Remarks Use this method to create an In

### SequenceFileViewMgr.BuildInteractiveArgs

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).BuildInteractiveArgs( createLoopArgs, [cancel])

#### Return Value

[InteractiveArgs](../tsapiref/interactiveargs.html)

A new InteractiveArgs object.

#### Purpose

Creates an InteractiveArgs object according to the current selection settings of the SequenceFileView Manager control.

#### Remarks

Use this method to create an InteractiveArgs object, which you can modify before you pass it as the optional parameter to a method that starts an interactive execution.

#### Parameters

createLoopArgs
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] When this parameter is
 True
 , this property launches the
 [Loop on Selected Steps](../tsref/loop-on-selected-steps-dialog-box.html)
 dialog box to create the InteractiveArgs object for the
 [SequenceFileViewMgr.LoopOnSelectedSteps](sequencefileviewmgr-looponselectedsteps.html)
 method.

cancel
 As
 [Variant](data-types-for-teststand-user-interface.html)

[Out] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] If the Loop on Selected Steps dialog box is cancelled, the value of the parameter passed in is
 True
 .

#### See Also

[Loop on Selected Steps dialog box](../tsref/loop-on-selected-steps-dialog-box.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceFileViewMgr.LoopOnSelectedSteps](sequencefileviewmgr-looponselectedsteps.html)

[SequenceFileViewMgr.RunSelectedSteps](sequencefileviewmgr-runselectedsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-configurationentrypoints.html language=enus -->
## TOPIC 05561: SequenceFileViewMgr.ConfigurationEntryPoints

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-configurationentrypoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-configurationentrypoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConfigurationEntryPoints Data Type EntryPoints Purpose Returns the collection of Configuration entry points for the selected sequence file. Remarks This collection can change when the selected sequence file changes. See Also EntryPoints SequenceFileViewMgr.ConnectSequenceF

### SequenceFileViewMgr.ConfigurationEntryPoints

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConfigurationEntryPoints

#### Data Type

[EntryPoints](entrypoints.html)

#### Purpose

Returns the collection of Configuration entry points for the selected sequence file.

#### Remarks

This collection can change when the selected sequence file changes.

#### See Also

[EntryPoints](entrypoints.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

[SequenceFileViewMgr.ExecutionEntryPoints](sequencefileviewmgr-executionentrypoints.html)

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectcaption.html language=enus -->
## TOPIC 05562: SequenceFileViewMgr.ConnectCaption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectcaption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectcaption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectCaption( uiObj, captionSource, longName) Return Value CaptionConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existin

### SequenceFileViewMgr.ConnectCaption

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectCaption( uiObj, captionSource, longName)

#### Return Value

[CaptionConnection](captionconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a caption source in a SequenceFileView Manager control to a visible control or an element of a visible control. The connection automatically updates the visible control with text that describes an aspect of the current application state.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, call the
 [SequenceFileViewMgrConnections.Caption](sequencefileviewmgrconnections-caption.html)
 property to obtain the
 [CaptionConnections](captionconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the visible control or element of a visible control to which the caption source connects. Pass a
 [Label](label.html)
 ,
 [ExpressionEdit](expressionedit.html)
 , or
 [StatusBarPane](statusbarpane.html)
 .

captionSource
 As
 [CaptionSources](captionsources.html)

[In] Specifies the type of caption source to connect.

longName
 As
 [Boolean](data-types-for-teststand-user-interface.html)

For certain caption sources, this parameter specifies whether the connection displays a long or short version of the caption text. Refer to the
 [CaptionSources](captionsources.html)
 enumeration for more information about determining when this option affects a caption source and for more information about the difference between the long and short versions of the text.

#### See Also

[ApplicationMgr.ConnectCaption](applicationmgr-connectcaption.html)

[CaptionConnections](captionconnections.html)

[CaptionSources](captionsources.html)

[ExecutionViewMgr.ConnectCaption](executionviewmgr-connectcaption.html)

[ExpressionEdit](expressionedit.html)

[Label](label.html)

[SequenceFileViewMgr.GetCaptionText](sequencefileviewmgr-getcaptiontext.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgr.GetCaptionText](sequencefileviewmgr-getcaptiontext.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.Caption](sequencefileviewmgrconnections-caption.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectcommand.html language=enus -->
## TOPIC 05563: SequenceFileViewMgr.ConnectCommand

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectcommand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectcommand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectCommand( uiObj, cmdKind, index = 0, opts = 0) Return Value CommandConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the ex

### SequenceFileViewMgr.ConnectCommand

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectCommand( uiObj, cmdKind, index = 0, opts = 0)

#### Return Value

[CommandConnection](commandconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a command source in a SequenceFileView Manager control to a TestStand button or checkbox control. The connection automatically updates the enabled, visible, and caption properties of the button or checkbox according to the state of the current execution. Clicking the button or enabling the checkbox control executes the command.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, access the
 [SequenceFileViewMgrConnections.Command](sequencefileviewmgrconnections-command.html)
 property to obtain the
 [CommandConnections](commandconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the button or checkbox control to which the command connects.

cmdKind
 As
 [CommandKinds](commandkinds.html)

[In] Specifies the type of command to connect.

index
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] For
 [CommandKinds](commandkinds.html)
 that are sets, this parameter indexes the set to obtain a particular command.

This parameter has a default value of
 0
 .

opts
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the options for the CommandConnection. Refer to the
 [CommandConnectionOptions](commandconnectionoptions.html)
 constants for more information about options for the CommandConnection object.

This parameter has a default value of
 0
 .

#### See Also

[Button](button.html)

[CommandConnectionOptions](commandconnectionoptions.html)

[CommandConnections](commandconnections.html)

[CommandKinds](commandkinds.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgr.GetCommand](sequencefileviewmgr-getcommand.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.Command](sequencefileviewmgrconnections-command.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectimage.html language=enus -->
## TOPIC 05564: SequenceFileViewMgr.ConnectImage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectimage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectimage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectImage( uiObj, imageSource) Return Value ImageConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is

### SequenceFileViewMgr.ConnectImage

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectImage( uiObj, imageSource)

#### Return Value

[ImageConnection](imageconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects an image source in a SequenceFileView Manager control to a visible control or an element of a visible control. The connection automatically updates the visible control with an icon that describes an aspect of the current application state.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, access the
 [SequenceFileViewMgrConnections.Image](sequencefileviewmgrconnections-image.html)
 property to obtain the
 [ImageConnections](imageconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the visible control or element of a visible control to which the caption source connects. Pass a
 [StatusBarPane](statusbarpane.html)
 or
 [Button](button.html)
 .

imageSource
 As
 [ImageSources](imagesources.html)

[In] Specifies the type of image source to connect.

#### See Also

[Button](button.html)

[ExecutionViewMgr.ConnectImage](executionviewmgr-connectimage.html)

[ImageConnections](imageconnections.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgr.GetImageName](sequencefileviewmgr-getimagename.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.Image](sequencefileviewmgrconnections-image.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectinsertionpalette.html language=enus -->
## TOPIC 05565: SequenceFileViewMgr.ConnectInsertionPalette

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectinsertionpalette.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectinsertionpalette.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectInsertionPalette( uiObj) Return Value InsertionPaletteConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing conne

### SequenceFileViewMgr.ConnectInsertionPalette

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectInsertionPalette( uiObj)

#### Return Value

[InsertionPaletteConnection](insertionpaletteconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects an
 [InsertionPalette](insertionpalette.html)
 control to display the step type list and templates list and enables inserting sequences, steps, and variables into controls connected to the SequenceFileView Manager control, such as the
 [ListBox](listbox.html)
 ,
 [SequenceView](sequenceview.html)
 , or
 [VariablesView](variablesview.html)
 controls.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, access the
 [SequenceFileViewMgrConnections.InsertionPalettes](sequencefileviewmgrconnections-insertionpalet.html)
 property to obtain the
 [InsertionPaletteConnections](insertionpaletteconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the reference to an InsertionPalette control that displays the step type list and templates list.

#### See Also

[InsertionPalette](insertionpalette.html)

[InsertionPaletteConnections](insertionpaletteconnections.html)

[ListBox](listbox.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.InsertionPalettes](sequencefileviewmgrconnections-insertionpalet.html)

[SequenceView](sequenceview.html)

[VariablesView](variablesview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connections.html language=enus -->
## TOPIC 05566: SequenceFileViewMgr.Connections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.Connections Data Type SequenceFileViewMgrConnections Purpose Returns the connections of this control. See Also SequenceFileViewMgrConnections

### SequenceFileViewMgr.Connections

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).Connections

#### Data Type

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

#### Purpose

Returns the connections of this control.

#### See Also

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectsequencefilelist.html language=enus -->
## TOPIC 05567: SequenceFileViewMgr.ConnectSequenceFileList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectsequencefilelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectsequencefilelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectSequenceFileList( uiObj, fullPath) Return Value SequenceFileListConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the exis

### SequenceFileViewMgr.ConnectSequenceFileList

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectSequenceFileList( uiObj, fullPath)

#### Return Value

[SequenceFileListConnection](sequencefilelistconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a user interface control that displays the list of opened sequence files. The control can also select a sequence file to place into the SequenceFileView Manager control.

#### Remarks

You can connect a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , and
 [ListBox](listbox.html)
 to SequenceFileLists.

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, access the
 [SequenceFileViewMgrConnections.SequenceFileList](sequencefileviewmgrconnections-sequencefileli.html)
 property to obtain the
 [SequenceFileListConnections](sequencefilelistconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Use a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 to display the list of sequence files.

fullPath
 As
 [Boolean](data-types-for-teststand-user-interface.html)

When this parameter is
 True
 , TestStand displays the sequence files with full pathnames.

#### See Also

[ComboBox](combobox.html)

[ListBarPage](listbarpage.html)

[ListBox](listbox.html)

[SequenceFileListConnections](sequencefilelistconnections.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.SequenceFileList](sequencefileviewmgrconnections-sequencefileli.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectsequencelist.html language=enus -->
## TOPIC 05568: SequenceFileViewMgr.ConnectSequenceList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectsequencelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectsequencelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectSequenceList( uiObj) Return Value SequenceListConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is

### SequenceFileViewMgr.ConnectSequenceList

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectSequenceList( uiObj)

#### Return Value

[SequenceListConnection](sequencelistconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a user interface control that displays the list of sequences in the current sequence file. The control can also select a sequence to place into the SequenceFileView Manager control.

#### Remarks

You can connect the
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , and
 [ListBox](listbox.html)
 to SequenceFileLists.

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, access the
 [SequenceFileViewMgrConnections.SequenceList](sequencefileviewmgrconnections-sequencelist.html)
 property to obtain the
 [SequenceListConnections](sequencelistconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Use
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 to display the list of sequence files.

#### See Also

[ComboBox](combobox.html)

[ListBarPage](listbarpage.html)

[ListBox](listbox.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.SequenceList](sequencefileviewmgrconnections-sequencelist.html)

[SequenceListConnections](sequencelistconnections.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectsequenceview.html language=enus -->
## TOPIC 05569: SequenceFileViewMgr.ConnectSequenceView

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectsequenceview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectsequenceview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectSequenceView( uiObj) Return Value SequenceViewConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is

### SequenceFileViewMgr.ConnectSequenceView

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectSequenceView( uiObj)

#### Return Value

[SequenceViewConnection](sequenceviewconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a
 [SequenceView](sequenceview.html)
 control to display the current sequence of the SequenceFileView Manager control.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, access the
 [SequenceFileViewMgrConnections.SequenceView](sequencefileviewmgrconnections-sequenceview.html)
 property to obtain the
 [SequenceViewConnections](sequenceviewconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the reference to a SequenceView control that displays the current sequence and step group.

#### See Also

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.SequenceView](sequencefileviewmgrconnections-sequenceview.html)

[SequenceViewConnections](sequenceviewconnections.html)

[SequenceView](sequenceview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectstepgrouplist.html language=enus -->
## TOPIC 05570: SequenceFileViewMgr.ConnectStepGroupList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectstepgrouplist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectstepgrouplist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectStepGroupList( uiObj) Return Value StepGroupListConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection

### SequenceFileViewMgr.ConnectStepGroupList

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectStepGroupList( uiObj)

#### Return Value

[StepGroupListConnection](stepgrouplistconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a user interface control that selects the step group of the current sequence file to place into the SequenceFileView Manager control.

#### Remarks

You can connect a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , and
 [ListBox](listbox.html)
 as StepGroupLists.

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, access the
 [SequenceFileViewMgrConnections.StepGroupList](sequencefileviewmgrconnections-stepgrouplist.html)
 property to obtain the
 [StepGroupListConnections](stepgrouplistconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Use a
 [ComboBox](combobox.html)
 ,
 [ListBarPage](listbarpage.html)
 , or
 [ListBox](listbox.html)
 to display the list of step groups.

#### See Also

[ComboBox](combobox.html)

[ListBarPage](listbarpage.html)

[ListBox](listbox.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.StepGroupList](sequencefileviewmgrconnections-stepgrouplist.html)

[StepGroup](sequencefileviewmgr-stepgroup.html)

[StepGroupListConnections](stepgrouplistconnections.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-connectvariables.html language=enus -->
## TOPIC 05571: SequenceFileViewMgr.ConnectVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-connectvariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-connectvariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ConnectVariables( uiObj) Return Value VariablesConnection A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is retur

### SequenceFileViewMgr.ConnectVariables

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ConnectVariables( uiObj)

#### Return Value

[VariablesConnection](variablesconnection.html)

A reference to an object that represents the new connection. Discarding the reference does not affect the connection. When the object is already connected to this type of connection, the existing connection is returned.

#### Purpose

Connects a
 [VariablesView](variablesview.html)
 control to display the current sequence context of the SequenceFileView Manager control.

#### Remarks

To disconnect an existing connection, you must first obtain the
 [SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)
 object from the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property. Then, access the
 [SequenceFileViewMgrConnections.Variables](sequencefileviewmgrconnections-variables.html)
 property to obtain the
 [VariablesConnections](variablesconnections.html)
 collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the reference to a VariablesView control that displays the current sequence context.

#### See Also

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html)

[SequenceFileViewMgrConnections.Variables](sequencefileviewmgrconnections-variables.html)

[VariablesConnections](variablesconnections.html)

[VariablesView](variablesview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-executionentrypoints.html language=enus -->
## TOPIC 05572: SequenceFileViewMgr.ExecutionEntryPoints

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-executionentrypoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-executionentrypoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ExecutionEntryPoints Data Type EntryPoints Purpose Returns the set of Execution entry points the model sequence file for the selected sequence file defines. The collection includes only entry points that set the Sequence.ShowEntryPointForFileWindow property. Remarks This c

### SequenceFileViewMgr.ExecutionEntryPoints

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ExecutionEntryPoints

#### Data Type

[EntryPoints](entrypoints.html)

#### Purpose

Returns the set of Execution entry points the model sequence file for the selected sequence file defines. The collection includes only entry points that set the
 
 [Sequence.ShowEntryPointForFileWindow](../tsapiref/sequence-showentrypointforfilewindow.html)
 property.

#### Remarks

This collection can change when the selected sequence file changes.

#### See Also

[ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)

[EntryPoints](entrypoints.html)

[ExecutionViewMgr.ExecutionEntryPoints](executionviewmgr-executionentrypoints.html)

[Sequence.ShowEntryPointForFileWindow](../tsapiref/sequence-showentrypointforfilewindow.html)

[SequenceFileViewMgr.ConfigurationEntryPoints](sequencefileviewmgr-configurationentrypoints.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-getcaptiontext.html language=enus -->
## TOPIC 05573: SequenceFileViewMgr.GetCaptionText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-getcaptiontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-getcaptiontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.GetCaptionText( captionSource, longName, formatExpression = "") Return Value String The current text for the caption source you specify. Purpose Returns the current caption text for a caption source in a SequenceFileView Manager control. Parameters captionSource As Caption

### SequenceFileViewMgr.GetCaptionText

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).GetCaptionText( captionSource, longName, formatExpression = "")

#### Return Value

[String](data-types-for-teststand-user-interface.html)

The current text for the caption source you specify.

#### Purpose

Returns the current caption text for a caption source in a SequenceFileView Manager control.

#### Parameters

captionSource
 As
 [CaptionSources](captionsources.html)

[In] Specifies the type of caption source from which to obtain text.

longName
 As
 [Boolean](data-types-for-teststand-user-interface.html)

For certain caption sources, this parameter specifies whether to return a long or short version of the caption text. Refer to the
 [CaptionSources](captionsources.html)
 enumeration for more information about determining when this option affects the text and for more information about the difference between the long and short versions of the text.

formatExpression
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies a format expression to evaluate when generating the caption text. For the
 [CaptionSource_MacroExpression](captionsources.html)
 caption source, specify a format expression that evaluates to a string value that contains macros that specify other caption sources. For all other caption sources, specify an expression that evaluates to a string value that contains the characters
 %1
 . The method replaces the
 %1
 characters with the text from the caption source. Pass an empty string to use the default format string for the caption source.

This parameter has a default value of
 ""
 .

#### See Also

[ApplicationMgr.GetCaptionText](applicationmgr-getcaptiontext.html)

[CaptionSources](captionsources.html)

[ExecutionViewMgr.GetCaptionText](executionviewmgr-getcaptiontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-getcommand.html language=enus -->
## TOPIC 05574: SequenceFileViewMgr.GetCommand

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-getcommand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-getcommand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.GetCommand( cmdKind, index = 0) Return Value Command Purpose Creates a Command object. When applicable, the command operates on the items the SequenceFileView Manager control selects. Parameters cmdKind As CommandKinds [In] Specifies the type of Command object to create. i

### SequenceFileViewMgr.GetCommand

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).GetCommand( cmdKind, index = 0)

#### Return Value

[Command](command.html)

#### Purpose

Creates a Command object. When applicable, the command operates on the items the SequenceFileView Manager control selects.

#### Parameters

cmdKind
 As
 [CommandKinds](commandkinds.html)

[In] Specifies the type of Command object to create.

index
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Use this parameter on commands that are sets to specify which command in the set to return.

This parameter has a default value of
 0
 .

#### See Also

[ApplicationMgr.GetCommand](applicationmgr-getcommand.html)

[CommandKinds](commandkinds.html)

[ExecutionViewMgr.GetCommand](executionviewmgr-getcommand.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-getimagename.html language=enus -->
## TOPIC 05575: SequenceFileViewMgr.GetImageName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-getimagename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-getimagename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.GetImageName( imageSource) Return Value String The current image name for the image source you specify. Purpose Returns the current image name for an image source in a SequenceFileView Manager control. Use the Images.FindImage method to acquire a reference to the image. Pa

### SequenceFileViewMgr.GetImageName

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).GetImageName( imageSource)

#### Return Value

[String](data-types-for-teststand-user-interface.html)

The current image name for the image source you specify.

#### Purpose

Returns the current image name for an image source in a SequenceFileView Manager control. Use the
 
 [Images.FindImage](../tsapiref/images-findimage.html)
 method to acquire a reference to the image.

#### Parameters

imageSource
 As
 [ImageSources](imagesources.html)

[In] Specifies the type of image source from which to obtain an image name.

#### See Also

[ApplicationMgr.GetImageName](applicationmgr-getimagename.html)

[Engine.Images](../tsapiref/engine-images.html)

[ExecutionViewMgr.GetImageName](executionviewmgr-getimagename.html)

[Images.FindImage](../tsapiref/images-findimage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-looponselectedsteps.html language=enus -->
## TOPIC 05576: SequenceFileViewMgr.LoopOnSelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-looponselectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-looponselectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.LoopOnSelectedSteps( [interactiveArgsVal], [editArgsVal]) Return Value Execution A new execution. Purpose Starts an execution that loops on the currently selected steps. Parameters interactiveArgsVal As Variant [In] [ Optional ] Specifies a custom InteractiveArgs object us

### SequenceFileViewMgr.LoopOnSelectedSteps

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).LoopOnSelectedSteps( [interactiveArgsVal], [editArgsVal])

#### Return Value

[Execution](../tsapiref/execution.html)

A new execution.

#### Purpose

Starts an execution that loops on the currently selected steps.

#### Parameters

interactiveArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies a custom
 
 [InteractiveArgs](../tsapiref/interactiveargs.html)
 object using this parameter. When you do not pass a custom
 InteractiveArgs
 object, the SequenceFileView Manager control builds an
 InteractiveArgs
 object according to the current selections.

editArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies a custom
 
 [EditArgs](../tsapiref/editargs.html)
 object using this parameter. When you do not pass a custom
 EditArgs
 object, the SequenceFileView Manager control builds an
 EditArgs
 object according to the current selections.

#### See Also

[CommandKind_LoopOnSelectedSteps](commandkinds.html)

[SequenceFileViewMgr.BuildEditArgs](sequencefileviewmgr-buildeditargs.html)

[SequenceFileViewMgr.BuildInteractiveArgs](sequencefileviewmgr-buildinteractiveargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceFileViewMgr.RunSelectedSteps](sequencefileviewmgr-runselectedsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-neweditcontext.html language=enus -->
## TOPIC 05577: SequenceFileViewMgr.NewEditContext

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-neweditcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-neweditcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.NewEditContext Return Value SequenceContext Purpose Returns a SequenceContext that has a Step property that has only properties common to all currently selected steps. Use the SequenceContext.GetMultipleValues method to determine whether the values of the Step subpropertie

### SequenceFileViewMgr.NewEditContext

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).NewEditContext

#### Return Value

[SequenceContext](../tsapiref/sequencecontext.html)

#### Purpose

Returns a
 SequenceContext
 that has a
 Step
 property that has only properties common to all currently selected steps. Use the
 
 [SequenceContext.GetMultipleValues](../tsapiref/sequencecontext-getmultiplevalues.html)
 method to determine whether the values of the
 Step
 subproperties are common across all the currently selected steps.

#### See Also

[Engine.NewEditContext](../tsapiref/engine-neweditcontext.html)

[ExecutionViewMgr.NewEditContext](executionviewmgr-neweditcontext.html)

[SequenceContext.GetMultipleValues](../tsapiref/sequencecontext-getmultiplevalues.html)

[SequenceContext.SetMultipleValues](../tsapiref/sequencecontext-setmultiplevalues.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-propertyobjectselectionch.html language=enus -->
## TOPIC 05578: SequenceFileViewMgr.PropertyObjectSelectionChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-propertyobjectselectionch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-propertyobjectselectionch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_PropertyObjectSelectionChanged Applies To SequenceFileViewMgr Purpose Occurs when the selected property objects change. For example, this event is generated when you change the selection in a VariablesView control that connects to the SequenceFileView Manager control or when you p

### SequenceFileViewMgr.PropertyObjectSelectionChanged

#### Syntax

ControlName_PropertyObjectSelectionChanged

#### Applies To

[SequenceFileViewMgr](sequencefileviewmgr.html)

#### Purpose

Occurs when the selected property objects change. For example, this event is generated when you change the selection in a VariablesView control that connects to the SequenceFileView Manager control or when you programmatically change the contents of the
 [SelectedPropertyObjects](sequencefileviewmgr-selectedpropertyobjects.html)
 collection.

#### See Also

[ExecutionViewMgr.PropertyObjectSelectionChanged](executionviewmgr-propertyobjectselectionchang.html)

[SequenceFileViewMgr.SelectedPropertyObjects](sequencefileviewmgr-selectedpropertyobjects.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-refresh.html language=enus -->
## TOPIC 05579: SequenceFileViewMgr.Refresh

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-refresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-refresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.Refresh Purpose Refreshes all connected controls. Remarks Typically, you do not call this method unless you have changed the state of the execution directly using the TestStand API. Call this method so these types of changes are reflected in the connected controls. See Als

### SequenceFileViewMgr.Refresh

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).Refresh

#### Purpose

Refreshes all connected controls.

#### Remarks

Typically, you do not call this method unless you have changed the state of the execution directly using the TestStand API. Call this method so these types of changes are reflected in the connected controls.

#### See Also

[ApplicationMgr.Refresh](applicationmgr-refresh.html)

[ApplicationMgr.RefreshAllViewMgrs](applicationmgr-refreshallviewmgrs.html)

[ExecutionViewMgr.Refresh](executionviewmgr-refresh.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-refreshstep.html language=enus -->
## TOPIC 05580: SequenceFileViewMgr.RefreshStep

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-refreshstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-refreshstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.RefreshStep( stepIndex) Purpose Refreshes a step in the current step group in a connected SequenceView control. Remarks Typically, you do not call this method unless you have changed the state of the step directly using the TestStand API. Call this method so these types of

### SequenceFileViewMgr.RefreshStep

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).RefreshStep( stepIndex)

#### Purpose

Refreshes a step in the current step group in a connected
 [SequenceView](sequenceview.html)
 control.

#### Remarks

Typically, you do not call this method unless you have changed the state of the step directly using the TestStand API. Call this method so these types of changes are reflected in the connected SequenceView control.

When you set the
 [SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)
 property to
 StepGroupMode_AllGroups
 , call the
 [SequenceFileViewMgr.RefreshStepEx](sequencefileviewmgr-refreshstepex.html)
 method instead of this method to specify the step group in which the step resides.

#### Parameters

stepIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the step to refresh. Passing
 -1
 refreshes all steps in the connected SequenceView control.

#### See Also

[SequenceFileViewMgr.RefreshStepEx](sequencefileviewmgr-refreshstepex.html)

[SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)

[SequenceView](sequenceview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-refreshstepex.html language=enus -->
## TOPIC 05581: SequenceFileViewMgr.RefreshStepEx

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-refreshstepex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-refreshstepex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.RefreshStepEx( group, stepIndex) Purpose Refreshes a step in all connected SequenceView controls. Remarks Typically, you do not call this method unless you change the state of the step directly using the TestStand API. Parameters group As StepGroups [In] Specifies a partic

### SequenceFileViewMgr.RefreshStepEx

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).RefreshStepEx( group, stepIndex)

#### Purpose

Refreshes a step in all connected
 [SequenceView](sequenceview.html)
 controls.

#### Remarks

Typically, you do not call this method unless you change the state of the step directly using the TestStand API.

#### Parameters

group
 As
 
 [StepGroups](../tsapiref/stepgroups.html)

[In] Specifies a particular step group.

stepIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index in the step group of the step to refresh. Pass
 -1
 to refresh all the steps in all groups in the connected SequenceView control.

#### See Also

[SequenceFileViewMgr.RefreshStep](sequencefileviewmgr-refreshstep.html)

[SequenceView](sequenceview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-refreshwindow.html language=enus -->
## TOPIC 05582: SequenceFileViewMgr.RefreshWindow

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-refreshwindow.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-refreshwindow.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_RefreshWindow Applies To SequenceFileViewMgr Purpose Occurs when TestStand sends a UIMsg_RefreshWindows message that requires a refresh of the selected sequence file. See Also ApplicationMgr.RefreshWindows ExecutionViewMgr.RefreshWindow SequenceFileViewMgr.Refresh UIMsg_RefreshWin

### SequenceFileViewMgr.RefreshWindow

#### Syntax

ControlName_RefreshWindow

#### Applies To

[SequenceFileViewMgr](sequencefileviewmgr.html)

#### Purpose

Occurs when TestStand sends a
 UIMsg_RefreshWindows
 message that requires a refresh of the selected sequence file.

#### See Also

[ApplicationMgr.RefreshWindows](applicationmgr-refreshwindows.html)

[ExecutionViewMgr.RefreshWindow](executionviewmgr-refreshwindow.html)

[SequenceFileViewMgr.Refresh](sequencefileviewmgr-refresh.html)

[UIMsg_RefreshWindows](../tsapiref/uimessagecodes.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-replacesequencefileonclos.html language=enus -->
## TOPIC 05583: SequenceFileViewMgr.ReplaceSequenceFileOnClose

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-replacesequencefileonclos.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-replacesequencefileonclos.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.ReplaceSequenceFileOnClose Data Type Boolean Purpose Specifies whether the SequenceFileView Manager control selects another sequence file when the currently selected sequence file closes. See Also ApplicationMgr.CloseSequenceFile SequenceFileViewMgr.SequenceFile

### SequenceFileViewMgr.ReplaceSequenceFileOnClose

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).ReplaceSequenceFileOnClose

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the SequenceFileView Manager control selects another sequence file when the currently selected sequence file closes.

#### See Also

[ApplicationMgr.CloseSequenceFile](applicationmgr-closesequencefile.html)

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-run.html language=enus -->
## TOPIC 05584: SequenceFileViewMgr.Run

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-run.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-run.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.Run( [editArgsVal]) Return Value Execution A new execution. Purpose Runs the current sequence without using a process model entry point. Parameters editArgsVal As Variant [In] [ Optional ] Specifies a custom EditArgs object using this parameter. When you do not pass a cust

### SequenceFileViewMgr.Run

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).Run( [editArgsVal])

#### Return Value

[Execution](../tsapiref/execution.html)

A new execution.

#### Purpose

Runs the current sequence without using a process model entry point.

#### Parameters

editArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies a custom
 
 [EditArgs](../tsapiref/editargs.html)
 object using this parameter. When you do not pass a custom
 EditArgs
 object, the SequenceFileView Manager control builds an
 EditArgs
 object according to the current selections.

#### See Also

[CommandKind_RunCurrentSequence](commandkinds.html)

[EditArgs](../tsapiref/editargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceFileViewMgr.BuildEditArgs](sequencefileviewmgr-buildeditargs.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-runselectedsteps.html language=enus -->
## TOPIC 05585: SequenceFileViewMgr.RunSelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-runselectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-runselectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.RunSelectedSteps( [interactiveArgsVal], [editArgsVal]) Return Value Execution A new execution. Purpose Starts an execution to run the currently selected steps. Parameters interactiveArgsVal As Variant [In] [ Optional ] Specifies a custom InteractiveArgs object using this p

### SequenceFileViewMgr.RunSelectedSteps

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).RunSelectedSteps( [interactiveArgsVal], [editArgsVal])

#### Return Value

[Execution](../tsapiref/execution.html)

A new execution.

#### Purpose

Starts an execution to run the currently selected steps.

#### Parameters

interactiveArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies a custom
 
 [InteractiveArgs](../tsapiref/interactiveargs.html)
 object using this parameter. When you do not pass a custom
 InteractiveArgs
 object, the SequenceFileView Manager control builds an
 InteractiveArgs
 object according to the current selections.

editArgsVal
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] [
 [Optional](/csh?context=ts_tsuiref_optional_parameters)
 ] Specifies a custom
 
 [EditArgs](../tsapiref/editargs.html)
 object using this parameter. When you do not pass a custom
 EditArgs
 object, the SequenceFileView Manager control builds an
 EditArgs
 object according to the current selections.

#### See Also

[CommandKind_RunSelectedSteps](commandkinds.html)

[EditArgs](../tsapiref/editargs.html)

[InteractiveArgs](../tsapiref/interactiveargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceFileViewMgr.BuildEditArgs](sequencefileviewmgr-buildeditargs.html)

[SequenceFileViewMgr.BuildInteractiveArgs](sequencefileviewmgr-buildinteractiveargs.html)

[SequenceFileViewMgr.LoopOnSelectedSteps](sequencefileviewmgr-looponselectedsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-selectedpropertyobjects.html language=enus -->
## TOPIC 05586: SequenceFileViewMgr.SelectedPropertyObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-selectedpropertyobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-selectedpropertyobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.SelectedPropertyObjects Data Type SelectedPropertyObjects Purpose Returns a collection of selected property objects. Remarks Use this collection to obtain the selected property objects or change the selected property objects for the selected file. TestStand User Interface

### SequenceFileViewMgr.SelectedPropertyObjects

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).SelectedPropertyObjects

#### Data Type

[SelectedPropertyObjects](selectedpropertyobjects.html)

#### Purpose

Returns a collection of selected property objects.

#### Remarks

Use this collection to obtain the selected property objects or change the selected property objects for the selected file. TestStand User Interface Controls connected to a SequenceFileView Manager control, such as the
 [VariablesView](variablesview.html)
 control, automatically set this property when you select variables and properties.

#### See Also

[SelectedPropertyObjects](selectedpropertyobjects.html)

[SequenceFileViewMgr.PropertyObjectSelectionChanged](sequencefileviewmgr-propertyobjectselectionch.html)

[VariablesView](variablesview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-selectedsequences.html language=enus -->
## TOPIC 05587: SequenceFileViewMgr.SelectedSequences

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-selectedsequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-selectedsequences.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.SelectedSequences Data Type SelectedSequences Purpose Returns a collection of selected sequences. Remarks Use this collection to obtain the selected sequences or to change the selected sequences for the selected file. Use the SequenceFileViewMgr.ConnectSequenceList method

### SequenceFileViewMgr.SelectedSequences

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).SelectedSequences

#### Data Type

[SelectedSequences](selectedsequences.html)

#### Purpose

Returns a collection of selected sequences.

#### Remarks

Use this collection to obtain the selected sequences or to change the selected sequences for the selected file. Use the
 [SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)
 method to connect a control that displays sequences and specifies the selected sequence. Use the
 [SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)
 property to determine the sequence a connected
 [SequenceView](sequenceview.html)
 control displays.

TestStand User Interface Controls connected to a SequenceFileView Manager control, such as the
 [ListBox](listbox.html)
 control, automatically set this property when you select sequences.

#### See Also

[ListBox](listbox.html)

[SelectedSequences](selectedsequences.html)

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

[SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)

[SequenceView](sequenceview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-selectedsteps.html language=enus -->
## TOPIC 05588: SequenceFileViewMgr.SelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-selectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-selectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.SelectedSteps Data Type SelectedSteps Purpose Returns a collection of selected steps. Remarks Use this collection to obtain the selected steps or to change the selected steps for the selected file. TestStand User Interface Controls connected to a SequenceFileView Manager c

### SequenceFileViewMgr.SelectedSteps

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).SelectedSteps

#### Data Type

[SelectedSteps](selectedsteps.html)

#### Purpose

Returns a collection of selected steps.

#### Remarks

Use this collection to obtain the selected steps or to change the selected steps for the selected file. TestStand User Interface Controls connected to a SequenceFileView Manager control, such as the
 [SequenceView](sequenceview.html)
 control, automatically set this property when you select steps.

#### See Also

[SelectedSteps](selectedsteps.html)

[SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)

[SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)

[SequenceView](sequenceview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-selectionchanged.html language=enus -->
## TOPIC 05589: SequenceFileViewMgr.SelectionChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-selectionchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-selectionchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SelectionChanged Applies To SequenceFileViewMgr Purpose Occurs when the selected steps are changed. See Also SequenceFileViewMgr.SelectedSteps

### SequenceFileViewMgr.SelectionChanged

#### Syntax

ControlName_SelectionChanged

#### Applies To

[SequenceFileViewMgr](sequencefileviewmgr.html)

#### Purpose

Occurs when the selected steps are changed.

#### See Also

[SequenceFileViewMgr.SelectedSteps](sequencefileviewmgr-selectedsteps.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-sequence.html language=enus -->
## TOPIC 05590: SequenceFileViewMgr.Sequence

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-sequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.Sequence Data Type Sequence Purpose Specifies the current sequence. Remarks Use the SequenceFileViewMgr.ConnectSequenceList method to connect a control that displays sequences and specifies the current sequence. The current sequence is the sequence the SequenceFileView Man

### SequenceFileViewMgr.Sequence

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).Sequence

#### Data Type

[Sequence](../tsapiref/sequence.html)

#### Purpose

Specifies the current sequence.

#### Remarks

Use the
 [SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)
 method to connect a control that displays sequences and specifies the current sequence.

The current sequence is the sequence the SequenceFileView Manager control displays in a connected
 [SequenceView](sequenceview.html)
 control. Use the
 [SequenceFileViewMgr.SelectedSequences](sequencefileviewmgr-selectedsequences.html)
 property to determine the list of sequence a connected control selects.

Use the
 [SequenceFileViewMgr.SetSequenceAndGroup](sequencefileviewmgr-setsequenceandgroup.html)
 method to set the current sequence when you must also set the
 [SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)
 property.

#### See Also

[Sequence](../tsapiref/sequence.html)

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

[SequenceFileViewMgr.SelectedSequences](sequencefileviewmgr-selectedsequences.html)

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

[SequenceFileViewMgr.SetSequenceAndGroup](sequencefileviewmgr-setsequenceandgroup.html)

[SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)

[SequenceView](sequenceview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-sequencechanged.html language=enus -->
## TOPIC 05591: SequenceFileViewMgr.SequenceChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-sequencechanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-sequencechanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SequenceChanged( newSequence) Applies To SequenceFileViewMgr Purpose Occurs when the current sequence changes. Parameters newSequence As Sequence [In] Specifies the new sequence. See Also SequenceFileViewMgr.Sequence

### SequenceFileViewMgr.SequenceChanged

#### Syntax

ControlName_SequenceChanged( newSequence)

#### Applies To

[SequenceFileViewMgr](sequencefileviewmgr.html)

#### Purpose

Occurs when the current sequence changes.

#### Parameters

newSequence
 As
 
 [Sequence](../tsapiref/sequence.html)

[In] Specifies the new sequence.

#### See Also

[SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-sequencefile.html language=enus -->
## TOPIC 05592: SequenceFileViewMgr.SequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-sequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-sequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.SequenceFile Data Type SequenceFile Purpose Specifies the selected sequence file the controls connected to the SequenceFileView Manager control display. Remarks Use the SequenceFileViewMgr.ConnectSequenceFileList method to connect a control that displays open sequence file

### SequenceFileViewMgr.SequenceFile

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).SequenceFile

#### Data Type

[SequenceFile](../tsapiref/sequencefile.html)

#### Purpose

Specifies the selected sequence file the controls connected to the SequenceFileView Manager control display.

#### Remarks

Use the
 [SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)
 method to connect a control that displays open sequence files and specifies the selected sequence file.

#### See Also

[SequenceFile](../tsapiref/sequencefile.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

[SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)

[SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-sequencefilechanged.html language=enus -->
## TOPIC 05593: SequenceFileViewMgr.SequenceFileChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-sequencefilechanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-sequencefilechanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SequenceFileChanged( newFile) Applies To SequenceFileViewMgr Purpose Occurs when the selected sequence file changes. Parameters newFile As SequenceFile [In] Specifies the new sequence file. See Also SequenceFileViewMgr.SequenceFile

### SequenceFileViewMgr.SequenceFileChanged

#### Syntax

ControlName_SequenceFileChanged( newFile)

#### Applies To

[SequenceFileViewMgr](sequencefileviewmgr.html)

#### Purpose

Occurs when the selected sequence file changes.

#### Parameters

newFile
 As
 
 [SequenceFile](../tsapiref/sequencefile.html)

[In] Specifies the new sequence file.

#### See Also

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-sequenceselectionchanged.html language=enus -->
## TOPIC 05594: SequenceFileViewMgr.SequenceSelectionChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-sequenceselectionchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-sequenceselectionchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_SequenceSelectionChanged Applies To SequenceFileViewMgr Purpose Occurs when the selected sequences change. See Also SequenceFileViewMgr.SelectedSequences SequenceFileViewMgr.Sequence

### SequenceFileViewMgr.SequenceSelectionChanged

#### Syntax

ControlName_SequenceSelectionChanged

#### Applies To

[SequenceFileViewMgr](sequencefileviewmgr.html)

#### Purpose

Occurs when the selected sequences change.

#### See Also

[SequenceFileViewMgr.SelectedSequences](sequencefileviewmgr-selectedsequences.html)

[SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-setsequenceandgroup.html language=enus -->
## TOPIC 05595: SequenceFileViewMgr.SetSequenceAndGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-setsequenceandgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-setsequenceandgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.SetSequenceAndGroup( newSequence, newGroup) Purpose Sets the current sequence and step group at the same time. Remarks This is more efficient than setting the SequenceFileViewMgr.Sequence property before setting the SequenceFileViewMgr.StepGroup property. Parameters newSeq

### SequenceFileViewMgr.SetSequenceAndGroup

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).SetSequenceAndGroup( newSequence, newGroup)

#### Purpose

Sets the current sequence and step group at the same time.

#### Remarks

This is more efficient than setting the
 [SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)
 property before setting the
 [SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)
 property.

#### Parameters

newSequence
 As
 
 [Sequence](../tsapiref/sequence.html)

[In] Specifies the sequence to set in the SequenceFileView Manager control.

newGroup
 As
 
 [StepGroups](../tsapiref/stepgroups.html)

[In] Specifies the step group value to set in the SequenceFileView Manager control.

#### See Also

[SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)

[SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-stepgroup.html language=enus -->
## TOPIC 05596: SequenceFileViewMgr.StepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-stepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.StepGroup Data Type StepGroups Use the following constants with this data type: StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step group. Purpose Spe

### SequenceFileViewMgr.StepGroup

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).StepGroup

#### Data Type

[StepGroups](../tsapiref/stepgroups.html)

Use the following constants with this data type:

- StepGroup_Cleanup 
 –(Value: 2) Specifies the Cleanup step group.
- StepGroup_Main 
 –(Value: 1) Specifies the Main step group.
- StepGroup_Setup 
 –(Value: 0) Specifies the Setup step group.

#### Purpose

Specifies the selected step group.

#### Remarks

A
 [SequenceView](sequenceview.html)
 control displays the selected step group or all groups depending on the value of the
 [SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)
 property. Use the
 [SequenceFileViewMgr.SetSequenceAndGroup](sequencefileviewmgr-setsequenceandgroup.html)
 method to set the step group when you must also set the
 [SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)
 property.

#### See Also

[SequenceFileViewMgr.Sequence](sequencefileviewmgr-sequence.html)

[SequenceFileViewMgr.SequenceFile](sequencefileviewmgr-sequencefile.html)

[SequenceFileViewMgr.SetSequenceAndGroup](sequencefileviewmgr-setsequenceandgroup.html)

[SequenceFileViewMgr.StepGroupMode](sequencefileviewmgr-stepgroupmode.html)

[SequenceView](sequenceview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-stepgroupchanged.html language=enus -->
## TOPIC 05597: SequenceFileViewMgr.StepGroupChanged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-stepgroupchanged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-stepgroupchanged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_StepGroupChanged( newGroup) Applies To SequenceFileViewMgr Purpose Occurs when the selected step group changes. Parameters newGroup As StepGroups [In] Specifies the new value of the step group property. See Also SequenceFileViewMgr.StepGroup

### SequenceFileViewMgr.StepGroupChanged

#### Syntax

ControlName_StepGroupChanged( newGroup)

#### Applies To

[SequenceFileViewMgr](sequencefileviewmgr.html)

#### Purpose

Occurs when the selected step group changes.

#### Parameters

newGroup
 As
 
 [StepGroups](../tsapiref/stepgroups.html)

[In] Specifies the new value of the step group property.

#### See Also

[SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-stepgroupmode.html language=enus -->
## TOPIC 05598: SequenceFileViewMgr.StepGroupMode

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-stepgroupmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-stepgroupmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.StepGroupMode Data Type StepGroupModes Use the following constants with this data type: StepGroupMode_AllGroups –(Value: 2) Displays the Setup, Main, and Cleanup step groups. StepGroupMode_OneGroup –(Value: 1) Displays only one step group. Purpose For connected controls th

### SequenceFileViewMgr.StepGroupMode

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).StepGroupMode

#### Data Type

[StepGroupModes](stepgroupmodes.html)

Use the following constants with this data type:

- StepGroupMode_AllGroups 
 –(Value: 2) Displays the Setup, Main, and Cleanup step groups.
- StepGroupMode_OneGroup 
 –(Value: 1) Displays only one step group.

#### Purpose

For connected controls that display steps, this property specifies whether to display all steps in the Cleanup, Main, and Setup groups or to display only the steps in the current step group.

#### Remarks

When you set this property to
 StepGroupMode_AllGroups
 , ensure that the application does not use the value of the
 [SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)
 property.

#### See Also

[SequenceFileViewMgr.StepGroup](sequencefileviewmgr-stepgroup.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-undostack.html language=enus -->
## TOPIC 05599: SequenceFileViewMgr.UndoStack

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-undostack.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-undostack.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.UndoStack Data Type UndoStack Purpose Returns the UndoStack for the currently selected SequenceFile . Remarks TestStand creates the UndoStack object and automatically adds items to this UndoStack for edits to the currently selected sequence file the TestStand User Interfac

### SequenceFileViewMgr.UndoStack

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).UndoStack

#### Data Type

[UndoStack](../tsapiref/undostack.html)

#### Purpose

Returns the UndoStack for the currently selected
 
 [SequenceFile](../tsapiref/sequencefile.html)
 .

#### Remarks

TestStand creates the UndoStack object and automatically adds items to this UndoStack for edits to the currently selected sequence file the TestStand User Interface Controls make.

#### See Also

[ApplicationMgr.UndoStack](applicationmgr-undostack.html)

[SequenceFile](../tsapiref/sequencefile.html)

[UndoStack](../tsapiref/undostack.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr-userdata.html language=enus -->
## TOPIC 05600: SequenceFileViewMgr.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgr.UserData Data Type Variant Purpose Stores data associated with this control. Remarks Stored data is cleared during the shutdown process.

### SequenceFileViewMgr.UserData

#### Syntax

[SequenceFileViewMgr](sequencefileviewmgr.html).UserData

#### Data Type

[Variant](data-types-for-teststand-user-interface.html)

#### Purpose

Stores data associated with this control.

#### Remarks

Stored data is cleared during the shutdown process.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgr.html language=enus -->
## TOPIC 05601: SequenceFileViewMgr

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A SequenceFileView Manager control performs the following tasks to manage how other visible TestStand User Interface (UI) Controls view and interact with a selected sequence file: Designates a sequence file as the selected sequence file. Tracks which sequence, step groups, and steps are selected in

### SequenceFileViewMgr

A SequenceFileView Manager control performs the following tasks to manage how other visible TestStand User Interface (UI) Controls view and interact with a selected sequence file:

- Designates a sequence file as the selected sequence file.
- Tracks which sequence, step groups, and steps are selected in the selected file and tracks the expansion of the step groups.
- Displays aspects of the selected file in the visible TestStand UI Controls to which it connects.
- Enables visible TestStand UI Controls to which it connects to change the selected file, sequence, step group, and steps.
- Provides methods for executing the selected sequence file.

An application must have one SequenceFileView Manager control for each location, such as a window, form, or panel, in which you display a sequence file or let the user select a current sequence file.

#### Properties

| ApplicationMgr (Read Only) |
| --- |
| ConfigurationEntryPoints (Read Only) |
| Connections (Read Only) |
| ExecutionEntryPoints (Read Only) |
| ReplaceSequenceFileOnClose |
| SelectedPropertyObjects (Read Only) |
| SelectedSequences (Read Only) |
| SelectedSteps (Read Only) |
| Sequence |
| SequenceFile |
| StepGroup |
| StepGroupMode |
| UndoStack (Read Only) |
| UserData |

#### Methods

| BuildEditArgs |
| --- |
| BuildInteractiveArgs |
| ConnectCaption |
| ConnectCommand |
| ConnectImage |
| ConnectInsertionPalette |
| ConnectSequenceFileList |
| ConnectSequenceList |
| ConnectSequenceView |
| ConnectStepGroupList |
| ConnectVariables |
| GetCaptionText |
| GetCommand |
| GetImageName |
| LoopOnSelectedSteps |
| NewEditContext |
| Refresh |
| RefreshStep |
| RefreshStepEx |
| Run |
| RunSelectedSteps |
| SetSequenceAndGroup |

#### Events

| PropertyObjectSelectionChanged |
| --- |
| RefreshWindow |
| SelectionChanged |
| SequenceChanged |
| SequenceFileChanged |
| SequenceSelectionChanged |
| StepGroupChanged |

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-caption.html language=enus -->
## TOPIC 05602: SequenceFileViewMgrConnections.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.Caption Data Type CaptionConnections Purpose Collection of CaptionConnection objects. See Also CaptionConnection CaptionConnections SequenceFileViewMgr.ConnectCaption

### SequenceFileViewMgrConnections.Caption

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).Caption

#### Data Type

[CaptionConnections](captionconnections.html)

#### Purpose

Collection of
 [CaptionConnection](captionconnection.html)
 objects.

#### See Also

[CaptionConnection](captionconnection.html)

[CaptionConnections](captionconnections.html)

[SequenceFileViewMgr.ConnectCaption](sequencefileviewmgr-connectcaption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-command.html language=enus -->
## TOPIC 05603: SequenceFileViewMgrConnections.Command

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-command.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-command.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.Command Data Type CommandConnections Purpose Collection of CommandConnection objects. See Also CommandConnection CommandConnections SequenceFileViewMgr.ConnectCommand

### SequenceFileViewMgrConnections.Command

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).Command

#### Data Type

[CommandConnections](commandconnections.html)

#### Purpose

Collection of
 [CommandConnection](commandconnection.html)
 objects.

#### See Also

[CommandConnection](commandconnection.html)

[CommandConnections](commandconnections.html)

[SequenceFileViewMgr.ConnectCommand](sequencefileviewmgr-connectcommand.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-image.html language=enus -->
## TOPIC 05604: SequenceFileViewMgrConnections.Image

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-image.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-image.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.Image Data Type ImageConnections Purpose Collection of ImageConnection objects. See Also ImageConnection ImageConnections SequenceFileViewMgr.ConnectImage

### SequenceFileViewMgrConnections.Image

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).Image

#### Data Type

[ImageConnections](imageconnections.html)

#### Purpose

Collection of
 [ImageConnection](imageconnection.html)
 objects.

#### See Also

[ImageConnection](imageconnection.html)

[ImageConnections](imageconnections.html)

[SequenceFileViewMgr.ConnectImage](sequencefileviewmgr-connectimage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-insertionpalet.html language=enus -->
## TOPIC 05605: SequenceFileViewMgrConnections.InsertionPalettes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-insertionpalet.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-insertionpalet.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.InsertionPalettes Data Type InsertionPaletteConnections Purpose Collection of InsertionPaletteConnection objects. See Also InsertionPaletteConnection InsertionPaletteConnections SequenceFileViewMgr.ConnectInsertionPalette

### SequenceFileViewMgrConnections.InsertionPalettes

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).InsertionPalettes

#### Data Type

[InsertionPaletteConnections](insertionpaletteconnections.html)

#### Purpose

Collection of
 [InsertionPaletteConnection](insertionpaletteconnection.html)
 objects.

#### See Also

[InsertionPaletteConnection](insertionpaletteconnection.html)

[InsertionPaletteConnections](insertionpaletteconnections.html)

[SequenceFileViewMgr.ConnectInsertionPalette](sequencefileviewmgr-connectinsertionpalette.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-sequencefileli.html language=enus -->
## TOPIC 05606: SequenceFileViewMgrConnections.SequenceFileList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-sequencefileli.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-sequencefileli.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.SequenceFileList Data Type SequenceFileListConnections Purpose Collection of SequenceFileListConnection objects. See Also SequenceFileListConnection SequenceFileListConnections SequenceFileViewMgr.ConnectSequenceFileList

### SequenceFileViewMgrConnections.SequenceFileList

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).SequenceFileList

#### Data Type

[SequenceFileListConnections](sequencefilelistconnections.html)

#### Purpose

Collection of
 [SequenceFileListConnection](sequencefilelistconnection.html)
 objects.

#### See Also

[SequenceFileListConnection](sequencefilelistconnection.html)

[SequenceFileListConnections](sequencefilelistconnections.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-sequencelist.html language=enus -->
## TOPIC 05607: SequenceFileViewMgrConnections.SequenceList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-sequencelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-sequencelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.SequenceList Data Type SequenceListConnections Purpose Collection of SequenceListConnection objects. See Also SequenceFileViewMgr.ConnectSequenceList SequenceListConnection SequenceListConnections

### SequenceFileViewMgrConnections.SequenceList

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).SequenceList

#### Data Type

[SequenceListConnections](sequencelistconnections.html)

#### Purpose

Collection of
 [SequenceListConnection](sequencelistconnection.html)
 objects.

#### See Also

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

[SequenceListConnection](sequencelistconnection.html)

[SequenceListConnections](sequencelistconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-sequenceview.html language=enus -->
## TOPIC 05608: SequenceFileViewMgrConnections.SequenceView

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-sequenceview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-sequenceview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.SequenceView Data Type SequenceViewConnections Purpose Collection of SequenceViewConnection objects. See Also SequenceFileViewMgr.ConnectSequenceView SequenceViewConnection SequenceViewConnections

### SequenceFileViewMgrConnections.SequenceView

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).SequenceView

#### Data Type

[SequenceViewConnections](sequenceviewconnections.html)

#### Purpose

Collection of
 [SequenceViewConnection](sequenceviewconnection.html)
 objects.

#### See Also

[SequenceFileViewMgr.ConnectSequenceView](sequencefileviewmgr-connectsequenceview.html)

[SequenceViewConnection](sequenceviewconnection.html)

[SequenceViewConnections](sequenceviewconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-stepgrouplist.html language=enus -->
## TOPIC 05609: SequenceFileViewMgrConnections.StepGroupList

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-stepgrouplist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-stepgrouplist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.StepGroupList Data Type StepGroupListConnections Purpose Collection of StepGroupListConnection objects. See Also SequenceFileViewMgr.ConnectStepGroupList StepGroupListConnection StepGroupListConnections

### SequenceFileViewMgrConnections.StepGroupList

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).StepGroupList

#### Data Type

[StepGroupListConnections](stepgrouplistconnections.html)

#### Purpose

Collection of
 [StepGroupListConnection](stepgrouplistconnection.html)
 objects.

#### See Also

[SequenceFileViewMgr.ConnectStepGroupList](sequencefileviewmgr-connectstepgrouplist.html)

[StepGroupListConnection](stepgrouplistconnection.html)

[StepGroupListConnections](stepgrouplistconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections-variables.html language=enus -->
## TOPIC 05610: SequenceFileViewMgrConnections.Variables

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections-variables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections-variables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFileViewMgrConnections.Variables Data Type VariablesConnections Purpose Collection of VariablesConnection objects. See Also SequenceFileViewMgr.ConnectVariables VariablesConnection VariablesConnections

### SequenceFileViewMgrConnections.Variables

#### Syntax

[SequenceFileViewMgrConnections](sequencefileviewmgrconnections.html).Variables

#### Data Type

[VariablesConnections](variablesconnections.html)

#### Purpose

Collection of
 [VariablesConnection](variablesconnection.html)
 objects.

#### See Also

[SequenceFileViewMgr.ConnectVariables](sequencefileviewmgr-connectvariables.html)

[VariablesConnection](variablesconnection.html)

[VariablesConnections](variablesconnections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencefileviewmgrconnections.html language=enus -->
## TOPIC 05611: SequenceFileViewMgrConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencefileviewmgrconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencefileviewmgrconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the connections for the SequenceFileView Manager control. Properties Caption (Read Only) Command (Read Only) Image (Read Only) InsertionPalettes (Read Only) SequenceFileList (Read Only) SequenceList (Read Only) SequenceView (Read Only) StepGroupList (Read Only) Variables (Read Only) See Als

### SequenceFileViewMgrConnections

Contains the connections for the
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control.

#### Properties

| Caption (Read Only) |
| --- |
| Command (Read Only) |
| Image (Read Only) |
| InsertionPalettes (Read Only) |
| SequenceFileList (Read Only) |
| SequenceList (Read Only) |
| SequenceView (Read Only) |
| StepGroupList (Read Only) |
| Variables (Read Only) |

#### See Also

[ApplicationMgrConnections](applicationmgrconnections.html)

[ExecutionViewMgrConnections](executionviewmgrconnections.html)

[SequenceFileView Manager](sequencefileviewmgr.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnection-getcolumnindex.html language=enus -->
## TOPIC 05612: SequenceListConnection.GetColumnIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnection-getcolumnindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnection-getcolumnindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnection.GetColumnIndex( column) Return Value Long Purpose When the specified column is visible, this method returns the index of the column within the ListBoxColumns collection. Otherwise, this method returns -1 . Remarks Use this index in the ListBoxColumns.Item property to re

### SequenceListConnection.GetColumnIndex

#### Syntax

[SequenceListConnection](sequencelistconnection.html).GetColumnIndex( column)

#### Return Value

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

When the specified column is visible, this method returns the index of the column within the
 [ListBoxColumns](listboxcolumns.html)
 collection. Otherwise, this method returns
 -1
 .

#### Remarks

Use this index in the
 [ListBoxColumns.Item](listboxcolumns-item.html)
 property to return the ListBoxColumn for a specific column.

#### Parameters

column
 As
 [SeqListConnectionColumns](seqlistconnectioncolumns.html)

[In] Specifies the column to select.

#### See Also

[ListBox.ColumnSet](listbox-columnset.html)

[ListBoxColumn](listboxcolumn.html)

[ListBoxColumns](listboxcolumns.html)

[ListBoxColumns.Item](listboxcolumns-item.html)

[SequenceListConnection.GetColumnVisible](sequencelistconnection-getcolumnvisible.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnection-getcolumnvisible.html language=enus -->
## TOPIC 05613: SequenceListConnection.GetColumnVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnection-getcolumnvisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnection-getcolumnvisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnection.GetColumnVisible( column) Return Value Boolean Purpose Returns a Boolean value that indicates whether the column is visible. Parameters column As SeqListConnectionColumns [In] Specifies the column to select. See Also SequenceListConnection.SetColumnVisible

### SequenceListConnection.GetColumnVisible

#### Syntax

[SequenceListConnection](sequencelistconnection.html).GetColumnVisible( column)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Boolean value that indicates whether the column is visible.

#### Parameters

column
 As
 [SeqListConnectionColumns](seqlistconnectioncolumns.html)

[In] Specifies the column to select.

#### See Also

[SequenceListConnection.SetColumnVisible](sequencelistconnection-setcolumnvisible.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnection-setcolumnvisible.html language=enus -->
## TOPIC 05614: SequenceListConnection.SetColumnVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnection-setcolumnvisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnection-setcolumnvisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnection.SetColumnVisible( column, val) Purpose Specifies whether the column is visible. Remarks You cannot hide the SeqListConnectionColumn_Label column. Parameters column As SeqListConnectionColumns [In] Specifies the column to select. val As Boolean [In] Pass False to hide th

### SequenceListConnection.SetColumnVisible

#### Syntax

[SequenceListConnection](sequencelistconnection.html).SetColumnVisible( column, val)

#### Purpose

Specifies whether the column is visible.

#### Remarks

You cannot hide the
 SeqListConnectionColumn_Label
 column.

#### Parameters

column
 As
 [SeqListConnectionColumns](seqlistconnectioncolumns.html)

[In] Specifies the column to select.

val
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Pass
 False
 to hide the column. Otherwise, the column is visible.

#### See Also

[SequenceListConnection.GetColumnVisible](sequencelistconnection-getcolumnvisible.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnection-showcommentintip.html language=enus -->
## TOPIC 05615: SequenceListConnection.ShowCommentInTip

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnection-showcommentintip.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnection-showcommentintip.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnection.ShowCommentInTip Data Type Boolean Purpose Specifies whether the item tooltip includes the sequence comment in controls you connect to display the list of sequences in the selected sequence file.

### SequenceListConnection.ShowCommentInTip

#### Syntax

[SequenceListConnection](sequencelistconnection.html).ShowCommentInTip

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the item tooltip includes the sequence comment in controls you connect to display the list of sequences in the selected sequence file.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnection-uicontrol.html language=enus -->
## TOPIC 05616: SequenceListConnection.UIControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnection-uicontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnection-uicontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnection.UIControl Data Type Object Purpose Returns the user interface control the connection connects to a SequenceFileView Manager control. See Also SequenceFileView Manager

### SequenceListConnection.UIControl

#### Syntax

[SequenceListConnection](sequencelistconnection.html).UIControl

#### Data Type

[Object](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the user interface control the connection connects to a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control.

#### See Also

[SequenceFileView Manager](sequencefileviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnection.html language=enus -->
## TOPIC 05617: SequenceListConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from a SequenceFileView Manager control to a control that displays a list of sequences for the current sequence file. Use the connected control to select the sequence to display. Properties ShowCommentInTip UIControl (Read Only) Methods GetColumnIndex GetColumnVisible SetColu

### SequenceListConnection

Represents a connection from a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control to a control that displays a list of sequences for the current sequence file. Use the connected control to select the sequence to display.

#### Properties

| ShowCommentInTip |
| --- |
| UIControl (Read Only) |

#### Methods

| GetColumnIndex |
| --- |
| GetColumnVisible |
| SetColumnVisible |

#### See Also

[SequenceListConnections](sequencelistconnections.html)

[SequenceFileView Manager](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnections-add.html language=enus -->
## TOPIC 05618: SequenceListConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnections.Add( uiObj) Return Value SequenceListConnection New SequenceListConnection. Purpose Creates and adds a new SequenceListConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also SequenceFileViewMgr.ConnectSequ

### SequenceListConnections.Add

#### Syntax

[SequenceListConnections](sequencelistconnections.html).Add( uiObj)

#### Return Value

[SequenceListConnection](sequencelistconnection.html)

New SequenceListConnection.

#### Purpose

Creates and adds a new SequenceListConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

[SequenceListConnections.Remove](sequencelistconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnections-clear.html language=enus -->
## TOPIC 05619: SequenceListConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnections.Clear Purpose Removes all items from the collection. See Also SequenceListConnections.Remove

### SequenceListConnections.Clear

#### Syntax

[SequenceListConnections](sequencelistconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[SequenceListConnections.Remove](sequencelistconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnections-count.html language=enus -->
## TOPIC 05620: SequenceListConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### SequenceListConnections.Count

#### Syntax

[SequenceListConnections](sequencelistconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnections-fromcontrol.html language=enus -->
## TOPIC 05621: SequenceListConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnections.FromControl( uiObj) Return Value SequenceListConnection SequenceListConnection connected to the uiObj parameter. When no SequenceListConnection exists for this control, this method returns NULL . Purpose Returns the SequenceListConnection connected to the uiObj paramet

### SequenceListConnections.FromControl

#### Syntax

[SequenceListConnections](sequencelistconnections.html).FromControl( uiObj)

#### Return Value

[SequenceListConnection](sequencelistconnection.html)

SequenceListConnection connected to the
 uiObj
 parameter. When no SequenceListConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the SequenceListConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnections-item.html language=enus -->
## TOPIC 05622: SequenceListConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnections.Item( itemIndex) Data Type SequenceListConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also SequenceListC

### SequenceListConnections.Item

#### Syntax

[SequenceListConnections](sequencelistconnections.html).Item( itemIndex)

#### Data Type

[SequenceListConnection](sequencelistconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[SequenceListConnection](sequencelistconnection.html)

[SequenceListConnections.Count](sequencelistconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnections-remove.html language=enus -->
## TOPIC 05623: SequenceListConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceListConnections.Remove( uiObj) Return Value Boolean Returns True when the SequenceListConnection is removed. Returns False when the SequenceListConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the

### SequenceListConnections.Remove

#### Syntax

[SequenceListConnections](sequencelistconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the SequenceListConnection is removed. Returns
 False
 when the SequenceListConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[SequenceListConnections.Add](sequencelistconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequencelistconnections.html language=enus -->
## TOPIC 05624: SequenceListConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequencelistconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequencelistconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of SequenceListConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also SequenceFileViewMgr.ConnectSequenceList SequenceListConnection

### SequenceListConnections

A collection of
 [SequenceListConnection](sequencelistconnection.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

[SequenceListConnection](sequencelistconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-appearance-property-page.html language=enus -->
## TOPIC 05625: SequenceView Appearance Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-appearance-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-appearance-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes to these settings apply only when the ApplicationMgr.UseStepListConfigurations property is False or when no applicable step list configurations exist in the application configuration file. Appearance Property Page The Appearance property page contains the following controls: Comments —Displa

### SequenceView Appearance Property Page

Note

ApplicationMgr.UseStepListConfigurations

False

#### Appearance Property Page

The Appearance property page contains the following controls:

- Comments 
 —Display step comments.
  - Display Step Comments 
 —Displays step comments above the step.
  - Draw Comments Bar 
 —Draws a vertical bar to the left of step comments.
  - Lines to Display 
 —The maximum number of comment lines to show for a step.
- Grid Lines 
 —Enables horizontal and vertical grid lines.
  - Horizontal 
 —Draws horizontal lines between steps.
  - Vertical 
 —Draws vertical lines between columns.
- Block Display Options 
 —Controls the appearance of steps, such as Flow Control steps, that define a block structure in a sequence.
  - Indent Blocks 
 —Indents the steps within a block.
  - Show Block Lines 
 —Draws a vertical bar to the left of the steps in a block.
  - Show Step Group Lines 
 —Draws a vertical line to the left of the steps to outline each step group. This option is available only when you enable the
 Show Block Lines 
 option.
  - Dotted Block Lines 
 —Draws the vertical bar to the left of the block with a dotted line. This option is available only when you enable the
 Show Block Lines 
 option.
  - Show Block Step Icons 
 —Displays icons for steps that define or operate according to the block structure of the sequence.
  - Bold Block Step Font 
 —Displays the step name in bold for steps that define or operate according to the block structure of the sequence.
  - Highlight Block Mismatch Errors 
 —Draws the step name in red for steps that start blocks that do not have an ending step and for block ending steps that do not match with a block starting step. Also draws the vertical block bar red for blocks that do not have an ending step.
- Appearance 
 —Defines the look and feel of the control.
  - Make Columns Always Fit 
 —When you enable this option, every column for which you enable the Autosize option on the
 Columns property page 
 automatically expands or contracts when the control size changes so all the columns fit within the available space.
  - Shade Alternate Columns 
 —TestStand uses a slightly darker color to paint the background for the alternate columns.
  - Round Cells 
 —TestStand uses rounded corners to draw the background for the individual cells. By default all cells have the same background color as the control. However, you can alter an individual cell background using the
 SeqViewColumn.BackColorExpression 
 property.
  - Show Step Icons 
 —TestStand draws the step icons.
  - Icon Size 
 —The size of icons to show in the control. Icons are always square. For example, when you select 32 in the Icon Size control, the icon dimensions are 32 × 32 pixels.

#### See Also

[Columns property page](sequenceview-columns-property-page.html)

[SeqViewColumn.BackColorExpression](seqviewcolumn-backcolorexpression.html)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-autosizecolumns.html language=enus -->
## TOPIC 05626: SequenceView.AutoSizeColumns

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-autosizecolumns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-autosizecolumns.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.AutoSizeColumns Data Type Boolean Purpose Specifies to make all columns fit within the width of the control. When the control resizes, the width of each column for which the SeqViewColumn.Autosizing property is a value other than AutoSizingOption_None adjusts so the columns fit t

### SequenceView.AutoSizeColumns

#### Syntax

[SequenceView](sequenceview.html).AutoSizeColumns

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies to make all columns fit within the width of the control. When the control resizes, the width of each column for which the
 [SeqViewColumn.Autosizing](seqviewcolumn-autosizing.html)
 property is a value other than
 AutoSizingOption_None
 adjusts so the columns fit the new size of the control. You must ensure that at least one column enables autosizing when you set this property to
 True
 .

#### Remarks

When this property is
 True
 , the sum of all column widths always equals the width of the control and the horizontal scrollbar is not visible.

When this property is
 False
 , you can resize the columns to any width and the horizontal scrollbar appears as needed.

#### See Also

[SequenceView.Columns](sequenceview-columns.html)

[SeqViewColumn.Autosizing](seqviewcolumn-autosizing.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-backcolor.html language=enus -->
## TOPIC 05627: SequenceView.BackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-backcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-backcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.BackColor Data Type Color Purpose Specifies the default background color. Remarks You can override this default color on a per-row, per-column basis using the SequenceView.ItemBackColorExpression and SeqViewColumn.BackColorExpression properties. When using the SequenceView contro

### SequenceView.BackColor

#### Syntax

[SequenceView](sequenceview.html).BackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the default background color.

#### Remarks

Note

SequenceView.ItemBackColorExpression

SeqViewColumn.BackColorExpression

Note

ExecutionViewConnection

SequenceView.BackColor

ExecutionViewConnection.Options

ExecutionViewConnection_IgnoreColors

#### See Also

[Color Object](../tsapiref/color.html)

[ExecutionViewConnection](executionviewconnection.html)

[ExecutionViewConnection.Options](executionviewconnection-options.html)

[SequenceView.CommentsColor](sequenceview-commentscolor.html)

[SequenceView.ItemBackColorExpression](sequenceview-itembackcolorexpression.html)

[SequenceView.TextColor](sequenceview-textcolor.html)

[SeqViewColumn.BackColorExpression](seqviewcolumn-backcolorexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-beginupdate.html language=enus -->
## TOPIC 05628: SequenceView.BeginUpdate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-beginupdate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-beginupdate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.BeginUpdate Purpose Prevents the SequenceView control from drawing until the SequenceView.EndUpdate method is called. Remarks Call this method to make multiple changes to the selection or the list of steps without updating the display. See Also SequenceView.EndUpdate

### SequenceView.BeginUpdate

#### Syntax

[SequenceView](sequenceview.html).BeginUpdate

#### Purpose

Prevents the SequenceView control from drawing until the
 [SequenceView.EndUpdate](sequenceview-endupdate.html)
 method is called.

#### Remarks

Call this method to make multiple changes to the selection or the list of steps without updating the display.

#### See Also

[SequenceView.EndUpdate](sequenceview-endupdate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-blockdisplayoptions.html language=enus -->
## TOPIC 05629: SequenceView.BlockDisplayOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-blockdisplayoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-blockdisplayoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.BlockDisplayOptions Data Type Long Purpose Specifies how the SequenceView control displays the block structure of a sequence. See Also BlockDisplayOptions

### SequenceView.BlockDisplayOptions

#### Syntax

[SequenceView](sequenceview.html).BlockDisplayOptions

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the SequenceView control displays the block structure of a sequence.

#### See Also

[BlockDisplayOptions](blockdisplayoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-borderdragged.html language=enus -->
## TOPIC 05630: SequenceView.BorderDragged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-borderdragged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-borderdragged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize) Applies To SequenceView Purpose Occurs when the user drags a draggable border of a control with the mouse. The event provides the location and size to which you must set the control for the draggable bord

### SequenceView.BorderDragged

#### Syntax

ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user drags a draggable border of a control with the mouse. The event provides the location and size to which you must set the control for the draggable borders to track the mouse cursor. However, you can choose to modify the location or size to which you set the control. For example, you can limit the width of the control so the left edge cannot be dragged off of the visible portion of the window.

In addition to changing the size and position of the control, you might also update the sizes and positions of the other controls on the window to account for the change.

#### Remarks

If you are using LabVIEW, you must add the Horizontal and Vertical components of the origin of the LabVIEW front panel to the
 newX
 and
 newY
 event parameter values before you can use the
 newX
 and
 newY
 event parameters to set the ActiveX Container (AxCont) Left and Top properties for the control. To obtain the origin of a LabVIEW front panel, place an ActiveX property node on the block diagram of the VI, right-click the node, and select
 Link to»Pane
 from the context menu. Right-click the node again and select
 Select Property»Origin
 .

#### Parameters

bordersChanged
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies which borders the user dragged. Refer to the
 [WhichBorders](whichborders.html)
 constants for more information about draggable borders.

newX
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new x-coordinate for the control.

newY
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new y-coordinate for the control.

newWidth
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new width for the control.

newHeight
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the new height for the control.

finalResize
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Specifies whether the event is the final event for the drag operation the user performs.

#### See Also

[Borders](borders.html)

[WhichBorders](whichborders.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-borders-property-page.html language=enus -->
## TOPIC 05631: SequenceView Borders Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-borders-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-borders-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Borders Property Page The property page contains the following controls: Control Frame —This section contains the following options: Visible —The control displays a thin rectangular frame that surrounds the control. Frame Location —The location of the frame the control displays. The Frame Location r

### SequenceView Borders Property Page

#### Borders Property Page

The property page contains the following controls:

- Control Frame 
 —This section contains the following options:
  - Visible 
 —The control displays a thin rectangular frame that surrounds the control.
  - Frame Location 
 —The location of the frame the control displays. The Frame Location ring control contains the following options:
    - Inside Borders 
 —The frame appears within the draggable borders of the control.
    - Outside Borders 
 —The frame appears around the draggable borders of the control.
  - Frame Style 
 —The appearance of the frame the control displays. The Frame Style ring control contains the following options:
    - Flat 
 —The frame appears flat.
    - Fixed Single 
 —The frame is a black line, one pixel thick.
    - Control Edge 
 —The frame has the appearance of a control edge. The appearance can vary depending on the Microsoft Windows appearance settings.
    - Raised 
 —The frame has a raised three-dimensional appearance.
    - Inset 
 —The frame has a sunken three-dimensional appearance.
- Drag Borders 
 —This section contains the following options:
  - Top Border 
 —A border at the top edge of the control.
  - Left Border 
 —A border at the left edge of the control.
  - Bottom Border 
 —A border at the bottom edge of the control.
  - Right Border 
 —A border at the right edge of the control.
  - Enable Border Drag Events 
 —The control displays a resizing cursor over the draggable borders and that the control generates
 BorderDragged 
 events when the user drags a draggable border with the mouse.
  - Edge Style 
 —The appearance of the border edge the control displays. The Edge Style contains the following options:
    - Flat 
 —The edge appears flat.
    - Fixed Single 
 —The edge is a black line, one pixel thick.
    - Control Edge 
 —The edge has the appearance of a control edge. The appearance can vary depending on the Windows appearance settings.
    - Raised 
 —The edge has a raised, three-dimensional appearance.
    - Inset 
 —The edge has a sunken, three-dimensional appearance.
  - Width 
 —The width, in pixels, of the draggable borders the control displays.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-borders.html language=enus -->
## TOPIC 05632: SequenceView.Borders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-borders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-borders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.Borders Data Type Borders Purpose Returns the frame and draggable borders that surround the control. See Also Borders SequenceView.BorderDragged

### SequenceView.Borders

#### Syntax

[SequenceView](sequenceview.html).Borders

#### Data Type

[Borders](borders.html)

#### Purpose

Returns the frame and draggable borders that surround the control.

#### See Also

[Borders](borders.html)

[SequenceView.BorderDragged](sequenceview-borderdragged.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-caneditlabel.html language=enus -->
## TOPIC 05633: SequenceView.CanEditLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-caneditlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-caneditlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.CanEditLabel Data Type Boolean Purpose Returns a value that indicates whether the SequenceView control can enter label-editing mode. See Also SequenceView.EditLabel SequenceView.EditingFlags

### SequenceView.CanEditLabel

#### Syntax

[SequenceView](sequenceview.html).CanEditLabel

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a value that indicates whether the SequenceView control can enter label-editing mode.

#### See Also

[SequenceView.EditLabel](sequenceview-editlabel.html)

[SequenceView.EditingFlags](sequenceview-editingflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-columnresized.html language=enus -->
## TOPIC 05634: SequenceView.ColumnResized

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-columnresized.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-columnresized.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ColumnResized( columnIndex, newSize) Applies To SequenceView Purpose Occurs when the user resizes a column in the SequenceView control. Parameters columnIndex As Long [In] Specifies the index of the resized column. newSize As Long [In] Specifies the new size of the column. See Als

### SequenceView.ColumnResized

#### Syntax

ControlName_ColumnResized( columnIndex, newSize)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user resizes a column in the SequenceView control.

#### Parameters

columnIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the resized column.

newSize
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the new size of the column.

#### See Also

[SeqViewColumn.Width](seqviewcolumn-width.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-columns-property-page.html language=enus -->
## TOPIC 05635: SequenceView Columns Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-columns-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-columns-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes to these settings apply only when the ApplicationMgr.UseStepListConfigurations property is False or when no applicable step list configurations exist in the application configuration file. Columns Property Page The Columns property page contains the following controls, which you can use to c

### SequenceView Columns Property Page

Note

ApplicationMgr.UseStepListConfigurations

False

#### Columns Property Page

The Columns property page contains the following controls, which you can use to configure the columns on the
 SequenceView
 control:

Note

SequenceView

- Column List 
 —List of columns in the
 SequenceView 
 control.
  - Add 
 —Adds a new column and assigns the column a unique default name.
  - Remove 
 —Deletes the currently selected column.
  - Up 
 —Moves the currently selected column up one position.
  - Down 
 —Moves the currently selected column down one position.
- Column Properties 
 —These options apply to the currently selected column in the column list.
  - Name 
 —The name of the currently selected column.
  - Caption 
 —The caption of the currently selected column.
 If the caption is a resource string tag in the string section the application uses to
 [localize](/csh?context=ts_tsfundamentals_localization)
 the control, the localized string replaces the caption at run time.
  - Type 
 —The type of the column. The available column types are Name, Index, Description, Execution Flow, Status, and Expression.
  - Width 
 —The horizontal size of the column in pixels.
  - Autosize 
 —The width of the column to adjust to fill the control when the size of the control changes. This option is enabled only when you select the
 Make Columns Always Fit 
 option on the
 Appearance property page 
 .
  - Visible 
 —When you disable this option, the column becomes invisible.
  - Expression 
 —Defines an expression TestStand evaluates for each step at run time and places the result of the expression in the column.
 Note 
 This property has no effect unless the column type is
 Expression
 .
  - Text Color Expression 
 —An expression that returns a
 numeric color value 
 . The column evaluates the expression at run time to determine the column text color. When the expression returns
 -1 
 , the column uses the default color specified in the Step Names option on the
 Fonts and Colors property page 
 .
  - Background Color Expression 
 —An expression that returns a
 numeric color value 
 . The column evaluates the expression at run time to determine the column background color. When the expression returns
 -1 
 , the column uses the default color specified in the Background option on the
 Fonts and Colors property page 
 .

#### See Also

[Appearance property page](sequenceview-appearance-property-page.html)

[ApplicationMgr.LocalizeAllControls](applicationmgr-localizeallcontrols.html)

[Color](/csh?context=ts_tsuiref_color_object)

[Fonts and Colors property page](sequenceview-fonts-and-colors-property-page.html)

[SequenceView.Localize](sequenceview-localize.html)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-columns.html language=enus -->
## TOPIC 05636: SequenceView.Columns

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-columns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-columns.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.Columns Data Type SeqViewColumns Purpose Returns the collection of columns. See Also SequenceView.AutoSizeColumns SeqViewColumns

### SequenceView.Columns

#### Syntax

[SequenceView](sequenceview.html).Columns

#### Data Type

[SeqViewColumns](seqviewcolumns.html)

#### Purpose

Returns the collection of columns.

#### See Also

[SequenceView.AutoSizeColumns](sequenceview-autosizecolumns.html)

[SeqViewColumns](seqviewcolumns.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-commentscolor.html language=enus -->
## TOPIC 05637: SequenceView.CommentsColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-commentscolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-commentscolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.CommentsColor Data Type Color Purpose Specifies the color of the comments for step items. See Also Color SequenceView.CommentsFont SequenceView.ShowComments

### SequenceView.CommentsColor

#### Syntax

[SequenceView](sequenceview.html).CommentsColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the color of the comments for step items.

#### See Also

[Color](../tsapiref/color.html)

[SequenceView.CommentsFont](sequenceview-commentsfont.html)

[SequenceView.ShowComments](sequenceview-showcomments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-commentsfont.html language=enus -->
## TOPIC 05638: SequenceView.CommentsFont

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-commentsfont.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-commentsfont.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.CommentsFont Data Type Font Purpose Specifies the font for comments when the value of the SequenceView.CommentsFontSource property is FontSource_UseFontProperty . See Also FontSources SequenceView.CommentsColor SequenceView.CommentsFontSource SequenceView.ShowComments

### SequenceView.CommentsFont

#### Syntax

[SequenceView](sequenceview.html).CommentsFont

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for comments when the value of the
 [SequenceView.CommentsFontSource](sequenceview-commentsfontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[FontSources](fontsources.html)

[SequenceView.CommentsColor](sequenceview-commentscolor.html)

[SequenceView.CommentsFontSource](sequenceview-commentsfontsource.html)

[SequenceView.ShowComments](sequenceview-showcomments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-commentsfontsource.html language=enus -->
## TOPIC 05639: SequenceView.CommentsFontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-commentsfontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-commentsfontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.CommentsFontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_U

### SequenceView.CommentsFontSource

#### Syntax

[SequenceView](sequenceview.html).CommentsFontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies. Refer to the
 [FontSources](fontsources.html)
 enumeration for the list of valid font sources.

Set this property to a value other than
 FontSource_UseFontProperty
 if you expect the font the
 [SequenceView.CommentsFont](sequenceview-commentsfont.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[FontSources](fontsources.html)

[SequenceView.CommentsFont](sequenceview-commentsfont.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-commentsoffset.html language=enus -->
## TOPIC 05640: SequenceView.CommentsOffset

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-commentsoffset.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-commentsoffset.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.CommentsOffset Data Type Long Purpose Specifies the number of pixels to indent the comment text and comment bar to the right. See Also SequenceView.ShowComments

### SequenceView.CommentsOffset

#### Syntax

[SequenceView](sequenceview.html).CommentsOffset

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the number of pixels to indent the comment text and comment bar to the right.

#### See Also

[SequenceView.ShowComments](sequenceview-showcomments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-connectionactivity.html language=enus -->
## TOPIC 05641: SequenceView.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To SequenceView Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### SequenceView.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-createcontextmenu.html language=enus -->
## TOPIC 05642: SequenceView.CreateContextMenu

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-createcontextmenu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-createcontextmenu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CreateContextMenu( menuHandle, x, y) Applies To SequenceView Purpose Occurs when the user right-clicks on the control so the application can build a context menu from which the user can select commands. Although you can implement context menus in most environments without using th

### SequenceView.CreateContextMenu

#### Syntax

ControlName_CreateContextMenu( menuHandle, x, y)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user right-clicks on the control so the application can build a context menu from which the user can select commands. Although you can implement context menus in most environments without using this event, some environments do not provide any other way to create a context menu. Also, creating a context menu using this event requires less code in most environments, especially when the context menu contains only TestStand commands.

#### Parameters

menuHandle
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the Microsoft Windows menu handle (HMENU). When you add menu items to the menu handle, the control displays them in a context menu. Use the
 [Commands.InsertIntoWin32Menu](commands-insertintowin32menu.html)
 method to insert TestStand commands to the menu.

You can also use the menu functions in the Windows Software Development Kit (SDK) to add other menu items. Menu items you add this way do not have an associated TestStand command. When the user selects an item that does not have a TestStand command, the control creates and executes a Command object of kind
 CommandKind_Custom
 . The control stores the menu item identifier (resource ID/command ID) as a long in the
 [Command.UserData](command-userdata.html)
 property and as a decimal string in the command display name. You can handle either the
 [ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)
 or
 [ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)
 event to receive a notification when the user selects a menu item you insert with the Windows SDK.

When the context menu closes, the control disposes of the menu items. Thus, you do not need to dispose of menu items you insert.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the horizontal position of the right-mouse click, relative to the control.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the vertical position of the right-mouse click, relative to the control.

#### See Also

[ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)

[ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)

[Command.UserData](command-userdata.html)

[Commands.InsertIntoWin32Menu](commands-insertintowin32menu.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-cursor.html language=enus -->
## TOPIC 05643: SequenceView.Cursor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-cursor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-cursor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.Cursor Data Type Long Purpose Specifies the cursor index. The cursor indicates the active item in the view using a dotted box that outlines the item. Setting this property clears the current selection and selects the specified item. See Also SequenceView.FocusIndex

### SequenceView.Cursor

#### Syntax

[SequenceView](sequenceview.html).Cursor

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the cursor index. The cursor indicates the active item in the view using a dotted box that outlines the item. Setting this property clears the current selection and selects the specified item.

#### See Also

[SequenceView.FocusIndex](sequenceview-focusindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-cursormoved.html language=enus -->
## TOPIC 05644: SequenceView.CursorMoved

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-cursormoved.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-cursormoved.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CursorMoved( itemIdx) Applies To SequenceView Purpose Occurs when the user moves the item cursor. Parameters itemIdx As Long [In] Specifies the index of the element that became the cursor. See Also SequenceView.Cursor

### SequenceView.CursorMoved

#### Syntax

ControlName_CursorMoved( itemIdx)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user moves the item cursor.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the element that became the cursor.

#### See Also

[SequenceView.Cursor](sequenceview-cursor.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-dblclick.html language=enus -->
## TOPIC 05645: SequenceView.DblClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-dblclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-dblclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DblClick Applies To SequenceView Purpose Occurs when the user double-clicks the mouse.

### SequenceView.DblClick

#### Syntax

ControlName_DblClick

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user double-clicks the mouse.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-editingflags.html language=enus -->
## TOPIC 05646: SequenceView.EditingFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-editingflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-editingflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.EditingFlags Data Type Long Purpose Specifies the types of editing the SequenceView control allows. Use any combination of the EditingFlags constants with this property. Remarks All editing types are allowed by default. These flags have no effect if the SequenceView control is no

### SequenceView.EditingFlags

#### Syntax

[SequenceView](sequenceview.html).EditingFlags

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the types of editing the SequenceView control allows. Use any combination of the
 [EditingFlags](editingflags.html)
 constants with this property.

#### Remarks

All editing types are allowed by default. These flags have no effect if the SequenceView control is not connected to display editable steps.

#### See Also

[EditingFlags](editingflags.html)

[SequenceView.CanEditLabel](sequenceview-caneditlabel.html)

[SequenceView.EditLabel](sequenceview-editlabel.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-editlabel.html language=enus -->
## TOPIC 05647: SequenceView.EditLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-editlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-editlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.EditLabel Purpose Enters label-editing mode for the active item in the step list. Label-editing mode enables you to edit the item text in the first column of the SequenceView listbox control. Remarks The SequenceView control automatically attempts to enter label-editing mode when

### SequenceView.EditLabel

#### Syntax

[SequenceView](sequenceview.html).EditLabel

#### Purpose

Enters label-editing mode for the active item in the step list. Label-editing mode enables you to edit the item text in the first column of the SequenceView listbox control.

#### Remarks

The SequenceView control automatically attempts to enter label-editing mode when you click the active item in the first column or when you press <F2> when the SequenceView control has the keyboard focus.

#### See Also

[SequenceView.CanEditLabel](sequenceview-caneditlabel.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-endupdate.html language=enus -->
## TOPIC 05648: SequenceView.EndUpdate

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-endupdate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-endupdate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.EndUpdate Purpose Allows the SequenceView control to resume updating, following a call to BeginUpdate . Remarks After making edits to the sequence, call this method to allow the display to update. See Also SequenceView.BeginUpdate

### SequenceView.EndUpdate

#### Syntax

[SequenceView](sequenceview.html).EndUpdate

#### Purpose

Allows the SequenceView control to resume updating, following a call to
 [BeginUpdate](sequenceview-beginupdate.html)
 .

#### Remarks

After making edits to the sequence, call this method to allow the display to update.

#### See Also

[SequenceView.BeginUpdate](sequenceview-beginupdate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-focusindex.html language=enus -->
## TOPIC 05649: SequenceView.FocusIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-focusindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-focusindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.FocusIndex Data Type Long Purpose Specifies the index of the item with the input focus. A dotted rectangle around the item represents the input focus. This property is identical to the SequenceView.Cursor property except that setting this property does not change the selection. S

### SequenceView.FocusIndex

#### Syntax

[SequenceView](sequenceview.html).FocusIndex

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the index of the item with the input focus. A dotted rectangle around the item represents the input focus. This property is identical to the
 [SequenceView.Cursor](sequenceview-cursor.html)
 property except that setting this property does not change the selection.

#### See Also

[SequenceView.Cursor](sequenceview-cursor.html)

[SequenceView.ItemIndexToStep](sequenceview-itemindextostep.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-fonts-and-colors-property-page.html language=enus -->
## TOPIC 05650: SequenceView Fonts and Colors Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-fonts-and-colors-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-fonts-and-colors-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes to these settings apply only when the ApplicationMgr.UseStepListConfigurations property is False or when no applicable step list configurations exist in the application configuration file. Fonts and Colors Property Page The Fonts and Colors property page contains the following controls: Colo

### SequenceView Fonts and Colors Property Page

Note

ApplicationMgr.UseStepListConfigurations

False

#### Fonts and Colors Property Page

The Fonts and Colors property page contains the following controls:

- Colors 
 —The default colors for the control.
  - Step Comments 
 —The color of step comments.
  - Step Names 
 —The color of step names.
  - Background 
 —The background color.
  - Lines 
 —The color of the lines that you enable with the Horizontal or Vertical Grid Lines option on the
 Appearance property page 
 .
- Color Expressions 
 —Use these expressions to customize the colors of a step at run time.
  - Step Text Color 
 —An expression that returns a
 number 
 . The number you specify is used at run time to paint the text. When an expression returns
 -1 
 , the default color specified in the Step Names option is used.
  - Step Background Color 
 —An expression that returns a
 number 
 . The number you specify is used at run time to paint the background of the
 SequenceView 
 control. When an expression returns
 -1 
 , the default color specified in the Background option is used.
- Fonts 
 —Sets different fonts for different portions of the
 SequenceView 
 control.
  - Font for the Item 
 —The item in the
 SequenceView 
 control for which you are changing the font.
    - Text 
 —The font used for text.
    - Comments 
 —The font used for comments.
    - Header 
 —The font used for the column header.
  - Font to Use 
 —The system font to use for the item you select in the Font for the Item control. If you select Use Custom Font for Font to Use, the Custom Font control specifies the font to use.
  - Custom Font 
 —Displays the custom font specified for the item you select in the Font for the Item control. Click the
 Change 
 button to launch the Font dialog box. This option is available only when you select Use Custom Font in the Font to Use control.
 Note 
 The Font dialog box includes a Script ring control. If you change the system language or apply a font selection on a computer with a different language setting, some of the characters in that language might not display in the font you select if the language uses a different script.
  - Change 
 —Launches the Font dialog box, in which you can specify a custom font.

#### See Also

[Appearance property page](sequenceview-appearance-property-page.html)

[Color](/csh?context=ts_tsuiref_color_object)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-headerfont.html language=enus -->
## TOPIC 05651: SequenceView.HeaderFont

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-headerfont.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-headerfont.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.HeaderFont Data Type Font Purpose Specifies the font for the header, which labels each column when the value of the SequenceView.HeaderFontSource property is FontSource_UseFontProperty . See Also FontSources SequenceView.Columns SequenceView.HeaderFontSource

### SequenceView.HeaderFont

#### Syntax

[SequenceView](sequenceview.html).HeaderFont

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for the header, which labels each column when the value of the
 [SequenceView.HeaderFontSource](sequenceview-headerfontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[FontSources](fontsources.html)

[SequenceView.Columns](sequenceview-columns.html)

[SequenceView.HeaderFontSource](sequenceview-headerfontsource.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-headerfontsource.html language=enus -->
## TOPIC 05652: SequenceView.HeaderFontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-headerfontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-headerfontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.HeaderFontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_Use

### SequenceView.HeaderFontSource

#### Syntax

[SequenceView](sequenceview.html).HeaderFontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies.

Set this property to a value other than
 FontSource_UseFontProperty
 if you expect the font the
 [SequenceView.HeaderFont](sequenceview-headerfont.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[FontSources](fontsources.html)

[SequenceView.HeaderFont](sequenceview-headerfont.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-hittest.html language=enus -->
## TOPIC 05653: SequenceView.HitTest

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-hittest.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-hittest.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.HitTest( x, y) Return Value Long Returns a numeric item index. Purpose Returns the zero-based index of the step at the location you specify. When the location is on the End step, the index is equal to the number of steps in the step group the control displays. A value of -1 indic

### SequenceView.HitTest

#### Syntax

[SequenceView](sequenceview.html).HitTest( x, y)

#### Return Value

[Long](data-types-for-teststand-user-interface.html)

Returns a numeric item index.

#### Purpose

Returns the zero-based index of the step at the location you specify. When the location is on the End step, the index is equal to the number of steps in the step group the control displays. A value of
 -1
 indicates the location is not on a step.

#### Remarks

Use this method to determine the item to which the given coordinates belong. For example, when a user clicks on the control, you might want to determine the item the user clicked.

#### Parameters

x
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the location to test, in pixels, relative to the control.

y
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the location to test, in pixels, relative to the control.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-horizlines.html language=enus -->
## TOPIC 05654: SequenceView.HorizLines

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-horizlines.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-horizlines.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.HorizLines Data Type Boolean Purpose Specifies whether the horizontal grid lines are visible. See Also SequenceView.LinesColor SequenceView.VertLines

### SequenceView.HorizLines

#### Syntax

[SequenceView](sequenceview.html).HorizLines

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the horizontal grid lines are visible.

#### See Also

[SequenceView.LinesColor](sequenceview-linescolor.html)

[SequenceView.VertLines](sequenceview-vertlines.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-hwnd.html language=enus -->
## TOPIC 05655: SequenceView.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.hWnd Data Type Long Purpose Returns a Window handle for the control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### SequenceView.hWnd

#### Syntax

[SequenceView](sequenceview.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Window handle for the control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-iconsize.html language=enus -->
## TOPIC 05656: SequenceView.IconSize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-iconsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-iconsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.IconSize Data Type Long Purpose Specifies the size of icons in the SequenceView control. Remarks Icons are always square. For example, when you specify an icon size of 32, the dimensions of the icons are 32 × 32 pixels.

### SequenceView.IconSize

#### Syntax

[SequenceView](sequenceview.html).IconSize

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the size of icons in the SequenceView control.

#### Remarks

Icons are always square. For example, when you specify an icon size of 32, the dimensions of the icons are 32 × 32 pixels.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-itembackcolorexpression.html language=enus -->
## TOPIC 05657: SequenceView.ItemBackColorExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-itembackcolorexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-itembackcolorexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.ItemBackColorExpression Data Type String Purpose Specifies an expression which the SequenceView control uses at run time to determine the background color for individual items. This expression overrides the item color the SequenceView.BackColor property defines. Remarks The expre

### SequenceView.ItemBackColorExpression

#### Syntax

[SequenceView](sequenceview.html).ItemBackColorExpression

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies an expression which the SequenceView control uses at run time to determine the background color for individual items. This expression overrides the item color the
 [SequenceView.BackColor](sequenceview-backcolor.html)
 property defines.

#### Remarks

The expression you specify must return a numeric color value. When you do not want to change the background color, return
 -1
 , as the following example shows:

Step.Result.Status == "Failed" ? tsRed : -1

When you use this expression string, the SequenceView control makes the background for all failed steps red.

If empty, the control ignores this property.

#### See Also

[Color](../tsapiref/color.html)

[SequenceView.BackColor](sequenceview-backcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-itemindextostep.html language=enus -->
## TOPIC 05658: SequenceView.ItemIndexToStep

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-itemindextostep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-itemindextostep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.ItemIndexToStep( itemIndex, group, stepIndex) Return Value Boolean Returns True when the item at itemIndex is a step. Returns False when the item is a step group start or end marker. Purpose Converts from an item index to a step group and step index. Parameters itemIndex As Long

### SequenceView.ItemIndexToStep

#### Syntax

[SequenceView](sequenceview.html).ItemIndexToStep( itemIndex, group, stepIndex)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the item at
 itemIndex
 is a step. Returns
 False
 when the item is a step group start or end marker.

#### Purpose

Converts from an item index to a step group and step index.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies a zero-based index that specifies an item in the control. Item indexes increase from top to bottom.

group
 As
 
 [StepGroups](../tsapiref/stepgroups.html)

[Out] Returns the step group of the specified step.

stepIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[Out] Returns the index within the step group for the specified step. Returns
 -1
 when the item is a start marker. Returns the number of steps in the step group when the item is an end marker.

#### See Also

[SequenceView.StepToItemIndex](sequenceview-steptoitemindex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-itemtextcolorexpression.html language=enus -->
## TOPIC 05659: SequenceView.ItemTextColorExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-itemtextcolorexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-itemtextcolorexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.ItemTextColorExpression Data Type String Purpose Specifies an expression which the SequenceView control uses at run time to determine the text color for individual items. This expression overrides the text color the SequenceView.TextColor property defines. Remarks The expression

### SequenceView.ItemTextColorExpression

#### Syntax

[SequenceView](sequenceview.html).ItemTextColorExpression

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies an expression which the SequenceView control uses at run time to determine the text color for individual items. This expression overrides the text color the
 [SequenceView.TextColor](sequenceview-textcolor.html)
 property defines.

#### Remarks

The expression you specify must return a numeric color value. When you do not want to change the background color, return
 -1
 , as the following example shows:

Step.Result.Status == "Failed" ? tsRed : -1

When you use this expression string, the SequenceView control makes the text color of all failed steps red.

If empty, the control ignores this property.

#### See Also

[Color](../tsapiref/color.html)

[SequenceView.TextColor](sequenceview-textcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-keydown.html language=enus -->
## TOPIC 05660: SequenceView.KeyDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-keydown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-keydown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyDown( keyCode, shift) Applies To SequenceView Purpose Occurs when the user presses a key while the SequenceView control has input focus. Parameters keyCode As Integer [In/Out] Specifies the KeyCodes constant of the key the user pressed. shift As Integer [In] Specifies a combina

### SequenceView.KeyDown

#### Syntax

ControlName_KeyDown( keyCode, shift)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user presses a key while the SequenceView control has input focus.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the
 [KeyCodes](keycodes.html)
 constant of the key the user pressed.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

#### See Also

[KeyCodes](keycodes.html)

[KeyModifiers](keymodifiers.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-linescolor.html language=enus -->
## TOPIC 05661: SequenceView.LinesColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-linescolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-linescolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.LinesColor Data Type Color Purpose Specifies the color of gridlines. See Also SequenceView.HorizLines SequenceView.VertLines

### SequenceView.LinesColor

#### Syntax

[SequenceView](sequenceview.html).LinesColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the color of gridlines.

#### See Also

[SequenceView.HorizLines](sequenceview-horizlines.html)

[SequenceView.VertLines](sequenceview-vertlines.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-localize.html language=enus -->
## TOPIC 05662: SequenceView.Localize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-localize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-localize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.Localize( sectionName) Purpose Localizes the captions of the columns in the SequenceView control. Remarks First, update a .ini file located in the TestStand Language directory with the required strings. Second, use the string tags in the .ini file as the column captions for the c

### SequenceView.Localize

#### Syntax

[SequenceView](sequenceview.html).Localize( sectionName)

#### Purpose

Localizes the captions of the columns in the SequenceView control.

#### Remarks

First, update a
 .ini
 file located in the TestStand
 Language
 directory with the required strings. Second, use the string tags in the
 .ini
 file as the column captions for the control.

When you call this method, the control replaces the column captions with the strings from the
 .ini
 file. If a caption is not a tag in the
 .ini
 file, the caption does not change.

#### Parameters

sectionName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the section in the language files that contains the localized text.

#### See Also

[ApplicationMgr.LocalizeAllControls](applicationmgr-localizeallcontrols.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-maxcommentsheight.html language=enus -->
## TOPIC 05663: SequenceView.MaxCommentsHeight

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-maxcommentsheight.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-maxcommentsheight.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.MaxCommentsHeight Data Type Long Purpose Specifies the maximum number of comment lines visible per step. Remarks Use this property to specify the maximum number of comment lines a step can display. By default, the value of this property is 3 . See Also SequenceView.ShowComments

### SequenceView.MaxCommentsHeight

#### Syntax

[SequenceView](sequenceview.html).MaxCommentsHeight

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the maximum number of comment lines visible per step.

#### Remarks

Use this property to specify the maximum number of comment lines a step can display. By default, the value of this property is
 3
 .

#### See Also

[SequenceView.ShowComments](sequenceview-showcomments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-mousedown.html language=enus -->
## TOPIC 05664: SequenceView.MouseDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-mousedown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-mousedown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseDown( btn, shift, x, y) Applies To SequenceView Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specif

### SequenceView.MouseDown

#### Syntax

ControlName_MouseDown( btn, shift, x, y)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user clicks the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

[SequenceView.MouseMove](sequenceview-mousemove.html)

[SequenceView.MouseUp](sequenceview-mouseup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-mousemove.html language=enus -->
## TOPIC 05665: SequenceView.MouseMove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-mousemove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-mousemove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseMove( btn, shift, x, y) Applies To SequenceView Purpose Occurs when the user moves the mouse over the control. Parameters btn As Integer [In] Specifies what mouse buttons are pressed. You can use any combination of the MouseButtons constants. shift As Integer [In] Specifies a

### SequenceView.MouseMove

#### Syntax

ControlName_MouseMove( btn, shift, x, y)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user moves the mouse over the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies what mouse buttons are pressed. You can use any combination of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

[SequenceView.MouseDown](sequenceview-mousedown.html)

[SequenceView.MouseUp](sequenceview-mouseup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-mouseup.html language=enus -->
## TOPIC 05666: SequenceView.MouseUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-mouseup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-mouseup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseUp( btn, shift, x, y) Applies To SequenceView Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifie

### SequenceView.MouseUp

#### Syntax

ControlName_MouseUp( btn, shift, x, y)

#### Applies To

[SequenceView](sequenceview.html)

#### Purpose

Occurs when the user clicks the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

[SequenceView.MouseDown](sequenceview-mousedown.html)

[SequenceView.MouseMove](sequenceview-mousemove.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-rounditemrects.html language=enus -->
## TOPIC 05667: SequenceView.RoundItemRects

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-rounditemrects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-rounditemrects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.RoundItemRects Data Type Boolean Purpose Specifies whether this control uses rounded corners to draw the background for the individual cells. Remarks By default, all cells have the same background color as the control, which prevents this property from having any discernable effe

### SequenceView.RoundItemRects

#### Syntax

[SequenceView](sequenceview.html).RoundItemRects

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether this control uses rounded corners to draw the background for the individual cells.

#### Remarks

By default, all cells have the same background color as the control, which prevents this property from having any discernable effect. However, you can alter the background color of an individual cell using the
 [SeqViewColumn.BackColorExpression](seqviewcolumn-backcolorexpression.html)
 property.

#### See Also

[SeqViewColumn.BackColorExpression](seqviewcolumn-backcolorexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-scalewithdpi.html language=enus -->
## TOPIC 05668: SequenceView.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are

### SequenceView.ScaleWithDPI

#### Syntax

[SequenceView](sequenceview.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are designed to work in all environments.

The following are the recommended settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-shadealternatecolumns.html language=enus -->
## TOPIC 05669: SequenceView.ShadeAlternateColumns

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-shadealternatecolumns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-shadealternatecolumns.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.ShadeAlternateColumns Data Type Boolean Purpose Specifies whether this control uses a darker color for the background of every other column.

### SequenceView.ShadeAlternateColumns

#### Syntax

[SequenceView](sequenceview.html).ShadeAlternateColumns

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether this control uses a darker color for the background of every other column.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-showcomments.html language=enus -->
## TOPIC 05670: SequenceView.ShowComments

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-showcomments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-showcomments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.ShowComments Data Type Boolean Purpose Specifies whether the control displays step comments. Remarks The control displays step comments above the step. Although step comments can be of any length, you can use the SequenceView.MaxCommentsHeight property to limit the number of comm

### SequenceView.ShowComments

#### Syntax

[SequenceView](sequenceview.html).ShowComments

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control displays step comments.

#### Remarks

The control displays step comments above the step. Although step comments can be of any length, you can use the
 [SequenceView.MaxCommentsHeight](sequenceview-maxcommentsheight.html)
 property to limit the number of comment lines that display for each step.

#### See Also

[SequenceView.CommentsOffset](sequenceview-commentsoffset.html)

[SequenceView.MaxCommentsHeight](sequenceview-maxcommentsheight.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-showcommentsbars.html language=enus -->
## TOPIC 05671: SequenceView.ShowCommentsBars

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-showcommentsbars.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-showcommentsbars.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.ShowCommentsBars Data Type Boolean Purpose When this property is True and the SequenceView.ShowComments property is True , vertical lines display to the left of the step comments. See Also SequenceView.ShowComments

### SequenceView.ShowCommentsBars

#### Syntax

[SequenceView](sequenceview.html).ShowCommentsBars

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 and the
 [SequenceView.ShowComments](sequenceview-showcomments.html)
 property is
 True
 , vertical lines display to the left of the step comments.

#### See Also

[SequenceView.ShowComments](sequenceview-showcomments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-showitemtipstrips.html language=enus -->
## TOPIC 05672: SequenceView.ShowItemTipStrips

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-showitemtipstrips.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-showitemtipstrips.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.ShowItemTipStrips Data Type Boolean Purpose Specifies whether the control displays tooltips. Remarks Item tooltips are the tooltips that appear when you hover over a partially visible item with the mouse. Tooltips allow you to see the full caption of a partially visible item.

### SequenceView.ShowItemTipStrips

#### Syntax

[SequenceView](sequenceview.html).ShowItemTipStrips

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control displays tooltips.

#### Remarks

Item tooltips are the tooltips that appear when you hover over a partially visible item with the mouse. Tooltips allow you to see the full caption of a partially visible item.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-stepiconsenabled.html language=enus -->
## TOPIC 05673: SequenceView.StepIconsEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-stepiconsenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-stepiconsenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.StepIconsEnabled Data Type Boolean Purpose Specifies whether the SequenceView control displays the step icons.

### SequenceView.StepIconsEnabled

#### Syntax

[SequenceView](sequenceview.html).StepIconsEnabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the SequenceView control displays the step icons.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-steptoitemindex.html language=enus -->
## TOPIC 05674: SequenceView.StepToItemIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-steptoitemindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-steptoitemindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.StepToItemIndex( group, stepIndex) Return Value Long Returns a zero-based index. The index identifies the item that displays the specified step. When the step is within a collapsed group, the index identifies the step group start marker. Purpose Converts from a step group and ste

### SequenceView.StepToItemIndex

#### Syntax

[SequenceView](sequenceview.html).StepToItemIndex( group, stepIndex)

#### Return Value

[Long](data-types-for-teststand-user-interface.html)

Returns a zero-based index. The index identifies the item that displays the specified step. When the step is within a collapsed group, the index identifies the step group start marker.

#### Purpose

Converts from a step group and step index to an index into the list of items the control displays.

#### Parameters

group
 As
 
 [StepGroups](../tsapiref/stepgroups.html)

[In] Specifies a step group.

stepIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies an index into the specified step group.

#### See Also

[SequenceView.ItemIndexToStep](sequenceview-itemindextostep.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-textcolor.html language=enus -->
## TOPIC 05675: SequenceView.TextColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-textcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-textcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.TextColor Data Type Color Purpose Specifies the default text color for the item text. Remarks You can override this default color on a per-row, per-column basis using the SequenceView.ItemTextColorExpression and SeqViewColumn.TextColorExpression properties. See Also Color Sequenc

### SequenceView.TextColor

#### Syntax

[SequenceView](sequenceview.html).TextColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the default text color for the item text.

#### Remarks

Note

SequenceView.ItemTextColorExpression

SeqViewColumn.TextColorExpression

#### See Also

[Color](../tsapiref/color.html)

[SequenceView.BackColor](sequenceview-backcolor.html)

[SequenceView.ItemTextColorExpression](sequenceview-itemtextcolorexpression.html)

[SeqViewColumn.TextColorExpression](seqviewcolumn-textcolorexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-textfont.html language=enus -->
## TOPIC 05676: SequenceView.TextFont

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-textfont.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-textfont.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.TextFont Data Type Font Purpose Specifies the font for the item text when the value of the SequenceView.TextFontSource property is FontSource_UseFontProperty . See Also FontSources SequenceView.TextColor SequenceView.TextFontSource

### SequenceView.TextFont

#### Syntax

[SequenceView](sequenceview.html).TextFont

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for the item text when the value of the
 [SequenceView.TextFontSource](sequenceview-textfontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[FontSources](fontsources.html)

[SequenceView.TextColor](sequenceview-textcolor.html)

[SequenceView.TextFontSource](sequenceview-textfontsource.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-textfontsource.html language=enus -->
## TOPIC 05677: SequenceView.TextFontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-textfontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-textfontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.TextFontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGU

### SequenceView.TextFontSource

#### Syntax

[SequenceView](sequenceview.html).TextFontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies.

Set the FontSource property to a value other than
 FontSource_UseFontProperty
 when you expect the font the
 Font
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[FontSources](fontsources.html)

[SequenceView.TextFont](sequenceview-textfont.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview-vertlines.html language=enus -->
## TOPIC 05678: SequenceView.VertLines

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview-vertlines.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview-vertlines.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceView.VertLines Data Type Boolean Purpose Specifies whether the vertical grid lines are visible. See Also SequenceView.HorizLines SequenceView.LinesColor

### SequenceView.VertLines

#### Syntax

[SequenceView](sequenceview.html).VertLines

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the vertical grid lines are visible.

#### See Also

[SequenceView.HorizLines](sequenceview-horizlines.html)

[SequenceView.LinesColor](sequenceview-linescolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceview.html language=enus -->
## TOPIC 05679: SequenceView

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a SequenceFileView Manager control or an ExecutionView Manager control to a SequenceView control to display the steps of a sequence from a selected file or execution. The SequenceView control displays the steps in a list with columns you specify when you configure the control. The SequenceVi

### SequenceView

Connect a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control or an
 [ExecutionView Manager](executionviewmgr.html)
 control to a SequenceView control to display the steps of a sequence from a selected file or execution. The SequenceView control displays the steps in a list with columns you specify when you configure the control.

The SequenceView control maintains a cursor that indicates the last active item you clicked using the mouse or highlighted using the arrow keys. The control denotes the cursor using a dotted box that outlines the step. Use the SequenceView control to select one or more steps at a time.

Use the SequenceFileView Manager control connected to the SequenceView control to control which sequence, step groups, and steps are selected in the file and to track the expansion of the step groups.

#### Properties

| AutoSizeColumns |
| --- |
| BackColor |
| BlockDisplayOptions |
| Borders (Read Only) |
| CanEditLabel (Read Only) |
| Columns (Read Only) |
| CommentsColor |
| CommentsFont |
| CommentsFontSource |
| CommentsOffset |
| Cursor |
| EditingFlags |
| FocusIndex |
| HeaderFont |
| HeaderFontSource |
| HorizLines |
| hWnd (Read Only) |
| IconSize |
| ItemBackColorExpression |
| ItemTextColorExpression |
| LinesColor |
| MaxCommentsHeight |
| RoundItemRects |
| ScaleWithDPI |
| ShadeAlternateColumns |
| ShowComments |
| ShowCommentsBars |
| ShowItemTipStrips |
| StepIconsEnabled |
| TextColor |
| TextFont |
| TextFontSource |
| VertLines |

#### Methods

| BeginUpdate |
| --- |
| EditLabel |
| EndUpdate |
| HitTest |
| ItemIndexToStep |
| Localize |
| StepToItemIndex |

#### Events

| BorderDragged |
| --- |
| ColumnResized |
| ConnectionActivity |
| CreateContextMenu |
| CursorMoved |
| DblClick |
| KeyDown |
| MouseDown |
| MouseMove |
| MouseUp |

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConnectExecutionView](executionviewmgr-connectexecutionview.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConnectSequenceView](sequencefileviewmgr-connectsequenceview.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnection-doubleclickeditssteppr.html language=enus -->
## TOPIC 05680: SequenceViewConnection.DoubleClickEditsStepProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnection-doubleclickeditssteppr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnection-doubleclickeditssteppr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceViewConnection.DoubleClickEditsStepProperties Data Type Boolean Purpose Specifies whether the connected SequenceView control displays the Step Properties dialog box when editing is enabled and the user double-clicks a step. This property defaults to True . Set the property to False if

### SequenceViewConnection.DoubleClickEditsStepProperties

#### Syntax

[SequenceViewConnection](sequenceviewconnection.html).DoubleClickEditsStepProperties

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the connected
 [SequenceView](sequenceview.html)
 control displays the
 [Step Properties](../tsref/step-properties-dialog-box.html)
 dialog box when editing is enabled and the user double-clicks a step. This property defaults to
 True
 . Set the property to
 False
 if you implement an alternate behavior for double-clicking a step in a sequence file.

#### See Also

[SequenceView](sequenceview.html)

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnection-uicontrol.html language=enus -->
## TOPIC 05681: SequenceViewConnection.UIControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnection-uicontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnection-uicontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceViewConnection.UIControl Data Type Object Purpose Returns the user interface control the connection connects to a SequenceFileView Manager control. See Also SequenceFileView Manager

### SequenceViewConnection.UIControl

#### Syntax

[SequenceViewConnection](sequenceviewconnection.html).UIControl

#### Data Type

[Object](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the user interface control the connection connects to a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control.

#### See Also

[SequenceFileView Manager](sequencefileviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnection.html language=enus -->
## TOPIC 05682: SequenceViewConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection from a SequenceFileView Manager control to a SequenceView control. The SequenceView control shows the contents of the current sequence in the SequenceFileView Manager control. Use the SequenceFileViewMgr.Connections property to obtain a collection of SequenceViewConnection ob

### SequenceViewConnection

Represents a connection from a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 control to a
 [SequenceView](sequenceview.html)
 control. The SequenceView control shows the contents of the current sequence in the SequenceFileView Manager control. Use the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property to obtain a collection of SequenceViewConnection objects.

#### Properties

| DoubleClickEditsStepProperties |
| --- |
| UIControl (Read Only) |

#### See Also

[SequenceFileView Manager](sequencefileviewmgr.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceView](sequenceview.html)

[SequenceViewConnections](sequenceviewconnections.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnections-add.html language=enus -->
## TOPIC 05683: SequenceViewConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceViewConnections.Add( uiObj) Return Value SequenceViewConnection New SequenceViewConnection. Purpose Creates and adds a new SequenceViewConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also SequenceFileViewMgr.ConnectSequ

### SequenceViewConnections.Add

#### Syntax

[SequenceViewConnections](sequenceviewconnections.html).Add( uiObj)

#### Return Value

[SequenceViewConnection](sequenceviewconnection.html)

New SequenceViewConnection.

#### Purpose

Creates and adds a new SequenceViewConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[SequenceFileViewMgr.ConnectSequenceView](sequencefileviewmgr-connectsequenceview.html)

[SequenceViewConnections.Remove](sequenceviewconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnections-clear.html language=enus -->
## TOPIC 05684: SequenceViewConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceViewConnections.Clear Purpose Removes all items from the collection. See Also SequenceViewConnections.Remove

### SequenceViewConnections.Clear

#### Syntax

[SequenceViewConnections](sequenceviewconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[SequenceViewConnections.Remove](sequenceviewconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnections-count.html language=enus -->
## TOPIC 05685: SequenceViewConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceViewConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### SequenceViewConnections.Count

#### Syntax

[SequenceViewConnections](sequenceviewconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnections-fromcontrol.html language=enus -->
## TOPIC 05686: SequenceViewConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceViewConnections.FromControl( uiObj) Return Value SequenceViewConnection SequenceViewConnection connected to the uiObj parameter. When no SequenceViewConnection exists for this control, this method returns NULL . Purpose Returns the SequenceViewConnection connected to the uiObj paramet

### SequenceViewConnections.FromControl

#### Syntax

[SequenceViewConnections](sequenceviewconnections.html).FromControl( uiObj)

#### Return Value

[SequenceViewConnection](sequenceviewconnection.html)

SequenceViewConnection connected to the
 uiObj
 parameter. When no SequenceViewConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the SequenceViewConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnections-item.html language=enus -->
## TOPIC 05687: SequenceViewConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceViewConnections.Item( itemIndex) Data Type SequenceViewConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also SequenceViewC

### SequenceViewConnections.Item

#### Syntax

[SequenceViewConnections](sequenceviewconnections.html).Item( itemIndex)

#### Data Type

[SequenceViewConnection](sequenceviewconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[SequenceViewConnection](sequenceviewconnection.html)

[SequenceViewConnections.Count](sequenceviewconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnections-remove.html language=enus -->
## TOPIC 05688: SequenceViewConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceViewConnections.Remove( uiObj) Return Value Boolean Returns True when the SequenceViewConnection is removed. Returns False when the SequenceViewConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the

### SequenceViewConnections.Remove

#### Syntax

[SequenceViewConnections](sequenceviewconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the SequenceViewConnection is removed. Returns
 False
 when the SequenceViewConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[SequenceViewConnections.Add](sequenceviewconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/sequenceviewconnections.html language=enus -->
## TOPIC 05689: SequenceViewConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/sequenceviewconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/sequenceviewconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of SequenceViewConnection objects you obtain by calling the SequenceFileViewMgr.Connections property. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also SequenceFileViewMgr.ConnectSequenceView SequenceFileViewMgr.Connections SequenceViewConnectio

### SequenceViewConnections

A collection of
 [SequenceViewConnection](sequenceviewconnection.html)
 objects you obtain by calling the
 [SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)
 property.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Clear |
| FromControl |
| Remove |

#### See Also

[SequenceFileViewMgr.ConnectSequenceView](sequencefileviewmgr-connectsequenceview.html)

[SequenceFileViewMgr.Connections](sequencefileviewmgr-connections.html)

[SequenceViewConnection](sequenceviewconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-autosizing.html language=enus -->
## TOPIC 05690: SeqViewColumn.AutoSizing

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-autosizing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-autosizing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.AutoSizing Data Type AutoSizingOptions Use the following constants with this data type: AutoSizingOption_None –(Value: 0) The item does not automatically resize itself. AutoSizingOption_Proportional –(Value: 1) The item resizes when the container resizes. The item determines the

### SeqViewColumn.AutoSizing

#### Syntax

[SeqViewColumn](seqviewcolumn.html).AutoSizing

#### Data Type

[AutoSizingOptions](autosizingoptions.html)

Use the following constants with this data type:

- AutoSizingOption_None 
 –(Value: 0) The item does not automatically resize itself.
- AutoSizingOption_Proportional 
 –(Value: 1) The item resizes when the container resizes. The item determines the amount to resize from the proportion that the current size occupies of the total size of all resizable items in the same container.

#### Purpose

Specifies whether the column automatically grows or shrinks to adjust to changes in the size of the control. This property does not take effect unless the
 [SequenceView.AutoSizeColumns](sequenceview-autosizecolumns.html)
 property is
 True
 .

#### See Also

[SequenceView.AutoSizeColumns](sequenceview-autosizecolumns.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-backcolorexpression.html language=enus -->
## TOPIC 05691: SeqViewColumn.BackColorExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-backcolorexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-backcolorexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.BackColorExpression Data Type String Purpose Specifies an expression used to determine the background color for individual cells in the selected column at run time. Remarks This expression overrides the item color the SequenceView.BackColor and SequenceView.ItemBackColorExpressi

### SeqViewColumn.BackColorExpression

#### Syntax

[SeqViewColumn](seqviewcolumn.html).BackColorExpression

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies an expression used to determine the background color for individual cells in the selected column at run time.

#### Remarks

This expression overrides the item color the
 [SequenceView.BackColor](sequenceview-backcolor.html)
 and
 [SequenceView.ItemBackColorExpression](sequenceview-itembackcolorexpression.html)
 properties define.

Specify an expression that returns a numeric color value. When you do not want to change the text color, return
 -1
 , as the following example shows:

Step.Result.Status == "Failed" ? tsRed: -1

When you assign this expression string to the
 BackColorExpression
 property of a column and run the application, the control colors the column background red for steps that fail.

When empty, the control ignores this property.

#### See Also

[SequenceView.BackColor](sequenceview-backcolor.html)

[SequenceView.ItemBackColorExpression](sequenceview-itembackcolorexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-caption.html language=enus -->
## TOPIC 05692: SeqViewColumn.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.Caption Data Type String Purpose Specifies the caption in the header for the column. See Also SeqViewColumn.Expression SeqViewColumn.Type

### SeqViewColumn.Caption

#### Syntax

[SeqViewColumn](seqviewcolumn.html).Caption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the caption in the header for the column.

#### See Also

[SeqViewColumn.Expression](seqviewcolumn-expression.html)

[SeqViewColumn.Type](seqviewcolumn-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-expression.html language=enus -->
## TOPIC 05693: SeqViewColumn.Expression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-expression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-expression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.Expression Data Type String Purpose Specifies the expression for the column. Remarks The column evaluates the expression and displays the evaluation result for each step. The Expression property is one of two ways you can define what a column displays. You can also use the SeqVi

### SeqViewColumn.Expression

#### Syntax

[SeqViewColumn](seqviewcolumn.html).Expression

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the expression for the column.

#### Remarks

The column evaluates the expression and displays the evaluation result for each step.

The Expression property is one of two ways you can define what a column displays. You can also use the
 [SeqViewColumn.Type](seqviewcolumn-type.html)
 property to define standard columns, such as step index or step description.

Note

SeqViewColumnType_Expression

#### See Also

[SeqViewColumn.Caption](seqviewcolumn-caption.html)

[SeqViewColumn.Type](seqviewcolumn-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-index.html language=enus -->
## TOPIC 05694: SeqViewColumn.Index

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-index.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-index.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.Index Data Type Long Purpose Returns the zero-based numeric index of the column within the SeqViewColumns collection. See Also SeqViewColumn.Name SeqViewColumns

### SeqViewColumn.Index

#### Syntax

[SeqViewColumn](seqviewcolumn.html).Index

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the zero-based numeric index of the column within the
 [SeqViewColumns](seqviewcolumns.html)
 collection.

#### See Also

[SeqViewColumn.Name](seqviewcolumn-name.html)

[SeqViewColumns](seqviewcolumns.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-name.html language=enus -->
## TOPIC 05695: SeqViewColumn.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.Name Data Type String Purpose Specifies the name for the column. Remarks Every column must have a unique name, which can be used to identify the column within the SeqViewColumns collection. Column names are not case-sensitive. See Also SeqViewColumn.Index SeqViewColumns

### SeqViewColumn.Name

#### Syntax

[SeqViewColumn](seqviewcolumn.html).Name

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the name for the column.

#### Remarks

Every column must have a unique name, which can be used to identify the column within the
 [SeqViewColumns](seqviewcolumns.html)
 collection. Column names are not case-sensitive.

#### See Also

[SeqViewColumn.Index](seqviewcolumn-index.html)

[SeqViewColumns](seqviewcolumns.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-textcolorexpression.html language=enus -->
## TOPIC 05696: SeqViewColumn.TextColorExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-textcolorexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-textcolorexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.TextColorExpression Data Type String Purpose Specifies an expression that determines the text color for individual cells in the column at run time. Remarks This expression overrides the item color the SequenceView.TextColor and SequenceView.ItemTextColorExpression properties def

### SeqViewColumn.TextColorExpression

#### Syntax

[SeqViewColumn](seqviewcolumn.html).TextColorExpression

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies an expression that determines the text color for individual cells in the column at run time.

#### Remarks

This expression overrides the item color the
 [SequenceView.TextColor](sequenceview-textcolor.html)
 and
 [SequenceView.ItemTextColorExpression](sequenceview-itemtextcolorexpression.html)
 properties define.

The expression must return a numeric color value. When you do not want to change the text color, return
 -1
 , as the following example shows:

Step.Result.Status == "Failed" ? tsRed: -1

When you assign this expression string to the
 TextColorExpression
 property of a column and run the application, the control colors the column text red for steps that fail.

When empty, the control ignores this property.

#### See Also

[SequenceView.ItemTextColorExpression](sequenceview-itemtextcolorexpression.html)

[SequenceView.TextColor](sequenceview-textcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-type.html language=enus -->
## TOPIC 05697: SeqViewColumn.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.Type Data Type SeqViewColumnTypes Use the following constants with this data type: SeqViewColumnType_Comment –(Value: 7) Comment for the step. SeqViewColumnType_Description –(Value: 3) Description of the step. SeqViewColumnType_ExecutionFlow –(Value: 4) Execution flow of the ste

### SeqViewColumn.Type

#### Syntax

[SeqViewColumn](seqviewcolumn.html).Type

#### Data Type

[SeqViewColumnTypes](seqviewcolumntypes.html)

Use the following constants with this data type:

- SeqViewColumnType_Comment 
 –(Value: 7) Comment for the step.
- SeqViewColumnType_Description 
 –(Value: 3) Description of the step.
- SeqViewColumnType_ExecutionFlow 
 –(Value: 4) Execution flow of the step.
- SeqViewColumnType_Expression 
 –(Value: 6) Custom Expression. Use the
 SeqViewColumn.Expression 
 property to specify an expression for the column.
- SeqViewColumnType_Name 
 –(Value: 1) Name of the step.
- SeqViewColumnType_Requirements 
 –(Value: 8) Requirements of the step.
- SeqViewColumnType_Status 
 –(Value: 5) Status of the step.
- SeqViewColumnType_StepIndex 
 –(Value: 2) Index of the step.
- SeqViewColumnType_StepSettings 
 –(Value: 4) A summary of the settings for the step.

#### Purpose

Specifies the type of the column.

#### Remarks

You can use this property to define what kind of information displays for each step in the column. When the type of column you need is not defined in
 [SeqViewColumnTypes](seqviewcolumntypes.html)
 , you can set the type to
 SeqViewColumnType_Expression
 and create your own type using the
 [SeqViewColumn.Expression](seqviewcolumn-expression.html)
 property. The result of the expression you specify displays for each step.

#### See Also

[SeqViewColumn.Expression](seqviewcolumn-expression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-visible.html language=enus -->
## TOPIC 05698: SeqViewColumn.Visible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-visible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-visible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.Visible Data Type Boolean Purpose Specifies whether the column is visible.

### SeqViewColumn.Visible

#### Syntax

[SeqViewColumn](seqviewcolumn.html).Visible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the column is visible.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn-width.html language=enus -->
## TOPIC 05699: SeqViewColumn.Width

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn-width.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn-width.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumn.Width Data Type Long Purpose Specifies the width of the column in pixels. When you set the width, the control generates the SequenceView.ColumnResized event. See Also SequenceView.ColumnResized

### SeqViewColumn.Width

#### Syntax

[SeqViewColumn](seqviewcolumn.html).Width

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the width of the column in pixels. When you set the width, the control generates the
 [SequenceView.ColumnResized](sequenceview-columnresized.html)
 event.

#### See Also

[SequenceView.ColumnResized](sequenceview-columnresized.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumn.html language=enus -->
## TOPIC 05700: SeqViewColumn

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumn.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumn.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The SeqViewColumn object represents a column in the SequenceView control. Use the SequenceView.Columns property to obtain a list of columns for the control. Properties AutoSizing BackColorExpression Caption Expression Index (Read Only) Name TextColorExpression Type Visible Width See Also SequenceVie

### SeqViewColumn

The SeqViewColumn object represents a column in the
 [SequenceView](sequenceview.html)
 control. Use the
 [SequenceView.Columns](sequenceview-columns.html)
 property to obtain a list of columns for the control.

#### Properties

| AutoSizing |
| --- |
| BackColorExpression |
| Caption |
| Expression |
| Index (Read Only) |
| Name |
| TextColorExpression |
| Type |
| Visible |
| Width |

#### See Also

[SequenceView](sequenceview.html)

[SequenceView.Columns](sequenceview-columns.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumns-clear.html language=enus -->
## TOPIC 05701: SeqViewColumns.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumns-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumns-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumns.Clear Purpose Removes all items from the collection. See Also SeqViewColumns.Insert

### SeqViewColumns.Clear

#### Syntax

[SeqViewColumns](seqviewcolumns.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[SeqViewColumns.Insert](seqviewcolumns-insert.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumns-count.html language=enus -->
## TOPIC 05702: SeqViewColumns.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumns-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumns-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumns.Count Data Type Long Purpose Returns the number of items in the collection. See Also SeqViewColumn

### SeqViewColumns.Count

#### Syntax

[SeqViewColumns](seqviewcolumns.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[SeqViewColumn](seqviewcolumn.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumns-insert.html language=enus -->
## TOPIC 05703: SeqViewColumns.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumns-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumns-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumns.Insert( itemName, columnType, columnWidth, insertBefore) Return Value SeqViewColumn Purpose Adds a new item to the collection and returns the new SeqViewColumn object. Parameters itemName As String [In] Specifies the name of the new column. The name must be unique but is not ca

### SeqViewColumns.Insert

#### Syntax

[SeqViewColumns](seqviewcolumns.html).Insert( itemName, columnType, columnWidth, insertBefore)

#### Return Value

[SeqViewColumn](seqviewcolumn.html)

#### Purpose

Adds a new item to the collection and returns the new
 [SeqViewColumn](seqviewcolumn.html)
 object.

#### Parameters

itemName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the new column. The name must be unique but is not case-sensitive.

columnType
 As
 [SeqViewColumnTypes](seqviewcolumntypes.html)

[In] Specifies the type of column. Refer to the
 [SeqViewColumn.Type](seqviewcolumn-type.html)
 property for more information about column types.

columnWidth
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the width of the new column, in pixels.

insertBefore
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the existing page before which to insert the new page. When you want the new page to be last, pass
 -1
 to this parameter.

#### See Also

[SeqViewColumn](seqviewcolumn.html)

[SeqViewColumn.Type](seqviewcolumn-type.html)

[SeqViewColumns.Clear](seqviewcolumns-clear.html)

[SeqViewColumnTypes](seqviewcolumntypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumns-item.html language=enus -->
## TOPIC 05704: SeqViewColumns.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumns-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumns-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumns.Item( itemIdx) Data Type SeqViewColumn Purpose Returns a reference to an item with the specified name or at the specified index in the collection. Parameters itemIdx As Variant [In] You can pass a number to obtain a column by its index value. You can also pass a string to obtai

### SeqViewColumns.Item

#### Syntax

[SeqViewColumns](seqviewcolumns.html).Item( itemIdx)

#### Data Type

[SeqViewColumn](seqviewcolumn.html)

#### Purpose

Returns a reference to an item with the specified name or at the specified index in the collection.

#### Parameters

itemIdx
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] You can pass a number to obtain a column by its index value. You can also pass a string to obtain the column using its name.

#### See Also

[SeqViewColumn](seqviewcolumn.html)

[SeqViewColumns.Count](seqviewcolumns-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumns-moveleft.html language=enus -->
## TOPIC 05705: SeqViewColumns.MoveLeft

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumns-moveleft.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumns-moveleft.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumns.MoveLeft( itemIdx) Purpose Moves a specific column one position to the left towards the beginning of the collection. For example, call Control.Columns.MoveLeft(1) to switch the first and second columns. Parameters itemIdx As Long [In] Specifies the zero-based index of the colum

### SeqViewColumns.MoveLeft

#### Syntax

[SeqViewColumns](seqviewcolumns.html).MoveLeft( itemIdx)

#### Purpose

Moves a specific column one position to the left towards the beginning of the collection. For example, call
 Control.Columns.MoveLeft(1)
 to switch the first and second columns.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the column to move in the collection.

#### See Also

[SeqViewColumns.MoveRight](seqviewcolumns-moveright.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumns-moveright.html language=enus -->
## TOPIC 05706: SeqViewColumns.MoveRight

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumns-moveright.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumns-moveright.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumns.MoveRight( itemIdx) Purpose Moves a specific column one position to the right towards the end of the collection. For example, call Control.Columns.MoveRight(0) to switch the first and second columns. Parameters itemIdx As Long [In] Specifies the zero-based index of the column t

### SeqViewColumns.MoveRight

#### Syntax

[SeqViewColumns](seqviewcolumns.html).MoveRight( itemIdx)

#### Purpose

Moves a specific column one position to the right towards the end of the collection. For example, call
 Control.Columns.MoveRight(0)
 to switch the first and second columns.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the column to move in the collection.

#### See Also

[SeqViewColumns.MoveLeft](seqviewcolumns-moveleft.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumns-remove.html language=enus -->
## TOPIC 05707: SeqViewColumns.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumns-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumns-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SeqViewColumns.Remove( itemIdx) Purpose Removes the specified item from this collection, if it exists. Parameters itemIdx As Long [In] Specifies the zero-based index of the column to remove from the collection. See Also SeqViewColumns.Clear

### SeqViewColumns.Remove

#### Syntax

[SeqViewColumns](seqviewcolumns.html).Remove( itemIdx)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the column to remove from the collection.

#### See Also

[SeqViewColumns.Clear](seqviewcolumns-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumns.html language=enus -->
## TOPIC 05708: SeqViewColumns

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumns.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of SeqViewColumn objects. Properties Count (Read Only) Item (Read Only) Methods Clear Insert MoveLeft MoveRight Remove See Also SeqViewColumn

### SeqViewColumns

A collection of
 [SeqViewColumn](seqviewcolumn.html)
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Insert |
| MoveLeft |
| MoveRight |
| Remove |

#### See Also

[SeqViewColumn](seqviewcolumn.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/seqviewcolumntypes.html language=enus -->
## TOPIC 05709: SeqViewColumnTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/seqviewcolumntypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/seqviewcolumntypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SeqViewColumn.Type property to define what type of information is displayed for each step in the column. SeqViewColumnType_Comment –(Value: 7) Comment for the step. SeqViewColumnType_Description –(Value: 3) Description of the step. SeqViewColumnType_ExecutionFlow –(Value

### SeqViewColumnTypes

Use these constants with the
 [SeqViewColumn.Type](seqviewcolumn-type.html)
 property to define what type of information is displayed for each step in the column.

- SeqViewColumnType_Comment 
 –(Value: 7) Comment for the step.
- SeqViewColumnType_Description 
 –(Value: 3) Description of the step.
- SeqViewColumnType_ExecutionFlow 
 –(Value: 4) Execution flow of the step.
- SeqViewColumnType_Expression 
 –(Value: 6) Custom Expression. Use the
 SeqViewColumn.Expression 
 property to specify an expression for the column.
- SeqViewColumnType_Name 
 –(Value: 1) Name of the step.
- SeqViewColumnType_Requirements 
 –(Value: 8) Requirements of the step.
- SeqViewColumnType_Status 
 –(Value: 5) Status of the step.
- SeqViewColumnType_StepIndex 
 –(Value: 2) Index of the step.
- SeqViewColumnType_StepSettings 
 –(Value: 4) A summary of the settings for the step.

#### See Also

[SeqViewColumn.Expression](seqviewcolumn-expression.html)

[SeqViewColumn.Type](seqviewcolumn-type.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/shortcutkeys.html language=enus -->
## TOPIC 05710: ShortcutKeys

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/shortcutkeys.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/shortcutkeys.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Command.ShortcutKey , ExpressionEditButton.ShortcutKey , and ApplicationMgr.EditModeShortcutKey properties. ShortcutKey_VK_0 –(Value: 0x30) The 0 key. ShortcutKey_VK_1 –(Value: 0x31) The 1 key. ShortcutKey_VK_2 –(Value: 0x32) The 2 key. ShortcutKey_VK_3 –(Value: 0x33) Th

### ShortcutKeys

Use these constants with the
 [Command.ShortcutKey](command-shortcutkey.html)
 ,
 [ExpressionEditButton.ShortcutKey](expressioneditbutton-shortcutkey.html)
 , and
 [ApplicationMgr.EditModeShortcutKey](applicationmgr-editmodeshortcutkey.html)
 properties.

- ShortcutKey_VK_0 
 –(Value: 0x30) The 0 key.
- ShortcutKey_VK_1 
 –(Value: 0x31) The 1 key.
- ShortcutKey_VK_2 
 –(Value: 0x32) The 2 key.
- ShortcutKey_VK_3 
 –(Value: 0x33) The 3 key.
- ShortcutKey_VK_4 
 –(Value: 0x34) The 4 key.
- ShortcutKey_VK_5 
 –(Value: 0x35) The 5 key.
- ShortcutKey_VK_6 
 –(Value: 0x36) The 6 key.
- ShortcutKey_VK_7 
 –(Value: 0x37) The 7 key.
- ShortcutKey_VK_8 
 –(Value: 0x38) The 8 key.
- ShortcutKey_VK_9 
 –(Value: 0x39) The 9 key.
- ShortcutKey_VK_A 
 –(Value: 0x41) The A key.
- ShortcutKey_VK_ADD 
 –(Value: 0x6B) The Add key.
- ShortcutKey_VK_B 
 –(Value: 0x42) The B key.
- ShortcutKey_VK_BACK 
 –(Value: 0x08) The Backspace key.
- ShortcutKey_VK_C 
 –(Value: 0x43) The C key.
- ShortcutKey_VK_D 
 –(Value: 0x44) The D key.
- ShortcutKey_VK_DECIMAL 
 –(Value: 0x6E) The Decimal key.
- ShortcutKey_VK_DELETE 
 –(Value: 0x2E) The Delete key.
- ShortcutKey_VK_DIVIDE 
 –(Value: 0x6F) The Divide key.
- ShortcutKey_VK_DOWN 
 –(Value: 0x28) The Down Arrow key.
- ShortcutKey_VK_E 
 –(Value: 0x45) The E key.
- ShortcutKey_VK_END 
 –(Value: 0x23) The End key.
- ShortcutKey_VK_ESCAPE 
 –(Value: 0x1B) The Escape key.
- ShortcutKey_VK_F 
 –(Value: 0x46) The F key.
- ShortcutKey_VK_F1 
 –(Value: 0x70) The F1 key.
- ShortcutKey_VK_F10 
 –(Value: 0x79) The F10 key.
- ShortcutKey_VK_F11 
 –(Value: 0x7A) The F11 key.
- ShortcutKey_VK_F12 
 –(Value: 0x7B) The F12 key.
- ShortcutKey_VK_F13 
 –(Value: 0x7C) The F13 key.
- ShortcutKey_VK_F14 
 –(Value: 0x7D) The F14 key.
- ShortcutKey_VK_F15 
 –(Value: 0x7E) The F15 key.
- ShortcutKey_VK_F16 
 –(Value: 0x7F) The F16 key.
- ShortcutKey_VK_F17 
 –(Value: 0x80) The F17 key.
- ShortcutKey_VK_F18 
 –(Value: 0x81) The F18 key.
- ShortcutKey_VK_F19 
 –(Value: 0x82) The F19 key.
- ShortcutKey_VK_F2 
 –(Value: 0x71) The F2 key.
- ShortcutKey_VK_F20 
 –(Value: 0x83) The F20 key.
- ShortcutKey_VK_F21 
 –(Value: 0x84) The F21 key.
- ShortcutKey_VK_F22 
 –(Value: 0x85) The F22 key.
- ShortcutKey_VK_F23 
 –(Value: 0x86) The F23 key.
- ShortcutKey_VK_F24 
 –(Value: 0x87) The F24 key.
- ShortcutKey_VK_F3 
 –(Value: 0x72) The F3 key.
- ShortcutKey_VK_F4 
 –(Value: 0x73) The F4 key.
- ShortcutKey_VK_F5 
 –(Value: 0x74) The F5 key.
- ShortcutKey_VK_F6 
 –(Value: 10x75) The F6 key.
- ShortcutKey_VK_F7 
 –(Value: 0x76)The F7 key.
- ShortcutKey_VK_F8 
 –(Value: 0x77) The F8 key.
- ShortcutKey_VK_F9 
 –(Value: 0x78) The F9 key.
- ShortcutKey_VK_G 
 –(Value: 0x47) The G key.
- ShortcutKey_VK_H 
 –(Value: 0x48) The H key.
- ShortcutKey_VK_HOME 
 –(Value: 0x24) The Home key.
- ShortcutKey_VK_I 
 –(Value: 0x49) The I key.
- ShortcutKey_VK_INSERT 
 –(Value: 0x2D) The Insert key.
- ShortcutKey_VK_J 
 –(Value: 0x4A) The J key.
- ShortcutKey_VK_K 
 –(Value: 0x4B) The K key.
- ShortcutKey_VK_L 
 –(Value: 0x4C) The L key.
- ShortcutKey_VK_LEFT 
 –(Value: 0x25) The Left Arrow key.
- ShortcutKey_VK_M 
 –(Value: 0x4D) The M key.
- ShortcutKey_VK_MULTIPLY 
 –(Value: 0x6A) The Multiply key.
- ShortcutKey_VK_N 
 –(Value: 0x4E) The N key.
- ShortcutKey_VK_NOT_A_KEY 
 –(Value: 0x00)
- ShortcutKey_VK_NUMPAD0 
 –(Value: 0x60) The numeric keypad 0 key.
- ShortcutKey_VK_NUMPAD1 
 –(Value: 0x61) The numeric keypad 1 key.
- ShortcutKey_VK_NUMPAD2 
 –(Value: 0x62) The numeric keypad 2 key.
- ShortcutKey_VK_NUMPAD3 
 –(Value: 0x63) The numeric keypad 3 key.
- ShortcutKey_VK_NUMPAD4 
 –(Value: 0x64) The numeric keypad 4 key.
- ShortcutKey_VK_NUMPAD5 
 –(Value: 0x65) The numeric keypad 5 key.
- ShortcutKey_VK_NUMPAD6 
 –(Value: 0x66) The numeric keypad 6 key.
- ShortcutKey_VK_NUMPAD7 
 –(Value: 0x67) The numeric keypad 7 key.
- ShortcutKey_VK_NUMPAD8 
 –(Value: 0x68) The numeric keypad 8 key.
- ShortcutKey_VK_NUMPAD9 
 –(Value: 0x69) The numeric keypad 9 key.
- ShortcutKey_VK_O 
 –(Value: 0x4F) The O key.
- ShortcutKey_VK_P 
 –(Value: 0x50) The P key.
- ShortcutKey_VK_Q 
 –(Value: 0x51) The Q key.
- ShortcutKey_VK_R 
 –(Value: 0x52) The R key.
- ShortcutKey_VK_RETURN 
 –(Value: 0x0D) The Enter key.
- ShortcutKey_VK_RIGHT 
 –(Value: 0x27) The Right Arrow key.
- ShortcutKey_VK_S 
 –(Value: 0x53) The S key.
- ShortcutKey_VK_SEPARATOR 
 –(Value: 0x6C) The Separator key.
- ShortcutKey_VK_SPACE 
 –(Value: 0x20) The Space key.
- ShortcutKey_VK_SUBTRACT 
 –(Value: 0x6D) The Subtract key.
- ShortcutKey_VK_T 
 –(Value: 0x54) The T key.
- ShortcutKey_VK_TAB 
 –(Value: 0x09) The <Tab> key.
- ShortcutKey_VK_U 
 –(Value: 0x55) The U key.
- ShortcutKey_VK_UP 
 –(Value: 0x26) The Up Arrow key.
- ShortcutKey_VK_V 
 –(Value: 0x56) The V key.
- ShortcutKey_VK_W 
 –(Value: 0x57) The W key.
- ShortcutKey_VK_X 
 –(Value: 0x58) The X key.
- ShortcutKey_VK_Y 
 –(Value: 0x59) The Y key.
- ShortcutKey_VK_Z 
 –(Value: 0x5A) The Z key.

#### See Also

[ApplicationMgr.EditModeShortcutKey](applicationmgr-editmodeshortcutkey.html)

[Command.ShortcutKey](command-shortcutkey.html)

[ExpressionEditButton.ShortcutKey](expressioneditbutton-shortcutkey.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/shortcutmodifiers.html language=enus -->
## TOPIC 05711: ShortcutModifiers

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/shortcutmodifiers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/shortcutmodifiers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Command.ShortcutModifier , ExpressionEditButton.ShortcutModifier , and ApplicationMgr.EditModeShortcutModifier properties. ShortcutModifier_Alt –(Value: 0x4) The <Alt> key. ShortcutModifier_Control –(Value: 0x2) The <Ctrl> key. ShortcutModifier_NotAModifier –(Value: 0x0)

### ShortcutModifiers

Use these constants with the
 [Command.ShortcutModifier](command-shortcutmodifier.html)
 ,
 [ExpressionEditButton.ShortcutModifier](expressioneditbutton-shortcutmodifier.html)
 , and
 [ApplicationMgr.EditModeShortcutModifier](applicationmgr-editmodeshortcutmodifier.html)
 properties.

- ShortcutModifier_Alt 
 –(Value: 0x4) The <Alt> key.
- ShortcutModifier_Control 
 –(Value: 0x2) The <Ctrl> key.
- ShortcutModifier_NotAModifier 
 –(Value: 0x0) No modifier keys are available.
- ShortcutModifier_Shift 
 –(Value: 0x1) The <Shift> key.

#### See Also

[ApplicationMgr.EditModeShortcutModifier](applicationmgr-editmodeshortcutmodifier.html)

[Command.ShortcutModifier](command-shortcutmodifier.html)

[ExpressionEditButton.ShortcutModifier](expressioneditbutton-shortcutmodifier.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/specifyexpressioneditbutton.html language=enus -->
## TOPIC 05712: SpecifyExpressionEditButton

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/specifyexpressioneditbutton.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/specifyexpressioneditbutton.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ExpressionEditButtons.GetItem and ExpressionEditButtons.Remove methods. SpecifyButton_ByIndex –(Value: 0) The indexOrKind parameter is a zero-based index of a button. SpecifyButton_ByKind –(Value: 1) The indexOrKind parameter is an ExpressionEditButtonKinds constant. See

### SpecifyExpressionEditButton

Use these constants with the
 [ExpressionEditButtons.GetItem](expressioneditbuttons-getitem.html)
 and
 [ExpressionEditButtons.Remove](expressioneditbuttons-remove.html)
 methods.

- SpecifyButton_ByIndex 
 –(Value: 0) The
 indexOrKind 
 parameter is a zero-based index of a button.
- SpecifyButton_ByKind 
 –(Value: 1) The
 indexOrKind 
 parameter is an
 ExpressionEditButtonKinds 
 constant.

#### See Also

[ExpressionEditButtonKinds](expressioneditbuttonkinds.html)

[ExpressionEditButtons.GetItem](expressioneditbuttons-getitem.html)

[ExpressionEditButtons.Remove](expressioneditbuttons-remove.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-autosize.html language=enus -->
## TOPIC 05713: StatusBar.AutoSize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-autosize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-autosize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.AutoSize Data Type Boolean Purpose Specifies whether the control places the status bar on the bottom of the parent window, auto-sizes the height of the status bar, and adjusts to match the width of the parent window at run time. Remarks This property has no effect when you edit a fo

### StatusBar.AutoSize

#### Syntax

[StatusBar](statusbar.html).AutoSize

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control places the status bar on the bottom of the parent window, auto-sizes the height of the status bar, and adjusts to match the width of the parent window at run time.

#### Remarks

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-connectionactivity.html language=enus -->
## TOPIC 05714: StatusBar.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To StatusBar Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### StatusBar.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[StatusBar](statusbar.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-dblclick.html language=enus -->
## TOPIC 05715: StatusBar.DblClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-dblclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-dblclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DblClick Applies To StatusBar Purpose Occurs when the user double-clicks the mouse over the control. Remarks Use the StatusBar.HitTest event to determine whether the user double-clicked the mouse on a pane. See Also StatusBar.HitTest

### StatusBar.DblClick

#### Syntax

ControlName_DblClick

#### Applies To

[StatusBar](statusbar.html)

#### Purpose

Occurs when the user double-clicks the mouse over the control.

#### Remarks

Use the
 [StatusBar.HitTest](statusbar-hittest.html)
 event to determine whether the user double-clicked the mouse on a pane.

#### See Also

[StatusBar.HitTest](statusbar-hittest.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-font.html language=enus -->
## TOPIC 05716: StatusBar.Font

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.Font Data Type Font Purpose Specifies the font for the control when the value of the StatusBar.FontSource property is FontSource_UseFontProperty . See Also FontSources StatusBar.FontSource

### StatusBar.Font

#### Syntax

[StatusBar](statusbar.html).Font

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for the control when the value of the
 [StatusBar.FontSource](statusbar-fontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[FontSources](fontsources.html)

[StatusBar.FontSource](statusbar-fontsource.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-fontsource.html language=enus -->
## TOPIC 05717: StatusBar.FontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-fontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-fontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.FontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFont –

### StatusBar.FontSource

#### Syntax

[StatusBar](statusbar.html).FontSource

#### Data Type

[FontSources](fontsources.html)

Use the following constants with this data type:

- FontSource_UseContainerFont 
 –(Value: 2) The font the container supplies.
- FontSource_UseFontProperty 
 –(Value: 0) A corresponding
 Font 
 property of the control determines the font.
- FontSource_UseGUIFont 
 –(Value: 1) The default system font for user interface objects.
- FontSource_UseIconFont 
 –(Value: 5) The system font for an icon title.
- FontSource_UseInactiveTitlebarFont 
 –(Value: 4) The system font for an inactive titlebar.
- FontSource_UseMenuFont 
 –(Value: 6) The system font for a menu.
- FontSource_UseMessageBoxFont 
 –(Value: 7) The system font for a message box.
- FontSource_UsePaletteTitleFont 
 –(Value: 8) The system font for the title of a Tools window.
- FontSource_UseSelectedItemsFont 
 –(Value: 9) The system font for the selected menu items.
- FontSource_UseSystemFixedWidthFont 
 –(Value: 11) The system font for monospaced text.
- FontSource_UseTitlebarFont 
 –(Value: 3) The system font for a title bar.
- FontSource_UseToolTipFont 
 –(Value: 10) The system font for tooltips and status bars.
- FontSource_UseUIStyleFont 
 –(Value: 12) The font the
 UIStyle 
 object supplies.

#### Purpose

Specifies the font the control uses. The default value for this property is
 FontSource_UseGUIFont
 .

#### Remarks

When the value of this property is
 FontSource_UseFontProperty
 , the corresponding
 Font
 property specifies the particular font the control uses. Otherwise, the control uses the font from the source this property specifies.

Set this property to a value other than
 FontSource_UseFontProperty
 if you expect the font the
 [StatusBar.Font](statusbar-font.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[FontSources](fontsources.html)

[StatusBar.Font](statusbar-font.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-general-property-page.html language=enus -->
## TOPIC 05718: StatusBar General Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-general-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-general-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Property Page The General property page contains the following controls: Resize with Parent —The control to place the status bar on the bottom of the parent window, auto-sizes the height of the status bar, and adjusts to match the width of the parent window at run time. Divider on Top —Place

### StatusBar General Property Page

#### General Property Page

The General property page contains the following controls:

- Resize with Parent 
 —The control to place the status bar on the bottom of the parent window, auto-sizes the height of the status bar, and adjusts to match the width of the parent window at run time.
- Divider on Top 
 —Places a visible divider line on the top-most border of the status bar.
- Show Resizing Grip 
 — Enables the resizing grip in the bottom right corner of the control.
 Note 
 Enable this option only when Resize with Parent is enabled and the parent form of the status bar is resizable.
- Icon Size 
 —The size of icons in the status bar. Icons are always square. For example, when you select 32 in the Icon Size control, the icon dimensions are 32 × 32 pixels.
- Font 
 —Changes the font used for the control.
  - Font to Use 
 —The system font to use for the status bar. When you select Use Custom Font for Font to Use, the Custom Font control specifies the font to use.
  - Custom Font 
 —Displays the custom font specified for the status bar. Click the
 Change 
 button to launch the Font dialog box. This option is available only when you select Use Custom Font in the Font to Use control.
 Note 
 The Font dialog box includes a Script ring control. If you change the system language or apply a font selection on a computer with a different language setting, some of the characters in that language might not display in the font you select if the language uses a different script.
  - Change 
 —Launches the Font dialog box, in which you can specify a custom font.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-hittest.html language=enus -->
## TOPIC 05719: StatusBar.HitTest

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-hittest.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-hittest.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.HitTest( x, y) Return Value Long Returns a zero-based item index. You can use this value to retrieve a StatusBarPane object from the StatusBarPanes collection. This method returns -1 when the location is not on a pane. Purpose Returns the index of the pane at the given coordinates.

### StatusBar.HitTest

#### Syntax

[StatusBar](statusbar.html).HitTest( x, y)

#### Return Value

[Long](data-types-for-teststand-user-interface.html)

Returns a zero-based item index. You can use this value to retrieve a
 [StatusBarPane](statusbarpane.html)
 object from the
 [StatusBarPanes](statusbarpanes.html)
 collection. This method returns
 -1
 when the location is not on a pane.

#### Purpose

Returns the index of the pane at the given coordinates.

#### Remarks

Use this method to determine the item to which the given coordinates belong. For example, when a user clicks on the control, you might want to determine the item the user clicked.

#### Parameters

x
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the location to test, in pixels, relative to the control.

y
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the location to test, in pixels, relative to the control.

#### See Also

[StatusBar.Panes](statusbar-panes.html)

[StatusBarPane](statusbarpane.html)

[StatusBarPanes](statusbarpanes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-hwnd.html language=enus -->
## TOPIC 05720: StatusBar.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.hWnd Data Type Long Purpose Returns the Window handle of the StatusBar control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### StatusBar.hWnd

#### Syntax

[StatusBar](statusbar.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the Window handle of the StatusBar control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-iconsize.html language=enus -->
## TOPIC 05721: StatusBar.IconSize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-iconsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-iconsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.IconSize Data Type Long Purpose Specifies the size of the icons in the control. Remarks Icons are always square. For example, when you specify an icon size of 32, the dimensions of the icons in the status bar are 32 × 32 pixels. See Also StatusBarPane.IconName

### StatusBar.IconSize

#### Syntax

[StatusBar](statusbar.html).IconSize

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the size of the icons in the control.

#### Remarks

Icons are always square. For example, when you specify an icon size of 32, the dimensions of the icons in the status bar are 32 × 32 pixels.

#### See Also

[StatusBarPane.IconName](statusbarpane-iconname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-localize.html language=enus -->
## TOPIC 05722: StatusBar.Localize

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-localize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-localize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.Localize( sectionName) Purpose Localizes all the text captions in the StatusBar control. Remarks First, update a .ini file located in the <TestStand Public> \Components\Language directory with the required strings. Second, use the string tags in the .ini file as the pane captions fo

### StatusBar.Localize

#### Syntax

[StatusBar](statusbar.html).Localize( sectionName)

#### Purpose

Localizes all the text captions in the StatusBar control.

#### Remarks

First, update a
 .ini
 file located in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\Language
 directory with the required strings. Second, use the string tags in the
 .ini
 file as the pane captions for the control.

When you call this method, the control replaces the pane captions with the strings from the
 .ini
 file. If a caption is not a tag in the
 .ini
 file, the caption does not change.

Note

#### Parameters

sectionName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the section in the language files that contains the localized text.

#### See Also

[ApplicationMgr.LocalizeAllControls](applicationmgr-localizeallcontrols.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-mousedown.html language=enus -->
## TOPIC 05723: StatusBar.MouseDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-mousedown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-mousedown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseDown( btn, shift, x, y) Applies To StatusBar Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies

### StatusBar.MouseDown

#### Syntax

ControlName_MouseDown( btn, shift, x, y)

#### Applies To

[StatusBar](statusbar.html)

#### Purpose

Occurs when the user clicks the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs..

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

[StatusBar.MouseMove](statusbar-mousemove.html)

[StatusBar.MouseUp](statusbar-mouseup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-mousemove.html language=enus -->
## TOPIC 05724: StatusBar.MouseMove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-mousemove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-mousemove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseMove( btn, shift, x, y) Applies To StatusBar Purpose Occurs when the user moves the mouse over the control. Parameters btn As Integer [In] Specifies what mouse buttons are pressed. You can use any combination of the MouseButtons constants. shift As Integer [In] Specifies a co

### StatusBar.MouseMove

#### Syntax

ControlName_MouseMove( btn, shift, x, y)

#### Applies To

[StatusBar](statusbar.html)

#### Purpose

Occurs when the user moves the mouse over the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies what mouse buttons are pressed. You can use any combination of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

[StatusBar.MouseDown](statusbar-mousedown.html)

[StatusBar.MouseUp](statusbar-mouseup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-mouseup.html language=enus -->
## TOPIC 05725: StatusBar.MouseUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-mouseup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-mouseup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseUp( btn, shift, x, y) Applies To StatusBar Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies a

### StatusBar.MouseUp

#### Syntax

ControlName_MouseUp( btn, shift, x, y)

#### Applies To

[StatusBar](statusbar.html)

#### Purpose

Occurs when the user clicks the mouse on the control.

#### Parameters

btn
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the mouse button pressed to cause this event. You can use any one of the
 [MouseButtons](mousebuttons.html)
 constants.

shift
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies a combination of the
 [KeyModifiers](keymodifiers.html)
 constants that specifies the state of the <Shift>, <Ctrl>, and <Alt> keys.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the x-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the y-coordinate of the mouse pointer, relative to the control, at the moment when the event occurs.

#### See Also

[KeyModifiers](keymodifiers.html)

[MouseButtons](mousebuttons.html)

[StatusBar.MouseDown](statusbar-mousedown.html)

[StatusBar.MouseMove](statusbar-mousemove.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-panes-property-page.html language=enus -->
## TOPIC 05726: StatusBar Panes Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-panes-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-panes-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Panes Property Page Use the Panes property page to create and configure StatusBar panes. Each StatusBar pane must have a unique name. The Panes property page contains the following controls: Panes List —Displays a list of the existing panes. Add —Adds a new pane with a unique default name. Remove —R

### StatusBar Panes Property Page

#### Panes Property Page

Use the Panes property page to create and configure
 StatusBar
 panes. Each
 StatusBar
 pane must have a unique name.

The Panes property page contains the following controls:

- Panes List 
 —Displays a list of the existing panes.
  - Add 
 —Adds a new pane with a unique default name.
  - Remove 
 —Removes the selected pane.
  - Up 
 —Moves the selected pane up one position.
  - Down 
 —Moves the selected pane down one position.
- Pane Properties 
 —This section contains the following options:
  - Caption 
 —The text that displays on the pane.
  - Width 
 —The width of the pane, in pixels.
  - Name 
 —The name of the pane.
 Note 
 The name of a each pane must be unique.
  - Style 
 —The visual appearance of the pane. The Style ring control contains the following options:
    - Etched 
 —The pane has an etched border, with a sunken outer edge and a raised inner edge.
    - Flat 
 —The pane is flat and has no borders.
    - Raised 
 —The pane has a raised border.
  - Alignment 
 —The alignment of the text in the pane. Text can be left-aligned, right-aligned, or centered.
  - Visible 
 —The pane is visible initially.
  - Use Available Space 
 —When you enable this option, the pane expands or shrinks, regardless of the Width property, to use all available space on the control. When you have more than one visible pane with Use Available Space enabled, only the leftmost pane honors the setting.

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-panes.html language=enus -->
## TOPIC 05727: StatusBar.Panes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-panes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-panes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.Panes Data Type StatusBarPanes Purpose Returns the StatusBarPanes collection. See Also StatusBarPanes

### StatusBar.Panes

#### Syntax

[StatusBar](statusbar.html).Panes

#### Data Type

[StatusBarPanes](statusbarpanes.html)

#### Purpose

Returns the
 [StatusBarPanes](statusbarpanes.html)
 collection.

#### See Also

[StatusBarPanes](statusbarpanes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-resized.html language=enus -->
## TOPIC 05728: StatusBar.Resized

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-resized.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-resized.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Resized( newWidth, newHeight) Applies To StatusBar Purpose Occurs when a status bar is resized. This occurs only when you set the StatusBar.AutoSize property to True and resize the parent window. Parameters newWidth As Integer [In] Specifies the new width of the status bar, in pix

### StatusBar.Resized

#### Syntax

ControlName_Resized( newWidth, newHeight)

#### Applies To

[StatusBar](statusbar.html)

#### Purpose

Occurs when a status bar is resized. This occurs only when you set the
 [StatusBar.AutoSize](statusbar-autosize.html)
 property to
 True
 and resize the parent window.

#### Parameters

newWidth
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the new width of the status bar, in pixels.

newHeight
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the new height of the status bar, in pixels.

#### See Also

[StatusBar.AutoSize](statusbar-autosize.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-scalewithdpi.html language=enus -->
## TOPIC 05729: StatusBar.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are de

### StatusBar.ScaleWithDPI

#### Syntax

[StatusBar](statusbar.html).ScaleWithDPI

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies how the control scales based on the dots per inch (DPI) setting.

#### Remarks

Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are designed to work in all environments.

The following are the recommended settings for various platforms:

- LabVIEW, LabWindows/CVI, C#, and Microsoft Visual Basic .NET—Set this property to
 False 
 .
- Active Template Library (ATL)/Microsoft Foundation Class (MFC)—Set this property to
 True 
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-showpanes.html language=enus -->
## TOPIC 05730: StatusBar.ShowPanes

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-showpanes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-showpanes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.ShowPanes( panesList) Purpose Shows the list of panes and hides any panes not in the list. Remarks Use this method to switch between sets of visible panes. Parameters panesList As String [In] Specifies a comma-separated list of pane names. For example, " pane1, pane2, pane3 ". See A

### StatusBar.ShowPanes

#### Syntax

[StatusBar](statusbar.html).ShowPanes( panesList)

#### Purpose

Shows the list of panes and hides any panes not in the list.

#### Remarks

Use this method to switch between sets of visible panes.

#### Parameters

panesList
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies a comma-separated list of pane names. For example, "
 pane1, pane2, pane3
 ".

#### See Also

[StatusBarPane.Visible](statusbarpane-visible.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-showresizinggrip.html language=enus -->
## TOPIC 05731: StatusBar.ShowResizingGrip

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-showresizinggrip.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-showresizinggrip.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.ShowResizingGrip Data Type Boolean Purpose Specifies to enable the resizing grip on the bottom right corner of the control. Remarks Enable this property only when the window on which you place the StatusBar control is resizable and when the StatusBar.AutoSize property is True . See

### StatusBar.ShowResizingGrip

#### Syntax

[StatusBar](statusbar.html).ShowResizingGrip

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies to enable the resizing grip on the bottom right corner of the control.

#### Remarks

Note

StatusBar.AutoSize

True

#### See Also

[StatusBar.AutoSize](statusbar-autosize.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar-showtopdivider.html language=enus -->
## TOPIC 05732: StatusBar.ShowTopDivider

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar-showtopdivider.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar-showtopdivider.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBar.ShowTopDivider Data Type Boolean Purpose Specifies whether the StatusBar control displays a horizontal line as the top border. Remarks When the application supports themes using Microsoft Windows XP, this property has no visual effect.

### StatusBar.ShowTopDivider

#### Syntax

[StatusBar](statusbar.html).ShowTopDivider

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the StatusBar control displays a horizontal line as the top border.

#### Remarks

When the application supports themes using Microsoft Windows XP, this property has no visual effect.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbar.html language=enus -->
## TOPIC 05733: StatusBar

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a manager control to panes of a StatusBar control to display text, image, or progress information about the application state. You can programmatically control individual StatusBar panes to display custom information. You can connect the panes to CaptionSources , NumericSources , and ImageSo

### StatusBar

Connect a manager control to panes of a StatusBar control to display text, image, or progress information about the application state. You can programmatically control individual
 StatusBar
 panes to display custom information.

You can connect the panes to
 [CaptionSources](captionsources.html)
 ,
 [NumericSources](numericsources.html)
 , and
 [ImageSources](imagesources.html)
 on the
 [Application Manager](applicationmgr.html)
 ,
 [ExecutionView Manager](executionviewmgr.html)
 , and
 [SequenceFileView Manager](sequencefileviewmgr.html)
 controls.

#### Properties

| AutoSize |
| --- |
| Font |
| FontSource |
| hWnd (Read Only) |
| IconSize |
| Panes (Read Only) |
| ScaleWithDPI |
| ShowResizingGrip |
| ShowTopDivider |

#### Methods

| HitTest |
| --- |
| Localize |
| ShowPanes |

#### Events

| ConnectionActivity |
| --- |
| DblClick |
| MouseDown |
| MouseMove |
| MouseUp |
| Resized |

#### See Also

[ApplicationMgr](applicationmgr.html)

[CaptionSources](captionsources.html)

[ExecutionViewMgr](executionviewmgr.html)

[ImageSources](imagesources.html)

[NumericSources](numericsources.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-caption.html language=enus -->
## TOPIC 05734: StatusBarPane.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.Caption Data Type String Purpose Specifies the caption for the StatusBar pane. Remarks You can display a caption and progress bar on the same StatusBar pane. When you connect a StatusBar pane to the caption source of a manager control, you cannot change the caption. When you con

### StatusBarPane.Caption

#### Syntax

[StatusBarPane](statusbarpane.html).Caption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the caption for the StatusBar pane.

#### Remarks

You can display a caption and progress bar on the same StatusBar pane.

Note

StatusBarPane.IconName

#### See Also

[StatusBarPane.IconName](statusbarpane-iconname.html)

[StatusBarPane.Name](statusbarpane-name.html)

[StatusBarPane.ProcessPercent](statusbarpane-processpercent.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-iconname.html language=enus -->
## TOPIC 05735: StatusBarPane.IconName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-iconname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-iconname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.IconName Data Type String Purpose Specifies an icon for the StatusBar pane. Remarks TestStand User Interface Controls use icons from the <TestStand> \Components\Icons and <TestStand Public> \Components\Icons directories. To specify an icon for a StatusBar pane, pass the name of

### StatusBarPane.IconName

#### Syntax

[StatusBarPane](statusbarpane.html).IconName

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies an icon for the StatusBar pane.

#### Remarks

TestStand User Interface Controls use icons from the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 directories. To specify an icon for a StatusBar pane, pass the name of the
 .ico
 file to this property.

Note

#### See Also

[StatusBarPane.Caption](statusbarpane-caption.html)

[StatusBarPane.ProcessPercent](statusbarpane-processpercent.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-index.html language=enus -->
## TOPIC 05736: StatusBarPane.Index

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-index.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-index.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.Index Data Type Long Purpose Returns the zero-based index of the pane in the StatusBarPanes collection. See Also StatusBarPanes

### StatusBarPane.Index

#### Syntax

[StatusBarPane](statusbarpane.html).Index

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the zero-based index of the pane in the
 [StatusBarPanes](statusbarpanes.html)
 collection.

#### See Also

[StatusBarPanes](statusbarpanes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-name.html language=enus -->
## TOPIC 05737: StatusBarPane.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.Name Data Type String Purpose Specifies the name for the pane. Remarks Every pane must have a unique name, which can be used to identify the pane within the StatusBarPanes collection. Pane names are not case-sensitive. See Also StatusBarPane.Caption StatusBarPane.Index StatusBar

### StatusBarPane.Name

#### Syntax

[StatusBarPane](statusbarpane.html).Name

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the name for the pane.

#### Remarks

Every pane must have a unique name, which can be used to identify the pane within the
 [StatusBarPanes](statusbarpanes.html)
 collection. Pane names are not case-sensitive.

#### See Also

[StatusBarPane.Caption](statusbarpane-caption.html)

[StatusBarPane.Index](statusbarpane-index.html)

[StatusBarPanes](statusbarpanes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-processpercent.html language=enus -->
## TOPIC 05738: StatusBarPane.ProcessPercent

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-processpercent.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-processpercent.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.ProcessPercent Data Type Double Purpose Specifies a number between 0 and 100 to determine the progress for the StatusBar pane. The StatusBar pane uses this number to draw a progress bar. Remarks You can combine a caption, image, and progress bar on the same StatusBar pane. Set P

### StatusBarPane.ProcessPercent

#### Syntax

[StatusBarPane](statusbarpane.html).ProcessPercent

#### Data Type

[Double](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a number between 0 and 100 to determine the progress for the StatusBar pane. The StatusBar pane uses this number to draw a progress bar.

#### Remarks

You can combine a caption, image, and progress bar on the same StatusBar pane. Set ProcessPercent to
 0
 when you do not want the StatusBar pane to contain a progress bar.

Note

#### See Also

[StatusBarPane.Caption](statusbarpane-caption.html)

[StatusBarPane.IconName](statusbarpane-iconname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-style.html language=enus -->
## TOPIC 05739: StatusBarPane.Style

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-style.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-style.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.Style Data Type StatusBarPaneStyles Use the following constants with this data type: StatusBarPaneStyle_Etched –(Value: 1) The pane has an etched border, with a sunken outer edge and a raised inner edge. StatusBarPaneStyle_Flat –(Value: 2) The pane is flat and has no border. Sta

### StatusBarPane.Style

#### Syntax

[StatusBarPane](statusbarpane.html).Style

#### Data Type

[StatusBarPaneStyles](statusbarpanestyles.html)

Use the following constants with this data type:

- StatusBarPaneStyle_Etched 
 –(Value: 1) The pane has an etched border, with a sunken outer edge and a raised inner edge.
- StatusBarPaneStyle_Flat 
 –(Value: 2) The pane is flat and has no border.
- StatusBarPaneStyle_Raised 
 –(Value: 3) The pane has a raised border.

#### Purpose

Specifies the appearance of the pane.

#### Remarks

A StatusBar pane can have only one style.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-textalignment.html language=enus -->
## TOPIC 05740: StatusBarPane.TextAlignment

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-textalignment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-textalignment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.TextAlignment Data Type AlignmentStyles Use the following constants with this data type: AlignmentStyle_Center –(Value: 2) Text is centered. AlignmentStyle_LeftJustify –(Value: 0) Text is left-aligned. AlignmentStyle_RightJustify –(Value: 1) Text is right-aligned. Purpose Specif

### StatusBarPane.TextAlignment

#### Syntax

[StatusBarPane](statusbarpane.html).TextAlignment

#### Data Type

[AlignmentStyles](alignmentstyles.html)

Use the following constants with this data type:

- AlignmentStyle_Center 
 –(Value: 2) Text is centered.
- AlignmentStyle_LeftJustify 
 –(Value: 0) Text is left-aligned.
- AlignmentStyle_RightJustify 
 –(Value: 1) Text is right-aligned.

#### Purpose

Specifies the alignment of the caption text.

#### Remarks

This method also applies to images when the StatusBar control is used to display images.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-tooltiptext.html language=enus -->
## TOPIC 05741: StatusBarPane.ToolTipText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-tooltiptext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-tooltiptext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.ToolTipText Data Type String Purpose Specifies the tooltip for a status bar pane. When this property is an empty string, the pane uses the StatusBarPane.Caption property for the tooltip. See Also StatusBarPane.Caption

### StatusBarPane.ToolTipText

#### Syntax

[StatusBarPane](statusbarpane.html).ToolTipText

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the tooltip for a status bar pane. When this property is an empty string, the pane uses the
 [StatusBarPane.Caption](statusbarpane-caption.html)
 property for the tooltip.

#### See Also

[StatusBarPane.Caption](statusbarpane-caption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-useavailablespace.html language=enus -->
## TOPIC 05742: StatusBarPane.UseAvailableSpace

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-useavailablespace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-useavailablespace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.UseAvailableSpace Data Type Boolean Purpose Set this property to True when you want a StatusBar pane to occupy all available space in the status bar not used by other panes. This property enables a pane to adjust to make full use of the available space when the status bar change

### StatusBarPane.UseAvailableSpace

#### Syntax

[StatusBarPane](statusbarpane.html).UseAvailableSpace

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Set this property to
 True
 when you want a StatusBar pane to occupy all available space in the status bar not used by other panes. This property enables a pane to adjust to make full use of the available space when the status bar changes size.

#### Remarks

Although you can have more than one StatusBar pane with a value of
 True
 for this property, only the leftmost visible StatusBar pane honors this setting.

#### See Also

[StatusBarPane.Width](statusbarpane-width.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-visible.html language=enus -->
## TOPIC 05743: StatusBarPane.Visible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-visible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-visible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.Visible Data Type Boolean Purpose Specifies whether the StatusBar pane is visible. See Also StatusBar.ShowPanes

### StatusBarPane.Visible

#### Syntax

[StatusBarPane](statusbarpane.html).Visible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the StatusBar pane is visible.

#### See Also

[StatusBar.ShowPanes](statusbar-showpanes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane-width.html language=enus -->
## TOPIC 05744: StatusBarPane.Width

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane-width.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane-width.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPane.Width Data Type Long Purpose Specifies the width for the pane in pixels. Remarks When you set the StatusBarPane.UseAvailableSpace property to True , the specified width of the pane is ignored when the StatusBar pane is the leftmost visible StatusBar pane with a True value for th

### StatusBarPane.Width

#### Syntax

[StatusBarPane](statusbarpane.html).Width

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the width for the pane in pixels.

#### Remarks

When you set the
 [StatusBarPane.UseAvailableSpace](statusbarpane-useavailablespace.html)
 property to
 True
 , the specified width of the pane is ignored when the StatusBar pane is the leftmost visible StatusBar pane with a
 True
 value for the
 StatusBarPane.UseAvailableSpace
 property.

#### See Also

[StatusBarPane.UseAvailableSpace](statusbarpane-useavailablespace.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpane.html language=enus -->
## TOPIC 05745: StatusBarPane

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a status bar pane. Properties Caption IconName Index (Read Only) Name ProcessPercent Style TextAlignment ToolTipText UseAvailableSpace Visible Width

### StatusBarPane

Represents a status bar pane.

#### Properties

| Caption |
| --- |
| IconName |
| Index (Read Only) |
| Name |
| ProcessPercent |
| Style |
| TextAlignment |
| ToolTipText |
| UseAvailableSpace |
| Visible |
| Width |

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpanes-clear.html language=enus -->
## TOPIC 05746: StatusBarPanes.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpanes-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpanes-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPanes.Clear Purpose Removes all items from the collection. See Also StatusBarPanes.Remove

### StatusBarPanes.Clear

#### Syntax

[StatusBarPanes](statusbarpanes.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[StatusBarPanes.Remove](statusbarpanes-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpanes-count.html language=enus -->
## TOPIC 05747: StatusBarPanes.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpanes-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpanes-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPanes.Count Data Type Long Purpose Returns the number of items in the collection. See Also StatusBarPane

### StatusBarPanes.Count

#### Syntax

[StatusBarPanes](statusbarpanes.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[StatusBarPane](statusbarpane.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpanes-insert.html language=enus -->
## TOPIC 05748: StatusBarPanes.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpanes-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpanes-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPanes.Insert( paneName, insertBefore) Return Value StatusBarPane Specifies the name of the new StatusBar pane. This name must be unique and is not case-sensitive. Purpose Adds a new item to the collection and returns the new StatusBarPane object. Parameters paneName As String [In] Sp

### StatusBarPanes.Insert

#### Syntax

[StatusBarPanes](statusbarpanes.html).Insert( paneName, insertBefore)

#### Return Value

[StatusBarPane](statusbarpane.html)

Specifies the name of the new StatusBar pane. This name must be unique and is not case-sensitive.

#### Purpose

Adds a new item to the collection and returns the new
 [StatusBarPane](statusbarpane.html)
 object.

#### Parameters

paneName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the new StatusBar pane.

insertBefore
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the existing StatusBar pane before which the new StatusBar pane is inserted. To insert at the end, pass
 -1
 to this parameter.

#### See Also

[StatusBarPane](statusbarpane.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpanes-item.html language=enus -->
## TOPIC 05749: StatusBarPanes.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpanes-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpanes-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPanes.Item( paneIndex) Data Type StatusBarPane Purpose Returns a reference to an item with the specified name or at the specified index in the collection. Parameters paneIndex As Variant [In] Specifies a number to obtain a StatusBar pane by the zero-based index. Pass a string to obta

### StatusBarPanes.Item

#### Syntax

[StatusBarPanes](statusbarpanes.html).Item( paneIndex)

#### Data Type

[StatusBarPane](statusbarpane.html)

#### Purpose

Returns a reference to an item with the specified name or at the specified index in the collection.

#### Parameters

paneIndex
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] Specifies a number to obtain a StatusBar pane by the zero-based index. Pass a string to obtain the StatusBar pane using the name.

#### See Also

[StatusBarPane](statusbarpane.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/statusbarpanes-remove.html language=enus -->
## TOPIC 05750: StatusBarPanes.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/statusbarpanes-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/statusbarpanes-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StatusBarPanes.Remove( paneIndex) Purpose Removes the specified item from this collection, if it exists. Parameters paneIndex As Variant [In] Specifies a number to remove a StatusBar pane by the zero-based index. Pass a string to remove a StatusBar pane using the name. See Also StatusBarPanes

### StatusBarPanes.Remove

#### Syntax

[StatusBarPanes](statusbarpanes.html).Remove( paneIndex)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

paneIndex
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] Specifies a number to remove a StatusBar pane by the zero-based index. Pass a string to remove a StatusBar pane using the name.

#### See Also

[StatusBarPanes.Clear](statusbarpanes-clear.html)

Parent topic:

Methods
