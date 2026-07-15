# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=5251 end=5500 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpage-caption.html language=enus -->
## TOPIC 05251: ListBarPage.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpage-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpage-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPage.Caption Data Type String Purpose Specifies the caption text of the page. See Also ListBarPage.Name

### ListBarPage.Caption

#### Syntax

[ListBarPage](listbarpage.html).Caption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the caption text of the page.

#### See Also

[ListBarPage.Name](listbarpage-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpage-cursor.html language=enus -->
## TOPIC 05252: ListBarPage.Cursor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpage-cursor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpage-cursor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPage.Cursor Data Type Long Purpose Specifies the zero-based index of the item the cursor selects. Remarks Use this property to obtain the position of the cursor or move the cursor on the page. See Also ListBar.CurrentPage ListBar.CursorMoved

### ListBarPage.Cursor

#### Syntax

[ListBarPage](listbarpage.html).Cursor

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the zero-based index of the item the cursor selects.

#### Remarks

Use this property to obtain the position of the cursor or move the cursor on the page.

#### See Also

[ListBar.CurrentPage](listbar-currentpage.html)

[ListBar.CursorMoved](listbar-cursormoved.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpage-enabled.html language=enus -->
## TOPIC 05253: ListBarPage.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpage-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpage-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPage.Enabled Data Type Boolean Purpose Specifies to enable or disable the ListBarPage. Remarks Users cannot move the cursor when the page is disabled.

### ListBarPage.Enabled

#### Syntax

[ListBarPage](listbarpage.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies to enable or disable the ListBarPage.

#### Remarks

Users cannot move the cursor when the page is disabled.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpage-index.html language=enus -->
## TOPIC 05254: ListBarPage.Index

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpage-index.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpage-index.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPage.Index Data Type Long Purpose Returns the numeric zero-based index of the page within the ListBarPages collection. See Also ListBar.CurrentPage ListBar.Pages ListBarPages ListBarPages.Item

### ListBarPage.Index

#### Syntax

[ListBarPage](listbarpage.html).Index

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the numeric zero-based index of the page within the
 [ListBarPages](listbarpages.html)
 collection.

#### See Also

[ListBar.CurrentPage](listbar-currentpage.html)

[ListBar.Pages](listbar-pages.html)

[ListBarPages](listbarpages.html)

[ListBarPages.Item](listbarpages-item.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpage-items.html language=enus -->
## TOPIC 05255: ListBarPage.Items

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpage-items.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpage-items.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPage.Items Data Type ListBarPageItems Purpose Returns a collection of items on the page. Remarks Use this property to obtain a ListBarPageItems collection, which you can use to iterate through all the items on the page. See Also ListBarPage.Cursor ListBarPageItems

### ListBarPage.Items

#### Syntax

[ListBarPage](listbarpage.html).Items

#### Data Type

[ListBarPageItems](listbarpageitems.html)

#### Purpose

Returns a collection of items on the page.

#### Remarks

Use this property to obtain a
 [ListBarPageItems](listbarpageitems.html)
 collection, which you can use to iterate through all the items on the page.

#### See Also

[ListBarPage.Cursor](listbarpage-cursor.html)

[ListBarPageItems](listbarpageitems.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpage-name.html language=enus -->
## TOPIC 05256: ListBarPage.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpage-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpage-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPage.Name Data Type String Purpose Specifies the name of the ListBarPage. Remarks Every ListBarPage must have a unique name, which can be used to identify the ListBarPage within the ListBarPages collection. ListBarPage names are not case-sensitive. See Also ListBarPage.Caption ListBarP

### ListBarPage.Name

#### Syntax

[ListBarPage](listbarpage.html).Name

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the name of the ListBarPage.

#### Remarks

Every ListBarPage must have a unique name, which can be used to identify the ListBarPage within the
 [ListBarPages](listbarpages.html)
 collection. ListBarPage names are not case-sensitive.

#### See Also

[ListBarPage.Caption](listbarpage-caption.html)

[ListBarPages](listbarpages.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpage.html language=enus -->
## TOPIC 05257: ListBarPage

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a SequenceFileView Manager or ExecutionView Manager control to a ListBarPage object so users can iterate through the items in the page and set the cursor, caption, and name of the page. Use the ListBarPages.Insert method to create a new ListBarPage object. Use the ListBarPage.Cursor property

### ListBarPage

Connect a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 or
 [ExecutionView Manager](executionviewmgr.html)
 control to a ListBarPage object so users can iterate through the items in the page and set the cursor, caption, and name of the page.

Use the
 [ListBarPages.Insert](listbarpages-insert.html)
 method to create a new ListBarPage object. Use the
 [ListBarPage.Cursor](listbarpage-cursor.html)
 property to determine the selected item in the page.

Use the ListBarPage control to connect to and display the
 [ExecutionViewMgrConnections.ExecutionList](executionviewmgrconnections-executionlist.html)
 ,
 [ExecutionViewMgrConnections.CallStack](executionviewmgrconnections-callstack.html)
 , and
 [ExecutionViewMgrConnections.ThreadList](executionviewmgrconnections-threadlist.html)
 properties in the ExecutionView Manager control and the
 [SequenceFileViewMgrConnections.SequenceList](sequencefileviewmgrconnections-sequencelist.html)
 ,
 [SequenceFileViewMgrConnections.SequenceFileList](sequencefileviewmgrconnections-sequencefileli.html)
 , and
 [SequenceFileViewMgrConnections.StepGroupList](sequencefileviewmgrconnections-stepgrouplist.html)
 properties in the SequenceFileView Manager control.

#### Properties

| Caption |
| --- |
| Cursor |
| Enabled |
| Index (Read Only) |
| Items (Read Only) |
| Name |

#### See Also

[ExecutionViewMgr.ConnectCallStack](executionviewmgr-connectcallstack.html)

[ExecutionViewMgr.ConnectExecutionList](executionviewmgr-connectexecutionlist.html)

[ExecutionViewMgr.ConnectThreadList](executionviewmgr-connectthreadlist.html)

[ListBar.CurrentPage](listbar-currentpage.html)

[ListBarPage.Cursor](listbarpage-cursor.html)

[ListBarPages.Insert](listbarpages-insert.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

[SequenceFileViewMgr.ConnectStepGroupList](sequencefileviewmgr-connectstepgrouplist.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitem-caption.html language=enus -->
## TOPIC 05258: ListBarPageItem.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitem-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitem-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItem.Caption Data Type String Purpose Specifies the caption for an item. Remarks When you connect a ListBarPage to a manager control, the ListBarPage becomes read-only. Attempting to change the caption of an item in the page results in an error.

### ListBarPageItem.Caption

#### Syntax

[ListBarPageItem](listbarpageitem.html).Caption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the caption for an item.

#### Remarks

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitem-iconname.html language=enus -->
## TOPIC 05259: ListBarPageItem.IconName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitem-iconname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitem-iconname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItem.IconName Data Type String Purpose Specifies the icon name for an item. Remarks TestStand User Interface Controls use the icon files in the <TestStand> \Components\Icons and <TestStand Public> \Components\Icons directories. To change an icon for any item, specify the name of th

### ListBarPageItem.IconName

#### Syntax

[ListBarPageItem](listbarpageitem.html).IconName

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the icon name for an item.

#### Remarks

TestStand User Interface Controls use the icon files in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 directories. To change an icon for any item, specify the name of the .ico file.

Note

ListBarPage

#### See Also

[ListBarPage](listbarpage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitem-index.html language=enus -->
## TOPIC 05260: ListBarPageItem.Index

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitem-index.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitem-index.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItem.Index Data Type Long Purpose Returns the zero-based index of an item. See Also ListBarPageItems.Item

### ListBarPageItem.Index

#### Syntax

[ListBarPageItem](listbarpageitem.html).Index

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the zero-based index of an item.

#### See Also

[ListBarPageItems.Item](listbarpageitems-item.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitem-tooltiptext.html language=enus -->
## TOPIC 05261: ListBarPageItem.ToolTipText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitem-tooltiptext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitem-tooltiptext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItem.ToolTipText Data Type String Purpose Specifies the tooltip for an item. When this property is an empty string, the item uses the ListBarPageItem.Caption property for the tooltip. See Also ListBarPageItem.Caption

### ListBarPageItem.ToolTipText

#### Syntax

[ListBarPageItem](listbarpageitem.html).ToolTipText

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the tooltip for an item. When this property is an empty string, the item uses the
 [ListBarPageItem.Caption](listbarpageitem-caption.html)
 property for the tooltip.

#### See Also

[ListBarPageItem.Caption](listbarpageitem-caption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitem.html language=enus -->
## TOPIC 05262: ListBarPageItem

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an item in the ListBarPage . Properties Caption IconName Index (Read Only) ToolTipText See Also ListBarPage ListBarPage.Cursor

### ListBarPageItem

Represents an item in the
 [ListBarPage](listbarpage.html)
 .

#### Properties

| Caption |
| --- |
| IconName |
| Index (Read Only) |
| ToolTipText |

#### See Also

[ListBarPage](listbarpage.html)

[ListBarPage.Cursor](listbarpage-cursor.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitems-clear.html language=enus -->
## TOPIC 05263: ListBarPageItems.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitems-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitems-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItems.Clear Purpose Removes all items from the collection. Remarks When the ListBarPage object is connected to a manager control, you cannot remove any items from the page. See Also ListBarPage ListBarPageItems.Insert ListBarPageItems.Remove

### ListBarPageItems.Clear

#### Syntax

[ListBarPageItems](listbarpageitems.html).Clear

#### Purpose

Removes all items from the collection.

#### Remarks

Note

#### See Also

[ListBarPage](listbarpage.html)

[ListBarPageItems.Insert](listbarpageitems-insert.html)

[ListBarPageItems.Remove](listbarpageitems-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitems-count.html language=enus -->
## TOPIC 05264: ListBarPageItems.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitems-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitems-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItems.Count Data Type Long Purpose Returns the number of items in the collection.

### ListBarPageItems.Count

#### Syntax

[ListBarPageItems](listbarpageitems.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitems-insert.html language=enus -->
## TOPIC 05265: ListBarPageItems.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitems-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitems-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItems.Insert( itemCaption, iconName, insertBefore) Return Value ListBarPageItem Purpose Inserts a new item into the ListBarPage. Remarks When you connect a ListBarPage to a manager control, the ListBarPage becomes read-only. Attempting to change the content by calling this method r

### ListBarPageItems.Insert

#### Syntax

[ListBarPageItems](listbarpageitems.html).Insert( itemCaption, iconName, insertBefore)

#### Return Value

[ListBarPageItem](listbarpageitem.html)

#### Purpose

Inserts a new item into the ListBarPage.

#### Remarks

Note

#### Parameters

itemCaption
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the caption for the new item.

iconName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name of the icon for the new item. Refer to the
 [ListBarPageItem.IconName](listbarpageitem-iconname.html)
 property for more information about naming icons for an item. Icon files are located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 directories.

insertBefore
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the existing item before which the new item is inserted. Pass
 -1
 to insert the item at the end.

#### See Also

[ListBarPageItem.IconName](listbarpageitem-iconname.html)

[ListBarPageItems.Clear](listbarpageitems-clear.html)

[ListBarPageItems.Remove](listbarpageitems-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitems-item.html language=enus -->
## TOPIC 05266: ListBarPageItems.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitems-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitems-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItems.Item( itemIdx) Data Type ListBarPageItem Purpose Returns a reference to an item with the specified name or at the specified index in the collection. Parameters itemIdx As Variant [In] You can pass a number to obtain a page item by its index value. You can also pass a string t

### ListBarPageItems.Item

#### Syntax

[ListBarPageItems](listbarpageitems.html).Item( itemIdx)

#### Data Type

[ListBarPageItem](listbarpageitem.html)

#### Purpose

Returns a reference to an item with the specified name or at the specified index in the collection.

#### Parameters

itemIdx
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] You can pass a number to obtain a page item by its index value. You can also pass a string to obtain the page item using its name.

#### See Also

[ListBarPageItem](listbarpageitem.html)

[ListBarPageItems.Count](listbarpageitems-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitems-remove.html language=enus -->
## TOPIC 05267: ListBarPageItems.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitems-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitems-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPageItems.Remove( itemIdx) Purpose Use this method to delete an item on the page. Remarks This method takes the numeric index of an item. When the ListBarPage is connected to a manager control, you cannot remove any items from the page. Parameters itemIdx As Long [In] Specifies the zer

### ListBarPageItems.Remove

#### Syntax

[ListBarPageItems](listbarpageitems.html).Remove( itemIdx)

#### Purpose

Use this method to delete an item on the page.

#### Remarks

This method takes the numeric index of an item.

Note

ListBarPage

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to remove.

#### See Also

[ListBarPage](listbarpage.html)

[ListBarPageItems.Clear](listbarpageitems-clear.html)

[ListBarPageItems.Insert](listbarpageitems-insert.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpageitems.html language=enus -->
## TOPIC 05268: ListBarPageItems

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpageitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpageitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ListBarPageItem objects. Use the ListBarPage.Items property to retrieve a ListBarPageItems object. Use the ListBarPage.Cursor property to determine the selected item in the page. Properties Count (Read Only) Item (Read Only) Methods Clear Insert Remove See Also ListBarPage.Cursor Lis

### ListBarPageItems

A collection of
 [ListBarPageItem](listbarpageitem.html)
 objects.

Use the
 [ListBarPage.Items](listbarpage-items.html)
 property to retrieve a ListBarPageItems object. Use the
 [ListBarPage.Cursor](listbarpage-cursor.html)
 property to determine the selected item in the page.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Insert |
| Remove |

#### See Also

[ListBarPage.Cursor](listbarpage-cursor.html)

[ListBarPage.Items](listbarpage-items.html)

[ListBarPageItem](listbarpageitem.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpages-clear.html language=enus -->
## TOPIC 05269: ListBarPages.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpages-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpages-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPages.Clear Purpose Removes all items from the collection. See Also ListBarPages.Remove

### ListBarPages.Clear

#### Syntax

[ListBarPages](listbarpages.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[ListBarPages.Remove](listbarpages-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpages-count.html language=enus -->
## TOPIC 05270: ListBarPages.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpages-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpages-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPages.Count Data Type Long Purpose Returns the number of items in the collection. See Also ListBarPage

### ListBarPages.Count

#### Syntax

[ListBarPages](listbarpages.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[ListBarPage](listbarpage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpages-insert.html language=enus -->
## TOPIC 05271: ListBarPages.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpages-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpages-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPages.Insert( pageName, insertBefore) Return Value ListBarPage Purpose Adds a new item to the collection and returns a reference to the new ListBarPage. Parameters pageName As String [In] Specifies the name for the new ListBarPage. ListBarPage names must be unique. ListBarPage names ar

### ListBarPages.Insert

#### Syntax

[ListBarPages](listbarpages.html).Insert( pageName, insertBefore)

#### Return Value

[ListBarPage](listbarpage.html)

#### Purpose

Adds a new item to the collection and returns a reference to the new ListBarPage.

#### Parameters

pageName
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the name for the new ListBarPage. ListBarPage names must be unique. ListBarPage names are not case-sensitive.

insertBefore
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the existing ListBarPage before which the new ListBarPage is inserted. To insert the new ListBarPage at the end, pass
 -1
 to this parameter.

#### See Also

[ListBarPage](listbarpage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpages-item.html language=enus -->
## TOPIC 05272: ListBarPages.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpages-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpages-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPages.Item( itemIdx) Data Type ListBarPage Purpose Returns a reference to an item with the specified name or at the specified index in the collection. Parameters itemIdx As Variant [In] You can pass a number to obtain a page by its zero-based index. You can also pass a string to obtain

### ListBarPages.Item

#### Syntax

[ListBarPages](listbarpages.html).Item( itemIdx)

#### Data Type

[ListBarPage](listbarpage.html)

#### Purpose

Returns a reference to an item with the specified name or at the specified index in the collection.

#### Parameters

itemIdx
 As
 [Variant](data-types-for-teststand-user-interface.html)

[In] You can pass a number to obtain a page by its zero-based index. You can also pass a string to obtain the ListBarPage using its name.

#### See Also

[ListBarPage](listbarpage.html)

[ListBarPages.Insert](listbarpages-insert.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpages-remove.html language=enus -->
## TOPIC 05273: ListBarPages.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpages-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpages-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBarPages.Remove( itemIdx) Purpose Removes the specified item from this collection, if it exists. Parameters itemIdx As Long [In] Pass the zero-based index for the page to remove. See Also ListBarPages.Clear

### ListBarPages.Remove

#### Syntax

[ListBarPages](listbarpages.html).Remove( itemIdx)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Pass the zero-based index for the page to remove.

#### See Also

[ListBarPages.Clear](listbarpages-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpages.html language=enus -->
## TOPIC 05274: ListBarPages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ListBarPage objects. Use the ListBar.Pages property to retrieve the ListBarPages object for a ListBar. Use the ListBar.CurrentPage property as an index to this collection to access the currently selected page. Properties Count (Read Only) Item (Read Only) Methods Clear Insert Remove

### ListBarPages

A collection of ListBarPage objects.

Use the
 [ListBar.Pages](listbar-pages.html)
 property to retrieve the ListBarPages object for a ListBar. Use the
 [ListBar.CurrentPage](listbar-currentpage.html)
 property as an index to this collection to access the currently selected page.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Insert |
| Remove |

#### See Also

[ListBar.CurrentPage](listbar-currentpage.html)

[ListBar.Pages](listbar-pages.html)

[ListBarPage](listbarpage.html)

[ListBarPage.Cursor](listbarpage-cursor.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbarpagestyles.html language=enus -->
## TOPIC 05275: ListBarPageStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbarpagestyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbarpagestyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ListBar.PageStyle property. Use the bitwise-OR operator to specify more than one option. ListBarPageStyle_FrameSelectedItem –(Value: 0x1) When set, a frame surrounds the selected item. When not set, the control highlights the text of the selected item. ListBarPageStyle_I

### ListBarPageStyles

Use these constants with the
 [ListBar.PageStyle](listbar-pagestyle.html)
 property. Use the bitwise-OR operator to specify more than one option.

- ListBarPageStyle_FrameSelectedItem 
 –(Value: 0x1) When set, a frame surrounds the selected item. When not set, the control highlights the text of the selected item.
- ListBarPageStyle_IconsOnTop 
 –(Value: 0x4) Items on the ListBar page draw icons above the text.
- ListBarPageStyle_Tracking 
 –(Value: 0x2) Items on the ListBar page that the mouse hovers over are highlighted.

#### See Also

[ListBar.PageStyle](listbar-pagestyle.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-autosizecolumns.html language=enus -->
## TOPIC 05276: ListBox.AutoSizeColumns

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-autosizecolumns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-autosizecolumns.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.AutoSizeColumns Data Type Boolean Purpose Specifies whether to make all columns fit within the width of the control. When the control resizes, the width of each column for which the ListBoxColumn.Autosizing property is a value other than AutoSizingOption_None adjusts so the columns fi

### ListBox.AutoSizeColumns

#### Syntax

[ListBox](listbox.html).AutoSizeColumns

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether to make all columns fit within the width of the control. When the control resizes, the width of each column for which the
 [ListBoxColumn.Autosizing](listboxcolumn-autosizing.html)
 property is a value other than
 AutoSizingOption_None
 adjusts so the columns fit the new size of the control. You must ensure that at least one column enables autosizing when you set this property to
 True
 .

#### Remarks

When this property is
 True
 , the sum of all column widths always equals the width of the control, and the horizontal scrollbar is not visible. When this property is
 False
 , you can resize the columns to any width, and the horizontal scrollbar appears as needed. When the value of the autosize property for each column is
 AutoSizingOption_None
 , the last column is autosized to fit the width of the control.

#### See Also

[ListBox.ColumnSet](listbox-columnset.html)

[ListBoxColumn.Autosizing](listboxcolumn-autosizing.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-backcolor.html language=enus -->
## TOPIC 05277: ListBox.BackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-backcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-backcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.BackColor Data Type Color Purpose Specifies the background color for the control. See Also ListBox.ForeColor

### ListBox.BackColor

#### Syntax

[ListBox](listbox.html).BackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color for the control.

#### See Also

[ListBox.ForeColor](listbox-forecolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-borderdragged.html language=enus -->
## TOPIC 05278: ListBox.BorderDragged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-borderdragged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-borderdragged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize) Applies To ListBox Purpose Occurs when the user drags a draggable border of a control with the mouse. The event provides the location and size to which you must set the control for the draggable borders t

### ListBox.BorderDragged

#### Syntax

ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize)

#### Applies To

[ListBox](listbox.html)

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-borders-property-page.html language=enus -->
## TOPIC 05279: ListBox Borders Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-borders-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-borders-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Borders Property Page The property page contains the following controls: Control Frame —This section contains the following options: Visible —The control displays a thin rectangular frame that surrounds the control. Frame Location —The location of the frame the control displays. The Frame Location r

### ListBox Borders Property Page

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-borders.html language=enus -->
## TOPIC 05280: ListBox.Borders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-borders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-borders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.Borders Data Type Borders Purpose Returns the frame and draggable borders that surround the control. See Also Borders ListBox.BorderDragged

### ListBox.Borders

#### Syntax

[ListBox](listbox.html).Borders

#### Data Type

[Borders](borders.html)

#### Purpose

Returns the frame and draggable borders that surround the control.

#### See Also

[Borders](borders.html)

[ListBox.BorderDragged](listbox-borderdragged.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-caneditlabel.html language=enus -->
## TOPIC 05281: ListBox.CanEditLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-caneditlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-caneditlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.CanEditLabel Data Type Boolean Purpose Returns a value that indicates whether the listbox can enter label-editing mode, in which you can edit the item text in the first column of the listbox. See Also ListBox.EditingFlags ListBox.EditLabel

### ListBox.CanEditLabel

#### Syntax

[ListBox](listbox.html).CanEditLabel

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a value that indicates whether the listbox can enter label-editing mode, in which you can edit the item text in the first column of the listbox.

#### See Also

[ListBox.EditingFlags](listbox-editingflags.html)

[ListBox.EditLabel](listbox-editlabel.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-click.html language=enus -->
## TOPIC 05282: ListBox.Click

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-click.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-click.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_Click Applies To ListBox Purpose Occurs when you press and release the mouse on the control or when the selected item of the control changes. See Also ListBox.MouseDown ListBox.MouseMove ListBox.MouseUp

### ListBox.Click

#### Syntax

ControlName_Click

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs when you press and release the mouse on the control or when the selected item of the control changes.

#### See Also

[ListBox.MouseDown](listbox-mousedown.html)

[ListBox.MouseMove](listbox-mousemove.html)

[ListBox.MouseUp](listbox-mouseup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-columns.html language=enus -->
## TOPIC 05283: ListBox.Columns

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-columns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-columns.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.Columns Data Type Long Purpose TestStand 4.0 or later does not support setting this property to create multiple columns. Setting this property has no effect. Remarks Use the ListBox.ColumnSet property to access information about list box columns. See Also ListBox.ColumnSet ListBox.Sho

### ListBox.Columns

#### Syntax

[ListBox](listbox.html).Columns

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

TestStand 4.0 or later does not support setting this property to create multiple columns. Setting this property has no effect.

#### Remarks

Use the
 [ListBox.ColumnSet](listbox-columnset.html)
 property to access information about list box columns.

#### See Also

[ListBox.ColumnSet](listbox-columnset.html)

[ListBox.ShowHeaders](listbox-showheaders.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-columnset.html language=enus -->
## TOPIC 05284: ListBox.ColumnSet

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-columnset.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-columnset.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.ColumnSet Data Type ListBoxColumns Purpose Returns the list of columns for the control. See Also ListBoxColumns ListBox.Columns

### ListBox.ColumnSet

#### Syntax

[ListBox](listbox.html).ColumnSet

#### Data Type

[ListBoxColumns](listboxcolumns.html)

#### Purpose

Returns the list of columns for the control.

#### See Also

[ListBoxColumns](listboxcolumns.html)

[ListBox.Columns](listbox-columns.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-columnsresized.html language=enus -->
## TOPIC 05285: ListBox.ColumnsResized

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-columnsresized.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-columnsresized.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ColumnsResized Applies To ListBox Purpose Occurs when one or more columns resize in the control. See Also ListBoxColumn.Width

### ListBox.ColumnsResized

#### Syntax

ControlName_ColumnsResized

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs when one or more columns resize in the control.

#### See Also

[ListBoxColumn.Width](listboxcolumn-width.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-connectionactivity.html language=enus -->
## TOPIC 05286: ListBox.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To ListBox Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### ListBox.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-count.html language=enus -->
## TOPIC 05287: ListBox.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.Count Data Type Long Purpose Returns the number of items in the listbox. See Also ListBox.ItemIndex

### ListBox.Count

#### Syntax

[ListBox](listbox.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the listbox.

#### See Also

[ListBox.ItemIndex](listbox-itemindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-createcontextmenu.html language=enus -->
## TOPIC 05288: ListBox.CreateContextMenu

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-createcontextmenu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-createcontextmenu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_CreateContextMenu( menuHandle, x, y) Applies To ListBox Purpose Occurs when you right-click the control so the application can build a context menu from which you can select commands. Even though you can implement context menus in most environments without using this event, some e

### ListBox.CreateContextMenu

#### Syntax

ControlName_CreateContextMenu( menuHandle, x, y)

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs when you right-click the control so the application can build a context menu from which you can select commands. Even though you can implement context menus in most environments without using this event, some environments do not provide any other way to create a context menu. Also, creating a context menu using this event is less complicated in most environments, especially when the context menu contains only TestStand commands.

#### Parameters

menuHandle
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the Microsoft Windows menu handle (HMENU). When you add menu items to the menu handle, the control displays them in a context menu. Use the
 [Commands.InsertIntoWin32Menu](commands-insertintowin32menu.html)
 method to insert TestStand commands into the menu.

You can also use the menu functions in the Windows Software Development Kit (SDK) to add other menu items; however, these menu items do not have an associated TestStand command. When you select an item without a TestStand command, the control creates and executes a Command object of kind
 CommandKind_Custom
 . The control stores the menu item identifier, such as resource ID or command ID, as a long in the
 [Command.UserData](command-userdata.html)
 property, and as a decimal string in the command display name. You can handle either the
 [ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)
 or
 [ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)
 event to receive a notification when the user selects a menu item you insert with the Windows SDK.

When you close the context menu, the control disposes of the menu items. You do not need to dispose of the menu items you insert.

x
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the horizontal position of right-clicking, relative to the control.

y
 As
 [long](data-types-for-teststand-user-interface.html)

[In] Specifies the vertical position of right-clicking, relative to the control.

#### See Also

[ApplicationMgr.PostCommandExecute](applicationmgr-postcommandexecute.html)

[ApplicationMgr.PreCommandExecute](applicationmgr-precommandexecute.html)

[Command.UserData](command-userdata.html)

[Commands.InsertIntoWin32Menu](commands-insertintowin32menu.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-dblclick.html language=enus -->
## TOPIC 05289: ListBox.DblClick

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-dblclick.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-dblclick.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_DblClick Applies To ListBox Purpose Occurs when you double-click using the left mouse button.

### ListBox.DblClick

#### Syntax

ControlName_DblClick

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs when you double-click using the left mouse button.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-editingflags.html language=enus -->
## TOPIC 05290: ListBox.EditingFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-editingflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-editingflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.EditingFlags Data Type Long Purpose Specifies the types of editing the listbox allows. Use any combination of the EditingFlags constants with this property. Remarks By default, TestStand allows all editing types. These flags have no effect if the listbox is not connected to display ed

### ListBox.EditingFlags

#### Syntax

[ListBox](listbox.html).EditingFlags

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the types of editing the listbox allows. Use any combination of the
 [EditingFlags](editingflags.html)
 constants with this property.

#### Remarks

By default, TestStand allows all editing types. These flags have no effect if the listbox is not connected to display editable items.

#### See Also

[EditingFlags](editingflags.html)

[ListBox.CanEditLabel](listbox-caneditlabel.html)

[ListBox.EditLabel](listbox-editlabel.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-editlabel.html language=enus -->
## TOPIC 05291: ListBox.EditLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-editlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-editlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.EditLabel Purpose Enters label-editing mode for the active item in the list. In label-editing mode, you can edit the item text in the first column of the listbox. Remarks The listbox automatically attempts to enter label-edit mode when you click the active item in the first column or

### ListBox.EditLabel

#### Syntax

[ListBox](listbox.html).EditLabel

#### Purpose

Enters label-editing mode for the active item in the list. In label-editing mode, you can edit the item text in the first column of the listbox.

#### Remarks

The listbox automatically attempts to enter label-edit mode when you click the active item in the first column or when you press <F2> when the listbox has the keyboard focus.

#### See Also

[ListBox.CanEditLabel](listbox-caneditlabel.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-enabled.html language=enus -->
## TOPIC 05292: ListBox.Enabled

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-enabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-enabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.Enabled Data Type Boolean Purpose The control responds to user input only when this property is True .

### ListBox.Enabled

#### Syntax

[ListBox](listbox.html).Enabled

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

The control responds to user input only when this property is
 True
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-font.html language=enus -->
## TOPIC 05293: ListBox.Font

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.Font Data Type Font Purpose Specifies the font for the control when the value of the ListBox.FontSource property is FontSource_UseFontProperty . See Also FontSources ListBox.FontSource

### ListBox.Font

#### Syntax

[ListBox](listbox.html).Font

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the font for the control when the value of the
 [ListBox.FontSource](listbox-fontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[FontSources](fontsources.html)

[ListBox.FontSource](listbox-fontsource.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-fontsource.html language=enus -->
## TOPIC 05294: ListBox.FontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-fontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-fontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.FontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_UseGUIFont –(V

### ListBox.FontSource

#### Syntax

[ListBox](listbox.html).FontSource

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
 [ListBox.Font](listbox-font.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[FontSources](fontsources.html)

[ListBox.Font](listbox-font.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-forecolor.html language=enus -->
## TOPIC 05295: ListBox.ForeColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-forecolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-forecolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.ForeColor Data Type Color Purpose Specifies the foreground color for the ListBox control. See Also ListBox.BackColor

### ListBox.ForeColor

#### Syntax

[ListBox](listbox.html).ForeColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the foreground color for the ListBox control.

#### See Also

[ListBox.BackColor](listbox-backcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-getitemtext.html language=enus -->
## TOPIC 05296: ListBox.GetItemText

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-getitemtext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-getitemtext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.GetItemText( itemIdx) Return Value String Purpose Returns the text of the item at a specified index. Parameters itemIdx As Long [In] Specifies the zero-based index of the item to return. Pass the ListBox.ItemIndex property or pass -1 to obtain the text of the currently selected item.

### ListBox.GetItemText

#### Syntax

[ListBox](listbox.html).GetItemText( itemIdx)

#### Return Value

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the text of the item at a specified index.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the zero-based index of the item to return. Pass the
 [ListBox.ItemIndex](listbox-itemindex.html)
 property or pass
 -1
 to obtain the text of the currently selected item.

#### See Also

[ListBox.Count](listbox-count.html)

[ListBox.ItemIndex](listbox-itemindex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-hittest.html language=enus -->
## TOPIC 05297: ListBox.HitTest

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-hittest.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-hittest.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.HitTest( x, y) Return Value Long Returns a numeric item index. Purpose Returns the index of the item at the given coordinates. Returns -1 when no item exists at the specified coordinates. Remarks Use this method to determine the item at the given coordinates. For example, when a user

### ListBox.HitTest

#### Syntax

[ListBox](listbox.html).HitTest( x, y)

#### Return Value

[Long](data-types-for-teststand-user-interface.html)

Returns a numeric item index.

#### Purpose

Returns the index of the item at the given coordinates. Returns
 -1
 when no item exists at the specified coordinates.

#### Remarks

Use this method to determine the item at the given coordinates. For example, when a user clicks on the control, you can determine the item the user clicked.

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-hwnd.html language=enus -->
## TOPIC 05298: ListBox.hWnd

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-hwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-hwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.hWnd Data Type Long Purpose Returns a Window handle for the ListBox control. Remarks You can use the returned Window handle with the Microsoft Windows API functions. Using Windows API functions with this property can cause undefined behavior.

### ListBox.hWnd

#### Syntax

[ListBox](listbox.html).hWnd

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns a Window handle for the ListBox control.

#### Remarks

You can use the returned Window handle with the Microsoft Windows API functions.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-itemindex.html language=enus -->
## TOPIC 05299: ListBox.ItemIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-itemindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-itemindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.ItemIndex Data Type Long Purpose Specifies the index of the currently selected item in the control. You cannot change this property at design time. Remarks When no item is selected, the value of this property is -1 . See Also ListBox.Count

### ListBox.ItemIndex

#### Syntax

[ListBox](listbox.html).ItemIndex

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the index of the currently selected item in the control.

Note

#### Remarks

When no item is selected, the value of this property is
 -1
 .

#### See Also

[ListBox.Count](listbox-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-keydown.html language=enus -->
## TOPIC 05300: ListBox.KeyDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-keydown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-keydown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyDown( keyCode, shift) Applies To ListBox Purpose Occurs when the user presses a key while the control has the input focus. This event occurs before the ListBox.KeyPress event. Parameters keyCode As Integer [In/Out] Specifies the KeyCodes constant of the key the user pressed. sh

### ListBox.KeyDown

#### Syntax

ControlName_KeyDown( keyCode, shift)

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs when the user presses a key while the control has the input focus. This event occurs before the
 [ListBox.KeyPress](listbox-keypress.html)
 event.

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

[ListBox.KeyPress](listbox-keypress.html)

[ListBox.KeyUp](listbox-keyup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-keypress.html language=enus -->
## TOPIC 05301: ListBox.KeyPress

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-keypress.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-keypress.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyPress( keyAscii) Applies To ListBox Purpose Occurs when the user presses a key while a control is active. This event occurs after the ListBox.KeyDown event. Parameters keyAscii As Integer [In/Out] Specifies the ASCII value of the pressed key. See Also ListBox.KeyDown ListBox.Ke

### ListBox.KeyPress

#### Syntax

ControlName_KeyPress( keyAscii)

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs when the user presses a key while a control is active. This event occurs after the
 [ListBox.KeyDown](listbox-keydown.html)
 event.

#### Parameters

keyAscii
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In/Out] Specifies the ASCII value of the pressed key.

#### See Also

[ListBox.KeyDown](listbox-keydown.html)

[ListBox.KeyUp](listbox-keyup.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-keyup.html language=enus -->
## TOPIC 05302: ListBox.KeyUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-keyup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-keyup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_KeyUp( keyCode, shift) Applies To ListBox Purpose Occurs when the user releases a key while the control has the input focus. Parameters keyCode As Integer [In] Specifies the KeyCodes constant of the key the user pressed. shift As Integer [In] Specifies a combination of the KeyModi

### ListBox.KeyUp

#### Syntax

ControlName_KeyUp( keyCode, shift)

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs when the user releases a key while the control has the input focus.

#### Parameters

keyCode
 As
 [Integer](data-types-for-teststand-user-interface.html)

[In] Specifies the
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

[ListBox.KeyDown](listbox-keydown.html)

[ListBox.KeyPress](listbox-keypress.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-mousedown.html language=enus -->
## TOPIC 05303: ListBox.MouseDown

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-mousedown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-mousedown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseDown( btn, shift, x, y) Applies To ListBox Purpose Occurs when the user clicks the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies a

### ListBox.MouseDown

#### Syntax

ControlName_MouseDown( btn, shift, x, y)

#### Applies To

[ListBox](listbox.html)

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

[ListBox.Click](listbox-click.html)

[ListBox.MouseMove](listbox-mousemove.html)

[ListBox.MouseUp](listbox-mouseup.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-mouseicon.html language=enus -->
## TOPIC 05304: ListBox.MouseIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-mouseicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-mouseicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.MouseIcon Data Type Picture Purpose Specifies a custom mouse pointer icon for the control. Remarks The control displays the specified picture as the cursor when the value of the ListBox.MousePointer property is MousePointer_Custom . When you set this property to NULL , the value of th

### ListBox.MouseIcon

#### Syntax

[ListBox](listbox.html).MouseIcon

#### Data Type

[Picture](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies a custom mouse pointer icon for the control.

#### Remarks

The control displays the specified picture as the cursor when the value of the
 [ListBox.MousePointer](listbox-mousepointer.html)
 property is
 MousePointer_Custom
 . When you set this property to
 NULL
 , the value of the
 ListBox.MousePointer
 property changes to
 MousePointer_Default
 .

Note

#### See Also

[ListBox.MousePointer](listbox-mousepointer.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-mousemove.html language=enus -->
## TOPIC 05305: ListBox.MouseMove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-mousemove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-mousemove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseMove( btn, shift, x, y) Applies To ListBox Purpose Occurs when the user moves the mouse over the control. Parameters btn As Integer [In] Specifies what mouse buttons are pressed. You can use any combination of the MouseButtons constants. shift As Integer [In] Specifies a comb

### ListBox.MouseMove

#### Syntax

ControlName_MouseMove( btn, shift, x, y)

#### Applies To

[ListBox](listbox.html)

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

[ListBox.Click](listbox-click.html)

[ListBox.MouseDown](listbox-mousedown.html)

[ListBox.MouseUp](listbox-mouseup.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-mousepointer.html language=enus -->
## TOPIC 05306: ListBox.MousePointer

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-mousepointer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-mousepointer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.MousePointer Data Type MousePointerStyles Use the following constants with this data type: MousePointer_Arrow –(Value: 1) MousePointer_ArrowHourGlass –(Value: 11) MousePointer_ArrowQuestion –(Value: 12) MousePointer_Crosshair –(Value: 2) MousePointer_Custom –(Value: 99) MousePointer_D

### ListBox.MousePointer

#### Syntax

[ListBox](listbox.html).MousePointer

#### Data Type

[MousePointerStyles](mousepointerstyles.html)

Use the following constants with this data type:

- MousePointer_Arrow 
 –(Value: 1)
- MousePointer_ArrowHourGlass 
 –(Value: 11)
- MousePointer_ArrowQuestion 
 –(Value: 12)
- MousePointer_Crosshair 
 –(Value: 2)
- MousePointer_Custom 
 –(Value: 99)
- MousePointer_Default 
 –(Value: 0)
- MousePointer_HourGlass 
 –(Value: 9)
- MousePointer_Ibeam 
 –(Value: 3)
- MousePointer_NoDrop 
 –(Value: 10)
- MousePointer_SizeAll 
 –(Value: 13)
- MousePointer_SizeNESW 
 –(Value: 4)
- MousePointer_SizeNS 
 –(Value: 5)
- MousePointer_SizeNWSE 
 –(Value: 6)
- MousePointer_SizeWE 
 –(Value: 7)
- MousePointer_UpArrow 
 –(Value: 8)

#### Purpose

Specifies the appearance of the mouse cursor when the cursor is over the control.

#### Remarks

When the parameter is
 MousePointer_Custom
 , the mouse cursor is the picture the
 [ListBox.MouseIcon](listbox-mouseicon.html)
 property specifies.

#### See Also

[ListBox.MouseIcon](listbox-mouseicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-mouseup.html language=enus -->
## TOPIC 05307: ListBox.MouseUp

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-mouseup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-mouseup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_MouseUp( btn, shift, x, y) Applies To ListBox Purpose Occurs when the user releases the mouse on the control. Parameters btn As Integer [In] Specifies the mouse button pressed to cause this event. You can use any one of the MouseButtons constants. shift As Integer [In] Specifies a

### ListBox.MouseUp

#### Syntax

ControlName_MouseUp( btn, shift, x, y)

#### Applies To

[ListBox](listbox.html)

#### Purpose

Occurs when the user releases the mouse on the control.

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

[ListBox.Click](listbox-click.html)

[ListBox.MouseDown](listbox-mousedown.html)

[ListBox.MouseMove](listbox-mousemove.html)

[MouseButtons](mousebuttons.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-scalewithdpi.html language=enus -->
## TOPIC 05308: ListBox.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are desi

### ListBox.ScaleWithDPI

#### Syntax

[ListBox](listbox.html).ScaleWithDPI

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-showheaders.html language=enus -->
## TOPIC 05309: ListBox.ShowHeaders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-showheaders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-showheaders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.ShowHeaders Data Type Boolean Purpose Specifies whether the control displays headers for the visible columns. See Also ListBox.Columns

### ListBox.ShowHeaders

#### Syntax

[ListBox](listbox.html).ShowHeaders

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control displays headers for the visible columns.

#### See Also

[ListBox.Columns](listbox-columns.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox-tooltipvisible.html language=enus -->
## TOPIC 05310: ListBox.ToolTipVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox-tooltipvisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox-tooltipvisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBox.ToolTipVisible Data Type Boolean Purpose Specifies whether the control shows tooltips.

### ListBox.ToolTipVisible

#### Syntax

[ListBox](listbox.html).ToolTipVisible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control shows tooltips.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listbox.html language=enus -->
## TOPIC 05311: ListBox

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listbox.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listbox.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connect a SequenceFileView Manager or ExecutionView Manager control to a ListBox control so users can view or select from a list of sequence files, sequences, step groups, steps, executions, threads, or stack frames. Connect an Application Manager control to a ListBox control so users can view or se

### ListBox

Connect a
 [SequenceFileView Manager](sequencefileviewmgr.html)
 or
 [ExecutionView Manager](executionviewmgr.html)
 control to a ListBox control so users can view or select from a list of sequence files, sequences, step groups, steps, executions, threads, or stack frames. Connect an
 [Application Manager](applicationmgr.html)
 control to a ListBox control so users can view or select the default adapter of the TestStand Engine. Use a ListBox control to display multiple pages, where each page contains a list of items that users can view or select.

Use the ListBox control to connect to and display the
 [ExecutionViewMgrConnections.ExecutionList](executionviewmgrconnections-executionlist.html)
 ,
 [ExecutionViewMgrConnections.CallStack](executionviewmgrconnections-callstack.html)
 , and
 [ExecutionViewMgrConnections.ThreadList](executionviewmgrconnections-threadlist.html)
 properties in the ExecutionView Manager control and the
 [SequenceFileViewMgrConnections.SequenceList](sequencefileviewmgrconnections-sequencelist.html)
 ,
 [SequenceFileViewMgrConnections.SequenceFileList](sequencefileviewmgrconnections-sequencefileli.html)
 , and
 [SequenceFileViewMgrConnections.StepGroupList](sequencefileviewmgrconnections-stepgrouplist.html)
 properties in the SequenceFileView Manager control.

Selecting an item in the ListBox control updates the application according to the type of connection.

#### Properties

| AutoSizeColumns |
| --- |
| BackColor |
| Borders (Read Only) |
| CanEditLabel (Read Only) |
| Columns |
| ColumnSet (Read Only) |
| Count (Read Only) |
| EditingFlags |
| Enabled |
| Font |
| FontSource |
| ForeColor |
| hWnd (Read Only) |
| ItemIndex |
| MouseIcon |
| MousePointer |
| ScaleWithDPI |
| ShowHeaders |
| ToolTipVisible |

#### Methods

| EditLabel |
| --- |
| GetItemText |
| HitTest |

#### Events

| BorderDragged |
| --- |
| Click |
| ColumnsResized |
| ConnectionActivity |
| CreateContextMenu |
| DblClick |
| KeyDown |
| KeyPress |
| KeyUp |
| MouseDown |
| MouseMove |
| MouseUp |

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConnectCallStack](executionviewmgr-connectcallstack.html)

[ExecutionViewMgr.ConnectExecutionList](executionviewmgr-connectexecutionlist.html)

[ExecutionViewMgr.ConnectThreadList](executionviewmgr-connectthreadlist.html)

[ExecutionViewMgrConnections.ExecutionList](executionviewmgrconnections-executionlist.html)

[ExecutionViewMgrConnections.CallStack](executionviewmgrconnections-callstack.html)

[ExecutionViewMgrConnections.ThreadList](executionviewmgrconnections-threadlist.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

[SequenceFileViewMgr.ConnectSequenceFileList](sequencefileviewmgr-connectsequencefilelist.html)

[SequenceFileViewMgr.ConnectSequenceList](sequencefileviewmgr-connectsequencelist.html)

[SequenceFileViewMgr.ConnectStepGroupList](sequencefileviewmgr-connectstepgrouplist.html)

[SequenceFileViewMgrConnections.SequenceList](sequencefileviewmgrconnections-sequencelist.html)

[SequenceFileViewMgrConnections.SequenceFileList](sequencefileviewmgrconnections-sequencefileli.html)

[SequenceFileViewMgrConnections.StepGroupList](sequencefileviewmgrconnections-stepgrouplist.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listboxcolumn-autosizing.html language=enus -->
## TOPIC 05312: ListBoxColumn.AutoSizing

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listboxcolumn-autosizing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listboxcolumn-autosizing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBoxColumn.AutoSizing Data Type AutoSizingOptions Use the following constants with this data type: AutoSizingOption_None –(Value: 0) The item does not automatically resize itself. AutoSizingOption_Proportional –(Value: 1) The item resizes when the container resizes. The item determines the

### ListBoxColumn.AutoSizing

#### Syntax

[ListBoxColumn](listboxcolumn.html).AutoSizing

#### Data Type

[AutoSizingOptions](autosizingoptions.html)

Use the following constants with this data type:

- AutoSizingOption_None 
 –(Value: 0) The item does not automatically resize itself.
- AutoSizingOption_Proportional 
 –(Value: 1) The item resizes when the container resizes. The item determines the amount to resize from the proportion that the current size occupies of the total size of all resizable items in the same container.

#### Purpose

Specifies whether the column automatically grows or shrinks to adjust to changes in the size of the control. This property does not take effect unless the
 [ListBox.AutoSizeColumns](listbox-autosizecolumns.html)
 property is
 True
 .

#### See Also

[ListBox.AutoSizeColumns](listbox-autosizecolumns.html)

[ListBoxColumn.Width](listboxcolumn-width.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listboxcolumn-caption.html language=enus -->
## TOPIC 05313: ListBoxColumn.Caption

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listboxcolumn-caption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listboxcolumn-caption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBoxColumn.Caption Data Type String Purpose Returns the caption in the header for the column.

### ListBoxColumn.Caption

#### Syntax

[ListBoxColumn](listboxcolumn.html).Caption

#### Data Type

[String](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the caption in the header for the column.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listboxcolumn-index.html language=enus -->
## TOPIC 05314: ListBoxColumn.Index

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listboxcolumn-index.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listboxcolumn-index.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBoxColumn.Index Data Type Long Purpose Returns the zero-based numeric index of the column within the ListBoxColumns collection. See Also ListBoxColumns

### ListBoxColumn.Index

#### Syntax

[ListBoxColumn](listboxcolumn.html).Index

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the zero-based numeric index of the column within the
 [ListBoxColumns](listboxcolumns.html)
 collection.

#### See Also

[ListBoxColumns](listboxcolumns.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listboxcolumn-width.html language=enus -->
## TOPIC 05315: ListBoxColumn.Width

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listboxcolumn-width.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listboxcolumn-width.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBoxColumn.Width Data Type Long Purpose Specifies the width of the column in pixels. See Also ListBoxColumn.Autosizing

### ListBoxColumn.Width

#### Syntax

[ListBoxColumn](listboxcolumn.html).Width

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the width of the column in pixels.

#### See Also

[ListBoxColumn.Autosizing](listboxcolumn-autosizing.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listboxcolumn.html language=enus -->
## TOPIC 05316: ListBoxColumn

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listboxcolumn.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listboxcolumn.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ListBoxColumn object represents a visible column in the ListBox control. Use the ListBox.ColumnSet property to obtain a list of columns for the control. When using a SequenceListConnection , use the SequenceListConnection.GetColumnIndex and SequenceListConnection.SetColumnVisible methods to dete

### ListBoxColumn

The ListBoxColumn object represents a visible column in the
 [ListBox](listbox.html)
 control. Use the
 [ListBox.ColumnSet](listbox-columnset.html)
 property to obtain a list of columns for the control.

When using a
 [SequenceListConnection](sequencelistconnection.html)
 , use the
 [SequenceListConnection.GetColumnIndex](sequencelistconnection-getcolumnindex.html)
 and
 [SequenceListConnection.SetColumnVisible](sequencelistconnection-setcolumnvisible.html)
 methods to determine the columns the ListBox control displays and the index for each column in
 [ListBoxColumns](listboxcolumns.html)
 .

#### Properties

| AutoSizing |
| --- |
| Caption (Read Only) |
| Index (Read Only) |
| Width |

#### See Also

[ListBox](listbox.html)

[ListBox.ColumnSet](listbox-columnset.html)

[ListBoxColumns](listboxcolumns.html)

[SequenceListConnection](sequencelistconnection.html)

[SequenceListConnection.GetColumnIndex](sequencelistconnection-getcolumnindex.html)

[SequenceListConnection.SetColumnVisible](sequencelistconnection-setcolumnvisible.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listboxcolumns-count.html language=enus -->
## TOPIC 05317: ListBoxColumns.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listboxcolumns-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listboxcolumns-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBoxColumns.Count Data Type Long Purpose Returns the number of items in the collection. See Also ListBoxColumn

### ListBoxColumns.Count

#### Syntax

[ListBoxColumns](listboxcolumns.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[ListBoxColumn](listboxcolumn.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listboxcolumns-item.html language=enus -->
## TOPIC 05318: ListBoxColumns.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listboxcolumns-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listboxcolumns-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ListBoxColumns.Item( itemIdx) Data Type ListBoxColumn Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIdx As Long [In] Pass the zero-based index of the column to return. See Also ListBoxColumn ListBoxColumns.Count

### ListBoxColumns.Item

#### Syntax

[ListBoxColumns](listboxcolumns.html).Item( itemIdx)

#### Data Type

[ListBoxColumn](listboxcolumn.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIdx
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Pass the zero-based index of the column to return.

#### See Also

[ListBoxColumn](listboxcolumn.html)

[ListBoxColumns.Count](listboxcolumns-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/listboxcolumns.html language=enus -->
## TOPIC 05319: ListBoxColumns

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/listboxcolumns.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/listboxcolumns.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of ListBoxColumn objects. Use the ListBox.ColumnSet property to obtain a collection of columns for a ListBox control. Properties Count (Read Only) Item (Read Only) See Also ListBox ListBox.ColumnSet ListBoxColumn

### ListBoxColumns

A collection of
 [ListBoxColumn](listboxcolumn.html)
 objects. Use the
 [ListBox.ColumnSet](listbox-columnset.html)
 property to obtain a collection of columns for a
 [ListBox](listbox.html)
 control.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[ListBox](listbox.html)

[ListBox.ColumnSet](listbox-columnset.html)

[ListBoxColumn](listboxcolumn.html)

Parent topic:

TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods.html language=enus -->
## TOPIC 05320: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ApplicationMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_10.html language=enus -->
## TOPIC 05321: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_10.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_10.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExecutionViewMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_11.html language=enus -->
## TOPIC 05322: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_11.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_11.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExpressionEdit

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_12.html language=enus -->
## TOPIC 05323: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_12.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_12.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExpressionEditButton

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_13.html language=enus -->
## TOPIC 05324: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_13.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_13.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExpressionEditButtons

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_14.html language=enus -->
## TOPIC 05325: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_14.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_14.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExpressionEditComboBoxItems

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_15.html language=enus -->
## TOPIC 05326: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_15.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_15.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Label

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_16.html language=enus -->
## TOPIC 05327: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_16.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_16.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ListBar

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_17.html language=enus -->
## TOPIC 05328: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_17.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_17.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ListBarPages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_18.html language=enus -->
## TOPIC 05329: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_18.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_18.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ListBarPageItems

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_19.html language=enus -->
## TOPIC 05330: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_19.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_19.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ListBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_2.html language=enus -->
## TOPIC 05331: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Borders

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_20.html language=enus -->
## TOPIC 05332: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_20.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_20.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ReportView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_21.html language=enus -->
## TOPIC 05333: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_21.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_21.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceFileViewMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_22.html language=enus -->
## TOPIC 05334: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_22.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_22.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_23.html language=enus -->
## TOPIC 05335: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_23.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_23.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SeqViewColumns

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_24.html language=enus -->
## TOPIC 05336: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_24.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_24.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

StatusBar

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_25.html language=enus -->
## TOPIC 05337: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_25.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_25.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

StatusBarPanes

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_26.html language=enus -->
## TOPIC 05338: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_26.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_26.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

AdapterListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_27.html language=enus -->
## TOPIC 05339: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_27.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_27.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CallStackConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_28.html language=enus -->
## TOPIC 05340: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_28.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_28.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CaptionConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_29.html language=enus -->
## TOPIC 05341: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_29.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_29.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CaptionConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_3.html language=enus -->
## TOPIC 05342: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Button

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_30.html language=enus -->
## TOPIC 05343: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_30.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_30.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CommandConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_31.html language=enus -->
## TOPIC 05344: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_31.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_31.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CommandConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_32.html language=enus -->
## TOPIC 05345: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_32.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_32.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExecutionListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_33.html language=enus -->
## TOPIC 05346: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_33.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_33.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExecutionViewConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_34.html language=enus -->
## TOPIC 05347: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_34.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_34.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ImageConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_35.html language=enus -->
## TOPIC 05348: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_35.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_35.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

InsertionPaletteConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_36.html language=enus -->
## TOPIC 05349: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_36.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_36.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

MRUFiles

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_37.html language=enus -->
## TOPIC 05350: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_37.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_37.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

NumericConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_38.html language=enus -->
## TOPIC 05351: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_38.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_38.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

NumericConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_39.html language=enus -->
## TOPIC 05352: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_39.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_39.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ReportViewConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_4.html language=enus -->
## TOPIC 05353: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CheckBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_40.html language=enus -->
## TOPIC 05354: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_40.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_40.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SelectedPropertyObjects

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_41.html language=enus -->
## TOPIC 05355: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_41.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_41.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SelectedSequences

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_42.html language=enus -->
## TOPIC 05356: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_42.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_42.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SelectedSteps

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_43.html language=enus -->
## TOPIC 05357: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_43.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_43.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceFileListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_44.html language=enus -->
## TOPIC 05358: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_44.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_44.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceListConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_45.html language=enus -->
## TOPIC 05359: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_45.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_45.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_46.html language=enus -->
## TOPIC 05360: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_46.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_46.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceViewConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_47.html language=enus -->
## TOPIC 05361: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_47.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_47.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

StepGroupListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_48.html language=enus -->
## TOPIC 05362: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_48.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_48.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Strings

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_49.html language=enus -->
## TOPIC 05363: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_49.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_49.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ThreadListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_5.html language=enus -->
## TOPIC 05364: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ComboBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_50.html language=enus -->
## TOPIC 05365: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_50.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_50.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

VariablesConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_6.html language=enus -->
## TOPIC 05366: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_6.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_6.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Command

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_7.html language=enus -->
## TOPIC 05367: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_7.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_7.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Commands

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_8.html language=enus -->
## TOPIC 05368: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_8.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_8.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

EntryPoint

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/methods_9.html language=enus -->
## TOPIC 05369: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/methods_9.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/methods_9.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Executions

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mousebuttons.html language=enus -->
## TOPIC 05370: MouseButtons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mousebuttons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mousebuttons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to indicate which mouse button has been clicked for MouseDown , MouseMove , and MouseUp events. MouseButton_Left –(Value: 1) The left mouse button. MouseButton_Middle –(Value: 4) The middle mouse button. MouseButton_Right –(Value: 2) The right mouse button.

### MouseButtons

Use these constants to indicate which mouse button has been clicked for
 MouseDown
 ,
 MouseMove
 , and
 MouseUp
 events.

- MouseButton_Left 
 –(Value: 1) The left mouse button.
- MouseButton_Middle 
 –(Value: 4) The middle mouse button.
- MouseButton_Right 
 –(Value: 2) The right mouse button.

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mousepointerstyles.html language=enus -->
## TOPIC 05371: MousePointerStyles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mousepointerstyles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mousepointerstyles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Button.MousePointer , ComboBox.MousePointer , ExpressionEdit.MousePointer , Label.MousePointer , and ListBox.MousePointer properties. MousePointer_Arrow –(Value: 1) MousePointer_ArrowHourGlass –(Value: 11) MousePointer_ArrowQuestion –(Value: 12) MousePointer_Crosshair –(

### MousePointerStyles

Use these constants with the
 [Button.MousePointer](button-mousepointer.html)
 ,
 [ComboBox.MousePointer](combobox-mousepointer.html)
 ,
 [ExpressionEdit.MousePointer](expressionedit-mousepointer.html)
 ,
 [Label.MousePointer](label-mousepointer.html)
 , and
 [ListBox.MousePointer](listbox-mousepointer.html)
 properties.

- MousePointer_Arrow 
 –(Value: 1)
- MousePointer_ArrowHourGlass 
 –(Value: 11)
- MousePointer_ArrowQuestion 
 –(Value: 12)
- MousePointer_Crosshair 
 –(Value: 2)
- MousePointer_Custom 
 –(Value: 99)
- MousePointer_Default 
 –(Value: 0)
- MousePointer_HourGlass 
 –(Value: 9)
- MousePointer_Ibeam 
 –(Value: 3)
- MousePointer_NoDrop 
 –(Value: 10)
- MousePointer_SizeAll 
 –(Value: 13)
- MousePointer_SizeNESW 
 –(Value: 4)
- MousePointer_SizeNS 
 –(Value: 5)
- MousePointer_SizeNWSE 
 –(Value: 6)
- MousePointer_SizeWE 
 –(Value: 7)
- MousePointer_UpArrow 
 –(Value: 8)

#### See Also

[Button.MousePointer](button-mousepointer.html)

[ComboBox.MousePointer](combobox-mousepointer.html)

[ExpressionEdit.MousePointer](expressionedit-mousepointer.html)

[Label.MousePointer](label-mousepointer.html)

[ListBox.MousePointer](listbox-mousepointer.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mrufiles-add.html language=enus -->
## TOPIC 05372: MRUFiles.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mrufiles-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mrufiles-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax MRUFiles.Add( fileNameVal) Purpose Adds a filename to the beginning of the collection. Parameters fileNameVal As String [In] Specifies the filename to add to the collection. See Also MRUFiles.Max MRUFiles.Remove

### MRUFiles.Add

#### Syntax

[MRUFiles](mrufiles.html).Add( fileNameVal)

#### Purpose

Adds a filename to the beginning of the collection.

#### Parameters

fileNameVal
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the filename to add to the collection.

#### See Also

[MRUFiles.Max](mrufiles-max.html)

[MRUFiles.Remove](mrufiles-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mrufiles-clear.html language=enus -->
## TOPIC 05373: MRUFiles.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mrufiles-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mrufiles-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax MRUFiles.Clear Purpose Removes all items from the collection. See Also MRUFiles.Remove

### MRUFiles.Clear

#### Syntax

[MRUFiles](mrufiles.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[MRUFiles.Remove](mrufiles-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mrufiles-count.html language=enus -->
## TOPIC 05374: MRUFiles.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mrufiles-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mrufiles-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax MRUFiles.Count Data Type Long Purpose Returns the number of items in the collection. See Also MRUFiles.Max

### MRUFiles.Count

#### Syntax

[MRUFiles](mrufiles.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[MRUFiles.Max](mrufiles-max.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mrufiles-getdisplayname.html language=enus -->
## TOPIC 05375: MRUFiles.GetDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mrufiles-getdisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mrufiles-getdisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax MRUFiles.GetDisplayName( itemIndex, maxWidth = 200) Return Value String The display name of the filename at the index. Purpose Returns a string that you can display in a menu used for opening the most recently used files. Parameters itemIndex As Long [In] Specifies the index of an item. maxWi

### MRUFiles.GetDisplayName

#### Syntax

[MRUFiles](mrufiles.html).GetDisplayName( itemIndex, maxWidth = 200)

#### Return Value

[String](data-types-for-teststand-user-interface.html)

The display name of the filename at the index.

#### Purpose

Returns a string that you can display in a menu used for opening the most recently used files.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of an item.

maxWidth
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the maximum width, in pixels, of the display name string. The width of the string is measured using the system menu font.

This parameter has a default value of
 200
 .

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mrufiles-item.html language=enus -->
## TOPIC 05376: MRUFiles.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mrufiles-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mrufiles-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax MRUFiles.Item( itemIndex) Data Type String Filename of the most recently used file at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also MRUFiles.Count

### MRUFiles.Item

#### Syntax

[MRUFiles](mrufiles.html).Item( itemIndex)

#### Data Type

[String](data-types-for-teststand-user-interface.html)

Filename of the most recently used file at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[MRUFiles.Count](mrufiles-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mrufiles-max.html language=enus -->
## TOPIC 05377: MRUFiles.Max

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mrufiles-max.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mrufiles-max.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax MRUFiles.Max Data Type Long Purpose Specifies the maximum size of the collection. Remarks The MRUFiles collection cannot become larger than the size this property specifies. When the collection reaches the maximum size, new items you add to the beginning of the collection replace the oldest i

### MRUFiles.Max

#### Syntax

[MRUFiles](mrufiles.html).Max

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the maximum size of the collection.

#### Remarks

The MRUFiles collection cannot become larger than the size this property specifies. When the collection reaches the maximum size, new items you add to the beginning of the collection replace the oldest items at the end of the collection. The
 [Application Manager](applicationmgr.html)
 control persists the value this property specifies.

#### See Also

[Application Manager](applicationmgr.html)

[MRUFiles.Add](mrufiles-add.html)

[MRUFiles.Count](mrufiles-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mrufiles-remove.html language=enus -->
## TOPIC 05378: MRUFiles.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mrufiles-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mrufiles-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax MRUFiles.Remove( fileNameVal) Return Value Boolean Returns True when the item is removed from the collection. Returns False when the item is not found. Purpose Removes the specified item from this collection, if it exists. Parameters fileNameVal As String [In] Specifies the filename to remove

### MRUFiles.Remove

#### Syntax

[MRUFiles](mrufiles.html).Remove( fileNameVal)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the item is removed from the collection. Returns
 False
 when the item is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

fileNameVal
 As
 [String](data-types-for-teststand-user-interface.html)

[In] Specifies the filename to remove from the collection.

#### See Also

[MRUFiles.Add](mrufiles-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/mrufiles.html language=enus -->
## TOPIC 05379: MRUFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/mrufiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/mrufiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of the most recently used (MRU) files. Each item in the collection is a filename. Properties Count (Read Only) Item (Read Only) Max Methods Add Clear GetDisplayName Remove See Also ApplicationMgr.MRUFiles

### MRUFiles

A collection of the most recently used (MRU) files. Each item in the collection is a filename.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |
| Max |

#### Methods

| Add |
| --- |
| Clear |
| GetDisplayName |
| Remove |

#### See Also

[ApplicationMgr.MRUFiles](applicationmgr-mrufiles.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnection-refresh.html language=enus -->
## TOPIC 05380: NumericConnection.Refresh

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnection-refresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnection-refresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax NumericConnection.Refresh Purpose Refreshes the connected control with the current value of the NumericSource.

### NumericConnection.Refresh

#### Syntax

[NumericConnection](numericconnection.html).Refresh

#### Purpose

Refreshes the connected control with the current value of the NumericSource.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnection-source.html language=enus -->
## TOPIC 05381: NumericConnection.Source

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnection-source.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnection-source.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax NumericConnection.Source Data Type NumericSources Use the following constants with this data type: NumericSources_NotASource –(Value: 0) Guaranteed to never be a valid numeric source specifier. NumericSources_ProgressPercent –(Value: 10) A value from 0.0 to 100.0 that indicates the percentage

### NumericConnection.Source

#### Syntax

[NumericConnection](numericconnection.html).Source

#### Data Type

[NumericSources](numericsources.html)

Use the following constants with this data type:

- NumericSources_NotASource 
 –(Value: 0) Guaranteed to never be a valid numeric source specifier.
- NumericSources_ProgressPercent 
 –(Value: 10) A value from
 0.0 
 to
 100.0 
 that indicates the percentage of progress the current execution reports. This value indicates the progress of operations for which the execution chooses to report the amount of progress. The value does not necessarily reflect the progress of the execution as a whole. This numeric source applies only to the
 ExecutionView Manager 
 control.

#### Purpose

NumericSource of the connection.

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnection.html language=enus -->
## TOPIC 05382: NumericConnection

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a connection to a numeric source. Property Source Method Refresh See Also NumericConnections NumericSources

### NumericConnection

Represents a connection to a numeric source.

#### Property

| Source |
| --- |

#### Method

| Refresh |
| --- |

#### See Also

[NumericConnections](numericconnections.html)

[NumericSources](numericsources.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnections-add.html language=enus -->
## TOPIC 05383: NumericConnections.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnections-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnections-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax NumericConnections.Add( uiObj) Return Value NumericConnection New NumericConnection. Purpose Creates and adds a new NumericConnection to the collection. Parameters uiObj As Object [In] Specifies the user interface object to connect. See Also ExecutionViewMgr.ConnectNumeric NumericConnections.

### NumericConnections.Add

#### Syntax

[NumericConnections](numericconnections.html).Add( uiObj)

#### Return Value

[NumericConnection](numericconnection.html)

New NumericConnection.

#### Purpose

Creates and adds a new NumericConnection to the collection.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to connect.

#### See Also

[ExecutionViewMgr.ConnectNumeric](executionviewmgr-connectnumeric.html)

[NumericConnections.Remove](numericconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnections-clear.html language=enus -->
## TOPIC 05384: NumericConnections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax NumericConnections.Clear Purpose Removes all items from the collection. See Also NumericConnections.Remove

### NumericConnections.Clear

#### Syntax

[NumericConnections](numericconnections.html).Clear

#### Purpose

Removes all items from the collection.

#### See Also

[NumericConnections.Remove](numericconnections-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnections-count.html language=enus -->
## TOPIC 05385: NumericConnections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax NumericConnections.Count Data Type Long Purpose Returns the number of items in the collection.

### NumericConnections.Count

#### Syntax

[NumericConnections](numericconnections.html).Count

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnections-fromcontrol.html language=enus -->
## TOPIC 05386: NumericConnections.FromControl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnections-fromcontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnections-fromcontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax NumericConnections.FromControl( uiObj) Return Value NumericConnection NumericConnection connected to the uiObj parameter. When no NumericConnection exists for this control, this method returns NULL . Purpose Returns the NumericConnection connected to the uiObj parameter. Parameters uiObj As O

### NumericConnections.FromControl

#### Syntax

[NumericConnections](numericconnections.html).FromControl( uiObj)

#### Return Value

[NumericConnection](numericconnection.html)

NumericConnection connected to the
 uiObj
 parameter. When no NumericConnection exists for this control, this method returns
 NULL
 .

#### Purpose

Returns the NumericConnection connected to the
 uiObj
 parameter.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the connected user interface object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnections-item.html language=enus -->
## TOPIC 05387: NumericConnections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax NumericConnections.Item( itemIndex) Data Type NumericConnection Item located at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters itemIndex As Long [In] Specifies the index of the item to retrieve. See Also NumericConnection Numer

### NumericConnections.Item

#### Syntax

[NumericConnections](numericconnections.html).Item( itemIndex)

#### Data Type

[NumericConnection](numericconnection.html)

Item located at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

itemIndex
 As
 [Long](data-types-for-teststand-user-interface.html)

[In] Specifies the index of the item to retrieve.

#### See Also

[NumericConnection](numericconnection.html)

[NumericConnections.Count](numericconnections-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnections-remove.html language=enus -->
## TOPIC 05388: NumericConnections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax NumericConnections.Remove( uiObj) Return Value Boolean Returns True when the NumericConnection is removed. Returns False when the NumericConnection is not found. Purpose Removes the specified item from this collection, if it exists. Parameters uiObj As Object [In] Specifies the user interface

### NumericConnections.Remove

#### Syntax

[NumericConnections](numericconnections.html).Remove( uiObj)

#### Return Value

[Boolean](data-types-for-teststand-user-interface.html)

Returns
 True
 when the NumericConnection is removed. Returns
 False
 when the NumericConnection is not found.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

uiObj
 As
 [Object](data-types-for-teststand-user-interface.html)

[In] Specifies the user interface object to disconnect.

#### See Also

[NumericConnections.Add](numericconnections-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericconnections.html language=enus -->
## TOPIC 05389: NumericConnections

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericconnections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericconnections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A collection of NumericConnection objects. Properties Count (Read Only) Item (Read Only) Methods Add Clear FromControl Remove See Also ExecutionViewMgr.ConnectNumeric NumericConnection

### NumericConnections

A collection of
 [NumericConnection](numericconnection.html)
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

[ExecutionViewMgr.ConnectNumeric](executionviewmgr-connectnumeric.html)

[NumericConnection](numericconnection.html)

Parent topic:

TestStand User Interface Support Controls

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/numericsources.html language=enus -->
## TOPIC 05390: NumericSources

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/numericsources.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/numericsources.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify types of numeric sources. Each numeric source provides numeric values that describe an aspect of the current application state. You can use these constants to connect the execution progress state to a StatusBarPane progress indicator with the ExecutionViewMgr.ConnectNumeric m

### NumericSources

These constants specify types of numeric sources. Each numeric source provides numeric values that describe an aspect of the current application state. You can use these constants to connect the execution progress state to a
 [StatusBarPane](statusbarpane.html)
 progress indicator with the
 [ExecutionViewMgr.ConnectNumeric](executionviewmgr-connectnumeric.html)
 method.

To obtain a numeric value without connecting it to a control, call the
 [ExecutionViewMgr.GetNumericValue](executionviewmgr-getnumericvalue.html)
 method.

A numeric source applies to all manager controls unless the help for the enumeration element specifies a particular manager control or controls with which it applies.

- NumericSources_NotASource 
 –(Value: 0) Guaranteed to never be a valid numeric source specifier.
- NumericSources_ProgressPercent 
 –(Value: 10) A value from
 0.0 
 to
 100.0 
 that indicates the percentage of progress the current execution reports. This value indicates the progress of operations for which the execution chooses to report the amount of progress. The value does not necessarily reflect the progress of the execution as a whole. This numeric source applies only to the
 ExecutionView Manager 
 control.

#### See Also

[ExecutionViewMgr](executionviewmgr.html)

[ExecutionViewMgr.ConnectNumeric](executionviewmgr-connectnumeric.html)

[ExecutionViewMgr.GetNumericValue](executionviewmgr-getnumericvalue.html)

[StatusBarPane](statusbarpane.html)

Parent topic:

Support UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/obsolete-applicationmgr-events.html language=enus -->
## TOPIC 05391: Obsolete ApplicationMgr Events

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/obsolete-applicationmgr-events.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/obsolete-applicationmgr-events.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following events are now obsolete. At this time, National Instruments supports these events. However, National Instruments recommends updating your files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Event Preferred Event ProcessUserCommands Process

### Obsolete ApplicationMgr Events

The following events are now obsolete. At this time, National Instruments supports these events. However, National Instruments recommends updating your files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Event | Preferred Event |
| --- | --- |
| ProcessUserCommands | ProcessUserCommandLineArguments |
| SequenceFileClosed | SequenceFileClosing |

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/obsolete-applicationmgr-methods.html language=enus -->
## TOPIC 05392: Obsolete ApplicationMgr Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/obsolete-applicationmgr-methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/obsolete-applicationmgr-methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following method is now obsolete. At this time, National Instruments supports this method. However, National Instruments recommends updating your files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Method Preferred Method ReloadModifiedSequenceFiles

### Obsolete ApplicationMgr Methods

The following method is now obsolete. At this time, National Instruments supports this method. However, National Instruments recommends updating your files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Method | Preferred Method |
| --- | --- |
| ReloadModifiedSequenceFiles | ReloadModifiedSequenceFilesEx |

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/obsolete-expressionedit-properties.html language=enus -->
## TOPIC 05393: Obsolete ExpressionEdit Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/obsolete-expressionedit-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/obsolete-expressionedit-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following property is now obsolete. At this time, National Instruments supports this property. However, National Instruments recommends updating your files to reflect these changes to ensure compatibility with future versions of TestStand. Obsolete Property Preferred Property AutoLocalize Displa

### Obsolete ExpressionEdit Properties

The following property is now obsolete. At this time, National Instruments supports this property. However, National Instruments recommends updating your files to reflect these changes to ensure compatibility with future versions of TestStand.

| Obsolete Property | Preferred Property |
| --- | --- |
| AutoLocalize | DisplayText |
| RequiredNamedTypeArrays | GetValidEvaluationTypes and SetValidEvaluationTypes methods |
| RequiredNamedTypes | GetValidEvaluationTypes and SetValidEvaluationTypes methods |
| RequiredTypes | GetValidEvaluationTypes and SetValidEvaluationTypes methods |

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/processcommandlineerrors.html language=enus -->
## TOPIC 05394: ProcessCommandLineErrors

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/processcommandlineerrors.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/processcommandlineerrors.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants in the ApplicationMgr.ProcessUserCommandLineArguments event to specify an error that occurs while processing the command line. ProcessCommandLineError_CustomError –(Value: 2) Specifies that an error you define occurred while processing the command line. ProcessCommandLineError_No

### ProcessCommandLineErrors

Use these constants in the
 [ApplicationMgr.ProcessUserCommandLineArguments](applicationmgr-processusercommandlineargument.html)
 event to specify an error that occurs while processing the command line.

- ProcessCommandLineError_CustomError 
 –(Value: 2) Specifies that an error you define occurred while processing the command line.
- ProcessCommandLineError_None 
 –(Value: 0) Specifies that no error occurred while processing the command line.
- ProcessCommandLineError_UnrecognizedArgumentError 
 –(Value: 1) Specifies that you encountered an unrecognized command-line argument while processing the command line.

#### See Also

[ApplicationMgr.ProcessUserCommandLineArguments](applicationmgr-processusercommandlineargument.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties.html language=enus -->
## TOPIC 05395: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ApplicationMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_10.html language=enus -->
## TOPIC 05396: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_10.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_10.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Executions

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_11.html language=enus -->
## TOPIC 05397: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_11.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_11.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExecutionViewMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_12.html language=enus -->
## TOPIC 05398: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_12.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_12.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExpressionEdit

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_13.html language=enus -->
## TOPIC 05399: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_13.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_13.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExpressionEditButton

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_14.html language=enus -->
## TOPIC 05400: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_14.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_14.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExpressionEditButtons

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_15.html language=enus -->
## TOPIC 05401: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_15.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_15.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExpressionEditComboBoxItem

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_16.html language=enus -->
## TOPIC 05402: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_16.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_16.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExpressionEditComboBoxItems

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_17.html language=enus -->
## TOPIC 05403: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_17.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_17.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

InsertionPalette

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_18.html language=enus -->
## TOPIC 05404: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_18.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_18.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

InsertionPalettePage

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_19.html language=enus -->
## TOPIC 05405: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_19.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_19.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

InsertionPalettePages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_2.html language=enus -->
## TOPIC 05406: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Borders

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_20.html language=enus -->
## TOPIC 05407: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_20.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_20.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Label

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_21.html language=enus -->
## TOPIC 05408: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_21.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_21.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ListBar

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_22.html language=enus -->
## TOPIC 05409: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_22.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_22.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ListBarPage

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_23.html language=enus -->
## TOPIC 05410: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_23.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_23.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ListBarPages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_24.html language=enus -->
## TOPIC 05411: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_24.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_24.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ListBarPageItem

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_25.html language=enus -->
## TOPIC 05412: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_25.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_25.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ListBarPageItems

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_26.html language=enus -->
## TOPIC 05413: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_26.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_26.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ListBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_27.html language=enus -->
## TOPIC 05414: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_27.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_27.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ListBoxColumn

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_28.html language=enus -->
## TOPIC 05415: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_28.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_28.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ListBoxColumns

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_29.html language=enus -->
## TOPIC 05416: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_29.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_29.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ReportView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_3.html language=enus -->
## TOPIC 05417: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Button

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_30.html language=enus -->
## TOPIC 05418: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_30.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_30.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceFiles

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_31.html language=enus -->
## TOPIC 05419: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_31.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_31.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceFileViewMgr

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_32.html language=enus -->
## TOPIC 05420: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_32.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_32.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_33.html language=enus -->
## TOPIC 05421: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_33.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_33.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SeqViewColumn

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_34.html language=enus -->
## TOPIC 05422: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_34.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_34.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SeqViewColumns

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_35.html language=enus -->
## TOPIC 05423: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_35.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_35.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

StatusBar

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_36.html language=enus -->
## TOPIC 05424: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_36.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_36.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

StatusBarPane

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_37.html language=enus -->
## TOPIC 05425: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_37.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_37.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

StatusBarPanes

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_38.html language=enus -->
## TOPIC 05426: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_38.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_38.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

VariablesView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_39.html language=enus -->
## TOPIC 05427: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_39.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_39.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

AdapterListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_4.html language=enus -->
## TOPIC 05428: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

CheckBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_40.html language=enus -->
## TOPIC 05429: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_40.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_40.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ApplicationMgrConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_41.html language=enus -->
## TOPIC 05430: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_41.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_41.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

CallStackConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_42.html language=enus -->
## TOPIC 05431: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_42.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_42.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

CaptionConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_43.html language=enus -->
## TOPIC 05432: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_43.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_43.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

CaptionConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_44.html language=enus -->
## TOPIC 05433: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_44.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_44.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

CommandConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_45.html language=enus -->
## TOPIC 05434: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_45.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_45.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

CommandConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_46.html language=enus -->
## TOPIC 05435: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_46.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_46.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExecutionListConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_47.html language=enus -->
## TOPIC 05436: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_47.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_47.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExecutionListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_48.html language=enus -->
## TOPIC 05437: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_48.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_48.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExecutionViewConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_49.html language=enus -->
## TOPIC 05438: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_49.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_49.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExecutionViewConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_5.html language=enus -->
## TOPIC 05439: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ComboBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_50.html language=enus -->
## TOPIC 05440: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_50.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_50.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ExecutionViewMgrConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_51.html language=enus -->
## TOPIC 05441: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_51.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_51.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ImageConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_52.html language=enus -->
## TOPIC 05442: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_52.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_52.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ImageConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_53.html language=enus -->
## TOPIC 05443: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_53.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_53.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

InsertionPaletteConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_54.html language=enus -->
## TOPIC 05444: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_54.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_54.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

InsertionPaletteConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_55.html language=enus -->
## TOPIC 05445: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_55.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_55.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

MRUFiles

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_56.html language=enus -->
## TOPIC 05446: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_56.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_56.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

NumericConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_57.html language=enus -->
## TOPIC 05447: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_57.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_57.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

NumericConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_58.html language=enus -->
## TOPIC 05448: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_58.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_58.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ReportViewConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_59.html language=enus -->
## TOPIC 05449: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_59.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_59.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SelectedPropertyObjects

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_6.html language=enus -->
## TOPIC 05450: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_6.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_6.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Command

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_60.html language=enus -->
## TOPIC 05451: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_60.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_60.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SelectedSequences

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_61.html language=enus -->
## TOPIC 05452: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_61.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_61.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SelectedSteps

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_62.html language=enus -->
## TOPIC 05453: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_62.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_62.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceFileListConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_63.html language=enus -->
## TOPIC 05454: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_63.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_63.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceFileListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_64.html language=enus -->
## TOPIC 05455: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_64.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_64.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceFileViewMgrConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_65.html language=enus -->
## TOPIC 05456: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_65.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_65.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceListConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_66.html language=enus -->
## TOPIC 05457: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_66.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_66.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_67.html language=enus -->
## TOPIC 05458: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_67.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_67.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceViewConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_68.html language=enus -->
## TOPIC 05459: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_68.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_68.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

SequenceViewConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_69.html language=enus -->
## TOPIC 05460: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_69.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_69.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

StepGroupListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_7.html language=enus -->
## TOPIC 05461: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_7.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_7.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Commands

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_70.html language=enus -->
## TOPIC 05462: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_70.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_70.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

Strings

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_71.html language=enus -->
## TOPIC 05463: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_71.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_71.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

ThreadListConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_72.html language=enus -->
## TOPIC 05464: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_72.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_72.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

VariablesConnection

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_73.html language=enus -->
## TOPIC 05465: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_73.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_73.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

VariablesConnections

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_8.html language=enus -->
## TOPIC 05466: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_8.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_8.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

EntryPoint

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/properties_9.html language=enus -->
## TOPIC 05467: Properties

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/properties_9.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/properties_9.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the properties in this class.

### Properties

This book contains the properties in this class.

Parent topic:

EntryPoints

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/property-pages.html language=enus -->
## TOPIC 05468: Property Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/property-pages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/property-pages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the property pages for this class.

### Property Pages

This book contains the property pages for this class.

Parent topic:

ExpressionEdit

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/property-pages_2.html language=enus -->
## TOPIC 05469: Property Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/property-pages_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/property-pages_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the property pages for this class.

### Property Pages

This book contains the property pages for this class.

Parent topic:

InsertionPalette

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/property-pages_3.html language=enus -->
## TOPIC 05470: Property Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/property-pages_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/property-pages_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the property pages for this class.

### Property Pages

This book contains the property pages for this class.

Parent topic:

ListBar

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/property-pages_4.html language=enus -->
## TOPIC 05471: Property Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/property-pages_4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/property-pages_4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the property pages for this class.

### Property Pages

This book contains the property pages for this class.

Parent topic:

ListBox

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/property-pages_5.html language=enus -->
## TOPIC 05472: Property Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/property-pages_5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/property-pages_5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the property pages for this class.

### Property Pages

This book contains the property pages for this class.

Parent topic:

ReportView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/property-pages_6.html language=enus -->
## TOPIC 05473: Property Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/property-pages_6.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/property-pages_6.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the property pages for this class.

### Property Pages

This book contains the property pages for this class.

Parent topic:

SequenceView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/property-pages_7.html language=enus -->
## TOPIC 05474: Property Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/property-pages_7.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/property-pages_7.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the property pages for this class.

### Property Pages

This book contains the property pages for this class.

Parent topic:

StatusBar

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/property-pages_8.html language=enus -->
## TOPIC 05475: Property Pages

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/property-pages_8.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/property-pages_8.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the property pages for this class.

### Property Pages

This book contains the property pages for this class.

Parent topic:

VariablesView

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/querycloseexecutionoptions.html language=enus -->
## TOPIC 05476: QueryCloseExecutionOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/querycloseexecutionoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/querycloseexecutionoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the opt parameter of the ApplicationMgr.QueryCloseExecution event. QueryCloseExecution_Abort –(Value: 2) Aborts the execution if it is running. QueryCloseExecution_AutoCloseWhenDone –(Value: 3) Marks the execution to close automatically when it completes. The dialog box prom

### QueryCloseExecutionOptions

Use these constants with the
 opt
 parameter of the
 [ApplicationMgr.QueryCloseExecution](applicationmgr-querycloseexecution.html)
 event.

- QueryCloseExecution_Abort 
 –(Value: 2) Aborts the execution if it is running.
- QueryCloseExecution_AutoCloseWhenDone 
 –(Value: 3) Marks the execution to close automatically when it completes. The dialog box prompts the user to abort, auto-close, terminate, or cancel.
- QueryCloseExecution_Cancel 
 –(Value: 4) Cancels the closing of an execution.
- QueryCloseExecution_Hide 
 –(Value: 5) Turns off tracing and hides the execution. The execution continues to run. If the execution hits a breakpoint, tracepoint, or run-time error, the execution displays again.
- QueryCloseExecution_ShowDialog 
 –(Value: 0) Launches a dialog box if the execution is not terminated.
- QueryCloseExecution_Terminate 
 –(Value: 1) Terminates the execution if it is running.

#### See Also

[ApplicationMgr.QueryCloseExecution](applicationmgr-querycloseexecution.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/queryreloadsequencefileoptions.html language=enus -->
## TOPIC 05477: QueryReloadSequenceFileOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/queryreloadsequencefileoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/queryreloadsequencefileoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the opt parameter of the ApplicationMgr.QueryReloadSequenceFile event. QueryReloadSequenceFile_Cancel –(Value: 2) The Application Manager control does not reload the sequence file. QueryReloadSequenceFile_Prompt –(Value: 0) The Application Manager control prompts the user to

### QueryReloadSequenceFileOptions

Use these constants with the
 opt
 parameter of the
 [ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)
 event.

- QueryReloadSequenceFile_Cancel 
 –(Value: 2) The Application Manager control does not reload the sequence file.
- QueryReloadSequenceFile_Prompt 
 –(Value: 0) The Application Manager control prompts the user to reload the sequence file.
- QueryReloadSequenceFile_Reload 
 –(Value: 1) The Application Manager control reloads the sequence file.

#### See Also

[ApplicationMgr.QueryReloadSequenceFile](applicationmgr-queryreloadsequencefile.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/queryshutdownoptions.html language=enus -->
## TOPIC 05478: QueryShutdownOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/queryshutdownoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/queryshutdownoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the opts parameter of the ApplicationMgr.QueryShutdown event. QueryShutdown_Cancel –(Value: 2) The ApplicationMgr.Shutdown method does nothing. QueryShutdown_Continue –(Value: 1) The ApplicationMgr.Shutdown method continues shutdown. If the shutdown process cannot continue b

### QueryShutdownOptions

Use these constants with the
 opts
 parameter of the
 [ApplicationMgr.QueryShutdown](applicationmgr-queryshutdown.html)
 event.

- QueryShutdown_Cancel 
 –(Value: 2) The
 ApplicationMgr.Shutdown 
 method does nothing.
- QueryShutdown_Continue 
 –(Value: 1) The
 ApplicationMgr.Shutdown 
 method continues shutdown. If the shutdown process cannot continue because of a running execution, the application generates an error.
- QueryShutdown_ShowDialog 
 –(Value: 0) The
 ApplicationMgr.Shutdown 
 method continues shutdown and launches a dialog box if the method needs to terminate a running execution.

#### See Also

[ApplicationMgr.Shutdown](applicationmgr-shutdown.html)

[ApplicationMgr.QueryShutdown](applicationmgr-queryshutdown.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/refreshoptions.html language=enus -->
## TOPIC 05479: RefreshOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/refreshoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/refreshoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ApplicationMgr.Refresh method. RefreshOption_AdapterList –(Value: 0x40) Refresh the connected adapter list. RefreshOption_All –(Value: 0xFFFFFFFF) Refresh all controls connected to any manager control. RefreshOption_AllCaptions –(Value: 0x20) Refresh all captions connect

### RefreshOptions

Use these constants with the
 [ApplicationMgr.Refresh](applicationmgr-refresh.html)
 method.

- RefreshOption_AdapterList 
 –(Value: 0x40) Refresh the connected adapter list.
- RefreshOption_All 
 –(Value: 0xFFFFFFFF) Refresh all controls connected to any manager control.
- RefreshOption_AllCaptions 
 –(Value: 0x20) Refresh all captions connected to any manager control.
- RefreshOption_AllCommands 
 –(Value: 0x10) Refresh all commands connected to any manager control.
- RefreshOption_AllExecutionViewMgrs 
 –(Value: 0x2) Refresh all controls connected to any
 ExecutionView Manager 
 control.
- RefreshOption_AllSequenceFileViewMgrs 
 –(Value: 0x1) Refresh all controls connected to any
 SequenceFileView Manager 
 control.
- RefreshOption_Captions 
 –(Value: 0x8) Refresh all captions connected to the
 Application Manager 
 control.
- RefreshOption_Commands 
 –(Value: 0x4) Refresh all commands connected to the
 Application Manager 
 control.
- RefreshOption_EntryPoints 
 –(Value: 0x80) Refresh the
 ApplicationMgr.ExecutionEntryPoints 
 and
 ApplicationMgr.ConfigurationEntryPoints 
 properties.

#### See Also

[ApplicationMgr](applicationmgr.html)

[ApplicationMgr.ConfigurationEntryPoints](applicationmgr-configurationentrypoints.html)

[ApplicationMgr.ExecutionEntryPoints](applicationmgr-executionentrypoints.html)

[ApplicationMgr.Refresh](applicationmgr-refresh.html)

[ExecutionViewMgr](executionviewmgr.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reloadfileoptions.html language=enus -->
## TOPIC 05480: ReloadFileOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reloadfileoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reloadfileoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ApplicationMgr.ReloadFile method. ReloadFileOption_NoOptions –(Value 0x0) No options. ReloadFileOption_OnlyIfModifiedInMemory –(Value 0x2) Use this option when you want to make reloading occur conditionally based on whether the file is modified in memory. You can combine

### ReloadFileOptions

Use these constants with the
 [ApplicationMgr.ReloadFile](applicationmgr-reloadfile.html)
 method.

- ReloadFileOption_NoOptions 
 –(Value 0x0) No options.
- ReloadFileOption_OnlyIfModifiedInMemory 
 –(Value 0x2) Use this option when you want to make reloading occur conditionally based on whether the file is modified in memory. You can combine this option with
 ReloadFileOption_OnlyIfModifiedOnDisk 
 .
- ReloadFileOption_OnlyIfModifiedOnDisk 
 –(Value 0x1) Use this option when you want to make reloading occur conditionally based on whether the file has been modified on disk since the user was last prompted to reload it. You can combine this option with
 ReloadFileOption_OnlyIfModifiedInMemory 
 .

#### See Also

[ApplicationMgr.ReloadFile](applicationmgr-reloadfile.html)

Parent topic:

Core UI Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reloadfiles.html language=enus -->
## TOPIC 05481: ReloadFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reloadfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reloadfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the ApplicationMgr.ReloadSequenceFilesOnStart property. ReloadFile_All –(Value: 2) Reloads all files. ReloadFile_None –(Value: 0) Does not reload any files. ReloadFile_Selected –(Value: 1) Reloads any file selected in a SequenceFileView Manager control. See Also ApplicationM

### ReloadFiles

Use these constants with the
 [ApplicationMgr.ReloadSequenceFilesOnStart](applicationmgr-reloadsequencefilesonstart.html)
 property.

- ReloadFile_All 
 –(Value: 2) Reloads all files.
- ReloadFile_None 
 –(Value: 0) Does not reload any files.
- ReloadFile_Selected 
 –(Value: 1) Reloads any file selected in a
 SequenceFileView Manager 
 control.

#### See Also

[ApplicationMgr.ReloadSequenceFilesOnStart](applicationmgr-reloadsequencefilesonstart.html)

[SequenceFileViewMgr](sequencefileviewmgr.html)

Parent topic:

Core UI Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-borderdragged.html language=enus -->
## TOPIC 05482: ReportView.BorderDragged

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-borderdragged.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-borderdragged.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize) Applies To ReportView Purpose Occurs when the user drags a draggable border of a control with the mouse. The event provides the location and size to which you must set the control for the draggable border

### ReportView.BorderDragged

#### Syntax

ControlName_BorderDragged( bordersChanged, newX, newY, newWidth, newHeight, finalResize)

#### Applies To

[ReportView](reportview.html)

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-borders-property-page.html language=enus -->
## TOPIC 05483: ReportView Borders Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-borders-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-borders-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Borders Property Page The property page contains the following controls: Control Frame —This section contains the following options: Visible —The control displays a thin rectangular frame that surrounds the control. Frame Location —The location of the frame the control displays. The Frame Location r

### ReportView Borders Property Page

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-borders.html language=enus -->
## TOPIC 05484: ReportView.Borders

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-borders.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-borders.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.Borders Data Type Borders Purpose Returns the frame and draggable borders that surround the control. See Also Borders ReportView.BorderDragged

### ReportView.Borders

#### Syntax

[ReportView](reportview.html).Borders

#### Data Type

[Borders](borders.html)

#### Purpose

Returns the frame and draggable borders that surround the control.

#### See Also

[Borders](borders.html)

[ReportView.BorderDragged](reportview-borderdragged.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-buttonsvisible.html language=enus -->
## TOPIC 05485: ReportView.ButtonsVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-buttonsvisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-buttonsvisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.ButtonsVisible Data Type Long Specifies which toolbar buttons are visible. Purpose Specifies which buttons are visible in the toolbar of the control. Use any combination of the ReportViewButtons constants. Use the bitwise-OR operator to specify more than one value. See Also ReportV

### ReportView.ButtonsVisible

#### Syntax

[ReportView](reportview.html).ButtonsVisible

#### Data Type

[Long](data-types-for-teststand-user-interface.html)

Specifies which toolbar buttons are visible.

#### Purpose

Specifies which buttons are visible in the toolbar of the control. Use any combination of the
 [ReportViewButtons](reportviewbuttons.html)
 constants. Use the bitwise-OR operator to specify more than one value.

#### See Also

[ReportViewButtons](reportviewbuttons.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-connectionactivity.html language=enus -->
## TOPIC 05486: ReportView.ConnectionActivity

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-connectionactivity.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-connectionactivity.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_ConnectionActivity( activity) Applies To ReportView Purpose Occurs after the connection to a manager control makes a change to a user interface control. Parameters activity As ConnectionActivityTypes [In] Specifies the type of change.

### ReportView.ConnectionActivity

#### Syntax

ControlName_ConnectionActivity( activity)

#### Applies To

[ReportView](reportview.html)

#### Purpose

Occurs after the connection to a manager control makes a change to a user interface control.

#### Parameters

activity
 As
 [ConnectionActivityTypes](connectionactivitytypes.html)

[In] Specifies the type of change.

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-general-property-page.html language=enus -->
## TOPIC 05487: ReportView General Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-general-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-general-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Property Page The General property page contains the following controls: Large Icons —Displays large icons in the toolbar. ToolBar Visible —Displays a toolbar. Show Print Options Dialog —Launches the Print dialog box before printing when the user clicks Print in the toolbar. Initial Report S

### ReportView General Property Page

#### General Property Page

The General property page contains the following controls:

- Large Icons 
 —Displays large icons in the toolbar.
- ToolBar Visible 
 —Displays a toolbar.
- Show Print Options Dialog 
 —Launches the Print dialog box before printing when the user clicks Print in the toolbar.
- Initial Report Style 
 —The type of report TestStand initially displays in the control. When the control updates the report from an
 
 Execution 
 object, the report format the
 
 Report.Format 
 property specifies determines the report style.
  - HTML Document 
 —Displays an HTML report.
  - ASCII Text File 
 —Displays a text report.
  - XML Document 
 —Displays an XML report.
- ToolBar Button Text Styles 
 —Adjusts appearance of text on the toolbar of the control. You can select Text Below, Text Right, or Text Invisible. Refer to the
 ToolBarTextStyles 
 enumeration for more information about displaying toolbar text.
- Show Toolbar Buttons 
 —Visible buttons on the toolbar. Some buttons are visible only in certain report formats.
  - Text Report 
 —The Viewer and Print buttons can be visible.
  - HTML and XML Reports 
 —The Back, Forward, Stop, Refresh, Home, Viewer, Print, and Font Size buttons can be visible.

#### See Also

[Execution](../tsapiref/execution.html)

[Report.Format](../tsapiref/report-format.html)

[ToolBarTextStyles](toolbartextstyles.html)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-gethtmlctrl.html language=enus -->
## TOPIC 05488: ReportView.GetHTMLCtrl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-gethtmlctrl.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-gethtmlctrl.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.GetHTMLCtrl Return Value Object Purpose Returns the handle to the WebBrowser control this control uses to display HTML and XML reports. Remarks Use this handle to access methods and properties of the WebBrowser control. Refer to Microsoft MSDN documentation for more information abo

### ReportView.GetHTMLCtrl

#### Syntax

[ReportView](reportview.html).GetHTMLCtrl

#### Return Value

[Object](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the handle to the WebBrowser control this control uses to display HTML and XML reports.

#### Remarks

Use this handle to access methods and properties of the WebBrowser control. Refer to Microsoft MSDN documentation for more information about WebBrowser control methods and properties.

#### See Also

[ReportView.GetRichEditCtrl](reportview-getricheditctrl.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-getricheditctrl.html language=enus -->
## TOPIC 05489: ReportView.GetRichEditCtrl

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-getricheditctrl.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-getricheditctrl.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.GetRichEditCtrl Return Value Long Purpose Returns the Window handle to the RichText control this control uses to display text reports. Remarks You can use a returned Window handle with the Microsoft Windows API functions. See Also ReportView.GetHTMLCtrl

### ReportView.GetRichEditCtrl

#### Syntax

[ReportView](reportview.html).GetRichEditCtrl

#### Return Value

[Long](data-types-for-teststand-user-interface.html)

#### Purpose

Returns the Window handle to the RichText control this control uses to display text reports.

#### Remarks

You can use a returned Window handle with the Microsoft Windows API functions.

#### See Also

[ReportView.GetHTMLCtrl](reportview-gethtmlctrl.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-largeicons.html language=enus -->
## TOPIC 05490: ReportView.LargeIcons

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-largeicons.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-largeicons.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.LargeIcons Data Type Boolean Purpose When this property is True , the control displays large icons in the toolbar. When this property is False , the control displays small icons in the toolbar. See Also ReportView.ToolBarVisible

### ReportView.LargeIcons

#### Syntax

[ReportView](reportview.html).LargeIcons

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

When this property is
 True
 , the control displays large icons in the toolbar. When this property is
 False
 , the control displays small icons in the toolbar.

#### See Also

[ReportView.ToolBarVisible](reportview-toolbarvisible.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-printreport.html language=enus -->
## TOPIC 05491: ReportView.PrintReport

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-printreport.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-printreport.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.PrintReport( showPrintDialog) Purpose Prints the current report. Parameters showPrintDialog As Boolean [In] Pass True to launch the Print dialog box, in which you can select a printer for printing the report.

### ReportView.PrintReport

#### Syntax

[ReportView](reportview.html).PrintReport( showPrintDialog)

#### Purpose

Prints the current report.

#### Parameters

showPrintDialog
 As
 [Boolean](data-types-for-teststand-user-interface.html)

[In] Pass
 True
 to launch the Print dialog box, in which you can select a printer for printing the report.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-scalewithdpi.html language=enus -->
## TOPIC 05492: ReportView.ScaleWithDPI

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-scalewithdpi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-scalewithdpi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.ScaleWithDPI Data Type Boolean Purpose Specifies how the control scales based on the dots per inch (DPI) setting. Remarks Some environments scale native controls based on the DPI settings of their display, while other environments do not. The TestStand User Interface Controls are d

### ReportView.ScaleWithDPI

#### Syntax

[ReportView](reportview.html).ScaleWithDPI

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-text-report-property-page.html language=enus -->
## TOPIC 05493: ReportView Text Report Property Page

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-text-report-property-page.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-text-report-property-page.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Text Report Property Page The Text Report property page contains the following controls for use when displaying an ASCII text report: Colors —Colors available for use in a text report. Text —Foreground color of the report text. Background —Background color of the report. Text Font —Font used in the

### ReportView Text Report Property Page

#### Text Report Property Page

The Text Report property page contains the following controls for use when displaying an ASCII text report:

- Colors 
 —Colors available for use in a text report.
  - Text 
 —Foreground color of the report text.
  - Background 
 —Background color of the report.
- Text Font 
 —Font used in the report.
  - Font to Use 
 —The font for the report text. Set this option to Custom Font to choose any available font. Refer to the
 FontSources 
 enumeration for more information about this option.
  - Custom Font 
 —Displays the custom font specified for the item you select in the Font for the Item control. Click the
 Change 
 button to launch the Font dialog box. This option is available only when you select Use Custom Font in the Font to Use control.
 Note 
 The Font dialog box includes a Script ring control. If you change the system language or apply a font selection on a computer with a different language setting, some of the characters in that language might not display in the font you select if the language uses a different script.
  - Change 
 —Launches the Font dialog box, in which you can specify a custom font.

#### See Also

[FontSources](fontsources.html)

Parent topic:

Property Pages

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-textreportbackcolor.html language=enus -->
## TOPIC 05494: ReportView.TextReportBackColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-textreportbackcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-textreportbackcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.TextReportBackColor Data Type Color Purpose Specifies the background color of the report when displaying text reports. See Also ReportView.TextReportColor

### ReportView.TextReportBackColor

#### Syntax

[ReportView](reportview.html).TextReportBackColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the background color of the report when displaying text reports.

#### See Also

[ReportView.TextReportColor](reportview-textreportcolor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-textreportcolor.html language=enus -->
## TOPIC 05495: ReportView.TextReportColor

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-textreportcolor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-textreportcolor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.TextReportColor Data Type Color Purpose Specifies the color of the text used when displaying reports. See Also ReportView.TextReportBackColor ReportView.TextReportFont

### ReportView.TextReportColor

#### Syntax

[ReportView](reportview.html).TextReportColor

#### Data Type

[Color](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the color of the text used when displaying reports.

#### See Also

[ReportView.TextReportBackColor](reportview-textreportbackcolor.html)

[ReportView.TextReportFont](reportview-textreportfont.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-textreportfont.html language=enus -->
## TOPIC 05496: ReportView.TextReportFont

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-textreportfont.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-textreportfont.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.TextReportFont Data Type Font Purpose Specifies the current font of the text used when displaying text reports. This font is used when the value of the ReportView.TextReportFontSource property is FontSource_UseFontProperty . See Also FontSources ReportView.TextReportColor ReportVie

### ReportView.TextReportFont

#### Syntax

[ReportView](reportview.html).TextReportFont

#### Data Type

[Font](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies the current font of the text used when displaying text reports. This font is used when the value of the
 [ReportView.TextReportFontSource](reportview-textreportfontsource.html)
 property is
 FontSource_UseFontProperty
 .

#### See Also

[FontSources](fontsources.html)

[ReportView.TextReportColor](reportview-textreportcolor.html)

[ReportView.TextReportBackColor](reportview-textreportbackcolor.html)

[ReportView.TextReportFontSource](reportview-textreportfontsource.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-textreportfontsource.html language=enus -->
## TOPIC 05497: ReportView.TextReportFontSource

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-textreportfontsource.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-textreportfontsource.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.TextReportFontSource Data Type FontSources Use the following constants with this data type: FontSource_UseContainerFont –(Value: 2) The font the container supplies. FontSource_UseFontProperty –(Value: 0) A corresponding Font property of the control determines the font. FontSource_U

### ReportView.TextReportFontSource

#### Syntax

[ReportView](reportview.html).TextReportFontSource

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

Specifies the font the control uses to display text reports.

Note

FontSource_UseSystemFixedWidthFont

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
 when you expect the font the
 [ReportView.TextReportFont](reportview-textreportfont.html)
 property specifies to not be present on a computer at run time. For example, a font present on an English version of the Microsoft Windows operating system might not be present on a Japanese version of the Windows operating system.

#### See Also

[FontSources](fontsources.html)

[ReportView.TextReportFont](reportview-textreportfont.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-toolbartextstyle.html language=enus -->
## TOPIC 05498: ReportView.ToolBarTextStyle

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-toolbartextstyle.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-toolbartextstyle.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.ToolBarTextStyle Data Type ToolBarTextStyles Use the following constants with this data type: ToolBarTextStyle_TextBelow –(Value: 0) Text for toolbar buttons displays below button icons. ToolBarTextStyle_TextInvisible –(Value: 2) Toolbar buttons do not have text. ToolBarTextStyle_T

### ReportView.ToolBarTextStyle

#### Syntax

[ReportView](reportview.html).ToolBarTextStyle

#### Data Type

[ToolBarTextStyles](toolbartextstyles.html)

Use the following constants with this data type:

- ToolBarTextStyle_TextBelow 
 –(Value: 0) Text for toolbar buttons displays below button icons.
- ToolBarTextStyle_TextInvisible 
 –(Value: 2) Toolbar buttons do not have text.
- ToolBarTextStyle_TextRight 
 –(Value: 1) Text for the toolbar buttons displays to the right of button icons.

#### Purpose

Specifies how the control displays the text for the toolbar buttons.

#### See Also

[ReportView.ToolBarVisible](reportview-toolbarvisible.html)

[ToolBarTextStyles](toolbartextstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-toolbarvisible.html language=enus -->
## TOPIC 05499: ReportView.ToolBarVisible

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-toolbarvisible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-toolbarvisible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.ToolBarVisible Data Type Boolean Purpose Specifies whether the control displays a toolbar. See Also ReportView.LargeIcons ToolBarTextStyles

### ReportView.ToolBarVisible

#### Syntax

[ReportView](reportview.html).ToolBarVisible

#### Data Type

[Boolean](data-types-for-teststand-user-interface.html)

#### Purpose

Specifies whether the control displays a toolbar.

#### See Also

[ReportView.LargeIcons](reportview-largeicons.html)

[ToolBarTextStyles](toolbartextstyles.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsuiref/reportview-updatefromexecution.html language=enus -->
## TOPIC 05500: ReportView.UpdateFromExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsuiref/reportview-updatefromexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsuiref/reportview-updatefromexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportView.UpdateFromExecution( exec) Purpose Updates the content of the control from an Execution object. Remarks This method changes the report style of the control to the style the report uses. When you connect this control to an ExecutionView Manager control, you do not need to call this

### ReportView.UpdateFromExecution

#### Syntax

[ReportView](reportview.html).UpdateFromExecution( exec)

#### Purpose

Updates the content of the control from an Execution object.

#### Remarks

This method changes the report style of the control to the style the report uses. When you connect this control to an ExecutionView Manager control, you do not need to call this method because the connection updates this control when the report for the selected execution changes.

#### Parameters

exec
 As
 
 [Execution](../tsapiref/execution.html)

[In] Specifies the execution from which the ReportView control obtains the report.

Parent topic:

Methods
