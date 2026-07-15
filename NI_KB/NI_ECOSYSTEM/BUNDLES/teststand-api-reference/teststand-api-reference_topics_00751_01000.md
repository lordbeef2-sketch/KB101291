# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=751 end=1000 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-delocalizeexpression.html language=enus -->
## TOPIC 00751: Engine.DelocalizeExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-delocalizeexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-delocalizeexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DelocalizeExpression( localizedExpressionString, decimalPointOption) Return Value String A string containing the delocalized expression. Purpose Converts a localized expression string to a standard form suitable for evaluation. Remarks TestStand requires expressions it evaluates throug

### Engine.DelocalizeExpression

#### Syntax

[Engine](engine.html).DelocalizeExpression( localizedExpressionString, decimalPointOption)

#### Return Value

[String](data-types-for-teststand.html)

A string containing the delocalized expression.

#### Purpose

Converts a localized expression string to a standard form suitable for evaluation.

#### Remarks

TestStand requires expressions it evaluates through the expression function Evaluate or the
 [PropertyObject.EvaluateEx](propertyobject-evaluateex.html)
 method to be in a standard, non-localized form so the result of the evaluation does not depend on the localization settings of the computer.

Call this method to delocalize expressions you obtain from user input. The method replaces the localized decimal point characters that represent decimal points in the expression with the period character. If the localized decimal point character is the comma character, the method also replaces semicolons that represent argument separators or expression separators with commas. The method does not change characters inside string constants.

#### Parameters

localizedExpressionString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the localized expression string to convert.

decimalPointOption
 As
 [DecimalPointLocalizationOptions](decimalpointlocalizationoptions.html)

[In] Pass a constant that specifies how the method determines which character the localized expression uses for the localized decimal point.

#### See Also

[DecimalPointLocalizationOptions](decimalpointlocalizationoptions.html)

[Engine.GetLocalizedDecimalPoint](engine-getlocalizeddecimalpoint.html)

[Engine.LocalizeExpression](engine-localizeexpression.html)

[PropertyObject.EvaluateEx](propertyobject-evaluateex.html)

[StationOptions.UseLocalizedDecimalPoint](stationoptions-uselocalizeddecimalpoint.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-disableresults.html language=enus -->
## TOPIC 00752: Engine.DisableResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-disableresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-disableresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisableResults Data Type Boolean Purpose This property is obsolete. Use the StationOptions.DisableResults property instead. Remarks Disables recording of results for all steps. When this property is True , TestStand does not record results for steps. When this property is False , TestS

### Engine.DisableResults

#### Syntax

[Engine](engine.html).DisableResults

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.DisableResults

#### Remarks

Disables recording of results for all steps.

When this property is
 True
 , TestStand does not record results for steps. When this property is
 False
 , TestStand records results based on the setting of the
 [Step.RecordResult](step-recordresult.html)
 property of each individual step or based on the
 [Sequence.DisableResults](sequence-disableresults.html)
 property and
 [Execution.DisableResults](execution-disableresults.html)
 property.

Note

#### See Also

[Execution.DisableResults](execution-disableresults.html)

[Sequence.DisableResults](sequence-disableresults.html)

[StationOptions.DisableResults](stationoptions-disableresults.html)

[Step.RecordResult](step-recordresult.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayadapterconfigdialog.html language=enus -->
## TOPIC 00753: Engine.DisplayAdapterConfigDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayadapterconfigdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayadapterconfigdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayAdapterConfigDialog( dlgTitle, adapterSelectorReadOnly, adapterCfgReadOnly, hideAdapterSelector, modalToAppMainWind) Return Value Boolean Returns True if the dialog box modifies adapter settings. Purpose Launches the Adapter Configuration dialog box, in which you can edit adapte

### Engine.DisplayAdapterConfigDialog

#### Syntax

[Engine](engine.html).DisplayAdapterConfigDialog( dlgTitle, adapterSelectorReadOnly, adapterCfgReadOnly, hideAdapterSelector, modalToAppMainWind)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the dialog box modifies adapter settings.

#### Purpose

Launches the
 [Adapter Configuration](../tsref/adapter-configuration-dialog-box.html)
 dialog box, in which you can edit adapter-specific settings and select the default adapter.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

adapterSelectorReadOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want a read-only version of the Selected column in the dialog box.

adapterCfgReadOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want read-only versions of the Adapter Configuration controls in the dialog box.

hideAdapterSelector
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to hide the Selected and Hidden columns in the dialog box. This is useful for user interfaces that do not require the ability to select a default adapter.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

#### See Also

[ActiveXAdapter](activexadapter.html)

[Adapter](adapter.html)

[Adapter Configuration dialog box](../tsref/adapter-configuration-dialog-box.html)

[CommonCAdapter](commoncadapter.html)

[CVIAdapter](cviadapter.html)

[DllAdapter](dlladapter.html)

[DotNetAdapter](dotnetadapter.html)

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.ConfigFile](engine-configfile.html)

[Engine.DefaultAdapter](engine-defaultadapter.html)

[Engine.DefaultAdapterIndex](engine-defaultadapterindex.html)

[HTBasicAdapter](htbasicadapter.html)

[LabVIEWAdapter](labviewadapter.html)

[SequenceAdapter](sequenceadapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaybreakpointdialog.html language=enus -->
## TOPIC 00754: Engine.DisplayBreakpointDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaybreakpointdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaybreakpointdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayBreakpointDialog( dlgTitle, sequenceContextParam, executionParam, selectedStep, stepGroupParam, dlgOptions = 0) Return Value Boolean Returns True if you click OK . Otherwise, returns False . Purpose Launches the Breakpoint Settings dialog box, in which you edit the breakpoint se

### Engine.DisplayBreakpointDialog

#### Syntax

[Engine](engine.html).DisplayBreakpointDialog( dlgTitle, sequenceContextParam, executionParam, selectedStep, stepGroupParam, dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 . Otherwise, returns
 False
 .

#### Purpose

Launches the
 [Breakpoint Settings](../tsref/breakpoint-settings-dialog-box.html)
 dialog box, in which you edit the breakpoint settings of a step or the End marker after the last step in a step group.

#### Remarks

Breakpoint settings for a particular execution apply only to that execution. Editing a breakpoint for a step in a sequence file overrides and breakpoint setting on the corresponding step in a running execution.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

sequenceContextParam
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context the dialog box uses to evaluate expressions specified for a conditional breakpoint. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context for the step or sequence file you are editing.

executionParam
 As
 [Execution](execution.html)

[In] If you want to set the breakpoint state for a particular execution only, specify a reference to an Execution object. Breakpoints set for a particular execution only apply to that execution and are lost when the Execution object is destroyed, or when you set the breakpoint state for the step by calling this method without passing an execution.

selectedStep
 As
 [Step](step.html)

[In] Specifies a reference to a Step object to specify which breakpoint to configure. Pass
 NULL
 to configure a breakpoint on the End marker after the last step in a step group. If you pass
 NULL
 , you must specify a value for the
 whichSteps
 parameter.

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] When the
 selectedStep
 parameter is
 NULL
 ,
 whichSteps
 specifies a particular step group that specifies the End marker.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [CommonDialogOptions](commondialogoptions.html)
 constants.

This parameter has a default value of
 0
 .

#### See Also

[Breakpoint Settings dialog box](../tsref/breakpoint-settings-dialog-box.html)

[CommonDialogOptions](commondialogoptions.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[Execution](execution.html)

[SequenceContext](sequencecontext.html)

[Step](step.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaybrowseexprdialog.html language=enus -->
## TOPIC 00755: Engine.DisplayBrowseExprDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaybrowseexprdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaybrowseexprdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayBrowseExprDialog( dlgTitle, sequenceContextParam, expressionIn, selectionStartIn, selectionEndIn, initialVariableName, usesCRLF, modalToAppMainWind, expressionOut, selectionStartOut, selectionEndOut) Return Value Boolean Returns True if you click OK in the dialog box. Returns Fa

### Engine.DisplayBrowseExprDialog

#### Syntax

[Engine](engine.html).DisplayBrowseExprDialog( dlgTitle, sequenceContextParam, expressionIn, selectionStartIn, selectionEndIn, initialVariableName, usesCRLF, modalToAppMainWind, expressionOut, selectionStartOut, selectionEndOut)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Note

Engine.DisplayBrowseExprDialogEx

#### Remarks

Launches a dialog box in which you can construct an expression string using variables, properties, constants, operators, and functions.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

sequenceContextParam
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context into which to browse. You can use the
 [SequenceFile.NewEditContext](sequencefile-neweditcontext.html)
 method to obtain an edit time sequence context from a sequence file.

expressionIn
 As
 [String](data-types-for-teststand.html)

[In] Specifies the initial expression string for the dialog box. This string must be a
 [localized expression](engine-localizeexpression.html)
 .

selectionStartIn
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the location in the initial expression where the selected text begins. If you want a cursor instead of selected text, pass the same index for selectionEndIn.

selectionEndIn
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index of the location in the initial expression of the first character beyond the selected text. If you want a cursor instead of selected text, pass the same index for selectionStartIn.

initialVariableName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the initial variable or property to show as selected in the dialog box.

usesCRLF
 As
 [Boolean](data-types-for-teststand.html)

[In] If the initial expression string uses a carriage return/linefeed combination ("\r\n") to indicate the end of a line of text, pass
 True
 for this parameter. If the string uses only a linefeed ("\n"), pass
 False
 . This parameter also determines if the carriage return/linefeed is inserted in the output expression for new lines.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

expressionOut
 As
 [String](data-types-for-teststand.html)

[Out] Returns the resulting expression from the dialog box when the user clicks OK. This expression string is a localized expression. Refer to
 [Engine.DelocalizeExpression](engine-delocalizeexpression.html)
 for more information about converting a localized expression string to a standard form suitable for evaluation.

selectionStartOut
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the index of the start of the selected text in the resulting expression when the user clicks OK.

selectionEndOut
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the index of the first character beyond the selected text in the resulting expression when the user clicks OK.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DelocalizeExpression](engine-delocalizeexpression.html)

[Engine.DisplayBrowseExprDialogEx](engine-displaybrowseexprdialogex.html)

[Engine.LocalizeExpression](engine-localizeexpression.html)

[SequenceContext](sequencecontext.html)

[SequenceFile.NewEditContext](sequencefile-neweditcontext.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaybrowseexprdialogex.html language=enus -->
## TOPIC 00756: Engine.DisplayBrowseExprDialogEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaybrowseexprdialogex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaybrowseexprdialogex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayBrowseExprDialogEx( dlgTitle, objectToBrowse, expressionIn, selectionStartIn, selectionEndIn, initialVariableName, dlgOptions, expressionOut, selectionStartOut, selectionEndOut) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cance

### Engine.DisplayBrowseExprDialogEx

#### Syntax

[Engine](engine.html).DisplayBrowseExprDialogEx( dlgTitle, objectToBrowse, expressionIn, selectionStartIn, selectionEndIn, initialVariableName, dlgOptions, expressionOut, selectionStartOut, selectionEndOut)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches a dialog box in which you can construct an expression string using variables, properties, constants, operators, and functions.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

objectToBrowse
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the object into which to browse. This is usually a
 [SequenceContext](sequencecontext.html)
 object. You can use the
 [SequenceFile.NewEditContext](sequencefile-neweditcontext.html)
 or
 [Engine.NewEditContext](engine-neweditcontext.html)
 methods to create a sequence context.

expressionIn
 As
 [String](data-types-for-teststand.html)

[In] Specifies the initial expression string for the dialog box. You can pass an empty string for this parameter. This string must be a
 [localized expression](engine-localizeexpression.html)
 .

selectionStartIn
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the location in the initial expression where the selected text begins. If you want a cursor instead of selected text, pass the same index for
 selectionEndIn
 .

selectionEndIn
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index of the location in the initial expression of the first character beyond the selected text. If you want a cursor instead of selected text, pass the same index for
 selectionStartIn
 . Pass -1 to select to the end of the text.

initialVariableName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the initial variable or property to show as selected in the dialog box. You can pass an empty string for the parameter to select the first item.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [BrowseExprDialogOptions](browseexprdialogoptions.html)
 constants.

expressionOut
 As
 [String](data-types-for-teststand.html)

[Out] Returns the resulting expression from the dialog box when the user clicks
 OK
 . This expression string is a localized expression. You can
 [convert a localized expression string to a standard form suitable for evaluation](engine-delocalizeexpression.html)
 .

selectionStartOut
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the index of the start of the selected text in the resulting expression when the user clicks
 OK
 .

selectionEndOut
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the index of the first character beyond the selected text in the resulting expression when the user clicks
 OK
 .

#### See Also

[BrowseExprDialogOptions](browseexprdialogoptions.html)

[Engine.DelocalizeExpression](engine-delocalizeexpression.html)

[Engine.LocalizeExpression](engine-localizeexpression.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[PropertyObject](propertyobject.html)

[SequenceContext](sequencecontext.html)

[SequenceFile.NewEditContext](sequencefile-neweditcontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaybrowsepropertyobjectdialog.html language=enus -->
## TOPIC 00757: Engine.DisplayBrowsePropertyObjectDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaybrowsepropertyobjectdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaybrowsepropertyobjectdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayBrowsePropertyObjectDialog( dlgTitle, objectToBrowse, initialLocation, dlgOptions = 0) Purpose Launches a dialog box in which you can see the structure of a PropertyObject object. Parameters dlgTitle As String [In] Specifies the title of the dialog box. Pass an empty string to u

### Engine.DisplayBrowsePropertyObjectDialog

#### Syntax

[Engine](engine.html).DisplayBrowsePropertyObjectDialog( dlgTitle, objectToBrowse, initialLocation, dlgOptions = 0)

#### Purpose

Launches a dialog box in which you can see the structure of a PropertyObject object.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

objectToBrowse
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the object into which to browse.

initialLocation
 As
 [String](data-types-for-teststand.html)

[In] Specifies a lookup string for the subproperty of the object to select initially.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specify
 [CommonDlgOption_NoOptions](commondialogoptions.html)
 or
 [CommonDlgOption_ModalToAppMainWind](commondialogoptions.html)
 .

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayconfiguretypepalettesdialog.html language=enus -->
## TOPIC 00758: Engine.DisplayConfigureTypePalettesDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayconfiguretypepalettesdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayconfiguretypepalettesdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayConfigureTypePalettesDialog( dlgTitle, dlgOptions = 0) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Even if this method returns False , modifications made to sequence files and type palettes might have been saved becaus

### Engine.DisplayConfigureTypePalettesDialog

#### Syntax

[Engine](engine.html).DisplayConfigureTypePalettesDialog( dlgTitle, dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

Note

False

#### Purpose

Launches a dialog box in which you can edit the order of the type palettes and add or remove type palettes for the engine to load.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specify
 [CommonDlgOption_NoOptions](commondialogoptions.html)
 or
 [CommonDlgOption_ModalToAppMainWind](commondialogoptions.html)
 . By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Pass
 CommonDlgOption_ModalToAppMainWind
 if you want a modal dialog box with respect to the window handle of the AppMainHwnd property. Typically, you do not need to set this option.

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[Engine.AppMainHwnd](engine-appmainhwnd.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayeditbreakandwatchdialog.html language=enus -->
## TOPIC 00759: Engine.DisplayEditBreakAndWatchDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayeditbreakandwatchdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayeditbreakandwatchdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayEditBreakAndWatchDialog( dlgTitle, dlgOptions = 0, [selectedItemParam]) Purpose Launches the Edit Breakpoints/Watch Expressions dialog box, in which you can edit the breakpoints and watch expressions defined for the current workspace. Parameters dlgTitle As String [In] Specifies

### Engine.DisplayEditBreakAndWatchDialog

#### Syntax

[Engine](engine.html).DisplayEditBreakAndWatchDialog( dlgTitle, dlgOptions = 0, [selectedItemParam])

#### Purpose

Launches the
 [Edit Breakpoints/Watch Expressions](../tsref/edit-breakpoints-watch-expressions-dialog-box.html)
 dialog box, in which you can edit the breakpoints and watch expressions defined for the current workspace.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [EditBreakAndWatchOptions](editbreakandwatchoptions.html)
 constants.

This parameter has a default value of
 0
 .

selectedItemParam
 As
 [Variant](data-types-for-teststand.html)

[Out] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If the user clicked the Goto button, this parameter returns information about the last selected item on the
 [Breakpoints tab](../tsref/breakpoints-tab-edit-breakpoints-watch-expres.html)
 of the Edit Breakpoints/Watch Expressions dialog box. Pass a
 [SelectedBreakpointItem](selectedbreakpointitem.html)
 object to access the last selected item.

#### See Also

[Breakpoints tab](../tsref/breakpoints-tab-edit-breakpoints-watch-expres.html)

[DisplayBreakpointDialog](engine-displaybreakpointdialog.html)

[Edit Breakpoints/Watch Expressions dialog box](../tsref/edit-breakpoints-watch-expressions-dialog-box.html)

[EditBreakAndWatchOptions](editbreakandwatchoptions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SelectedBreakpointItem](selectedbreakpointitem.html)

[WatchExpression.DisplayConfigurationDialog](watchexpression-displayconfigurationdialog.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayeditnumericformatdialog.html language=enus -->
## TOPIC 00760: Engine.DisplayEditNumericFormatDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayeditnumericformatdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayeditnumericformatdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayEditNumericFormatDialog( dlgTitle, numericFormat, dlgOptions = 0, sampleNumber = 1.5) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose This method is obsolete. Use the PropertyObject.DisplayEditNumericFormatDialog m

### Engine.DisplayEditNumericFormatDialog

#### Syntax

[Engine](engine.html).DisplayEditNumericFormatDialog( dlgTitle, numericFormat, dlgOptions = 0, sampleNumber = 1.5)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Note

PropertyObject.DisplayEditNumericFormatDialog

#### Remarks

Launches a dialog box in which you can edit a numeric format string used to display numbers.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

numericFormat
 As
 [String](data-types-for-teststand.html)

[In/Out] The numeric format string to edit. Enable
 EditNumFormat_AllowDefaultFormat
 if you want to pass an empty string.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [EditNumericFormatOptions](editnumericformatoptions.html)
 constants.

This parameter has a default value of
 0
 .

sampleNumber
 As
 [Double](data-types-for-teststand.html)

[In] Specifies a number to format initially in the dialog box.

This parameter has a default value of
 1.5
 .

#### See Also

[EditNumericFormatOptions](editnumericformatoptions.html)

[PropertyObject.DisplayEditNumericFormatDialog](propertyobject-displayeditnumericformatdialog.html)

[PropertyObject.GetFormattedValue](propertyobject-getformattedvalue.html)

[PropertyObject.NumericFormat](propertyobject-numericformat.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayeditnumericformatdialogex.html language=enus -->
## TOPIC 00761: Engine.DisplayEditNumericFormatDialogEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayeditnumericformatdialogex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayeditnumericformatdialogex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayEditNumericFormatDialogEx( dlgTitle, numericFormat, validFormat, dlgOptions = 0, sampleNumber = 1.5) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose This method is obsolete. Use the PropertyObject.DisplayEditNumeri

### Engine.DisplayEditNumericFormatDialogEx

#### Syntax

[Engine](engine.html).DisplayEditNumericFormatDialogEx( dlgTitle, numericFormat, validFormat, dlgOptions = 0, sampleNumber = 1.5)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Note

PropertyObject.DisplayEditNumericFormatDialog

#### Remarks

Launches a dialog box in which you can edit a
 [numeric format string](propertyobject-numericformat.html)
 used to display numbers.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

numericFormat
 As
 [String](data-types-for-teststand.html)

[In/Out] The numeric format string to edit. Enable
 EditNumFormat_AllowDefaultFormat
 if you want to pass an empty string.

validFormat
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the returned format is valid, otherwise returns
 False
 .

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [EditNumericFormatOptions](editnumericformatoptions.html)
 constants.

This parameter has a default value of
 0
 .

sampleNumber
 As
 [Double](data-types-for-teststand.html)

[In] Specifies a number to format initially in the dialog box.

This parameter has a default value of
 1.5
 .

#### See Also

[EditNumericFormatOptions](editnumericformatoptions.html)

[PropertyObject.DisplayEditNumericFormatDialog](propertyobject-displayeditnumericformatdialog.html)

[PropertyObject.GetFormattedValue](propertyobject-getformattedvalue.html)

[PropertyObject.NumericFormat](propertyobject-numericformat.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayeditpathsinfilesdialog.html language=enus -->
## TOPIC 00762: Engine.DisplayEditPathsInFilesDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayeditpathsinfilesdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayeditpathsinfilesdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayEditPathsInFilesDialog( dlgTitle, dlgOptions = 0, [initialFile]) Return Value Boolean Returns True if you modify one or more files from the dialog box. Purpose Launches a dialog box in which you can edit the properties stored in TestStand files that contain pathnames. Remarks Th

### Engine.DisplayEditPathsInFilesDialog

#### Syntax

[Engine](engine.html).DisplayEditPathsInFilesDialog( dlgTitle, dlgOptions = 0, [initialFile])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you modify one or more files from the dialog box.

#### Purpose

Launches a dialog box in which you can edit the properties stored in TestStand files that contain pathnames.

#### Remarks

This method first launches a dialog box in which you can select which files to edit. After you select those files, this method launches a dialog box that shows all the path properties within those files. You can use this dialog box to change the paths stored in any TestStand file, including sequence files, workspace files, project files, engine configuration files, the station globals file, and the user file.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [EditPathsDialogOptions](editpathsdialogoptions.html)
 constants.

This parameter has a default value of
 0
 .

initialFile
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an optional
 [PropertyObjectFile](propertyobjectfile.html)
 object the dialog box initially selects in the list control.

#### See Also

[EditPathsDialogOptions](editpathsdialogoptions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayedituserdialog.html language=enus -->
## TOPIC 00763: Engine.DisplayEditUserDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayedituserdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayedituserdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayEditUserDialog( dlgTitle, userObject, modalToAppMainWind) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches a dialog box in which you can edit user information for a specific user. You can edit the name, com

### Engine.DisplayEditUserDialog

#### Syntax

[Engine](engine.html).DisplayEditUserDialog( dlgTitle, userObject, modalToAppMainWind)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches a dialog box in which you can edit user information for a specific user. You can edit the name, comment, and password.

#### Remarks

Calling the
 [PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)
 method on a User object and passing default dialog options is equivalent to calling this method.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

userObject
 As
 [User](user.html)

[In] Specifies the User object you want to edit.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property returns. Typically, you do not need to set this option.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)

[User](user.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayenvironmentconfigurationdialog.html language=enus -->
## TOPIC 00764: Engine.DisplayEnvironmentConfigurationDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayenvironmentconfigurationdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayenvironmentconfigurationdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayEnvironmentConfigurationDialog( dlgOptions = 0, path = "") Return Value Boolean Parameters dlgOptions As Long [In] path As String [In/Out]

### Engine.DisplayEnvironmentConfigurationDialog

#### Syntax

[Engine](engine.html).DisplayEnvironmentConfigurationDialog( dlgOptions = 0, path = "")

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Parameters

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In]

path
 As
 [String](data-types-for-teststand.html)

[In/Out]

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayerrordialog.html language=enus -->
## TOPIC 00765: Engine.DisplayErrorDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayerrordialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayerrordialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayErrorDialog( dlgTitle, errorMessage, errorCode, dlgOptions) Purpose Launches a dialog box to display an error message. Remarks Depending on the error message, the dialog might divide the message into expandable subsections. If the message includes location information, the dialo

### Engine.DisplayErrorDialog

#### Syntax

[Engine](engine.html).DisplayErrorDialog( dlgTitle, errorMessage, errorCode, dlgOptions)

#### Purpose

Launches a dialog box to display an error message.

#### Remarks

Depending on the error message, the dialog might divide the message into expandable subsections. If the message includes location information, the dialog can offer the user the option to navigate to the location.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

errorMessage
 As
 [String](data-types-for-teststand.html)

[In] Specifies the error message text to display in the dialog box.

errorCode
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the error code to display in the dialog box. If the error code is a TestStand error code and the
 errorMessage
 does not already contain the description of the error code, the dialog also displays the error code description.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies
 CommonDlgOption_NoOptions
 or
 CommonDlgOption_DisableGotoLocation
 .

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayexpressioneditoptionsdialog.html language=enus -->
## TOPIC 00766: Engine.DisplayExpressionEditOptionsDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayexpressioneditoptionsdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayexpressioneditoptionsdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayExpressionEditOptionsDialog( dlgTitle = "", dlgOptions = 0) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches the Expression Editing Options dialog box, in which you can edit the options for displaying expre

### Engine.DisplayExpressionEditOptionsDialog

#### Syntax

[Engine](engine.html).DisplayExpressionEditOptionsDialog( dlgTitle = "", dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Expression Editing Options](../tsref/expression-editing-options-dialog-box.html)
 dialog box, in which you can edit the options for displaying expressions.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

This parameter has a default value of
 ""
 .

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specify
 CommonDlgOption_NoOptions
 or
 CommonDlgOption_ModalToAppMainWnd
 . By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Pass
 CommonDlgOption_ModalToAppMainWnd
 if you want the dialog box to be modal with respect to the window handle of the AppMainHwnd property. Typically, you do not need to set this option.

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Expression Editing Options dialog box](../tsref/expression-editing-options-dialog-box.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayexternalviewerdialog.html language=enus -->
## TOPIC 00767: Engine.DisplayExternalViewerDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayexternalviewerdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayexternalviewerdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayExternalViewerDialog( dlgTitle, readOnly, modalToAppMainWind) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. Purpose Launches a dialog box in which you can edit the external

### Engine.DisplayExternalViewerDialog

#### Syntax

[Engine](engine.html).DisplayExternalViewerDialog( dlgTitle, readOnly, modalToAppMainWind)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Launches a dialog box in which you can edit the external file viewer settings.

#### Remarks

The external viewer settings specify the external viewer applications you use to view report files of various formats. Formats include text (
 .txt
 ) and HTML (
 .html
 ) files.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

readOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want a read-only version of the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.ConfigFile](engine-configfile.html)

[Engine.ExternalReportViewers](engine-externalreportviewers.html)

[Engine.LaunchExternalViewer](engine-launchexternalviewer.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayfiledialog.html language=enus -->
## TOPIC 00768: Engine.DisplayFileDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayfiledialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayfiledialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayFileDialog( dlgTitle, okButtonText, initialPath, selectedPaths, absolutePaths, openFileDialogFlags = 0, defaultExtension = "", win32Flags = WinFileDlg_HIDEREADONLY | WinFileDlg_FILEMUSTEXIST, fileFilter = "", [currentFile], [fileFilterIndex], [dirHistoryList]) Return Value Boole

### Engine.DisplayFileDialog

#### Syntax

[Engine](engine.html).DisplayFileDialog( dlgTitle, okButtonText, initialPath, selectedPaths, absolutePaths, openFileDialogFlags = 0, defaultExtension = "", win32Flags = WinFileDlg_HIDEREADONLY | WinFileDlg_FILEMUSTEXIST, fileFilter = "", [currentFile], [fileFilterIndex], [dirHistoryList])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches a dialog box in which the user can select files or directories to open or to save.

#### Remarks

This method launches the TestStand File dialog box. Depending on the options you pass, TestStand selects a single file, multiple files, a single directory, or multiple directories. Additional options specify whether TestStand returns absolute or relative pathnames for the selected files. TestStand can return a relative pathname only when the file is located under one of the TestStand
 [search directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 . If the file is not located under any of the TestStand search directories and the user requests that TestStand return a relative pathname, the dialog box prompts the user to add the name of the directory that contains the file to the list of TestStand search directories. You can pass a SequenceFile object, WorkspaceFile object, or a project file object to include its directory among the list of search directories that are valid for a relative pathname.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

okButtonText
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string to display on the OK button. Pass an empty string to use the default.

initialPath
 As
 [String](data-types-for-teststand.html)

[In] For a file selection dialog box, specify the path of the file you want the dialog box to display initially. If you specify the path of a directory, the filename control in the dialog box remains empty. For a directory selection dialog box, specify the path of the directory you want the user to browse initially. Pass an empty string to specify the current directory. The path must specify an existing file or directory.

selectedPaths
 As
 [String Array](data-types-for-teststand.html)

[Out] Returns the array of pathnames of the files or directories the user selected. The pathnames can be relative or absolute depending on the dialog box settings.

absolutePaths
 As
 [String Array](data-types-for-teststand.html)

[Out] Returns the array of absolute pathnames of the files or directories the user selected.

openFileDialogFlags
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for the default behavior, or pass one or more
 [OpenFileDialogOptions](openfiledialogoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

This parameter has a default value of
 0
 .

defaultExtension
 As
 [String](data-types-for-teststand.html)

[In] Specifies the extension to append to the pathname if the user specifies no extension. Do not include the period in the extension.

This parameter has a default value of
 ""
 .

win32Flags
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the Microsoft
 [Windows file dialog flags](windowsfiledialogflags.html)
 .

This parameter has a default value of
 WinFileDlg_HIDEREADONLY | WinFileDlg_FILEMUSTEXIST
 .

fileFilter
 As
 [String](data-types-for-teststand.html)

[In] Specifies the extensions files must have to appear in the dialog box. Each filter the string contains has two parts. The first part is a descriptive name for the filter and the second part lists the extensions the file can have. Specify multiple extensions using a semi-colon (;) as a delimiter, and end each section with a vertical bar (|). End the string with a final vertical bar (|). The following example illustrates this format:

"Sequence Files (*.seq)|*.seq|Report Files (*.txt;*.htm;*.html)|*.txt;*.htm;*.html||"

This parameter has a default value of
 ""
 .

currentFile
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Pass a
 [PropertyObjectFile](propertyobjectfile.html)
 object for a sequence file, workspace file, or project file if you want to include the directory of the file in the list of search directories that are valid for a relative pathname. The search directory "current sequence file" refers to the object passed as this parameter. If you pass a workspace file or project file, TestStand searches the directory of the file before searching the other search directories for the relative pathname.

fileFilterIndex
 As
 [Variant](data-types-for-teststand.html)

[In/Out] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] When passed as an input parameter, the parameter specifies the file type to be initially selected in the File Type ring control.

The index corresponding to the selected file type within the list control is returned as an output parameter.

dirHistoryList
 As
 [Variant](data-types-for-teststand.html)

[In/Out] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Pass an array of strings if you want to set the contents of the directory history combo box in the dialog box. If you omit this parameter, TestStand sets the contents of the combo box with a default
 [history list](engine-filedialogdirhistorylist.html)
 .

#### See Also

[Engine.SearchDirectories](engine-searchdirectories.html)

[Engine.FileDialogDirHistoryList](engine-filedialogdirhistorylist.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[OpenFileDialogOptions](openfiledialogoptions.html)

[PropertyObjectFile](propertyobjectfile.html)

[WindowsFileDialogFlags](windowsfiledialogflags.html)

[WorkspaceObject.ProjectFile](workspaceobject-projectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayhelpfile.html language=enus -->
## TOPIC 00769: Engine.DisplayHelpFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayhelpfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayhelpfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayHelpFile( htmlFile, helpFile = "", tableOfContentsFile = "", indexFile = "", homeFile = "", windowCaption = "") Return Value Long Returns the window handle of the created help window. Purpose Opens to a topic in a HTML Help file using the topic filename, such as Engine.htm . Rem

### Engine.DisplayHelpFile

#### Syntax

[Engine](engine.html).DisplayHelpFile( htmlFile, helpFile = "", tableOfContentsFile = "", indexFile = "", homeFile = "", windowCaption = "")

#### Return Value

[Long](data-types-for-teststand.html)

Returns the window handle of the created help window.

#### Purpose

Opens to a topic in a HTML Help file using the topic filename, such as
 Engine.htm
 .

#### Remarks

Opens the HTML Help window to a given topic within the compiled help file (
 .chm
 ) using the filename of the help topic. If any of the following parameters are specified—
 tableOfContentsFile
 ,
 indexFile
 , or
 homeFile
 —all three are used to build the HTML Help window. If none of these parameters are specified, the information stored in the help file is used to build the HTML Help window.

To ensure proper navigation within the opened help file, National Instruments recommends that all three parameters—
 tableOfContentsFile
 ,
 indexFile
 , and
 homeFile
 —be specified together.

To specify that a file is within a CHM, use the following syntax:

CHMFileName.chm::\\FileName.
 xxx

#### Parameters

htmlFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the HTML help topic within the help file to which the help window is opened. Include the file extension (
 .htm
 ,
 .html
 ) of the page. Specify the entire path of the page within the help file.

Pass
 ""
 to open the help file to the default topic.

helpFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the HTML help file to open. Include the absolute path of the help file and the extension. If you do not specify a help file, TestStand uses the
 NI TestStand Help
 .

This parameter has a default value of
 ""
 .

tableOfContentsFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the table of contents file to use with the help file. Include the absolute path of the table of contents file along with the extension.

This parameter has a default value of
 ""
 .

indexFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the index file to use with the help file. Include the absolute path of the index file along with the extension.

This parameter has a default value of
 ""
 .

homeFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the default topic to display for the help file. Include the absolute path of the default topic along with the extension.

This parameter has a default value of
 ""
 .

windowCaption
 As
 [String](data-types-for-teststand.html)

[In] Specifies the help window caption to display. This parameter is ignored unless a table of contents file, an index file, or a default topic file is specified. If none of these files are specified, the help window caption is the caption the author of the help file specifies. If you specify a contents file or an index file but do not specify this parameter, the window caption defaults to
 NI TestStand Help
 .

This parameter has a default value of
 ""
 .

#### See Also

[Engine.DisplayHelpTopic](engine-displayhelptopic.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayhelptopic.html language=enus -->
## TOPIC 00770: Engine.DisplayHelpTopic

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayhelptopic.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayhelptopic.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayHelpTopic( tagID, helpFile = "", tableOfContentsFile = "", indexFile = "", homeFile = "", windowCaption = "") Return Value Long Returns the window handle of the created help window. Purpose Opens to a topic in a HTML Help file using a help ID. Remarks Uses the assigned help ID t

### Engine.DisplayHelpTopic

#### Syntax

[Engine](engine.html).DisplayHelpTopic( tagID, helpFile = "", tableOfContentsFile = "", indexFile = "", homeFile = "", windowCaption = "")

#### Return Value

[Long](data-types-for-teststand.html)

Returns the window handle of the created help window.

#### Purpose

Opens to a topic in a HTML Help file using a help ID.

#### Remarks

Uses the assigned help ID to open the compiled help file (
 .chm
 ) to a particular topic. If any of the following parameters are specified—
 tableOfContentsFile
 ,
 indexFile
 , or
 homeFile
 —then all three are used to build the HTML Help window. If none of these parameters are specified, the information stored in the help file is used to build the HTML Help window.

To ensure proper navigation within the opened help file, National Instruments recommends that all three parameters—
 tableOfContentsFile
 ,
 indexFile
 , and
 homeFile
 —be specified together.

To specify that a file is within a CHM, use the following syntax:

CHMFileName.chm::\\FileName.
 xxx

If TestStand
 helpFile
 is passed, then the help content will be opened by NI Help Launcher by calling into
 [Engine.DisplayHelpTopicEx](engine-displayhelptopicex.html)
 API.

#### Parameters

tagID
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the help ID of the help topic within the compiled help file to open. The help file author associates help IDs with topic files.

Pass
 0
 to open the help file to the default topic.

helpFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the HTML help file to open. Include the absolute path of the help file and the extension. If you do not specify a help file, TestStand uses the
 NI TestStand Help
 .

This parameter has a default value of
 ""
 .

tableOfContentsFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the table of contents file to use with the help file. Include the absolute path of the table of contents file along with the extension.

This parameter has a default value of
 ""
 .

indexFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the index file to use with the help file. Include the absolute path of the index file along with the extension.

This parameter has a default value of
 ""
 .

homeFile
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the default topic to display for the help file. Include the absolute path of the default topic along with the extension.

This parameter has a default value of
 ""
 .

windowCaption
 As
 [String](data-types-for-teststand.html)

[In] Specifies the help window caption to display. This parameter is ignored unless a table of contents file, an index file, or a default topic file is specified. If none of these files are specified, the help window caption is the caption the author of the help file specifies. If you specify a contents file or an index file but do not specify this parameter, the window caption defaults to
 NI TestStand Help
 .

This parameter has a default value of
 ""
 .

#### See Also

[Engine.DisplayHelpFile](engine-displayhelpfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayhelptopicex.html language=enus -->
## TOPIC 00771: Engine.DisplayHelpTopicEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayhelptopicex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayhelptopicex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayHelpTopicEx( helpContextID ) Purpose Opens a topic referred by the help context ID using NI Help Launcher. Remarks Uses the assigned helpcontextID of NI products help content to open it using NI Help Launcher. Online or Offline help Content is launched based on the option select

### Engine.DisplayHelpTopicEx

#### Syntax

[Engine](engine.html).DisplayHelpTopicEx( helpContextID )

#### Purpose

Opens a topic referred by the help context ID using NI Help Launcher.

#### Remarks

Uses the assigned
 helpcontextID
 of NI products help content to open it using NI Help Launcher.

Note

#### Parameters

helpContextID
 As
 [String](data-types-for-teststand.html)

[In] Specifies the help context ID or resource ID assigned for the help topics of NI products.

If you are trying to launch TestStand help content, ensure that the prefix for
 **helpContextID**
 is "ts_".

#### See Also

[Engine.DisplayHelpTopic](engine-displayhelptopic.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayioconfigurationoptionsdialog.html language=enus -->
## TOPIC 00772: Engine.DisplayIOConfigurationOptionsDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayioconfigurationoptionsdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayioconfigurationoptionsdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayIOConfigurationOptionsDialog Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel. Purpose Launches a dialog box for configuring IO Configuration options.

### Engine.DisplayIOConfigurationOptionsDialog

#### Syntax

[Engine](engine.html).DisplayIOConfigurationOptionsDialog

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click OK in the dialog box. Returns
 False
 if you click Cancel.

#### Purpose

Launches a dialog box for configuring IO Configuration options.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaylockunlockdialog.html language=enus -->
## TOPIC 00773: Engine.DisplayLockUnlockDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaylockunlockdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaylockunlockdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayLockUnlockDialog( dlgTitle = "", dlgMsg = "", propObject = NULL, options = 0, [passwordString = NULL]) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches a dialog box in which you can lock or unlock a Propert

### Engine.DisplayLockUnlockDialog

#### Syntax

[Engine](engine.html).DisplayLockUnlockDialog( dlgTitle = "", dlgMsg = "", propObject = NULL, options = 0, [passwordString = NULL])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches a dialog box in which you can lock or unlock a PropertyObjectFile, or prompt for a password to perform a lock or unlock operation.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

This parameter has a default value of
 ""
 .

dlgMsg
 As
 [String](data-types-for-teststand.html)

[In] Specifies the message in the dialog box. Pass an empty string to use the default message for the dialog box.

This parameter has a default value of
 ""
 .

propObject
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an object to lock or unlock. The object lock state determines whether the dialog box performs a lock or unlock operation by calling the
 [PropertyObjectFile.Lock](propertyobjectfile-lock.html)
 and
 [PropertyObjectFile.Unlock](propertyobjectfile-unlock.html)
 methods respectively.

When you pass
 NULL
 , the dialog box does not operate on any object. The
 options
 parameter specifies whether the dialog box performs a lock or unlock operation. If you pass
 NULL
 and perform an unlock operation, you must specify the required password using the
 passwordString
 parameter.

This parameter has a default value of
 NULL
 .

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [LockUnlockDialogOptions](lockunlockdialogoptions.html)
 constants.

This parameter has a default value of
 0
 .

passwordString
 As
 [Variant](data-types-for-teststand.html)

[In/Out] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies the password the dialog box expects when you specify
 [LockUnlockDialogOption_Unlock](lockunlockdialogoptions.html)
 in the
 options
 parameter, and returns the entered password from the dialog box when you specify
 [LockUnlockDialogOption_Lock](lockunlockdialogoptions.html)
 in the
 options
 parameter.

This parameter has a default value of
 NULL
 .

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[LockUnlockDialogOptions](lockunlockdialogoptions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[PropertyObject](propertyobject.html)

[PropertyObjectFile.Lock](propertyobjectfile-lock.html)

[PropertyObjectFile.Unlock](propertyobjectfile-unlock.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaylogindialog.html language=enus -->
## TOPIC 00774: Engine.DisplayLoginDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaylogindialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaylogindialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayLoginDialog( dlgTitle, initialLoginName, initialPassword, modalToAppMainWind, userObject) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches a login dialog box. Remarks A drop-down list box in the dialog box

### Engine.DisplayLoginDialog

#### Syntax

[Engine](engine.html).DisplayLoginDialog( dlgTitle, initialLoginName, initialPassword, modalToAppMainWind, userObject)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches a login dialog box.

#### Remarks

A drop-down list box in the dialog box contains the login names of all current TestStand users.

The LoginLogout Front-End callback calls this method.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

initialLoginName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the initial login name you want displayed in the dialog box. If you pass an empty string, the first login name in the ring control is selected.

initialPassword
 As
 [String](data-types-for-teststand.html)

[In] Specifies the initial password you want displayed in the dialog box. It appears on screen as all asterisks (*).

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

userObject
 As
 [User](user.html)

[Out] Returns the User object that represents the user who logged in.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.CurrentUser](engine-currentuser.html)

[Engine.GetUser](engine-getuser.html)

[User](user.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaylooponstepsdialog.html language=enus -->
## TOPIC 00775: Engine.DisplayLoopOnStepsDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaylooponstepsdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaylooponstepsdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayLoopOnStepsDialog( dlgTitle, selectedStep, modalToAppMainWnd, loopCountValue, stopExpressionValue) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches a dialog box that prompts the user to provide interactive

### Engine.DisplayLoopOnStepsDialog

#### Syntax

[Engine](engine.html).DisplayLoopOnStepsDialog( dlgTitle, selectedStep, modalToAppMainWnd, loopCountValue, stopExpressionValue)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches a dialog box that prompts the user to provide interactive execution information required for the Loop On Selected Steps command.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

selectedStep
 As
 [Step](step.html)

[In] Specifies a reference to the first currently selected step. The dialog box uses this step to display property information if the user browses to create the 'stop on' expression.

modalToAppMainWnd
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property returns. Typically, you do not need to set this option.

loopCountValue
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the value of the loop count the user specifies in the dialog box. A value of -1 indicates an infinite loop.

stopExpressionValue
 As
 [String](data-types-for-teststand.html)

[Out] Returns the value of the stop expression the user specifies in the dialog box. An empty string indicates that the stop expression is not used.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Step](step.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaymessagebox.html language=enus -->
## TOPIC 00776: Engine.DisplayMessageBox

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaymessagebox.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaymessagebox.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayMessageBox( dlgTitle, messageText, msgBoxType = MsgBox_Information, dlgOptions = 0, win32Flags = 0) Return Value Long Returns the user response. This is the same as the return value from the Microsoft Windows Software Development Kit MessageBox function. The following are typica

### Engine.DisplayMessageBox

#### Syntax

[Engine](engine.html).DisplayMessageBox( dlgTitle, messageText, msgBoxType = MsgBox_Information, dlgOptions = 0, win32Flags = 0)

#### Return Value

[Long](data-types-for-teststand.html)

Returns the user response. This is the same as the return value from the Microsoft Windows Software Development Kit MessageBox function. The following are typical values: IDOK (1), IDCANCEL (2), IDYES (6), IDNO (7).

#### Purpose

Launches a message dialog box.

#### Remarks

Calling this method on a remote instance of the engine displays the message on the local computer.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

messageText
 As
 [String](data-types-for-teststand.html)

[In] Specifies the text to display in the message box.

msgBoxType
 As
 [MsgBoxTypes](msgboxtypes.html)

[In] Specifies the type of message box. This tells the message box which icon to display.

This parameter has a default value of
 MsgBox_Information
 .

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specify
 [CommonDlgOption_NoOptions](commondialogoptions.html)
 or
 [CommonDlgOption_ModalToAppMainWnd](commondialogoptions.html)
 .

This parameter has a default value of
 0
 .

win32Flags
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any additional flags the Windows SDK MessageBox function allows.

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[MsgBoxTypes](msgboxtypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaynewuserdialog.html language=enus -->
## TOPIC 00777: Engine.DisplayNewUserDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaynewuserdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaynewuserdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayNewUserDialog( dlgTitle, modalToAppMainWind, userObject) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches a dialog box for creating a new user. Parameters dlgTitle As String [In] Specifies the title of the

### Engine.DisplayNewUserDialog

#### Syntax

[Engine](engine.html).DisplayNewUserDialog( dlgTitle, modalToAppMainWind, userObject)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches a dialog box for creating a new user.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

userObject
 As
 [User](user.html)

[Out] Returns the User object that represents the newly created user.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayEditUserDialog](engine-displayedituserdialog.html)

[PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)

[User](user.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayopenfiledialog.html language=enus -->
## TOPIC 00778: Engine.DisplayOpenFileDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayopenfiledialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayopenfiledialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayOpenFileDialog( dlgTitle, okButtonText, initialPath, modalToAppMainWind, selectedPath, absolutePath, openFileDialogFlags = 0, defaultExtension = "", win32Flags = WinFileDlg_HIDEREADONLY | WinFileDlg_FILEMUSTEXIST, fileFilter = "", [currentSequenceFile]) Return Value Boolean Retu

### Engine.DisplayOpenFileDialog

#### Syntax

[Engine](engine.html).DisplayOpenFileDialog( dlgTitle, okButtonText, initialPath, modalToAppMainWind, selectedPath, absolutePath, openFileDialogFlags = 0, defaultExtension = "", win32Flags = WinFileDlg_HIDEREADONLY | WinFileDlg_FILEMUSTEXIST, fileFilter = "", [currentSequenceFile])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Note

Engine.DisplayFileDialog

#### Remarks

Launches a dialog box in which the user can select a file. The user can choose whether the dialog box returns an absolute or relative pathname for the file. The dialog box can only return a relative pathname when the file is located under one of the TestStand
 [search directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 . If the file is not located under any of the TestStand search directories and the user requests that the dialog box return a relative pathname, the dialog box prompts the user to add the name of the directory that contains the file to the list of TestStand search directories. You can pass a sequence file object to include the directory among the list of valid search directories for a relative pathname.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

okButtonText
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string to display on the OK button. Pass an empty string to use the default.

initialPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the path of the directory you want the user to browse initially. Pass an empty string to specify the current directory.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle that the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property returns. Typically, you do not need to set this option.

selectedPath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the pathname the user specifies in the dialog box. The path can be relative.

absolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute pathname of the file the user selects.

openFileDialogFlags
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for the default behavior, or pass one or more
 [OpenFileDialogOptions](openfiledialogoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

This parameter has a default value of
 0
 .

defaultExtension
 As
 [String](data-types-for-teststand.html)

[In] Specifies the extension to append to the pathname if the user specifies no extension. Do not include the period in the extension.

This parameter has a default value of
 ""
 .

win32Flags
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the
 [WindowsFileDialogFlags](windowsfiledialogflags.html)
 .

This parameter has a default value of
 WinFileDlg_HIDEREADONLY | WinFileDlg_FILEMUSTEXIST
 .

fileFilter
 As
 [String](data-types-for-teststand.html)

[In] Specifies the extensions files must have to appear in the dialog box. Each filter the string contains has two parts. The first part is a descriptive name for the filter and the second part lists the extensions the file can have. Specify multiple extensions using a semi-colon (;) as a delimiter, and end each section with a vertical bar (|). End the string with a final vertical bar (|). The following example illustrates this format:

"Sequence Files (*.seq)|*.seq|Report Files (*.txt;*.htm;*.html)|*.txt;*.htm;*.html||"

This parameter has a default value of
 ""
 .

currentSequenceFile
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a SequenceFile object if you want to include the directory of the sequence file in the list of valid search directories for a relative pathname.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayFileDialog](engine-displayfiledialog.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[OpenFileDialogOptions](openfiledialogoptions.html)

[WindowsFileDialogFlags](windowsfiledialogflags.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayoptionsdialog.html language=enus -->
## TOPIC 00779: Engine.DisplayOptionsDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayoptionsdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayoptionsdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayOptionsDialog( dlgTitle, readOnly, modalToAppMainWind) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches the Station Options dialog box. Remarks The Station Options dialog box contains numerous settings that

### Engine.DisplayOptionsDialog

#### Syntax

[Engine](engine.html).DisplayOptionsDialog( dlgTitle, readOnly, modalToAppMainWind)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Station Options](../tsref/station-options-dialog-box.html)
 dialog box.

#### Remarks

The Station Options dialog box contains numerous settings that affect execution, user privileges, and process models. Click
 OK
 in the dialog box to save these options in the engine configuration file
 [Engine.ConfigFile](engine-configfile.html)
 property.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

readOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want a read-only version of the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property returns. Typically, you do not need to set this option.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.ConfigFile](engine-configfile.html)

[Engine.StationOptions](engine-stationoptions.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaypasswordprotecttypedefinitionsd.html language=enus -->
## TOPIC 00780: Engine.DisplayPasswordProtectTypeDefinitionsDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaypasswordprotecttypedefinitionsd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaypasswordprotecttypedefinitionsd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayPasswordProtectTypeDefinitionsDialog( typeDefinitions, modifiedTypeDefinitions, dlgOptions = 0) Return Value Boolean Returns True if the user clicked OK in the dialog box and False if the user clicked Cancel . When this method returns True , use the modifiedTypeDefinitions param

### Engine.DisplayPasswordProtectTypeDefinitionsDialog

#### Syntax

[Engine](engine.html).DisplayPasswordProtectTypeDefinitionsDialog( typeDefinitions, modifiedTypeDefinitions, dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the user clicked
 OK
 in the dialog box and
 False
 if the user clicked
 Cancel
 . When this method returns
 True
 , use the
 modifiedTypeDefinitions
 parameter to determine which types, if any, were modified.

#### Purpose

Displays the
 [Password Protect Type Definitions](../tsref/password-protect-type-definitions-dialog-box.html)
 dialog box, in which you can edit the password protection settings of the types you specify.

#### Remarks

Note

password-protecting type definitions

PropertyObject

#### Parameters

typeDefinitions
 As
 [Object Array](data-types-for-teststand.html)

[In] Specifies an array of type definitions for which you want to edit the password protection information.

modifiedTypeDefinitions
 As
 [Object Array](data-types-for-teststand.html)

[Out] Returns the subset of types you passed to the
 typeDefinitions
 parameter the user modified in the dialog box. The dialog box might modify only a subset of the types because some of the types might already use the settings the user specified.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the
 [CommonDialogOptions](commondialogoptions.html)
 option you want to use. Use the bitwise-OR operator to specify more than one option.

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[Engine.DisplayUnlockTypeDefinitionsDialog](engine-displayunlocktypedefinitionsdialog.html)

[Password Protect Type Definitions dialog box](../tsref/password-protect-type-definitions-dialog-box.html)

[PropertyObject.GetTypeDefinitionProtection](propertyobject-gettypedefinitionprotection.html)

[PropertyObject.LockTypeDefinition](propertyobject-locktypedefinition.html)

[PropertyObject.SetTypeDefinitionProtection](propertyobject-settypedefinitionprotection.html)

[PropertyObject.TypeDefinitionLocked](propertyobject-typedefinitionlocked.html)

[PropertyObject.UnlockTypeDefinition](propertyobject-unlocktypedefinition.html)

[ProtectedObjectOptions](protectedobjectoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaypreconditionbuilderdialog.html language=enus -->
## TOPIC 00781: Engine.DisplayPreconditionBuilderDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaypreconditionbuilderdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaypreconditionbuilderdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayPreconditionBuilderDialog( dlgTitle, preconditionExpr, sequence, dlgOptions = 0, sequenceContext = NULL) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches the Preconditions dialog box, in which you construct

### Engine.DisplayPreconditionBuilderDialog

#### Syntax

[Engine](engine.html).DisplayPreconditionBuilderDialog( dlgTitle, preconditionExpr, sequence, dlgOptions = 0, sequenceContext = NULL)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Preconditions](../tsref/preconditions-dialog-box.html)
 dialog box, in which you construct the precondition expression of a step.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

preconditionExpr
 As
 [String](data-types-for-teststand.html)

[In/Out] Specifies the initial precondition expression string for the dialog box. You can pass an empty string for this parameter. This string must be a
 [localized expression](engine-localizeexpression.html)
 .

sequence
 As
 [Sequence](sequence.html)

[In] Specifies the sequence the dialog box displays for building the precondition expression.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specify
 CommonDlgOption_NoOptions
 or
 CommonDlgOption_ModalToAppMainWind
 . By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. Pass
 CommonDlgOption_ModalToAppMainWind
 if you want the dialog box to be modal with respect to the window handle of the AppMainHwnd property. Typically, you do not need to set this option.

This parameter has a default value of
 0
 .

sequenceContext
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the context to use for browsing expressions.

This parameter has a default value of
 NULL
 .

#### See Also

[Preconditions dialog box](../tsref/preconditions-dialog-box.html)

[Sequence](sequence.html)

[SequenceContext](sequencecontext.html)

[Step.Precondition](step-precondition.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaypreconditiondialog.html language=enus -->
## TOPIC 00782: Engine.DisplayPreconditionDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaypreconditiondialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaypreconditiondialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayPreconditionDialog( dlgTitle, sequence, readOnly, modalToAppMainWind, [initialStep]) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. Purpose Launches a dialog box in which you

### Engine.DisplayPreconditionDialog

#### Syntax

[Engine](engine.html).DisplayPreconditionDialog( dlgTitle, sequence, readOnly, modalToAppMainWind, [initialStep])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Launches a dialog box in which you can edit the preconditions for a step or for all steps in a sequence.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

sequence
 As
 [Sequence](sequence.html)

[In] Specifies the sequence in which to edit preconditions.

readOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want a read-only version of the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

initialStep
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a Step object if you want the dialog box to display only the preconditions for a particular step.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayStepPropDialog](engine-displaysteppropdialog.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Sequence](sequence.html)

[Step](step.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayruntimeerrordialog.html language=enus -->
## TOPIC 00783: Engine.DisplayRunTimeErrorDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayruntimeerrordialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayruntimeerrordialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayRunTimeErrorDialog( dlgTitle, errorMessage, inCleanupStepGroup, modalToAppMainWind, displayOnNextError, suspendExecution, runTimeErrorAction) Purpose This method is obsolete. Use the Engine.DisplayRunTimeErrorDialogEx method instead. Remarks Launches the Run-Time Error dialog bo

### Engine.DisplayRunTimeErrorDialog

#### Syntax

[Engine](engine.html).DisplayRunTimeErrorDialog( dlgTitle, errorMessage, inCleanupStepGroup, modalToAppMainWind, displayOnNextError, suspendExecution, runTimeErrorAction)

#### Purpose

Note

Engine.DisplayRunTimeErrorDialogEx

#### Remarks

Launches the
 [Run-Time Error](../tsref/run-time-error-dialog-box.html)
 dialog box. The sequence editor and user interface typically call this function in response to a
 [UIMsg_BreakOnRunTimeError](uimessage-event.html)
 event. The Run-Time Error dialog box allows the user to specify how the execution is to proceed.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

errorMessage
 As
 [String](data-types-for-teststand.html)

[In] Specifies the error message to display in the dialog box.

inCleanupStepGroup
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if the run-time error occurred in the Cleanup step group of the sequence. This information affects the list of options the dialog box displays to the user.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

displayOnNextError
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the user wants this dialog box to launch again if another run-time error occurs in the current execution.

suspendExecution
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the user wants the current execution to suspend at the location of the run-time error.

runTimeErrorAction
 As
 [RTEOptions](rteoptions.html)

[Out] Returns the option the user selects in the dialog box to specify how the execution should proceed.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayRunTimeErrorDialogEx](engine-displayruntimeerrordialogex.html)

[RTEOptions](rteoptions.html)

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[UIMessage.Event](uimessage-event.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayruntimeerrordialogex.html language=enus -->
## TOPIC 00784: Engine.DisplayRunTimeErrorDialogEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayruntimeerrordialogex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayruntimeerrordialogex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayRunTimeErrorDialogEx( dlgTitle, sequenceContextParam, dlgOptions, suspendExecution, dontShowAgainForExecution, dontShowAgainForBatch, runTimeErrorAction) Purpose Launches the Run-Time Error dialog box to display error information for the specified sequence context. Remarks The s

### Engine.DisplayRunTimeErrorDialogEx

#### Syntax

[Engine](engine.html).DisplayRunTimeErrorDialogEx( dlgTitle, sequenceContextParam, dlgOptions, suspendExecution, dontShowAgainForExecution, dontShowAgainForBatch, runTimeErrorAction)

#### Purpose

Launches the
 [Run-Time Error](../tsref/run-time-error-dialog-box.html)
 dialog box to display error information for the specified sequence context.

#### Remarks

The sequence editor and user interfaces typically call this function in response to a
 [UIMsg_BreakOnRunTimeError](uimessage-event.html)
 event. The dialog box allows the user to specify how the execution is to proceed.

If you use this method within an Engine callback, use the
 [ThisContext.Caller](sequencecontext-caller.html)
 property to pass the sequence context of the sequence that generated the error.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

sequenceContextParam
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context from the thread that caused the run-time error.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specify
 [CommonDlgOption_NoOptions](commondialogoptions.html)
 or
 [CommonDlgOption_ModalToAppMainWnd](commondialogoptions.html)
 .

suspendExecution
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the user wants the current execution to suspend at the location of the run-time error.

dontShowAgainForExecution
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the user wants this dialog box to launch again if another run-time error occurs in the current execution. If this value is
 True
 , set the
 [Execution.RTEOptionForThisExecution](execution-rteoptionforthisexecution.html)
 property to specify what to do on a run-time error for this execution.

dontShowAgainForBatch
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the user wants this dialog box to launch again if another run-time error occurs in any execution that has a thread from the same batch as the thread in the sequence context you specify. If this value is
 True
 , call the
 [Thread.SetBatchRTEOption](thread-setbatchrteoption.html)
 method to set what to do on a run-time error for these executions.

runTimeErrorAction
 As
 [RTEOptions](rteoptions.html)

[Out] Returns the option the user selects in the dialog box to specify how the execution is to proceed.

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[Execution.RTEOptionForThisExecution](execution-rteoptionforthisexecution.html)

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[RTEOptions](rteoptions.html)

[SequenceContext](sequencecontext.html)

[Thread.SetBatchRTEOption](thread-setbatchrteoption.html)

[UIMessage.Event](uimessage-event.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaysearchdirdialog.html language=enus -->
## TOPIC 00785: Engine.DisplaySearchDirDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaysearchdirdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaysearchdirdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplaySearchDirDialog( dlgTitle, readOnly, modalToAppMainWind) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. Purpose Launches a dialog box in which you can edit the list of TestSt

### Engine.DisplaySearchDirDialog

#### Syntax

[Engine](engine.html).DisplaySearchDirDialog( dlgTitle, readOnly, modalToAppMainWind)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Launches a dialog box in which you can edit the list of TestStand
 [search directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

readOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want a read-only version of the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.ConfigFile](engine-configfile.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayseqfilepropdialog.html language=enus -->
## TOPIC 00786: Engine.DisplaySeqFilePropDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayseqfilepropdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayseqfilepropdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplaySeqFilePropDialog( dlgTitle, sequenceFileParam, readOnly, modalToAppMainWind, showViewContentsBtn, viewContents) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. Purpose Launch

### Engine.DisplaySeqFilePropDialog

#### Syntax

[Engine](engine.html).DisplaySeqFilePropDialog( dlgTitle, sequenceFileParam, readOnly, modalToAppMainWind, showViewContentsBtn, viewContents)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Launches a dialog box in which you can edit the properties of a sequence file.

#### Remarks

You can edit the load/unload options, model options, and other options. Calling the
 [PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)
 method on a
 [SequenceFile](sequencefile.html)
 object is equivalent to calling this method. Locking and unlocking a file on the
 [Advanced tab](../tsref/advanced-tab-sequence-file-properties-dialog.html)
 of the
 [Sequence File Properties](../tsref/sequence-file-properties-dialog-box.html)
 dialog box immediately changes the lock state of the file. To determine whether the lock state changes, even when the return value from the method is
 False
 , you can use the
 [PropertyObjectFile.Locked](propertyobjectfile-locked.html)
 property to acquire the lock state before and after calling this method and compare the values.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Pass a SequenceFile object to specify which sequence file you want to edit.

readOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want a read-only version of the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

showViewContentsBtn
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to show a
 View Contents
 button in the dialog box. If you pass
 True
 , the
 viewContents
 parameter of this method returns
 True
 when a user clicks the View Contents button.

viewContents
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if a user clicks the View Contents button in the dialog box.

#### See Also

[Advanced tab](../tsref/advanced-tab-sequence-file-properties-dialog.html)

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)

[PropertyObjectFile.Locked](propertyobjectfile-locked.html)

[Sequence File Properties dialog box](../tsref/sequence-file-properties-dialog-box.html)

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaysequencefilecallbacksdialog.html language=enus -->
## TOPIC 00787: Engine.DisplaySequenceFileCallbacksDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaysequencefilecallbacksdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaysequencefilecallbacksdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplaySequenceFileCallbacksDialog( dlgTitle, sequenceFileParam, dlgOptions, sequenceToEdit, numCallbacksAdded, numCallbacksDeleted) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. P

### Engine.DisplaySequenceFileCallbacksDialog

#### Syntax

[Engine](engine.html).DisplaySequenceFileCallbacksDialog( dlgTitle, sequenceFileParam, dlgOptions, sequenceToEdit, numCallbacksAdded, numCallbacksDeleted)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Launches a dialog box in which you can show, add, and remove Sequence File callbacks.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Pass a SequenceFile object to specify which sequence file you want to edit.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [CommonDialogOptions](commondialogoptions.html)
 constants.

sequenceToEdit
 As
 [String](data-types-for-teststand.html)

[Out] Returns to the dialog box the name of the callback sequence the user chose to edit. An empty string indicates the user did not select a callback to edit.

numCallbacksAdded
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the number of callbacks the dialog box added to the sequence file. Callbacks are added to the end of the list of sequences.

numCallbacksDeleted
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the number of callbacks that the dialog box deleted from the sequence file.

#### See Also

[CallbackTypes](callbacktypes.html)

[CommonDialogOptions](commondialogoptions.html)

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaysequencepropdialog.html language=enus -->
## TOPIC 00788: Engine.DisplaySequencePropDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaysequencepropdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaysequencepropdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplaySequencePropDialog( dlgTitle, sequence, readOnly, modalToAppMainWind, showViewContentsBtn, viewContents) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. Purpose Launches a dia

### Engine.DisplaySequencePropDialog

#### Syntax

[Engine](engine.html).DisplaySequencePropDialog( dlgTitle, sequence, readOnly, modalToAppMainWind, showViewContentsBtn, viewContents)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Launches a dialog box in which you can edit the properties of a sequence.

#### Remarks

Calling this method is equivalent to calling the
 [PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)
 method on a
 [Sequence](sequence.html)
 object. Locking and unlocking a file on the Advanced tab immediately apply to the file. To determine whether the lock state changes, even when the return value from the method is
 False
 , you can use the
 [PropertyObjectFile.Locked](propertyobjectfile-locked.html)
 property to acquire the lock state before and after calling this method and compare the values.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

sequence
 As
 [Sequence](sequence.html)

[In] Specifies the Sequence object that contains the properties you want to edit.

readOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want a read-only version of the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

showViewContentsBtn
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to show a
 View Contents
 button in the dialog box. If you pass
 True
 , the
 viewContents
 parameter of this method returns
 True
 if the user clicks the View Contents button in the dialog box.

viewContents
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the user clicks the View Contents button in the dialog box.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)

[PropertyObjectFile.Locked](propertyobjectfile-locked.html)

[Sequence](sequence.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaysteppropdialog.html language=enus -->
## TOPIC 00789: Engine.DisplayStepPropDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaysteppropdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaysteppropdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayStepPropDialog( dlgTitle, step, readOnly, modalToAppMainWind, showViewContentsBtn, viewContents, modifiedStep) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches a dialog box in which you can edit the propert

### Engine.DisplayStepPropDialog

#### Syntax

[Engine](engine.html).DisplayStepPropDialog( dlgTitle, step, readOnly, modalToAppMainWind, showViewContentsBtn, viewContents, modifiedStep)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches a dialog box in which you can edit the properties of a step.

#### Remarks

Calling the
 [PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)
 method on a
 [Step](step.html)
 object is equivalent to calling this method.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

step
 As
 [Step](step.html)

[In] Specifies the Step object that contains the properties you want to edit.

readOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to launch a read-only version of the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

showViewContentsBtn
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to show a
 View Contents
 button in the dialog box. If you pass
 True
 , the
 viewContents
 parameter of this method returns
 True
 when a user clicks the View Contents button.

viewContents
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the user clicks the View Contents button in the dialog box.

modifiedStep
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the step was modified.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)

[Step](step.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaysteptypemenueditor.html language=enus -->
## TOPIC 00790: Engine.DisplayStepTypeMenuEditor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaysteptypemenueditor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaysteptypemenueditor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayStepTypeMenuEditor( dlgTitle, forSubsteps, dlgOptions = 0) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. Purpose This method is obsolete. Use the Engine.DisplayStepTypeMenuE

### Engine.DisplayStepTypeMenuEditor

#### Syntax

[Engine](engine.html).DisplayStepTypeMenuEditor( dlgTitle, forSubsteps, dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Note

Engine.DisplayStepTypeMenuEditorEx

#### Remarks

Launches a dialog box in which you can edit the order in which step types appear in the Insert Step submenu.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

forSubsteps
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 when editing the menu information for substeps.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specify
 [CommonDlgOption_NoOptions](commondialogoptions.html)
 or
 [CommonDlgOption_ModalToAppMainWnd](commondialogoptions.html)
 .

This parameter has a default value of
 0
 .

#### See Also

[Engine.DisplayStepTypeMenuEditorEx](engine-displaysteptypemenueditorex.html)

[Engine.GetInsertStepMenuStructure](engine-getinsertstepmenustructure.html)

[CommonDialogOptions](commondialogoptions.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaysteptypemenueditorex.html language=enus -->
## TOPIC 00791: Engine.DisplayStepTypeMenuEditorEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaysteptypemenueditorex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaysteptypemenueditorex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayStepTypeMenuEditorEx( dlgTitle, selectedFile, forSubsteps, dlgOptions = 0) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. Purpose Launches a dialog box in which you can edit

### Engine.DisplayStepTypeMenuEditorEx

#### Syntax

[Engine](engine.html).DisplayStepTypeMenuEditorEx( dlgTitle, selectedFile, forSubsteps, dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Launches a dialog box in which you can edit the order in which step types appear in the Insert Step submenu.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

selectedFile
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies the PropertyObjectFile that represents the type palette file to edit.

forSubsteps
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 when editing the menu information for substeps.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specify
 [CommonDlgOption_NoOptions](commondialogoptions.html)
 or
 [CommonDlgOption_ModalToAppMainWnd](commondialogoptions.html)
 .

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displaytoolmenudialog.html language=enus -->
## TOPIC 00792: Engine.DisplayToolMenuDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displaytoolmenudialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displaytoolmenudialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayToolMenuDialog( dlgTitle, readOnly, modalToAppMainWind) Return Value Boolean Returns True if you make modifications and click OK in the dialog box. Returns False if you click Cancel or make no modifications. Purpose Launches a dialog box in which you can edit the Tools menu item

### Engine.DisplayToolMenuDialog

#### Syntax

[Engine](engine.html).DisplayToolMenuDialog( dlgTitle, readOnly, modalToAppMainWind)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you make modifications and click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 or make no modifications.

#### Purpose

Launches a dialog box in which you can edit the Tools menu items.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

readOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want a read-only version of the dialog box.

modalToAppMainWind
 As
 [Boolean](data-types-for-teststand.html)

[In] By default, the dialog box is modal to the last active window of the calling thread, or if there is none, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 [Engine.AppMainHwnd](engine-appmainhwnd.html)
 property. Typically, you do not need to set this option.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayunlocktypedefinitionsdialog.html language=enus -->
## TOPIC 00793: Engine.DisplayUnlockTypeDefinitionsDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayunlocktypedefinitionsdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayunlocktypedefinitionsdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayUnlockTypeDefinitionsDialog( typeDefinitions, allTypesUnlocked, dlgOptions = 0) Return Value Boolean Returns True if any types were unlocked in the Unlock Type Definitions dialog box, even if not all types were successfully unlocked or if the user clicked OK and no types needed

### Engine.DisplayUnlockTypeDefinitionsDialog

#### Syntax

[Engine](engine.html).DisplayUnlockTypeDefinitionsDialog( typeDefinitions, allTypesUnlocked, dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if any types were unlocked in the
 [Unlock Type Definitions](../tsref/unlock-type-definitions-dialog-box.html)
 dialog box, even if not all types were successfully unlocked or if the user clicked
 OK
 and no types needed to be unlocked because all the types were already unlocked or were not password-protected.

#### Purpose

Displays the Unlock Type Definitions dialog box, in which you can unlock the specified types.

#### Remarks

Note

password-protecting type definitions

PropertyObject

#### Parameters

typeDefinitions
 As
 [Object Array](data-types-for-teststand.html)

[In] Specifies an array of type definitions you want to unlock.

allTypesUnlocked
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if all the types you passed to the
 typeDefinitions
 parameter were successfully unlocked, already unlocked, or not password-protected.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [LockUnlockDialogOptions](lockunlockdialogoptions.html)
 constants.

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[Engine.DisplayPasswordProtectTypeDefinitionsDialog](engine-displaypasswordprotecttypedefinitionsd.html)

[Password Protect Type Definitions dialog box](../tsref/password-protect-type-definitions-dialog-box.html)

[PropertyObject.GetTypeDefinitionProtection](propertyobject-gettypedefinitionprotection.html)

[PropertyObject.LockTypeDefinition](propertyobject-locktypedefinition.html)

[PropertyObject.SetTypeDefinitionProtection](propertyobject-settypedefinitionprotection.html)

[PropertyObject.TypeDefinitionLocked](propertyobject-typedefinitionlocked.html)

[PropertyObject.UnlockTypeDefinition](propertyobject-unlocktypedefinition.html)

[ProtectedObjectOptions](protectedobjectoptions.html)

[Unlock Type Definitions dialog box](../tsref/unlock-type-definitions-dialog-box.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-displayworkspacebrowserdialog.html language=enus -->
## TOPIC 00794: Engine.DisplayWorkspaceBrowserDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-displayworkspacebrowserdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-displayworkspacebrowserdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DisplayWorkspaceBrowserDialog( dlgTitle, dlgOptions = 0) Purpose Launches a dialog box in which you select and edit a workspace file. Remarks User interfaces use this method to allow users to select a workspace file, load and unload a workspace file, edit the files in the workspace fil

### Engine.DisplayWorkspaceBrowserDialog

#### Syntax

[Engine](engine.html).DisplayWorkspaceBrowserDialog( dlgTitle, dlgOptions = 0)

#### Purpose

Launches a dialog box in which you select and edit a workspace file.

#### Remarks

User interfaces use this method to allow users to select a workspace file, load and unload a workspace file, edit the files in the workspace file and project files, and perform SCC operations.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [WorkspaceBrowserDialogOptions](workspacebrowserdialogoptions.html)
 constants. Pass
 WorkspaceBrowserDlgOption_Editable
 to enable editing of the workspace. Use the bitwise-OR operator to specify more than one option.

This parameter has a default value of
 0
 .

#### See Also

[CommonDialogOptions](commondialogoptions.html)

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[WorkspaceBrowserDialogOptions](workspacebrowserdialogoptions.html)

[WorkspaceFile](workspacefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-dodotnetgarbagecollection.html language=enus -->
## TOPIC 00795: Engine.DoDotNetGarbageCollection

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-dodotnetgarbagecollection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-dodotnetgarbagecollection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DoDotNetGarbageCollection( reserved = 0) Purpose Forces .NET garbage collection and waits for pending finalizers to ensure that all unreferenced COM objects that have ever been referenced in .NET in the TestStand process are synchronously freed. For example, if you are handling events

### Engine.DoDotNetGarbageCollection

#### Syntax

[Engine](engine.html).DoDotNetGarbageCollection( reserved = 0)

#### Purpose

Forces .NET garbage collection and waits for pending finalizers to ensure that all unreferenced COM objects that have ever been referenced in .NET in the TestStand process are synchronously freed.

For example, if you are handling events from any of the TestStand User Interface (UI) controls in a .NET user interface, .NET references all the parameters to all the events for the TestStand UI Control. The lifetimes of these parameters are extended until garbage collection occurs. When you use .NET to handle any event on an ActiveX control, such as a TestStand UI Control, the .NET Framework handles all events for that control even if you do not handle the events directly in code.

In addition, if sequences pass TestStand interface objects as parameters to .NET code modules, .NET references those parameters, which extends the lifetimes of those parameters until garbage collection occurs.

#### Remarks

You typically do not need to call this method because TestStand automatically calls this method at various critical points, such as when an execution completes or when a sequence file or execution closes.

Note

version of the .NET CLR the TestStand Engine uses directly

System.GC.Collect

System.GC.WaitForPendingFinalizers

#### Parameters

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use. You must always pass
 0
 for this parameter.

This parameter has a default value of
 0
 .

#### See Also

[Engine.DotNetCLRVersion](engine-dotnetclrversion.html)

[Engine.DotNetGarbageCollectionInterval](engine-dotnetgarbagecollectioninterval.html)

[Managing Versions of .NET to Use with TestStand](/csh?context=ts_tsref_net_clr)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-dotnetclrversion.html language=enus -->
## TOPIC 00796: Engine.DotNetCLRVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-dotnetclrversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-dotnetclrversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DotNetCLRVersion Data Type String Purpose Returns the .NET Common Language Runtime version the TestStand Engine and the .NET Adapter use. See Also .NET Adapter Engine.DoDotNetGarbageCollection Engine.DotNetGarbageCollectionInterval

### Engine.DotNetCLRVersion

#### Syntax

[Engine](engine.html).DotNetCLRVersion

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the .NET Common Language Runtime version the TestStand Engine and the
 [.NET Adapter](/csh?context=ts_tsref_net)
 use.

#### See Also

[.NET Adapter](/csh?context=ts_tsref_net)

[Engine.DoDotNetGarbageCollection](engine-dodotnetgarbagecollection.html)

[Engine.DotNetGarbageCollectionInterval](engine-dotnetgarbagecollectioninterval.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-dotnetgarbagecollectioninterval.html language=enus -->
## TOPIC 00797: Engine.DotNetGarbageCollectionInterval

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-dotnetgarbagecollectioninterval.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-dotnetgarbagecollectioninterval.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DotNetGarbageCollectionInterval Data Type Long Purpose Specifies the interval, in milliseconds, at which TestStand forces .NET garbage collection. Set this property to a value less than or equal to 0 to disable automatic garbage collection by the TestStand Engine. By default, in applic

### Engine.DotNetGarbageCollectionInterval

#### Syntax

[Engine](engine.html).DotNetGarbageCollectionInterval

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the interval, in milliseconds, at which TestStand forces .NET garbage collection. Set this property to a value less than or equal to
 0
 to disable automatic garbage collection by the TestStand Engine. By default, in applications that use the TestStand
 
 [ApplicationMgr](../tsuiref/applicationmgr.html)
 control, this value is set to
 3000
 (3-second interval). In applications that do not use the ApplicationMgr control, this property is set to
 -1
 . Forcing garbage collection at regular intervals reduces memory usage and improves performance by ensuring that TestStand objects that have previously been referenced in .NET code are promptly freed or marked for reuse.

#### Remarks

If you use the default interval setting and notice constant CPU usage for the garbage collection the garbage collection timer performs, the following issues are the most likely causes:

- A significant number of managed objects (on the order of tens of millions or more)–If you have too many managed objects, increase the garbage collection interval.
- Leaking managed objects–Managed objects can leak as a result of unexpected unreleased references, such as references incurred when you add an event handler with an instance method. Use .NET leak detection tools to identify unreleased references.

Note

version of the .NET Common Language Runtime (CLR) the TestStand Engine uses directly

GC.Collect

#### See Also

[Engine.DoDotNetGarbageCollection](engine-dodotnetgarbagecollection.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-enableremote.html language=enus -->
## TOPIC 00798: Engine.EnableRemote

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-enableremote.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-enableremote.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.EnableRemote Data Type Boolean Purpose This property is obsolete. Use the StationOptions.AllowSequenceCallsFromRemoteMachine property instead. Remarks Specifies if remote TestStand installations can execute sequences on the local computer. When this property is True , TestStand allows

### Engine.EnableRemote

#### Syntax

[Engine](engine.html).EnableRemote

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.AllowSequenceCallsFromRemoteMachine

#### Remarks

Specifies if remote TestStand installations can execute sequences on the local computer.

When this property is
 True
 , TestStand allows instances of the TestStand Engine on remote computers to connect to the local computer to execute sequences. When this property is
 False
 , only instances of TestStand on the local computer can execute sequences on the local computer.

#### See Also

[Engine.IsRemote](engine-isremote.html)

[StationOptions.AllowSequenceCallsFromRemoteMachine](stationoptions-allowsequencecallsfromremotema.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-enableuserprivilegechecking.html language=enus -->
## TOPIC 00799: Engine.EnableUserPrivilegeChecking

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-enableuserprivilegechecking.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-enableuserprivilegechecking.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.EnableUserPrivilegeChecking Data Type Boolean Purpose This property is obsolete. Use the StationOptions.EnableUserPrivilegeChecking property instead. Remarks Specifies whether the sequence editor or user interface verifies user privileges. When this property is False , the sequence edi

### Engine.EnableUserPrivilegeChecking

#### Syntax

[Engine](engine.html).EnableUserPrivilegeChecking

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.EnableUserPrivilegeChecking

#### Remarks

Specifies whether the sequence editor or user interface verifies user privileges.

When this property is
 False
 , the sequence editor or user interface does not verify that the user has the privileges necessary for performing specific operations. Instead, all operations that depend on user privileges are always available.

#### See Also

[Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)

[StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)

[StationOptions.RequireUserLogin](stationoptions-requireuserlogin.html)

[User.HasPrivilege](user-hasprivilege.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-endprofiling.html language=enus -->
## TOPIC 00800: Engine.EndProfiling

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-endprofiling.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-endprofiling.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.EndProfiling Purpose Balances one call to Engine.BeginProfiling. If all calls to BeginProfiling are balanced, profiling is disabled.

### Engine.EndProfiling

#### Syntax

[Engine](engine.html).EndProfiling

#### Purpose

Balances one call to Engine.BeginProfiling. If all calls to BeginProfiling are balanced, profiling is disabled.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-engineversionstring.html language=enus -->
## TOPIC 00801: Engine.EngineVersionString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-engineversionstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-engineversionstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.EngineVersionString Data Type String Purpose Returns the full version of TestStand Engine as a string.

### Engine.EngineVersionString

#### Syntax

[Engine](engine.html).EngineVersionString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the full version of TestStand Engine as a string.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-evaltoolmenuitemexprs.html language=enus -->
## TOPIC 00802: Engine.EvalToolMenuItemExprs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-evaltoolmenuitemexprs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-evaltoolmenuitemexprs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.EvalToolMenuItemExprs( [editArgsParam]) Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Reevaluates the Enable Expression and Item Text Expression of all the items in the Tools menu. You can extract th

### Engine.EvalToolMenuItemExprs

#### Syntax

[Engine](engine.html).EvalToolMenuItemExprs( [editArgsParam])

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Reevaluates the Enable Expression and Item Text Expression of all the items in the Tools menu.

You can extract the new Enabled Expression and Item Text Expression values for a particular Tools menu item by calling the
 [Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)
 or
 [Engine.GetToolMenuItemInfoWithIDEx](engine-gettoolmenuiteminfowithidex.html)
 methods.

Note

#### Parameters

editArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies the currently selected items in the user interface.

#### See Also

[EditArgs](editargs.html)

[Engine.DisplayToolMenuDialog](engine-displaytoolmenudialog.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)

[Engine.GetToolMenuItemInfoWithIDEx](engine-gettoolmenuiteminfowithidex.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-executionmask.html language=enus -->
## TOPIC 00803: Engine.ExecutionMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-executionmask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-executionmask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ExecutionMask Data Type Long Purpose This property is obsolete. Use the StationOptions.ExecutionMask property instead. Remarks Sets or gets execution options. Specifies the execution options using ExecutionMask constants. To specify multiple execution options, use the bitwise-OR operat

### Engine.ExecutionMask

#### Syntax

[Engine](engine.html).ExecutionMask

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.ExecutionMask

#### Remarks

Sets or gets execution options.

Specifies the execution options using
 [ExecutionMask](executionmask.html)
 constants. To specify multiple execution options, use the bitwise-OR operator.

#### See Also

[ExecutionMask](executionmask.html)

[StationOptions.ExecutionMask](stationoptions-executionmask.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-expandpathmacros.html language=enus -->
## TOPIC 00804: Engine.ExpandPathMacros

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-expandpathmacros.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-expandpathmacros.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ExpandPathMacros( pathString) Return Value Boolean Returns True if at least one macro was found and expanded. Returns False if no macros were expanded. Purpose Expands all supported macros in the path string. Remarks 32-bit TestStand replaces the $(Platform) path macro with win32 , and

### Engine.ExpandPathMacros

#### Syntax

[Engine](engine.html).ExpandPathMacros( pathString)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if at least one macro was found and expanded. Returns
 False
 if no macros were expanded.

#### Purpose

Expands all supported macros in the path string.

#### Remarks

32-bit TestStand replaces the
 $(Platform)
 path macro with
 win32
 , and 64-bit TestStand replaces the macro with
 x64
 . For example, 32-bit TestStand replaces
 C:\bin\$(Platform)\module.dll
 with
 C:\bin\win32\module.dll
 , and 64-bit TestStand replaces the same macro with
 C:\bin\x64\module.dll
 . TestStand does not change paths that do not contain macros.

Using a second
 $
 character escapes the macro to form a literal part of a path. For example, TestStand expands
 C:\bin\$$(Platform)\module.dll
 to
 C:\bin\$(Platform)\module.dll
 . This method returns
 False
 if TestStand escapes but does not expand a macro.

#### Parameters

pathString
 As
 [String](data-types-for-teststand.html)

[In/Out] The path string in which to expand path macros. If TestStand expands the macros, it modifies this string.

#### See Also

[Engine.FindFileEx](engine-findfileex.html)

[Engine.FindPath](engine-findpath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-externalreportviewers.html language=enus -->
## TOPIC 00805: Engine.ExternalReportViewers

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-externalreportviewers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-externalreportviewers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ExternalReportViewers Data Type ExternalReportViewers Purpose Returns a reference to the ExternalReportViewers object, which is a collection that contains a list of the current external report viewers. Remarks You must obtain the external report viewer collection before adding or modif

### Engine.ExternalReportViewers

#### Syntax

[Engine](engine.html).ExternalReportViewers

#### Data Type

[ExternalReportViewers](externalreportviewers.html)

#### Purpose

Returns a reference to the ExternalReportViewers object, which is a collection that contains a list of the current external report viewers.

#### Remarks

You must obtain the external report viewer collection before adding or modifying an external report viewer.

#### See Also

[ExternalReportViewers](externalreportviewers.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-filedialogdirhistorylist.html language=enus -->
## TOPIC 00806: Engine.FileDialogDirHistoryList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-filedialogdirhistorylist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-filedialogdirhistorylist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.FileDialogDirHistoryList Data Type String Array An array of strings that specify the paths to be inserted in the directory history list control in the File dialog box. Purpose Specifies the list of directories to display in the directory history list in the File dialog box. Remarks The

### Engine.FileDialogDirHistoryList

#### Syntax

[Engine](engine.html).FileDialogDirHistoryList

#### Data Type

[String Array](data-types-for-teststand.html)

An array of strings that specify the paths to be inserted in the directory history list control in the File dialog box.

#### Purpose

Specifies the list of directories to display in the directory history list in the File dialog box.

#### Remarks

The dialog box the
 [Engine.DisplayFileDialog](engine-displayfiledialog.html)
 method launches has a directory history control that lists the directories that the user most recently visited. Use this property to customize the contents of that control. When the dialog box opens, it initializes the control with the values specified by this property. When the dialog box closes, it updates this property to contain the current contents of the control.

#### See Also

[Engine.DisplayFileDialog](engine-displayfiledialog.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-findfile.html language=enus -->
## TOPIC 00807: Engine.FindFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-findfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-findfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.FindFile( fileToFind, absolutePath, userCancelled, promptOption = FindFile_PromptHonorUserPreference, srchListOption = FindFile_AddDirToSrchList_Ask, isCommand = False, [currentSequenceFile]) Return Value Boolean Returns True if the file is found. Purpose This method is obsolete. Use t

### Engine.FindFile

#### Syntax

[Engine](engine.html).FindFile( fileToFind, absolutePath, userCancelled, promptOption = FindFile_PromptHonorUserPreference, srchListOption = FindFile_AddDirToSrchList_Ask, isCommand = False, [currentSequenceFile])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the file is found.

#### Purpose

Note

Engine.FindFileEx

#### Parameters

fileToFind
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string that contains the simple filename or relative pathname of the file to search for. TestStand expands macros in the path as specified by the
 [Engine.ExpandPathMacros](engine-expandpathmacros.html)
 method before searching.

absolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute pathname of the file if the file is found.

userCancelled
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the method prompts the user and the user cancels the find operation.

promptOption
 As
 [FindFilePromptOptions](findfilepromptoptions.html)

[In] Specifies whether to prompt the user if the file is not initially found.

This parameter has a default value of
 FindFile_PromptHonorUserPreference
 .

srchListOption
 As
 [FindFileSearchListOptions](findfilesearchlistoptions.html)

[In] Specifies file search options.

This parameter has a default value of
 FindFile_AddDirToSrchList_Ask
 .

isCommand
 As
 [Boolean](data-types-for-teststand.html)

[In] If this flag is
 True
 and fileToFind has no file extension, then the FindFile method searches for files with the same basename that end in the common command extensions:
 .exe
 ,
 .com
 , and
 .bat
 .

This parameter has a default value of
 False
 .

currentSequenceFile
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you pass a SequenceFile object for this parameter, the FindFile method initially searches the directory where the sequence file is stored if the Current Sequence File Directory option is enabled. Enable the current sequence file directory in the sequence editor by selecting
 Configure»Search Directories
 and enabling the
 Current Sequence File Directory
 option.

#### See Also

[Engine.ExpandPathMacros](engine-expandpathmacros.html)

[Engine.FindPath](engine-findpath.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

[FindFilePromptOptions](findfilepromptoptions.html)

[FindFileSearchListOptions](findfilesearchlistoptions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SearchDirectoryTypes](searchdirectorytypes.html)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-findfileex.html language=enus -->
## TOPIC 00808: Engine.FindFileEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-findfileex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-findfileex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.FindFileEx( fileToFind, absolutePath, srchDirType, searchDirectoryIndex, userCancelled, promptOption = FindFile_PromptHonorUserPreference, srchListOption = FindFile_AddDirToSrchList_Ask, isCommand = False, [searchContext], [reserved]) Return Value Boolean Returns True if the file is fo

### Engine.FindFileEx

#### Syntax

[Engine](engine.html).FindFileEx( fileToFind, absolutePath, srchDirType, searchDirectoryIndex, userCancelled, promptOption = FindFile_PromptHonorUserPreference, srchListOption = FindFile_AddDirToSrchList_Ask, isCommand = False, [searchContext], [reserved])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the file is found.

#### Purpose

Searches for a file in the TestStand search directories using a simple filename or relative pathname.

#### Parameters

fileToFind
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string that contains the simple filename or relative pathname of the file to search for. TestStand expands macros in the path as specified by the
 Engine.ExpandPathMacros
 method before searching.

absolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute pathname of the file if the file is found.

srchDirType
 As
 [SearchDirectoryTypes](searchdirectorytypes.html)

[Out] Returns the
 SearchDirectoryType
 in which the specified
 fileToFind
 was found. This can be any of the types located in
 SearchDirectoryTypes
 .

searchDirectoryIndex
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the index of the TestStand search directory used to find the
 fileToFind
 specified. The list of search directories can be obtained by using the TestStand API
 SearchDirectories
 . You can retrieve any search directory from there using this
 searchDirectoryIndex
 .

userCancelled
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the method prompts the user and the user cancels the find operation.

promptOption
 As
 [FindFilePromptOptions](findfilepromptoptions.html)

[In] Specifies whether to prompt the user if the file is not initially found.

This parameter has a default value of
 FindFile_PromptHonorUserPreference
 .

srchListOption
 As
 [FindFileSearchListOptions](findfilesearchlistoptions.html)

[In] Specifies file search options.

This parameter has a default value of
 FindFile_AddDirToSrchList_Ask
 .

isCommand
 As
 [Boolean](data-types-for-teststand.html)

[In] If this flag is
 True
 and
 fileToFind
 has no file extension, then the
 FindFile
 method searches for files with the same basename that end in the common command extensions:
 .exe
 ,
 .com
 , and
 .bat
 .

This parameter has a default value of
 False
 .

searchContext
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Contains the directory of the sequence file, which may also be searched for relative paths. This argument may be empty.

reserved
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Reserved for future use.

#### See Also

[Engine.ExpandPathMacros](engine-expandpathmacros.html)

[SearchDirectoryTypes](searchdirectorytypes.html)

[Engine.FindFile](engine-findfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-findpath.html language=enus -->
## TOPIC 00809: Engine.FindPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-findpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-findpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.FindPath( pathToFind, absolutePath, statusFlag, [currentSequenceFile]) Return Value Boolean Returns True if the file or directory is found. Purpose Searches for a file or directory under the TestStand search directories using a simple file or directory name or relative pathname. Parame

### Engine.FindPath

#### Syntax

[Engine](engine.html).FindPath( pathToFind, absolutePath, statusFlag, [currentSequenceFile])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the file or directory is found.

#### Purpose

Searches for a file or directory under the TestStand
 [search directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 using a simple file or directory name or relative pathname.

#### Parameters

pathToFind
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string that contains the simple file or directory name or relative pathname of the file or directory to search for. TestStand expands macros in the path as specified by the
 [Engine.ExpandPathMacros](engine-expandpathmacros.html)
 method before searching.

absolutePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the absolute pathname of the file or directory if it is found.

statusFlag
 As
 [FindPathStatusValues](findpathstatusvalues.html)

[Out] Returns more information about the file or directory.

currentSequenceFile
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you pass a SequenceFile object for this parameter, the
 Engine.FindPath
 method initially searches the directory where the sequence file is stored if the Current Sequence File Directory option is enabled. Select
 Configure»Search Directories
 to launch the
 [Edit Search Directories](../tsref/edit-search-directories-dialog-box.html)
 dialog box and enable the
 Current Sequence File Directory
 option.

#### See Also

[Edit Search Directories dialog box](../tsref/edit-search-directories-dialog-box.html)

[Engine.ExpandPathMacros](engine-expandpathmacros.html)

[Engine.FindFileEx](engine-findfileex.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

[FindPathStatusValues](findpathstatusvalues.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SearchDirectoryTypes](searchdirectorytypes.html)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getadapter.html language=enus -->
## TOPIC 00810: Engine.GetAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetAdapter( adapterIndex) Return Value Adapter Purpose Returns a module Adapter object from the list of module adapters. Remarks Each adapter defines a module-specific adapter interface. You must obtain the module-specific adapter interface for an Adapter class object to configure the

### Engine.GetAdapter

#### Syntax

[Engine](engine.html).GetAdapter( adapterIndex)

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns a module Adapter object from the list of module adapters.

#### Remarks

Each adapter defines a module-specific adapter interface. You must obtain the module-specific adapter interface for an Adapter class object to configure the adapter.

#### Parameters

adapterIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for the Adapter object to return. You can obtain the number of Adapter objects from the
 [Engine.NumAdapters](engine-numadapters.html)
 property. To obtain a reference to a specific adapter, or to iterate through the adapters in a specific order, use the
 [Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)
 method instead.

#### See Also

[Adapter](adapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

[Engine.NumAdapters](engine-numadapters.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getadapterbykeyname.html language=enus -->
## TOPIC 00811: Engine.GetAdapterByKeyName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getadapterbykeyname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getadapterbykeyname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetAdapterByKeyName( adapterKeyName) Return Value Adapter The adapter that has the specified key name. Purpose Returns an Adapter object from the list of module adapters. Remarks To access the properties and methods of a specific adapter, call GetAdapterByKeyName and then query the ret

### Engine.GetAdapterByKeyName

#### Syntax

[Engine](engine.html).GetAdapterByKeyName( adapterKeyName)

#### Return Value

[Adapter](adapter.html)

The adapter that has the specified key name.

#### Purpose

Returns an Adapter object from the list of module adapters.

#### Remarks

To access the properties and methods of a specific adapter, call GetAdapterByKeyName and then query the returned Adapter object for the interface of the desired adapter.

#### Parameters

adapterKeyName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name to use as a key to find the adapter in the list. Pass one of the
 [AdapterKeyNames](adapterkeynames.html)
 constants.

#### See Also

[Adapter](adapter.html)

[AdapterKeyNames](adapterkeynames.html)

[Engine.GetAdapter](engine-getadapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getedittimetoolmenuitems.html language=enus -->
## TOPIC 00812: Engine.GetEditTimeToolMenuItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getedittimetoolmenuitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getedittimetoolmenuitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetEditTimeToolMenuItems( reserved = 0) Return Value EditTimeMenuItems Purpose Returns a reference to a EditTimeMenuItems object. Remarks TestStand maintains a collection of tools menu items. Use this collection to customize the tools menu items the sequence editor and user interface d

### Engine.GetEditTimeToolMenuItems

#### Syntax

[Engine](engine.html).GetEditTimeToolMenuItems( reserved = 0)

#### Return Value

[EditTimeMenuItems](edittimemenuitems.html)

#### Purpose

Returns a reference to a EditTimeMenuItems object.

#### Remarks

TestStand maintains a collection of tools menu items. Use this collection to customize the tools menu items the sequence editor and user interface display. Each menu item in the collection specifies the menu item type and expressions which determine menu item text, hidden state, and enabled state. A menu item can specify a collection of submenu items.

You can use the
 [Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)
 method to obtain a reference to a run-time instance of the Tools menu. TestStand evaluates edit-time menu item expressions to determine the value of run-time properties. The run-time properties specify the menu item text and whether a menu item is enabled. TestStand excludes any menu items with hidden expressions that evaluate to
 False
 from the run-time copy of the Tools menu. The run-time copy of the Tools menu also contains expanded submenus for menu items using the
 ToolMenuType_SequenceFile
 type, where each submenu item is a menu item using the
 ToolMenuType_Sequence
 type.

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

[EditTimeMenuItem](edittimemenuitem.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getengineconfigfile.html language=enus -->
## TOPIC 00813: Engine.GetEngineConfigFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getengineconfigfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getengineconfigfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetEngineConfigFile( configFileType) Return Value PropertyObjectFile Purpose Returns the PropertyObjectFile that contains settings, such as station options or search directories. Remarks Engine.GetEngineConfigFile provides direct access to TestStand Engine configuration files. Use this

### Engine.GetEngineConfigFile

#### Syntax

[Engine](engine.html).GetEngineConfigFile( configFileType)

#### Return Value

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the PropertyObjectFile that contains settings, such as station options or search directories.

#### Remarks

Engine.GetEngineConfigFile provides direct access to TestStand Engine configuration files. Use this API with caution, particularly when changing settings. It is possible to put the configuration into an invalid state using this API. In most cases, there is a more appropriate, higher-level API that should be preferred. For example, prefer Engine.StationOptions when working with station options, or Engine.SearchDirectories when working with search directories.

#### Parameters

configFileType
 As
 [PropertyObjectFileTypes](propertyobjectfiletypes.html)

[In] Specifies the engine configuration file to return. Supported options are FileType_GeneralEngineConfigFile, FileType_SearchDirectoriesConfigFile, FileType_AdaptersConfigFile, FileType_TypePalettesConfigFile, FileType_CustomConfigFile, FileType_UsersFile, and FileType_StationGlobalsFile. Passing any other value results in a run time error.

#### See Also

[PropertyObjectFileContentTypes](propertyobjectfilecontenttypes.html)

[Engine.StationOptions](engine-stationoptions.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getenvironmentpath.html language=enus -->
## TOPIC 00814: Engine.GetEnvironmentPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getenvironmentpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getenvironmentpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetEnvironmentPath Return Value String The path of the environment configuration (.tsenv) file that defines the environment in which the engine is running. If the engine is running in the global environment, an empty string is returned. Purpose Get the path of the environment configura

### Engine.GetEnvironmentPath

#### Syntax

[Engine](engine.html).GetEnvironmentPath

#### Return Value

[String](data-types-for-teststand.html)

The path of the environment configuration (.tsenv) file that defines the environment in which the engine is running. If the engine is running in the global environment, an empty string is returned.

#### Purpose

Get the path of the environment configuration (.tsenv) file that defines the environment in which the engine is running. If the engine is running in the global environment, an empty string is returned.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-geterrorstring.html language=enus -->
## TOPIC 00815: Engine.GetErrorString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-geterrorstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-geterrorstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetErrorString( errorCode, errorString) Return Value Boolean Returns False when the errorCode is not a TSError. Purpose Returns an error description string that corresponds to a specific TSError code. Parameters errorCode As TSError [In] Specifies the error code to describe. errorStrin

### Engine.GetErrorString

#### Syntax

[Engine](engine.html).GetErrorString( errorCode, errorString)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 False
 when the errorCode is not a TSError.

#### Purpose

Returns an error description string that corresponds to a specific
 [TSError](tserror.html)
 code.

#### Parameters

errorCode
 As
 [TSError](tserror.html)

[In] Specifies the error code to describe.

errorString
 As
 [String](data-types-for-teststand.html)

[Out] Returns a description of the errorCode. If the error code is not a TSError, the parameter returns the string
 "User defined error code."

#### See Also

[StepProperties](stepproperties.html)

[TSError](tserror.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getexecution.html language=enus -->
## TOPIC 00816: Engine.GetExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetExecution( executionId) Return Value Execution Purpose Gets the execution object with the given ID. If no execution is found with given ID, this method returns NULL. Parameters executionId As Long [In] Specifies the execution ID of the given object. See Also Execution.ChildExecution

### Engine.GetExecution

#### Syntax

[Engine](engine.html).GetExecution( executionId)

#### Return Value

[Execution](execution.html)

#### Purpose

Gets the execution object with the given ID. If no execution is found with given ID, this method returns NULL.

#### Parameters

executionId
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the execution ID of the given object.

#### See Also

[Execution.ChildExecutionIds](execution-childexecutionids.html)

[Execution.ParentExecutionId](execution-parentexecutionid.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getfileinformation.html language=enus -->
## TOPIC 00817: Engine.GetFileInformation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getfileinformation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getfileinformation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetFileInformation( path) Return Value FileInformation Returns a new FileInformation object. Purpose Creates and returns a reference to a new FileInformation object you use to retrieve information about a specified file, such as file version, file format version and whether it is a Seq

### Engine.GetFileInformation

#### Syntax

[Engine](engine.html).GetFileInformation( path)

#### Return Value

[FileInformation](fileinformation.html)

Returns a new FileInformation object.

#### Purpose

Creates and returns a reference to a new
 [FileInformation](fileinformation.html)
 object you use to retrieve information about a specified file, such as file version, file format version and whether it is a Sequence File or a custom format file.

#### Remarks

TestStand does not access the file you specify when it calls this method. TestStand accesses the file when you call the properties and methods on the FileInformation object. Thus, TestStand returns a new FileInformation object when the file does not exist at the specified path. Calling methods or properties on a FileInformation object might throw an exception if the file cannot be located. To verify that the file exists on disk and is accessible at the given path, use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute pathname of the file.

#### See Also

[FileInformation](fileinformation.html)

[FileInformation.FileExists](fileinformation-fileexists.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getimageindex.html language=enus -->
## TOPIC 00818: Engine.GetImageIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getimageindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getimageindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetImageIndex( imageName) Return Value Long The index of the image in both of the engine image lists. Returns -1 if the image name is not found. Purpose Returns the index of the image with the specified name, which you can use to access the list of images returned from the Engine.Large

### Engine.GetImageIndex

#### Syntax

[Engine](engine.html).GetImageIndex( imageName)

#### Return Value

[Long](data-types-for-teststand.html)

The index of the image in both of the engine image lists. Returns
 -1
 if the image name is not found.

#### Purpose

Returns the index of the image with the specified name, which you can use to access the list of images returned from the
 [Engine.LargeImageListEx](engine-largeimagelistex.html)
 and
 [Engine.SmallImageListEx](engine-smallimagelistex.html)
 properties.

#### Parameters

imageName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the image. Typically, the name includes a filename and the extension.

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.GetImageName](engine-getimagename.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Engine.NumImages](engine-numimages.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getimagename.html language=enus -->
## TOPIC 00819: Engine.GetImageName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getimagename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getimagename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetImageName( imageIndex) Return Value String The name of the image at the index. Purpose Returns the name of the image at the specified index. Typically, the name includes a filename and the extension. Parameters imageIndex As Long [In] Specifies the image index. The image index must

### Engine.GetImageName

#### Syntax

[Engine](engine.html).GetImageName( imageIndex)

#### Return Value

[String](data-types-for-teststand.html)

The name of the image at the index.

#### Purpose

Returns the name of the image at the specified index. Typically, the name includes a filename and the extension.

#### Parameters

imageIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the image index. The image index must be less than the number of images in the image lists.

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.GetImageIndex](engine-getimageindex.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Engine.NumImages](engine-numimages.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getinsertstepmenustructure.html language=enus -->
## TOPIC 00820: Engine.GetInsertStepMenuStructure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getinsertstepmenustructure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getinsertstepmenustructure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetInsertStepMenuStructure( selectedFile, hiddenFlags) Return Value PropertyObject The object that specifies the menu structure. Purpose Creates a PropertyObject object that specifies the structure of the menu used to insert steps in the sequence editor. Remarks The sequence editor use

### Engine.GetInsertStepMenuStructure

#### Syntax

[Engine](engine.html).GetInsertStepMenuStructure( selectedFile, hiddenFlags)

#### Return Value

[PropertyObject](propertyobject.html)

The object that specifies the menu structure.

#### Purpose

Creates a PropertyObject object that specifies the structure of the menu used to insert steps in the sequence editor.

#### Remarks

The sequence editor uses this method to create the submenu that appears when you select
 Insert Step
 from the Steps pane context menu. The structure of this menu depends upon the types in the type palettes, the types in the sequence file, the default adapter, and the step type menu configuration. This method constructs a PropertyObject
 [object that contains properties that specify the submenu structure](menuitemproperties.html)
 .

#### Parameters

selectedFile
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies the currently selected file. The method includes the step types defined in this file as well as the step types located in the type palette. Pass
 0
 or
 NULL
 if there is no selected file.

hiddenFlags
 As
 [Long](data-types-for-teststand.html)

[In] Pass a set of
 [PropertyFlags](propertyflags.html)
 that specify which step types are not included in the menu. For example, pass
 PropFlags_Hidden
 to exclude the hidden step types.

#### See Also

[Engine.DisplayStepTypeMenuEditorEx](engine-displaysteptypemenueditorex.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetInsertVariableMenuStructure](engine-getinsertvariablemenustructure.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[MenuItemProperties](menuitemproperties.html)

[PropertyFlags](propertyflags.html)

[PropertyObject](propertyobject.html)

[PropertyObjectFile](propertyobjectfile.html)

[Step.GetEditSubstepMenuStructure](step-geteditsubstepmenustructure.html)

[StepType.GetSubstep](steptype-getsubstep.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getinsertvariablemenustructure.html language=enus -->
## TOPIC 00821: Engine.GetInsertVariableMenuStructure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getinsertvariablemenustructure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getinsertvariablemenustructure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetInsertVariableMenuStructure( selectedFile, hiddenFlags) Return Value PropertyObject The object that specifies the menu structure. Purpose Creates a PropertyObject object that specifies the structure of the menu used to insert named data type variables in the sequence editor. Remarks

### Engine.GetInsertVariableMenuStructure

#### Syntax

[Engine](engine.html).GetInsertVariableMenuStructure( selectedFile, hiddenFlags)

#### Return Value

[PropertyObject](propertyobject.html)

The object that specifies the menu structure.

#### Purpose

Creates a PropertyObject object that specifies the structure of the menu used to insert named data type variables in the sequence editor.

#### Remarks

The sequence editor uses this method to create the Types submenu that appears when you select Insert Local, Insert Global, or Insert Parameter from the context menu. Refer to
 [MenuItemProperties](menuitemproperties.html)
 for a description of this property object.

#### Parameters

selectedFile
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies the currently selected file. The method includes the step types defined in this file as well as the step types located in the type palette. Pass
 0
 or
 NULL
 if there is no selected file.

hiddenFlags
 As
 [Long](data-types-for-teststand.html)

[In] Pass a set of
 [PropertyFlags](propertyflags.html)
 that specify which step types are not included in the menu. For example, pass
 PropFlags_Hidden
 to exclude the hidden step types.

#### See Also

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetInsertStepMenuStructure](engine-getinsertstepmenustructure.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[MenuItemProperties](menuitemproperties.html)

[PropertyFlags](propertyflags.html)

[PropertyObject](propertyobject.html)

[PropertyObjectFile](propertyobjectfile.html)

[Step.GetEditSubstepMenuStructure](step-geteditsubstepmenustructure.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getinternaloption.html language=enus -->
## TOPIC 00822: Engine.GetInternalOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getinternaloption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getinternaloption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetInternalOption( option) Return Value Variant The value of the internal option the option parameter specifies. Purpose Returns the value for the internal option the option parameter specifies. Parameters option As InternalOptions [In] Specifies the internal option the method returns.

### Engine.GetInternalOption

#### Syntax

[Engine](engine.html).GetInternalOption( option)

#### Return Value

[Variant](data-types-for-teststand.html)

The value of the internal option the
 option
 parameter specifies.

#### Purpose

Returns the value for the internal option the
 option
 parameter specifies.

#### Parameters

option
 As
 [InternalOptions](internaloptions.html)

[In] Specifies the internal option the method returns.

#### See Also

[Engine.SetInternalOption](engine-setinternaloption.html)

[InternalOptions](internaloptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getlicensedescription.html language=enus -->
## TOPIC 00823: Engine.GetLicenseDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getlicensedescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getlicensedescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetLicenseDescription( reserved = 0) Return Value String Purpose Returns the current license description. Parameters reserved As Long [In] Pass 0 for this parameter. This parameter has a default value of 0 . See Also Activating Your Software with the NI License Manager Engine.GetProduc

### Engine.GetLicenseDescription

#### Syntax

[Engine](engine.html).GetLicenseDescription( reserved = 0)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the current
 
 [license](/csh?context=ts_9050)
 description.

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

[Activating Your Software with the NI License Manager](../tshelp/activating-your-software.html)

[Engine.GetProductRegistrationInfo](engine-getproductregistrationinfo.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getlocalizeddecimalpoint.html language=enus -->
## TOPIC 00824: Engine.GetLocalizedDecimalPoint

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getlocalizeddecimalpoint.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getlocalizeddecimalpoint.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetLocalizedDecimalPoint( decimalPointOption) Return Value String A string that contains the localized decimal point character. Purpose Returns the localized decimal point character. Parameters decimalPointOption As DecimalPointLocalizationOptions [In] A constant that specifies how the

### Engine.GetLocalizedDecimalPoint

#### Syntax

[Engine](engine.html).GetLocalizedDecimalPoint( decimalPointOption)

#### Return Value

[String](data-types-for-teststand.html)

A string that contains the localized decimal point character.

#### Purpose

Returns the localized decimal point character.

#### Parameters

decimalPointOption
 As
 [DecimalPointLocalizationOptions](decimalpointlocalizationoptions.html)

[In] A constant that specifies how the method determines which character is the localized decimal point character.

#### See Also

[DecimalPointLocalizationOptions](decimalpointlocalizationoptions.html)

[Engine.DelocalizeExpression](engine-delocalizeexpression.html)

[Engine.LocalizeExpression](engine-localizeexpression.html)

[StationOptions.UseLocalizedDecimalPoint](stationoptions-uselocalizeddecimalpoint.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getlocationfornextdialog.html language=enus -->
## TOPIC 00825: Engine.GetLocationForNextDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getlocationfornextdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getlocationfornextdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetLocationForNextDialog( locationLookupString, elementAtLocation, selectionStart, selectionLength, clearLoc = True) Purpose This method is typically used by a dialog box to obtain the information needed to select and highlight the control associated with the location the Engine.SetLoc

### Engine.GetLocationForNextDialog

#### Syntax

[Engine](engine.html).GetLocationForNextDialog( locationLookupString, elementAtLocation, selectionStart, selectionLength, clearLoc = True)

#### Purpose

This method is typically used by a dialog box to obtain the information needed to select and highlight the control associated with the location the
 [Engine.SetLocationForNextDialog](engine-setlocationfornextdialog.html)
 method previously specified.

#### Parameters

locationLookupString
 As
 [String](data-types-for-teststand.html)

[Out] Returns a lookup string that indicates the subproperty of the object that contains the corresponding control you want to highlight in the dialog box.

elementAtLocation
 As
 [Long](data-types-for-teststand.html)

[Out] Returns one of the following
 [SearchElements](searchelements.html)
 constants to indicate which part of the property to highlight in the dialog box: SearchElement_Name, SearchElement_Comment, SearchElement_StringValue, SearchElement_NumericValue, or SearchElement_BooleanValue.

selectionStart
 As
 [Long](data-types-for-teststand.html)

[Out] If the control the
 locationLookupString
 and
 elementAtLocation
 parameters indicate is an Edit control, use this parameter to determine a particular section of the text within the control for the dialog box to select. Returns the index of the character within the string for the start of the selection.

selectionLength
 As
 [Long](data-types-for-teststand.html)

[Out] If the control the
 locationLookupString
 and
 elementAtLocation
 parameters indicate is an Edit control, use this parameter to determine a particular section of the text within the control for the dialog box to select. Returns the number of characters, starting from the selStartIndex character, for the dialog box to select in the Edit control.

clearLoc
 As
 [Boolean](data-types-for-teststand.html)

[In] Typically, calling this method clears the internal data in the engine for the location of the dialog box so the next time this method is called, no location information is returned. To override this behavior, pass
 False
 for this parameter.

This parameter has a default value of
 True
 .

#### See Also

[Engine.SetLocationForNextDialog](engine-setlocationfornextdialog.html)

[SearchElements](searchelements.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getmoduleprofiling.html language=enus -->
## TOPIC 00826: Engine.GetModuleProfiling

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getmoduleprofiling.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getmoduleprofiling.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetModuleProfiling( adapterKeyName) Return Value Boolean Returns whether the profiler collects timing information for code modules that the specified adapter loads and executes. Purpose Indicates whether the profiler collects timing information for code modules the specified adapter lo

### Engine.GetModuleProfiling

#### Syntax

[Engine](engine.html).GetModuleProfiling( adapterKeyName)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns whether the profiler collects timing information for code modules that the specified adapter loads and executes.

#### Purpose

Indicates whether the profiler collects timing information for code modules the specified adapter loads and executes.

#### Parameters

adapterKeyName
 As
 [String](data-types-for-teststand.html)

[Out] Specifies the adapter.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getnumtoolmenuitems.html language=enus -->
## TOPIC 00827: Engine.GetNumToolMenuItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getnumtoolmenuitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getnumtoolmenuitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetNumToolMenuItems( menuIndex) Return Value Long The number of Tools menu items. Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Returns the number of menu items a specific Tools menu contains. Call t

### Engine.GetNumToolMenuItems

#### Syntax

[Engine](engine.html).GetNumToolMenuItems( menuIndex)

#### Return Value

[Long](data-types-for-teststand.html)

The number of Tools menu items.

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Returns the number of menu items a specific Tools menu contains.

Call the
 [Engine.ConstructToolMenus](engine-constructtoolmenus.html)
 method before calling this function.

#### Parameters

menuIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the Tools menu from which to obtain the number of Tools menu items.

#### See Also

[Engine.ConstructToolMenus](engine-constructtoolmenus.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getnumtoolmenus.html language=enus -->
## TOPIC 00828: Engine.GetNumToolMenus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getnumtoolmenus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getnumtoolmenus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetNumToolMenus Return Value Long The number of Tools menus. Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Returns the number of Tools menus. Call the Engine.ConstructToolMenus method before calling

### Engine.GetNumToolMenus

#### Syntax

[Engine](engine.html).GetNumToolMenus

#### Return Value

[Long](data-types-for-teststand.html)

The number of Tools menus.

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Returns the number of Tools menus.

Call the
 [Engine.ConstructToolMenus](engine-constructtoolmenus.html)
 method before calling this function. The first Tools menu is the top-level menu. The rest of the menus are submenus.

#### See Also

[Engine.ConstructToolMenus](engine-constructtoolmenus.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getoutputmessages.html language=enus -->
## TOPIC 00829: Engine.GetOutputMessages

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getoutputmessages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getoutputmessages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetOutputMessages Return Value OutputMessages Purpose This method is obsolete. Use the OutputMessages.CopyMessagesToCollection method instead. Returns a reference to the OutputMessages object TestStand maintains. This object is a collection that contains a list of the most recent outpu

### Engine.GetOutputMessages

#### Syntax

[Engine](engine.html).GetOutputMessages

#### Return Value

[OutputMessages](outputmessages.html)

#### Purpose

Note

OutputMessages.CopyMessagesToCollection

Returns a reference to the
 [OutputMessages](outputmessages.html)
 object TestStand maintains. This object is a collection that contains a list of the most recent output messages the
 [OutputMessage.Post](outputmessage-post.html)
 method or OutputMessage
 [expression function](../tsfundamentals/expression-functions.html)
 posts.

#### Remarks

In TestStand 4.0 and 4.0.1, an application could access this collection in response to the
 UIMsg_OutputMessages
 event to obtain new output messages. The application was expected to clear the collection in the handler for this event. If the application did not handle the event or did not clear the collection, the collection could grow without bounds. In TestStand 4.1 or later this method is deprecated, and this collection clears automatically if the application fails to clear it in response to the
 UIMsg_OutputMessages
 event. In addition, TestStand adds a warning output message to the collection to notify users about automatically discarded output messages and that the application incorrectly accessed GetOutputMessages without clearing the collection. Although existing applications can handle the
 UIMsg_OutputMessages
 event by calling GetOutputMessages and clearing the collection, ensure that new application code obtains the OutputMessages collection that contains the most recent output messages from the ActiveXData member of the user interface message for the
 UIMsg_OutputMessages
 event.

#### See Also

[Engine.OutputMessagesEnabled](engine-outputmessagesenabled.html)

[Expression Functions](../tsfundamentals/expression-functions.html)

[OutputMessage.Post](outputmessage-post.html)

[OutputMessages](outputmessages.html)

[OutputMessages.CopyMessagesToCollection](outputmessages-copymessagestocollection.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getproductregistrationinfo.html language=enus -->
## TOPIC 00830: Engine.GetProductRegistrationInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getproductregistrationinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getproductregistrationinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetProductRegistrationInfo( userName, companyName, serialNumber) Return Value Boolean Returns True if this is a registered installation of TestStand. Purpose Returns the product registration information for this installation of TestStand. Remarks This method returns the information you

### Engine.GetProductRegistrationInfo

#### Syntax

[Engine](engine.html).GetProductRegistrationInfo( userName, companyName, serialNumber)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if this is a registered installation of TestStand.

#### Purpose

Returns the product registration information for this installation of TestStand.

#### Remarks

This method returns the information you entered at install time or from the National Instruments License Manager when activating the license for TestStand.

#### Parameters

userName
 As
 [String](data-types-for-teststand.html)

[Out] Returns the name of the user currently logged into the National Instruments License Manager.

companyName
 As
 [String](data-types-for-teststand.html)

[Out] Returns the company name of the user currently logged into the National Instruments License Manager.

serialNumber
 As
 [String](data-types-for-teststand.html)

[Out] Returns the serial number for this installation of TestStand.

#### See Also

[Engine.GetLicenseDescription](engine-getlicensedescription.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getrelativepathfromabsolutepath.html language=enus -->
## TOPIC 00831: Engine.GetRelativePathFromAbsolutePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getrelativepathfromabsolutepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getrelativepathfromabsolutepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetRelativePathFromAbsolutePath( absolutePath, searchContext, relativePath, searchDirectoryPath) Return Value Boolean Returns True if the file is found. Purpose Searches for a file in the TestStand search directories using an absolute path and returns the relative path with respect to

### Engine.GetRelativePathFromAbsolutePath

#### Syntax

[Engine](engine.html).GetRelativePathFromAbsolutePath( absolutePath, searchContext, relativePath, searchDirectoryPath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns True if the file is found.

#### Purpose

Searches for a file in the TestStand search directories using an absolute path and returns the relative path with respect to the search directory.

#### Parameters

absolutePath
 As
 [String](data-types-for-teststand.html)

[In] An absolute or relative path for the file to find.

searchContext
 As
 [Variant](data-types-for-teststand.html)

[In] Contains the directory of the sequence file, which may also be searched for relative paths.

relativePath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the relative path if the file exists on disk and a relative path is found. Otherwise, returns the absolute path.

searchDirectoryPath
 As
 [String](data-types-for-teststand.html)

[Out] Returns the related search directory if the relative path is found.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getresourcestring.html language=enus -->
## TOPIC 00832: Engine.GetResourceString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getresourcestring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getresourcestring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetResourceString( section, symbol, [defaultString], [found]) Return Value String The resource string. Purpose Returns a string from the TestStand string resource file for the current language. You specify the string by category and symbol, which are the section and item labels for the

### Engine.GetResourceString

#### Syntax

[Engine](engine.html).GetResourceString( section, symbol, [defaultString], [found])

#### Return Value

[String](data-types-for-teststand.html)

The resource string.

#### Purpose

Returns a string from the TestStand string resource file for the current language. You specify the string by category and symbol, which are the section and item labels for the string in the string resource file.

#### Remarks

The string resource files are located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Language
 and
 <TestStand Public>\Components\Language
 directories. Typically, you customize the strings in the resource files in the
 <TestStand>\Components\Language
 directory by adding a section and item with the same name to the corresponding file in the
 <TestStand Public>\Components\Language
 directory.

Use the
 ResStr
 [expression function](../tsfundamentals/expression-functions.html)
 to retrieve a TestStand resource string from within an expression.

#### Parameters

section
 As
 [String](data-types-for-teststand.html)

[In] Specifies the category or section label.

symbol
 As
 [String](data-types-for-teststand.html)

[In] Specifies the symbol or item label.

defaultString
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a default string to return when the string resource file does not contain an entry with the category and symbol you specify. If you do not specify this parameter and the string resource file does not contain the entry, this function returns the string,
 String not found in table.

found
 As
 [Variant](data-types-for-teststand.html)

[Out] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Returns
 True
 if the string is found in the resource file and
 False
 if the string is not found in the resource file.

#### See Also

[Engine.ReloadStringResourceFiles](engine-reloadstringresourcefiles.html)

[Expression Functions](../tsfundamentals/expression-functions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getresourcesymbols.html language=enus -->
## TOPIC 00833: Engine.GetResourceSymbols

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getresourcesymbols.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getresourcesymbols.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetResourceSymbols( section) Return Value String Array An array of strings that contains the names of all the symbols under the given category. Purpose Returns a list of symbols from the TestStand string resource file for the current language. Remarks You specify the categories, which

### Engine.GetResourceSymbols

#### Syntax

[Engine](engine.html).GetResourceSymbols( section)

#### Return Value

[String Array](data-types-for-teststand.html)

An array of strings that contains the names of all the symbols under the given category.

#### Purpose

Returns a list of symbols from the TestStand string resource file for the current language.

#### Remarks

You specify the categories, which are the sections in the string resource file.

The string resource files are located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Language
 and
 "<TestStand Public>\Components\Language
 directories. You can customize the strings in the resource files in the
 <TestStand>\Components\Language
 directory by adding a section and item with the same name to the corresponding file in the
 <TestStand Public>\Components\Language
 directory.

#### Parameters

section
 As
 [String](data-types-for-teststand.html)

[In] Specifies the category or section label.

#### See Also

[Engine.GetResourceString](engine-getresourcestring.html)

[Engine.ReloadStringResourceFiles](engine-reloadstringresourcefiles.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getruntimetoolmenuitems.html language=enus -->
## TOPIC 00834: Engine.GetRunTimeToolMenuItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getruntimetoolmenuitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getruntimetoolmenuitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetRunTimeToolMenuItems( [editArgsParam], reserved = 0) Return Value RunTimeMenuItems Purpose Returns a reference to a RunTimeMenuItems object. Use this method to determine the run-time text and dimmed state of menu items defined in the collection the Engine.GetEditTimeToolMenuItems me

### Engine.GetRunTimeToolMenuItems

#### Syntax

[Engine](engine.html).GetRunTimeToolMenuItems( [editArgsParam], reserved = 0)

#### Return Value

[RunTimeMenuItems](runtimemenuitems.html)

#### Purpose

Returns a reference to a RunTimeMenuItems object. Use this method to determine the run-time text and dimmed state of menu items defined in the collection the
 [Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)
 method returns.

#### Remarks

TestStand maintains a collection of Tools menu items. You can obtain a reference to the collection using the
 Engine.GetEditTimeToolMenuItems
 method. You can also customize the contents of the Tools menu.

TestStand uses the menu items in the edit-time collection to generate a run-time version of the menu items. TestStand evaluates edit-time menu item expressions to determine the value of run-time properties, such as menu item text and whether menu items are enabled. TestStand excludes any edit-time menu items with hidden expressions that evaluate to
 False
 from the run-time collection. The run-time collection also contains expanded submenus for menu items using the
 ToolMenuType_SequenceFile
 type.

#### Parameters

editArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies the currently selected items in the user interface. The menu item expressions can use this information to determine item text, hidden state, and enabled state.

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

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[RunTimeMenuItems](runtimemenuitems.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getsequencefile.html language=enus -->
## TOPIC 00835: Engine.GetSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetSequenceFile( seqFilePath, getSeqFileFlags = GetSeqFile_OperatorInterfaceFlags) Return Value SequenceFile A SequenceFile object. Purpose This method is obsolete. Use the Engine.GetSequenceFileEx method instead. Remarks Returns the SequenceFile object for the sequence file the sequen

### Engine.GetSequenceFile

#### Syntax

[Engine](engine.html).GetSequenceFile( seqFilePath, getSeqFileFlags = GetSeqFile_OperatorInterfaceFlags)

#### Return Value

[SequenceFile](sequencefile.html)

A SequenceFile object.

#### Purpose

Note

Engine.GetSequenceFileEx

#### Remarks

Returns the SequenceFile object for the sequence file the
 sequenceFilePath
 parameter specifies.

#### Parameters

seqFilePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the sequence file.

getSeqFileFlags
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [GetSeqFileOptions](getseqfileoptions.html)
 constants. Use the bitwise-OR operator to specify multiple sequence file flags.

This parameter has a default value of
 GetSeqFile_OperatorInterfaceFlags
 .

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.NewSequenceFile](engine-newsequencefile.html)

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[GetSeqFileOptions](getseqfileoptions.html)

[SequenceFile](sequencefile.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getsequencefileex.html language=enus -->
## TOPIC 00836: Engine.GetSequenceFileEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getsequencefileex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getsequencefileex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetSequenceFileEx( seqFilePath, getSeqFileFlags = GetSeqFile_OperatorInterfaceFlags, handlerType = ConflictHandler_Error) Return Value SequenceFile A SequenceFile object. Purpose Returns the SequenceFile object for the sequence file the sequenceFilePath parameter specifies. Remarks Loa

### Engine.GetSequenceFileEx

#### Syntax

[Engine](engine.html).GetSequenceFileEx( seqFilePath, getSeqFileFlags = GetSeqFile_OperatorInterfaceFlags, handlerType = ConflictHandler_Error)

#### Return Value

[SequenceFile](sequencefile.html)

A SequenceFile object.

#### Purpose

Returns the SequenceFile object for the sequence file the
 sequenceFilePath
 parameter specifies.

#### Remarks

Loads the sequence file from disk, if necessary. Call the
 [Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)
 method on this object before releasing it.

This method loads the sequence file into the internal cache of the engine and adds a load reference to the sequence file. TestStand uses the load reference count to determine when to unload the sequence file from the internal cache of the engine. In addition to this method, the
 [SequenceFile.AddLoadReference](sequencefile-addloadreference.html)
 and
 [Engine.NewSequenceFile](engine-newsequencefile.html)
 methods add a load reference to the sequence file. The
 [Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)
 method removes a load reference.

You must call the
 Engine.ReleaseSequenceFileEx
 method for each load reference you add to the sequence file. When you release the last load reference, TestStand unloads the file from the internal cache of the engine. While unloading the file from the cache, TestStand executes the SequenceFileUnload callback sequence, if applicable.

You can use the
 [SequenceAdapter.GetSequenceFile](sequenceadapter-getsequencefile.html)
 method to examine the contents of a sequence file without running load and unload callbacks, without preloading modules, and without merging types.

You can use the
 [GetSeqFile_GetFileOnlyIfInCache](getseqfileoptions.html)
 option with this method to determine whether a sequence file is already loaded in the engine internal cache.

#### Parameters

seqFilePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the sequence file. If the pathname is relative, this method tries to find it in the current directory, unless you specify the
 [GetSeqFile_FindFile](getseqfileoptions.html)
 option.

getSeqFileFlags
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [GetSeqFileOptions](getseqfileoptions.html)
 constants. Use the bitwise-OR operator to specify multiple sequence file flags.

This parameter has a default value of
 GetSeqFile_OperatorInterfaceFlags
 .

handlerType
 As
 [TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[In] Specifies how to handle type conflicts.

This parameter has a default value of
 ConflictHandler_Error
 .

#### See Also

[Engine.NewSequenceFile](engine-newsequencefile.html)

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[GetSeqFileOptions](getseqfileoptions.html)

[SequenceAdapter.GetSequenceFile](sequenceadapter-getsequencefile.html)

[SequenceFile](sequencefile.html)

[SequenceFile.AddLoadReference](sequencefile-addloadreference.html)

[TypeConflictHandlerTypes](typeconflicthandlertypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getstationmodelsequencefile.html language=enus -->
## TOPIC 00837: Engine.GetStationModelSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getstationmodelsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getstationmodelsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetStationModelSequenceFile( modelDescriptionString) Return Value SequenceFile Purpose Returns a reference to the process model sequence file TestStand associates with the test station. Remarks Release this reference when you are done using it. This method returns an error if the seque

### Engine.GetStationModelSequenceFile

#### Syntax

[Engine](engine.html).GetStationModelSequenceFile( modelDescriptionString)

#### Return Value

[SequenceFile](sequencefile.html)

#### Purpose

Returns a reference to the process model sequence file TestStand associates with the test station.

#### Remarks

Release this reference when you are done using it.

This method returns an error if the sequence file exists but TestStand cannot load it for some reason. For example, TestStand might be unable to load the sequence file if there are type conflicts that cannot be automatically resolved.

#### Parameters

modelDescriptionString
 As
 [String](data-types-for-teststand.html)

[Out] Returns a string that describes the process model file.

#### See Also

[SequenceFile](sequencefile.html)

[SequenceFile.GetModelSequenceFile](sequencefile-getmodelsequencefile.html)

[StationOptions.AllowOtherModels](stationoptions-allowothermodels.html)

[StationOptions.StationModelSequenceFilePath](stationoptions-stationmodelsequencefilepath.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getsyncmanager.html language=enus -->
## TOPIC 00838: Engine.GetSyncManager

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getsyncmanager.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getsyncmanager.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetSyncManager( syncObjectName) Return Value IUnknown A pointer to the TestStand Synchronization Manager the Synchronization object name describes. Purpose Returns a top-level API for synchronizing with TestStand Synchronization objects. Remarks The TestStand Synchronization Manager is

### Engine.GetSyncManager

#### Syntax

[Engine](engine.html).GetSyncManager( syncObjectName)

#### Return Value

[IUnknown](data-types-for-teststand.html)

A pointer to the TestStand Synchronization Manager the Synchronization object name describes.

#### Purpose

Returns a top-level API for synchronizing with TestStand Synchronization objects.

#### Remarks

The
 [TestStand Synchronization Manager](../tssyncserver/teststand-synchronization-server.html)
 is the API the Synchronization step types use. The name of the Synchronization object passed to this function determines which Synchronization Manager to use—in process, out of process (used to share Synchronization objects between processes), or remote machine (used to share Synchronization objects across machines). Refer to the NI TestStand Synchronization type library for more information.

#### Parameters

syncObjectName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the Synchronization object for which the Synchronization Manager is needed. When the Synchronization object begins with an '*' (for example,
 *syncobjectname
 ) or a computer name such as
 \\machinename\syncobjectname
 , a Synchronization Manager object corresponding to the computer in question is returned.

When the Synchronization object name begins with an asterisk or computer name, you can use a
 32
 or
 64
 prefix to specify using 32- or 64-bit TestStand to host the out-of-process Synchronization object. For example, the name
 64*syncobj
 specifies a Synchronization object called
 *syncobj
 in the 64-bit TestStand host process, even when used from 32-bit TestStand. Use the prefix to share Synchronization objects between 32-bit TestStand and 64-bit TestStand in the same host process. If you do not use the prefix, 32-bit TestStand hosts out-of-process Synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process Synchronization objects in a 64-bit process.

#### See Also

[TestStand Synchronization Manager](../tssyncserver/teststand-synchronization-server.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettemplatesfile.html language=enus -->
## TOPIC 00839: Engine.GetTemplatesFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettemplatesfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettemplatesfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetTemplatesFile( options = 0) Return Value PropertyObjectFile The file that contains the editing templates. Purpose Returns the PropertyObjectFile that contains templates for variables, steps, and sequences you can insert while editing. Parameters options As Long [In] Specifies any co

### Engine.GetTemplatesFile

#### Syntax

[Engine](engine.html).GetTemplatesFile( options = 0)

#### Return Value

[PropertyObjectFile](propertyobjectfile.html)

The file that contains the editing templates.

#### Purpose

Returns the PropertyObjectFile that contains templates for variables, steps, and sequences you can insert while editing.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of
 [GetTemplatesFileOptions](gettemplatesfileoptions.html)
 .

This parameter has a default value of
 0
 .

#### See Also

[GetTemplatesFileOptions](gettemplatesfileoptions.html)

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getteststandpath.html language=enus -->
## TOPIC 00840: Engine.GetTestStandPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getteststandpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getteststandpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetTestStandPath( testStandPath) Return Value String Purpose Returns the pathname of the TestStand directory the testStandPath parameter specifies. Remarks The pathname does not contain a trailing backslash. Parameters testStandPath As TestStandPaths [In] Specifies the TestStand direct

### Engine.GetTestStandPath

#### Syntax

[Engine](engine.html).GetTestStandPath( testStandPath)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the pathname of the TestStand directory the
 testStandPath
 parameter specifies.

#### Remarks

The pathname does not contain a trailing backslash.

#### Parameters

testStandPath
 As
 [TestStandPaths](teststandpaths.html)

[In] Specifies the
 [TestStand directory](teststandpaths.html)
 to return.

#### See Also

[Engine.SearchDirectories](engine-searchdirectories.html)

[TestStandPaths](teststandpaths.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettoolmenuiteminfo.html language=enus -->
## TOPIC 00841: Engine.GetToolMenuItemInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettoolmenuiteminfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettoolmenuiteminfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetToolMenuItemInfo( menuIndex, itemIndex, itemText, subMenuIndex, enabled, uniqueItemID) Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Returns information about a Tools menu item. Parameters menuInd

### Engine.GetToolMenuItemInfo

#### Syntax

[Engine](engine.html).GetToolMenuItemInfo( menuIndex, itemIndex, itemText, subMenuIndex, enabled, uniqueItemID)

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Returns information about a Tools menu item.

#### Parameters

menuIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for a Tools menu or submenu.

itemIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for an item within the menu or submenu.

itemText
 As
 [String](data-types-for-teststand.html)

[Out] Returns the text to display in the menu item.

subMenuIndex
 As
 [Long](data-types-for-teststand.html)

[Out] If the item is a submenu, this parameter returns the zero-based menu index of the Tools menu for the item. Otherwise, it returns
 -1
 .

enabled
 As
 [Boolean](data-types-for-teststand.html)

[Out] If this parameter is
 True
 , enable the menu item. If this parameter is
 False
 , disable it.

uniqueItemID
 As
 [Long](data-types-for-teststand.html)

[Out] Returns a unique ID to identify the menu item. Use this ID to invoke the Tools menu item or to obtain the menu item information again at a later time.

#### See Also

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettoolmenuiteminfoex.html language=enus -->
## TOPIC 00842: Engine.GetToolMenuItemInfoEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettoolmenuiteminfoex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettoolmenuiteminfoex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetToolMenuItemInfoEx( menuIndex, itemIndex, itemText, subMenuIndex, itemAttributes, uniqueItemID) Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Returns information about a Tools menu item, which you

### Engine.GetToolMenuItemInfoEx

#### Syntax

[Engine](engine.html).GetToolMenuItemInfoEx( menuIndex, itemIndex, itemText, subMenuIndex, itemAttributes, uniqueItemID)

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Returns information about a Tools menu item, which you specify with a menu index and an item index.

Use this information when constructing a Tools menu in a user interface. You must call the
 [Engine.ConstructToolMenus](engine-constructtoolmenus.html)
 method before calling this function.

#### Parameters

menuIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for a Tools menu or submenu.

itemIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for an item within the menu or submenu.

itemText
 As
 [String](data-types-for-teststand.html)

[Out] Returns the text to display in the menu item.

subMenuIndex
 As
 [Long](data-types-for-teststand.html)

[Out] If the item is a submenu, this parameter returns the zero-based menu index of the Tools menu for the item. Otherwise, it returns
 -1
 .

itemAttributes
 As
 [Long](data-types-for-teststand.html)

[Out] The bitwise-OR combination of one or more
 [ToolMenuItemAttributes](toolmenuitemattributes.html)
 constants. Use the bitwise-AND operator to determine whether an item has a specific attribute.

uniqueItemID
 As
 [Long](data-types-for-teststand.html)

[Out] Returns a unique ID to identify the menu item. Use this ID to invoke the Tools menu item or to obtain the menu item information again at a later time.

#### See Also

[Engine.ConstructToolMenus](engine-constructtoolmenus.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[ToolMenuItemAttributes](toolmenuitemattributes.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettoolmenuiteminfowithid.html language=enus -->
## TOPIC 00843: Engine.GetToolMenuItemInfoWithID

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettoolmenuiteminfowithid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettoolmenuiteminfowithid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetToolMenuItemInfoWithID( uniqueItemID, itemText, subMenuIndex, enabled) Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Returns information about a Tools menu item. Parameters uniqueItemID As Long [I

### Engine.GetToolMenuItemInfoWithID

#### Syntax

[Engine](engine.html).GetToolMenuItemInfoWithID( uniqueItemID, itemText, subMenuIndex, enabled)

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Returns information about a Tools menu item.

#### Parameters

uniqueItemID
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a Tools menu item ID you obtain from the
 [Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)
 method.

itemText
 As
 [String](data-types-for-teststand.html)

[Out] Returns the text to display in the menu item.

subMenuIndex
 As
 [Long](data-types-for-teststand.html)

[Out] If the item is a submenu, this parameter returns the zero-based menu index of the Tools menu for the item. Otherwise, it returns
 -1
 .

enabled
 As
 [Boolean](data-types-for-teststand.html)

[Out] If this parameter is
 True
 , enable the menu item. If this parameter is
 False
 , disable it.

#### See Also

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettoolmenuiteminfowithidex.html language=enus -->
## TOPIC 00844: Engine.GetToolMenuItemInfoWithIDEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettoolmenuiteminfowithidex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettoolmenuiteminfowithidex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetToolMenuItemInfoWithIDEx( uniqueItemID, itemText, subMenuIndex, itemAttributes) Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Returns information about a Tools menu item, which you specify with a

### Engine.GetToolMenuItemInfoWithIDEx

#### Syntax

[Engine](engine.html).GetToolMenuItemInfoWithIDEx( uniqueItemID, itemText, subMenuIndex, itemAttributes)

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Returns information about a Tools menu item, which you specify with a unique Tools menu item ID.

The information returned is useful for constructing a Tools menu in a user interface. You must call the
 [Engine.ConstructToolMenus](engine-constructtoolmenus.html)
 method before calling this function.

#### Parameters

uniqueItemID
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the Tools menu item ID you obtain from the
 [Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)
 method or the
 [Menu_ToolIDProp](menuitemproperties.html)
 property on the object the
 [Engine.GetToolMenuStructure](engine-gettoolmenustructure.html)
 method returns.

itemText
 As
 [String](data-types-for-teststand.html)

[Out] Returns the text to display in the menu item.

subMenuIndex
 As
 [Long](data-types-for-teststand.html)

[Out] If the item is a submenu, this parameter returns the zero-based menu index of the Tools menu for the item. Otherwise, it returns
 -1
 .

itemAttributes
 As
 [Long](data-types-for-teststand.html)

[Out] The bitwise-OR combination of one or more
 [ToolMenuItemAttributes](toolmenuitemattributes.html)
 constants. Use the bitwise-AND operator to determine whether an item has a specific attribute.

#### See Also

[Engine.ConstructToolMenus](engine-constructtoolmenus.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)

[Engine.GetToolMenuStructure](engine-gettoolmenustructure.html)

[MenuItemProperties](menuitemproperties.html)

[ToolMenuItemAttributes](toolmenuitemattributes.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettoolmenustructure.html language=enus -->
## TOPIC 00845: Engine.GetToolMenuStructure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettoolmenustructure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettoolmenustructure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetToolMenuStructure Return Value PropertyObject The object that specifies the menu structure. See MenuItemProperties for a description of this property object. Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead.

### Engine.GetToolMenuStructure

#### Syntax

[Engine](engine.html).GetToolMenuStructure

#### Return Value

[PropertyObject](propertyobject.html)

The object that specifies the menu structure. See
 [MenuItemProperties](menuitemproperties.html)
 for a description of this property object.

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Obtains a PropertyObject object that specifies the structure of the Tools menu.

Note

Engine.ConstructToolMenus

You can use this method to obtain information about the Tools menu items instead of using the
 [Engine.GetNumToolMenus](engine-getnumtoolmenus.html)
 ,
 [Engine.GetNumToolMenuItems](engine-getnumtoolmenuitems.html)
 ,
 [Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)
 , and
 [Engine.GetToolMenuItemInfoWithIDEx](engine-gettoolmenuiteminfowithidex.html)
 methods.

#### See Also

[Engine.ConstructToolMenus](engine-constructtoolmenus.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetNumToolMenus](engine-getnumtoolmenus.html)

[Engine.GetNumToolMenuItems](engine-getnumtoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)

[Engine.GetToolMenuItemInfoWithIDEx](engine-gettoolmenuiteminfowithidex.html)

[MenuItemProperties](menuitemproperties.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettypedefinition.html language=enus -->
## TOPIC 00846: Engine.GetTypeDefinition

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettypedefinition.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettypedefinition.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetTypeDefinition( typeNameParam) Return Value PropertyObject The type definition PropertyObject. Returns NULL or 0 if the type definition does not exist. Purpose Returns the PropertyObject object for the specified type name. Remarks The returned PropertyObject object is the type defin

### Engine.GetTypeDefinition

#### Syntax

[Engine](engine.html).GetTypeDefinition( typeNameParam)

#### Return Value

[PropertyObject](propertyobject.html)

The type definition PropertyObject. Returns
 NULL
 or
 0
 if the type definition does not exist.

#### Purpose

Returns the PropertyObject object for the specified type name.

#### Remarks

The returned PropertyObject object is the type definition for the specified type name.

#### Parameters

typeNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the type to obtain.

#### See Also

[Engine.GetTypeNames](engine-gettypenames.html)

[Engine.GetTypeUsageLocations](engine-gettypeusagelocations.html)

[PropertyObject](propertyobject.html)

[PropertyObject.GetTypeDefinition](propertyobject-gettypedefinition.html)

[PropertyObject.IsTypeDefinition](propertyobject-istypedefinition.html)

[PropertyObject.TypeCategory](propertyobject-typecategory.html)

[PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)

[TypeUsageList](typeusagelist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettypenames.html language=enus -->
## TOPIC 00847: Engine.GetTypeNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettypenames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettypenames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetTypeNames Return Value String Array An array of strings that contains the names of all currently loaded types. Purpose Returns an array of all currently loaded type names. See Also Engine.GetTypeDefinition Engine.GetTypeUsageLocations PropertyObjectFile.TypeUsageList TypeUsageList

### Engine.GetTypeNames

#### Syntax

[Engine](engine.html).GetTypeNames

#### Return Value

[String Array](data-types-for-teststand.html)

An array of strings that contains the names of all currently loaded types.

#### Purpose

Returns an array of all currently loaded type names.

#### See Also

[Engine.GetTypeDefinition](engine-gettypedefinition.html)

[Engine.GetTypeUsageLocations](engine-gettypeusagelocations.html)

[PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)

[TypeUsageList](typeusagelist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettypepalettefilelist.html language=enus -->
## TOPIC 00848: Engine.GetTypePaletteFileList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettypepalettefilelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettypepalettefilelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetTypePaletteFileList Return Value Object Array An array of pointers to the PropertyObjectFile interfaces of the loaded type palette files. Purpose Returns the list of currently loaded type palette files in the TestStand Engine. Remarks Type palette files contain step type and data ty

### Engine.GetTypePaletteFileList

#### Syntax

[Engine](engine.html).GetTypePaletteFileList

#### Return Value

[Object Array](data-types-for-teststand.html)

An array of pointers to the PropertyObjectFile interfaces of the loaded type palette files.

#### Purpose

Returns the list of currently loaded type palette files in the TestStand Engine.

#### Remarks

Type palette files contain step type and data type definitions. The TestStand Engine loads these files when the sequence editor and user interfaces launch. Call this method to obtain the list of loaded type palettes.

#### See Also

[Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)

[Engine.SetTypePaletteFileList](engine-settypepalettefilelist.html)

[Engine.UnloadTypePaletteFiles](engine-unloadtypepalettefiles.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettypes.html language=enus -->
## TOPIC 00849: Engine.GetTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetTypes( reserved = 0) Return Value TypeUsageList Purpose Returns a TypeUsageList that contains all the types currently in memory. Parameters reserved As Long [In] Reserved for future use. This parameter has a default value of 0 . See Also TypeUsageList

### Engine.GetTypes

#### Syntax

[Engine](engine.html).GetTypes( reserved = 0)

#### Return Value

[TypeUsageList](typeusagelist.html)

#### Purpose

Returns a
 [TypeUsageList](typeusagelist.html)
 that contains all the types currently in memory.

#### Parameters

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use.

This parameter has a default value of
 0
 .

#### See Also

[TypeUsageList](typeusagelist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-gettypeusagelocations.html language=enus -->
## TOPIC 00850: Engine.GetTypeUsageLocations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-gettypeusagelocations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-gettypeusagelocations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetTypeUsageLocations( typeNameParam) Return Value Object Array An array of PropertyObjectFile objects that use the type that the type name specifies. Purpose Returns an array of PropertyObjectFile objects that use the specified type name. Remarks A PropertyObjectFile object uses a typ

### Engine.GetTypeUsageLocations

#### Syntax

[Engine](engine.html).GetTypeUsageLocations( typeNameParam)

#### Return Value

[Object Array](data-types-for-teststand.html)

An array of PropertyObjectFile objects that use the type that the type name specifies.

#### Purpose

Returns an array of PropertyObjectFile objects that use the specified type name.

#### Remarks

A PropertyObjectFile object uses a type if it has an instance of the type or if the type is stored in the
 [TypeUsageList](typeusagelist.html)
 for that file.

#### Parameters

typeNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the type.

#### See Also

[Engine.GetTypeDefinition](engine-gettypedefinition.html)

[Engine.GetTypeNames](engine-gettypenames.html)

[PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)

[TypeUsageList](typeusagelist.html)

[TypeUsageList.GetIsTypeAttachedToFile](typeusagelist-getistypeattachedtofile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getuimessage.html language=enus -->
## TOPIC 00851: Engine.GetUIMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getuimessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getuimessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetUIMessage Return Value UIMessage Purpose Obtains the next available message from the queue. Remarks Use this method to poll for UIMessages. See Also Engine.RegisterUIMessageCallback Engine.UIMessageEvent Engine.UIMessagePollingEnabled StationOptions.UIMessageDelay StationOptions.UIM

### Engine.GetUIMessage

#### Syntax

[Engine](engine.html).GetUIMessage

#### Return Value

[UIMessage](uimessage.html)

#### Purpose

Obtains the next available message from the queue.

#### Remarks

Use this method to poll for UIMessages.

#### See Also

[Engine.RegisterUIMessageCallback](engine-registeruimessagecallback.html)

[Engine.UIMessageEvent](engine-uimessageevent.html)

[Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)

[StationOptions.UIMessageDelay](stationoptions-uimessagedelay.html)

[StationOptions.UIMessageMinDelay](stationoptions-uimessagemindelay.html)

[UIMessage](uimessage.html)

[User Interface (UI) Messages](/csh?context=ts_tsapiref_app_user_interface_ui_messages)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getuser.html language=enus -->
## TOPIC 00852: Engine.GetUser

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getuser.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getuser.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetUser( loginName) Return Value User Purpose Obtains the User object that contains a specific login name. Remarks Returns NULL if no User object has the specified login name. Parameters loginName As String [In] Specifies the login name to find. See Also Engine.CurrentUser Engine.Displ

### Engine.GetUser

#### Syntax

[Engine](engine.html).GetUser( loginName)

#### Return Value

[User](user.html)

#### Purpose

Obtains the
 [User](user.html)
 object that contains a specific login name.

#### Remarks

Returns
 NULL
 if no User object has the specified login name.

#### Parameters

loginName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the login name to find.

#### See Also

[Engine.CurrentUser](engine-currentuser.html)

[Engine.DisplayEditUserDialog](engine-displayedituserdialog.html)

[Engine.UsersFile](engine-usersfile.html)

[User](user.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getusergroup.html language=enus -->
## TOPIC 00853: Engine.GetUserGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getusergroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getusergroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetUserGroup( userGroupName) Return Value User Purpose Obtains the User object that represents a specific user group. Remarks Returns NULL if the user group does not exist. The user group specifies the list of user names that are members of the group and the shared privileges granted t

### Engine.GetUserGroup

#### Syntax

[Engine](engine.html).GetUserGroup( userGroupName)

#### Return Value

[User](user.html)

#### Purpose

Obtains the
 [User](user.html)
 object that represents a specific user group.

#### Remarks

Returns
 NULL
 if the user group does not exist.

The user group specifies the list of user names that are members of the group and the shared privileges granted to the members. Use the
 [User.Members](user-members.html)
 property to edit the list of user names.

#### Parameters

userGroupName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the user group to return.

#### See Also

[Engine.DisplayEditUserDialog](engine-displayedituserdialog.html)

[Engine.GetUser](engine-getuser.html)

[Engine.UsersFile](engine-usersfile.html)

[User](user.html)

[User.Members](user-members.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getuserprofile.html language=enus -->
## TOPIC 00854: Engine.GetUserProfile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getuserprofile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getuserprofile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetUserProfile( userProfileName) Return Value User Purpose This method is obsolete. Use Engine.GetUserGroup method instead. Remarks Obtains the User object that contains a specific user profile. Returns NULL if the user profile does not exist. The user profile is a template for an actu

### Engine.GetUserProfile

#### Syntax

[Engine](engine.html).GetUserProfile( userProfileName)

#### Return Value

[User](user.html)

#### Purpose

Note

Engine.GetUserGroup

#### Remarks

Obtains the
 [User](user.html)
 object that contains a specific user profile. Returns
 NULL
 if the user profile does not exist.

The user profile is a template for an actual user. Pass the user profile object to the
 [Engine.NewUser](engine-newuser.html)
 method to create a new user.

#### Parameters

userProfileName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the user profile to return.

#### See Also

[Engine.DisplayEditUserDialog](engine-displayedituserdialog.html)

[Engine.GetUser](engine-getuser.html)

[Engine.NewUser](engine-newuser.html)

[Engine.UsersFile](engine-usersfile.html)

[User](user.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getwatchexpressions.html language=enus -->
## TOPIC 00855: Engine.GetWatchExpressions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getwatchexpressions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getwatchexpressions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetWatchExpressions( clientSequenceFileParam = NULL, scopingSeqContext = NULL, filterOptions = WatchExpressionFilter_NoOptions) Return Value WatchExpressions Returns an empty list if no watch expressions in the list are valid for the specified scope. Purpose Returns a list of reference

### Engine.GetWatchExpressions

#### Syntax

[Engine](engine.html).GetWatchExpressions( clientSequenceFileParam = NULL, scopingSeqContext = NULL, filterOptions = WatchExpressionFilter_NoOptions)

#### Return Value

[WatchExpressions](watchexpressions.html)

Returns an empty list if no watch expressions in the list are valid for the specified scope.

#### Purpose

Returns a list of references to WatchExpression objects in the watch expression list that the engine maintains. The method returns only objects that match the scope and filter settings specified by the parameters this method contains.

#### Remarks

A watch expression is global if it is not associated with a client sequence file.

The
 [WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)
 ,
 [WatchExpression.ExecutionScope](watchexpression-executionscope.html)
 ,
 [WatchExpression.SequenceFileScope](watchexpression-sequencefilescope.html)
 , and
 [WatchExpression.SequenceScope](watchexpression-sequencescope.html)
 properties specify the scope of a WatchExpression object.

Use the
 clientSequenceFileParam
 and the
 scopingSeqContext
 parameters of this method to filter the watch expression list. Pass
 NULL
 for both of these parameters to return the entire watch expression list. If you pass values for these parameters, TestStand uses the
 filterOptions
 parameter to identify
 [which watch expression properties](watchexpressionfilteroptions.html)
 to compare to the parameter values you pass.

#### Parameters

clientSequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies a reference to a client sequence file used to identify and limit the watch expressions to return. The method does not return a watch expression if the
 [WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)
 property does not match the name of the file this parameter specifies. Pass
 NULL
 to instruct the method to not filter watch expressions based on the client sequence file. Pass
 WatchExpressionFilter_IncludeGlobals
 in the
 filterOptions
 parameter to instruct the method to include watch expressions that specify an empty string for the
 WatchExpression.ClientSequenceFile
 property.

This parameter has a default value of
 NULL
 .

scopingSeqContext
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies a reference to a sequence context used to identify and limit the watch expressions to return. The method requires a sequence context when you pass
 WatchExpressionFilter_FilterByExecution
 ,
 WatchExpressionFilter_FilterBySequence
 , or
 WatchExpressionFilter_FilterBySequenceFile
 to the
 filterOptions
 parameter. The method does not return a watch expression if you pass a filter option and the corresponding scope property for the watch expression does not match the given sequence context. The method ignores the filter option for a watch expression if the corresponding scope property does not specify a value. Pass
 NULL
 if you do not want the method to exclude watch expressions based on the scoping filter options.

This parameter has a default value of
 NULL
 .

filterOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the criteria for filtering the watch expression list. Pass a combination of the
 [WatchExpressionFilterOptions](watchexpressionfilteroptions.html)
 constants. A watch expression must meet all the filter criteria to be included in the returned list.

This parameter has a default value of
 WatchExpressionFilter_NoOptions
 .

#### See Also

[SequenceContext](sequencecontext.html)

[SequenceFile](sequencefile.html)

[WatchExpression.ClientSequenceFile](watchexpression-clientsequencefile.html)

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

[WatchExpression.SequenceFileScope](watchexpression-sequencefilescope.html)

[WatchExpression.SequenceScope](watchexpression-sequencescope.html)

[WatchExpressionFilterOptions](watchexpressionfilteroptions.html)

[WatchExpressions](watchexpressions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-getwatchexpressionschangecount.html language=enus -->
## TOPIC 00856: Engine.GetWatchExpressionsChangeCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-getwatchexpressionschangecount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-getwatchexpressionschangecount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GetWatchExpressionsChangeCount Return Value Long Purpose Returns the number of modifications made to the watch expression list the engine maintains or to the watch expressions in the list. Remarks When you insert or remove a WatchExpression object from the watch expression list the eng

### Engine.GetWatchExpressionsChangeCount

#### Syntax

[Engine](engine.html).GetWatchExpressionsChangeCount

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of modifications made to the watch expression list the engine maintains or to the watch expressions in the list.

#### Remarks

When you insert or remove a WatchExpression object from the watch expression list the engine maintains or when you modify a watch expression in the list, the engine increments the change count. The sequence editor and user interfaces can use this count to determine when to refresh the Watch View pane.

#### See Also

[WatchExpression](watchexpression.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-globals.html language=enus -->
## TOPIC 00857: Engine.Globals

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-globals.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-globals.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.Globals Data Type PropertyObject Purpose Returns the PropertyObject that contains the global variables for the test station. Remarks When you are writing a GUI, use this property to display or edit global variables from the sequence editor or user interface. See Also Engine.TemporaryGl

### Engine.Globals

#### Syntax

[Engine](engine.html).Globals

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the PropertyObject that contains the global variables for the test station.

#### Remarks

When you are writing a GUI, use this property to display or edit global variables from the sequence editor or user interface.

#### See Also

[Engine.TemporaryGlobals](engine-temporaryglobals.html)

[Engine.GlobalsFile](engine-globalsfile.html)

[PropertyObject](propertyobject.html)

[SequenceContext.StationGlobals](sequencecontext-stationglobals.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-globalsfile.html language=enus -->
## TOPIC 00858: Engine.GlobalsFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-globalsfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-globalsfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.GlobalsFile Data Type PropertyObjectFile Purpose Returns the PropertyObjectFile that contains the test station global variables. See Also Engine.CommitGlobalsToDisk Engine.ConfigDirectory Engine.Globals PropertyObjectFile

### Engine.GlobalsFile

#### Syntax

[Engine](engine.html).GlobalsFile

#### Data Type

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the PropertyObjectFile that contains the test station global variables.

#### See Also

[Engine.CommitGlobalsToDisk](engine-commitglobalstodisk.html)

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.Globals](engine-globals.html)

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-hasaddonlicense.html language=enus -->
## TOPIC 00859: Engine.HasAddonLicense

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-hasaddonlicense.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-hasaddonlicense.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.HasAddonLicense( addonFeatureName) Return Value Boolean Returns True if TestStand was able to successfully check out the specified addon license. Purpose Provides a way for addon products to check the licensing status of a specified feature. Remarks TestStand acquires licenses for asso

### Engine.HasAddonLicense

#### Syntax

[Engine](engine.html).HasAddonLicense( addonFeatureName)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if TestStand was able to successfully check out the specified addon license.

#### Purpose

Provides a way for addon products to check the licensing status of a specified feature.

#### Remarks

TestStand acquires licenses for associated addon products when you call the
 [Engine.AcquireLicense](engine-acquirelicense.html)
 method.

#### Parameters

addonFeatureName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the feature to check the status of.

#### See Also

[Engine.AcquireLicense](engine-acquirelicense.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-images.html language=enus -->
## TOPIC 00860: Engine.Images

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-images.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-images.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.Images Data Type Images Purpose Returns a reference to an Images object, which is a collection that contains a list of images. The collection specifies the images that TestStand loads from the <TestStand> \Components\Icons and <TestStand Public>\Components\Icons directories, as well as

### Engine.Images

#### Syntax

[Engine](engine.html).Images

#### Data Type

[Images](images.html)

#### Purpose

Returns a reference to an
 Images
 object, which is a collection that contains a list of images. The collection specifies the images that TestStand loads from the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories, as well as images you add using the
 [Engine.AddImage](engine-addimage.html)
 method. Use the
 [Images.FindImage](images-findimage.html)
 method to find an image using an image name.

#### Remarks

You must obtain the
 Images
 collection before accessing an image. Use the
 Images
 collection as an alternative to the
 [Engine.LargeImageListEx](engine-largeimagelistex.html)
 and
 [Engine.SmallImageListEx](engine-smallimagelistex.html)
 properties.

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

[Images](images.html)

[Images.FindImage](images-findimage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-invoketoolmenuitem.html language=enus -->
## TOPIC 00861: Engine.InvokeToolMenuItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-invoketoolmenuitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-invoketoolmenuitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.InvokeToolMenuItem( menuIndex, itemIndex) Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Executes the action associated with a Tools menu item, which you specify with a menu index and an item index. Y

### Engine.InvokeToolMenuItem

#### Syntax

[Engine](engine.html).InvokeToolMenuItem( menuIndex, itemIndex)

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Executes the action associated with a Tools menu item, which you specify with a menu index and an item index.

Note

Engine.ConstructToolMenus

#### Parameters

menuIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for a Tools menu or submenu.

itemIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for an item within a Tools menu or submenu.

#### See Also

[Engine.ConstructToolMenus](engine-constructtoolmenus.html)

[Engine.DisplayToolMenuDialog](engine-displaytoolmenudialog.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-invoketoolmenuitemwithid.html language=enus -->
## TOPIC 00862: Engine.InvokeToolMenuItemWithID

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-invoketoolmenuitemwithid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-invoketoolmenuitemwithid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.InvokeToolMenuItemWithID( uniqueItemID) Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Executes the action associated with a Tools menu item, which you specify with a unique Tools menu item ID. You mu

### Engine.InvokeToolMenuItemWithID

#### Syntax

[Engine](engine.html).InvokeToolMenuItemWithID( uniqueItemID)

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Executes the action associated with a Tools menu item, which you specify with a unique Tools menu item ID.

Note

Engine.ConstructToolMenus

#### Parameters

uniqueItemID
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the Tools menu item ID you obtain from the
 [Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)
 method or the
 [Menu_ToolIDProp](menuitemproperties.html)
 property on the object the
 [Engine.GetToolMenuStructure](engine-gettoolmenustructure.html)
 method returns.

#### See Also

[Engine.ConstructToolMenus](engine-constructtoolmenus.html)

[Engine.DisplayToolMenuDialog](engine-displaytoolmenudialog.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[Engine.GetToolMenuItemInfoEx](engine-gettoolmenuiteminfoex.html)

[Engine.GetToolMenuStructure](engine-gettoolmenustructure.html)

[MenuItemProperties](menuitemproperties.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-is64bit.html language=enus -->
## TOPIC 00863: Engine.Is64Bit

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-is64bit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-is64bit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.Is64Bit Data Type Boolean Returns True if this instance of the TestStand Engine is 64-bit. Purpose Indicates whether this instance of the TestStand Engine is 64-bit. See Also Engine.ExpandPathMacros

### Engine.Is64Bit

#### Syntax

[Engine](engine.html).Is64Bit

#### Data Type

[Boolean](data-types-for-teststand.html)

Returns
 True
 if this instance of the TestStand Engine is 64-bit.

#### Purpose

Indicates whether this instance of the TestStand Engine is 64-bit.

#### See Also

[Engine.ExpandPathMacros](engine-expandpathmacros.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-iscurrentsequencefileversion.html language=enus -->
## TOPIC 00864: Engine.IsCurrentSequenceFileVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-iscurrentsequencefileversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-iscurrentsequencefileversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.IsCurrentSequenceFileVersion( FilePath) Return Value Long Purpose Determines whether the TestStand Engine that saved the specified sequence file is the current version, an older version, or a newer version. Remarks The method returns one of the following values: -1 if an older version

### Engine.IsCurrentSequenceFileVersion

#### Syntax

[Engine](engine.html).IsCurrentSequenceFileVersion( FilePath)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Determines whether the TestStand Engine that saved the specified sequence file is the current version, an older version, or a newer version.

#### Remarks

The method returns one of the following values:

- -1 
 if an older version of the TestStand Engine created the sequence file.
- 0 
 if the currently active version of the TestStand Engine created the sequence file.
- 1 
 if a newer version of the TestStand Engine created the sequence file.

You can use this method in a sequence editor application that prompts the user before overwriting a sequence file saved in an older format.

#### Parameters

FilePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute pathname of the file.

#### See Also

[Engine.MajorVersion](engine-majorversion.html)

[Engine.MinorVersion](engine-minorversion.html)

[Engine.RevisionVersion](engine-revisionversion.html)

[Engine.VersionString](engine-versionstring.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-isremote.html language=enus -->
## TOPIC 00865: Engine.IsRemote

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-isremote.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-isremote.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.IsRemote Data Type Boolean Purpose Specifies whether the engine was created to execute sequences on a remote computer. Remarks A TestStand Engine must set this property. National Instruments recommends not setting this property manually. When TestStand executes sequences on a remote co

### Engine.IsRemote

#### Syntax

[Engine](engine.html).IsRemote

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether the engine was created to execute sequences on a remote computer.

#### Remarks

Note

When TestStand executes sequences on a remote computer, the software creates an instance of the TestStand Engine on the remote computer and sets this property on the remote engine to
 True
 . To determine whether the engine was created for remote execution, obtain the value of this property.

Note

#### See Also

[Engine.MasterEngine](engine-masterengine.html)

[StationOptions.AllowSequenceCallsFromRemoteMachine](stationoptions-allowsequencecallsfromremotema.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-isuimessagequeueempty.html language=enus -->
## TOPIC 00866: Engine.IsUIMessageQueueEmpty

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-isuimessagequeueempty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-isuimessagequeueempty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.IsUIMessageQueueEmpty Data Type Boolean Purpose Returns a value that indicates whether the user interface message queue is empty. Remarks If you are writing a sequence editor or user interface, use this property when polling for UIMessages to determine whether a message in the queue is

### Engine.IsUIMessageQueueEmpty

#### Syntax

[Engine](engine.html).IsUIMessageQueueEmpty

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the user interface message queue is empty.

#### Remarks

If you are writing a sequence editor or user interface, use this property when polling for UIMessages to determine whether a message in the queue is pending. You must set the
 [Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)
 property to
 True
 to poll for UIMessages.

#### See Also

[Engine.GetUIMessage](engine-getuimessage.html)

[Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)

[UIMessage](uimessage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-largeimagelist.html language=enus -->
## TOPIC 00867: Engine.LargeImageList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-largeimagelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-largeimagelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LargeImageList Data Type Long Purpose This property is obsolete. Use the Engine.LargeImageListEx property instead. Calling this property on a 64-bit instance of the TestStand Engine results in an error. Remarks Returns the Microsoft Windows handle for the TestStand list of large images

### Engine.LargeImageList

#### Syntax

[Engine](engine.html).LargeImageList

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

Engine.LargeImageListEx

#### Remarks

Returns the Microsoft Windows handle for the TestStand list of large images.

The TestStand Engine maintains lists of images for all the icons from the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories and images you add using the
 [Engine.AddImage](engine-addimage.html)
 method. TestStand separates the images according to size and places each image in the list of large images or in the list of small images.

This method returns a Windows handle, HIMAGELIST, for the list of large images. You can use the image list functions in the Microsoft Windows Platform Software Development Kit to access the images in the list. Use this property as an alternative to using the
 [Images](images.html)
 collection.

Note

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.GetImageIndex](engine-getimageindex.html)

[Engine.GetImageName](engine-getimagename.html)

[Engine.NumImages](engine-numimages.html)

[Engine.SmallImageList](engine-smallimagelist.html)

[Images](images.html)

[Step.LargeIconIndex](step-largeiconindex.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-largeimagelistex.html language=enus -->
## TOPIC 00868: Engine.LargeImageListEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-largeimagelistex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-largeimagelistex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LargeImageListEx Data Type Variant Purpose Returns the Microsoft Windows handle for the TestStand list of large images. Remarks The TestStand Engine maintains lists of images for all the icons from the <TestStand> \Components\Icons and <TestStand Public>\Components\Icons directories an

### Engine.LargeImageListEx

#### Syntax

[Engine](engine.html).LargeImageListEx

#### Data Type

[Variant](data-types-for-teststand.html)

#### Purpose

Returns the Microsoft Windows handle for the TestStand list of large images.

#### Remarks

The TestStand Engine maintains lists of images for all the icons from the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories and images you add using the
 [Engine.AddImage](engine-addimage.html)
 method. TestStand separates the images according to size and places each image in the list of large images or in the list of small images.

This method returns a Windows handle, HIMAGELIST, for the list of large images. The type of the variant matches the architecture of the TestStand Engine, for example,
 VT_UI4
 for 32-bit TestStand and
 VT_UI8
 for 64-bit TestStand. You can use the image list functions in the Microsoft Windows Platform Software Development Kit to access the images in the list. Use this property as an alternative to using the
 [Images](images.html)
 collection.

Note

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.GetImageIndex](engine-getimageindex.html)

[Engine.GetImageName](engine-getimagename.html)

[Engine.NumImages](engine-numimages.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

[Images](images.html)

[Step.LargeIconIndex](step-largeiconindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-lastworkspacepath.html language=enus -->
## TOPIC 00869: Engine.LastWorkspacePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-lastworkspacepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-lastworkspacepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LastWorkspacePath Data Type String Purpose Specifies the pathname of the workspace file that was open when the sequence editor last shut down. Remarks When the sequence editor shuts down, it sets this property to the pathname of the current workspace file. If no workspace file is curre

### Engine.LastWorkspacePath

#### Syntax

[Engine](engine.html).LastWorkspacePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the workspace file that was open when the sequence editor last shut down.

#### Remarks

When the sequence editor shuts down, it sets this property to the pathname of the current workspace file. If no workspace file is currently open, the sequence editor sets this property to an empty string. If the
 [StationOptions.ReloadWorkspaceAtStartup](stationoptions-reloadworkspaceatstartup.html)
 property is
 True
 , the sequence editor loads the workspace file that the last workspace pathname specifies.

#### See Also

[StationOptions.ReloadWorkspaceAtStartup](stationoptions-reloadworkspaceatstartup.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-launchexternalviewer.html language=enus -->
## TOPIC 00870: Engine.LaunchExternalViewer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-launchexternalviewer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-launchexternalviewer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LaunchExternalViewer( FilePath) Purpose Launches an external file viewer. Remarks Typically, you use this method to display test reports. This method specifies the external viewer based on settings you can edit when you call the Engine.DisplayExternalViewerDialog method. If the dialog

### Engine.LaunchExternalViewer

#### Syntax

[Engine](engine.html).LaunchExternalViewer( FilePath)

#### Purpose

Launches an external file viewer.

#### Remarks

Typically, you use this method to display test reports.

This method specifies the external viewer based on settings you can edit when you call the
 [Engine.DisplayExternalViewerDialog](engine-displayexternalviewerdialog.html)
 method. If the dialog box contains no settings that apply to the file, TestStand launches a viewer based on the file extension association defined for the operating system.

#### Parameters

FilePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the file to view.

#### See Also

[Engine.DisplayExternalViewerDialog](engine-displayexternalviewerdialog.html)

[ExternalReportViewers](externalreportviewers.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-licensetype.html language=enus -->
## TOPIC 00871: Engine.LicenseType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-licensetype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-licensetype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LicenseType Data Type LicenseTypes Use the following constants with this data type: LicenseType_BaseDeploymentEngine –(Value: 3) Indicates that TestStand is using a TestStand Base Deployment Engine License. LicenseType_CustomEditorDeployment –(Value: 9) Indicates that TestStand is usin

### Engine.LicenseType

#### Syntax

[Engine](engine.html).LicenseType

#### Data Type

[LicenseTypes](licensetypes.html)

Use the following constants with this data type:

- LicenseType_BaseDeploymentEngine 
 –(Value: 3) Indicates that TestStand is using a TestStand Base Deployment Engine License.
- LicenseType_CustomEditorDeployment 
 –(Value: 9) Indicates that TestStand is using a TestStand Custom Sequence Editor License.
- LicenseType_DebugDeploymentEnv 
 –(Value: 2) Indicates that TestStand is using a TestStand Debug Deployment Environment License.
- LicenseType_DevelopmentSystem 
 –(Value: 1) Indicates that TestStand is using a TestStand Development System License.
- LicenseType_Evaluation 
 –(Value: 5) Indicates that TestStand is using an Evaluation license.
- LicenseType_NoLicense 
 –(Value: 6) Indicates that TestStand is using no license.
- LicenseType_OEM 
 –(Value: 4) Indicates that TestStand is using an OEM license.
- LicenseType_Other 
 –(Value: 8) Indicates that TestStand cannot determine the type of license.
- LicenseType_Temporary 
 –(Value: 7) Indicates that TestStand is using a temporary license. TestStand acquires a temporary license when NI License Manager cannot access the Volume License server.

#### Purpose

Returns the type of the
 
 [license](/csh?context=ts_9050)
 the TestStand Engine is using.

#### Remarks

If multiple license types are activated on the same computer, the TestStand Engine prioritizes the minimum required license over others. If all four TestStand license types are activated on a computer, the following licenses are prioritized:

- TestStand Sequence Editor–Debug Deployment Environment
- TestStand Editor UI–Custom Sequence Editor
- TestStand Operator UI–Base Deployment Engine

#### See Also

[Activating Your Software with the NI License Manager](../tshelp/activating-your-software.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-loadtypepalettefiles.html language=enus -->
## TOPIC 00872: Engine.LoadTypePaletteFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-loadtypepalettefiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-loadtypepalettefiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LoadTypePaletteFiles Purpose This method is obsolete. Use the Engine.LoadTypePaletteFilesEx method instead. Remarks Loads the TestStand Engine list of type palette files. Type palette files contain step type and data type definitions. LoadTypePaletteFiles is the method the sequence edi

### Engine.LoadTypePaletteFiles

#### Syntax

[Engine](engine.html).LoadTypePaletteFiles

#### Purpose

Note

Engine.LoadTypePaletteFilesEx

#### Remarks

Loads the TestStand Engine list of type palette files. Type palette files contain step type and data type definitions. LoadTypePaletteFiles is the method the sequence editor and user interfaces call on the TestStand Engine to load these files when they launch. You can call this method outside of the sequence editor or a user interface if an instance of the TestStand Engine has been created and the type palette files need to be loaded.

#### See Also

[Engine.GetTypePaletteFileList](engine-gettypepalettefilelist.html)

[Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)

[Engine.SetTypePaletteFileList](engine-settypepalettefilelist.html)

[Engine.UnloadTypePaletteFiles](engine-unloadtypepalettefiles.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-loadtypepalettefilesex.html language=enus -->
## TOPIC 00873: Engine.LoadTypePaletteFilesEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-loadtypepalettefilesex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-loadtypepalettefilesex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LoadTypePaletteFilesEx( handlerType = ConflictHandler_Prompt, options = 0) Purpose Loads the list of type palette files found in the TestStand Engine. Remarks Type palette files contain step type and data type definitions. LoadTypePaletteFilesEx is the method the sequence editor and us

### Engine.LoadTypePaletteFilesEx

#### Syntax

[Engine](engine.html).LoadTypePaletteFilesEx( handlerType = ConflictHandler_Prompt, options = 0)

#### Purpose

Loads the list of type palette files found in the TestStand Engine.

#### Remarks

Type palette files contain step type and data type definitions. LoadTypePaletteFilesEx is the method the sequence editor and user interfaces call on the TestStand Engine to load these files when they start up. You can call this method outside of the sequence editor or a user interface if an instance of the TestStand Engine has been created and the type palette files need to be loaded.

Note

create the TestStand Engine

#### Parameters

handlerType
 As
 [TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[In] Specifies how to handle type conflicts.

This parameter has a default value of
 ConflictHandler_Prompt
 .

options
 As
 [Long](data-types-for-teststand.html)

[In] This parameter is reserved.

This parameter has a default value of
 0
 .

#### See Also

[Creating the TestStand Engine](/csh?context=ts_tsapiref_app_creating_the_teststand_engine)

[Engine.GetTypePaletteFileList](engine-gettypepalettefilelist.html)

[Engine.SetTypePaletteFileList](engine-settypepalettefilelist.html)

[Engine.UnloadTypePaletteFiles](engine-unloadtypepalettefiles.html)

[TypeConflictHandlerTypes](typeconflicthandlertypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-localizeexpression.html language=enus -->
## TOPIC 00874: Engine.LocalizeExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-localizeexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-localizeexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LocalizeExpression( expressionString, decimalPointOption) Return Value String String containing the localized expression. Purpose Converts an expression string to conform to the localization settings for the computer. Remarks Call this method to localize an expression before you displa

### Engine.LocalizeExpression

#### Syntax

[Engine](engine.html).LocalizeExpression( expressionString, decimalPointOption)

#### Return Value

[String](data-types-for-teststand.html)

String containing the localized expression.

#### Purpose

Converts an expression string to conform to the localization settings for the computer.

#### Remarks

Call this method to localize an expression before you display it. The method replaces the periods that represent decimal points in the expression with the localized decimal point character. If the localized decimal point character is the comma character, the method also replaces commas that represent argument or expression separators with semicolons. The method does not change periods used as property field separators or any characters inside string constants.

#### Parameters

expressionString
 As
 [String](data-types-for-teststand.html)

[In] Specifies an unlocalized expression string to convert.

decimalPointOption
 As
 [DecimalPointLocalizationOptions](decimalpointlocalizationoptions.html)

[In] Constant that specifies how the method determines which character is the localized decimal point that it uses to localize the expression.

#### See Also

[DecimalPointLocalizationOptions](decimalpointlocalizationoptions.html)

[Engine.DelocalizeExpression](engine-delocalizeexpression.html)

[Engine.GetLocalizedDecimalPoint](engine-getlocalizeddecimalpoint.html)

[StationOptions.UseLocalizedDecimalPoint](stationoptions-uselocalizeddecimalpoint.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-logprofileraction.html language=enus -->
## TOPIC 00875: Engine.LogProfilerAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-logprofileraction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-logprofileraction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.LogProfilerAction( profilerMechanism, adapterKeyName, sequenceContextParam, threadId, threadDisplayName, name, synchronizationState, operation, timeout, postMessage, reserved) Return Value OutputMessage Returns the OutputMessage this method creates that stores the profiler information.

### Engine.LogProfilerAction

#### Syntax

[Engine](engine.html).LogProfilerAction( profilerMechanism, adapterKeyName, sequenceContextParam, threadId, threadDisplayName, name, synchronizationState, operation, timeout, postMessage, reserved)

#### Return Value

[OutputMessage](outputmessage.html)

Returns the OutputMessage this method creates that stores the profiler information. If you pass True to postMessage, you do not need to operate on the returned OutputMessage. The OutputMessage.Category property has a value of Engine.ProfilerOutputMessageCategoryName to indicate that it contains profiler information and should not be displayed in an output messages window.

A TestStand profiler window functions by collecting OutputMessages that have this category name and inspecting their contents.

#### Purpose

Logs the beginning, end, or a change in the state of an operation so that the information can be collected and displayed by a profiler. The method performs no action if Engine.ProfilingEnabled is not true.

#### Remarks

This method creates an OutputMessage that stores the profiler information. The built-in properties of the OutputMessage store some information, such as the source location of the event being logged and the time that it occurred. This methods adds custom sub-properties to the OutputMessage to store the remaining information. The ProfilerOutputMessageSubProperties constants define the names of these sub-properties.

#### Parameters

profilerMechanism
 As
 [String](data-types-for-teststand.html)

[In] Pass a ProfilerMechanisms constant, or a string that indicates the mechanism the profiler event is recording.

adapterKeyName
 As
 [String](data-types-for-teststand.html)

[In] Pass an adapter key name, if applicable. If this value is not null or an empty string, the method stores it as a sub-property of the OutputMessage with a name defined by ProfilerOutputMessageSubProperty_AdapterKeyName.

sequenceContextParam
 As
 [SequenceContext](sequencecontext.html)

[In] Pass the current SequenceContext, if applicable. Otherwise pass null or Nothing. This method uses the sequence context to determine location and test socket information for the source of profiler event.

threadId
 As
 [String](data-types-for-teststand.html)

[In] Pass the UniqueThreadId property of the current TestStand thread as a string. If the current thread is not a TestStand execution thread, pass the decimal formatted result of the Win32 GetCurrentThreadId function as a string with the following string appended:
 "|"

threadDisplayName
 As
 [String](data-types-for-teststand.html)

[In] Pass the DisplayName property of the current TestStand thread. If the current thread is not a TestStand execution thread, pass the result of Engine.GetResourceString("PROFILER", "NON_EXECUTION_THREAD").

name
 As
 [String](data-types-for-teststand.html)

[In] Pass the name of the item that generated the profiler event. This method stores the name as a sub-property of the OutputMessage with a name defined by ProfilerOutputMessageSubProperty_Name.

synchronizationState
 As
 [ProfilerStates](profilerstates.html)

[In] Pass an element of the ProfilerStates enumeration that describes the transition that the profiler event records. This method stores the
 profilerState
 as a numeric sub-property of the
 OutputMessage
 with a name defined by
 ProfilerOutputMessageSubProperty_State
 .

operation
 As
 [String](data-types-for-teststand.html)

[In] Pass a string that describes the operation that the profiler event is recording a transition for. If applicable, pass an element of the ProfilerOperations module. This method stores the operation as a sub-property of the OutputMessage with a name defined by ProfilerOutputMessageSubProperty_Operation.

timeout
 As
 [Double](data-types-for-teststand.html)

[In] If you pass the value of ProfilerState_Blocked to profilerState, this method stores the value you pass to timeout as a numeric sub-property of the OutputMessage with a name defined by ProfilerOutputMessageSubProperty_TimeoutPeriod.

postMessage
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether this method calls the Post method on the OutputMessage it creates. If you pass false, you must later call the Post method on the OutputMessage the method returns. Pass false if you need to add additional data to the OutputMessage before posting it.

reserved
 As
 [LPUNKNOWN](propertyvaluetypes.html)

[In] Pass Null or Nothing to this reserved parameter.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-majorversion.html language=enus -->
## TOPIC 00876: Engine.MajorVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-majorversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-majorversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.MajorVersion Data Type Long Purpose Returns the major version number for the current version of TestStand. Remarks The version number usually appears in the MajorVersion.MinorVersion.RevisionVersion format, such as 1.0.2 . See Also Engine.BuildVersion Engine.MinorVersion Engine.PatchVe

### Engine.MajorVersion

#### Syntax

[Engine](engine.html).MajorVersion

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the major version number for the current version of TestStand.

#### Remarks

The version number usually appears in the
 MajorVersion.MinorVersion.RevisionVersion
 format, such as
 1.0.2
 .

#### See Also

[Engine.BuildVersion](engine-buildversion.html)

[Engine.MinorVersion](engine-minorversion.html)

[Engine.PatchVersion](engine-patchversion.html)

[Engine.RevisionVersion](engine-revisionversion.html)

[Engine.VersionString](engine-versionstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-masterengine.html language=enus -->
## TOPIC 00877: Engine.MasterEngine

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-masterengine.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-masterengine.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.MasterEngine Data Type Object Purpose Specifies the controlling engine for remote engines. Remarks A TestStand Engine must set this property. National Instruments recommends not setting this property manually. When TestStand executes sequences on a remote computer, it creates an instan

### Engine.MasterEngine

#### Syntax

[Engine](engine.html).MasterEngine

#### Data Type

[Object](data-types-for-teststand.html)

#### Purpose

Specifies the controlling engine for remote engines.

#### Remarks

Note

When TestStand executes sequences on a remote computer, it creates an instance of the TestStand Engine on the remote computer and sets this property on the remote engine to refer back to the controlling engine. If this engine is a remote engine, you can use this property to access the engine on the other computer.

#### See Also

[Engine.IsRemote](engine-isremote.html)

[StationOptions.AllowSequenceCallsFromRemoteMachine](stationoptions-allowsequencecallsfromremotema.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-minorversion.html language=enus -->
## TOPIC 00878: Engine.MinorVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-minorversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-minorversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.MinorVersion Data Type Long Purpose Returns the minor version number for the current version of TestStand. Remarks The version number usually appears in the MajorVersion.MinorVersion.RevisionVersion format, such as 1.0.2 . Prior to TestStand 2016, the revision version sometimes indicat

### Engine.MinorVersion

#### Syntax

[Engine](engine.html).MinorVersion

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the minor version number for the current version of TestStand.

#### Remarks

The version number usually appears in the
 MajorVersion.MinorVersion.RevisionVersion
 format, such as
 1.0.2
 .

Note

Engine.MinorVersion

Engine.RevisionVersion

#### See Also

[Engine.BuildVersion](engine-buildversion.html)

[Engine.MajorVersion](engine-majorversion.html)

[Engine.PatchVersion](engine-patchversion.html)

[Engine.RevisionVersion](engine-revisionversion.html)

[Engine.VersionString](engine-versionstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newcsvfileinputrecordstream.html language=enus -->
## TOPIC 00879: Engine.NewCsvFileInputRecordStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newcsvfileinputrecordstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newcsvfileinputrecordstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewCsvFileInputRecordStream( absolutePath) Return Value CsvFileInputRecordStream Purpose Create a new CsvFileInputRecordStream for the specified file. Remarks When the returned CsvFileInputRecordStream is no longer needed, it should be closed by calling CsvFileInputRecordStream.Close .

### Engine.NewCsvFileInputRecordStream

#### Syntax

[Engine](engine.html).NewCsvFileInputRecordStream( absolutePath)

#### Return Value

[CsvFileInputRecordStream](csvfileinputrecordstream.html)

#### Purpose

Create a new
 CsvFileInputRecordStream
 for the specified file.

#### Remarks

When the returned
 CsvFileInputRecordStream
 is no longer needed, it should be closed by calling
 CsvFileInputRecordStream.Close
 . If it is not closed already, the stream closes automatically when the last reference to it is removed.

#### Parameters

absolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path to the CSV file.

#### See Also

[CsvFileInputRecordStream](csvfileinputrecordstream.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newcsvfileoutputrecordstream.html language=enus -->
## TOPIC 00880: Engine.NewCsvFileOutputRecordStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newcsvfileoutputrecordstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newcsvfileoutputrecordstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewCsvFileOutputRecordStream( absolutePath, openMode) Return Value CsvFileOutputRecordStream Purpose Create a new CsvFileOutputRecordStream for the specified file. Remarks When the returned CsvFileOutputRecordStream is no longer needed, it should be closed by calling OutputRecordStream

### Engine.NewCsvFileOutputRecordStream

#### Syntax

[Engine](engine.html).NewCsvFileOutputRecordStream( absolutePath, openMode)

#### Return Value

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html)

#### Purpose

Create a new
 CsvFileOutputRecordStream
 for the specified file.

#### Remarks

When the returned
 CsvFileOutputRecordStream
 is no longer needed, it should be closed by calling
 [OutputRecordStream.Close](outputrecordstream-close.html)
 . If it is not closed already, the stream closes automatically when the last reference to it is removed.

#### Parameters

absolutePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path to the CSV file.

openMode
 As
 [Long](data-types-for-teststand.html)

[In] Specifies how to open the CSV file. Supported options include:

- FileOpenMode_NoOptions 
 - Create the file if it does not exist. Fail with a run-time error if the file exists.
- FileOpenMode_Truncate 
 - If the file exists, overwrite it deleting the previous contents. Create a new file if it does not exist.
- FileOpenMode_Append 
 - If the file exists, append to the end of it, preserving the existing contents. Create a new file if it does not exist.
- FileOpenMode_Uniquify 
 - Create a new file if it does not exist. If a file with the specified path exists, attempt to make the file name unique by appending "_" (underscore) plus a numeric suffix to the file name. For example, if
 AlreadyExists.csv 
 already exists,
 AlreadyExists_2.csv 
 is tried, then
 AlreadyExists_3.csv 
 , etc. until a unique name has been found. If a unique name is not found after 10000 attempts, the method fails and throws a runtime error.

#### See Also

[CsvFileOutputRecordStream](csvfileoutputrecordstream.html)

[OutputRecordStream.Close](outputrecordstream-close.html)

[FileOpenModes](fileopenmodes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newdatatype.html language=enus -->
## TOPIC 00881: Engine.NewDataType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newdatatype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newdatatype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewDataType( ValueType, asArray, typeNameParam, options) Return Value PropertyObject The newly created data type. Purpose Creates and returns a new TestStand data type. Remarks This method creates a PropertyObject object that is a data type. Once you create a data type, you can use the

### Engine.NewDataType

#### Syntax

[Engine](engine.html).NewDataType( ValueType, asArray, typeNameParam, options)

#### Return Value

[PropertyObject](propertyobject.html)

The newly created data type.

#### Purpose

Creates and returns a new TestStand data type.

#### Remarks

This method creates a PropertyObject object that is a data type. Once you create a data type, you can use the
 [Engine.NewPropertyObject](engine-newpropertyobject.html)
 method to create an instance of the type. You can add the type to a
 [TypeUsageList](typeusagelist.html)
 to associate the type with a particular
 [PropertyObjectFile](propertyobjectfile.html)
 .

Note

TypeUsageList.ValidateNewTypeName

#### Parameters

ValueType
 As
 [PropertyValueTypes](propertyvaluetypes.html)

[In] Specifies the type of value you want instances of the type to contain.

asArray
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want the type to be an array.

typeNameParam
 As
 [String](data-types-for-teststand.html)

[In] If you pass
 [PropValType_NamedType](namedpropertytypes.html)
 for the ValueType, pass the name of the type for this parameter. Otherwise, pass an empty string. If you pass a type name, the type must not already be in memory.

options
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 to specify the default behavior, or pass one or more
 [PropertyOptions](propertyoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options.

#### See Also

[Engine.NewPropertyObject](engine-newpropertyobject.html)

[NamedPropertyTypes](namedpropertytypes.html)

[PropertyObject](propertyobject.html)

[PropertyObjectFile](propertyobjectfile.html)

[PropertyOptions](propertyoptions.html)

[PropertyValueTypes](propertyvaluetypes.html)

[TypeUsageList](typeusagelist.html)

[TypeUsageList.ValidateNewTypeName](typeusagelist-validatenewtypename.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-neweditargs.html language=enus -->
## TOPIC 00882: Engine.NewEditArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-neweditargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-neweditargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewEditArgs Return Value EditArgs Purpose Creates and returns an EditArgs object. Remarks You can pass the object this method returns as a parameter to one of the following methods: Engine.NewExecution , Engine.NewHierarchicalExecution , Engine.GetEditTimeToolMenuItems , Engine.GetRunT

### Engine.NewEditArgs

#### Syntax

[Engine](engine.html).NewEditArgs

#### Return Value

[EditArgs](editargs.html)

#### Purpose

Creates and returns an EditArgs object.

#### Remarks

You can pass the object this method returns as a parameter to one of the following methods:
 [Engine.NewExecution](engine-newexecution.html)
 ,
 [Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)
 ,
 [Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)
 ,
 [Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)
 ,
 [Engine.NewEditContext](engine-neweditcontext.html)
 ,
 [Sequence.EvalEntryPointNameExpressionEx](sequence-evalentrypointnameexpressionex.html)
 ,
 [Sequence.EvalEntryPointEnabledExpressionEx](sequence-evalentrypointenabledexpressionex.html)
 , and
 [RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)
 .

#### See Also

[EditArgs](editargs.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[Engine.NewExecution](engine-newexecution.html)

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

[RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)

[Sequence.EvalEntryPointEnabledExpressionEx](sequence-evalentrypointenabledexpressionex.html)

[Sequence.EvalEntryPointNameExpressionEx](sequence-evalentrypointnameexpressionex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-neweditcontext.html language=enus -->
## TOPIC 00883: Engine.NewEditContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-neweditcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-neweditcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewEditContext( obj, [editArgsParam], [locationString]) Return Value SequenceContext A reference to a SequenceContext object. Release this reference when you are finished using it. Purpose Returns a SequenceContext object that approximates the sequence context TestStand creates when yo

### Engine.NewEditContext

#### Syntax

[Engine](engine.html).NewEditContext( obj, [editArgsParam], [locationString])

#### Return Value

[SequenceContext](sequencecontext.html)

A reference to a SequenceContext object. Release this reference when you are finished using it.

#### Purpose

Returns a SequenceContext object that approximates the sequence context TestStand creates when you run a sequence.

#### Remarks

You can pass the object this method returns as a parameter to the
 [Engine.DisplayBrowseExprDialogEx](engine-displaybrowseexprdialogex.html)
 and
 [Engine.DisplayBrowsePropertyObjectDialog](engine-displaybrowsepropertyobjectdialog.html)
 methods.

When you pass an array of step references, this method returns a context with a
 [Step](step.html)
 property that represents multiple steps, where the subproperties of Step contain only properties common to all steps in the array. Use the context with
 [SequenceContext.GetMultipleValues](sequencecontext-getmultiplevalues.html)
 to determine whether an element of the property, such as the value, comment, format, or flags, represents the shared element value for all the steps in the array. If at least one step has a different value for an element, the property element in the context contains a default value.

#### Parameters

obj
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the object to initialize the sequence context. You can pass a sequence file, sequence, step, variable, or array of object references to steps. This method sets the sequence context properties that correspond to the object you pass.

editArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an
 [EditArgs](editargs.html)
 object that indicates which items are currently selected in the user interface.

locationString
 As
 [Variant](data-types-for-teststand.html)

[Out] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Returns the lookupString for the object passed in. Use this lookupString to access the object from the sequence context.

#### See Also

[Engine.DisplayBrowseExprDialogEx](engine-displaybrowseexprdialogex.html)

[Engine.DisplayBrowsePropertyObjectDialog](engine-displaybrowsepropertyobjectdialog.html)

[EditArgs](editargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[PropertyObject](propertyobject.html)

[SequenceContext](sequencecontext.html)

[SequenceContext.GetMultipleValues](sequencecontext-getmultiplevalues.html)

[SequenceFile.NewEditContext](sequencefile-neweditcontext.html)

[Step](step.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newevaluationtypes.html language=enus -->
## TOPIC 00884: Engine.NewEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewEvaluationTypes( initialPropertyValueTypes = -1) Return Value EvaluationTypes Purpose Creates and returns a new EvaluationTypes object. Parameters initialPropertyValueTypes As Long [In] Specifies the value for the EvaluationTypes.PropertyValueTypeFlags property on the object this me

### Engine.NewEvaluationTypes

#### Syntax

[Engine](engine.html).NewEvaluationTypes( initialPropertyValueTypes = -1)

#### Return Value

[EvaluationTypes](evaluationtypes.html)

#### Purpose

Creates and returns a new
 [EvaluationTypes](evaluationtypes.html)
 object.

#### Parameters

initialPropertyValueTypes
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value for the
 [EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)
 property on the object this method returns.

This parameter has a default value of
 -1
 .

#### See Also

[EvaluationTypes](evaluationtypes.html)

[EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newexecution.html language=enus -->
## TOPIC 00885: Engine.NewExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewExecution( sequenceFileParam, sequenceNameParam, processModelParam, breakAtFirstStep, executionTypeMaskParam, [sequenceArgsParam], [editArgsParam], [InteractiveArgsParam]) Return Value Execution Purpose Creates and returns a new Execution object. Remarks When you call this method, t

### Engine.NewExecution

#### Syntax

[Engine](engine.html).NewExecution( sequenceFileParam, sequenceNameParam, processModelParam, breakAtFirstStep, executionTypeMaskParam, [sequenceArgsParam], [editArgsParam], [InteractiveArgsParam])

#### Return Value

[Execution](execution.html)

#### Purpose

Creates and returns a new Execution object.

#### Remarks

When you call this method, the execution begins immediately.

Sequence editor and user interface programs use this method to run sequences.

You can pass parameters as arguments to this method when executing an
 
 [entry point](/csh?context=ts_tsapiref_app_process_model_entry_points)
 or
 
 [sequence](/csh?context=ts_tsapiref_app_executing_a_sequence)
 .

#### Parameters

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the SequenceFile object that contains the sequence to execute. If the execution uses a process model, pass the client SequenceFile object.

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the sequence or Process Model entry point to execute.

processModelParam
 As
 [SequenceFile](sequencefile.html)

[In] Pass the process model SequenceFile object if you want to execute a Process Model entry point. Otherwise, a
 NULL
 object reference in LabVIEW,
 0
 in LabWindows/CVI, or the
 Nothing
 keyword in Visual Basic, pass a
 NULL
 dispatch pointer in Microsoft Foundation Classes.

breakAtFirstStep
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to suspend execution before executing the first step.

executionTypeMaskParam
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for the default behavior or pass one or more
 [ExecutionTypeMask](executiontypemask.html)
 constants. Use the bitwise-OR operator to pass multiple constants.

sequenceArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a PropertyObject object that contains the arguments to the sequence you want to execute. Each subproperty of the PropertyObject object represents a parameter to the sequence. The subproperties must appear in the same order as the sequence parameters.

editArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an
 [EditArgs](editargs.html)
 object that indicates which items are currently selected in the user interface. This is required only for Process Model entry points.

InteractiveArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an
 [InteractiveArgs](interactiveargs.html)
 object that indicates which steps are currently selected in the user interface and contains looping information necessary for an interactive execution. Pass this parameter only for interactive executions.

#### See Also

[EditArgs](editargs.html)

[Engine.NewEditArgs](engine-neweditargs.html)

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

[Engine.NewInteractiveArgs](engine-newinteractiveargs.html)

[Executing a Sequence](/csh?context=ts_tsapiref_app_executing_a_sequence)

[Execution](execution.html)

[ExecutionTypeMask](executiontypemask.html)

[InteractiveArgs](interactiveargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Process Model Entry Points](/csh?context=ts_tsapiref_app_process_model_entry_points)

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newexpression.html language=enus -->
## TOPIC 00886: Engine.NewExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewExpression Return Value Expression Purpose Creates and returns an Expression object. See Also Expression

### Engine.NewExpression

#### Syntax

[Engine](engine.html).NewExpression

#### Return Value

[Expression](expression.html)

#### Purpose

Creates and returns an Expression object.

#### See Also

[Expression](expression.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newhierarchicalexecution.html language=enus -->
## TOPIC 00887: Engine.NewHierarchicalExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newhierarchicalexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newhierarchicalexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewHierarchicalExecution( sequenceCallSteps, hierarchicalExecutionFlags, sequenceFileParam, sequenceNameParam, processModelParam, breakAtFirstStep, executionTypeMaskParam, [sequenceArgsParam], [editArgsParam], [InteractiveArgsParam]) Return Value Execution Purpose Creates and returns a

### Engine.NewHierarchicalExecution

#### Syntax

[Engine](engine.html).NewHierarchicalExecution( sequenceCallSteps, hierarchicalExecutionFlags, sequenceFileParam, sequenceNameParam, processModelParam, breakAtFirstStep, executionTypeMaskParam, [sequenceArgsParam], [editArgsParam], [InteractiveArgsParam])

#### Return Value

[Execution](execution.html)

#### Purpose

Creates and returns a new Execution object.

#### Remarks

Use a hierarchical execution to specify a call stack of Sequence Call steps that only execute the setup and Cleanup steps of sequences in the call stack while continuing normal execution in the sequence that the last Sequence Call step specifies.

To specify the call stack to create, pass an array of Sequence Call steps to the
 sequenceCallSteps
 parameter. When the hierarchical execution starts, TestStand executes the sequence the
 sequenceName
 parameter specifies, just as TestStand does when you call the
 [Engine.NewExecution](engine-newexecution.html)
 method. When the execution reaches the sequence that contains the first Sequence Call step the
 sequenceCallSteps
 parameter specifies, the execution follows the execution path the array of Sequence Call steps defines. The execution does not execute any of the Main steps in the sequences of the call stack, but the
 hierarchicalExecutionFlags
 parameter specifies whether the execution executes the setup and Cleanup steps in the sequences of the call stack. Execution resumes normally in the sequence that the last Sequence Call step in the array calls. Even though the steps in the Main step group of the sequences that contain the Sequence Call steps do not execute, local variables propagate normally according to their propagation settings.

#### Parameters

sequenceCallSteps
 As
 [Object Array](data-types-for-teststand.html)

[In] Specifies an array of Sequence Call steps. The array represents a call stack to recreate. The execution does not execute any of the main steps in the sequences of the call stack, but the
 hierarchicalExecutionFlags
 parameter specifies whether the execution executes the setup and cleanup steps in the sequences of the call stack. Except for the first step, each step in the array is a step that resides in the sequence the previous step in the array calls.

hierarchicalExecutionFlags
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for the default behavior or pass one or more
 [HierarchicalExecutionFlags](hierarchicalexecutionflags.html)
 constants. Use the bitwise-OR operator to pass multiple constants.

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the SequenceFile object that contains the sequence to execute. If the execution uses a process model, pass the client SequenceFile object.

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the sequence or Process Model entry point to execute.

processModelParam
 As
 [SequenceFile](sequencefile.html)

[In] Pass the process model SequenceFile object if you want to execute a Process Model entry point. Otherwise, a
 NULL
 object reference in LabVIEW,
 0
 in LabWindows/CVI, or the
 Nothing
 keyword in Visual Basic, pass a
 NULL
 dispatch pointer in Microsoft Foundation Classes.

breakAtFirstStep
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to suspend execution before executing the first step.

executionTypeMaskParam
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for the default behavior or pass one or more
 [ExecutionTypeMask](executiontypemask.html)
 constants. Use the bitwise-OR operator to pass multiple constants.

sequenceArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a PropertyObject object that contains the arguments to the sequence you want to execute. Each subproperty of the PropertyObject object represents a parameter to the sequence. The subproperties must appear in the same order as the sequence parameters.

editArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an
 [EditArgs](editargs.html)
 object that indicates which items are currently selected in the user interface. This is required only for Process Model entry points.

InteractiveArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies an
 [InteractiveArgs](interactiveargs.html)
 object that indicates which steps are currently selected in the user interface and contains looping information necessary for an interactive execution. Pass this parameter for interactive executions only.

#### See Also

[EditArgs](editargs.html)

[Engine.NewEditArgs](engine-neweditargs.html)

[Engine.NewExecution](engine-newexecution.html)

[Engine.NewInteractiveArgs](engine-newinteractiveargs.html)

[Execution](execution.html)

[ExecutionTypeMask](executiontypemask.html)

[HierarchicalExecutionFlags](hierarchicalexecutionflags.html)

[InteractiveArgs](interactiveargs.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newinteractiveargs.html language=enus -->
## TOPIC 00888: Engine.NewInteractiveArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newinteractiveargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newinteractiveargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewInteractiveArgs Return Value InteractiveArgs Purpose Creates and returns an InteractiveArgs object. Remarks You can pass the object this method returns as a parameter to one of the following methods: Engine.NewExecution , Engine.NewHierarchicalExecution , or Thread.DoInteractiveExec

### Engine.NewInteractiveArgs

#### Syntax

[Engine](engine.html).NewInteractiveArgs

#### Return Value

[InteractiveArgs](interactiveargs.html)

#### Purpose

Creates and returns an InteractiveArgs object.

#### Remarks

You can pass the object this method returns as a parameter to one of the following methods:
 [Engine.NewExecution](engine-newexecution.html)
 ,
 [Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)
 , or
 [Thread.DoInteractiveExecution](thread-dointeractiveexecution.html)
 .

#### See Also

[EditArgs](editargs.html)

[Engine.NewExecution](engine-newexecution.html)

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

[InteractiveArgs](interactiveargs.html)

[Thread.DoInteractiveExecution](thread-dointeractiveexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newlocations.html language=enus -->
## TOPIC 00889: Engine.NewLocations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newlocations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newlocations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewLocations Return Value Locations Purpose Creates and returns a new Locations object. See Also Locations

### Engine.NewLocations

#### Syntax

[Engine](engine.html).NewLocations

#### Return Value

[Locations](locations.html)

#### Purpose

Creates and returns a new Locations object.

#### See Also

[Locations](locations.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newoutputmessage.html language=enus -->
## TOPIC 00890: Engine.NewOutputMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newoutputmessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newoutputmessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewOutputMessage( messageText, categoryText = "", severity = OutputMessageSeverity_Information, sequenceContext = NULL) Return Value OutputMessage Purpose Creates and returns a new OutputMessage object. Remarks When creating a new object, TestStand initializes the OutputMessage.TimeSta

### Engine.NewOutputMessage

#### Syntax

[Engine](engine.html).NewOutputMessage( messageText, categoryText = "", severity = OutputMessageSeverity_Information, sequenceContext = NULL)

#### Return Value

[OutputMessage](outputmessage.html)

#### Purpose

Creates and returns a new
 [OutputMessage](outputmessage.html)
 object.

#### Remarks

When creating a new object, TestStand initializes the
 [OutputMessage.TimeStamp](outputmessage-timestamp.html)
 property to the current time, sets the
 [OutputMessage.TextColor](outputmessage-textcolor.html)
 property to black, and sets the
 [OutputMessage.IconName](outputmessage-iconname.html)
 property based on the severity.

You must call the
 [OutputMessage.Post](outputmessage-post.html)
 method to copy the message to the collection the
 [Engine.GetOutputMessages](engine-getoutputmessages.html)
 method returns.

#### Parameters

messageText
 As
 [String](data-types-for-teststand.html)

[In] Specifies the message text.

categoryText
 As
 [String](data-types-for-teststand.html)

[In] Specifies the category of the message. Applications typically use the category to filter or sort messages. If you do not specify a category, the output message is considered uncategorized. You can specify any value for this parameter.

This parameter has a default value of
 ""
 .

severity
 As
 [OutputMessageSeverityTypes](outputmessageseveritytypes.html)

[In/Out] Specifies the severity of the output message.

This parameter has a default value of
 OutputMessageSeverity_Information
 .

sequenceContext
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context of the current execution, if available. TestStand extracts information from the sequence context to construct the
 [OutputMessage.FileLocations](outputmessage-filelocations.html)
 and
 [OutputMessage.ExecutionLocations](outputmessage-executionlocations.html)
 properties for the new object.

This parameter has a default value of
 NULL
 .

#### See Also

[Engine.GetOutputMessages](engine-getoutputmessages.html)

[Engine.NewOutputMessages](engine-newoutputmessages.html)

[Output Messages (Example)](/csh?context=ts_8127)

[OutputMessage](outputmessage.html)

[OutputMessage.ExecutionLocations](outputmessage-executionlocations.html)

[OutputMessage.FileLocations](outputmessage-filelocations.html)

[OutputMessage.IconName](outputmessage-iconname.html)

[OutputMessage.Post](outputmessage-post.html)

[OutputMessage.TextColor](outputmessage-textcolor.html)

[OutputMessage.TimeStamp](outputmessage-timestamp.html)

[OutputMessageSeverityTypes](outputmessageseveritytypes.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newoutputmessages.html language=enus -->
## TOPIC 00891: Engine.NewOutputMessages

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newoutputmessages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newoutputmessages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewOutputMessages Return Value OutputMessages Purpose Returns a reference to a new OutputMessages object. This collection is initially empty. Remarks An application typically creates a new OutputMessages object to collect the output messages the application must process or display. The

### Engine.NewOutputMessages

#### Syntax

[Engine](engine.html).NewOutputMessages

#### Return Value

[OutputMessages](outputmessages.html)

#### Purpose

Returns a reference to a new
 [OutputMessages](outputmessages.html)
 object. This collection is initially empty.

#### Remarks

An application typically creates a new OutputMessages object to collect the output messages the application must process or display. The application receives output messages by handling the
 UIMsg_OutputMessages
 event and copying the output messages from the collection stored in the
 [UIMessage.ActiveXData](uimessage-activexdata.html)
 property into a private collection.

#### See Also

[OutputMessages](outputmessages.html)

[UIMessage.ActiveXData](uimessage-activexdata.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newpropertyobject.html language=enus -->
## TOPIC 00892: Engine.NewPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newpropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newpropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewPropertyObject( ValueType, asArray, typeNameParam, options) Return Value PropertyObject Purpose Creates and returns a new PropertyObject object. Remarks TestStand does not validate property names you create programmatically for invalid characters, such as spaces, which can result in

### Engine.NewPropertyObject

#### Syntax

[Engine](engine.html).NewPropertyObject( ValueType, asArray, typeNameParam, options)

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Creates and returns a new PropertyObject object.

#### Remarks

TestStand does not validate property names you create programmatically for invalid characters, such as spaces, which can result in errors when you use expressions. Use the
 [PropertyObject.ValidateNewName](propertyobject-validatenewname.html)
 ,
 [PropertyObject.ValidateNewSubPropertyName](propertyobject-validatenewsubpropertyname.html)
 , or
 [PropertyObject.ValidateNewElementName](propertyobject-validatenewelementname.html)
 methods to validate property names. TestStand expressions require PropertyObject names to be strings that contain only letters, numbers, and underscores. PropertyObject names cannot contain spaces, start with a number, or be empty.

Additionally, the PropertyObject name cannot be
 Value
 , and you cannot have duplicate subproperty names.

For example,
 MyVariableName_2000
 is a valid PropertyObject name.

Names of elements in a PropertyObject array can contain any character. Both sequence names and step names are examples of such named array elements. However, sequence names cannot be empty or contain control characters. You cannot have duplicate sequence names. The name
 NI
 is reserved at the root level for attributes.

#### Parameters

ValueType
 As
 [PropertyValueTypes](propertyvaluetypes.html)

[In] Specifies the type of value you want the property to contain.

asArray
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want the property value to be an array.

typeNameParam
 As
 [String](data-types-for-teststand.html)

[In] If you pass
 PropValType_NamedType
 for the
 ValueType
 parameter, pass the name of the type for this parameter. Otherwise, pass an empty string. If you pass a type name, the type must already be in memory. Refer to
 [NamedPropertyTypes](namedpropertytypes.html)
 for a list of built-in name types.

options
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 to specify the default behavior, or pass one or more
 [PropertyOptions](propertyoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options.

#### See Also

[NamedPropertyTypes](namedpropertytypes.html)

[PropertyObject](propertyobject.html)

[PropertyObject.ValidateNewElementName](propertyobject-validatenewelementname.html)

[PropertyObject.ValidateNewName](propertyobject-validatenewname.html)

[PropertyObject.ValidateNewSubPropertyName](propertyobject-validatenewsubpropertyname.html)

[PropertyOptions](propertyoptions.html)

[PropertyValueTypes](propertyvaluetypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newpropertyobjectfile.html language=enus -->
## TOPIC 00893: Engine.NewPropertyObjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newpropertyobjectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newpropertyobjectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewPropertyObjectFile( fileType) Return Value PropertyObjectFile Purpose Creates and returns a new PropertyObjectFile object. Remarks Use this method to create type palette files, workspace files, project files, sequence files, and generic property object files. You cannot create a use

### Engine.NewPropertyObjectFile

#### Syntax

[Engine](engine.html).NewPropertyObjectFile( fileType)

#### Return Value

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Creates and returns a new PropertyObjectFile object.

#### Remarks

Use this method to create type palette files, workspace files, project files, sequence files, and generic property object files. You cannot create a users file, configuration file, or a station globals file using this method.

#### Parameters

fileType
 As
 [PropertyObjectFileTypes](propertyobjectfiletypes.html)

[In] Specifies the type of file to create.

#### See Also

[Engine.NewSequenceFile](engine-newsequencefile.html)

[Engine.NewWorkspaceFile](engine-newworkspacefile.html)

[PropertyObjectFile](propertyobjectfile.html)

[PropertyObjectFileTypes](propertyobjectfiletypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newpropertyobjecttype.html language=enus -->
## TOPIC 00894: Engine.NewPropertyObjectType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newpropertyobjecttype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newpropertyobjecttype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewPropertyObjectType( ValueType, TypeName = "", ElementType = NULL, IsObject = True) Return Value PropertyObjectType Purpose Creates and returns a new PropertyObjectType object. Remarks You can use this method to create an object to assign to the AdditionalResult.Type property. Parame

### Engine.NewPropertyObjectType

#### Syntax

[Engine](engine.html).NewPropertyObjectType( ValueType, TypeName = "", ElementType = NULL, IsObject = True)

#### Return Value

[PropertyObjectType](propertyobjecttype.html)

#### Purpose

Creates and returns a new
 [PropertyObjectType](propertyobjecttype.html)
 object.

#### Remarks

You can use this method to create an object to assign to the
 [AdditionalResult.Type](additionalresult-type.html)
 property.

#### Parameters

ValueType
 As
 [PropertyValueTypes](propertyvaluetypes.html)

[In] Specifies the value of the
 [PropertyObjectType.ValueType](propertyobjecttype-valuetype.html)
 property of the object this method creates. If you pass
 PropValType_NamedType
 , this method uses the type you specify with the
 TypeName
 parameter to determine the values of the properties of the
 PropertyObjectType
 object this method creates.

TypeName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the value of the
 [PropertyObjectType.TypeName](propertyobjecttype-typename.html)
 property of the object this method creates. If you pass
 PropValType_NamedType
 for the
 ValueType
 parameter, pass the name of a currently loaded type. Otherwise, pass an empty string. If you specify a type name, this method uses the type you specify to determine the values of the properties of the
 PropertyObjectType
 object this method creates instead of the other parameters you pass to this method.

This parameter has a default value of
 ""
 .

ElementType
 As
 [PropertyObjectType](propertyobjecttype.html)

[In] Specifies the value of the
 [PropertyObjectType.ElementType](propertyobjecttype-elementtype.html)
 property of the object this method creates. Pass a
 PropertyObjectType
 object if you pass
 PropValType_Array
 for the
 ValueType
 parameter. Otherwise, pass
 NULL
 . Typically, you make another call to this method to create an object to pass for this parameter.

This parameter has a default value of
 NULL
 .

IsObject
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies the value of the
 [PropertyObjectType.IsObject](propertyobjecttype-isobject.html)
 property of the object this method creates. Pass
 False
 for this parameter only to create an object for the type of an element of an array of numbers, Boolean values, strings, or references.

This parameter has a default value of
 True
 .

#### See Also

[PropertyObjectType](propertyobjecttype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newresultlog.html language=enus -->
## TOPIC 00895: Engine.NewResultLog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newresultlog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newresultlog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewResultLog Return Value ResultLog Purpose Creates and returns a new ResultLog object.

### Engine.NewResultLog

#### Syntax

[Engine](engine.html).NewResultLog

#### Return Value

[ResultLog](resultlog.html)

#### Purpose

Creates and returns a new
 [ResultLog](resultlog.html)
 object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newresultlogger.html language=enus -->
## TOPIC 00896: Engine.NewResultLogger

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newresultlogger.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newresultlogger.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewResultLogger Return Value ResultLogger Purpose Creates and returns a new ResultLogger object.

### Engine.NewResultLogger

#### Syntax

[Engine](engine.html).NewResultLogger

#### Return Value

[ResultLogger](resultlogger.html)

#### Purpose

Creates and returns a new
 [ResultLogger](resultlogger.html)
 object.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newsequence.html language=enus -->
## TOPIC 00897: Engine.NewSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newsequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newsequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewSequence Return Value Sequence Purpose Creates and returns a new Sequence object. Remarks Pass the new Sequence object to the SequenceFile.InsertSequenceEx method to add a sequence to a sequence file. TestStand does not validate sequence names you create programmatically for invalid

### Engine.NewSequence

#### Syntax

[Engine](engine.html).NewSequence

#### Return Value

[Sequence](sequence.html)

#### Purpose

Creates and returns a new Sequence object.

#### Remarks

Pass the new Sequence object to the
 [SequenceFile.InsertSequenceEx](sequencefile-insertsequenceex.html)
 method to add a sequence to a sequence file.

Note

PropertyObject.ValidateNewElementName

#### See Also

[PropertyObject.ValidateNewElementName](propertyobject-validatenewelementname.html)

[Sequence](sequence.html)

[SequenceFile.InsertSequenceEx](sequencefile-insertsequenceex.html)

[SequenceFile.RemoveSequence](sequencefile-removesequence.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newsequencefile.html language=enus -->
## TOPIC 00898: Engine.NewSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewSequenceFile Return Value SequenceFile Purpose Creates and returns a new SequenceFile object. Remarks Call the Engine.ReleaseSequenceFileEx method on this object before you release it. This method stores the new sequence file in the internal cache of the engine and adds a load refer

### Engine.NewSequenceFile

#### Syntax

[Engine](engine.html).NewSequenceFile

#### Return Value

[SequenceFile](sequencefile.html)

#### Purpose

Creates and returns a new SequenceFile object.

#### Remarks

Call the
 [Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)
 method on this object before you release it.

This method stores the new sequence file in the internal cache of the engine and adds a load reference to the sequence file. TestStand uses the load reference count to determine when to unload the sequence file from the internal cache of the engine. In addition to this method, the
 [SequenceFile.AddLoadReference](sequencefile-addloadreference.html)
 and
 [Engine.GetSequenceFileEx](engine-getsequencefileex.html)
 methods add a load reference to the sequence file. The
 Engine.ReleaseSequenceFileEx
 method removes a load reference.

You must call
 Engine.ReleaseSequenceFileEx
 for each load reference you add to the sequence file. When you release the last load reference, TestStand unloads the file from the internal cache of the engine. While unloading the file from the internal cache of the engine, TestStand executes the SequenceFileUnload callback sequence, if applicable.

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.NewPropertyObjectFile](engine-newpropertyobjectfile.html)

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[SequenceFile](sequencefile.html)

[SequenceFile.AddLoadReference](sequencefile-addloadreference.html)

[SequenceFile.Save](sequencefile-save.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newstep.html language=enus -->
## TOPIC 00899: Engine.NewStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewStep( adapterKeyNameVal, stepTypeName) Return Value Step Purpose Creates and returns a new Step object. Remarks Pass the new Step object to the Sequence.InsertStep method to add a step to a sequence. When you use this method to create a new Step object, the step name is empty. You c

### Engine.NewStep

#### Syntax

[Engine](engine.html).NewStep( adapterKeyNameVal, stepTypeName)

#### Return Value

[Step](step.html)

#### Purpose

Creates and returns a new Step object.

#### Remarks

Pass the new Step object to the
 [Sequence.InsertStep](sequence-insertstep.html)
 method to add a step to a sequence.

When you use this method to create a new
 Step
 object, the step name is empty. You can use the following code snippet to set the default name of the new step:

Step.Name = Step.StepType.AsPropertyObject.EvaluateEx(Step.StepType.DefaultNameExpr, EvalOption_DoNotAlterValues).GetValString("", 0)

Note

PropertyObject.ValidateNewElementName

#### Parameters

adapterKeyNameVal
 As
 [String](data-types-for-teststand.html)

[In] Specifies the key name of the module Adapter object to use to create the step. Pass an empty string to use the adapter the step type designates or, if the step has no designated adapter, to use the adapter the
 [Engine.DefaultAdapter](engine-defaultadapter.html)
 property specifies.

stepTypeName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the
 [step type](steptypes.html)
 with which to create the step. The step type must already be in memory. The sequence editor and custom user interfaces load step types into memory when calling the
 [Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)
 method or when loading a sequence file from disk. To create a new step type, use the
 [Engine.NewStepType](engine-newsteptype.html)
 method.

#### See Also

[AdapterKeyNames](adapterkeynames.html)

[Engine.DefaultAdapter](engine-defaultadapter.html)

[Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)

[Engine.NewStepType](engine-newsteptype.html)

[PropertyObject.ValidateNewElementName](propertyobject-validatenewelementname.html)

[Sequence.InsertStep](sequence-insertstep.html)

[Sequence.RemoveStep](sequence-removestep.html)

[Step](step.html)

[Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)

[StepTypes](steptypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newsteptype.html language=enus -->
## TOPIC 00900: Engine.NewStepType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newsteptype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newsteptype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewStepType Return Value StepType Purpose Creates and returns a new StepType object. Remarks You must specify the name of the new step type by setting the StepType.Name property. You can add the type to a TypeUsageList object to associate the type with a particular PropertyObjectFile o

### Engine.NewStepType

#### Syntax

[Engine](engine.html).NewStepType

#### Return Value

[StepType](steptype.html)

#### Purpose

Creates and returns a new StepType object.

#### Remarks

You must specify the name of the new step type by setting the
 [StepType.Name](steptype-name.html)
 property. You can add the type to a
 [TypeUsageList](typeusagelist.html)
 object to associate the type with a particular
 [PropertyObjectFile](propertyobjectfile.html)
 object. Once you create the step type, you can use the
 [Engine.NewStep](engine-newstep.html)
 method to create an instance of the type.

Note

TypeUsageList.ValidateNewTypeName

#### See Also

[Engine.NewStep](engine-newstep.html)

[PropertyObjectFile](propertyobjectfile.html)

[StepType](steptype.html)

[StepType.Name](steptype-name.html)

[TypeUsageList](typeusagelist.html)

[TypeUsageList.ValidateNewTypeName](typeusagelist-validatenewtypename.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newtypeusagelist.html language=enus -->
## TOPIC 00901: Engine.NewTypeUsageList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newtypeusagelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newtypeusagelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewTypeUsageList( reservedParam) Return Value TypeUsageList Purpose Creates and returns a new TypeUsageList. Parameters reservedParam As Long [In] Pass 0 . See Also TypeUsageList

### Engine.NewTypeUsageList

#### Syntax

[Engine](engine.html).NewTypeUsageList( reservedParam)

#### Return Value

[TypeUsageList](typeusagelist.html)

#### Purpose

Creates and returns a new TypeUsageList.

#### Parameters

reservedParam
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 .

#### See Also

[TypeUsageList](typeusagelist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newundoitemcreator.html language=enus -->
## TOPIC 00902: Engine.NewUndoItemCreator

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newundoitemcreator.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newundoitemcreator.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewUndoItemCreator( kindParam, editedFileParam, editDescription = "") Return Value UndoItemCreator Purpose Creates and returns a new UndoItemCreator object. Parameters kindParam As EditKinds [In] Specifies the kind of edit for which the UndoItemCreator creates an undo item. editedFileP

### Engine.NewUndoItemCreator

#### Syntax

[Engine](engine.html).NewUndoItemCreator( kindParam, editedFileParam, editDescription = "")

#### Return Value

[UndoItemCreator](undoitemcreator.html)

#### Purpose

Creates and returns a new UndoItemCreator object.

#### Parameters

kindParam
 As
 [EditKinds](editkinds.html)

[In] Specifies the kind of edit for which the UndoItemCreator creates an undo item.

editedFileParam
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies the file you are editing.

editDescription
 As
 [String](data-types-for-teststand.html)

[In] Specifies a string to use as the UndoDescription and RedoDescription of the undo item the UndoItemCreator creates. If you pass an empty string, the UndoItemCreator uses a default description.

This parameter has a default value of
 ""
 .

#### See Also

[EditKinds](editkinds.html)

[PropertyObjectFile](propertyobjectfile.html)

[UndoItemCreator](undoitemcreator.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newundostack.html language=enus -->
## TOPIC 00903: Engine.NewUndoStack

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newundostack.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newundostack.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewUndoStack Return Value UndoStack Purpose Creates and returns a new UndoStack object. Remarks You must call the UndoStack.Clear method on the UndoStack before you release the last reference to it. See Also UndoStack UndoStack.Clear

### Engine.NewUndoStack

#### Syntax

[Engine](engine.html).NewUndoStack

#### Return Value

[UndoStack](undostack.html)

#### Purpose

Creates and returns a new UndoStack object.

#### Remarks

You must call the
 [UndoStack.Clear](undostack-clear.html)
 method on the UndoStack before you release the last reference to it.

#### See Also

[UndoStack](undostack.html)

[UndoStack.Clear](undostack-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newuser.html language=enus -->
## TOPIC 00904: Engine.NewUser

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newuser.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newuser.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewUser( userProfile) Return Value User Purpose Creates and returns a new User object. Remarks Typically, only the sequence editor uses this method. Parameters userProfile As User [In] Specifies a User object with which to create the new user. The new user inherits the privileges from

### Engine.NewUser

#### Syntax

[Engine](engine.html).NewUser( userProfile)

#### Return Value

[User](user.html)

#### Purpose

Creates and returns a new User object.

#### Remarks

Typically, only the sequence editor uses this method.

#### Parameters

userProfile
 As
 [User](user.html)

[In] Specifies a User object with which to create the new user. The new user inherits the privileges from the User object the
 userProfile
 parameter specifies. The new user is not added as a member of any user groups of which the User object is a member.

Pass a
 NULL
 reference if you want to create a NewUser object without using a user profile. The new user inherits the default values as specified by the User standard data type.

You can obtain user groups using the
 [Engine.GetUserGroup](engine-getusergroup.html)
 method.

#### See Also

[Engine.CurrentUser](engine-currentuser.html)

[Engine.GetUser](engine-getuser.html)

[Engine.GetUserGroup](engine-getusergroup.html)

[User](user.html)

[UsersFile](usersfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-newworkspacefile.html language=enus -->
## TOPIC 00905: Engine.NewWorkspaceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-newworkspacefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-newworkspacefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NewWorkspaceFile Return Value WorkspaceFile Purpose Creates and returns a new WorkspaceFile object. See Also Engine.CurrentWorkspaceFile Engine.OpenWorkspaceFile WorkspaceFile

### Engine.NewWorkspaceFile

#### Syntax

[Engine](engine.html).NewWorkspaceFile

#### Return Value

[WorkspaceFile](workspacefile.html)

#### Purpose

Creates and returns a new WorkspaceFile object.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[Engine.OpenWorkspaceFile](engine-openworkspacefile.html)

[WorkspaceFile](workspacefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-notifyendofmodaldialog.html language=enus -->
## TOPIC 00906: Engine.NotifyEndOfModalDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-notifyendofmodaldialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-notifyendofmodaldialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NotifyEndOfModalDialog( modalID) Purpose Notifies TestStand that you are no longer displaying the modal dialog box the modalID parameter specifies. Remarks TestStand uses this notification to determine when to re-enable the main window of the application. Do not call this method when d

### Engine.NotifyEndOfModalDialog

#### Syntax

[Engine](engine.html).NotifyEndOfModalDialog( modalID)

#### Purpose

Notifies TestStand that you are no longer displaying the modal dialog box the
 modalID
 parameter specifies.

#### Remarks

TestStand uses this notification to determine when to re-enable the main window of the application.

Note

#### Parameters

modalID
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the modalID you receive as a return value from the
 [Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)
 method.

#### See Also

[Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)

[Engine.RegisterModalWindow](engine-registermodalwindow.html)

[Engine.UnregisterModalWindow](engine-unregistermodalwindow.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-notifystartofmodaldialog.html language=enus -->
## TOPIC 00907: Engine.NotifyStartOfModalDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-notifystartofmodaldialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-notifystartofmodaldialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NotifyStartOfModalDialog Return Value Long Returns the modalID to pass to the Engine.NotifyEndOfModalDialog method when the dialog box no longer appears onscreen. Purpose This method is obsolete. Use the Engine.NotifyStartOfModalDialogEx method instead. Remarks Notifies TestStand that

### Engine.NotifyStartOfModalDialog

#### Syntax

[Engine](engine.html).NotifyStartOfModalDialog

#### Return Value

[Long](data-types-for-teststand.html)

Returns the modalID to pass to the
 [Engine.NotifyEndOfModalDialog](engine-notifyendofmodaldialog.html)
 method when the dialog box no longer appears onscreen.

#### Purpose

Note

Engine.NotifyStartOfModalDialogEx

#### Remarks

Notifies TestStand that you are about to launch a modal dialog box.

#### See Also

[Engine.NotifyEndOfModalDialog](engine-notifyendofmodaldialog.html)

[Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)

[Engine.RegisterModalWindow](engine-registermodalwindow.html)

[Engine.UnregisterModalWindow](engine-unregistermodalwindow.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-notifystartofmodaldialogex.html language=enus -->
## TOPIC 00908: Engine.NotifyStartOfModalDialogEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-notifystartofmodaldialogex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-notifystartofmodaldialogex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NotifyStartOfModalDialogEx( sequenceContextParam, shouldAbort) Return Value Long Returns the modalID to pass to the Engine.NotifyEndOfModalDialog method when the dialog box no longer appears onscreen. Purpose Notifies TestStand that you are about to launch a modal dialog box. If you ca

### Engine.NotifyStartOfModalDialogEx

#### Syntax

[Engine](engine.html).NotifyStartOfModalDialogEx( sequenceContextParam, shouldAbort)

#### Return Value

[Long](data-types-for-teststand.html)

Returns the modalID to pass to the
 [Engine.NotifyEndOfModalDialog](engine-notifyendofmodaldialog.html)
 method when the dialog box no longer appears onscreen.

#### Purpose

Notifies TestStand that you are about to launch a modal dialog box.

Note

Engine.NotifyStartOfModalDialogEx

Engine.NotifyEndOfModalDialog

Engine.NotifyStartOfModalDialogEx

#### Remarks

This method returns a modalID, which you pass to the
 Engine.NotifyEndOfModalDialog
 method when the dialog box is closed. TestStand uses this notification to determine when to disable the main window of the application and to enforce the modality of the dialog box.

LabVIEW modal dialog box

Call
 Start Modal Dialog.vi
 and
 End Modal Dialog.vi
 in
 TestStand.llb
 instead of the
 Engine.NotifyStartOfModalDialogEx
 and
 Engine.NotifyEndOfModalDialog
 methods.

LabWindows/CVI modal dialog box

Call
 TS_EndModalDialog
 or
 TS_StartModalDialogEx
 in
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \API\CVI\tsutil.fp
 instead of the
 Engine.NotifyStartOfModalDialogEx
 and
 Engine.NotifyEndOfModalDialog
 methods.

Note

Note

Engine.NotifyStartOfModalDialog

Engine.NotifyEndOfModalDialog

Engine.RegisterModalWindow

#### Parameters

sequenceContextParam
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context of the step launching the modal dialog box. You can also pass a
 NULL
 reference but doing so loses the added functionality of this method.

shouldAbort
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 when the user terminates or aborts the corresponding execution for the sequence context parameter you passed while you were blocked inside this method call. The step skips launching the dialog box and returns as soon as possible. You can call the
 [Engine.NotifyEndOfModalDialog](engine-notifyendofmodaldialog.html)
 method in this case, though it is not necessary. If you are using the CVI
 TS_StartModalDialogEx
 function, always call the corresponding
 TS_EndModalDialog
 function. Similarly, if you are using
 Start Modal Dialog.vi
 in LabVIEW, always call
 End Modal Dialog.vi
 .

#### See Also

[Engine.NotifyEndOfModalDialog](engine-notifyendofmodaldialog.html)

[Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)

[Engine.RegisterModalWindow](engine-registermodalwindow.html)

[Engine.UnregisterModalWindow](engine-unregistermodalwindow.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-numadapters.html language=enus -->
## TOPIC 00909: Engine.NumAdapters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-numadapters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-numadapters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NumAdapters Data Type Long Purpose Returns the number of module adapters available for use with TestStand. Remarks TestStand maintains a list of available module adapters. Use the Engine.GetAdapter method to obtain a module adapter object by index. See Also Engine.GetAdapter

### Engine.NumAdapters

#### Syntax

[Engine](engine.html).NumAdapters

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of module adapters available for use with TestStand.

#### Remarks

TestStand maintains a list of available module adapters. Use the
 [Engine.GetAdapter](engine-getadapter.html)
 method to obtain a module adapter object by index.

#### See Also

[Engine.GetAdapter](engine-getadapter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-numimages.html language=enus -->
## TOPIC 00910: Engine.NumImages

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-numimages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-numimages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.NumImages Data Type Long Purpose Returns the number of images in the large and small image lists. See Also Engine.LargeImageListEx

### Engine.NumImages

#### Syntax

[Engine](engine.html).NumImages

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of images in the large and small image lists.

#### See Also

[Engine.LargeImageListEx](engine-largeimagelistex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-openworkspacefile.html language=enus -->
## TOPIC 00911: Engine.OpenWorkspaceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-openworkspacefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-openworkspacefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.OpenWorkspaceFile( workspaceFilePath, options = OpenWorkspaceFile_NoOptions, handlerType = ConflictHandler_Error) Return Value WorkspaceFile Purpose Returns the WorkspaceFile object for the workspace file the workspaceFilePath parameter specifies. Remarks Reads the workspace file from

### Engine.OpenWorkspaceFile

#### Syntax

[Engine](engine.html).OpenWorkspaceFile( workspaceFilePath, options = OpenWorkspaceFile_NoOptions, handlerType = ConflictHandler_Error)

#### Return Value

[WorkspaceFile](workspacefile.html)

#### Purpose

Returns the WorkspaceFile object for the workspace file the
 workspaceFilePath
 parameter specifies.

#### Remarks

Reads the workspace file from disk. The path must be an absolute path. If the path is not absolute, TestStand raises an exception when trying to read the workspace file.

#### Parameters

workspaceFilePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute pathname of the workspace file.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specify one or more
 [OpenWorkspaceFileOptions](openworkspacefileoptions.html)
 constants. Use the bitwise-OR operator to specify more than one option.

This parameter has a default value of
 OpenWorkspaceFile_NoOptions
 .

handlerType
 As
 [TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[In] Specifies how to handle type conflicts.

This parameter has a default value of
 ConflictHandler_Error
 .

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[Engine.NewWorkspaceFile](engine-newworkspacefile.html)

[OpenWorkspaceFileOptions](openworkspacefileoptions.html)

[TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[WorkspaceFile](workspacefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-outputmessagesenabled.html language=enus -->
## TOPIC 00912: Engine.OutputMessagesEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-outputmessagesenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-outputmessagesenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.OutputMessagesEnabled Data Type Boolean Purpose Specifies whether TestStand sends UIMsg_OutputMessages messages to the user interface. The default value is True . Remarks Independent of this property, TestStand always sends output messages to a debugger if you enable the DebugOptions_S

### Engine.OutputMessagesEnabled

#### Syntax

[Engine](engine.html).OutputMessagesEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether TestStand sends
 UIMsg_OutputMessages
 messages to the user interface. The default value is
 True
 .

#### Remarks

Independent of this property, TestStand always sends output messages to a debugger if you enable the
 DebugOptions_SendOutputMessagesToDebugger
 option of the
 [StationOptions.DebugOptions](stationoptions-debugoptions.html)
 property.

#### See Also

[DebugOptions](debugoptions.html)

[Engine.GetOutputMessages](engine-getoutputmessages.html)

[OutputMessage.Post](outputmessage-post.html)

[StationOptions.DebugOptions](stationoptions-debugoptions.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-parselookupstring.html language=enus -->
## TOPIC 00913: Engine.ParseLookupString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-parselookupstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-parselookupstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ParseLookupString( lookupString, options = 0) Return Value String Array Purpose Converts a lookup string into a String Array of the property names in the lookup string. Parameters lookupString As String [In] Specifies the lookup string to parse. options As Long [In] Specify any combina

### Engine.ParseLookupString

#### Syntax

[Engine](engine.html).ParseLookupString( lookupString, options = 0)

#### Return Value

[String Array](data-types-for-teststand.html)

#### Purpose

Converts a lookup string into a String Array of the property names in the lookup string.

#### Parameters

lookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the lookup string to parse.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specify any combination of
 [ParseLookupStringOptions](parselookupstringoptions.html)
 .

This parameter has a default value of
 0
 .

#### See Also

[ParseLookupStringOptions](parselookupstringoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-patchversion.html language=enus -->
## TOPIC 00914: Engine.PatchVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-patchversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-patchversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.PatchVersion Data Type Long Purpose Returns the patch version number for the current version of TestStand. Remarks The version number is separate from the MajorVersion.MinorVersion.RevisionVersion format, such as 1.0.2. Instead, it appears as the 'f' number in patch releases, such as T

### Engine.PatchVersion

#### Syntax

[Engine](engine.html).PatchVersion

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the patch version number for the current version of TestStand.

#### Remarks

The version number is separate from the MajorVersion.MinorVersion.RevisionVersion format, such as 1.0.2. Instead, it appears as the 'f' number in patch releases, such as
 TestStand 2020 f1
 .

Note

Engine.PatchVersion

Engine.RevisionVersion

Engine.MinorVersion

Engine.RevisionVersion

0

#### See Also

[Engine.BuildVersion](engine-buildversion.html)

[Engine.MajorVersion](engine-majorversion.html)

[Engine.MinorVersion](engine-minorversion.html)

[Engine.RevisionVersion](engine-revisionversion.html)

[Engine.VersionString](engine-versionstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-persistbreakpoints.html language=enus -->
## TOPIC 00915: Engine.PersistBreakpoints

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-persistbreakpoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-persistbreakpoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.PersistBreakpoints Data Type Boolean The default return value is False . For applications that support breakpoint persistence, such as the sequence editor, set this property to True . Purpose Specifies whether the engine associates the list of breakpoints with the current workspace and

### Engine.PersistBreakpoints

#### Syntax

[Engine](engine.html).PersistBreakpoints

#### Data Type

[Boolean](data-types-for-teststand.html)

The default return value is
 False
 . For applications that support breakpoint persistence, such as the sequence editor, set this property to
 True
 .

#### Purpose

Specifies whether the engine associates the list of breakpoints with the current workspace and automatically saves and reloads breakpoint lists when the current workspace changes. This property defaults to
 False
 for each instance of the engine. Applications that support breakpoint persistence, such as the sequence editor, should set this property to
 True
 . TestStand reads into memory the persisted breakpoint list when you change the option to
 True
 .

#### Remarks

When the engine unloads a workspace and this setting is
 True
 , the engine saves the current breakpoint list in an options file with the same name as the workspace and in the same directory as the workspace file. The engine also saves the current breakpoint list when you save the current workspace or any sequence file in the workspace or when you close any sequence file.

When the engine loads a new workspace and this setting is
 True
 , the engine automatically loads the breakpoint list previously saved in the options file. Otherwise, the engine keeps the current breakpoint list.

If no current workspace is loaded, the engine persists the breakpoint list to a default options file.

TestStand persists only breakpoints that apply to sequence files. TestStand does not persist breakpoints associated with executions.

#### See Also

[Engine.PersistWatchExpressions](engine-persistwatchexpressions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-persistconfigfile.html language=enus -->
## TOPIC 00916: Engine.PersistConfigFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-persistconfigfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-persistconfigfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.PersistConfigFile Data Type Boolean The default return value is True . Purpose Specifies whether the engine automatically saves its configuration files: StarupCfg.ini , GeneralEngine.cfg , Adapters.cfg , SearchDirectories.cfg , TypePalettes.cfg , and Custom.cfg . This property defaults

### Engine.PersistConfigFile

#### Syntax

[Engine](engine.html).PersistConfigFile

#### Data Type

[Boolean](data-types-for-teststand.html)

The default return value is
 True
 .

#### Purpose

Specifies whether the engine automatically saves its configuration files:
 StarupCfg.ini
 ,
 GeneralEngine.cfg
 ,
 Adapters.cfg
 ,
 SearchDirectories.cfg
 ,
 TypePalettes.cfg
 , and
 Custom.cfg
 . This property defaults to
 True
 True for each instance of the engine. Applications can set this property to
 False
 to prevent changes to configuration information from affecting future instances of the engine.

#### See Also

[Engine.ConfigFile](engine-configfile.html)

[Engine.PersistBreakpoints](engine-persistbreakpoints.html)

[Engine.PersistWatchExpressions](engine-persistwatchexpressions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-persistwatchexpressions.html language=enus -->
## TOPIC 00917: Engine.PersistWatchExpressions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-persistwatchexpressions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-persistwatchexpressions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.PersistWatchExpressions Data Type Boolean The default return value is False . For applications that support watch expression persistence, such as the sequence editor, set this property to True . Purpose Specifies whether the engine associates the list of watch expressions with the curr

### Engine.PersistWatchExpressions

#### Syntax

[Engine](engine.html).PersistWatchExpressions

#### Data Type

[Boolean](data-types-for-teststand.html)

The default return value is
 False
 . For applications that support watch expression persistence, such as the sequence editor, set this property to
 True
 .

#### Purpose

Specifies whether the engine associates the list of watch expressions with the current workspace, and automatically saves and reloads the watch expression list when the current workspace changes. This property defaults to
 False
 for each instance of the engine. For applications that support watch expression persistence, such as the sequence editor, set this property to
 True
 . TestStand reads into memory the persisted watch expression when you change the option to
 True
 .

#### Remarks

When the engine unloads a workspace and this setting is
 True
 , the engine saves the current watch expression list in an options file with the same name as the workspace and in the same directory as the workspace file. The engine also saves the current watch expression list when you save the current workspace or any sequence file in the workspace or when you close any sequence file.

When the engine loads a new workspace and this setting is
 True
 , the engine automatically loads the watch expression list previously saved in the options file. Otherwise, the engine keeps the current watch expression list.

If no current workspace is loaded, the engine persists the watch expression list to a default options file.

TestStand persists only watch expressions that are not associated with a particular execution, such as when
 [WatchExpression.ExecutionScope](watchexpression-executionscope.html)
 is
 NULL
 .

#### See Also

[Engine.PersistBreakpoints](engine-persistbreakpoints.html)

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-postuimessage.html language=enus -->
## TOPIC 00918: Engine.PostUIMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-postuimessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-postuimessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.PostUIMessage( executionParam, threadParam, eventCode, numericDataParam, stringDataParam, activeXDataParam, synchronous) Purpose Posts a user interface message to the current sequence editor or user interface. Remarks You can post the following messages from a step: UIMsg_ProgressPerce

### Engine.PostUIMessage

#### Syntax

[Engine](engine.html).PostUIMessage( executionParam, threadParam, eventCode, numericDataParam, stringDataParam, activeXDataParam, synchronous)

#### Purpose

Posts a user interface message to the current sequence editor or user interface.

#### Remarks

You can post the following messages from a step:
 UIMsg_ProgressPercent
 and
 UIMsg_ProgressText
 . These messages tell the user interface to display a progress indicator or text message for the execution.

#### Parameters

executionParam
 As
 [Execution](execution.html)

[In] Specifies the execution to pass with the message.

threadParam
 As
 [Thread](thread.html)

[In] Specifies the thread to pass with the message.

eventCode
 As
 [UIMessageCodes](uimessagecodes.html)

[In] Specifies the type of UIMessage.

numericDataParam
 As
 [Double](data-types-for-teststand.html)

[In] Specifies numeric data to pass with the message. When you post a
 UIMsg_ProgressPercent
 event, this parameter specifies the percent done.

stringDataParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies string data to pass with the message. When you post a
 UIMsg_ProgressText
 event, this parameter specifies the text to display.

activeXDataParam
 As
 [IUnknown](data-types-for-teststand.html)

[In] Specifies an ActiveX reference to pass with the message.

synchronous
 As
 [Boolean](data-types-for-teststand.html)

[In] Typically, you pass
 True
 for this parameter to direct the method to wait until the user interface processes the message. If you pass
 False
 , the method returns immediately without waiting for the user interface to handle the message. If you pass
 False
 and post messages faster than the user interface processes messages, the number of messages in the queue the user interface must handle grows unbounded and floods the user interface with messages, which causes the user interface to become unresponsive.

#### See Also

[Execution](execution.html)

[Thread](thread.html)

[Thread.PostUIMessageEx](thread-postuimessageex.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-profilerinputoutputcapturemaximumtextl.html language=enus -->
## TOPIC 00919: Engine.ProfilerInputOutputCaptureMaximumTextLength

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-profilerinputoutputcapturemaximumtextl.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-profilerinputoutputcapturemaximumtextl.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ProfilerInputOutputCaptureMaximumTextLength Data Type Long Purpose Specifies the maximum text size per row of the Module Inputs and Outputs column on the Operations table. Remarks This property is the programmatic interface to the Limit Module Input/Output Text Length numeric control o

### Engine.ProfilerInputOutputCaptureMaximumTextLength

#### Syntax

[Engine](engine.html).ProfilerInputOutputCaptureMaximumTextLength

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the maximum text size per row of the Module Inputs and Outputs column on the Operations table.

#### Remarks

This property is the programmatic interface to the Limit Module Input/Output Text Length numeric control on the Configure Data Collection dialog box. A value of
 -1
 indicates no limit.

#### See Also

[Configure Data Collection Dialog Box](../tsref/configure-data-collection-dialog-box.html)

[Operations Table](../tsref/operations-table.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-profileroptions.html language=enus -->
## TOPIC 00920: Engine.ProfilerOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-profileroptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-profileroptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ProfilerOptions Data Type Long Purpose Specifies options that determine the types of data that profiling collects. Remarks Refer to ProfilerOptions. for a list of options. You can limit the types of data that profiling collects in order to reduce profiling overhead. See Also ProfilerOp

### Engine.ProfilerOptions

#### Syntax

[Engine](engine.html).ProfilerOptions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies options that determine the types of data that profiling collects.

#### Remarks

Refer to
 [ProfilerOptions.](profileroptions.html)
 for a list of options. You can limit the types of data that profiling collects in order to reduce profiling overhead.

#### See Also

[ProfilerOptions](profileroptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-profileroutputmessagecategoryname.html language=enus -->
## TOPIC 00921: Engine.ProfilerOutputMessageCategoryName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-profileroutputmessagecategoryname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-profileroutputmessagecategoryname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ProfilerOutputMessageCategoryName Data Type String Purpose Indicates the category name the TestStand engine assigns to the OutputMessages the Engine.LogProfilerAction method creates.

### Engine.ProfilerOutputMessageCategoryName

#### Syntax

[Engine](engine.html).ProfilerOutputMessageCategoryName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Indicates the category name the TestStand engine assigns to the OutputMessages the Engine.LogProfilerAction method creates.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-profilingenabled.html language=enus -->
## TOPIC 00922: Engine.ProfilingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-profilingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-profilingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ProfilingEnabled Data Type Boolean Purpose This property indicates whether profiling is enabled. Profiling is enabled when a call to Engine.BeginProfiling has not been balanced by a call to Engine.EndProfiling. If profiling is not enabled, calls to Engine.LogProfilerAction do nothing.

### Engine.ProfilingEnabled

#### Syntax

[Engine](engine.html).ProfilingEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

This property indicates whether profiling is enabled. Profiling is enabled when a call to Engine.BeginProfiling has not been balanced by a call to Engine.EndProfiling. If profiling is not enabled, calls to Engine.LogProfilerAction do nothing.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-promptwhenaddingfilestosc.html language=enus -->
## TOPIC 00923: Engine.PromptWhenAddingFilesToSC

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-promptwhenaddingfilestosc.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-promptwhenaddingfilestosc.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.PromptWhenAddingFilesToSC Data Type Boolean Purpose This property is obsolete. Use the StationOptions.PromptWhenAddingFilesToSC property instead. Remarks Specifies if the sequence editor prompts you to add files to source code control when you add files to a workspace. When this option

### Engine.PromptWhenAddingFilesToSC

#### Syntax

[Engine](engine.html).PromptWhenAddingFilesToSC

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.PromptWhenAddingFilesToSC

#### Remarks

Specifies if the sequence editor prompts you to add files to source code control when you add files to a workspace.

When this option is
 True
 , the sequence editor launches a dialog box in which you can add files to source code control whenever you add them to a workspace file. When this option is
 False
 , the sequence editor does not launch a dialog box.

#### See Also

[StationOptions.CheckOutFilesWhenEdited](stationoptions-checkoutfileswhenedited.html)

[StationOptions.CheckOutOnlySelectedFiles](stationoptions-checkoutonlyselectedfiles.html)

[StationOptions.PromptWhenAddingFilesToSC](stationoptions-promptwhenaddingfilestosc.html)

[StationOptions.UseDialogForCheckOut](stationoptions-usedialogforcheckout.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-readpropertyobjectfile.html language=enus -->
## TOPIC 00924: Engine.ReadPropertyObjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-readpropertyobjectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-readpropertyobjectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ReadPropertyObjectFile( path, userCancelled, handlerType = ConflictHandler_Error, options = 0) Return Value PropertyObjectFile The newly created PropertyObjectFile object. Purpose Creates a new PropertyObjectFile object, determines the file type, and reads the object as that file type.

### Engine.ReadPropertyObjectFile

#### Syntax

[Engine](engine.html).ReadPropertyObjectFile( path, userCancelled, handlerType = ConflictHandler_Error, options = 0)

#### Return Value

[PropertyObjectFile](propertyobjectfile.html)

The newly created
 PropertyObjectFile
 object.

#### Purpose

Creates a new
 [PropertyObjectFile](propertyobjectfile.html)
 object, determines the file type, and reads the object as that file type.

#### Remarks

Use this method to examine the internal structure, data, and types contained in a
 PropertyObjectFile
 , even if the file type is unknown. Calling this method produces the same result as calling the
 [FileInformation.PropertyObjectFileType](fileinformation-propertyobjectfiletype.html)
 property, the

[Engine.NewPropertyObjectFile](engine-newpropertyobjectfile.html)
 method, and the
 [PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)
 method.

You cannot read a users file, a configuration file, or a station globals file using this method. This method returns an error if the file is not a
 PropertyObjectFile
 . Use
 [FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)
 property to determine if the file is a
 PropertyObjectFile
 .

Note

Engine.GetSequenceFileEx

Engine.GetSequenceFileEx

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the file.

userCancelled
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the file has type conflicts and the user cancelled the operation.

handlerType
 As
 [TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[In] Specifies how to handle type conflicts.

This parameter has a default value of
 ConflictHandler_Error
 .

options
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 to specify the default behavior or pass one or more
 [ReadPropertyObjectFileOptions](readpropertyobjectfileoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options.

This parameter has a default value of
 0
 .

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.NewPropertyObjectFile](engine-newpropertyobjectfile.html)

[Engine.OpenWorkspaceFile](engine-openworkspacefile.html)

[FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)

[FileInformation.PropertyObjectFileType](fileinformation-propertyobjectfiletype.html)

[PropertyObjectFile](propertyobjectfile.html)

[PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)

[ReadPropertyObjectFileOptions](readpropertyobjectfileoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-registermodalwindow.html language=enus -->
## TOPIC 00925: Engine.RegisterModalWindow

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-registermodalwindow.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-registermodalwindow.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.RegisterModalWindow( sequenceContextParam, modalHWND, shouldAbort) Return Value Long Returns the modalID to pass to the Engine.UnregisterModalWindow method when the dialog box no longer appears on screen. Purpose Notifies TestStand that the specified window is a modal dialog box. Remar

### Engine.RegisterModalWindow

#### Syntax

[Engine](engine.html).RegisterModalWindow( sequenceContextParam, modalHWND, shouldAbort)

#### Return Value

[Long](data-types-for-teststand.html)

Returns the modalID to pass to the
 [Engine.UnregisterModalWindow](engine-unregistermodalwindow.html)
 method when the dialog box no longer appears on screen.

#### Purpose

Notifies TestStand that the specified window is a modal dialog box.

#### Remarks

Call this method after you create a modal dialog box. TestStand disables the main application window and forwards any activation requests to the specified window. Call the
 [Engine.UnregisterModalWindow](engine-unregistermodalwindow.html)
 method when the dialog box closes.

You must call this method after you have created the dialog box window. An alternative to using this method is to call the
 [Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)
 method, which you must call before creating the dialog box window.

For a Microsoft Visual Basic modal dialog box, if you display the dialog box from multiple threads at the same time, you must use an executable ActiveX Automation server project and set the project settings to Thread Per Object.

#### Parameters

sequenceContextParam
 As
 [SequenceContext](sequencecontext.html)

[In] If you display the dialog box from the step of an execution, pass the sequence context of the step; otherwise, pass a
 NULL
 reference. If you pass a sequence context, this method serializes calls from multiple threads the same way the
 [Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)
 method serializes calls.

modalHWND
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the window handle of the modal dialog box.

shouldAbort
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 when the user terminates or aborts the corresponding execution for the sequence context parameter you passed while you were blocked inside this method call. The step skips launching the dialog box and returns as soon as possible. You can call
 [Engine.UnregisterModalWindow](engine-unregistermodalwindow.html)
 in this case, though it is not necessary.

#### See Also

[Engine.NotifyEndOfModalDialog](engine-notifyendofmodaldialog.html)

[Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)

[Engine.UnregisterModalWindow](engine-unregistermodalwindow.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-registersequencetoexecuteoncrash.html language=enus -->
## TOPIC 00926: Engine.RegisterSequenceToExecuteOnCrash

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-registersequencetoexecuteoncrash.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-registersequencetoexecuteoncrash.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.RegisterSequenceToExecuteOnCrash( seqFilePath, seqName, options, reserved) Return Value Long Returns the registration id for Engine.UnregisterSequenceToExecuteOnCrash . Purpose Registers the sequence to execute on TestStand application crash. Remarks The sequence is executed in an exte

### Engine.RegisterSequenceToExecuteOnCrash

#### Syntax

[Engine](engine.html).RegisterSequenceToExecuteOnCrash( seqFilePath, seqName, options, reserved)

#### Return Value

[Long](data-types-for-teststand.html)

Returns the registration id for
 Engine.UnregisterSequenceToExecuteOnCrash
 .

#### Purpose

Registers the sequence to execute on TestStand application crash.

#### Remarks

The sequence is executed in an external application on TestStand application crash. Default parameter values are used when calling the registered sequence. If run time error option is set to
 Show dialog
 , the setting is ignored (no dialogs are shown from external application) and cleanup will be executed.

#### Parameters

seqFilePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the sequence file. If the pathname is relative, this method tries to find it using
 Engine.FindFileEx
 method.

seqName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the sequence to execute on TestStand application crash.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies whether to load the sequence file in the external application after TestStand application crash or when sequence is registered. Pass
 0
 to specify the default behavior, or pass one or more
 [CrashCallbackOptions](crashcallbackoptions.html)
 . Use the bitwise-OR operator to specify multiple options.

reserved
 As
 [Variant](data-types-for-teststand.html)

[In] This parameter is reserved.

#### See Also

[Engine.FindFileEx](engine-findfileex.html)

[CrashCallbackOptions](crashcallbackoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-registeruimessage.html language=enus -->
## TOPIC 00927: Engine.RegisterUIMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-registeruimessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-registeruimessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.RegisterUIMessage( messageName) Return Value Long Returns the event code for the message. Use this value as the eventCode parameter of the Thread.PostUIMessageEx method. Returns -1 if there are no more message codes available for registration. Purpose Defines a new UIMessage that is gu

### Engine.RegisterUIMessage

#### Syntax

[Engine](engine.html).RegisterUIMessage( messageName)

#### Return Value

[Long](data-types-for-teststand.html)

Returns the event code for the message. Use this value as the
 eventCode
 parameter of the
 [Thread.PostUIMessageEx](thread-postuimessageex.html)
 method.

Returns
 -1
 if there are no more message codes available for registration.

#### Purpose

Defines a new UIMessage that is guaranteed to be unique for the lifetime of the engine.

#### Remarks

Use this method to define new messages for step types or user interfaces to ensure that they do not conflict with messages defined by other custom TestStand components, such as add-on products. This method returns the previously assigned message code if the message is already assigned.

Messages the
 Engine.RegisterUIMessages
 method defines do not generate an
 
 [ApplicationMgr.UserMessage](../tsuiref/applicationmgr-usermessage.html)
 event, but TestStand does send the message to
 
 [ApplicationMgr.UIMessageEvent](../tsuiref/applicationmgr-uimessageevent.html)
 .

#### Parameters

messageName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the message to register.

#### See Also

[Engine.PostUIMessage](engine-postuimessage.html)

[Thread.PostUIMessageEx](thread-postuimessageex.html)

[UIMessage](uimessage.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-registeruimessagecallback.html language=enus -->
## TOPIC 00928: Engine.RegisterUIMessageCallback

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-registeruimessagecallback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-registeruimessagecallback.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.RegisterUIMessageCallback( callbackFuncAddr) Purpose This method is obsolete. Use the Engine.RegisterUIMessageCallbackEx method instead. Calling this method on a 64-bit instance of the TestStand Engine results in an error. Remarks Registers a C function as the user interface message ev

### Engine.RegisterUIMessageCallback

#### Syntax

[Engine](engine.html).RegisterUIMessageCallback( callbackFuncAddr)

#### Purpose

Note

Engine.RegisterUIMessageCallbackEx

#### Remarks

Registers a C function as the user interface message event callback.

Note

Application Manager control

ApplicationMgr.AfterUIMessageEvent

ApplicationMgr.UIMessageEvent

<TestStand>

You can use a C function as the Event callback, instead of using ActiveX events or polling. Ensure the
 [Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)
 property is
 False
 or TestStand does not call the callback.

The callback function must use the following C function prototype:

void __cdecl UIMessageCallback(struct IDispatch *UIMessageDisp);

The
 UIMessageDisp
 parameter is the IDispatch pointer to a UIMessage object. Because this pointer is passed to the callback as a parameter, do not release it when you finish using it.

Note

#### Parameters

callbackFuncAddr
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the address of the callback function.

#### See Also

[Engine.GetUIMessage](engine-getuimessage.html)

[Engine.UIMessageEvent](engine-uimessageevent.html)

[Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)

[StationOptions.UIMessageDelay](stationoptions-uimessagedelay.html)

[StationOptions.UIMessageMinDelay](stationoptions-uimessagemindelay.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-registeruimessagecallbackex.html language=enus -->
## TOPIC 00929: Engine.RegisterUIMessageCallbackEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-registeruimessagecallbackex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-registeruimessagecallbackex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.RegisterUIMessageCallbackEx( callbackFuncAddr) Purpose Registers a C function as the user interface message event callback. National Instruments recommends using the Application Manager control with the ApplicationMgr.AfterUIMessageEvent and ApplicationMgr.UIMessageEvent events as need

### Engine.RegisterUIMessageCallbackEx

#### Syntax

[Engine](engine.html).RegisterUIMessageCallbackEx( callbackFuncAddr)

#### Purpose

Registers a C function as the user interface message event callback.

Note

Application Manager control

ApplicationMgr.AfterUIMessageEvent

ApplicationMgr.UIMessageEvent

<TestStand>

#### Remarks

You can use a C function as the Event callback, instead of using ActiveX events or polling. Ensure the
 [Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)
 property is
 False
 or TestStand does not call the callback.

The callback function must use the following C function prototype:

void __cdecl UIMessageCallback(struct IDispatch *UIMessageDisp);

The
 UIMessageDisp
 parameter is the IDispatch pointer to a UIMessage object. Because this pointer is passed to the callback as a parameter, do not release it when you finish using it.

Note

#### Parameters

callbackFuncAddr
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the address of the callback function. The type of the variant must match the pointer size for the current platform, for example
 VT_UI4
 for 32-bit TestStand and
 VT_UI8
 for 64-bit TestStand.

#### See Also

[Engine.GetUIMessage](engine-getuimessage.html)

[Engine.UIMessageEvent](engine-uimessageevent.html)

[Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)

[StationOptions.UIMessageDelay](stationoptions-uimessagedelay.html)

[StationOptions.UIMessageMinDelay](stationoptions-uimessagemindelay.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-releaselicense.html language=enus -->
## TOPIC 00930: Engine.ReleaseLicense

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-releaselicense.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-releaselicense.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ReleaseLicense( licenseHandle, reserved = 0) Purpose Informs TestStand that a previously acquired license is no longer needed. An application requires a type of license until you release all license handles for the license type. Parameters licenseHandle As Long [In] Specifies the licen

### Engine.ReleaseLicense

#### Syntax

[Engine](engine.html).ReleaseLicense( licenseHandle, reserved = 0)

#### Purpose

Informs TestStand that a previously acquired
 
 [license](/csh?context=ts_9050)
 is no longer needed. An application requires a type of license until you release all license handles for the license type.

#### Parameters

licenseHandle
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the license handle to release. Pass a handle the
 [Engine.AcquireLicense](engine-acquirelicense.html)
 method returned.

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use.

This parameter has a default value of
 0
 .

#### See Also

[Engine.AcquireLicense](engine-acquirelicense.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-releasesequencefile.html language=enus -->
## TOPIC 00931: Engine.ReleaseSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-releasesequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-releasesequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ReleaseSequenceFile( sequenceFileToRelease) Purpose This method is obsolete. Use the Engine.ReleaseSequenceFileEx method instead. Remarks Releases the SequenceFile object from the Engine internal cache. Calling this method does not release the ActiveX reference to the sequence file. Pa

### Engine.ReleaseSequenceFile

#### Syntax

[Engine](engine.html).ReleaseSequenceFile( sequenceFileToRelease)

#### Purpose

Note

Engine.ReleaseSequenceFileEx

#### Remarks

Releases the SequenceFile object from the Engine internal cache.

Note

#### Parameters

sequenceFileToRelease
 As
 [SequenceFile](sequencefile.html)

[In] Pass a reference to the sequence file to release.

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.NewSequenceFile](engine-newsequencefile.html)

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-releasesequencefileex.html language=enus -->
## TOPIC 00932: Engine.ReleaseSequenceFileEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-releasesequencefileex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-releasesequencefileex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ReleaseSequenceFileEx( sequenceFileToRelease, options = 0) Return Value Boolean Returns True if the file was removed from the TestStand internal cache. Returns False if the file remained in the cache because it has multiple load references or if TestStand initiates the execution of the

### Engine.ReleaseSequenceFileEx

#### Syntax

[Engine](engine.html).ReleaseSequenceFileEx( sequenceFileToRelease, options = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the file was removed from the TestStand internal cache. Returns
 False
 if the file remained in the cache because it has multiple load references or if TestStand initiates the execution of the SequenceFileUnload callback sequence for the SequenceFile object.

Refer to
 [SequenceFile.CanUnload](sequencefile-canunload.html)
 for more information about loading and unloading files in the cache.

#### Purpose

Releases the SequenceFile object from the internal cache of the engine.

#### Remarks

Call this method to release the sequence file you obtained from the
 [Engine.NewSequenceFile](engine-newsequencefile.html)
 or
 [Engine.GetSequenceFileEx](engine-getsequencefileex.html)
 methods.

This method removes a load reference from the sequence file. TestStand uses the load reference count to determine when to unload the sequence file from the internal cache of the engine.

When you release the last load reference, TestStand unloads the file from the internal cache of the engine. While unloading the file from the internal cache of the engine, TestStand executes the SequenceFileUnload callback, if applicable.

If this method generates an error, TestStand does not release the object from the internal cache of the engine. If your development environment requires you to explicitly release COM references, only release the COM reference to a SequenceFile object if this method succeeds.

Use the
 ReleaseSeqFile_DoNotRunUnloadCallback
 option to prevent the SequenceFileUnload callback from running if the callback exists and the load reference being released is the last load reference. TestStand executes the SequenceFileUnloadCallback after this method returns.

Note

#### Parameters

sequenceFileToRelease
 As
 [SequenceFile](sequencefile.html)

[In] Specifies a reference to the sequence file to release.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specify one or more
 [ReleaseSeqFileOptions](releaseseqfileoptions.html)
 constants. Use the bitwise-OR operator to specify multiple sequence file flags.

This parameter has a default value of
 0
 .

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.NewSequenceFile](engine-newsequencefile.html)

[ReleaseSeqFileOptions](releaseseqfileoptions.html)

[SequenceFile](sequencefile.html)

[SequenceFile.AddLoadReference](sequencefile-addloadreference.html)

[SequenceFile.CanUnload](sequencefile-canunload.html)

[SequenceFile.IsExecuting](sequencefile-isexecuting.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-reloaddocswhenopeningworkspace.html language=enus -->
## TOPIC 00933: Engine.ReloadDocsWhenOpeningWorkspace

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-reloaddocswhenopeningworkspace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-reloaddocswhenopeningworkspace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ReloadDocsWhenOpeningWorkspace Data Type Boolean Purpose This property is obsolete. Use the StationOptions.ReloadDocsWhenOpeningWorkspace property instead. Remarks Specifies if the sequence editor opens the documents that were open when the workspace was unloaded. If this property is T

### Engine.ReloadDocsWhenOpeningWorkspace

#### Syntax

[Engine](engine.html).ReloadDocsWhenOpeningWorkspace

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.ReloadDocsWhenOpeningWorkspace

#### Remarks

Specifies if the sequence editor opens the documents that were open when the workspace was unloaded.

If this property is
 True
 and you open a workspace file, the sequence editor opens the documents that were open when the workspace file was last closed.

#### See Also

[StationOptions.ReloadDocsWhenOpeningWorkspace](stationoptions-reloaddocswhenopeningworkspace.html)

[StationOptions.ReloadWorkspaceAtStartup](stationoptions-reloadworkspaceatstartup.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-reloadglobals.html language=enus -->
## TOPIC 00934: Engine.ReloadGlobals

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-reloadglobals.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-reloadglobals.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ReloadGlobals Purpose Reloads global variables from disk. All global reference variables and properties that exist after you call this method retain the reference values they had before the call to ReloadGlobals. To clear reference values, explicitly set the references to nothing or de

### Engine.ReloadGlobals

#### Syntax

[Engine](engine.html).ReloadGlobals

#### Purpose

Reloads global variables from disk. All global reference variables and properties that exist after you call this method retain the reference values they had before the call to ReloadGlobals. To clear reference values, explicitly set the references to nothing or delete the global reference variables and properties before you call this method.

#### See Also

[Engine.CommitGlobalsToDisk](engine-commitglobalstodisk.html)

[Engine.Globals](engine-globals.html)

[Engine.GlobalsFile](engine-globalsfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-reloadstringresourcefiles.html language=enus -->
## TOPIC 00935: Engine.ReloadStringResourceFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-reloadstringresourcefiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-reloadstringresourcefiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ReloadStringResourceFiles Purpose Refreshes the TestStand Engine string table, affecting future calls to the Engine.GetResourceString method. Remarks TestStand does not unload the strings but overwrites existing ones. Components that have already cached resource strings might not updat

### Engine.ReloadStringResourceFiles

#### Syntax

[Engine](engine.html).ReloadStringResourceFiles

#### Purpose

Refreshes the TestStand Engine string table, affecting future calls to the
 [Engine.GetResourceString](engine-getresourcestring.html)
 method.

#### Remarks

TestStand does not unload the strings but overwrites existing ones. Components that have already cached resource strings might not update with new values.

The string table is updated with the files corresponding to the last language selected.

#### See Also

[Engine.GetResourceString](engine-getresourcestring.html)

[StationOptions.Language](stationoptions-language.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-reloadworkspaceatstartup.html language=enus -->
## TOPIC 00936: Engine.ReloadWorkspaceAtStartup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-reloadworkspaceatstartup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-reloadworkspaceatstartup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ReloadWorkspaceAtStartup Data Type Boolean Purpose This property is obsolete. Use the StationOptions.ReloadWorkspaceAtStartup property instead. Remarks Specifies if the sequence editor opens the last workspace file when it launches. If this option is True when the sequence editor launc

### Engine.ReloadWorkspaceAtStartup

#### Syntax

[Engine](engine.html).ReloadWorkspaceAtStartup

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.ReloadWorkspaceAtStartup

#### Remarks

Specifies if the sequence editor opens the last workspace file when it launches.

If this option is
 True
 when the sequence editor launches, the sequence editor loads the workspace file the
 [Engine.LastWorkspacePath](engine-lastworkspacepath.html)
 property specifies.

#### See Also

[Engine.LastWorkspacePath](engine-lastworkspacepath.html)

[StationOptions.ReloadDocsWhenOpeningWorkspace](stationoptions-reloaddocswhenopeningworkspace.html)

[StationOptions.ReloadWorkspaceAtStartup](stationoptions-reloadworkspaceatstartup.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-requireuserlogin.html language=enus -->
## TOPIC 00937: Engine.RequireUserLogin

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-requireuserlogin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-requireuserlogin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.RequireUserLogin Data Type Boolean Purpose This property is obsolete. Use the StationOptions.RequireUserLogin property instead. Remarks Specifies if the sequence editor or user interfaces require that a user be logged in. TestStand uses this property only when Engine.EnableUserPrivileg

### Engine.RequireUserLogin

#### Syntax

[Engine](engine.html).RequireUserLogin

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.RequireUserLogin

#### Remarks

Specifies if the sequence editor or user interfaces require that a user be logged in.

TestStand uses this property only when
 Engine.EnableUserPrivilegeChecking
 is
 True
 . When this property is
 True
 , TestStand disables the user interfaces until a user successfully logs in.

Note

Engine.EnableUserPrivilegeChecking

StationOptions.EnableUserPrivilegeChecking

#### See Also

[StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)

[StationOptions.RequireUserLogin](stationoptions-requireuserlogin.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-resettypeinstances.html language=enus -->
## TOPIC 00938: Engine.ResetTypeInstances

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-resettypeinstances.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-resettypeinstances.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ResetTypeInstances( typeParam, resetTypeInstancesOptions = ResetTypeInst_ResetFlags | ResetTypeInst_ResetValues) Return Value Boolean Returns True if this method finds any type instances or returns False if it finds none. Purpose Searches for all instances of the specified type definit

### Engine.ResetTypeInstances

#### Syntax

[Engine](engine.html).ResetTypeInstances( typeParam, resetTypeInstancesOptions = ResetTypeInst_ResetFlags | ResetTypeInst_ResetValues)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if this method finds any type instances or returns
 False
 if it finds none.

#### Purpose

Searches for all instances of the specified type definition in the TestStand Engine and sets the values and flags of each type definition instance to the default value and flags for the type.

#### Remarks

Use this method to apply the value of a type definition property to all instances of the type. Normally, when you change the value of a type definition property, the values in the instances of the type do not change.

Note

typeParam

ResetTypeInst_RecurseSubProperties

#### Parameters

typeParam
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a type definition or a subproperty of a type definition.

resetTypeInstancesOptions
 As
 [Long](data-types-for-teststand.html)

[In] Pass one or more
 [ResetTypeInstancesOptions](resettypeinstanceoptions.html)
 constants to specify different options. Use the bitwise-OR operator to specify more than one option. If you want to reset the values/flags of all the subproperties in all instances of a type, pass
 ResetTypeInst_RecurseSubProperties
 using the bitwise-OR operator with
 ResetTypeInst_ResetFlags
 or
 ResetTypeInst_ResetValues
 .

Note

ResetTypeInst_ResetFlags

PropFlags_PassByReference

Sequence Call

Engine.ResetTypeInstances

This parameter has a default value of
 ResetTypeInst_ResetFlags | ResetTypeInst_ResetValues
 .

#### See Also

[PropertyObject](propertyobject.html)

[PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)

[ResetTypeInstanceOptions](resettypeinstanceoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-revisionversion.html language=enus -->
## TOPIC 00939: Engine.RevisionVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-revisionversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-revisionversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.RevisionVersion Data Type Long Purpose Returns the revision version number for the current version of TestStand. Remarks The version number usually appears in the MajorVersion.MinorVersion.RevisionVersion format, such as 1.0.2 . Prior to TestStand 2016, the revision version sometimes i

### Engine.RevisionVersion

#### Syntax

[Engine](engine.html).RevisionVersion

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the revision version number for the current version of TestStand.

#### Remarks

The version number usually appears in the
 MajorVersion.MinorVersion.RevisionVersion
 format, such as
 1.0.2
 .

Note

Engine.MinorVersion

Engine.RevisionVersion

#### See Also

[Engine.BuildVersion](engine-buildversion.html)

[Engine.MajorVersion](engine-majorversion.html)

[Engine.MinorVersion](engine-minorversion.html)

[Engine.PatchVersion](engine-patchversion.html)

[Engine.VersionString](engine-versionstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-rteoption.html language=enus -->
## TOPIC 00940: Engine.RTEOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-rteoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-rteoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.RTEOption Data Type RTEOptions Use the following constants with this data type: RTEOption_Abort –(Value: 3) Instructs the execution to abort the execution. RTEOption_Continue –(Value: 1) Instructs the execution to process the error by propagating the error to the calling sequence, if o

### Engine.RTEOption

#### Syntax

[Engine](engine.html).RTEOption

#### Data Type

[RTEOptions](rteoptions.html)

Use the following constants with this data type:

- RTEOption_Abort 
 –(Value: 3) Instructs the execution to abort the execution.
- RTEOption_Continue 
 –(Value: 1) Instructs the execution to process the error by propagating the error to the calling sequence, if one exists. If the current step group is Setup or Main, the execution jumps directly to the Cleanup step group.
- RTEOption_Ignore 
 –(Value: 2) Instructs the execution to ignore the error and continue normal execution.
- RTEOption_Retry 
 –(Value: 4) Instructs the execution to ignore the error and re-execute the step that caused the error condition. For the
 StationOptions.RTEOption 
 property, the
 Execution.RTEOptionForThisExecution 
 property, and the
 Thread.SetBatchRTEOption 
 method, TestStand interprets the
 RTEOption_Retry 
 value as
 RTEOption_Continue 
 .
- RTEOption_ShowDialog 
 –(Value: 0) Instructs the execution to launch the
 Run-Time Error 
 dialog box when an error occurs.

#### Purpose

Note

StationOptions.RTEOption

#### Remarks

Specifies the default behavior of TestStand when a run-time error occurs in an execution.

Note

BreakOnRTE

#### See Also

[Execution.RTEOptionForThisExecution](execution-rteoptionforthisexecution.html)

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[StationOptions.RTEOption](stationoptions-rteoption.html)

[Thread.SetBatchRTEOption](thread-setbatchrteoption.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-saveallmodifiedseqfiles.html language=enus -->
## TOPIC 00941: Engine.SaveAllModifiedSeqFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-saveallmodifiedseqfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-saveallmodifiedseqfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SaveAllModifiedSeqFiles( options = 0) Return Value Boolean Returns True if all modified files were saved successfully. Returns False if one or more files could not be saved or if the user cancels the operation. Purpose Saves all modified sequence files in the engine internal cache. Rem

### Engine.SaveAllModifiedSeqFiles

#### Syntax

[Engine](engine.html).SaveAllModifiedSeqFiles( options = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if all modified files were saved successfully. Returns
 False
 if one or more files could not be saved or if the user cancels the operation.

#### Purpose

Saves all modified sequence files in the engine internal cache.

#### Remarks

If this method prompts the user to save a file and the user selects
 No
 , subsequent calls to this method do not prompt the user to save the file unless the file is modified further.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specify one or more
 [SaveAllSeqFileOptions](saveallseqfileoptions.html)
 constants. Use the bitwise-OR operator to specify multiple sequence file flags.

This parameter has a default value of
 0
 .

#### See Also

[SaveAllSeqFileOptions](saveallseqfileoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-searchdirectories.html language=enus -->
## TOPIC 00942: Engine.SearchDirectories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-searchdirectories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-searchdirectories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SearchDirectories Data Type SearchDirectories Purpose Returns a reference to the SearchDirectories object. This object is a collection that contains a list of the current search directories . Remarks You must obtain the search directory collection before adding or modifying a search di

### Engine.SearchDirectories

#### Syntax

[Engine](engine.html).SearchDirectories

#### Data Type

[SearchDirectories](searchdirectories.html)

#### Purpose

Returns a reference to the
 [SearchDirectories](searchdirectories.html)
 object. This object is a collection that contains a list of the current
 [search directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### Remarks

You must obtain the search directory collection before adding or modifying a search directory.

#### See Also

[Engine.BinDirectory](engine-bindirectory.html)

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.TestStandDirectory](engine-teststanddirectory.html)

[SearchDirectories](searchdirectories.html)

[SearchDirectory](searchdirectory.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-searchfiles.html language=enus -->
## TOPIC 00943: Engine.SearchFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-searchfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-searchfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SearchFiles( searchString, searchOptions, filterOptions, elementsToSearch, limitToAdapters, limitToNamedProps, limitToPropsOfNamedTypes, openFilesToSearch, directoriesAndFilePaths) Return Value SearchResults A SearchResults object. Purpose Begin a new find in files search. Remarks Retu

### Engine.SearchFiles

#### Syntax

[Engine](engine.html).SearchFiles( searchString, searchOptions, filterOptions, elementsToSearch, limitToAdapters, limitToNamedProps, limitToPropsOfNamedTypes, openFilesToSearch, directoriesAndFilePaths)

#### Return Value

[SearchResults](searchresults.html)

A SearchResults object.

#### Purpose

Begin a new find in files search.

#### Remarks

Returns a
 [SearchResults](searchresults.html)
 object that is a handle to the asynchronous search already in progress. To wait for the search to complete, call the
 [SearchResults.IsComplete](searchresults-iscomplete.html)
 method.

#### Parameters

searchString
 As
 [String](data-types-for-teststand.html)

[In] Pass the string or regular expression for which to search. To use regular expressions, you must specify
 [SearchOptions_RegExpr](searchoptions.html)
 for the
 searchOptions
 parameter.

searchOptions
 As
 [Long](data-types-for-teststand.html)

[In] Pass one or more
 [SearchOptions](searchoptions.html)
 constants. Use the bitwise-OR operator to specify multiple search options.

filterOptions
 As
 [Long](data-types-for-teststand.html)

[In] Pass one or more
 [SearchFilterOptions](searchfilteroptions.html)
 constants. Use the bitwise-OR operator to specify multiple search filter options.

elementsToSearch
 As
 [Long](data-types-for-teststand.html)

[In] Pass one or more
 [SearchElements](searchelements.html)
 constants. Use the bitwise-OR operator to specify multiple elements to search.

limitToAdapters
 As
 [String Array](data-types-for-teststand.html)

[In] Pass an array of
 [AdapterKeyNames](adapterkeynames.html)
 constants to indicate the steps of which adapters to search. Pass an empty array or
 NULL
 to search steps that use any adapter.

limitToNamedProps
 As
 [String Array](data-types-for-teststand.html)

[In] Pass an array of property names under which to limit the search. Pass an empty array or
 NULL
 to search all properties. If you specify names of properties to which to limit the search, TestStand searches only those properties with the names you specify and all their subproperties.

limitToPropsOfNamedTypes
 As
 [String Array](data-types-for-teststand.html)

[In] Pass an array of type names to which to limit the search. Pass an empty array or
 NULL
 to search instances of all types. Use this parameter to limit the search instances of all types. Use this parameter to limit the search to instances of the types you specify.

openFilesToSearch
 As
 [Object Array](data-types-for-teststand.html)

[In] Pass an array of PropertyObjectFile references to specify already open files in which to search. You can pass an empty array or
 NULL
 for this parameter.

directoriesAndFilePaths
 As
 [String Array](data-types-for-teststand.html)

[In] Pass an array of directories and/or file paths to indicate which files to load and search. All paths must be absolute paths. If you specify a directory, TestStand searches all sequence files under the directory and any of the subdirectories. You can pass an empty array or
 NULL
 for this parameter.

#### See Also

[AdapterKeyNames](adapterkeynames.html)

[PropertyObject.Search](propertyobject-search.html)

[SearchElements](searchelements.html)

[SearchFilterOptions](searchfilteroptions.html)

[SearchMatch](searchmatch.html)

[SearchOptions](searchoptions.html)

[SearchResults](searchresults.html)

[SearchResults.IsComplete](searchresults-iscomplete.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-secondsatstartin1970universalcoordinat.html language=enus -->
## TOPIC 00944: Engine.SecondsAtStartIn1970UniversalCoordinatedTime

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-secondsatstartin1970universalcoordinat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-secondsatstartin1970universalcoordinat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SecondsAtStartIn1970UniversalCoordinatedTime Data Type Double Purpose Returns the time in seconds at which the engine started since midnight (00:00:00), January 1, 1970, coordinated universal time (UTC). UTC is also known as Greenwich mean time. Remarks Some time values in TestStand, s

### Engine.SecondsAtStartIn1970UniversalCoordinatedTime

#### Syntax

[Engine](engine.html).SecondsAtStartIn1970UniversalCoordinatedTime

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the time in seconds at which the engine started since midnight (00:00:00), January 1, 1970, coordinated universal time (UTC). UTC is also known as Greenwich mean time.

#### Remarks

Some time values in TestStand, such as the
 TS.StartTime
 property of a step result, are in terms of seconds since the engine started. You can add the value of the
 Engine.SecondsAtStartIn1970UniversalCoordinatedTime
 property to these times to convert to a universal time base.

#### See Also

[Engine.SecondsSince1970UniversalCoordinatedTime](engine-secondssince1970universalcoordinatedti.html)

[Engine.SecondsSinceStart](engine-secondssincestart.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-secondssince1970universalcoordinatedti.html language=enus -->
## TOPIC 00945: Engine.SecondsSince1970UniversalCoordinatedTime

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-secondssince1970universalcoordinatedti.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-secondssince1970universalcoordinatedti.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SecondsSince1970UniversalCoordinatedTime Data Type Double Purpose Returns the time in seconds since midnight (00:00:00), January 1, 1970, coordinated universal time (UTC). UTC is also known as Greenwich mean time. See Also Engine.SecondsSinceStart

### Engine.SecondsSince1970UniversalCoordinatedTime

#### Syntax

[Engine](engine.html).SecondsSince1970UniversalCoordinatedTime

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the time in seconds since midnight (00:00:00), January 1, 1970, coordinated universal time (UTC). UTC is also known as Greenwich mean time.

#### See Also

[Engine.SecondsSinceStart](engine-secondssincestart.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-secondssincestart.html language=enus -->
## TOPIC 00946: Engine.SecondsSinceStart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-secondssincestart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-secondssincestart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SecondsSinceStart Data Type Double Purpose Returns the number of seconds since you created the engine. See Also Engine.SecondsSince1970UniversalCoordinatedTime

### Engine.SecondsSinceStart

#### Syntax

[Engine](engine.html).SecondsSinceStart

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the number of seconds since you created the engine.

#### See Also

[Engine.SecondsSince1970UniversalCoordinatedTime](engine-secondssince1970universalcoordinatedti.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-seqfileversionautoincrementopt.html language=enus -->
## TOPIC 00947: Engine.SeqFileVersionAutoIncrementOpt

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-seqfileversionautoincrementopt.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-seqfileversionautoincrementopt.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SeqFileVersionAutoIncrementOpt Data Type FileVersionAutoIncrement Use the following constants with this data type: FileVersionInc_Build –(Value: 4) Specifies that the build version number is incremented. FileVersionInc_Major –(Value: 1) Specifies that the major version number is increm

### Engine.SeqFileVersionAutoIncrementOpt

#### Syntax

[Engine](engine.html).SeqFileVersionAutoIncrementOpt

#### Data Type

[FileVersionAutoIncrement](fileversionautoincrement.html)

Use the following constants with this data type:

- FileVersionInc_Build 
 –(Value: 4) Specifies that the build version number is incremented.
- FileVersionInc_Major 
 –(Value: 1) Specifies that the major version number is incremented.
- FileVersionInc_Minor 
 –(Value: 2) Specifies that the minor version number is incremented.
- FileVersionInc_None 
 –(Value: 0) Specifies that sequence file versions are not automatically incremented.
- FileVersionInc_Revision 
 –(Value: 3) Specifies that the revision version number is incremented.

#### Purpose

Note

StationOptions.SeqFileVersionAutoIncrementOpt

#### Remarks

Specifies if sequence file versions are automatically incremented when the file is saved.

#### See Also

[StationOptions.SeqFileVersionAutoIncrementOpt](stationoptions-seqfileversionautoincrementopt.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-serializeobjects.html language=enus -->
## TOPIC 00948: Engine.SerializeObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-serializeobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-serializeobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SerializeObjects( objects, options = 0) Return Value String Returns the string that contains the serialized objects. Purpose Serializes PropertyObject objects into a string. Remarks This method converts one or more objects into a string that can be unserialized using the Engine.Unseria

### Engine.SerializeObjects

#### Syntax

[Engine](engine.html).SerializeObjects( objects, options = 0)

#### Return Value

[String](data-types-for-teststand.html)

Returns the string that contains the serialized objects.

#### Purpose

Serializes PropertyObject objects into a string.

#### Remarks

This method converts one or more objects into a string that can be unserialized using the
 [Engine.UnserializeObjects](engine-unserializeobjects.html)
 method. Typically, you use the SerializeObjects and
 Engine.UnserializeObjects
 methods to put TestStand data on the Microsoft Windows clipboard and to obtain data from it.

If you call this method on an alias object, TestStand generates the stream using the object to which the alias refers. This method does not include alias subproperty objects in the stream. Refer to
 [PropertyObject.IsAliasObject](propertyobject-isaliasobject.html)
 for more information about alias objects.

Use the
 [Engine.UnserializeObjectsAndTypes](engine-unserializeobjectsandtypes.html)
 method instead of
 Engine.UnserializeObjects
 if you intend to insert the array of property objects generated from the stream into a property object file. Also add the types the
 Engine.UnserializeObjectsAndTypes
 method returns to the file by calling the
 [TypeUsageList.Union](typeusagelist-union.html)
 method on the object the
 [PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)
 property returns. Pass the typesUsed output value as the
 unionTypeUsageList
 parameter to
 TypeUsageList.Union
 .

When you unserialize a step or a sequence, call the
 [Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)
 ,
 [Sequence.CreateNewUniqueStepIds](sequence-createnewuniquestepids.html)
 , or
 [Engine.CreateNewUniqueStepIds](engine-createnewuniquestepids.html)
 methods to replace the unique step ID with a new unique ID.

#### Parameters

objects
 As
 [Object Array](data-types-for-teststand.html)

[In] Pass the array of property objects to serialize.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specify one or more
 [SerializationOptions](serializationoptions.html)
 using a bitwise combination. This parameter specifies options for how you want to serialize the data. National Instruments recommends using the
 SerializationOption_UseBinary
 option for best performance and memory usage, unless you need to parse or read the data more easily. The
 [Engine.UnserializeObjects](engine-unserializeobjects.html)
 and
 [Engine.UnserializeObjectsAndTypes](engine-unserializeobjectsandtypes.html)
 methods always autodetect and unserialize the data appropriately.

This parameter has a default value of
 0
 .

#### See Also

[Engine.CreateNewUniqueStepIds](engine-createnewuniquestepids.html)

[Engine.UnserializeObjects](engine-unserializeobjects.html)

[Engine.UnserializeObjectsAndTypes](engine-unserializeobjectsandtypes.html)

[PropertyObject.IsAliasObject](propertyobject-isaliasobject.html)

[PropertyObject.Serialize](propertyobject-serialize.html)

[PropertyObject.UnserializeEx](propertyobject-unserializeex.html)

[PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)

[Sequence.CreateNewUniqueStepIds](sequence-createnewuniquestepids.html)

[SerializationOptions](serializationoptions.html)

[Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)

[TypeUsageList.Union](typeusagelist-union.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-setconfigdirectory.html language=enus -->
## TOPIC 00949: Engine.SetConfigDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-setconfigdirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-setconfigdirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SetConfigDirectory( Path, CopyFilesOnEngineShutdown) Purpose Specifies the pathname of the TestStand configuration directory. Remarks Changes to the TestStand configuration directory do not take effect until you have shut down the TestStand Engine. The configuration directory contains

### Engine.SetConfigDirectory

#### Syntax

[Engine](engine.html).SetConfigDirectory( Path, CopyFilesOnEngineShutdown)

#### Purpose

Specifies the pathname of the TestStand configuration directory.

#### Remarks

Changes to the TestStand configuration directory do not take effect until you have shut down the TestStand Engine.

The configuration directory contains engine and sequence editor option files, the users file, the globals file, and the tools menu file.

#### Parameters

Path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the new pathname where TestStand stores configuration files. You can pass an empty string to instruct TestStand to use the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg
 directory.

CopyFilesOnEngineShutdown
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether TestStand copies all files located in the current TestStand configuration directory to the new location upon shutdown.

#### See Also

[Engine.BinDirectory](engine-bindirectory.html)

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

[Engine.TestStandDirectory](engine-teststanddirectory.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-setinternaloption.html language=enus -->
## TOPIC 00950: Engine.SetInternalOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-setinternaloption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-setinternaloption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SetInternalOption( option, newValue) Purpose Specifies the value for the internal option the option parameter specifies. Remarks TestStand does not persist internal options between instances of the engine. Parameters option As InternalOptions [In] Specifies the internal option the meth

### Engine.SetInternalOption

#### Syntax

[Engine](engine.html).SetInternalOption( option, newValue)

#### Purpose

Specifies the value for the internal option the
 option
 parameter specifies.

#### Remarks

TestStand does not persist internal options between instances of the engine.

#### Parameters

option
 As
 [InternalOptions](internaloptions.html)

[In] Specifies the internal option the method sets.

newValue
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the value of the internal option the
 option
 parameter specifies.

#### See Also

[Engine.GetInternalOption](engine-getinternaloption.html)

[InternalOptions](internaloptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-setlocationfornextdialog.html language=enus -->
## TOPIC 00951: Engine.SetLocationForNextDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-setlocationfornextdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-setlocationfornextdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SetLocationForNextDialog( locationLookupString, elementAtLocation, selectionStart, selectionLength) Purpose Sets the location of the control in a dialog box that edits the property you specify. When you launch the dialog box again, the control associated with the location is selected a

### Engine.SetLocationForNextDialog

#### Syntax

[Engine](engine.html).SetLocationForNextDialog( locationLookupString, elementAtLocation, selectionStart, selectionLength)

#### Purpose

Sets the location of the control in a dialog box that edits the property you specify. When you launch the dialog box again, the control associated with the location is selected and highlighted. The following methods launch dialog boxes that support this feature:
 [PropertyObject.DisplayAttributesDialog](propertyobject-displayattributesdialog.html)
 ,
 [PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)
 ,
 [Step.SpecifyModule](step-specifymodule.html)
 ,
 [StepType.SpecifyModule](steptype-specifymodule.html)
 ,
 [Engine.DisplayEditUserDialog](engine-displayedituserdialog.html)
 ,
 [Engine.DisplayStepPropDialog](engine-displaysteppropdialog.html)
 ,
 [Engine.DisplaySequencePropDialog](engine-displaysequencepropdialog.html)
 ,
 [Engine.DisplaySeqFilePropDialog](engine-displayseqfilepropdialog.html)
 ,
 [Engine.DisplayPreconditionDialog](engine-displaypreconditiondialog.html)
 .

#### Parameters

locationLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the subproperty of the object that specifies the corresponding control that is highlighted in the dialog box the next time it is launched.

elementAtLocation
 As
 [Long](data-types-for-teststand.html)

[In] Pass one of the following
 [SearchElements](searchelements.html)
 constants to indicate which part of the property you want to highlight in the dialog box while editing:
 SearchElement_Name
 ,
 SearchElement_Comment
 ,
 SearchElement_StringValue
 ,
 SearchElement_NumericValue
 , or
 SearchElement_BooleanValue
 . For example, to highlight a portion of a local variable comment, pass an empty string for the
 locationLookupString
 parameter and
 SearchElement_Comment
 for this parameter, then call
 PropertyObject.DisplayPropertiesDialog
 on the variable property.

selectionStart
 As
 [Long](data-types-for-teststand.html)

[In] If the control the
 locationLookupString
 and
 elementAtLocation
 parameters indicate is an Edit control, you can use this parameter to select a particular section of the text within the control when TestStand launches the dialog box. Pass the index of the character within the string where you want the selection to start.

selectionLength
 As
 [Long](data-types-for-teststand.html)

[In] If the control the
 locationLookupString
 and
 elementAtLocation
 parameters specify is an Edit control, you can use this parameter to select a particular section of the text within the control when TestStand launches the dialog box. Starting from the selStartIndex character, pass the numbers of characters you want the dialog box to select in the Edit control.

#### See Also

[Engine.DisplayEditUserDialog](engine-displayedituserdialog.html)

[Engine.DisplayPreconditionDialog](engine-displaypreconditiondialog.html)

[Engine.DisplaySeqFilePropDialog](engine-displayseqfilepropdialog.html)

[Engine.DisplaySequencePropDialog](engine-displaysequencepropdialog.html)

[Engine.DisplayStepPropDialog](engine-displaysteppropdialog.html)

[Engine.GetLocationForNextDialog](engine-getlocationfornextdialog.html)

[PropertyObject.DisplayAttributesDialog](propertyobject-displayattributesdialog.html)

[PropertyObject.DisplayPropertiesDialog](propertyobject-displaypropertiesdialog.html)

[SearchElements](searchelements.html)

[Step.SpecifyModule](step-specifymodule.html)

[StepType.SpecifyModule](steptype-specifymodule.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-setmoduleprofiling.html language=enus -->
## TOPIC 00952: Engine.SetModuleProfiling

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-setmoduleprofiling.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-setmoduleprofiling.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SetModuleProfiling( adapterKeyName, enabled) Purpose Specifies whether the profiler collects timing information about code modules the specified adapter loads and executes. Parameters adapterKeyName As String [In] Specifies which adapter for which to enable or disable profiler data col

### Engine.SetModuleProfiling

#### Syntax

[Engine](engine.html).SetModuleProfiling( adapterKeyName, enabled)

#### Purpose

Specifies whether the profiler collects timing information about code modules the specified adapter loads and executes.

#### Parameters

adapterKeyName
 As
 [String](data-types-for-teststand.html)

[In] Specifies which adapter for which to enable or disable profiler data collection. Pass an empty string to enable or disable profiling for all adapters.

enabled
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to enable or disable profiler data collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-setproductregistrationinfo.html language=enus -->
## TOPIC 00953: Engine.SetProductRegistrationInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-setproductregistrationinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-setproductregistrationinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SetProductRegistrationInfo( userName, companyName, serialNumber) Return Value Boolean Returns False Purpose This method is obsolete. The National Instruments License Manager sets user registration information when you activate TestStand. Remarks Sets the product registration informatio

### Engine.SetProductRegistrationInfo

#### Syntax

[Engine](engine.html).SetProductRegistrationInfo( userName, companyName, serialNumber)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 False

#### Purpose

Note

#### Remarks

Sets the product registration information for this installation of TestStand.

This method sets the information that you entered in the TestStand Product Registration dialog box, which launches the first time you launch the sequence editor after installation.

#### Parameters

userName
 As
 [String](data-types-for-teststand.html)

[In] This parameter is obsolete and no longer supported.

companyName
 As
 [String](data-types-for-teststand.html)

[In] This parameter is obsolete and no longer supported.

serialNumber
 As
 [String](data-types-for-teststand.html)

[In] This parameter is obsolete and no longer supported.

#### See Also

[Engine.GetLicenseDescription](engine-getlicensedescription.html)

[Engine.GetProductRegistrationInfo](engine-getproductregistrationinfo.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-settypepalettefilelist.html language=enus -->
## TOPIC 00954: Engine.SetTypePaletteFileList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-settypepalettefilelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-settypepalettefilelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SetTypePaletteFileList( typePaletteFiles) Purpose Sets the list of currently loaded type palette files in the TestStand Engine. Remarks Type palette files contain step type and data type definitions. The TestStand Engine loads these files when the sequence editor and user interfaces la

### Engine.SetTypePaletteFileList

#### Syntax

[Engine](engine.html).SetTypePaletteFileList( typePaletteFiles)

#### Purpose

Sets the list of currently loaded type palette files in the TestStand Engine.

#### Remarks

Type palette files contain step type and data type definitions. The TestStand Engine loads these files when the sequence editor and user interfaces launch. Call this method to change the list of loaded type palettes. If the TestStand Engine already has type palette files loaded and they are not in the new list, TestStand unloads the files.

#### Parameters

typePaletteFiles
 As
 [Object Array](data-types-for-teststand.html)

[In] Specifies an array of pointers to the PropertyObjectFile interfaces of the type palette files. Build the array by calling the
 [Engine.NewPropertyObjectFile](engine-newpropertyobjectfile.html)
 and
 [PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)
 methods for each type palette.

#### See Also

[Engine.GetTypePaletteFileList](engine-gettypepalettefilelist.html)

[Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)

[Engine.NewPropertyObjectFile](engine-newpropertyobjectfile.html)

[Engine.UnloadTypePaletteFiles](engine-unloadtypepalettefiles.html)

[PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-shouldautolaunchexternalreportviewer.html language=enus -->
## TOPIC 00955: Engine.ShouldAutoLaunchExternalReportViewer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-shouldautolaunchexternalreportviewer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-shouldautolaunchexternalreportviewer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ShouldAutoLaunchExternalReportViewer( FilePath) Return Value Boolean Returns True if the user interface launches the external viewer. Purpose Returns a value that indicates whether the user interface automatically launches an external report viewer when an execution finishes. Remarks T

### Engine.ShouldAutoLaunchExternalReportViewer

#### Syntax

[Engine](engine.html).ShouldAutoLaunchExternalReportViewer( FilePath)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the user interface launches the external viewer.

#### Purpose

Returns a value that indicates whether the user interface automatically launches an external report viewer when an execution finishes.

#### Remarks

This method uses the report file extension and the external viewer configuration options to determine whether the user interface automatically launches the report viewer.

#### Parameters

FilePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the report file path. This method uses only the file extension of the parameter.

#### See Also

[Engine.DisplayExternalViewerDialog](engine-displayexternalviewerdialog.html)

[ExternalReportViewer.AutoLaunch](externalreportviewer-autolaunch.html)

[ExternalReportViewers](externalreportviewers.html)

[ExternalReportViewers.AutoLaunchDefaultExternalViewers](externalreportviewers-autolaunchdefaultextern.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-showhiddenproperties.html language=enus -->
## TOPIC 00956: Engine.ShowHiddenProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-showhiddenproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-showhiddenproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ShowHiddenProperties Data Type Boolean Purpose This property is obsolete. Use the StationOptions.ShowHiddenProperties property instead. Remarks Specifies whether to display in user interfaces properties marked as hidden. When this property is True , the sequence editor and user interfa

### Engine.ShowHiddenProperties

#### Syntax

[Engine](engine.html).ShowHiddenProperties

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.ShowHiddenProperties

#### Remarks

Specifies whether to display in user interfaces properties marked as hidden.

When this property is
 True
 , the sequence editor and user interfaces display all subproperties of property objects in dialog boxes and variables views. When this property is
 False
 , the sequence editor does not show subproperties marked with the
 [PropFlags_Hidden](propertyflags.html)
 flag.

#### See Also

[PropertyFlags](propertyflags.html)

[PropertyObject.GetFlags](propertyobject-getflags.html)

[StationOptions.ShowHiddenProperties](stationoptions-showhiddenproperties.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-shutdown.html language=enus -->
## TOPIC 00957: Engine.ShutDown

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-shutdown.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ShutDown( final) Purpose Attempts to close all open sequence files and terminate all executions. Remarks If you are writing a user interface that does not use the TestStand User Interface (UI) Controls, call this function before exiting the application. TestStand sends a UIMsg_ShutDown

### Engine.ShutDown

#### Syntax

[Engine](engine.html).ShutDown( final)

#### Purpose

Attempts to close all open sequence files and terminate all executions.

#### Remarks

If you are writing a user interface that does not use the TestStand User Interface (UI) Controls, call this function before exiting the application.

TestStand sends a
 [UIMsg_ShutDownComplete](uimessagecodes.html)
 message to notify you when the
 [shut down](/csh?context=ts_tsapiref_app_shutting_down_the_engine)
 is complete.

#### Parameters

final
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 when performing the final shutdown before exiting the application. Passing
 False
 permits the user to cancel shutdown when executions are running.

#### See Also

[Shutting Down the Engine](/csh?context=ts_tsapiref_app_shutting_down_the_engine)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-smallimagelist.html language=enus -->
## TOPIC 00958: Engine.SmallImageList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-smallimagelist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-smallimagelist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SmallImageList Data Type Long Purpose This property is obsolete. Use the Engine.SmallImageListEx property instead. Calling this property on a 64-bit instance of the TestStand Engine results in an error. Remarks Returns the Microsoft Windows handle for the TestStand list of small images

### Engine.SmallImageList

#### Syntax

[Engine](engine.html).SmallImageList

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

Engine.SmallImageListEx

#### Remarks

Returns the Microsoft Windows handle for the TestStand list of small images.

The TestStand Engine maintains lists of images for all the icons from the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 "<TestStand Public>\Components\Icons
 directories and images you add using the
 [Engine.AddImage](engine-addimage.html)
 method. TestStand separates the images according to size and places each image in the list of large images or in the list of small images.

This method returns a Windows handle, HIMAGELIST, for the list of small images. You can use the image list functions in the Microsoft Windows Platform Software Development Kit to access the images in the list. Use this property as an alternative to using the
 [Images](images.html)
 collection.

Note

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.GetImageIndex](engine-getimageindex.html)

[Engine.GetImageName](engine-getimagename.html)

[Engine.LargeImageList](engine-largeimagelist.html)

[Engine.NumImages](engine-numimages.html)

[Images](images.html)

[Step.SmallIconIndex](step-smalliconindex.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-smallimagelistex.html language=enus -->
## TOPIC 00959: Engine.SmallImageListEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-smallimagelistex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-smallimagelistex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.SmallImageListEx Data Type Variant Purpose Returns the Microsoft Windows handle for the TestStand list of small images. Remarks The TestStand Engine maintains lists of images for all the icons from the <TestStand> \Components\Icons and "<TestStand Public>\Components\Icons directories a

### Engine.SmallImageListEx

#### Syntax

[Engine](engine.html).SmallImageListEx

#### Data Type

[Variant](data-types-for-teststand.html)

#### Purpose

Returns the Microsoft Windows handle for the TestStand list of small images.

#### Remarks

The TestStand Engine maintains lists of images for all the icons from the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 "<TestStand Public>\Components\Icons
 directories and images you add using the
 [Engine.AddImage](engine-addimage.html)
 method. TestStand separates the images according to size and places each image in the list of large images or in the list of small images.

This method returns a Windows handle, HIMAGELIST, for the list of small images. The type of the variant matches the architecture of the TestStand Engine, for example,
 VT_UI4
 for 32-bit TestStand and
 VT_UI8
 for 64-bit TestStand. You can use the image list functions in the Microsoft Windows Platform Software Development Kit to access the images in the list. Use this property as an alternative to using the
 [Images](images.html)
 collection.

Note

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.GetImageIndex](engine-getimageindex.html)

[Engine.GetImageName](engine-getimagename.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Engine.NumImages](engine-numimages.html)

[Images](images.html)

[Step.SmallIconIndex](step-smalliconindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-stationid.html language=enus -->
## TOPIC 00960: Engine.StationID

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-stationid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-stationid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.StationID Data Type String Purpose This property is obsolete. Use the StationOptions.StationID property instead. Remarks Specifies a test station identification string for this instance of the TestStand Engine. This property never returns an empty string. If you set this property to an

### Engine.StationID

#### Syntax

[Engine](engine.html).StationID

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.StationID

#### Remarks

Specifies a test station identification string for this instance of the TestStand Engine.

Note

Engine.ComputerName

#### See Also

[Engine.ComputerName](engine-computername.html)

[StationOptions.StationID](stationoptions-stationid.html)

[UniqueEngineId](engine-uniqueengineid.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-stationmodelsequencefilepath.html language=enus -->
## TOPIC 00961: Engine.StationModelSequenceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-stationmodelsequencefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-stationmodelsequencefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.StationModelSequenceFilePath Data Type String Purpose This property is obsolete. Use the StationOptions.StationModelSequenceFilePath property instead. Remarks Specifies the pathname of the station model sequence file. This property is a relative pathname. TestStand uses the Engine.Find

### Engine.StationModelSequenceFilePath

#### Syntax

[Engine](engine.html).StationModelSequenceFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.StationModelSequenceFilePath

#### Remarks

Specifies the pathname of the station model sequence file.

Note

Engine.FindFileEx

#### See Also

[Engine.FindFileEx](engine-findfileex.html)

[StationOptions.StationModelSequenceFilePath](stationoptions-stationmodelsequencefilepath.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-stationoptions.html language=enus -->
## TOPIC 00962: Engine.StationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-stationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-stationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.StationOptions Data Type StationOptions Purpose Returns a reference to the StationOptions object. Remarks Use the StationOptions object to set preferences for the TestStand station. Station option settings affect all sequence editor and user interface sessions you run on the computer.

### Engine.StationOptions

#### Syntax

[Engine](engine.html).StationOptions

#### Data Type

[StationOptions](stationoptions.html)

#### Purpose

Returns a reference to the StationOptions object.

#### Remarks

Use the StationOptions object to set preferences for the TestStand station. Station option settings affect all sequence editor and user interface sessions you run on the computer.

#### See Also

[StationOptions](stationoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-steptypes.html language=enus -->
## TOPIC 00963: Engine.StepTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-steptypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-steptypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.StepTypes Data Type PropertyObject Purpose This property is obsolete. Use the Engine.GetTypeNames and Engine.GetTypeDefinition properties instead. Remarks If you attempt to read this property, TestStand returns an error. See Also Engine.GetTypeDefinition Engine.GetTypeNames PropertyObj

### Engine.StepTypes

#### Syntax

[Engine](engine.html).StepTypes

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Note

Engine.GetTypeNames

Engine.GetTypeDefinition

#### Remarks

If you attempt to read this property, TestStand returns an error.

#### See Also

[Engine.GetTypeDefinition](engine-gettypedefinition.html)

[Engine.GetTypeNames](engine-gettypenames.html)

[PropertyObject](propertyobject.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-temporaryglobals.html language=enus -->
## TOPIC 00964: Engine.TemporaryGlobals

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-temporaryglobals.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-temporaryglobals.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.TemporaryGlobals Data Type PropertyObject Purpose Creates and accesses global variables that you want to exist only for the current run of the TestStand Engine. Remarks These globals differ from those you access with the Engine.Globals property in that TestStand never writes these glob

### Engine.TemporaryGlobals

#### Syntax

[Engine](engine.html).TemporaryGlobals

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Creates and accesses global variables that you want to exist only for the current run of the TestStand Engine.

#### Remarks

These globals differ from those you access with the
 [Engine.Globals](engine-globals.html)
 property in that TestStand never writes these globals to disk.

#### See Also

[Engine.Globals](engine-globals.html)

[Execution.RunTimeVariables](execution-runtimevariables.html)

[PropertyObject](propertyobject.html)

[Thread.RunTimeVariables](thread-runtimevariables.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-terminateall.html language=enus -->
## TOPIC 00965: Engine.TerminateAll

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-terminateall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-terminateall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.TerminateAll Purpose Terminates all existing executions. See Also Engine.AbortAll Engine.BreakAll Execution.CancelTermination Execution.Terminate

### Engine.TerminateAll

#### Syntax

[Engine](engine.html).TerminateAll

#### Purpose

Terminates all existing executions.

#### See Also

[Engine.AbortAll](engine-abortall.html)

[Engine.BreakAll](engine-breakall.html)

[Execution.CancelTermination](execution-canceltermination.html)

[Execution.Terminate](execution-terminate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-teststanddirectory.html language=enus -->
## TOPIC 00966: Engine.TestStandDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-teststanddirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-teststanddirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.TestStandDirectory Data Type String Purpose This property is obsolete. Use the Engine.GetTestStandPath method instead. Remarks Returns the pathname of the directory in which you installed TestStand. The pathname does not contain a trailing backslash. See Also Engine.BinDirectory Engine

### Engine.TestStandDirectory

#### Syntax

[Engine](engine.html).TestStandDirectory

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Engine.GetTestStandPath

#### Remarks

Returns the pathname of the directory in which you installed TestStand. The pathname does not contain a trailing backslash.

#### See Also

[Engine.BinDirectory](engine-bindirectory.html)

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.GetTestStandPath](engine-getteststandpath.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-tracingenabled.html language=enus -->
## TOPIC 00967: Engine.TracingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-tracingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-tracingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.TracingEnabled Data Type Boolean Purpose This property is obsolete. Use the StationOptions.TracingEnabled property instead. Remarks Specifies if tracing is enabled for sequence editors and user interfaces. See Also Execution.TracingDisabled StationOptions.BreakpointsEnabled StationOpti

### Engine.TracingEnabled

#### Syntax

[Engine](engine.html).TracingEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.TracingEnabled

#### Remarks

Specifies if tracing is enabled for sequence editors and user interfaces.

#### See Also

[Execution.TracingDisabled](execution-tracingdisabled.html)

[StationOptions.BreakpointsEnabled](stationoptions-breakpointsenabled.html)

[StationOptions.TracingEnabled](stationoptions-tracingenabled.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-uimessagedelay.html language=enus -->
## TOPIC 00968: Engine.UIMessageDelay

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-uimessagedelay.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-uimessagedelay.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UIMessageDelay Data Type Long Purpose This property is obsolete. Use the StationOptions.UIMessageDelay property instead. Remarks Specifies how many milliseconds must pass between postings of UIMsg_Trace events. Set this property to specify how many milliseconds must pass before you rec

### Engine.UIMessageDelay

#### Syntax

[Engine](engine.html).UIMessageDelay

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.UIMessageDelay

#### Remarks

Specifies how many milliseconds must pass between postings of
 UIMsg_Trace
 events.

Set this property to specify how many milliseconds must pass before you receive the next
 UIMsg_Trace
 event. Use this property to slow down the posting of trace messages to the sequence editor or user interface to allow time for processing mouse events and/or to display the trace of an execution more slowly.

Note

Engine.UIMessageMinDelay

#### See Also

[Engine.GetUIMessage](engine-getuimessage.html)

[Engine.RegisterUIMessageCallbackEx](engine-registeruimessagecallbackex.html)

[Engine.UIMessageEvent](engine-uimessageevent.html)

[Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)

[StationOptions.UIMessageDelay](stationoptions-uimessagedelay.html)

[UIMessage](uimessage.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-uimessageevent.html language=enus -->
## TOPIC 00969: Engine.UIMessageEvent

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-uimessageevent.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-uimessageevent.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ControlName_UIMessageEvent( msg) Applies To Engine Purpose Handles user interface message events as ActiveX events. Remarks You must implement this method if you are writing a user interface and you want to receive UIMessages as ActiveX events. If you are using the TestStand ActiveX control i

### Engine.UIMessageEvent

#### Syntax

ControlName_UIMessageEvent( msg)

#### Applies To

[Engine](engine.html)

#### Purpose

Handles user interface message events as ActiveX events.

#### Remarks

You must implement this method if you are writing a user interface and you want to receive UIMessages as ActiveX events. If you are using the TestStand ActiveX control in Microsoft Visual Basic, double-click the TestStand control icon on the form to implement the ActiveX event callback.

#### Parameters

msg
 As
 [UIMessage](uimessage.html)

[In] The user interface message that TestStand passes to the event.

#### See Also

[Engine.GetUIMessage](engine-getuimessage.html)

[Engine.RegisterUIMessageCallback](engine-registeruimessagecallback.html)

[Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)

[StationOptions.UIMessageDelay](stationoptions-uimessagedelay.html)

[StationOptions.UIMessageMinDelay](stationoptions-uimessagemindelay.html)

[UIMessage](uimessage.html)

Parent topic:

Events

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-uimessagemindelay.html language=enus -->
## TOPIC 00970: Engine.UIMessageMinDelay

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-uimessagemindelay.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-uimessagemindelay.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UIMessageMinDelay Data Type Long Purpose This property is obsolete. Use the StationOptions.UIMessageMinDelay property instead. Remarks Specifies the minimum value allowed for the Engine.UIMessageDelay property. Use this property to specify the minimum value allowed for the UIMessageDel

### Engine.UIMessageMinDelay

#### Syntax

[Engine](engine.html).UIMessageMinDelay

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.UIMessageMinDelay

#### Remarks

Specifies the minimum value allowed for the
 Engine.UIMessageDelay
 property.

Use this property to specify the minimum value allowed for the
 UIMessageDelay
 property for the sequence editor or user interface.

#### See Also

[Engine.GetUIMessage](engine-getuimessage.html)

[Engine.RegisterUIMessageCallback](engine-registeruimessagecallback.html)

[Engine.UIMessageEvent](engine-uimessageevent.html)

[Engine.UIMessagePollingEnabled](engine-uimessagepollingenabled.html)

[StationOptions.UIMessageMinDelay](stationoptions-uimessagemindelay.html)

[UIMessage](uimessage.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-uimessagepollingenabled.html language=enus -->
## TOPIC 00971: Engine.UIMessagePollingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-uimessagepollingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-uimessagepollingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UIMessagePollingEnabled Data Type Boolean Purpose Specifies if user interface message polling is enabled. Remarks Default value is False . Set this property to True when writing a user interface which uses polling rather than events to obtain UIMessages from TestStand. To poll, call th

### Engine.UIMessagePollingEnabled

#### Syntax

[Engine](engine.html).UIMessagePollingEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if user interface message polling is enabled.

#### Remarks

Default value is
 False
 .

Set this property to
 True
 when writing a user interface which uses polling rather than events to obtain UIMessages from TestStand.

To poll, call the
 [Engine.IsUIMessageQueueEmpty](engine-isuimessagequeueempty.html)
 property. If
 IsUIMessageQueueEmpty
 returns
 False
 , call the
 [Engine.GetUIMessage](engine-getuimessage.html)
 method to retrieve the next
 [UIMessage](uimessage.html)
 . If your development environment requires you to explicitly release COM references, release the COM reference to the previous user interface message before obtaining the next one.

Note

True

#### See Also

[Engine.GetUIMessage](engine-getuimessage.html)

[Engine.IsUIMessageQueueEmpty](engine-isuimessagequeueempty.html)

[Engine.RegisterUIMessageCallbackEx](engine-registeruimessagecallbackex.html)

[Engine.UIMessageEvent](engine-uimessageevent.html)

[Setting Up a User Interface Message Handler](/csh?context=ts_tsapiref_app_set_up_uimsg_handler)

[StationOptions.UIMessageDelay](stationoptions-uimessagedelay.html)

[StationOptions.UIMessageMinDelay](stationoptions-uimessagemindelay.html)

[UIMessage](uimessage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-undolimit.html language=enus -->
## TOPIC 00972: Engine.UndoLimit

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-undolimit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-undolimit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UndoLimit Data Type Long Purpose Specifies the maximum number of undo items an UndoStack can contain. The default value is -1 , which means no limit exists to the number of undo items an UndoStack can contain. Remarks Setting this property does not remove undo items from UndoStacks. Wh

### Engine.UndoLimit

#### Syntax

[Engine](engine.html).UndoLimit

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the maximum number of undo items an
 [UndoStack](undostack.html)
 can contain. The default value is
 -1
 , which means no limit exists to the number of undo items an UndoStack can contain.

#### Remarks

Setting this property does not remove undo items from UndoStacks. When you push an undo item onto an UndoStack, the UndoStack removes the oldest undo items from the UndoStack so that the number of items on the UndoStack does not exceed the UndoLimit.

The Engine initializes this property to
 -1
 . The Engine does not persist the value of this property.

#### See Also

[UndoStack](undostack.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-uniqueengineid.html language=enus -->
## TOPIC 00973: Engine.UniqueEngineId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-uniqueengineid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-uniqueengineid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UniqueEngineId Data Type String Purpose Returns an identification string that is unique among all instances of the TestStand Engine. Remarks Use this string to uniquely identify a particular instance of an engine. The returned string is a representation of a UUID or GUID, such as " 6B2

### Engine.UniqueEngineId

#### Syntax

[Engine](engine.html).UniqueEngineId

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns an identification string that is unique among all instances of the TestStand Engine.

#### Remarks

Use this string to uniquely identify a particular instance of an engine. The returned string is a representation of a UUID or GUID, such as "
 6B29FC40-CA47-1067-B31D-00DD010662DA
 ."

#### See Also

[Engine.ComputerName](engine-computername.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-unloadallmodules.html language=enus -->
## TOPIC 00974: Engine.UnloadAllModules

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-unloadallmodules.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-unloadallmodules.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UnloadAllModules Purpose Unloads all code modules associated with steps, step types, and substeps. Remarks Call this method to force all modules to be unloaded and then reloaded when they are next called so you can rebuild DLLs and other code modules. This method also unloads the stati

### Engine.UnloadAllModules

#### Syntax

[Engine](engine.html).UnloadAllModules

#### Purpose

Unloads all code modules associated with steps, step types, and substeps.

#### Remarks

Call this method to force all modules to be unloaded and then reloaded when they are next called so you can rebuild DLLs and other code modules. This method also unloads the station model sequence file. Typically, you only call this method when no executions are running.

#### See Also

[Sequence.UnloadModules](sequence-unloadmodules.html)

[SequenceFile.UnloadModules](sequencefile-unloadmodules.html)

[Step.UnloadModule](step-unloadmodule.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-unloadtypepalettefiles.html language=enus -->
## TOPIC 00975: Engine.UnloadTypePaletteFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-unloadtypepalettefiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-unloadtypepalettefiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UnloadTypePaletteFiles Purpose Unloads the TestStand Engine list of type palette files. Remarks Type palette files contain step type and data type definitions. UnloadTypePaletteFiles is the method the sequence editor and user interfaces call on the TestStand Engine to unload these file

### Engine.UnloadTypePaletteFiles

#### Syntax

[Engine](engine.html).UnloadTypePaletteFiles

#### Purpose

Unloads the TestStand Engine list of type palette files.

#### Remarks

Type palette files contain step type and data type definitions.
 UnloadTypePaletteFiles
 is the method the sequence editor and user interfaces call on the TestStand Engine to unload these files when they exit. If the
 [Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)
 method was previously called, call this method to unload the type palette files.

#### See Also

[Engine.GetTypePaletteFileList](engine-gettypepalettefilelist.html)

[Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)

[Engine.SetTypePaletteFileList](engine-settypepalettefilelist.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-unregistermodalwindow.html language=enus -->
## TOPIC 00976: Engine.UnregisterModalWindow

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-unregistermodalwindow.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-unregistermodalwindow.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UnregisterModalWindow( modalID) Purpose Notifies TestStand that the specified window is no longer a modal dialog box. Remarks Call this method when a dialog box you registered with the Engine.RegisterModalWindow method closes. Parameters modalID As Long [In] Pass the modalID you receiv

### Engine.UnregisterModalWindow

#### Syntax

[Engine](engine.html).UnregisterModalWindow( modalID)

#### Purpose

Notifies TestStand that the specified window is no longer a modal dialog box.

#### Remarks

Call this method when a dialog box you registered with the
 [Engine.RegisterModalWindow](engine-registermodalwindow.html)
 method closes.

#### Parameters

modalID
 As
 [Long](data-types-for-teststand.html)

[In] Pass the modalID you receive as a return value from the
 [Engine.RegisterModalWindow](engine-registermodalwindow.html)
 .

#### See Also

[Engine.NotifyEndOfModalDialog](engine-notifyendofmodaldialog.html)

[Engine.NotifyStartOfModalDialogEx](engine-notifystartofmodaldialogex.html)

[Engine.RegisterModalWindow](engine-registermodalwindow.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-unregistersequencetoexecuteoncrash.html language=enus -->
## TOPIC 00977: Engine.UnregisterSequenceToExecuteOnCrash

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-unregistersequencetoexecuteoncrash.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-unregistersequencetoexecuteoncrash.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UnregisterSequenceToExecuteOnCrash( registrationId) Purpose Unregisters the sequence to execute on TestStand application crash. Parameters registrationId As Long [In] Pass the registrationId you receive as the return value from Engine.RegisterSequenceToExecuteOnCrash method. See Also C

### Engine.UnregisterSequenceToExecuteOnCrash

#### Syntax

[Engine](engine.html).UnregisterSequenceToExecuteOnCrash( registrationId)

#### Purpose

Unregisters the sequence to execute on TestStand application crash.

#### Parameters

registrationId
 As
 [Long](data-types-for-teststand.html)

[In] Pass the registrationId you receive as the return value from
 Engine.RegisterSequenceToExecuteOnCrash
 method.

#### See Also

[CrashCallbackOptions](crashcallbackoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-unserializeobjects.html language=enus -->
## TOPIC 00978: Engine.UnserializeObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-unserializeobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-unserializeobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UnserializeObjects( stream, reservedParam = 0, handlerType = ConflictHandler_Error) Return Value Object Array Returns the array of unserialized property objects. Purpose Converts a string of serialized objects into an array of PropertyObjects. Remarks Call this method to convert the re

### Engine.UnserializeObjects

#### Syntax

[Engine](engine.html).UnserializeObjects( stream, reservedParam = 0, handlerType = ConflictHandler_Error)

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns the array of unserialized property objects.

#### Purpose

Converts a string of serialized objects into an array of PropertyObjects.

#### Remarks

Call this method to convert the return value of the
 [Engine.SerializeObjects](engine-serializeobjects.html)
 method into an array of objects. Typically, you use the
 Engine.SerializeObjects
 method and this method to put TestStand data on the Microsoft Windows clipboard and to obtain data from it.

Use the
 [Engine.UnserializeObjectsAndTypes](engine-unserializeobjectsandtypes.html)
 method instead of this method if you intend to insert the array of property objects generated from the stream into a property object file. Also add the types the
 Engine.UnserializeObjectsAndTypes
 method returns to the file. You can add the types to the file by calling the
 [TypeUsageList.Union](typeusagelist-union.html)
 method on the object the
 [PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)
 property returns. Pass the
 typesUsed
 output value as the
 unionTypeUsageList
 parameter to
 TypeUsageList.Union
 .

When you unserialize a step or a sequence, call the
 [Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)
 ,
 [Sequence.CreateNewUniqueStepIds](sequence-createnewuniquestepids.html)
 , or
 [Engine.CreateNewUniqueStepIds](engine-createnewuniquestepids.html)
 method to replace the unique step ID with a new unique ID.

#### Parameters

stream
 As
 [String](data-types-for-teststand.html)

[In] Specifies the serialized objects the
 [Engine.SerializeObjects](engine-serializeobjects.html)
 method creates.

reservedParam
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 .

This parameter has a default value of
 0
 .

handlerType
 As
 [TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[In] Specifies how to handle type conflicts in the stream.

This parameter has a default value of
 ConflictHandler_Error
 .

#### See Also

[Engine.CreateNewUniqueStepIds](engine-createnewuniquestepids.html)

[Engine.SerializeObjects](engine-serializeobjects.html)

[Engine.UnserializeObjectsAndTypes](engine-unserializeobjectsandtypes.html)

[PropertyObject.Serialize](propertyobject-serialize.html)

[PropertyObject.UnserializeEx](propertyobject-unserializeex.html)

[PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)

[Sequence.CreateNewUniqueStepIds](sequence-createnewuniquestepids.html)

[Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)

[TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[TypeUsageList.Union](typeusagelist-union.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-unserializeobjectsandtypes.html language=enus -->
## TOPIC 00979: Engine.UnserializeObjectsAndTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-unserializeobjectsandtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-unserializeobjectsandtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UnserializeObjectsAndTypes( stream, typesUsed, reservedParam = 0, handlerType = ConflictHandler_Error) Return Value Object Array Returns the array of unserialized property objects. Purpose Converts a string of serialized objects into an array of property objects and a TypeUsageList tha

### Engine.UnserializeObjectsAndTypes

#### Syntax

[Engine](engine.html).UnserializeObjectsAndTypes( stream, typesUsed, reservedParam = 0, handlerType = ConflictHandler_Error)

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns the array of unserialized property objects.

#### Purpose

Converts a string of serialized objects into an array of property objects and a TypeUsageList that contains types the PropertyObjects use.

#### Remarks

Call this method to convert the return value of the
 [Engine.SerializeObjects](engine-serializeobjects.html)
 method into an array of property objects and a list of types. Typically, you use the
 Engine.SerializeObjects
 and
 [Engine.UnserializeObjects](engine-unserializeobjects.html)
 methods to put TestStand data on the Microsoft Windows clipboard and to obtain data from it.

If you insert the array of property objects this method returns into a property object file, add the types it uses to the file. You can also add the types to the file by calling the
 [TypeUsageList.Union](typeusagelist-union.html)
 method on the object the
 [PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)
 property returns. Pass the typesUsed output value as the
 unionTypeUsageList
 parameter to
 TypeUsageList.Union
 .

When you unserialize a step or a sequence, call the
 [Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)
 ,
 [Sequence.CreateNewUniqueStepIds](sequence-createnewuniquestepids.html)
 , or
 [Engine.CreateNewUniqueStepIds](engine-createnewuniquestepids.html)
 method to replace the unique step ID with a new unique ID.

#### Parameters

stream
 As
 [String](data-types-for-teststand.html)

[In] Specifies the serialized objects the
 [Engine.SerializeObjects](engine-serializeobjects.html)
 method creates.

typesUsed
 As
 [TypeUsageList](typeusagelist.html)

[Out] Returns the list of types the serialized objects use.

reservedParam
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 .

This parameter has a default value of
 0
 .

handlerType
 As
 [TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[In] Specifies how to handle type conflicts in the stream.

This parameter has a default value of
 ConflictHandler_Error
 .

#### See Also

[Engine.CreateNewUniqueStepIds](engine-createnewuniquestepids.html)

[Engine.SerializeObjects](engine-serializeobjects.html)

[Engine.UnserializeObjects](engine-unserializeobjects.html)

[PropertyObject.Serialize](propertyobject-serialize.html)

[PropertyObject.UnserializeEx](propertyobject-unserializeex.html)

[PropertyObjectFile.TypeUsageList](propertyobjectfile-typeusagelist.html)

[Sequence.CreateNewUniqueStepIds](sequence-createnewuniquestepids.html)

[Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)

[TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[TypeUsageList](typeusagelist.html)

[TypeUsageList.Union](typeusagelist-union.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-usedialogforcheckout.html language=enus -->
## TOPIC 00980: Engine.UseDialogForCheckOut

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-usedialogforcheckout.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-usedialogforcheckout.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UseDialogForCheckOut Data Type Boolean Purpose This property is obsolete. Use the StationOptions.UseDialogForCheckOut property instead. Remarks Specifies if the sequence editor launches a dialog box to check out files from source code control. When this property is True , the sequence

### Engine.UseDialogForCheckOut

#### Syntax

[Engine](engine.html).UseDialogForCheckOut

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.UseDialogForCheckOut

#### Remarks

Specifies if the sequence editor launches a dialog box to check out files from source code control.

When this property is
 True
 , the sequence editor always launches a dialog box when you check out files from source code control. When this property is
 False
 , the sequence editor checks out the files without launching a dialog box.

#### See Also

[StationOptions.CheckOutFilesWhenEdited](stationoptions-checkoutfileswhenedited.html)

[StationOptions.PromptWhenAddingFilesToSC](stationoptions-promptwhenaddingfilestosc.html)

[StationOptions.UseDialogForCheckOut](stationoptions-usedialogforcheckout.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-uselocalizeddecimalpoint.html language=enus -->
## TOPIC 00981: Engine.UseLocalizedDecimalPoint

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-uselocalizeddecimalpoint.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-uselocalizeddecimalpoint.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UseLocalizedDecimalPoint Data Type Boolean Purpose This property is obsolete. Use the StationOptions.UseLocalizedDecimalPoint property instead. Remarks Specifies whether to use the operating system setting to determine the character used as a decimal point. When this property is True ,

### Engine.UseLocalizedDecimalPoint

#### Syntax

[Engine](engine.html).UseLocalizedDecimalPoint

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.UseLocalizedDecimalPoint

#### Remarks

Specifies whether to use the operating system setting to determine the character used as a decimal point.

When this property is
 True
 , TestStand uses the operating system setting to determine the character it uses as the localized decimal point. When this property is
 False
 , TestStand uses the period character to represent decimal points.

#### See Also

[StationOptions.GetLanguages](stationoptions-getlanguages.html)

[StationOptions.Language](stationoptions-language.html)

[StationOptions.RecognizeMBChars](stationoptions-recognizembchars.html)

[StationOptions.UseLocalizedDecimalPoint](stationoptions-uselocalizeddecimalpoint.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-userfilepath.html language=enus -->
## TOPIC 00982: Engine.UserFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-userfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-userfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UserFilePath Data Type String Purpose This property is obsolete. Use the StationOptions.UserFilePath property instead. Remarks Specifies the location of the current user manager file. Changes to this property do not take effect until you restart the TestStand Engine. See Also Engine.Cu

### Engine.UserFilePath

#### Syntax

[Engine](engine.html).UserFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.UserFilePath

#### Remarks

Specifies the location of the current user manager file.

Changes to this property do not take effect until you restart the TestStand Engine.

#### See Also

[Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)

[StationOptions.AutoLoginSystemUser](stationoptions-autologinsystemuser.html)

[StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)

[StationOptions.RequireUserLogin](stationoptions-requireuserlogin.html)

[StationOptions.UserFilePath](stationoptions-userfilepath.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-usernameexists.html language=enus -->
## TOPIC 00983: Engine.UserNameExists

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-usernameexists.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-usernameexists.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UserNameExists( loginName) Return Value Boolean Purpose Returns True if a user with a specific login name exists. Parameters loginName As String [In] Specifies the login name to find. See Also Engine.CurrentUser Engine.GetUser User UsersFile

### Engine.UserNameExists

#### Syntax

[Engine](engine.html).UserNameExists( loginName)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if a user with a specific login name exists.

#### Parameters

loginName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the login name to find.

#### See Also

[Engine.CurrentUser](engine-currentuser.html)

[Engine.GetUser](engine-getuser.html)

[User](user.html)

[UsersFile](usersfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-usersfile.html language=enus -->
## TOPIC 00984: Engine.UsersFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-usersfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-usersfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.UsersFile Data Type UsersFile Purpose Returns the PropertyObjectFile that contains the list of TestStand users and user groups. Remarks Sequence editors and user interfaces typically use this object to display users and user groups or to edit lists of users and user groups, their prope

### Engine.UsersFile

#### Syntax

[Engine](engine.html).UsersFile

#### Data Type

[UsersFile](usersfile.html)

#### Purpose

Returns the PropertyObjectFile that contains the list of TestStand users and user groups.

#### Remarks

Sequence editors and user interfaces typically use this object to display users and user groups or to edit lists of users and user groups, their properties and privileges, and save those lists to disk.

#### See Also

[Engine.ConfigFile](engine-configfile.html)

[Engine.CurrentUser](engine-currentuser.html)

[Engine.GetUser](engine-getuser.html)

[Engine.GetUserGroup](engine-getusergroup.html)

[Engine.GlobalsFile](engine-globalsfile.html)

[UsersFile](usersfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-utility.html language=enus -->
## TOPIC 00985: Engine.Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-utility.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.Utility Data Type Utility Purpose Returns a reference to the Utility object, which you can use to access utility functions. See Also Utility

### Engine.Utility

#### Syntax

[Engine](engine.html).Utility

#### Data Type

[Utility](utility.html)

#### Purpose

Returns a reference to the
 [Utility](utility.html)
 object, which you can use to access utility functions.

#### See Also

[Utility](utility.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-versionstring.html language=enus -->
## TOPIC 00986: Engine.VersionString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-versionstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-versionstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.VersionString Data Type String Purpose Returns the full version of the TestStand Engine as a string. Remarks Use this string for display purposes. Use the other version properties for conditional code. See Also Engine.BuildVersion Engine.MajorVersion Engine.MinorVersion Engine.PatchVer

### Engine.VersionString

#### Syntax

[Engine](engine.html).VersionString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the full version of the TestStand Engine as a string.

#### Remarks

Use this string for display purposes. Use the other version properties for conditional code.

#### See Also

[Engine.BuildVersion](engine-buildversion.html)

[Engine.MajorVersion](engine-majorversion.html)

[Engine.MinorVersion](engine-minorversion.html)

[Engine.PatchVersion](engine-patchversion.html)

[Engine.RevisionVersion](engine-revisionversion.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-watchexpressionsenabled.html language=enus -->
## TOPIC 00987: Engine.WatchExpressionsEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-watchexpressionsenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-watchexpressionsenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.WatchExpressionsEnabled Data Type Boolean The default return value is False . Applications that support watch expressions, such as the sequence editor, set this property to True . Purpose Specifies if the TestStand Engine evaluates watch expressions after each step executes in an execu

### Engine.WatchExpressionsEnabled

#### Syntax

[Engine](engine.html).WatchExpressionsEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

The default return value is
 False
 . Applications that support watch expressions, such as the sequence editor, set this property to
 True
 .

#### Purpose

Specifies if the TestStand Engine evaluates watch expressions after each step executes in an execution. Applications that support watch expressions, such as the sequence editor, set this property to
 True
 . This property is not persisted and defaults to
 False
 for each instance of the engine.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-writetoolmenutodisk.html language=enus -->
## TOPIC 00988: Engine.WriteToolMenuToDisk

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-writetoolmenutodisk.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-writetoolmenutodisk.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.WriteToolMenuToDisk( reserved = 0) Purpose Updates the Tools menu configuration file, <TestStand Application Data> \Cfg\ToolMenu.ini , with the latest changes. Remarks If you make changes to the contents of the current Tools menu using the TestStand API, those changes are not saved aut

### Engine.WriteToolMenuToDisk

#### Syntax

[Engine](engine.html).WriteToolMenuToDisk( reserved = 0)

#### Purpose

Updates the Tools menu configuration file,
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\ToolMenu.ini
 , with the latest changes.

#### Remarks

If you make changes to the contents of the current Tools menu using the TestStand API, those changes are not saved automatically to the Tools menu configuration file. Call this method to save those changes to disk. Otherwise, the configuration file is automatically saved when the engine shuts down.

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

[GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine.html language=enus -->
## TOPIC 00989: Engine

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Engine class to create and access objects of other classes, control executions, launch built-in dialog boxes, implement a Tools menu, find files and directories, and invoke various utilities. Create the Engine object directly using ActiveX. To access the Engine object from a step, use the Te

### Engine

Use the
 Engine
 class to create and access objects of other classes, control executions, launch built-in dialog boxes, implement a Tools menu, find files and directories, and invoke various utilities. Create the
 Engine
 object directly using ActiveX. To access the
 Engine
 object from a step, use the TestStand API to obtain the value of the
 Engine
 property from the
 SequenceContext
 class or pass the
 SequenceContext
 property
 RunState.Engine
 as an object parameter to the step.

The following examples show how to create the initial Engine object:

LabWindows/CVI

CAObjHandle engineObj = 0;
 TS_NewEngine(NULL, &engineObj);

Visual Basic

'Place the TestStand Engine ActiveX control on the main form.

Visual C/C++

#import "C:\TestStand\Bin\teapi.dll"
 TS::IEnginePtr engine;
 HRESULT hr = engine.CreateInstance(__uuidof(TS::Engine))
 ;

#### Properties

| ApplicationIsEditor |
| --- |
| ApplicationLicense (Read Only) |
| AppMainHwnd |
| BuildVersion (Read Only) |
| ComputerName (Read Only) |
| CurrentUser |
| CurrentWorkspaceFile |
| DefaultAdapter |
| DefaultAdapterIndex |
| DotNetCLRVersion (Read Only) |
| DotNetGarbageCollectionInterval |
| ExternalReportViewers (Read Only) |
| FileDialogDirHistoryList |
| Globals (Read Only) |
| GlobalsFile (Read Only) |
| Images (Read Only) |
| Is64Bit (Read Only) |
| IsRemote |
| IsUIMessageQueueEmpty (Read Only) |
| LargeImageListEx (Read Only) |
| LastWorkspacePath |
| LicenseType (Read Only) |
| MajorVersion (Read Only) |
| MasterEngine |
| MinorVersion (Read Only) |
| NumAdapters (Read Only) |
| NumImages (Read Only) |
| OutputMessagesEnabled |
| PatchVersion (Read Only) |
| PersistBreakpoints |
| PersistConfigFile |
| PersistWatchExpressions |
| ProfilerInputOutputCaptureMaximumTextLength |
| ProfilerOptions |
| ProfilerOutputMessageCategoryName (Read Only) |
| ProfilingEnabled (Read Only) |
| RevisionVersion (Read Only) |
| SearchDirectories (Read Only) |
| SecondsAtStartIn1970UniversalCoordinatedTime (Read Only) |
| SecondsSince1970UniversalCoordinatedTime (Read Only) |
| SecondsSinceStart (Read Only) |
| SmallImageListEx (Read Only) |
| StationOptions (Read Only) |
| TemporaryGlobals (Read Only) |
| UIMessagePollingEnabled |
| UndoLimit |
| UniqueEngineId (Read Only) |
| UsersFile (Read Only) |
| Utility (Read Only) |
| VersionString (Read Only) |
| WatchExpressionsEnabled |

#### Methods

| AbortAll |
| --- |
| AcquireLicense |
| AddImage |
| BeginProfiling |
| BreakAll |
| CallFrontEndCallbackEx |
| CanCreateStep |
| CheckExpression |
| CheckExprSyntax |
| ClearFilePasswordCache |
| CommitGlobalsToDisk |
| CopyPropertyObject |
| CreateNewUniqueStepIds |
| CreateTempFile |
| CurrentUserHasPrivilege |
| DelocalizeExpression |
| DisplayAdapterConfigDialog |
| DisplayBreakpointDialog |
| DisplayBrowseExprDialogEx |
| DisplayBrowsePropertyObjectDialog |
| DisplayConfigureTypePalettesDialog |
| DisplayEditBreakAndWatchDialog |
| DisplayEditPathsInFilesDialog |
| DisplayEditUserDialog |
| DisplayErrorDialog |
| DisplayExpressionEditOptionsDialog |
| DisplayExternalViewerDialog |
| DisplayFileDialog |
| DisplayHelpFile |
| DisplayHelpTopic |
| DisplayHelpTopicEx |
| DisplayIOConfigurationOptionsDialog |
| DisplayLockUnlockDialog |
| DisplayLoginDialog |
| DisplayLoopOnStepsDialog |
| DisplayMessageBox |
| DisplayNewUserDialog |
| DisplayOptionsDialog |
| DisplayPasswordProtectTypeDefinitionsDialog |
| DisplayPreconditionBuilderDialog |
| DisplayPreconditionDialog |
| DisplayRunTimeErrorDialogEx |
| DisplaySearchDirDialog |
| DisplaySeqFilePropDialog |
| DisplaySequenceFileCallbacksDialog |
| DisplaySequencePropDialog |
| DisplayStepPropDialog |
| DisplayStepTypeMenuEditorEx |
| DisplayToolMenuDialog |
| DisplayUnlockTypeDefinitionsDialog |
| DisplayWorkspaceBrowserDialog |
| DoDotNetGarbageCollection |
| EndProfiling |
| ExpandPathMacros |
| FindFileEx |
| FindPath |
| GetAdapter |
| GetAdapterByKeyName |
| GetEditTimeToolMenuItems |
| GetEngineConfigFile |
| GetEnvironmentPath |
| GetErrorString |
| GetFileInformation |
| GetImageIndex |
| GetImageName |
| GetInsertStepMenuStructure |
| GetInsertVariableMenuStructure |
| GetInternalOption |
| GetLicenseDescription |
| GetLocalizedDecimalPoint |
| GetLocationForNextDialog |
| GetModuleProfiling |
| GetProductRegistrationInfo |
| GetRelativePathFromAbsolutePath |
| GetResourceString |
| GetResourceSymbols |
| GetRunTimeToolMenuItems |
| GetSequenceFileEx |
| GetStationModelSequenceFile |
| GetSyncManager |
| GetTemplatesFile |
| GetTestStandPath |
| GetTypeDefinition |
| GetTypeNames |
| GetTypePaletteFileList |
| GetTypes |
| GetTypeUsageLocations |
| GetUIMessage |
| GetUser |
| GetUserGroup |
| GetWatchExpressions |
| GetWatchExpressionsChangeCount |
| HasAddonLicense |
| IsCurrentSequenceFileVersion |
| LaunchExternalViewer |
| LoadTypePaletteFilesEx |
| LocalizeExpression |
| LogProfilerAction |
| NewCsvFileInputRecordStream |
| NewCsvFileOutputRecordStream |
| NewDataType |
| NewEditArgs |
| NewEditContext |
| NewEvaluationTypes |
| NewExecution |
| NewExpression |
| NewHierarchicalExecution |
| NewInteractiveArgs |
| NewLocations |
| NewOutputMessage |
| NewOutputMessages |
| NewPropertyObject |
| NewPropertyObjectFile |
| NewPropertyObjectType |
| NewResultLog |
| NewResultLogger |
| NewSequence |
| NewSequenceFile |
| NewStep |
| NewStepType |
| NewTypeUsageList |
| NewUndoItemCreator |
| NewUndoStack |
| NewUser |
| NewWorkspaceFile |
| NotifyEndOfModalDialog |
| NotifyStartOfModalDialogEx |
| OpenWorkspaceFile |
| ParseLookupString |
| PostUIMessage |
| ReadPropertyObjectFile |
| RegisterModalWindow |
| RegisterSequenceToExecuteOnCrash |
| RegisterUIMessage |
| RegisterUIMessageCallbackEx |
| ReleaseLicense |
| ReleaseSequenceFileEx |
| ReloadGlobals |
| ReloadStringResourceFiles |
| ResetTypeInstances |
| SaveAllModifiedSeqFiles |
| SearchFiles |
| SerializeObjects |
| SetConfigDirectory |
| SetInternalOption |
| SetLocationForNextDialog |
| SetModuleProfiling |
| SetTypePaletteFileList |
| ShouldAutoLaunchExternalReportViewer |
| ShutDown |
| TerminateAll |
| UnloadAllModules |
| UnloadTypePaletteFiles |
| UnregisterModalWindow |
| UnregisterSequenceToExecuteOnCrash |
| UnserializeObjects |
| UnserializeObjectsAndTypes |
| UserNameExists |
| WriteToolMenuToDisk |

#### Event

| UIMessageEvent |
| --- |

#### See Also

[SequenceContext.Engine](sequencecontext-engine.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineenvironment-environmentpath.html language=enus -->
## TOPIC 00990: EngineEnvironment.EnvironmentPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineenvironment-environmentpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineenvironment-environmentpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineEnvironment.EnvironmentPath Data Type String

### EngineEnvironment.EnvironmentPath

#### Syntax

[EngineEnvironment](engineenvironment.html).EnvironmentPath

#### Data Type

[String](data-types-for-teststand.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineenvironment-getteststandpath.html language=enus -->
## TOPIC 00991: EngineEnvironment.GetTestStandPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineenvironment-getteststandpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineenvironment-getteststandpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineEnvironment.GetTestStandPath( testStandPath, resolveAbsolutePath = True) Return Value String Parameters testStandPath As TestStandPaths [In] resolveAbsolutePath As Boolean [In]

### EngineEnvironment.GetTestStandPath

#### Syntax

[EngineEnvironment](engineenvironment.html).GetTestStandPath( testStandPath, resolveAbsolutePath = True)

#### Return Value

[String](data-types-for-teststand.html)

#### Parameters

testStandPath
 As
 [TestStandPaths](teststandpaths.html)

[In]

resolveAbsolutePath
 As
 [Boolean](data-types-for-teststand.html)

[In]

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineenvironment-readfile.html language=enus -->
## TOPIC 00992: EngineEnvironment.ReadFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineenvironment-readfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineenvironment-readfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineEnvironment.ReadFile(path) Parameters path As String [In]

### EngineEnvironment.ReadFile

#### Syntax

[EngineEnvironment](engineenvironment.html).ReadFile(path)

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In]

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineenvironment-setteststandpath.html language=enus -->
## TOPIC 00993: EngineEnvironment.SetTestStandPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineenvironment-setteststandpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineenvironment-setteststandpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineEnvironment.SetTestStandPath( testStandPath, path) Parameters testStandPath As TestStandPaths [In] path As String [In]

### EngineEnvironment.SetTestStandPath

#### Syntax

[EngineEnvironment](engineenvironment.html).SetTestStandPath( testStandPath, path)

#### Parameters

testStandPath
 As
 [TestStandPaths](teststandpaths.html)

[In]

path
 As
 [String](data-types-for-teststand.html)

[In]

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineenvironment-writefile.html language=enus -->
## TOPIC 00994: EngineEnvironment.WriteFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineenvironment-writefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineenvironment-writefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineEnvironment.WriteFile

### EngineEnvironment.WriteFile

#### Syntax

[EngineEnvironment](engineenvironment.html).WriteFile

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineenvironment.html language=enus -->
## TOPIC 00995: EngineEnvironment

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineenvironment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineenvironment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Property EnvironmentPath Methods GetTestStandPath ReadFile SetTestStandPath WriteFile

### EngineEnvironment

#### Property

| EnvironmentPath |
| --- |

#### Methods

| GetTestStandPath |
| --- |
| ReadFile |
| SetTestStandPath |
| WriteFile |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineinitializationsettings-caninitializeeng.html language=enus -->
## TOPIC 00996: EngineInitializationSettings.CanInitializeEngine

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineinitializationsettings-caninitializeeng.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineinitializationsettings-caninitializeeng.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineInitializationSettings.CanInitializeEngine Return Value Boolean

### EngineInitializationSettings.CanInitializeEngine

#### Syntax

[EngineInitializationSettings](engineinitializationsettings.html).CanInitializeEngine

#### Return Value

[Boolean](data-types-for-teststand.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineinitializationsettings-setenvironmentpa.html language=enus -->
## TOPIC 00997: EngineInitializationSettings.SetEnvironmentPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineinitializationsettings-setenvironmentpa.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineinitializationsettings-setenvironmentpa.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineInitializationSettings.SetEnvironmentPath( path) Parameters path As String [In]

### EngineInitializationSettings.SetEnvironmentPath

#### Syntax

[EngineInitializationSettings](engineinitializationsettings.html).SetEnvironmentPath( path)

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In]

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineinitializationsettings-setinternalstart.html language=enus -->
## TOPIC 00998: EngineInitializationSettings.SetInternalStartupOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineinitializationsettings-setinternalstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineinitializationsettings-setinternalstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineInitializationSettings.SetInternalStartupOption( option, newValue) Purpose Specifies the value for the internal startup option the option parameter specifies. Parameters option As InternalStartupOptions [In] Specifies the internal startup option the method sets. newValue As Variant [In]

### EngineInitializationSettings.SetInternalStartupOption

#### Syntax

[EngineInitializationSettings](engineinitializationsettings.html).SetInternalStartupOption( option, newValue)

#### Purpose

Specifies the value for the internal startup option the option parameter specifies.

#### Parameters

option
 As
 [InternalStartupOptions](internalstartupoptions.html)

[In] Specifies the internal startup option the method sets.

newValue
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the value of the internal startup option the option parameter specifies.

#### See Also

[Engine.SetInternalOption](engine-setinternaloption.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineinitializationsettings.html language=enus -->
## TOPIC 00999: EngineInitializationSettings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineinitializationsettings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineinitializationsettings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the EngineInitializationSettings class to configure options that must be set prior to Engine construction. Methods CanInitializeEngine SetEnvironmentPath SetInternalStartupOption

### EngineInitializationSettings

Use the EngineInitializationSettings class to configure options that must be set prior to Engine construction.

#### Methods

| CanInitializeEngine |
| --- |
| SetEnvironmentPath |
| SetInternalStartupOption |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineinitializer-cansetenvironmentpath.html language=enus -->
## TOPIC 01000: EngineInitializer.CanSetEnvironmentPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineinitializer-cansetenvironmentpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineinitializer-cansetenvironmentpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineInitializer.CanSetEnvironmentPath Return Value Boolean Returns True if it is still possible to initialize the TestStand engine, False otherwise. Purpose Check whether it is possible to initialize the TestStand Engine. Remarks It is not possible to initialize the TestStand engine after i

### EngineInitializer.CanSetEnvironmentPath

#### Syntax

[EngineInitializer](engineinitializer.html).CanSetEnvironmentPath

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if it is still possible to initialize the TestStand engine,
 False
 otherwise.

#### Purpose

Check whether it is possible to initialize the TestStand Engine.

#### Remarks

It is not possible to initialize the TestStand engine after it has been constructed.

Parent topic:

Methods
