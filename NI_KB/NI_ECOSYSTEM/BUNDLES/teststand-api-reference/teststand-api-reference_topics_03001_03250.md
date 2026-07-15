# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=3001 end=3250 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-aggregatetopundoitems.html language=enus -->
## TOPIC 03001: UndoStack.AggregateTopUndoItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-aggregatetopundoitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-aggregatetopundoitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.AggregateTopUndoItems( numItemsToAggregate, aggregateItemDescription = "", aggregatePreEditLocations = NULL, aggregatePostEditLocations = NULL) Purpose Combines a specified number of items on the top of the undo stack into one item. Parameters numItemsToAggregate As Long [In] Specif

### UndoStack.AggregateTopUndoItems

#### Syntax

[UndoStack](undostack.html).AggregateTopUndoItems( numItemsToAggregate, aggregateItemDescription = "", aggregatePreEditLocations = NULL, aggregatePostEditLocations = NULL)

#### Purpose

Combines a specified number of items on the top of the undo stack into one item.

#### Parameters

numItemsToAggregate
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the number of items to combine into one item.

aggregateItemDescription
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 [UndoItem.UndoDescription](undoitem-undodescription.html)
 and
 [UndoItem.RedoDescription](undoitem-redodescription.html)
 properties of the aggregate item. If you pass an empty string, the aggregate item uses the
 UndoItem.UndoDescription
 and
 UndoItem.RedoDescription
 properties of the lowest undo item on the stack this method aggregates.

This parameter has a default value of
 ""
 .

aggregatePreEditLocations
 As
 [Locations](locations.html)

[In] Specifies the
 [UndoItem.PreEditLocations](undoitem-preeditlocations.html)
 property of the aggregate undo item. If you pass
 NULL
 , the aggregate undo item computes the
 UndoItem.PreEditLocations
 property from the
 UndoItem.PreEditLocations
 of the aggregated undo items.

This parameter has a default value of
 NULL
 .

aggregatePostEditLocations
 As
 [Locations](locations.html)

[In] Specifies the
 [UndoItem.PostEditLocations](undoitem-posteditlocations.html)
 property of the aggregate undo item. If you pass
 NULL
 , the aggregate undo item computes the
 UndoItem.PostEditLocations
 from the
 UndoItem.PostEditLocations
 of the aggregated undo items.

This parameter has a default value of
 NULL
 .

#### See Also

[Locations](locations.html)

[UndoItem.RedoDescription](undoitem-redodescription.html)

[UndoItem.PostEditLocations](undoitem-posteditlocations.html)

[UndoItem.PreEditLocations](undoitem-preeditlocations.html)

[UndoItem.UndoDescription](undoitem-undodescription.html)

[UndoStack.Redo](undostack-redo.html)

[UndoStack.Undo](undostack-undo.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-canredo.html language=enus -->
## TOPIC 03002: UndoStack.CanRedo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-canredo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-canredo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.CanRedo Data Type Boolean Purpose If this property is False , do not call the UndoStack.Redo method. See Also UndoStack.CanUndo UndoStack.Redo

### UndoStack.CanRedo

#### Syntax

[UndoStack](undostack.html).CanRedo

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If this property is
 False
 , do not call the
 [UndoStack.Redo](undostack-redo.html)
 method.

#### See Also

[UndoStack.CanUndo](undostack-canundo.html)

[UndoStack.Redo](undostack-redo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-canundo.html language=enus -->
## TOPIC 03003: UndoStack.CanUndo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-canundo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-canundo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.CanUndo Data Type Boolean Purpose If this property is False , do not call the UndoStack.Undo method. See Also UndoStack.CanRedo UndoStack.Undo

### UndoStack.CanUndo

#### Syntax

[UndoStack](undostack.html).CanUndo

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If this property is
 False
 , do not call the
 [UndoStack.Undo](undostack-undo.html)
 method.

#### See Also

[UndoStack.CanRedo](undostack-canredo.html)

[UndoStack.Undo](undostack-undo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-clear.html language=enus -->
## TOPIC 03004: UndoStack.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.Clear Purpose Removes all items from the undo and redo stacks. See Also UndoItems.Remove

### UndoStack.Clear

#### Syntax

[UndoStack](undostack.html).Clear

#### Purpose

Removes all items from the undo and redo stacks.

#### See Also

[UndoItems.Remove](undoitems-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-getredodescription.html language=enus -->
## TOPIC 03005: UndoStack.GetRedoDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-getredodescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-getredodescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.GetRedoDescription( acceleratorPrefix) Return Value String Purpose Returns the menu item text describing the next redo operation. Parameters acceleratorPrefix As String [In] Specifies the character(s) you want to precede the accelerator character, if one exists, in the description t

### UndoStack.GetRedoDescription

#### Syntax

[UndoStack](undostack.html).GetRedoDescription( acceleratorPrefix)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the menu item text describing the next redo operation.

#### Parameters

acceleratorPrefix
 As
 [String](data-types-for-teststand.html)

[In] Specifies the character(s) you want to precede the accelerator character, if one exists, in the description the method returns. The accelerator prefix for menu items and button labels varies according to the programming environment. For example, LabVIEW uses "_", LabWindows/CVI uses "__", and Microsoft Visual C++/Visual Basic use "&".

#### See Also

[UndoStack.GetUndoDescription](undostack-getundodescription.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-getundodescription.html language=enus -->
## TOPIC 03006: UndoStack.GetUndoDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-getundodescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-getundodescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.GetUndoDescription( acceleratorPrefix) Return Value String Purpose Returns the menu item text describing the next undo operation. Parameters acceleratorPrefix As String [In] Specifies the character(s) you want to precede the accelerator character, if one exists, in the description t

### UndoStack.GetUndoDescription

#### Syntax

[UndoStack](undostack.html).GetUndoDescription( acceleratorPrefix)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the menu item text describing the next undo operation.

#### Parameters

acceleratorPrefix
 As
 [String](data-types-for-teststand.html)

[In] Specifies the character(s) you want to precede the accelerator character, if one exists, in the description the method returns. The accelerator prefix for menu items and button labels varies according to the programming environment. For example, LabVIEW uses "_", LabWindows/CVI uses "__", and Microsoft Visual C++/Visual Basic use "&".

#### See Also

[UndoStack.GetRedoDescription](undostack-getredodescription.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-inredo.html language=enus -->
## TOPIC 03007: UndoStack.InRedo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-inredo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-inredo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.InRedo Data Type Boolean Purpose Indicates whether the UndoStack is currently performing a Redo operation. Read this property when handling refresh or focus change events to determine if the event was triggered by a Redo operation.

### UndoStack.InRedo

#### Syntax

[UndoStack](undostack.html).InRedo

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates whether the
 UndoStack
 is currently performing a Redo operation. Read this property when handling refresh or focus change events to determine if the event was triggered by a Redo operation.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-inundo.html language=enus -->
## TOPIC 03008: UndoStack.InUndo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-inundo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-inundo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.InUndo Data Type Boolean Purpose Indicates whether the UndoStack is currently performing an Undo operation. Read this property when handling refresh or focus change events to determine if the event was triggered by an Undo operation.

### UndoStack.InUndo

#### Syntax

[UndoStack](undostack.html).InUndo

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates whether the
 UndoStack
 is currently performing an Undo operation. Read this property when handling refresh or focus change events to determine if the event was triggered by an Undo operation.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-push.html language=enus -->
## TOPIC 03009: UndoStack.Push

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-push.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-push.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.Push( item) Purpose Adds an item at the top of the undo stack and clears the redo stack. Parameters item As UndoItem [In] Specifies the item to add to the undo stack. See Also UndoItem UndoItem.UndoStack

### UndoStack.Push

#### Syntax

[UndoStack](undostack.html).Push( item)

#### Purpose

Adds an item at the top of the undo stack and clears the redo stack.

#### Parameters

item
 As
 [UndoItem](undoitem.html)

[In] Specifies the item to add to the undo stack.

#### See Also

[UndoItem](undoitem.html)

[UndoItem.UndoStack](undoitem-undostack.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-redo.html language=enus -->
## TOPIC 03010: UndoStack.Redo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-redo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-redo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.Redo Purpose Calls the UndoItem.Redo method on the top redo item and then moves the item from the top of the redo stack to the top of the undo stack. See Also UndoItem.Redo UndoStack.Undo

### UndoStack.Redo

#### Syntax

[UndoStack](undostack.html).Redo

#### Purpose

Calls the
 [UndoItem.Redo](undoitem-redo.html)
 method on the top redo item and then moves the item from the top of the redo stack to the top of the undo stack.

#### See Also

[UndoItem.Redo](undoitem-redo.html)

[UndoStack.Undo](undostack-undo.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-redoitems.html language=enus -->
## TOPIC 03011: UndoStack.RedoItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-redoitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-redoitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.RedoItems Data Type UndoItems Purpose Returns the items on the redo stack. See Also UndoItems UndoStack.UndoItems

### UndoStack.RedoItems

#### Syntax

[UndoStack](undostack.html).RedoItems

#### Data Type

[UndoItems](undoitems.html)

#### Purpose

Returns the items on the redo stack.

#### See Also

[UndoItems](undoitems.html)

[UndoStack.UndoItems](undostack-undoitems.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-undo.html language=enus -->
## TOPIC 03012: UndoStack.Undo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-undo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-undo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.Undo Purpose Calls UndoItem.Undo on the top undo item and then moves the item from the top of the undo stack to the top of the redo stack. See Also UndoItem.Redo UndoItem.Undo

### UndoStack.Undo

#### Syntax

[UndoStack](undostack.html).Undo

#### Purpose

Calls
 [UndoItem.Undo](undoitem-undo.html)
 on the top undo item and then moves the item from the top of the undo stack to the top of the redo stack.

#### See Also

[UndoItem.Redo](undoitem-redo.html)

[UndoItem.Undo](undoitem-undo.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack-undoitems.html language=enus -->
## TOPIC 03013: UndoStack.UndoItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack-undoitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack-undoitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UndoStack.UndoItems Data Type UndoItems Purpose The items on the undo stack. See Also UndoItems UndoStack.RedoItems

### UndoStack.UndoItems

#### Syntax

[UndoStack](undostack.html).UndoItems

#### Data Type

[UndoItems](undoitems.html)

#### Purpose

The items on the undo stack.

#### See Also

[UndoItems](undoitems.html)

[UndoStack.RedoItems](undostack-redoitems.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/undostack.html language=enus -->
## TOPIC 03014: UndoStack

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/undostack.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/undostack.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An UndoStack manages a stack of undo items and a stack of redo items. Normally, you create an UndoStack for every document in a sequence editor in which you can undo edits to a TestStand file. You receive undo items to push onto an undo stack through the UIMessage.ActiveXData property of a UIMsg_Pus

### UndoStack

An UndoStack manages a stack of undo items and a stack of redo items. Normally, you create an UndoStack for every document in a sequence editor in which you can undo edits to a TestStand file. You receive undo items to push onto an undo stack through the
 [UIMessage.ActiveXData](uimessage-activexdata.html)
 property of a
 UIMsg_PushUndoItem
 UI Message. You use the
 [UndoItem.EditedFile](undoitem-editedfile.html)
 property of the undo item to determine onto which document undo stack to push the undo item.

Use the
 [Engine.NewUndoStack](engine-newundostack.html)
 method to create an UndoStack object. You typically use UndoStack objects with the
 
 [ApplicationMgr.UndoStack](../tsuiref/applicationmgr-undostack.html)
 and
 
 [SequenceFileViewMgr.UndoStack](../tsuiref/sequencefileviewmgr-undostack.html)
 properties.

#### Properties

| CanRedo (Read Only) |
| --- |
| CanUndo (Read Only) |
| InRedo (Read Only) |
| InUndo (Read Only) |
| RedoItems (Read Only) |
| UndoItems (Read Only) |

#### Methods

| AggregateTopUndoItems |
| --- |
| Clear |
| GetRedoDescription |
| GetUndoDescription |
| Push |
| Redo |
| Undo |

#### See Also

[ApplicationMgr.UndoStack](../tsuiref/applicationmgr-undostack.html)

[Engine.NewUndoStack](engine-newundostack.html)

[SequenceFileViewMgr.UndoStack](../tsuiref/sequencefileviewmgr-undostack.html)

[UIMessage.ActiveXData](uimessage-activexdata.html)

[UIMessageCodes](uimessagecodes.html)

[UndoItem.EditedFile](undoitem-editedfile.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalue-name.html language=enus -->
## TOPIC 03015: UnmappedArgumentValue.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalue-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalue-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UnmappedArgumentValue.Name Data Type String Purpose Returns the symbolic name for the argument. See Also UnmappedArgumentValue.TypeName UnmappedArgumentValue.ValueExpr

### UnmappedArgumentValue.Name

#### Syntax

[UnmappedArgumentValue](unmappedargumentvalue.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the symbolic name for the argument.

#### See Also

[UnmappedArgumentValue.TypeName](unmappedargumentvalue-typename.html)

[UnmappedArgumentValue.ValueExpr](unmappedargumentvalue-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalue-typename.html language=enus -->
## TOPIC 03016: UnmappedArgumentValue.TypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalue-typename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalue-typename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UnmappedArgumentValue.TypeName Data Type String Purpose Returns the type name of the argument. See Also UnmappedArgumentValue.Name UnmappedArgumentValue.ValueExpr

### UnmappedArgumentValue.TypeName

#### Syntax

[UnmappedArgumentValue](unmappedargumentvalue.html).TypeName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the type name of the argument.

#### See Also

[UnmappedArgumentValue.Name](unmappedargumentvalue-name.html)

[UnmappedArgumentValue.ValueExpr](unmappedargumentvalue-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalue-unmappedargumentvalues.html language=enus -->
## TOPIC 03017: UnmappedArgumentValue.UnmappedArgumentValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalue-unmappedargumentvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalue-unmappedargumentvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UnmappedArgumentValue.UnmappedArgumentValues Data Type UnmappedArgumentValues Purpose Returns the UnmappedArgumentValues for fields of a container or elements of an array. See Also UnmappedArgumentValues

### UnmappedArgumentValue.UnmappedArgumentValues

#### Syntax

[UnmappedArgumentValue](unmappedargumentvalue.html).UnmappedArgumentValues

#### Data Type

[UnmappedArgumentValues](unmappedargumentvalues.html)

#### Purpose

Returns the
 [UnmappedArgumentValues](unmappedargumentvalues.html)
 for fields of a container or elements of an array.

#### See Also

[UnmappedArgumentValues](unmappedargumentvalues.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalue-valueexpr.html language=enus -->
## TOPIC 03018: UnmappedArgumentValue.ValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalue-valueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalue-valueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UnmappedArgumentValue.ValueExpr Data Type String Purpose Returns the value expression for the argument. See Also UnmappedArgumentValue.Name UnmappedArgumentValue.TypeName

### UnmappedArgumentValue.ValueExpr

#### Syntax

[UnmappedArgumentValue](unmappedargumentvalue.html).ValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the value expression for the argument.

#### See Also

[UnmappedArgumentValue.Name](unmappedargumentvalue-name.html)

[UnmappedArgumentValue.TypeName](unmappedargumentvalue-typename.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalue.html language=enus -->
## TOPIC 03019: UnmappedArgumentValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the UnmappedArgumentValue class to obtain specific information for an item in the UnmappedArgumentValues collection class. Properties Name (Read Only) TypeName (Read Only) UnmappedArgumentValues (Read Only) ValueExpr (Read Only) See Also Module.UnmappedArgumentValues UnmappedArgumen

### UnmappedArgumentValue

Use objects from the UnmappedArgumentValue class to obtain specific information for an item in the
 [UnmappedArgumentValues](unmappedargumentvalues.html)
 collection class.

#### Properties

| Name (Read Only) |
| --- |
| TypeName (Read Only) |
| UnmappedArgumentValues (Read Only) |
| ValueExpr (Read Only) |

#### See Also

[Module.UnmappedArgumentValues](module-unmappedargumentvalues.html)

[UnmappedArgumentValues](unmappedargumentvalues.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalues-clear.html language=enus -->
## TOPIC 03020: UnmappedArgumentValues.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalues-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalues-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UnmappedArgumentValues.Clear Purpose Removes all items from this collection.

### UnmappedArgumentValues.Clear

#### Syntax

[UnmappedArgumentValues](unmappedargumentvalues.html).Clear

#### Purpose

Removes all items from this collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalues-count.html language=enus -->
## TOPIC 03021: UnmappedArgumentValues.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalues-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalues-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UnmappedArgumentValues.Count Data Type Long Purpose Returns the number of items in the collection.

### UnmappedArgumentValues.Count

#### Syntax

[UnmappedArgumentValues](unmappedargumentvalues.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalues-item.html language=enus -->
## TOPIC 03022: UnmappedArgumentValues.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalues-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalues-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UnmappedArgumentValues.Item( index) Data Type UnmappedArgumentValue Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also UnmappedArgumentValue

### UnmappedArgumentValues.Item

#### Syntax

[UnmappedArgumentValues](unmappedargumentvalues.html).Item( index)

#### Data Type

[UnmappedArgumentValue](unmappedargumentvalue.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[UnmappedArgumentValue](unmappedargumentvalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/unmappedargumentvalues.html language=enus -->
## TOPIC 03023: UnmappedArgumentValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/unmappedargumentvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/unmappedargumentvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the UnmappedArgumentValues class to obtain a list of the current arguments not used as inputs and outputs of the corresponding module. Use the Module.UnmappedArgumentValues and DotNetCall.UnmappedArgumentValues properties to obtain the collection of unmapped argument values for a mo

### UnmappedArgumentValues

Use objects from the UnmappedArgumentValues class to obtain a list of the current arguments not used as inputs and outputs of the corresponding module. Use the
 [Module.UnmappedArgumentValues](module-unmappedargumentvalues.html)
 and
 [DotNetCall.UnmappedArgumentValues](dotnetcall-unmappedargumentvalues.html)
 properties to obtain the collection of unmapped argument values for a module.

When a module prototype changes, TestStand attempts to map the current module arguments to the new prototype by looking for matching argument names and data types, and by matching argument positions and data types. If TestStand fails to assign an argument to the new prototype, the argument is added to this collection.

TestStand does not clear the collection when you load a new prototype. Use the
 [UnmappedArgumentValues.Clear](unmappedargumentvalues-clear.html)
 method to clear the collection before calling the
 [Module.LoadPrototype](module-loadprototype.html)
 or
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Method

| Clear |
| --- |

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[Module.LoadPrototype](module-loadprototype.html)

[Module.UnmappedArgumentValues](module-unmappedargumentvalues.html)

[UnmappedArgumentValue](unmappedargumentvalue.html)

[UnmappedArgumentValues.Clear](unmappedargumentvalues-clear.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/updatemodulefromstepoptions.html language=enus -->
## TOPIC 03024: UpdateModuleFromStepOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/updatemodulefromstepoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/updatemodulefromstepoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: UpdateModuleFromStepOption_CopyParameterDefaultCheckState –(Value: 2) UpdateModuleFromStepOption_CopyParameterLogCheckState –(Value: 4) UpdateModuleFromStepOption_CopyParameterValue –(Value: 1) UpdateModuleFromStepOption_CopyShowFrontPanelState –(Value: 8) UpdateModuleFromStepOption_CopyStepRTEState

### UpdateModuleFromStepOptions

- UpdateModuleFromStepOption_CopyParameterDefaultCheckState 
 –(Value: 2)
- UpdateModuleFromStepOption_CopyParameterLogCheckState 
 –(Value: 4)
- UpdateModuleFromStepOption_CopyParameterValue 
 –(Value: 1)
- UpdateModuleFromStepOption_CopyShowFrontPanelState 
 –(Value: 8)
- UpdateModuleFromStepOption_CopyStepRTEState 
 –(Value: 16)
- UpdateModuleFromStepOption_None 
 –(Value: 0)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user-aspropertyobject.html language=enus -->
## TOPIC 03025: User.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax User.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the User object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### User.AsPropertyObject

#### Syntax

[User](user.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the User object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user-fullname.html language=enus -->
## TOPIC 03026: User.FullName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user-fullname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user-fullname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax User.FullName Data Type String Purpose Specifies the full name of the user.

### User.FullName

#### Syntax

[User](user.html).FullName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the full name of the user.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user-hasprivilege.html language=enus -->
## TOPIC 03027: User.HasPrivilege

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user-hasprivilege.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user-hasprivilege.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax User.HasPrivilege( privilegeName) Return Value Boolean Purpose Returns True if the user or any user group of which the user is a member has the privilege you specify by name. Parameters privilegeName As String [In] Specifies the name of the privilege to check. You can specify the name of any

### User.HasPrivilege

#### Syntax

[User](user.html).HasPrivilege( privilegeName)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the user or any user group of which the user is a member has the privilege you specify by name.

#### Parameters

privilegeName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the privilege to check. You can specify the name of any privilege property. You can specify the full privilege path in the
 [UserPrivileges](userprivileges.html)
 property view, such as
 Debug.RunSelectedTests
 , or you can specify the base privilege name, such as
 RunSelectedTests
 . If you specify only the base privilege name and more than one instance of the base privilege name exists, the method returns the value of the first base privilege it finds with that name.

#### See Also

[Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)

[UserPrivileges](userprivileges.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user-loginname.html language=enus -->
## TOPIC 03028: User.LoginName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user-loginname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user-loginname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax User.LoginName Data Type String Purpose Specifies the login name of the user.

### User.LoginName

#### Syntax

[User](user.html).LoginName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the login name of the user.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user-members.html language=enus -->
## TOPIC 03029: User.Members

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user-members.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user-members.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax User.Members Data Type PropertyObject Purpose Returns the underlying PropertyObject that represents the list of user names that are members of the group. This property applies only to user groups. See Also Engine.GetUserGroup PropertyObject UsersFile.UserGroupList

### User.Members

#### Syntax

[User](user.html).Members

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the list of user names that are members of the group. This property applies only to user groups.

#### See Also

[Engine.GetUserGroup](engine-getusergroup.html)

[PropertyObject](propertyobject.html)

[UsersFile.UserGroupList](usersfile-usergrouplist.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user-password.html language=enus -->
## TOPIC 03030: User.Password

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user-password.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user-password.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax User.Password Data Type String Purpose Specifies the password for the user. Remarks When you set this property, TestStand scrambles the password before storing it internally. When you get this property, TestStand returns the scrambled password to you, to prevent users from programmatically ac

### User.Password

#### Syntax

[User](user.html).Password

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the password for the user.

#### Remarks

When you set this property, TestStand scrambles the password before storing it internally. When you get this property, TestStand returns the scrambled password to you, to prevent users from programmatically accessing passwords without authorization.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user-privileges.html language=enus -->
## TOPIC 03031: User.Privileges

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user-privileges.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user-privileges.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax User.Privileges Data Type PropertyObject Purpose Returns the PropertyObject that contains the privilege settings for the user. Remarks Do not use this property to determine whether a user has certain privileges. Instead, use the User.HasPrivilege or Engine.CurrentUserHasPrivilege methods. See

### User.Privileges

#### Syntax

[User](user.html).Privileges

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the
 [PropertyObject](propertyobject.html)
 that contains the privilege settings for the user.

#### Remarks

Do not use this property to determine whether a user has certain privileges. Instead, use the
 [User.HasPrivilege](user-hasprivilege.html)
 or
 [Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)
 methods.

#### See Also

[Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)

[PropertyObject](propertyobject.html)

[User.HasPrivilege](user-hasprivilege.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user-validatepassword.html language=enus -->
## TOPIC 03032: User.ValidatePassword

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user-validatepassword.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user-validatepassword.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax User.ValidatePassword( passwordString) Return Value Boolean Purpose Returns True if the string you specify matches the user password. Parameters passwordString As String [In] Specifies the string to compare with the user password.

### User.ValidatePassword

#### Syntax

[User](user.html).ValidatePassword( passwordString)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the string you specify matches the user password.

#### Parameters

passwordString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the string to compare with the user password.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/user.html language=enus -->
## TOPIC 03033: User

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/user.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/user.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the User class represent the data and privileges TestStand associates with a TestStand user or user group. Call the Engine.GetUser or Engine.NewUser method to obtain a User object for a particular user or user group. Obtain the object for the currently logged-in user from the Engine.Curre

### User

Objects of the User class represent the data and privileges TestStand associates with a TestStand user or user group. Call the
 [Engine.GetUser](engine-getuser.html)
 or
 [Engine.NewUser](engine-newuser.html)
 method to obtain a User object for a particular user or user group. Obtain the object for the currently logged-in user from the
 [Engine.CurrentUser](engine-currentuser.html)
 property.

You can obtain an array of users or user groups using the
 [UsersFile.UserList](usersfile-userlist.html)
 and
 [UsersFile.UserGroupList](usersfile-usergrouplist.html)
 properties. Use the PropertyObject class methods to add or remove objects from the array to change the TestStand user or user group list.

You can use the PropertyObject class to access the subproperties of an object from the User class. Refer to
 [User Data Type Subproperties](../tsref/user-and-group-privileges.html)
 for the default subproperties TestStand defines.

#### Properties

| FullName |
| --- |
| LoginName |
| Members (Read Only) |
| Password |
| Privileges (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| HasPrivilege |
| ValidatePassword |

#### See Also

[Engine.CurrentUser](engine-currentuser.html)

[Engine.GetUser](engine-getuser.html)

[Engine.NewUser](engine-newuser.html)

[UserPrivileges](userprivileges.html)

[UsersFile.UserGroupList](usersfile-usergrouplist.html)

[UsersFile.UserList](usersfile-userlist.html)

[User Data Type Subproperties](../tsref/user-and-group-privileges.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/userprivileges.html language=enus -->
## TOPIC 03034: UserPrivileges

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/userprivileges.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/userprivileges.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these string constants to check if a user has a particular built-in privilege . Use the Engine.CurrentUserHasPrivilege or User.HasPrivilege method with these constants. Priv_Abort –(Value: "Abort") Priv_ConfigAdapter –(Value: "ConfigAdapter") Priv_ConfigApp –(Value: "ConfigApp") Priv_ConfigDatab

### UserPrivileges

Use these string constants to check if a user has a particular built-in
 [privilege](../tsref/user-and-group-privileges.html)
 . Use the
 [Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)
 or
 [User.HasPrivilege](user-hasprivilege.html)
 method with these constants.

- Priv_Abort 
 –(Value: "Abort")
- Priv_ConfigAdapter 
 –(Value: "ConfigAdapter")
- Priv_ConfigApp 
 –(Value: "ConfigApp")
- Priv_ConfigDatabase 
 –(Value: "ConfigDatabase")
- Priv_ConfigEngine 
 –(Value: "ConfigEngine")
- Priv_ConfigModel 
 –(Value: "ConfigModel")
- Priv_ConfigReport 
 –(Value: "ConfigReport")
- Priv_Configure 
 –(Value: "Configure")
- Priv_CtrlExecFlow 
 –(Value: "ControlExecFlow")
- Priv_Debug 
 –(Value: "Debug")
- Priv_Develop 
 –(Value: "Develop")
- Priv_EditProcessModelFiles 
 –(Value: "EditProcessModelFiles")
- Priv_EditRuntimeVariables 
 –(Value: "EditRuntimeVariables")
- Priv_EditSequenceFiles 
 –(Value: "EditSequenceFiles")
- Priv_EditStationGlobals 
 –(Value: "EditStationGlobals")
- Priv_EditTemplates 
 –(Value: "EditTemplates")
- Priv_EditTypes 
 –(Value: "EditTypes")
- Priv_EditUsers 
 –(Value: "EditUsers")
- Priv_EditWorkspace 
 –(Value: "EditWorkspace")
- Priv_Execute 
 –(Value: "Execute")
- Priv_GrantAll 
 –(Value: "GrantAll") This property exists in all the group privileges in the user privileges property view. If the value is
 True 
 , the user is granted all the privileges in the group.
 Note 
 Do not use this constant with the
 [Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)
 method.
- Priv_LoopSelectedTests 
 –(Value: "LoopSelectedTests")
- Priv_Operate 
 –(Value: "Operate")
- Priv_RunAnySequence 
 –(Value: "RunAnySequence")
- Priv_RunSelectedTests 
 –(Value: "RunSelectedTests")
- Priv_SaveSequenceFiles 
 –(Value: "SaveSequenceFiles")
- Priv_SinglePass 
 –(Value: "SinglePass")
- Priv_Terminate 
 –(Value: "Terminate")
- Priv_UserLoggedIn 
 –(Value: "*") Use this value with the
 Engine.CurrentUserHasPrivilege 
 method to determine whether a user is logged in.
- Priv_UseSourceControl 
 –(Value: "UseSourceControl")

#### See Also

[Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)

[User.HasPrivilege](user-hasprivilege.html)

[User and Group Privileges](../tsref/user-and-group-privileges.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/usersfile-aspropertyobjectfile.html language=enus -->
## TOPIC 03035: UsersFile.AsPropertyObjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/usersfile-aspropertyobjectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/usersfile-aspropertyobjectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UsersFile.AsPropertyObjectFile Return Value PropertyObjectFile Purpose Returns the underlying PropertyObjectFile that represents the UsersFile object. See Also PropertyObjectFile

### UsersFile.AsPropertyObjectFile

#### Syntax

[UsersFile](usersfile.html).AsPropertyObjectFile

#### Return Value

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the underlying PropertyObjectFile that represents the UsersFile object.

#### See Also

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/usersfile-reloadfromdisk.html language=enus -->
## TOPIC 03036: UsersFile.ReloadFromDisk

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/usersfile-reloadfromdisk.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/usersfile-reloadfromdisk.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UsersFile.ReloadFromDisk Purpose Reloads the users file from disk. Remarks After reloading the user file, any references to the UsersFile.UserList property and other users will be out of date. See Also UsersFile.UserList

### UsersFile.ReloadFromDisk

#### Syntax

[UsersFile](usersfile.html).ReloadFromDisk

#### Purpose

Reloads the users file from disk.

#### Remarks

Note

UsersFile.UserList

#### See Also

[UsersFile.UserList](usersfile-userlist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/usersfile-usergrouplist.html language=enus -->
## TOPIC 03037: UsersFile.UserGroupList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/usersfile-usergrouplist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/usersfile-usergrouplist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UsersFile.UserGroupList Data Type PropertyObject Returns a property object that is an array of User objects. Purpose Specifies the array of User objects. Remarks Use the methods of the PropertyObject class to add or remove user groups from this object to change the TestStand user group list,

### UsersFile.UserGroupList

#### Syntax

[UsersFile](usersfile.html).UserGroupList

#### Data Type

[PropertyObject](propertyobject.html)

Returns a property object that is an array of
 [User](user.html)
 objects.

#### Purpose

Specifies the array of User objects.

#### Remarks

Use the methods of the PropertyObject class to add or remove user groups from this object to change the TestStand user group list, and to access the subproperties of each element in the array of group objects. Use the
 [User.Members](user-members.html)
 property to edit the user names that are members of the group. Refer to
 [User Data Type Subproperties](../tsref/user-and-group-privileges.html)
 for the default subproperties TestStand defines.

#### See Also

[PropertyObject](propertyobject.html)

[User](user.html)

[User Data Type Subproperties](../tsref/user-and-group-privileges.html)

[User.Members](user-members.html)

[UserPrivileges](userprivileges.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/usersfile-userlist.html language=enus -->
## TOPIC 03038: UsersFile.UserList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/usersfile-userlist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/usersfile-userlist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UsersFile.UserList Data Type PropertyObject Returns a property object that is an array of User objects. Purpose Specifies the array of users. Remarks Use the methods of the PropertyObject class to add or remove users from this object to change the TestStand user list, and to access the subpro

### UsersFile.UserList

#### Syntax

[UsersFile](usersfile.html).UserList

#### Data Type

[PropertyObject](propertyobject.html)

Returns a property object that is an array of
 [User](user.html)
 objects.

#### Purpose

Specifies the array of users.

#### Remarks

Use the methods of the PropertyObject class to add or remove users from this object to change the TestStand user list, and to access the subproperties of each element in the array of User objects. Refer to
 [User Data Type Subproperties](../tsref/user-and-group-privileges.html)
 for the default subproperties that TestStand defines.

#### See Also

[PropertyObject](propertyobject.html)

[User](user.html)

[User Data Type Subproperties](../tsref/user-and-group-privileges.html)

[UserPrivileges](userprivileges.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/usersfile-userprofilelist.html language=enus -->
## TOPIC 03039: UsersFile.UserProfileList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/usersfile-userprofilelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/usersfile-userprofilelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax UsersFile.UserProfileList Data Type PropertyObject Returns a property object that is an array of User objects. Purpose Specifies the array of user profiles. This property is obsolete. Use UserGroupList instead. Remarks Use the methods of the PropertyObject class to add or remove user profiles

### UsersFile.UserProfileList

#### Syntax

[UsersFile](usersfile.html).UserProfileList

#### Data Type

[PropertyObject](propertyobject.html)

Returns a property object that is an array of
 [User](user.html)
 objects.

#### Purpose

Specifies the array of user profiles.

Note

UserGroupList

#### Remarks

Use the methods of the PropertyObject class to add or remove user profiles from this object to change the TestStand user list, and to access the
 [subproperties](../tsref/user-and-group-privileges.html)
 of each element in the array of User objects.

#### See Also

[PropertyObject](propertyobject.html)

[User](user.html)

[User Data Type Subproperties](../tsref/user-and-group-privileges.html)

[UserPrivileges](userprivileges.html)

Parent topic:

Obsolete UsersFile Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/usersfile.html language=enus -->
## TOPIC 03040: UsersFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/usersfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/usersfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The UsersFile class represents the file that contains a list of TestStand users and user profiles. Use this class to add or delete users and user profiles. You can obtain a reference to the users file TestStand loads at startup with the Engine.UsersFile property. To perform read or write operations

### UsersFile

The UsersFile class represents the file that contains a list of TestStand users and user profiles. Use this class to add or delete users and user profiles. You can obtain a reference to the users file TestStand loads at startup with the
 [Engine.UsersFile](engine-usersfile.html)
 property.

To perform read or write operations for objects from the UsersFile class, obtain a reference to the PropertyObjectFile interface by using the AsPropertyObjectFile methods, then use the
 [PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)
 and
 [PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)
 methods.

#### Properties

| UserGroupList |
| --- |
| UserList |

#### Methods

| AsPropertyObjectFile |
| --- |
| ReloadFromDisk |

#### See Also

[AsPropertyObjectFile](usersfile-aspropertyobjectfile.html)

[Engine.UsersFile](engine-usersfile.html)

[PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)

[PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/utility-createdebuglogs.html language=enus -->
## TOPIC 03041: Utility.CreateDebugLogs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/utility-createdebuglogs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/utility-createdebuglogs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Utility.CreateDebugLogs( reserved = 0) Purpose Creates TestStand logs. Remarks Call this method to create TestStand crash log and NIER dump files. After an application crash, this method creates the crash log in <TestStand_LocalAppData>\CrashLogs and the NIER dump file in <TestStand_LocalAppD

### Utility.CreateDebugLogs

#### Syntax

[Utility](utility.html).CreateDebugLogs( reserved = 0)

#### Purpose

Creates TestStand logs.

#### Remarks

Call this method to create TestStand crash log and NIER dump files. After an application crash, this method creates the crash log in
 <TestStand_LocalAppData>\CrashLogs
 and the NIER dump file in
 <TestStand_LocalAppData>\NIERDump
 . The contents of these files depend on the settings you specify in the configuration INI file for the application.

#### Parameters

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for this parameter.

This parameter has a default value of
 0
 .

#### See Also

[TestStand Crash Log and Dump File](/csh?context=ts_tsfundamentals_crashrecoveryanddumpfile)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/utility-escape.html language=enus -->
## TOPIC 03042: Utility.Escape

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/utility-escape.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/utility-escape.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Utility.Escape( stringToEscape, options) Return Value String The escaped string. Purpose Replaces special characters with the following escaping sequences: Sequence Purpose \n New line \r Carriage return \r\n Carriage return/new line \" Quotation marks \\ Backslash character \t Tab Parameters

### Utility.Escape

#### Syntax

[Utility](utility.html).Escape( stringToEscape, options)

#### Return Value

[String](data-types-for-teststand.html)

The escaped string.

#### Purpose

Replaces special characters with the following escaping sequences:

| Sequence | Purpose |
| --- | --- |
| \\n | New line |
| \\r | Carriage return |
| \\r\\n | Carriage return/new line |
| \\" | Quotation marks |
| \\\\ | Backslash character |
| \\t | Tab |

#### Parameters

stringToEscape
 As
 [String](data-types-for-teststand.html)

[In] Specifies the string to escape.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the
 [EscapingOptions](escapingoptions.html)
 constants to surround the returned string in quotation marks.

#### See Also

[Engine.Utility](engine-utility.html)

[EscapingOptions](escapingoptions.html)

[Utility.Unescape](utility-unescape.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/utility-unescape.html language=enus -->
## TOPIC 03043: Utility.Unescape

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/utility-unescape.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/utility-unescape.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Utility.Unescape( stringToUnescape, options) Return Value String The unescaped string. Purpose Converts escaping sequences to special characters as follows: Sequence Purpose \n New line \r Carriage return \r\n Carriage return/new line \" Quotation marks \\ Backslash character \t Tab Parameter

### Utility.Unescape

#### Syntax

[Utility](utility.html).Unescape( stringToUnescape, options)

#### Return Value

[String](data-types-for-teststand.html)

The unescaped string.

#### Purpose

Converts escaping sequences to special characters as follows:

| Sequence | Purpose |
| --- | --- |
| \\n | New line |
| \\r | Carriage return |
| \\r\\n | Carriage return/new line |
| \\" | Quotation marks |
| \\\\ | Backslash character |
| \\t | Tab |

#### Parameters

stringToUnescape
 As
 [String](data-types-for-teststand.html)

[In] Specifies the string to unescape.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the
 [EscapingOptions](escapingoptions.html)
 constants to remove surrounding quotation marks before unescaping the string.

#### See Also

[Engine.Utility](engine-utility.html)

[EscapingOptions](escapingoptions.html)

[Utility.Escape](utility-escape.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/utility.html language=enus -->
## TOPIC 03044: Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/utility.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this class to perform utility functions. Use the Engine.Utility property to obtain an instance of this class. Methods CreateDebugLogs Escape Unescape See Also Engine.Utility

### Utility

Use this class to perform utility functions. Use the
 [Engine.Utility](engine-utility.html)
 property to obtain an instance of this class.

#### Methods

| CreateDebugLogs |
| --- |
| Escape |
| Unescape |

#### See Also

[Engine.Utility](engine-utility.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/vartype.html language=enus -->
## TOPIC 03045: VARTYPE

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/vartype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/vartype.html
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

Data Types for TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/visualstudiodteversions.html language=enus -->
## TOPIC 03046: VisualStudioDTEVersions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/visualstudiodteversions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/visualstudiodteversions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the DotNetAdapter.VisualStudioDTEVersionForEditing , DotNetAdapter.VisualStudioDTEVersionForDebugging , DllAdapter.VisualStudioDTEVersionForEditing , and DllAdapter.VisualStudioDTEVersionForDebugging properties. VisualStudioDTEVersion_2022 –(Value: "VisualStudio.DTE.

### VisualStudioDTEVersions

Use the following constants with the
 [DotNetAdapter.VisualStudioDTEVersionForEditing](dotnetadapter-visualstudiodteversionforeditin.html)
 ,
 [DotNetAdapter.VisualStudioDTEVersionForDebugging](dotnetadapter-visualstudiodteversionfordebugg.html)
 ,
 [DllAdapter.VisualStudioDTEVersionForEditing](dlladapter-visualstudiodteversionforediting.html)
 , and
 [DllAdapter.VisualStudioDTEVersionForDebugging](dlladapter-visualstudiodteversionfordebugging.html)
 properties.

- VisualStudioDTEVersion_2022 
 –(Value: "VisualStudio.DTE.17.0") The adapter uses the Microsoft Visual Studio 2022 DTE, if installed. If only one version of the DTE is installed, the adapter ignores this value and always uses the installed version. If the Visual Studio 2022 DTE is not installed, but more than one version of the DTE is installed, the adapter prompts the user to select which version to use.
- VisualStudioDTEVersion_AlwaysPrompt 
 –(Value: "AlwaysPrompt") Prompt for each operation to select a version of the Visual Studio DTE. If only one version of the DTE is installed, the adapter does not prompt and instead uses the installed version.
- VisualStudioDTEVersion_MatchProject 
 –(Value: "MatchProject") Use the Visual Studio DTE version that corresponds to the project file the step specifies. If only one version of the DTE is installed, the adapter ignores this value and always uses the installed version. If the version of the DTE that corresponds to the project file is not installed, but more than one version of the DTE is installed, the adapter prompts the user to select which version to use. This option applies only to the
 DotNetAdapter.VisualStudioDTEVersionForEditing 
 and
 DllAdapter.VisualStudioDTEVersionForEditing 
 properties.

#### See Also

[DllAdapter.VisualStudioDTEVersionForDebugging](dlladapter-visualstudiodteversionfordebugging.html)

[DllAdapter.VisualStudioDTEVersionForEditing](dlladapter-visualstudiodteversionforediting.html)

[DotNetAdapter.VisualStudioDTEVersionForDebugging](dotnetadapter-visualstudiodteversionfordebugg.html)

[DotNetAdapter.VisualStudioDTEVersionForEditing](dotnetadapter-visualstudiodteversionforeditin.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-breakpointtriggered.html language=enus -->
## TOPIC 03047: WatchExpression.BreakpointTriggered

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-breakpointtriggered.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-breakpointtriggered.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.BreakpointTriggered( seqContext) Return Value Boolean Returns True if the breakpoint condition has been met. Otherwise, returns False . Purpose Returns a value that indicates whether the suspension of the execution was a result of the breakpoint condition being met for the wat

### WatchExpression.BreakpointTriggered

#### Syntax

[WatchExpression](watchexpression.html).BreakpointTriggered( seqContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the breakpoint condition has been met. Otherwise, returns
 False
 .

#### Purpose

Returns a value that indicates whether the suspension of the execution was a result of the breakpoint condition being met for the watch expression.

#### Remarks

Call this method after the TestStand Engine suspends an execution. Multiple watch expressions can return
 True
 for this method simultaneously if their breakpoint conditions are satisfied. This method returns the same value until the engine evaluates the watch expression again.

#### Parameters

seqContext
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context for the suspended execution.

#### See Also

[Engine.GetWatchExpressions](engine-getwatchexpressions.html)

[SequenceContext](sequencecontext.html)

[WatchExpression.BreakpointType](watchexpression-breakpointtype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-breakpointtype.html language=enus -->
## TOPIC 03048: WatchExpression.BreakpointType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-breakpointtype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-breakpointtype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.BreakpointType Data Type WatchExpressionBreakType Use the following constants with this data type: WatchExpressionBreakType_None –(Value: 0x0) Specifies no breakpoint. WatchExpressionBreakType_OnChange –(Value: 0x1) Specifies to suspend the execution when the evaluated value o

### WatchExpression.BreakpointType

#### Syntax

[WatchExpression](watchexpression.html).BreakpointType

#### Data Type

[WatchExpressionBreakType](watchexpressionbreaktype.html)

Use the following constants with this data type:

- WatchExpressionBreakType_None 
 –(Value: 0x0) Specifies no breakpoint.
- WatchExpressionBreakType_OnChange 
 –(Value: 0x1) Specifies to suspend the execution when the evaluated value of the watch expression changes.
- WatchExpressionBreakType_OnExpressionTrue 
 –(Value: 0x2) Specifies to suspend the execution whenever the coerced value of the watch expression evaluates to
 True 
 . This option has no effect on arrays or containers.

#### Purpose

Specifies the type of the conditional breakpoint settings for the watch expression.

#### Remarks

The TestStand Engine maintains and monitors a list of watch expressions and evaluates conditional breakpoint settings during execution. You can add a watch expression to the list that the engine maintains and monitors by passing
 True
 to the
 insertInEngine
 parameter of the
 [WatchExpressions.Insert](watchexpressions-insert.html)
 method. Breakpoints are ignored if you disable them using the
 [StationOptions.BreakpointsEnabled](stationoptions-breakpointsenabled.html)
 property.

#### See Also

[StationOptions.BreakpointsEnabled](stationoptions-breakpointsenabled.html)

[WatchExpressions.Insert](watchexpressions-insert.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-clientsequencefile.html language=enus -->
## TOPIC 03049: WatchExpression.ClientSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-clientsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-clientsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.ClientSequenceFile Data Type String Purpose Specifies the name of the client sequence file associated with the watch expression. Remarks Every watch expression created in the sequence editor Watch View pane is associated with a client sequence file, and is visible only within

### WatchExpression.ClientSequenceFile

#### Syntax

[WatchExpression](watchexpression.html).ClientSequenceFile

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the client sequence file associated with the watch expression.

#### Remarks

Every watch expression created in the sequence editor Watch View pane is associated with a client sequence file, and is visible only within executions that use the specified client sequence file. By default, a watch expression is associated with the client sequence file that was executing when the watch expression was created. The watch expression is valid throughout the execution of the specified client sequence file, unless it is restricted by other scope properties, such as sequence filename or sequence. All scoping properties have the suffix
 Scope
 attached to their name.

A watch expression without an associated client sequence file is called a global watch expression. Global watch expressions are visible in executions for all client sequence files, unless restricted by other scope properties. You can create Global watch expressions using the
 [Watch Expressions tab](../tsref/watch-expressions-tab-edit-breakpoints-watch.html)
 of the
 [Edit Breakpoints/Watch Expressions](../tsref/edit-breakpoints-watch-expressions-dialog-box.html)
 dialog box.

#### See Also

[Edit Breakpoints/Watch Expressions dialog box](../tsref/edit-breakpoints-watch-expressions-dialog-box.html)

[Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)

[ExecutionScope](watchexpression-executionscope.html)

[SequenceFileScope](watchexpression-sequencefilescope.html)

[SequenceScope](watchexpression-sequencescope.html)

[Watch Expressions tab](../tsref/watch-expressions-tab-edit-breakpoints-watch.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-displayconfigurationdialog.html language=enus -->
## TOPIC 03050: WatchExpression.DisplayConfigurationDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-displayconfigurationdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-displayconfigurationdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.DisplayConfigurationDialog( dlgTitle, context, dlgOptions = 0) Return Value Boolean Returns True if the user clicks OK . Otherwise, returns False . Purpose Launches the Watch Expression Settings dialog box, in which you can edit the settings of the watch expression. Parameters

### WatchExpression.DisplayConfigurationDialog

#### Syntax

[WatchExpression](watchexpression.html).DisplayConfigurationDialog( dlgTitle, context, dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the user clicks
 OK
 . Otherwise, returns
 False
 .

#### Purpose

Launches the
 [Watch Expression Settings](../tsref/watch-expression-settings-dialog-box.html)
 dialog box, in which you can edit the settings of the watch expression.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

context
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context the dialog box uses to evaluate expressions specified for the watch expression. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [CommonDialogOptions](commondialogoptions.html)
 constants

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[SequenceContext](sequencecontext.html)

[Watch Expression Settings dialog box](../tsref/watch-expression-settings-dialog-box.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-evaluate.html language=enus -->
## TOPIC 03051: WatchExpression.Evaluate

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-evaluate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-evaluate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.Evaluate( seqContext, reserved) Return Value PropertyObject Result of the expression, in the form of PropertyObject. The PropertyObject can contain a value of any type depending on the expression. The returned PropertyObject is the actual object and not a copy. Purpose Evaluat

### WatchExpression.Evaluate

#### Syntax

[WatchExpression](watchexpression.html).Evaluate( seqContext, reserved)

#### Return Value

[PropertyObject](propertyobject.html)

Result of the expression, in the form of PropertyObject. The PropertyObject can contain a value of any type depending on the expression. The returned PropertyObject is the actual object and not a copy.

#### Purpose

Evaluates the watch expression and returns the result.

#### Remarks

TestStand evaluates the watch expression within the context of the PropertyObject on which you call this method. This means that the expression can reference the subproperties of the PropertyObject as variables. This method modifies the context if the expression contains operators or method calls that change property values. This method throws an exception if the evaluation of the watch expression fails.

#### Parameters

seqContext
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the SequenceContext to use while evaluating the watch expression. This context must be associated with a currently running execution.

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for this parameter.

#### See Also

[Execution](execution.html)

[PropertyObject](propertyobject.html)

[PropertyObject.EvaluateEx](propertyobject-evaluateex.html)

[SequenceContext](sequencecontext.html)

[WatchExpression.Expression](watchexpression-expression.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-executionscope.html language=enus -->
## TOPIC 03052: WatchExpression.ExecutionScope

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-executionscope.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-executionscope.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.ExecutionScope Data Type Execution Purpose Specifies the execution to which the watch expression applies. Remarks Limits the scope of the watch expression by associating the object with a particular execution. The TestStand Engine only evaluates a watch expression for the spec

### WatchExpression.ExecutionScope

#### Syntax

[WatchExpression](watchexpression.html).ExecutionScope

#### Data Type

[Execution](execution.html)

#### Purpose

Specifies the execution to which the watch expression applies.

#### Remarks

Limits the scope of the watch expression by associating the object with a particular execution. The TestStand Engine only evaluates a watch expression for the specified execution. Watch expressions that apply to a specific execution are discarded when you release the execution. Set this property to
 NULL
 to associate the watch expression with all executions for the specified client sequence file. Watch expressions that apply to all executions are automatically saved and reloaded if the
 [Engine.PersistWatchExpressions](engine-persistwatchexpressions.html)
 property is set to
 True
 .

#### See Also

[Engine.PersistWatchExpressions](engine-persistwatchexpressions.html)

[Execution](execution.html)

[WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)

[WatchExpression.SequenceFileScope](watchexpression-sequencefilescope.html)

[WatchExpression.SequenceScope](watchexpression-sequencescope.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-expression.html language=enus -->
## TOPIC 03053: WatchExpression.Expression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-expression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-expression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.Expression Data Type String Purpose Specifies the expression for the watch expression. Remarks Set this property to a variable name, property name, or expression. Call the WatchExpression.Evaluate method to evaluate the expression against a specific context. See Also WatchExpr

### WatchExpression.Expression

#### Syntax

[WatchExpression](watchexpression.html).Expression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the expression for the watch expression.

#### Remarks

Set this property to a variable name, property name, or expression. Call the
 [WatchExpression.Evaluate](watchexpression-evaluate.html)
 method to evaluate the expression against a specific context.

#### See Also

[WatchExpression.Evaluate](watchexpression-evaluate.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-getscopingcontext.html language=enus -->
## TOPIC 03054: WatchExpression.GetScopingContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-getscopingcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-getscopingcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.GetScopingContext( currentSeqContext) Return Value SequenceContext The sequence context associated with the specified scope. Returns NULL if a sequence context is not associated with the scope or if the WatchExpressionUseScopingContext property is False . Purpose Returns the s

### WatchExpression.GetScopingContext

#### Syntax

[WatchExpression](watchexpression.html).GetScopingContext( currentSeqContext)

#### Return Value

[SequenceContext](sequencecontext.html)

The sequence context associated with the specified scope. Returns
 NULL
 if a sequence context is not associated with the scope or if the
 [WatchExpressionUseScopingContext](watchexpression-usescopingcontext.html)
 property is
 False
 .

#### Purpose

Returns the scoping context, if any, associated with the watch expression.

#### Remarks

The scoping context is stored when the
 WatchExpression.UseScopingContext
 property is
 True
 and a thread enters the specified scope. The context is released if the UseScopingContext property is
 False
 or if the specified scope is changed.

#### Parameters

currentSeqContext
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies a reference to the sequence context from the current execution.

#### See Also

[SequenceContext](sequencecontext.html)

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

[WatchExpression.SequenceFileScope](watchexpression-sequencefilescope.html)

[WatchExpression.SequenceScope](watchexpression-sequencescope.html)

[WatchExpression.UseScopingContext](watchexpression-usescopingcontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-numericformat.html language=enus -->
## TOPIC 03055: WatchExpression.NumericFormat

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-numericformat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-numericformat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.NumericFormat Data Type String Purpose Specifies the numeric format to use when displaying the value the WatchExpression.Evaluate method returns. Remarks This property applies only to watch expressions that evaluate to numeric, container, or array values. For arrays and contai

### WatchExpression.NumericFormat

#### Syntax

[WatchExpression](watchexpression.html).NumericFormat

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the numeric format to use when displaying the value the
 [WatchExpression.Evaluate](watchexpression-evaluate.html)
 method returns.

#### Remarks

This property applies only to watch expressions that evaluate to numeric, container, or array values. For arrays and containers, the numeric format applies to all the subproperties of an array or container. The syntax of the numeric format string is identical to the format string the C printf function accepts, with the following exceptions:

- Place a
 $ 
 character after the
 % 
 character in the format string to remove trailing zeros after the decimal point.
- Use a format code of
 %b 
 to format a number in binary.
- Specify an empty string to set the format to the default numeric format.

#### See Also

[Engine.DisplayEditNumericFormatDialog](engine-displayeditnumericformatdialog.html)

[PropertyObject.GetFormattedValue](propertyobject-getformattedvalue.html)

[PropertyObject.NumericFormat](propertyobject-numericformat.html)

[WatchExpression.Evaluate](watchexpression-evaluate.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-sequencefilescope.html language=enus -->
## TOPIC 03056: WatchExpression.SequenceFileScope

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-sequencefilescope.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-sequencefilescope.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.SequenceFileScope Data Type String Purpose Specifies the sequence file to which the watch expression applies. Remarks Limits the scope of a watch expression by associating the object with a particular sequence file. The TestStand Engine only evaluates a watch expression when a

### WatchExpression.SequenceFileScope

#### Syntax

[WatchExpression](watchexpression.html).SequenceFileScope

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the sequence file to which the watch expression applies.

#### Remarks

Limits the scope of a watch expression by associating the object with a particular sequence file. The TestStand Engine only evaluates a watch expression when a sequence in the specified sequence file is executing. Set this property to an empty string to instruct TestStand to evaluate the watch expression for all sequence files. You can specify a sequence filename or an absolute path name.

Use the
 [WatchExpression.SequenceScope](watchexpression-sequencescope.html)
 property to limit the scope of the watch expression to sequences with a particular name.

#### See Also

[WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

[WatchExpression.SequenceScope](watchexpression-sequencescope.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-sequencescope.html language=enus -->
## TOPIC 03057: WatchExpression.SequenceScope

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-sequencescope.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-sequencescope.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.SequenceScope Data Type String Purpose Specifies the name of the sequence to which the watch expression applies. Remarks Limits the scope of the watch expression by associating the object with a particular sequence name. The TestStand Engine evaluates a watch expression only w

### WatchExpression.SequenceScope

#### Syntax

[WatchExpression](watchexpression.html).SequenceScope

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the sequence to which the watch expression applies.

#### Remarks

Limits the scope of the watch expression by associating the object with a particular sequence name. The TestStand Engine evaluates a watch expression only when the specified sequence executes. Set this property to an empty string to evaluate the watch expression for all sequences.

#### See Also

[WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-uniquewatchid.html language=enus -->
## TOPIC 03058: WatchExpression.UniqueWatchId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-uniquewatchid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-uniquewatchid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.UniqueWatchId Data Type String Purpose Returns an identification string unique to this watch expression in all instances of the TestStand Engine. Remarks The unique ID of a watch expression persists if the watch expression persists.

### WatchExpression.UniqueWatchId

#### Syntax

[WatchExpression](watchexpression.html).UniqueWatchId

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns an identification string unique to this watch expression in all instances of the TestStand Engine.

#### Remarks

The unique ID of a watch expression persists if the watch expression persists.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression-usescopingcontext.html language=enus -->
## TOPIC 03059: WatchExpression.UseScopingContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression-usescopingcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression-usescopingcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpression.UseScopingContext Data Type Boolean Purpose Specifies if TestStand attaches a watch expression to a sequence context that matches the scoping properties of the watch expression. While the attached sequence context is valid, the watch expression uses the sequence context to eva

### WatchExpression.UseScopingContext

#### Syntax

[WatchExpression](watchexpression.html).UseScopingContext

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if TestStand attaches a watch expression to a sequence context that matches the scoping properties of the watch expression. While the attached sequence context is valid, the watch expression uses the sequence context to evaluate the watch expression, even if the thread adds additional call stack levels by invoking subsequences.

#### Remarks

If this property is set, TestStand automatically caches the scoping context when a thread enters a specified scope. Otherwise, use the active context to evaluate the watch expression.

This property defaults to
 False
 .

#### See Also

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

[WatchExpression.GetScopingContext](watchexpression-getscopingcontext.html)

[WatchExpression.SequenceFileScope](watchexpression-sequencefilescope.html)

[WatchExpression.SequenceScope](watchexpression-sequencescope.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpression.html language=enus -->
## TOPIC 03060: WatchExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects of the WatchExpression class to monitor the values of properties and variables using expressions. Typically, you use WatchExpression objects to display run-time values in a Watch View pane in a user interface. A WatchExpression object defines an expression TestStand evaluates during sequ

### WatchExpression

Use objects of the WatchExpression class to monitor the values of properties and variables using expressions. Typically, you use WatchExpression objects to display run-time values in a Watch View pane in a user interface. A WatchExpression object defines an expression TestStand evaluates during sequence execution.

You can configure a conditional breakpoint on a watch expression. The breakpoint suspends execution when a value of the watch expression changes, or whenever the coerced value of the watch expression evaluates to
 True
 . The TestStand Engine maintains a list of watch expressions and evaluates conditional breakpoints during execution.

You can also specify the scope of the watch expression, which specifies whether the expression applies to all executions of the client sequence file or only the current execution, and whether to evaluate the watch expression only when executing within a specific sequence file or sequence.

Use the collection object the
 [Engine.GetWatchExpressions](engine-getwatchexpressions.html)
 method returns to manage a watch expression list. You can create new watch expressions by using the
 [WatchExpressions.Insert](watchexpressions-insert.html)
 method, which adds a new watch expression to the collection and returns the new object. To add a watch expression to the list the engine maintains and monitors, pass
 True
 for the
 insertInEngine
 parameter.

#### Properties

| BreakpointType |
| --- |
| ClientSequenceFile |
| ExecutionScope |
| Expression |
| NumericFormat |
| SequenceFileScope |
| SequenceScope |
| UniqueWatchId (Read Only) |
| UseScopingContext |

#### Methods

| BreakpointTriggered |
| --- |
| DisplayConfigurationDialog |
| Evaluate |
| GetScopingContext |

#### See Also

[Engine.GetWatchExpressions](engine-getwatchexpressions.html)

[WatchExpressions.Insert](watchexpressions-insert.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressionbreaktype.html language=enus -->
## TOPIC 03061: WatchExpressionBreakType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressionbreaktype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressionbreaktype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the breakpoint type value of the WatchExpression.BreakpointType property. WatchExpressionBreakType_None –(Value: 0x0) Specifies no breakpoint. WatchExpressionBreakType_OnChange –(Value: 0x1) Specifies to suspend the execution when the evaluated value of the watch expre

### WatchExpressionBreakType

Use these constants to specify the breakpoint type value of the
 [WatchExpression.BreakpointType](watchexpression-breakpointtype.html)
 property.

- WatchExpressionBreakType_None 
 –(Value: 0x0) Specifies no breakpoint.
- WatchExpressionBreakType_OnChange 
 –(Value: 0x1) Specifies to suspend the execution when the evaluated value of the watch expression changes.
- WatchExpressionBreakType_OnExpressionTrue 
 –(Value: 0x2) Specifies to suspend the execution whenever the coerced value of the watch expression evaluates to
 True 
 . This option has no effect on arrays or containers.

#### See Also

[WatchExpression.BreakpointType](watchexpression-breakpointtype.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressionfilteroptions.html language=enus -->
## TOPIC 03062: WatchExpressionFilterOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressionfilteroptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressionfilteroptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify filtering options for the Engine.GetWatchExpressions method. To be included in the returned list, a watch expression must meet all the specified filters. WatchExpressionFilter_FilterByExecution –(Value: 0x2) Specifies that only watch expressions associated with the exe

### WatchExpressionFilterOptions

Use these constants to specify filtering options for the
 [Engine.GetWatchExpressions](engine-getwatchexpressions.html)
 method. To be included in the returned list, a watch expression must meet all the specified filters.

- WatchExpressionFilter_FilterByExecution 
 –(Value: 0x2) Specifies that only watch expressions associated with the execution the
 scopingSeqContext 
 parameter of the
 Engine.GetWatchExpressions 
 method specifies pass through this filter. Watch expressions that are not associated with any execution pass through this filter.
- WatchExpressionFilter_FilterBySequence 
 –(Value: 0x8) Specifies that only watch expressions that specify a
 WatchExpression.SequenceScope 
 property that matches the currently executing sequence the
 seqContext 
 parameter of the
 Engine.GetWatchExpressions 
 method specifies pass through this filter. Watch expressions that do not specify a sequence scope pass through this filter.
- WatchExpressionFilter_FilterBySequenceFile 
 –(Value: 0x4) Specifies that only watch expressions that specify a
 WatchExpression.SequenceFileScope 
 property that matches the currently executing sequence file the
 seqContext 
 parameter of the
 Engine.GetWatchExpressions 
 method specifies pass through this filter. Watch expressions that do not specify a sequence file scope pass through this filter.
- WatchExpressionFilter_IncludeGlobals 
 –(Value: 0x1) Specifies that global watch expressions that do not specify a client sequence file pass through the client sequence file filter. The global watch expressions included are in addition to the watch expressions that match the
 clientSequenceFile 
 parameter of the
 Engine.GetWatchExpressions 
 method.
- WatchExpressionFilter_NoOptions 
 –(Value: 0x0) Specifies that only the
 clientSequenceFile 
 parameter of the
 Engine.GetWatchExpressions 
 method filters the returned list. This returns all watch expressions if the
 clientSequenceFile 
 parameter is empty or only the watch expressions that specify a
 WatchExpression.ClientSequenceFile 
 property that matches the
 clientSequenceFile 
 parameter.

#### See Also

[Engine.GetWatchExpressions](engine-getwatchexpressions.html)

[WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

[WatchExpression.SequenceFileScope](watchexpression-sequencefilescope.html)

[WatchExpression.SequenceScope](watchexpression-sequencescope.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressions-clear.html language=enus -->
## TOPIC 03063: WatchExpressions.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressions-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressions-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpressions.Clear Purpose Removes all WatchExpression objects from both the collection and the watch expression list the engine maintains. Remarks This method releases only the references to the WatchExpression objects the collection and the engine hold. To delete the WatchExpression obj

### WatchExpressions.Clear

#### Syntax

[WatchExpressions](watchexpressions.html).Clear

#### Purpose

Removes all WatchExpression objects from both the collection and the watch expression list the engine maintains.

#### Remarks

This method releases only the references to the WatchExpression objects the collection and the engine hold. To delete the WatchExpression objects, you must release any other references to the WatchExpression objects.

#### See Also

[Engine.GetWatchExpressions](engine-getwatchexpressions.html)

[WatchExpression](watchexpression.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressions-clone.html language=enus -->
## TOPIC 03064: WatchExpressions.Clone

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressions-clone.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressions-clone.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpressions.Clone( [insertInEngine]) Return Value WatchExpressions A WatchExpression object collection that contains clones of the WatchExpression objects in the original collection. Purpose Clones the WatchExpression objects in the collection and returns the cloned objects in a new coll

### WatchExpressions.Clone

#### Syntax

[WatchExpressions](watchexpressions.html).Clone( [insertInEngine])

#### Return Value

[WatchExpressions](watchexpressions.html)

A WatchExpression object collection that contains clones of the WatchExpression objects in the original collection.

#### Purpose

Clones the WatchExpression objects in the collection and returns the cloned objects in a new collection.

#### Parameters

insertInEngine
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies if TestStand adds the new WatchExpression objects to the watch expression list the engine maintains. Pass
 True
 to add the watch expressions to the cloned collection and to the watch expression list the engine maintains. Pass
 False
 to add only the new watch expression to the cloned collection. If no value is specified, the behavior is the same as passing
 True
 .

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[WatchExpressions](watchexpressions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressions-count.html language=enus -->
## TOPIC 03065: WatchExpressions.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressions-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressions-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpressions.Count Data Type Long Purpose Returns the number of items in the collection. See Also Engine.GetWatchExpressions WatchExpression

### WatchExpressions.Count

#### Syntax

[WatchExpressions](watchexpressions.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[Engine.GetWatchExpressions](engine-getwatchexpressions.html)

[WatchExpression](watchexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressions-insert.html language=enus -->
## TOPIC 03066: WatchExpressions.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressions-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressions-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpressions.Insert( beforePos = NULL, [clientSequenceFileParam], [insertInEngine]) Return Value WatchExpression The newly created watch expression. Purpose Adds a new item to the collection and inserts it into the watch expression list. Remarks The TestStand Engine maintains a list of wa

### WatchExpressions.Insert

#### Syntax

[WatchExpressions](watchexpressions.html).Insert( beforePos = NULL, [clientSequenceFileParam], [insertInEngine])

#### Return Value

[WatchExpression](watchexpression.html)

The newly created watch expression.

#### Purpose

Adds a new item to the collection and inserts it into the watch expression list.

#### Remarks

The TestStand Engine maintains a list of watch expressions. The engine automatically evaluates watch expressions with conditional break settings during execution. The engine only monitors for value changes in watch expressions for which the current sequence context matches the scope the
 [WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)
 ,
 [WatchExpression.ExecutionScope](watchexpression-executionscope.html)
 and
 [WatchExpression.SequenceScope](watchexpression-sequencescope.html)
 properties define. To add the newly created watch expression to the watch expression list the engine maintains, pass
 True
 for the
 insertInEngine
 parameter.

If the
 [Engine.PersistWatchExpressions](engine-persistwatchexpressions.html)
 property is
 True
 , the engine associates the list of watch expressions with the current workspace. When you change the current workspace, the engine automatically saves the current watch expression list associated with the new workspace. The engine saves the watch expression list every time TestStand saves the workspace or sequence files in it.

#### Parameters

beforePos
 As
 [WatchExpression](watchexpression.html)

[In] Specifies a reference to a WatchExpression object already in the list to specify the object before which TestStand inserts the new WatchExpression object. Pass
 NULL
 to insert the new object at the end of the list.

This parameter has a default value of
 NULL
 .

clientSequenceFileParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies the client sequence file to associate with the newly created WatchExpression object. Pass
 NULL
 to create a global watch expression, a watch expression associated with no client sequence file. If this parameter is not specified, the parameter defaults to
 NULL
 .

insertInEngine
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies whether to insert the new WatchExpression object in the watch expression list the engine maintains. Pass
 True
 to add the watch expression to the collection and to the watch expression list the engine maintains. Pass
 False
 to add only the new watch expression to the collection. If no value is specified, the behavior is the same as passing
 True
 .

#### See Also

[Engine.GetWatchExpressions](engine-getwatchexpressions.html)

[Engine.PersistWatchExpressions](engine-persistwatchexpressions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[WatchExpression](watchexpression.html)

[WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

[WatchExpression.SequenceScope](watchexpression-sequencescope.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressions-item.html language=enus -->
## TOPIC 03067: WatchExpressions.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressions-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressions-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpressions.Item( index) Data Type WatchExpression The item at the specified index. Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the index of the item to retrieve within the collection. See Also Engine.GetWatc

### WatchExpressions.Item

#### Syntax

[WatchExpressions](watchexpressions.html).Item( index)

#### Data Type

[WatchExpression](watchexpression.html)

The item at the specified index.

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the index of the item to retrieve within the collection.

#### See Also

[Engine.GetWatchExpressions](engine-getwatchexpressions.html)

[WatchExpression](watchexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressions-remove.html language=enus -->
## TOPIC 03068: WatchExpressions.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressions-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressions-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WatchExpressions.Remove( WatchExpression) Purpose Removes a watch expression from the collection and the watch expression list that the engine maintains. Remarks This method removes only the watch expression from the collection and the watch expression list that the engine maintains. To delet

### WatchExpressions.Remove

#### Syntax

[WatchExpressions](watchexpressions.html).Remove( WatchExpression)

#### Purpose

Removes a watch expression from the collection and the watch expression list that the engine maintains.

#### Remarks

This method removes only the watch expression from the collection and the watch expression list that the engine maintains. To delete the WatchExpression object itself, you must release any references to the object after calling this method. This method does not return an error if the WatchExpression object is not in the collection or in the watch expression list that the engine maintains.

#### Parameters

WatchExpression
 As
 [WatchExpression](watchexpression.html)

[In] Specifies a reference to the WatchExpression object to remove from the collection.

#### See Also

[Engine.GetWatchExpressions](engine-getwatchexpressions.html)

[WatchExpression](watchexpression.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/watchexpressions.html language=enus -->
## TOPIC 03069: WatchExpressions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/watchexpressions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/watchexpressions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the WatchExpressions class are collections of objects of the WatchExpression class. Properties Count (Read Only) Item (Read Only) Methods Clear Clone Insert Remove See Also WatchExpression

### WatchExpressions

Objects of the WatchExpressions class are collections of objects of the WatchExpression class.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Clone |
| Insert |
| Remove |

#### See Also

[WatchExpression](watchexpression.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/windowactivationoptions.html language=enus -->
## TOPIC 03070: WindowActivationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/windowactivationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/windowactivationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants as the values of the Step.WindowActivation and StepType.WindowActivation properties. WinActOption_ActivateWhenStepCompletes –(Value: 2) Activate when the step completes. WinActOption_IfActiveReactivateWhenStepCompletes –(Value: 3) If initially active, reactivate when the step com

### WindowActivationOptions

Use these constants as the values of the
 [Step.WindowActivation](step-windowactivation.html)
 and
 [StepType.WindowActivation](steptype-windowactivation.html)
 properties.

- WinActOption_ActivateWhenStepCompletes 
 –(Value: 2) Activate when the step completes.
- WinActOption_IfActiveReactivateWhenStepCompletes 
 –(Value: 3) If initially active, reactivate when the step completes.
- WinActOption_None 
 –(Value: 1) No activation.

#### See Also

[Step.WindowActivation](step-windowactivation.html)

[StepType.WindowActivation](steptype-windowactivation.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/windowsfiledialogflags.html language=enus -->
## TOPIC 03071: WindowsFileDialogFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/windowsfiledialogflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/windowsfiledialogflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the win32Flags parameter of the Engine.DisplayFileDialog method. Use the bitwise-OR operator to specify more than one option. These flags are the same ones you pass to the Microsoft Windows Software Development Kit functions GetOpenFileName and

### WindowsFileDialogFlags

These constants represent the options you can use with the
 win32Flags
 parameter of the
 [Engine.DisplayFileDialog](engine-displayfiledialog.html)
 method. Use the bitwise-OR operator to specify more than one option.

These flags are the same ones you pass to the Microsoft Windows Software Development Kit functions GetOpenFileName and GetSaveFileName.

- WinFileDlg_ALLOWMULTISELECT 
 –(Value: 0x200) Specifies that the file list allows multiple selections.
- WinFileDlg_CREATEPROMPT 
 –(Value: 0x2000) If the user specifies a file that does not exist, this flag causes the dialog box to prompt the user for permission to create the file. If the user chooses to create the file, the dialog box closes, and the function returns the specified name. Otherwise, the dialog box remains open. This option does not actually create the file. If you use this flag with the
 WinFileDlg_ALLOWMULTISELECT 
 flag, the dialog box allows the user to specify only one non-existent file.
- WinFileDlg_DONTADDTORECENT 
 –(Value: 0x2000000) Prevents the system from adding a link to the selected file in the file system directory that contains the most recently used documents for the user.
- WinFileDlg_ENABLEHOOK 
 –(Value: 0x20) Do not use this flag because it has no effect.
- WinFileDlg_ENABLEINCLUDENOTIFY 
 –(Value: 0x400000) Do not use this flag because it has no effect.
- WinFileDlg_ENABLESIZING 
 –(Value: 0x800000) Do not use this flag because it has no effect.
- WinFileDlg_ENABLETEMPLATE 
 –(Value: 0x40) Do not use this flag because it has no effect.
- WinFileDlg_ENABLETEMPLATEHANDLE 
 –(Value: 0x80) Do not use this flag because it has no effect.
- WinFileDlg_EXPLORER 
 –(Value: 0x80000) Do not use this flag because it has no effect.
- WinFileDlg_EXTENSIONDIFFERENT 
 –(Value: 0x400) Do not use this flag because it has no effect.
- WinFileDlg_FILEMUSTEXIST 
 –(Value: 0x1000) Specifies that you can select only existing files. If you enter a file that does not exist, the dialog box displays a warning message. If this flag is specified, the
 WinFileDlg_PATHMUSTEXIST 
 flag is also used.
- WinFileDlg_FORCESHOWHIDDEN 
 –(Value: 0x10000000) Forces the showing of system and hidden files, thus overriding the user setting to show or not show hidden files. However, a file marked both system and hidden is not shown.
- WinFileDlg_HIDEREADONLY 
 –(Value: 0x4) Hides the Read Only option.
- WinFileDlg_LONGNAMES 
 –(Value: 0x200000) Do not use this flag because it has no effect.
- WinFileDlg_NOCHANGEDIR 
 –(Value: 0x8) Restores the current directory to the original value if the user changed the directory while searching for files.
- WinFileDlg_NODEREFERENCELINKS 
 –(Value: 100000) Directs the dialog box to return the path and filename of the selected shortcut (
 .LNK 
 ) file. If this value is not specified, the dialog box returns the path and filename of the file the shortcut references.
- WinFileDlg_NOLONGNAMES 
 –(Value: 0x40000) Do not use this flag because it has no effect.
- WinFileDlg_NONETWORKBUTTON 
 –(Value: 0x20000) Hides and disables the Network option.
- WinFileDlg_NOREADONLYRETURN 
 –(Value: 0x8000) Do not use this flag because it has no effect.
- WinFileDlg_NOTESTFILECREATE 
 –(Value: 0x10000) Do not use this flag because it has no effect.
- WinFileDlg_NOVALIDATE 
 –(Value: 0x100) Specifies that the dialog box allow invalid characters in the returned filename.
- WinFileDlg_OVERWRITEPROMPT 
 –(Value: 0x2) Causes the dialog box to generate a message box if the selected file already exists. The user must confirm whether to overwrite the file.
- WinFileDlg_PATHMUSTEXIST 
 –(Value: 0x800) Specifies that you can type only valid paths and filenames. If this flag is used and the you type an invalid path, the dialog box displays a warning.
- WinFileDlg_READONLY 
 –(Value: 0x1) Causes the Read Only option to be selected initially when the dialog box is created. This flag indicates the state of the Read Only option when the dialog box is closed.
- WinFileDlg_SHAREAWARE 
 –(Value: 0x4000) Do not use this flag because it has no effect.
- WinFileDlg_SHOWHELP 
 –(Value: 0x10) Do not use this flag because it has no effect. The Help button is always visible.

#### See Also

[Engine.DisplayFileDialog](engine-displayfiledialog.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacebrowserdialogoptions.html language=enus -->
## TOPIC 03072: WorkspaceBrowserDialogOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacebrowserdialogoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacebrowserdialogoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the dlgOptions parameter of the Engine.DisplayWorkspaceBrowserDialog method. WorkspaceBrowserDlgOption_Editable –(Value: 1) Enable the dialog box to edit the contents of the currently loaded workspace and the project files in the workspace. WorkspaceBrowserDlgOption_ModalToA

### WorkspaceBrowserDialogOptions

Use these constants with the
 dlgOptions
 parameter of the
 [Engine.DisplayWorkspaceBrowserDialog](engine-displayworkspacebrowserdialog.html)
 method.

- WorkspaceBrowserDlgOption_Editable 
 –(Value: 1) Enable the dialog box to edit the contents of the currently loaded workspace and the project files in the workspace.
- WorkspaceBrowserDlgOption_ModalToAppMainWind 
 –(Value: 0x00010000) By default, the dialog box is modal to the last active window of the calling thread, or if none exists, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 Engine.AppMainHwnd 
 property. Typically, you do not need to set this option.
- WorkspaceBrowserDlgOption_NoOptions 
 –(Value: 0) No options.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayWorkspaceBrowserDialog](engine-displayworkspacebrowserdialog.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-aspropertyobjectfile.html language=enus -->
## TOPIC 03073: WorkspaceFile.AsPropertyObjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-aspropertyobjectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-aspropertyobjectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.AsPropertyObjectFile Return Value PropertyObjectFile Purpose Returns the underlying PropertyObjectFile that represents the WorkspaceFile object. See Also PropertyObjectFile

### WorkspaceFile.AsPropertyObjectFile

#### Syntax

[WorkspaceFile](workspacefile.html).AsPropertyObjectFile

#### Return Value

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the underlying PropertyObjectFile that represents the WorkspaceFile object.

#### See Also

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-displayaddfiletoworkspacedialog.html language=enus -->
## TOPIC 03074: WorkspaceFile.DisplayAddFileToWorkspaceDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-displayaddfiletoworkspacedialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-displayaddfiletoworkspacedialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.DisplayAddFileToWorkspaceDialog( selectedProject, fullPath) Return Value Boolean Returns True if the file was added to the workspace. Purpose Launches the Add File To Workspace dialog box, in which you can add a file to the workspace file at the location you select. Parameters s

### WorkspaceFile.DisplayAddFileToWorkspaceDialog

#### Syntax

[WorkspaceFile](workspacefile.html).DisplayAddFileToWorkspaceDialog( selectedProject, fullPath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the file was added to the workspace.

#### Purpose

Launches the
 [Add File To Workspace](../tsref/add-file-to-workspace-dialog-box.html)
 dialog box, in which you can add a file to the workspace file at the location you select.

#### Parameters

selectedProject
 As
 [WorkspaceObject](workspaceobject.html)

[In] Specifies the currently selected project in the workspace. Pass a
 NULL
 reference if nothing is selected.

fullPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute pathname of the file to add it to the workspace.

#### See Also

[Add File To Workspace dialog box](../tsref/add-file-to-workspace-dialog-box.html)

[WorkspaceObject](workspaceobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-findworkspaceobject.html language=enus -->
## TOPIC 03075: WorkspaceFile.FindWorkspaceObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-findworkspaceobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-findworkspaceobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.FindWorkspaceObject( fullPath) Return Value WorkspaceObject Returns the first WorkspaceObject in the workspace that corresponds to the specified pathname. Returns a NULL reference if no object is found. Purpose Finds a WorkspaceObject for the specified pathname. Parameters fullP

### WorkspaceFile.FindWorkspaceObject

#### Syntax

[WorkspaceFile](workspacefile.html).FindWorkspaceObject( fullPath)

#### Return Value

[WorkspaceObject](workspaceobject.html)

Returns the first WorkspaceObject in the workspace that corresponds to the specified pathname. Returns a
 NULL
 reference if no object is found.

#### Purpose

Finds a WorkspaceObject for the specified pathname.

#### Parameters

fullPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies ss the absolute pathname of the file to find.

#### See Also

[WorkspaceObject](workspaceobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-isconnectedtoscprovider.html language=enus -->
## TOPIC 03076: WorkspaceFile.IsConnectedToSCProvider

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-isconnectedtoscprovider.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-isconnectedtoscprovider.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.IsConnectedToSCProvider Data Type Boolean Purpose Returns a value that indicates whether the workspace file is connected to a source code control (SCC) provider. Remarks TestStand connects a workspace file to an SCC provider when you set the Engine.CurrentWorkspaceFile property.

### WorkspaceFile.IsConnectedToSCProvider

#### Syntax

[WorkspaceFile](workspacefile.html).IsConnectedToSCProvider

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the workspace file is connected to a source code control (SCC) provider.

#### Remarks

TestStand connects a workspace file to an SCC provider when you set the
 [Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)
 property. The
 [WorkspaceFile.ProviderName](workspacefile-providername.html)
 property specifies the associated provider. If the workspace file does not have a provider associated with it, TestStand connects to the default provider specified in the registry at
 HKEY_LOCAL_MACHINE\SOFTWARE\SourceCodeControlProvider
 .
 (32-bit TestStand)
 On 64-bit operating systems, this registry key appears only in the 32-bit registry. Use the path
 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\SourceCodeControlProvider
 to access the key in the registry editor.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[StationOptions.SystemDefaultSourceCodeControlProvider](stationoptions-systemdefaultsourcecodecontrol.html)

[WorkspaceFile.ProviderName](workspacefile-providername.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-optionsfile.html language=enus -->
## TOPIC 03077: WorkspaceFile.OptionsFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-optionsfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-optionsfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.OptionsFile Data Type PropertyObjectFile Purpose Returns the workspace options file. Remarks The workspace options file is a file with the same base name as the workspace file, but with the .tso extension. TestStand saves information in this file to preserve certain user setting

### WorkspaceFile.OptionsFile

#### Syntax

[WorkspaceFile](workspacefile.html).OptionsFile

#### Data Type

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the workspace options file.

#### Remarks

The workspace options file is a file with the same base name as the workspace file, but with the
 .tso
 extension. TestStand saves information in this file to preserve certain user settings, such as window positions, source code control information, and the expansion state of the Workspace pane.

Note

#### See Also

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-providername.html language=enus -->
## TOPIC 03078: WorkspaceFile.ProviderName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-providername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-providername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.ProviderName Data Type String Purpose Specifies the name of the source code control provider. The registry key entries located in HKEY_LOCAL_MACHINE\Software\SourceCodeControlProvider\InstalledSCCProviders define the name for a provider. (32-bit TestStand) On 64-bit operating sy

### WorkspaceFile.ProviderName

#### Syntax

[WorkspaceFile](workspacefile.html).ProviderName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the source code control provider. The registry key entries located in
 HKEY_LOCAL_MACHINE\Software\SourceCodeControlProvider\InstalledSCCProviders
 define the name for a provider.
 (32-bit TestStand)
 On 64-bit operating systems, this registry key appears only in the 32-bit registry. Use the path
 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\SourceCodeControlProvider\InstalledSCCProviders
 to access the key in the registry editor.

#### Remarks

This property returns
 <None>
 if the workspace does not specify any provider. An empty value specifies to use the default provider specified by the system.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-rootworkspaceobject.html language=enus -->
## TOPIC 03079: WorkspaceFile.RootWorkspaceObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-rootworkspaceobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-rootworkspaceobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.RootWorkspaceObject Data Type WorkspaceObject Purpose Returns the root WorkspaceObject. Remarks This object contains all the projects the workspace file contains. See Also WorkspaceObject

### WorkspaceFile.RootWorkspaceObject

#### Syntax

[WorkspaceFile](workspacefile.html).RootWorkspaceObject

#### Data Type

[WorkspaceObject](workspaceobject.html)

#### Purpose

Returns the root WorkspaceObject.

#### Remarks

This object contains all the projects the workspace file contains.

#### See Also

[WorkspaceObject](workspaceobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-runsourcecontrolprovider.html language=enus -->
## TOPIC 03080: WorkspaceFile.RunSourceControlProvider

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-runsourcecontrolprovider.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-runsourcecontrolprovider.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.RunSourceControlProvider Purpose Launches the user interface of the source code control provider.

### WorkspaceFile.RunSourceControlProvider

#### Syntax

[WorkspaceFile](workspacefile.html).RunSourceControlProvider

#### Purpose

Launches the user interface of the source code control provider.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile-saveworkspaceandprojectfiles.html language=enus -->
## TOPIC 03081: WorkspaceFile.SaveWorkspaceAndProjectFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile-saveworkspaceandprojectfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile-saveworkspaceandprojectfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceFile.SaveWorkspaceAndProjectFiles( options = SaveWorkspaceFile_NoOptions) Return Value Boolean Returns False if you click Cancel in the Prompt dialog box. Purpose Writes the contents of the workspace file and the projects to disk if the files have been modified. Remarks This method d

### WorkspaceFile.SaveWorkspaceAndProjectFiles

#### Syntax

[WorkspaceFile](workspacefile.html).SaveWorkspaceAndProjectFiles( options = SaveWorkspaceFile_NoOptions)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 False
 if you click
 Cancel
 in the Prompt dialog box.

#### Purpose

Writes the contents of the workspace file and the projects to disk if the files have been modified.

#### Remarks

This method does nothing if the workspace and project files have not been modified. If the files have been modified, this method prompts the user with the option to save and then writes the files.
 [PropertyObjectFile.Path](propertyobjectfile-path.html)
 determines the pathname of the file to write. If an error occurs while saving any of the files, an exception is thrown containing all the files that could not be saved.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [SaveWorkspaceFileOptions](saveworkspacefileoptions.html)
 constants. Use the bitwise-OR operator to specify more than one options.

This parameter has a default value of
 SaveWorkspaceFile_NoOptions
 .

#### See Also

[PropertyObjectFile.IsModified](propertyobjectfile-ismodified.html)

[PropertyObjectFile.Path](propertyobjectfile-path.html)

[PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)

[SaveWorkspaceFileOptions](saveworkspacefileoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspacefile.html language=enus -->
## TOPIC 03082: WorkspaceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspacefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspacefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the WorkspaceFile class represent workspace files that can contain projects. A workspace file contains a list of project files and source code control provider information. Each project file contains lists of sequence files, code modules, and other files required by a particular test syst

### WorkspaceFile

Objects of the WorkspaceFile class represent workspace files that can contain projects. A workspace file contains a list of project files and source code control provider information. Each project file contains lists of sequence files, code modules, and other files required by a particular test system.

To perform read or write operations for objects from the WorkspaceFile class, obtain a reference to the PropertyObjectFile interface by using the
 [WorkspaceFile.AsPropertyObjectFile](workspacefile-aspropertyobjectfile.html)
 method, then use the
 [PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)
 and
 [PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)
 methods, respectively.

#### Properties

| IsConnectedToSCProvider (Read Only) |
| --- |
| OptionsFile (Read Only) |
| ProviderName |
| RootWorkspaceObject (Read Only) |

#### Methods

| AsPropertyObjectFile |
| --- |
| DisplayAddFileToWorkspaceDialog |
| FindWorkspaceObject |
| RunSourceControlProvider |
| SaveWorkspaceAndProjectFiles |

#### See Also

[AsPropertyObjectFile](workspacefile-aspropertyobjectfile.html)

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)

[PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)

[WorkspaceObject](workspaceobject.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-aspropertyobject.html language=enus -->
## TOPIC 03083: WorkspaceObject.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the WorkspaceObject object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### WorkspaceObject.AsPropertyObject

#### Syntax

[WorkspaceObject](workspaceobject.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the WorkspaceObject object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-candosourcecontrolcommand.html language=enus -->
## TOPIC 03084: WorkspaceObject.CanDoSourceControlCommand

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-candosourcecontrolcommand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-candosourcecontrolcommand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.CanDoSourceControlCommand( scCommand, options = 0, [itemList]) Return Value Boolean Returns True if the command is supported. Purpose Indicates if the provider supports the specified source code control command for the specified files. Remarks Call this function to determine w

### WorkspaceObject.CanDoSourceControlCommand

#### Syntax

[WorkspaceObject](workspaceobject.html).CanDoSourceControlCommand( scCommand, options = 0, [itemList])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the command is supported.

#### Purpose

Indicates if the provider supports the specified source code control command for the specified files.

#### Remarks

Call this function to determine whether you can call the
 [WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)
 method on the selected files.

#### Parameters

scCommand
 As
 [SourceControlCommands](sourcecontrolcommands.html)

[In] Specifies the command to check.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more of the
 [SourceControlCommandOptions](sourcecontrolcommandoptions.html)
 constants.

This parameter has a default value of
 0
 .

itemList
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an array of WorkspaceObjects that specifies the selected files. If you omit this argument, the method uses the file associated with this WorkspaceObject.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SourceControlCommandOptions](sourcecontrolcommandoptions.html)

[WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)

[WorkspaceObject.SourceControlStatus](workspaceobject-sourcecontrolstatus.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-codemoduleseqfilepath.html language=enus -->
## TOPIC 03085: WorkspaceObject.CodeModuleSeqFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-codemoduleseqfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-codemoduleseqfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.CodeModuleSeqFilePath Data Type String The pathname of the sequence file. This pathname can be relative. Purpose Specifies the pathname of the sequence file to which this code module belongs. Remarks This property associates a WorkspaceObject with a particular sequence file. C

### WorkspaceObject.CodeModuleSeqFilePath

#### Syntax

[WorkspaceObject](workspaceobject.html).CodeModuleSeqFilePath

#### Data Type

[String](data-types-for-teststand.html)

The pathname of the sequence file. This pathname can be relative.

#### Purpose

Specifies the pathname of the sequence file to which this code module belongs.

#### Remarks

This property associates a WorkspaceObject with a particular sequence file. Code modules that are stored in the workspace use the property to determine to which sequence file they belong.

#### See Also

[WorkspaceObject.InsertCodeModules](workspaceobject-insertcodemodules.html)

[WorkspaceObject.IsCodeModule](workspaceobject-iscodemodule.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-displayname.html language=enus -->
## TOPIC 03086: WorkspaceObject.DisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-displayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-displayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.DisplayName Data Type String Purpose Specifies the display name for this WorkspaceObject. Remarks Generally, the display name is the name of the file, if one exists. See Also WorkspaceObject.GetAbsolutePath WorkspaceObject.ObjectType WorkspaceObject.Path

### WorkspaceObject.DisplayName

#### Syntax

[WorkspaceObject](workspaceobject.html).DisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the display name for this WorkspaceObject.

#### Remarks

Generally, the display name is the name of the file, if one exists.

#### See Also

[WorkspaceObject.GetAbsolutePath](workspaceobject-getabsolutepath.html)

[WorkspaceObject.ObjectType](workspaceobject-objecttype.html)

[WorkspaceObject.Path](workspaceobject-path.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-dosourcecontrolcommand.html language=enus -->
## TOPIC 03087: WorkspaceObject.DoSourceControlCommand

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-dosourcecontrolcommand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-dosourcecontrolcommand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.DoSourceControlCommand( scCommand, modifiedObject, options, [itemList]) Return Value Boolean Returns True if the command was completed successfully for all specified files. Purpose Performs the specified source code control command on the specified files. Remarks Call the Work

### WorkspaceObject.DoSourceControlCommand

#### Syntax

[WorkspaceObject](workspaceobject.html).DoSourceControlCommand( scCommand, modifiedObject, options, [itemList])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the command was completed successfully for all specified files.

#### Purpose

Performs the specified source code control command on the specified files.

#### Remarks

Call the
 [WorkspaceObject.CanDoSourceControlCommand](workspaceobject-candosourcecontrolcommand.html)
 method before calling this method.

#### Parameters

scCommand
 As
 [SourceControlCommands](sourcecontrolcommands.html)

[In] Specifies the source code control command to perform.

modifiedObject
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the command modified the workspace file.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more of the
 [SourceControlCommandOptions](sourcecontrolcommandoptions.html)
 constants.

itemList
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an array of WorkspaceObjects that specifies the selected files. If you omit this argument, the method uses the file associated with this WorkspaceObject.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SourceControlCommandOptions](sourcecontrolcommandoptions.html)

[SourceControlStatus](workspaceobject-sourcecontrolstatus.html)

[WorkspaceObject.CanDoSourceControlCommand](workspaceobject-candosourcecontrolcommand.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-fileexists.html language=enus -->
## TOPIC 03088: WorkspaceObject.FileExists

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-fileexists.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-fileexists.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.FileExists Data Type Boolean Purpose Returns a value that indicates whether the file associated with the WorkspaceObject exists. Remarks This method is valid only on WorkspaceObjects that contain a pathname. See Also WorkspaceObject.GetAbsolutePath WorkspaceObject.ObjectType W

### WorkspaceObject.FileExists

#### Syntax

[WorkspaceObject](workspaceobject.html).FileExists

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the file associated with the WorkspaceObject exists.

#### Remarks

This method is valid only on WorkspaceObjects that contain a pathname.

#### See Also

[WorkspaceObject.GetAbsolutePath](workspaceobject-getabsolutepath.html)

[WorkspaceObject.ObjectType](workspaceobject-objecttype.html)

[WorkspaceObject.Path](workspaceobject-path.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-getabsolutepath.html language=enus -->
## TOPIC 03089: WorkspaceObject.GetAbsolutePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-getabsolutepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-getabsolutepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.GetAbsolutePath Return Value String Purpose Returns the absolute pathname of the file associated with this WorkspaceObject. See Also WorkspaceObject.Path

### WorkspaceObject.GetAbsolutePath

#### Syntax

[WorkspaceObject](workspaceobject.html).GetAbsolutePath

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute pathname of the file associated with this WorkspaceObject.

#### See Also

[WorkspaceObject.Path](workspaceobject-path.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-getcontainedobject.html language=enus -->
## TOPIC 03090: WorkspaceObject.GetContainedObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-getcontainedobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-getcontainedobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.GetContainedObject( index) Return Value WorkspaceObject Purpose Returns the WorkspaceObject the index specifies. Parameters index As Long [In] Specifies the zero-based index of the object contained by this WorkspaceObject. See Also WorkspaceObject WorkspaceObject.GetParentCont

### WorkspaceObject.GetContainedObject

#### Syntax

[WorkspaceObject](workspaceobject.html).GetContainedObject( index)

#### Return Value

[WorkspaceObject](workspaceobject.html)

#### Purpose

Returns the WorkspaceObject the index specifies.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the object contained by this WorkspaceObject.

#### See Also

[WorkspaceObject](workspaceobject.html)

[WorkspaceObject.GetParentContainer](workspaceobject-getparentcontainer.html)

[WorkspaceObject.NumContainedObjects](workspaceobject-numcontainedobjects.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-getparentcontainer.html language=enus -->
## TOPIC 03091: WorkspaceObject.GetParentContainer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-getparentcontainer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-getparentcontainer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.GetParentContainer Return Value WorkspaceObject Purpose Returns the parent WorkspaceObject that contains this WorkspaceObject. Remarks This method returns a NULL reference for the parent WorkspaceObject. See Also WorkspaceFile.RootWorkspaceObject WorkspaceObject WorkspaceObjec

### WorkspaceObject.GetParentContainer

#### Syntax

[WorkspaceObject](workspaceobject.html).GetParentContainer

#### Return Value

[WorkspaceObject](workspaceobject.html)

#### Purpose

Returns the parent WorkspaceObject that contains this WorkspaceObject.

#### Remarks

This method returns a
 NULL
 reference for the parent WorkspaceObject.

#### See Also

[WorkspaceFile.RootWorkspaceObject](workspacefile-rootworkspaceobject.html)

[WorkspaceObject](workspaceobject.html)

[WorkspaceObject.GetContainedObject](workspaceobject-getcontainedobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-insertcodemodules.html language=enus -->
## TOPIC 03092: WorkspaceObject.InsertCodeModules

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-insertcodemodules.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-insertcodemodules.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.InsertCodeModules( [itemList]) Return Value Object Array Returns an array of WorkspaceObjects that were added to the workspace. Purpose Inserts WorkspaceObjects for the code modules of the specified sequence files. Remarks This method traverses the WorkspaceObject hierarchy se

### WorkspaceObject.InsertCodeModules

#### Syntax

[WorkspaceObject](workspaceobject.html).InsertCodeModules( [itemList])

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns an array of WorkspaceObjects that were added to the workspace.

#### Purpose

Inserts WorkspaceObjects for the code modules of the specified sequence files.

#### Remarks

This method traverses the WorkspaceObject hierarchy searching for sequence files. For each sequence file it finds, this method finds all the code modules in the sequence file and adds a WorkspaceObject for each one to the workspace.

Note

#### Parameters

itemList
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an array of WorkspaceObjects that specifies the selected files. If you omit this argument, the method uses this WorkspaceObject.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-insertobject.html language=enus -->
## TOPIC 03093: WorkspaceObject.InsertObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-insertobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-insertobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.InsertObject( obj, index) Purpose Inserts a WorkspaceObject at the specified index under another WorkspaceObject. Remarks Use the WorkspaceObject.NewFile or WorkspaceObject.NewFolder method to create a new WorkspaceObject. Parameters obj As WorkspaceObject [In] Specifies the W

### WorkspaceObject.InsertObject

#### Syntax

[WorkspaceObject](workspaceobject.html).InsertObject( obj, index)

#### Purpose

Inserts a WorkspaceObject at the specified index under another WorkspaceObject.

#### Remarks

Use the
 [WorkspaceObject.NewFile](workspaceobject-newfile.html)
 or
 [WorkspaceObject.NewFolder](workspaceobject-newfolder.html)
 method to create a new WorkspaceObject.

#### Parameters

obj
 As
 [WorkspaceObject](workspaceobject.html)

[In] Specifies the WorkspaceObject to be insert.

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index specifying the location at which to insert the WorkspaceObject.

#### See Also

[WorkspaceObject](workspaceobject.html)

[WorkspaceObject.NewFile](workspaceobject-newfile.html)

[WorkspaceObject.NewFolder](workspaceobject-newfolder.html)

[WorkspaceObject.NumContainedObjects](workspaceobject-numcontainedobjects.html)

[WorkspaceObject.RemoveObject](workspaceobject-removeobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-iscodemodule.html language=enus -->
## TOPIC 03094: WorkspaceObject.IsCodeModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-iscodemodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-iscodemodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.IsCodeModule Data Type Boolean Purpose Returns a value that indicates whether the WorkspaceObject refers to a code module. See Also WorkspaceObject.ObjectType

### WorkspaceObject.IsCodeModule

#### Syntax

[WorkspaceObject](workspaceobject.html).IsCodeModule

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the WorkspaceObject refers to a code module.

#### See Also

[WorkspaceObject.ObjectType](workspaceobject-objecttype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-lastsourcecontrolmessages.html language=enus -->
## TOPIC 03095: WorkspaceObject.LastSourceControlMessages

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-lastsourcecontrolmessages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-lastsourcecontrolmessages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.LastSourceControlMessages Data Type String Purpose Returns the most recent information and error messages the source code control provider reports. Remarks Call this method after calling the WorkspaceObject.DoSourceControlCommand method to obtain any messages the SCC provider

### WorkspaceObject.LastSourceControlMessages

#### Syntax

[WorkspaceObject](workspaceobject.html).LastSourceControlMessages

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the most recent information and error messages the source code control provider reports.

#### Remarks

Call this method after calling the
 [WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)
 method to obtain any messages the SCC provider reports.

#### See Also

[WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-newfile.html language=enus -->
## TOPIC 03096: WorkspaceObject.NewFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-newfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-newfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.NewFile( path) Return Value WorkspaceObject Purpose Creates a new WorkspaceObject associated with the specified pathname. Remarks Use the WorkspaceObject.InsertObject method to insert the object into the workspace. This method uses the file extension to determine the type of W

### WorkspaceObject.NewFile

#### Syntax

[WorkspaceObject](workspaceobject.html).NewFile( path)

#### Return Value

[WorkspaceObject](workspaceobject.html)

#### Purpose

Creates a new WorkspaceObject associated with the specified pathname.

#### Remarks

Use the
 [WorkspaceObject.InsertObject](workspaceobject-insertobject.html)
 method to insert the object into the workspace. This method uses the file extension to determine the type of WorkspaceObject.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname associated with the WorkspaceObject. This pathname can be relative.

#### See Also

[WorkspaceObject](workspaceobject.html)

[WorkspaceObject.InsertObject](workspaceobject-insertobject.html)

[WorkspaceObject.NewFolder](workspaceobject-newfolder.html)

[WorkspaceObject.ObjectType](workspaceobject-objecttype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-newfolder.html language=enus -->
## TOPIC 03097: WorkspaceObject.NewFolder

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-newfolder.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-newfolder.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.NewFolder( Name) Return Value WorkspaceObject Purpose Creates a WorkspaceObject folder. Remarks Use the WorkspaceObject.InsertObject method to insert the object into the workspace. Parameters Name As String [In] Specifies the name of the folder. See Also WorkspaceObject Worksp

### WorkspaceObject.NewFolder

#### Syntax

[WorkspaceObject](workspaceobject.html).NewFolder( Name)

#### Return Value

[WorkspaceObject](workspaceobject.html)

#### Purpose

Creates a WorkspaceObject folder.

#### Remarks

Use the
 [WorkspaceObject.InsertObject](workspaceobject-insertobject.html)
 method to insert the object into the workspace.

#### Parameters

Name
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the folder.

#### See Also

[WorkspaceObject](workspaceobject.html)

[WorkspaceObject.InsertObject](workspaceobject-insertobject.html)

[WorkspaceObject.NewFile](workspaceobject-newfile.html)

[WorkspaceObject.ObjectType](workspaceobject-objecttype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-numcontainedobjects.html language=enus -->
## TOPIC 03098: WorkspaceObject.NumContainedObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-numcontainedobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-numcontainedobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.NumContainedObjects Data Type Long Purpose Returns the number of objects that this WorkspaceObject contains. See Also WorkspaceObject.InsertObject WorkspaceObject.ObjectType

### WorkspaceObject.NumContainedObjects

#### Syntax

[WorkspaceObject](workspaceobject.html).NumContainedObjects

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of objects that this WorkspaceObject contains.

#### See Also

[WorkspaceObject.InsertObject](workspaceobject-insertobject.html)

[WorkspaceObject.ObjectType](workspaceobject-objecttype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-objecttype.html language=enus -->
## TOPIC 03099: WorkspaceObject.ObjectType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-objecttype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-objecttype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.ObjectType Data Type WorkspaceObjectTypes Use the following constants with this data type: WorkspaceObjType_Folder –(Value: 3) Specifies a folder object. Folders do not have a pathname associated with them. WorkspaceObjType_OtherFile –(Value: 5) Specifies a file other than a s

### WorkspaceObject.ObjectType

#### Syntax

[WorkspaceObject](workspaceobject.html).ObjectType

#### Data Type

[WorkspaceObjectTypes](workspaceobjecttypes.html)

Use the following constants with this data type:

- WorkspaceObjType_Folder 
 –(Value: 3) Specifies a folder object. Folders do not have a pathname associated with them.
- WorkspaceObjType_OtherFile 
 –(Value: 5) Specifies a file other than a sequence file, workspace file, or project file, such as a code module. This type of object cannot contain other objects.
- WorkspaceObjType_ProjectFile 
 –(Value: 2) Specifies a project file object.
- WorkspaceObjType_SequenceFile 
 –(Value: 4) Specifies a sequence file object.
- WorkspaceObjType_WorkspaceFile 
 –(Value: 1) Specifies a workspace file object.

#### Purpose

Returns the WorkspaceObject type.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-path.html language=enus -->
## TOPIC 03100: WorkspaceObject.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.Path Data Type String Purpose Returns the pathname associated with the WorkspaceObject. Remarks Folder objects do not contain a pathname. The pathname can be relative.

### WorkspaceObject.Path

#### Syntax

[WorkspaceObject](workspaceobject.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the pathname associated with the WorkspaceObject.

#### Remarks

Folder objects do not contain a pathname. The pathname can be relative.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-projectfile.html language=enus -->
## TOPIC 03101: WorkspaceObject.ProjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-projectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-projectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.ProjectFile Data Type PropertyObjectFile Purpose Returns the project file to which this object belongs. Remarks All WorkspaceObjects belong to a single project file in the workspace. See Also PropertyObjectFile WorkspaceObject.GetAbsolutePath WorkspaceObject.ObjectType Workspa

### WorkspaceObject.ProjectFile

#### Syntax

[WorkspaceObject](workspaceobject.html).ProjectFile

#### Data Type

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the project file to which this object belongs.

#### Remarks

All WorkspaceObjects belong to a single project file in the workspace.

#### See Also

[PropertyObjectFile](propertyobjectfile.html)

[WorkspaceObject.GetAbsolutePath](workspaceobject-getabsolutepath.html)

[WorkspaceObject.ObjectType](workspaceobject-objecttype.html)

[WorkspaceObject.Path](workspaceobject-path.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-removeobject.html language=enus -->
## TOPIC 03102: WorkspaceObject.RemoveObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-removeobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-removeobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.RemoveObject( index) Return Value WorkspaceObject Returns the removed object. Purpose Removes the WorkspaceObject at the specified index. Parameters index As Long [In] Specifies the zero-based index of the object to remove. See Also WorkspaceObject.InsertObject WorkspaceObject

### WorkspaceObject.RemoveObject

#### Syntax

[WorkspaceObject](workspaceobject.html).RemoveObject( index)

#### Return Value

[WorkspaceObject](workspaceobject.html)

Returns the removed object.

#### Purpose

Removes the WorkspaceObject at the specified index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the object to remove.

#### See Also

[WorkspaceObject.InsertObject](workspaceobject-insertobject.html)

[WorkspaceObject.NumContainedObjects](workspaceobject-numcontainedobjects.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-sourcecontrolstatus.html language=enus -->
## TOPIC 03103: WorkspaceObject.SourceControlStatus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-sourcecontrolstatus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-sourcecontrolstatus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.SourceControlStatus Data Type Long One of the values in SourceControlStatuses . Purpose Returns the current source code control status of this WorkspaceObject. See Also SourceControlStatuses

### WorkspaceObject.SourceControlStatus

#### Syntax

[WorkspaceObject](workspaceobject.html).SourceControlStatus

#### Data Type

[Long](data-types-for-teststand.html)

One of the values in
 [SourceControlStatuses](sourcecontrolstatuses.html)
 .

#### Purpose

Returns the current source code control status of this WorkspaceObject.

#### See Also

[SourceControlStatuses](sourcecontrolstatuses.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject-updatestatus.html language=enus -->
## TOPIC 03104: WorkspaceObject.UpdateStatus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject-updatestatus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject-updatestatus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax WorkspaceObject.UpdateStatus( options = 0) Purpose Updates the source code control status of the specified WorkspaceObjects. Parameters options As Long [In] Pass SCCmdOption_DoNotRecurse to specify only this WorkspaceObject. Otherwise, this method updates the status of all contained objects a

### WorkspaceObject.UpdateStatus

#### Syntax

[WorkspaceObject](workspaceobject.html).UpdateStatus( options = 0)

#### Purpose

Updates the source code control status of the specified WorkspaceObjects.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 [SCCmdOption_DoNotRecurse](sourcecontrolcommandoptions.html)
 to specify only this WorkspaceObject. Otherwise, this method updates the status of all contained objects as well.

This parameter has a default value of
 0
 .

#### See Also

[SourceControlCommandOptions](sourcecontrolcommandoptions.html)

[SourceControlStatus](workspaceobject-sourcecontrolstatus.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobject.html language=enus -->
## TOPIC 03105: WorkspaceObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the WorkspaceObject class represent nodes for workspace and project files on the Workspace pane. Workspace objects handle all source code control operations on files. Properties CodeModuleSeqFilePath DisplayName FileExists (Read Only) IsCodeModule (Read Only) LastSourceControlMessages (Re

### WorkspaceObject

Objects of the WorkspaceObject class represent nodes for workspace and project files on the Workspace pane. Workspace objects handle all source code control operations on files.

#### Properties

| CodeModuleSeqFilePath |
| --- |
| DisplayName |
| FileExists (Read Only) |
| IsCodeModule (Read Only) |
| LastSourceControlMessages (Read Only) |
| NumContainedObjects (Read Only) |
| ObjectType (Read Only) |
| Path |
| ProjectFile (Read Only) |
| SourceControlStatus (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| CanDoSourceControlCommand |
| DoSourceControlCommand |
| GetAbsolutePath |
| GetContainedObject |
| GetParentContainer |
| InsertCodeModules |
| InsertObject |
| NewFile |
| NewFolder |
| RemoveObject |
| UpdateStatus |

#### See Also

[WorkspaceFile.RootWorkspaceObject](workspacefile-rootworkspaceobject.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/workspaceobjecttypes.html language=enus -->
## TOPIC 03106: WorkspaceObjectTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/workspaceobjecttypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/workspaceobjecttypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify the type of a workspace object. Use the values of this enumeration with the WorkspaceObject.ObjectType property. WorkspaceObjType_Folder –(Value: 3) Specifies a folder object. Folders do not have a pathname associated with them. WorkspaceObjType_OtherFile

### WorkspaceObjectTypes

This data type contains values that specify the type of a workspace object. Use the values of this enumeration with the
 [WorkspaceObject.ObjectType](workspaceobject-objecttype.html)
 property.

- WorkspaceObjType_Folder 
 –(Value: 3) Specifies a folder object. Folders do not have a pathname associated with them.
- WorkspaceObjType_OtherFile 
 –(Value: 5) Specifies a file other than a sequence file, workspace file, or project file, such as a code module. This type of object cannot contain other objects.
- WorkspaceObjType_ProjectFile 
 –(Value: 2) Specifies a project file object.
- WorkspaceObjType_SequenceFile 
 –(Value: 4) Specifies a sequence file object.
- WorkspaceObjType_WorkspaceFile 
 –(Value: 1) Specifies a workspace file object.

#### See Also

[WorkspaceObject.ObjectType](workspaceobject-objecttype.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/writefileformat.html language=enus -->
## TOPIC 03107: WriteFileFormat

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/writefileformat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/writefileformat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants specify the file format version TestStand uses to write a file. If you save a sequence file in a previous format and the file contains step types not present in the previous version of TestStand or if the file uses features the previous version of TestStand does not support, the sequ

### WriteFileFormat

These constants specify the file format version TestStand uses to write a file.

If you save a sequence file in a previous format and the file contains step types not present in the previous version of TestStand or if the file uses features the previous version of TestStand does not support, the sequence file you save will not function correctly.

Note

- WriteFileFormat_Current 
 –(Value: 1) Specifies that TestStand writes out the file using the current TestStand file format.
- WriteFileFormat_TestStand_14_0 
 –(Value: 14) Specifies that TestStand writes out the file using the TestStand 2014 file format. Save the file in this format to enable TestStand version 2014 to load the file. TestStand 14.0 is the internal
 
 version number 
 for TestStand 2014.
- WriteFileFormat_TestStand_16_0 
 –(Value: 15) Specifies that TestStand writes out the file using the TestStand 2016 file format. Save the file in this format to enable TestStand version 2016 to load the file. TestStand 16.0 is the internal
 
 version number 
 for TestStand 2016.
- WriteFileFormat_TestStand_17 
 –(Value: 16) Specifies that TestStand writes out the file using the TestStand 2017 file format. Save the file in this format to enable TestStand version 2017 to load the file. TestStand 17.0 is the internal
 
 version number 
 for TestStand 2017.
- WriteFileFormat_TestStand_19 
 –(Value: 17) Specifies that TestStand writes out the file using the TestStand 2019 file format. Save the file in this format to enable TestStand version 2019 to load the file. TestStand 19.0 is the internal
 
 version number 
 for TestStand 2019.
- WriteFileFormat_TestStand_20 
 –(Value: 18) Specifies that TestStand writes out the file using the TestStand 2020 file format. Save the file in this format to enable TestStand version 2020 to load the file. TestStand 20.0 is the internal
 
 version number 
 for TestStand 2020.
- WriteFileFormat_TestStand_21 
 –(Value: 19) Specifies that TestStand writes out the file using the TestStand 2021 file format. Save the file in this format to enable TestStand version 2021 to load the file. TestStand 21.0 is the internal
 
 version number 
 for TestStand 2021.
- WriteFileFormat_TestStand_22 
 –(Value: 20) Specifies that TestStand writes out the file using the TestStand 2022 file format. Save the file in this format to enable TestStand version 2022 to load the file. TestStand 22.0 is the internal
 
 version number 
 for TestStand 2022.
- WriteFileFormat_TestStand_23 
 –(Value: 21) Specifies that TestStand writes out the file using the TestStand 2023 file format. Save the file in this format to enable TestStand version 2023 to load the file. TestStand 23.0 is the internal
 
 version number 
 for TestStand 2023.
- WriteFileFormat_TestStand4 
 –(Value: 8) Specifies that TestStand writes out the file using the TestStand 4.0 file format. Save the file in this format to enable TestStand version 4.0 to load the file.
- WriteFileFormat_TestStand41 
 –(Value: 9) Specifies that TestStand writes out the file using the TestStand 4.1 file format. Save the file in this format to enable TestStand version 4.1 to load the file.
- WriteFileFormat_TestStand42 
 –(Value: 10) Specifies that TestStand writes out the file using the TestStand 4.2 file format. Save the file in this format to enable TestStand version 4.2 to load the file.
- WriteFileFormat_TestStand45 
 –(Value: 11) Specifies that TestStand writes out the file using the TestStand 2010 file format. Save the file in this format to enable TestStand version 2010 to load the file. TestStand 4.5 is the internal
 
 version number 
 for TestStand 2010.
- WriteFileFormat_TestStand50 
 –(Value: 12) Specifies that TestStand writes out the file using the TestStand 2012 file format. Save the file in this format to enable TestStand version 2012 to load the file. TestStand 5.0 is the internal
 
 version number 
 for TestStand 2012.
- WriteFileFormat_TestStand51 
 –(Value: 13) Specifies that TestStand writes out the file using the TestStand 2013 file format. Save the file in this format to enable TestStand version 2013 to load the file. TestStand 5.1 is the internal
 
 version number 
 for TestStand 2013.

#### See Also

[PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/xmloptions.html language=enus -->
## TOPIC 03108: XMLOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/xmloptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/xmloptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the GenerationOptions parameter of the PropertyObject.GetXML method. XMLOption_AllowInvalidObjects –(Value 0x1000) Pass this option to PropertyObject.GetXML to allow serialization of invalid instances of TestStand enumerator data types. Pass this option to PropertyObje

### XMLOptions

Use these constants to specify the
 GenerationOptions
 parameter of the
 [PropertyObject.GetXML](propertyobject-getxml.html)
 method.

- XMLOption_AllowInvalidObjects 
 –(Value 0x1000) Pass this option to PropertyObject.GetXML to allow serialization of invalid instances of TestStand enumerator data types. Pass this option to PropertyObject.SetXML to allow deserialization of invalid instances of TestStand enumerator data types.
- XMLOption_ExcludeAliasObjects 
 –(Value: 0x100) Instructs TestStand to exclude
 alias 
 subproperty objects in the XML stream. By default, the
 PropertyObject.GetXML 
 method includes alias subproperty objects in the XML stream.
- XMLOption_ExcludeArrayPrototypes 
 –(Value: 0x200) Excludes the default prototype definition for array element properties.
- XMLOption_ExcludeAttributes 
 –(Value: 0x400 | 0x800) Excludes
 PropertyObject 
 attributes and type attributes from the generated XML.
- XMLOption_ExcludeComments 
 –(Value: 0x1) Excludes PropertyObject comments from the generated XML.
- XMLOption_ExcludeEmptyObjects 
 –(Value: 0x8) Excludes objects without values from the generated XML.
- XMLOption_ExcludeFlags 
 –(Value: 0x2) Excludes the flag related attributes from the generated XML.
- XMLOption_ExcludeVersionInfo 
 –(Value: 0x4) Excludes version information from the header of the generated XML.
- XMLOption_NoCRLF 
 –(Value: 0x40) Instructs TestStand to not automatically format the generated XML by adding LF or CRLF characters.
- XMLOption_NoIndentation 
 –(Value: 0x20) Instructs TestStand to not automatically format the generated XML by indenting new lines with tab characters.
- XMLOption_NoOptions 
 –(Value: 0x0) No options.
- XMLOption_UseCRLFInsteadOfLF 
 –(Value: 0x80) Instructs TestStand to use CRLF characters instead of adding LF characters when automatically formatting generated XML.
- XMLOption_UseValueFormatIfDefined 
 –(Value: 0x10) Instructs TestStand to use the formatString of each numeric object when the
 formatString 
 parameter is not empty. If this flag is not set or the format string of the numeric object is empty, the
 PropertyObject.GetXML 
 method uses the
 formatString 
 parameter for the formatting, or
 "%.17g" 
 if the
 formatString 
 parameter is empty. The default for double-precision, 64-bit floating-point values is
 %.17g 
 ,
 %d 
 for signed 64-bit integer values, and
 %u 
 for unsigned 64-bit integer values.

#### See Also

[PropertyObject.GetXML](propertyobject-getxml.html)

[PropertyObject.IsAliasObject](propertyobject-isaliasobject.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19000-general-error.html language=enus -->
## TOPIC 03109: -19000: General Error

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19000-general-error.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19000-general-error.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message An error occurred while deploying the test system. Why does this error occur? The deployment could not be created successfully. How do I resolve this error? Restart the deployment utility and related application development environments and try to deploy again. If the issue persists, contact

### -19000: General Error

#### Message

An error occurred while deploying the test system.

#### Why does this error occur?

The deployment could not be created successfully.

#### How do I resolve this error?

Restart the deployment utility and related application development environments and try to deploy again.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19001-file-not-found.html language=enus -->
## TOPIC 03110: -19001: File Not Found

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19001-file-not-found.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19001-file-not-found.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following files were not located: Why does this error occur? The files specified in the error message were not located or cannot be read. This message can occur in the following cases: For top-level VIs that cannot be located using the path specified in a sequence file or workspace file

### -19001: File Not Found

#### Message

The following files were not located:

#### Why does this error occur?

The files specified in the error message were not located or cannot be read. This message can occur in the following cases:

- For top-level VIs that cannot be located using the path specified in a sequence file or workspace file
- For LabVIEW dependencies that cannot be located in their callers, for example, because the fully qualified name does not match the expected name or because the libraries to which they belong do not mark them as members
- One or more code modules specified in the sequence are configured using a path relative to the workspace file.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Navigate to the directories listed in the message and verify the file exists. If required, copy the missing files to the directories specified.
- If the file exists, change the file permissions so the user running the deployment utility can access the file.
- If the file is a top-level file called directly from a TestStand sequence, the message details indicate which sequence file and sequence calls the code module. Open the sequence and remove the step or steps that call into the file or fix the paths.
- If the file is a dependency of a top-level VI, the message contains the list of VIs that call the file. Open one of the specified callers to remove the missing dependency or update the path to the dependency.
 Note: 
 The Run arrow for the VIs might not appear broken because the missing dependency is located in a diagram disable structure. You must remove the call to the missing VI from the diagram disable structure or remove the disabled case.
- After you have fixed the specified VIs, mass compile the source or run the TestStand Sequence Analyzer to verify that the deployment does not have any other broken VIs.
- If the steps are configured using a path relative to the workspace file:
  1. In the sequence editor, open the search directories dialog box.
  2. Explicitly add the directory where the workspace file is located to the search directories.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19002-file-version-not-updated-in-patch-deplo.html language=enus -->
## TOPIC 03111: -19002: File Version not Updated in Patch Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19002-file-version-not-updated-in-patch-deplo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19002-file-version-not-updated-in-patch-deplo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following files in the patch installer will not replace the files the previous full deployment or patch deployment installer installed because the version number of the file is not greater than the version number of the file included in the full deployment or previous patch deployment: W

### -19002: File Version not Updated in Patch Deployment

#### Message

The following files in the patch installer will not replace the files the previous full deployment or patch deployment installer installed because the version number of the file is not greater than the version number of the file included in the full deployment or previous patch deployment:

#### Why does this error occur?

One or more versioned files in the patch deployment have been modified since the full deployment or previous patch deployment, but the version numbers have not changed.

#### How do I resolve this error?

Update the version numbers and rebuild the files. Refer to the help in the development environment used to create the versioned files for more information about how to set the version of the files.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19004-module-not-specified.html language=enus -->
## TOPIC 03112: -19004: Module Not Specified

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19004-module-not-specified.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19004-module-not-specified.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The code module for the following steps was not specified: Why does this error occur? The code module for the step listed in the error message was not specified. You must specify a code module for the step to execute successfully. How do I resolve this error? Use the TestStand Sequence Edito

### -19004: Module Not Specified

#### Message

The code module for the following steps was not specified:

#### Why does this error occur?

The code module for the step listed in the error message was not specified. You must specify a code module for the step to execute successfully.

#### How do I resolve this error?

Use the TestStand Sequence Editor to edit the sequence files and verify that the steps listed in the error message are correctly configured.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19006-broken-vis.html language=enus -->
## TOPIC 03113: -19006: Broken VIs

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19006-broken-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19006-broken-vis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following VIs are broken: Why does this error occur? One or more VIs included in the deployment are not executable. How do I resolve this error? Use the following suggestions to resolve the issue. Open the specified VIs in the active version of the LabVIEW development environment, launch

### -19006: Broken VIs

#### Message

The following VIs are broken:

#### Why does this error occur?

One or more VIs included in the deployment are not executable.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Open the specified VIs in the active version of the LabVIEW development environment, launch the Errors List dialog box, and resolve all the issues listed.
- In some cases, you might have to deploy VIs that are broken, such as when you use the VIs listed as template VIs for scripting. In the LabVIEW VI Options dialog box, which you launch from the Distributed Files tab, disable the Check for Broken VIs option.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19007-vis-cannot-be-loaded.html language=enus -->
## TOPIC 03114: -19007: VIs Cannot Be Loaded

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19007-vis-cannot-be-loaded.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19007-vis-cannot-be-loaded.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Active version of the LabVIEW development system could not load the following VIs: Why does this error occur? The specified VIs could not be loaded in the active version of the LabVIEW development system, which can happen because the VIs are saved in a version of LabVIEW that is different fr

### -19007: VIs Cannot Be Loaded

#### Message

Active version of the LabVIEW development system could not load the following VIs:

#### Why does this error occur?

The specified VIs could not be loaded in the active version of the LabVIEW development system, which can happen because the VIs are saved in a version of LabVIEW that is different from the active version of the LabVIEW development system or if the VIs are corrupted.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Open and save the specified VIs in the active version of the LabVIEW development system.
- Contact National Instruments for support if the VIs cannot be opened in the active version of the LabVIEW development system.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19009-paths-not-updated.html language=enus -->
## TOPIC 03115: -19009: Paths not Updated

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19009-paths-not-updated.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19009-paths-not-updated.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following paths cannot be updated with the relative paths to the files included in the deployment: Why does this error occur? After the deployment utility finishes copying the test system files to the image directory, it opens the deployed sequence files and updates any relative paths th

### -19009: Paths not Updated

#### Message

The following paths cannot be updated with the relative paths to the files included in the deployment:

#### Why does this error occur?

After the deployment utility finishes copying the test system files to the image directory, it opens the deployed sequence files and updates any relative paths that were changed to call deployed code modules correctly. The deployment utility could not update the paths for the steps the message specifies.

#### How do I resolve this error?

On the Distributed Files tab, ensure that the relative paths between the sequence and its required files are not changed.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19010-deployment-requires-labview-development.html language=enus -->
## TOPIC 03116: -19010: Deployment Requires LabVIEW Development System

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19010-deployment-requires-labview-development.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19010-deployment-requires-labview-development.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Deploying LabVIEW files requires the LabVIEW development system. Why does this error occur? To guarantee that the VIs included in the deployment are not broken, the deployment utility compiles the VIs and all their static dependencies using the LabVIEW development system. How do I resolve th

### -19010: Deployment Requires LabVIEW Development System

#### Message

Deploying LabVIEW files requires the LabVIEW development system.

#### Why does this error occur?

To guarantee that the VIs included in the deployment are not broken, the deployment utility compiles the VIs and all their static dependencies using the LabVIEW development system.

#### How do I resolve this error?

Ensure that the LabVIEW development system is installed and has been licensed. Also ensure that LabVIEW has been launched at least once to register the ActiveX server. If you do not want to recompile the VIs, enable the Include without Processing Item or Dependencies option for all the included LabVIEW files.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19011-deployment-contains-no-files-or-compone.html language=enus -->
## TOPIC 03117: -19011: Deployment Contains No Files or Components

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19011-deployment-contains-no-files-or-compone.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19011-deployment-contains-no-files-or-compone.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The deployment contains no files or components. Why does this error occur? The deployment does not contain any files or components. How do I resolve this error? Add files or components to the deployment. If the issue persists, contact National Instruments for support. Save a technical suppor

### -19011: Deployment Contains No Files or Components

#### Message

The deployment contains no files or components.

#### Why does this error occur?

The deployment does not contain any files or components.

#### How do I resolve this error?

Add files or components to the deployment.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19013-destination-directories-with-lvlibp-ext.html language=enus -->
## TOPIC 03118: -19013: Destination Directories With LVLIBP Extension

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19013-destination-directories-with-lvlibp-ext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19013-destination-directories-with-lvlibp-ext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The destination path for the following files in the deployment includes the extension ".lvlibp". A directory with the extension ".lvlibp" cannot be created inside a packed project library. Why does this error occur? The destination for the files specified in the error message includes direct

### -19013: Destination Directories With LVLIBP Extension

#### Message

The destination path for the following files in the deployment includes the extension ".lvlibp". A directory with the extension ".lvlibp" cannot be created inside a packed project library.

#### Why does this error occur?

The destination for the files specified in the error message includes directories with the ".lvlibp" file extension, and the distribution is creating a packed project library.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- On the Distributed Files tab, select the Build Preview view and remove the extension ".lvlibp" from the nodes in the destination specified in the message.
- On the Distributed Files tab, click the LabVIEW Options button to launch the LabVIEW VI Options dialog box, in which you can disable the Output VIs to Packed Project Library option.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19014-empty-path-specified-for-teststand-depl.html language=enus -->
## TOPIC 03119: -19014: Empty Path Specified for TestStand Deployment Utility Option

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19014-empty-path-specified-for-teststand-depl.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19014-empty-path-specified-for-teststand-depl.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following empty paths are invalid: Why does this error occur? One or more TestStand Deployment Utility options have not been specified. How do I resolve this error? Update the path specified for the deployment utility option. The error message specifies which path to update: Update the D

### -19014: Empty Path Specified for TestStand Deployment Utility Option

#### Message

The following empty paths are invalid:

#### Why does this error occur?

One or more TestStand Deployment Utility options have not been specified.

#### How do I resolve this error?

Update the path specified for the deployment utility option. The error message specifies which path to update:

- Update the Default Installer Directory option on the Installer Options tab.
- Update the Create Program Item option on the Distributed Files tab.
- Update the Shortcuts options in the Shortcuts dialog box, which you can launch from the Distributed Files tab.
- Update the SubVI Location option in the LabVIEW VI Options dialog box, which you can launch from the Distributed Files tab.
- Update the Default Installation Subdirectory option on the Installer Options tab.
- Update the Start Menu Item Group option on the Installer Options tab.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19015-invalid-characters-in-path.html language=enus -->
## TOPIC 03120: -19015: Invalid Characters In Path

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19015-invalid-characters-in-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19015-invalid-characters-in-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following paths are invalid because they contain one or more characters not allowed in filenames: Why does this error occur? The paths specified contain one or more invalid characters. A filename cannot contain any of the following characters: \, /, :, *, ?, ", <, >, or |. How do I resol

### -19015: Invalid Characters In Path

#### Message

The following paths are invalid because they contain one or more characters not allowed in filenames:

#### Why does this error occur?

The paths specified contain one or more invalid characters. A filename cannot contain any of the following characters: \, /, :, *, ?, ", <, >, or |.

#### How do I resolve this error?

The error message specifies which path to update:

- Update the Default Installer Directory option on the Installer Options tab.
- Update the Create Program Item option on the Distributed Files tab.
- Update the Shortcuts options in the Shortcuts dialog box, which you can launch from the Distributed Files tab.
- Update the SubVI Location option in the LabVIEW VI Options dialog box, which you can launch from the Distributed Files tab.
- Update the Default Installation Subdirectory option on the Installer Options tab.
- Update the Start Menu Item Group option on the Installer Options tab.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19020-invalid-directory.html language=enus -->
## TOPIC 03121: -19020: Invalid Directory

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19020-invalid-directory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19020-invalid-directory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Cannot read from or write to the following directories: Why does this error occur? The deployment utility does not have the required permissions to read or write files to the specified directory, the path specified is longer than 260 characters, or the specified path is invalid, for example,

### -19020: Invalid Directory

#### Message

Cannot read from or write to the following directories:

#### Why does this error occur?

The deployment utility does not have the required permissions to read or write files to the specified directory, the path specified is longer than 260 characters, or the specified path is invalid, for example, the path includes an unmapped drive.

#### How do I resolve this error?

Open the specified directory in Microsoft Windows Explorer and ensure that the user has read and write permissions for the directory. If the path is to a network drive, ensure that the drive is correctly mapped and the user has the correct permissions to access the drive.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19021-cannot-open-specified-teststand-workspa.html language=enus -->
## TOPIC 03122: -19021: Cannot Open Specified TestStand Workspace File

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19021-cannot-open-specified-teststand-workspa.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19021-cannot-open-specified-teststand-workspa.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Cannot locate the specified file in the TestStand workspace. Why does this error occur? The specified workspace file is not valid. The file might be corrupted. How do I resolve this error? Attempt opening the workspace file in the sequence editor and saving it. If the issue persists, contact

### -19021: Cannot Open Specified TestStand Workspace File

#### Message

Cannot locate the specified file in the TestStand workspace.

#### Why does this error occur?

The specified workspace file is not valid. The file might be corrupted.

#### How do I resolve this error?

Attempt opening the workspace file in the sequence editor and saving it.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19022-cannot-process-file-associated-with-tes.html language=enus -->
## TOPIC 03123: -19022: Cannot Process File Associated with TestStand Workspace File

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19022-cannot-process-file-associated-with-tes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19022-cannot-process-file-associated-with-tes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The specified workspace file could not be opened. The display names of the affected objects are: Why does this error occur? The workspace refers to one or more missing files. These files might have been deleted, you might need to update the TestStand search directories, or the workspace migh

### -19022: Cannot Process File Associated with TestStand Workspace File

#### Message

The specified workspace file could not be opened.
The display names of the affected objects are:

#### Why does this error occur?

The workspace refers to one or more missing files. These files might have been deleted, you might need to update the TestStand search directories, or the workspace might be corrupted.

#### How do I resolve this error?

Open the workspace file in the TestStand Sequence Editor and resolve references to the specified files.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19024-projects-open-in-labview-development-sy.html language=enus -->
## TOPIC 03124: -19024: Projects Open in LabVIEW Development System

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19024-projects-open-in-labview-development-sy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19024-projects-open-in-labview-development-sy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following projects are open in the LabVIEW development system. Close all projects before creating a deployment. Why does this error occur? One or more of the projects are open in the active version of the LabVIEW development system while creating the deployment. As part of the deployment

### -19024: Projects Open in LabVIEW Development System

#### Message

The following projects are open in the LabVIEW development system. Close all projects before creating a deployment.

#### Why does this error occur?

One or more of the projects are open in the active version of the LabVIEW development system while creating the deployment. As part of the deployment creation process, the deployment utility creates copies of these projects. To prevent cross-linking, the deployment cannot be generated while the projects are open in LabVIEW.

#### How do I resolve this error?

Close all projects in LV before creating a deployment. If the error persists, restart the LabVIEW development system.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19025-packed-project-libraries-open-in-labvie.html language=enus -->
## TOPIC 03125: -19025: Packed Project Libraries Open in LabVIEW Development System

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19025-packed-project-libraries-open-in-labvie.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19025-packed-project-libraries-open-in-labvie.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following packed project libraries are open in the active LabVIEW development system. Close and restart the LabVIEW development system to unload all files. Why does this error occur? One or more packed project libraries are open in the active version of the LabVIEW development system whi

### -19025: Packed Project Libraries Open in LabVIEW Development System

#### Message

The following packed project libraries are open in the active LabVIEW development system. Close and restart the LabVIEW development system to unload all files.

#### Why does this error occur?

One or more packed project libraries are open in the active version of the LabVIEW development system while creating the deployment, which can lead to cross-linking.

#### How do I resolve this error?

Restart the LabVIEW development system.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19026-invalid-project.html language=enus -->
## TOPIC 03126: -19026: Invalid Project

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19026-invalid-project.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19026-invalid-project.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Could not locate VIs the following projects reference: Why does this error occur? The deployment utility could not obtain the list of VIs the specified project references, which might happen because the active version of the LabVIEW development system cannot open the project file. How do I r

### -19026: Invalid Project

#### Message

Could not locate VIs the following projects reference:

#### Why does this error occur?

The deployment utility could not obtain the list of VIs the specified project references, which might happen because the active version of the LabVIEW development system cannot open the project file.

#### How do I resolve this error?

Attempt to open the project in LabVIEW and save it again.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19027-error-generated-by-teststand-engine-whe.html language=enus -->
## TOPIC 03127: -19027: Error Generated by TestStand Engine when Creating Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19027-error-generated-by-teststand-engine-whe.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19027-error-generated-by-teststand-engine-whe.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The TestStand Engine reported the following errors: Why does this error occur? The TestStand Engine reported an error during deployment. How do I resolve this error? Refer to the error message for specific instructions. If the issue persists, contact National Instruments for support. Save a

### -19027: Error Generated by TestStand Engine when Creating Deployment

#### Message

The TestStand Engine reported the following errors:

#### Why does this error occur?

The TestStand Engine reported an error during deployment.

#### How do I resolve this error?

Refer to the error message for specific instructions.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19028-error-occurred-when-accessing-teststand.html language=enus -->
## TOPIC 03128: -19028: Error Occurred when Accessing TestStand Registry Keys

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19028-error-occurred-when-accessing-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19028-error-occurred-when-accessing-teststand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Cannot read the National Instruments directory from the registry. Why does this error occur? One or more software products installed by National Instruments are corrupted. How do I resolve this error? Repair the installation of National Instruments software. If the issue persists, contact Na

### -19028: Error Occurred when Accessing TestStand Registry Keys

#### Message

Cannot read the National Instruments directory from the registry.

#### Why does this error occur?

One or more software products installed by National Instruments are corrupted.

#### How do I resolve this error?

Repair the installation of National Instruments software.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19029-patch-deployment-files-incorrectly-conf.html language=enus -->
## TOPIC 03129: -19029: Patch Deployment Files Incorrectly Configured to Install at Higher Level than Full Deployment Installation Directory

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19029-patch-deployment-files-incorrectly-conf.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19029-patch-deployment-files-incorrectly-conf.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following files in the patch deployment are configured to install in a directory higher than the installation directory of the full deployment installer: Why does this error occur? A full deployment installer installs all the files in a specified installation directory, for example, C:\P

### -19029: Patch Deployment Files Incorrectly Configured to Install at Higher Level than Full Deployment Installation Directory

#### Message

The following files in the patch deployment are configured to install in a directory higher than the installation directory of the full deployment installer:

#### Why does this error occur?

A full deployment installer installs all the files in a specified installation directory, for example,
 C:\Program Files\My System
 . Patch installers cannot install files at a higher level than this directory because doing so might break other applications installed on the computer. To avoid this behavior, the deployment utility prevents you from creating a patch deployment installer that installs files at a higher level than the current installation directory for the full deployment.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Create a full deployment instead of a patch deployment.
- If creating a full deployment is not possible, use the Distributed Files tab to move the destinations of all the specified files to a directory other than the installation directory.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19030-replacement-file-and-added-file-going-t.html language=enus -->
## TOPIC 03130: -19030: Replacement File and Added File Going to the Same Destination

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19030-replacement-file-and-added-file-going-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19030-replacement-file-and-added-file-going-t.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following destinations in the patch deployment are the same for an added file and a replacement file: Why does this error occur? The deployment contains a replacement file and an added file configured to install in the same destination. Because both files were manually added to the deplo

### -19030: Replacement File and Added File Going to the Same Destination

#### Message

The following destinations in the patch deployment are the same for an added file and a replacement file:

#### Why does this error occur?

The deployment contains a replacement file and an added file configured to install in the same destination. Because both files were manually added to the deployment, the deployment utility cannot determine which file to include in the patch deployment image.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Remove the file that was added manually.
- Change the destination of the replacement file so that it does not conflict with the file added manually.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19031-inconsistent-capitalization-in-sequence.html language=enus -->
## TOPIC 03131: -19031: Inconsistent Capitalization in Sequence Files

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19031-inconsistent-capitalization-in-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19031-inconsistent-capitalization-in-sequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Sequence files are referencing code modules at the following paths with inconsistent capitalization. Use the TestStand Sequence Editor to edit the sequence files and make the case consistent. Why does this error occur? One or more steps refer to code modules with the same path but with incon

### -19031: Inconsistent Capitalization in Sequence Files

#### Message

Sequence files are referencing code modules at the following paths with inconsistent capitalization. Use the TestStand Sequence Editor to edit the sequence files and make the case consistent.

#### Why does this error occur?

One or more steps refer to code modules with the same path but with inconsistent capitalization. This configuration can lead to undefined behavior.

#### How do I resolve this error?

Open the sequence files in the TestStand Sequence Editor and use the Find and Replace tool to replace all the instances of the path with the same capitalization.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19033-cannot-load-distribution-vis.html language=enus -->
## TOPIC 03132: -19033: Cannot Load Distribution VIs

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19033-cannot-load-distribution-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19033-cannot-load-distribution-vis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The TestStand Deployment Utility encountered a problem while loading the following files in the TestStand Components\Tools\Deployment Utility\TestStand - Build VI Distribution directory: Why does this error occur? The TestStand palette was not found in the active version of LabVIEW The TestS

### -19033: Cannot Load Distribution VIs

#### Message

The TestStand Deployment Utility encountered a problem while loading the following files in the TestStand Components\Tools\Deployment Utility\TestStand - Build VI Distribution directory:

#### Why does this error occur?

- The TestStand palette was not found in the active version of LabVIEW
- The TestStand installation has been corrupted.

#### How do I resolve this error?

- Run the sequence editor to create the TestStand palette
- Repair the TestStand installation to recreate the deployment utility components to resolve the issue.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19034-cannot-call-distribution-vis.html language=enus -->
## TOPIC 03133: -19034: Cannot Call Distribution VIs

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19034-cannot-call-distribution-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19034-cannot-call-distribution-vis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The TestStand Deployment Utility encountered a problem while executing the following file in the TestStand Components\Tools\Deployment Utility\TestStand - Build VI Distribution directory: Why does this error occur? The TestStand installation has been corrupted. How do I resolve this error? R

### -19034: Cannot Call Distribution VIs

#### Message

The TestStand Deployment Utility encountered a problem while executing the following file in the TestStand Components\Tools\Deployment Utility\TestStand - Build VI Distribution directory:

#### Why does this error occur?

The TestStand installation has been corrupted.

#### How do I resolve this error?

Repair the TestStand installation to resolve the issue and to recreate the deployment utility components.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19035-duplicate-files-included-in-deployment.html language=enus -->
## TOPIC 03134: -19035: Duplicate Files Included in Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19035-duplicate-files-included-in-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19035-duplicate-files-included-in-deployment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following VIs or project libraries have duplicate names. You must change the duplicate VI names or add the VIs to project libraries. Why does this error occur? One or more files deployed to the same base destination have duplicate qualified names. The active version of the LabVIEW develo

### -19035: Duplicate Files Included in Deployment

#### Message

The following VIs or project libraries have duplicate names.
You must change the duplicate VI names or add the VIs to project libraries.

#### Why does this error occur?

One or more files deployed to the same base destination have duplicate qualified names. The active version of the LabVIEW development system uses qualified names to uniquely identify VIs. Having duplicate qualified names can lead to cross-linking and can break a test system or lead to inconsistent results.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Add the files with duplicate names to a LabVIEW project library.
- Rename the files with duplicate names and use the LabVIEW rename option to update the callers automatically.
- Configure the steps in the sequence to be called in the context of different LabVIEW projects.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19036-cannot-load-sequence-file.html language=enus -->
## TOPIC 03135: -19036: Cannot Load Sequence File

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19036-cannot-load-sequence-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19036-cannot-load-sequence-file.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following sequence files cannot be opened: Why does this error occur? The specified sequence file could not be loaded for the TestStand Engine to process. How do I resolve this error? Open the sequence file in the TestStand Sequence Editor, resolve any errors, and save the sequence file.

### -19036: Cannot Load Sequence File

#### Message

The following sequence files cannot be opened:

#### Why does this error occur?

The specified sequence file could not be loaded for the TestStand Engine to process.

#### How do I resolve this error?

Open the sequence file in the TestStand Sequence Editor, resolve any errors, and save the sequence file.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19037-packed-library-cannot-set-relative-path.html language=enus -->
## TOPIC 03136: -19037: Packed Library Cannot Set Relative Path To Dependencies

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19037-packed-library-cannot-set-relative-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19037-packed-library-cannot-set-relative-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following packed project libraries contain dependencies that are not within the image directory or its subdirectories: Why does this error occur? The deployment contains packed project libraries that have external dependencies with a destination higher than the packed project library. Th

### -19037: Packed Library Cannot Set Relative Path To Dependencies

#### Message

The following packed project libraries contain dependencies that are not within the image directory or its subdirectories:

#### Why does this error occur?

The deployment contains packed project libraries that have external dependencies with a destination higher than the packed project library. The relative path from the packed project library to the external dependencies would install the dependencies in a directory higher than the installation directory.

For example, if you deploy
 C:\source\a.lvlibp
 , which has a dependency on
 C:\dep.dll
 , a.lvlibp installs in the following destination:
 <image>\a.lvlibp
 , and dep.dll must install in a directory higher than the installation directory to maintain the relative path.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- On the Distributed Files tab, select the packed project library and change the destination so that the dependencies can be placed inside the installation directory.
- Alternatively, rebuild the packed project libraries and place the dependencies in a relative directory that is not higher than the directory in which the packed project library resides.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19038-labview-version-changed-in-patch.html language=enus -->
## TOPIC 03137: -19038: LabVIEW Version Changed In Patch

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19038-labview-version-changed-in-patch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19038-labview-version-changed-in-patch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message You are using a different version of the LabVIEW development system to create the patch deployment than you used to create the full deployment. Why does this error occur? The active version of the LabVIEW development system is different than the version of LabVIEW used to create the full dep

### -19038: LabVIEW Version Changed In Patch

#### Message

You are using a different version of the LabVIEW development system to create the patch deployment than you used to create the full deployment.

#### Why does this error occur?

The active version of the LabVIEW development system is different than the version of LabVIEW used to create the full deployment. This error applies only to major version changes, for example, changing from LabVIEW 2013 to LabVIEW 2014. Minor version changes, such as service pack releases and patches, do not prevent you from creating a patch deployment.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Change the active version of the LabVIEW development system to match the version of LabVIEW used in the full deployment.
- Create a full deployment.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19039-feature-not-supported-in-active-labview.html language=enus -->
## TOPIC 03138: -19039: Feature Not Supported In Active LabVIEW Version

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19039-feature-not-supported-in-active-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19039-feature-not-supported-in-active-labview.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The active version of the LabVIEW development system does not support the following features: Why does this error occur? The active version of the LabVIEW development system does not support one or more features used in the test system. How do I resolve this error? Use the following suggesti

### -19039: Feature Not Supported In Active LabVIEW Version

#### Message

The active version of the LabVIEW development system does not support the following features:

#### Why does this error occur?

The active version of the LabVIEW development system does not support one or more features used in the test system.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Close the currently active version of the LabVIEW development system and launch a version of the LabVIEW development system that supports the features specified.
- Modify the sequences to remove the features the error message specifies.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19040-cannot-delete-file.html language=enus -->
## TOPIC 03139: -19040: Cannot Delete File

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19040-cannot-delete-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19040-cannot-delete-file.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Cannot delete the following files: Why does this error occur? The specified files cannot be deleted because another process has the files locked. If you have run the sequence files from the image folder, another application, such as TestStand, might still have the files open. How do I resolv

### -19040: Cannot Delete File

#### Message

Cannot delete the following files:

#### Why does this error occur?

The specified files cannot be deleted because another process has the files locked. If you have run the sequence files from the image folder, another application, such as TestStand, might still have the files open.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- In the sequence editor, select File»Unload All Modules.
- Close all files, projects, and VIs open in the active version of the LabVIEW development system.
- Close other programs that might be using the file.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19041-cannot-copy-files.html language=enus -->
## TOPIC 03140: -19041: Cannot Copy Files

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19041-cannot-copy-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19041-cannot-copy-files.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Could not copy the following files: Why does this error occur? The specified files could not be copied to the destination. The destination might not be writable, the computer might not have sufficient disk space, or the file might exceed the maximum path length. How do I resolve this error?

### -19041: Cannot Copy Files

#### Message

Could not copy the following files:

#### Why does this error occur?

The specified files could not be copied to the destination. The destination might not be writable, the computer might not have sufficient disk space, or the file might exceed the maximum path length.

#### How do I resolve this error?

Ensure that the specified destination is writeable, that the drive has enough empty space, and that the destination path for the files do not exceed the maximum path length (260 characters, including the drive letter). Alternatively, change the destination of the file or the image or installation directory.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19042-overriding-dependency-installer.html language=enus -->
## TOPIC 03141: -19042: Overriding Dependency Installer

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19042-overriding-dependency-installer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19042-overriding-dependency-installer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The patch deployment installer is configured to overwrite the installer required to create the patch deployment. Choose another directory for the patch installer. Why does this error occur? The patch deployment installer uses the same destination as the dependency installer. The deployment u

### -19042: Overriding Dependency Installer

#### Message

The patch deployment installer is configured to overwrite the installer required to create the patch deployment. Choose another directory for the patch installer.

#### Why does this error occur?

The patch deployment installer uses the same destination as the dependency installer. The deployment utility uses the dependency installer to obtain information required to correctly create the patch installer.

#### How do I resolve this error?

On the Installer Options tab, change the installer destination to a different directory.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19043-disk-is-full.html language=enus -->
## TOPIC 03142: -19043: Disk Is Full

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19043-disk-is-full.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19043-disk-is-full.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Not enough disk space to create an installer. Why does this error occur? The specified installer directory does not have enough space to save the installer. How do I resolve this error? Use the following suggestions to resolve the issue. Move the installer directory to a different drive. Del

### -19043: Disk Is Full

#### Message

Not enough disk space to create an installer.

#### Why does this error occur?

The specified installer directory does not have enough space to save the installer.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Move the installer directory to a different drive.
- Delete files in the drive of the current installer directory to free additional space.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19044-conflicting-destinations.html language=enus -->
## TOPIC 03143: -19044: Conflicting Destinations

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19044-conflicting-destinations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19044-conflicting-destinations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following files have conflicting destinations: Why does this error occur? One or more files are configured with the same name and the same destination directory and base path. How do I resolve this error? Navigate to the specified file in Build Preview view on the Distributed Files tab a

### -19044: Conflicting Destinations

#### Message

The following files have conflicting destinations:

#### Why does this error occur?

One or more files are configured with the same name and the same destination directory and base path.

#### How do I resolve this error?

Navigate to the specified file in Build Preview view on the Distributed Files tab and change the destination or base path of all the conflicting files except one.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19045-must-install-max-4-0-or-later-to-create.html language=enus -->
## TOPIC 03144: -19045: Must Install MAX 4.0 or Later to Create Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19045-must-install-max-4-0-or-later-to-create.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19045-must-install-max-4-0-or-later-to-create.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message You must have Measurement and Automation Explorer (MAX) 4.0 or later installed to build an installer that includes a hardware configuration data file. Why does this error occur? Measurement & Automation Explorer (MAX) 4.0 or later is required to deploy an installer that includes a hardware c

### -19045: Must Install MAX 4.0 or Later to Create Deployment

#### Message

You must have Measurement and Automation Explorer (MAX) 4.0 or later installed to build an installer that includes a hardware configuration data file.

#### Why does this error occur?

Measurement & Automation Explorer (MAX) 4.0 or later is required to deploy an installer that includes a hardware configuration data file.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Install MAX 4.0 or later. For more information, visit ni.com/info and enter the code tsdu-max.
- In the Drivers and Components section on the Installer Options tab, disable the Include Hardware Configuration option.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19046-general-error-while-building-installer.html language=enus -->
## TOPIC 03145: -19046: General Error While Building Installer

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19046-general-error-while-building-installer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19046-general-error-while-building-installer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Error occurred while generating installer build. Why does this error occur? A general error occurred while building the installer. Refer to the message details for additional information about the error. How do I resolve this error? Use the following suggestions to resolve the issue. Make su

### -19046: General Error While Building Installer

#### Message

Error occurred while generating installer build.

#### Why does this error occur?

A general error occurred while building the installer. Refer to the message details for additional information about the error.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Make sure that no installers are running while creating a deployment.
- Make sure that only one instance of the deployment utility is running.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19052-problem-reading-dependencies.html language=enus -->
## TOPIC 03146: -19052: Problem Reading Dependencies

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19052-problem-reading-dependencies.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19052-problem-reading-dependencies.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message LabVIEW reported an error while determining dependency information for one or more top-level VIs. Refer to the error details below for more information. Why does this error occur? This error occurs when the deployment utility encounters an unexpected problem when attempting to obtain informa

### -19052: Problem Reading Dependencies

#### Message

LabVIEW reported an error while determining dependency information for one or more top-level VIs. Refer to the error details below for more information.

#### Why does this error occur?

This error occurs when the deployment utility encounters an unexpected problem when attempting to obtain information about the dependencies of a top-level VI. This error can occur in the following cases:

- A VI is saved in an earlier or later version of LabVIEW and cannot be opened in the active version of LabVIEW.
- The namespace of a VI is not valid, which can happen if you add or remove a VI from a library without saving the VI and the library.
- The VI does not exist on disk.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Mass compile all the VIs in the active version of LabVIEW. In the Mass Compile dialog box, ensure that the Include Warnings for Read-only VIs option is enabled. Once the mass compile completes, inspect any VIs that the mass compile warnings or errors log includes.
- Open the VIs specified by the error message in LabVIEW and make sure that they are connected to the correct library.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19053-vi-version-later-than-active-version.html language=enus -->
## TOPIC 03147: -19053: VI Version Later Than Active Version

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19053-vi-version-later-than-active-version.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19053-vi-version-later-than-active-version.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message One or more subVIs are saved in a LabVIEW version later than the active LabVIEW version. Why does this error occur? One or more of the files is saved in a version later than the active version of LabVIEW. How do I resolve this error? Use the following suggestions to resolve the issue. Use a

### -19053: VI Version Later Than Active Version

#### Message

One or more subVIs are saved in a LabVIEW version later than the active LabVIEW version.

#### Why does this error occur?

One or more of the files is saved in a version later than the active version of LabVIEW.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Use a newer version of LabVIEW to deploy the files
- Open the specified file in a newer version of LabVIEW and save the files for a previous version.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19054-packed-library-cannot-be-opened.html language=enus -->
## TOPIC 03148: -19054: Packed Library Cannot Be Opened

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19054-packed-library-cannot-be-opened.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19054-packed-library-cannot-be-opened.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message A packed library called by one of the top-level VIs is not saved in the active version of LabVIEW. Why does this error occur? One or more of your top-level files are calling into a packed library that was not saved in the active version of the LabVIEW development system. LabVIEW packed proje

### -19054: Packed Library Cannot Be Opened

#### Message

A packed library called by one of the top-level VIs is not saved in the active version of LabVIEW.

#### Why does this error occur?

One or more of your top-level files are calling into a packed library that was not saved in the active version of the LabVIEW development system. LabVIEW packed project libraries do not contain the source used to create them so they cannot be recompiled by LabVIEW during deployment.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

- Rebuild the packed library specified in the error message details.
- After you have rebuilt the specified packed project library, mass compile the source or run the TestStand Analyzer to verify that the deployment does not have any other packed project libraries not saved in the active version of the LabVIEW development system.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19055-error-rebuilding-distribution-vis.html language=enus -->
## TOPIC 03149: -19055: Error Rebuilding Distribution VIs

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19055-error-rebuilding-distribution-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19055-error-rebuilding-distribution-vis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The distribution VIs could not be rebuilt. Why does this error occur? The distribution VIs could not be rebuilt. The deployment utility automatically creates a new set of distribution VIs for every version of LabVIEW that was released after TestStand was released and mass compiles them for p

### -19055: Error Rebuilding Distribution VIs

#### Message

The distribution VIs could not be rebuilt.

#### Why does this error occur?

The distribution VIs could not be rebuilt. The deployment utility automatically creates a new set of distribution VIs for every version of LabVIEW that was released after TestStand was released and mass compiles them for performance reasons. This error could mean that the deployment utility does not have access to the <TestStand Public>\Components\Tools\Deployment Utility directory.

#### How do I resolve this error?

Ensure that the <TestStand Public>\Components\Tools\Deployment Utility is writeable and the user running the deployment utility has write access to it.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19056-incorrectly-specified-code-module.html language=enus -->
## TOPIC 03150: -19056: Incorrectly Specified Code Module

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19056-incorrectly-specified-code-module.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19056-incorrectly-specified-code-module.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The code module paths specified in the following steps are empty, invalid, or could not be found on disk. Why does this error occur? The code modules for the specified step was not found on disk or is not a valid path. How do I resolve this error? Select the specified steps in the sequence e

### -19056: Incorrectly Specified Code Module

#### Message

The code module paths specified in the following steps are empty, invalid, or could not be found on disk.

#### Why does this error occur?

The code modules for the specified step was not found on disk or is not a valid path.

#### How do I resolve this error?

Select the specified steps in the sequence editor, and update the module path to a valid file.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19057-vi-namespace-mismatch.html language=enus -->
## TOPIC 03151: -19057: VI Namespace Mismatch

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19057-vi-namespace-mismatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19057-vi-namespace-mismatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following VIs do not have the expected qualified name: Why does this error occur? This error occurs when a VI in the deployment is expected by the caller to be part of one namespace, but the VI claims to be in another. LabVIEW namespaces include project libraries, packed project librarie

### -19057: VI Namespace Mismatch

#### Message

The following VIs do not have the expected qualified name:

#### Why does this error occur?

This error occurs when a VI in the deployment is expected by the caller to be part of one namespace, but the VI claims to be in another. LabVIEW namespaces include project libraries, packed project libraries, and LabVIEW classes.When a VI is part of a LabVIEW namespace, LabVIEW qualifies the VI name with the namespace name to avoid cross-linking. A qualified name includes the filename and the qualified name of the owning namespace. For example, if you build a VI named caller.vi that includes a subVI named init.vi that library1.lvlib owns, the qualified name that LabVIEW records when you save caller.vi is library1.lvlib:init.vi. If caller.vi is expecting to find init.vi within library2.lvlib, LabVIEW will be unable to load the vi since the expected and actual qualified names do not match.

#### How do I resolve this error?

Open the specified VIs and their callers to resolve the namespace mismatch. LabVIEW may prompt you to find dependent VIs. In this case, browse to the path of the intended dependency. Be careful to choose the correct instance of the VI name, since multiple different copies of the VI may be present on the system. After all VIs are open, ensure that no VIs are broken due to namespace conflicts. You may need to open the namespace files specified in the LabVIEW error, and add or remove VIs from these namespaces as directed. Refer to the LabVIEW error help topics, accessible through the help button in the error list dialog, for specific information on resolving LabVIEW errors.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19058-additional-components-not-installed.html language=enus -->
## TOPIC 03152: -19058: Additional Components Not Installed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19058-additional-components-not-installed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19058-additional-components-not-installed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message One or more products are included in the .tsd file that are not installed on the system. You must deselect these products in the drivers and components dialog before building an installer. Why does this error occur? The build configuration file was saved on a system with different products i

### -19058: Additional Components Not Installed

#### Message

One or more products are included in the .tsd file that are not installed on the system. You must deselect these products in the drivers and components dialog before building an installer.

#### Why does this error occur?

The build configuration file was saved on a system with different products installed. One of the products you selected to include in the deployment is not installed on the current system, and therefore cannot be included in the deployment

#### How do I resolve this error?

In the Isntaller tab, click the Drivers and Components button to view the products that are no longer installed. Either deselect these products, or install the products on the system and reopen the deployment configuration file.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19058-included-products-are-not-installed-on.html language=enus -->
## TOPIC 03153: -19058: Included products are not installed on the System

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19058-included-products-are-not-installed-on.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19058-included-products-are-not-installed-on.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message One or more products are included in the .tsd file that are not installed on the system. You must deselect these products in the drivers and components dialog before building an installer. Why does this error occur? This error occurs when you build a deployment that includes products that ar

### -19058: Included products are not installed on the System

#### Message

One or more products are included in the .tsd file that are not installed on the system. You must deselect these products in the drivers and components dialog before building an installer.

#### Why does this error occur?

This error occurs when you build a deployment that includes products that are not installed on the system. This can happen if products are removed from the system after the .tsd file was last saved, or if the file was last saved on another system.

#### How do I resolve this error?

In the Installer Options tab, click the Drivers and Components button to launch the Drivers and Components dialog box. Deselect all products that are specified as not installed on the system, then rebuild the deployment.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19059-invalid-max-configuration.html language=enus -->
## TOPIC 03154: -19059: Invalid MAX Configuration

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19059-invalid-max-configuration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19059-invalid-max-configuration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The MAX Hardware Configuration File is invalid. Verify that required components are selected in the Drivers and Components Dialog. Verify that the Hardware Configuration File setting in the Drivers and Components dialog specifies a valid configuration file path. Why does this error occur? Th

### -19059: Invalid MAX Configuration

#### Message

The MAX Hardware Configuration File is invalid. Verify that required components are selected in the Drivers and Components Dialog. Verify that the Hardware Configuration File setting in the Drivers and Components dialog specifies a valid configuration file path.

#### Why does this error occur?

The selected MAX configuration file, specified in the Drivers and Components dialog on the Installer Options tab, is invalid.

#### How do I resolve this error?

Open the MAX configuration file in MAX to get additional information on why the file is not valid.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19060-failed-to-create-packed-project-library.html language=enus -->
## TOPIC 03155: -19060: Failed to Create Packed Project Library

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19060-failed-to-create-packed-project-library.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19060-failed-to-create-packed-project-library.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The deployment utility was unable to find the code module for the specified step within the Packed Project Library created in the deployment. Why does this error occur? After building a packed project library for the deployment, the deployment utility was unable to find a code modulle within

### -19060: Failed to Create Packed Project Library

#### Message

The deployment utility was unable to find the code module for the specified step within the Packed Project Library created in the deployment.

#### Why does this error occur?

After building a packed project library for the deployment, the deployment utility was unable to find a code modulle within the packed project library.

#### How do I resolve this error?

Open the VI referenced by the TestStand step and ensure that it is not broken. Ensure that the VI does nto contain diagram disable structures which contain invalid or broken VIs, since the LabVIEW build process attempts to find all subVIs, even if they are disabled in the VI.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19062-package-distribution-failed.html language=enus -->
## TOPIC 03156: -19062: Package Distribution Failed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19062-package-distribution-failed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19062-package-distribution-failed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message An Error occurred while building the package distribution Why does this error occur? The package distribution failed to build. How do I resolve this error? Refer to the deployment log for additional messages with further details. The source files for the package distribution can be viewed in

### -19062: Package Distribution Failed

#### Message

An Error occurred while building the package distribution

#### Why does this error occur?

The package distribution failed to build.

#### How do I resolve this error?

Refer to the deployment log for additional messages with further details. The source files for the package distribution can be viewed in the current user temp directory in the subdirectory "tspkg", which may provide additional insight into the cause of the error.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19063-failed-to-build-gll.html language=enus -->
## TOPIC 03157: -19063: Failed to Build GLL

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19063-failed-to-build-gll.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19063-failed-to-build-gll.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message An Error occured while rebuilding the specified GLL Why does this error occur? An error occurred while building a GLL from the LabVIEW NXG source files specified for one or more LabVIEW NXG code modules. This can occur if a VI in the component is broken or if the target GLL is read-only or w

### -19063: Failed to Build GLL

#### Message

An Error occured while rebuilding the specified GLL

#### Why does this error occur?

An error occurred while building a GLL from the LabVIEW NXG source files specified for one or more LabVIEW NXG code modules. This can occur if a VI in the component is broken or if the target GLL is read-only or write-protected.

#### How do I resolve this error?

Refer to the deployment log for additional messages with further details. For more information, try opening the LabVIEW NXG project file in the LabVIEW NXG environment, selecting the component file (.gcomp), and selecting the build GLL option.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19064-ni-package-manager-is-not-installed.html language=enus -->
## TOPIC 03158: -19064: NI Package Manager Is Not Installed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19064-ni-package-manager-is-not-installed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19064-ni-package-manager-is-not-installed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message To create package-based deployments, NI Package Manager and Package Deployment Support must be installed on the system. Why does this error occur? You attempted to create a package-based deployment, but NI package manager is not present on the system. How do I resolve this error? Refer to th

### -19064: NI Package Manager Is Not Installed

#### Message

To create package-based deployments, NI Package Manager and Package Deployment Support must be installed on the system.

#### Why does this error occur?

You attempted to create a package-based deployment, but NI package manager is not present on the system.

#### How do I resolve this error?

Refer to the message details for instructions to install NI Package Manager on the system.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19065-labview-nxg-not-installed.html language=enus -->
## TOPIC 03159: -19065: LabVIEW NXG Not Installed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19065-labview-nxg-not-installed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19065-labview-nxg-not-installed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message To deploy LabVIEW NXG code modules, you must have the LabVIEW NXG development system installed. The following steps reference LabVIEW NXG code modules. Why does this error occur? You attempted to deploy files which call LabVIEW NXG code modules, but LabVIEW NXG is not present on the system.

### -19065: LabVIEW NXG Not Installed

#### Message

To deploy LabVIEW NXG code modules, you must have the LabVIEW NXG development system installed. The following steps reference LabVIEW NXG code modules.

#### Why does this error occur?

You attempted to deploy files which call LabVIEW NXG code modules, but LabVIEW NXG is not present on the system.

#### How do I resolve this error?

Install LabVIEW NXG from NI package manager or from ni.com.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19200-general-warning.html language=enus -->
## TOPIC 03160: 19200: General Warning

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19200-general-warning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19200-general-warning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message A warning occurred while deploying the test system. Why does this warning occur? A warning occurred while deploying the test system. How do I resolve this warning? Contact National Instruments for support. If the issue persists, contact National Instruments for support. Save a technical supp

### 19200: General Warning

#### Message

A warning occurred while deploying the test system.

#### Why does this warning occur?

A warning occurred while deploying the test system.

#### How do I resolve this warning?

Contact National Instruments for support.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19201-version-not-updated-in-patch-warning.html language=enus -->
## TOPIC 03161: 19201: Version Not Updated In Patch (Warning)

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19201-version-not-updated-in-patch-warning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19201-version-not-updated-in-patch-warning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The file version of the following files included in the patch deployment is not greater than the file version of the file included in the full deployment: Why does this warning occur? One or more of the versioned files included in the patch deployment use the same version as the dependent in

### 19201: Version Not Updated In Patch (Warning)

#### Message

The file version of the following files included in the patch deployment is not greater than the file version of the file included in the full deployment:

#### Why does this warning occur?

One or more of the versioned files included in the patch deployment use the same version as the dependent installer. Installers created with the deployment utility use the file version to determine if files have to be installed in the test system. Not incrementing the file versions when modifying the files could lead to a broken system.

#### How do I resolve this warning?

In the active version of the LabVIEW development system, use the build specifications properties page to increment the file versions. In LabWindows/CVI use the Version Info option in the Target Settings dialog box to increment the file versions. In Visual Studio, use the Project Properties tab to increment the file versions.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19202-code-module-paths-not-updated-warning.html language=enus -->
## TOPIC 03162: 19202: Code Module Paths not Updated (Warning)

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19202-code-module-paths-not-updated-warning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19202-code-module-paths-not-updated-warning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following paths cannot be updated with the relative paths to the files included in the deployment: Why does this warning occur? After the deployment utility completes copying the test system files to the image directory, it opens the deployed sequence files and updates any relative paths

### 19202: Code Module Paths not Updated (Warning)

#### Message

The following paths cannot be updated with the relative paths to the files included in the deployment:

#### Why does this warning occur?

After the deployment utility completes copying the test system files to the image directory, it opens the deployed sequence files and updates any relative paths that were changed so that the deployed code modules can be correctly called. The deployment utility could not update the paths specified in the message. This could happen if the deployment contains files that are deployed to different base destinations.

#### How do I resolve this warning?

On the Distributed Files tab, ensure that the relative paths between the sequence file and code modules the sequence file references are not changed.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19203-absolute-path-in-step-type.html language=enus -->
## TOPIC 03163: 19203: Absolute Path in Step Type

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19203-absolute-path-in-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19203-absolute-path-in-step-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following substeps are configured to call a code module using an absolute path: Why does this warning occur? You deployed a step type that contains a substep that is configured to call a code module using an absolute path. The absolute path, which might not be valid if the deployment is

### 19203: Absolute Path in Step Type

#### Message

The following substeps are configured to call a code module using an absolute path:

#### Why does this warning occur?

You deployed a step type that contains a substep that is configured to call a code module using an absolute path. The absolute path, which might not be valid if the deployment is installed into a non-default directory.

#### How do I resolve this warning?

Use the TestStand Sequence Editor to edit the substep of the step type to use a relative path to the code module.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19204-deployment-contains-file-configured-to.html language=enus -->
## TOPIC 03164: 19204: Deployment Contains File Configured to Install in Standard National Instruments Directory

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19204-deployment-contains-file-configured-to.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19204-deployment-contains-file-configured-to.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The destinations of the following files are configured to install in a standard National Instruments directory, which might conflict with National Instruments products: Why does this warning occur? A file in the deployment is installed in a National Instruments directory. The files might ove

### 19204: Deployment Contains File Configured to Install in Standard National Instruments Directory

#### Message

The destinations of the following files are configured to install in a standard National Instruments directory, which might conflict with National Instruments products:

#### Why does this warning occur?

A file in the deployment is installed in a National Instruments directory. The files might overwrite files that are required for the correct function of National Instruments products. The files also might be loaded instead of the National Instruments components. If the file does not conflict with a National Instruments file, you can safely ignore this message.

#### How do I resolve this warning?

Use the following suggestions to resolve the issue.

- Change the destination of the specified files so that the files are not configured to be installed in a standard National Instruments directory.
- You can ignore this warning if you have verified that the file should install in a National Instruments directory and that the file does not accidentally overwrite a National Instruments file. You must validate this situation for every product you update or patch in the National Instruments directory and for every version of the test system.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19205-dependencies-not-included.html language=enus -->
## TOPIC 03165: 19205: Dependencies Not Included

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19205-dependencies-not-included.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19205-dependencies-not-included.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following dependencies were detected, but they will not be included in the deployment. You must determine whether to include these files on the Distributed Files tab. Why does this warning occur? The deployment utility detected a DLL used in the deployment but will not include the file i

### 19205: Dependencies Not Included

#### Message

The following dependencies were detected, but they will not be included in the deployment. You must determine whether to include these files on the Distributed Files tab.

#### Why does this warning occur?

The deployment utility detected a DLL used in the deployment but will not include the file in the deployment automatically because the file is an operating system DLL or because the file is part of a National Instruments product. Do not include copies of these types of files in a deployment. Instead, run the operating system or National Instruments installers to install the correct versions of these file for the test system.

#### How do I resolve this warning?

Determine whether you need to include the dependency in the deployment. For example, you do not need to include DLLs from the operating system or those installed by third-party installers. You must include utility DLLs that code modules call into.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19206-top-level-and-subvi-in-different-destin.html language=enus -->
## TOPIC 03166: 19206: Top-Level and SubVI In Different Destinations

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19206-top-level-and-subvi-in-different-destin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19206-top-level-and-subvi-in-different-destin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The deployment includes sequence files that reference the following code module VIs as top-level VIs and as subVIs, and the VIs are configured to deploy in two different base directories. This situation can cause a load failure if the TestStand execution loads one of these VI as a subVI befo

### 19206: Top-Level and SubVI In Different Destinations

#### Message

The deployment includes sequence files that reference the following code module VIs as top-level VIs and as subVIs, and the VIs are configured to deploy in two different base directories. This situation can cause a load failure if the TestStand execution loads one of these VI as a subVI before you load the VI as a top-level VI.

#### Why does this warning occur?

The VIs specified in the message are top-level files in the deployment that are called by other top-level files and are configured to deploy to different base destinations, which creates a copy of the files. Loading a subVI before loading the top-level file can cause a load failure.

#### How do I resolve this warning?

Determine whether the VIs must install to different base destinations. If no good reason exists to install the VIs in different base destinations, move the VIs to a single base destination. If a good reason exists to install the VIs in different base destinations, create a new wrapper for the VI and replace the instance where the VI is called as a top-level file in the sequences or workspace with the wrapper VI instead.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19207-no-relative-path-exists-between-sequenc.html language=enus -->
## TOPIC 03167: 19207: No Relative Path Exists between Sequence File and Code Module

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19207-no-relative-path-exists-between-sequenc.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19207-no-relative-path-exists-between-sequenc.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message No relative path exists between the sequence file and code modules. Why does this warning occur? No relative path exists between a sequence file and a code module included in the deployment. In some cases, this might lead to the deployment utility incorrectly fixing the paths in sequence fil

### 19207: No Relative Path Exists between Sequence File and Code Module

#### Message

No relative path exists between the sequence file and code modules.

#### Why does this warning occur?

No relative path exists between a sequence file and a code module included in the deployment. In some cases, this might lead to the deployment utility incorrectly fixing the paths in sequence files.

#### How do I resolve this warning?

Specify the code module using a path relative to the sequence file. If the path is resolved using a search directory, ensure that the search directory is included in the deployment, for example, by including the TestExec.ini file, which includes the search directories. Alternatively, you can use the Distributed Files tab to install the files without a relative path between them in the same base destination.
In some cases, the deployment utility incorrectly remaps code module paths if it cannot find a relative path between the sequence file and code module. If this occurs, complete the following steps to work around the behavior:

1. Use the code module path fields in the calling step to determine the base directory TestStand uses to find the affected file. The directory is typically a custom search directory. For example, if a code module is located at "C:\Program Files\myCompanyDir\code\module.vi", and the relative path specified in the calling step is "code\module.vi", the base directory is "C:\Program Files\myCompanyDir".
2. Add a new search directory for the deployment image path that corresponds to the base directory in the previous step. The deployment image directory is specified on the System tab of the deployment utility. For example, if the base directory is "C:\Program Files\myCompanyDir", create a new search directory "<Image>\ProgramFiles\myCompanyDir", where <Image> is the absolute path to the deployment image folder you specified in the deployment utility. Use the existing image directory to verify that the equivalent base directory is correct. Move this new directory to the top of the search directories list. Repeat this step for each unique base directory.
3. Delete all files from the deployment image directory to prevent the deployment utility from finding the files in the image directory while analyzing the source files.
4. Rebuild the deployment and verify that the paths to the affected code modules in the image directory are the same as the source files.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19208-projects-with-same-name-in-packed-libra.html language=enus -->
## TOPIC 03168: 19208: Projects With Same Name In Packed Library Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19208-projects-with-same-name-in-packed-libra.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19208-projects-with-same-name-in-packed-libra.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The deployment contains projects with the same name targeted to the same base path. National Instruments recommends that you use unique project names. To avoid name collisions, the deployment utility changes the names of the packed project libraries created for the following projects: Why do

### 19208: Projects With Same Name In Packed Library Deployment

#### Message

The deployment contains projects with the same name targeted to the same base path. National Instruments recommends that you use unique project names. To avoid name collisions, the deployment utility changes the names of the packed project libraries created for the following projects:

#### Why does this warning occur?

The distribution contains one or more projects with the same name configured to deploy to the same destination and you are deploying to packed project libraries. The deployment utility creates one packed project library for every project and names it with the same name as the project. Because the deployment contains projects with the same names, the deployment utility creates a unique name for the library. However, you must ensure that any dynamic calls made to VIs in the project library are still correct after deployment.

#### How do I resolve this warning?

National Instruments strongly recommends that you use unique names for projects. Change the name of the projects specified in the message.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19209-file-destinations-changed-to-prevent-co.html language=enus -->
## TOPIC 03169: 19209: File Destinations Changed To Prevent Conflict

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19209-file-destinations-changed-to-prevent-co.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19209-file-destinations-changed-to-prevent-co.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The destinations of the following files were changed to prevent conflicts with National Instruments products: Why does this warning occur? The destinations for the specified files can potentially conflict with a National Instruments product. To prevent these conflicts, the deployment utility

### 19209: File Destinations Changed To Prevent Conflict

#### Message

The destinations of the following files were changed to prevent conflicts with National Instruments products:

#### Why does this warning occur?

The destinations for the specified files can potentially conflict with a National Instruments product. To prevent these conflicts, the deployment utility automatically changes the file destinations.

#### How do I resolve this warning?

Review the listed files and ensure that no issues will occur as a result of the relocation of the files on the target computer. National Instruments recommends that you change the destinations of these files on the Distributed Files tab to prevent potential issues.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19210-file-not-found-when-loading-tsd-file.html language=enus -->
## TOPIC 03170: 19210: File not Found when Loading .tsd File

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19210-file-not-found-when-loading-tsd-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19210-file-not-found-when-loading-tsd-file.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message While loading the .tsd file, the following files were not found in the original location or in the updated location: Why does this warning occur? The specified files were not found in the same relative location to the .tsd file as it was before, or in the same absolute path as it was before.

### 19210: File not Found when Loading .tsd File

#### Message

While loading the .tsd file, the following files were not found in the original location or in the updated location:

#### Why does this warning occur?

The specified files were not found in the same relative location to the .tsd file as it was before, or in the same absolute path as it was before., which can lead to problems when building the deployment.

#### How do I resolve this warning?

Use the following suggestions to resolve the issue.

- Analyze the files on the Distributed Files tab to ensure that the files the deployment utility discovers all the files needed for the deployment.
- If you set file property flags on one or more of the specified files, ensure that the flags are preserved. In some cases, this message indicates that the deployment utility will lose the file properties.
- Put the files in the same location as they were the last time you saved the .tsd file.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19211-required-labview-rte-not-included.html language=enus -->
## TOPIC 03171: 19211: Required LabVIEW RTE not Included

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19211-required-labview-rte-not-included.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19211-required-labview-rte-not-included.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The installer does not include the following LabVIEW Run-Time Engines required to execute VIs. If you include the LabVIEW 2017 Run-Time Engine or later and enable the 'Backwards Compatible Runtime Engine' option in the LabVIEW adapter settings, you can ignore this warning. Why does this warn

### 19211: Required LabVIEW RTE not Included

#### Message

The installer does not include the following LabVIEW Run-Time Engines required to execute VIs. If you include the LabVIEW 2017 Run-Time Engine or later and enable the 'Backwards Compatible Runtime Engine' option in the LabVIEW adapter settings, you can ignore this warning.

#### Why does this warning occur?

You created an installer that includes VIs but does not include the LabVIEW Run-Time Engine (RTE) required to run those VIs. Because source only VIs do not include compiled code, you cannot run these types of VIs with the run-time engine. Additionaly, if you include a source only VI in a deployment, the log reports the bitness as unknown.

#### How do I resolve this warning?

Ignore this warning if you use another installer to install the LabVIEW RTE or if the LabVIEW RTE is already installed on the test station computer. Otherwise, use the Drivers and Components dialog box to include the specified LabVIEW RTEs in the installer.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19212-drivers-and-components-were-reverted-to.html language=enus -->
## TOPIC 03172: 19212: Drivers and Components Were Reverted to Earlier Version

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19212-drivers-and-components-were-reverted-to.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19212-drivers-and-components-were-reverted-to.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following drivers and components were downgraded: Why does this warning occur? The version of a driver or component you included in the patch installer is an earlier version than the version of the driver or component included in the previous deployment. This warning can occur if you rev

### 19212: Drivers and Components Were Reverted to Earlier Version

#### Message

The following drivers and components were downgraded:

#### Why does this warning occur?

The version of a driver or component you included in the patch installer is an earlier version than the version of the driver or component included in the previous deployment. This warning can occur if you reverted driver software to an earlier version after building the full distribution deployment that this patch deployment is patching. National Instruments recommends that all driver software be the same or a later version when creating a patch installer. 
If you continue the deployment without resolving this issue, the deployment utility does not revert the drivers and components the patch deployment includes to the earlier version of the drivers and components used in the full or previous deployment, which means that the development system and the test system include a different set of drivers and components.

#### How do I resolve this warning?

If you need to downgrade a driver, uninstall all drivers and components from the test system and create a new full distribution installer to ensure that the correct drivers and components are installed.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19213-teststand-workspace-file-not-found.html language=enus -->
## TOPIC 03173: 19213: TestStand Workspace File not Found

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19213-teststand-workspace-file-not-found.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19213-teststand-workspace-file-not-found.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Cannot locate the specified file in the TestStand workspace. Why does this warning occur? The path of the specified file could not be resolved, which can indicate one of the following situations: The file was deleted. TestStand search directories have changed and the file cannot be found. No

### 19213: TestStand Workspace File not Found

#### Message

Cannot locate the specified file in the TestStand workspace.

#### Why does this warning occur?

The path of the specified file could not be resolved, which can indicate one of the following situations:

- The file was deleted.
- TestStand search directories have changed and the file cannot be found.

Note:

#### How do I resolve this warning?

Complete the following steps to resolve the issue.

1. Open the specified workspace.
2. If the message specified a TestStand project, locate the TestStand project.
3. Once you find the missing file, update the workspace path, and ensure that the file exists on disk and is readable.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19215-installer-generation-warning.html language=enus -->
## TOPIC 03174: 19215: Installer Generation Warning

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19215-installer-generation-warning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19215-installer-generation-warning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Internal warning occurred when creating an installer. Why does this warning occur? The specified internal warnings occurred when creating an installer. How do I resolve this warning? Refer to the specific message details to resolve the warning. Additional information on the error can be foun

### 19215: Installer Generation Warning

#### Message

Internal warning occurred when creating an installer.

#### Why does this warning occur?

The specified internal warnings occurred when creating an installer.

#### How do I resolve this warning?

Refer to the specific message details to resolve the warning. Additional information on the error can be found in the TSDU Installer Build Log file. To generate this file, select the Save Log Button dropdown menu, and select the Save Technical Support Report option. The generated ZIP archive contains the TSDU Installer Build Log file.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19216-required-product-not-included.html language=enus -->
## TOPIC 03175: 19216: Required Product Not Included

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19216-required-product-not-included.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19216-required-product-not-included.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message A Product required by a file in the deployment is not included in the installer. Why does this warning occur? A file in the deployment requires a product that is not included in the deployment. If the product is not already installed on the target system, the deployment will fail to execute.

### 19216: Required Product Not Included

#### Message

A Product required by a file in the deployment is not included in the installer.

#### Why does this warning occur?

A file in the deployment requires a product that is not included in the deployment. If the product is not already installed on the target system, the deployment will fail to execute.

#### How do I resolve this warning?

To resolve this issue, click the Drivers and Components button in the Installer tab to launch the Drivers and Components dialog box, then either select the
 Automatically include Required Products
 setting or manually select the specified products in the Installers tree.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19217-require-product-newer-than-installed-ve.html language=enus -->
## TOPIC 03176: 19217: Require Product Newer Than Installed Version

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19217-require-product-newer-than-installed-ve.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19217-require-product-newer-than-installed-ve.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The version of a product on the system is lower than the version required by a file in the deployment. Why does this warning occur? A file in the deployment requires a product version that is newer than the version installed on the system How do I resolve this warning? To resolve this issue,

### 19217: Require Product Newer Than Installed Version

#### Message

The version of a product on the system is lower than the version required by a file in the deployment.

#### Why does this warning occur?

A file in the deployment requires a product version that is newer than the version installed on the system

#### How do I resolve this warning?

To resolve this issue, install the specified version of the product. If the product will already be present on the target machine where you will install the deployment, you can ignore this warning.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19218-required-product-not-installed.html language=enus -->
## TOPIC 03177: 19218: Required Product Not Installed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19218-required-product-not-installed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19218-required-product-not-installed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message A Product required by a file in the deployment is not installed on the system. Why does this warning occur? You have selected the "Automatically Include Required Installers" option in the Drivers & Components dialog, but an installer required by a file in the deployment is not available on t

### 19218: Required Product Not Installed

#### Message

A Product required by a file in the deployment is not installed on the system.

#### Why does this warning occur?

You have selected the "Automatically Include Required Installers" option in the Drivers & Components dialog, but an installer required by a file in the deployment is not available on the system.

#### How do I resolve this warning?

Install the products specified in the warning message. If the product is alreday installed on the target machine, you can ignore this warning.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19219-could-not-rebuild-distribution-vis.html language=enus -->
## TOPIC 03178: 19219: Could Not Rebuild Distribution VIs

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19219-could-not-rebuild-distribution-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19219-could-not-rebuild-distribution-vis.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The distribution VIs could not be rebuilt. The deployment will continue with a cached copy of the distribution VIs, which negatively impacts deployment speed but does not affect the build output. See the error message below for additional details. Why does this warning occur? The distributio

### 19219: Could Not Rebuild Distribution VIs

#### Message

The distribution VIs could not be rebuilt. The deployment will continue with a cached copy of the distribution VIs, which negatively impacts deployment speed but does not affect the build output. See the error message below for additional details.

#### Why does this warning occur?

The distribution VIs could not be rebuilt. The deployment utility automatically creates a new set of distribution VIs for every version of LabVIEW that was released after TestStand was released and mass compiles them for performance reasons. This error could mean that the deployment utility does not have access to the <TestStand Public>\Components\Tools\Deployment Utility directory.

#### How do I resolve this warning?

Ensure that the <TestStand Public>\Components\Tools\Deployment Utility is writeable and the user running the deployment utility has write access to it.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19220-required-package-version-not-installed.html language=enus -->
## TOPIC 03179: 19220: Required Package Version Not Installed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19220-required-package-version-not-installed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19220-required-package-version-not-installed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The version requirements for the specified package are not satisfied by the version installed on the system Why does this warning occur? For the specified package, you specified a version requirement in the Dependencies dialog in the Package Distribution Options tab, but the version installe

### 19220: Required Package Version Not Installed

#### Message

The version requirements for the specified package are not satisfied by the version installed on the system

#### Why does this warning occur?

For the specified package, you specified a version requirement in the Dependencies dialog in the Package Distribution Options tab, but the version installed on the system does not meet the requirements.

#### How do I resolve this warning?

Update the required version to include the currently installed version, or install a version of the specified package which satisfies the version requirements you specified.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19221-gll-destination-has-moved-relative-to-l.html language=enus -->
## TOPIC 03180: 19221: GLL Destination Has Moved Relative To LabVIEW NXG Project

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19221-gll-destination-has-moved-relative-to-l.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19221-gll-destination-has-moved-relative-to-l.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The Location of the GLL relative to the Project file has changed for the following steps. The step will be executable, but you will be unable to rebuild the GLLs on a target machine without updating the GLL path. Why does this warning occur? In the distributed files tab, you modified the des

### 19221: GLL Destination Has Moved Relative To LabVIEW NXG Project

#### Message

The Location of the GLL relative to the Project file has changed for the following steps. The step will be executable, but you will be unable to rebuild the GLLs on a target machine without updating the GLL path.

#### Why does this warning occur?

In the distributed files tab, you modified the destination of either the LabVIEW project or the GLL for a LabVIEW NXG step. For LabVIEW NXG steps to support rebuilding the GLL automatically from the source files, the GLL and LabVIEW NXG project must remain in the same relative location.

#### How do I resolve this warning?

Ensure that the destination for all GLLs and LabVIEW NXG projects are set such that the files are deployed in the same relative location.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19222-labview-nxg-not-supported-in-32-bit-tes.html language=enus -->
## TOPIC 03181: 19222: LabVIEW NXG Not Supported in 32-bit TestStand

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19222-labview-nxg-not-supported-in-32-bit-tes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19222-labview-nxg-not-supported-in-32-bit-tes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Files in the deployment contains LabVIEW NXG Modules, which are not supported in 32-bit TestStand. To deploy these files, you must use the 64-bit TestStand Deployment Utility. Why does this warning occur? You attempted to deploy sequence files which call LabVIEW NXG code modules from the 32-

### 19222: LabVIEW NXG Not Supported in 32-bit TestStand

#### Message

Files in the deployment contains LabVIEW NXG Modules, which are not supported in 32-bit TestStand. To deploy these files, you must use the 64-bit TestStand Deployment Utility.

#### Why does this warning occur?

You attempted to deploy sequence files which call LabVIEW NXG code modules from the 32-bit TestStand deployment utility. LabVIEW NXG code modules can only be called from 64-bit TestStand

#### How do I resolve this warning?

To deploy LabVIEW NXG code modules, use the 64-bit version of the TestStand Deployment Utility

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19223-no-corresponding-package-is-installed-f.html language=enus -->
## TOPIC 03182: 19223: No Corresponding Package Is Installed for Required Product

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19223-no-corresponding-package-is-installed-f.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19223-no-corresponding-package-is-installed-f.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message No package is installed which provides the following required products. The product must be installed on the test station computer before executing the deployed files. Why does this warning occur? The deployment detected products that the code modules in the deployment require, but no packag

### 19223: No Corresponding Package Is Installed for Required Product

#### Message

No package is installed which provides the following required products. The product must be installed on the test station computer before executing the deployed files.

#### Why does this warning occur?

The deployment detected products that the code modules in the deployment require, but no package currently installed on the system satisfies the requirement.

#### How do I resolve this warning?

Some required products may only be available as MSI-based installers, which cannot be included in a package based distribution. Either use the MSI-based installer build output type on the Mode tab, or manually install the specified products on the test station computer.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19404-file-moved-in-patch.html language=enus -->
## TOPIC 03183: 19404: File Moved In Patch

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19404-file-moved-in-patch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19404-file-moved-in-patch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The destinations for the following files changed in the current patch deployment: Why does this information message occur? A file that was included in the full deployment has a new destination in the patch deployment. Generally this situation does not cause problems, but methods called dynam

### 19404: File Moved In Patch

#### Message

The destinations for the following files changed in the current patch deployment:

#### Why does this information message occur?

A file that was included in the full deployment has a new destination in the patch deployment. Generally this situation does not cause problems, but methods called dynamically or steps called using expressions might incorrectly call the old file.

#### How do I resolve this information message?

National Instruments recommends that you do not change the destination of files in a patch deployment because patch deployments cannot remove files, which can leave orphaned files in a test system and lead to subtle problems that are difficult to debug. If you need to move the file, create a new full deployment.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19405-file-deleted-in-patch.html language=enus -->
## TOPIC 03184: 19405: File Deleted In Patch

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19405-file-deleted-in-patch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19405-file-deleted-in-patch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The current image does not contain the following files: Why does this information message occur? A file that was in the full deployment is no longer present in the patch deployment. Generally this situation does not cause problems, but methods called dynamically or steps called using express

### 19405: File Deleted In Patch

#### Message

The current image does not contain the following files:

#### Why does this information message occur?

A file that was in the full deployment is no longer present in the patch deployment. Generally this situation does not cause problems, but methods called dynamically or steps called using expressions might incorrectly call the old file.

#### How do I resolve this information message?

National Instruments recommends that you do not delete files in a patch deployment because patch deployments cannot remove files, which can leave orphaned files in a test system and lead to subtle problems that are difficult to debug. If you need to remove the file, create a new full deployment.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19407-project-library-missing-files-in-full-d.html language=enus -->
## TOPIC 03185: 19407: Project Library Missing Files In Full Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19407-project-library-missing-files-in-full-d.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19407-project-library-missing-files-in-full-d.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following project libraries do not reference the same set of files included in the dependent deployment: Why does this information message occur? The project libraries specified in the error message contained one or more files that the project libraries included in the patch deployment n

### 19407: Project Library Missing Files In Full Deployment

#### Message

The following project libraries do not reference the same set of files included in the dependent deployment:

#### Why does this information message occur?

The project libraries specified in the error message contained one or more files that the project libraries included in the patch deployment no longer reference. The deployment utility did not include these files because the test sequences no longer reference the files. Any VIs that dynamically call into these VIs will be broken.

#### How do I resolve this information message?

If you call these VIs dynamically and deploy using a workspace, add the VIs to the TestStand workspace to include them with the deployment. If you call these VIs dynamically and deploy using a directory, copy the files into the top-level directory.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19408-source-path-changed-in-patch.html language=enus -->
## TOPIC 03186: 19408: Source Path Changed In Patch

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19408-source-path-changed-in-patch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19408-source-path-changed-in-patch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The source file path for the following files is different from the source file path of the file included in the dependency deployment: Why does this information message occur? The source file path in the patch is different in the patch deployment than it was in the full deployment. For examp

### 19408: Source Path Changed In Patch

#### Message

The source file path for the following files is different from the source file path of the file included in the dependency deployment:

#### Why does this information message occur?

The source file path in the patch is different in the patch deployment than it was in the full deployment. For example, the full deployment included
 C:\orig\a.vi
 installing in
 <Image>\a.vi
 , and the patch deployment included
 C:\new\a.vi
 installing in
 <Image>\a.vi
 .

#### How do I resolve this information message?

Verify that the new source location is correct. If it is not correct, use the hierarchy view on the Distributed Files tab to determine the callers of the file and use the appropriate application development environment to modify the callers to refer to the appropriate file.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19409-llb-missing-files-in-patch-deployment.html language=enus -->
## TOPIC 03187: 19409: LLB Missing Files in Patch Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19409-llb-missing-files-in-patch-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19409-llb-missing-files-in-patch-deployment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following LLBs do not contain all the VIs that were included in the dependency deployment: Why does this information message occur? The LLBs specified in the error message contained one or more files in the dependent deployment that are no longer included in the LLBs in the patch deploym

### 19409: LLB Missing Files in Patch Deployment

#### Message

The following LLBs do not contain all the VIs that were included in the dependency deployment:

#### Why does this information message occur?

The LLBs specified in the error message contained one or more files in the dependent deployment that are no longer included in the LLBs in the patch deployment. The deployment utility did not include these files because the sequence files in the current deployment no longer reference the files. Any VIs that dynamically call into these VIs will be broken.

#### How do I resolve this information message?

If you are calling these VIs dynamically, add them to the LLB to include them with the deployment. If the files were top-level files installed in an LLB destination, add the files to the TestStand workspace to include the files in the deployment and change the destination on the Distributed Files tab so the files install in the destination LLB.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19410-files-moved-to-llb.html language=enus -->
## TOPIC 03188: 19410: Files Moved to LLB

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19410-files-moved-to-llb.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19410-files-moved-to-llb.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following VIs have a file name with invalid character(s) and will be copied to IllegalFilenames.llb in the SupportVIs directory: Why does this information message occur? The deployment contains one or more VIs with names that contain invalid characters. These files were moved to an LLB t

### 19410: Files Moved to LLB

#### Message

The following VIs have a file name with invalid character(s) and will be copied to IllegalFilenames.llb in the SupportVIs directory:

#### Why does this information message occur?

The deployment contains one or more VIs with names that contain invalid characters. These files were moved to an LLB to keep the file name the same. A filename cannot contain any of the following characters: \, /, :, *, ?, ", <, >, or |.

#### How do I resolve this information message?

Use the following suggestions to resolve the issue.

- Rename the files so they do not contain invalid characters.
- Because the deployment utility changes the destination of the files to use LLBs, you can safely ignore this message.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19411-file-filtered.html language=enus -->
## TOPIC 03189: 19411: File Filtered

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19411-file-filtered.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19411-file-filtered.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following files were filtered: Why does this information message occur? The deployment utility detected that some dependent files should be filtered out because they match the filtering criteria specified in the filter.ini file. Filtering removes files that you do not want to include in

### 19411: File Filtered

#### Message

The following files were filtered:

#### Why does this information message occur?

The deployment utility detected that some dependent files should be filtered out because they match the filtering criteria specified in the filter.ini file. Filtering removes files that you do not want to include in the deployment, such as system DLLs or TestStand DLLs. DLLs that are part of TestStand should be deployed by including the TestStand Runtime or by installing TestStand in the test system.

#### How do I resolve this information message?

This message is only informational.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19412-file-excluded.html language=enus -->
## TOPIC 03190: 19412: File Excluded

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19412-file-excluded.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19412-file-excluded.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following files were excluded: Why does this information message occur? The deployment utility detected that some dependent files should be excluded because they match the exclusion criteria specified in the filter.ini file. Exclusions remove files that you would not want to include in a

### 19412: File Excluded

#### Message

The following files were excluded:

#### Why does this information message occur?

The deployment utility detected that some dependent files should be excluded because they match the exclusion criteria specified in the filter.ini file. Exclusions remove files that you would not want to include in a deployment, such as DLLs that are part of the Microsoft Windows operating system.

#### How do I resolve this information message?

This message is only informational.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19413-custom-sequence-file.html language=enus -->
## TOPIC 03191: 19413: Custom Sequence File

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19413-custom-sequence-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19413-custom-sequence-file.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following custom sequence files have not been processed. Verify that all the dependent files are being deployed to the correct locations. Why does this information message occur? The deployment includes a custom sequence file, which the deployment utility cannot process. How do I resolve

### 19413: Custom Sequence File

#### Message

The following custom sequence files have not been processed. Verify that all the dependent files are being deployed to the correct locations.

#### Why does this information message occur?

The deployment includes a custom sequence file, which the deployment utility cannot process.

#### How do I resolve this information message?

Review all the dependencies in the custom sequence files and ensure that the paths will work on the test station computers, particularly absolute paths and paths that are relative to the sequence file. Ensure that all destinations are set so that the files remain in the same relative paths as they exist in the source.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19414-filenames-that-contain-non-ascii-charac.html language=enus -->
## TOPIC 03192: 19414: Filenames that Contain Non-ASCII Characters Included in English Installer

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19414-filenames-that-contain-non-ascii-charac.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19414-filenames-that-contain-non-ascii-charac.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following filenames contain non-ASCII characters and were included in an English installer: Why does this information message occur? One or more of the files contain non-ASCII characters, and the installer language is set to English. When the installer language is set to English, the dep

### 19414: Filenames that Contain Non-ASCII Characters Included in English Installer

#### Message

The following filenames contain non-ASCII characters and were included in an English installer:

#### Why does this information message occur?

One or more of the files contain non-ASCII characters, and the installer language is set to English. When the installer language is set to English, the deployment utility optimizes the memory consumption of the installer by interpreting all characters as ASCII. If the installer includes Unicode or other non-ASCII characters, the filenames installed in the test system will be incorrect.

#### How do I resolve this information message?

Use the following suggestions to resolve the issue.

- Change paths to use only ASCII characters.
- Use the Advanced Installer Options dialog box to change the installer language.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19415-labview-project-consolidation-failed-be.html language=enus -->
## TOPIC 03193: 19415: LabVIEW Project Consolidation Failed because Projects Contain Different Conditional Disable Symbols

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19415-labview-project-consolidation-failed-be.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19415-labview-project-consolidation-failed-be.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Could not consolidate LabVIEW projects because conditional disable symbols defined in the project are different for the following LabVIEW projects: Why does this information message occur? The deployment utility could not consolidate projects because one or more projects had different values

### 19415: LabVIEW Project Consolidation Failed because Projects Contain Different Conditional Disable Symbols

#### Message

Could not consolidate LabVIEW projects because conditional disable symbols defined in the project are different for the following LabVIEW projects:

#### Why does this information message occur?

The deployment utility could not consolidate projects because one or more projects had different values for the same conditional disable symbols.

#### How do I resolve this information message?

Use the following suggestions to resolve the issue.

- Ensure that any conditional disable symbols defined in multiple projects all have the same value.
- Disable the Consolidate Files Projects Share option in the LabVIEW VI Options dialog box.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19416-labview-project-consolidation-failed-be.html language=enus -->
## TOPIC 03194: 19416: LabVIEW Project Consolidation Failed because of File Conflicts

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19416-labview-project-consolidation-failed-be.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19416-labview-project-consolidation-failed-be.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Could not consolidate LabVIEW projects because multiple projects include the following files that have the same filename: Why does this information message occur? Two or more VIs called in the test system have the same filename. To prevent possible cross-linking issues, the deployment utilit

### 19416: LabVIEW Project Consolidation Failed because of File Conflicts

#### Message

Could not consolidate LabVIEW projects because multiple projects include the following files that have the same filename:

#### Why does this information message occur?

Two or more VIs called in the test system have the same filename. To prevent possible cross-linking issues, the deployment utility does not consolidate the projects.
 Note:
 You can call the same VI from multiple projects. The consolidation is cancelled only if two or more different VIs have the same name.

#### How do I resolve this information message?

Use the following suggestions to resolve the issue.

- Ensure that no duplicate file names exist among the projects.
- Disable the Consolidate Files Projects Share option in the LabVIEW VI Options dialog box.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19417-labview-projects-consolidation-failed-b.html language=enus -->
## TOPIC 03195: 19417: LabVIEW Projects Consolidation Failed because Projects Specify Multiple Targets

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19417-labview-projects-consolidation-failed-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19417-labview-projects-consolidation-failed-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Could not consolidate the following LabVIEW projects because the projects contain targets other than My Computer: Why does this information message occur? Some of the projects contain targets other than My Computer. The deployment utility cannot consolidate projects with other target types.

### 19417: LabVIEW Projects Consolidation Failed because Projects Specify Multiple Targets

#### Message

Could not consolidate the following LabVIEW projects because the projects contain targets other than My Computer:

#### Why does this information message occur?

Some of the projects contain targets other than My Computer. The deployment utility cannot consolidate projects with other target types.

#### How do I resolve this information message?

Use the following suggestions to resolve the issue.

- Remove all targets other than My Computer from the projects.
- Disable the Consolidate Files Projects Share option in the LabVIEW VI Options dialog box.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19418-labview-projects-consolidation-failed-b.html language=enus -->
## TOPIC 03196: 19418: LabVIEW Projects Consolidation Failed because of Error Creating Project

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19418-labview-projects-consolidation-failed-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19418-labview-projects-consolidation-failed-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Could not create the consolidated project required to create a deployment. Why does this information message occur? The deployment utility was not able to create the consolidated LabVIEW project. How do I resolve this information message? Disable the Consolidate File Projects Share option in

### 19418: LabVIEW Projects Consolidation Failed because of Error Creating Project

#### Message

Could not create the consolidated project required to create a deployment.

#### Why does this information message occur?

The deployment utility was not able to create the consolidated LabVIEW project.

#### How do I resolve this information message?

Disable the Consolidate File Projects Share option in the LabVIEW VI Options dialog box.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19419-labview-projects-consolidation-failed-b.html language=enus -->
## TOPIC 03197: 19419: LabVIEW Projects Consolidation Failed because of Conflict between Loose VIs and VIs Project References

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19419-labview-projects-consolidation-failed-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19419-labview-projects-consolidation-failed-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Cannot consolidate LabVIEW projects because some VIs are referenced by test sequences in the context of a LabVIEW project and outside the context of a LabVIEW project. Why does this information message occur? The deployment includes sequence files that refer to VIs using a LabVIEW project an

### 19419: LabVIEW Projects Consolidation Failed because of Conflict between Loose VIs and VIs Project References

#### Message

Cannot consolidate LabVIEW projects because some VIs are referenced by test sequences in the context of a LabVIEW project and outside the context of a LabVIEW project.

#### Why does this information message occur?

The deployment includes sequence files that refer to VIs using a LabVIEW project and without using a LabVIEW project, and you have enabled the Consolidate Files Projects Share option in the LabVIEW VI Options dialog box. For example, you have one top-level VI in a step configured to call the VI in the context of a LabVIEW project and another VI called in a step configured to call the VI without using a LabVIEW project.

#### How do I resolve this information message?

Use the following suggestions to resolve the issue.

- Ensure all VIs in the deployment are called only in the context of a LabVIEW project (not necessarily the same project for all of them) or outside the context of a LabVIEW project but not both.
- Disable the Consolidate Files Projects Share option in the LabVIEW VI Options dialog box.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19420-unprocessed-file-overwrites-file-in-ima.html language=enus -->
## TOPIC 03198: 19420: Unprocessed File Overwrites File In Image

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19420-unprocessed-file-overwrites-file-in-ima.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19420-unprocessed-file-overwrites-file-in-ima.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following unprocessed files already exist in the image directory: Why does this information message occur? One or more of the files you are including as unprocessed file are overwriting files that are already in the image directory. This usually means that the files are dependencies of o

### 19420: Unprocessed File Overwrites File In Image

#### Message

The following unprocessed files already exist in the image directory:

#### Why does this information message occur?

One or more of the files you are including as unprocessed file are overwriting files that are already in the image directory. This usually means that the files are dependencies of one or more of the processed top-level files and were included as part of the deployment process. Ensure that the top-level files will work correctly with the unprocessed file.

#### How do I resolve this information message?

This issue does not affect the deployment. You can process the files to avoid receiving this message again.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19421-image-or-installer-is-protected-directo.html language=enus -->
## TOPIC 03199: 19421: Image or Installer is Protected Directory

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19421-image-or-installer-is-protected-directo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19421-image-or-installer-is-protected-directo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following location is inside a protected directory. Files in this directory cannot be deleted. National Instruments strongly recommends that you select another directory for the image or installer directory. Why does this information message occur? The image directory or installer direct

### 19421: Image or Installer is Protected Directory

#### Message

The following location is inside a protected directory. Files in this directory cannot be deleted. National Instruments strongly recommends that you select another directory for the image or installer directory.

#### Why does this information message occur?

The image directory or installer directory is set to a protected directory. The following directories are protected:

- Microsoft Windows directory
- 32-bit and 64-bit Program Files directories
- TestStand directory
- User profile directory
- System directory

#### How do I resolve this information message?

Change the image directory and installer directory to a different directory.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19422-max-configuration-not-included-in-patch.html language=enus -->
## TOPIC 03200: 19422: MAX Configuration not Included in Patch

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19422-max-configuration-not-included-in-patch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19422-max-configuration-not-included-in-patch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The specified MAX configuration file is modified. Consider including it in the patch deployment. Why does this information message occur? The specified MAX configuration file was not included in the patch deployment, but the deployment utility detected that the file has been modified. How do

### 19422: MAX Configuration not Included in Patch

#### Message

The specified MAX configuration file is modified. Consider including it in the patch deployment.

#### Why does this information message occur?

The specified MAX configuration file was not included in the patch deployment, but the deployment utility detected that the file has been modified.

#### How do I resolve this information message?

Include the MAX configuration file from the Drivers and Components dialog box on the Installer Options tab.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19423-file-destinations-were-changed.html language=enus -->
## TOPIC 03201: 19423: File destinations were changed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19423-file-destinations-were-changed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19423-file-destinations-were-changed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message During load, the deployment utility updated the destination of the following directories: Why does this information message occur? During load, the deployment utility updated the location of the image directory or installer directory, which usually happens when the image directory or install

### 19423: File destinations were changed

#### Message

During load, the deployment utility updated the destination of the following directories:

#### Why does this information message occur?

During load, the deployment utility updated the location of the image directory or installer directory, which usually happens when the image directory or installer directory are set to a directory that is specific to a certain computer, for example, the user directory. The deployment utility has automatically updated the .tsd file to point to the directories specified in the message. Ensure that the locations are correct.

#### How do I resolve this information message?

Save the .tsd file so the message will not display the next time the deployment utility opens the .tsd file. Alternatively, if more than one computer must share the file, ensure that the image directory and installer directory are not in the user directory.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19424-installation-type-of-a-driver-or-compon.html language=enus -->
## TOPIC 03202: 19424: Installation Type Of A Driver Or Component Does Not Match Previous Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19424-installation-type-of-a-driver-or-compon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19424-installation-type-of-a-driver-or-compon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The installer type for the following installers does not match the type used in the full deployment: Why does this information message occur? You are creating a patch deployment installer, and the installation type of a driver or component does not match the installation type used in the dep

### 19424: Installation Type Of A Driver Or Component Does Not Match Previous Deployment

#### Message

The installer type for the following installers does not match the type used in the full deployment:

#### Why does this information message occur?

You are creating a patch deployment installer, and the installation type of a driver or component does not match the installation type used in the dependency deployment. For example, this message occurs if the previous deployment was built with the DAQmx Core driver, and you upgraded to the DAQmx Full driver before creating a patch deployment. This situation is a problem only when one of the installation types is not a subset of the other one. Contact National Instruments support for more information about this issue.

#### How do I resolve this information message?

This message is informational only.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19425-could-not-record-project-library-conten.html language=enus -->
## TOPIC 03203: 19425: Could Not Record Project Library Contents

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19425-could-not-record-project-library-conten.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19425-could-not-record-project-library-conten.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Contents of project libraries included in the deployment were not recorded because LabVIEW is not responding. Why does this information message occur? The deployment utility could not obtain the contents of the deployed project libraries. Future patch deployments you create with this .tsd fi

### 19425: Could Not Record Project Library Contents

#### Message

Contents of project libraries included in the deployment were not recorded because LabVIEW is not responding.

#### Why does this information message occur?

The deployment utility could not obtain the contents of the deployed project libraries. Future patch deployments you create with this .tsd file will not warn about mismatched contents in project libraries. This situation has no effect on the deployed files and affects only the warnings displayed by future patch deployments that use this deployment as the dependent deployment.

#### How do I resolve this information message?

Create the deployment again.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19426-labview-project-included-but-not-refere.html language=enus -->
## TOPIC 03204: 19426: LabVIEW Project Included But Not Referenced

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19426-labview-project-included-but-not-refere.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19426-labview-project-included-but-not-refere.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following LabVIEW projects are not referenced by any steps in the TestStand sequence files and will not be updated: Why does this information message occur? You have included a LabVIEW project in the deployment that is not referenced by any of the LabVIEW steps in the sequence files. Bec

### 19426: LabVIEW Project Included But Not Referenced

#### Message

The following LabVIEW projects are not referenced by any steps in the TestStand sequence files and will not be updated:

#### Why does this information message occur?

You have included a LabVIEW project in the deployment that is not referenced by any of the LabVIEW steps in the sequence files. Because the project is not referenced, the deployment utility does not make any changes to the project, and the project might not work correctly if opened on the target computer.

#### How do I resolve this information message?

This issue will not affect the functionality of the deployment. To prevent this message, you must reference the project in one of the LabVIEW steps in the sequence file, or omit the project from the deployment on the Distributed Files tab.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19427-found-labview-project-files-within-anot.html language=enus -->
## TOPIC 03205: 19427: Found LabVIEW Project Files Within Another Project

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19427-found-labview-project-files-within-anot.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19427-found-labview-project-files-within-anot.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following project files were referenced by another project and are not processed: Why does this information message occur? A LabVIEW project included in the deployment references one or more LabVIEW project files. The deployment utility does not process these nested project files. How do

### 19427: Found LabVIEW Project Files Within Another Project

#### Message

The following project files were referenced by another project and are not processed:

#### Why does this information message occur?

A LabVIEW project included in the deployment references one or more LabVIEW project files. The deployment utility does not process these nested project files.

#### How do I resolve this information message?

This situation does not cause any issues with the current deployment. To prevent this message from displaying and to ensure that these projects are processed in the deployment utility if steps reference the files in the project dynamically, add them to the TestStand workspace or include them in the directory specified on the System Source tab.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19428-modified-files-not-included-in-patch.html language=enus -->
## TOPIC 03206: 19428: Modified Files Not Included In Patch

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19428-modified-files-not-included-in-patch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19428-modified-files-not-included-in-patch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following files were not included in the patch deployment because the file status was set to Not Included, but the files have been modified: Why does this information message occur? You have chosen not to include files in a patch deployment that were modified since the previous deploymen

### 19428: Modified Files Not Included In Patch

#### Message

The following files were not included in the patch deployment because the file status was set to Not Included, but the files have been modified:

#### Why does this information message occur?

You have chosen not to include files in a patch deployment that were modified since the previous deployment.

#### How do I resolve this information message?

Review the files listed in this message and verify that the files are not required in the patch. In the case of LabVIEW files, open the files and verify that any subVIs called were not modified in the patch. Use the list of files included in the deployment in the Build Complete message to determine modification status of all the files in the deployment. In many cases, changes to a subVI require LabVIEW to recompile any calling VIs. If any of the subVIs were modified, include the files in the patch by changing the Inclusion State on the Distributed Files tab. Not including these modified files in a patch deployment can cause the VIs to become broken on the target computer.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19429-process-model-mismatch-during-deploymen.html language=enus -->
## TOPIC 03207: 19429: Process Model Mismatch During Deployment (Default Models Active)

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19429-process-model-mismatch-during-deploymen.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19429-process-model-mismatch-during-deploymen.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message There is a mismatch between the currently active process model and the process model the TestStand Runtime installer will include. Your computer currently has the default process models, but the installer will use the legacy process models. Why does this information message occur? The comput

### 19429: Process Model Mismatch During Deployment (Default Models Active)

#### Message

There is a mismatch between the currently active process model and the process model the TestStand Runtime installer will include. Your computer currently has the default process models, but the installer will use the legacy process models.

#### Why does this information message occur?

The computer currently has the default process models active but the deployment is configured to use the legacy process models.

#### How do I resolve this information message?

Ensure that the deployment will work correctly with the legacy process models. To change the currently active model, use the Legacy Model Switcher, located in the TestStand Start menu group.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19430-process-model-mismatch-during-deploymen.html language=enus -->
## TOPIC 03208: 19430: Process Model Mismatch During Deployment (Legacy Models Active)

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19430-process-model-mismatch-during-deploymen.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19430-process-model-mismatch-during-deploymen.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message There is a mismatch between the currently active process model and the process model the TestStand Runtime installer will include. Your computer currently has the legacy process models, but the installer will use the default process models. Why does this information message occur? The comput

### 19430: Process Model Mismatch During Deployment (Legacy Models Active)

#### Message

There is a mismatch between the currently active process model and the process model the TestStand Runtime installer will include. Your computer currently has the legacy process models, but the installer will use the default process models.

#### Why does this information message occur?

The computer currently has the legacy process models active but the deployment is configured to use the default process models.

#### How do I resolve this information message?

Ensure that the deployment will work correctly with the default process models. To change the currently active model, use the Legacy Model Switcher, located in the TestStand Start menu group.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19431-installer-requires-teststand-to-be-alre.html language=enus -->
## TOPIC 03209: 19431: Installer Requires TestStand To Be Already Installed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19431-installer-requires-teststand-to-be-alre.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19431-installer-requires-teststand-to-be-alre.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Because this installer copies files in the TestStand directory, you must install TestStand before you run the installer. Why does this information message occur? Some files in the deployment are configured to be copied in the TestStand directory on the target computer. If you install TestSta

### 19431: Installer Requires TestStand To Be Already Installed

#### Message

Because this installer copies files in the TestStand directory, you must install TestStand before you run the installer.

#### Why does this information message occur?

Some files in the deployment are configured to be copied in the TestStand directory on the target computer. If you install TestStand after the test system was installed, the TestStand installer might overwrite these files. Install TestStand on the target computer before installing this deployment.

#### How do I resolve this information message?

Do not deploy files to the TestStand directory. Use the TestStand Public directory instead. If you will not install TestStand in the test system, you can safely ignore this message.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19436-merge-failed-loose-vis-with-multiple-de.html language=enus -->
## TOPIC 03210: 19436: Merge Failed Loose VIs With Multiple Destinations

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19436-merge-failed-loose-vis-with-multiple-de.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19436-merge-failed-loose-vis-with-multiple-de.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Could not consolidate because the deployment installs files to multiple installation destinations. Why does this information message occur? The deployment is distributing files to more than one destination. The deployment utility creates one LabVIEW project to distribute files for every inst

### 19436: Merge Failed Loose VIs With Multiple Destinations

#### Message

Could not consolidate because the deployment installs files to multiple installation destinations.

#### Why does this information message occur?

The deployment is distributing files to more than one destination. The deployment utility creates one LabVIEW project to distribute files for every installation destination and cannot consolidate files if the deployment has multiple destinations.

#### How do I resolve this information message?

Use the following suggestions to resolve the issue.

- Move all the files to the same destination. Use the Build Preview view on the Distributed Files tab to select the destination root and change all the files in it.
- Resolving this error message might improve build time.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19437-deployment-will-set-specific-process-mo.html language=enus -->
## TOPIC 03211: 19437: Deployment Will Set Specific Process Model

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19437-deployment-will-set-specific-process-mo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19437-deployment-will-set-specific-process-mo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The deployment will set the process model to the following value: Why does this information message occur? You enabled the option to set a specific process model during installation of the test system. The additional details in the message specify which process model will be set. How do I re

### 19437: Deployment Will Set Specific Process Model

#### Message

The deployment will set the process model to the following value:

#### Why does this information message occur?

You enabled the option to set a specific process model during installation of the test system. The additional details in the message specify which process model will be set.

#### How do I resolve this information message?

This message is only informational.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19438-cannot-read-dll-dependencies.html language=enus -->
## TOPIC 03212: 19438: Cannot Read DLL Dependencies

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19438-cannot-read-dll-dependencies.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19438-cannot-read-dll-dependencies.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message Cannot read DLL dependencies because the bitness of the deployment utility does not match the bitness of the DLL. Why does this information message occur? The DLLs the message specifies do not match the bitness of the deployment utility and cannot be loaded to determine their dependencies. H

### 19438: Cannot Read DLL Dependencies

#### Message

Cannot read DLL dependencies because the bitness of the deployment utility does not match the bitness of the DLL.

#### Why does this information message occur?

The DLLs the message specifies do not match the bitness of the deployment utility and cannot be loaded to determine their dependencies.

#### How do I resolve this information message?

Recompile the DLLs so they are the same bitness as the deployment utility. Alternatively, make sure that the deployment includes all the required dependencies for the DLLs and that code modules are called by a separate process that can load the files.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19439-ni-product-not-found.html language=enus -->
## TOPIC 03213: 19439: NI Product Not Found

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19439-ni-product-not-found.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19439-ni-product-not-found.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following TestStand features are not installed or installation is not complete: Why does this information message occur? One or more TestStand features are not installed or have invalid deployment information. This situation can occur when you launch the deployment utility on a computer

### 19439: NI Product Not Found

#### Message

The following TestStand features are not installed or installation is not complete:

#### Why does this information message occur?

One or more TestStand features are not installed or have invalid deployment information. This situation can occur when you launch the deployment utility on a computer on which you did not install all the TestStand features when installing TestStand, or on a computer on which you installed a partial deployment that included the deployment utility. The specified features cannot be included in a distribution that the deployment utility creates. You can, however, continue to deploy other features of TestStand.

#### How do I resolve this information message?

If you need to deploy the features specified in the error message, use the TestStand installer to install the features or use a different deployment created with the deployment utility.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19440-teststand-component-not-migrated.html language=enus -->
## TOPIC 03214: 19440: TestStand Component Not Migrated

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19440-teststand-component-not-migrated.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19440-teststand-component-not-migrated.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The specified TestStand components were not migrated to the current version of TestStand. Verify that required components are selected in the Drivers and Components Dialog. Why does this information message occur? The deployment configuration contains references to TestStand components that

### 19440: TestStand Component Not Migrated

#### Message

The specified TestStand components were not migrated to the current version of TestStand. Verify that required components are selected in the Drivers and Components Dialog.

#### Why does this information message occur?

The deployment configuration contains references to TestStand components that do not have equivalent components in the latest TestStand version.

#### How do I resolve this information message?

In the Installers tab, select the "Drivers and Components" button to verify that the TestStand components required for the deployment are selected.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19441-teststand-component-migrated.html language=enus -->
## TOPIC 03215: 19441: TestStand Component Migrated

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19441-teststand-component-migrated.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19441-teststand-component-migrated.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The specified TestStand components were migrated from a previous version of TestStand. Verify that required components are selected in the Drivers and Components Dialog. Why does this information message occur? The deployment configuration contains references to TestStand components that hav

### 19441: TestStand Component Migrated

#### Message

The specified TestStand components were migrated from a previous version of TestStand. Verify that required components are selected in the Drivers and Components Dialog.

#### Why does this information message occur?

The deployment configuration contains references to TestStand components that have equivalent components in the latest TestStand version. These components were automatically upgraded to the current TestStand version.

#### How do I resolve this information message?

In the Installers tab, select the "Drivers and Components" button to verify that the TestStand components required for the deployment are selected.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19442-referenced-packages.html language=enus -->
## TOPIC 03216: 19442: Referenced Packages

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19442-referenced-packages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19442-referenced-packages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following dependent packages are referenced by the main package Why does this information message occur? The listed packages are referenced by the main package. If you selected the package only mode, the packages listed as required must be present on the system in order to install the pa

### 19442: Referenced Packages

#### Message

The following dependent packages are referenced by the main package

#### Why does this information message occur?

The listed packages are referenced by the main package. If you selected the package only mode, the packages listed as required must be present on the system in order to install the package. If you created a repository or package installer, refer to the build summary for a list of packages included in the distribution.

#### How do I resolve this information message?

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19443-gll-build-result.html language=enus -->
## TOPIC 03217: 19443: GLL Build Result

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19443-gll-build-result.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19443-gll-build-result.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message GLL Build Result: Why does this information message occur? When rebuilding a GLL from the LabVIEW NXG source files, LabVIEW reported the following information. How do I resolve this information message? If the build did not complete successfully, use this information to troubleshoot the issu

### 19443: GLL Build Result

#### Message

GLL Build Result:

#### Why does this information message occur?

When rebuilding a GLL from the LabVIEW NXG source files, LabVIEW reported the following information.

#### How do I resolve this information message?

If the build did not complete successfully, use this information to troubleshoot the issue.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19444-substep-modules-not-included-in-deploym.html language=enus -->
## TOPIC 03218: 19444: Substep Modules Not Included in Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19444-substep-modules-not-included-in-deploym.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19444-substep-modules-not-included-in-deploym.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following substep modules specified by step types in the deployment were not included based on the current settings. Why does this information message occur? Sequence Files in the deployment use one or more custom step types, and code modules used by the substeps in these custom step typ

### 19444: Substep Modules Not Included in Deployment

#### Message

The following substep modules specified by step types in the deployment were not included based on the current settings.

#### Why does this information message occur?

Sequence Files in the deployment use one or more custom step types, and code modules used by the substeps in these custom step types were not included in the deployment.

#### How do I resolve this information message?

If the "Output VIs to a Packed Project Library" is disabled, you can enable the "Include Module Files for LabVIEW Substeps" option to include these files in the deployment. If the "Output VIs to a Packed Project Library" option is enabled, National Instruments recommends creating a seperate packed project library to contain substep VIs, then including these packed project libraries in the deployment.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19445-substep-modules-destinations-were-chang.html language=enus -->
## TOPIC 03219: 19445: Substep Modules Destinations Were Changed

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19445-substep-modules-destinations-were-chang.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19445-substep-modules-destinations-were-chang.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The destinations for the following substep modules specified by step types in the deployment may have changed. Why does this information message occur? Code Modules for substeps defined in custom step types were included in the deployment, but the file destinations may have changed, which wi

### 19445: Substep Modules Destinations Were Changed

#### Message

The destinations for the following substep modules specified by step types in the deployment may have changed.

#### Why does this information message occur?

Code Modules for substeps defined in custom step types were included in the deployment, but the file destinations may have changed, which will cause the module paths to be invalid on a deployment computer.

#### How do I resolve this information message?

Ensure that you deploy the proper search directories to ensure that these files will be found on the deployment computer.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19446-python-virtual-directories-are-specifie.html language=enus -->
## TOPIC 03220: 19446: Python Virtual Directories are Specified in the Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19446-python-virtual-directories-are-specifie.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19446-python-virtual-directories-are-specifie.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following Python Virtual Environment Directories are specified by Python adapter steps in the deployment. Ensure that you include these directories in the deployment. Why does this information message occur? Steps which use the python adapter can optionally specify a specific virtual env

### 19446: Python Virtual Directories are Specified in the Deployment

#### Message

The following Python Virtual Environment Directories are specified by Python adapter steps in the deployment. Ensure that you include these directories in the deployment.

#### Why does this information message occur?

Steps which use the python adapter can optionally specify a specific virtual environment directory to use for execution. The Deployment Utility will detect these directories, but will not automatically include them in the deployment.

#### How do I resolve this information message?

You should include the directories specified by the message in the deployment by, for example, adding them to your workspace. Also, ensure that you deploy the directories to the same relative location to the sequence file.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/19447-required-python-interpreter-versions-de.html language=enus -->
## TOPIC 03221: 19447: Required Python Interpreter Versions Detected

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/19447-required-python-interpreter-versions-de.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/19447-required-python-interpreter-versions-de.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message The following Python Interpreter Versions are required by Python adapter steps in the deployment. Ensure that you include these versions of the interpreter in the deployment. Why does this error occur? Steps which use the Python adapter can optionally specify a specific version of the Python

### 19447: Required Python Interpreter Versions Detected

#### Message

The following Python Interpreter Versions are required by Python adapter steps in the deployment. Ensure that you include these versions of the interpreter in the deployment.

#### Why does this error occur?

Steps which use the Python adapter can optionally specify a specific version of the Python interpreter. These versions must be installed in order for the sequence file to execute.

#### How do I resolve this information message?

Ensure that the specified versions of the Python interpreter are installed on the target computer.

If the issue persists, contact National Instruments for support. Save a technical support record to send to National Instruments by selecting
 Save Technical Support Report
 from the
 Save Log
 button pull-down menu.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/general-overview-of-deployment.html language=enus -->
## TOPIC 03222: General Overview of Deployment

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/general-overview-of-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/general-overview-of-deployment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the TestStand Deployment Utility to build an installer or create an image directory you can use to deploy a test system in a production environment A deployment consists of the following phases: Analysis —During analysis, the deployment utility analyzes all the top-level files in workspaces and

### General Overview of Deployment

Use the TestStand Deployment Utility to build an installer or create an image directory you can use to deploy a test system in a production environment

A deployment consists of the following phases:

- Analysis 
 —During analysis, the deployment utility analyzes all the top-level files in workspaces and directories for the required dependencies to correctly deploy the test system.
- Build 
 —During the build process, the deployment utility packages all the top-level files and dependencies and creates a deployable image that contains all the files in the test system.
- Installer Creation 
 —During the installer creation process, the deployment utility builds an installer that includes all the specified drivers and components and all the files in the deployable image.

Parent topic:

TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand-api-reference path=tserrors/teststand-deployment-utility-messages.html language=enus -->
## TOPIC 03223: TestStand Deployment Utility Messages

- bundle_id: `teststand-api-reference`
- source_path: `tserrors/teststand-deployment-utility-messages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tserrors/teststand-deployment-utility-messages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This help file contains detailed information about the errors, warnings, and messages the TestStand Deployment Utility returns. If you open help files directly from the <TestStand> \Doc\Help directory, National Instruments recommends that you open TSHelp.chm first because this file is a collection o

### TestStand Deployment Utility Messages

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

Build Status Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/abs-function.html language=enus -->
## TOPIC 03224: Abs Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/abs-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/abs-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Abs(Number number) Return Value Number The absolute value of the number you pass.

### Abs Function

#### Syntax

Number Abs(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The absolute value of the number you pass.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/acos-function.html language=enus -->
## TOPIC 03225: ACos Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/acos-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/acos-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number ACos(Number number) Return Value Number The principal value in radians of the arc cosine of the specified argument. An indeterminate value (IND) results when the argument is not in the range [-1,1].

### ACos Function

#### Syntax

Number ACos(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The principal value in radians of the arc cosine of the specified argument. An indeterminate value (IND) results when the argument is not in the range [-1,1].

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/allof-function.html language=enus -->
## TOPIC 03226: AllOf Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/allof-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/allof-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Boolean AllOf(Boolean parameter1, Boolean parameter2, Boolean paramete3, etc.) Return Value Boolean The logical AND for any number of boolean parameters. This function uses short-circuit evaluation, i.e. if the function encounters a False parameter, the function immediately returns False with

### AllOf Function

#### Syntax

Boolean AllOf(Boolean parameter1, Boolean parameter2, Boolean paramete3, etc.)

#### Return Value

[Boolean](../tsapiref/data-types-for-teststand.html)

The logical AND for any number of boolean parameters. This function uses short-circuit evaluation, i.e. if the function encounters a False parameter, the function immediately returns False without evaluating the remaining parameters.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/anyof-function.html language=enus -->
## TOPIC 03227: AnyOf Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/anyof-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/anyof-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Boolean AnyOf(Boolean parameter1, Boolean parameter2, Boolean parameter3, etc.) Return Value Boolean The logical OR of all the parameters. This function uses short-circuit evaluation, i.e. if the function encounters a True parameter, the function immediately returns True without evaluating th

### AnyOf Function

#### Syntax

Boolean AnyOf(Boolean parameter1, Boolean parameter2, Boolean parameter3, etc.)

#### Return Value

[Boolean](../tsapiref/data-types-for-teststand.html)

The logical OR of all the parameters. This function uses short-circuit evaluation, i.e. if the function encounters a True parameter, the function immediately returns True without evaluating the remaining parameters.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/array-expression-functions.html language=enus -->
## TOPIC 03228: Array Expression Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/array-expression-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/array-expression-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following array functions in TestStand expressions: Contains FindIndex FindOffset GetArrayBounds GetNumElements IndexToOffset InsertElements OffsetToIndex RemoveElements SetArrayBounds SetElements SetNumElements Sort

### Array Expression Functions

You can use the following array functions in TestStand expressions:

- Contains
- FindIndex
- FindOffset
- GetArrayBounds
- GetNumElements
- IndexToOffset
- InsertElements
- OffsetToIndex
- RemoveElements
- SetArrayBounds
- SetElements
- SetNumElements
- Sort

Parent topic:

Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/asc-function.html language=enus -->
## TOPIC 03229: Asc Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/asc-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/asc-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Asc(String string) Return Value Number The character code value of the first character in the string.

### Asc Function

#### Syntax

Number Asc(String string)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The character code value of the first character in the string.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/asin-function.html language=enus -->
## TOPIC 03230: ASin Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/asin-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/asin-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number ASin(Number number) Return Value Number The principal value in radians of the arc sine of the specified argument. An indeterminate value (IND) results when the argument is not in the range [-1,1].

### ASin Function

#### Syntax

Number ASin(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The principal value in radians of the arc sine of the specified argument. An indeterminate value (IND) results when the argument is not in the range [-1,1].

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/atan-function.html language=enus -->
## TOPIC 03231: ATan Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/atan-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/atan-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number ATan(Number number) Return Value Number The principal value in radians of the arc tangent of the specified argument.

### ATan Function

#### Syntax

Number ATan(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The principal value in radians of the arc tangent of the specified argument.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/base-subproperties.html language=enus -->
## TOPIC 03232: Base Subproperties

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/base-subproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/base-subproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Base property contains subproperties that specify functionality common to all plug-ins. The process model uses the subproperties of the Base property to determine how to invoke plug-in entry points and other aspects of plug-in operation. The Base property includes the following subproperties. Th

### Base Subproperties

The
 Base
 property contains subproperties that specify functionality common to all plug-ins. The process model uses the subproperties of the
 Base
 property to determine how to invoke plug-in entry points and other aspects of plug-in operation.

The
 Base
 property includes the following subproperties. The data type appears in parentheses.

- Enabled 
 (Boolean)—Specifies whether the model invokes the instance of the plug-in at run time.
- DisplayNameExpression 
 (Expression)—An expression that specifies the name to display in the
 Result Processing 
 dialog box to identify the instance of the plug-in, such as
 "<Company Name> Production Database" 
 , including the quotation marks. The value is an expression so that the default value the plug-in defines can refer to localized text using the
 ResStr 
 expression function. You can edit the text in the Output Name column of the Result Processing dialog box.
- NewThread 
 (Boolean)—Specifies whether the plug-in performs some operations in a separate thread.
- UseDefaultNewThreadImplementation 
 (Boolean)—Specifies whether the process model automatically calls the
 Model Plugin – UUT Done 
 and
 Model Plugin – Batch Done 
 entry points in a new thread when the
 NewThread 
 property is
 True 
 . Set this property to
 False 
 if the plug-in provides its own implementation for processing in a new thread when the
 NewThread 
 property is
 True 
 .
- OnTheFlyDisablesNewThread 
 (Boolean)—Specifies that the value of the
 NewThread 
 property is implicitly considered False when the
 ProcessOnTheFly 
 property is
 True 
 .
- CompleteBeforeNextUUT 
 (Boolean)—Specifies whether the
 ModelSupport.seq 
 file waits for the Post UUT thread of the process model plug-in to complete before calling any further entry points for the current execution except for the Post UUT entry points of other result processors.
- ProcessOnTheFly 
 (Boolean)—Specifies whether the process model calls the
 Model Plugin – OnTheFly Step Results 
 entry point.
- CanProcessOfflineOnTheFlyResults 
 (Boolean)—Indicates whether the plug-in can process an offline results file written on-the-fly. Set this property to
 False 
 for plug-ins that do not use the OnTheFly Step Results entry point or that access the
 Step 
 or
 Context 
 parameters within that entry point. The entry point must not access the
 Step 
 or
 Context 
 parameters because TestStand does not pass any data to these parameters when processing data from an offline results file.
- CanProcessOfflineResultsTree 
 (Boolean)—Indicates whether the plug-in can process an offline results file that was not written on-the-fly. A value of
 True 
 indicates that the UUT Done and
 Model Plugin – Post UUT 
 entry points completely process the results without requiring a call to the OnTheFly Step Results entry point.
- OptionsDescriptionExpression 
 (Expression)—The result of the expression evaluation is the text you want to display to summarize the option settings in a configuration dialog box. Use the
 ModelPlugin 
 prefix to access the properties of the plug-in instance in the expression. For example, you could use the following expression to display the path of a plug-in-specific output directory:
 "My plug-in stores its output files at: " + ModelPlugin.PluginSpecific.Options.MyPluginOutputPath
- SequenceFileName 
 (String)—The process model sets this property to the filename of the sequence file that implements the instance of the plug-in. The filename is relative to the enclosing
 ModelPlugins 
 directory.
- IconName 
 (String)—Set this property to the name of an icon that represents the instance of the plug-in. The leftmost column of the Result Processing dialog box displays this icon. The icon name must be a valid argument to the
 Images.FindImage 
 method.
- GUID 
 (String)—A string that uniquely identifies the instance of the plug-in.
- AlwaysInitialize 
 (Boolean)—If this property is
 True 
 , the process model calls the
 Model Plugin – Initialize 
 entry point and the
 ModelPluginOptions 
 callback for the plug-in even when the
 Enabled 
 property is
 False 
 . The entry point and callback can set the
 Enabled 
 property to
 True 
 . This option adds overhead for a disabled plug-in instance because the process model must load the plug-in sequence file at run time.
- RequiresBatchControllerAndSocketSynchronization 
 (Boolean)—If this property is
 True 
 , the Batch process model allows the plug-in instance to perform
 controller and socket 
 synchronization 
 between the
 Model Plugin – Batch Start 
 and
 Model Plugin – UUT Start 
 entry points and between the Batch Done and UUT Done entry points. This property is
 True 
 by default. If you do not require controller and socket synchronization, setting this property to
 False 
 can slightly improve performance when executing the Batch process model.
- RunOrder 
 (Number)—If the
 RunOrder 
 properties of two plug-in instances are not equal, the process model invokes entry points on the plug-in with the lower
 RunOrder 
 value first.
- RuntimeVariables 
 (NI_ModelPluginRuntimeVariables)—Variables the process model updates to control and indicate the execution state of the instance of the plug-in.
- AutoAddToConfigurations 
 (Boolean)—Specifies whether TestStand automatically adds an instance of a new plug-in to existing configurations. Refer to
 Automatically Adding or Removing a Plug-In File to or from Configurations 
 for more information.

Parent topic:

NI_ModelPlugin

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/cantranslate.html language=enus -->
## TOPIC 03233: CanTranslate

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/cantranslate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/cantranslate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: long CanTranslate(const char *extension, IDispatch *inputStream, long *index, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes) Purpose Determines whether a translator in the DLL can translate the file the extension and inputStream parameters specify and returns the index of the tra

### CanTranslate

long CanTranslate(const char *extension, IDispatch *inputStream, long *index, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes)

#### Purpose

Determines whether a translator in the DLL can translate the file the
 extension
 and
 inputStream
 parameters specify and returns the index of the translator that can translate the file.

Note

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| extension | string | The extension of the file TestStand attempts to open. The extension parameter does not include the period ( "." ) character in the extension string. |
| inputStream | InputStream | A reference to an InputStream object that contains the contents of the file TestStand attempts to open. |
| index | long | Returns the zero-based index of the translator that can translate the file. |
| errorCode | TSERROR | Returns the error code when an error occurs in the callback. |
| errorMsg | string | Returns the error message when an error occurs in the callback. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxErrorMsgLengthInBytes parameter to determine the size of the buffer. |
| maxErrorMsgLengthInBytes | long | The maximum number of bytes the DLL can copy to the errorMsg parameter. |

#### Return Value

Returns whether a translator in the DLL can translate the file. A value of
 0
 indicates that the translator cannot translate the file. A value of
 1
 indicates that the translator can translate the file.

When CanTranslate returns a non-zero value for the
 error
 parameter, TestStand reports an error and does not attempt to call CanTranslate for other sequence file translator DLLs on the computer. National Instruments recommends that translators catch errors that occur while attempting to determine whether the translator can load the file and return
 0
 from CanTranslate.

Parent topic:

Sequence File Translator Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/categoryspecific-subproperties.html language=enus -->
## TOPIC 03234: CategorySpecific Subproperties

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/categoryspecific-subproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/categoryspecific-subproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The CategorySpecific property provides a location for related plugs-ins to store information common to all plug-ins within a category. You do not need to edit the CategorySpecific property unless you are developing a set of related plug-ins that store common properties to support behavior that all p

### CategorySpecific Subproperties

The
 CategorySpecific
 property provides a location for related plugs-ins to store information common to all plug-ins within a category. You do not need to edit the
 CategorySpecific
 property unless you are developing a set of related plug-ins that store common properties to support behavior that all plug-ins in the category share.

The
 CategorySpecific
 property includes the following subproperties. The data type appears in parentheses.

- Name 
 (String)—Specifies the category to which the plug-in belongs. Plug-ins with the same case-insensitive name belong to the same category. Code that implements category-specific functionality can inspect this field to determine the category of the plug-in.
 Note 
 Typically, you should avoid using a value of empty string as it will match against any name.
- Settings 
 (
 <company prefix>_<category name> 
 CategorySettings)—The specific data type of category settings defines the option properties common to plug-ins in a category.

The built-in reporting, database, and offline results plug-ins set the
 CategorySpecific.Name
 property to
 ResultProcessor
 and set the data type of the
 CategorySpecific.Settings
 property to
 NI_ResultProcessorCategorySettings
 . You must use these values for a plug-in to appear in the
 [Result Processing](../tsref/result-processing-dialog-box.html)
 dialog box. TestStand uses these default values for any plug-in you create from within the Result Processing dialog box.

The NI_ResultProcessorCategorySettings data type has two Boolean subproperties:

- CanDisplayReport 
 —Specifies whether the Result Processing dialog box provides a checkbox for the process model plug-in instance in the Display column.
- DisplayReport 
 —Specifies whether the report for the process model plug-in instance displays as the active report. The checkbox in the Display column of the Result Processing dialog box sets this property.If DisplayReport is false for a plug-in instance, the instance should allocate a new report for its use in the
 Runstate.Execution.Reports 
 collection. If DisplayReport is true, the plug-in instance should adopt the default report for its own use by storing the value of
 Runstate.Execution.Reports.ActiveReport 
 in a plug-in run-time variable in the Model Plugin-Begin entry point and use then that report. If a plug-in does not generate both controller and socket reports and DisplayReport is false, it should not allocate a report for executions in which it does not generate reports. If DisplayReport is true, it should call
 Execution.Reports.Remove 
 to delete the default report in the executions for which is does not generate reports. Plugins that generate reports in separate threads should allocate a new report for each UUT/Batch in Model Plugin-UUT Start and Model Plugin-Batch Start

Parent topic:

NI_ModelPlugin

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/checklimits-function.html language=enus -->
## TOPIC 03235: CheckLimits Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/checklimits-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/checklimits-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String CheckLimits(Number value, Number high, Number low, String comparisonType, Boolean doNotCopyToResults = True, Number nominal = 0, String thresholdType = "") Return Value String "Passed" if the value is within the limits or if the comparison type is LOG. Returns "Failed" otherwise. Purpo

### CheckLimits Function

#### Syntax

String CheckLimits(Number value, Number high, Number low, String comparisonType, Boolean doNotCopyToResults = True, Number nominal = 0, String thresholdType = "")

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

"Passed" if the value is within the limits or if the comparison type is LOG. Returns "Failed" otherwise.

#### Purpose

This function evaluates whether a value is within the specified limits

#### Parameters

value
 as
 [Number](../tsapiref/data-types-for-teststand.html)

A number to compare against limits.

high
 as
 [Number](../tsapiref/data-types-for-teststand.html)

A number that specifies the upper limit.

low
 as
 [Number](../tsapiref/data-types-for-teststand.html)

A number that specifies the lower limit.

comparisonType
 as
 [String](../tsapiref/data-types-for-teststand.html)

Specifies how to compare the value against the limits. The valid values are EQ, NE, GT, LT, GE, LE, GTLT, GELE, GELT, GTLE, LTGT, LEGE, LTGE, LEGT and LOG. The comparisons are identical to the corresponding comparisons of the Numeric Limit Test step.

doNotCopyToResults
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Pass True to set the DontCopyToResults property flag on the properties you pass to the high and low arguments that are not used in the comparison. This default is True.

nominal
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) A number that specifies the nominal value. This parameter is used only with the
 EQT (==+/-)
 comparison type.

thresholdType
 as
 [String](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies how to compute the upper and lower limits for the
 EQT (==+/-)
 comparison type. The valid values are PERCENTAGE, PPM, and DELTA. The threshold types are identical to the corresponding
 [threshold types](../tsref/limits-tab-numeric-limit-test-edit-tabs.html)
 of the Numeric Limit Test step.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/checkstrlimit-function.html language=enus -->
## TOPIC 03236: CheckStrLimit Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/checkstrlimit-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/checkstrlimit-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String CheckStrLimit(String stringA, String stringB, String comparisonType, Number maxChars = -1) Return Value String "Passed" if the comparison indicates that the strings match or if the Comparison Type is "LOG". "Failed" if otherwise. Purpose This function compares two strings or a string a

### CheckStrLimit Function

#### Syntax

String CheckStrLimit(String stringA, String stringB, String comparisonType, Number maxChars = -1)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

"Passed" if the comparison indicates that the strings match or if the Comparison Type is "LOG". "Failed" if otherwise.

#### Purpose

This function compares two strings or a string against a regular expression pattern using the comparison type you specify.

#### Parameters

stringA
 as
 [String](../tsapiref/data-types-for-teststand.html)

The first string to compare.

stringB
 as
 [String](../tsapiref/data-types-for-teststand.html)

The second string or pattern to compare.

Note

Microsoft documentation for regular expressions

comparisonType
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string that specifies how to compare the strings. The valid values are "LOG", "IgnoreCase", "CaseSensitive", "RegularExpressionIgnoreCase", and "RegularExpressionCaseSensitive".

maxChars
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) A number that specifies the maximum number of characters to compare. Pass -1 to compare all characters. The default is -1. For Regular Expression cases, it matches the first maxChars characters of the string to the given pattern.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/chr-function.html language=enus -->
## TOPIC 03237: Chr Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/chr-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/chr-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String Chr(Number number) Return Value String A string containing the character with the specified character code.

### Chr Function

#### Syntax

String Chr(Number number)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string containing the character with the specified character code.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/commentof-function.html language=enus -->
## TOPIC 03238: CommentOf Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/commentof-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/commentof-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String CommentOf(PropertyObject propertyObject) Return Value String The comment for a propertyObject. Parameters propertyObject as PropertyObject A property object (String, Number, Container, etc.).

### CommentOf Function

#### Syntax

String CommentOf(PropertyObject propertyObject)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The comment for a propertyObject.

#### Parameters

propertyObject
 as
 [PropertyObject](../tsapiref/propertyobject.html)

A property object (String, Number, Container, etc.).

Parent topic:

Property Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/contains-function.html language=enus -->
## TOPIC 03239: Contains Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/contains-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/contains-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Boolean Contains(Array array, PropertyObject object, Boolean caseSensitive = True) Return Value Boolean If found, returns True. If not found, returns False. Purpose This function returns True if the specified object or value is found in the array. Note: To find the location of the object or v

### Contains Function

#### Syntax

Boolean Contains(Array array, PropertyObject object, Boolean caseSensitive = True)

#### Return Value

[Boolean](../tsapiref/data-types-for-teststand.html)

If found, returns True. If not found, returns False.

#### Purpose

This function returns True if the specified object or value is found in the array. Note: To find the location of the object or value, use the FindIndex or FindOffset functions to obtain the array index string (e.g. "[0][1]") or the offset value, respectively.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

An array to search.

object
 as
 [PropertyObject](../tsapiref/propertyobject.html)

Value to be searched.

caseSensitive
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

For string arrays, pass True to use a case-sensitive comparison.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/convertcolor-function.html language=enus -->
## TOPIC 03240: ConvertColor Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/convertcolor-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/convertcolor-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number ConvertColor(Number color) Return Value Number The color value converted to the opposite format. Purpose This function converts between the big-endian and little-endian color value formats. Color values are stored as four-byte integers expressed in one of two common formats: little-end

### ConvertColor Function

#### Syntax

Number ConvertColor(Number color)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The color value converted to the opposite format.

#### Purpose

This function converts between the big-endian and little-endian color value formats. Color values are stored as four-byte integers expressed in one of two common formats: little-endian and big-endian. Windows and ActiveX use the little-endian format, while LabVIEW and LabWindows/CVI use the big-endian format. The little-endian format stores red, green, and blue color components in the form 0x00BBGGRR. The big-endian format stores the color components in the form 0x00RRGGBB.

#### Parameters

color
 as
 [Number](../tsapiref/data-types-for-teststand.html)

A numeric color value.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/cos-function.html language=enus -->
## TOPIC 03241: Cos Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/cos-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/cos-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Cos(Number number) Return Value Number The cosine of the number (where the number is measured in radians). To convert from degrees to radians, multiply degrees by (PI/180).

### Cos Function

#### Syntax

Number Cos(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The cosine of the number (where the number is measured in radians). To convert from degrees to radians, multiply degrees by (PI/180).

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/currentuserhasprivilege-function.html language=enus -->
## TOPIC 03242: CurrentUserHasPrivilege Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/currentuserhasprivilege-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/currentuserhasprivilege-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Boolean CurrentUserHasPrivilege(String privilegeName) Return Value Boolean True if the current user has the privilege or if user privilege checking is disabled. Returns False otherwise. Purpose This function returns True if the current user has the privilege you specify. Parameters privilegeN

### CurrentUserHasPrivilege Function

#### Syntax

Boolean CurrentUserHasPrivilege(String privilegeName)

#### Return Value

[Boolean](../tsapiref/data-types-for-teststand.html)

True if the current user has the privilege or if user privilege checking is disabled. Returns False otherwise.

#### Purpose

This function returns True if the current user has the privilege you specify.

#### Parameters

privilegeName
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string containing the name of the privilege. Pass "*" to determine if a user is currently logged in.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/date-function.html language=enus -->
## TOPIC 03243: Date Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/date-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/date-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String Date(Boolean longFormat = False, [Out] [Number year], [Out] [Number month], [Out] [Number monthDay], [Out] [Number weekDay], [Number timeStampInSeconds], [Boolean baseTimeIsInitTime]) Return Value String A string containing the current date in localized format. Purpose This function re

### Date Function

#### Syntax

String Date(Boolean longFormat = False, [Out] [Number year], [Out] [Number month], [Out] [Number monthDay], [Out] [Number weekDay], [Number timeStampInSeconds], [Boolean baseTimeIsInitTime])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string containing the current date in localized format.

#### Purpose

This function returns the current date.

#### Parameters

longFormat
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Pass True to return the date in long format (the default is False).

year
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional output) Containing the current year.

month
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional output) The current month (from 1 to 12).

monthDay
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional output) The day of the month (from 1 to 31).

weekDay
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional output) The day of the week (from 1 (Sunday) to 7 (Saturday)).

timeStampInSeconds
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) A timestamp the function uses in place of the current time. Pass a time value you obtain from the expression function Seconds().

baseTimeIsInitTime
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the base time for the timestamp you pass to parameter 6. Pass True if the base time is the time at which the application initialized the TestStand Engine. Pass False if the base time is midnight, January 1, 1970, universal coordinated time (UTC). UTC is also known as Greenwich mean time (GMT).

Parent topic:

Time Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/delocalizeexpression-function.html language=enus -->
## TOPIC 03244: DelocalizeExpression Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/delocalizeexpression-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/delocalizeexpression-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String DelocalizeExpression(String localizedExpressionString, Number decimalPointOption = 1) Return Value String A string containing the delocalized expression. Purpose This function converts a localized expression string to a standard form that is suitable for evaluation. TestStand requires

### DelocalizeExpression Function

#### Syntax

String DelocalizeExpression(String localizedExpressionString, Number decimalPointOption = 1)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string containing the delocalized expression.

#### Purpose

This function converts a localized expression string to a standard form that is suitable for evaluation. TestStand requires expressions that it evaluates through the Evaluate expression function or the Evaluate API method to be in a standard non-localized form so that the result of the evaluation does not depend on the localization settings of your computer. Call this function to delocalize expressions you obtain from user input. The function replaces the localized decimal point characters that represent decimal points in the expression with the period character. If the localized decimal point character is the comma character, the function also replaces semicolons that represent argument separators or expression separators with commas. The function does not change characters inside string constants.

#### Parameters

localizedExpressionString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The localized expression string to convert.

decimalPointOption
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies how the function determines which character it assumes that the localized expression uses for the localized decimal point. The valid values are:     1 - (default) Use the Station Options localization preferences to determine whether to use the operating system setting.     2 - Use the operating system setting.     3 - Use the period character.     4 - Use the comma character

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/enum-function.html language=enus -->
## TOPIC 03245: Enum Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/enum-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/enum-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Enum(String enumType, [String/Number value]) Return Value Enumeration An enumeration with the specified type and value. Purpose Create an enumeration with the specified type and value. If the optional value is not specified, the returned enumeration has the default value. Parameters enumType

### Enum Function

#### Syntax

Enum(String enumType, [String/Number value])

#### Return Value

Enumeration

An enumeration with the specified type and value.

#### Purpose

Create an enumeration with the specified type and value.

Note

#### Parameters

enumType
 as
 [String](../tsapiref/data-types-for-teststand.html)

Specifies the type of enumeration to create.

value
 as
 [String](../tsapiref/data-types-for-teststand.html)
 or
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the value of the enumeration as a string or number. The value will be coerced to the specified enumeration data type.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/evaluate-function.html language=enus -->
## TOPIC 03246: Evaluate Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/evaluate-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/evaluate-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax PropertyObject Evaluate(String string) Return Value PropertyObject The result of evaluating the expression. Purpose This function returns the value of an expression you specify in a string. Parameters string as String The expression to evaluate. Note: You must escape any special characters in

### Evaluate Function

#### Syntax

PropertyObject Evaluate(String string)

#### Return Value

[PropertyObject](../tsapiref/data-types-for-teststand.html)

The result of evaluating the expression.

#### Purpose

This function returns the value of an expression you specify in a string.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

The expression to evaluate. Note: You must escape any special characters in your expression string. Refer to the Special String Characters Help topic for more information.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/exp-function.html language=enus -->
## TOPIC 03247: Exp Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/exp-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/exp-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Exp(Number x) Return Value Number The numeric constant e raised to the x power.

### Exp Function

#### Syntax

Number Exp(Number x)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The numeric constant e raised to the x power.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/expression-functions.html language=enus -->
## TOPIC 03248: Expression Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/expression-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/expression-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following types of expression functions in TestStand: Array Numeric Property String Switching Time Other

### Expression Functions

You can use the following types of expression functions in TestStand:

- Array
- Numeric
- Property
- String
- Switching
- Time
- Other

Parent topic:

Operators/Functions Tab - Expression Browser Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/find-function.html language=enus -->
## TOPIC 03249: Find Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/find-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/find-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Find(String string, String stringToSearchFor, Number indexToSearchFrom = 0, Boolean ignoreCase = False, Boolean searchInReverse = False) Return Value Number The zero-based character index, starting at the beginning of the string, of the first character in the substring. The function re

### Find Function

#### Syntax

Number Find(String string, String stringToSearchFor, Number indexToSearchFrom = 0, Boolean ignoreCase = False, Boolean searchInReverse = False)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The zero-based character index, starting at the beginning of the string, of the first character in the substring. The function returns -1 if it does not find the substring.

#### Purpose

This function searches a string for a substring.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string.

stringToSearchFor
 as
 [String](../tsapiref/data-types-for-teststand.html)

The substring to find.

indexToSearchFrom
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) the zero-based character index at which to begin searching. The default is 0.

ignoreCase
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Pass True to ignore character case when searching. The default is False.

searchInReverse
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Pass True to search the string in reverse. The default is False. If you search in reverse, the index to search from that you pass to parameter 3 is zero-based with respect to the last character in the string. The return value remains zero-based with respect to the first character in the original non-reversed string.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/findfile-function.html language=enus -->
## TOPIC 03250: FindFile Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/findfile-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/findfile-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Boolean FindFile(String fileToFind, Boolean useCurSeqFileDir = True, [String PathToFile], Number promptFlag = 1, Number searchFlag = 1, [Out] [Boolean canceled], Boolean isCommand = False) Return Value Boolean True if the file is found, False otherwise. Purpose This function attempts to locat

### FindFile Function

#### Syntax

Boolean FindFile(String fileToFind, Boolean useCurSeqFileDir = True, [String PathToFile], Number promptFlag = 1, Number searchFlag = 1, [Out] [Boolean canceled], Boolean isCommand = False)

#### Return Value

[Boolean](../tsapiref/data-types-for-teststand.html)

True if the file is found, False otherwise.

#### Purpose

This function attempts to locate the file you specify in the TestStand search directories.

#### Parameters

fileToFind
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string containing the name of the file to search for.

useCurSeqFileDir
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Pass True to search the current sequence file directory (if any). Default value is True.

PathToFile
 as
 [String](../tsapiref/data-types-for-teststand.html)

(Optional output) The full path to the file, if the file is found. If the file is not found, this parameter contains an empty string

promptFlag
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies whether to prompt the user for the location of the file if it cannot be found in the search directories. The valid values are:     1 - (default) Use the engine's configuration option to determine whether to prompt the user.     2 - Prompt the user.     3 - Do not prompt the user.

searchFlag
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the behavior of the "Add Directory to Search Directory List" check box, if you choose to prompt the user. The valid values are:     1 - (default) Undim the checkbox, thereby allowing the user to decide whether to append the directory that contains the file to the list of search directories, if the current user has configure engine privileges.     2 - Dim the checkbox in the enabled state if the current user has configure engine privileges.     3 - Dim the checkbox in the disabled state.     4 - Same as 1 but does not check user privileges.     5 - Same as 2 but does not check user privileges.

canceled
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional output) whether the user cancelled the search for the file.

isCommand
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies whether the file is a command. If you pass true and fileToFind has no file extension then FindFile searches for files with the same basename that end in the common command extensions: .exe, .com, and .bat. If the file is not found in the search directories, FindFile searches the registry for registered applications. The default is False.

Parent topic:

Other Expression Functions
