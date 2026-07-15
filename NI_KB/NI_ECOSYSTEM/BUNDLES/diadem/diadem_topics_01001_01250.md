# NI DOCUMENT BUNDLE: diadem

<!--NI_BUNDLE_CHUNK bundle=diadem start=1001 end=1250 -->
<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_file_extensions.htm language=enus -->
## TOPIC 01001: Filename Extensions in DIAdem

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_file_extensions.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_file_extensions.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > [Basic Information](../genshell/genshell_basciinformation_overview.htm) > Filename Extensions in DIAdem

Filename Extensions in DIAdem

Overview of the most important filename extensions in DIAdem:

| Filename extension | Meaning |
| --- | --- |
| anp | Specifies an Analysis automation procedure in SystemLink TDM. |
| asc | Specifies a file in the ASCII format. |
| atf | Specifies a file in the ASAM Transport Format (ASCII). |
| atfx | Specifies a file in the ASAM Transport Format (XML). |
| bdn | Specifies a bar definition that you configure via the Bar manager interface. |
| bdy | Specifies a Deployment file of a bar definition. |
| dat | Specifies a data file in the DAT format. |
| ddd | Specifies a Desktop file. |
| dfc | Specifies a DataFinder configuration. |
| dpp | Specifies a Data preparation procedure in SystemLink TDM. |
| llb | Specifies a LabVIEW library with VIs. |
| lvm | Specifies a LabVIEW file. |
| mme | Specifies a file in the Multimedia Data Exchange Format for Impact Tests ISO-TS 13499. |
| msc | Specifies a MathScript file. |
| par | Specifies a Parameter file. |
| r64 | Specifies a file with data in the 8 byte Word format (64 bit). |
| stp | Specifies a configuration file for a DataPlugin or for the Browse Path of the ASAM Data Service. |
| suc | Specifies an encrypted user dialog box file (SUD file). |
| sud | Specifies a User dialog box file. |
| tbs | Specifies a file with Browse Settings. |
| tca | Specifies a file with Calculations. |
| tcc | Specifies a file with settings for the Bus Log Converter. |
| tdl | Specifies a Loading configuration. |
| tdm | Specifies a data file in TDM format. |
| tdms | Specifies a data file in TDMS format. |
| tdms_index | Specifies a file with header information of a TDM file. |
| tdp | Specifies a file with Context parameters of a data store. |
| tdq | Specifies a query in a DataFinder or a Data store. |
| tdr | Specifies a layout file in DIAdem REPORT. |
| tdrm | Specifies a Master layout in DIAdem REPORT. |
| tdrz | Specifies a compressed layout file in DIAdem REPORT. |
| tdv | Specifies a layout file in DIAdem VIEW. |
| tdx | Specifies a binary file with the numeric data of a TDM file. |
| tpr | Specifies the Template for custom properties. |
| tuc | Specifies the Units catalog. |
| urf | Specifies the configuration for a Data instance. |
| uri | Specifies the configuration for a DataPlugin. |
| urs | Specifies the configuration for a Data store. |
| vas | Specifies a definition file for user variables. |
| vbc | Specifies an encrypted user script file (VBS file). |
| vbs | Specifies a Script file. |
| vbsa | Specifies an Analysis script file of an analysis automation procedure in SystemLink TDM. |
| vbsd | Specifies a DataPlugin script file. |
| vbsp | Specifies a script file of the Data preparation. |
| vi | Specifies a virtual LabVIEW instrument. |

<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_generalabort.htm language=enus -->
## TOPIC 01002: Abort and Error Behavior of Commands, Scripts, or User Dialog Boxes

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_generalabort.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_generalabort.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > [Basic Information](../genshell/genshell_basciinformation_overview.htm) > Abort and Error Behavior of Commands, Scripts, or User Dialog Boxes

Abort and Error Behavior of Commands, Scripts, or User Dialog Boxes

#### Abort Behavior

You can press the <Esc> button to cancel interactive commands, scripts, or user dialog boxes in DIAdem. If you press the <Esc> button to abort interactively called DIAdem commands such as the loading of a file or the execution of a calculation, DIAdem terminates the action with a message. If a script calls these commands, DIAdem displays an error message after you press the <Esc> button. You can use the [Err object](../../vbs/objects/vbs_objects_errobj.htm) to handle this error. You also can press <Esc> to abort scripts which you started with [ScriptStart](../../comoff/scriptstart.htm). DIAdem reports an error to the calling script.

If a DIAdem dialog box is open, pressing the <Esc> key is the same as clicking the **Cancel** button. This also applies to a user dialog box that is not executing a script. Pressing the <Esc> key is the same as clicking the [Cancel](../../sudref/methods/sud_method_cancel_tosudviewobint.htm) button. DIAdem closes the user dialog box and triggers the [EventTerminate()](../../sudref/events/sud_event_eventterminate.htm) event if this event is defined.

However you cannot use <Esc> to abort user commands, active scripts within user dialog boxes, or scripts that are integrated into user dialog boxes with [ScriptInclude](../../comoff/scriptinclude.htm). You can use the [IsEscKeyPressed](../../comoff/isesckeypressed.htm) command to react to pressing <Esc> and, for example, use the [Exit statement](../../vbs/general/vbs_exit.htm) to terminate the user command. You also can integrate scripts in user commands and user dialog boxes with ScriptStart and use <Esc> to abort these scripts.

If you set the [AutoAbort](../../varoff/autoabort.htm) variable to FALSE, scripts do not abort when <Esc> is pressed. In script sections where errors may occur unexpectedly, for example, opening a file, you can suppress these errors with [On Error Resume Next](../../vbs/general/vbs_onerror.htm) and use the Err object to handle the errors.

In nested user dialog boxes, use the dialog box property [EscapeMode](../../sudref/properties/sud_property_escapemode_tosudviewobint.htm) to suppress cancellation with <Esc>.

#### Examples

The following example shows how you can use the Dialog.EscapeMode property to prevent the main dialog box from being cancelled when the <Esc> button is pressed:

[Copy script](javascript:void(0);)

```text
Sub Dialog_EventInitialize()
Dim This : Set This = Dialog
    Dialog.EscapeMode = 0
End Sub
```

The following example shows how you prevent the calling dialog box from aborting when the <Esc> button is pressed and held. The user must release the <Esc> button before he can cancel the procedure on the next dialog box level:

[Copy script](javascript:void(0);)

```text
Dialog.EscapeMode = 0
Call SudDlgShow("SubDlg","MyDialog.SUD")
While IsESCKeyPressed()
  'Wait for release ESC button
Wend
Dialog.EscapeMode = 1
```

The following example shows how you can use ScriptStart to integrate your script, which is part of a user dialog box, or a user command into another script. You can use the <Esc> button to cancel the integrated script. If the integrated script is cancelled, the calling script handles the error that occurs.

[Copy script](javascript:void(0);)

```text
Sub MyEvent
  On Error Resume Next 'Enables error handling
  Call ScriptStart("MyLongEvaluation.vbs")
  If Err.Number <> 0 Then
    Call MsgBoxDisp ("Error # " & CStr(Err.Number) & " " & Err.Description)
    Err.Clear   ' Clear the error.
    If MsgBoxDisp ("Cancel Evaluation?", "MB_OKCANCEL") = "IDCancel" Then
      Exit Sub
    End If
  End If
  On Error Goto 0 'Disables error handling
'...
End Sub
```

#### Error behavior

If an error occurs in the constructor [Class_Initialize](../../vbs/general/vbs_class_constructor.htm) method, DIAdem does not abort the script, it continues running the script. DIAdem reacts exactly the same as Microsoft Windows Scripting Host.

If you debug a script and terminate the script either with the <ESC> key or with the respective symbol on the toolbar, DIAdem continues executing the destructor [Class_Terminate](../../vbs/general/vbs_class_constructor.htm) method.

|  | Note Refer to Err object and the linked pages for information on error handling. Refer to Error Handling in Scripts for an example of error handling that you can run. DIAdem generally records errors in the Logfile. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_generalevents.htm language=enus -->
## TOPIC 01003: Working with Events in DIAdem

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_generalevents.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_generalevents.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > [Basic Information](../genshell/genshell_basciinformation_overview.htm) > Working with Events in DIAdem

Working with Events in DIAdem

Events occur in DIAdem as soon as you execute a specific action. In DIAdem NAVIGATOR an event occurs, for example, when you search for files or load files. In DIAdem VIEW an event occurs, for example, when you move the cursor.

If an event occurs, you can call a [user command](../../procauto/procauto/procauto_usercommand.htm) in order to manipulate data. Observe the following rules to prevent errors when DIAdem executes user commands after events:

**General rules**

- Do not use the InteractionOn command, which enables an interaction, in the requested user command.
- If you do not delete the groups and the channels in the requested user command, DIAdem receives all the groups and channels created in this user command after the event has run.
- Use the AddUserCommandToEvent command to assign several user commands to one event. Use the RemoveUserCommandFromEvent command to delete a single user command from a list of user commands which you assigned to an event .

**Rules for the curve transformation and the event****OnCursorChanged**

- Do not change the internally assigned numbers of the loaded channels in the user command. Do not use the ChnRenumber command for renumbering channels. Do not use commands for deleting or inserting channels such as ChnDel , GroupDel , or ChnClpPaste . Do not use GroupDefaultSet to change the default group.
- Do not access internal channels and do not change the contents of internal channels in the requested user command. Usually internal channels only exist during the runtime of an event. Use the ChnIsIntern command to specify whether a channel is an internal channel.
- The channel number and the group index might have different numbers during the runtime of an event than after the event.

#### Events in DIAdem NAVIGATOR

DIAdem NAVIGATOR contains the [Events](../../scriptnavi/objects/navigator_objects_ievents.htm) object. The Events object provides the user commands assigned to an event in DIAdem NAVIGATOR. The Navigator provides the following events:

[OnAllowSearch](../../scriptnavi/events/navigator_event_onallowsearch.htm): DIAdem NAVIGATOR triggers the event OnAllowSearch before a search with a DataFinder runs. The event starts the user command that you assigned to the property Navigator.Events.[OnAllowSearch](../../scriptnavi/properties/navigator_property_onallowsearch_ievents.htm).

[OnSearched](../../scriptnavi/events/navigator_event_onsearched.htm): DIAdem NAVIGATOR triggers the event OnSearched after a search with a DataFinder has run. The event starts the user command that you assigned to the property Navigator.Events.[OnSearched](../../scriptnavi/properties/navigator_property_onsearched_ievents.htm).

[OnShowingContextMenu](../../scriptnavi/events/navigator_event_onshowingcontextmenu.htm): DIAdem NAVIGATOR triggers the OnShowingContextMenu event when a context menu is displayed in the search results list or in the browser. The event starts the user command that you assigned to the property Navigator.Events.[OnShowingContextMenu](../../scriptnavi/properties/navigator_property_onshowingcontextmenu_ievents.htm).

[OnContextMenuPointSelected](../../scriptnavi/events/navigator_event_oncontextmenupointselected.htm): DIAdem NAVIGATOR triggers the OnContextMenuPointSelected event when a context menu is selected in the search results list or in the browser. The event starts the user command that you assigned to the property Navigator.Events.[OnContextMenuPointSelected](../../scriptnavi/properties/navigator_property_oncontextmenupointselected_ievents.htm).

[OnDataProviderOpened](../../scriptnavi/events/navigator_event_ondataprovideropened.htm): DIAdem NAVIGATOR triggers the OnDataProviderOpened event before a DataFinder or a data store is opened. The event starts the user command that you assigned to the property Navigator.Events.[OnDataProviderOpened](../../scriptnavi/properties/navigator_property_ondataprovideropened_ievents.htm).

[OnDataProviderClosing](../../scriptnavi/events/navigator_event_ondataproviderclosing.htm): DIAdem NAVIGATOR triggers the OnDataProviderClosing event before a DataFinder or a data store are closed. The event starts the user command that you assigned to the property Navigator.Events.[OnDataProviderClosing](../../scriptnavi/properties/navigator_property_ondataproviderclosing_ievents.htm). 
 
[OnFileLoading](../../scriptnavi/events/navigator_event_onfileloading.htm): DIAdem NAVIGATOR triggers the OnFileLoading event before data is loaded from a file. The event starts the user command that you assigned to the property Navigator.Events.[OnFileLoading](../../scriptnavi/properties/navigator_property_onfileloading_ievents.htm).

[OnDataStoreLoading](../../scriptnavi/events/navigator_event_ondatastoreloading.htm): DIAdem NAVIGATOR triggers the OnDataStoreLoading event before data is loaded from a data store. The event starts the user command that you assigned to the property Navigator.Events.[OnDataStoreLoading](../../scriptnavi/properties/navigator_property_ondatastoreloading_ievents.htm).

[OnDataStoreSaving](../../scriptnavi/events/navigator_event_ondatastoresaving.htm): DIAdem NAVIGATOR triggers the OnDataStoreSaving event before data is saved from a data store. The event starts the user command that you assigned to the property Navigator.Events.[OnDataStoreSaving](../../scriptnavi/properties/navigator_property_ondatastoresaving_ievents.htm).

[OnLoaded](../../scriptnavi/events/navigator_event_onloaded.htm): DIAdem NAVIGATOR triggers the OnLoaded event after data is loaded. The event starts the user command that you assigned to the property Navigator.Events.[OnLoaded](../../scriptnavi/properties/navigator_property_onloaded_ievents.htm).

[OnInteractionLoading](../../scriptnavi/events/navigator_event_oninteractionloading.htm): DIAdem NAVIGATOR triggers the OnInteractionLoading event before a command called by drag and drop is executed. The event starts the user command which you assigned to the property Navigator.Events.[OnInteractionLoading](../../scriptnavi/properties/navigator_property_oninteractionloading_ievents.htm).

[OnInteractionLoaded](../../scriptnavi/events/navigator_event_oninteractionloaded.htm): DIAdem NAVIGATOR triggers the OnInteractionLoaded event after a command called by drag and drop is completed. The event starts the user command which you assigned to the property Navigator.Events.[OnInteractionLoaded](../../scriptnavi/properties/navigator_property_oninteractionloaded_ievents.htm).

#### Data Portal Events

The Data Portal contains the [Events](../../portal/objects/diacmpnt_objects_portalevents.htm) object. The Events object provides the user commands that are assigned to an event in the Data Portal.

[OnContextMenuPointSelected](../../portal/events/portal_events_oncontextmenupointselected.htm): Is triggered in the Data Portal when an item in a context menu is selected. The event starts the [user command](../../procauto/procauto/procauto_usercommand.htm) that you assigned to the [OnContextMenuPointSelected](../../portal/properties/diacmpnt_property_oncontextmenupointselected_portalevents.htm) property.

[OnShowingContextMenu](../../portal/events/portal_events_onshowingcontextmenu.htm): Is triggered in the Data Portal when a context menu displays. The event starts the [user command](../../procauto/procauto/procauto_usercommand.htm) you assigned to the [OnShowingContextMenu](../../portal/properties/diacmpnt_property_onshowingcontextmenu_portalevents.htm) property.

#### Events in DIAdem VIEW

DIAdem VIEW contains the [Events](../../scriptview/objects/view_objects_itoeventsint.htm) object. The Events object provides the user commands assigned to an event in DIAdem VIEW. DIAdem saves the Event object in the VIEW layout file.

The DIAdem VIEW panel provides the following events:

[OnActiveSheetChanged](../../scriptview/events/view_events_activesheetchanged.htm): DIAdem VIEW triggers the OnActiveSheetChanged event when the active worksheet is exchanged. The event starts the user command that you assigned to the property [OnActiveSheetChanged](../../scriptview/properties/view_property_onactivesheetchanged_itoeventsint.htm).

[OnCursorChanged](../../scriptview/events/view_events_cursorchanged.htm): DIAdem VIEW triggers the OnCursorChanged event when the cursor is moved, the measurement mode or cursor is changed, and when the active area is exchanged. The event starts the user command that you assigned to the property [OnCursorChanged](../../scriptview/properties/view_property_oncursorchanged_itoeventsint.htm).

[OnShowingContextMenu](../../scriptview/events/view_events_onshowingcontextmenu.htm): DIAdem VIEW triggers the OnShowingContextMenu event when a context menu is displayed. The event starts the user command that you assigned to the property View.Events.[OnShowingContextMenu](../../scriptview/properties/view_property_onshowingcontextmenu_itoeventsint.htm).

[OnContextMenuPointSelected](../../scriptview/events/view_events_oncontextmenupointselected.htm): DIAdem VIEW triggers the OnContextMenuPointSelected event when a context menu is selected. The event starts the user command that you assigned to the property View.Events.[OnContextMenuPointSelected](../../scriptview/properties/view_property_oncontextmenupointselected_itoeventsint.htm).

[OnDblClick](../../scriptview/events/view_events_ondblclick.htm): DIAdem VIEW triggers the OnDblClick event when an area is double-clicked. The event starts the user command that you assigned to the property View.Events.[OnDblClick](../../scriptview/properties/view_property_ondblclick_itoeventsint.htm).

[OnDrop](../../scriptview/events/view_events_ondrop.htm): DIAdem VIEW triggers the OnDrop event when an element is dragged and dropped from the Data Portal onto an area. The event starts the user command that you assigned to the property View.Events.[OnDrop](../../scriptview/properties/view_property_ondrop_itoeventsint.htm).

[OnDropAllowed](../../scriptview/events/view_events_ondropallowed.htm): DIAdem VIEW triggers the OnDropAllowed event when an element from the Data Portal is dragged and dropped from the Data Portal onto an area. The event starts the user command that you assigned to the property View.Events.[OnDropAllowed](../../scriptview/properties/view_property_ondropallowed_itoeventsint.htm).

[OnLegendClicked](../../scriptview/events/view_events_onlegendclicked.htm): DIAdemVIEW triggers the OnLegendClick event when a legend is clicked. The event starts the user command that you assigned to the property View.Events.[OnLegend](../../scriptview/properties/view_property_onlegendclicked_itoeventsint.htm).

#### Events in DIAdem REPORT

DIAdem REPORT provides the following events:

[OnArrow](../../reportapi/events/report_event_onarrow_irepreportontooltipint.htm), [OnAxisSystem2D](../../reportapi/events/report_event_onaxissystem2d_irepreportontooltipint.htm), [OnAxisSystem3D](../../reportapi/events/report_event_onaxissystem3d_irepreportontooltipint.htm), [OnCircle](../../reportapi/events/report_event_oncircle_irepreportontooltipint.htm), [OnComment](../../reportapi/events/report_event_oncomment_irepreportontooltipint.htm), [OnFormulaDisplay](../../reportapi/events/report_event_onformuladisplay_irepreportontooltipint.htm), [OnFrame](../../reportapi/events/report_event_onframe_irepreportontooltipint.htm), [OnImage](../../reportapi/events/report_event_onimage_irepreportontooltipint.htm), [OnPolarSystem](../../reportapi/events/report_event_onpolarsystem_irepreportontooltipint.htm), [OnSpider](../../reportapi/events/report_event_onspider_irepreportontooltipint.htm), [OnTable2D](../../reportapi/events/report_event_ontable2d_irepreportontooltipint.htm), [OnTable3D](../../reportapi/events/report_event_ontable3d_irepreportontooltipint.htm), and [OnText](../../reportapi/events/report_event_ontext_irepreportontooltipint.htm) for [ToolTipEvents](../../reportapi/objects/report_objects_irepreportontooltipint.htm): DIAdem REPORT triggers these events if you hold the shift key and move the mouse over a REPORT object.

[OnAxisSystem2D](../../reportapi/events/report_event_onaxissystem2d_irepreportondropint.htm), [OnAxisSystem3D](../../reportapi/events/report_event_onaxissystem3d_irepreportondropint.htm), [OnComment](../../reportapi/events/report_event_oncomment_irepreportondropint.htm), [OnPage](../../reportapi/events/report_event_onpage_irepreportondropint.htm), [OnPolarSystem](../../reportapi/events/report_event_onpolarsystem_irepreportondropint.htm), [OnTable2D](../../reportapi/events/report_event_ontable2d_irepreportondropint.htm), [OnTable3D](../../reportapi/events/report_event_ontable3d_irepreportondropint.htm), [OnText](../../reportapi/events/report_event_ontext_irepreportondropint.htm) for [DropEvents](../../reportapi/objects/report_objects_irepreportondropint.htm): DIAdem REPORT triggers these events when an element is dragged and dropped onto a REPORT object.

[OnAxisSystemPolar](../../reportapi/events/report_event_onaxissystempolar_irepreportonclickedwithkeyint.htm), [OnAxisSystem2D](../../reportapi/events/report_event_onaxissystem2d_irepreportonclickedwithkeyint.htm) for [ClickedWithKeyEvents](../../reportapi/objects/report_objects_irepreportonclickedwithkeyint.htm): DIAdem REPORT triggers these events when a polar axis system or a 2D axis system are clicked while a key is pressed.

[OnLayoutLoaded](../../reportapi/events/report_event_onlayoutloaded_irepreporteventsint.htm): DIAdem REPORT triggers this event when a layout is loaded.

[OnLayoutSaving](../../reportapi/events/report_event_onlayoutsaving_irepreporteventsint.htm): DIAdem REPORT triggers this event when a layout is saved.

[OnInitializeSheetRefresh for Events](../../reportapi/events/report_event_oninitializesheetrefresh_irepreporteventsint.htm) and [OnInitializeSheetRefresh for SheetEvents](../../reportapi/events/report_event_oninitializesheetrefresh_irepsheeteventsint.htm): DIAdem REPORT triggers the events OnInitializeSheetRefresh for Events and OnInitializeSheetRefresh for SheetEvents before refreshing a worksheet.

[OnFinalizeSheetRefresh for Events](../../reportapi/events/report_event_onfinalizesheetrefresh_irepreporteventsint.htm) and [OnFinalizeSheetRefresh for SheetEvents](../../reportapi/events/report_event_onfinalizesheetrefresh_irepsheeteventsint.htm): DIAdem REPORT triggers the events OnFinalizeSheetRefresh for Events and OnFinalizeSheetRefresh for SheetEvents after refreshing a worksheet.

[OnDrawingCell](../../reportapi/events/report_event_ondrawingcell_ireptable2dcolumnsettingsint.htm): DIAdem REPORT triggers the OnDrawingCell event while a 2D table line is being plotted.

[OnCurveTransformation for 2DCurve](../../reportapi/events/report_event_oncurvetransformation_irepd2curveint.htm): DIAdem REPORT triggers the OnCurveTransformation event to transform the 2D curve while it is being plotted.

[OnCurveTransformation for 3DCurve](../../reportapi/events/report_event_oncurvetransformation_irepd2curveint.htm): DIAdem REPORT triggers the OnCurveTransformation event to transform the 3D curve while it is being plotted.

[OnChannelTransformation](../../reportapi/events/report_event_onchanneltransformation_ireptable2dcolumnchannelint.htm): DIAdem REPORT triggers the OnChannelTransformation event to transform the values of a table column while it is being plotted.

The DIAdem REPORT panel provides the following events from the earlier, non object-oriented script interface to maintain compatibility:

[OnPicUpdateStart](../../varoff/onpicupdatestart.htm): DIAdem REPORT triggers the OnPicUpdateStart event before a report is refreshed.

[OnPicUpdateEnd](../../varoff/onpicupdateend.htm): DIAdem REPORT triggers the OnPicUpdateEnd event after a report was refreshed.

[OnPicUpdatePageS](../../varoff/onpicupdatepages.htm): DIAdem REPORT triggers the OnPicUpdatePageS event before the current worksheet is refreshed.

[OnPicUpdatePageE](../../varoff/onpicupdatepagee.htm): DIAdem REPORT triggers the OnPicUpdatePageE event after the current worksheet was refreshed.

#### Parallel Processing Events

[OnWorkerStateChange](../../parallelprocesscontrol/events/parallelprocesscontrol_event_onworkerstatechange_iparallelprocesscontrol.htm): DIAdem triggers the OnWorkerStateChange event in parallel processing when a Worker object changes status.

[OnScriptFinished](../../parallelprocesscontrol/events/parallelprocesscontrol_event_onscriptfinished_iparallelprocesscontrol.htm): DIAdem triggers the OnScriptFinished event in parallel processing when a Worker object stops the script that was started with the [Run for Worker](../../parallelprocesscontrol/methods/parallelprocesscontrol_method_run_iworker.htm) method.

#### General Events

[OnPanelChanged](../../varoff/onpanelchanged.htm): DIAdem trigger the OnPanelChanged event when you select a new panel.

[OnFilterKeyShortcut](../../varoff/onfilterkeyshortcut.htm): DIAdem triggers the OnFilterKeyShortcut event every time a key combination with <Shift>, <Ctrl> , or <Alt> is pressed. DIAdem does not trigger this event when you execute the shortcut in DIAdem SCRIPT. You cannot assign several user commands to the OnFilterKeyShortcut event.

[OnF1KeyPressed](../../varoff/onf1keypressed.htm):  DIAdem triggers the OnF1KeyPressed event when you press the F1 key.

[OnFilterDroppedFile](../../varoff/onfilterdroppedfile.htm): DIAdem triggers the OnFilterDroppedFile event when one or several files are dragged or dropped into DIAdem. DIAdem does not trigger this event when you drag the files onto DIAdem SCRIPT. You cannot assign several user commands to the OnFilterDroppedFile event.

[OnCallingHelp](../../varoff/oncallinghelp.htm): DIAdem triggers the OnCallingHelp event when the help is called.

|  | Note Events also occur in user dialog boxes. The above mentioned rules do not apply for events in user dialog boxes. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=genshell/genshell/genshell_working_with_elements.htm language=enus -->
## TOPIC 01004: Working with the Elements Collection, the ElementList Collection, and the Element Object

- bundle_id: `diadem`
- source_path: `genshell/genshell/genshell_working_with_elements.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genshell/genshell/genshell_working_with_elements.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[General](../genshell/genshell_general_overview.htm) > [Basic Information](../genshell/genshell_basciinformation_overview.htm) > Working with the Elements Collection, the ElementList Collection, and the Element Object

Working with the Elements Collection, the ElementList Collection, and the Element Object

You can use the ElementList collection and the Element object in several object-oriented script interfaces. The Element object always contains the properties Name and Properties and the method IsKindOf, regardless of the interface. The ElementList collection and the Elements collection always have the Item method and the Count property. The ElementList collection of the Data API and the Elements collection also have the Add method, the Removemethod, and the RemoveAll method.

The following section contains an overview of the use of the **ElementList collection** and the **Element object** in the various object-oriented interfaces:

| Interface | Data (Internal data) | DataFinder (NAVIGATOR) | Data stores (NAVIGATOR) | DataPlugins |
| --- | --- | --- | --- | --- |
| Use | Access to the Elements in the Data Portal. | Access to the Elements of the Search Results List or of the File Browser of a local DataFinder or of a DataFinder instance. Access can occur with and without using the Navigator interface. | Access to the Elements in the Search Results List of a data store or in the Data Browser. Access can occur with and without using the Navigator interface. | Import of different file formats, with a script. |
| Possible Access | Data.Portal.Structure.Selection... Data.Portal.List.Selection... Data.Root... | Navigator.ConnectDataFinder() Navigator.Display.CurrDataFinder.Browser... Navigator.Display.CurrDataFinder.ResultsList... | Navigator.ConnectDataStore() Navigator.ConnectDataStoreByParameter() Navigator.Display.CurrDataStore. Browser...Navigator.Display.CurrDataStore. ResultsList... | Sub ReadStore() ... ... |
| Object Overviews | Objects Overview | Objects Overview | Objects Overview | Objects Overview |
| Access | Read and write access | Readonly | Read and write access | Read and write access |
| Possible Types | Root, channel group, channel (TDM data model) | File, channel group, channel (TDM data model) | Depending on data model. The ASAM base model contains, for example, the elements MyTest, MySubtest, MyMeasurement, MyMeaQuantity, MySubmatrix, MyLocalColumn, MyUnit, MyUser, and MyUnitUnderTest. | Root, channel group, channel (TDM data model) |
| Transition to the Internal Data | Data already internally available | Loading the elements with the method Navigator.LoadData into the Data Portal. | Loading the elements with the method Navigator.LoadData into the Data Portal. | Loading the elements with DataFileLoad() including the DataPlugin specifications. |
| Elements collections | Data.Root.Channelgroups Data.Root.Channelgroups(i).Channels | None | ...RootElements(i).Children...Reference.Elements | Root.Channelgroups Root.Channelgroups(i).Channels |
| ElementList collections | Return values of the loading functions: Data.GetChannels Data.CreateElementList | Navigator.Display.CurrDataFinder. Browser.SelectedElements Navigator.Display.CurrDataFinder. ResultsList.Selection ResultsList.Elements oMyDataFinder.Results ...Channelgroups ...Channels | Navigator.Display.CurrDataStore. Browser.SelectedElements Navigator.Display.CurrDataStore. ResultsList.Selection ResultsList.Elements oMyStore.GetElementList() | None |

#### Additional Notes

- Elements of the internal data : Use the methods Add and Remove from the collections Channelgroups and Channels to create new channel groups and channels and to delete existing elements. Use the property Properties of the Element object to determine the properties of the root, of a channel group, or of a channel and to assign values to these properties. You also can use the property Properties to create new custom properties.
- Elements of a DataFinder : DataFinders Use the property Properties of the Element object to determine the properties of a file, of a channel group, or of a channel. You cannot create new custom properties or change the values of properties with a script. You cannot create new elements with the ElementList collection.
- Elements of a DataFinder : If you want to create channel groups or channels or if you want to edit properties, you must load the data into the Data Portal and edit the data with the <Data> element object in the Data Portal and then save the data.

- Elements of a data store : Use the methods Add and Remove from the collections RootElements , Children , and Reference . Elements , for example, to create new SubTests, Measurements, or UnitUnderTests or to delete existing elements. You can use the methods AddReference and RemoveReference to join elements and to undo concatenations. Use the property Properties of the Element object, for example, to determine different properties of a test, of a measurement quantity, or of a user and to create new instance properties.
- Elements of a data store : Use a Loading configuration to specify how DIAdem imports the properties of different elements and levels into DIAdem.
- In the Data Interface , the ElementList collection is a list of elements in the Data Portal. Use the ElementList collection to access channels, channel groups, or the root. You can add elements to the collection or remove elements from the collection. The data in the Data Portal remains unchanged. Every element of the collection ElementList is an Element .

<!--NI_TOPIC bundle=diadem path=genview/genview/view_video.htm language=enus -->
## TOPIC 01005: Video

- bundle_id: `diadem`
- source_path: `genview/genview/view_video.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genview/genview/view_video.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem VIEW](../genview/view_overview.htm) > Video

Video

Select **Display Type**»**Video** from the shortcut menu of a VIEW area to insert a video of a test procedure into the layout. In DIAdem VIEW, you can play back videos in MPEG, MPG, WMV, and AVI format. The videos must be freely positionable, so that DIAdem can display each frame in the videos. Refer to [Requirements for Playing Videos in DIAdem VIEW](../genview/view_video_format.htm) for further information.

Use **Play**, **Repeat Play**, or **Pause** in the toolbar, and the functions for fast forward or fast reverse and step-by-step forward or step-by-step reverse in the [Position Cursor](../../dlgview/dlgview/view_coordinatedisplay_dialog.htm) dialog box, to control the video. If your layout contains a video and an axis system, and you move the cursor across the axis system, DIAdem plays the video synchronously to the cursor. Select [Display](../../dlgview/dlgview/view_video_syncprop_dialog.htm) from the context menu to specify the speed and the duration of the video.

Before playing the video, you can select [Zoom](../genview/view_zoom.htm) from the context menu to enlarge the video display. You can also enable **Sound On** in the context menu to play the video with sound. In a script you use the property [Sound for CurveChart2D](../../scriptview/properties/view_property_sound_ito2dchartint.htm) to do so.

#### Examples

[3D Interpolation](../../explonl/explonl/explonl_dac_3d_map.htm) | [Bird's Eye View Display](../../exploff/examples/expl_birds_eye_view_example.htm) | [Overlaying Objects in Videos](../../exploff/examples/expl_view_video_objects_austin_example.htm) | [Planetary Motion](../../exploff/examples/expl_planets_example.htm) | [Recording Video and Measurement Data](../../explonl/explonl/explonl_dac_video.htm) | [Synchronizing Maps, Videos, and Measurement Data](../../exploff/examples/expl_austin_drive.htm) | [Synchronizing Videos and Data](../../exploff/examples/expl_view_av4.htm) | [Synchronizing Videos and Data](../../exploff/examples/expl_view_av4.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm) | [Synchronizing Videos and Waveform Data](../../exploff/examples/expl_view_av5.htm) | [Various Display Modes in DIAdem VIEW](../../exploff/examples/example_example_view.htm)

<!--NI_TOPIC bundle=diadem path=genview/genview/view_zoom.htm language=enus -->
## TOPIC 01006: Zoom Functions

- bundle_id: `diadem`
- source_path: `genview/genview/view_zoom.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genview/genview/view_zoom.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([2D Axis System](../genview/view_2d_axis_system.htm) | [Cursor Types](../genview/view_cursor.htm)) > Zoom Functions

Zoom Functions

Use the zooming function to zoom into sections of the active area in order to examine sections of the curve in details. DIAdem VIEW offers various zoom types in the context menu of the axis systems or on the axis system toolbar. DIAdem scales the area according to the zoom. The video and graphics displays provide zoom functions in the context menu.

|  | Mouse wheel | Use the mouse wheel to enlarge and reduce the active area centrically. If you press <Ctrl> while you zoom, DIAdem zooms in larger steps.In the Channel Table you can scroll with the mouse wheel through the displayed table columns. To scroll linewise through several table columns, Press <Shift> at the same time. To zoom the channel table, press <Ctrl> simultaneously. |
| --- | --- | --- |
|  | Zoom In | Click Zoom In on the toolbar of an axis system in order to enlarge the display in the active area. You can also use the plus key. |
|  | Zoom Out | Click Zoom Out on the toolbar of an axis system in order to reduce the display in the active area. You can also use the minus key. |
|  | Right Mouse Button | Press the right mouse button and drag open a band or a frame in order to enlarge a section in the active area. DIAdem fills the area with the selected section. |
|  | Band Zoom | Click Band Zoom on the axis system toolbar and press the left mouse button to select and enlarge an axis section. You can repeat the zoom so that you can examine ever smaller areas. |
|  | Frame Zoom | Click Frame Zoom on the axis system toolbar and press the left mouse button to select and enlarge a section. You can repeat the zoom so that you can examine ever smaller areas. |
|  | Move | Click Move on the axis system toolbar and press the left mouse button to move the enlarged display. |
|  | Scroll in Cursor Range | Select Band Cursor or Frame Cursor in the axis system and click Sroll in Cursor Area on the toolbar. To move along the enlarged curve, click and drag the cursor horizontally. If there are further axis systems with the same value range on the worksheet, the cursor also moves in these axis systems. |
|  | Zoom Off | This function on the axis system toolbar switches off every zoom function. DIAdem restores the original curve. |

#### Further Settings

[Cursor](../genview/view_cursor.htm) | Zoom Functions | [Flag Functions](../genview/view_flags.htm) | [Cursor Synchronization](../genview/view_synchronisation.htm) | [Legend](../genview/view_legend.htm)

<!--NI_TOPIC bundle=diadem path=genvis/genvis/dac_map.htm language=enus -->
## TOPIC 01007: Map Display

- bundle_id: `diadem`
- source_path: `genvis/genvis/dac_map.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/genvis/genvis/dac_map.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem VISUAL](../genvis/visual_general.htm) > Map Display

Map Display

Use the [Map Display](../../dlgvis/dlgvis/dlgvislistmap_dialog.htm) to display the measured geographical data. The script driver, for example, can read the geographical data from a GPS receiver. DIAdem displays the coordinates with a rhombus. As soon as the rhombus moves towards the edge of the map section, DIAdem shifts the map. DIAdem can also draw the path as a line on the map.

You can use maps from OpenStreetMap for the display. The OpenStreetMap project aims to collect geographical data in a database to create maps. You can use OpenStreetMap data free of licensing costs and edit and customize the data as you like. Visit http://www.OpenStreetMap.org for further information on OpenStreetMap. You can enable a cache for OpenStreetMap so that DIAdem saves all displayed map sections as PNG files on a cache storage path. If you select the Cache map source, you can use the map sections without connecting to the internet. You can also use the cache mode to speed up the map display. If you use the same cache path for both panels, you can use the buffered maps also for an offline analysis in DIAdem VIEW.

You can move the map section displayed in DIAdem VISUAL and also zoom in and out of it. In order to zoom in or out of the map section, click in the map and move the mouse wheel. The higher the zoom step, the more detailed the map section is. The performance effort increases with a greater zoom. To move a map section, press and hold the left mouse button and move the mouse in a specific direction. In OpenStreetMap you can use the zoom and navigation elements, and hide the map scale and the mouse position.

Double-click the map to specify the signal list and the parameters. Click the frame of the map display to select the display instrument and to change the size and position of the workspace.

The map display in DIAdem uses the Standard World Geodetic System 1984 (WGS 84) as a reference system in cartography. WGS 84 is a geodetic reference system for global, three-dimensional, satellite-supported measurements. The system consists of a reference ellipsoid which describes an idealized earth model, a geoid which includes in a model all irregularities of the earth model, and the coordinates of the base stations distributed worldwide which are the reference points for the position specifications.

#### Related Topics

[Map Display in DIAdem VIEW](../../genview/genview/view_map.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/alarm_script_overview.htm language=enus -->
## TOPIC 01008: Script Capability of the Alarm Blocks

- bundle_id: `diadem`
- source_path: `gfsalarm/alarm_script_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/alarm_script_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > Script Capability of the Alarm Blocks

Script Capability of the Alarm Blocks

The subordinate topics contained in the tree on the contents tab of the Help contain overviews of the variables and commands of the alarm blocks.

<!--NI_TOPIC bundle=diadem path=gfsalarm/alarm_uebersicht.htm language=enus -->
## TOPIC 01009: Alarm System Blocks

- bundle_id: `diadem`
- source_path: `gfsalarm/alarm_uebersicht.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/alarm_uebersicht.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > Alarm System Blocks

Alarm System Blocks

The following topics describe the dialog boxes where you make your settings for the alarm system blocks.

<!--NI_TOPIC bundle=diadem path=gfsalarm/alarm_variables_overview.htm language=enus -->
## TOPIC 01010: Alarm System Variables

- bundle_id: `diadem`
- source_path: `gfsalarm/alarm_variables_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/alarm_variables_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > Alarm System Variables

Alarm System Variables

The subordinate topics contained in the tree on the contents tab of the Help contain overviews of the variables of the alarm system.

<!--NI_TOPIC bundle=diadem path=gfsalarm/alarmtab_auto.htm language=enus -->
## TOPIC 01011: Script Capability of the Alarm Table

- bundle_id: `diadem`
- source_path: `gfsalarm/alarmtab_auto.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/alarmtab_auto.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Scriptability of theAlarm Blocks](../gfsalarm/alarm_script_overview.htm) > Script Capability of the Alarm Table

Script Capability of the Alarm Table

| Variable | Meaning |
| --- | --- |
| PkAlTabColCount | Specifies the number of columns in an alarm table. |
| PkAlTabVar | Specifies the alarm attribute that DIAdem displays in the column that is referenced. |
| PKALTabBackColor | Specifies the background color of a row in the alarm table. |
| PKALTabCaption | Specifies the column head of the column referenced in an alarm table. |
| PKALTabDisp | Specifies the display mode of the column referenced in an alarm table. |
| PKALTabWidth | Specifies the relative width of the referenced column. |
| PkAlTabRHAuto | Specifies whether DIAdem specifies the row height in the alarm table automatically or uses the value of the PkAlTabRowHeight variable. |
| PkAlTabRowHeight | Specifies the row height in the alarm table. |
| PkAlTabSelColor | Specifies the color of the rows that are selected in the alarm table. |
| PkAlTabConfirm | Specifies whether DIAdem displays the button for confirming alarms, while a block diagram is running. |
| PkAlTabHide | Specifies whether DIAdem hides the alarm table as long as no messages are displayed. |
| PkAlConfirmAll | Specifies whether DIAdem confirms all the alarms that are selected in the table. |
| PkAlFltGroup | Specifies the names of the alarm groups that are to be displayed. |
| PkAlFltGroupCnt | Specifies the number of alarm groups that are to be displayed. |
| PkAlFltPriority | Specifies the names of the priorities that are to be displayed. |
| PkAlFltPtyCnt | Specifies the number of priorities that are to be displayed. |
| PkAlFltQLCnt | Specifies the number of quit levels that are to be displayed. |
| PkAlFltQuitLevel | Specifies the names of the quit levels that are to be displayed. |
| PkAlFltState | Specifies the names of the alarm states that are to be displayed. |
| PkAlFltStateCnt | Specifies the number of alarm states that are to be displayed. |
| PkAlFrame | Specifies whether DIAdem displays a frame. |
| PkAlNoDraftOnL | Specifies whether DIAdem deactivates the draft mode online. |
| PkAlNoDraftOffL | Specifies whether DIAdem deactivates the draft mode offline. |
| PkAlOnTop | Specifies whether DIAdem sets a window mode online, in which the window is always visible. |
| PkAlTxtX | Specifies the horizontal label. |
| PkAlFrameColor | Specifies the color of the frame. |
| PkAlTxtColor | Specifies the color of the label on the OK button. |
| PkAlInstrPosX | Specifies the x-position of the instrument in DIAdem VISUAL. |
| PkAlInstrPosY | Specifies the y-position of the instrument in DIAdem VISUAL. |
| PkAlInstrWidth | Specifies the width of the instrument in DIAdem VISUAL. |
| PkAlInstrHeight | Specifies the height of the instrument in DIAdem VISUAL. |
| PkAlInstrPosRel | Specifies the alignment of the instrument in DIAdem VISUAL. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/alarmtab_dialog.htm language=enus -->
## TOPIC 01012: Alarm Table

- bundle_id: `diadem`
- source_path: `gfsalarm/alarmtab_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/alarmtab_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Alarm Table

Alarm Table

Use this dialog box to visualize and to confirm the alarms that the alarm generator generates.

#### Settings

| Table columns |  |
| --- | --- |
| Variable | Specifies the variable that is to be displayed in the overview. |
| Display | Specifies the type of alarm display. |
| Relative Width | Specifies the width of the columns in relation to each other. A column with a relative width of two is displayed twice as wide as a column with a relative width of one. |
| Label | Specifies the labels for columns in the alarm table. By default, DIAdem displays the name of the attribute. |
| Row-related background color |  |
| Color is determined by | Specifies which variable specifies the color of the alarms in the online display of the alarm table. |
|  |  |
| Filter Criteria | Opens the dialog box where you specify the filter criteria. |
| General Layout | Opens the dialog box where you specify the general layout of the alarm table. |
| Display | Opens the dialog box where you specify the display of the alarm table. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/alarmtablay_dialog.htm language=enus -->
## TOPIC 01013: Alarm Table - Display

- bundle_id: `diadem`
- source_path: `gfsalarm/alarmtablay_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/alarmtablay_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Alarm Table - Display

Alarm Table - Display

Use this dialog box to specify the behavior and the appearance of the alarm table.

#### Settings

| Define line height automatically | Specifies that DIAdem specifies the line height automatically. |
| --- | --- |
| Line height | Specifies the line height that you enter manually. |
| Only confirm marked alarms | Specifies that you can confirm only selected alarms. |
| Background color of the selected line | Displays the background color of the selected line. |
| Color | Opens the dialog box where you specify the background color of the selected line. |
| Display button for alarm confirmation | Specifies that DIAdem enables you to select and to confirm alarms during runtime. |
| Hide window if no messages are available | Specifies that DIAdem hides the online display if there are no alarms that meet the filter criteria. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/alarmuebersicht_dialog.htm language=enus -->
## TOPIC 01014: Global Parameters - Overview

- bundle_id: `diadem`
- source_path: `gfsalarm/alarmuebersicht_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/alarmuebersicht_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Global Parameters - Overview

Global Parameters - Overview

Use this dialog box to edit the global parameters.

#### Settings

| Index | Specifies the incrementing number. |
| --- | --- |
| Title | Specifies the name. |
| Color | Specifies the color. |
| Graphic | Specifies a graphic. |
|  |  |
| New Entry | Opens the dialog box where you create a new entry. |
| Edit | Opens the dialog box where you edit the selected entry. |
| Delete | Deletes the selected entry. |

|  | Note Refer to the page on Alarm Status for more information on the various alarm states. |
| --- | --- |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/onllogin_dialog.htm language=enus -->
## TOPIC 01015: Log User On/Off

- bundle_id: `diadem`
- source_path: `gfsalarm/onllogin_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/onllogin_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Log User On/Off

Log User On/Off

Use this dialog box to log on or log off in the user management when a DAC block diagram is running.

#### Settings

| Time-out active | Specifies whether DIAdem automatically activates the log off after a specific period of time. |
| --- | --- |
| Log out after ... Minutes | Specifies the period of time after which DIAdem automatically logs off the user from the user management. |
| General Layout | Opens the dialog box where you configure the online display of the login block. |
| Format String | Opens the dialog box where you specify the format strings for the alarm texts. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/onlms_outlook_dialog.htm language=enus -->
## TOPIC 01016: Text Output Outlook - MS Outlook

- bundle_id: `diadem`
- source_path: `gfsalarm/onlms_outlook_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/onlms_outlook_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Text Output Outlook - MS Outlook

Text Output Outlook - MS Outlook

Use this dialog box to remote control Microsoft Outlook through a network.

#### Settings

| MS Outlook is located... | Specifies whether Microsoft Outlook is installed on the local computer or on another computer in the network. |
| --- | --- |
| ...on the following computer in the network | Specifies the name of the computer in the network that Microsoft Outlook is installed on. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/onltextdde_dialog.htm language=enus -->
## TOPIC 01017: Text Output DDE

- bundle_id: `diadem`
- source_path: `gfsalarm/onltextdde_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/onltextdde_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Text Output DDE

Text Output DDE

Use this dialog box to process text packets and to transmit alarm messages over long distances using fax software, e-mail software, or paging software, or to archive alarm messages in a database. DIAdem sends these texts via DDE to any program that you can use as a DDE server.

#### Settings

| Parameter DDE communication |  |
| --- | --- |
| DDE Server | Specifies the DDE server that is to be accessed. |
| DDE Topic | Specifies the file that the DDE server edits. |
| DDE Item | Specifies where or how the DDE server processes the data. |
| Text additions |  |
| Leading | Specifies a text that is to be added at the start. |
| Trailing | Specifies a text that is to be appended. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/onltxtaus_dialog.htm language=enus -->
## TOPIC 01018: Dynamic Text Display

- bundle_id: `diadem`
- source_path: `gfsalarm/onltxtaus_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/onltxtaus_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Dynamic Text Display

Dynamic Text Display

Use this dialog box to set parameters for a screen window that is similar to an editor. The window displays incoming texts in the order that they arrive.

#### Settings

| Maximum number of lines | Specifies the maximum number of lines in the window. |
| --- | --- |
| Minimum number of lines | Specifies the minimum number of lines in the window. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/onltxtein_dialog.htm language=enus -->
## TOPIC 01019: Text Entry

- bundle_id: `diadem`
- source_path: `gfsalarm/onltxtein_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/onltxtein_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Text Entry

Text Entry

Use this dialog box to enter texts during a message and to send the text packets.

#### Settings

| Display OK button | Specifies whether DIAdem displays the OK button. |
| --- | --- |
| Label button | Specifies the text that you see on the button while DIAdem shows the entry field. |
| Open windows only for data input | Specifies whether DIAdem first displays only the name and the button of the block. DIAdem does not display the entry field until the user clicks the button while the block diagram is running. If you do not select this checkbox, DIAdem always displays the name, the button, and the entry field. |
| Key label (window closed) | Specifies the text that you see on the button while DIAdem hides the entry field. |
| General Layout | Opens the dialog box where you specify the general layout of an online display. |
| Format String | Opens the dialog box where you use format strings to combine and to control alarm texts. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/onltxtlog_dialog.htm language=enus -->
## TOPIC 01020: Logfile

- bundle_id: `diadem`
- source_path: `gfsalarm/onltxtlog_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/onltxtlog_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Logfile

Logfile

Use this dialog box to save incoming text packets in the specified file.

#### Settings

| Filename | Specifies the name of the file in which DIAdem saves the incoming data. |
| --- | --- |
| Append to logfile | Specifies whether DIAdem opens the existing file every time a measurement starts and starts with the new entries at the end of the file. Otherwise, DIAdem regenerates the file every time a measurement starts and deletes the existing contents. |
| Browse | Opens the dialog box where you specify the logfile. |
| Create backup logfile | Specifies whether DIAdem creates a copy of the logfile. |
| Filename | Specifies the name of the copy of the logfile. |
| Browse | Opens the dialog box where you specify the backup logfile. |
| Log file reset |  |
| Maximum file size | Specifies the maximum size of the logfile in kilobytes, before a reset. |
| Minimum file size | Specifies the minimum size of the logfile in kilobytes, after a reset. |
| Format strings |  |
| Start Row | Opens the dialog box where you specify a multiline text that DIAdem writes to the file first when the measurement starts. |
| End Row | Opens the dialog box where you specify a multiline text that DIAdem writes to the file last when the measurement stops. |
| Start Row after Reset | Opens the dialog box where you specify a multiline text that DIAdem writes to the file after the logfile resets. |
|  |  |
| Editor | Opens the editor that you specified in Windows as the editor for the specific filename extensions. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/onltxtoutlook_dialog.htm language=enus -->
## TOPIC 01021: Text Output Outlook

- bundle_id: `diadem`
- source_path: `gfsalarm/onltxtoutlook_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/onltxtoutlook_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Alarm Blocks](../gfsalarm/alarm_uebersicht.htm) > Text Output Outlook

Text Output Outlook

Use this dialog box to communicate with Microsoft Outlook via OLE. Microsoft Outlook must be located on the local computer or must be remote-controlled on another computer in the network.

#### Settings

| Email parameters |  |
| --- | --- |
| Receiver | Specifies the name of the receiver. You must specify the name previously in Microsoft Outlook. |
| Reference | Specifies the subject of the mail. The maximum reference length is 255 characters. |
| Add file | Specifies that you want to attach a file to the mail. |
| Browse | Opens the dialog box where you select the file to be appended. |
| Filename | Specifies the name of the file that you attach. |
| Importance | Specifies the priority level of the mail. |
| Text supplements |  |
| Leading | Specifies a text that is to be added at the start. |
| Trailing | Specifies a text that is to be appended. |
|  |  |
| MS Outlook | Opens a dialog box where you remote control Microsoft Outlook through a network. |

#### Examples

[Alarm-Related Visualization](../explonl/explonl/explonl_dac_av50.htm) | [Confirming Alarms](../explonl/explonl/explonl_dac_av46.htm) | [Critical Alarms Linked to a Master Alarm](../explonl/explonl/explonl_dac_ab7.htm) | [Displaying Alarm Status](../explonl/explonl/explonl_dac_av45.htm) | [Displaying Alarms as Text](../explonl/explonl/explonl_dac_av48.htm) | [Displaying Alarms in a Table](../explonl/explonl/explonl_dac_av44.htm) | [Extended Alarm Status Display](../explonl/explonl/explonl_dac_av47.htm) | [Filtering Alarm Messages with Format Blocks](../explonl/explonl/explonl_dac_av51.htm) | [Text Input for Commenting Alarms](../explonl/explonl/explonl_dac_av49.htm)

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalactive.htm language=enus -->
## TOPIC 01022: Variable: PkAlActive

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalactive.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalactive.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlActive

Variable: PkAlActive

Specifies whether the alarm definition that is specified by the index, is activated.

| Definition | PkAlActive, String variable |
| --- | --- |
|  | "Yes"/"No" |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlActive = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalappend.htm language=enus -->
## TOPIC 01023: Variable: PkAlAppend

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalappend.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalappend.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlAppend

Variable: PkAlAppend

Specifies whether DIAdem deletes and recreates the logfile at the beginning of a measurement. If you assign the value FALSE to the PkAlAppend variable, DIAdem creates a new logfile. If you assign the value TRUE to the PkAlAppend variable, DIAdem appends new logfile entries to the existing entries.

| Definition | PkAlAppend, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlAppend = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalattachfile.htm language=enus -->
## TOPIC 01024: Variable: PkAlAttachFile

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalattachfile.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalattachfile.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlAttachFile

Variable: PkAlAttachFile

Specifies the name of a file that is to be sent as an attachment.

| Definition | PkAlAttachFile, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlAttachFile = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalattachflag.htm language=enus -->
## TOPIC 01025: Variable: PkAlAttachFlag

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalattachflag.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalattachflag.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlAttachFlag

Variable: PkAlAttachFlag

Specifies whether DIAdem sends a file as an attachment.

| Definition | PkAlAttachFlag, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlAttachFlag = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalbackname.htm language=enus -->
## TOPIC 01026: Variable: PkAlBackName

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalbackname.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalbackname.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlBackName

Variable: PkAlBackName

Specifies the name of the security logfile, including the filename extension.

| Definition | PkAlBackName, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlBackName = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalbackup.htm language=enus -->
## TOPIC 01027: Variable: PkAlBackup

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalbackup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalbackup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlBackup

Variable: PkAlBackup

Specifies whether DIAdem creates a security logfile.

| Definition | PkAlActive, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlBackup = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalchn.htm language=enus -->
## TOPIC 01028: Variable: PkAlChn

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalchn.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalchn.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlChn

Variable: PkAlChn

Specifies the index of the alarm definition that is to be monitored.

| Definition | PkAlChn, LongInteger variable |
| --- | --- |
|  | 1 ... 255 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlChn = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalchnname.htm language=enus -->
## TOPIC 01029: Variable: PkAlChnName

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalchnname.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalchnname.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlChnName

Variable: PkAlChnName

Specifies the channel name of the alarm definition that the index references.

| Definition | PkAlChnName, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlChnName = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalcomment.htm language=enus -->
## TOPIC 01030: Variable: PkAlComment

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalcomment.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalcomment.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlComment

Variable: PkAlComment

Specifies the comment for an alarm definition.

| Definition | PkAlComment(i), String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlComment = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalconfirmall.htm language=enus -->
## TOPIC 01031: Variable: PkAlConfirmAll

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalconfirmall.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalconfirmall.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlConfirmAll

Variable: PkAlConfirmAll

Specifies whether DIAdem confirms all the alarms that are selected in the table. If you assign the value 1 to the PkAlConfirmAll variable, DIAdem confirms all the alarms. Otherwise, DIAdem confirms only the selected alarms.

| Definition | PkAlConfirmAll, LongInteger variable |
| --- | --- |
|  | 0, 1 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlConfirmAll = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalddefoot.htm language=enus -->
## TOPIC 01032: Variable: PkAlDdeFoot

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalddefoot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalddefoot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlDdeFoot

Variable: PkAlDdeFoot

Specifies a trailing text, which DIAdem appends to a text that is to be sent via DDE.

| Definition | PkAlDdeFoot, String variable |
| --- | --- |
|  | Maximum 249 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlDdeFoot = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalddeheader.htm language=enus -->
## TOPIC 01033: Variable: PkAlDdeHeader

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalddeheader.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalddeheader.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlDdeHeader

Variable: PkAlDdeHeader

Specifies a leading text, which DIAdem inserts before a text that is to be sent via DDE.

| Definition | PkAlDdeFoot, String variable |
| --- | --- |
|  | Maximum 249 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlDdeHeader = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalddeitem.htm language=enus -->
## TOPIC 01034: Variable: PkAlDdeItem

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalddeitem.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalddeitem.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlDdeItem

Variable: PkAlDdeItem

Specifies the name of an item for DDE communication.

| Definition | PkAlDdeItem, String variable |
| --- | --- |
|  | Maximum 249 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlDdeItem = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalddeserver.htm language=enus -->
## TOPIC 01035: Variable: PkAlDdeServer

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalddeserver.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalddeserver.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlDdeServer

Variable: PkAlDdeServer

Specifies the name of the DDE server application.

| Definition | PkAlDdeServer, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlDdeServer = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalddetopic.htm language=enus -->
## TOPIC 01036: Variable: PkAlDdeTopic

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalddetopic.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalddetopic.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlDdeTopic

Variable: PkAlDdeTopic

Specifies the name of the topic of the DDE communication.

| Definition | PkAlDdeTopic, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlDdeTopic = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaldefcount.htm language=enus -->
## TOPIC 01037: Variable: PkAlDefCount

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaldefcount.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaldefcount.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlDefCount

Variable: PkAlDefCount

Specifies the number of alarm definitions in the alarm generator. If you enter a number that is lower than the number that the alarm generator contains, DIAdem rejects the remaining alarm definitions.

| Definition | PkAlDefCount, LongInteger variable |
| --- | --- |
|  | 1 ... 250 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlDefCount = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaldelay.htm language=enus -->
## TOPIC 01038: Variable: PkAlDelay

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaldelay.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaldelay.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlDelay

Variable: PkAlDelay

Specifies the delay for an alarm definition.

| Definition | PkAlDelay(i), Integer variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlDelay(i) = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfilename.htm language=enus -->
## TOPIC 01039: Variable: PkAlFileName

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfilename.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfilename.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFileName

Variable: PkAlFileName

Specifies the name of the logfile.

| Definition | PkAlFileName, String variable |
| --- | --- |
|  | Maximum 250 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFileName = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfltgroup.htm language=enus -->
## TOPIC 01040: Variable: PkAlFltGroup

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfltgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfltgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFltGroup

Variable: PkAlFltGroup

Specifies the names of the alarm groups that are to be displayed.

| Definition | PkAlFltGroup, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFltGroup = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfltgroupcnt.htm language=enus -->
## TOPIC 01041: Variable: PkAlFltGroupCnt

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfltgroupcnt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfltgroupcnt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFltGroupCnt

Variable: PkAlFltGroupCnt

Specifies the number of alarm groups that are to be displayed.

| Definition | PkAlFltGroupCnt, LongInteger variable |
| --- | --- |
|  | Value range: 0 ... 255 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFltGroupCnt = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfltpriority.htm language=enus -->
## TOPIC 01042: Variable: PkAlFltPriority

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfltpriority.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfltpriority.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFltPriority

Variable: PkAlFltPriority

Specifies the names of the priorities that are to be displayed.

| Definition | PkAlFltPriority, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFltPriority = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfltptycnt.htm language=enus -->
## TOPIC 01043: Variable: PkAlFltPtyCnt

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfltptycnt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfltptycnt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFltPtyCnt

Variable: PkAlFltPtyCnt

Specifies the number of priorities that are to be displayed.

| Definition | PkAlFltPtyCnt, LongInteger variable |
| --- | --- |
|  | 0 ... 255 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFltPtyCnt = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfltqlcnt.htm language=enus -->
## TOPIC 01044: Variable: PkAlFltQLCnt

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfltqlcnt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfltqlcnt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFltQLCnt

Variable: PkAlFltQLCnt

Specifies the number of quit levels that are to be displayed.

| Definition | PkAlFltQLCnt, LongInteger variable |
| --- | --- |
|  | 0 ... 255 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFltQLCnt = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfltquitlevel.htm language=enus -->
## TOPIC 01045: Variable: PkAlFltQuitLevel

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfltquitlevel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfltquitlevel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFltQuitLevel

Variable: PkAlFltQuitLevel

Specifies the names of the quit levels that are to be displayed.

| Definition | PkAlFltQuitLevel, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFltQuitLevel = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfltstate.htm language=enus -->
## TOPIC 01046: Variable: PkAlFltState

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfltstate.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfltstate.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFltState

Variable: PkAlFltState

Specifies the names of the alarm states that are to be displayed.

| Definition | PkAlFltState, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFltState = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfltstatecnt.htm language=enus -->
## TOPIC 01047: Variable: PkAlFltStateCnt

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfltstatecnt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfltstatecnt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFltStateCnt

Variable: PkAlFltStateCnt

Specifies the number of alarm states that are to be displayed.

| Definition | PkAlFltStateCnt, String variable |
| --- | --- |
|  | 0 ... 255 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFltStateCnt = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfmtadd.htm language=enus -->
## TOPIC 01048: Command: PkAlFmtAdd

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfmtadd.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfmtadd.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Commands](../gfsalarm/alarm_commands_overview.htm) > Command: PkAlFmtAdd

Command: PkAlFmtAdd

Appends the character string that is transferred as a parameter, to the current format string.

```text
Call PkAlFmtAdd
```

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call PkAlFmtAdd Call DACObjClose(BlockName)Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfmtclear.htm language=enus -->
## TOPIC 01049: Command: PkAlFMTClear

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfmtclear.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfmtclear.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Commands](../gfsalarm/alarm_commands_overview.htm) > Command: PkAlFMTClear

Command: PkAlFMTClear

Deletes the current format string. Use the [PkAlFMTAdd](../gfsalarm/pkalfmtadd.htm) command to create new format strings.

```text
Call PkAlFMTClear
```

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call PkAlFMTClear Call DACObjClose(BlockName)Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfmtstring.htm language=enus -->
## TOPIC 01050: Variable: PkAlFmtString

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfmtstring.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfmtstring.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFmtString

Variable: PkAlFmtString

Specifies a format string.

| Definition | PkAlFmtString, String variable |
| --- | --- |
|  | Maximum 250 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFmtString = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfoot.htm language=enus -->
## TOPIC 01051: Variable: PkAlFoot

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfoot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfoot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFoot

Variable: PkAlFoot

Specifies the end text of the logfile. DIAdem writes this end text to the logfile after each measurement.

| Definition | PkAlFoot, String variable |
| --- | --- |
|  | Maximum 255 characters |

|  | Note You must use the following object hierarchy to access the variable:Call DACObjOpen(BlockName) PkAlFoot = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfootadd.htm language=enus -->
## TOPIC 01052: Command: PkAlFootAdd

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfootadd.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfootadd.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Commands](../gfsalarm/alarm_commands_overview.htm) > Command: PkAlFootAdd

Command: PkAlFootAdd

Adds a string to the format string for the end text of the logfile. DIAdem adds this string each time a measurement starts.

```text
Call PkAlFootAdd
```

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call PkAlFootAdd Call DACObjClose(BlockName)Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalfootclear.htm language=enus -->
## TOPIC 01053: Command: PkAlFootClear

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalfootclear.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalfootclear.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Commands](../gfsalarm/alarm_commands_overview.htm) > Command: PkAlFootClear

Command: PkAlFootClear

Deletes the format string for the end text of the logfile.

```text
Call PkAlFootClear
```

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call PkAlFootClear Call DACObjClose(BlockName)Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalformat.htm language=enus -->
## TOPIC 01054: Variable: PkAlFormat

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalformat.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalformat.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFormat

Variable: PkAlFormat

Specifies the current format string.

| Definition | PkAlFormat, String variable |
| --- | --- |
|  | Maximum 255 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFormat = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalframe.htm language=enus -->
## TOPIC 01055: Variable: PkAlFrame

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalframe.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalframe.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFrame

Variable: PkAlFrame

Specifies whether DIAdem displays a frame.

| Definition | PkAlFrame, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFrame = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalframecolor.htm language=enus -->
## TOPIC 01056: Variable: PkAlFrameColor

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalframecolor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalframecolor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlFrameColor

Variable: PkAlFrameColor

Specifies the color of the frame.

| Definition | PkAlFrameColor, LongInteger variable |
| --- | --- |
|  | Color |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlFrameColor = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalgroup.htm language=enus -->
## TOPIC 01057: Variable: PkAlGroup

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlGroup

Variable: PkAlGroup

Specifies the names of the defined alarm groups.

| Definition | PkAlGroup, String variable |
| --- | --- |
|  | Predefined setting: "Alarm group 1", "Alarm group 2", "Alarm group 3" |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlGroup = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalheadadd.htm language=enus -->
## TOPIC 01058: Command: PkAlHeadAdd

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalheadadd.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalheadadd.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Commands](../gfsalarm/alarm_commands_overview.htm) > Command: PkAlHeadAdd

Command: PkAlHeadAdd

Adds a string to the format string for the start text that DIAdem writes to the logfile when a measurement starts.

```text
Call PkAlHeadAdd
```

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call PkAlHeadAdd Call DACObjClose(BlockName)Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalheadclear.htm language=enus -->
## TOPIC 01059: Command: PkAlHeadClear

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalheadclear.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalheadclear.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Commands](../gfsalarm/alarm_commands_overview.htm) > Command: PkAlHeadClear

Command: PkAlHeadClear

Deletes the format string for the start text that DIAdem writes to the logfile when a measurement starts.

```text
Call PkAlHeadClear
```

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call PkAlHeadClear Call DACObjClose(BlockName)Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalheader.htm language=enus -->
## TOPIC 01060: Variable: PkAlHeader

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalheader.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalheader.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlHeader

Variable: PkAlHeader

Specifies the start text of the logfile. DIAdem writes the start text to the logfile at the beginning of each measurement.

| Definition | PkAlHeader, String variable |
| --- | --- |
|  | Maximum 255 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlHeader = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalimportance.htm language=enus -->
## TOPIC 01061: Variable: PKALImportance

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalimportance.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalimportance.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PKALImportance

Variable: PKALImportance

Specifies the topic of the DDE communication.

| Definition | PKALImportance, LongInteger variable |
| --- | --- |
|  | Value range: 0, 1, 2 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PKALImportance = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalinstrheight.htm language=enus -->
## TOPIC 01062: Variable: PkAlInstrHeight

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalinstrheight.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalinstrheight.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlInstrHeight

Variable: PkAlInstrHeight

Specifies the height of the instrument in DIAdem VISUAL.

| Definition | PkAlInstrHeight, LongInteger variable |
| --- | --- |
|  | Value range: 0 ... 100 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlInstrHeight = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalinstrposrel.htm language=enus -->
## TOPIC 01063: Variable: PkAlInstrPosRel

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalinstrposrel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalinstrposrel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlInstrPosRel

Variable: PkAlInstrPosRel

Specifies the alignment of the instrument in DIAdem VISUAL.

| Definition | PkAlInstrPosRel, String variable |
| --- | --- |
|  | Value range: r_top, cent, right, r_bot, top, bottom, l_top, left, l_bot |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlInstrPosRel = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalinstrposx.htm language=enus -->
## TOPIC 01064: Variable: PkAlInstrPosX

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalinstrposx.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalinstrposx.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlInstrPosX

Variable: PkAlInstrPosX

Specifies the x-position of the instrument in DIAdem VISUAL.

| Definition | PkAlInstrPosX, LongInteger variable |
| --- | --- |
|  | Value range: 0 ... 100 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlInstrPosX = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalinstrposy.htm language=enus -->
## TOPIC 01065: Variable: PkAlInstrPosY

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalinstrposy.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalinstrposy.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlInstrPosY

Variable: PkAlInstrPosY

Specifies the y-position of the instrument in DIAdem VISUAL.

| Definition | PkAlInstrPosY, LongInteger variable |
| --- | --- |
|  | Value range: 0 ... 100 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlInstrPosY = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalinstrwidth.htm language=enus -->
## TOPIC 01066: Variable: PkAlInstrWidth

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalinstrwidth.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalinstrwidth.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlInstrWidth

Variable: PkAlInstrWidth

Specifies the width of the instrument in DIAdem VISUAL.

| Definition | PkAlInstrWidth, LongInteger variable |
| --- | --- |
|  | Value range: 0 ... 100 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlInstrWidth = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkallogsizemax.htm language=enus -->
## TOPIC 01067: Variable: PkAlLogSizeMax

- bundle_id: `diadem`
- source_path: `gfsalarm/pkallogsizemax.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkallogsizemax.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlLogSizeMax

Variable: PkAlLogSizeMax

Specifies the size that the logfile has to reach for DIAdem to reset the logfile. If you assign the value 0 to the PkAlLogSizeMax variable, DIAdem does not reset the logfile.

| Definition | PkAlLogSizeMax, LongInteger variable |
| --- | --- |
|  | Unit: KByte |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlLogSizeMax = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkallogsizemin.htm language=enus -->
## TOPIC 01068: Variable: PkAlLogSizeMin

- bundle_id: `diadem`
- source_path: `gfsalarm/pkallogsizemin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkallogsizemin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlLogSizeMin

Variable: PkAlLogSizeMin

Specifies the size of the logfile block that is maintained in the file when DIAdem resets the logfile.

| Definition | PkAlLogSizeMin, LongInteger variable |
| --- | --- |
|  | Unit: KByte |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlLogSizeMin = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalmailfoot.htm language=enus -->
## TOPIC 01069: Variable: PkAlMailFoot

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalmailfoot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalmailfoot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlMailFoot

Variable: PkAlMailFoot

Specifies a concluding text that DIAdem sends as a mail.

| Definition | PkAlMailFoot, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlMailFoot = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalmailheader.htm language=enus -->
## TOPIC 01070: Variable: PkAlMailHeader

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalmailheader.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalmailheader.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlMailHeader

Variable: PkAlMailHeader

Specifies a leading text that DIAdem sends as mail.

| Definition | PkAlMailHeader, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlMailHeader = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalminimized.htm language=enus -->
## TOPIC 01071: Variable: PkAlMinimized

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalminimized.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalminimized.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlMinimized

Variable: PkAlMinimized

Specifies whether DIAdem minimizes the window during runtime.

| Definition | PkAlMinimized, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlMinimized = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalname.htm language=enus -->
## TOPIC 01072: Variable: PkAlName

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalname.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalname.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlName

Variable: PkAlName

Specifies the name of the referenced alarm definition.

| Definition | PkAlName(i), String variable |
| --- | --- |
|  | Any character strings |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlName(i) = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalnodraftoffl.htm language=enus -->
## TOPIC 01073: Variable: PkAlNoDraftOffL

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalnodraftoffl.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalnodraftoffl.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlNoDraftOffL

Variable: PkAlNoDraftOffL

Specifies whether DIAdem deactivates the draft mode offline.

| Definition | PkAlNoDraftOffL, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlNoDraftOffL = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalnodraftonl.htm language=enus -->
## TOPIC 01074: Variable: PkAlNoDraftOnL

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalnodraftonl.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalnodraftonl.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlNoDraftOnL

Variable: PkAlNoDraftOnL

Specifies whether DIAdem deactivates the draft mode online.

| Definition | PkAlNoDraftOnL, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlNoDraftOnL = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalontop.htm language=enus -->
## TOPIC 01075: Variable: PkAlOnTop

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalontop.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalontop.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlOnTop

Variable: PkAlOnTop

Specifies whether DIAdem sets a window mode online, in which the window is always visible.

| Definition | PkAlOnTop, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlOnTop = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalpriority.htm language=enus -->
## TOPIC 01076: Variable: PkAlPriority

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalpriority.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalpriority.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlPriority

Variable: PkAlPriority

Specifies the names of the priorities of an alarm definition.

| Definition | PkAlPriority, String variable |
| --- | --- |
|  | Default setting: "Note", "Warning", "Error" |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlPriority = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalquitlevel.htm language=enus -->
## TOPIC 01077: Variable: PkAlQuitLevel

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalquitlevel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalquitlevel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlQuitLevel

Variable: PkAlQuitLevel

Specifies the name of the quit level for an alarm definition.

| Definition | PkAlQuitLevel, String variable |
| --- | --- |
|  | Predefined settings: "User 1", "User 2", "User 3" |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlQuitLevel = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalrecipient.htm language=enus -->
## TOPIC 01078: Variable: PkAlRecipient

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalrecipient.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalrecipient.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlRecipient

Variable: PkAlRecipient

Specifies the name of a DDE server application.

| Definition | PkAlRecipient, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlRecipient = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalrefvalue.htm language=enus -->
## TOPIC 01079: Variable: PkAlRefValue

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalrefvalue.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalrefvalue.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlRefValue

Variable: PkAlRefValue

Specifies the limit for an alarm definition.

| Definition | PkAlRefValue(i), Real variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlRefValue(i) = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalremoteflag.htm language=enus -->
## TOPIC 01080: Variable: PkAlRemoteFlag

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalremoteflag.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalremoteflag.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlRemoteFlag

Variable: PkAlRemoteFlag

Specifies whether DIAdem launches MS Outlook on another computer.

| Definition | PkAlRemoteFlag, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlRemoteFlag = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalremotepc.htm language=enus -->
## TOPIC 01081: Variable: PkAlRemotePC

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalremotepc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalremotepc.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlRemotePC

Variable: PkAlRemotePC

Specifies the name of the remote computer.

| Definition | PkAlRemotePC, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlRemotePC = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalresadd.htm language=enus -->
## TOPIC 01082: Command: PkAlResAdd

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalresadd.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalresadd.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Commands](../gfsalarm/alarm_commands_overview.htm) > Command: PkAlResAdd

Command: PkAlResAdd

Adds a string to the format string that DIAdem writes to the logfile after the logfile is reset.

```text
Call PkAlResAdd
```

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call PkAlResAdd Call DACObjClose(BlockName)Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalresclear.htm language=enus -->
## TOPIC 01083: Command: PkAlResClear

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalresclear.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalresclear.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Commands](../gfsalarm/alarm_commands_overview.htm) > Command: PkAlResClear

Command: PkAlResClear

Deletes the format string that DIAdem writes to the logfile after the logfile is reset.

```text
Call PkAlFMTClear
```

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call PkAlResClear Call DACObjClose(BlockName)Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalrowmax.htm language=enus -->
## TOPIC 01084: Variable: PkAlRowMax

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalrowmax.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalrowmax.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlRowMax

Variable: PkAlRowMax

Specifies the number of rows at which DIAdem automatically resets the display.

| Definition | PkAlRowMax, LongInteger variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlRowMax = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalrowmin.htm language=enus -->
## TOPIC 01085: Variable: PkAlRowMin

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalrowmin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalrowmin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlRowMin

Variable: PkAlRowMin

Specifies the number of rows that DIAdem retains when DIAdem deletes the display.

| Definition | PkAlRowMin, LongInteger variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlRowMin = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalshowbutton.htm language=enus -->
## TOPIC 01086: Variable: PkAlShowButton

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalshowbutton.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalshowbutton.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlShowButton

Variable: PkAlShowButton

Specifies whether DIAdem displays the OK button in the text window.

| Definition | PkAlShowButton, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlShowButton = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalsubject.htm language=enus -->
## TOPIC 01087: Variable: PKALSubject

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalsubject.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalsubject.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PKALSubject

Variable: PKALSubject

Specifies the name of the topic for DDE communication.

| Definition | PKALSubject, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PKALSubject = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabbackcolor.htm language=enus -->
## TOPIC 01088: Variable: PKALTabBackColor

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabbackcolor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabbackcolor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PKALTabBackColor

Variable: PKALTabBackColor

Specifies the background color of a row in the alarm table.

| Definition | PKALTabBackColor, String variable |
| --- | --- |
|  | ‘PkAlGroup’ / ‘PkAlType’ / ‘PkAlState’ / ‘PkAlPriority’ / ‘PkAlQuitLevel’ |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PKALTabBackColor = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabcaption.htm language=enus -->
## TOPIC 01089: Variable: PKALTabCaption

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabcaption.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabcaption.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PKALTabCaption

Variable: PKALTabCaption

Specifies the column head of the column referenced in an alarm table.

| Definition | PKALTabCaption, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PKALTabCaption = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabcolcount.htm language=enus -->
## TOPIC 01090: Variable: PkAlTabColCount

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabcolcount.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabcolcount.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTabColCount

Variable: PkAlTabColCount

Specifies the number of columns in an alarm table.

| Definition | PkAlTabColCount, LongInteger variable |
| --- | --- |
|  | 1 ... 32 |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTabColCount = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabconfirm.htm language=enus -->
## TOPIC 01091: Variable: PkAlTabConfirm

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabconfirm.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabconfirm.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTabConfirm

Variable: PkAlTabConfirm

Specifies whether DIAdem displays the button for confirming alarms, while a block diagram is running. This requires the output of the alarm table to be connected to the T input of an alarm generator.

| Definition | PkAlTabConfirm, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTabConfirm = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabdisp.htm language=enus -->
## TOPIC 01092: Variable: PKALTabDisp

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabdisp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabdisp.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PKALTabDisp

Variable: PKALTabDisp

Specifies the display mode of the column that is referenced in an alarm table.

| Definition | PKALTabDisp, String variable |
| --- | --- |
|  | ‘Text’ / ‘Graphic’ / ‘TextGraphic’ |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PKALTabDisp = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabhide.htm language=enus -->
## TOPIC 01093: Variable: PkAlTabHide

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabhide.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabhide.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTabHide

Variable: PkAlTabHide

Specifies whether DIAdem hides the alarm table as long as no messages are displayed.

| Definition | PkAlTabHide, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTabHide = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabrhauto.htm language=enus -->
## TOPIC 01094: Variable: PkAlTabRHAuto

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabrhauto.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabrhauto.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTabRHAuto

Variable: PkAlTabRHAuto

Specifies whether DIAdem specifies the row height in the alarm table automatically or uses the value of the PkAlTabRowHeight variable.

| Definition | PkAlTabRHAuto, Boolean variable |
| --- | --- |
|  | TRUE/FALSE |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTabRHAuto = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabrowheight.htm language=enus -->
## TOPIC 01095: Variable: PkAlTabRowHeight

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabrowheight.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabrowheight.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTabRowHeight

Variable: PkAlTabRowHeight

Specifies the row height in the alarm table.

| Definition | PkAlTabRowHeight, LongInteger variable |
| --- | --- |
|  | Unit: Pixel |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTabRowHeight = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabselcolor.htm language=enus -->
## TOPIC 01096: Variable: PkAlTabSelColor

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabselcolor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabselcolor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTabSelColor

Variable: PkAlTabSelColor

Specifies the color of the rows that are selected in the alarm table.

| Definition | PkAlTabSelColor, LongInteger variable |
| --- | --- |
|  | RGB color value |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTabSelColor = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabvar.htm language=enus -->
## TOPIC 01097: Variable: PkAlTabVar

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabvar.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabvar.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTabVar

Variable: PkAlTabVar

Specifies the alarm attribute that DIAdem displays in the column that is referenced.

| Definition | PkAlTabVar, String variable |
| --- | --- |
|  | Value range/Meaning |
|  | 'PkAlChn': Channel number |
|  | 'PkAlChnName': Channel name |
|  | 'PkAlType': Alarm type |
|  | 'PkAlValue': Actual value |
|  | 'PkAlRefValue': Limit value |
|  | 'PkAlUnit': Unit |
|  | 'PkAlCounter': Unit |
|  | 'PkAlName': Name |
|  | 'PkAlComment': Comment |
|  | 'PkAlGroup': Alarm group |
|  | 'PkAlPriority': Priority |
|  | 'PkAlState': Alarm status |
|  | 'PkAlTimeStamp': Time stamp |
|  | 'PkAlQuitLevel': Quit level |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTabVar = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltabwidth.htm language=enus -->
## TOPIC 01098: Variable: PKALTabWidth

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltabwidth.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltabwidth.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PKALTabWidth

Variable: PKALTabWidth

Specifies the relative width of the referenced column.

| Definition | PKALTabWidth, Real variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PKALTabWidth = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltimeauto.htm language=enus -->
## TOPIC 01099: Variable: PkAlTimeAuto

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltimeauto.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltimeauto.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTimeAuto

Variable: PkAlTimeAuto

Specifies whether DIAdem automatically adds a time stamp to an entry.

| Definition | PkAlTimeAuto, Boolean variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTimeAuto = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltimeout.htm language=enus -->
## TOPIC 01100: Variable: PkAlTimeOut

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltimeout.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltimeout.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTimeOut

Variable: PkAlTimeOut

Specifies the time in minutes, after which DIAdem automatically logs off a user.

| Definition | PkAlTimeOut, LongInteger variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTimeOut = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltimeoutflag.htm language=enus -->
## TOPIC 01101: Variable: PkAlTimeOutFlag

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltimeoutflag.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltimeoutflag.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTimeOutFlag

Variable: PkAlTimeOutFlag

Specifies whether DIAdem automatically logs off a user after a specific period of time.

| Definition | PkAlTimeOutFlag, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTimeOutFlag = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltxtclosed.htm language=enus -->
## TOPIC 01102: Variable: PkAlTxtClosed

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltxtclosed.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltxtclosed.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTxtClosed

Variable: PkAlTxtClosed

Specifies the label for the OK button if the entry window is closed.

| Definition | PkAlTxtClosed, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTxtClosed = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltxtcolor.htm language=enus -->
## TOPIC 01103: Variable: PkAlTxtColor

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltxtcolor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltxtcolor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTxtColor

Variable: PkAlTxtColor

Specifies the color of the label on the OK button.

| Definition | PkAlTxtColor, LongInteger variable |
| --- | --- |
|  | Color |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTxtColor = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltxtopen.htm language=enus -->
## TOPIC 01104: Variable: PkAlTxtOpen

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltxtopen.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltxtopen.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTxtOpen

Variable: PkAlTxtOpen

Specifies the label for the OK button.

| Definition | PkAlTxtOpen, String variable |
| --- | --- |
|  | Maximum 255 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTxtOpen = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltxtx.htm language=enus -->
## TOPIC 01105: Variable: PkAlTxtX

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltxtx.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltxtx.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlTxtX

Variable: PkAlTxtX

Specifies the horizontal label.

| Definition | PkAlTxtX, String variable |
| --- | --- |
|  | Maximum 255 characters |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlTxtX = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkaltype.htm language=enus -->
## TOPIC 01106: Variable: PkAlType

- bundle_id: `diadem`
- source_path: `gfsalarm/pkaltype.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkaltype.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlType

Variable: PkAlType

Specifies the alarm type for the alarm definition that is referenced by the index.

| Definition | PkAlType, String variable |
| --- | --- |
|  | "<", ">", "<=", ">=","=" |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlType = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsalarm/pkalunit.htm language=enus -->
## TOPIC 01107: Variable: PkAlUnit

- bundle_id: `diadem`
- source_path: `gfsalarm/pkalunit.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsalarm/pkalunit.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Alarm System](../gfsalarm/alarm_grundlagen.htm) > [Variables](../gfsalarm/alarm_variables_overview.htm) > Variable: PkAlUnit

Variable: PkAlUnit

Specifies the unit of the alarm definition that is referenced by the index.

| Definition | PkAlUnit, String variable |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: Call DACObjOpen(BlockName) PkAlUnit = Value Call DACObjClose(BlockName)You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsgraph/txtobj/txtobj_general_dialog.htm language=enus -->
## TOPIC 01108: Text Object Editor

- bundle_id: `diadem`
- source_path: `gfsgraph/txtobj/txtobj_general_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsgraph/txtobj/txtobj_general_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Text Object Editor

Text Object Editor

Use text objects to create text with paragraphs and characters that are in different formats. Use the **Decorations** function group [to create a text object](../../procpresent/text/procpres_textobject_insert.htm). DIAdem inserts the text object into the worksheet as a white rectangle. Double-click the white rectangle to open the text object. DIAdem opens the text object editor, where you enter and edit your text.

The toolbar of the text editor contains functions for cutting, copying, and pasting texts. The toolbar also contains functions for specifying the font, the font size, the font color, the text attributes, and the alignment of words or sections. Structure your text with list items and paragraphs.

You can use [DIAdem expressions](../../genpresent/genpresent/genreport_format.htm) within a text. DIAdem expressions can include [DIAdem variables](../../genas/genauto/genauto_programmvariables.htm), [user commands](../../genshell/genshell/genshell_user_commands.htm), [formula expressions](../../dlgcalculator/dlgcalculator/dlgformulacalc_dialog.htm) and text which DIAdem refreshes with the report. You must enclose the variable name or the Calculator expression in @@ characters in order to define a DIAdem expression.

|  | Note If you zoom in and out on text objects using object markers, you modify the text lines, not the size of the letters. If you enlarge a text object in the text editor, the text field is enlarged accordingly. You cannot rotate text objects. |
| --- | --- |

#### Context Menu of a Text Object

| Frame | Enabling/disabling the frame display |
| --- | --- |
| Transparent | Enabling/disabling the background color. |

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_can/dlganzeigeauswahlcan_dialog.htm language=enus -->
## TOPIC 01109: Display Options

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_can/dlganzeigeauswahlcan_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_can/dlganzeigeauswahlcan_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > [NI-CAN](../ni_can/nican_allgemein.htm) > Display Options

Display Options

Use this dialog box to specify the parameters that the MAX displays in the [Signal list](../ni_can/dlgmaxcan_dialog.htm), for the available and the selected signals.

| Msg. ID | Specifies whether the MAX displays the CAN message ID for the assigned signal as a hexadecimal in the signal list. |
| --- | --- |
| Interface | Specifies whether the MAX displays the CAN interface name (CAN node) to which the signal is assigned, in the signal list. |
| Message | Specifies whether the MAX displays the name of the CAN message that you specify in the MAX, in the signal list. The signals (message channels) are assigned to a CAN message. |
| Unit | Specifies whether the MAX displays the measurement unit in which the program acquires the signal data, in the signal list. |

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_can/dlgmaxcan_dialog.htm language=enus -->
## TOPIC 01110: MAX Signal List (NI-CAN)

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_can/dlgmaxcan_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_can/dlgmaxcan_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > [Measurement & Automation Explorer (MAX)](../ni_daq/nidaq_max.htm) > MAX Signal List (NI-CAN)

MAX Signal List (NI-CAN)

Use this dialog box to configure the inputs and outputs of various NI devices. The MAX (Measurement & Automation Explorer) is an easy-to-use configuration tool for most NI hardware and is installed automatically when the NI-DAQ driver library is installed. The CAN block in DIAdem DAC accesses the signals configured in the MAX.

#### Settings

| Available signals | Displays a list of all the CAN signals (message channels) that are defined in the MAX. The input block displays the input signals. The output block displays the output signals. |
| --- | --- |
| Name | Specifies the name of the signal that is defined in the MAX (message channel). |
| Selected signals | Displays signals selected in the MAX from the list of available CAN signals. By default all signals are enabled. The Signal Name column displays the signal name that is also used in the block diagram. |
| Enabled | Specifies whether the particular signal is activated during the measurement. |
| Signal Name | Specifies the name of the signal in DIAdem. DIAdem creates the name automatically when you add a CAN signal to the list of selected signals. The maximum name length is 16 characters. |
| Msg. ID | Specifies the CAN message ID for the assigned signal as a hexadecimal. |
| Interface | Specifies the CAN interface name (CAN node) to which the signal is assigned. |
| Message | Specifies the name of the CAN message that you specify in the MAX. The signals (message channels) are assigned to a CAN message. |
| Unit | Specifies the measurement unit in which the program acquires the signal data. |
| Cyclical output | Specifies whether the NI-CAN driver outputs all the signals that are selected in the dialog box, at a fixed rate. The hardware automatically outputs the CAN messages. This separates the data output on the CAN bus from the DIAdem output clock. |
| Output interval | Specifies the time interval in milliseconds in which the hardware outputs the respective CAN messages for cyclic output. For data output, the specified time interval must be lower than the output rate that is set in DIAdem. |
| Interrupt output | Specifies whether DIAdem enables interrupt output. To execute the interrupt output for the NI-CAN driver you must use the Measurement Mode Windows timing. |
| Up/Down | Changes the position of the selected channels in the list of selected signals. |
| Add | Copies selected signals from the list of available signals to the list of selected signals. |
| Remove | Removes signals from the list of selected signals. |
| New Entry | Creates a new entry in the signals list. |
| Display options | Specifies which parameters the MAX displays in the signal list. |
| Driver Options | Opens the dialog box where you configure the driver. |

#### Symbol Meanings

|  | The channel is defined in the MAX. You can measure and output this channel with DIAdem. |
| --- | --- |
|  | The channel was defined in the MAX. The Measurement mode is Windows timing. This means that all the channels in this driver have real-time capabilities. |
|  | The channel is not available, because the definition of the signal in the MAX is incorrect. You may not have assigned the signal to a CAN node, or the signal definition includes bits that overlap with other signals. |

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_can/nican_allgemein.htm language=enus -->
## TOPIC 01111: General Information on the CAN Driver in DIAdem

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_can/nican_allgemein.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_can/nican_allgemein.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > General Information on the CAN Driver in DIAdem

General Information on the CAN Driver in DIAdem

If you want to use the DIAdem CAN driver, you must install the NI-CAN device driver version 2.0 or later. After installing the NI-CAN device driver, use the NI [Measurement & Automation Explorer](../ni_can/dlgmaxcan_dialog.htm) (MAX) to configure the CAN signals. The MAX and the NI-CAN device driver are automatically installed together. Refer to the MAX Help for more information about configuring the signals.

The DIAdem CAN driver supports the following measurement modes:

- Acquisition and output of single values in [Software clock in the foreground](../ni_daq/nidaq_swtaktvg.htm)
- Acquisition and output of single values in the interrupt mode (only in connection with the "Windows Timing" measurement mode)
- Acquisition of data in the [Hardware clock](../ni_daq/nidaq_hwtakt.htm) measurement mode
- Cyclical output of CAN messages by the hardware, independent of the DIAdem output clock. This separates the output clock of the CAN messages from the DIAdem output clock. When you configure the output mode, the output clock of the CAN message must be higher than the related output clock in DIAdem.

For DIAdem to process the signals in a CAN message, you must assign the CAN messages to a CAN node during configuration in the MAX. You must assign every bit in a message to a signal, but you must not assign one bit to several signals. Otherwise, the MAX registers the signals from the CAN messages as false, and as not processed by the NI-CAN device driver. If you use these signals in a DIAdem measurement, DIAdem displays an error message.

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_can/nican_buffer.htm language=enus -->
## TOPIC 01112: Driver Options (NI-CAN)

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_can/nican_buffer.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_can/nican_buffer.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > [NI-CAN](../ni_can/nican_allgemein.htm) > Driver Options (NI-CAN)

Driver Options (NI-CAN)

Use this dialog box to configure the RTSI synchronization for NI-CAN boards.

#### Settings

| Active NI-DAQ driver | Specifies whether you use traditional NI-DAQ or NI-DAQmx. You cannot use traditional DAQ and DAQmx together. This setting applies to all NI-DAQ and NI-CAN block diagram items. |
| --- | --- |
| RTSI synchronization | Specifies that you can synchronize multiple NI-CAN boards for Hardware clock measurements. You can choose between the following synchronization modes: |
|  | No synchronization DIAdem does not synchronize the boards to each other. Boardclock synchronization This synchronization mode uses the RTSI bus (RTSI7) to synchronize the time bases of the individual boards with each other. This ensures that all the clock signals on the boards derive from the same time base and that the clock signals on the individual boards do not drift. Measurements that are spread over multiple boards which execute in the same DIAdem clock system, start together. To do this, each clock system uses an RTSI bus (RTSI0 … RTSI6). Synchronizing the time bases of the individual boards enables the user to run measurements with different sampling rates on different boards without the sampling times drifting apart. However, measurements with different sampling rates do not start together. Many PCI boards support this mode. Synchronized with PXI 10MHz timebase This synchronization mode synchronizes the time bases of the individual boards via the 10 MHz signal on the PXI backplane. The boards are synchronized and the measurements start as described in Boardclock synchronization.Only PXI boards support this synchronization mode. Synchronized with PXI Star This synchronization mode uses the PXI Star buses to synchronize the time bases of the individual boards with each other. The boards are synchronized and the measurements start as described in Boardclock synchronization.Only PXI boards support this synchronization mode. Scanclock synchronization This synchronization mode synchronizes the measurements on different boards via the scanclock signal of a board. The mode uses the PFI buses PFI0 to PFI6. Measurements with different sampling rates cannot be synchronized in this synchronization mode because the measurement synchronization on the different boards runs via the clock signal of the measurement. Synchronized with 10 Hz Resync (DAQ) You use this synchronization mode to synchronize a DAQCard with a PCMCIA-CAN board. The DAQCards do not have RTSI signals for synchronization. Therefore, the mode generates a 10 Hz signal on the DAQCard 0 counter and uses the signal as the Resync signal of the CAN board. Use the DAQ board to connect the following CAN board signals: DAQCard PCMCIA-CAN CTR0 RTSI1 PFI0 RTSI0 Synchronized with 10 Hz Resync (CAN) This synchronization mode synchronizes multiple NI-CAN boards. Connect all the RTSI buses of one board to the respective RTSI buses on the other board. This synchronization mode also can synchronize multiple series 1CAN boards. |
| No synchronization | DIAdem does not synchronize the boards to each other. |
| Boardclock synchronization | This synchronization mode uses the RTSI bus (RTSI7) to synchronize the time bases of the individual boards with each other. This ensures that all the clock signals on the boards derive from the same time base and that the clock signals on the individual boards do not drift. Measurements that are spread over multiple boards which execute in the same DIAdem clock system, start together. To do this, each clock system uses an RTSI bus (RTSI0 … RTSI6). Synchronizing the time bases of the individual boards enables the user to run measurements with different sampling rates on different boards without the sampling times drifting apart. However, measurements with different sampling rates do not start together. Many PCI boards support this mode. |
| Synchronized with PXI 10MHz timebase | This synchronization mode synchronizes the time bases of the individual boards via the 10 MHz signal on the PXI backplane. The boards are synchronized and the measurements start as described in Boardclock synchronization.Only PXI boards support this synchronization mode. |
| Synchronized with PXI Star | This synchronization mode uses the PXI Star buses to synchronize the time bases of the individual boards with each other. The boards are synchronized and the measurements start as described in Boardclock synchronization.Only PXI boards support this synchronization mode. |
| Scanclock synchronization | This synchronization mode synchronizes the measurements on different boards via the scanclock signal of a board. The mode uses the PFI buses PFI0 to PFI6. Measurements with different sampling rates cannot be synchronized in this synchronization mode because the measurement synchronization on the different boards runs via the clock signal of the measurement. |
| Synchronized with 10 Hz Resync (DAQ) | You use this synchronization mode to synchronize a DAQCard with a PCMCIA-CAN board. The DAQCards do not have RTSI signals for synchronization. Therefore, the mode generates a 10 Hz signal on the DAQCard 0 counter and uses the signal as the Resync signal of the CAN board. Use the DAQ board to connect the following CAN board signals: DAQCard PCMCIA-CAN CTR0 RTSI1 PFI0 RTSI0 |
| DAQCard | PCMCIA-CAN |
| CTR0 | RTSI1 |
| PFI0 | RTSI0 |
| Synchronized with 10 Hz Resync (CAN) | This synchronization mode synchronizes multiple NI-CAN boards. Connect all the RTSI buses of one board to the respective RTSI buses on the other board. This synchronization mode also can synchronize multiple series 1CAN boards. |

|  | Note You can synchronize the CAN driver only with DAQmx via RTSI. Therefore, you cannot select RTSI synchronization for the NI-CAN block if you select Traditional NI-DAQ as the Active NI-DAQ driver. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_daq/dlganzeigeauswahl_dialog.htm language=enus -->
## TOPIC 01113: Display Options

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_daq/dlganzeigeauswahl_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_daq/dlganzeigeauswahl_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > [NI-DAQ](../ni_daq/nidaq_allgemein.htm) > Display Options

Display Options

Use this dialog box to specify the parameters that the MAX displays in the [Signal list](../ni_daq/dlgmax_dialog.htm), for the available and the selected signals.

| Channel | Specifies whether the MAX displays the terminal number on the hardware, in the signal list. |
| --- | --- |
| Device | Specifies whether the MAX displays the device number of the channel that you assign to the device in the MAX, in the signal list. |
| Device type | Specifies whether the MAX displays the device name in the signal list. The device type enables you to identify channels if various devices are installed. |
| Sensor type | Specifies whether the MAX displays the sensor type in the signal list. |

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_daq/dlgmax_dialog.htm language=enus -->
## TOPIC 01114: MAX Signal List (NI-DAQ)

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_daq/dlgmax_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_daq/dlgmax_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > [Measurement & Automation Explorer (MAX)](../ni_daq/nidaq_max.htm) > MAX Signal List (NI-DAQ)

MAX Signal List (NI-DAQ)

Use this dialog box to configure the inputs and outputs of various NI devices. The MAX (Measurement & Automation Explorer) is an easy-to-use configuration tool for most NI hardware and is installed automatically when the NI-DAQ driver library is installed. The DAQ block in DIAdem DAC accesses the signals configured in the MAX.

#### Settings

| Available signals | Displays all the signals that are defined in the MAX. The input block displays the input signals. The output block displays the output signals. |
| --- | --- |
| Name | Specifies the name of the signal that is defined in the MAX. |
| Selected signals | Displays the signals that are selected in the MAX from the list of available signals. By default all signals are enabled. The Signal Name column displays the signal name that is also used in the block diagram. |
| Enabled | Specifies whether the particular signal is activated during the measurement. |
| Signal Name | Specifies the name of the signal in DIAdem. DIAdem creates the name automatically when you add a signal to the list of selected signals. The maximum name length is 16 characters. |
| Channel | Specifies the terminal number for the selected signal on the hardware. |
| Device | Specifies the name of the device in the MAX that the signal is assigned to. |
| Device type | Specifies the device or board type of the hardware used. |
| Sensor type | Specifies which sensor type is set in the MAX for the channel. |
| Interrupt output | Specifies whether Interrupt output is activated. |
| Up/Down | Changes the position of the selected channels in the list of selected signals. |
| Add | Copies selected signals from the list of available signals to the list of selected signals. |
| Remove | Removes signals from the list of selected signals. |
| New Entry | Creates a new entry in the signals list. |
| Counter | Opens the dialog box where you configure counter channels. |
| Display options | Specifies which parameters the MAX displays in the signal list. |
| Driver Options | Opens the dialog box where you configure the driver. |

#### Symbol Meanings

|  | The channel is defined in the MAX. You can measure and output this channel with DIAdem. |  |
| --- | --- | --- |
|  | The channel is defined in MAX and is based on real-time hardware. Note In MAX, do not select a calibration. The hardware must support realtime data acquisition. |  |
|  | Note In MAX, do not select a calibration. The hardware must support realtime data acquisition. |  |
|  | The channel was defined in the MAX. The Measurement mode is Windows timing. This means that all the channels in this driver have real-time capabilities. |  |
|  | The channel was defined and configured in the NI-DAQ driver. You can measure and output this channel with DIAdem. The channel has no realtime capability. |  |
|  | The channel is not available, because the definition of the signal in the MAX is incorrect. The respective device might not be connected to the port or an input is not assigned to a device. |  |
|  | The channel is connected to a TEDS (Transducer Electronic Data Sheet). DIAdem saves the following data from the TEDS when measuring channel properties. Property Data type Description NI_Sensor_TEDSManufacturerID DataTypeInt32 Manufacturer ID of the sensor NI_Sensor_TEDSManufacturer DataTypeString Manufacturer's name of the sensor NI_Sensor_TEDSModelID DataTypeInt32 Model number of the sensor NI_Sensor_TEDSVersionNumber DataTypeInt32 Version number of the sensor NI_Sensor_TEDSVersionLetter DataTypeString Label with the version number of the sensor NI_Sensor_TEDSSerialNumber DataTypeInt32 Serial number of the sensor NI_Sensor_TEDSType DataTypeString Electrical signal type of the transducer NI_Sensor_TEDSCalibrationDate DataTypeDate Calibration date NI_Sensor_TEDSCalibrationPeriod DataTypeInt32 Calibration duration (days) NI_Sensor_TEDSCalibrationInitials DataTypeString Calibration initials NI_Sensor_TEDSMeasurementLocationID DataTypeInt32 Measurement location ID |  |
| Property | Data type | Description |
| NI_Sensor_TEDSManufacturerID | DataTypeInt32 | Manufacturer ID of the sensor |
| NI_Sensor_TEDSManufacturer | DataTypeString | Manufacturer's name of the sensor |
| NI_Sensor_TEDSModelID | DataTypeInt32 | Model number of the sensor |
| NI_Sensor_TEDSVersionNumber | DataTypeInt32 | Version number of the sensor |
| NI_Sensor_TEDSVersionLetter | DataTypeString | Label with the version number of the sensor |
| NI_Sensor_TEDSSerialNumber | DataTypeInt32 | Serial number of the sensor |
| NI_Sensor_TEDSType | DataTypeString | Electrical signal type of the transducer |
| NI_Sensor_TEDSCalibrationDate | DataTypeDate | Calibration date |
| NI_Sensor_TEDSCalibrationPeriod | DataTypeInt32 | Calibration duration (days) |
| NI_Sensor_TEDSCalibrationInitials | DataTypeString | Calibration initials |
| NI_Sensor_TEDSMeasurementLocationID | DataTypeInt32 | Measurement location ID |

|  | Note If you do not have administrator rights, you only can connect a USB device to a terminal that a user with administrator rights previously connected this USB device to. Otherwise the device is installed again and Windows saves the USB hub and the USB port in addition to the driver. You must have administrator rights to install this device. |
| --- | --- |

|  | Note The driver always needs an NI-DAQmx installation. This also applies when you use a traditional NI-DAQ. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_daq/nidaq_allgemein.htm language=enus -->
## TOPIC 01115: NI-DAQ and DIAdem Components

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_daq/nidaq_allgemein.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_daq/nidaq_allgemein.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > NI-DAQ and DIAdem Components

NI-DAQ and DIAdem Components

In order for DIAdem to work with NI-DAQ hardware in a measurement system, you require the following components:

##### Device

All boards that are linked to the computer via interfaces, are called devices. The devices are plug-in boards installed on a computer (PCI or ISA bus), PC-Card boards for the PC-Card interface, and external devices that you connect via standard interfaces such as USB or the printer port. You must install devices correctly to be able to make settings and to execute measurements.

##### NI-DAQ

The NI-DAQ is supplied with the device. You must install Version 6.9 or later. You can use the MAX (Measurement and Automation Explorer) configuration program, which is installed with the NI-DAQ, to configure the hardware and to execute function tests. You need MAX Version 2.0 or later.

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_daq/nidaq_counter.htm language=enus -->
## TOPIC 01116: Counter

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_daq/nidaq_counter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_daq/nidaq_counter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > [NI-DAQ](../ni_daq/nidaq_allgemein.htm) > Counter

Counter

Use this dialog box to define and set parameters for counter channels of the measurement hardware. You can then use the driver to execute event counting and frequency measurements, period duration measurements, and pulse width measurements.

#### Settings

| Available counters | Specifies all the defined counter channels. |
| --- | --- |
| Name | Specifies the name of the counter channel. |
| Device | Specifies the number that the MAX has assigned to the device. |
| Counter | Specifies the number of the counter that you use for the measurement. The number of counters depends on the hardware. |
| Measurement drive | Specifies the type of measurement. |
| Input signal | Specifies the board input to which the signal to be measured is connected. You can choose from signals PFI0 to PFI39. On some hardware, you cannot assign the counter input to all the input signals. Refer to the hardware documentation for more information. |
| Control input | Specifies the control input. You can use the control input to control the counter via an external signal, and specify that the counter only counts under specific conditions. If you select Unused, DIAdem counts all the incoming impulses. Which signals DIAdem uses to control the counter depends on the hardware. Refer to the hardware documentation for more information. |
| Polarity | Specifies which slope the counter responds to. If you select the rising slope, the counter responds to the rising slope, which is a level of the input signal or of the control signal that corresponds to a logical one. If you select falling slope, the counter responds to the falling slope, which means to a signal that is corresponds to a logical zero. |
| Gate time | Specifies the time that the driver requires to determine the frequency that is to be measured. The longer the gate time, the greater the accuracy of the frequency measurement. |
| Counter frequency | Specifies the counter frequency of the internal counter for period length measurements and for pulse width measurements. The higher the counter frequency, the more precise the measurement. If the internal counter overflows, the driver returns a NoValue. |
| Counting | Specifies the direction the counter counts in. If you set Hardware-controlled, the polarity of an external signal defines the counting direction. Refer to the hardware documentation for more information. |
| Counter | Generates a new counter definition. You can configure the same counter multiple times for different tasks. However, you only can use each counter once when you select signals in a measurement. A frequency measurement requires two consecutive counters. |
| Delete counter | Deletes the selected counter. |

|  | Note You only can use the Counter dialog box if you first select Traditional NI-DAQ as the active NI-DAQ driver in the Driver options dialog box. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsnidaq/ni_daq/nidaq_swtaktvg.htm language=enus -->
## TOPIC 01117: Measurement Types: Software Clock with Windows Timing

- bundle_id: `diadem`
- source_path: `gfsnidaq/ni_daq/nidaq_swtaktvg.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/ni_daq/nidaq_swtaktvg.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[NI DAQ/NI CAN](../nidaqcan_overview.htm) > [Measurement Modes](../ni_daq/nidaq_messarten.htm) > Measurement Types: Software Clock with Windows Timing

Measurement Types: Software Clock with Windows Timing

In the Software clock with Windows timing measurement mode the Windows system generates the clock. This measurement mode processes analog and digital values synchronously. In the Windows timing measurement mode, you can run measurements with almost all types of hardware and with many different devices simultaneously.

You can run measurements with different sampling rates simultaneously on one device. DIAdem requests the measurement values from the hardware at the clock rate that Windows generates. DIAdem processes the measured values and displays the results, or outputs values from the open and closed loop control signals.

Because other programs or the internal Windows management can all access the operating system, Windows is not very reliable in maintaining the clock rate. If you do not use the computer for other activities, you can prevent this behavior.

|  | Note For many measurements the Software clock with Windows timing is sufficient. Especially if the data is saved with a real-time reference axis. Even if the sampling rate is not exactly adhered to, you get the exact time stamp of each measurement value. When open-loop or closed-loop control values are output for slow processes, or data is linked manually, the clock rate does not have to be accurate. The Software clock with Windows timing measurement mode is unsuitable for processes that require guaranteed reaction times. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsnidaq/nidaqcan_overview.htm language=enus -->
## TOPIC 01118: NI DAQ/NI CAN

- bundle_id: `diadem`
- source_path: `gfsnidaq/nidaqcan_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsnidaq/nidaqcan_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

NI DAQ/NI CAN

NI DAQ/NI CAN

The subordinate topics contained in the tree on the contents tab of the Help describe NI DAQ and NI CAN drivers.

<!--NI_TOPIC bundle=diadem path=gfsopc/errorhandling_opc/errorcodes_opc.htm language=enus -->
## TOPIC 01119: Error Codes for the Variable OPCErrorCode

- bundle_id: `diadem`
- source_path: `gfsopc/errorhandling_opc/errorcodes_opc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/errorhandling_opc/errorcodes_opc.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Error Codes for the Variable OPCErrorCode

Error Codes for the Variable OPCErrorCode

| eOPCAuto_Ok=0 | No error. |
| --- | --- |
| eOPCAuto_GeneralError=1 | General error. |
| eOPCAuto_BlockMapEntryNotFound=2 | No entry for the signal and device specification found in the driver blockmap. |
| eOPCAuto_UnidentifiedBlocktype=3 | Invalid block type (no DAC input or output block open). |
| eOPCAuto_OPCBlockNotOpen=4 | No DAC block opened with DACObjOpen. |
| eOPCAuto_InvalidSignalIndex=5 | The signal index is invalid (valid values: 1 ... 255). |
| eOPCAuto_InvalidLogReset=6 | Invalid value for the logfile reset time. |
| eOPCAuto_InvalidReportVerbosity=7 | Invalid value for type and extent of information to be recorded. |
| eOPCAuto_ProgIDNotInLocalRegistry=8 | The ProgID that was transferred was not found in the local registry (The server named by the ProgID is not registered locally). |
| eOPCAuto_ServerNotConnected=9 | The OPC server is not connected. |
| eOPCAuto_DataConversionFail=10 | Data conversion is impossible. |
| eOPCAuto_InvalidErrorAction=11 | The value provided for the error reaction is invalid. |
| eOPCAuto_InvalidDACSigListLen=12 | The length of the DAC signal list specified in the block is invalid. |
| eOPCAuto_InvalidServerName=13 | No valid name specified for an OPC server. |
| eOPCAuto_NotImplemented=14 | The function not implemented. |
| eOPCAuto_RemoteConnectWithoutClassID=15 | You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. To access the remote server without registering it locally, transfer the ClassID to the OPCSrvConnect command. |
| eOPCAuto_ArrayAccesNotAllowed=16 | Arrays cannot be accessed with this function. |
| eOPCAuto_NoMoreHandles=17 | You cannot create or manage further OPC objects in the script area, because too many objects already exist. |
| eOPCAuto_InvalidServerHandle=18 | The server handle provided for the function is invalid. |
| eOPCAuto_InvalidGroupHandle=19 | The group handle provided for the function is invalid. |
| eOPCAuto_InvalidItemHandle=20 | The item handle provided for the function is invalid. |
| eOPCAuto_ConnectTimeout=21 | Timeout occurred while connecting to OPC server. Either the server is inaccessible (for example over the network) or a proxy-DLL is not registered (op.dl or op_PS.dl). |
| eOPCAuto_CallTimeout=22 | A timeout occurred while an OPC server function was being called. |
| eOPCAuto_NoIOPCServer=23 | No IOPCServer interface at OPC/server. |
| eOPCAuto_NoIOPCItemMgt=24 | No IOPCItemMgt interface at OPC/server. |
| eOPCAuto_NoIOPCSyncIO=25 | No IOPCSyncIO interface at OPC/server. |
| eOPCAuto_NoIOPCGroupStateMgt=26 | No IOPCGroupStateMgt interface at OPC/server. |
| eOPCAuto_InvalidItemNo=27 | The number of items is invalid or you have tried to include more items than allowed in an OPC group. |

<!--NI_TOPIC bundle=diadem path=gfsopc/errorhandling_opc/errorhandling_opc.htm language=enus -->
## TOPIC 01120: OPC Error Handling

- bundle_id: `diadem`
- source_path: `gfsopc/errorhandling_opc/errorhandling_opc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/errorhandling_opc/errorhandling_opc.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Error Handling

OPC Error Handling

You must use the variables OPCErrorCode, OPCHResult, and aOPCItemError to recognize and to handle errors, because script commands which you use to access an OPC server, do not work with message boxes. The DIAdem variable [OPCErrorCode](../../varonl/opcerrorcode.htm) indicates after an OPC script command call whether DIAdem executed the command. The value 0 indicates that no error has occurred.

When the appropriate function at the OPC user interface has been called, the DIAdem variable [OPCHResult](../../varonl/opchresult.htm) contains the HRESULT code of the function. The value 0 (S_OK) indicates that DIAdem processed the command. A value of 1 (S_False) indicates that the command has only been partly completed. In this case, information about the items is located in aOPCItemError. Other values show that the action failed. See also the OPC documentation on the individual functions.

If an OPC function results in S_FALSE, (OPCHResult=S_FALSE), you can ascertain problems with individual items with the item-related error codes in the [aOPCItemError](../../varonl/aopcitemerror.htm) variable.

#### Method

1. Call the script command, for example OPCAddItems.
2. Check the variable OPCErrorCode:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If OPCERRORCODE=0 Then
'The related opc command was called.
Else
'The related opc command was not called. See list of error codes
End If
```

[Copy script](javascript:void(0);)

```text
if OPCERRORCODE==0 : 
#The related opc command was called.
else: 
#The related opc command was not called. See list of error codes
```

1. When you have completed the OPCErrorCode check successfully, you can determine the HRESULT code over the OPCHResult variable and start further actions.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Select Case OPCHRESULT
Case 0
   Call MSGBOXDISP("The opc command was successfully executed.) 
Case 1
   T1="The opc command was successfully executed in parts" 
   T1=T1+" (aOPCItemError evaluate!)." 
   Call MSGBOXDISP(T1) 
Case Else
   Call MSGBOXDISP("Error when executing opc command.") 
End Select
```

[Copy script](javascript:void(0);)

```text
select_variable_0 = OPCHRESULT 
if (select_variable_0 == 0) : 
    dd.MSGBOXDISP("The opc command was successfully executed.) 
elif (select_variable_0 == 1) : 
    dd.T1="The opc command was successfully executed in parts" 
    dd.T1=T1+" (aOPCItemError evaluate!)." 
    dd.MSGBOXDISP(dd.T1) 
else: 
    dd.MSGBOXDISP("Error when executing opc command.") 
```

1. Some OPC functions provide error codes for each included OPC item. You can call these error codes over the aOPCItemError field.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call OPCADDITEMS(OPCGRPHANDLE, 2) 
If OPCERRORCODE=0 Then
   ' The related opc command was called. 
Select Case OPCHRESULT
Case 0
Case 1
L1=1 
Do While L1<=2
   If AOPCITEMERROR(L1)=0 Then
      T1="Item "+AOPCITEMID(L1) 
      T1=T1+"successfully inserted in the group" 
      Call MSGBOXDISP(T1) 
   Else
      T1="When inserting the item "+AOPCITEMID(L1) 
      T1=T1+" an error occurred." 
      Call MSGBOXDISP(T1) 
   End If
   L1 = L1 + 1 ' <<< Step 1 or Step -1 
Loop
Case Else
End Select
Else
   'The related command was not called. See list of error codes.
End If
```

[Copy script](javascript:void(0);)

```text
OPCADDITEMS(OPCGRPHANDLE, 2) 
if OPCERRORCODE==0 : 
# The related opc command was called. 
    select_variable_0 = OPCHRESULT 
    if (select_variable_0 == 0) : 
    elif (select_variable_0 == 1) : 
        L1=1 
        while Do : 
            if AOPCITEMERROR(dd.L1)==0 : 
                dd.T1="Item "+AOPCITEMID(dd.L1) 
                dd.T1=T1+"successfully inserted in the group" 
                dd.MSGBOXDISP(dd.T1) 
            else: 
                dd.T1="When inserting the item "+AOPCITEMID(dd.L1) 
                dd.T1=T1+" an error occurred." 
                dd.MSGBOXDISP(dd.T1) 
            dd.L1 = dd.L1 + 1 # <<< Step 1 or Step -1 
    else: 
else: 
#The related command was not called. See list of error codes.
```

1. Use the commands [OPCClear](../../comonl/opcclear.htm), [OPCClearServer](../../comonl/opcclearserver.htm), and [OPCClearGroup](../../comonl/opccleargroup.htm) to help with error handling.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcaccepteddatatypes.htm language=enus -->
## TOPIC 01121: Using OLE Data Types in DIAdem DAC

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcaccepteddatatypes.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcaccepteddatatypes.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Using OLE Data Types in DIAdem DAC

Using OLE Data Types in DIAdem DAC

In DIAdem DAC you can acquire and output the following OLE data types with OPC blocks:

#### Read Blocks

- Simple numeric data types (VT_I2, VT_I4, VT_R8 and so on) that are transferred as values
- Simple numeric data types that are transferred as reference (VT_I2 | VT_BYREF, VT_I4 | VT_BYREF, VT_R8 | VT_BYREF and so on)
- Strings, if the OPC server transfers these texts as VT_BSTR and if the Windows function VariantChangeType can convert these strings to VT_R8 (double).

If the OPC server provides strings in formats that the Windows function VariantChangeType cannot convert to VT_R8 (double), the measurement aborts.

#### Write Blocks

If the blocks are write blocks, the OPC server must interpret the data adequately. DIAdem always writes the values with the data type VT_R8 (double) to the OPC server. If OPC servers do not accept the data type VT_R8 (double), contact the manufacturer of your OPC server for support.

The identifiers for the data types (VT_UI2: Unsigned Integer 2 Byte and so on) have been taken from the Microsoft OLE documentation.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcarray.htm language=enus -->
## TOPIC 01122: OPC - Items that Provide Data as Arrays

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcarray.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcarray.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC - Items that Provide Data as Arrays

OPC - Items that Provide Data as Arrays

In an OPC input block, you can assign signals to OPC items that return their data in arrays. Because arrays contain several elements, you must specify which field element each signal gets its data from. You assign a signal to a field element by giving the signal an index. There are two different ways to index signals: If you double-click the signal, you open the [Define New Signal](../opc/hid_opcsignaldefinition.htm) dialog box where you can specify an index for each signal individually, or select the **Edit** function from the [Signal list](../opc/hid_opcsiglist.htm) context menu. You also can specify indexes for a group of signals if you select a group of signals in the [Signal list](../opc/hid_opcsiglist.htm) and select **Set indexes** from the context menu.

|  | Note In output blocks, you must not use any OPC items that expect their data as arrays. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opccommunicationmode.htm language=enus -->
## TOPIC 01123: Transfer Mode

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opccommunicationmode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opccommunicationmode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Transfer Mode

Transfer Mode

For data transfer between the OPC server and the OPC client you can select the synchronous or asynchronous transfer mode.

#### Synchronous Transfer

The OPC client (DIAdem) sends a command for reading or writing data to the OPC server and waits until the server has done the operation. During this time the measurement is blocked which means that DIAdem does not read in values, does not calculate values, and does not output values. The length of this time depends on the implementation of the OPC server. If the server accesses the data, for example, via a serial interface, this process can last some seconds.

The advantage of synchronous data transfer lies in the fact that read OPC blocks always return current measurement values. Read blocks do not end their actions until the OPC server receives the values.

#### Asynchronous Transfer

The OPC client (DIAdem) sends a read or write command to the OPC server. The OPC client (DIAdem) does not wait until the read or write operation is finished. Instead, the OPC server informs the OPC client (DIAdem) of the results of the action later, for example, input measured values or status of the writing operation.

Between the sending of the command and the arrival of the results from the OPC server, the DAC measurement core continues working. The driver uses internal measured value buffers to respond sufficiently and without delay to all the inquiries for inputs and outputs from the DAC measurement core.

#### Read OPC Blocks

If you use read blocks, the OPC driver responds to the DAC requests for new values by reading out the measured values from the internal measurement value buffer. DIAdem always receives the last measurement value that the server wrote into the buffer. All measurement values have an age that corresponds with the update rate of the OPC block.

If the clock rate set in the DAC clock block is smaller than the update rate in the OPC block, measurement values are lost. If the opposite is the case, (rate in clock block > update rate in the OPC block), the DAC measurement core receives the same measured value several times in succession.

#### Write OPC Blocks

If you use a write block, the driver transfers the measured values to the OPC server in every DAC cycle, without waiting for the server to confirm the success of the output operation. The OPC server later informs the driver of the success or failure of the writing procedure and can then react accordingly if an error occurs.

If a write OPC block has asynchronous data transfer, you must enter a DAC clock rate that is not smaller than the time an OPC server requires to complete and confirm a writing requirement. Otherwise, the writing requests lead to a jam in the OPC server, because the server cannot finish writing jobs before new requests arrive.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcdeletesignals.htm language=enus -->
## TOPIC 01124: Deleting Signals

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcdeletesignals.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcdeletesignals.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Deleting Signals

Deleting Signals

If you remove signals at the end of the signal list, DIAdem shortens the signal list accordingly. If you delete signals at other positions in the signal list, DIAdem marks the entries in the signal list invalid.

|  | Note A block diagram can contain references to signal names, at different places. These references become invalid if you delete the respective signals. When a measurement starts, error messages appear if you deleted signals that are still required in the block diagram. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcfaq.htm language=enus -->
## TOPIC 01125: OPC: Frequently Asked Questions

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcfaq.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcfaq.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC: Frequently Asked Questions

OPC: Frequently Asked Questions

#### Is the term OPC a synonym for field bus?

OPC is not a field bus, it is a communication standard between two programs and is based on OLE. OPC stands for Open Platform Communication (formerly: OLE for Process Control). Most applications that use this communication standard are in the automation and the process control. You usually use [OPC Servers](../opc/hid_opcserver.htm) to acquire and to output data in field bus systems, for example, profibus or interbus, with Windows applications.

The type of data exchange with OPC is similar to the DDE data exchange. DDE is a standardized form of data exchange between Windows applications whereby in special cases DDE servers also acquire field bus data. An OPC server fulfills the same function for the Windows application. The OPC server acquires data, for example, in a field bus and transfers this data to the application.

#### What is the DCOM configuration?

The DCOM configuration in Windows is where you or your system administrator specify how your OLE client applications can access other OLE servers. OPC is based on OLE technology. If you cannot find your OPC server with DIAdem, check the settings of the DCOM configuration. You can find the respective program under DCOMCNFG.EXE.

#### Why is the OPC block dimmed in the DIAdem DAC function group?

Check whether the GfSOPC-DLL is marked "not loaded" in the GPI-DLL registration although the DLL is in the specified folder. Possible causes are:

- You registered the GfSOPC.DLL under **Settings»Extensions»GPI Extensions**. You must not register the GfSOPC.DLL as GPI-DLL.
- Copy the GfSOPC.DLL into the DIAdem program folder. This problem can only occur in the GfSOPC.DLL of the 6.00 DIAdem version.

#### Why does my system get stuck when a certain OPC server is selected?

Windows cannot find the OPC server. If another computer executes the OPC server, the network search might last a while. You can operate DIAdem again after a timeout. Specify the timeout in the [Settings for OPC Server](../opc/hid_opcserversettings.htm) dialog box.

#### What does the message that an OPC server is not accessible mean?

First check with another OPC client on your computer whether you can access the OPC server. You can find clients on the Internet free of charge or on the CDs from the manufacturer of the OPC server. If you cannot establish connection to another client either, you might have registered the server incorrectly or you made incorrect settings in the DCOM configuration.

#### Which OPC specification does DIAdem support?

The driver supports in its current version the OPC specifications Data Access 1.0A and Data Access 2.0.

#### The program crashes when DIAdem closes (runtime error)

If DIAdem uses blocks with asynchronous data transfer, the program might crash when DIAdem finishes (runtime error).

1. This problem can occur when the OPC Client (DIAdem) calls functions of the OPC server asynchronously and the OPC server runs on a remote computer. Asynchronous data transfer means that the OPC server sends a message to the OPC client to inform about changes to data or the occurrence of an event. The OPC server requests a so-called callback function of the OPC client. This is only possible if the safety settings of the OPC server are set accordingly in the DCOM configuration. The respective setting is in the DCOM configuration of the computer on which the OPC server is active. Select the **Interactive user** setting on the **Identity** tab in the OPC server properties. You also can specify that the OPC server is executed with the same name and same password with which you are logged into the computer with the OPC client.

2. Some OPC servers do not correctly release the OLE interfaces used for asynchronous data transfer. This applies to OPC servers that are not implemented as required by the Microsoft OLE documentation. Contact your OPC server manufacturer or disable the option for asynchronous communication.

#### The program crashes after the connection to an OPC server was lost

Complete the following steps to prevent the link to the OPC server from failing:

- Ensure that your network is running smoothly.
- Do not close the OPC server manually. DIAdem automatically closes the OPC server when the program no longer requires the server.
- Do not close the OPC server with the Task Manager.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcgeneral.htm language=enus -->
## TOPIC 01126: General Properties of the Driver

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcgeneral.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcgeneral.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > General Properties of the Driver

General Properties of the Driver

Use this dialog box to make general settings for the OPC server. These settings apply to all OPC blocks.

#### Settings

| Terminate OPC server always after measurement/configuration. | Specifies that DIAdem ends all OPC servers immediately when the server is not required anymore. |
| --- | --- |
| Keep OPC server running | Specifies that DIAdem establishes connection to all OPC servers when loading the block diagram. DIAdem maintains connection to the OPC servers until you delete in a block diagram the last block that references the OPC server, until you delete the entire block, or until you finish DIAdem. |
| Validate items automatically | Specifies that DIAdem checks whether the ItemId of a signal definition is valid. The validation is not possible when a OPC server cannot start. If the driver cannot establish connection to the OPC server, you receive a message which asks whether you want to validate, before the signal validation. If you enable validation, DIAdem executes the validation without a further prompt. Therefore ensure that all OPC servers that are used in the block diagram during validation are accessible. |
| Write logfile | Specifies that DIAdem writes a logfile. The logfile records the communication between DIAdem and the OPC servers. |
| Logfile name | Opens the dialog box where you specify the name of the logfiles. |
| Logfile Name | Specifies the name of the logfile. |
| Protocol Length | Opens the dialog box where you specify the length of the logfiles. |
| Logfile Reset | Resets the logfile. |
| Logfile reset | Executes the reset. |
| About | Opens the dialog box that contains general information about the OPC client. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcindexing.htm language=enus -->
## TOPIC 01127: Indexing Signals

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcindexing.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcindexing.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Indexing Signals

Indexing Signals

Use this dialog box to assign indexes for accessing field elements to a selected signal group.

| Use indexing | Specifies whether the selected signal group uses the field indexing in a following measurement. |
| --- | --- |
| Index direction | Specifies whether to assign indexes to the selected signal group in rising or falling order, beginning at the start index. |
| Start index | Specifies where the indexing of the selected signal group starts. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcinpblock.htm language=enus -->
## TOPIC 01128: OPC Driver (Input)

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcinpblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcinpblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Driver (Input)

OPC Driver (Input)

Use this dialog box to configure an OPC input block. The dialog box has the following functions:

- Assigns an [OPC server](../opc/hid_opcserver.htm) to the block.
- Displays and edits the [Signal list](../opc/hid_opcsiglist.htm) of the block.
- Displays the [Tree display](../opc/hid_opcpagebrowser.htm) for the server address space.
- Specifies the block parameters.
- Access to [Settings for the OPC Server](../opc/hid_opcserversettings.htm) and to [the General Properties](../opc/hid_opcgeneral.htm), that apply to the entire OPC driver.

#### Settings

| Signal List | Specifies the assignment of buses in the block diagram to sources that provide measurement values. |
| --- | --- |
| Symbol bar | The signal bar is above the signal list and provides functions for the signal list. |
| Context menu for the signal list | Contains functions for the signal list. |

|  | Note For more information on the tabs of this dialog box, refer to the OPC Input / Output Block: Browser Tab , OPC Input Block: Parameter Tab and the OPC Input Block: OLE Tab pages. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcinsertsignals.htm language=enus -->
## TOPIC 01129: Inserting Signals

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcinsertsignals.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcinsertsignals.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Inserting Signals

Inserting Signals

If the signal list does not contain invalid entries, DIAdem appends signals to the end of the signal list. If the signal list contains invalid entries, DIAdem assigns the new signal definitions to the invalid entries. If DIAdem has filled all invalid entries, the signal list adds new signal definitions to the end of the list.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcitem.htm language=enus -->
## TOPIC 01130: OPC Item

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcitem.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcitem.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Item

OPC Item

An OPC item is a data source (input) or a data sink (output) on an [OPC server](../opc/hid_opcserver.htm). You can read data from these items during a DAC measurement ([input block](../opc/hid_opcoutpblock.htm)) or you can write data to these items ([output block](../opc/hid_opcinpblock.htm)).

An item is identified on the OPC server by its itemID. ItemIDs are usually character strings from which the meaning of the item is apparent. The itemIDs are defined in the OPC server and cannot be altered by the OPC client program (DIAdem). An OPC client must use the Browser interface of a server to determine which item the server has.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opclogfile.htm language=enus -->
## TOPIC 01131: Configure Report Length

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opclogfile.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opclogfile.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Configure Report Length

Configure Report Length

Use this dialog box to specify which messages DIAdem records in the logfile.

#### Settings

| Error | DIAdem only reports the errors that cause the measurement to terminate. |
| --- | --- |
| Warnings | DIAdem displays warnings about problems during a measurement, which do not necessarily lead to a measurement termination. |
| Information | DIAdem records general information about the measurement. |
| Preparing for a measurement | DIAdem records information about the progress of the measurement preparations for OPC blocks. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opconmeasstart.htm language=enus -->
## TOPIC 01132: Behavior at Start of Measurement

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opconmeasstart.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opconmeasstart.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Behavior at Start of Measurement

Behavior at Start of Measurement

You can specify in the general settings of the OPC driver when DIAdem starts the OPC server in the block diagram:

- DIAdem starts all OPC servers at the beginning of a measurement and saves the servers after the measurement stops (default), until you delete the block diagram or exit DIAdem.
- DIAdem starts all OPC servers at the beginning of a measurement and deletes the servers after the measurement from the memory ( Terminate OPC server always after measurement/configuration enabled).
- DIAdem starts all OPC servers when loading the block diagram and removes the servers from the memory when deleting the block diagram or when finishing ( Keep OPC server running enabled).

If DIAdem starts the servers at the beginning of a measurement, the servers might not return measurement values when the first measurement value is acquired. The OPC servers usually display this status with the values "OPC_QUALITY_BAD" or "OPC_QUALITY_UNCERTAIN", which are set by the OPC Foundation. DIAdem interprets these values as errors during data acquisition. Depending on the settings these errors lead to a termination of the measurement or to a transfer of NoValues at the DAC inputs.

If you select **Abort measurement** as your error reaction, you cannot start the reading of the measured values because the OPC server always displays "OPC_QUALITY_BAD" or "OPC_QUALITY_UNCERTAIN" for the first few measured values. You also can specify that DIAdem waits for a certain period before starting to acquire data, so the OPC server has time to complete all the initialization tasks. Make the settings on the [Parameter](../opc/hid_opcpageparaminput.htm) tab.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcoutpblock.htm language=enus -->
## TOPIC 01133: OPC Driver (Output)

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcoutpblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcoutpblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Driver (Output)

OPC Driver (Output)

Use this dialog box to configure an OPC output block. The dialog box has the following functions:

- Assigns an [OPC server](../opc/hid_opcserver.htm) to the block.
- Displays and edits the [Signal list](../opc/hid_opcsiglist.htm) of the block.
- Displays the [Tree display](../opc/hid_opcpagebrowser.htm) for the server address space.
- Specifies the block parameters.
- Access to [Settings for the OPC Server](../opc/hid_opcserversettings.htm) and to [the General Properties](../opc/hid_opcgeneral.htm), that apply to the entire OPC driver.

#### Settings

| Signal List | Specifies the assignment of buses in the block diagram to targets that can output values. |
| --- | --- |
| Symbol bar | The signal bar is above the signal list and provides functions for the signal list. |
| Context menu for the signal list | Contains functions for the signal list. |

|  | Note For more information on the tabs of this dialog box, refer to the OPC Input / Output Block: Browser Tab, OPC Input Block: Parameter Tab, and the OPC Input Block: OLE Tab pages. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcpagebrowser.htm language=enus -->
## TOPIC 01134: OPC Input/Output Block: Browser Tab

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcpagebrowser.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcpagebrowser.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Input/Output Block: Browser Tab

OPC Input/Output Block: Browser Tab

Use this dialog box to assign an [OPC server](../opc/hid_opcserver.htm) to a block in DIAdem DAC, to define signals, and to display the server address tree and server information.

#### Settings

| Browser | Displays the address space of the OPC server. You can select one or more OPC items in the tree display. Click Transfer to List or drag and drop the selected OPC items into the signal list. If you want to display the address space, the OPC server must have a Browser interface. If this interface exists, an OPC client can determine the names of the available OPC items from the OPC server. Otherwise, a message appears and you must define the signals manually. |
| --- | --- |
| Update | Reads in the OPC server address space and updates the Browser display. |
| Select Server | Opens the dialog box where you assign a different server to the DAC block. If the server changes, the signal list of the block is deleted. |
| Server Info | Opens the dialog box that contains general information about the OPC server. |
| Transfer to List | Transfers the selected OPC server to the server list. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcpageole.htm language=enus -->
## TOPIC 01135: OPC Input/Output Block: OLE Tab

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcpageole.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcpageole.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Input/Output Block: OLE Tab

OPC Input/Output Block: OLE Tab

Use this dialog box to specify the parameters that monitor the OLE communication.

#### Settings

| Timeout for synchronous OLE calls during the measurement. | Specifies the timeout after which DIAdem executes the specfied error reaction. |
| --- | --- |
| Milliseconds | Specifies the milliseconds that the OPC clients waits for the OPC server. |
| Reaction to error | Specifies the behavior of DIAdem when an error in the OPC communication occurs. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcpageparaminput.htm language=enus -->
## TOPIC 01136: OPC Input Block: Parameter Tab

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcpageparaminput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcpageparaminput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Input Block: Parameter Tab

OPC Input Block: Parameter Tab

Use this dialog box to specify parameters for the OPC input block.

#### Settings

| Transfer mode | Specifies whether DIAdem uses a synchronous or an asynchronous transfer mode with the OPC server. If you select asynchronous transfer, you must specify an update rate and a value for the deadband. |
| --- | --- |
| Update rate | Specifies the rate at which the OPC server updates its data. |
| Deadband | Specifies the deadband as a percentage. |
| Device read active | Specifies how DIAdem calls values from the server during a measurement. Contact the OPC server manufacturer for further information. |
| Wait until server returns valid data | Specifies whether DIAdem must wait at the start of the measurement until the OPC server provides the quality value OPC_QUALITY_GOOD for all OPC items. Refer to Behavior at Measurement Start for further information. |
| Waiting time | Specifies how long DIAdem waits for valid values to arrive from the server, when the measurement starts. |
| Server Settings | Opens the dialog box where you can make general settings for the OPC server. |
| Driver Settings | Opens the dialog box where you can make general settings for the OPC driver. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcpageparamoutput.htm language=enus -->
## TOPIC 01137: OPC Output Block: Parameter Tab

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcpageparamoutput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcpageparamoutput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Output Block: Parameter Tab

OPC Output Block: Parameter Tab

Use this dialog box to specify parameters for the OPC output block.

#### Settings

| Transfer mode | Specifies whether DIAdem uses a synchronous or an asynchronous transfer mode with the OPC server. |
| --- | --- |
| Server Settings | Opens the dialog box where you can make general settings for the OPC server. |
| Server Settings | Opens the dialog box where you can make general settings for the OPC driver. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcsearchmethod.htm language=enus -->
## TOPIC 01138: Browsing for OPC Servers

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcsearchmethod.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcsearchmethod.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Browsing for OPC Servers

Browsing for OPC Servers

You can search for OPC servers with OPCENUM.EXE and you can scan the Windows registration.

#### Using OPCENUM.EXE

The OPC-Foundation defined for version 2.0 and later versions of the OPC specification the IOPCServerList interface, with which an OPC client searches for OPC servers on the OPC computer or on other computers. To use this interface the following requirements apply:

- The OPCCOMN_PS.DLL is registered on the client computer. This DLL is included in the DIAdem package and registers automatically when the program starts.
- The OPCENUM.EXE file must be registered on the computer that is searched. This file belongs to the DIAdem package. The file is not registered automatically. Execute the following command on the target computer to install the OPCENUM.EXE file:

OPCENUM.EXE /RegServer

|  | Note The files OPCENUM.EXE and OPCCOMN_PS.DLL are on the OPC foundation homepage. Many OPC servers that meet the requirements of the OPC specification 2.0 execute the OPCENUM.EXE registration automatically. |
| --- | --- |

|  | Note In the DCOM configuration for the target computer, you must grant access to the OPCENUM-OLE servers of remote systems. |
| --- | --- |

#### Scanning the Windows Registry

You also can scan the Windows registry database to find OPC servers. Most OPC clients that meet OPC specification version 1.0A use this method. The following requirements for the successful use of this search method apply:

- The user who is logged in must have reading rights for the Windows registry in the target system.
- The OPC servers must be entered in the Windows registry on the target system in accordance with version 1.0A of the OPC specification.

|  | Note You meet the requirements if you install a login on all computers, on which you want to start OPC servers, for the user logged in locally. |
| --- | --- |

|  | Note If the OPC server cannot access the target computer or there are no reading rights in the registry, response times of up to several minutes may occur in the tree view when you open the computer node. Please wait until DIAdem can operate again. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcserver.htm language=enus -->
## TOPIC 01139: OPC: General Information

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcserver.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcserver.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

OPC: General Information

OPC: General Information

The communication standard OPC (Open Platform Communications) allows efficient data transfer between various hardware and software components of an application. You can connect field bus systems and various kinds of hardware for which OPC servers are available to DIAdem as the client.

DIAdem-DAC can access several OPC servers simultaneously, so various field busses and PLC systems can be connected. DIAdem functions as a data exchange between the systems, regardless of whether automation components, visualization systems, or data archiving are involved.

A server is software that provides services to another software. In the OPC area, these services are usually process data output or input.

DIAdem is a classic client application in the OPC area. During measurements, DIAdem requests data from or supplies data to, one or more OPC servers.

#### Examples for Inputting Process Data

- Actual value of the temperature
- Status of a switch position

#### Examples for Process Data Output

- Set point for temperature controller
- Switching a switch

With an OPC interface, various programs (clients) can use the services of one OPC server. For the client program, it is irrelevant where the OPC server is located. The following situations are possible:

- The server is an element of the client process, for example, a DLL. In this case it is called an InProcess server, because the server runs in the address space of the client application. The communication between OPC client and OPC server is very fast.
- The server is located on the same computer as the client. In this case a server is called a local server (it runs locally on its own computer but in a different address space than the client application). The communication between the OPC client and the OPC server runs slower than with a InProcess server because Windows (NT, 95, 98) must transfer the data from the process space of the server to the process space of the client.
- The server is located on a remote computer and can be accessed over the network. This is a remote server. The communication between the OPC client and the OPC server runs slower because Windows must transfer the data from the server computer to the client computer or vice versa over a network.

Your operating system usually ensures that each client request is forwarded to the correct server, even if the server is on a remote computer. You must register the OPC server in order to inform your operating system about how to find the OPC server you need. The exact procedure for registering an OPC server differs from server to server. The following methods are valid:

- OPC server completely installed and started on the client system.
- Registration of the server (without complete installation of the server software) on the client system by an installation program of the server.
- Registration of the server using a registration file.
- Server is started once on the client system with an option, for example/RegServer.
- Manual editing of the Windows registration.

After registration, you might have to change some settings in the [DCOM Configuration](../opc/hid_opcfaq.htm).

|  | Note When problems occur with OPC servers or the integration of OPC servers into your system, NI only provides limited support, because server software is always third-party software. |
| --- | --- |

If we have information about your problem, we will be pleased to help. Otherwise we recommend the following:

- Contact your system administrator if you have problems concerning the DCOM-configuration area.
- Contact your server manufacturer if you cannot register your server or if you have general problems with your server.
- Refer to www.microsoft.com for further information about OLE and DCOM.
- For further information about OPC refer to the Homepage of the OPC foundation www.opcfoundation.org.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcserverselect_manual.htm language=enus -->
## TOPIC 01140: Specifying an OPC Server Manually

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcserverselect_manual.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcserverselect_manual.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Specifying an OPC Server Manually

Specifying an OPC Server Manually

Specify the class ID in this dialog box in order to specify an OPC server.

#### Settings

| Computer name | Specifies the name of the computer in the network on which DIAdem starts the OPC server with the help of the block diagram. |
| --- | --- |
| OPC server | Specifies the name of the OPC server the block diagram is to use. |
| Class ID | Specifies the class ID of the OPC server. This class ID identifies the OPC precisely. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcserverselectx.htm language=enus -->
## TOPIC 01141: Selecting an OPC Server

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcserverselectx.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcserverselectx.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Selecting an OPC Server

Selecting an OPC Server

Use this dialog box to select an OPC server for the input or output block.

#### Settings

| OPC Server browser | Displays an overview of the available OPC servers. |
| --- | --- |
| Computer name | Specifies the name of the computer in the network on which you start the OPC server. If you do not specify a name, DIAdem creates the list of OPC servers on the local computer you are working at. |
| OPC server | Specifies the OPC server. |
| Class ID | Specifies a precise ID for an OPC server. |
| Manual | Opens the dialog box where you use a class ID to assign an OPC server to the DIAdem block. |
| Search with OPC server browser | Specifies that DIAdem uses the file OPCENUM.EXE to search for OPC servers. |
| Browse in Windows registry | Specifies that DIAdem also searches for OPC servers in the Windows registry. |
| Refresh | Refreshes the list of available OPC servers in the browser. |

|  | Note Refer to Browse for OPC Servers for further information on searching for OPC servers. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcserversettings.htm language=enus -->
## TOPIC 01142: Settings for OPC Server

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcserversettings.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcserversettings.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Settings for OPC Server

Settings for OPC Server

Use this dialog box to specify the timeout settings of the OPC server.

#### Settings

| Timeout for establishing connection in milliseconds | Specifies the maximum waiting time for establishing the link to the OPC server. The recommended value is 15 seconds. |
| --- | --- |
| Timeout for general OLE calls | Specifies the maximum waiting time for various actions with the OPC server, for example, generating/deleting OPC groups, adding items to an OPC group, and so on. The recommended value is 5 seconds. |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcsiglist.htm language=enus -->
## TOPIC 01143: OPC Signal List

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcsiglist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcsiglist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > OPC Signal List

OPC Signal List

The input and output terminals of a block lead every entry of the signal list out of the block as a bus. A signal list can contain up to 255 entries (signals). If you want to use signals or signal related buses in a block diagram, you must first define the signal and enable the signal.

#### Columns in the Signal List

| Active / Number | Specifies a serial number of the signal. DIAdem leads the signals from the block to the block diagram in the order of these numbers. You can see the number when you close the OPC block and double click one of the incoming or outgoing green buses. The active key indicates whether the signal in a measurement is active. |
| --- | --- |
| Signal Name | Specifies the short name of the signal with a maximum of 16 letters. In the block diagram you can use this name, for example, to access the signal within a formula block. |
| Item ID | Specifies the identifier that DIAdem uses to access the signal on the OPC Server. The ItemID creates the link between the signal and a real data source (OPC item for input blocks) or a data sink (OPC item for output blocks) to the OPC server. |
| Validation | Specifies the result of the last validation of the ItemID of the OPC item on the OPC server. |
| Data Type | Specifies the OLE data type which the OPC server uses for the signal (OPC item). Ensure that only data types that DIAdem can process in the DAC area appear in this entry after a Validation. |
| Index (only in the input block) | Specifies the index with which you can access single values within a field. Some OPC servers supply their data as arrays. |
| Access rights | Specifies after a validation whether the OPC item assigned to the signal is read only (READ), write only (WRITE), or read and write (READ / WRITE). Use this information to accept only READ-signals in the signal list of input blocks and only WRITE-signals in the signal list of output blocks. |

|  | Note The access rights are not checked automatically. If you, for example, define OPC items with the access right READ in an output block you only receive an error message when you start the block diagram. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcsiglistuseguide.htm language=enus -->
## TOPIC 01144: Notes on Working with the Signal List

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcsiglistuseguide.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcsiglistuseguide.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Notes on Working with the Signal List

Notes on Working with the Signal List

Before you can use an OPC block in the block diagram, you must define signals. When you open the block dialog box the signal list is empty. You have the following possibilities to define signals in the [Signal list](../opc/hid_opcinsertsignals.htm):

- If the OPC server that is assigned to the block has an interface, you can select one or more OPC items on the [Browser](../opc/hid_opcpagebrowser.htm) tab and drag and drop them into the signal list.
- Select the items in the tree display and click **Add** to add the items to the signal list .
- Create new signal list entries via the **New** button on the toolbar.
- You can call a **New Signal** from the context menu of the signal list.

Select the signals and click **Delete** in the symbol bar to delete signals from the signal list. You also can select **Delete** from the context menu of the signal list.

If you do not disable [Signal validation](../opc/hid_opcvalidatesignals.htm), the driver automatically validates when defining the signals. The driver checks whether the itemID of the signal is available on the OPC server and provides further information about the item. You also can start a validation manually. Select the signals you want to validate in the signal list and click **Validation** on the symbol bar or in the context menu of the signal list.

Select **Edit** from the context menu of the signal list to [edit the signal definition](../opc/hid_opcsignaldefinition.htm).

If you use OPC-items that supply data as arrays you can select the respective signals in the signal list. Select **Set Indexes** from the context menu to assign [Indexes](../opc/hid_opcindexing.htm) to this signal group.

You can [assign signal names](../opc/hid_opcsignamegene.htm) to groups retrospectively. Select the respective signals and click **Generate Name** in the context menu. You can either derive the signal names from the ItemID or assign a base name and an additional number.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcupdaterate.htm language=enus -->
## TOPIC 01145: Update Rate for OPC Group

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcupdaterate.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcupdaterate.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Update Rate for OPC Group

Update Rate for OPC Group

The update rate specifies the rate at which the OPC server updates its data. Many OPC servers use an internal data cache and use the update rate to update the values in the cache. If you select asynchronous communication in the block, the uprate is also the rate at which the OPC server informs DIAdem about data changes. The update rate should correspond to the clock rate of the DIAdem clock system. A yellow clock cable connects the clock system and the acquisition block. The two values, expressed as time, should be approximately the same.

The update rate setting affects the performance of the entire system. The OPC update rate and the clock rate of the DIAdem clock system affect each other in the following ways:

- If the OPC update rate is substantially lower than the DIAdem sampling rate, the OPC server must supply its data faster than DIAdem can process the data. In this case, the communication system uses more computer power than necessary for the solution of the task. The moment when the input signal is measured is not earlier than the previous impulse in the DIAdem clock system.
- If the OPC update rate is substantially higher than the DIAdem sampling rate, the OPC server supplies its data much less frequently than DIAdem requests the data. DIAdem always displays the date that the OPC server determined at the last update. The moment when the input signal is measured might be earlier than the previous impulse in the DIAdem clock system. The data must not be older than the OPC update rate.

When DIAdem [validates](../opc/hid_opcvalidatesignals.htm) signals, DIAdem also requests the OPC server whether the server supports the value entered in the **Update rate** box. If not, the OPC server suggests a new value. DIAdem automatically includes this new value in the dialog box.

<!--NI_TOPIC bundle=diadem path=gfsopc/opc/hid_opcvalidatesignals.htm language=enus -->
## TOPIC 01146: Validating Signals

- bundle_id: `diadem`
- source_path: `gfsopc/opc/hid_opcvalidatesignals.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsopc/opc/hid_opcvalidatesignals.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[OPC](../opc/hid_opcserver.htm) > Validating Signals

Validating Signals

Validate the OPC item to check whether the signal definitions are valid. A validation uses the ItemId to send a query to the OPC server. The OPC server returns the following results for the item, which DIAdem also displays in the signal list:

- Results of the validation/check
- OLE data type for the OPC item
- Access rights (READ / WRITE)

The result of the validation shows whether the OPC server can provide the signals you defined. If you use invalid ItemIDs, errors occur when the measurement starts.

When you run a validation, DIAdem also determines whether the OPC server supports the value entered in the field [Update rate](../opc/hid_opcupdaterate.htm). If not, the OPC suggests a new value which DIAdem automatically integrates in the dialog box.

If you configure an OPC block, the OPC driver validates automatically in the following situations:

- After creating signal definitions with the Browser tab .
- After creating new signal definitions via the entry New on the toolbar.
- After editing signal definitions by double-clicking an entry in the Signal list .
- By closing the block dialog box with OK .

A warning is displayed if a validation for one or more signals fails.

<!--NI_TOPIC bundle=diadem path=gfsstd/useradm/dlgusernew_dialog.htm language=enus -->
## TOPIC 01147: Create New User Account

- bundle_id: `diadem`
- source_path: `gfsstd/useradm/dlgusernew_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsstd/useradm/dlgusernew_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[User Management](../useradm/useradmin_overview.htm) > Create New User Account

Create New User Account

Use this dialog box to set the parameters for user management. You only can open this dialog box if you are logged on as the DIAdem administrator.

#### Settings

| Log on name | Specifies the name of the user account. |
| --- | --- |
| Full name | Specifies the complete user name. |
| Default password | Specifies the password for the user account. |

<!--NI_TOPIC bundle=diadem path=gfsstd/useradm/dlgusernewprivilege_dialog.htm language=enus -->
## TOPIC 01148: Create New User Right

- bundle_id: `diadem`
- source_path: `gfsstd/useradm/dlgusernewprivilege_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsstd/useradm/dlgusernewprivilege_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[User Management](../useradm/useradmin_overview.htm) > Create New User Right

Create New User Right

Use this dialog box to create a new user right.

#### Settings

| Short name | Specifies the name of the new user right. |
| --- | --- |
| Description | Specifies the description of the new user right. |

<!--NI_TOPIC bundle=diadem path=gfsstd/useradm/dlguserpassword_dialog.htm language=enus -->
## TOPIC 01149: DIAdem User Account - Change Password

- bundle_id: `diadem`
- source_path: `gfsstd/useradm/dlguserpassword_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsstd/useradm/dlguserpassword_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[User Management](../useradm/useradmin_overview.htm) > DIAdem User Account - Change Password

DIAdem User Account - Change Password

Use this dialog box to change the password for a user in the user management. By default, DIAdem suggests DIAdem as the password for the guest and for the administrator. Change this password to make the password effective.

#### Settings

| Log on name | Specifies the name of the user account. |
| --- | --- |
| Full name | Specifies the complete user name. |
| Enter new password | Specifies the new password. |
| Confirm new password | Confirms the new password. |

<!--NI_TOPIC bundle=diadem path=gfsstd/useradm/useradmin_overview.htm language=enus -->
## TOPIC 01150: User Management - General

- bundle_id: `diadem`
- source_path: `gfsstd/useradm/useradmin_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsstd/useradm/useradmin_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

User Management - General

User Management - General

Use the user management to protect specific DIAdem functions in the alarm system from unauthorized access. In the user management, you specify the user accounts and rights, which DIAdem saves in an encrypted file (diadem.adm). During runtime, DIAdem checks whether the user has the necessary rights before it executes a function.

When DIAdem saves a block diagram, DIAdem saves the access rights required for the function to be performed, but not the user accounts or passwords.

The administrator grants rights and passwords, and creates or deletes user accounts. To register as the administrator, select **Settings»Alarm System»User Management**, log on as administrator, and enter diadem as your password. If you log on as Guest, you have general DIAdem rights of use.

You can use the following commands to include the user management in scripts:

| ADMLogIn | Opens the dialog box where the user logs on and off. |
| --- | --- |
| AskADMPermission | Checks the access rights of the current user and opens the dialog box for logging on if the user does not have the required rights. |
| ADMAdmin | Opens the dialog box for user management. If the user is not logged on in the user management, DIAdem opens the dialog box for logging on. |
| AskADMPermRt | Checks the access rights of the current user. |
| ADMCreateRight | Creates a new access right for the user management. |
| ADMLogOut | Logs out the current user from the user management. |

You can use the following variables to include the user management in scripts:

| ADMCurUser | Specifies the name of the registered user. |
| --- | --- |
| ADMRight | Specifies the name of a user right. |
| ADMPermission | Receives the result of the user rights check. |
| ADMDescription | Describes a user right. |

<!--NI_TOPIC bundle=diadem path=gfstimer/erf_timer.htm language=enus -->
## TOPIC 01151: GfS Timer

- bundle_id: `diadem`
- source_path: `gfstimer/erf_timer.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfstimer/erf_timer.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[GfSTimer](../gfstimer/timer_overview.htm) > GfS Timer

GfS Timer

Use this dialog box to specify the time acquisition and the operating mode of the GfSTimer. You can use the GPI-DAC driver GfSTimer to test the time behavior of a measurement task in DIAdem. DIAdem outputs the acquired times in seconds.

#### Settings

| Time acquisition | Specifies whether DIAdem determines the time that has elapsed since the measurement started, or the duration of one measurement cycle. |
| --- | --- |
| Operating mode | Specifies whether DIAdem determines the data of the process that is running in the foreground, or the data of the real-time kernel. |

|  | Note You can use the timer only once for each clock system. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfstimer/erf_timer_anmeld.htm language=enus -->
## TOPIC 01152: Registering

- bundle_id: `diadem`
- source_path: `gfstimer/erf_timer_anmeld.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfstimer/erf_timer_anmeld.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[GfSTimer](../gfstimer/timer_overview.htm) > Registering

Registering

To work with the GPI-DAC driver GfSTimer, you must first register the associated DLL GfSTimer in DIAdem. Refer to [Registering GPI Extensions](../procshell/procshell/procshell_register_gpi.htm) for further information.

<!--NI_TOPIC bundle=diadem path=gfstimer/timer_overview.htm language=enus -->
## TOPIC 01153: GfSTimer

- bundle_id: `diadem`
- source_path: `gfstimer/timer_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfstimer/timer_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

GfSTimer

GfSTimer

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes in which you configure the GPI-DAC driver GfSTimer.

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/append.htm language=enus -->
## TOPIC 01154: Function: Append

- bundle_id: `diadem`
- source_path: `gfsvbsdr/append.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/append.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Function: Append

Function: Append

Appends, in the Script driver, the contents of a variable (pvValue) to the pvBuffer output buffer in the vFormat.

```text
Append(Buffer, Value, Format)
```

#### Parameters

| Buffer | Specifies the variable to which the contents of the pvValue variable are appended. |
| --- | --- |
| Value | Specifies the variable of which the contents are appended to the pvBuffer buffer. |
| Format | Specifies the format of the variable that is to be appended. |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/errortextget.htm language=enus -->
## TOPIC 01155: Function: ErrorTextGet

- bundle_id: `diadem`
- source_path: `gfsvbsdr/errortextget.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/errortextget.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Function: ErrorTextGet

Function: ErrorTextGet

Calls an error description for the UDI device.

```text
ErrorTextGet()
```

| Return value | Error message text |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/namedvalueget.htm language=enus -->
## TOPIC 01156: Nominal Variable: NamedValueGet

- bundle_id: `diadem`
- source_path: `gfsvbsdr/namedvalueget.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/namedvalueget.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Nominal Variable: NamedValueGet

Nominal Variable: NamedValueGet

Reads, in the Script driver, the value of the nominal variable called Name.

```text
NamedValueGet(Name)
```

#### Parameters

| vName | Specifies the variable name. |
| --- | --- |
| Return value | Specifies the variable value. |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/namedvalueset.htm language=enus -->
## TOPIC 01157: Nominal Variable: NamedValueSet

- bundle_id: `diadem`
- source_path: `gfsvbsdr/namedvalueset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/namedvalueset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Nominal Variable: NamedValueSet

Nominal Variable: NamedValueSet

Sets the value of the nominal variable called Name in the [script driver](../gfsvbsdr/schntrb_ueber.htm).

```text
NamedValueSet(Name, Value)
```

#### Parameters

| vName | Specifies the variable name. |
| --- | --- |
| vValue | Specifies the variable value. |

#### Example

[Copy script](javascript:void(0);)

```text
Dim vScaledValue
' Read value of Temperature variable. Value is assigned to the local variable vScaledValue.
vScaledValue = oUDI.NamedValueGet("Temperature")

'Offset correction and scale variable 
vScaledValue = (vScaledValue-32.145) * 0.01

'Return the value
oUDI.NamedValueSet("Temperature",vScaledValue)
```

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/paramset.htm language=enus -->
## TOPIC 01158: Function: ParamSet

- bundle_id: `diadem`
- source_path: `gfsvbsdr/paramset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/paramset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Function: ParamSet

Function: ParamSet

Sets an interface-specific parameter for the UDI device in the [script driver](../gfsvbsdr/schntrb_ueber.htm).

```text
ParamSet(Parameter, Value)
```

#### Parameters

| Parameters | Specifies the name of the parameter to be changed. |
| --- | --- |
| Value | Specifies the new value of the parameter. |

#### Example

[Copy script](javascript:void(0);)

```text
Call oUDI.ParamSet( "BAUDRATE", "9600" )
```

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/parse.htm language=enus -->
## TOPIC 01159: Function: Parse

- bundle_id: `diadem`
- source_path: `gfsvbsdr/parse.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/parse.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Function: Parse

Function: Parse

Accesses the data that DIAdem reads from a UDI device, using the Read command in the [script driver](../gfsvbsdr/schntrb_ueber.htm). The function especially supports access to binary data.

Byte ordering is the order in which the driver transfers the binary data, using the ByteSwap parameter of the UDI object. If you assign the value False to the ByteSwap parameter, the driver processes the binary data with the Parse command, in the order High Byte -> Low Byte. If you assign the value True to the ByteSwap parameter, the driver processes the binary data in the order Low Byte -> High Byte.

```text
Parse(Data, FormatDescriptor)
```

#### Parameters

| Data | Specifies the variable with the data that DIAdem reads using Read. |
| --- | --- |
| Format | Specifies the structure of the binary data. Use the following syntax: %[n](U,L,D,S)[<Name>]. The meanings of these characters are listed in the following: %: Defines the start of a new format description.N:: Number of bytes to be interpreted for the variable.U: Unsigned IntegerL: Signed IntegerD: Real NumberS: TextName: Name of the Variable |
| Return value | Specifies the values of the variable. If the description of a variable is in the vFormat, one value is returned. If several descriptions are entered (see Example 2), a field of values is returned. |

#### Example 1

[Copy script](javascript:void(0);)

```text
Dim vData, vValue
vData = oUDI.Read() ' Read all available data from the UDI object
vValue = Parse(vData,"%2L") 'Read 2 bytes from vData and return the read value to the vData variable
```

#### Example 2

[Copy script](javascript:void(0);)

```text
Dim vData, vArray
vData = oUDI.Read() 'Read all available data from the UDI object
vArray = oUDI.Parse(vData,"%2L%4L") 'Read a total of 6 bytes from vData and return 2 values to the field
For L = 1 To UBound(vArray) 'Display the two values in a message box
  MsgBox(CStr(vArray(L))
Next
```

#### Example 3

[Copy script](javascript:void(0);)

```text
Dim vData, vArray, vScaledValue
vData = oUDI.Read() 'Read all available data from the UDI object
vArray = oUDI.Parse(vData,"%2L<Trigger>%4L<Temperature>") 'Read a total of 6 bytes from vData and return 2 values to the vArray field
vScaledValue = oUDI.NamedValueGet("Temperature ")*0.01' 
MsgBox(vScaledValue) 'Directly accesses the specified "Temperature" value and displays the scaled value in a message box
```

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_andere.htm language=enus -->
## TOPIC 01160: Affecting Other Drivers

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_andere.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_andere.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Operation](../gfsvbsdr/schntrb_arbeitsweise.htm) > Affecting Other Drivers

Affecting Other Drivers

If you use your own system clocks to process the scripts when working with the [script driver](../gfsvbsdr/schntrb_ueber.htm), you can reduce interference with other drivers and the program kernel to a minimum. Refer to the Help page on [Operating Modes of the Script Driver](../gfsvbsdr/schntrb_modi.htm) for more information. All the scripts are processed on one program path, which means that the scripts may interfere with each other. When you create the scripts, ensure that the program processes the scripts at the optimum speed.

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_arbeitsweise.htm language=enus -->
## TOPIC 01161: Working with the Script Driver

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_arbeitsweise.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_arbeitsweise.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > Working with the Script Driver

Working with the Script Driver

The [script driver](../gfsvbsdr/schntrb_ueber.htm) is based on two elements. On the one hand there is the DIAdem driver with its user interface, and on the other hand, VBScript as the programming language and interpreter. While you configure the driver, only the DIAdem driver is active and it is the interface between the user and the driver. During the measurement preparation VBScript starts in its own program thread. The driver checks the script file for syntax errors and transfers the script file to VBScript. As soon as the driver detects an error, the measurement preparations abort with an error message. After correcting the error, you can restart the measurement.

After the syntax check, the driver processes the initialization section of the script. The driver then calls the functions for initializing the devices and the inputs and outputs. When the measurement preparations are complete, the measurement starts and the driver calls the respective functions in the script. The driver deals with a measurement and the subsequent measurement post-processing in the same way.

If you set the error variable (ErrorP) to process a function in the script, the driver outputs an error message after the measurement has run with contents of the error variables. measurement aborts and an error message appears with the contents of the error variable.

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_close.htm language=enus -->
## TOPIC 01162: Function: Close

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_close.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_close.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Function: Close

Function: Close

Closes an interface in the [script driver](../gfsvbsdr/schntrb_ueber.htm) that you opened with Open.

```text
Close()
```

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_kommu.htm language=enus -->
## TOPIC 01163: Communication Interfaces of the Script Driver

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_kommu.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_kommu.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Operation](../gfsvbsdr/schntrb_arbeitsweise.htm) > Communication Interfaces of the Script Driver

Communication Interfaces of the Script Driver

#### Serial Interface (RS-232)

Driver for operating the serial interfaces

| Driver name | COM |
| --- | --- |
| Device name | COM1 ... COMx |

#### Parameters

| BAUD RATE | Specifies at which baud rate DIAdem operates the interface. |
| --- | --- |
| PARITY | Specifies the parity. The valid values are NONE (no parity), ODD (odd parity), and EVEN (even parity) |
| STOP BITS | Specifies the number of stop bits with which DIAdem operates the interface (1, 2). |
| DATA BITS | Specifies the number of data bits that DIAdem transfers with each character (7, 8). |
| TIMEOUT | Period of time in ms, that a transfer function waits for data before exiting with a timeout error. |
| DELIMITER | Specifies the character string that marks the end of a line. There may be several characters in the string. You transfer the delimiter as a normal character string. You can enter special characters as \\HH.Example: The following command sets the delimiter to the character sequence <CR><LF>:Call oUDI.ParamSet("DELIMITER", "\\0D\\0A" ) |

The following example opens the serial interface COM1 with a baud rate of 9600.

[Copy script](javascript:void(0);)

```text
Dim oUDI : Set oUDI = CreateUDI
Call oUDI.Open("COM", ""COM1")
Call oUDI.ParamSet("BAUDRATE", "9600")
```

#### NI GPIB

Operates the GPIB boards from NI. This driver requires the NI-488.2 driver from NI on the computer.

| Driver name | NI GPIB |
| --- | --- |
| Device name | Dev 1 ... Dev30 |

#### Parameters

| TIMEOUT | Period of time in ms, that a transfer function waits for data before exiting with a timeout error. |
| --- | --- |
| DELIMITER | Specifies the character string that marks the end of a line. There may be several characters in the string. You transfer the delimiter as a normal character string. You can enter special characters as \\HH.Example: The following command sets the delimiter to the character sequence <CR><LF>:Call oUDI.ParamSet("DELIMITER", "\\0D\\0A" ) |

The following example opens the NI GPIB interface Dev14.

[Copy script](javascript:void(0);)

```text
Dim oUDI : Set oUDI = CreateUDI
Call oUDI.Open("NI GPIB", "DEV14")
```

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_modi.htm language=enus -->
## TOPIC 01164: Script Driver Operating Modes

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_modi.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_modi.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Operation](../gfsvbsdr/schntrb_arbeitsweise.htm) > Script Driver Operating Modes

Script Driver Operating Modes

The [script driver](../gfsvbsdr/schntrb_ueber.htm) differentiates between two operating modes: "Synchronous to the measurement clock" and "Asynchronous to the measurement clock". The script driver calls the functions for data acquisition and output differently in the script for each of the two operating modes. All other functions are called independently of the selected operating mode, because function processing is not time-critical.

#### Synchronous to the measurement clock

The script driver calls the SFD_GetScan() function in the script at the beginning of the measurement cycle. The script driver waits until the function has been processed. The script driver then calls the SFD_ReadChannel() function for each active measurement channel and waits until the function is complete. After the data is acquired from all channels, the script driver transfers the data to the DIAdem measurement kernel.

The script driver always waits until the functions in the script are complete, and it blocks the DIAdem measurement kernel and other drivers for this period. As long as the script driver is the only active driver in the DAC block diagram, and the sampling rate allows sufficient time for the script functions to be processed, no problems arise. However, if the functions take a long time and other DIAdem drivers are activated at the same time, the script driver might block the other drivers or block the measurement kernel for longer than the acceptable period, and this could cause data loss or buffer overflows in the other drivers. Select the "Asynchronous to the measurement clock" operating mode to avoid these problems.

#### Asynchronous to the measurement clock

The script driver does not wait until the script processes the functions. It reads the data from an internal buffer where the script saves the data, and forwards the data directly to the DIAdem measurement kernel. Measurement cycles run as follows:

Firstly, the script driver checks whether all the script functions for data acquisition are complete. (In the SFD_ReadChannel() function, a value was assigned to the DataP parameter every time it was called.) If data acquisition is complete, the new measurement values are copied into an internal buffer in the script driver. The script DAC driver then calls the functions for data acquisition in the script (SFD_GetScan() and for each active channel SFD_ReadChannel), but does not wait for them to return. Regardless of the results of the previous test, the script driver then reads the measurement values from the internal buffer and transfers the values to the DIAdem measurement kernel.

This ensures that every time the script driver measurement routine is called, valid measurement data is available, which also can be transferred directly to the measurement kernel. Unlike the "Synchronous to the measurement clock" operating mode, however, there is no guarantee that "new" measured data will be transferred to the DIAdem measurement kernel in every measurement cycle. On the other hand, you can run the script driver at any sampling rate regardless of how long the individual script functions run, and without affecting other drivers or the DIAdem measurement kernel.

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_procedures.htm language=enus -->
## TOPIC 01165: Script Driver Procedures

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_procedures.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_procedures.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > Script Driver Procedures

Script Driver Procedures

There are a number of pre-defined script functions, which the [script driver](../gfsvbsdr/schntrb_ueber.htm) can call and use as an interface to VBScript. Most of these functions are optional. You only define these functions if you actually require them. The minimum range of functions in a script is a function for data acquisition or for data output.

The script driver transfers parameters that have the suffix V to the script as a value. The script driver ignores changes to this parameter in the script. If you call the script again, the driver transfers this parameter to the script with the original value. The script driver evaluates changes to the parameters that have the suffix P or saves these values. If the function is called again, the parameter has the changed value.

Parameters with the same name always mean the same for the function. For example, the script driver uses the parameter ErrorP to transfer an error message from the script to the script driver. If you assign a text to this parameter within a function, the driver stops the current measurement and displays an error message that shows the value of the ErrorP parameter.

You can create the following procedures in the script driver or have them created as a template in the [Script Driver: Script Template](../dlgdacsv/dac_dlg_input/dlgscriptdac_input_script_dialog.htm) dialog box.

| SFD_DeInit | Deinitializes the connected device. |
| --- | --- |
| SFD_DeInitInChannel | Deinitializes an input channel. |
| SFD_DeInitOutChannel | Deinitializes an output channel. |
| SFD_DeInitProcessChannel | Deinitializes a data processing channel. |
| SFD_FinalStop | Stops the measurement. |
| SFD_GetBlockScan | Requests scans in the measurement mode Hardware clock from the connected device. |
| SFD_GetScan | Reads a complete scan from the connected device. |
| SFD_Init | Initializes the connected device. |
| SFD_InitInChannel | Initializes an input channel. |
| SFD_InitOutChannel | Initializes an output channel. |
| SFD_InitProcessChannel | Initializes a data processing channel. |
| SFD_ProcessChannel | Calculates a measured value from the data of the connected input signals. |
| SFD_ProcessScan | Processes all the signals of a scan simultaneously. |
| SFD_ReadChannel | Transfers the measurement data of a single channel from the script to the script driver. |
| SFD_SendScan | Transfers the data of a complete scan to the connected device. |
| SFD_Start | Restarts the measurement on the connected device when a trigger sequence changes. |
| SFD_WriteChannel | Transfers measured values from the script driver to the script. |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_read.htm language=enus -->
## TOPIC 01166: Function: Read

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_read.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_read.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Function: Read

Function: Read

Reads data from the communication interface in the [script driver](../gfsvbsdr/schntrb_ueber.htm).

```text
Read(Count,Mode)
```

#### Parameters

| Count | Specifies the number of bytes to be read. This parameter is optional. If you do not specify this parameter, all the bytes in the buffer of the UDI device are read out. |
| --- | --- |
| Mode | Specifies the data transfer mode. This parameter is optional. Use one of the following values:0: Reads up to a specified number of characters (binary transfer).1: Reads up to a specified delimiter or the specified number of characters.If you do not specify the parameter, the default value 1 is used. |
| Return value | The function returns the bytes that UDI reads, as a string. The string also can contain binary elements, which you can then process with the Parse method. |

#### Example

[Copy script](javascript:void(0);)

```text
Dim oUDI : Set oUDI = CreateUDI
Receive = oUDI.Read(5,1)
```

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_sleep.htm language=enus -->
## TOPIC 01167: Function: Sleep

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_sleep.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_sleep.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Function: Sleep

Function: Sleep

Interrupts the script for a specified number of milliseconds in the [script driver](../gfsvbsdr/schntrb_ueber.htm).

```text
Sleep(MilliSeconds)
```

#### Parameters

| Milliseconds | Specifies the number of milliseconds. |
| --- | --- |

#### Example

[Copy script](javascript:void(0);)

```text
Dim oUDI : Set oUDI = CreateUDI
Call oUDI.Sleep(100)
```

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_var_guelt.htm language=enus -->
## TOPIC 01168: Validity of Script Driver Variables

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_var_guelt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_var_guelt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Operation](../gfsvbsdr/schntrb_arbeitsweise.htm) > Validity of Script Driver Variables

Validity of Script Driver Variables

The [script driver](../gfsvbsdr/schntrb_ueber.htm) processes all scripts in an own context. Therefore the variables used are only valid in the respective script and maintain their values between the calls of the individual functions. Variables that are declared within a function, are only valid in the range of the respective function and lose their validity when leaving this function.

Because the scripts are processed in their own contexts, data cannot be mistakenly overwritten if several scripts use variables with the same names. If you use the same script in two different DIAdem blocks, the scripts cannot influence each other. Therefore you can use several devices at different communication interfaces but use the same script with a different configuration.

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/schntrb_write.htm language=enus -->
## TOPIC 01169: Function: Write

- bundle_id: `diadem`
- source_path: `gfsvbsdr/schntrb_write.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/schntrb_write.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Methods of the UDI Object](../gfsvbsdr/schntrb_befehle.htm) > Function: Write

Function: Write

Sends data to a connected device over a communication interface in the [script driver](../gfsvbsdr/schntrb_ueber.htm).

Write(Data, [Count], [Mode])

#### Parameters

| Data | Specifies the text that is output to the UDI device. |
| --- | --- |
| [Count] | Specifies the number of bytes that are output to the UDI device. This parameter is optional. If you do not specify this parameter, the entire contents of the Data variable is output. |
| [Mode] | Specifies the data transfer mode. This parameter is optional. If you do not specify this parameter, the default value 1 is used. Use one of the following values:0 The data is transferred without an added delimiter.1Before the data is sent, a delimiter is appended. |
| 0 | The data is transferred without an added delimiter. |
| 1 | Before the data is sent, a delimiter is appended. |

#### Example

[Copy script](javascript:void(0);)

```text
Dim oUDI : Set oUDI = CreateUDI
Call oUDI.Write( "Hello", 5, 1 )
```

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_deinitinchannel.htm language=enus -->
## TOPIC 01170: Function: SFD_DeInitInChannel

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_deinitinchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_deinitinchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_DeInitInChannel

Function: SFD_DeInitInChannel

Deinitializes the inputs used in the [script driver](../gfsvbsdr/schntrb_ueber.htm). DIAdem calls the SFD_DeInitInChannel function during the measurement wrap-up, once for every active measurement channel.

SFD_DeInitInChannel(ChannelNumberV, ErrorP)

#### Parameters

| ChannelNumberV | Transfers the terminal number of the input from the dialog box for the script driver to the script. You can use this parameter in the script to refer to the physical input of the connected device. |
| --- | --- |
| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |

|  | Note This function is optional. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_deinitoutchannel.htm language=enus -->
## TOPIC 01171: Function: SFD_DeInitOutChannel

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_deinitoutchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_deinitoutchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_DeInitOutChannel

Function: SFD_DeInitOutChannel

Deinitializes an active output channel in the [script driver](../gfsvbsdr/schntrb_ueber.htm). DIAdem calls the SFD_DeInitOutChannel function during the measurement wrap-up, once for every active output.

SFD_DeInitOutChannel(ChannelNumberV, ErrorP)

#### Parameters

| ChannelNumberV | Transfers the terminal number of the output from the dialog box for the script driver to the script. You can use this parameter in the script to refer to the physical output of the connected device. |
| --- | --- |
| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |

|  | Note This function is optional. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_deinitprocesschannel.htm language=enus -->
## TOPIC 01172: Function: SFD_DeInitProcessChannel

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_deinitprocesschannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_deinitprocesschannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_DeInitProcessChannel

Function: SFD_DeInitProcessChannel

Deinitializes the data processing channels used in the [script driver](../gfsvbsdr/schntrb_ueber.htm). DIAdem calls the SFD_DeInitProcessChannel function during the measurement wrap-up, once for every active data processing channel.

SFD_DeInitProcessChannel(ChannelNumberV, ErrorP)

#### Parameters

| ChannelNumberV | Transfers the terminal number of the signal from the dialog box for the script driver transferred to the script. Use this parameter in the script as reference to the block input that is to be processed. |
| --- | --- |
| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |

|  | Note This function is optional. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_finalstop.htm language=enus -->
## TOPIC 01173: Function: SFD_FinalStop

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_finalstop.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_finalstop.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_FinalStop

Function: SFD_FinalStop

Ends the measurement or the communication with a device in the [script driver](../gfsvbsdr/schntrb_ueber.htm). DIAdem calls the SFD_FinalStop function once when it completes the DAC task.

SFD_FinalStop(ErrorP)

#### Parameters

| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |
| --- | --- |

|  | Note This function is optional. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_initprocesschannel.htm language=enus -->
## TOPIC 01174: Function: SFD_InitProcessChannel

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_initprocesschannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_initprocesschannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_InitProcessChannel

Function: SFD_InitProcessChannel

Initializes the required channels for data processing in the [script driver](../gfsvbsdr/schntrb_ueber.htm). DIAdem calls the SFD_InitProcessChannel function during the measurement preparation, once for every active data processing channel.

SFD_InitProcessChannel( ChannelNumberP, InputListV, ParamP, ErrorP, [ScalingFactorP], [ScalingOffsetP], [ChannelCountV], [UnitP], [PropertyListP])

#### Parameters

| ChannelNumberP | Transfers the terminal number of the signal from the dialog box for the script driver to the script. Use this parameter in the script as reference to the block input that is to be offset. |
| --- | --- |
| InputListV | Contains a list of all inputs that you defined for the respective block. This array contains for each signal input one entry with the information whether a signal is connected to this input. The inputs are numbered starting with the index 0. |
| ParamP | Transfers the signal parameter to the script. You can use this parameter, for example, to specify the measurement range of an input. |
| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |
| [ScalingFactorP] | Returns a scaling factor to the script driver, with which the output values of a channel are automatically offset during a measurement. The parameter is optional. You can only use this parameter with the ScalingOffsetP parameter. |
| [ScalingOffsetP] | Returns a scaling offset to the script driver, with which the output values of a channel are automatically offset during a measurement. The parameter is optional. You can only use this parameter with the ScalingFactorP parameter. |
| [ChannelCountV] | Specifies the number of active channels that the script must process. You can use this information, for example, to generate adequately large arrays for the measurement data. The parameter is optional. |
| [UnitP] | Returns a unit to the script driver, with which the channel unit is set. The parameter is optional. |
| [PropertyListP] | Returns custom properties to the script driver, with which the custom properties of the channel are set. The parameter is optional. The parameter is a zero-based vector of the dimension 3*n-1 which means 3*n elements. A triplet of data type, property name, and property value specifies the custom property. The first (fourth, seventh, ...) element contains the data type. "PropertyTypeString", "PropertyTypeInteger", and "PropertyTypeDouble" are reliable values. The second (fifth, eighth, ...) element contains the name of the custom property and the third (sixth. ninth,...) element contains the value of the custom property. |

The following example defines two custom properties.

[Copy script](javascript:void(0);)

```text
Sub SFD_InitProcessChannel(ChannelNumberP, InputListV, ParamP, ErrorP , ScalingFactorP, ScalingOffsetP , ChannelCountV, UnitP, PropertyListP)
  Dim aProperties(5)
  aProperties(0) = "PropertyTypeInteger"
  aProperties(1) = "MyInteger"
  aProperties(2) = 5
  aProperties(3) = "PropertyTypeString"
  aProperties(4) = "MyString"
  aProperties(5) = "This is the string value"
  PropertyListP = aProperties     
End Sub
```

|  | Note This function is optional. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_processchannel.htm language=enus -->
## TOPIC 01175: Function: SFD_ProcessChannel

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_processchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_processchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_ProcessChannel

Function: SFD_ProcessChannel

Offsets the data of the connected input signals against each other in the [script driver](../gfsvbsdr/schntrb_ueber.htm). DIAdem calls this function once per measurement cycle for each channel in the block.

SFD_ProcessChannel(ChannelNumberP, InputListV, ParamP, DataP, ErrorP)

#### Global Parameters

| ChannelNumberP | Transfers the terminal number of the signal from the dialog box for the script driver to the script. This parameter identifies the wanted measurement channel. |
| --- | --- |
| InputListV | Transfers an array with the current measurement data of the connected signals. The array contains exactly one entry per signal input of the block. If no signals are connected to the inputs, the respective entry is initialized to the value 1.0. DIAdem avoids runtime errors in the script which can occur due to unconnected input signals. |
| ParamP | Transfers the signal parameter from the user interface of the script driver to the function. |
| DataP | Transfers the measured data from the script to the script driver. The parameter must contain a value at every function call, because otherwise the script driver considers the function to be incomplete and the driver then gets stuck. |
| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |

|  | Note You must use this function for scripts that output data. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_processscan.htm language=enus -->
## TOPIC 01176: Function: SFD_ProcessScan

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_processscan.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_processscan.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_ProcessScan

Function: SFD_ProcessScan

Enables simultaneous processing of all signals of a scan in the [script driver](../gfsvbsdr/schntrb_ueber.htm). You can save the results in a script global array, and then transfer the results to DIAdem with the SFD_ProcessChannel function.

SFD_ProcessScan(InputListV, ErrorP)

#### Global Parameters

| InputListV | Contains a list of the data of all connected input signals. |
| --- | --- |
| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |

|  | Note This function is optional. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_readchannel.htm language=enus -->
## TOPIC 01177: Function: SFD_ReadChannel

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_readchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_readchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_ReadChannel

Function: SFD_ReadChannel

Transfers the measurement data of a single channel from the script to the [script driver](../gfsvbsdr/schntrb_ueber.htm). The function can request the data of this channel directly from the measurement device or from the respective script variables. Before the function can request measurement data from variables, the SFD_GetScan function must save the measurement data in variables, read out the data, and transfer the measurement data to the script driver. DIAdem calls this function once per measurement cycle for every active measurement channel.

SFD_ReadChannel(ChannelNumberP, ParamP, DataP, ErrorP)

#### Parameters

| ChannelNumberP | Transfers the terminal number of the signal from the dialog box for the script driver to the script. This parameter identifies the wanted measurement channel. |
| --- | --- |
| ParamP | Transfers the signal parameter from the user interface of the script driver to the script. |
| DataP | Transfers the measurement data from the script to the script driver. The parameter must contain a value at every function call, because otherwise the script driver considers the function to be incomplete and the driver then gets stuck. |
| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |

|  | Note This function must be used when data is acquired with the script driver in the single value mode. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_sendscan.htm language=enus -->
## TOPIC 01178: Function: SFD_SendScan

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_sendscan.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_sendscan.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_SendScan

Function: SFD_SendScan

Transfers the data of a complete scan to the connected device in the [script driver](../gfsvbsdr/schntrb_ueber.htm). DIAdem calls this function once per measurement cycle.

SFD_SendScan(ErrorP)

#### Parameters

| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |
| --- | --- |

|  | Note This function is optional. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=gfsvbsdr/sfd_start.htm language=enus -->
## TOPIC 01179: Function: SFD_Start

- bundle_id: `diadem`
- source_path: `gfsvbsdr/sfd_start.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/gfsvbsdr/sfd_start.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Script Driver](../gfsvbsdr/schntrb_ueber.htm) > [Script Driver Procedures](../gfsvbsdr/schntrb_procedures.htm) > Function: SFD_Start

Function: SFD_Start

Restarts the measurement on the connected device when a trigger sequence changes in the [script driver](../gfsvbsdr/schntrb_ueber.htm).

SFD_Start(SamplingRateV, ErrorP)

#### Parameters

| SamplingrateV | Transfers the specified sampling rate to the script. |
| --- | --- |
| ErrorP | Returns an error message to the script driver. You also can use this parameter to specify the error message text. |

|  | Note This function is optional. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=header/header/header_overview.htm language=enus -->
## TOPIC 01180: DIAdem DAT File Format

- bundle_id: `diadem`
- source_path: `header/header/header_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/header/header/header_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

DIAdem DAT File Format

DIAdem DAT File Format

The subordinate topics contained in the tree on the contents tab of the Help describe the structure of the DAT file format. The topics provide information about the structure of the header file and examples of ASCII file headers and binary file headers.

<!--NI_TOPIC bundle=diadem path=header/header/headerascblock_beispiel.htm language=enus -->
## TOPIC 01181: Example of a Header File for ASCII Block Files

- bundle_id: `diadem`
- source_path: `header/header/headerascblock_beispiel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/header/header/headerascblock_beispiel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAT File Format](../header/header_overview.htm) > Example of a Header File for ASCII Block Files

Example of a Header File for ASCII Block Files

The following ASCII data file is to be read into DIAdem. It is an ASCII file in block format with 6 channels, each containing 12 values. Channel 1 is a time channel in the format mm.dd.yyyy hh:nn:ss.

15.01.1993 05:47:19, 1, 1, 6, 2.10, 3.34

15.01.1993 11:32:03, 2, 2, 14, 7.50, 6.65

15.01.1993 16:56:24, 3, 3, 22, 5.70, 4.98

16.01.1993 06:05:31, 1, 4, 6, 1.30, 2.37

16.01.1993 11:51:38, 2, 5, 14, 10.20, 1.12

16.01.1993 17:15:57, 3, 6, 22, 5.90, 2.69

17.01.1993 06:02:27, 1, 7, 6, 3.40, 3.72

17.01.1993 11:12:55, 2, 8, 14, 4.60, 1.89

17.01.1993 17:51:41, 3, 9, 22, 0.50, 6.47

18.01.1993 05:35:05, 1, 10, 6, 2.90, 9.15

18.01.1993 11:14:48, 2, 11, 14, 5.00, 3.29

18.01.1993 16:54:41, 3, 12, 22, 4.40, 1.54

#### Header file

The header file needed to read the ASCII block file shown above is printed below.

DIAEXTENDED {@:ENGLISH

| #BEGINGLOBALHEADER | ( General header ) |
| --- | --- |
| 1,WINDOWS | ( Operating system ) |
| 2,{@R:200 | ( Revision number ) |
| 101,Read in an ASCII block file | ( File comment ) |
| 102,ASCII block file with time channel | (100 Comments on the data set ) |
| 103,Kr | ( Author ) |
| 104,22.04.1996 | ( Date of the file storage ) |
| 105,12:15:25 | ( Time of the file storage ) |
| 110,#dd.mm.yyyy hh:nn:ss | ( Time format ) |
| 111,9.9E+34 | ( NoValue value in the file ) |
| #ENDGLOBALHEADER |  |

| #BEGINCHANNELHEADER | ( Channel header for channel 1 ) |
| --- | --- |
| 200,Time channel | ( Channel name ) |
| 201,ASCII block file | ( Channel comment ) |
| 202,[-] | ( Unit ) |
| 210,EXPLICIT | ( Channel type ) |
| 211,TIME_ASC.ASC | ( Data filename ) |
| 213,BLOCK | ( Data storage type ) |
| 214,ASCII | ( Data type ) |
| 220,12 | ( Number of values in the channel ) |
| 221,1 | ( Line with the first channel value ) |
| 223,1 | ( Local ASCII pointer to the channel column ) |
| 230,44 | ( Separator character: Comma ) |
| 231,46 | ( Decimal symbol: Comma ) |
| 232,69 | ( Exponential character: E ) |
| 240,0 | ( Start value ) |
| 241,1 | ( Scaling factor ) |
| 250,62831051239 | ( Minimum value ) |
| 251,62831350481 | ( Maximum value ) |
| 252,No | ( NoValues in the channel ) |
| 253,increasing | ( Monotony ) |
| 260,Time | ( Data display for interface ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 1 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 2 ) |
| --- | --- |
| 200,Channel number2 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,2 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-241 identical to those in channel header 1 ) |
| 250,1 | ( Minimum value ) |
| 251,3 | ( Maximum value ) |
| 252,No | ( NoValues in the channel ) |
| 253,increasing | ( Monotony ) |
| 260,Numeric | ( Data display for interface ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 2 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 3 ) |
| --- | --- |
| 200,Channel number3 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,3 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-241 identical to those in channel header 1 ) |
| 250,1 | ( Minimum value ) |
| 251,12 | ( Maximum value ) |
| 252,No | ( NoValues in the channel ) |
| 253,increasing | ( Monotony ) |
| 260,Numeric | ( Data display for interface ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 3 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 4 ) |
| --- | --- |
| 200,Channel number4 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,4 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-241 identical to those in channel header 1 ) |
| 250,6 | ( Minimum value ) |
| 251,22 | ( Maximum value ) |
| 252,No | ( NoValues in the channel ) |
| 253,increasing | ( Monotony ) |
| 260,Numeric | ( Data display for interface ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 4 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 5 ) |
| --- | --- |
| 200,Channel number5 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,5 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-241 identical to those in channel header 1 ) |
| 250,0.5 | ( Minimum value ) |
| 251,10.2 | ( Maximum value ) |
| 252,No | ( NoValues in the channel ) |
| 253,increasing | ( Monotony ) |
| 260,Numeric | ( Data display for interface ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 5 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 6 ) |
| --- | --- |
| 200,Channel number6 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,6 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-241 identical to those in channel header 1 ) |
| 250,1.12 | ( Minimum value ) |
| 251,9.15 | ( Maximum value ) |
| 252,No | ( NoValues in the channel ) |
| 253,increasing | ( Monotony ) |
| 260,Numeric | ( Data display for interface ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 6 ) |

<!--NI_TOPIC bundle=diadem path=header/header/headerascblockkom_beispiel.htm language=enus -->
## TOPIC 01182: Example for Reading in ASCII Block Files with Comments

- bundle_id: `diadem`
- source_path: `header/header/headerascblockkom_beispiel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/header/header/headerascblockkom_beispiel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAT File Format](../header/header_overview.htm) > Example for Reading in ASCII Block Files with Comments

Example for Reading in ASCII Block Files with Comments

The following ASCII data file is to be read into DIAdem. It is an ASCII file in block format with 6 channels, each containing 12 values. Channel 3 is a time channel with the format mm.dd.yyyy. There are 5 comment lines at the beginning of the file, which DIAdem should skip. The blank lines are also counted as comment lines.

| 1. line: | Example for reading in an ASCII block file |
| --- | --- |
| 2. line: | All channels with values that can be interpreted numerically |
| 3. line: | are included in the DIAdem data area. |
| 4. line: |  |
| 5. line: |  |
| 6. line: | First measurement 1 15.01.1991 6.00 2.1 3.34 |
| 7. line: | Second measurement 2 15.01.1991 14.00 7.5 6.65 |
| 8. line: | Third measurement 3 15.01.1991 22.00 5.7 4.98 |
| 9. line: | First measurement 4 16.01.1991 6.00 1.3 2.37 |
| 10. line: | Second Measurement 5 16.01.1991 14.00 10.2 1.12 |
| 11. line: | Third measurement 6 16.01.1991 22.00 5.9 2.69 |
| 12. line: | First measurement 7 17.01.1991 6.00 3.4 3.72 |
| 13. line: | Second measurement 8 17.01.1991 14.00 4.6 1.89 |
| 14. line: | Third measurement 9 17.01.1991 22.00 0.5 6.47 |
| 15. line: | First measurement 10 18.01.1991 6.00 2.9 9.15 |
| 16. line: | Second measurement 11 18.01.1991 14.00 5 3.29 |
| 17. line: | Third measurement 12 18.01.1991 22.00 4.4 1.54 |

#### Header file

Use the header file shown below to read in the ASCII block file displayed above:

DIAEXTENDED {@.ENGLISH

| #BEGINGLOBALHEADER | ( General header ) |
| --- | --- |
| 1,WINDOWS | ( Operating system ) |
| 2,{@R:200 | ( Revision number ) |
| Read in an ASCII channel file | ( File comment ) |
| 102,ASCII block file with time channel | (100 Comments on the data set ) |
| 103,Kr | ( Author ) |
| 104,22.04.1996 | ( Date of the file storage ) |
| 105,12:15:25 | ( Time of the file storage ) |
| 110,#dd.mm.yyyy hh:nn:ss | ( Time format ) |
| 111,9.9E+34 | ( NoValue value in the file ) |
| #ENDGLOBALHEADER |  |

| #BEGINCHANNELHEADER | ( Channel header for channel 1 ) |
| --- | --- |
| 200,Channel number1 | ( Channel name ) |
| 201,ASCII block file | ( Channel comment ) |
| 202,[-] | ( Unit ) |
| 210,EXPLICIT | ( Channel type ) |
| 211,ASCIIBLK.ASC | ( Data filename ) |
| 213,BLOCK | ( Data storage type ) |
| 214,ASCII | ( Data type ) |
| 223,1 | ( Local ASCII pointer to the channel column ) |
| 230,32 | ( Separator character: Space ) |
| 231,46 | ( Decimal symbol: Comma ) |
| 232,69 | ( Exponential character: E ) |
| 220,12 | ( Number of values in the channel ) |
| 221,6 | ( Line with the first channel value ) |
| 240,0 | ( Offset ) |
| 241,1 | ( Scaling factor ) |
| 260,Numeric | ( Data display for interface ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 1 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 2 ) |
| --- | --- |
| 200,Channel number2 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,2 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-301 identical to those in channel header 1 ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 2 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 3 ) |
| --- | --- |
| 200,Channel number3 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,3 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-254 identical to those in channel header 1 ) |
| 260,Time | ( Data display for interface ) |
| ... | ( Entries 270-301 identical to those in channel header 1 ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 3 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 4 ) |
| --- | --- |
| 200,Channel number4 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,4 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-301 identical to those in channel header 1 ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 4 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 5 ) |
| --- | --- |
| 200,Channel number5 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,5 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-301 identical to those in channel header 1 ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 5 ) |

| #BEGINCHANNELHEADER | ( Channel header for channel 6 ) |
| --- | --- |
| 200,Channel number6 | ( Channel name ) |
| ... | ( Entries 201-221 identical to those in channel header 1 ) |
| 223,6 | ( Local ASCII pointer to the channel column ) |
| ... | ( Entries 230-301 identical to those in channel header 1 ) |
| #ENDCHANNELHEADER | ( End of channel header for channel 6 ) |

<!--NI_TOPIC bundle=diadem path=icalculationset/icalculationset_overview.htm language=enus -->
## TOPIC 01183: Calculations

- bundle_id: `diadem`
- source_path: `icalculationset/icalculationset_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/icalculationset_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Calculations

Calculations

The subordinate topics contained in the tree on the contents tab of the Help describe the object-oriented script interface of the calculations. The topics provide information about all objects, collections, methods, properties, and events, and examples that demonstrate how to use the interface.

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_add_ioutputcollection.htm language=enus -->
## TOPIC 01184: Method: Add for Outputs

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_add_ioutputcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_add_ioutputcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: Add for Outputs

Method: Add for Outputs

Adds a new output to the Outputs collection and returns an Output object.

```text
Set oOutput = Object.Add(Name, AdaptorType)
```

| Object | OutputsObject with this method |  |
| --- | --- | --- |
| Name | StringSpecifies the name of the output of a calculation. The name must conform to the naming conventions for calculations. If the name does not conform to the name conventions, DIAdem corrects the name. If the name already exists as an input or an output of the calculation, DIAdem does not generate a new object, it displays an error message. |  |
| AdaptorType | Specifies the type of the output.Enumeration with the following selection terms: 100eAdaptorTypeValueThe output refers to a value. 101eAdaptorTypeChannelThe output refers to a channel. 102eAdaptorTypeChannelListThe output refers to a channel list. |  |
| 100 | eAdaptorTypeValue | The output refers to a value. |
| 101 | eAdaptorTypeChannel | The output refers to a channel. |
| 102 | eAdaptorTypeChannelList | The output refers to a channel list. |
| oOutput | OutputReturned object |  |

The following example adds the R output to the first calculation of the calculation group Custom if the output does not already exist:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalcTemp
Set oMyCalcTemp = CalculationSet.CalculationGroups("Custom").Calculations(1)
If not oMyCalcTemp.Outputs.Exists("R") Then
  Call oMyCalcTemp.Outputs.Add("R", eAdaptorTypeChannel)
End If
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups("Custom").Calculations(1) 
if not oMyCalcTemp.Outputs.Exists("R") : 
    oMyCalcTemp.Outputs.Add("R", dd.eAdaptorTypeChannel) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_addbyoutput_iinputcollection.htm language=enus -->
## TOPIC 01185: Method: AddByOutput for Inputs

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_addbyoutput_iinputcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_addbyoutput_iinputcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: AddByOutput for Inputs

Method: AddByOutput for Inputs

Generates an input that is dependent on an output of a calculation and adds this input to the Inputs collection. The properties of the generated input correspond to the properties of the specified output. You can edit the name of the input afterwards. You cannot change the other properties from the specified output. If the output properties change, the changes influence all dependent inputs.

If the name of the specified output already exists in the Inputs or Outputs collection, DIAdem does not generate a new object, it displays an error message. If the dependent input is correct, DIAdem also extends the [TargetInputs](../properties/formulacalc_property_targetinputs_ioutput.htm) output property.

```text
Set oInput = Object.AddByOutput(Output)
```

| Object | InputsObject with this method |
| --- | --- |
| Output | OutputOutput on which the input is to be dependent. |
| oInput | InputReturned object |

The following example uses the first output of the first calculation in the Custom calculation group to generate a new dependent input for the second calculation:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyOutput
Set oMyOutput = CalculationSet.CalculationGroups("Custom").Calculations(1).Outputs(1)
Call CalculationSet.CalculationGroups("Custom").Calculations(2).Inputs.AddByOutput(oMyOutput)
```

[Copy script](javascript:void(0);)

```text
oMyOutput = dd.CalculationSet.CalculationGroups("Custom").Calculations(1).Outputs(1) 
dd.CalculationSet.CalculationGroups("Custom").Calculations(2).Inputs.AddByOutput(oMyOutput) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_exists_icalculationcollection.htm language=enus -->
## TOPIC 01186: Method: Exists for Calculations

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_exists_icalculationcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_exists_icalculationcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: Exists for Calculations

Method: Exists for Calculations

Checks whether a calculation with a specific name exists.

```text
bExists = Object.Exists(Name)
```

| Object | CalculationsObject with this method |
| --- | --- |
| Name | StringSpecifies the calculation name. |
| bExists | BooleanThe value is TRUE if the collection contains an object with the specified name. |

The following example adds the new calculation Custom to the first calculation group if this calculation does not exist:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If not CalculationSet.CalculationGroups(1).Calculations.Exists("Custom") Then
  Call CalculationSet.CalculationGroups(1).Calculations.Add("Custom")
End If
```

[Copy script](javascript:void(0);)

```text
if not dd.CalculationSet.CalculationGroups(1).Calculations.Exists("Custom") : 
    dd.CalculationSet.CalculationGroups(1).Calculations.Add("Custom") 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_exists_icalculationgroupcollection.htm language=enus -->
## TOPIC 01187: Method: Exists for CalculationGroups

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_exists_icalculationgroupcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_exists_icalculationgroupcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: Exists for CalculationGroups

Method: Exists for CalculationGroups

Checks whether a calculation group with a specific name exists.

```text
bExists = Object.Exists(Name)
```

| Object | CalculationGroupsObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the calculation group. |
| bExists | BooleanThe value is TRUE if the collection contains an object with the specified name. |

The following example adds the new calculation group Custom to the current calculation set if this group does not exist:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If not CalculationSet.CalculationGroups.Exists("Custom") Then
  Call CalculationSet.CalculationGroups.Add("Custom")
End If
```

[Copy script](javascript:void(0);)

```text
if not dd.CalculationSet.CalculationGroups.Exists("Custom") : 
    dd.CalculationSet.CalculationGroups.Add("Custom") 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_exists_iinputcollection.htm language=enus -->
## TOPIC 01188: Method: Exists for Inputs

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_exists_iinputcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_exists_iinputcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: Exists for Inputs

Method: Exists for Inputs

Checks whether a calculation contains an input with a specific name.

```text
bExists = Object.Exists(Name)
```

| Object | InputsObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the input. |
| bExists | BooleanThe value is TRUE if the collection contains an object with the specified name. |

The following example adds the Z input to the first calculation of the calculation group Custom if this input does not already exist:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalcTemp
Set oMyCalcTemp = CalculationSet.CalculationGroups("Custom").Calculations(1)
If not oMyCalcTemp.Inputs.Exists("Z") Then
  Call oMyCalcTemp.Inputs.Add("Z", eAdaptorTypeChannel)
End If
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups("Custom").Calculations(1) 
if not oMyCalcTemp.Inputs.Exists("Z") : 
    oMyCalcTemp.Inputs.Add("Z", dd.eAdaptorTypeChannel) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_exists_ioutputcollection.htm language=enus -->
## TOPIC 01189: Method: Exists for Outputs

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_exists_ioutputcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_exists_ioutputcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: Exists for Outputs

Method: Exists for Outputs

Checks whether a calculation contains an output with a specific name.

```text
bExists = Object.Exists(Name)
```

| Object | OutputsObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the output. |
| bExists | BooleanThe value is TRUE if the collection contains an object with the specified name. |

The following example adds the R output to the first calculation of the calculation group Custom if the output does not already exist:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalcTemp
Set oMyCalcTemp = CalculationSet.CalculationGroups("Custom").Calculations(1)
If not oMyCalcTemp.Outputs.Exists("R") Then
  Call oMyCalcTemp.Outputs.Add("R", eAdaptorTypeChannel)
End If
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups("Custom").Calculations(1) 
if not oMyCalcTemp.Outputs.Exists("R") : 
    oMyCalcTemp.Outputs.Add("R", dd.eAdaptorTypeChannel) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_export_icalculationset.htm language=enus -->
## TOPIC 01190: Method: Export for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_export_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_export_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: Export for CalculationSet

Method: Export for CalculationSet

Exports all or selected calculations into a calculation set file (*.tca).

```text
Object.Export(FileName, [CalculationSelection], [ExportMode])
```

| Object | CalculationSetObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the name of the calculation set file (*.tca) that is to be exported. If you do not specify a filename extension, DIAdem adds the filename extension automatically. If you do not specify a path, DIAdem saves the file in the User folder for configuration files. |  |
| [CalculationSelection] | Specifies whether DIAdem saves all or only selected calculations. If you do not set this parameter, DIAdem saves all calculations.Enumeration with the following selection terms: 120eCalculationAllDIAdem saves all calculations. 121eCalculationSelectionDIAdem saves only the selected calculationsThe Selected property specifies whether a calculation is selected.A dependent input loses its dependency when it is saved if you do not save the associated output as well. |  |
| 120 | eCalculationAll | DIAdem saves all calculations. |
| 121 | eCalculationSelection | DIAdem saves only the selected calculationsThe Selected property specifies whether a calculation is selected.A dependent input loses its dependency when it is saved if you do not save the associated output as well. |
| [ExportMode] | Specifies whether DIAdem saves the calculation set file encrypted or unencrypted. If you do not specify this parameter, DIAdem saves the file unencrypted. All scripts and formulas saved in the calculations are encrypted.Enumeration with the following selection terms:130eExportModeStandardDIAdem saves the calculation unencrypted. 131eExportModeCryptedDIAdem saves the calculation encrypted. |  |
| 130 | eExportModeStandard | DIAdem saves the calculation unencrypted. |
| 131 | eExportModeCrypted | DIAdem saves the calculation encrypted. |

|  | Note When you save the encrypted calculation, you cannot overwrite an existing file. Always save the unencrypted calculations, because you cannot decrypt a file once it is encrypted. |
| --- | --- |

The following example exports all calculations unencrypted into the calculation set file MyCalculationSet.tca:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call CalculationSet.Export("MyCalculationSet.tca", eCalculationAll)
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.Export("MyCalculationSet.tca", dd.eCalculationAll) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_getindex_icalculationcollection.htm language=enus -->
## TOPIC 01191: Method: GetIndex for Calculations

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_getindex_icalculationcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_getindex_icalculationcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: GetIndex for Calculations

Method: GetIndex for Calculations

Returns the index of a calculation from a calculation group.

```text
iGetIndex = Object.GetIndex(Name)
```

| Object | CalculationsObject with this method |
| --- | --- |
| Name | StringSpecifies the calculation name. |
| iGetIndex | LongIntegerReceives the index of the calculation. |

The following example specifies the index of the calculation Custom from the first calculation group and displays the associated name:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim iGetIndex
iGetIndex = CalculationSet.CalculationGroups(1).Calculations.GetIndex("Custom")
Call MsgBoxDisp(CalculationSet.CalculationGroups(1).Calculations(iGetIndex).Name)
```

[Copy script](javascript:void(0);)

```text
iGetIndex = dd.CalculationSet.CalculationGroups(1).Calculations.GetIndex("Custom") 
dd.MsgBoxDisp(dd.CalculationSet.CalculationGroups(1).Calculations(iGetIndex).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_getindex_icalculationgroupcollection.htm language=enus -->
## TOPIC 01192: Method: GetIndex for CalculationGroups

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_getindex_icalculationgroupcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_getindex_icalculationgroupcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: GetIndex for CalculationGroups

Method: GetIndex for CalculationGroups

Returns the index of a calculation group from the current calculation set.

```text
iGetIndex = Object.GetIndex(Name)
```

| Object | CalculationGroupsObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the calculation group. |
| iGetIndex | LongIntegerReceives the index of the calculation group. |

The following example specifies the index of the calculation group Custom and displays the associated name:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim iGetIndex
iGetIndex = CalculationSet.CalculationGroups.GetIndex("Custom")
Call MsgBoxDisp(CalculationSet.CalculationGroups(iGetIndex).Name)
```

[Copy script](javascript:void(0);)

```text
iGetIndex = dd.CalculationSet.CalculationGroups.GetIndex("Custom") 
dd.MsgBoxDisp(dd.CalculationSet.CalculationGroups(iGetIndex).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_getpostcalculations_icalculation.htm language=enus -->
## TOPIC 01193: Method: GetPostCalculations for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_getpostcalculations_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_getpostcalculations_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: GetPostCalculations for Calculation

Method: GetPostCalculations for Calculation

Returns a collection with the calculations that DIAdem does not execute until DIAdem has executed the actual calculation. The dependencies and the execution sequence of the calculations result from the dependent inputs.

```text
Set oCalculationList = Object.GetPostCalculations
```

| Object | CalculationObject with this method |
| --- | --- |
| oCalculationList | CalculationListReturned collection |

The following example displays the names of the calculations that DIAdem executes after executing the first calculation of the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalc, oMyCalcList, oMyPostCalc
Set oMyCalc = CalculationSet.CalculationGroups(1).Calculations(1)
Set oMyCalcList = oMyCalc.GetPreCalculations()
For Each oMyPostCalc in oMyCalcList
  Call MsgBoxDisp(oMyPostCalc.Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalc = dd.CalculationSet.CalculationGroups(1).Calculations(1) 
oMyCalcList = oMyCalc.GetPreCalculations() 
for oMyPostCalc in oMyCalcList: 
    dd.MsgBoxDisp(oMyPostCalc.Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_getprecalculations_icalculation.htm language=enus -->
## TOPIC 01194: Method: GetPreCalculations for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_getprecalculations_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_getprecalculations_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: GetPreCalculations for Calculation

Method: GetPreCalculations for Calculation

Returns a collection with the calculations that DIAdem executes in the specified order before executing the actual calculation. If DIAdem cannot clearly determine the calculation order, DIAdem displays an error message. The dependencies and the execution sequence of the calculations result from the dependent inputs.

```text
Set oCalculationList = Object.GetPreCalculations
```

| Object | CalculationObject with this method |
| --- | --- |
| oCalculationList | CalculationListReturned collection |

The following example displays the names of the calculations that DIAdem executes before executing the first calculation of the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalc, oMyCalcList, oMyPreCalc
Set oMyCalc = CalculationSet.CalculationGroups(1).Calculations(1)
Set oMyCalcList = oMyCalc.GetPreCalculations()
For Each oMyPreCalc in oMyCalcList
  Call MsgBoxDisp(oMyPreCalc.Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalc = dd.CalculationSet.CalculationGroups(1).Calculations(1) 
oMyCalcList = oMyCalc.GetPreCalculations() 
for oMyPreCalc in oMyCalcList: 
    dd.MsgBoxDisp(oMyPreCalc.Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_getvalidatemessage_icalculation.htm language=enus -->
## TOPIC 01195: Method: GetValidateMessage for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_getvalidatemessage_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_getvalidatemessage_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: GetValidateMessage for Calculation

Method: GetValidateMessage for Calculation

Returns information about the last execution of the [Validate](../methods/formulacalc_method_validate_icalculation.htm) method which indicates why the test failed.

```text
sGetValidateMessage = Object.GetValidateMessage
```

| Object | CalculationObject with this method |
| --- | --- |
| sGetValidateMessage | StringContains the information why the test failed. |

The following example checks the first calculation in the first calculation group. If the calculation is incorrect, the example displays an error message:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim bMyErr
bMyErr = CalculationSet.CalculationGroups(1).Calculations(1).Validate()
If not bMyErr Then
  Call MsgBoxDisp("Error: " & CalculationSet.CalculationGroups(1).Calculations(1).GetValidateMessage())
End If
```

[Copy script](javascript:void(0);)

```text
bMyErr = dd.CalculationSet.CalculationGroups(1).Calculations(1).Validate() 
if not bMyErr : 
    dd.MsgBoxDisp("Error: " + dd.CalculationSet.CalculationGroups(1).Calculations(1).GetValidateMessage()) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_iscrypted_icalculation.htm language=enus -->
## TOPIC 01196: Method: IsCrypted for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_iscrypted_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_iscrypted_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: IsCrypted for Calculation

Method: IsCrypted for Calculation

Specifies whether the calculation is encrypted. If the calculation is encrypted, you cannot view or edit formulas and scripts. However, you can execute the calculation.

```text
bIsCrypted = Object.IsCrypted
```

| Object | CalculationObject with this method |
| --- | --- |
| bIsCrypted | BooleanIf the calculation is encrypted, the IsCrypted method returns the value TRUE, otherwise FALSE. |

The following example displays a message if the first calculation in the first calculation group is encrypted:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If CalculationSet.CalculationGroups(1).Calculations(1).IsCrypted Then
  Call MsgBoxDisp("Calculation has been crypted")
End If
```

[Copy script](javascript:void(0);)

```text
if dd.CalculationSet.CalculationGroups(1).Calculations(1).IsCrypted : 
    dd.MsgBoxDisp("Calculation has been crypted") 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_isoutputconnected_iinput.htm language=enus -->
## TOPIC 01197: Method: IsOutputConnected for Input

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_isoutputconnected_iinput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_isoutputconnected_iinput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: IsOutputConnected for Input

Method: IsOutputConnected for Input

Specifies whether the input of a calculation is dependent on an output of a different calculation.

```text
bIsOutputConnected = Object.IsOutputConnected
```

| Object | InputObject with this method |
| --- | --- |
| bIsOutputConnected | BooleanIf the input of an output is dependent on an output, the IsOutputConnected method returns the value TRUE otherwise FALSE. |

The following example displays a message if the first input of the third calculation is dependent on an output:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(3).Inputs(1)
If oMyInput.IsOutputConnected Then
  Call MsgBoxDisp("Output connected: " & oMyInput.SourceOutput.Calculation.Name)
End If
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(3).Inputs(1) 
if oMyInput.IsOutputConnected : 
    dd.MsgBoxDisp("Output connected: " + oMyInput.SourceOutput.Calculation.Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_overview.htm language=enus -->
## TOPIC 01198: Methods

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > Methods

Methods

Use methods to execute actions. For example, you can use a method to add a new element to a list. Many methods return an object that contains the new element in the list.

The subordinate topics contained in the tree on the contents tab of the Help describe all the methods of the script interface for calculations.

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_runparametrized_icalculation.htm language=enus -->
## TOPIC 01199: Method: RunParametrized for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_runparametrized_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_runparametrized_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: RunParametrized for Calculation

Method: RunParametrized for Calculation

Executes the calculation without resolving the references of the inputs and outputs. Instead, the method uses the contents of the vectors that are specified as parameters. The vectors are assigned to the inputs or to the outputs via the name specified in *Symbols* when the index is the same. The *Values* vector can contain value-unit objects (Value data type), channel objects (Channel data type), and channel object collections (Channel list data type). Ensure that the object type specified in *Values* matches the data type of the input or output that the data type *Symbols* references.

Use the [ValidateParametrized](../methods/formulacalc_method_validateparametrized_icalculation.htm) method to execute the configured validation script.

```text
Object.RunParametrized(Symbols, Values)
```

| Object | CalculationObject with this method |
| --- | --- |
| Symbols | VariantVector that contains the name of the inputs and outputs to which DIAdem assigns the values of Values. |
| Values | VariantVector that contains the values that DIAdem uses for the respective input or output. |

The following example replaces the inputs A and B with the values 2 and 3 when executing and checking the first calculation in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMySymbols(2)
Dim oMyValues(2)
oMySymbols(0) = "A"
Set oMyValues(1) = CreateValueWithUnit(2,"")
oMySymbols(0) = "B"
Set oMyValues(1) = CreateValueWithUnit(3,"")
Dim oMyCalc
Set oMyCalc = CalculationSet.CalculationGroups(1).Calculations(1)
If oMyCalc.ValidateParametrized(oMySymbols,oMyValues) Then
  Call oMyCalc.RunParametrized(oMySymbols,oMyValues)
End If
```

[Copy script](javascript:void(0);)

```text
oMySymbols[0] = "A" 
oMyValues(1) = dd.CreateValueWithUnit(2,"") 
oMySymbols[0] = "B" 
oMyValues(1) = dd.CreateValueWithUnit(3,"") 
oMyCalc = dd.CalculationSet.CalculationGroups(1).Calculations(1) 
if oMyCalc.ValidateParametrized(oMySymbols,oMyValues) : 
    oMyCalc.RunParametrized(oMySymbols,oMyValues) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_save_icalculationset.htm language=enus -->
## TOPIC 01200: Method: Save for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_save_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_save_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: Save for CalculationSet

Method: Save for CalculationSet

Saves the current calculation set in the current calculation set file. The [FileName](../properties/formulacalc_property_filename_icalculationset.htm) property contains the name of the calculation set file.

```text
Object.Save
```

| Object | CalculationSetObject with this method |
| --- | --- |

The following example saves the current calculation set:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call CalculationSet.Save()
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.Save() 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_selectall_icalculationgroup.htm language=enus -->
## TOPIC 01201: Method: SelectAll for CalculationGroup

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_selectall_icalculationgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_selectall_icalculationgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: SelectAll for CalculationGroup

Method: SelectAll for CalculationGroup

Selects or deselects all the calculations of the calculation group.

```text
Object.SelectAll(SelectValue)
```

| Object | CalculationGroupObject with this method |
| --- | --- |
| SelectValue | BooleanSpecifies whether DIAdem selects all calculations (TRUE) or whether DIAdem deselects all calculations (FALSE). |

The following example selects the first and the second calculation of the Crash calculation group and executes them.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyRunedCalculations
Call CalculationSet.CalculationGroups("Crash").SelectAll(FALSE)
CalculationSet.CalculationGroups("Crash").Calculations(1).Selected = TRUE
CalculationSet.CalculationGroups("Crash").Calculations(2).Selected = TRUE
Set oMyRunedCalculations = CalculationSet.RunSelected
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.CalculationGroups("Crash").SelectAll(False) 
CalculationSet.CalculationGroups("Crash").Calculations(1).Selected = True 
CalculationSet.CalculationGroups("Crash").Calculations(2).Selected = True 
oMyRunedCalculations = dd.CalculationSet.RunSelected 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_selectall_icalculationset.htm language=enus -->
## TOPIC 01202: Method: SelectAll for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_selectall_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_selectall_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: SelectAll for CalculationSet

Method: SelectAll for CalculationSet

Selects or deselects all calculations.

```text
Object.SelectAll(SelectValue)
```

| Object | CalculationSetObject with this method |
| --- | --- |
| SelectValue | BooleanSpecifies whether DIAdem selects all calculations (TRUE) or whether DIAdem deselects all calculations (FALSE). |

The following example selects the first and the second calculation of the Crash calculation group and executes them.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyRunedCalculations
Call CalculationSet.SelectAll(FALSE)
CalculationSet.CalculationGroups("Crash").Calculations(1).Selected = TRUE
CalculationSet.CalculationGroups("Crash").Calculations(2).Selected = TRUE
Set oMyRunedCalculations = CalculationSet.RunSelected
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.SelectAll(False) 
CalculationSet.CalculationGroups("Crash").Calculations(1).Selected = True 
CalculationSet.CalculationGroups("Crash").Calculations(2).Selected = True 
oMyRunedCalculations = dd.CalculationSet.RunSelected 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_showexecutiondlg_icalculationset.htm language=enus -->
## TOPIC 01203: Method: ShowExecutionDlg for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_showexecutiondlg_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_showexecutiondlg_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: ShowExecutionDlg for CalculationSet

Method: ShowExecutionDlg for CalculationSet

Opens the dialog box for the execution of calculations.

```text
sShowExecutionDlg = Object.ShowExecutionDlg
```

| Object | CalculationSetObject with this method |
| --- | --- |
| sShowExecutionDlg | StringReceives the status of the dialog box after you exit it. The return value is a DlgState type. |

The following example opens the dialog box for the execution of calculations:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call CalculationSet.ShowExecutionDlg()
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.ShowExecutionDlg() 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_showsettingsdlg_icalculationset.htm language=enus -->
## TOPIC 01204: Method: ShowSettingsDlg for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_showsettingsdlg_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_showsettingsdlg_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: ShowSettingsDlg for CalculationSet

Method: ShowSettingsDlg for CalculationSet

Opens the dialog box for editing a calculation set.

```text
sShowSettingsDlg = Object.ShowSettingsDlg
```

| Object | CalculationSetObject with this method |
| --- | --- |
| sShowSettingsDlg | StringReceives the status of the dialog box after you exit it. The return value is a DlgState type. |

The following example opens the dialog box for editing a calculation set:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call CalculationSet.ShowSettingsDlg()
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.ShowSettingsDlg() 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_validate_icalculation.htm language=enus -->
## TOPIC 01205: Method: Validate for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_validate_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_validate_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: Validate for Calculation

Method: Validate for Calculation

Checks whether DIAdem can execute the calculation. DIAdem checks whether the input references and the output references of the calculation can be resolved. DIAdem also executes the [Validation script](../properties/formulacalc_property_validationscript_icalculation.htm), in which you can specify further conditions for the execution of the calculation.

If the calculation expects input from the output of another calculation, DIAdem also checks this calculation. DIAdem checks in the required order of the execution. If DIAdem cannot determine the execution sequence, the calculation cannot be executed.

If the calculation is incorrect, DIAdem neither outputs an error message nor aborts the executing script. If the test fails, the [GetValidateMessage](../methods/formulacalc_method_getvalidatemessage_icalculation.htm) method contains the information about the error cause.

Use the [ValidateSelected](../methods/formulacalc_method_validateselected_icalculationset.htm) method of the calculation set to execute the validation scripts of all selected calculations.

```text
bValidate = Object.Validate
```

| Object | CalculationObject with this method |
| --- | --- |
| bValidate | BooleanIf DIAdem can execute the calculation, the Validate method returns the value TRUE, otherwise FALSE. |

The following example checks the first calculation in the first calculation group. If the calculation is incorrect, the example displays an error message:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim bNoErr
bNoErr = CalculationSet.CalculationGroups(1).Calculations(1).Validate()
If not bNoErr Then
  Call MsgBoxDisp("Error: " & CalculationSet.CalculationGroups(1).Calculations(1).GetValidateMessage())
End If
```

[Copy script](javascript:void(0);)

```text
bNoErr = dd.CalculationSet.CalculationGroups(1).Calculations(1).Validate() 
if not bNoErr : 
    dd.MsgBoxDisp("Error: " + dd.CalculationSet.CalculationGroups(1).Calculations(1).GetValidateMessage()) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_validateparametrized_icalculation.htm language=enus -->
## TOPIC 01206: Method: ValidateParametrized for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_validateparametrized_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_validateparametrized_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: ValidateParametrized for Calculation

Method: ValidateParametrized for Calculation

Checks the calculation without resolving the input and output references and executes the [Validation script](../properties/formulacalc_property_validationscript_icalculation.htm).

Instead of the input and output references, the method uses the vector contents that are specified as parameters. The vectors are assigned to the inputs or to the outputs via the name specified in *Symbols* when the index is the same. The *Values* vector can contain value-unit objects (Value data type), channel objects (Channel data type), and channel object collections (Channel list data type). Ensure that the object type specified in *Values* matches the data type of the input or output that the data type *Symbols* references.

Use the [RunParametrized](../methods/formulacalc_method_runparametrized_icalculation.htm) method to execute the configured calculation script.

```text
bValidateParametrized = Object.ValidateParametrized(Symbols, Values)
```

| Object | CalculationObject with this method |
| --- | --- |
| Symbols | VariantVector that contains the name of the inputs and outputs to which DIAdem assigns the values of Values. |
| Values | VariantVector that contains the values that DIAdem uses for the respective input or output. |
| bValidateParametrized | BooleanIf the check is error free, the ValidateParametrized method returns the value TRUE, otherwise FALSE. |

The following example replaces the inputs A and B with the values 2 and 3 when executing and checking the first calculation in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMySymbols(2)
Dim oMyValues(2)
oMySymbols(0) = "A"
Set oMyValues(0) = CreateValueWithUnit(2,"")
oMySymbols(1) = "B"
Set oMyValues(1) = CreateValueWithUnit(3,"")
Dim oMyCalc
Set oMyCalc = CalculationSet.CalculationGroups(1).Calculations(1)
If oMyCalc.ValidateParametrized(oMySymbols,oMyValues) Then
  Call oMyCalc.RunParametrized(oMySymbols,oMyValues)
End If
```

[Copy script](javascript:void(0);)

```text
oMySymbols[0] = "A" 
oMyValues(0) = dd.CreateValueWithUnit(2,"") 
oMySymbols[1] = "B" 
oMyValues(1) = dd.CreateValueWithUnit(3,"") 
oMyCalc = dd.CalculationSet.CalculationGroups(1).Calculations(1) 
if oMyCalc.ValidateParametrized(oMySymbols,oMyValues) : 
    oMyCalc.RunParametrized(oMySymbols,oMyValues) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/methods/formulacalc_method_validateselected_icalculationset.htm language=enus -->
## TOPIC 01207: Method: ValidateSelected for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/methods/formulacalc_method_validateselected_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/methods/formulacalc_method_validateselected_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Methods](../methods/formulacalc_method_overview.htm) > Method: ValidateSelected for CalculationSet

Method: ValidateSelected for CalculationSet

Checks whether DIAdem can execute the selected calculations. The [Selected](../properties/formulacalc_property_selected_icalculation.htm) property of a calculation specifies whether the calculation is selected.

DIAdem checks whether the input references and the output references of each calculation can be removed. DIAdem also executes the [Validation script](../properties/formulacalc_property_validationscript_icalculation.htm) in which you can specify further conditions for the execution of each calculation.

If a calculation expects input from the output of another calculation, DIAdem also checks this calculation. DIAdem checks in the required order of the execution. If DIAdem cannot determine the execution sequence, the calculation cannot run.

If the inspection fails, DIAdem writes the list of incorrect calculations in the FailedCalculationsparameter.

Use the [Validate](../methods/formulacalc_method_validate_icalculation.htm) method of a calculation to execute the validation script of each calculation.

```text
bValidateSelected = Object.ValidateSelected([FailedCalculations])
```

| Object | CalculationSetObject with this method |
| --- | --- |
| [FailedCalculations] | CalculationListReturned collection of failed calculations |
| bValidateSelected | BooleanIf DIAdem can execute the calculation, the ValidateSelected method returns the value TRUE, otherwise FALSE. |

The following example checks all calculations. If calculations are incorrect, the example outputs the name of the first incorrect calculation:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyValidatedCalculations
Call CalculationSet.SelectAll(TRUE) 
If not CalculationSet.ValidateSelected(oMyValidatedCalculations) Then
  Call MsgBoxDisp("Invalid calculation: " & oMyValidatedCalculations(1).Name)
End If
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.SelectAll(True) 
if not dd.CalculationSet.ValidateSelected(oMyValidatedCalculations) : 
    dd.MsgBoxDisp("Invalid calculation: " + oMyValidatedCalculations(1).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_names.htm language=enus -->
## TOPIC 01208: Name Conventions for Calculations

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_names.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_names.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > Name Conventions for Calculations

Name Conventions for Calculations

If you use one of the following characters in the name of a calculation or of a calculation group, DIAdem replaces this character with the character in the right column of the table. The text *Name* stands for the entire channel name:

| Character | Replacement |
| --- | --- |
| / | \\ |
| * | x |
| ? | ! |
| ' | ` |
| [Name] | (Name) |

The names of inputs and outputs of a calculation must comply with the following rules:

- The name must begin with a letter.
- The maximum name length is 255 characters.
- The name may only contain ASCII characters.
- The name must not contain any special characters other than the underscore.
- The name must not be the same as a VBS keyword.

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_icalculation.htm language=enus -->
## TOPIC 01209: Object: Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([CalculationList](../objects/formulacalc_objects_icalculationlist.htm) | [Calculations](../objects/formulacalc_objects_icalculationcollection.htm) | [Input](../objects/formulacalc_objects_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm)) > Object: Calculation

Object: Calculation

The Calculation object provides a calculation. The Calculation object is an element of the [Calculations](../objects/formulacalc_objects_icalculationcollection.htm) collection.

The following example generates a new calculation in the first calculation group and assigns an appropriate description to the calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalcTemp
Set oMyCalcTemp = CalculationSet.CalculationGroups(1).Calculations.Add("Resultant")
oMyCalcTemp.Description = "Resultant of Head Acceleration"
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups(1).Calculations.Add("Resultant") 
oMyCalcTemp.Description = "Resultant of Head Acceleration" 
```

#### Properties

[CalculationGroup](../properties/formulacalc_property_calculationgroup_icalculation.htm) | [CalculationScript](../properties/formulacalc_property_calculationscript_icalculation.htm) | [Description](../properties/formulacalc_property_description_icalculation.htm) | [Inputs](../properties/formulacalc_property_inputs_icalculation.htm) | [Name](../properties/formulacalc_property_name_icalculation.htm) | [Outputs](../properties/formulacalc_property_outputs_icalculation.htm) | [QuantityBased](../properties/formulacalc_property_quantitybased_icalculation.htm) | [RunCount](../properties/formulacalc_property_runcount_icalculation.htm) | [Selected](../properties/formulacalc_property_selected_icalculation.htm) | [Tag](../properties/formulacalc_property_tag_icalculation.htm) | [ValidationScript](../properties/formulacalc_property_validationscript_icalculation.htm)

#### Methods

[GetPostCalculations](../methods/formulacalc_method_getpostcalculations_icalculation.htm) | [GetPreCalculations](../methods/formulacalc_method_getprecalculations_icalculation.htm) | [GetValidateMessage](../methods/formulacalc_method_getvalidatemessage_icalculation.htm) | [IsCrypted](../methods/formulacalc_method_iscrypted_icalculation.htm) | [Run](../methods/formulacalc_method_run_icalculation.htm) | [RunParametrized](../methods/formulacalc_method_runparametrized_icalculation.htm) | [Validate](../methods/formulacalc_method_validate_icalculation.htm) | [ValidateParametrized](../methods/formulacalc_method_validateparametrized_icalculation.htm)

#### Returned From

[CalculationList](../objects/formulacalc_objects_icalculationlist.htm).[Item](../methods/formulacalc_method_item_icalculationlist.htm) | [Calculations](../objects/formulacalc_objects_icalculationcollection.htm).[Add](../methods/formulacalc_method_add_icalculationcollection.htm) | [Calculations](../objects/formulacalc_objects_icalculationcollection.htm).[Item](../methods/formulacalc_method_item_icalculationcollection.htm) | [Input](../objects/formulacalc_objects_iinput.htm).[Calculation](../properties/formulacalc_property_calculation_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm).[Calculation](../properties/formulacalc_property_calculation_ioutput.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_icalculationcollection.htm language=enus -->
## TOPIC 01210: Collection: Calculations

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_icalculationcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_icalculationcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([CalculationGroup](../objects/formulacalc_objects_icalculationgroup.htm) | [Collections](../objects/icalculationset_objects_collections.htm)) > Collection: Calculations

Collection: Calculations

Collection of all [Calculations](../objects/formulacalc_objects_icalculation.htm) of a calculation group. To access an individual calculation in a script use the [Item](../methods/formulacalc_method_item_icalculationcollection.htm) method or enter the index or the name in parentheses.

The following example displays the names of all calculations in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcTemp, oMyCalc
Set oMyCalcTemp = CalculationSet.CalculationGroups(1).Calculations
For Each oMyCalc in oMyCalcTemp
  Call MsgBoxDisp("Name of calculation: " & oMyCalc.Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups(1).Calculations 
for oMyCalc in oMyCalcTemp: 
    dd.MsgBoxDisp("Name of calculation: " + oMyCalc.Name) 
```

#### Properties

[Count](../properties/formulacalc_property_count_icalculationcollection.htm)

#### Methods

[Add](../methods/formulacalc_method_add_icalculationcollection.htm) | [Exists](../methods/formulacalc_method_exists_icalculationcollection.htm) | [GetIndex](../methods/formulacalc_method_getindex_icalculationcollection.htm) | [Item](../methods/formulacalc_method_item_icalculationcollection.htm) | [Remove](../methods/formulacalc_method_remove_icalculationcollection.htm) | [RemoveAll](../methods/formulacalc_method_removeall_icalculationcollection.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_icalculationgroup.htm language=enus -->
## TOPIC 01211: Object: CalculationGroup

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_icalculationgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_icalculationgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Calculation](../objects/formulacalc_objects_icalculation.htm) | [CalculationGroups](../objects/formulacalc_objects_icalculationgroupcollection.htm)) > Object: CalculationGroup

Object: CalculationGroup

The CalculationGroup object provides a calculation group. The CalculationGroup object is an element of the [CalculationGroups](../objects/formulacalc_objects_icalculationgroupcollection.htm) collection.

The following example generates a new calculation group and assigns an appropriate description to the calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalcGroup
Set oMyCalcGroup = CalculationSet.CalculationGroups.Add("Head_EuroNCAP")
oMyCalcGroup.Description = "Head Criterion - European New Car Assessment Program"
```

[Copy script](javascript:void(0);)

```text
oMyCalcGroup = dd.CalculationSet.CalculationGroups.Add("Head_EuroNCAP") 
oMyCalcGroup.Description = "Head Criterion - European New Car Assessment Program" 
```

#### Properties

[Calculations](../properties/formulacalc_property_calculations_icalculationgroup.htm) | [Description](../properties/formulacalc_property_description_icalculationgroup.htm) | [Name](../properties/formulacalc_property_name_icalculationgroup.htm) | [Tag](../properties/formulacalc_property_tag_icalculationgroup.htm)

#### Methods

[SelectAll](../methods/formulacalc_method_selectall_icalculationgroup.htm)

#### Returned From

[Calculation](../objects/formulacalc_objects_icalculation.htm).[CalculationGroup](../properties/formulacalc_property_calculationgroup_icalculation.htm) | [CalculationGroups](../objects/formulacalc_objects_icalculationgroupcollection.htm).[Add](../methods/formulacalc_method_add_icalculationgroupcollection.htm) | [CalculationGroups](../objects/formulacalc_objects_icalculationgroupcollection.htm).[Item](../methods/formulacalc_method_item_icalculationgroupcollection.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_icalculationgroupcollection.htm language=enus -->
## TOPIC 01212: Collection: CalculationGroups

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_icalculationgroupcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_icalculationgroupcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([CalculationSet](../objects/formulacalc_objects_icalculationset.htm) | [Collections](../objects/icalculationset_objects_collections.htm)) > Collection: CalculationGroups

Collection: CalculationGroups

Collection of all [Calculation groups](../objects/formulacalc_objects_icalculationgroup.htm) in a calculation set. To access a single calculation group in scripts, either use the [Item](../methods/formulacalc_method_item_icalculationgroupcollection.htm) method or enter the index or the name in parentheses.

The following example displays the names of the individual calculation groups:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalcGroup, sText
For Each oMyCalcGroup in CalculationSet.CalculationGroups
  sText = sText & "Calculation Group : " & oMyCalcGroup.Name & vbCRLF
Next
Call MsgBoxDisp(sText)
```

[Copy script](javascript:void(0);)

```text
for oMyCalcGroup in dd.CalculationSet.CalculationGroups: 
    sText = sText + "Calculation Group : " + oMyCalcGroup.Name + "\r\n" 
dd.MsgBoxDisp(sText) 
```

#### Properties

[Count](../properties/formulacalc_property_count_icalculationgroupcollection.htm)

#### Methods

[Add](../methods/formulacalc_method_add_icalculationgroupcollection.htm) | [Exists](../methods/formulacalc_method_exists_icalculationgroupcollection.htm) | [GetIndex](../methods/formulacalc_method_getindex_icalculationgroupcollection.htm) | [Item](../methods/formulacalc_method_item_icalculationgroupcollection.htm) | [Remove](../methods/formulacalc_method_remove_icalculationgroupcollection.htm) | [RemoveAll](../methods/formulacalc_method_removeall_icalculationgroupcollection.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_icalculationlist.htm language=enus -->
## TOPIC 01213: Collection: CalculationList

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_icalculationlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_icalculationlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Calculation](../objects/formulacalc_objects_icalculation.htm) | [CalculationSet](../objects/formulacalc_objects_icalculationset.htm) | [Collections](../objects/icalculationset_objects_collections.htm)) > Collection: CalculationList

Collection: CalculationList

[Calculations](../objects/formulacalc_objects_icalculation.htm) collection.

If a calculation requires an output from an other calculation as an input, DIAdem first executes the other calculation. DIAdem uses this method to specify the sequence in which calculations are to be executed, and automatically expands the volume of calculations to be executed, if required.

This collection is not name oriented so that the collection can contain objects with the same name. Use the [Item](../methods/formulacalc_method_item_icalculationlist.htm) method or specify the index in parenthesis to access an individual input in this collection in scripts. You cannot change the collection elements.

The following example executes selected calculations and then displays the number of executed calculations:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyRunedCalculations
Call CalculationSet.SelectAll(TRUE)
Set oMyRunedCalculations = CalculationSet.RunSelected()
Call MsgBoxDisp("No of calculations: " & oMyRunedCalculations.Count)
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.SelectAll(True) 
oMyRunedCalculations = dd.CalculationSet.RunSelected() 
dd.MsgBoxDisp("No of calculations: " + oMyRunedCalculations.Count) 
```

#### Properties

[Count](../properties/formulacalc_property_count_icalculationlist.htm)

#### Methods

[Item](../methods/formulacalc_method_item_icalculationlist.htm)

#### Returned From

[Calculation](../objects/formulacalc_objects_icalculation.htm).[GetPostCalculations](../methods/formulacalc_method_getpostcalculations_icalculation.htm) | [Calculation](../objects/formulacalc_objects_icalculation.htm).[GetPreCalculations](../methods/formulacalc_method_getprecalculations_icalculation.htm) | [Calculation](../objects/formulacalc_objects_icalculation.htm).[Run](../methods/formulacalc_method_run_icalculation.htm) | [CalculationSet](../objects/formulacalc_objects_icalculationset.htm).[RunSelected](../methods/formulacalc_method_runselected_icalculationset.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_icalculationset.htm language=enus -->
## TOPIC 01214: Object: CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Objects](../objects/icalculationset_objects_overview.htm) > Object: CalculationSet

Object: CalculationSet

The CalculationSet object enables access to a calculation set. Use the CalculationSet object to load and to save the calculation sets. In scripts the CalculationSet object is available as a global object. Do not create an object or a variable with the name CalculationSet, because that overwrites the CalculationSet object.

The following example displays the names of the individual calculation groups and the associated calculations:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCalcGroup, oMyCalcTemp, sText
For Each oMyCalcGroup in CalculationSet.CalculationGroups
  sText = "Calculation Group : " & oMyCalcGroup.Name & vbCRLF
  For Each oMyCalcTemp in oMyCalcGroup.Calculations
    sText = sText & "Calculation: " & oMyCalcTemp.Name & vbCRLF
  Next
  Call MsgBoxDisp(sText)
Next
```

[Copy script](javascript:void(0);)

```text
for oMyCalcGroup in dd.CalculationSet.CalculationGroups: 
    sText = "Calculation Group : " + oMyCalcGroup.Name + "\r\n" 
    for oMyCalcTemp in oMyCalcGroup.Calculations: 
        sText = sText + "Calculation: " + oMyCalcTemp.Name + "\r\n" 
    dd.MsgBoxDisp(sText) 
```

#### Properties

[CalculationGroups](../properties/formulacalc_property_calculationgroups_icalculationset.htm) | [Description](../properties/formulacalc_property_description_icalculationset.htm) | [FileName](../properties/formulacalc_property_filename_icalculationset.htm) | [Name](../properties/formulacalc_property_name_icalculationset.htm)

#### Methods

[Append](../methods/formulacalc_method_append_icalculationset.htm) | [Clear](../methods/formulacalc_method_clear_icalculationset.htm) | [Copy](../methods/formulacalc_method_copy_icalculationset.htm) | [Export](../methods/formulacalc_method_export_icalculationset.htm) | [IsModified](../methods/formulacalc_method_ismodified_icalculationset.htm) | [Load](../methods/formulacalc_method_load_icalculationset.htm) | [Move](../methods/formulacalc_method_move_icalculationset.htm) | [RunSelected](../methods/formulacalc_method_runselected_icalculationset.htm) | [Save](../methods/formulacalc_method_save_icalculationset.htm) | [SaveAs](../methods/formulacalc_method_saveas_icalculationset.htm) | [SelectAll](../methods/formulacalc_method_selectall_icalculationset.htm) | [ShowExecutionDlg](../methods/formulacalc_method_showexecutiondlg_icalculationset.htm) | [ShowSettingsDlg](../methods/formulacalc_method_showsettingsdlg_icalculationset.htm) | [ValidateSelected](../methods/formulacalc_method_validateselected_icalculationset.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_iformulaadaptor.htm language=enus -->
## TOPIC 01215: Object: InputOrOutput

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_iformulaadaptor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_iformulaadaptor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Reference](../objects/formulacalc_objects_ireferenceabstract.htm) | [ReferenceChannel](../objects/formulacalc_objects_ireferencechannel.htm) | [ReferenceChannelGroupProperty](../objects/formulacalc_objects_ireferencechannelgroupproperty.htm) | [ReferenceChannelList](../objects/formulacalc_objects_ireferencechannellist.htm) | [ReferenceChannelProperty](../objects/formulacalc_objects_ireferencechannelproperty.htm) | [ReferenceDatasetProperty](../objects/formulacalc_objects_ireferencedatasetproperty.htm) | [ReferenceValue](../objects/formulacalc_objects_ireferencevalue.htm)) > Object: InputOrOutput

Object: InputOrOutput

The InputOrOutput object provides a calculation input or output.

The InputOrOutput object corresponds to one of the following objects:

| Input (IInput) | The Input object provides a calculation input. |
| --- | --- |
| Output (IOutput) | The Output object provides a calculation output. |

The pages of the objects [Input](../objects/formulacalc_objects_iinput.htm) and [Output](../objects/formulacalc_objects_ioutput.htm) contain examples.

#### Properties

[AdaptorType](../properties/formulacalc_property_adaptortype_iformulaadaptor.htm) | [Calculation](../properties/formulacalc_property_calculation_iformulaadaptor.htm) | [Name](../properties/formulacalc_property_name_iformulaadaptor.htm) | [Optional](../properties/formulacalc_property_optional_iformulaadaptor.htm) | [Reference](../properties/formulacalc_property_reference_iformulaadaptor.htm) | [ReferenceType](../properties/formulacalc_property_referencetype_iformulaadaptor.htm) | [Tag](../properties/formulacalc_property_tag_iformulaadaptor.htm)

#### Returned From

[Reference](../objects/formulacalc_objects_ireferenceabstract.htm).[Parent](../properties/formulacalc_property_parent_ireferenceabstract.htm) | [ReferenceChannel](../objects/formulacalc_objects_ireferencechannel.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannel.htm) | [ReferenceChannelGroupProperty](../objects/formulacalc_objects_ireferencechannelgroupproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannelgroupproperty.htm) | [ReferenceChannelList](../objects/formulacalc_objects_ireferencechannellist.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannellist.htm) | [ReferenceChannelProperty](../objects/formulacalc_objects_ireferencechannelproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannelproperty.htm) | [ReferenceDatasetProperty](../objects/formulacalc_objects_ireferencedatasetproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencedatasetproperty.htm) | [ReferenceValue](../objects/formulacalc_objects_ireferencevalue.htm).[Parent](../properties/formulacalc_property_parent_ireferencevalue.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_iinput.htm language=enus -->
## TOPIC 01216: Object: Input

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_iinput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_iinput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([InputList](../objects/formulacalc_objects_iinputlist.htm) | [Inputs](../objects/formulacalc_objects_iinputcollection.htm) | [Reference](../objects/formulacalc_objects_ireferenceabstract.htm) | [ReferenceChannel](../objects/formulacalc_objects_ireferencechannel.htm) | [ReferenceChannelGroupProperty](../objects/formulacalc_objects_ireferencechannelgroupproperty.htm) | [ReferenceChannelList](../objects/formulacalc_objects_ireferencechannellist.htm) | [ReferenceChannelProperty](../objects/formulacalc_objects_ireferencechannelproperty.htm) | [ReferenceDatasetProperty](../objects/formulacalc_objects_ireferencedatasetproperty.htm) | [ReferenceValue](../objects/formulacalc_objects_ireferencevalue.htm)) > Object: Input

Object: Input

The Input object provides a calculation input. The Input object is an element of the [Inputs](../objects/formulacalc_objects_iinputcollection.htm) collection.

The following example displays the calculations on which the inputs of the first calculation in the first calculation group are dependent:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
For Each oMyInput In CalculationSet.CalculationGroups(1).Calculations(1).Inputs
  If oMyInput.IsOutputConnected Then
    Call MsgBoxDisp("Input depending on calculation: " & oMyInput.SourceOutput.Calculation.Name)
  End If
Next
```

[Copy script](javascript:void(0);)

```text
for oMyInput in dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs: 
    if oMyInput.IsOutputConnected : 
        dd.MsgBoxDisp("Input depending on calculation: " + oMyInput.SourceOutput.Calculation.Name) 
```

#### Properties

[AdaptorType](../properties/formulacalc_property_adaptortype_iinput.htm) | [Calculation](../properties/formulacalc_property_calculation_iinput.htm) | [Name](../properties/formulacalc_property_name_iinput.htm) | [Optional](../properties/formulacalc_property_optional_iinput.htm) | [Reference](../properties/formulacalc_property_reference_iinput.htm) | [ReferenceType](../properties/formulacalc_property_referencetype_iinput.htm) | [SourceOutput](../properties/formulacalc_property_sourceoutput_iinput.htm) | [Tag](../properties/formulacalc_property_tag_iinput.htm)

#### Methods

[ConnectOutput](../methods/formulacalc_method_connectoutput_iinput.htm) | [DisconnectOutput](../methods/formulacalc_method_disconnectoutput_iinput.htm) | [IsOutputConnected](../methods/formulacalc_method_isoutputconnected_iinput.htm)

#### Returned From

[InputList](../objects/formulacalc_objects_iinputlist.htm).[Item](../methods/formulacalc_method_item_iinputlist.htm) | [Inputs](../objects/formulacalc_objects_iinputcollection.htm).[Add](../methods/formulacalc_method_add_iinputcollection.htm) | [Inputs](../objects/formulacalc_objects_iinputcollection.htm).[AddByOutput](../methods/formulacalc_method_addbyoutput_iinputcollection.htm) | [Inputs](../objects/formulacalc_objects_iinputcollection.htm).[Item](../methods/formulacalc_method_item_iinputcollection.htm) | [Reference](../objects/formulacalc_objects_ireferenceabstract.htm).[Parent](../properties/formulacalc_property_parent_ireferenceabstract.htm) | [ReferenceChannel](../objects/formulacalc_objects_ireferencechannel.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannel.htm) | [ReferenceChannelGroupProperty](../objects/formulacalc_objects_ireferencechannelgroupproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannelgroupproperty.htm) | [ReferenceChannelList](../objects/formulacalc_objects_ireferencechannellist.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannellist.htm) | [ReferenceChannelProperty](../objects/formulacalc_objects_ireferencechannelproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannelproperty.htm) | [ReferenceDatasetProperty](../objects/formulacalc_objects_ireferencedatasetproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencedatasetproperty.htm) | [ReferenceValue](../objects/formulacalc_objects_ireferencevalue.htm).[Parent](../properties/formulacalc_property_parent_ireferencevalue.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_iinputcollection.htm language=enus -->
## TOPIC 01217: Collection: Inputs

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_iinputcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_iinputcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Calculation](../objects/formulacalc_objects_icalculation.htm) | [Collections](../objects/icalculationset_objects_collections.htm)) > Collection: Inputs

Collection: Inputs

Collection of all [Inputs](../objects/formulacalc_objects_iinput.htm) of a calculation. To access an individual input in scripts, use the [Item](../methods/formulacalc_method_item_iinputcollection.htm) method, or enter the index or the name in parentheses.

The following example displays the names of all inputs of the first calculation in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcInputs, oMyInput
Set oMyCalcInputs = CalculationSet.CalculationGroups(1).Calculations(1).Inputs
For Each oMyInput in oMyCalcInputs
  Call MsgBoxDisp("Name of input: " & oMyInput.Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcInputs = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs 
for oMyInput in oMyCalcInputs: 
    dd.MsgBoxDisp("Name of input: " + oMyInput.Name) 
```

#### Properties

[Count](../properties/formulacalc_property_count_iinputcollection.htm)

#### Methods

[Add](../methods/formulacalc_method_add_iinputcollection.htm) | [AddByOutput](../methods/formulacalc_method_addbyoutput_iinputcollection.htm) | [Exists](../methods/formulacalc_method_exists_iinputcollection.htm) | [Item](../methods/formulacalc_method_item_iinputcollection.htm) | [Move](../methods/formulacalc_method_move_iinputcollection.htm) | [Remove](../methods/formulacalc_method_remove_iinputcollection.htm) | [RemoveAll](../methods/formulacalc_method_removeall_iinputcollection.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_iinputlist.htm language=enus -->
## TOPIC 01218: Collection: InputList

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_iinputlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_iinputlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/icalculationset_objects_collections.htm) | [Output](../objects/formulacalc_objects_ioutput.htm)) > Collection: InputList

Collection: InputList

Collection of all the [Inputs](../objects/formulacalc_objects_iinput.htm) that are dependent on an output of a calculation. This collection is not name oriented so that the collection can contain objects with the same name. Use the [Item](../methods/formulacalc_method_item_iinputlist.htm) method or specify the index in parenthesis to access an individual input in this collection in scripts. You cannot change the collection elements.

The following example displays the number of inputs that are dependent on the first output of the first calculation in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDepInputs
Set oMyDepInputs = CalculationSet.CalculationGroups(1).Calculations(1).Outputs(1).TargetInputs
Call MsgBoxDisp("No of inputs depending on output: " & oMyDepInputs.Count)
```

[Copy script](javascript:void(0);)

```text
oMyDepInputs = dd.CalculationSet.CalculationGroups(1).Calculations(1).Outputs(1).TargetInputs 
dd.MsgBoxDisp("No of inputs depending on output: " + oMyDepInputs.Count) 
```

#### Properties

[Count](../properties/formulacalc_property_count_iinputlist.htm)

#### Methods

[Item](../methods/formulacalc_method_item_iinputlist.htm)

#### Returned From

[Output](../objects/formulacalc_objects_ioutput.htm).[TargetInputs](../properties/formulacalc_property_targetinputs_ioutput.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_ioutput.htm language=enus -->
## TOPIC 01219: Object: Output

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_ioutput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_ioutput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Input](../objects/formulacalc_objects_iinput.htm) | [Outputs](../objects/formulacalc_objects_ioutputcollection.htm) | [Reference](../objects/formulacalc_objects_ireferenceabstract.htm) | [ReferenceChannel](../objects/formulacalc_objects_ireferencechannel.htm) | [ReferenceChannelGroupProperty](../objects/formulacalc_objects_ireferencechannelgroupproperty.htm) | [ReferenceChannelList](../objects/formulacalc_objects_ireferencechannellist.htm) | [ReferenceChannelProperty](../objects/formulacalc_objects_ireferencechannelproperty.htm) | [ReferenceDatasetProperty](../objects/formulacalc_objects_ireferencedatasetproperty.htm) | [ReferenceValue](../objects/formulacalc_objects_ireferencevalue.htm)) > Object: Output

Object: Output

The Output object provides a calculation output. The Output object is an element of the [Outputs](../objects/formulacalc_objects_ioutputcollection.htm) collection.

The following example displays the number of inputs that are dependent on the first output in the first calculation:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyOutput
Set oMyOutput = CalculationSet.CalculationGroups(1).Calculations(1).Outputs(1)
Call MsgBoxDisp("No of inputs depending on output: " & oMyOutput.TargetInputs.Count)
```

[Copy script](javascript:void(0);)

```text
oMyOutput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Outputs(1) 
dd.MsgBoxDisp("No of inputs depending on output: " + oMyOutput.TargetInputs.Count) 
```

#### Properties

[AdaptorType](../properties/formulacalc_property_adaptortype_ioutput.htm) | [Calculation](../properties/formulacalc_property_calculation_ioutput.htm) | [Name](../properties/formulacalc_property_name_ioutput.htm) | [Optional](../properties/formulacalc_property_optional_ioutput.htm) | [Reference](../properties/formulacalc_property_reference_ioutput.htm) | [ReferenceType](../properties/formulacalc_property_referencetype_ioutput.htm) | [Tag](../properties/formulacalc_property_tag_ioutput.htm) | [TargetInputs](../properties/formulacalc_property_targetinputs_ioutput.htm)

#### Returned From

[Input](../objects/formulacalc_objects_iinput.htm).[SourceOutput](../properties/formulacalc_property_sourceoutput_iinput.htm) | [Outputs](../objects/formulacalc_objects_ioutputcollection.htm).[Add](../methods/formulacalc_method_add_ioutputcollection.htm) | [Outputs](../objects/formulacalc_objects_ioutputcollection.htm).[Item](../methods/formulacalc_method_item_ioutputcollection.htm) | [Reference](../objects/formulacalc_objects_ireferenceabstract.htm).[Parent](../properties/formulacalc_property_parent_ireferenceabstract.htm) | [ReferenceChannel](../objects/formulacalc_objects_ireferencechannel.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannel.htm) | [ReferenceChannelGroupProperty](../objects/formulacalc_objects_ireferencechannelgroupproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannelgroupproperty.htm) | [ReferenceChannelList](../objects/formulacalc_objects_ireferencechannellist.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannellist.htm) | [ReferenceChannelProperty](../objects/formulacalc_objects_ireferencechannelproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencechannelproperty.htm) | [ReferenceDatasetProperty](../objects/formulacalc_objects_ireferencedatasetproperty.htm).[Parent](../properties/formulacalc_property_parent_ireferencedatasetproperty.htm) | [ReferenceValue](../objects/formulacalc_objects_ireferencevalue.htm).[Parent](../properties/formulacalc_property_parent_ireferencevalue.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_ioutputcollection.htm language=enus -->
## TOPIC 01220: Collection: Outputs

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_ioutputcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_ioutputcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Calculation](../objects/formulacalc_objects_icalculation.htm) | [Collections](../objects/icalculationset_objects_collections.htm)) > Collection: Outputs

Collection: Outputs

Collection of all [Outputs](../objects/formulacalc_objects_ioutput.htm) of a calculation. To access an individual output in scripts, use the [Item](../methods/formulacalc_method_item_ioutputcollection.htm) method, or enter the index or the name in parentheses.

The following example displays the names of all outputs of the first calculation in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcOutputs, oMyOutput
Set oMyCalcOutputs = CalculationSet.CalculationGroups(1).Calculations(1).Outputs
For Each oMyOutput in oMyCalcOutputs
  Call MsgBoxDisp("Name of output: " & oMyOutput.Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcOutputs = dd.CalculationSet.CalculationGroups(1).Calculations(1).Outputs 
for oMyOutput in oMyCalcOutputs: 
    dd.MsgBoxDisp("Name of output: " + oMyOutput.Name) 
```

#### Properties

[Count](../properties/formulacalc_property_count_ioutputcollection.htm)

#### Methods

[Add](../methods/formulacalc_method_add_ioutputcollection.htm) | [Exists](../methods/formulacalc_method_exists_ioutputcollection.htm) | [Item](../methods/formulacalc_method_item_ioutputcollection.htm) | [Move](../methods/formulacalc_method_move_ioutputcollection.htm) | [Remove](../methods/formulacalc_method_remove_ioutputcollection.htm) | [RemoveAll](../methods/formulacalc_method_removeall_ioutputcollection.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_ireferenceabstract.htm language=enus -->
## TOPIC 01221: Object: Reference

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_ireferenceabstract.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_ireferenceabstract.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Input](../objects/formulacalc_objects_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm)) > Object: Reference

Object: Reference

The Reference object provides a reference for an input or an output of a calculation.

The Reference object corresponds to one of the following objects:

| ReferenceValue (IReferenceValue) | The reference refers to a value (ReferenceType = eReferenceTypeValue). |
| --- | --- |
| ReferenceDatasetProperty (IReferenceDataSetProperty) | The reference refers to a data set property (ReferenceType = eReferenceTypeValue). |
| ReferenceChannelGroupProperty (IReferenceChannelGroupProperty) | The reference refers to a channel group property (ReferenceType = eReferenceTypeValue). |
| ReferenceChannelProperty (IReferenceChannelProperty) | The reference refers to a channel property (ReferenceType = eReferenceTypeValue). |
| ReferenceChannel (IReferenceChannel) | The reference refers to a channel (ReferenceType = eReferenceTypeChannel). |
| ReferenceChannelList (IReferenceChannelList) | The reference refers to a channel list (ReferenceType = eReferenceTypeChannelList). |

The pages of the reference objects contain examples.

#### Properties

[Parent](../properties/formulacalc_property_parent_ireferenceabstract.htm)

#### Returned From

[Input](../objects/formulacalc_objects_iinput.htm).[Reference](../properties/formulacalc_property_reference_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm).[Reference](../properties/formulacalc_property_reference_ioutput.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_ireferencechannel.htm language=enus -->
## TOPIC 01222: Object: ReferenceChannel

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_ireferencechannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_ireferencechannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Input](../objects/formulacalc_objects_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm)) > Object: ReferenceChannel

Object: ReferenceChannel

The ReferenceChannel object provides a channel reference for an input or an output of a calculation. The channel reference specifies which channel DIAdem uses for the execution of the calculation for the input or the output.

The following example defines the input R which is a Channel data type for the first calculation in the first calculation group. Then the example defines with which channel DIAdem replaces the input when the calculation is executed.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeChannel)
oMyInput.ReferenceType = eReferenceTypeChannel
oMyInput.Reference.Channel = "Revs"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeChannel) 
oMyInput.ReferenceType = dd.eReferenceTypeChannel 
oMyInput.Reference.Channel = "Revs" 
```

#### Properties

[Channel](../properties/formulacalc_property_channel_ireferencechannel.htm) | [Parent](../properties/formulacalc_property_parent_ireferencechannel.htm)

#### Returned From

[Input](../objects/formulacalc_objects_iinput.htm).[Reference](../properties/formulacalc_property_reference_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm).[Reference](../properties/formulacalc_property_reference_ioutput.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_ireferencechannelgroupproperty.htm language=enus -->
## TOPIC 01223: Object: ReferenceChannelGroupProperty

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_ireferencechannelgroupproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_ireferencechannelgroupproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Input](../objects/formulacalc_objects_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm)) > Object: ReferenceChannelGroupProperty

Object: ReferenceChannelGroupProperty

The ReferenceChannelGroupProperty object provides a channel group property reference for an input or an output of a calculation. The channel group property reference specifies which channel group property DIAdem uses for the execution of the calculation for the input or the output.

The following example defines the input R which is a Value data type for the first calculation in the first calculation group. Then the example defines with which channel group property DIAdem replaces the input when the calculation is executed.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeValue)
oMyInput.ReferenceType = eReferenceTypeChannelGroupProperty
oMyInput.Reference.ChannelGroup = "Crash"
oMyInput.Reference.PropertyName = "Duration"
oMyInput.Reference.UnitSymbol = "ms"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeValue) 
oMyInput.ReferenceType = dd.eReferenceTypeChannelGroupProperty 
oMyInput.Reference.ChannelGroup = "Crash" 
oMyInput.Reference.PropertyName = "Duration" 
oMyInput.Reference.UnitSymbol = "ms" 
```

#### Properties

[ChannelGroup](../properties/formulacalc_property_channelgroup_ireferencechannelgroupproperty.htm) | [Parent](../properties/formulacalc_property_parent_ireferencechannelgroupproperty.htm) | [PropertyName](../properties/formulacalc_property_propertyname_ireferencechannelgroupproperty.htm) | [UnitPropertyName](../properties/formulacalc_property_unitpropertyname_ireferencechannelgroupproperty.htm) | [UnitSymbol](../properties/formulacalc_property_unitsymbol_ireferencechannelgroupproperty.htm)

#### Returned From

[Input](../objects/formulacalc_objects_iinput.htm).[Reference](../properties/formulacalc_property_reference_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm).[Reference](../properties/formulacalc_property_reference_ioutput.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/objects/formulacalc_objects_ireferencechannellist.htm language=enus -->
## TOPIC 01224: Object: ReferenceChannelList

- bundle_id: `diadem`
- source_path: `icalculationset/objects/formulacalc_objects_ireferencechannellist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/objects/formulacalc_objects_ireferencechannellist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Input](../objects/formulacalc_objects_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm)) > Object: ReferenceChannelList

Object: ReferenceChannelList

The ReferenceChannelList object provides a channel list reference for an input or an output of a calculation. The channel list reference specifies which channels DIAdem uses for the execution of the calculation for the input or the output.

The following example defines the input R which is a Channel list data type for the first calculation in the first calculation group. Then the example defines with which channels DIAdem replaces the input when the calculation is executed.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeChannelList)
oMyInput.ReferenceType = eReferenceTypeChannelList
oMyInput.Reference.ChannelList = "'Revs_1','Revs_3'"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeChannelList) 
oMyInput.ReferenceType = dd.eReferenceTypeChannelList 
oMyInput.Reference.ChannelList = "'Revs_1','Revs_3'" 
```

#### Properties

[ChannelList](../properties/formulacalc_property_channellist_ireferencechannellist.htm) | [Parent](../properties/formulacalc_property_parent_ireferencechannellist.htm)

#### Returned From

[Input](../objects/formulacalc_objects_iinput.htm).[Reference](../properties/formulacalc_property_reference_iinput.htm) | [Output](../objects/formulacalc_objects_ioutput.htm).[Reference](../properties/formulacalc_property_reference_ioutput.htm)

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_channel_ireferencechannelproperty.htm language=enus -->
## TOPIC 01225: Property: Channel for ReferenceChannelProperty

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_channel_ireferencechannelproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_channel_ireferencechannelproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Channel for ReferenceChannelProperty

Property: Channel for ReferenceChannelProperty

Specifies the name of the [Channel](../../genshell/genshell/genshell_data_channels.htm) that contains the channel property with which DIAdem replaces an input or an output when a calculation is executed.

You can add the contents of a DIAdem variable or a calculator expression to the channel name if you enclose the variable or the calculator expression in @@ characters.

If the input of the calculation is dependent on an output from another calculation, you cannot change the Channel property.

```text
Object.Channel
```

| Object | ReferenceChannelPropertyObject with this property |
| --- | --- |
| Object.Channel | String with read and write access |

The following example changes the channel property with which DIAdem replaces the R input when DIAdem executes the first calculation from the first calculation group, if the input is defined with a channel property reference.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs("R")
If oMyInput.ReferenceType = eReferenceTypeChannelProperty Then
  oMyInput.Reference.Channel = "Revs"
  oMyInput.Reference.PropertyName = "Maximum"
  oMyInput.Reference.UnitPropertyName = "unit_string"
End If
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs("R") 
if oMyInput.ReferenceType == dd.eReferenceTypeChannelProperty : 
    oMyInput.Reference.Channel = "Revs" 
    oMyInput.Reference.PropertyName = "Maximum" 
    oMyInput.Reference.UnitPropertyName = "unit_string" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_channellist_ireferencechannellist.htm language=enus -->
## TOPIC 01226: Property: ChannelList for ReferenceChannelList

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_channellist_ireferencechannellist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_channellist_ireferencechannellist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: ChannelList for ReferenceChannelList

Property: ChannelList for ReferenceChannelList

Specifies the channel list with which DIAdem replaces an input or an output when a calculation is executed.

[Group index]

[Channel index]

here

You can add the contents of a DIAdem variable or a calculator expression to the channel group property if you enclose the variable or the calculator expression in @@ characters.

If the input of the calculation is dependent on an output from another calculation, you cannot change the ChannelList property.

```text
Object.ChannelList
```

| Object | ReferenceChannelListObject with this property |
| --- | --- |
| Object.ChannelList | Variant with read and write accessContains a Channel list object or a string with the channels if you use wildcards. |

The following example defines the input R which is a Channel list data type for the first calculation in the first calculation group. Then the example defines with which channels DIAdem replaces the input when the calculation is executed. DIAdem displays the used channel names in a message:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput, oInputChannel
CalculationSet.CalculationGroups.Item(1).Calculations.Item(1).Inputs.RemoveAll
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeChannelList)
oMyInput.ReferenceType = eReferenceTypeChannelList
oMyInput.Reference.ChannelList = "'Res_1'-'Res_5'"
For Each oInputChannel in oMyInput.Reference.ChannelList
  Call MsgBox(oInputChannel.Name)
Next
```

[Copy script](javascript:void(0);)

```text
CalculationSet.CalculationGroups.Item(1).Calculations.Item(1).Inputs.RemoveAll() 
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeChannelList) 
oMyInput.ReferenceType = dd.eReferenceTypeChannelList 
oMyInput.Reference.ChannelList = "'Res_1'-'Res_5'" 
for oInputChannel in oMyInput.Reference.ChannelList: 
    print(oInputChannel.Name) 
```

The following example defines the input R which is a Channel list data type for the first calculation in the first calculation group. Then the example uses wildcards to define with which channels DIAdem replaces the input when the calculation is executed. DIAdem displays the used channel names in a message:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
CalculationSet.CalculationGroups(1).Calculations(1).Inputs.RemoveAll
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeChannelList)
oMyInput.ReferenceType = eReferenceTypeChannelList
oMyInput.Reference.ChannelList = "Temp*"
Call MsgBox(oMyInput.Reference.ChannelList)
```

[Copy script](javascript:void(0);)

```text
CalculationSet.CalculationGroups(1).Calculations(1).Inputs.RemoveAll() 
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeChannelList) 
oMyInput.ReferenceType = dd.eReferenceTypeChannelList 
oMyInput.Reference.ChannelList = "Temp*" 
print(oMyInput.Reference.ChannelList) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_count_icalculationcollection.htm language=enus -->
## TOPIC 01227: Property: Count for Calculations

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_count_icalculationcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_count_icalculationcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Count for Calculations

Property: Count for Calculations

Returns the number of calculations in a calculation group.

```text
Object.Count
```

| Object | CalculationsObject with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example displays the number of calculations in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp("Number of calculations: " & CalculationSet.CalculationGroups(1).Calculations.Count)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp("Number of calculations: " + dd.CalculationSet.CalculationGroups(1).Calculations.Count) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_count_icalculationgroupcollection.htm language=enus -->
## TOPIC 01228: Property: Count for CalculationGroups

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_count_icalculationgroupcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_count_icalculationgroupcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Count for CalculationGroups

Property: Count for CalculationGroups

Returns the number of calculation groups in the current calculation set.

```text
Object.Count
```

| Object | CalculationGroupsObject with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example displays the number of calculation groups in the current calculation set:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp("Number of calculation groups: " & CalculationSet.CalculationGroups.Count)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp("Number of calculation groups: " + dd.CalculationSet.CalculationGroups.Count) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_count_icalculationlist.htm language=enus -->
## TOPIC 01229: Property: Count for CalculationList

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_count_icalculationlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_count_icalculationlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Count for CalculationList

Property: Count for CalculationList

Returns the number of calculations that are executed during a calculation sequence, or are put before or after a calculation sequence.

If a calculation requires an output from an other calculation as an input, DIAdem first executes the other calculation. DIAdem uses this method to specify the sequence in which calculations are to be executed, and automatically expands the volume of calculations to be executed, if required.

```text
Object.Count
```

| Object | CalculationListObject with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example executes selected calculations and then displays the number of executed calculations:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyRunedCalculations
Call CalculationSet.SelectAll(FALSE)
CalculationSet.CalculationGroups("Custom").Calculations(1).Selected = TRUE
CalculationSet.CalculationGroups("Custom").Calculations(2).Selected = TRUE
Set oMyRunedCalculations = CalculationSet.RunSelected
Call MsgBoxDisp("No of calculations: " & oMyRunedCalculations.Count)
```

[Copy script](javascript:void(0);)

```text
dd.CalculationSet.SelectAll(False) 
CalculationSet.CalculationGroups("Custom").Calculations(1).Selected = True 
CalculationSet.CalculationGroups("Custom").Calculations(2).Selected = True 
oMyRunedCalculations = dd.CalculationSet.RunSelected 
dd.MsgBoxDisp("No of calculations: " + oMyRunedCalculations.Count) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_count_iinputcollection.htm language=enus -->
## TOPIC 01230: Property: Count for Inputs

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_count_iinputcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_count_iinputcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Count for Inputs

Property: Count for Inputs

Returns the number of inputs in a calculation.

```text
Object.Count
```

| Object | InputsObject with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example displays the number of inputs for the first calculation in the Custom calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp("Number of inputs: " & CalculationSet.CalculationGroups("Custom").Calculations(1).Inputs.Count)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp("Number of inputs: " + dd.CalculationSet.CalculationGroups("Custom").Calculations(1).Inputs.Count) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_count_iinputlist.htm language=enus -->
## TOPIC 01231: Property: Count for InputList

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_count_iinputlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_count_iinputlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Count for InputList

Property: Count for InputList

Returns the number of inputs that are dependent on an output of a calculation.

```text
Object.Count
```

| Object | InputListObject with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example displays the number of inputs that are dependent on the first output of the first calculation in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyDepInputs
Set oMyDepInputs = CalculationSet.CalculationGroups(1).Calculations(1).Outputs(1).TargetInputs
Call MsgBoxDisp("No of inputs depending on output: " & oMyDepInputs.Count)
```

[Copy script](javascript:void(0);)

```text
oMyDepInputs = dd.CalculationSet.CalculationGroups(1).Calculations(1).Outputs(1).TargetInputs 
dd.MsgBoxDisp("No of inputs depending on output: " + oMyDepInputs.Count) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_count_ioutputcollection.htm language=enus -->
## TOPIC 01232: Property: Count for Outputs

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_count_ioutputcollection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_count_ioutputcollection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Count for Outputs

Property: Count for Outputs

Returns the number of outputs in a calculation.

```text
Object.Count
```

| Object | OutputsObject with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example displays the number of outputs for the first calculation in the Custom calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp("Number of outputs: " & CalculationSet.CalculationGroups("Custom").Calculations(1).Outputs.Count)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp("Number of outputs: " + dd.CalculationSet.CalculationGroups("Custom").Calculations(1).Outputs.Count) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_description_icalculation.htm language=enus -->
## TOPIC 01233: Property: Description for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_description_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_description_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Description for Calculation

Property: Description for Calculation

Specifies the calculation description.

```text
Object.Description
```

| Object | CalculationObject with this property |
| --- | --- |
| Object.Description | String with read and write access |

The following example displays the descriptions of all calculations in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcTemp
Set oMyCalcTemp = CalculationSet.CalculationGroups(1).Calculations
For I = 1 To oMyCalcTemp.Count
  Call MsgBoxDisp(oMyCalcTemp(i).Description)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups(1).Calculations 
for I in range( 1, oMyCalcTemp.Count + 1): 
    dd.MsgBoxDisp(oMyCalcTemp(i).Description) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_description_icalculationgroup.htm language=enus -->
## TOPIC 01234: Property: Description for CalculationGroup

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_description_icalculationgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_description_icalculationgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Description for CalculationGroup

Property: Description for CalculationGroup

Specifies the description of the calculation group.

```text
Object.Description
```

| Object | CalculationGroupObject with this property |
| --- | --- |
| Object.Description | String with read and write access |

The following example displays the descriptions of all calculation groups:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcTemp
Set oMyCalcTemp = CalculationSet.CalculationGroups
For I = 1 To oMyCalcTemp.Count
  Call MsgBoxDisp(oMyCalcTemp(i).Description)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups 
for I in range( 1, oMyCalcTemp.Count + 1): 
    dd.MsgBoxDisp(oMyCalcTemp(i).Description) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_description_icalculationset.htm language=enus -->
## TOPIC 01235: Property: Description for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_description_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_description_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Description for CalculationSet

Property: Description for CalculationSet

Specifies the description of the calculation group.

```text
Object.Description
```

| Object | CalculationSetObject with this property |
| --- | --- |
| Object.Description | String with read and write access |

The following example assigns a description to the current calculation set and saves the calculation set as MyCalculationSet.tca:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
CalculationSet.Description = "My calculation set"
Call CalculationSet.SaveAs("MyCalculationSet.tca")
```

[Copy script](javascript:void(0);)

```text
CalculationSet.Description = "My calculation " 
dd.CalculationSet.SaveAs("MyCalculationSet.tca") 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_filename_icalculationset.htm language=enus -->
## TOPIC 01236: Property: FileName for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_filename_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_filename_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: FileName for CalculationSet

Property: FileName for CalculationSet

Returns the path and the filename of the current calculation set file.

```text
Object.FileName
```

| Object | CalculationSetObject with this property |
| --- | --- |
| Object.FileName | String with read access |

The following example displays the name of the current calculation set file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp("Name of calculation set file: " & CalculationSet.FileName)
```

[Copy script](javascript:void(0);)

```text
Call dd.MsgBoxDisp("Name of calculation file: " + dd.CalculationSet.FileName) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_inputs_icalculation.htm language=enus -->
## TOPIC 01237: Property: Inputs for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_inputs_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_inputs_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Inputs for Calculation

Property: Inputs for Calculation

Provides the collection of all inputs of a calculation.

```text
Set oInputs = Object.Inputs
```

| Object | CalculationObject with this property |
| --- | --- |
| oInputs | InputsReturned object |

The following example displays the names of all inputs of the first calculation in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcInputs
Set oMyCalcInputs = CalculationSet.CalculationGroups(1).Calculations(1).Inputs
For i = 1 to oMyCalcInputs.Count
  Call MsgBoxDisp("Name of input: " & oMyCalcInputs(i).Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcInputs = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs 
for i in range( 1, oMyCalcInputs.Count + 1): 
    dd.MsgBoxDisp("Name of input: " + oMyCalcInputs(i).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_name_icalculation.htm language=enus -->
## TOPIC 01238: Property: Name for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_name_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_name_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Name for Calculation

Property: Name for Calculation

Specifies the calculation name. The name must conform to the [naming conventions](../objects/formulacalc_names.htm) for calculations. If the name does not conform to the name conventions, DIAdem corrects the name.

```text
Object.Name
```

| Object | CalculationObject with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example displays the names of all calculations in the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcTemp
Set oMyCalcTemp = CalculationSet.CalculationGroups(1).Calculations
For I = 1 To oMyCalcTemp.Count
  Call MsgBoxDisp(oMyCalcTemp(i).Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups(1).Calculations 
for I in range( 1, oMyCalcTemp.Count + 1): 
    dd.MsgBoxDisp(oMyCalcTemp(i).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_name_icalculationgroup.htm language=enus -->
## TOPIC 01239: Property: Name for CalculationGroup

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_name_icalculationgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_name_icalculationgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Name for CalculationGroup

Property: Name for CalculationGroup

Specifies the name of the calculation group. The name must conform to the [naming conventions](../objects/formulacalc_names.htm) for calculations. If the name does not conform to the name conventions, DIAdem corrects the name.

```text
Object.Name
```

| Object | CalculationGroupObject with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example displays the names of all calculation groups:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcTemp
Set oMyCalcTemp = CalculationSet.CalculationGroups
For I = 1 To oMyCalcTemp.Count
  Call MsgBoxDisp(oMyCalcTemp(i).Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcTemp = dd.CalculationSet.CalculationGroups 
for I in range( 1, oMyCalcTemp.Count + 1): 
    dd.MsgBoxDisp(oMyCalcTemp(i).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_name_icalculationset.htm language=enus -->
## TOPIC 01240: Property: Name for CalculationSet

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_name_icalculationset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_name_icalculationset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Name for CalculationSet

Property: Name for CalculationSet

Specifies the name of the calculation set.

```text
Object.Name
```

| Object | CalculationSetObject with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example displays the name of the current calculation set file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp("Name of calculation set: " & CalculationSet.Name)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp("Name of calculation : " + dd.CalculationSet.Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_name_iformulaadaptor.htm language=enus -->
## TOPIC 01241: Property: Name for InputOrOutput

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_name_iformulaadaptor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_name_iformulaadaptor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Name for InputOrOutput

Property: Name for InputOrOutput

Specifies the name of the input or output of a calculation.

```text
Object.Name
```

| Object | InputOrOutputObject with this property |
| --- | --- |
| Object.Name | String with read and write access |

The pages of the objects [Input](../objects/formulacalc_objects_iinput.htm) and [Output](../objects/formulacalc_objects_ioutput.htm) contain examples.

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_name_iinput.htm language=enus -->
## TOPIC 01242: Property: Name for Input

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_name_iinput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_name_iinput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Name for Input

Property: Name for Input

Specifies the name of the input of a calculation. The name must conform to the [naming conventions](../objects/formulacalc_names.htm) for calculations. If the name does not conform to the name conventions, DIAdem corrects the name.

```text
Object.Name
```

| Object | InputObject with this property |
| --- | --- |
| Object.Name | String with read and write accessYou cannot change the name of a dependent channel. |

The following example displays the names of all inputs in the first calculation in the Custom calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyInputs
Set oMyInputs = CalculationSet.CalculationGroups("Custom").Calculations(1).Inputs
For I = 1 To oMyInputs.Count
  Call MsgBoxDisp("Name: " & oMyInputs(i).Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyInputs = dd.CalculationSet.CalculationGroups("Custom").Calculations(1).Inputs 
for I in range( 1, oMyInputs.Count + 1): 
    dd.MsgBoxDisp("Name: " + oMyInputs(i).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_name_ioutput.htm language=enus -->
## TOPIC 01243: Property: Name for Output

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_name_ioutput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_name_ioutput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Name for Output

Property: Name for Output

Specifies the name of the output of a calculation. The name must conform to the [naming conventions](../objects/formulacalc_names.htm) for calculations. If the name does not conform to the name conventions, DIAdem corrects the name.

```text
Object.Name
```

| Object | OutputObject with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example displays the names of all outputs in the first calculation in the Custom calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyOutputs
Set oMyOutputs = CalculationSet.CalculationGroups("Custom").Calculations(1).Outputs
For I = 1 To oMyOutputs.Count
  Call MsgBoxDisp("Name: " & oMyOutputs(i).Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyOutputs = dd.CalculationSet.CalculationGroups("Custom").Calculations(1).Outputs 
for I in range( 1, oMyOutputs.Count + 1): 
    dd.MsgBoxDisp("Name: " + oMyOutputs(i).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_optional_iformulaadaptor.htm language=enus -->
## TOPIC 01244: Property: Optional for InputOrOutput

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_optional_iformulaadaptor.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_optional_iformulaadaptor.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Optional for InputOrOutput

Property: Optional for InputOrOutput

Specifies whether the input or the output is an optional input or output.

```text
Object.Optional
```

| Object | InputOrOutputObject with this property |
| --- | --- |
| Object.Optional | Boolean with read and write access |

The pages of the objects [Input](../objects/formulacalc_objects_iinput.htm) and [Output](../objects/formulacalc_objects_ioutput.htm) contain examples.

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_optional_iinput.htm language=enus -->
## TOPIC 01245: Property: Optional for Input

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_optional_iinput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_optional_iinput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Optional for Input

Property: Optional for Input

Specifies whether the input is an optional input.

If DIAdem cannot resolve the reference of an optional input, DIAdem assigns the Empty variable contents to this input. This prevents an error occurring when DIAdem checks whether a calculation can be executed.

```text
Object.Optional
```

| Object | InputObject with this property |
| --- | --- |
| Object.Optional | Boolean with read and write access |

The following example defines the optional input R which is a Value data type for the first calculation in the first calculation group. Then the example defines with which value DIAdem replaces the input when the calculation is executed:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeValue)
oMyInput.Optional = TRUE
oMyInput.ReferenceType = eReferenceTypeValue
oMyInput.Reference.ValueExpression = "R1"
oMyInput.Reference.UnitSymbol = "mm"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeValue) 
oMyInput.Optional = True 
oMyInput.ReferenceType = dd.eReferenceTypeValue 
oMyInput.Reference.ValueExpression = "R1" 
oMyInput.Reference.UnitSymbol = "mm" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_optional_ioutput.htm language=enus -->
## TOPIC 01246: Property: Optional for Output

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_optional_ioutput.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_optional_ioutput.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Optional for Output

Property: Optional for Output

Specifies whether the output is an optional output.

The channel that an optional output references only displays in the Data Portal if channel values are assigned to the channel during the calculation.

If the optional channel references a non-existent channel in the Data Portal, DIAdem only generates this channel if you assign channel values to this channel during the calculation. If you only change the properties of the channel during the calculation, DIAdem does not generate this channel.

```text
Object.Optional
```

| Object | OutputObject with this property |
| --- | --- |
| Object.Optional | Boolean with read and write access |

The following example defines the optional output R which is a Channel data type for the first calculation in the first calculation group. The example then defines which channel DIAdem replaces the output with when the calculation is executed.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyOutput
Set oMyOutput = CalculationSet.CalculationGroups(1).Calculations(1).Outputs.Add("R",eAdaptorTypeChannel)
oMyOutput.Optional = TRUE
oMyOutput.ReferenceType = eReferenceTypeChannel
oMyOutput.Reference.Channel = "Revs"
```

[Copy script](javascript:void(0);)

```text
oMyOutput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Outputs.Add("R",dd.eAdaptorTypeChannel) 
oMyOutput.Optional = True 
oMyOutput.ReferenceType = dd.eReferenceTypeChannel 
oMyOutput.Reference.Channel = "Revs" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_outputs_icalculation.htm language=enus -->
## TOPIC 01247: Property: Outputs for Calculation

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_outputs_icalculation.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_outputs_icalculation.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Outputs for Calculation

Property: Outputs for Calculation

Provides the collection of all outputs of a calculation.

```text
Set oOutputs = Object.Outputs
```

| Object | CalculationObject with this property |
| --- | --- |
| oOutputs | OutputsReturned object |

The following example displays the names of all outputs of the first calculation from the first calculation group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim i, oMyCalcOutputs
Set oMyCalcOutputs = CalculationSet.CalculationGroups(1).Calculations(1).Outputs
For i = 1 to oMyCalcOutputs.Count
  Call MsgBoxDisp("Name of output: " & oMyCalcOutputs(i).Name)
Next
```

[Copy script](javascript:void(0);)

```text
oMyCalcOutputs = dd.CalculationSet.CalculationGroups(1).Calculations(1).Outputs 
for i in range( 1, oMyCalcOutputs.Count + 1): 
    dd.MsgBoxDisp("Name of output: " + oMyCalcOutputs(i).Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_overview.htm language=enus -->
## TOPIC 01248: Properties

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > Properties

Properties

Properties determine the appearance and the behavior of objects or generate new objects. These new objects can have properties and methods.

The subordinate topics contained in the tree on the contents tab of the Help describe all the properties of the script interface for calculations.

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_parent_ireferencevalue.htm language=enus -->
## TOPIC 01249: Property: Parent for ReferenceValue

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_parent_ireferencevalue.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_parent_ireferencevalue.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: Parent for ReferenceValue

Property: Parent for ReferenceValue

Specifies the input or the output of a calculation to which the value reference is assigned.

```text
Set oInputOrOutput = Object.Parent
```

| Object | ReferenceValueObject with this property |
| --- | --- |
| oInputOrOutput | InputOrOutputReturned object |

The following example displays the name of the calculation to which the transferred calculation is assigned:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub Display(oMyReference)
  Call MsgBoxDisp(oMyReference.Parent.Calculation.Name)
End Sub
```

[Copy script](javascript:void(0);)

```text
def Display(oMyReference): 
    dd.MsgBoxDisp(oMyReference.Parent.Calculation.Name) 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)

<!--NI_TOPIC bundle=diadem path=icalculationset/properties/formulacalc_property_propertyname_ireferencechannelgroupproperty.htm language=enus -->
## TOPIC 01250: Property: PropertyName for ReferenceChannelGroupProperty

- bundle_id: `diadem`
- source_path: `icalculationset/properties/formulacalc_property_propertyname_ireferencechannelgroupproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/icalculationset/properties/formulacalc_property_propertyname_ireferencechannelgroupproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculations](../icalculationset_overview.htm) > [Properties](../properties/formulacalc_property_overview.htm) > Property: PropertyName for ReferenceChannelGroupProperty

Property: PropertyName for ReferenceChannelGroupProperty

Specifies the name of the channel group property with which DIAdem replaces an input or an output when a calculation is executed.

You can add the contents of a DIAdem variable or a calculator expression to the channel group property if you enclose the variable or the calculator expression in @@ characters.

If the input of the calculation is dependent on an output from another calculation, you cannot change the PropertyName property.

```text
Object.PropertyName
```

| Object | ReferenceChannelGroupPropertyObject with this property |
| --- | --- |
| Object.PropertyName | String with read and write access |

The following example generates the R input, which is a Value data type, in the first calculation of the first calculation group. The example then defines a channel group property reference for this input and specifies the channel group, the property, and the associated unit.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyInput
Set oMyInput = CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",eAdaptorTypeValue)
oMyInput.ReferenceType = eReferenceTypeChannelGroupProperty
oMyInput.Reference.ChannelGroup = "Crash"
oMyInput.Reference.PropertyName = "Duration"
oMyInput.Reference.UnitSymbol = "ms"
```

[Copy script](javascript:void(0);)

```text
oMyInput = dd.CalculationSet.CalculationGroups(1).Calculations(1).Inputs.Add("R",dd.eAdaptorTypeValue) 
oMyInput.ReferenceType = dd.eReferenceTypeChannelGroupProperty 
oMyInput.Reference.ChannelGroup = "Crash" 
oMyInput.Reference.PropertyName = "Duration" 
oMyInput.Reference.UnitSymbol = "ms" 
```

#### See Also

[Objects Overview](../objects/icalculationset_objects_overview.htm)

#### Procedures

[Connecting Channels and Values in Calculations](../../procmaths/procmaths/mathsproc_formular_value.htm) | [Creating a Calculation Script with Debug Option](../../procmaths/procmaths/mathsproc_formular_clipboard.htm) | [Creating and Executing Calculations](../../procmaths/procmaths/mathsproc_formular.htm) | [Executing Calculations Multiple Times](../../procmaths/procmaths/mathsproc_formular_multiple.htm) | [Using Channel Lists in Calculations](../../procmaths/procmaths/mathsproc_formular_chnlist.htm) | [Working with Dependent Inputs](../../procmaths/procmaths/mathsproc_formular_input.htm)

#### Examples

[Calculating the Sound Pressure Level with Calculation Templates](../../exploff/examples/calculationset_example.htm)
